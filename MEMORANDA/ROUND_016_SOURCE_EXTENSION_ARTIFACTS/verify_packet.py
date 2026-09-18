#!/usr/bin/env python3
"""Read-only exact packet verification; never extracts archive members."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import sys
import tarfile


PREFIX = "MEMORANDA/ROUND_016_SOURCE_EXTENSION_ARTIFACTS/"
MANIFEST = PREFIX + "OUTPUT_SHA256SUMS.txt"
MEMBERS = PREFIX + "ARCHIVE_MEMBERS.txt"
INPUT_MANIFEST = PREFIX + "INPUT_SHA256SUMS.txt"
REPORT = "MEMORANDA/ROUND_016_SOURCE_EXTENSION.md"


def parse_manifest(data):
    parsed = {}
    for line in data.decode("utf-8").splitlines():
        digest, name = line.split("  ", 1)
        assert len(digest) == 64 and all(c in "0123456789abcdef" for c in digest)
        assert name not in parsed
        parsed[name] = digest
    return parsed


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: verify_packet.py ARCHIVE.tar.gz")
    archive = Path(sys.argv[1])
    archive_hash = hashlib.sha256(archive.read_bytes()).hexdigest()
    payload = {}
    with tarfile.open(archive, "r:gz") as handle:
        for member in handle.getmembers():
            path = PurePosixPath(member.name)
            assert member.isfile(), ("nonregular member", member.name)
            assert not path.is_absolute() and ".." not in path.parts
            assert str(path) == member.name and member.name not in payload
            assert member.name == REPORT or member.name.startswith(PREFIX)
            stream = handle.extractfile(member)
            assert stream is not None
            data = stream.read()
            assert len(data) == member.size
            payload[member.name] = data
    assert REPORT in payload
    declared = payload[MEMBERS].decode("utf-8").splitlines()
    assert len(declared) == len(set(declared))
    assert sorted(declared) == sorted(payload)
    output = parse_manifest(payload[MANIFEST])
    assert set(output) == set(payload) - {MANIFEST}
    for name, digest in output.items():
        assert hashlib.sha256(payload[name]).hexdigest() == digest, name
    inputs = parse_manifest(payload[INPUT_MANIFEST])
    assert len(inputs) == 9
    for name, digest in inputs.items():
        member_name = PREFIX + "INPUTS/" + name
        assert hashlib.sha256(payload[member_name]).hexdigest() == digest, name
    result = {
        "status": "PASS",
        "archive": str(archive.resolve()),
        "archive_sha256": archive_hash,
        "regular_members": len(payload),
        "output_byte_hashes_verified": len(output),
        "exact_input_byte_hashes_verified": len(inputs),
        "output_manifest_sha256": hashlib.sha256(payload[MANIFEST]).hexdigest(),
        "membership": sorted(payload),
        "extraction_performed": False,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
