#!/usr/bin/env python3
"""Finite exact controls for LC1--LC4; no convergence census or imports."""
from hashlib import sha256
import json
from pathlib import Path


def need(ok, message):
    if not ok:
        raise ValueError(message)


def shortcut(n):
    need(type(n) is int and n > 0, "positive ordinary input")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def odd_step(n):
    need(n > 0 and n % 2, "positive odd input")
    value = 3 * n + 1
    gap = (value & -value).bit_length() - 1
    return value >> gap, gap


def replay(n, word, endpoint, first_hit=False):
    total = 0
    for gap in word:
        need(type(gap) is int and gap > 0, "positive exponent")
        need(not first_hit or n != 1, "earlier source first hit")
        target, actual_gap = odd_step(n)
        need(actual_gap == gap, "actual accelerated exponent")
        for _ in range(gap):
            n = shortcut(n)
            total += 1
        need(n == target and n % 2, "literal shortcut endpoint")
    need(n == endpoint, "word endpoint")
    return total


def first_hit(n):
    source, word = n, []
    for _ in range(10000):
        if n == 1:
            replay(source, word, 1, first_hit=True)
            return word
        n, exponent = odd_step(n)
        word.append(exponent)
    raise ValueError("finite fixture first-hit budget exhausted")


def recognize(word):
    # The empty source endpoint certificate at 1 maps to the empty word at 5.
    if not word:
        return []
    count = len(word)
    clock = correction = 0
    for exponent in word:
        need(type(exponent) is int and exponent > 0, "decoder exponent domain")
        correction = 3 * correction + 2 ** clock
        clock += exponent
    residual = 5 * correction
    gaps = []
    for remaining in range(count, 1, -1):
        difference = residual - 3 ** (remaining - 1)
        if difference <= 0 or difference % 2:
            return None
        exponent = (difference & -difference).bit_length() - 1
        gaps.append(exponent)
        residual = difference >> exponent
    if residual != 1 or sum(gaps) >= clock:
        return None
    return gaps + [clock - sum(gaps)]


def prefix(n, length):
    source, clock, word, odds = n, 0, [], 0
    literal = n
    for _ in range(length):
        need(literal != 1, "paired prefix precedes first hit")
        odds += literal % 2
        literal = shortcut(literal)
    need(literal % 2, "paired prefix has odd endpoint")
    while clock < length:
        n, exponent = odd_step(n)
        word.append(exponent)
        clock += exponent
    need(clock == length and n == literal and len(word) == odds, "prefix clock and odd count")
    replay(source, word, literal)
    return literal, word


def composition_control(x, length, q):
    source_endpoint, alpha = prefix(x, length)
    target_endpoint, alpha_star = prefix(5 * x, length)
    need(source_endpoint == q and target_endpoint == 5 * q, "prescribed paired endpoints")
    need(len(alpha) == len(alpha_star), "paired odd counts")
    need(recognize(alpha) == alpha_star, "prefix recognized uniquely")
    beta = first_hit(q)
    beta_target = first_hit(5 * q)
    source_word = first_hit(x)
    target_word = first_hit(5 * x)
    need(source_word == alpha + beta, "source first-hit decomposition")
    need(target_word == alpha_star + beta_target, "target first-hit decomposition")
    decoded_suffix, decoded_full = recognize(beta), recognize(source_word)
    need((decoded_suffix is None) == (decoded_full is None), "exact prefix cancellation equivalence")
    if decoded_suffix is not None:
        need(decoded_full == alpha_star + decoded_suffix, "unique concatenated decoder output")
        replay(5 * q, decoded_suffix, 5)
        replay(5 * x, decoded_full, 5)
        replay(5 * x, decoded_full + [4], 1, first_hit=True)
    return {
        "source": x,
        "source_multiple": 5 * x,
        "endpoint": q,
        "prefix_clock": length,
        "prefix_odd_count": len(alpha),
        "source_prefix": alpha,
        "target_prefix": alpha_star,
        "source_suffix_first_hit": beta,
        "target_suffix_first_hit": beta_target,
        "recognizable": decoded_full is not None,
        "source_first_hit": {"rank": len(source_word), "clock": sum(source_word)},
        "target_first_hit": {"rank": len(target_word), "clock": sum(target_word)},
        "endpoint_first_hit": {"rank": len(beta), "clock": sum(beta)},
        "endpoint_multiple_first_hit": {"rank": len(beta_target), "clock": sum(beta_target)},
    }


def small_lift(q):
    need(q > 0 and q % 2 and q % 3, "positive odd ternary-unit endpoint")
    initial = next(L for L in range(6, 12) if (2 ** L * q - 7) % 9 == 0)
    for length in (initial, initial + 6):
        x = (2 ** length * q - 7) // 9
        if x % 3:
            need(x > 0 and x % 64 == 49, "covered-ladder source class")
            need(9 * x < 2 ** 17 * q, "stated strict height bound")
            return x, length
    raise ValueError("both small lift candidates were nonunits")


def main():
    seed = composition_control(6375551795, 71, 1215835)
    need(seed["prefix_odd_count"] == 37, "published seed odd count")
    need(seed["source_prefix"][:7] == [1, 3, 3, 3, 3, 3, 3], "published initial valuation pattern")
    need(seed["source_first_hit"] == {"rank": 115, "clock": 215}, "seed source certificate")
    need(seed["target_first_hit"] == {"rank": 104, "clock": 200}, "seed target certificate")
    need(seed["endpoint_first_hit"] == {"rank": 78, "clock": 144}, "seed endpoint certificate")
    need(seed["endpoint_multiple_first_hit"] == {"rank": 67, "clock": 129}, "seed target endpoint certificate")
    need(not seed["recognizable"], "seed does not repair its endpoint")

    lifts = []
    for q in (1, 5, 7, 17, 49, 85, 113):
        x, length = small_lift(q)
        row = composition_control(x, length, q)
        need(row["source_prefix"] == [2, length - 2], "small-lift source word")
        need(row["target_prefix"] == [5, length - 5], "small-lift target word")
        lifts.append(row)
    need(lifts[0]["source_suffix_first_hit"] == [] and lifts[0]["recognizable"], "empty q=1 endpoint handled")
    need(any(row["endpoint"] > 1 and row["recognizable"] for row in lifts), "nonempty successful composition control")
    need(any(not row["recognizable"] for row in lifts), "unresolved composition controls")

    family = []
    for j in (1, 2, 3, 4, 5, 7, 8, 16, 31, 64):
        numerator = 7 * (64 ** j - 1)
        need(numerator % 9 == 0, "integral symbolic-family source")
        x = numerator // 9
        source_word = [2, 6 * j - 2, 1, 1, 2, 3, 4]
        target_word = [5, 6 * j - 5, 1, 5, 4]
        replay(x, source_word, 1, first_hit=True)
        replay(5 * x, target_word, 1, first_hit=True)
        need(x % 64 == 49 and x % 3 == j % 3, "exact binary and ternary source classes")
        need(7 * (64 ** (j + 1) - 1) // 9 == 64 * x + 49, "symbolic-family affine recurrence")
        need(recognize(source_word) is None, "symbolic-family homogeneous failure")
        row = composition_control(x, 6 * j, 7)
        need(row["source_first_hit"] == {"rank": 7, "clock": 6 * j + 11}, "symbolic source resources")
        need(row["target_first_hit"] == {"rank": 5, "clock": 6 * j + 10}, "symbolic target resources")
        family.append({"j": j, "source": x, "unit": bool(x % 3),
                       "source_word": source_word, "target_word": target_word})

    report = {
        "status": "PASS: finite exact controls for homogeneous localization LC1--LC4",
        "proof_sha256": sha256(Path(__file__).with_name("HOMOGENEOUS_LOCALIZATION.md").read_bytes()).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "comparison_source_commit": "fd991063721e9c157d318e40bb20131762f7d750",
        "decoder_source_sha256": "f2872fad5c04e3aba9219f4b54576ef438d2922d7dcad9b0a8423974c4d2c31b",
        "seed": seed,
        "small_constant_lifts": lifts,
        "explicit_infinite_family_controls": family,
        "scope": [
            "The paired-prefix cancellation theorem is proved in the note, not inferred from these fixtures.",
            "Every displayed source and target certificate is replayed through ordinary shortcut steps.",
            "Unresolved homogeneous recognition is not evidence of target nonconvergence.",
            "Different-clock or different-odd-count transports and independently certified terminal families remain available.",
            "No full Collatz claim or complete progression closure is made.",
        ],
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
