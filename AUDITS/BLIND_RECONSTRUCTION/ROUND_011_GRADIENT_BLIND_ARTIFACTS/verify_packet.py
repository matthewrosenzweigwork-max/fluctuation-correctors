#!/usr/bin/env python3
"""Read-only verification of the TASK-068 blind packet."""
from hashlib import sha256
from pathlib import Path
import json
import zipfile

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[2]

def digest(data):
    return sha256(data).hexdigest()

def manifest(path):
    out = {}
    for line in path.read_text().splitlines():
        expected, relative = line.split("  ",1)
        p = Path(relative)
        assert not p.is_absolute() and ".." not in p.parts, relative
        assert relative not in out, relative
        assert len(expected) == 64, relative
        assert digest((WORK/p).read_bytes()) == expected, relative
        out[relative] = expected
    return out

inputs = manifest(HERE/"INPUT_SHA256SUMS.txt")
outputs = manifest(HERE/"OUTPUT_SHA256SUMS.txt")
seals = manifest(HERE/"SEAL_SHA256SUMS.txt")
assert len(inputs) == 21
assert len(outputs) == 7
assert len(seals) == 2
expected = dict(inputs)
for path, value in outputs.items():
    assert path not in expected
    expected[path] = value
outpath = (HERE/"OUTPUT_SHA256SUMS.txt").relative_to(WORK).as_posix()
expected[outpath] = digest((WORK/outpath).read_bytes())
archives = [p for p in seals if p.endswith(".zip")]
assert len(archives) == 1
with zipfile.ZipFile(WORK/archives[0]) as packet:
    names = packet.namelist()
    assert len(names) == len(set(names))
    assert set(names) == set(expected), (set(names)-set(expected),set(expected)-set(names))
    assert packet.testzip() is None
    for path in names:
        p = Path(path)
        assert not p.is_absolute() and ".." not in p.parts
        assert digest(packet.read(path)) == expected[path], path
print(json.dumps({
    "status":"PASS",
    "inputs_verified":len(inputs),
    "outputs_verified":len(outputs),
    "archive_members_verified":len(expected),
    "seal_entries_verified":len(seals),
    "archive":archives[0],
    "archive_sha256":seals[archives[0]],
},indent=2))

