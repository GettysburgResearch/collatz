"""Exact rational controls for the full-denominator Pell and cubic statements."""

import json
from fractions import Fraction
from itertools import product
from math import gcd, isqrt

from check_pell_returns import kfree, require


def step(n, d):
    total = 3*n + d
    a = (total & -total).bit_length() - 1
    return total >> a, a


def pell_data(n, d):
    m = 3*n*(3*n + d)
    left = kfree(3*n, 2)
    right = kfree(3*n+d, 2)
    D = left*right//gcd(left, right)**2
    V = 2*isqrt(m//D)
    X = 6*n+d
    require(X*X-D*V*V == d*d and gcd(V*D, d) == 1, "integral Pell lift")
    R = X*pow(V, -1, d*d) % (d*d) if d > 1 else 0
    require((R*R-D) % (d*d) == 0, "full square root modulus")
    return D, R, X, V


def cube_root(value):
    lo, hi = 0, 1 << ((value.bit_length()+2)//3)
    while lo+1 < hi:
        mid = (lo+hi)//2
        if mid**3 <= value:
            lo = mid
        else:
            hi = mid
    answer = hi if hi**3 == value else lo
    require(answer**3 == value, "integral cube")
    return answer


def thue_data(n, target, a, d):
    S, T = kfree(n, 3), kfree(target, 3)
    U = cube_root(n//S)
    V = 2**(a//3)*cube_root(target//T)
    A, B = 3*S, 2**(a % 3)*T
    require(B*V**3-A*U**3 == d and gcd(A*B*U*V, d) == 1, "diagonal cubic")
    R = V*pow(U, -1, d) % d if d > 1 else 0
    Z = (V-R*U)//d
    require(V == R*U+d*Z, "cube root class lift")
    last, error = divmod(B*R**3-A, d)
    require(error == 0, "integral last coefficient")
    value = B*d*d*Z**3+3*B*R*d*Z*Z*U+3*B*R*R*Z*U*U+last*U**3
    require(value == 1, "binary cubic represents one")
    require((2**a*T*pow(d, -1, 9)) % 9 in (2, 4, 5, 7),
            "excluded modulo-nine exponent class")


def orbit(n, d, period):
    result = []
    seen = set()
    for _ in range(period):
        require(n not in seen and n % 2 == 1 and gcd(n, 3*d) == 1,
                "primitive reduced odd numerator")
        seen.add(n)
        target, a = step(n, d)
        thue_data(n, target, a, d)
        result.append((n, a, pell_data(n, d)))
        n = target
    require(n == result[0][0], "full closure")
    carry = clock = 0
    for _, a, _ in result:
        carry = 3*carry+2**clock
        clock += a
    require(Fraction(carry, 2**clock-3**period) == Fraction(n, d),
            "complete determinant reduction")
    return result


def short_cycles():
    cycles = set()
    for length in range(1, 6):
        for word in product(range(1, 5), repeat=length):
            if word != min(word[i:]+word[:i] for i in range(length)):
                continue
            if any(length % j == 0 and word == word[:j]*(length//j)
                   for j in range(1, length)):
                continue
            carry = clock = 0
            for a in word:
                carry = 3*carry + 2**clock
                clock += a
            determinant = 2**clock-3**length
            if determinant > 0:
                x = Fraction(carry, determinant)
                data = orbit(x.numerator, x.denominator, length)
                require(tuple(row[1] for row in data) == word, "all edge exponents")
                cycles.add((length, x.numerator, x.denominator))
    return {"primitive_cycles": len(cycles), "replayed_odd_edges": sum(i[0] for i in cycles),
            "largest_reduced_denominator": max(i[2] for i in cycles)}


def selected_cycles():
    negative = orbit(5, 7, 2)
    pri, sec = negative[0][2], negative[1][2]
    require(pri[:2] == (330, 43) and sec[:2] == (330, 6), "necessary root coordinate")
    d = 1661
    data = orbit(4225, d, 200)
    n, a, (D, R, X, V) = data[0]
    target, _, (next_D, next_R, Y, W) = data[1]
    require((target, a, D, R) == (7, 11, 42, 523273) and (next_D, next_R) == (D, R),
            "genuine positive rational matching fiber")
    trace, rem = divmod(X*Y-D*V*W, d*d)
    other, rem2 = divmod(V*Y-X*W, d*d)
    require(rem == rem2 == 0 and trace*trace-D*other*other == 1
            and trace % 12 == 1 and trace >= 13, "integral joint unit")
    A, B = 3, 2**a
    K = 6+B-A
    N = A*A+B*B-2*A*B*trace
    require(N % 2 == 1 and (K*d)**2-D*(B*W-A*V)**2 == d*d*N, "normalized odd norm")
    return {"untagged_counterexample": {"d": 7, "numerators": [5, 11], "D": 330,
                                        "different_full_roots": [43, 6]},
            "matching_example": {"d": d, "primitive_odd_period": 200,
                                 "total_shortcut_clock": sum(i[1] for i in data),
                                 "source_numerator": n, "target_numerator": target,
                                 "edge_exponent": a, "D": D, "common_full_root": R,
                                 "quotient_trace": trace, "absolute_second_coordinate": abs(other),
                                 "normalized_return_norm": N}}


if __name__ == "__main__":
    print(json.dumps({"short_words": short_cycles(), "physical_controls": selected_cycles()},
                     indent=2, sort_keys=True))
