#!/usr/bin/env python3
"""Exact controls for the finite weighted triadic certificate, not existence."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def weight(r):
    f = 1
    for j in range(r):
        f *= 1 + 3**j
    return f


def shortcut(n):
    return (3*n+1)//2 if n % 2 else n//2


def horizon(n, a, r):
    return 9 * (n*max(1, abs(a))*weight(r)).bit_length() + 1


def old_horizon(n, a, r):
    return 8*n.bit_length() + (9*r+8)*max(1, abs(a), 3**r).bit_length() + 2


def reconstruct_dual(n):
    x, bits = n, []
    while x != 1:
        require(len(bits) < 10000, "finite control orbit exceeded its guard")
        bits.append(x % 2)
        x = shortcut(x)
    y = Fraction(2)
    for e in reversed(bits):
        y = 2*y if e else (2*y-1)/3
    d, r = y.denominator, 0
    while d > 1:
        require(d % 3 == 0, "reconstructed denominator was not triadic")
        d //= 3
        r += 1
    return y.numerator, r, len(bits)


def paired_prefix(n, a, r, length):
    x, w, h = n, a, r
    first_one = 0 if x == 1 else None
    for k in range(length):
        if (x+w) % 2 != 1:
            return k, first_one
        old_p = x * abs(w) * weight(h)
        old_w, old_h, old_x = w, h, x
        if x % 2:
            x, w = (3*x+1)//2, w//2
        elif h:
            h -= 1
            x, w = x//2, (w+3**h)//2
        else:
            x, w = x//2, (3*w+1)//2
        if old_x > 1:
            p = x * abs(w) * weight(h)
            require(p <= old_p, "weighted product increased")
            if old_w != 0 and not (old_h == 0 and old_w == 1):
                require(6*p <= 5*old_p, "step contraction failed")
            if old_w != 0 and w == 0:
                require(x+1 <= old_p, "zero-entry resource was unpaid")
        if first_one is None and x == 1:
            first_one = k+1
    return None, first_one


def carry(n, length):
    modulus = 1 << length
    x, b, d, bit = n, 0, 0, 1
    for _ in range(length):
        e = x % 2
        if not e:
            b += 1
            d = (3*d+bit) % modulus
        x = shortcut(x)
        bit <<= 1
    return b, d, modulus


def congruence(a, r, b, d, modulus):
    return (pow(3, b, modulus)*a + pow(3, r, modulus)*d) % modulus == 0


def main():
    cases = []
    mutations = 0
    for n in (1, 2, 3, 4, 7, 27, 97):
        a, r, tau = reconstruct_dual(n)
        h = horizon(n, a, r)
        failure, first_one = paired_prefix(n, a, r, h)
        require(failure is None and first_one == tau, "genuine finite control failed")
        b, d, modulus = carry(n, h)
        require(congruence(a, r, b, d, modulus), "complete congruence failed")
        require(not congruence(a+1, r, b, d, modulus), "altered numerator accepted")
        require(not congruence(a, r, b, d+1, modulus), "altered carry accepted")
        require(not congruence(a, r+1, b, d, modulus), "altered denominator accepted")
        mutations += 3
        cases.append(dict(n=n, numerator=str(a), denominator_exponent=r,
                          known_first_hit=tau, new_horizon=h,
                          previous_horizon=old_horizon(n, a, r),
                          all_tests_passed=True, complete_congruence=True))

    # The old clock alone is not a certificate for a newly enlarged candidate.
    n, a, r = 3, -4, 2
    stale = horizon(n, a, r)
    altered = a + 3**r * (1 << stale)
    b, d, modulus = carry(n, stale)
    require(congruence(altered, r, b, d, modulus), "stale-clock control lost its prefix")
    own_h = horizon(n, altered, r)
    require(own_h > stale, "candidate height did not charge new bits")
    failure, _ = paired_prefix(n, altered, r, own_h)
    require(failure == stale, "long-prefix perturbation failed at wrong clock")
    own_b, own_d, own_mod = carry(n, own_h)
    require(not congruence(altered, r, own_b, own_d, own_mod), "own-clock forgery accepted")
    mutations += 1

    # Pure height comparison; these are not asserted accepted candidates.
    height_only = []
    for r in (2, 10, 20):
        a = 1 << 4096
        height_only.append(dict(n=3, numerator_bits=a.bit_length(),
                                denominator_exponent=r,
                                new_horizon=horizon(3, a, r),
                                previous_horizon=old_horizon(3, a, r),
                                scope="height comparison only; no accepted candidate"))

    return dict(schema="collatz-triadic-amortized-controls/v1",
                scope="exact finite controls; no universal candidate construction",
                control_source_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                accepted_known_controls=cases,
                rejected_mutations=mutations,
                stale_clock_control=dict(old_clock=stale, own_clock=own_h,
                                         first_failure=failure),
                numerator_heavy_comparisons=height_only)


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
