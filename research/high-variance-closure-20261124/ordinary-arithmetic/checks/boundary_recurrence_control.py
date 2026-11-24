"""Exact independent finite controls for the ordinary periodic-boundary theorem."""
from fractions import Fraction
import json


def require(condition, label):
    if not condition:
        raise ValueError(label)


def shortcut(x):
    return (3*x+1)/2 if x.numerator & 1 else x/2


def profile(n, d, clocks):
    """Shortcut numerator on rationals of odd denominator d, with unreduced numerator."""
    p = 0
    for _ in range(clocks):
        if n % 2:
            p += 1
            n = (3*n+d)//2
        else:
            n //= 2
    return n, p


def root_cycle(x, d):
    visited = {}
    while x not in visited:
        require(len(visited) < 1000, "unexpected long rational orbit")
        visited[x] = len(visited)
        x = profile(x, d, 1)[0]
    return set(visited), set(list(visited)[visited[x]:])


def counted_fusion(u, offset, horizon):
    v = u+offset
    p = q = 0
    for i in range(horizon):
        u, a = profile(u, 1, 1)
        v, b = profile(v, 1, 1)
        p += a
        q += b
        if u == v and p == q:
            return i+1
    return None


def signed_fixture():
    left = set()
    right = set()
    for r in (11, 7, 14, 13):
        path, cycle = root_cycle(-r, 15)
        require(cycle == {3, 6, 12}, "left rational cycle")
        left.update(path)
        path, cycle = root_cycle(15-r, 15)
        require(cycle == {57, 93, 147, 228, 114}, "right rational cycle")
        right.update(path)
    require(left.isdisjoint(right), "signed seed intersection")
    require(min(left) == -14 and max(right) == 228, "residual bound")
    n = 17
    alpha = Fraction(15*n+11, 15)
    h = 6
    i, j = 8+36*h, 8+20*h
    left_input = (2**i*alpha).__floor__()
    right_input = (2**j*alpha).__floor__()+1
    u, p = profile(left_input, 1, i)
    v, q = profile(right_input, 1, j)
    require(p == q == 5+12*h and v == u+3, "matched ordinary arms")
    require(5*u-4 == 3**(12*h+4)*(15*n+11), "ordinary multiplier")
    clock = counted_fusion(u, 3, 16)
    require(clock == 10, "explicit ordinary common future")
    return {"fixed_root": n, "left_level": i, "right_level": j,
            "extra_clocks": clock, "common_odd_grade": p,
            "all_native_residuals_left": sorted(left),
            "all_native_residuals_right": sorted(right)}


def uniform_finite_block():
    # For n!=11 mod 16, v_2(5u_0-4)=v_2(15n+11) < 4.
    # Count over the actual exponent orbit modulo 2^16, never a fresh start.
    modulus = 2**16
    five_inverse = pow(5, -1, modulus)
    seen = set()
    cycles = 0
    longest = 0
    for u in range(modulus):
        if (5*u-4) % 16 == 0 or u in seen:
            continue
        index_to_residue = []
        while u not in seen:
            seen.add(u)
            index_to_residue.append(u)
            u = ((3**12*(5*u-4)+4)*five_inverse) % modulus
        require(index_to_residue[0] == u, "permutation orbit")
        hit = [k for k, v in enumerate(index_to_residue) if counted_fusion(v, 3, 16)]
        require(hit, "empty admissible exponent orbit")
        lengths = [(hit[(k+1) % len(hit)]-h-1) % len(index_to_residue)
                   for k, h in enumerate(hit)]
        longest = max(longest, max(lengths))
        cycles += 1
    require(len(seen) == 15*4096 and longest == 1023, "uniform period bound")
    max_level = 8+36*longest
    require(max_level % 4 == 0, "whole 1011 blocks")
    return {"modulus": modulus, "residues_covered": len(seen),
            "distinct_exponent_orbits": cycles, "max_failed_exponents_before_hit": longest,
            "extra_merger_clock_at_most": 16, "sufficient_1011_repetitions": max_level//4}


def triadic_controls():
    y = Fraction(1, 3)
    for d in range(2, 15):
        lifted = 2*y
        e = 1
        while lifted <= 1:
            lifted *= 2
            e += 1
        nxt = (lifted-1)/3
        z = nxt
        for _ in range(e):
            z = shortcut(z)
        require(z == y and 0 < nxt < 1 and nxt.denominator == 3**d,
                "positive triadic preimage")
        y = nxt
        x = Fraction(-3**d+2**(d+1), 3**d)
        z = x
        for _ in range(d):
            z = shortcut(z)
        require(z == 1 and -1 < x < 0 and x.denominator == 3**d,
                "negative triadic preimage")
    return {"highest_seed_denominator": 3**14}


def terminal_fixture():
    b, k = 5, 51
    u = 3**k*b-1
    require(counted_fusion(u, 2, 24) == 9, "even right-side merger")
    require(counted_fusion(2*u, 3, 24) == 22, "odd right-side merger")
    left = 2**k*b-1
    right_even = 2**(2*k)*b+1
    right_odd = 2**(2*k+1)*b+1
    clocks = [k+21, 2*k+21, 2*k+22]
    endpoints = [profile(n, 1, t)[0] for n, t in
                 zip((left, right_even, right_odd), clocks)]
    require(endpoints[0] == endpoints[1] == endpoints[2], "three original ordinary sources")
    return {"fixed_center": b, "exponent": k, "actual_meeting_clocks": clocks}


if __name__ == "__main__":
    print(json.dumps({"order_4_ray": signed_fixture(), "uniform_control": uniform_finite_block(),
                      "triadic_seeds": triadic_controls(), "terminal_sides": terminal_fixture()}, indent=2))
