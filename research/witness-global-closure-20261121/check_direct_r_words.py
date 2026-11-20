#!/usr/bin/env python3
"""Exact replay for DIRECT_R_WORDS.md; no universal R decision procedure."""

from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(n):
    require(isinstance(n, int) and n > 0, "valuation needs a positive integer")
    return (n & -n).bit_length() - 1


def validate(n, word):
    require(isinstance(n, int) and n > 0 and n % 2 == 1,
            "source must be a positive odd integer")
    original = n
    cumulative = 0
    additive = 0
    for a in word:
        require(isinstance(a, int) and not isinstance(a, bool) and a > 0,
                "every exponent must be a positive integer")
        require(valuation(3 * n + 1) == a, "incorrect exact valuation")
        additive = 3 * additive + 2 ** cumulative
        cumulative += a
        n = (3 * n + 1) // 2 ** a
    require(n == 1, "word does not end at one")
    require(3 ** len(word) * original + additive == 2 ** cumulative,
            "witness identity failed")
    return len(word), cumulative


def fixture_word(n, cap=20000):
    """Produce a finite fixture only; exceeding the cap is an explicit error."""
    require(n > 0 and n % 2 == 1, "fixture source must be positive odd")
    word = []
    current = n
    for _ in range(cap):
        if current == 1:
            validate(n, word)
            return tuple(word)
        a = valuation(3 * current + 1)
        word.append(a)
        current = (3 * current + 1) // 2 ** a
    raise ValueError("fixture orbit cap exceeded; no certificate produced")


def normal_form(a, t):
    require(a >= 1 and t > 0 and t % 2 == 1, "invalid first-letter input")
    require((2 ** a * t - 1) % 81 == 0, "missing congruence modulo 81")
    n = (2 ** a * t - 1) // 3
    require(n > 0 and n % 27 == 0, "source is not a positive multiple of 27")
    if a == 1:
        b = valuation(t + 1)
        require((t + 1) % (3 * 2 ** b) == 0, "nonintegral low-letter endpoint")
        return n, (t + 1) // (3 * 2 ** b), (b + 1,), False
    if a == 2:
        b = valuation(t + 1)
        return n, (t + 1) // 2 ** b, (1, b + 1), False
    d = a // 2
    if a % 2 == 0:
        return n, 3 ** (d - 2) * t, (1, 1) + (2,) * (d - 2), True
    return n, 2 * 3 ** (d - 1) * t + 1, (1, 1) + (2,) * (d - 1), False


def reconstruct(a, t, endpoint_word):
    n, q, prefix, jump = normal_form(a, t)
    validate(q, endpoint_word)
    tail = tuple(endpoint_word)
    if jump:
        require(q > 1 and len(tail) > 0, "missing nonempty J tail")
        tail = (tail[0] + 2,) + tail[1:]
    output = prefix + tail
    validate(n // 3, output)
    return output


def rewrite_a4(n, source_word):
    validate(n, source_word)
    require(n % 27 == 0, "source must be divisible by 27")
    require(len(source_word) >= 2 and source_word[0] == 4,
            "a4 rewrite requires a first letter four and a nonempty tail")
    result = (1, 1, source_word[1] + 2) + tuple(source_word[2:])
    validate(n // 3, result)
    return result


def rewrite_regular(n, source_word):
    validate(n, source_word)
    require(n % 27 == 0, "source must be divisible by 27")
    word = tuple(source_word)
    k = 0
    while k < len(word) and word[k] == 2:
        k += 1
    require(k < len(word), "unsupported prefix: only twos")
    if word[k] == 4:
        tail = word[k + 1:]
        prefix = (1,) + (2,) * k + (1,)
    elif word[k] == 3:
        end = k + 1
        while end < len(word) and word[end] == 1:
            end += 1
        require(end < len(word) and word[end] == 2,
                "unsupported prefix after the exponent-three block")
        ell = end - k - 1
        tail = word[end + 1:]
        prefix = (1,) + (2,) * k + (1,) * (ell + 2)
    else:
        raise ValueError("UNRESOLVED: source is outside the stated languages")
    require(len(tail) > 0, "missing nonempty tail")
    result = prefix + (tail[0] + 2,) + tail[1:]
    validate(n // 3, result)
    require(len(result) == len(word) + 1, "wrong transformed odd length")
    require(sum(result) == sum(word), "wrong transformed total exponent")
    return result


def compose(f, g):
    return f[0] * g[0], f[0] * g[1] + f[1]


def affine_identity_checks():
    f = lambda a: (Fraction(3, 2 ** a), Fraction(1, 2 ** a))
    d = (Fraction(1, 2), Fraction(1, 2))
    j = (Fraction(4), Fraction(1))
    h = (Fraction(2), Fraction(1))
    third = (Fraction(1, 3), Fraction(0))
    checks = [
        (compose(f(1), third), d),
        (compose(f(2), d), compose(d, f(2))),
        (compose(f(1), d), compose(j, f(4))),
        (compose(f(1), d), compose(h, f(3))),
        (compose(f(1), h), compose(h, f(1))),
        (compose(f(1), h), compose(j, f(2))),
    ]
    for left, right in checks:
        require(left == right, "affine schema identity failed")
    return len(checks)


def source_with_prefix(prefix):
    """Choose one ordinary fixture in the exact prefix and multiple-27 class."""
    cumulative = 0
    additive = 0
    for a in prefix:
        additive = 3 * additive + 2 ** cumulative
        cumulative += a
    modulus = 3 ** (len(prefix) + 3)
    endpoint = (additive * pow(2 ** cumulative, -1, modulus)) % modulus
    if endpoint % 2 == 0:
        endpoint += modulus
    while endpoint <= 1 or 2 ** cumulative * endpoint <= additive:
        endpoint += 2 * modulus
    n = (2 ** cumulative * endpoint - additive) // 3 ** len(prefix)
    word = tuple(prefix) + fixture_word(endpoint)
    validate(n, word)
    require(n % 27 == 0, "fixture congruence failed")
    return n, word


def run():
    affine_checks = affine_identity_checks()
    normal_count = 0
    for a in tuple(range(1, 21)) + (27, 32, 54, 60, 65, 108):
        t = pow(pow(2, a, 81), -1, 81)
        if t % 2 == 0:
            t += 81
        source_tail = fixture_word(t)
        n, q, _, _ = normal_form(a, t)
        validate(n, (a,) + source_tail)
        endpoint_word = fixture_word(q)
        output = reconstruct(a, t, endpoint_word)
        l, b = len(endpoint_word), sum(endpoint_word)
        if a == 1:
            expected = (l + 1, b + valuation(t + 1) + 1)
        elif a == 2:
            expected = (l + 2, b + valuation(t + 1) + 2)
        elif a % 2 == 0:
            expected = (l + a // 2, b + a)
        else:
            expected = (l + a // 2 + 1, b + a - 1)
        require((len(output), sum(output)) == expected,
                "normal-form length or exponent reconstruction failed")
        padded = reconstruct(a, t, endpoint_word + (2, 2))
        require(padded == output + (2, 2), "terminal padding was not preserved")
        normal_count += 1

    a4_count = 0
    for m in (31, 63, 95, 127):
        n = 27 * m
        source = fixture_word(n)
        for word in (source, source + (2, 2, 2)):
            output = rewrite_a4(n, word)
            require(len(output) == len(word) + 1 and sum(output) == sum(word),
                    "a4 reconstruction statistics failed")
            a4_count += 1

    regular_count = 0
    for k in range(7):
        n, word = source_with_prefix((2,) * k + (4,))
        rewrite_regular(n, word)
        regular_count += 1
    for k in range(5):
        for ell in range(5):
            n, word = source_with_prefix((2,) * k + (3,) + (1,) * ell + (2,))
            rewrite_regular(n, word)
            regular_count += 1

    order = next(a for a in range(1, 55) if pow(2, a, 81) == 1)
    require(order == 54, "incorrect order modulo 81")
    for k in (1, 2):
        a = 54 * k
        n, q, _, _ = normal_form(a, 1)
        validate(n, (a,))
        require(q == 3 ** (27 * k - 2), "one-letter residual failed")
        reconstruct(a, 1, fixture_word(q))

    h = Fraction(213597, 23)
    hp = Fraction(355995, 23)
    even_bound = lambda d: hp * Fraction(82, 243) * Fraction(3, 4) ** d
    odd_bound = lambda d: h * Fraction(2 * 3 ** d + 3, 2 * 4 ** d - 1)
    require(even_bound(30) < 1 and even_bound(29) > 1,
            "even first-letter threshold failed")
    require(odd_bound(32) < 1 and odd_bound(31) > 1,
            "odd first-letter threshold failed")
    require(h * Fraction(14, 27 * 2 ** 13) < 1,
            "a1 low-letter tail bound failed")
    require(h * Fraction(62, 81 * 2 ** 13) < 1,
            "a2 low-letter tail bound failed")

    rejected = 0
    cases = [
        lambda: validate(837, (4,)),
        lambda: validate(837, (4, 0)),
        lambda: validate(837, (4, True)),
        lambda: validate(838, (4,)),
        lambda: rewrite_a4(27, fixture_word(27)),
        lambda: rewrite_a4(5, (4,)),
        lambda: reconstruct(4, 1, ()),
        lambda: reconstruct(1, 41, ()),
    ]
    for case in cases:
        try:
            case()
        except ValueError:
            rejected += 1
        else:
            raise ValueError("malformed or unsupported input was accepted")

    require(rejected == len(cases), "incomplete rejection coverage")
    print(json.dumps({
        "status": "PASS",
        "affine_induction_schema_identities": affine_checks,
        "normal_form_fixtures": normal_count,
        "normal_form_padding_reconstructions": normal_count,
        "a4_complete_witness_reconstructions": a4_count,
        "regular_language_complete_witness_reconstructions": regular_count,
        "one_letter_residual_fixtures": 2,
        "exact_height_thresholds": {"even_first_letter": 60, "odd_first_letter": 65},
        "least_failure_a1_a2_tail_valuation_max": 12,
        "malformed_or_unsupported_inputs_rejected": rejected,
        "full_R": "UNRESOLVED",
        "evidence_limit": "Exact affine identities and stated finite fixtures; no all-word coverage or formal verification.",
    }, sort_keys=True))


if __name__ == "__main__":
    run()
