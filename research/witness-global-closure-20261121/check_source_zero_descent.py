#!/usr/bin/env python3
"""Exact widened source-zero descent; no universal R decision procedure."""

from fractions import Fraction
import json


W = (1, 2, 1, 2, 3, 1, 3, 3)
V = (2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 3)
A = (1, 1, 2, 1)
PARENT_MODULUS = 69984
PARENT_RESIDUE = 50063


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(n):
    require(isinstance(n, int) and n != 0, "valuation requires a nonzero integer")
    n = abs(n)
    return (n & -n).bit_length() - 1


def correction(word):
    c = 0
    total = 0
    for a in word:
        require(isinstance(a, int) and not isinstance(a, bool) and a > 0,
                "exponents must be positive integers")
        c = 3 * c + 2 ** total
        total += a
    return len(word), total, c


def validate(n, word):
    require(isinstance(n, int) and n > 0 and n % 2 == 1,
            "witness source must be positive odd")
    original = n
    r, total, c = correction(word)
    for a in word:
        require(valuation(3 * n + 1) == a, "incorrect exact exponent")
        n = (3 * n + 1) // 2 ** a
    require(n == 1, "incomplete witness")
    require(3 ** r * original + c == 2 ** total,
            "defining witness identity failed")
    return r, total


def child_parameter(m):
    require(isinstance(m, int) and m > 0,
            "parent parameter must be a positive integer")
    require(m % PARENT_MODULUS == PARENT_RESIDUE,
            "UNRESOLVED: parent is outside the certified progression")
    numerator = 2048 * m - 277
    require(numerator % 2187 == 0, "nonintegral child parameter")
    p = numerator // 2187
    require(0 < p < m and p % 64 == 33, "child positivity, descent or residue failed")
    return p


def prefixes(m, arm):
    child_parameter(m)
    t = (81 * m + 1) // 32
    require(32 * t == 81 * m + 1, "nonintegral partial source endpoint")
    if arm == "source":
        h = valuation(t)
        return (5 + h,), W[:-1] + (3 + h,)
    if arm == "target":
        g = valuation(9 * t + 2)
        return A[:-1] + (1 + g,), V[:-1] + (3 + g,)
    raise ValueError("unknown witness arm")


def splice(m, word, arm, forward=True):
    """Copy a supplied complete tail, including an empty tail; never search."""
    p = child_parameter(m)
    old, new = prefixes(m, arm)
    multiplier = 27 if arm == "source" else 9
    input_parameter, output_parameter = m, p
    if not forward:
        old, new = new, old
        input_parameter, output_parameter = p, m
    word = tuple(word)
    validate(multiplier * input_parameter, word)
    require(len(word) >= len(old) and word[:len(old)] == old,
            "missing forced exact prefix")
    output = new + word[len(old):]
    validate(multiplier * output_parameter, output)
    sign = 1 if forward else -1
    require(len(output) - len(word) == 7 * sign, "incorrect witness length change")
    require(sum(output) - sum(word) == 11 * sign, "incorrect total exponent change")
    return output


def fixture_word(n, cap=20000):
    """A bounded producer for the small, separately reported fixtures only."""
    require(n > 0 and n % 2 == 1, "fixture start must be positive odd")
    original = n
    word = []
    for _ in range(cap):
        if n == 1:
            validate(original, word)
            return tuple(word)
        a = valuation(3 * n + 1)
        word.append(a)
        n = (3 * n + 1) // 2 ** a
    raise ValueError("fixture cap exceeded; no certificate produced")


def affine_partial_replay(start, word):
    """The last endpoint may be even; preceding endpoints must be odd."""
    slope, intercept = start
    require(slope > 0 and slope % 2 == 0 and intercept > 1 and intercept % 2,
            "invalid ordinary affine start")
    for i, a in enumerate(word):
        denominator = 2 ** a
        require((3 * slope) % denominator == 0, "nonintegral affine slope")
        require((3 * intercept + 1) % denominator == 0, "nonintegral affine intercept")
        slope = 3 * slope // denominator
        intercept = (3 * intercept + 1) // denominator
        require(slope > 0 and intercept > 1, "nonpositive affine prefix")
        if i + 1 < len(word):
            require(slope % 2 == 0 and intercept % 2 == 1,
                    "nonterminal affine endpoint is not always odd")
    return slope, intercept


def reference_replay(start, word):
    q = Fraction(start)
    for a in word:
        require(q.denominator % 2 == 1 and valuation(q.numerator) == 0,
                "reference input is not two-adically odd")
        y = 3 * q + 1
        require(y != 0 and y.denominator % 2 == 1, "zero or invalid reference numerator")
        require(valuation(y.numerator) == a, "incorrect reference valuation")
        q = y / 2 ** a
    return q


def run():
    require(correction(W) == (8, 16, 24485), "source correction failed")
    require(correction(A) == (4, 5, 73), "parent target correction failed")
    require(correction(V) == (11, 16, 351437), "target correction failed")
    require(351437 == 9 * 24485 + 2 ** 17, "matching correction identity failed")

    parent = (69984, 50063)
    child = (65536, 46881)
    require(2048 * parent[0] == 2187 * child[0], "parameter slope failed")
    require(2048 * parent[1] - 277 == 2187 * child[1], "parameter constant failed")
    require((parent[0] - child[0], parent[1] - child[1]) == (4448, 3182),
            "strict contraction coefficients failed")
    require(parent[1] % 32 == 15 and parent[1] % 2187 == 1949,
            "parent CRT residues failed")
    require(parent[0] == 32 * 2187 and child[0] % 64 == 0 and child[1] % 64 == 33,
            "whole progression residue failed")
    require(2048 * 1949 % 2187 == 277, "ternary inverse condition failed")

    old_s = affine_partial_replay((27 * parent[0], 27 * parent[1]), (5,))
    new_s = affine_partial_replay((27 * child[0], 27 * child[1]), W)
    old_t = affine_partial_replay((9 * parent[0], 9 * parent[1]), A)
    new_t = affine_partial_replay((9 * child[0], 9 * child[1]), V)
    require(old_s == new_s == (177147, 126722), "source endpoints differ")
    require(old_t == new_t == (1594323, 1140500), "target endpoints differ")
    require(old_t == (9 * old_s[0], 9 * old_s[1] + 2), "endpoint relation failed")

    require(reference_replay(Fraction(-138991, 19683), W) == Fraction(-1, 3),
            "source reference failed")
    require(reference_replay(Fraction(-138991, 59049), V) == -1,
            "target reference failed")
    require(reference_replay(Fraction(-35, 9), (5,)) == Fraction(-1, 3),
            "parent source reference failed")
    require(reference_replay(Fraction(-35, 27), A) == -1,
            "parent target reference failed")

    modulus = 3 ** 12
    period = 2 * 3 ** 11
    require(period == 354294, "exponent period failed")
    require(pow(2, period, modulus) == 1 and pow(2, period // 3, modulus) != 1,
            "ternary order data failed")
    require(pow(2, period // 2, modulus) != 1, "parity factor in order failed")
    require(pow(2, 93, 243) == 35 and pow(2, 44, 243) == 67,
            "rank-two parent classes failed")
    require(pow(2, 246009, modulus) == 35 + 243 * 1949 == 473642,
            "a5 exponent class failed")
    require(pow(2, 295532, modulus) == 67 + 243 * 1949 == 473674,
            "a6 exponent class failed")
    require(88 + 162 * 1518 == 246004 and 38 + 162 * 1824 == 295526,
            "rank-two parameter conversion failed")
    require(162 * 2187 == period, "rank-two parameter period failed")

    source_reconstructions = 0
    target_reconstructions = 0
    observed_corrections = []
    for u in range(4):
        m = parent[0] * u + parent[1]
        p = child_parameter(m)
        t = (81 * m + 1) // 32
        observed_corrections.append([valuation(t), valuation(9 * t + 2)])
        source_word = fixture_word(27 * m)
        child_target_word = fixture_word(9 * p)
        for padding in ((), (2, 2, 2)):
            supplied_source = source_word + padding
            new_source = splice(m, supplied_source, "source", True)
            require(splice(m, new_source, "source", False) == supplied_source,
                    "source round trip changed the supplied tuple")
            source_reconstructions += 2
            supplied_target = child_target_word + padding
            new_target = splice(m, supplied_target, "target", False)
            require(splice(m, new_target, "target", True) == supplied_target,
                    "target round trip changed the supplied tuple")
            target_reconstructions += 2
    require(observed_corrections[0] == [1, 2] and observed_corrections[1] == [0, 0],
            "widened and original halves not exercised")

    # Supplied rank-two certificates; neither huge target orbit is searched.
    huge_sources = []
    for a, b, constant in ((5, 246004, 35), (6, 295526, 67)):
        m = (2 ** (a + b) - constant) // 243
        require(243 * m == 2 ** (a + b) - constant, "huge parent integrality failed")
        supplied = (a, b)
        validate(27 * m, supplied)
        output = splice(m, supplied, "source", True)
        require(output == W[:-1] + (a - 2, b), "huge inherited source tail changed")
        require(validate(27 * child_parameter(m), output) == (9, a + b + 11),
                "huge child witness statistics failed")
        require(splice(m, output, "source", False) == supplied, "huge round trip failed")
        huge_sources.append({
            "source_first_exponent": a,
            "last_source_exponent": b,
            "source_odd_length": 2,
            "child_odd_length": 9,
            "child_total_exponent": a + b + 11,
            "source_bit_length": (27 * m).bit_length(),
            "target_orbit": "NOT_ATTEMPTED",
        })

    # Empty inherited source tail: t is a power of two.
    a = 46764
    require(pow(2, a, 3 ** 11) == 1 + 81 * 1949,
            "empty-source-tail modular fixture failed")
    m = (2 ** a - 1) // 81
    supplied = (a,)
    validate(27 * m, supplied)
    output = splice(m, supplied, "source", True)
    require(output == W[:-1] + (a - 2,), "empty source tail was not accepted")
    require(splice(m, output, "source", False) == supplied,
            "empty source tail round trip failed")

    # Empty inherited target tail: q is a power of two. No orbit search.
    g = 739663
    require(pow(2, g, 3 ** 13) == 1140500,
            "empty-target-tail modular fixture failed")
    u = (2 ** g - 1140500) // (3 ** 13)
    require((3 ** 13) * u + 1140500 == 2 ** g,
            "empty-target-tail integrality failed")
    m = parent[0] * u + parent[1]
    supplied = V[:-1] + (3 + g,)
    validate(9 * child_parameter(m), supplied)
    output = splice(m, supplied, "target", False)
    require(output == A[:-1] + (1 + g,), "empty target tail was not accepted")
    require(splice(m, output, "target", True) == supplied,
            "empty target tail round trip failed")

    rejected = 0
    bad_cases = [
        lambda: child_parameter(50063 + 32),
        lambda: child_parameter(-50063),
        lambda: splice(50063, (6,), "source", True),
        lambda: splice(50063, W[:-1] + (4,), "source", False),
        lambda: splice(50063, A[:-1] + (3,), "target", True),
        lambda: splice(50063, V[:-1] + (5,), "target", False),
        lambda: splice(50063, (5, 1), "source", True),
        lambda: validate(27 * 50063, (6, 0)),
        lambda: validate(27 * 50063, (6, True)),
        lambda: reference_replay(Fraction(-1, 3), (1,)),
    ]
    for case in bad_cases:
        try:
            case()
        except ValueError:
            rejected += 1
        else:
            raise ValueError("malformed, unsupported, or zero-reference input accepted")

    print(json.dumps({
        "status": "PASS",
        "universal_ordinary_prefix_schemas": 4,
        "partial_affine_divisions_checked": 24,
        "last_valuation_normalizations": 4,
        "finite_exact_reference_paths": 4,
        "complete_source_tuple_reconstructions": source_reconstructions,
        "complete_target_tuple_reconstructions": target_reconstructions,
        "small_progression_fixtures": 4,
        "observed_last_valuation_corrections": observed_corrections,
        "huge_source_only_fixtures": huge_sources,
        "empty_inherited_tail_fixtures": 2,
        "malformed_or_unsupported_inputs_rejected": rejected,
        "all_rank_two_exponents": "UNRESOLVED",
        "full_R": "UNRESOLVED",
        "evidence_limit": "Exact affine certificates, arithmetic congruences, and stated reconstruction fixtures; no universal R coverage or formal verification.",
    }, sort_keys=True))


if __name__ == "__main__":
    run()
