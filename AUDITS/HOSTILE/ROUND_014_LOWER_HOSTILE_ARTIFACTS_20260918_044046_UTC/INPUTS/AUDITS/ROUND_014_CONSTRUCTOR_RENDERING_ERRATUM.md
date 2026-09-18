# Round014 constructor rendering erratum

2026-09-18 UTC. This separate root record preserves the issued constructor SHA256266d8fe2cdbaa4111c3f5b515ed22c791f291508987618de525c49f9c67d3f14 and its complete sealed packet unchanged.

In equation(4.6), source lines267–268, the sum subscript is split as the literal text `\sum_{i,j,k\ {`, newline, `m distinct}}`. The intended sum is over the ordered pairwise distinct labels i,j,k, exactly as defined in the frozen R1/R8 convention, the immediately preceding/following prose and literal checker. A readable TeX rendering is `\sum_{\substack{i,j,k\\\mathrm{distinct}}}`. This changes neither the coefficient1/N^3 nor any label, background contraction or mathematical claim. No control byte remains in the issued file, but its macro text is malformed. The original report was Markdown-format checked, not TeX-rendered, as its verification record explicitly states.

The fresh hostile reviewer must examine this interpretation against the full sources and report any mathematical disagreement. Root grants no independent audit status by this erratum. Future standalone synthesis uses the readable distinct-label notation; no in-place correction of an issued input or checksum is made.
