#!/usr/bin/env python3
"""Exact finite controls for CYCLE_IDEAL.md, not a universal cycle census.

Only Python standard-library integer arithmetic is used. All checks remain
active under python -O. Four deliberately damaged controls must be rejected.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
import hashlib
import json
from math import gcd, isqrt, lcm
from pathlib import Path
import time


def require(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % p for p in range(2, isqrt(n) + 1))


def phi(n: int) -> int:
    require(n >= 1, "positive modulus required")
    if n == 1:
        return 1
    return sum(gcd(i, n) == 1 for i in range(1, n))


def carry(word: bytes) -> int:
    result = 0
    for i, bit in enumerate(word):
        require(bit in (0, 1), "nonbinary word")
        if bit:
            result = 3 * result + (1 << i)
    return result


def primitive(word: bytes) -> bool:
    require(bool(word), "empty word")
    prefix = [0] * len(word)
    for i in range(1, len(word)):
        j = prefix[i - 1]
        while j and word[i] != word[j]:
            j = prefix[j - 1]
        if word[i] == word[j]:
            j += 1
        prefix[i] = j
    period = len(word) - prefix[-1]
    return period == len(word) or len(word) % period != 0


def digest(n: int) -> str:
    require(n >= 0, "digest expects nonnegative integer")
    return hashlib.sha256(n.to_bytes(max(1, (n.bit_length() + 7) // 8), "big")).hexdigest()


@dataclass(frozen=True)
class Certificate:
    M: int
    ell: int
    q: int
    B: int
    t: int
    a0: int
    a: int
    p: int
    k: int
    U: bytes
    V: bytes
    word: bytes
    P: int
    C: int
    D: int
    ordinary_source: int


def construct(M: int, q: int, ell: int | None = None, B: int = 1) -> Certificate:
    require(M >= 1 and gcd(M, 6) == 1 and q >= 12, "parameter domain")
    if ell is None:
        ell = 5
        while not is_prime(ell) or M % ell == 0:
            ell += 2
    require(is_prime(ell) and ell >= 5 and M % ell != 0, "bad-prime domain")
    require(B >= 1, "positive height multiplier required")
    t = lcm(phi(M), ell - 1)
    a0 = (3**q).bit_length()
    a, p = t * a0, t * q
    raw = bytes(((j + 1) * p // a - j * p // a) for j in range(a))
    # Find a cyclic 10101, then rotate it to the start.
    start = (raw + raw[:4]).find(bytes([1, 0, 1, 0, 1]))
    require(0 <= start < a, "balanced marker not found")
    U = raw[start:] + raw[:start]
    V = U[:1] + bytes([1, 0]) + U[3:]
    CU, CV = carry(U), carry(V)
    k = 1 if (CU + CV) % ell else 2
    word = U * (k * M) + V * M
    P = sum(word)
    C = carry(word)
    modulus = 1 << len(word)
    threeP = 3**P
    D = modulus - threeP
    n = (-C * pow(threeP, -1, modulus)) % modulus
    if n == 0:
        n = modulus
    return Certificate(M, ell, q, B, t, a0, a, p, k, U, V, word, P, C, D, n)


def verify_word(cert: Certificate, ordinary: bool = True) -> dict:
    w, L, P, C, D = cert.word, len(cert.word), cert.P, cert.C, cert.D
    require(sum(w) == P, "claimed odd count is false")
    require(carry(w) == C, "claimed full carry is false")
    require((1 << L) - 3**P == D, "claimed full denominator is false")
    require(D > 0 and 4 * L < 7 * P, "positive-cycle cone failed")
    require(primitive(w), "word is not primitive")
    require(D % cert.M == 0 and C % cert.M == 0, "fixed precision failed")
    require(D % cert.ell == 0 and C % cert.ell != 0, "bad prime failed")
    reduced_denominator = D // gcd(C, D)
    require(reduced_denominator % cert.ell == 0, "bad prime was cancelled")

    # Independent physical rational replay, all L rotations, common odd D.
    current = C
    minimum = C
    for bit in w:
        require(current % 2 == bit, "rational parity does not match word")
        current = (3 * current + D) // 2 if bit else current // 2
        require(current > 0, "nonpositive rational state")
        minimum = min(minimum, current)
    require(current == C, "rational cycle does not close")
    require(216 * minimum > cert.B * cert.a0 * D, "all-state height bound failed")
    require(216 * minimum > (cert.q - 1) * D, "chosen H bound failed")

    endpoint = None
    if ordinary:
        require(cert.ordinary_source > 0, "nonpositive ordinary witness")
        current = cert.ordinary_source
        for bit in w:
            require(current % 2 == bit, "ordinary witness parity mismatch")
            current = (3 * current + 1) // 2 if bit else current // 2
        endpoint = current
        require((1 << L) * endpoint == 3**P * cert.ordinary_source + C,
                "ordinary endpoint identity failed")

    return {
        "M": cert.M, "ell": cert.ell, "q": cert.q, "B": cert.B, "t": cert.t,
        "a0": cert.a0, "a": cert.a, "p": cert.p, "k": cert.k,
        "L": L, "P": P, "H_numerator": cert.q - 1, "H_denominator": 216,
        "cycle_minimum_floor": minimum // D,
        "full_carry_bits": C.bit_length(), "full_denominator_bits": D.bit_length(),
        "C_sha256_be": digest(C), "D_sha256_be": digest(D),
        "minimum_numerator_sha256_be": digest(minimum),
        "reduced_denominator_bits": reduced_denominator.bit_length(),
        "C_mod_M": C % cert.M, "D_mod_M": D % cert.M,
        "C_mod_ell": C % cert.ell, "D_mod_ell": D % cert.ell,
        "ordinary_source_bits": cert.ordinary_source.bit_length(),
        "ordinary_source_sha256_be": digest(cert.ordinary_source),
        "ordinary_endpoint_sha256_be": digest(endpoint) if endpoint is not None else None,
        "primitive_kmp": True, "rational_steps_checked": L,
        "ordinary_steps_checked": L if ordinary else 0,
    }


def verify_family(cert: Certificate) -> dict:
    M, a, p, U, V = cert.M, cert.a, cert.p, cert.U, cert.V
    require(M >= 1 and gcd(M, 6) == 1 and cert.q >= 12 and cert.B >= 1,
            "certificate parameter domain")
    require(is_prime(cert.ell) and cert.ell >= 5 and M % cert.ell != 0,
            "certificate bad-prime domain")
    require(cert.a0 == (3**cert.q).bit_length(), "a0 differs from exact bit length")
    require((1 << (cert.B * cert.a0)) < 2 * 3**(cert.B * cert.q),
            "exact heightened approximation condition failed")
    require(cert.t == lcm(phi(M), cert.ell - 1), "wrong common exponent")
    require(a == cert.t * cert.a0 and p == cert.t * cert.q, "wrong block counts")
    require(len(U) == a and len(V) == a and sum(U) == p and sum(V) == p, "block identity")
    require(U[:5] == bytes([1, 0, 1, 0, 1]) and V[:5] == bytes([1, 1, 0, 0, 1]),
            "wrong swap location")
    require(V == U[:1] + bytes([1, 0]) + U[3:], "more than one swap")
    require(carry(U) - carry(V) == 2 * 3**(p - 2), "swap carry identity")
    require(2**a % M == 1 % M and 3**p % M == 1 % M, "Euler payment M")
    require(2**a % cert.ell == 1 and 3**p % cert.ell == 1, "Fermat payment ell")
    require(cert.k in (1, 2), "selector outside two choices")
    require((cert.k * carry(U) + carry(V)) % cert.ell != 0, "selector failed")
    require(cert.word == U * (cert.k * M) + V * M, "whole word mismatch")

    # Exact discrepancy range: multiply every discrepancy by a.
    weight, low, high = 0, 0, 0
    for j, bit in enumerate(cert.word, 1):
        weight += bit
        deviation = a * weight - p * j
        low, high = min(low, deviation), max(high, deviation)
    require(low > -a and high < 2 * a and high - low < 3 * a,
            "cyclic discrepancy bound failed")
    markers = [i for i in range(len(cert.word))
               if cert.word[i] == 0 and cert.word[(i + 1) % len(cert.word)] == 0]
    require(len(markers) == M, "wrong marker count")
    gaps = [(markers[(i + 1) % M] - markers[i]) % len(cert.word)
            for i in range(M)]
    if M == 1:
        gaps = [len(cert.word)]
    require(gaps.count((cert.k * M + 1) * a) == 1, "unique long marker gap failed")
    require(all(g == a or g == (cert.k * M + 1) * a for g in gaps), "extra gap")
    require(all(not (cert.word[i] == cert.word[(i + 1) % len(cert.word)] ==
                     cert.word[(i + 2) % len(cert.word)] == 0)
                for i in range(len(cert.word))), "000 occurs")
    answer = verify_word(cert)
    answer["marker_count"] = M
    answer["long_marker_gap"] = (cert.k * M + 1) * a
    answer["scaled_discrepancy_min"] = low
    answer["scaled_discrepancy_max"] = high
    return answer


def damaged_controls() -> list[str]:
    cert = construct(5, 12)
    bad = [
        ("odd-count", replace(cert, P=cert.P + 1)),
        ("carry", replace(cert, C=cert.C + 1)),
        ("ordinary-source", replace(cert, ordinary_source=cert.ordinary_source + 1)),
    ]
    doubled = cert.word * 2
    bad.append(("nonprimitive-repeat", replace(cert, word=doubled, P=2 * cert.P,
                   C=carry(doubled), D=(1 << len(doubled)) - 3**(2 * cert.P))))
    rejected = []
    for label, damaged in bad:
        try:
            verify_word(damaged)
        except ValueError:
            rejected.append(label)
        else:
            raise ValueError("damaged control was accepted: " + label)
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    cases = [(1, 306, 306), (5, 41, 41), (25, 12, 1), (35, 12, 1)]
    result = {
        "schema": "collatz-fixed-ideal-controls/v1",
        "scope": "four exact finite constructions; arbitrary-modulus/height theorem remains written",
        "cases": [verify_family(construct(M, q, B=B)) for M, q, B in cases],
        "rejected_damaged_controls": damaged_controls(),
        "success": True,
        "seconds": round(time.monotonic() - start, 6),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
