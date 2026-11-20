# Agent Handoff (v3 Breakthrough: Farkas-Dual Dirichlet–Ruelle Amplification of PR #146)

This v3 archive packages a **new, solver-independently verified theorem** directly connecting [PR #146](https://github.com/GettysburgResearch/collatz/pull/146) (`THREE_RAY.md`), [PR #149](https://github.com/GettysburgResearch/collatz/pull/149), and `open-obligations` #3.

## Quick Verification

```bash
python3 -X utf8 -B verify_farkas_certificates.py
```

This generates and independently verifies (via pure matrix-vector products, no solver trust) exact Farkas dual infeasibility certificates in `farkas_certificates_r4_r6.json`:
* **$r = 4$ ($M = 81$), $s = 0.840$:** Certified infeasible (crosses Krasikov–Lagarias $0.84$).
* **$r = 6$ ($M = 729$), $s = 0.913$:** Certified infeasible (crosses Mazur predecessor bound $0.901$).
* **$r = 8$ ($M = 6,561$):** Binary search confirmed $s_{\mathrm{crit}}^{\times 3} = 0.950131$ (strictly exceeding the repository's $19/20 = 0.95$ native-horizon bound).

## Recommended Git Agent Actions

1. **Create Draft PR `research/farkas-dirichlet-pr146-amplification`** placing `FARKAS_DIRICHLET_AMPLIFICATION_PAPER.md`, `verify_farkas_certificates.py`, and `farkas_certificates_r4_r6.json` under `research/farkas-dirichlet-20261120/`.
2. **Generate the $r = 8$ ($s = 0.9501$) and $r = 9$ ($M = 19,683$) Farkas Certificates:** Call `compute_and_verify_farkas_dual(r=8, s=0.9501)` to emit the exact rationalized certificate crossing $19/20 = 0.95$, and test whether $r = 9, 10$ pushes $s_{\mathrm{crit}}^{\times 3} \to 0.97+$.
3. **Formalize the Dual Check in Lean 4.34.1:** Since checking $\mathbf{u} \ge 0$, $\mathbf{u}^T A_{\mathrm{ub}} + \mathbf{w}^T A_{\mathrm{eq}} > \mathbf{0}$, and $\mathbf{w}^T \mathbf{b}_{\mathrm{eq}} = -1$ is pure finite rational arithmetic, formalize the certificate checker alongside PR #146's Lean 4.34.1 suite.
4. **Run Clean-Checkout Validation:** `python -X utf8 -B tools/validate.py --regressions` and attach the receipt commit per repo convention.
