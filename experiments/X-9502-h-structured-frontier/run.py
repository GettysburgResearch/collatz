#!/usr/bin/env python3
"""Structured exact audit for the H phase frontier.

This finite experiment checks canonical input/output ranges, the exact
fixed-point phase identity, same-sign phase closure, a critical mechanical family
of first-contracting words, a false naive fixed-point bound, and bounded-alphabet
upper candidates for the finite extremals mu_L.

Finite verification is not a proof of any universal claim.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
from dataclasses import asdict, dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


def e(r: int) -> int:
    return 3 * r + 2


def s(r: int) -> int:
    return 2 * r + 1


def data(word: tuple[int, ...]) -> tuple[int, int, int, int, int, int, int]:
    """Return normalized U,V,B,A,Y,D,Delta for one exact word."""
    U = 1
    V = 1
    B = 0
    for r in word:
        ur = 1 << e(r)
        vr = 3 ** s(r)
        br = ur >> 2
        B = vr * B + U * br
        U *= ur
        V *= vr
    A = (-B * pow(V, -1, U)) % U
    Y = (V * A + B) // U
    D = U - V
    delta = A - Y
    return U, V, B, A, Y, D, delta


def least_admissible(word: tuple[int, ...]) -> int:
    U, V, B, A, Y, D, delta = data(word)
    del V, B, Y, D, delta
    alpha = 4 * A
    period_2 = 4 * U
    t = ((1 - alpha) * pow(period_2, -1, 3)) % 3
    p = alpha + period_2 * t
    period = 3 * period_2
    if p <= 0:
        p += period
    if p < 16:
        p += ((16 - p + period - 1) // period) * period
    return p


def prefix_expanding(word: tuple[int, ...]) -> bool:
    U = 1
    V = 1
    for r in word:
        U *= 1 << e(r)
        V *= 3 ** s(r)
        if V <= U:
            return False
    return True


def critical_word(length: int, kappa: Decimal) -> tuple[int, ...]:
    """Mechanical first-contracting word at the critical slope."""
    if length < 2:
        raise ValueError("length must be at least 2")
    totals = [0]
    for k in range(1, length):
        totals.append(int(kappa * Decimal(k)) + 1)
    totals.append(int(kappa * Decimal(length)))
    return tuple(totals[i + 1] - totals[i] for i in range(length))


def concat_alignment(u: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, int]:
    U, V, B, A, Y, D, delta = data(u)
    R, W, C, Av, Yv, Dv, deltav = data(v)
    del U, B, A, D, delta, W, C, Yv, Dv, deltav
    h = ((Av - Y) * pow(V, -1, R)) % R
    j = (Y + h * V - Av) // R
    return h, j


@dataclass(frozen=True)
class Summary:
    seed: int
    random_trials: int
    random_max_length: int
    random_max_letter: int
    canonical_endpoint_checks: int
    phase_identity_checks: int
    same_sign_closure_checks: int
    critical_max_length: int
    critical_words_checked: int
    critical_displacement_failures: int
    first_naive_fixed_point_bound_failure_length: int | None
    first_naive_fixed_point_bound_ratio: str | None
    mu_max_length: int
    mu_max_letter: int
    mu_upper_candidates: list[dict]
    digest_sha256: str


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=9502)
    parser.add_argument("--random-trials", type=int, default=20_000)
    parser.add_argument("--random-max-length", type=int, default=40)
    parser.add_argument("--random-max-letter", type=int, default=10)
    parser.add_argument("--critical-max-length", type=int, default=200)
    parser.add_argument("--mu-max-length", type=int, default=5)
    parser.add_argument("--mu-max-letter", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.random_trials < 0:
        raise SystemExit("random-trials must be nonnegative")
    if args.random_max_length < 1 or args.random_max_letter < 0:
        raise SystemExit("invalid random word range")
    if args.critical_max_length < 2:
        raise SystemExit("critical-max-length must be at least 2")
    if args.mu_max_length < 1 or args.mu_max_letter < 0:
        raise SystemExit("invalid mu search range")

    rng = random.Random(args.seed)
    digest = hashlib.sha256()
    canonical_checks = 0
    phase_checks = 0
    same_sign_checks = 0

    for _ in range(args.random_trials):
        length = rng.randint(1, args.random_max_length)
        word = tuple(rng.randint(0, args.random_max_letter) for _ in range(length))
        U, V, B, A, Y, D, delta = data(word)
        if not (0 <= A < U and 0 <= Y < V):
            raise AssertionError(("canonical endpoint failure", word, U, V, A, Y))
        canonical_checks += 1

        t = Fraction(B, D)
        rho = Fraction(delta, D)
        if Fraction(A) != t + rho * U or Fraction(Y) != t + rho * V:
            raise AssertionError(("phase identity failure", word))
        phase_checks += 1

        if length >= 2:
            cut = rng.randint(1, length - 1)
            u = word[:cut]
            v = word[cut:]
            du = data(u)
            dv = data(v)
            if du[5] * dv[5] > 0:
                rho_u = Fraction(du[6], du[5])
                rho_v = Fraction(dv[6], dv[5])
                if not (0 <= rho_u < 1 and 0 <= rho_v < 1):
                    raise AssertionError(("component phase failure", u, v))
                h, j = concat_alignment(u, v)
                if not (0 <= h < dv[0] and 0 <= j < du[1]):
                    raise AssertionError(("carry rectangle failure", u, v, h, j))
                if not (0 <= rho < 1):
                    raise AssertionError(("same-sign closure failure", word, rho))
                same_sign_checks += 1

        digest.update(
            json.dumps(
                {
                    "w": word,
                    "U": U,
                    "V": V,
                    "B": B,
                    "A": A,
                    "Y": Y,
                    "D": D,
                    "delta": delta,
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        )

    getcontext().prec = 100
    kappa = (Decimal(4) / Decimal(3)).ln() / (Decimal(9) / Decimal(8)).ln()
    critical_failures = 0
    first_naive: tuple[int, Fraction, tuple[int, ...]] | None = None

    for length in range(2, args.critical_max_length + 1):
        word = critical_word(length, kappa)
        if not prefix_expanding(word[:-1]):
            raise AssertionError(("proper prefix not expanding", length, word))
        U, V, B, A, Y, D, delta = data(word)
        del V, A, Y
        if D <= 0:
            raise AssertionError(("full critical word not contracting", length, word))
        if not (0 <= delta < D):
            critical_failures += 1
        first_residue = 1 << (3 * word[0])
        ratio = Fraction(B, D * first_residue)
        if ratio > 1 and first_naive is None:
            first_naive = (length, ratio, word)
        digest.update(
            json.dumps(
                {
                    "critical_L": length,
                    "word": word,
                    "D": D,
                    "delta": delta,
                    "ratio": [ratio.numerator, ratio.denominator],
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        )

    mu_candidates: list[dict] = []
    for length in range(1, args.mu_max_length + 1):
        best_p: int | None = None
        best_word: tuple[int, ...] | None = None
        count = 0
        for word in itertools.product(range(args.mu_max_letter + 1), repeat=length):
            if not prefix_expanding(word):
                continue
            count += 1
            p = least_admissible(word)
            if best_p is None or p < best_p:
                best_p = p
                best_word = word
        result = {
            "length": length,
            "prefix_expanding_words": count,
            "best_p": best_p,
            "best_word": list(best_word) if best_word else None,
        }
        mu_candidates.append(result)
        digest.update(json.dumps(result, sort_keys=True, separators=(",", ":")).encode("utf-8"))

    summary = Summary(
        seed=args.seed,
        random_trials=args.random_trials,
        random_max_length=args.random_max_length,
        random_max_letter=args.random_max_letter,
        canonical_endpoint_checks=canonical_checks,
        phase_identity_checks=phase_checks,
        same_sign_closure_checks=same_sign_checks,
        critical_max_length=args.critical_max_length,
        critical_words_checked=args.critical_max_length - 1,
        critical_displacement_failures=critical_failures,
        first_naive_fixed_point_bound_failure_length=(first_naive[0] if first_naive else None),
        first_naive_fixed_point_bound_ratio=(str(first_naive[1]) if first_naive else None),
        mu_max_length=args.mu_max_length,
        mu_max_letter=args.mu_max_letter,
        mu_upper_candidates=mu_candidates,
        digest_sha256=digest.hexdigest(),
    )

    rendered = json.dumps(asdict(summary), indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
