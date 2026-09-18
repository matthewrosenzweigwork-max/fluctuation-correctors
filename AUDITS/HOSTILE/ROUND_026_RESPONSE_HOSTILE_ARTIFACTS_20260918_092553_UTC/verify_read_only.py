#!/usr/bin/env python3
"""Portable AUD072 verifier. It reads bytes and never extracts or writes files.

Place the packet, .tar.gz, .INVENTORY.json, .CORE_VERIFICATION.json,
.SHA256SUMS and ROUND_026_RESPONSE_REVIEW.md in the same parent directory.
No source checkout, repository metadata, third-party library, or network needed.
"""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import stat
import sys
import tarfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def demand(condition, message):
    if not condition:
        raise ValueError(message)


def safe_relative(name):
    demand(isinstance(name,str) and name!='', 'empty/nonstring path')
    demand(not name.startswith('/') and '\\' not in name,
           'absolute or backslash path: '+name)
    parts=name.split('/')
    demand(all(p not in ('','.','..') for p in parts),'unsafe path component: '+name)
    demand(all(ord(c)>=32 and ord(c)!=127 for c in name),'control byte in path')
    demand(str(PurePosixPath(name))==name,'nonnormal path: '+name)
    return name


def match_bytes(data, expected, label):
    actual=digest(data)
    demand(actual==expected,'digest mismatch: {}: {} != {}'.format(label,actual,expected))


def member_set(expected, actual, label):
    demand(set(expected)==set(actual),
           '{} member mismatch: missing={} extra={}'.format(
               label,sorted(set(expected)-set(actual)),sorted(set(actual)-set(expected))))


def safe_tar_member(member, prefix):
    safe_relative(member.name)
    demand(member.name.startswith(prefix+'/'),'wrong archive prefix: '+member.name)
    demand(member.isreg(),'archive member is not a regular file: '+member.name)
    demand(not member.issym() and not member.islnk(),'archive link: '+member.name)
    demand(member.mode==0o444,'archive mode is not read-only: '+member.name)


def read_regular(path):
    info=path.lstat()
    demand(stat.S_ISREG(info.st_mode),'not regular: '+str(path))
    demand(stat.S_IMODE(info.st_mode)==0o444,'not mode 0444: '+str(path))
    return path.read_bytes()


def read_checksums(data):
    out={}
    for line in data.decode('utf-8').splitlines():
        pair=line.split('  ',1)
        demand(len(pair)==2,'invalid checksum row')
        value,name=pair
        safe_relative(name)
        demand(len(value)==64 and all(c in '0123456789abcdef' for c in value),
               'invalid SHA-256: '+name)
        demand(name not in out,'duplicate checksum row: '+name)
        out[name]=value
    return out


def verify(packet,skip_seal=False):
    packet=packet.absolute()
    demand(packet.is_dir() and not packet.is_symlink(),'packet is not a regular directory')
    if not skip_seal:
        demand(stat.S_IMODE(packet.lstat().st_mode)==0o555,'packet directory is not mode 0555')
    parent=packet.parent
    prefix=packet.name
    archive=parent/(prefix+'.tar.gz')
    inventory_path=parent/(prefix+'.INVENTORY.json')
    verification_path=parent/(prefix+'.CORE_VERIFICATION.json')
    seal=parent/(prefix+'.SHA256SUMS')
    external_report=parent/'ROUND_026_RESPONSE_REVIEW.md'
    inventory=json.loads(read_regular(inventory_path))
    demand(inventory['format']=='AUD072-portable-regular-inventory-v1','wrong inventory format')
    demand(inventory['packet_name']==prefix,'inventory packet-name mismatch')
    entries=inventory['files']
    expected={}
    for row in entries:
        rel=safe_relative(row['path'])
        demand(rel not in expected,'duplicate inventory entry: '+rel)
        demand(row['mode']=='0444','inventory file mode mismatch: '+rel)
        expected[rel]=row
    actual=[]
    directories=[]
    for base,subdirs,files in os.walk(str(packet),followlinks=False):
        base=Path(base)
        for name in subdirs:
            child=base/name
            demand(stat.S_ISDIR(child.lstat().st_mode),'nonregular directory: '+str(child))
            if not skip_seal:
                demand(stat.S_IMODE(child.lstat().st_mode)==0o555,
                       'payload directory is not mode 0555: '+str(child))
            directories.append(child.relative_to(packet).as_posix())
        for name in files:
            path=base/name
            rel=path.relative_to(packet).as_posix()
            safe_relative(rel)
            demand(stat.S_ISREG(path.lstat().st_mode),'nonregular payload: '+rel)
            actual.append(rel)
    member_set(expected,actual,'directory')
    member_set(inventory['directories'],directories,'directory tree')
    for rel,row in expected.items():
        data=read_regular(packet/rel)
        demand(len(data)==row['bytes'],'byte-size mismatch: '+rel)
        match_bytes(data,row['sha256'],rel)

    sources=read_checksums(read_regular(packet/'INPUT_SHA256SUMS.txt'))
    demand(len(sources)==13,'expected exactly thirteen input hashes')
    actual_sources={p[len('INPUTS/'):] for p in actual if p.startswith('INPUTS/')}
    member_set(sources,actual_sources,'copied sources')
    for rel,sha in sources.items():
        match_bytes(read_regular(packet/'INPUTS'/rel),sha,'input '+rel)

    seen={}
    archive_bytes=read_regular(archive)
    with tarfile.open(fileobj=io.BytesIO(archive_bytes),mode='r:gz') as handle:
        for member in handle:
            safe_tar_member(member,prefix)
            rel=member.name[len(prefix)+1:]
            demand(rel not in seen,'duplicate archive member: '+rel)
            demand(rel in expected,'unexpected archive member: '+rel)
            data=handle.extractfile(member).read()
            row=expected[rel]
            demand(member.size==row['bytes']==len(data),'archive size mismatch: '+rel)
            match_bytes(data,row['sha256'],'archive '+rel)
            demand(data==read_regular(packet/rel),'archive/directory byte mismatch: '+rel)
            seen[rel]=True
    member_set(expected,seen,'archive')
    report_bytes=read_regular(external_report)
    demand(report_bytes==read_regular(packet/'REPORT.md'),'external report differs from packet report')

    if not skip_seal:
        sealed=read_checksums(read_regular(seal))
        required={prefix+'/'+rel for rel in expected}
        required.update((archive.name,inventory_path.name,verification_path.name,external_report.name))
        member_set(required,sealed,'sibling seal')
        for rel,sha in sealed.items():
            match_bytes(read_regular(parent/rel),sha,'sealed '+rel)
        core=json.loads(read_regular(verification_path))
        demand(core['status']=='PASS','core verification record is not PASS')
    return {'status':'PASS','packet_name':prefix,'payload_regular_files':len(expected),
            'archive_regular_members':len(seen),'input_hashes':len(sources),
            'exact_directory_inventory':True,'safe_regular_archive':True,
            'archive_directory_equality':True,'external_report_equality':True,
            'read_only_file_modes':True,'sibling_seal_checked':not skip_seal,
            'writes':0,'extractions':0}


def mutation(which):
    # Deliberately invalid in-memory evidence, sent through the same guards.
    # Nothing is extracted or written, including path traversal controls.
    if which=='digest_corruption':
        match_bytes(b'changed payload',digest(b'original payload'),'deliberate corruption')
    elif which=='unsafe_archive_path':
        member=tarfile.TarInfo('../escape')
        member.mode=0o444
        safe_tar_member(member,'packet')
    elif which=='archive_symlink':
        member=tarfile.TarInfo('packet/link')
        member.type=tarfile.SYMTYPE
        member.linkname='/outside'
        member.mode=0o444
        safe_tar_member(member,'packet')
    elif which=='extra_inventory_member':
        member_set({'allowed'},{'allowed','unlisted'},'deliberate inventory corruption')
    else:
        raise ValueError('unknown control')
    raise RuntimeError('mutation unexpectedly accepted')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet',type=Path,default=Path(__file__).parent)
    parser.add_argument('--skip-seal',action='store_true',help='issuance-only core verification')
    parser.add_argument('--control',choices=('digest_corruption','unsafe_archive_path',
                                           'archive_symlink','extra_inventory_member'))
    args=parser.parse_args()
    try:
        if args.control:
            mutation(args.control)
        result=verify(args.packet,args.skip_seal)
    except Exception as error:
        print(json.dumps({'status':'FAIL','control':args.control,
                          'error':str(error),'writes':0,'extractions':0},indent=2))
        return 1
    print(json.dumps(result,indent=2))
    return 0


if __name__=='__main__':
    sys.exit(main())
