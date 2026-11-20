#!/usr/bin/env python3
"""Independent exact review of the scoped first-ternary-exit lemma.

Uses ternary digit lifting instead of the author's linear exponent search,
and constructs complete upper certificates backwards from 1. Unknown
target convergence is never inferred. All file inputs are colocated.
"""

from pathlib import Path
import hashlib
import json


HERE = Path(__file__).resolve().parent
HEIGHT = 176106


def need(ok, why):
    if not ok:
        raise ValueError(why)


def val(n, prime):
    need(n != 0, "valuation of zero")
    n = abs(n)
    if prime == 2:
        return (n & -n).bit_length() - 1
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent


def forward(n, letters):
    for letter in letters:
        need(n > 0 and n % 2, "nonpositive or even odd-step input")
        numerator = 3 * n + 1
        need(val(numerator, 2) == letter, "inexact odd-step exponent")
        n = numerator >> letter
    return n


def backward_first_hit(letters):
    n = 1
    for letter in reversed(letters):
        numerator = (n << letter) - 1
        need(numerator % 3 == 0, "nonintegral inverse in source certificate")
        n = numerator // 3
        need(n > 1 and n % 2, "source word was not first-hit")
    need(forward(n, letters) == 1, "source certificate failed forward check")
    return n


def lift_class(h):
    eta = h + 5
    full_modulus = 3 ** (eta + 2)
    digit = 2 * pow(4, -h, 9) % 9
    target = (11 + 3 ** eta * digit) * pow(4, -1, full_modulus) % full_modulus
    exponent, period, modulus = 119, 162, 243
    need(pow(2, exponent, modulus) == target % modulus, "wrong base exponent class")
    while modulus < full_modulus:
        need(val(pow(2, period, 3 * modulus) - 1, 3) == val(modulus, 3),
             "next ternary digit is not controlled by the exact period")
        modulus *= 3
        candidates = [exponent + j * period for j in (0, 1, 2)
                      if pow(2, exponent + j * period, modulus) == target % modulus]
        need(len(candidates) == 1, "ternary digit lift is not unique")
        exponent = candidates[0]
        period *= 3
    need(period == 2 * 3 ** (eta + 1), "wrong full exponent period")
    need(exponent >= 119 and (exponent - 119) % 162 == 0, "class left rank-five progression")
    residue = (4 * pow(2, exponent, full_modulus) - 11) % full_modulus
    need(val(residue, 3) == eta and (residue // 3 ** eta) % 9 == digit,
         "class did not force the exact valuation and exit digit")
    need(pow(2, period, full_modulus) == 1, "class period does not preserve its conditions")
    return exponent, period, digit


def actual_case(h, exponent, period, digit, translate):
    e = exponent + translate * period
    eta = h + 5
    p = 1 << e
    need(val(4 * p - 11, 3) == eta, "actual source has wrong ternary valuation")
    d = (4 * p - 11) // 3 ** eta
    need(d > 0 and d % 2 and d % 3 and d % 9 == digit, "actual exit digit failed")
    source_word = [2, 2, 2, 5, e - 1]
    x = backward_first_hit(source_word)
    need(243 * x == 1024 * p - 2573, "complete source has wrong affine identity")
    y = (x + 1) // 2
    k = (x - 1) // 128
    need(x == 1 + 256 * 3 ** h * d and k == 2 * 3 ** h * d,
         "original source/index formula failed")
    need(forward(y, [2, 2, 2, 1, 2]) == p - 1, "lower does not reach Mersenne")
    ah = backward_first_hit([2] * h + source_word)
    bh = 1 + 128 * 4 ** h * d
    need(ah == 1 + 256 * 4 ** h * d and ah == 2 * bh - 1,
         "paired inverse endpoint failed")
    need(forward(ah, [2] * h) == x and forward(bh, [2] * h) == y,
         "paired inverse provenance failed")
    for i in range(h + 1):
        ai = 1 + 256 * 4 ** i * 3 ** (h - i) * d
        bi = 1 + 128 * 4 ** i * 3 ** (h - i) * d
        need(forward(ai, [2] * i) == x and forward(bi, [2] * i) == y,
             "intermediate precision state lost its original component")
    need(ah % 3 == 0 and (2 * bh - 1) % 3 == 0, "first exit is nonintegral")
    z = ah // 3
    need(forward(z, [1]) == bh, "exit exponent was not exactly one")
    difference = 2 * z - 1 - x
    need(3 * difference == 256 * d * (2 * 4 ** h - 3 ** (h + 1)) - 4,
         "height repayment identity failed")
    need((difference > 0) if h >= 2 else (difference < 0), "wrong height sign")
    need(z % 256 == 171 and z % 256 not in (65, 129, 193), "binary reverse guard passed")
    need(z % 3 == 0, "exit is not a ternary dead end")
    # Powers of two modulo three have period two, so these two residues
    # verify the entire odd inverse family, not merely a finite exponent cap.
    need(all(((2 ** a * z - 1) % 3 == 2) for a in (1, 2)),
         "an odd inverse survives at a multiple of three")
    if h >= 1:
        need(k % 3 == 0, "positive-depth original index did not miss both new169 guards")
        need(((ah - 1) // 128) % 8 == 0, "expanded index did not miss binary bypass guard")
    r0 = (2 * p - 1) // 9
    need(9 * r0 == 2 * p - 1 and r0 % 2, "r0 was not positive odd integral")
    need(forward(r0, [1, 1]) == (p >> 1) + 1, "r0 plus-power path failed")
    small_representative = 3 ** ((e - 1) // 2) + 1
    need(HEIGHT * small_representative < x, "r0 representative misses original H2 floor")
    if p % 5 == 3:
        q = (32 * p - 61) // 135
        need(135 * q == 32 * p - 61, "four-phase source not integral")
        need(5 * forward(q, [4]) == r0, "four-phase certificate provenance failed")
        phase = "first_valuation_four"
    else:
        need(p % 5 == 2, "unknown physical-five phase")
        q = (128 * p - 271) // 405
        need(405 * q == 128 * p - 271, "three-phase source not integral")
        need(forward(5 * forward(q, [3]), [3]) == r0,
             "three-phase certificate provenance failed")
        phase = "first_valuation_three"
    need(forward(4 * r0 - 1, [1, 2]) == p - 1, "required shifted target left Mersenne component")
    c3 = h >= 1
    if c3:
        need(r0 % 81 == 41, "r0 misses c3 kernel")
        numerator = 512 * r0 - 175
        need(numerator % 81 == 0, "c3 source is not integral")
        xhat = numerator // 81
        yhat = (xhat + 1) // 2
        need(3 * xhat == x + 2 and xhat < x, "c3 source height formula failed")
        khat = (xhat - 1) // 128
        need(3 * khat == k and khat > 0 and khat % 4 == 2,
             "c3 index is not smaller eligible k/3")
        need(forward(xhat, [2, 2, 2, 3]) == r0, "c3 source provenance failed")
        need(forward(yhat, [2, 2, 2, 1]) == 2 * r0 + 1, "c3 lower target changed")
        a = val(r0 + 1, 2)
        block_e = val(3 ** a * ((r0 + 1) >> a) - 1, 2)
        need((a, block_e) == (3, 1), "internal c3 block was not (3,1)")
        # A direct ordinary merger independently verifies this e_block=1
        # comparison, without assuming convergence of the shifted bad value.
        need(forward(r0, [1, 1, 2, 2]) == forward(2 * r0 + 1, [1, 1, 1, 4]),
             "direct c3 target merger failed")
        need(2 * r0 + 1 != 4 * r0 - 1, "different targets were identified")
    else:
        need((512 * r0 - 175) % 81 != 0, "eta=5 incorrectly admitted the c3 embedding")
    return {"h": h, "eta": eta, "e_residue": exponent, "e_period": period,
            "representative_translate": translate, "D_mod9": digit,
            "upper_bits": x.bit_length(), "source_rank": 5,
            "expanded_source_rank": h + 5, "exit_mod256": z % 256,
            "exit_divisible_by_three": True, "upper_height_repaid": difference < 0,
            "five_phase": phase, "smaller_c3_embedding_checked": c3}


def main():
    need(val(2 ** 162 - 1, 3) == 5, "base ternary order identity failed")
    need(2 * pow(2, 119, 243) % 243 == 127,
         "unexpected base power residue")
    need(2 * 4 ** 2 - 3 ** 3 == 5 and 256 * 5 - 4 > 0,
         "all-depth positive-height base failed")
    # With u=4^h and v=3^h, F_(h+1)=8u-9v=3(2u-3v)+2u.
    need((8, -9) == (3 * 2 + 2, 3 * -3), "height sign recurrence failed")
    need(pow(3, -1, 256) == 171, "binary guard residue failed")
    need(16384 % 3 == 6049 % 3 == 1 and 32768 % 3 == 9911 % 3 == 2,
         "PR169 necessary ternary guards changed")
    need(HEIGHT * (3 ** 59 + 1) < (1024 * 2 ** 119 - 2573) // 243
         and 3 ** 81 < 2 ** 162, "universal r0 height induction failed")
    modular_classes = [lift_class(h) for h in range(31)]
    need(modular_classes[2] == (767, 13122, 8), "published example class changed")
    cases = []
    for h in range(6):
        exponent, period, digit = modular_classes[h]
        for translate in (0, 1):
            cases.append(actual_case(h, exponent, period, digit, translate))
    need({row["five_phase"] for row in cases}
         == {"first_valuation_three", "first_valuation_four"}, "both provenance phases were not tested")
    files = ("FIRST_TERNARY_EXIT.md", "check_first_ternary_exit.py")
    report = {
        "status": "PASS",
        "scope": "First I1 exit and the displayed c3 embedding only; no exclusion of longer adaptive constructions",
        "input_sha256": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                         for name in files},
        "independent_exponent_method": "unique ternary-digit lifting",
        "modular_class_depths_checked": list(range(31)),
        "actual_certified_sources": cases,
        "all_depth_height_certificate": {"F_2": 5, "recurrence": "F_(h+1)=3*F_h+2*4^h"},
        "odd_inverse_dead_end_certificate": "Z=0 mod3 and the two residues of 2^a mod3",
        "c3_target_membership_dependency": "r0 reaches the original H2 floor; direct e_block=1 ordinary merger",
        "full_collatz_proved": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
