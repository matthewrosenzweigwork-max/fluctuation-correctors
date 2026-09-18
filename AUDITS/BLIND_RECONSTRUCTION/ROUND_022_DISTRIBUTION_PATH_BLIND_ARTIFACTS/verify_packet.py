#!/usr/bin/env python3
"""AUD063 safe byte verifier. It never extracts archive members."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import io
import json
import stat
import tarfile

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def safe(name):
    p = PurePosixPath(name)
    return bool(name) and name not in (".", "..") and not p.is_absolute() and str(p) == name and \
        all(x not in ("", ".", "..") for x in p.parts) and \
        "\\" not in name and "\x00" not in name

def read_manifest(path):
    result = {}
    for line in path.read_text().splitlines():
        h, name = line.split("  ", 1)
        assert len(h) == 64 and all(c in "0123456789abcdef" for c in h)
        assert safe(name), ("unsafe manifest path", name)
        assert name not in result, ("duplicate manifest path", name)
        result[name] = h
    return result

def check_tar(source, expected, disk):
    with tarfile.open(fileobj=source, mode="r:*") as archive:
        members = archive.getmembers()
        names = [m.name for m in members]
        assert len(names) == len(set(names)), "duplicate archive members"
        assert set(names) == set(expected), "archive membership mismatch"
        size = 0
        for m in members:
            assert safe(m.name), ("unsafe archive path", m.name)
            assert m.isfile() and not m.issym() and not m.islnk(), ("nonregular member", m.name)
            assert not m.pax_headers, ("unexpected extended header", m.name)
            assert m.mode == 0o444, ("unsealed member mode", m.name)
            wanted = disk[m.name]
            assert m.size == len(wanted), ("member size mismatch", m.name)
            stream = archive.extractfile(m)
            assert stream is not None
            with stream:
                raw = stream.read(len(wanted)+1)
            assert raw == wanted and digest(raw) == expected[m.name], ("member bytes mismatch", m.name)
            size += len(raw)
    return len(names), size

def verifier_controls():
    """Deliberately hostile in-memory archives; no file is extracted or written."""
    def make(rows):
        memory = io.BytesIO()
        with tarfile.open(fileobj=memory, mode="w", format=tarfile.USTAR_FORMAT) as archive:
            for name, raw, kind in rows:
                info = tarfile.TarInfo(name)
                info.mode = 0o444
                info.type = kind
                if kind == tarfile.SYMTYPE:
                    info.linkname = "../escape"
                    info.size = 0
                    archive.addfile(info)
                else:
                    info.size = len(raw)
                    archive.addfile(info, io.BytesIO(raw))
        memory.seek(0)
        return memory
    wanted = {"packet/a": b"alpha", "packet/b": b"beta"}
    expected = {k: digest(v) for k, v in wanted.items()}
    good = [(k, v, tarfile.REGTYPE) for k, v in wanted.items()]
    check_tar(make(good), expected, wanted)
    attacks = {
        "duplicate": good+[good[0]],
        "missing": good[:1],
        "extra": good+[("packet/c", b"gamma", tarfile.REGTYPE)],
        "wrong_byte": [("packet/a", b"alphx", tarfile.REGTYPE), good[1]],
        "symlink": [("packet/a", b"", tarfile.SYMTYPE), good[1]],
        "traversal": [("../a", b"alpha", tarfile.REGTYPE), good[1]],
        "absolute": [("/packet/a", b"alpha", tarfile.REGTYPE), good[1]],
    }
    outcomes = {}
    for key, rows in attacks.items():
        try:
            check_tar(make(rows), expected, wanted)
        except AssertionError:
            outcomes[key] = "REJECTED"
        else:
            raise AssertionError(("verifier accepted mutation", key))
    for name in (".", "..", "../a", "/a", "a//b", "a/./b", "a/../b", "a\\b", "", "a\x00b"):
        assert not safe(name), ("unsafe name accepted", name)
    return outcomes

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-readonly", action="store_true")
    parser.add_argument("--write-result", type=Path)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    parent = packet.parent
    stem = packet.name
    report = parent/"ROUND_022_DISTRIBUTION_PATH_RECONSTRUCTION.md"
    archive_path = parent/(stem+".tar.gz")
    member_manifest = parent/(stem+"_ARCHIVE_MEMBER_SHA256SUMS.txt")
    seal_path = parent/(stem+"_SEAL.json")
    assert packet.is_dir() and not packet.is_symlink()
    all_paths = list(packet.rglob("*"))
    assert all(not p.is_symlink() for p in all_paths), "packet contains a symlink"
    assert all(p.is_file() or p.is_dir() for p in all_paths), "packet contains a special file"
    files = {p.relative_to(packet).as_posix(): p for p in all_paths if p.is_file()}
    content = read_manifest(packet/"CONTENT_SHA256SUMS.txt")
    assert set(content) == set(files)-{"CONTENT_SHA256SUMS.txt"}, "content manifest coverage"
    for name, h in content.items():
        assert digest(files[name].read_bytes()) == h, ("content digest", name)
    inputs = read_manifest(packet/"INPUT_SHA256SUMS.txt")
    assert len(inputs) == 16, "wrong input count"
    assert {x[7:] for x in files if x.startswith("INPUTS/")} == set(inputs), "input-copy coverage"
    for name, h in inputs.items():
        assert digest((packet/"INPUTS"/name).read_bytes()) == h, ("input digest", name)
    outputs = read_manifest(packet/"OUTPUT_SHA256SUMS.txt")
    authored = set(files)-{x for x in files if x.startswith("INPUTS/")}-{
        "OUTPUT_SHA256SUMS.txt", "CONTENT_SHA256SUMS.txt"}
    assert set(outputs) == authored, "output manifest coverage"
    for name, h in outputs.items():
        assert digest((packet/name).read_bytes()) == h, ("output digest", name)
    assert report.read_bytes() == (packet/"RECONSTRUCTION.md").read_bytes(), "report copy mismatch"
    diagnostic = json.loads((packet/"DIAGNOSTIC_RESULTS.json").read_text())
    assert diagnostic["status"] == "PASS"
    assert diagnostic["program_sha256"] == digest((packet/"round022_blind_diagnostic.py").read_bytes())
    assert all(v["status"] == "REJECTED" for v in diagnostic["mutations"].values())
    assert diagnostic["assertions"] == sum(diagnostic["categories"].values())
    expected = read_manifest(member_manifest)
    disk = {stem+"/"+name: p.read_bytes() for name, p in files.items()}
    assert set(expected) == set(disk), "archive manifest coverage"
    for name, raw in disk.items():
        assert digest(raw) == expected[name], ("archive manifest digest", name)
    with archive_path.open("rb") as source:
        count, size = check_tar(source, expected, disk)
    controls = verifier_controls()
    seal = json.loads(seal_path.read_text())
    seal_checks = {
        "archive_sha256": digest(archive_path.read_bytes()),
        "archive_member_manifest_sha256": digest(member_manifest.read_bytes()),
        "content_manifest_sha256": digest((packet/"CONTENT_SHA256SUMS.txt").read_bytes()),
        "output_manifest_sha256": digest((packet/"OUTPUT_SHA256SUMS.txt").read_bytes()),
        "input_manifest_sha256": digest((packet/"INPUT_SHA256SUMS.txt").read_bytes()),
        "report_sha256": digest(report.read_bytes()),
    }
    for key, value in seal_checks.items():
        assert seal[key] == value, ("seal digest", key)
    assert seal["archive_members"] == count and seal["archive_payload_bytes"] == size
    if args.require_readonly:
        protected = all_paths+[packet, report, archive_path, member_manifest, seal_path]
        for p in protected:
            assert not stat.S_IMODE(p.stat().st_mode) & 0o222, ("writable issued path", str(p))
    result = {
        "audit": "AUD063",
        "status": "PASS",
        "input_copies_verified": len(inputs),
        "authored_output_files_verified": len(outputs),
        "archive_members_verified": count,
        "archive_payload_bytes_verified": size,
        "archive_extraction": "NONE",
        "safe_membership_and_bytes": "PASS",
        "report_copy_equality": "PASS",
        "read_only_checked": args.require_readonly,
        "hostile_verifier_controls": controls,
        "diagnostic_assertions": diagnostic["assertions"],
        "diagnostic_mutations": diagnostic["mutation_count"],
        **seal_checks,
    }
    if args.write_result:
        assert not args.write_result.exists(), "never replace an issued verification result"
        with args.write_result.open("x") as out:
            out.write(json.dumps(result, indent=2, sort_keys=True)+"\n")
        args.write_result.chmod(0o444)
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
