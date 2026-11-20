#!/usr/bin/env python3
"""Independent targeted review controls for RU1--RU3 and FD1--FD3.

No author code is imported.  Canonical words are prescribed first, then
realized by an exact inverse congruence and replayed by ordinary shortcut
steps.  This is a small adversarial fixture set, not a convergence census.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


PINS = {
    "MULTISTEP_CORE_RETURNS.md": "a1f939725bb3ffc333255fb57cafa8e95ed8dace8155650b5a608ef34ba20d5b",
    "check_multistep_core_returns.py": "c36e3180590d4cfd6215a43417c9da712ae594700527421c283df961fd3a1593",
    "multistep-core-returns-report.json": "e1eab13cea6f2d5edde5d91f8cc44fbef3bb12cd1f3e11c5d3fef3086d0cd630",
    "multistep-core-returns-report-oo.json": "e1eab13cea6f2d5edde5d91f8cc44fbef3bb12cd1f3e11c5d3fef3086d0cd630",
    "FIXED_DEFECT_CORE_RETURNS.md": "2412c6bfdcb3eeb280079235c5f04656cff49feaf091ba5421147acd1e81ba64",
    "check_fixed_defect_core_returns.py": "016695a9eefe241a952fe25af1cfaa066518ee6c24d0e66ea9eb07fe205d9093",
    "fixed-defect-core-returns-report.json": "96e259b2c3ba9ab2885b2f3961bef81f75248d6b90bb5a2896870bfea97bef52",
    "fixed-defect-core-returns-report-oo.json": "96e259b2c3ba9ab2885b2f3961bef81f75248d6b90bb5a2896870bfea97bef52",
}


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


def vp(number, prime):
    require(isinstance(number, int) and number > 0, "valuation domain")
    count = 0
    while number % prime == 0:
        count += 1
        number //= prime
    return count


def smooth_part(number, primes):
    rest = number
    for prime in primes:
        rest //= prime ** vp(rest, prime)
    return number // rest, rest


def shortcut_path(source, odd_count):
    require(type(source) is int and source > 0 and source % 2, "positive odd start")
    states, gaps = [source], []
    for _ in range(odd_count):
        # Count actual shortcut transitions, rather than evaluating U directly.
        current = (3 * states[-1] + 1) // 2
        elapsed = 1
        while current % 2 == 0:
            current //= 2
            elapsed += 1
        states.append(current)
        gaps.append(elapsed)
    return states, tuple(gaps)


def realize_word(word, lift=1):
    require(word and all(type(a) is int and a > 0 for a in word), "inverse word domain")
    # For 3^r x + B = 2^A q, choose an odd endpoint in the unique
    # permitted residue class modulo 3^r.  Reverse every individual edge.
    A = B = 0
    for exponent in word:
        B = 3 * B + 2 ** A
        A += exponent
    modulus = 3 ** len(word)
    endpoint = B * pow(2 ** A, -1, modulus) % modulus
    if endpoint % 2 == 0:
        endpoint += modulus
    endpoint += 2 * lift * modulus
    current = endpoint
    reverse = [current]
    for exponent in reversed(word):
        numerator = 2 ** exponent * current - 1
        require(numerator % 3 == 0, "each inverse division is integral")
        current = numerator // 3
        require(current > 0 and current % 2, "each inverse state is positive odd")
        reverse.append(current)
    states, actual = shortcut_path(current, len(word))
    require(actual == tuple(word) and states == reverse[::-1], "literal inverse-cylinder replay")
    return states


def subset_sums(terms):
    sums = [0]
    for term in terms:
        sums.extend([old + term for old in sums])
    return sums


def cumulative(word):
    result = [0]
    for exponent in word:
        result.append(result[-1] + exponent)
    return result


def ru_control(states, word):
    require(len(word) <= 8, "bounded exhaustive RU fixture")
    r = len(word)
    A = cumulative(word)
    terms = [3 ** r * (states[0] + 1)]
    terms.extend(3 ** (r - 1 - i) * 2 ** A[i] for i in range(1, r))
    terms.extend((2 ** A[-1], -2 ** A[-1] * (states[-1] + 1)))
    require(sum(terms) == 2 * 3 ** (r - 1), "RU shifted identity")
    sums = subset_sums(terms)
    zeros = [i for i, total in enumerate(sums) if total == 0]
    expected = [0]
    if all(a == 1 for a in word):
        expected.append(1 + 2 ** (len(terms) - 1))
    require(zeros == expected, "RU exact all-ones-only degeneracy")
    return len(sums)


def fd_control(states, word, pools):
    require(word[0] >= 2 and word[-1] >= 2, "canonical fixture")
    r = len(word)
    A = cumulative(word)
    defects = [i for i in range(1, r + 1) if word[i - 1] > 1]
    initial = 3 ** r * (states[0] + 1)
    endpoint = 2 ** A[-1] * (states[-1] + 1)
    positive = [3 ** (r - i) * 2 ** A[i] for i in defects]
    negative = [3 ** (r - i) * 2 ** (A[i - 1] + 1) for i in defects]
    terms = [initial, *positive, *(-n for n in negative), -endpoint]
    sums = subset_sums(terms)
    zeros = [i for i, total in enumerate(sums) if total == 0]
    require(zeros == [0, 2 ** len(terms) - 1], "FD all proper signed subsums are nonzero")

    # Reconstruct the homogeneous identity from the affine shifted recurrence.
    multiplier, correction = Fraction(1), Fraction(0)
    for exponent in word:
        multiplier *= Fraction(3, 2 ** exponent)
        correction = Fraction(3, 2 ** exponent) * correction + 1 - Fraction(2, 2 ** exponent)
    require(multiplier * (states[0] + 1) + correction == states[-1] + 1,
            "separately accumulated shifted affine recurrence")
    require(correction * 2 ** A[-1] == sum(positive) - sum(negative),
            "compressed corrections equal affine accumulation")

    normalization = 2 * 3 ** (r - 1)
    require(negative[0] == normalization, "canonical normalizer")
    vector_checks = 0
    for pool in pools:
        u, q = smooth_part(states[0] + 1, pool)
        v, qp = smooth_part(states[-1] + 1, pool)
        pos = [Fraction(2 ** (A[i] - 1), 3 ** (i - 1)) for i in defects]
        neg = [Fraction(2 ** A[i - 1], 3 ** (i - 1)) for i in defects[1:]]
        tail = Fraction(2 ** (A[-1] - 1) * v, 3 ** (r - 1))
        vector = [Fraction(u), *pos, *neg, tail]
        coeff = [Fraction(3 * q, 2), *([1] * len(defects)), *([-1] * (len(defects) - 1)), -qp]
        require(len(vector) == 2 * len(defects) + 1, "defect-count dimension")
        require(all(smooth_part(z.numerator, pool)[1] == 1 and
                    smooth_part(z.denominator, pool)[1] == 1 for z in vector), "fixed-prime units")
        require(sum(c * z for c, z in zip(coeff, vector)) == 1, "fixed-coefficient unit equation")
        # Recover the full ordinary path from the unit vector alone, using
        # only the fixed core q and the labeled positive coordinates.
        recovered_source = q * vector[0] - 1
        require(recovered_source.denominator == 1, "recovered integral source")
        recovered_positions, recovered_clocks = [], []
        for z in pos:
            two = vp(z.numerator, 2)
            three = vp(z.denominator, 3)
            require(z == Fraction(2 ** two, 3 ** three), "pure correction coordinate")
            recovered_positions.append(three + 1)
            recovered_clocks.append(two + 1)
        recovered_states, recovered_word = shortcut_path(int(recovered_source), recovered_positions[-1])
        require(recovered_positions == defects and recovered_clocks == [A[i] for i in defects],
                "unique positions and cumulative clocks")
        require(recovered_states == states and recovered_word == tuple(word), "full path decoded from fixed-core vector")
        vector_checks += 1
    return len(sums), vector_checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reviewed-dir", type=Path, default=Path(__file__).resolve().parent,
                        help="directory containing the eight frozen author artifacts")
    args = parser.parse_args()
    for filename, digest in PINS.items():
        require(sha256((args.reviewed_dir / filename).read_bytes()).hexdigest() == digest,
                "changed reviewed artifact: " + filename)

    # Deliberately vary defect exponents and several intervening runs.
    # The two independently lifted realizations per word avoid depending
    # on the author's small-source and special two-defect fixture family.
    words = [
        (2,), (4,), (40,), (2, 2), (2, 1, 2), (7, 1, 1, 2),
        (2,) + (1,) * 19 + (3,),
        (5,) + (1,) * 127 + (8,),
        (2,) + (1,) * 257 + (2,),
        (2,) + (1,) * 17 + (3,) + (1,) * 31 + (4,),
        (7,) + (1,) * 2 + (2,) + (1,) * 41 + (11,),
        (2, 3, 4, 5),
        (2,) + (1,) * 3 + (9,) + (1,) * 5 + (2,) + (1,) * 7 + (6,),
        (4, 1, 2, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1, 1, 5),
    ]
    pools = ((2, 3), (2, 3, 5, 11))
    canonical_count = fd_subsets = vectors = ru_subsets = shortcut_edges = 0
    fixture_rows = []
    for word in words:
        for lift in (1, 4):
            states = realize_word(word, lift)
            count, checks = fd_control(states, word, pools)
            canonical_count += 1
            fd_subsets += count
            vectors += checks
            shortcut_edges += sum(word)
            if len(word) <= 8:
                ru_subsets += ru_control(states, word)
            fixture_rows.append({"odd_length": len(word), "defects": sum(a > 1 for a in word),
                                 "max_exponent": max(word), "lift": lift,
                                 "source_bits": states[0].bit_length()})

    # RU negative controls cover different placements of a lone defect;
    # all-ones paths must retain their unique endpoint cancellation.
    ru_words = [(1,), (1, 1), (1,) * 8,
                (1, 4), (4, 1), (1, 1, 3, 1, 1), (1,) * 7 + (2,)]
    for word in ru_words:
        states = realize_word(word)
        ru_subsets += ru_control(states, word)
        shortcut_edges += sum(word)

    excursion_states, excursion_word = shortcut_path(17, 2)
    require(excursion_states == [17, 13, 5] and excursion_word == (2, 3), "outside excursion fixture")
    fd_control(excursion_states, excursion_word, pools)
    # Bound the possible end extensions by reconstructing every allowed
    # source and replaying to the same canonical segment 29 -> 11.
    # The leading extension is 19 -> 29; the terminal extension is 11 -> 17.
    states, word = shortcut_path(29, 1)
    require(states == [29, 11] and word == (3,), "two-sided extension fixture")
    fd_control(states, word, pools)
    initial_shift, final_shift = states[0] + 1, states[-1] + 1
    left_bound = vp(initial_shift, 3)
    right_bound = vp(final_shift, 2) - 1
    extension_count = 0
    for left in range(left_bound + 1):
        extended_shift = Fraction(initial_shift * 2 ** left, 3 ** left)
        require(extended_shift.denominator == 1, "legal backward end run")
        for right in range(right_bound + 1):
            extension_states, extension_word = shortcut_path(int(extended_shift) - 1, left + len(word) + right)
            require(extension_word == (1,) * left + word + (1,) * right,
                    "end extensions contain exactly the original defects")
            require(extension_states[left:left + len(states)] == states, "trimmed segment is unchanged")
            extension_count += 1
    require(Fraction(initial_shift * 2 ** (left_bound + 1), 3 ** (left_bound + 1)).denominator > 1,
            "next backward extension forbidden by integrality")
    require(shortcut_path(states[-1], right_bound + 1)[1][-1] > 1,
            "next forward extension is a defect")

    rejected_noncanonical = 0
    for start, length in ((19, 2), (29, 2)):
        noncanonical_states, noncanonical_word = shortcut_path(start, length)
        try:
            fd_control(noncanonical_states, noncanonical_word, pools)
        except RuntimeError as error:
            require(str(error) == "canonical fixture", "expected canonical-scope rejection")
            rejected_noncanonical += 1
        else:
            raise RuntimeError("untrimmed path counted as canonical")

    # Finite cycle laps are repeated occurrences, not distinct encoded
    # segments.  Changing the number of laps changes the defect count.
    one, word_one = shortcut_path(1, 1)
    two, word_two = shortcut_path(1, 2)
    require(one == [1, 1] and two == [1, 1, 1] and word_one == (2,) and word_two == (2, 2),
            "cycle occurrence/count distinction")

    report = {
        "status": "PASS: independent finite arithmetic review controls",
        "reviewed_sha256": PINS,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "construction": "Prescribed exponent words, inverse endpoint congruences, then literal shortcut replay; no author imports.",
        "canonical_inverse_cylinder_controls": canonical_count,
        "compressed_signed_subsums_evaluated": fd_subsets,
        "full_path_signed_subsums_evaluated": ru_subsets,
        "independently_decoded_unit_vectors": vectors,
        "literal_shortcut_edges_in_inverse_controls": shortcut_edges,
        "largest_odd_length": max(map(len, words)),
        "fixed_pool_sizes": [len(pool) for pool in pools],
        "fixtures": fixture_rows,
        "additional_ru_words": [list(w) for w in ru_words],
        "outside_excursion": excursion_states,
        "extension_canonical_segment": states,
        "end_extension_controls": extension_count,
        "end_extension_bounds": {"left": left_bound, "right": right_bound},
        "valid_but_noncanonical_paths_rejected": rejected_noncanonical,
        "cycle_occurrence_control": "Repeated 1 -> 1 edges encode the same length-one segment; a two-lap segment has two defects.",
        "scope": [
            "Finite controls supplement the separate written proof review.",
            "The external Evertse theorem and the infinite count bound are not computationally proved.",
            "No height bound, complete exception list, finite-convergence census, or Collatz resolution is claimed.",
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
