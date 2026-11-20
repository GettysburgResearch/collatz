#!/usr/bin/env python3
"""Independent checks for the sibling arbitrary-tail c=3 note.

No functions from the author's checker are imported. The inequality check
uses four integer induction bases, rather than the author's squared bound;
the witness checks reconstruct starts backwards; and tail residues are
selected by incremental ternary lifting, rather than a full residue census.
"""

import argparse
import hashlib
import json
from pathlib import Path


H = 176106
PINNED_FILES = {
    "C3_ARBITRARY_TAIL_DESCENT.md": "ee2cd5973d50b88af5056be3af654d1e287ff8f0a831eaa335fef04f64552c11",
    "check_c3_arbitrary_tail.py": "d11595cace6337f12304445a1920351c198a1dbed40bf76131e1bfb7245919e2",
}


def demand(condition, message):
    if not condition:
        raise ValueError(message)


def order_two(n):
    demand(n > 0, "positive valuation input required")
    return (n & -n).bit_length() - 1


def backward(word, endpoint=1):
    demand(endpoint > 0 and endpoint % 2, "odd positive endpoint required")
    n = endpoint
    for exponent in reversed(word):
        demand(isinstance(exponent, int) and exponent > 0, "bad exponent")
        numerator = (1 << exponent) * n - 1
        demand(numerator > 0 and numerator % 3 == 0, "illegal ordinary inverse")
        n = numerator // 3
        demand(n % 2 == 1, "inverse endpoint not odd")
    return n


def terminal_word(n, bound=20000):
    demand(n > 0 and n % 2 == 1, "odd positive source required")
    word = []
    while n != 1:
        demand(len(word) < bound, "bounded ordinary replay unresolved")
        numerator = 3 * n + 1
        exponent = order_two(numerator)
        word.append(exponent)
        n = numerator >> exponent
    return word


def representative(e, w):
    return 3**((e - 1)//2) * w if e % 2 else 2 * 3**(e//2) * w + 1


def difference_data(a, e):
    # D is exactly 81*3**a*(X-H*R) when w=1, including all intercepts.
    leading = 2**(a + e + 9)
    if e % 2:
        negative = 81 * H * 3**(a + (e - 1)//2)
        c0 = 687
    else:
        negative = 162 * H * 3**(a + e//2)
        c0 = 687 + 81 * H
    intercept = 2**(a + 9) - c0 * 3**a
    return leading, negative, intercept, c0


def check_integer_induction():
    bases = []
    for a in (1, 2):
        for offset in (0, 1):
            e = 3*a + 80 + offset
            leading, negative, intercept, c0 = difference_data(a, e)
            d = leading - negative + intercept
            demand(d > 0 and intercept < 0, "failed exact induction base")
            bases.append({"a": a, "e": e, "scaled_difference_at_w1": d})
    # These integer guards prove positivity of the symbolic recurrences.
    demand(2**10 < 687 * 3, "intercept base must be negative")
    demand(2 < 3, "intercept induction requires slower positive growth")
    demand(13 * 2**5 > 239, "a-increment recurrence guard failed")
    # Check the two recurrence identities independently on many parameters;
    # their proof as identities is given in the review note.
    identities = 0
    for a in range(1, 15):
        for delta in (0, 1, 2, 11):
            e = 3*a + 80 + delta
            aa, bb, cc, c0 = difference_data(a, e)
            d = aa - bb + cc
            aa2, bb2, cc2, _ = difference_data(a, e + 2)
            demand(aa2 - bb2 + cc2 == 3*d + aa - 2*cc,
                   "e-increment recurrence identity failed")
            aa3, bb3, cc3, _ = difference_data(a + 2, e + 6)
            demand(aa3 - bb3 + cc3 == 243*d + 13*aa
                   - 239*2**(a + 9) + 234*c0*3**a,
                   "a-increment recurrence identity failed")
            demand(d > 0 and aa > bb and cc < 0, "integer induction replay failed")
            identities += 2
    return bases, identities


def check_backward_splices():
    cases = 0
    parities = set()
    direct_tail = 0
    for t in range(40):
        k = 2 + 8*t
        x, y = 128*k + 1, 64*k + 1
        z = (162*k + 4)//8
        demand(z % 81 == 41, "bad c=3 sample")
        a = order_two(z + 1)
        q = (z + 1) >> a
        e = order_two(3**a * q - 1)
        w = (3**a * q - 1) >> e
        source_word = [2, 2, 2, 3] + [1]*(a - 1) + [e + 1] + terminal_word(w)
        demand(backward(source_word) == x, "source splice reconstructed another source")
        r = representative(e, w)
        suffix = terminal_word(r)
        if not suffix:
            suffix = [2]
        if e % 2:
            suffix = [suffix[0] + 2] + suffix[1:]
        target_word = [2, 2, 2, 1] + [1]*a + [2]*(e//2) + suffix
        demand(backward(target_word) == y, "target splice reconstructed another target")
        parities.add(e % 2)
        direct_tail += int(e == 1)
        cases += 1
    demand(parities == {0, 1} and direct_tail > 0, "normalization cases missing")
    return cases


def ladder_residue(r, h, length):
    divisor = 3**(r + 1)
    modulus = 3**length
    residue = pow(4, 3**r * h, divisor * modulus)
    demand((residue - 1) % divisor == 0, "residue quotient nonintegral")
    return (1 + pow(4, r + 1, modulus) * ((residue - 1)//divisor)) % modulus


def lift_tail_parameter(r, target, length):
    h, modulus = 0, 1
    for digit_position in range(length):
        next_modulus = 3 * modulus
        choices = [h + digit*modulus for digit in range(3)
                   if ladder_residue(r, h + digit*modulus, digit_position + 1)
                   == target % next_modulus]
        demand(len(choices) == 1, "ternary isometry did not give one lift")
        h, modulus = choices[0], next_modulus
    return h or modulus


def actual_source(a, e, w):
    numerator = (1 << a) * ((1 << e)*w + 1)
    demand(numerator % 3**a == 0, "nonintegral source block")
    z = numerator//3**a - 1
    demand(z > 0 and z % 81 == 41, "wrong c=3 kernel")
    demand((512*z - 175) % 81 == 0 and (256*z - 47) % 81 == 0,
           "nonintegral reverse source")
    x, y = (512*z - 175)//81, (256*z - 47)//81
    demand((x - 1) % 128 == 0, "wrong upper form")
    k = (x - 1)//128
    demand(k > 0 and k % 4 and y == 64*k + 1, "ineligible pair")
    return x, y, z


def check_nonvacuity():
    cases = 0
    ranks = set()
    for a in (1, 2):
        e = 3*a + 80
        length = a + 4
        modulus = 3**length
        target = (pow(2, -e, modulus)
                  * (42*3**a*pow(2, -a, 81) - 1)) % modulus
        demand(target % 3 != 0, "prescribed tail must be a unit")
        for r in range(5):
            h0 = lift_tail_parameter(r, target, length)
            for h in (h0, h0 + modulus):
                tail_word = [2]*r + [2 + 2*3**r*h]
                w = backward(tail_word)
                formula_w = 1 + 4**(r + 1) * ((4**(3**r*h) - 1)//3**(r + 1))
                demand(w == formula_w and w > 1, "ladder inverse identity failed")
                demand(terminal_word(w) == tail_word, "tail rank is padded rather than first-hit")
                demand(w % modulus == target, "tail misses required ternary cylinder")
                x, _, z = actual_source(a, e, w)
                demand(order_two(z + 1) == a, "a not exact in prescribed-rank source")
                demand(order_two(3**a*((z + 1) >> a) - 1) == e,
                       "e not exact in prescribed-rank source")
                demand(backward([2, 2, 2, 3] + [1]*(a - 1) + [e + 1] + tail_word) == x,
                       "prescribed-rank source splice failed")
                demand(H * representative(e, w) < x, "prescribed-rank height inequality failed")
                ranks.add(r + 1)
                cases += 1
    demand(ranks == set(range(1, 6)), "prescribed ranks missing")
    return cases


def canonical(level, w):
    demand(level >= 0 and w > 0 and w % 2, "bad canonical state")
    if level % 2:
        return 2*3**((level + 1)//2)*w + 1
    return 3**(level//2)*w


def downward_calls(e, w):
    calls = []
    for level in range(e + 25, e - 1, -1):
        j = (level + 1)//2
        demand(j >= 3, "P/Q call is below its positive-index domain")
        m = 3**(j - 3)*w
        source, target = canonical(level, w), canonical(level - 1, w)
        if level % 2 == 0:
            demand(source == 27*m and target == 54*m + 1, "not the asserted P call")
            query_upper = 256*m + 1
            kind = "P"
        else:
            demand(source == 54*m + 1 and target == 9*m, "not the asserted Q call")
            query_upper = 128*m + 1
            kind = "Q"
        demand(m > 0 and m % 2, "nonodd or nonpositive P/Q parameter")
        calls.append((kind, m, query_upper))
    demand(len(calls) == 26, "not exactly 26 calls")
    return calls


def check_exchange():
    chain_count = 0
    for e in range(5, 13):
        for w in (1, 5, 7):
            calls = downward_calls(e, w)
            demand(canonical(e - 1, w) == representative(e, w), "wrong chain endpoint")
            expected = (3**((e + 25)//2)*w if e % 2
                        else 2*3**((e + 26)//2)*w + 1)
            demand(canonical(e + 25, w) == expected, "wrong chain start")
            chain_count += 1
    rejected = []
    for e in (1, 2, 3, 4):
        try:
            downward_calls(e, 1)
        except ValueError:
            rejected.append(e)
        else:
            raise ValueError("out-of-domain resource chain was accepted")
    actual_cases = 0
    for a, e in ((4, 5), (4, 6), (5, 5), (5, 6)):
        length = a + 4
        modulus = 3**length
        target = (pow(2, -e, modulus)
                  * (42*3**a*pow(2, -a, 81) - 1)) % modulus
        h = lift_tail_parameter(0, target, length)
        tail = [2 + 2*h]
        w = backward(tail)
        x, _, _ = actual_source(a, e, w)
        demand(((1 << (e + 27))*w - 1) % 81 == 0, "exchange integrality")
        m = ((1 << (e + 27))*w - 1)//81
        xp = 256*m + 1
        old_word = [2, 2, 2, 3] + [1]*(a - 1) + [e + 1] + tail
        new_word = [2, 2, 2, e + 29] + tail
        demand(backward(old_word) == x and backward(new_word) == xp, "exchange witness identity")
        demand(len(new_word) == len(old_word) - a, "exchange rank identity")
        demand(sum(new_word) == sum(old_word) + 26 - a, "exchange exponent identity")
        demand(xp > x, "exchange has no least-value descent")
        actual_cases += 1
    return {"valid_26_call_chains": chain_count, "checked_PQ_calls": 26*chain_count,
            "rejected_low_end_exponents": rejected, "actual_exchange_cases": actual_cases}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path,
                        default=Path(__file__).resolve().parent)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    for name, expected in PINNED_FILES.items():
        demand(hashlib.sha256((args.source_dir/name).read_bytes()).hexdigest() == expected,
               "reviewed source changed: " + name)
    bases, recurrences = check_integer_induction()
    report = {"status": "PASS_SCOPED_REVIEW", "reviewed_sha256": PINNED_FILES,
              "independent_integer_induction_bases": bases,
              "bounded_recurrence_identity_replays": recurrences,
              "backward_witness_splices": check_backward_splices(),
              "prescribed_rank_source_constructions": check_nonvacuity(),
              "resource_exchange": check_exchange(),
              "scope": "The guarded arbitrary-tail reduction and nonvacuity pass; universal closure is not proved"}
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        demand(not args.output.exists(), "refusing to overwrite review evidence")
        args.output.write_text(rendered)
    print(rendered)


if __name__ == "__main__":
    main()
