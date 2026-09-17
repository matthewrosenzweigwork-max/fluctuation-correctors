# Diffusion-rescaling scope correction

2026-09-17. The fresh hostile reviewer independently identified an overbroad sentence in the sealed root memorandum MEMORANDA/ROUND_003_DIFFUSION_RESCALING.md. Preserve that submission unchanged. Its punctured chain-rule identity is unaffected. Its last substantive paragraph says, under full microscopic subcriticality, that no single diffusion limit follows without the rate. For fixed d<=s+2 this is false; the correct fixed-parameter classification is below.

Write e=s(s+2-d)/(d(s+2)), so chi_N=N^e/lambda_N exactly. Under lambda_N->0:

- If d<=s+2, then e>=0 and N^e>=1, hence chi_N>=1/lambda_N->infinity. No further rate assumption is needed.
- If d>s+2, write a=-e>0. Then chi_N=N^-a/lambda_N. Taking lambda_N=N^(-a/2), N^-a or N^(-2a) gives respectively zero, one or infinity as its limit. For example lambda_N=N^-a/(1+sin(log N)/2) gives a positive bounded oscillating chi_N and still satisfies full subcriticality.

The critical classification in the submitted note remains correct. All statements classify a scalar coefficient only; no closed collision-domain realization, solution existence, convergence, stochastic generator passage or full hierarchy theorem follows. This is a scope correction to an unpromoted root calculation, not a retraction of an audited theorem. The independent final verdict and exact input hash are recorded in the fresh hostile report when sealed.
