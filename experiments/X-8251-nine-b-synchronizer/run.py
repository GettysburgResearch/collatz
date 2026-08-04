#!/usr/bin/env python3
"""Exact generator/checker for X-8251.

This standard-library-only program verifies the nine-B two-place synchronizer,
the branch-independent odd invariant D_9=16^9-9^9, the centered quotient map,
the high-run positivity threshold, and a declared finite quotient corpus.

No counterexample or infinite orbit is asserted.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Iterable

D9 = 16**9 - 9**9
OMEGA = 37_933_813_917
A = (9**9 * OMEGA + 1) // D9
B = (16**9 * OMEGA + 1) // D9


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0)")
    n = abs(n)
    return (n & -n).bit_length() - 1


def v3(n: int) -> int:
    if n == 0:
        raise ValueError("v3(0)")
    n = abs(n)
    out = 0
    while n % 3 == 0:
        n //= 3
        out += 1
    return out


def crt_pair(a: int, m: int, b: int, n: int) -> int:
    if math.gcd(m, n) != 1:
        raise ValueError("CRT moduli must be coprime")
    return (a + ((b - a) * pow(m, -1, n) % n) * m) % (m * n)


def z_step(z: int) -> tuple[int, str] | None:
    if z > 0 and z % 8 == 0:
        return 9 * z // 8, "A"
    if z > 0 and z % 16 == 1:
        return (9 * z + 7) // 16, "B"
    return None


def branch_data(s: int) -> tuple[int, int, int, int, int]:
    """Return (xi_s, 2^h, c_s, 9^(s+9), T_s).

    In the centered coordinate W=OMEGA+D9*X, a defined branch is
        X = xi_s + 2^(3s+36) k,
        X' = c_s + 9^(s+9) k.
    """
    h = 3 * s + 36
    radix = 1 << h
    multiplier = 9 ** (s + 9)
    toll = 9**s * A - 8**s * B
    xi = (-toll * pow(multiplier, -1, radix)) % radix
    numerator = multiplier * xi + toll
    if numerator % radix:
        raise AssertionError("branch residue does not divide")
    c = numerator // radix
    return xi, radix, c, multiplier, toll


def raw_W_step(W: int, s: int) -> int | None:
    """Apply one high-run-plus-eight-zero-run block with next high run s."""
    numerator = 9**s * (1 + 9**9 * W) - 2 ** (3 * s)
    denominator = 2 ** (3 * s + 36)
    if numerator % denominator:
        return None
    if v2(1 + 9**9 * W) != 3 * s:
        return None
    return numerator // denominator


def centered_X_step(X: int, s: int) -> int | None:
    xi, radix, c, multiplier, _ = branch_data(s)
    if (X - xi) % radix:
        return None
    k = (X - xi) // radix
    return c + multiplier * k


def joint_domain(r: int, s: int) -> tuple[int, int]:
    """Unique W residue carrying current high run r and next high run s.

    Conditions:
      W == OMEGA mod D9,
      9^r | 1+16^9 W,
      the s-branch is defined exactly.
    """
    xi, radix, _, _, _ = branch_data(s)
    # W=OMEGA+D9*X and X=xi mod radix is equivalent to one W residue mod D9*radix.
    w2 = OMEGA + D9 * xi
    m2 = D9 * radix

    m3 = 9**r
    if r:
        w3 = (-pow(16**9, -1, m3)) % m3
        W = crt_pair(w2 % m2, m2, w3, m3)
    else:
        W = w2 % m2
    modulus = m2 * m3
    return W, modulus


def physical_block_check(W: int, r: int, s: int) -> tuple[int, int]:
    """Reconstruct and replay A^r B^9 physically; return (W', final z)."""
    p = 1 + 16**9 * W
    if p % (7 * 9**r):
        raise AssertionError("current pre-B state lacks 7*9^r")
    v = p // (7 * 9**r)
    if v <= 0 or v % 2 == 0:
        raise AssertionError("initial core is not positive odd")
    z = 7 * 2 ** (3 * r) * v

    for _ in range(r):
        nxt = z_step(z)
        if nxt is None or nxt[1] != "A":
            raise AssertionError("A-run replay failed")
        z = nxt[0]
    if z != p:
        raise AssertionError("pre-B state mismatch")

    for _ in range(9):
        nxt = z_step(z)
        if nxt is None or nxt[1] != "B":
            raise AssertionError("B^9 replay failed")
        z = nxt[0]

    if z != 1 + 9**9 * W:
        raise AssertionError("post-B^9 section mismatch")
    if v2(z) != 3 * s:
        raise AssertionError("next high run mismatch")

    for _ in range(s):
        nxt = z_step(z)
        if nxt is None or nxt[1] != "A":
            raise AssertionError("next A-run replay failed")
        z = nxt[0]

    Wp = raw_W_step(W, s)
    if Wp is None:
        raise AssertionError("raw W branch failed")
    expected = 1 + 16**9 * Wp
    if z != expected:
        raise AssertionError("next pre-B boundary mismatch")
    return Wp, z


def quotient_pair(s: int, t: int) -> tuple[int, int]:
    """Pull the t-domain through one centered s-branch.

    If X=xi_s+2^h_s k, then continuation with t is
        k = rho + 2^h_t ell,
        k' = sigma + 9^(s+9) ell.
    """
    xi_s, radix_s, c_s, multiplier_s, _ = branch_data(s)
    xi_t, radix_t, _, _, _ = branch_data(t)
    del xi_s, radix_s
    rho = ((xi_t - c_s) * pow(multiplier_s, -1, radix_t)) % radix_t
    sigma_numerator = c_s + multiplier_s * rho - xi_t
    if sigma_numerator % radix_t:
        raise AssertionError("pair quotient is not integral")
    sigma = sigma_numerator // radix_t
    return rho, sigma


def prime_factors_trial(n: int) -> list[int]:
    factors: list[int] = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors.append(n)
    return factors


def build_payload() -> dict[str, object]:
    if D9 != 68_332_056_247:
        raise AssertionError("D9 constant mismatch")
    if OMEGA != (-pow(9**9, -1, D9)) % D9:
        raise AssertionError("omega is not the common inverse residue")
    if (9**9 * OMEGA + 1) % D9 or (16**9 * OMEGA + 1) % D9:
        raise AssertionError("boundary divisibility failed")
    if B - A != OMEGA:
        raise AssertionError("Bezout quotient relation failed")

    factors = prime_factors_trial(D9)
    if factors != [7, 13, 19, 37, 163, 6553]:
        raise AssertionError("unexpected D9 factorization")

    threshold = {
        "multiplier_43_positive": 9**52 > 2**165,
        "multiplier_44_positive": 9**53 > 2**168,
        "toll_43": str(9**43 * A - 8**43 * B),
        "toll_44": str(9**44 * A - 8**44 * B),
    }
    if threshold["multiplier_43_positive"]:
        raise AssertionError("the multiplier threshold should fail at 43")
    if not threshold["multiplier_44_positive"]:
        raise AssertionError("the multiplier threshold should hold at 44")
    if int(threshold["toll_43"]) >= 0 or int(threshold["toll_44"]) <= 0:
        raise AssertionError("the toll threshold is not 44")

    counters = {
        "centered_branch_instances": 0,
        "raw_centered_agreements": 0,
        "invariant_residue_checks": 0,
        "physical_high_block_replays": 0,
        "quotient_pair_identities": 0,
        "high_growth_checks": 0,
        "bounded_zero_carry_pairs": 0,
    }
    digest = hashlib.sha256()
    samples: list[dict[str, object]] = []

    # Centered branch and invariant checks over a broad deterministic corpus.
    for s in range(0, 97):
        xi, radix, c, multiplier, toll = branch_data(s)
        for lift in range(0, 17):
            X = xi + radix * lift
            Xp = c + multiplier * lift
            W = OMEGA + D9 * X
            Wp = raw_W_step(W, s)
            if Wp is None:
                raise AssertionError("declared branch unexpectedly undefined")
            if Wp != OMEGA + D9 * Xp:
                raise AssertionError("raw and centered maps disagree")
            if W % D9 != OMEGA or Wp % D9 != OMEGA:
                raise AssertionError("D9 invariant residue failed")
            if W % 7 != 6 or Wp % 7 != 6:
                raise AssertionError("divisible-seven projection failed")
            if s >= 44:
                if Xp <= X:
                    raise AssertionError("high centered branch failed strict growth")
                counters["high_growth_checks"] += 1
            counters["centered_branch_instances"] += 1
            counters["raw_centered_agreements"] += 1
            counters["invariant_residue_checks"] += 1
            digest.update(f"B|{s}|{lift}|{X}|{Xp}\n".encode("ascii"))
        if s in {0, 1, 43, 44, 64, 65, 96}:
            samples.append(
                {
                    "run": s,
                    "radix_bits": 3 * s + 36,
                    "xi": str(xi),
                    "canonical_output": str(c),
                    "toll": str(toll),
                    "multiplier_bits": multiplier.bit_length(),
                }
            )

    # Exact physical A^r B^9 replay, including high-high transitions.
    physical_pairs = list(itertools.product(range(0, 9), repeat=2))
    physical_pairs += list(itertools.product(range(44, 51), repeat=2))
    for r, s in physical_pairs:
        R, modulus = joint_domain(r, s)
        for lift in range(0, 5):
            W = R + modulus * lift
            Wp, final_z = physical_block_check(W, r, s)
            X = (W - OMEGA) // D9
            Xp = centered_X_step(X, s)
            if Xp is None or Wp != OMEGA + D9 * Xp:
                raise AssertionError("physical and centered coordinates disagree")
            counters["physical_high_block_replays"] += 1
            digest.update(f"P|{r}|{s}|{lift}|{final_z}\n".encode("ascii"))

    # Pair quotient law and a bounded zero-carry audit.
    pair_ranges = list(itertools.product(range(0, 17), repeat=2))
    pair_ranges += list(itertools.product(range(44, 65), repeat=2))
    seen_pairs: set[tuple[int, int]] = set()
    for s, t in pair_ranges:
        if (s, t) in seen_pairs:
            continue
        seen_pairs.add((s, t))
        rho, sigma = quotient_pair(s, t)
        xi_s, radix_s, c_s, multiplier_s, _ = branch_data(s)
        xi_t, radix_t, _, _, _ = branch_data(t)
        for ell in range(0, 7):
            k = rho + radix_t * ell
            X = xi_s + radix_s * k
            Xp = centered_X_step(X, s)
            if Xp is None:
                raise AssertionError("pair source branch undefined")
            kp = (Xp - xi_t) // radix_t
            if Xp != xi_t + radix_t * kp:
                raise AssertionError("target branch residue failed")
            if kp != sigma + multiplier_s * ell:
                raise AssertionError("pair quotient identity failed")
            counters["quotient_pair_identities"] += 1
            digest.update(f"Q|{s}|{t}|{ell}|{k}|{kp}\n".encode("ascii"))
        if rho == 0 and sigma == 0:
            counters["bounded_zero_carry_pairs"] += 1

    # Separate wider bounded search for an exactly zero pair in the live high range.
    zero_pairs: list[list[int]] = []
    for s in range(44, 81):
        for t in range(44, 81):
            rho, sigma = quotient_pair(s, t)
            if rho == 0 and sigma == 0:
                zero_pairs.append([s, t])
    if zero_pairs:
        raise AssertionError("unexpected high zero-carry pair")
    counters["bounded_zero_carry_pairs"] = len(zero_pairs)

    return {
        "experiment_id": "X-8251",
        "status": "exact finite verification of the declared corpus; L-8251/L-8252 remain PROPOSED",
        "constants": {
            "D9": D9,
            "D9_factorization": factors,
            "omega": OMEGA,
            "a": A,
            "b": B,
            "b_minus_a": B - A,
        },
        "threshold": threshold,
        "scope": {
            "centered_runs": [0, 96],
            "lifts_per_centered_run": 17,
            "physical_small_runs": [0, 8],
            "physical_high_runs": [44, 50],
            "physical_lifts_per_pair": 5,
            "quotient_small_runs": [0, 16],
            "quotient_high_runs": [44, 64],
            "quotient_lifts_per_pair": 7,
            "zero_carry_search": [44, 80],
        },
        "counters": counters,
        "zero_carry_pairs": zero_pairs,
        "samples": samples,
        "transcript_sha256": digest.hexdigest(),
    }


def stable_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write-results", type=Path)
    group.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    rendered = stable_json(payload)
    target: Path = args.write_results or args.check_results
    if args.write_results:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")
        print(f"wrote {target}")
    else:
        existing = target.read_text(encoding="utf-8")
        if existing != rendered:
            raise SystemExit(f"result mismatch: {target}")
        print(f"verified {target}")

    print(json.dumps(payload["counters"], sort_keys=True))
    print(f"transcript_sha256={payload['transcript_sha256']}")


if __name__ == "__main__":
    main()
