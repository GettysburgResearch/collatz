#!/usr/bin/env python3
"""Independent verifier for X-8201's frozen sparse-resultant corpus.

This file intentionally does not import run.py.  It recomputes the cycle data,
chain correction, one-variable resultants, valuation certificates, caps, counters,
and transcript digest from the declared corpus, then compares them to the frozen
JSON artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Iterable, Sequence


BASES = ((1, 2), (1, 1, 1, 2, 1, 1, 4))


def ord2(n: int) -> int:
    if not n:
        raise AssertionError("zero eliminant")
    n = abs(n)
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count


def psums(seq: Sequence[int]) -> list[int]:
    total = 0
    out = [0]
    for x in seq:
        total += x
        out.append(total)
    return out


def numerator(seq: Sequence[int]) -> int:
    s = psums(seq)
    n = len(seq)
    return sum(pow(3, n - 1 - j) * pow(2, s[j]) for j in range(n))


def rotated(seq: Sequence[int], amount: int) -> tuple[int, ...]:
    amount %= len(seq)
    return tuple(seq[amount:]) + tuple(seq[:amount])


def orbit(seq: Sequence[int]) -> tuple[int, list[int], list[int]]:
    s = psums(seq)
    den = pow(2, s[-1]) - pow(3, len(seq))
    num = numerator(seq)
    assert den and num % den == 0
    start = num // den
    assert start < 0 and start & 1
    out = [start]
    x = start
    for a in seq:
        y = 3 * x + 1
        assert ord2(y) == a
        x = y // pow(2, a)
        out.append(x)
    assert x == start
    return start, out, s


def word_stream() -> Iterable[tuple[str, tuple[int, ...]]]:
    for b_index, base in enumerate(BASES, 1):
        max_rep = 5 if len(base) == 2 else 2
        for rep in range(1, max_rep + 1):
            seq = base * rep
            for shift in range(len(base)):
                yield f"cycle{b_index}-r{rep}-rot{shift}", rotated(seq, shift)


def supports(length: int) -> Iterable[tuple[int, ...]]:
    for size in range(1, min(5, length) + 1):
        for tail in itertools.combinations(range(1, length), size - 1):
            yield (0,) + tail


def height_stream(size: int) -> Iterable[tuple[int, ...]]:
    if size <= 4:
        yield from itertools.product((1, 2, 3, 4), repeat=size)
        return
    values = {
        tuple(1 for _ in range(size)),
        tuple(2 for _ in range(size)),
        tuple(1 + (j % 4) for j in range(size)),
        tuple(4 - (j % 4) for j in range(size)),
        tuple(j + 1 for j in range(size)),
        tuple(size - j for j in range(size)),
    }
    for value in sorted(values):
        yield value
    for seed in range(32):
        yield tuple(1 + ((seed * (2 * j + 1) + j * j + 3) % 9) for j in range(size))


def products(xs: Sequence[int]) -> list[int]:
    out = [1]
    for x in xs:
        out.append(out[-1] * x)
    return out


def packet(seq: Sequence[int], chosen: Sequence[int]) -> dict[str, object]:
    z0, states, s = orbit(seq)
    u, q = pow(2, s[-1]), pow(3, len(seq))
    w = [
        (-states[pos + 1]) * pow(3, len(seq) - 1 - pos) * pow(2, s[pos + 1])
        for pos in chosen
    ]
    coeff = [-w[0]] + [w[j - 1] - w[j] for j in range(1, len(w))] + [w[-1]]
    assert sum(coeff) == 0
    for j, weight in enumerate(w, 1):
        assert ord2(coeff[j]) == ord2(weight)

    rmin = pow(2, len(chosen) - 1)
    lam = []
    cap = []
    for i in range(1, len(chosen) + 1):
        li = u * sum(abs(coeff[j]) for j in range(i)) + q * sum(
            abs(coeff[j]) for j in range(i, len(chosen) + 1)
        )
        lam.append(li)
        cap.append((rmin * li + q) // (rmin * u))
    return {
        "z0": z0,
        "states": states,
        "prefix": s,
        "u": u,
        "q": q,
        "weights": w,
        "coeff": coeff,
        "lambda": lam,
        "cap": cap,
    }


def check_case(
    seq: Sequence[int],
    chosen: Sequence[int],
    data: dict[str, object],
    hs: Sequence[int],
) -> tuple[int, int, int, int]:
    xs = [pow(2, h) for h in hs]
    pp = products(xs)
    coeff = data["coeff"]
    assert isinstance(coeff, list)
    hval = sum(coeff[j] * pp[j] for j in range(len(coeff)))

    candidate = list(seq)
    for pos, h in zip(chosen, hs):
        candidate[pos] += h
    cpref = psums(candidate)
    cnum = numerator(candidate)
    cden = pow(2, cpref[-1]) - pow(3, len(candidate))
    assert cnum - int(data["z0"]) * cden == hval

    direct = sum(
        int(data["weights"][j]) * (xs[j] - 1) * pp[j]
        for j in range(len(chosen))
    )
    assert direct == hval

    hit = int(cden > 0 and hval % cden == 0)
    resultant_count = valuation_count = cap_count = 0
    u, q = int(data["u"]), int(data["q"])

    for i in range(len(xs)):
        # Regard both D and H as degree-one polynomials in xs[i].
        p_before = math.prod(xs[:i])
        after = math.prod(xs[i + 1 :])
        d1 = u * p_before * after
        d0 = -q

        h0 = sum(coeff[j] * pp[j] for j in range(i + 1))
        h1 = 0
        trail = 1
        for j in range(i + 1, len(coeff)):
            if j > i + 1:
                trail *= xs[j - 1]
            h1 += coeff[j] * p_before * trail

        resultant = d1 * h0 - d0 * h1
        assert resultant % p_before == 0
        reduced = resultant // p_before
        assert reduced == u * after * hval - (h1 // p_before) * cden
        assert (hval % cden == 0) == (reduced % cden == 0)
        resultant_count += 1

        assert ord2(reduced) == ord2(coeff[i + 1])
        valuation_count += 1

        other = math.prod(xs[:i] + xs[i + 1 :])
        assert abs(reduced) <= int(data["lambda"][i]) * other
        if hit:
            assert xs[i] <= int(data["cap"][i])
            cap_count += 1

    return resultant_count, valuation_count, cap_count, hit


def two_pulse_check(
    seq: Sequence[int],
    chosen: Sequence[int],
    data: dict[str, object],
    hs: Sequence[int],
) -> int:
    if len(chosen) != 2:
        return 0
    x, m = pow(2, hs[0]), pow(2, hs[1])
    gap = chosen[1]
    common = pow(2, seq[0]) * pow(3, len(seq) - gap - 1)
    c0, c1, c2 = data["coeff"]
    assert c0 % common == c1 % common == c2 % common == 0
    alpha, gamma, beta = -c0 // common, c1 // common, c2 // common
    expected_first = common * (
        int(data["q"]) * (beta * m + gamma) - int(data["u"]) * m * alpha
    )
    expected_second = common * (
        int(data["u"]) * (x * gamma - alpha) + beta * int(data["q"])
    )

    pp = products((x, m))
    coeff = data["coeff"]
    hval = sum(coeff[j] * pp[j] for j in range(3))
    dval = int(data["u"]) * x * m - int(data["q"])

    # Independent Bezout forms.
    first_b = c1 + c2 * m
    first_e = int(data["u"]) * m * c0 + int(data["q"]) * first_b
    second_a = c0 + c1 * x
    second_e = int(data["u"]) * second_a + int(data["q"]) * c2
    assert first_e == expected_first and second_e == expected_second
    assert first_e == int(data["u"]) * m * hval - first_b * dval
    assert second_e == int(data["u"]) * hval - c2 * dval
    return 2


def reconstruct() -> dict[str, object]:
    counts = {
        "negative_cycle_words": 0,
        "fixed_support_packets": 0,
        "pulse_instances": 0,
        "resultant_identities": 0,
        "valuation_certificates": 0,
        "cap_checks_on_divisor_hits": 0,
        "formal_positive_divisor_hits": 0,
        "two_pulse_eliminant_matches": 0,
    }
    digest = hashlib.sha256()
    samples = []
    max_bits = 0

    for name, seq in word_stream():
        counts["negative_cycle_words"] += 1
        for chosen in supports(len(seq)):
            data = packet(seq, chosen)
            counts["fixed_support_packets"] += 1
            max_bits = max(max_bits, *(int(x).bit_length() for x in data["cap"]))

            if len(samples) < 12 and (
                len(chosen) in {1, 2, 3, 5} or chosen == tuple(range(len(chosen)))
            ):
                samples.append(
                    {
                        "word": name,
                        "support": list(chosen),
                        "weights": [str(x) for x in data["weights"]],
                        "coefficients": [str(x) for x in data["coeff"]],
                        "uniform_caps": [str(x) for x in data["cap"]],
                        "coefficient_valuations": [
                            ord2(data["coeff"][j]) for j in range(1, len(data["coeff"]))
                        ],
                    }
                )

            for hs in height_stream(len(chosen)):
                rc, vc, cc, hit = check_case(seq, chosen, data, hs)
                counts["pulse_instances"] += 1
                counts["resultant_identities"] += rc
                counts["valuation_certificates"] += vc
                counts["cap_checks_on_divisor_hits"] += cc
                counts["formal_positive_divisor_hits"] += hit
                counts["two_pulse_eliminant_matches"] += two_pulse_check(
                    seq, chosen, data, hs
                )
                digest.update(name.encode("ascii"))
                digest.update(b"|")
                digest.update(",".join(str(x) for x in chosen).encode("ascii"))
                digest.update(b"|")
                digest.update(",".join(str(x) for x in hs).encode("ascii"))
                digest.update(b"\n")

    return {
        "claim": "L-8201",
        "status": "exact finite verification of the declared corpus; theorem remains PROPOSED",
        "scope": {
            "primitive_negative_cycles": [list(x) for x in BASES],
            "repetitions": {"cycle_1": [1, 5], "cycle_2": [1, 2]},
            "primitive_rotations": True,
            "maximum_support_size": 5,
            "small_height_grid": [1, 4],
            "large_support_structured_vectors": 38,
        },
        "counters": counts,
        "maximum_uniform_cap_bits": max_bits,
        "transcript_sha256": digest.hexdigest(),
        "samples": samples,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    args = parser.parse_args()
    frozen = json.loads(args.artifact.read_text(encoding="utf-8"))
    rebuilt = reconstruct()
    if rebuilt != frozen:
        raise SystemExit("independent reconstruction does not match the frozen artifact")
    print("independent reconstruction matches")
    print(json.dumps(rebuilt["counters"], sort_keys=True))
    print(f"transcript_sha256={rebuilt['transcript_sha256']}")


if __name__ == "__main__":
    main()
