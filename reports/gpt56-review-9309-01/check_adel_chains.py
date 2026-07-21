#!/usr/bin/env python3
"""Independent exact/finite checker for the ADEL 9309--9312 review chains.

This script intentionally imports no repository or author code.  It uses only the
Python standard library.  Finite checks are adversarial corroboration, not proofs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import random
import sys
import time
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Sequence

TARGET_COMMIT = "e5383d44cfa9fb75f7e92ff0bf031a2a6ca529a6"
REVIEWER = "gpt56-review-9309-01"
SEED = 0xADE19309


def signed_residue(a: int, modulus: int) -> int:
    """Representative in (-modulus/2, modulus/2]."""
    r = a % modulus
    return r - modulus if 2 * r > modulus else r


@lru_cache(maxsize=None)
def reciprocal_plan(K: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (modulus, (-17 * pow(64, -(K - ell), modulus)) % modulus)
        for ell in range(K)
        for modulus in (81 ** (ell + 1),)
    )


def reciprocal_q(K: int, h: int, ell: int) -> int:
    modulus, coefficient = reciprocal_plan(K)[ell]
    return (coefficient * h) % modulus


def reciprocal_prefix(K: int, h: int, L: int) -> tuple[int, ...]:
    if not (1 <= L <= K):
        raise ValueError("require 1 <= L <= K")
    qs = [reciprocal_q(K, h, ell) for ell in range(L)]
    out = [qs[0]]
    for ell in range(L - 1):
        out.append(qs[ell + 1] // (81 ** (ell + 1)))
    return tuple(out)


def encode_base81(digits: Sequence[int]) -> int:
    value = 0
    multiplier = 1
    for digit in digits:
        if not 0 <= digit < 81:
            raise AssertionError(f"not an 81-digit: {digit}")
        value += digit * multiplier
        multiplier *= 81
    return value


def low_energy_scaled(K: int, L: int, h: int) -> tuple[bool, int, int]:
    """Return E<=L/64 and E's numerator over D^2, D=81^L."""
    D = 81**L
    total = 0
    for ell in range(L):
        modulus = 81 ** (ell + 1)
        q = reciprocal_q(K, h, ell)
        distance_numerator = min(q, modulus - q)
        scaled = distance_numerator * (81 ** (L - ell - 1))
        total += scaled * scaled
    return 64 * total <= L * D * D, total, D * D


def decimal_power(base: Decimal, exponent: Decimal) -> Decimal:
    if base <= 0:
        raise ValueError("positive base required")
    return (base.ln() * exponent).exp()


def beta_eta() -> tuple[Decimal, Decimal]:
    with localcontext() as ctx:
        ctx.prec = 90
        beta = Decimal(17) * Decimal(2).sqrt() / Decimal(27)
        eta = -beta.ln() / Decimal(81).ln()
        return +beta, +eta


def triadic_log_coefficient(K: int, h: int) -> float:
    result = 0.0
    for ell in range(K):
        modulus = 81 ** (ell + 1)
        q = reciprocal_q(K, h, ell)
        c = abs(math.cos(math.pi * (q / modulus)))
        if c == 0.0:
            return -math.inf
        result += math.log(c)
    return result


@lru_cache(maxsize=None)
def dyadic_plan(K: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (modulus, (17 * pow(81 ** (ell + 1), -1, modulus)) % modulus)
        for ell in range(K)
        for modulus in (64 ** (K - ell),)
    )


def dyadic_log_coefficient(K: int, h: int) -> float:
    """Direct dyadic product, independent of triadic comparison code."""
    result = 0.0
    for modulus, coefficient in dyadic_plan(K):
        z = (coefficient * h) % modulus
        c = abs(math.cos(math.pi * (z / modulus)))
        if c == 0.0:
            return -math.inf
        result += math.log(c)
    return result


def exp_or_zero(log_value: float) -> float:
    return 0.0 if log_value < -745.0 else math.exp(log_value)


def pi_ratio_power64(h: int, K: int) -> float:
    exponent = math.log(math.pi) + math.log(abs(h)) - K * math.log(64.0)
    return 0.0 if exponent < -745.0 else math.exp(exponent)



@dataclass(frozen=True)
class CarryChain:
    M: int
    N: int
    c: int
    K: int
    h: int
    s: tuple[int, ...]
    a: tuple[int, ...]


def carry_chain(M: int, N: int, c: int, K: int, h: int) -> CarryChain:
    if not (2 <= M < N and math.gcd(M, N) == 1):
        raise ValueError("invalid coprime expanding chart")
    if c == 0 or math.gcd(c, M) != 1:
        raise ValueError("c must be a nonzero M-unit")
    if K < 1 or h == 0 or h % M == 0:
        raise ValueError("invalid primitive chain")
    s: list[int] = []
    for ell in range(K):
        modulus = N ** (ell + 1)
        inv = pow(M, -(K - ell), modulus)
        s.append(signed_residue(-c * h * inv, modulus))
    carries: list[int] = []
    for ell in range(K - 1):
        numerator = M * s[ell] - s[ell + 1]
        denominator = N ** (ell + 1)
        if numerator % denominator:
            raise AssertionError("nonintegral carry")
        carries.append(numerator // denominator)
    return CarryChain(M, N, c, K, h, tuple(s), tuple(carries))


def zero_runs(carries: Sequence[int]) -> list[tuple[int, int]]:
    runs: list[tuple[int, int]] = []
    i = 0
    while i < len(carries):
        if carries[i] != 0:
            i += 1
            continue
        start = i
        while i < len(carries) and carries[i] == 0:
            i += 1
        runs.append((start, i - start))
    return runs


def all_zero_run_lengths(carries: Sequence[int]) -> list[int]:
    """z_0,...,z_W including zero-length terminal/intermediate runs."""
    lengths: list[int] = []
    current = 0
    for a in carries:
        if a == 0:
            current += 1
        else:
            lengths.append(current)
            current = 0
    lengths.append(current)
    return lengths


def verify_carry_chain(chain: CarryChain, check_global: bool = True) -> dict[str, int | float]:
    M, N, c, K, h = chain.M, chain.N, chain.c, chain.K, chain.h
    s, carries = chain.s, chain.a

    # Exact carry-energy inequality over the common denominator N^(2K).
    energy_den = N ** (2 * K)
    energy_num = sum(
        s_ell * s_ell * (N ** (2 * (K - ell - 1)))
        for ell, s_ell in enumerate(s)
    )
    W = sum(a != 0 for a in carries)
    sum_a2 = sum(a * a for a in carries)
    if W > sum_a2:
        raise AssertionError("W <= sum a^2 failed")
    if sum_a2 * energy_den > 2 * (M * M + N * N) * energy_num:
        raise AssertionError("carry-energy inequality failed")

    longest = 0
    for ell, r in zero_runs(carries):
        longest = max(longest, r)
        if ell + r >= K:
            raise AssertionError("zero-run endpoint convention failed")
        t = K - ell - r
        if t < 1:
            raise AssertionError("terminal phase length is not positive")
        if s[ell + r] != (M**r) * s[ell]:
            raise AssertionError("zero-run recurrence failed")
        Z = (M ** (K - ell)) * s[ell] + c * h
        modulus = N ** (ell + r + 1)
        if Z == 0:
            raise AssertionError("primitive numerator produced Z=0")
        if Z % modulus:
            raise AssertionError("completion modulus failed")
        if 2 * (N**r) > (M ** (r + t)) + 2 * abs(c * h):
            raise AssertionError("exact height squeeze failed")
        if N**r > 2 * abs(c * h) and not (N**r < M ** (r + t)):
            raise AssertionError("criticality branch failed")

    # Check each zero run, including zero-length separators, against the theorem's
    # right-to-left terminal convention.
    run_lengths = all_zero_run_lengths(carries)
    if len(run_lengths) != W + 1:
        raise AssertionError("run decomposition count failed")
    if sum(run_lengths) + W != K - 1:
        raise AssertionError("run decomposition length failed")

    # Directly reconstruct the t_i values used in the proof for every case.
    starts: list[int] = []
    position = 0
    for idx, r in enumerate(run_lengths):
        starts.append(position)
        position += r
        if idx < W:
            position += 1
    t_values = [K - starts[i] - run_lengths[i] for i in range(W + 1)]
    if t_values[-1] != 1:
        raise AssertionError("terminal t_W != 1")
    for i in range(W):
        if t_values[i] != t_values[i + 1] + run_lengths[i + 1] + 1:
            raise AssertionError("right-to-left indexing recurrence failed")

    if check_global:
        with localcontext() as ctx:
            ctx.prec = 100
            dM, dN = Decimal(M), Decimal(N)
            kappa = dM.ln() / (dN.ln() - dM.ln())
            C_h = Decimal(2 * abs(c * h)).ln() / dN.ln()
            A = Decimal(1) + kappa
            B = Decimal(1) + (C_h + Decimal(1)) / kappa
            for i, r in enumerate(run_lengths):
                if Decimal(r) > kappa * Decimal(t_values[i]) + C_h + Decimal("1e-80"):
                    raise AssertionError("zero-run logarithmic bound failed")

            rhs_K = B * (A ** (W + 1))
            if Decimal(K) > rhs_K + Decimal("1e-75"):
                raise AssertionError("global chaining bound failed")
            lower_W = max(
                Decimal(0),
                (Decimal(K) / B).ln() / A.ln() - Decimal(1),
            ) if Decimal(K) > B else Decimal(0)
            if Decimal(W) + Decimal("1e-75") < lower_W:
                raise AssertionError("nonzero-carry lower bound failed")
            energy_decimal = Decimal(energy_num) / Decimal(energy_den)
            lower_E = lower_W / (Decimal(2) * Decimal(M * M + N * N))
            if energy_decimal + Decimal("1e-75") < lower_E:
                raise AssertionError("logarithmic energy lower bound failed")

    return {
        "K": K,
        "W": W,
        "longest_zero_run": longest,
        "max_abs_carry": max((abs(a) for a in carries), default=0),
    }


def primitive_log_bound_64_81(K: int, h: int) -> float:
    if h == 0 or h % 64 == 0:
        raise ValueError("primitive h required")
    kappa = math.log(64.0) / math.log(81.0 / 64.0)
    A = 1.0 + kappa
    Cstar = 2.0 * (64.0**2 + 81.0**2)
    C_h = math.log(34.0 * abs(h), 81.0)
    B_h = 1.0 + (C_h + 1.0) / kappa
    active = max(0.0, math.log(K / B_h) / math.log(A) - 1.0) if K > 0 else 0.0
    return -(2.0 / Cstar) * active


def make_h_samples(K: int, rng: random.Random, count: int) -> list[int]:
    bound = max(2, int(math.exp(math.sqrt(K))))
    fixed = {
        1, 2, 3, 5, 17, 31, 63, 65, 127, 257,
        K * K + 1, K**3 + 17, bound - 1, bound,
    }
    samples = set()
    for h in fixed:
        if h > 0:
            samples.add(h)
            samples.add(-h)
    for _ in range(count):
        h = rng.randrange(1, bound + 1)
        samples.add(h)
        samples.add(-h)
    return sorted(samples)


def check_l9309(full: bool) -> dict[str, object]:
    exhaustive_K = [1, 2, 3] if full else [1, 2]
    tuples_checked = 0
    for K in exhaustive_K:
        size = 81**K
        seen = bytearray(size)
        for h in range(size):
            prefix = reciprocal_prefix(K, h, K)
            code = encode_base81(prefix)
            if seen[code]:
                raise AssertionError(f"L-9309 collision at K={K}")
            seen[code] = 1
            tuples_checked += 1
            qs = [reciprocal_q(K, h, ell) for ell in range(K)]
            for ell in range(K - 1):
                base = 81 ** (ell + 1)
                d = qs[ell + 1] // base
                expected = (64 * qs[ell]) % base + d * base
                if qs[ell + 1] != expected:
                    raise AssertionError("lift recurrence failed")
                lhs = Fraction(qs[ell + 1], 81 ** (ell + 2))
                rhs = (Fraction((64 * qs[ell]) % base, base) + d) / 81
                if lhs != rhs:
                    raise AssertionError("normalized recurrence failed")
        if not all(seen):
            raise AssertionError(f"L-9309 not surjective at K={K}")

    rng = random.Random(SEED ^ 0x9309)
    random_checks = 3000 if full else 500
    for _ in range(random_checks):
        K = rng.randint(1, 80)
        L = rng.randint(1, K)
        h = rng.randrange(-(10**100), 10**100)
        delta = rng.randrange(-(10**80), 10**80)
        modulus = 81**L
        if reciprocal_prefix(K, h, L) != reciprocal_prefix(K, h % modulus, L):
            raise AssertionError("prefix does not depend only on h mod 81^L")
        for ell in {0, L - 1, K - 1}:
            if 0 <= ell < K:
                m = 81 ** (ell + 1)
                lhs = reciprocal_q(K, h + delta, ell) - reciprocal_q(K, h, ell)
                rhs = -17 * delta * pow(64, -(K - ell), m)
                if (lhs - rhs) % m:
                    raise AssertionError("perturbation law failed")
    return {
        "verdict": "no finite counterexample",
        "exhaustive_K": exhaustive_K,
        "tuples_checked": tuples_checked,
        "random_large_signed_checks": random_checks,
        "max_random_K": 80,
        "random_integer_digits": 100,
    }


def count_low_energy(K: int, L: int, start: int, H: int) -> int:
    return sum(low_energy_scaled(K, L, h)[0] for h in range(start, start + H))


def check_t9307(full: bool) -> dict[str, object]:
    beta, eta = beta_eta()
    complete_cases: list[dict[str, object]] = []
    max_L = 3 if full else 2
    starts_by_L = {
        1: [0, -10**30 + 7, 10**30 + 19],
        2: [0, -10**24 + 123, 10**24 + 911],
        3: [-10**18 + 2027],
    }
    with localcontext() as ctx:
        ctx.prec = 90
        for L in range(1, max_L + 1):
            K = L + 7
            block = 81**L
            bound = (Decimal(81) ** L) * (beta ** L)
            for start in starts_by_L[L]:
                count = count_low_energy(K, L, start, block)
                if Decimal(count) > bound:
                    raise AssertionError("complete-block entropy bound failed")
                complete_cases.append({
                    "K": K,
                    "L": L,
                    "start": str(start),
                    "H": block,
                    "count": count,
                    "bound": str(+bound),
                })

        arbitrary_specs = [
            (12, -10**21 + 17, 81),
            (20, 10**20 + 3, 500),
            (20, -10**19 + 51, 6560),
            (20, 10**18 + 5, 6561),
            (24, -10**17 + 71, 10_000),
        ]
        if full:
            arbitrary_specs.extend([
                (30, 10**16 + 12345, 100_000),
                (30, -10**15 + 76543, 600_000),
            ])
        arbitrary_cases: list[dict[str, object]] = []
        for K, start, H in arbitrary_specs:
            L = int(math.log(H, 81))
            while 81 ** (L + 1) <= H:
                L += 1
            while 81**L > H:
                L -= 1
            if L > K:
                raise AssertionError("bad test specification")
            count = count_low_energy(K, L, start, H)
            exponent = Decimal(1) - eta
            bound = Decimal(81) * decimal_power(Decimal(H), exponent)
            if Decimal(count) > bound:
                raise AssertionError("arbitrary-interval entropy bound failed")
            arbitrary_cases.append({
                "K": K,
                "L": L,
                "start": str(start),
                "H": H,
                "count": count,
                "bound": str(+bound),
            })

    # Check the Fourier implication directly on nonexceptional samples.
    rng = random.Random(SEED ^ 0x9307)
    fourier_checks = 0
    for _ in range(500 if full else 100):
        K = rng.randint(3, 80)
        L = rng.randint(1, K)
        h = rng.randrange(-(10**60), 10**60)
        low, _, _ = low_energy_scaled(K, L, h)
        if not low:
            log_prefix = 0.0
            for ell in range(L):
                m = 81 ** (ell + 1)
                q = reciprocal_q(K, h, ell)
                c = abs(math.cos(math.pi * (q / m)))
                log_prefix += math.log(c)
            if log_prefix > -L / 32.0 + 1e-12:
                raise AssertionError("T-9307 Fourier corollary failed")
            fourier_checks += 1
    return {
        "verdict": "no finite counterexample",
        "beta": str(beta),
        "eta": str(eta),
        "complete_cases": complete_cases,
        "arbitrary_translated_cases": arbitrary_cases,
        "nonexceptional_fourier_checks": fourier_checks,
        "largest_interval": max(c["H"] for c in arbitrary_cases),
    }


def check_l9310(full: bool) -> dict[str, object]:
    cases = 0
    longest = 0
    max_K = 0
    max_abs_h_digits = 0

    # Exhaustive small general coprime charts, including even N and signed c,h.
    max_M = 7 if full else 6
    max_N = 10 if full else 9
    max_K_small = 10 if full else 8
    h_lim = 16 if full else 12
    for M in range(2, max_M + 1):
        for N in range(M + 1, max_N + 1):
            if math.gcd(M, N) != 1:
                continue
            for c in range(-5, 6):
                if c == 0 or math.gcd(c, M) != 1:
                    continue
                for h in range(-h_lim, h_lim + 1):
                    if h == 0 or h % M == 0:
                        continue
                    for K in range(1, max_K_small + 1):
                        stats = verify_carry_chain(
                            carry_chain(M, N, c, K, h),
                            check_global=(K == max_K_small or (abs(h) <= 2 and c > 0)),
                        )
                        cases += 1
                        longest = max(longest, int(stats["longest_zero_run"]))
                        max_K = max(max_K, K)
                        max_abs_h_digits = max(max_abs_h_digits, len(str(abs(h))))

    # Random large general charts and huge signed numerators.
    rng = random.Random(SEED ^ 0x9310)
    random_cases = 900 if full else 600
    for _ in range(random_cases):
        M = rng.randint(2, 180)
        Ns = [N for N in range(M + 1, min(300, M + 80)) if math.gcd(M, N) == 1]
        N = rng.choice(Ns)
        while True:
            c = rng.randint(-10_000, 10_000)
            if c and math.gcd(c, M) == 1:
                break
        digits = rng.randint(1, 70)
        h = rng.randrange(10 ** (digits - 1), 10**digits)
        if rng.randrange(2):
            h = -h
        while h % M == 0:
            h += 1
        K = rng.randint(1, 220)
        stats = verify_carry_chain(carry_chain(M, N, c, K, h))
        cases += 1
        longest = max(longest, int(stats["longest_zero_run"]))
        max_K = max(max_K, K)
        max_abs_h_digits = max(max_abs_h_digits, len(str(abs(h))))

    # Special 64->81 tests beyond the author's K<=80, h<=K^2 scan.
    special_depths = [81, 127, 191, 257, 383, 512] if full else [81, 127]
    special_hs = [
        1, -1, 63, -63, 65, -65, 10**40 + 7, -(10**50 + 31),
    ]
    for K in special_depths:
        special_hs_K = special_hs + [K**5 + 17, -(K**7 + 29), int(math.exp(math.sqrt(K))) + 1]
        for h in special_hs_K:
            while h % 64 == 0:
                h += 1
            stats = verify_carry_chain(carry_chain(64, 81, 17, K, h))
            cases += 1
            longest = max(longest, int(stats["longest_zero_run"]))
            max_K = max(max_K, K)
            max_abs_h_digits = max(max_abs_h_digits, len(str(abs(h))))

    return {
        "verdict": "no finite counterexample",
        "chains_checked": cases,
        "general_chart_M_max": max_M,
        "general_chart_N_max": max_N,
        "random_general_cases": random_cases,
        "max_K": max_K,
        "max_abs_h_decimal_digits": max_abs_h_digits,
        "longest_zero_run_seen": longest,
        "special_depths": special_depths,
    }


def check_t9311(full: bool) -> dict[str, object]:
    rng = random.Random(SEED ^ 0x9311)
    primitive_checks = 0
    arbitrary_checks = 0
    self_similarity_checks = 0
    max_K = 0
    max_h_digits = 0

    depths = [32, 64, 81, 96, 128, 160, 224, 320] if full else [32, 81, 128]
    for K in depths:
        for h in make_h_samples(K, rng, 30 if full else 8):
            if h % 64 != 0:
                log_f3 = triadic_log_coefficient(K, h)
                log_bound = primitive_log_bound_64_81(K, h)
                if log_f3 > log_bound + 2e-12:
                    raise AssertionError("primitive T-9311 triadic bound failed")
                log_f2 = dyadic_log_coefficient(K, h)
                f2 = exp_or_zero(log_f2)
                bound = math.exp(log_bound) + pi_ratio_power64(h, K)
                if f2 > bound + 2e-12:
                    raise AssertionError("primitive T-9311 dyadic bound failed")
                primitive_checks += 1

            # Inject exact powers of 64 and verify shallower-copy reduction.
            v_max = min(8, K - 1)
            v = rng.randint(0, v_max)
            h0 = h
            while h0 % 64 == 0:
                h0 += 1 if h0 > 0 else -1
            hv = (64**v) * h0
            if abs(hv) < 64**K:
                log_full = dyadic_log_coefficient(K, hv)
                log_shallow = dyadic_log_coefficient(K - v, h0)
                f_full = exp_or_zero(log_full)
                f_shallow = exp_or_zero(log_shallow)
                if abs(f_full - f_shallow) > 2e-11 * max(1.0, f_full, f_shallow):
                    raise AssertionError("exact 64-power depth reduction failed numerically")
                log_bound0 = primitive_log_bound_64_81(K - v, h0)
                rhs = math.exp(log_bound0) + pi_ratio_power64(h0, K - v)
                if f_full > rhs + 2e-11:
                    raise AssertionError("arbitrary-numerator T-9311 bound failed")
                arbitrary_checks += 1
                self_similarity_checks += 1
            max_h_digits = max(max_h_digits, len(str(abs(h))))
        max_K = max(max_K, K)

    # Exhaustive polynomial windows beyond the author's K<=80 ceiling.
    window_depths = [96, 112] if full else [84]
    maxima: list[dict[str, object]] = []
    for K in window_depths:
        H = K * K
        max_value = 0.0
        argmax = 0
        for h in range(1, H + 1):
            value = exp_or_zero(dyadic_log_coefficient(K, h))
            if value > max_value:
                max_value = value
                argmax = h
        maxima.append({"K": K, "H": H, "max_F2": max_value, "argmax": argmax})

    return {
        "verdict": "no finite counterexample",
        "primitive_signed_checks": primitive_checks,
        "arbitrary_power64_checks": arbitrary_checks,
        "self_similarity_checks": self_similarity_checks,
        "max_K": max_K,
        "max_abs_h_decimal_digits": max_h_digits,
        "polynomial_window_maxima": maxima,
    }


def explicit_tail_constant() -> tuple[float, float, float, float]:
    beta = 17.0 * math.sqrt(2.0) / 27.0
    eta = -math.log(beta) / math.log(81.0)
    gamma = 1.0 / (32.0 * math.log(81.0))
    delta = min(eta, gamma)
    C = 81.0 / (1.0 - 2.0 ** (-eta)) + math.exp(1.0 / 32.0) / (1.0 - 2.0 ** (-gamma))
    return eta, gamma, delta, C


def check_t9308_t9312(full: bool) -> dict[str, object]:
    eta, gamma, delta, Ctail = explicit_tail_constant()
    depth_values = list(range(4, 19 if full else 14))
    e_values: list[dict[str, object]] = []
    tail_checks = 0

    for K in depth_values:
        max_h = 2**K
        f2 = [0.0] * (max_h + 1)
        f3 = [0.0] * (max_h + 1)
        E = 0.0
        for h in range(1, max_h + 1):
            f2[h] = exp_or_zero(dyadic_log_coefficient(K, h))
            f3[h] = exp_or_zero(triadic_log_coefficient(K, h))
            E += f2[h] / h
        e_values.append({"K": K, "E_K": E, "max_h": max_h})
        if K >= 7:  # 2^K >= 81
            cutoffs = {81, max(81, max_h // 8), max(81, max_h // 3), max_h}
            for M in sorted(c for c in cutoffs if c <= max_h):
                tail3 = sum(f3[h] / h for h in range(M, max_h + 1))
                rhs3 = Ctail * (M ** (-delta))
                if tail3 > rhs3 + 1e-10:
                    raise AssertionError("explicit T-9308 triadic tail bound failed")
                tail2 = sum(f2[h] / h for h in range(M, max_h + 1))
                rhs2 = rhs3 + math.pi * (2.0 ** (-5 * K))
                if tail2 > rhs2 + 1e-10:
                    raise AssertionError("explicit T-9308 dyadic tail bound failed")
                tail_checks += 1

    # Exact algebraic partition check at cutoff K for every numerically evaluated depth.
    split_checks = 0
    for item in e_values:
        K = int(item["K"])
        if K > 2**K:
            continue
        low = sum(exp_or_zero(dyadic_log_coefficient(K, h)) / h for h in range(1, min(K, 2**K + 1)))
        high = sum(exp_or_zero(dyadic_log_coefficient(K, h)) / h for h in range(K, 2**K + 1))
        reconstructed = low + high
        if abs(reconstructed - float(item["E_K"])) > 2e-10:
            raise AssertionError("T-9312 cutoff partition failed")
        split_checks += 1

    return {
        "verdict": "no finite counterexample",
        "eta": eta,
        "gamma": gamma,
        "delta": delta,
        "explicit_C_tail_used": Ctail,
        "full_frequency_depths": depth_values,
        "largest_full_frequency_h": 2 ** max(depth_values),
        "tail_checks": tail_checks,
        "split_checks": split_checks,
        "E_K_samples": e_values,
    }


def run(full: bool) -> dict[str, object]:
    started = time.time()
    checks: dict[str, object] = {}
    checks["L-9309"] = check_l9309(full)
    checks["T-9307"] = check_t9307(full)
    checks["L-9310"] = check_l9310(full)
    checks["T-9311"] = check_t9311(full)
    checks["T-9308_and_T-9312"] = check_t9308_t9312(full)
    payload: dict[str, object] = {
        "reviewer": REVIEWER,
        "model": "GPT-5.6 Pro",
        "target_commit": TARGET_COMMIT,
        "mode": "full" if full else "quick",
        "seed": SEED,
        "python": sys.version,
        "platform": platform.platform(),
        "elapsed_seconds": round(time.time() - started, 6),
        "checks": checks,
        "limitations": [
            "Finite computation corroborates but does not prove universal claims.",
            "Floating-point cosine evaluations are diagnostic only; load-bearing modular and carry assertions use exact integers/Fractions/Decimals.",
            "No author module or repository checker is imported.",
        ],
    }
    digest_payload = dict(payload)
    for volatile_key in ("elapsed_seconds", "python", "platform"):
        digest_payload.pop(volatile_key, None)
    canonical = json.dumps(digest_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    payload["semantic_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="run a reduced smoke suite")
    parser.add_argument("--output", type=Path, default=Path("independent-results.json"))
    parser.add_argument("--check-results", type=Path, help="compare semantic digest with a frozen result")
    args = parser.parse_args()
    payload = run(full=not args.quick)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "mode": payload["mode"],
        "semantic_sha256": payload["semantic_sha256"],
        "elapsed_seconds": payload["elapsed_seconds"],
        "output": str(args.output),
    }, indent=2, sort_keys=True))
    if args.check_results:
        expected = json.loads(args.check_results.read_text(encoding="utf-8"))
        if payload["semantic_sha256"] != expected.get("semantic_sha256"):
            print("semantic digest mismatch", file=sys.stderr)
            return 1
        print("frozen semantic digest reproduced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
