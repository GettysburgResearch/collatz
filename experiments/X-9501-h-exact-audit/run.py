#!/usr/bin/env python3
"""Exact finite audit for the H block system.

The script checks, over a user-selected finite word box:

* direct and recursive exact-cylinder residues agree;
* the affine endpoint formula agrees with stepwise simulation;
* every computed cylinder representative realizes every prescribed letter exactly;
* the proposed signed displacement inequality holds;
* every contracting tested cylinder descends at its least positive admissible point.

This is finite verification only. It is not a proof of any universal claim.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class AuditSummary:
    max_length: int
    max_letter: int
    words_checked: int
    contracting_words: int
    expanding_words: int
    all_zero_equalities: int
    direct_recursive_residue_checks: int
    exact_simulation_checks: int
    displacement_checks: int
    contracting_descent_checks: int
    digest_sha256: str


def e(r: int) -> int:
    return 3 * r + 2


def s(r: int) -> int:
    return 2 * r + 1


def affine_data(word: Sequence[int]) -> tuple[int, int, int]:
    """Return U,V,C with F_w(p)=(V*p+C)/U."""
    U = 1
    V = 1
    C = 0
    for r in word:
        er = e(r)
        sr = s(r)
        c = 3**sr
        C = c * C + U * 2**er
        U *= 2**er
        V *= c
    return U, V, C


def direct_alpha(word: Sequence[int]) -> int:
    """Exact 2-adic starting residue modulo 4U from the ghost sum."""
    E = sum(e(r) for r in word)
    modulus = 2 ** (E + 2)
    E_k = 0
    S_k = 0
    total = 0
    for r in word:
        E_k += e(r)
        S_k += s(r)
        total += 2**E_k * pow(3, -S_k, modulus)
        total %= modulus
    return (-total) % modulus


def recursive_alpha(word: Sequence[int]) -> int:
    """Exact starting residue from suffix recursion."""
    if not word:
        raise ValueError("word must be nonempty")
    if len(word) == 1:
        r = word[0]
        return 2 ** e(r)
    r = word[0]
    suffix = word[1:]
    suffix_E = sum(e(x) for x in suffix)
    modulus = 2 ** (e(r) + suffix_E + 2)
    a_suffix = recursive_alpha(suffix)
    return (2 ** e(r) * pow(3, -s(r), modulus) * (a_suffix - 1)) % modulus


def least_admissible(alpha: int, U: int, minimum: int = 16) -> int:
    """Least p>=minimum with p=alpha mod 4U and p=1 mod 3."""
    period_2 = 4 * U
    t = ((1 - alpha) * pow(period_2, -1, 3)) % 3
    p = alpha + period_2 * t
    period = 3 * period_2
    if p <= 0:
        p += period
    if p < minimum:
        p += ((minimum - p + period - 1) // period) * period
    return p


def exact_step(p: int, r: int) -> int:
    er = e(r)
    sr = s(r)
    modulus = 2 ** (er + 2)
    if p % modulus != 2**er:
        raise AssertionError(("bad exact 2-adic class", p, r))
    if p % 3 != 1:
        raise AssertionError(("bad mod-3 class", p, r))
    numerator = 3**sr * p
    if numerator % 2**er:
        raise AssertionError(("nonintegral step", p, r))
    q = numerator // 2**er + 1
    if q % 4 != 0 or q % 3 != 1:
        raise AssertionError(("endpoint is not an A-state", p, r, q))
    return q


def simulate(p: int, word: Sequence[int]) -> int:
    for r in word:
        p = exact_step(p, r)
    return p


def audit(max_length: int, max_letter: int) -> AuditSummary:
    words_checked = 0
    contracting_words = 0
    expanding_words = 0
    all_zero_equalities = 0
    direct_recursive_residue_checks = 0
    exact_simulation_checks = 0
    displacement_checks = 0
    contracting_descent_checks = 0
    digest = hashlib.sha256()

    for length in range(1, max_length + 1):
        for word in itertools.product(range(max_letter + 1), repeat=length):
            words_checked += 1
            U, V, C = affine_data(word)
            alpha_direct = direct_alpha(word)
            alpha_recursive = recursive_alpha(word)
            if alpha_direct != alpha_recursive:
                raise AssertionError(("residue mismatch", word, alpha_direct, alpha_recursive))
            direct_recursive_residue_checks += 1

            if alpha_direct % 4:
                raise AssertionError(("alpha not divisible by 4", word, alpha_direct))
            if (V * alpha_direct + C) % U:
                raise AssertionError(("affine endpoint nonintegral", word))
            endpoint_alpha = (V * alpha_direct + C) // U
            if endpoint_alpha % 4:
                raise AssertionError(("alpha endpoint not divisible by 4", word, endpoint_alpha))

            A = alpha_direct // 4
            Y = endpoint_alpha // 4
            D = U - V
            delta = A - Y
            if D > 0:
                contracting_words += 1
                if not (0 <= delta < D):
                    raise AssertionError(("contracting displacement failure", word, D, delta, A, Y))
                if delta == 0:
                    if any(r != 0 for r in word):
                        raise AssertionError(("unexpected equality", word))
                    all_zero_equalities += 1
            else:
                expanding_words += 1
                if not (D < delta < 0):
                    raise AssertionError(("expanding displacement failure", word, D, delta, A, Y))
            displacement_checks += 1

            p = least_admissible(alpha_direct, U)
            endpoint_sim = simulate(p, word)
            endpoint_affine = (V * p + C) // U
            if endpoint_sim != endpoint_affine:
                raise AssertionError(("simulation mismatch", word, p, endpoint_sim, endpoint_affine))
            exact_simulation_checks += 1

            if D > 0:
                if not endpoint_sim < p:
                    raise AssertionError(("tested contracting cylinder does not descend", word, p, endpoint_sim))
                contracting_descent_checks += 1

            digest.update(
                json.dumps(
                    {
                        "w": word,
                        "U": U,
                        "V": V,
                        "C": C,
                        "alpha": alpha_direct,
                        "A": A,
                        "Y": Y,
                        "D": D,
                        "delta": delta,
                        "p": p,
                        "Fp": endpoint_sim,
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            )

    return AuditSummary(
        max_length=max_length,
        max_letter=max_letter,
        words_checked=words_checked,
        contracting_words=contracting_words,
        expanding_words=expanding_words,
        all_zero_equalities=all_zero_equalities,
        direct_recursive_residue_checks=direct_recursive_residue_checks,
        exact_simulation_checks=exact_simulation_checks,
        displacement_checks=displacement_checks,
        contracting_descent_checks=contracting_descent_checks,
        digest_sha256=digest.hexdigest(),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=6)
    parser.add_argument("--max-letter", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.max_length < 1 or args.max_letter < 0:
        raise SystemExit("invalid range")

    summary = audit(args.max_length, args.max_letter)
    rendered = json.dumps(asdict(summary), indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
