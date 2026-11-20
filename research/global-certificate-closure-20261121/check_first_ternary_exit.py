#!/usr/bin/env python3
"""Exact first-exit checks on actual certified Mersenne-family sources.

This does not exclude other adaptive words or forward excursions. It does
not infer nonconvergence from a finite computation.
"""

import argparse
import json
from pathlib import Path


def need(condition, message):
    if not condition:
        raise ValueError(message)


def val(n, p):
    need(n != 0, "nonzero valuation argument required")
    n, v = abs(n), 0
    if p == 2:
        return (n & -n).bit_length() - 1
    while n % p == 0:
        n //= p
        v += 1
    return v


def word(n, exponents):
    need(n > 0 and n % 2, "positive odd source required")
    for a in exponents:
        v = 3*n + 1
        need(val(v, 2) == a, "inexact ordinary exponent")
        n = v >> a
    return n


def exponent_class(h):
    eta = h + 5
    modulus = 3**(eta + 2)
    d0 = 2*pow(4, -h, 9) % 9
    p0 = (11 + 3**eta*d0)*pow(4, -1, modulus) % modulus
    p = pow(2, 119, modulus)
    step = pow(2, 162, modulus)
    for j in range(3**(h + 2)):
        if p == p0:
            return 119 + 162*j, 162*3**(h + 2), d0
        p = p*step % modulus
    raise ValueError("ternary lift not found")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = []
    for h in range(7):
        e, period, d0 = exponent_class(h)
        p, eta = 1 << e, h + 5
        need(val(4*p - 11, 3) == eta, "wrong exact agreement")
        d = (4*p - 11)//3**eta
        need(d > 0 and d % 2 and d % 3 and d % 9 == d0, "wrong exit digit")
        x = (1024*p - 2573)//243
        y = (x + 1)//2
        need(x == 1 + 256*3**h*d and y == 1 + 128*3**h*d, "starting pair")
        need(word(x, [2, 2, 2, 5, e - 1]) == 1, "upper rank-five certificate")
        need(word(y, [2, 2, 2, 1, 2]) == p - 1, "lower Mersenne path")
        ah, bh = x, y
        for i in range(h):
            need((4*ah - 1) % 3 == 0 and (4*bh - 1) % 3 == 0,
                 "illegal precision-spending inverse")
            ah, bh = (4*ah - 1)//3, (4*bh - 1)//3
            need(ah == 1 + 256*4**(i + 1)*3**(h - i - 1)*d, "upper identity")
            need(bh == 1 + 128*4**(i + 1)*3**(h - i - 1)*d, "lower identity")
        need(word(ah, [2]*h + [2, 2, 2, 5, e - 1]) == 1,
             "expanded upper lost its certificate")
        need(word(bh, [2]*h + [2, 2, 2, 1, 2]) == p - 1,
             "expanded lower lost its target path")
        need((2*bh - 1) % 3 == 0, "first I1 exit illegal")
        z = (2*bh - 1)//3
        need(z == ah//3 and word(z, [1]) == bh, "exit connection")
        need(z % 3 == 0 and z % 256 == 171, "exit guards")
        difference = 2*z - 1 - x
        need(3*difference == 256*d*(2*4**h - 3**(h + 1)) - 4,
             "wrong repayment difference")
        need((difference > 0) == (h >= 2), "wrong repayment threshold")
        for a in range(1, 30):
            need(((1 << a)*z - 1) % 3 != 0, "multiple of three acquired an inverse")
        if eta >= 6:
            r0 = (2*p - 1)//9
            need(r0 % 81 == 41, "r0 c=3 kernel")
            xhat = (512*r0 - 175)//81
            yhat = (xhat + 1)//2
            need(xhat < x and (xhat - 1)//128 == (x - 1)//384,
                 "smaller c=3 embedding")
            need(word(xhat, [2, 2, 2, 3]) == r0, "c=3 source prefix")
            need(word(yhat, [2, 2, 2, 1]) == 2*r0 + 1, "c=3 target prefix")
            a = val(r0 + 1, 2)
            q = (r0 + 1) >> a
            block_e = val(3**a*q - 1, 2)
            need((a, block_e) == (3, 1), "c=3 internal block")
            need(2*r0 + 1 != 4*r0 - 1, "different target identified")
        cases.append({"h": h, "eta": eta, "e_residue": e, "e_modulus": period,
                      "D_mod9": d0, "upper_bits": x.bit_length(),
                      "exit_mod256": z % 256, "exit_divisible_by_three": True,
                      "putative_upper_exceeds_original": difference > 0})
    need(2*4**2 - 3**3 == 5 and 256*5 - 4 > 0, "all-h sign induction base")
    need(6049 % 3 == 16384 % 3 == 1, "new169 A congruence")
    need(9911 % 3 == 32768 % 3 == 2, "new169 B congruence")
    report = {"status": "PASS_SCOPED_FIRST_EXIT_LEMMA",
              "actual_certified_source_classes": cases,
              "all_h_claim": "for h>=2 the first I1 exit exceeds the reverse height budget and misses the binary guard",
              "infinite_dead_end_classes": "D=2*4^(-h) mod9, for each h>=0",
              "new169_direct_domain": "both c5 bypasses require eta=5 on the hard Mersenne family",
              "scope": "does not exclude different earlier branches, longer adaptive words, or forward excursions",
              "full_collatz_proved": False}
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        need(not args.output.exists(), "refusing to overwrite evidence")
        args.output.write_text(rendered)
    print(rendered)


if __name__ == "__main__":
    main()
