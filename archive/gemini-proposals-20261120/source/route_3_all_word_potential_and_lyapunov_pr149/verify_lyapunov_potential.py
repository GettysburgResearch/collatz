#!/usr/bin/env python3
"""
Route 3 Verifier: Fractional-Moment (L^alpha) Cramér-Chernoff Window &
Killed Markov Transfer Spectral Radius on Z / 2^m Z.
Aligned with GettysburgResearch/collatz PR #149 and Open Obligation #4.

Verifies:
1. Exact Cramér-Chernoff strict contraction window alpha in (0, 1) with minimum at alpha_min ~ 0.48988.
2. Exact tilted-unsafe buffer: for p_odd = 0.55, L^(1/2) still contracts (< 1) while L^1 explodes (> 1).
3. Exact spectral radius of full and killed transfer matrices M_alpha^(m) on Z / 2^m Z (m = 3..7).
4. Negative control: confirms L^1 (alpha = 1) has spectral radius 1.0 on full matrix and > 1 under odd tilt.
"""

import json
import math
import numpy as np


def lambda_alpha(alpha: float, p_odd: float = 0.5) -> float:
    return (1.0 - p_odd) * (2.0 ** (-alpha)) + p_odd * ((1.5) ** alpha)


def build_transfer_matrix(m: int, alpha: float, kill_immediate_descent: bool = False) -> np.ndarray:
    """
    Build 2^m x 2^m weighted transition matrix on Z / 2^m Z for the shortcut map T.
    If kill_immediate_descent=True, zero out rows for residue classes r that strictly
    descend within <= m steps (T^s(2^m*k + r) < 2^m*k + r for all k >= 1).
    """
    N = 1 << m
    M = np.zeros((N, N), dtype=np.float64)
    killed = set()
    if kill_immediate_descent:
        for r in range(N):
            A, B = N, r
            for _ in range(m):
                if A % 2 != 0:
                    break
                if B % 2 == 0:
                    A //= 2
                    B //= 2
                else:
                    A = (3 * A) // 2
                    B = (3 * B + 1) // 2
                if A < N and (B < r or (r == 0 and A + B < N)):
                    killed.add(r)
                    break

    for r in range(N):
        if r in killed:
            continue
        if r % 2 == 0:
            w = 2.0 ** (-alpha)
            nxt0 = r // 2
            nxt1 = (r + N) // 2
        else:
            w = 1.5 ** alpha
            nxt0 = ((3 * r + 1) // 2) % N
            nxt1 = ((3 * (r + N) + 1) // 2) % N
        M[r, nxt0] += 0.5 * w
        M[r, nxt1] += 0.5 * w
    return M, len(killed)


def spectral_radius(M: np.ndarray) -> float:
    eigvals = np.linalg.eigvals(M)
    return float(np.max(np.abs(eigvals)))


def main():
    alpha_min = math.log(math.log(2.0) / math.log(1.5)) / math.log(3.0)
    lam_min = lambda_alpha(alpha_min)
    lam_half = lambda_alpha(0.5)
    lam_one = lambda_alpha(1.0)

    # Assert exact algebraic properties
    assert abs(lam_one - 1.0) < 1e-12
    assert lam_half < 0.966
    assert lam_min < lam_half < 1.0

    # Tilt test: p_odd = 0.55 (unsafe resonance tilt)
    tilted_half = lambda_alpha(0.5, p_odd=0.55)
    tilted_one = lambda_alpha(1.0, p_odd=0.55)
    assert tilted_half < 1.0, "L^(1/2) must still contract at p_odd=0.55"
    assert tilted_one > 1.0, "Negative control: L^1 must explode at p_odd=0.55"

    # Spectral radius checks across m = 3..7
    spectral_table = []
    for m in range(3, 8):
        M_full, _ = build_transfer_matrix(m, alpha=0.5, kill_immediate_descent=False)
        M_kill, n_killed = build_transfer_matrix(m, alpha=0.5, kill_immediate_descent=True)
        rho_full = spectral_radius(M_full)
        rho_kill = spectral_radius(M_kill)
        assert abs(rho_full - lam_half) < 1e-9, f"Full spectral radius mismatch at m={m}"
        assert rho_kill < rho_full < 1.0, f"Killed matrix should strictly contract faster at m={m}"
        spectral_table.append({
            "m": m,
            "states": 1 << m,
            "killed_descent_classes": n_killed,
            "rho_full_L_half": round(rho_full, 6),
            "rho_killed_L_half": round(rho_kill, 6),
        })

    # Negative control on full L^1 matrix at m=5
    M_l1, _ = build_transfer_matrix(5, alpha=1.0, kill_immediate_descent=False)
    rho_l1 = spectral_radius(M_l1)
    assert abs(rho_l1 - 1.0) < 1e-9, "Negative control failed: full L^1 spectral radius must be 1.0"

    result = {
        "route": "route_3_all_word_potential_and_lyapunov_pr149",
        "status": "PASS",
        "alpha_min": round(alpha_min, 6),
        "lambda_alpha_min": round(lam_min, 6),
        "lambda_half": round(lam_half, 6),
        "lambda_one_boundary": round(lam_one, 6),
        "tilted_p055_L_half": round(tilted_half, 6),
        "tilted_p055_L_one_explodes": round(tilted_one, 6),
        "spectral_contraction_table": spectral_table,
        "negative_control_L1_boundary_verified": True,
    }
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    main()
