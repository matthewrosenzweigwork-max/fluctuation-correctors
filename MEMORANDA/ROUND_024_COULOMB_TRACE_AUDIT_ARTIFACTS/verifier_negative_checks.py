#!/usr/bin/env python3
"""Exercise byte/member rejections in memory, with no extraction or temp files."""
import io
import json
from pathlib import Path
import runpy
import tarfile

api = runpy.run_path(str(Path(__file__).with_name("verify_packet.py")))
digest, parse, verify = api["digest"], api["parse_manifest"], api["verify_archive"]
payload = b"frozen evidence\n"
manifest = (digest(payload) + "  packet/evidence.txt\n").encode()
entries = {"packet/evidence.txt": digest(payload)}
manifest_name = "packet/MANIFEST.txt"


def archive(members):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tf:
        for name, data, kind, link in members:
            info = tarfile.TarInfo(name)
            info.type = kind
            info.linkname = link
            info.size = len(data) if kind == tarfile.REGTYPE else 0
            tf.addfile(info, io.BytesIO(data) if kind == tarfile.REGTYPE else None)
    buf.seek(0)
    return buf


good = [("packet/evidence.txt", payload, tarfile.REGTYPE, ""),
        (manifest_name, manifest, tarfile.REGTYPE, "")]
assert verify(archive(good), entries, manifest_name, manifest) == 2
bad = {
    "wrong_bytes": [("packet/evidence.txt", payload + b"x", tarfile.REGTYPE, ""), good[1]],
    "missing_member": [good[1]],
    "duplicate_member": good + [good[0]],
    "extra_member": good + [("packet/extra.txt", b"x", tarfile.REGTYPE, "")],
    "traversal": [("../evidence.txt", payload, tarfile.REGTYPE, ""), good[1]],
    "absolute_path": [("/packet/evidence.txt", payload, tarfile.REGTYPE, ""), good[1]],
    "symlink": [("packet/evidence.txt", b"", tarfile.SYMTYPE, "/etc/passwd"), good[1]],
    "hardlink": [("packet/evidence.txt", b"", tarfile.LNKTYPE, "outside"), good[1]],
    "directory_member": [("packet/evidence.txt", b"", tarfile.DIRTYPE, ""), good[1]],
    "wrong_manifest_bytes": [good[0], (manifest_name, manifest + b"\n", tarfile.REGTYPE, "")],
}
detected = []
for name, members in bad.items():
    try:
        verify(archive(members), entries, manifest_name, manifest)
    except (ValueError, tarfile.TarError):
        detected.append(name)
    else:
        raise AssertionError("mutation escaped verifier: " + name)
for name, content in [
    ("duplicate_manifest_path", manifest + manifest),
    ("bad_manifest_digest", b"z" * 64 + b"  packet/evidence.txt\n"),
    ("manifest_traversal", digest(payload).encode() + b"  ../evidence.txt\n"),
]:
    try:
        parse(content)
    except ValueError:
        detected.append(name)
    else:
        raise AssertionError("manifest mutation escaped: " + name)
print(json.dumps({"status": "PASS", "positive_archive_checks": 1,
                  "negative_cases_detected": detected, "extraction": False}, indent=2))
