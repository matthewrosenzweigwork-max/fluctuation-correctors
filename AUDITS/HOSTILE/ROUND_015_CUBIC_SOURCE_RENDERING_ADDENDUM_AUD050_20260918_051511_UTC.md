# AUD050 rendering addendum

2026-09-18 05:15:11 UTC. This is a rendering clarification of my own issued AUD050 report, prompted by root's byte inspection. It is **not a new independent audit or gate**. The mathematical verdict remains **CONDITIONAL PASS of the complete frozen THM-036 / THM-037 conjunction**, with exactly the earlier-module qualifications and limitations in the original review.

## Immutable original and exact defects

The original is `AUDITS/HOSTILE/ROUND_015_CUBIC_SOURCE_REVIEW.md`, 32,174 bytes, SHA-256:

`9ff4765f3ded77f6a3d41fa575d53460b28890f45aa5403764c70a93a0384da1`.

It remains unchanged, as do every original packet payload, manifest, archive, seal and sidecar. The original archive SHA-256 is `37fef68c77ee86ec6a4a8b1c272d37c6f4de74cb2cd5ff2acd5309edc49e950c`.

The report contains exactly three form-feed bytes, U+000C (hex `0c`), at the locations below. Lines are counted using LF byte delimiters; line and byte column are one-based. File byte offsets are zero-based. No original byte has been replaced.

| Original location | File byte offset | One-based byte position | Stored prefix | Intended printable prefix |
|---|---:|---:|---|---|
| Line 364, byte column 35, H16 second coefficient | 23058 | 23059 | `0c 72 61 63` | `5c 66 72 61 63` |
| Line 364, byte column 57, H16 scalar coefficient | 23080 | 23081 | `0c 72 61 63` | `5c 66 72 61 63` |
| Line 420, byte column 49, whole-square inequality background coefficient | 26372 | 26373 | `0c 72 61 63` | `5c 66 72 61 63` |

Each stored prefix is a form-feed followed by the ASCII letters `rac`. Each intended prefix is the ASCII backslash followed by `frac`. Thus each affected TeX command lost the intended printable backslash-plus-f pair in serialization. The intended command tails are respectively `1{N^3}`, `{m^2}{4N^2}` and `2N`. The abbreviated fraction arguments are written with explicit braces below for readability; their coefficients are unchanged.

## Intended readable formulas

In H16, the intended second-moment equality is

\[
 \mathbb E|P_N[F]|^2
 =\frac{N-1}{2N^3}\|F_\circ\|_2^2
  +\frac{1}{N^3}\|q_0\|_2^2
  +\frac{m^2}{4N^2}.
\]

Here the definitions and norm identity in the original report remain unchanged. In plain text, the three coefficients are `(N-1)/(2 N^3)`, `1/N^3` and `1/(4 N^2)`, multiplying the squared norm of the degenerate kernel, the squared norm of the first projection and the squared scalar mean, respectively.

The intended whole-square inequality spanning original lines 418–421 is

\[
 \mathbb E\sum_i|\nabla_iP_N|^2
 \le \frac{2(N-1)^2}{N^3}\mathbb E|G(X_1,X_2)|^2
    +\frac{2}{N}\|A_\Phi\|_2^2.
\]

In plain text, the background squared norm has coefficient `2/N`. There is no change to the pair coefficient, any power of N, or the whole-square interpretation.

## Disposition and verification

This addendum changes only the readable rendering of three command prefixes. It does not change any mathematical assertion, coefficient, proof scope, centering, conditional premise, exclusion or verdict. It does not introduce a corrected theorem, new proof, new independent certification or replacement report. The original remains the issued content-addressed report with these rendering defects documented separately.

The accompanying control-byte scan records the exact original locations and verifies that this addendum contains no C0/C1 control characters other than ordinary line feeds. Its mathematical backslashes are printable ASCII. A preservation check compares all 44 originally issued files with their pre-addendum hashes. The new archive contains only this clarification and its own verification records; its membership and member bytes are checked exactly. The new SHA-256 sidecar and seal identify this addendum independently of the original packet.
