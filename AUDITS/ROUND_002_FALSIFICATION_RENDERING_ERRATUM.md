# Rendering erratum to the sealed Round 002 falsification report

2026-09-17. Original report MEMORANDA/ROUND_002_FALSIFICATION.md remains immutable at SHA-256 125317981b543cf83a47a64efc1455453fbd942e476a52b15e64ec984c216856. The hostile reviewer found one formatting defect in (2.5): a form-feed control byte followed by `rac` appears where the first fraction command belongs. The exact intended and independently recomputed formulas are

\[
 \frac{d[M_\Phi]}{dt}=\frac{2}{\beta N^2}\sum_i|H_i|^2,
 \qquad
 \frac{d[M_f,M_\Phi]}{dt}
 =\frac{2}{\beta N^2}\sum_i\nabla f(X_i)\cdot H_i.
\]

This is a rendering correction, with no changed mathematical coefficient, theorem scope, proof step, or audit input. Use this readable display when consulting the sealed original. The original proof bytes have not been normalized or silently repaired.
