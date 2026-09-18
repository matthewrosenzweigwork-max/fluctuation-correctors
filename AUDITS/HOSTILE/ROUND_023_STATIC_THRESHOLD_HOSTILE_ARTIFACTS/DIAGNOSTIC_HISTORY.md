# Diagnostic development and final evidence

The diagnostic is new code from this hostile context. No root or earlier worker code/results were read. Python 3.9.6 standard library only; deterministic cases and no random seed. Mathematical claims are established analytically in the review; floating Ewald calculations are nonrigorous support.

The first execution reached the finite-grid source convergence check and failed an absolute error threshold of 0.15 when the largest grid tested was 13. An inspection-only rerun printed the values: the scaled source at 13 was approximately -2.1164035357 and the analytic target approximately -1.9481818207, leaving error 0.1682217150. The theorem states no finite-grid convergence rate. The final test extended the grid list to 17, without weakening the threshold; error there is approximately 0.1004429149. A cutoff-3/cutoff-4 comparison remains a separate check.

Before rerunning, an intended epsilon-sign parity test was restricted to the even grid 6, where translating by one half permutes the grid and reverses the deformation. Odd grids do not have that relabelling symmetry; the code makes no parity assertion for them. This was a diagnostic design correction, not a change to the candidate or its theorem. A read-only `--verify` mode was then added and the final results regenerated because the code hash changed.

Final normal execution: PASS, 384 assertions, 22 categories, 12 detecting mutations. The result JSON records the complete numerical and exact cases and the final script hash. The final seal procedure also reruns `--verify`, which compares the complete recomputation with the saved result and writes nothing.

The false candidate support sentence is tested independently by rotating the source coordinates through pi/2; this defect is identified analytically in AUD066-F01. It is recorded as an actual discovered assertion failure, separate from the twelve deliberately invented coefficient/scaling/averaging mutations.

The sealed result does not retrospectively hide the preliminary failed diagnostic or claim interval certification. No earlier development result is used as final evidence.
