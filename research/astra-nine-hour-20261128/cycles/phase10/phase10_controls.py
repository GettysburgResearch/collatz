"""Exact controls for native comparison, integer grid windows and signed carries."""
from fractions import Fraction
from itertools import product
from math import prod
from pathlib import Path
import sys

sys.dont_write_bytecode = True
here = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(here / "phase8"))
sys.path.insert(0, str(here / "phase9"))
from grid_clock_controls import forward, native, require
from staircase_controls import greatest, weights


def check_envelopes():
    cases = 0
    for x in range(1, 8192, 2):
        y, e = native(x)
        for b in (1, 2):
            B = 2**b
            for h in range(-8, 9):
                c = Fraction(2)**h
                next_c = c * Fraction(2)**(e-b)
                if c <= 1 and next_c <= 1:
                    r = 2*c*x
                    next_r = 2*next_c*y
                    require(B*int(next_r) - 3*int(r) <= 2, "dyadic subsolution")
                    cases += 1
                if c >= 1 and next_c >= 1:
                    v, next_v = 1+2*c*x, 1+2*next_c*y
                    require(B*next_v-3*v == B-1+2*(c-1), "scaled supersolution")
                    cases += 1
    total = saturated = 0
    for p in range(1, 6):
        for es in product(range(1, 5), repeat=p):
            Bs = [2**e for e in es]
            ws, power = weights(Bs)
            D = power - 3**p
            if D <= 0:
                continue
            x = Fraction(sum(ws), D)
            top = greatest(Bs)
            all_max = all(B*y-3*z == B-1 for B, z, y in zip(Bs, top, top[1:]))
            require(all_max == (x.denominator == 1), "whole native endpoint equivalence")
            if all_max:
                require(top[0] == 2*x+1 and x == 1, "calibration of saturated returns")
            total += 1
            saturated += all_max
    print(f"{cases} true odd-step envelope inequalities; {total} cyclic native words, {saturated} saturated.")


def check_horizon():
    tests = 0
    for K in range(1024, 1537):
        L, power = 0, 1
        while power < 2*K:
            L += 1
            power *= 3
        # Test every start and both total-winding extremes for the theorem's length.
        for x in range(K, 2*K):
            z = x
            possible = {0, 1}
            for _ in range(2*L+1):
                z, b, r = forward(K, z)
                if r != 0:
                    possible.discard(0)
                if r != 2**b-1:
                    possible.discard(1)
                if not possible:
                    break
            require(not possible, "extreme string exceeded the tested horizon")
            tests += 1
    print(f"{tests} complete starting labels in 513 grids for the extreme-run bound.")


def log_interval(x):
    """Rational integral bounds for log(x), using an atanh series after scaling."""
    if x < 1:
        lower, upper = log_interval(1/x)
        return -upper, -lower
    if x > 2:
        a, b = log_interval(x/2)
        c, d = log_interval(Fraction(2))
        return a+c, b+d
    u = (x-1)/(x+1)
    terms = 28
    lower = 2*sum(u**(2*k+1)/(2*k+1) for k in range(terms))
    error = 2*u**(2*terms+1)/((2*terms+1)*(1-u*u))
    return lower, lower+error


def check_entropy():
    d = Fraction(59, 500)
    lo2, hi2 = log_interval(Fraction(2))
    lo3, _ = log_interval(Fraction(3))
    _, a = log_interval(1/d)
    _, b = log_interval(1/(1-d))
    require(3*(d*a+(1-d)*b) < lo3, "strict entropy certificate")
    require(1/(6*hi2**2)+d/(6*hi2) > Fraction(3,8), "strict drift certificate")
    require(lo2 > 0, "positive logarithm")
    print("Two strict rational logarithmic inequalities certify the 3/8 threshold.")


def check_carries():
    cases = 0
    for length in range(1, 8):
        for radix_letters in product((2, 4), repeat=length):
            for Ps, Qs in ((radix_letters, [3]*length), ([3]*length, radix_letters)):
                M = prod(Ps)
                for m in (-9, -2, 1, 6, 13):
                    modulus = M
                    qprod = 1
                    previous = Fraction(m, M)
                    total = 0
                    for i in range(length+1):
                        if i < length:
                            Q = Qs[i]
                            numerator = (m*pow(qprod*Q, -1, modulus)) % modulus
                            if 2*numerator > modulus:
                                numerator -= modulus
                            a = Fraction(numerator, modulus)
                        else:
                            Q, a = 1, Fraction(0)
                        v = Q*a - previous
                        require(v.denominator == 1, "integer centered carry")
                        total += int(v)*modulus*qprod
                        if i < length:
                            previous = Ps[i]*a
                            modulus //= Ps[i]
                            qprod *= Q
                    require(total == -m, "signed two-base carry telescope")
                    cases += 1
    print(f"{cases} dyadic and ternary telescopes with exact signed centered phases.")


if __name__ == "__main__":
    check_envelopes()
    check_horizon()
    check_entropy()
    check_carries()
