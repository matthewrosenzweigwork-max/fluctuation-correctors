#!/usr/bin/env python3
"""TASK047 supplemental integrity/location checks; standard library only.

This checks frozen bytes and finite scalar inequalities. It is not a proof of
local regularity; the supplied source argument is reviewed in the report.
No original TASK044 file is written.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).parent
ORIGINAL_OUTPUT_SEAL = '10b4836f893136fd2166af4e9358c3c0612c76da8f17bab93a0fbbfa8ca89c03'
ORIGINAL_INPUT_SEAL = 'd75bf1f5f67fbc8cabc65ba097d0c77bfda3dc485e50d2808b6b30ecc9fb446e'
SUPPLEMENTAL_INPUT_SEAL = '892ab43a9933fc844dd880e8d7e3e90c9203296236555293f43298f3d434e22b'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check_manifest(path):
    checked = []
    for line in path.read_text().splitlines():
        expected, rel = line.split(None, 1)
        rel = rel.strip()
        actual = sha(ROOT / rel)
        assert actual == expected, (rel, expected, actual)
        checked.append({'path': rel, 'sha256': actual})
    return checked

old_in = HERE/'ROUND_005_INTERFACE_INPUT_SHA256SUMS.txt'
old_out = HERE/'ROUND_005_INTERFACE_OUTPUT_SHA256SUMS.txt'
new_in = HERE/'ROUND_005_INTERFACE_SOURCE_RECHECK_INPUT_SHA256SUMS.txt'
assert sha(old_in) == ORIGINAL_INPUT_SEAL
assert sha(old_out) == ORIGINAL_OUTPUT_SEAL
assert sha(new_in) == SUPPLEMENTAL_INPUT_SEAL
old_inputs = check_manifest(old_in)
old_outputs = check_manifest(old_out)
new_inputs = check_manifest(new_in)
assert len(old_inputs) == 9 and len(old_outputs) == 5 and len(new_inputs) == 5

source = ROOT/'MEMORANDA/ROUND_004_SINGULAR_RESPONSE.md'
reconstruction = ROOT/'AUDITS/BLIND_RECONSTRUCTION/ROUND_004_RESPONSE_RECONSTRUCTION.md'
hostile = ROOT/'AUDITS/HOSTILE/ROUND_004_SINGULAR_RESPONSE_REVIEW.md'
addendum = ROOT/'AUDITS/ROUND_005_INTERFACE_SOURCE_AND_CONSTANT_ADDENDUM.md'
addendum_text = addendum.read_text()
for path in (source, reconstruction, hostile):
    assert sha(path) in addendum_text, path
lines = source.read_text().splitlines()
assert len(lines) == 541
assert lines[64] == '## 2. Source and normalization preflight'
source_span = '\n'.join(lines[68:109])
for tag in ('2.1', '2.2', '2.3', '2.4'):
    assert '\\tag{'+tag+'}' in source_span
assert 'C^\\infty(B_{1/3})' in source_span
assert 'smooth away from the origin' in source_span
r_lines = reconstruction.read_text().splitlines()
assert r_lines[17] == '## 1. Fourier normalization, finite divergence, and lower bound'
assert 'smooth locally' in r_lines[69]
assert 'nonnegative, even' in r_lines[26]
h_lines = hostile.read_text().splitlines()
assert 'C01.' in h_lines[34] and '**PASS**' in h_lines[34]
assert h_lines[60] == '### 3.1. Heat normalization, boundary terms and compensation'
assert 'all spatial derivatives remain integrable' in h_lines[75]

constant_cases = 0
for k21 in (F(0), F(1,3), F(5)):
    for c23 in (F(0), F(1,3), F(5)):
        kappa = max(k21, c23)
        assert -k21 >= -kappa
        for N in (2, 3, 17):
            assert c23/N <= kappa/N <= kappa/2
            constant_cases += 1

result = {
    'status': 'PASS',
    'scope': 'Integrity, cited source-location checks, and finite exact scalar diagnostics only.',
    'python': platform.python_version(),
    'dependencies': 'Python standard library only',
    'context_reused': True,
    'new_blind_review': False,
    'original_input_manifest_sha256': sha(old_in),
    'original_output_manifest_sha256': sha(old_out),
    'supplemental_input_manifest_sha256': sha(new_in),
    'original_inputs_unchanged': old_inputs,
    'original_outputs_unchanged': old_outputs,
    'supplemental_inputs_verified': new_inputs,
    'source_hashes_in_addendum_verified': 3,
    'source_locations': {
        'constructor': 'Section 2, lines 69-109, equations (2.1)-(2.4)',
        'reconstruction': 'Section 1, lines 20-70; evenness at line 27',
        'hostile': 'C01 at line 35; Section 3.1, lines 63-76',
    },
    'exact_constant_inequality_cases': constant_cases,
    'historical_r4_manifests_read': False,
    'historical_creation_chronology_verified': False,
}
output=HERE/'ROUND_005_INTERFACE_SOURCE_RECHECK_CHECK_RESULTS.json'
output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('original_inputs_unchanged','original_outputs_unchanged','supplemental_inputs_verified')}, indent=2, sort_keys=True))
