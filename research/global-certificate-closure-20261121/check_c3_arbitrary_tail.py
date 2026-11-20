#!/usr/bin/env python3
"""Exact finite replay for C3_ARBITRARY_TAIL_DESCENT.md.

The universal height statement is proved by the symbolic identities and
the two exact integer inequalities replayed here. Samples test the finite
witness compiler; they are not a claim of all-input coverage.
"""

from fractions import Fraction
import json


HEIGHT = 176106


def require(condition, message):
    if not condition:
        raise ValueError(message)


def v2(value):
    require(value > 0, "valuation input must be positive")
    return (value & -value).bit_length() - 1


def replay(start, word):
    require(start > 0 and start % 2, "start must be positive odd")
    value = start
    for exponent in word:
        require(isinstance(exponent, int) and exponent > 0,
                "exponent must be a positive integer")
        numerator = 3 * value + 1
        require(v2(numerator) == exponent, "inexact prescribed exponent")
        value = numerator >> exponent
        require(value > 0 and value % 2, "intermediate must be positive odd")
    return value


def verify_witness(start, word):
    require(replay(start, word) == 1, "witness did not reach 1")
    intercept = 0
    total = 0
    for exponent in word:
        intercept = 3 * intercept + (1 << total)
        total += exponent
    require(3 ** len(word) * start + intercept == 1 << total,
            "defining witness identity failed")
    return len(word), total


def finite_witness(start, limit=100000):
    value = start
    word = []
    while value != 1:
        require(len(word) < limit, "finite sample exceeded declared replay cap")
        exponent = v2(3 * value + 1)
        value = (3 * value + 1) >> exponent
        word.append(exponent)
    verify_witness(start, word)
    return word


def make_source(a, e, w):
    require(a >= 1 and e >= 1 and w > 0 and w % 2,
            "invalid block data")
    numerator = 2 ** a * (2 ** e * w + 1)
    require(numerator % 3 ** a == 0, "source block is not integral")
    z = numerator // 3 ** a - 1
    require(z > 0 and z % 81 == 41, "source is outside c=3 kernel")
    require(v2(z + 1) == a, "a is not exact")
    require(v2(3 ** a * ((z + 1) >> a) - 1) == e, "e is not exact")
    x = (512 * z - 175) // 81
    y = (256 * z - 47) // 81
    require(81 * x == 512 * z - 175, "nonintegral X")
    require(81 * y == 256 * z - 47, "nonintegral Y")
    k = (x - 1) // 128
    require(x == 128 * k + 1 and k > 0 and k % 4,
            "ineligible reverse instance")
    require(y == 64 * k + 1, "wrong adjacent target")
    require(v2(162 * k + 4) == 3, "wrong fourth valuation")
    source_prefix = [2, 2, 2, 3] + [1] * (a - 1) + [e + 1]
    require(replay(x, [2, 2, 2, 3]) == z, "source kernel prefix failed")
    require(replay(x, source_prefix) == w, "source block endpoint failed")
    require(replay(y, [2, 2, 2, 1]) == 2 * z + 1,
            "target kernel prefix failed")
    require(replay(y, [2, 2, 2, 1] + [1] * a) == 2 ** (e + 1) * w + 1,
            "target block endpoint failed")
    return x, y, z, source_prefix


def representative(e, w):
    if e % 2:
        return 3 ** ((e - 1) // 2) * w
    return 2 * 3 ** (e // 2) * w + 1


def target_witness(a, e, r, r_word):
    verify_witness(r, r_word)
    word = list(r_word)
    if not word:
        require(r == 1, "empty witness supplied for nonterminal state")
        word = [2]
    prefix = [2, 2, 2, 1] + [1] * a + [2] * (e // 2)
    if e % 2:
        word[0] += 2
    return prefix + word


def check_symbolic_height_certificate():
    require(3 ** 5 < 4 ** 4, "geometric bound failed")
    require((3 * HEIGHT) ** 2 * 243 < 2 ** 46,
            "height constant integer certificate failed")
    require(26 * 2 ** 80 > 687, "source lower bound failed")
    bound = Fraction((3 * HEIGHT) ** 2, 64) * Fraction(243, 256) * Fraction(3, 4) ** 80
    require(bound < 1, "exact squared-ratio bound failed")
    return {"squared_ratio_bound_numerator": bound.numerator,
            "squared_ratio_bound_denominator": bound.denominator}


def check_small_compiler_cases():
    count = 0
    parity = set()
    exponent_one = 0
    for k in (2, 10, 18, 26, 34, 42, 58, 74, 90, 106, 122, 138):
        x = 128 * k + 1
        z = (162 * k + 4) // 8
        a = v2(z + 1)
        q = (z + 1) >> a
        e = v2(3 ** a * q - 1)
        w = (3 ** a * q - 1) >> e
        xx, y, _, prefix = make_source(a, e, w)
        require(xx == x, "fixed source changed")
        w_word = finite_witness(w)
        verify_witness(x, prefix + w_word)
        r = representative(e, w)
        r_word = finite_witness(r)
        verify_witness(y, target_witness(a, e, r, r_word))
        parity.add(e % 2)
        exponent_one += int(e == 1)
        count += 1
    require(parity == {0, 1}, "both parity normalizations were not tested")
    require(exponent_one > 0, "direct tail case was not tested")
    return count


def eligible_exponent(a, w, minimum):
    """Choose a finite actual source; no limiting or symbolic source is used."""
    modulus = 3 ** (a + 4)
    period = 2 * 3 ** (a + 3)
    required = (-1 + 42 * 3 ** a * pow(2 ** a, -1, 81)) % modulus
    required = required * pow(w, -1, modulus) % modulus
    value = 1
    for residue in range(period):
        if value == required:
            return residue + period * max(0, (minimum - residue + period - 1) // period)
        value = (2 * value) % modulus
    raise ValueError("declared finite discrete logarithm did not exist")


def check_large_guard_cases():
    count = 0
    parity = set()
    tails = set()
    for a in (1, 2, 3, 4):
        for w in (1, 5, 7, 17):
            e = eligible_exponent(a, w, 3 * a + 80)
            x, y, _, prefix = make_source(a, e, w)
            verify_witness(x, prefix + finite_witness(w))
            r = representative(e, w)
            require(HEIGHT * r < x, "large-gap height conclusion failed")
            b_value = Fraction(2 ** (a + e) * w, 3 ** a)
            require(x > 6 * b_value, "source lower estimate failed")
            # Squared form removes irrational square roots from the replay.
            require(16 * r * r <= 81 * 3 ** e * w * w,
                    "representative upper estimate failed")
            target_prefix = [2, 2, 2, 1] + [1] * a + [2] * (e // 2)
            endpoint = replay(y, target_prefix)
            require(endpoint == (4 * r + 1 if e % 2 else r),
                    "arbitrary-tail endpoint identity failed")
            parity.add(e % 2)
            tails.add(w)
            count += 1
    require(parity == {0, 1} and len(tails - {1}) >= 2,
            "guard tests did not include both parities and nontrivial tails")
    return count


def check_resource_exchange():
    count = 0
    # The exact exponent/rank identities are independent of a sample bound.
    # These a=4 examples replay all actual integer/certificate operations;
    # the final arithmetic separately checks strict descent at every a>=27.
    for a in (4, 5, 6):
        for w in (1, 5, 7):
            e = eligible_exponent(a, w, 5)
            x, _, _, prefix = make_source(a, e, w)
            w_word = finite_witness(w)
            old_rank, old_a = verify_witness(x, prefix + w_word)
            require((2 ** (e + 27) * w - 1) % 81 == 0,
                    "resource-exchange parameter is nonintegral")
            m = (2 ** (e + 27) * w - 1) // 81
            xp = 256 * m + 1
            new_word = [2, 2, 2, e + 29] + w_word
            new_rank, new_a = verify_witness(xp, new_word)
            require(new_rank == old_rank - a, "wrong exchanged source rank")
            require(new_a == old_a + 26 - a, "wrong exchanged source exponent")
            require(xp > x, "exchange unexpectedly decreased actual value")
            old_level = e - 1
            new_level = (e + 27) - 2
            require(new_level - old_level == 26, "wrong canonical-level gap")
            count += 1
    require(26 - 27 < 0, "strict exponent descent threshold failed")
    require(pow(2, 27, 81) == 80, "ternary resource congruence failed")
    return count


def ladder_tail(r, h):
    require(r >= 0 and h >= 1, "invalid prescribed-rank tail parameters")
    power = 4 ** (3 ** r * h)
    denominator = 3 ** (r + 1)
    require((power - 1) % denominator == 0, "tail quotient is nonintegral")
    w = 1 + 4 ** (r + 1) * ((power - 1) // denominator)
    word = [2] * r + [2 + 2 * 3 ** r * h]
    require(finite_witness(w) == word, "tail does not have exact prescribed first-hit rank")
    return w, word


def tail_residue(r, h, length):
    denominator = 3 ** (r + 1)
    modulus = 3 ** length
    numerator = pow(4, 3 ** r * h, denominator * modulus) - 1
    require(numerator % denominator == 0, "modular quotient is nonintegral")
    return (1 + 4 ** (r + 1) * (numerator // denominator)) % modulus


def check_prescribed_rank_sources():
    count = 0
    ranks = set()
    parity = set()
    for a in (1, 2):
        e = 3 * a + 80
        length = a + 4
        modulus = 3 ** length
        wanted = pow(2, -e, modulus) * (3 ** a * 42 * pow(2, -a, 81) - 1) % modulus
        for r in (0, 1, 2, 3):
            residues = [tail_residue(r, h, length) for h in range(modulus)]
            require(len(set(residues)) == modulus, "tail residue map is not bijective")
            h0 = residues.index(wanted)
            h0 = h0 if h0 > 0 else modulus
            for h in (h0, h0 + modulus):
                w, word = ladder_tail(r, h)
                require(w % modulus == wanted, "chosen tail missed its residue")
                x, y, _, prefix = make_source(a, e, w)
                tail_rank, _ = verify_witness(w, word)
                require(tail_rank == r + 1, "wrong supplied tail rank")
                verify_witness(x, prefix + word)
                require(HEIGHT * representative(e, w) < x,
                        "prescribed-rank source missed the height guard")
                require(y == (x + 1) // 2, "prescribed-rank source changed target")
                ranks.add(tail_rank)
                parity.add(e % 2)
                count += 1
    require(ranks == {1, 2, 3, 4} and parity == {0, 1},
            "prescribed-rank tests missed a declared rank or exponent parity")
    return count


def main():
    integer_certificate = check_symbolic_height_certificate()
    report = {
        "status": "PASS",
        "small_complete_witness_compilations": check_small_compiler_cases(),
        "large_guard_actual_sources": check_large_guard_cases(),
        "resource_exchange_actual_sources": check_resource_exchange(),
        "prescribed_positive_tail_rank_sources": check_prescribed_rank_sources(),
        "height_constant": HEIGHT,
        "guard": "e >= 3*a + 80",
        "scope": "Exact identities and guard; full reverse criterion remains OPEN",
        **integer_certificate,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
