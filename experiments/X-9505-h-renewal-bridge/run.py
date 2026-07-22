#!/usr/bin/env python3
"""Exact finite audit for the H centered-renewal identities.

Checks:
* finite-code ghost boundaries are negative rational numbers;
* exact cylinder starts replay and satisfy the dual renewal bridge;
* the integral renewal-height sign law;
* no integer bridge-core plateau in a finite exponent box.

Standard library only. Finite checks do not prove universal claims.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
from dataclasses import asdict, dataclass
from fractions import Fraction
from math import floor, log
from pathlib import Path


def e(r: int) -> int:
    return 3 * r + 2


def s(r: int) -> int:
    return 2 * r + 1


def ghost_boundary(word: tuple[int, ...]) -> Fraction:
    x = Fraction(0, 1)
    for r in reversed(word):
        x = Fraction(2 ** e(r), 3 ** s(r)) * (x - 1)
    return x


def direct_alpha(word: tuple[int, ...]) -> int:
    E = sum(e(r) for r in word)
    modulus = 1 << (E + 2)
    total = 0
    E_k = 0
    S_k = 0
    for r in word:
        E_k += e(r)
        S_k += s(r)
        total = (total + (1 << E_k) * pow(3, -S_k, modulus)) % modulus
    return (-total) % modulus


def least_admissible(word: tuple[int, ...], minimum: int = 16) -> int:
    E = sum(e(r) for r in word)
    U = 1 << E
    alpha = direct_alpha(word)
    step = 4 * U
    t = ((1 - alpha) * pow(step, -1, 3)) % 3
    p = alpha + step * t
    period = 3 * step
    if p < minimum:
        p += ((minimum - p + period - 1) // period) * period
    return p


def exact_step(p: int, r: int) -> tuple[int, int]:
    er = e(r)
    if p % (1 << (er + 2)) != 1 << er or p % 3 != 1:
        raise AssertionError(("illegal", p, r))
    u = p >> er
    if u % 4 != 1:
        raise AssertionError(("bad core", p, r, u))
    q = 3 ** s(r) * u + 1
    if q % 4 or q % 3 != 1:
        raise AssertionError(("bad endpoint", p, r, q))
    return q, u


def replay(p: int, word: tuple[int, ...]) -> tuple[list[int], list[int]]:
    states = [p]
    cores: list[int] = []
    for r in word:
        p, u = exact_step(p, r)
        cores.append(u)
        states.append(p)
    return states, cores


def renewal_audit(
    states: list[int], cores: list[int], word: tuple[int, ...]
) -> tuple[int, int]:
    nonzero = [i for i, r in enumerate(word) if r > 0]
    bridge_checks = 0
    sign_checks = 0
    for z in range(len(nonzero) - 1):
        i, j = nonzero[z], nonzero[z + 1]
        R, S = word[i], word[j]
        L = j - i
        U, V = cores[i], cores[j]

        left = 9**R * U - 1
        if left % (4**L):
            raise AssertionError(("left bridge", i, j))
        W = left // (4**L)
        if 2 ** (3 * S) * V - 1 != 3**L * W:
            raise AssertionError(("right bridge", i, j))
        if W % 6 != 5:
            raise AssertionError(("bridge core class", W))

        Z = (states[i] - 4) // 4
        Z_next = (states[j] - 4) // 4
        # C > 0 iff (9/8)^R (3/4)^L > 1.
        lhs = 9**R * 3**L
        rhs = 8**R * 4**L
        if lhs == rhs:
            raise AssertionError("impossible neutral capital")
        if (Z_next > Z) != (lhs > rhs):
            raise AssertionError(("sign law", R, L, Z, Z_next))

        bridge_checks += 1
        sign_checks += 1
    return bridge_checks, sign_checks


def plateau_scan(R_max: int, a_max: int) -> tuple[int, list[tuple[int, ...]]]:
    candidates = 0
    solutions: list[tuple[int, ...]] = []
    for R in range(1, R_max + 1):
        numerator = 9**R - 8**R
        for a in range(1, a_max + 1):
            center = (R * log(9 / 8) + a * log(3)) / log(4)
            b_0 = floor(center)
            for b in range(max(1, b_0 - 2), b_0 + 5):
                denominator = 8**R * 4**b - 9**R * 3**a
                if 0 < denominator <= numerator:
                    candidates += 1
                    if numerator % denominator == 0:
                        W = numerator // denominator
                        if W % 6 == 5:
                            U_num = 3**a * W + 1
                            if (
                                U_num % (8**R) == 0
                                and 4**b * W + 1
                                == 9**R * (U_num // 8**R)
                            ):
                                solutions.append((R, a, b, W, U_num // 8**R))
    return candidates, solutions


@dataclass(frozen=True)
class Summary:
    boundary_words: int
    random_words: int
    renewal_bridges: int
    renewal_sign_checks: int
    plateau_Rmax: int
    plateau_amax: int
    plateau_candidates: int
    plateau_solutions: list[tuple[int, ...]]
    digest_sha256: str


def audit(
    max_boundary_length: int,
    max_letter: int,
    random_trials: int,
    seed: int,
    R_max: int,
    a_max: int,
) -> Summary:
    digest = hashlib.sha256()
    boundary_count = 0
    for length in range(1, max_boundary_length + 1):
        for word in itertools.product(range(max_letter + 1), repeat=length):
            value = ghost_boundary(word)
            if not value < 0:
                raise AssertionError(("boundary nonnegative", word, value))
            boundary_count += 1
            digest.update(
                f"B{word}:{value.numerator}/{value.denominator};".encode()
            )

    rng = random.Random(seed)
    bridge_checks = 0
    sign_checks = 0
    for _ in range(random_trials):
        length = rng.randint(2, 30)
        word = tuple(rng.randint(0, 10) for _ in range(length))
        p = least_admissible(word)
        states, cores = replay(p, word)
        count_1, count_2 = renewal_audit(states, cores, word)
        bridge_checks += count_1
        sign_checks += count_2
        digest.update(f"W{word}:{p}:{states[-1]};".encode())

    candidate_count, plateau_solutions = plateau_scan(R_max, a_max)
    digest.update(
        json.dumps(
            {"candidates": candidate_count, "solutions": plateau_solutions},
            sort_keys=True,
        ).encode()
    )

    return Summary(
        boundary_words=boundary_count,
        random_words=random_trials,
        renewal_bridges=bridge_checks,
        renewal_sign_checks=sign_checks,
        plateau_Rmax=R_max,
        plateau_amax=a_max,
        plateau_candidates=candidate_count,
        plateau_solutions=plateau_solutions,
        digest_sha256=digest.hexdigest(),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-boundary-length", type=int, default=6)
    parser.add_argument("--max-letter", type=int, default=5)
    parser.add_argument("--random-trials", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=9505)
    parser.add_argument("--plateau-rmax", type=int, default=300)
    parser.add_argument("--plateau-amax", type=int, default=300)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    summary = audit(
        args.max_boundary_length,
        args.max_letter,
        args.random_trials,
        args.seed,
        args.plateau_rmax,
        args.plateau_amax,
    )
    rendered = json.dumps(asdict(summary), indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
