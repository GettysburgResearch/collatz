#!/usr/bin/env python3
"""Exact checker for the two smaller-five comparisons in the Mersenne family.

It checks universal affine prefixes and exact induction bases, plus bounded
ordinary replays. It does not assert that any counterexample exists, and
does not promote the conditional least-failure premise to a Collatz proof.
"""

from fractions import Fraction
from pathlib import Path
import argparse
import json


H = 176106
MIN_E = 119


def need(condition, message):
    if not condition:
        raise ValueError(message)


def v2(n):
    need(n != 0, "zero has no finite valuation")
    n = abs(n)
    return (n & -n).bit_length() - 1


def shortcut(n):
    need(n > 0, "ordinary path must be positive")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def iterate(n, clock):
    for _ in range(clock):
        n = shortcut(n)
    return n


def odd_word(n, word):
    need(n > 0 and n % 2 == 1, "odd word domain")
    for exponent in word:
        numerator = 3 * n + 1
        need(v2(numerator) == exponent, "inexact odd exponent")
        n = numerator >> exponent
    return n


def affine_word(a, b, word, min_e=MIN_E):
    """Prove the odd word on a*P+b, where P is divisible by 2**min_e.

    Integrality is supplied by the stated source exponent progression. The
    parity proof is over rationals of odd denominator: the P term is more
    2-divisible than each claimed exact valuation of the intercept.
    """
    a, b = Fraction(a), Fraction(b)
    for exponent in word:
        need(b.denominator % 2 == 1 and b.numerator % 2 == 1,
             "intercept does not force an odd source")
        numerator = 3 * b + 1
        need(numerator and v2(numerator.numerator) - v2(numerator.denominator) == exponent,
             "false universal exponent")
        a_order = v2(a.numerator) - v2(a.denominator)
        need(min_e + a_order > exponent, "perturbation can change the exponent")
        a, b = 3 * a / (1 << exponent), numerator / (1 << exponent)
    need(b.denominator % 2 == 1 and b.numerator % 2 == 1,
         "prefix endpoint not uniformly odd")
    return a, b


def affine_clocks(a, b, count, min_e=MIN_E):
    a, b = Fraction(a), Fraction(b)
    parities = []
    for _ in range(count):
        need(b.denominator % 2 == 1, "nonintegral binary intercept")
        need(min_e + v2(a.numerator) - v2(a.denominator) >= 1,
             "perturbation changes specified parity")
        parity = b.numerator % 2
        parities.append(parity)
        if parity:
            a, b = 3 * a / 2, (3 * b + 1) / 2
        else:
            a, b = a / 2, b / 2
    return a, b, parities


def family(e):
    need(e >= 119 and (e - 119) % 162 == 0, "wrong Mersenne family")
    p = 1 << e
    need((1024 * p - 2573) % 243 == 0, "upper integrality")
    x = (1024 * p - 2573) // 243
    if p % 5 == 3:
        numerator, denominator = 32 * p - 61, 135
        tag = "first_valuation_four"
    else:
        need(p % 5 == 2, "wrong mod-five phase")
        numerator, denominator = 128 * p - 271, 405
        tag = "first_valuation_three"
    need(numerator % denominator == 0, "five source integrality")
    q = numerator // denominator
    need(q > 0 and q % 2 == 1 and q % 3 != 0, "five source domain")
    need(13 * q < x, "not below the common height bound")
    return p, x, q, tag


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--base-certificate", type=Path)
    args = parser.parse_args()

    # Universal, parameter-free two-adic calculations for each affine prefix.
    q4 = (Fraction(32, 135), Fraction(-61, 135))
    q3 = (Fraction(128, 405), Fraction(-271, 405))
    need(affine_word(*q4, [4, 1, 2, 1, 1, 2, 1])
         == (Fraction(81, 640), Fraction(19, 5)), "slow-cycle prefix identity")
    need(affine_word(*q3, [3, 2, 1, 4])
         == (Fraction(1, 40), Fraction(1, 5)), "fast-cycle prefix identity")
    need(affine_word(5 * q4[0], 5 * q4[1], [2, 1, 2])
         == (Fraction(1), Fraction(-1)), "first target-to-Mersenne identity")
    need(affine_word(5 * q3[0], 5 * q3[1], [2, 2, 1, 2])
         == (Fraction(1), Fraction(-1)), "second target-to-Mersenne identity")

    u4 = affine_word(*q4, [4])
    u3 = affine_word(*q3, [3])
    need(affine_clocks(5 * u4[0], 5 * u4[1], 2)[:2]
         == (Fraction(1, 2), Fraction(1)), "first successor-five identity")
    need(affine_clocks(5 * u3[0], 5 * u3[1], 5)[:2]
         == (Fraction(1, 2), Fraction(1)), "second successor-five identity")

    # The slow cycle has specified OOOEE parities for a perturbation divisible
    # by 32. The fast cycle has OEE parities for divisibility by eight.
    a, b, parities = affine_clocks(Fraction(1, 5), Fraction(19, 5), 5, min_e=5)
    need((a, b, parities) == (Fraction(27, 160), Fraction(19, 5), [1, 1, 1, 0, 0]),
         "slow cycle identity")
    a, b, parities = affine_clocks(Fraction(1, 5), Fraction(1, 5), 3, min_e=3)
    need((a, b, parities) == (Fraction(3, 40), Fraction(1, 5), [1, 0, 0]),
         "fast cycle identity")

    need(20**5 * 32**4 < 3**33, "slow-cycle uniform residual bound")
    bases = {}
    for exponent, kind in [(119, "successor_five"), (281, "fast"), (443, "slow")]:
        p, x, q, _ = family(exponent)
        if kind == "successor_five":
            left, right = H * (3**((exponent - 1)//2) + 1), x
        elif kind == "fast":
            left, right = H * 3**((exponent - 5)//3), x
        else:
            left, right = H**5 * 3**(3 * exponent), x**5
        need(left < right, f"failed universal base {kind}")
        bases[kind] = {"exponent": exponent, "left": str(left), "right": str(right)}
    # Growth guards used to propagate each exact base inequality forever.
    need(3 < 4 and 3 < 8 and 27 < 32, "wrong growth comparison")

    p, x, q, _ = family(119)
    base_path = [q]
    for _ in range(136):
        base_path.append(shortcut(base_path[-1]))
    need(base_path[-1] == 9900175581272098130203189984031, "changed base endpoint")
    need(H * base_path[-1] < x, "base ordinary prefix does not enter H2")
    base_certificate = {
        "exponent": 119, "upper": x, "five_source": q, "shortcut_clock": 136,
        "endpoint": base_path[-1], "ordinary_values": base_path,
        "required_hypothesis": "this upper is the global least reverse failure",
    }

    replays = []
    for j in range(32):
        e = 119 + 162 * j
        p, x, q, tag = family(e)
        u = odd_word(q, [4 if j % 2 == 0 else 3])
        clock = 2 if j % 2 == 0 else 5
        need(iterate(5 * u, clock) == (p >> 1) + 1, "numeric successor-five bridge")
        need(iterate((p >> 1) + 1, e - 1) == 3**((e - 1)//2) + 1,
             "numeric plus-power path")
        need(H * (3**((e - 1)//2) + 1) < x, "numeric successor-five H2 bound")
        if j % 2 == 0:
            need(160 * q == 9 * x + 23, "first exact height formula")
            need(odd_word(5*q, [2, 1, 2]) == p - 1, "first target path")
            r = odd_word(q, [4, 1, 2, 1, 1, 2, 1])
            need(r == (81 * (1 << (e - 7)) + 19)//5, "first prefix endpoint")
            m, ell = divmod(e - 7, 5)
            residual = (81 * 27**m * (1 << ell) + 19)//5
            need(iterate(r, 5*m) == residual, "numeric slow-cycle path")
            need(residual**5 < 3**(3*e), "numeric slow residual bound")
            if e != 119:
                need(H * residual < x, "numeric slow H2 bound")
            source_clock = 136 if e == 119 else 12 + 5*m
            source_endpoint = base_path[-1] if e == 119 else residual
        else:
            need(40 * q == 3 * x + 5, "second exact height formula")
            need(odd_word(5*q, [2, 2, 1, 2]) == p - 1, "second target path")
            r = odd_word(q, [3, 2, 1, 4])
            need(r == ((1 << (e - 3)) + 1)//5, "second prefix endpoint")
            m = (e - 5)//3
            residual = (4 * 3**m + 1)//5
            need(iterate(r, 3*m) == residual, "numeric fast-cycle path")
            need(residual < 3**m and H * residual < x, "numeric fast H2 bound")
            source_clock, source_endpoint = 10 + 3*m, residual
        need(iterate(q, source_clock) == source_endpoint, "complete numeric source prefix")
        replays.append({"exponent": e, "family": tag, "source_clock": source_clock,
                        "source_endpoint_bits": source_endpoint.bit_length(),
                        "upper_bits": x.bit_length()})

    report = {
        "status": "proved least-failure reduction; no full Collatz proof",
        "universal_claim": "q<X/13, q and 5U(q) are certified by the same global least-reverse floor, while 5q shares the Mersenne component",
        "universal_affine_prefixes": 6,
        "universal_rational_cycle_blocks": 2,
        "growth_comparisons": ["3<4", "3<8", "27<32"],
        "induction_bases": bases,
        "base_119_prefix": {key: value for key, value in base_certificate.items() if key != "ordinary_values"},
        "bounded_replays": replays,
        "full_collatz_proved": False,
    }
    rendered = json.dumps(report, indent=2) + "\n"
    for destination, payload in [(args.output, rendered),
                                 (args.base_certificate, json.dumps(base_certificate, indent=2) + "\n")]:
        if destination:
            need(not destination.exists(), "refusing to overwrite an evidence file")
            destination.write_text(payload)
    print(rendered)


if __name__ == "__main__":
    main()
