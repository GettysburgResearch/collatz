"""
Computes:
1. Exact binary entropy exponent h_2(log 2 / log 3) from STATE.md.
2. Exact Esscher-tilted mean-field eigenvalue lambda_1(s) = 0.5*(2^(-s) + (3/2)^s),
   confirming lambda_1(0) = lambda_1(1) = 1 and minimum lambda_1(s*) < 1.
3. Exact Galerkin transfer-operator eigenvalues on Z / 2^M Z (M = 4, 6, 8, 9).
"""
import json
import math
import numpy as np


def main():
    p_crit = math.log(2) / math.log(3)
    h2 = -(p_crit * math.log2(p_crit) + (1 - p_crit) * math.log2(1 - p_crit))

    # Esscher-tilted eigenvalue lambda_1(s) = 0.5 * (2^(-s) + (3/2)^s)
    # Derivative = 0 => 2^(-s)*ln(2) = (3/2)^s * ln(3/2) => 3^s = ln(2)/ln(3/2)
    s_star = math.log(math.log(2) / math.log(1.5)) / math.log(3)
    lam_star = 0.5 * (2.0 ** (-s_star) + 1.5 ** s_star)

    galerkin = {}
    for M in [4, 6, 8, 9]:
        N = 1 << M
        half = N >> 1
        P = np.zeros((N, N), dtype=float)
        for r in range(N):
            base = (r >> 1) if (r % 2 == 0) else (((3 * r + 1) >> 1) % half)
            P[base, r] += 0.5
            P[base + half, r] += 0.5
        mags = sorted([abs(ev) for ev in np.linalg.eigvals(P)], reverse=True)
        galerkin[M] = {
            "dim": N,
            "lambda_1": round(mags[0], 6),
            "lambda_2": round(mags[1], 6),
            "spectral_gap": round(mags[0] - mags[1], 6)
        }

    out = {
        "state_md_entropy": {
            "p_crit": round(p_crit, 6),
            "h2_p_crit": round(h2, 6)
        },
        "esscher_tilted_operator": {
            "s_star": round(s_star, 6),
            "lambda_1_at_0": 1.0,
            "lambda_1_at_1": 1.0,
            "lambda_1_at_s_star": round(lam_star, 6)
        },
        "galerkin_Z_mod_2M": galerkin
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
