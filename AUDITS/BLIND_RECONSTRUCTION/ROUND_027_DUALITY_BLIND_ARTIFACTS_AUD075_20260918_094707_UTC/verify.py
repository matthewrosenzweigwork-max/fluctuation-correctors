#!/usr/bin/env python3
"""Portable AUD075 verifier. Read-only. Standard library. No archive extraction."""
import argparse,hashlib,io,json,os,stat,subprocess,sys,tarfile
from pathlib import Path,PurePosixPath

SOURCE_SHA256={
 'AGENTS.md':'cc3a478358f1fcb3ccf472615c715acfdef575d9a80b5aa49417593a25825ed3',
 'MODEL_ORCHESTRATION.md':'e49ee3901ea41494b36f251d16a72f1d06d6405a842cc09d889a2c87c1ef83e1',
 'TASKS/ACTIVE/ROUND_001_MODEL.md':'3fdad096402a18f0c42f9661cfec48897d9dd5c917dc21f209a0aa3494aadf57',
 'TASKS/ACTIVE/TASK-117_ROUND027_DUALITY_BLIND.md':'9425649c574b9fafd04406057aed668259d8c53faf02b427d404aa413e80d433',
 'THEOREMS/THM-052_KILLED_ATTRACTIVE_COULOMB_DUALITY.md':'b40019d72424818df99ffd4193dd65402d22d8fb133e871d0d0ad4cd389b1309',
 'MEMORANDA/ROUND_001_ALGEBRA.md':'e5db5923ba82bf929218e23fe641ed5a7387c106220e6374f37bd06b80c3e4de',
 'MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md':'135b726c4dd4a69bc8206ea81671c2c949b454d4b80e98002af6378a7d6f34be',
 'MEMORANDA/ROUND_006_SINGULAR_PARTICLE_REALIZATION.md':'d4d1eae9f18d5796e8e99aa4b5e364b39321167f48eb27fa764bc7e327272017'}
MUTANTS=('pair_half','atom_deleted','noise_half','reverse_noise_sign','endpoint_orientation','drop_conditioning','endpoint_only_kill','fourier_response_sign','path_order')
SELF_SEALS={'PAYLOAD_INVENTORY.json','PAYLOAD_SHA256SUMS.txt'}

class VerificationError(Exception): pass

def require(ok,message):
    if not ok: raise VerificationError(message)

def sha(data): return hashlib.sha256(data).hexdigest()

def safe_name(name):
    require(isinstance(name,str) and name!='' and '\\' not in name and '\x00' not in name,'unsafe member name')
    p=PurePosixPath(name)
    require(not p.is_absolute() and all(s not in ('','.', '..') for s in name.split('/')),'unsafe member name: '+name)
    require(str(p)==name,'noncanonical member name: '+name)
    return name

def collect_files(root,readonly=True):
    result={}
    require(root.is_dir() and not root.is_symlink(),'packet must be a real directory')
    require(not readonly or not(root.stat().st_mode & 0o222),'writable packet directory')
    def walk(folder):
        for entry in os.scandir(folder):
            p=Path(entry.path); rel=safe_name(p.relative_to(root).as_posix()); st=entry.stat(follow_symlinks=False)
            require(not stat.S_ISLNK(st.st_mode),'symlink forbidden: '+rel)
            require(not readonly or not(st.st_mode & 0o222),'writable member: '+rel)
            if stat.S_ISDIR(st.st_mode): walk(p)
            else:
                require(stat.S_ISREG(st.st_mode),'nonregular member: '+rel)
                result[rel]=p.read_bytes()
    walk(root)
    return result

def inventory_map(document):
    require(document.get('schema')=='AUD075-inventory-v1','wrong inventory schema')
    rows=document.get('files'); require(isinstance(rows,list),'missing inventory files')
    out={}
    for row in rows:
        name=safe_name(row['path']); require(name not in out,'duplicate inventory entry: '+name)
        require(isinstance(row['bytes'],int) and row['bytes']>=0,'invalid byte count')
        digest=row['sha256']; require(isinstance(digest,str) and len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'invalid digest')
        out[name]=row
    return out

def check_bytes(actual,expected):
    require(set(actual)==set(expected),'inventory names differ; missing='+str(sorted(set(expected)-set(actual)))+' extra='+str(sorted(set(actual)-set(expected))))
    for name,data in actual.items():
        row=expected[name]
        require(len(data)==row['bytes'],'byte count mismatch: '+name)
        require(sha(data)==row['sha256'],'SHA-256 mismatch: '+name)

def check_tar(data,packet_name,expected):
    seen={}
    with tarfile.open(fileobj=io.BytesIO(data),mode='r:*') as archive:
        for member in archive:
            name=safe_name(member.name)
            require(member.isreg() and not member.issym() and not member.islnk() and not member.sparse,'archive member is not an ordinary regular file: '+name)
            require(name.startswith(packet_name+'/'),'wrong archive root: '+name)
            rel=safe_name(name[len(packet_name)+1:]); require(rel not in seen,'duplicate archive member: '+rel)
            require((member.mode & 0o222)==0,'writable archived file: '+rel)
            require(rel in expected,'extra archive member: '+rel)
            require(member.size==expected[rel]['bytes'],'archive size mismatch: '+rel)
            stream=archive.extractfile(member); require(stream is not None,'missing archive stream')
            seen[rel]=stream.read()
    check_bytes(seen,expected)
    return len(seen)

def synthetic_guard(name):
    expected={'a.txt':{'path':'a.txt','bytes':3,'sha256':sha(b'abc')}}
    if name=='changed_payload': check_bytes({'a.txt':b'abd'},expected)
    elif name=='missing_payload': check_bytes({},expected)
    elif name=='extra_payload': check_bytes({'a.txt':b'abc','extra':b'x'},expected)
    elif name=='unsafe_path': safe_name('../escape')
    elif name in ('archive_link','archive_duplicate','archive_unsafe','archive_changed','archive_missing'):
        buff=io.BytesIO()
        with tarfile.open(fileobj=buff,mode='w') as tar:
            if name!='archive_missing':
                t=tarfile.TarInfo('../escape' if name=='archive_unsafe' else 'packet/a.txt'); t.mode=0o444
                if name=='archive_link': t.type=tarfile.SYMTYPE; t.linkname='../escape'; tar.addfile(t)
                else:
                    blob=b'abd' if name=='archive_changed' else b'abc'; t.size=3; tar.addfile(t,io.BytesIO(blob))
                    if name=='archive_duplicate': tar.addfile(t,io.BytesIO(blob))
        check_tar(buff.getvalue(),'packet',expected)
    else: raise VerificationError('unknown guard mutation')
    raise RuntimeError('guard mutation was not rejected')

def verify(packet,payload_only,run_diagnostics):
    actual=collect_files(packet)
    require(SELF_SEALS.issubset(actual),'missing payload sealing files')
    inv=json.loads(actual['PAYLOAD_INVENTORY.json']); expected=inventory_map(inv)
    require(set(inv['excluded_self_seals'])==SELF_SEALS,'incorrect inventory self-seal exclusions')
    check_bytes({k:v for k,v in actual.items() if k not in SELF_SEALS},expected)
    checksums=''.join(expected[name]['sha256']+'  '+name+'\n' for name in sorted(expected)).encode()
    require(actual['PAYLOAD_SHA256SUMS.txt']==checksums,'payload checksum manifest differs')
    frozen=[]
    for name,digest in SOURCE_SHA256.items():
        require(sha(actual['INPUTS/'+name])==digest,'frozen source mismatch: '+name)
        frozen.append(digest+'  '+name)
    require(actual['FROZEN_INPUT_SHA256SUMS.txt']==('\n'.join(frozen)+'\n').encode(),'frozen manifest bytes differ')
    report='ROUND_027_DUALITY_RECONSTRUCTION.md'
    require(report in actual,'report missing')
    baseline=json.loads(actual['diagnostic_baseline.json'])
    require(baseline['status']=='PASS' and baseline['checks']==322 and baseline['failed_count']==0,'recorded baseline failed')
    ms=json.loads(actual['mutation_summary.json'])
    require({x['mutant'] for x in ms}==set(MUTANTS),'mutation summary coverage mismatch')
    for row in ms:
        require(row['returncode']==1 and row['detected'] and row['failed_count']>0,'undetected semantic mutant')
    result={'status':'PASS_PAYLOAD_ONLY' if payload_only else 'PASS','packet':packet.name,'regular_packet_members':len(actual),'frozen_inputs':len(SOURCE_SHA256),'baseline_checks':322,'semantic_mutants_detected':len(ms),'read_only':True,'archive_extracted':False}
    if not payload_only:
        parent=packet.parent
        for sibling in (packet.name+'_INVENTORY.json',packet.name+'.tar.gz',packet.name+'_SHA256SUMS.txt',packet.name+'_SEAL.json',report):
            st=(parent/sibling).lstat()
            require(stat.S_ISREG(st.st_mode) and not(st.st_mode & 0o222),'sibling must be read-only regular file: '+sibling)
        fullpath=parent/(packet.name+'_INVENTORY.json'); full=inventory_map(json.loads(fullpath.read_bytes()))
        check_bytes(actual,full)
        archive=parent/(packet.name+'.tar.gz'); result['archive_regular_members']=check_tar(archive.read_bytes(),packet.name,full)
        require((parent/report).read_bytes()==actual[report],'assigned report and packet report differ')
        sums=parent/(packet.name+'_SHA256SUMS.txt')
        needed={packet.name+'/'+name:data for name,data in actual.items()}
        needed.update({fullpath.name:fullpath.read_bytes(),archive.name:archive.read_bytes(),report:actual[report]})
        expected_sums=''.join(sha(needed[name])+'  '+name+'\n' for name in sorted(needed)).encode()
        require(sums.read_bytes()==expected_sums,'complete sibling checksum manifest differs')
        seal=json.loads((parent/(packet.name+'_SEAL.json')).read_bytes())
        require(seal['packet']==packet.name and seal['schema']=='AUD075-seal-v1','incorrect outer seal')
        for name,digest in seal['sibling_sha256'].items():
            safe_name(name); require('/' not in name,'seal entry must be a sibling basename')
            require(sha((parent/name).read_bytes())==digest,'sibling seal mismatch: '+name)
        require(set(seal['sibling_sha256'])=={fullpath.name,archive.name,sums.name,report},'incomplete sibling seal')
        result['archive_sha256']=sha(archive.read_bytes()); result['report_sha256']=sha(actual[report])
    if run_diagnostics:
        runs=[]
        for mutant in ('baseline',)+MUTANTS:
            args=[sys.executable,'-B',str(packet/'diagnostics.py')]
            if mutant!='baseline': args+=['--mutant',mutant]
            env=dict(os.environ); env['PYTHONDONTWRITEBYTECODE']='1'
            p=subprocess.run(args,capture_output=True,env=env,check=False)
            wanted=0 if mutant=='baseline' else 1
            require(p.returncode==wanted,'fresh diagnostic return code differs: '+mutant)
            saved='diagnostic_baseline.json' if mutant=='baseline' else 'mutation_'+mutant+'.json'
            require(p.stdout==actual[saved],'fresh diagnostic output differs: '+mutant)
            require(p.stderr==b'','fresh diagnostic stderr: '+mutant)
            runs.append({'mutant':mutant,'returncode':p.returncode})
        result['fresh_read_only_runs']=runs
    return result

def main():
    p=argparse.ArgumentParser(); p.add_argument('--packet',type=Path,default=Path(__file__).resolve().parent); p.add_argument('--payload-only',action='store_true'); p.add_argument('--run-diagnostics',action='store_true'); p.add_argument('--guard-mutant'); a=p.parse_args()
    try:
        if a.guard_mutant: synthetic_guard(a.guard_mutant)
        result=verify(a.packet.resolve(),a.payload_only,a.run_diagnostics)
        print(json.dumps(result,indent=2)); return 0
    except (VerificationError,OSError,ValueError,KeyError,tarfile.TarError) as e:
        print(json.dumps({'status':'FAIL','guard_mutant':a.guard_mutant,'reason':str(e)},indent=2)); return 1

if __name__=='__main__': sys.exit(main())
