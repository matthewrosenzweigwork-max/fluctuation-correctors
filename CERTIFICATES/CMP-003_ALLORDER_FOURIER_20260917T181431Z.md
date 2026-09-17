# CMP-003 — independent finite Fourier recursion tests

- Status: REPRODUCED finite exact battery; no claim of a general-proof certificate.
- Statement source: exact candidate kernels supplied by isolated Max recursion worker before its proof report.
- Verifier: VERIFICATION_CODE/round001_allorder_fourier_check.py, SHA-256 `c0b1ad41b6ff4a44e50144e47c8263272a92513997c47a68ee45aee09b44b7f9`.
- It imports only root's pre-existing rational polynomial primitives; no worker discovery code or substantive algorithm is shared. Direct particle-coordinate differentiation of expanded U_k is compared with separately assembled operator kernels.
- Command: `python3 VERIFICATION_CODE/round001_allorder_fourier_check.py > BUILD/round001_allorder_fourier_check.json`.
- Environment: Python 3.9.6, standard library; seed none; tolerance zero.
- Cases: k=1,2,3,4; N=2,3,4 including k>N; nu=0,1/3,2; constant, sum-mode, product-mode, symmetric mixed-mode kernels. Uniform stationary reference and g=cos(2 pi x); generator divided by (2 pi)^2.
- Expected/actual: PASS, 144 cases; every rational Laurent coefficient vanishes exactly.
- Output SHA-256: `07cd61759f5410c29bab922db2b2d45959fece1a50b260085e6c2797c561dc34`.
- Limitations: smooth homogeneous one-dimensional battery only. Does not prove general subset formula, critical power counting, singular passage, or a hierarchy tail bound.
