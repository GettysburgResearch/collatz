"""Exact finite physical controls and a rational enclosure of the ladder constant."""
from fractions import Fraction
from math import comb
import json


def log_bounds(integer, terms=75):
    t = Fraction(integer - 1, integer + 1)
    partial = sum(2 * t ** (2*j+1) / (2*j+1) for j in range(terms))
    remainder = 2*t**(2*terms+1) / ((2*terms+1)*(1-t*t))
    return partial, partial + remainder


def decimal_box(lo, hi, digits=12):
    scale = 10**digits
    return {"scale": scale, "lower_units": int(lo*scale),
            "upper_units": -(-(hi*scale).numerator // (hi*scale).denominator)}


def ladder_bound(depth):
    """Count the first strictly positive log slope with integer comparisons only."""
    counts = {0: 1}
    mass_num = odds_num = clock_num = 0
    ternary_powers = [3**q for q in range(depth+1)]
    for clock in range(1, depth+1):
        raw = {}
        for q, count in counts.items():
            raw[q] = raw.get(q, 0) + count
            raw[q+1] = raw.get(q+1, 0) + count
        counts = {}
        for q, count in raw.items():
            if ternary_powers[q] <= (1 << clock):
                counts[q] = count
            else:
                normalized_count = count << (depth-clock)
                mass_num += normalized_count
                odds_num += q * normalized_count
                clock_num += clock * normalized_count
    den = 1 << depth
    prob = Fraction(mass_num, den)
    odds, time = Fraction(odds_num, den), Fraction(clock_num, den)
    l2, u2 = log_bounds(2)
    l3, u3 = log_bounds(3)
    eh_lower = odds * l3 - time * u2
    eh_upper = odds * u3 - time * l2
    # (1+sqrt(3))/(2 sqrt(2)) < 97/100. Squaring twice is exact.
    if not 3*(2500**2) < 4409**2:
        raise RuntimeError("square-root majorant")
    lam = Fraction(97, 100)
    tail = lam**(depth+1) / (1-lam)
    p_lower, p_upper = prob, prob+tail
    c_lower = eh_lower / (1-p_lower)
    c_upper = (eh_upper+(u3-l2)*tail) / (1-p_upper)
    return {"clock": depth, "first_ladder_probability": decimal_box(p_lower, p_upper),
            "harmonic_background": decimal_box(c_lower, c_upper),
            "tail_bound": decimal_box(0, tail, 15)}


def native_sieve(cutoff):
    depth = cutoff.bit_length() - 1
    gates = set()
    # A reverse prefix represents (2^i y - carry)/modulus.
    words = [(1, 0)]
    for i in range(1, depth+1):
        new_words = []
        for modulus, carry in words:
            if 2*modulus >= 1 << i:
                new_words.append((modulus, 2*carry))
            if 6*modulus >= 1 << i:
                new_words.append((3*modulus, 2*carry+modulus))
        words = new_words
    end = (3*cutoff-2)//2
    for modulus, carry in words:
        residue = carry * pow(1 << depth, -1, modulus) % modulus
        first = cutoff + (residue-cutoff) % modulus
        gates.update(range(first, end+1, modulus))
    return gates


def first_exits(cutoff):
    memo = {}
    for src in range(1, cutoff):
        x = src
        path = []
        seen = set()
        while x < cutoff and x not in memo and x not in seen:
            path.append(x)
            seen.add(x)
            x = (3*x+1)//2 if x % 2 else x//2
        found = (x, 0, 0) if x >= cutoff else memo.get(x)
        for previous in reversed(path):
            if found is not None:
                z, clock, grade = found
                found = (z, clock+1, grade+previous%2)
            memo[previous] = found
    return memo


def physical_control(cutoff):
    k = cutoff.bit_length()-1
    grade_cap = 0
    while 3**(grade_cap+1) <= cutoff:
        grade_cap += 1
    sieve = native_sieve(cutoff)
    scale = 10**14
    data = {key: [0, 0] for key in
            ("early_harmonic", "off_sieve_harmonic", "grade_capped_squared_times_X")}
    for hit in first_exits(cutoff).values():
        if hit is None:
            continue
        gate, clock, grade = hit
        num, den = 3**grade, (1 << clock)*gate
        if clock >= k and gate not in sieve:
            raise RuntimeError("long physical exit outside sieve")
        for key, good, numerator, denominator in [
                ("early_harmonic", clock <= k, num, den),
                ("off_sieve_harmonic", gate not in sieve, num, den),
                ("grade_capped_squared_times_X", grade <= grade_cap,
                 cutoff*num*num, den*den)]:
            if good:
                data[key][0] += 1
                data[key][1] += scale*numerator//denominator
    return {"X": cutoff, "native_depth": k, "grade_cap": grade_cap,
            "native_sieve_size": len(sieve), "scale": scale,
            "intervals": {key: {"sources": n, "lower_units": mass,
                                "upper_units": mass+n}
                          for key, (n, mass) in data.items()}}


def check_moments():
    for j in range(11):
        histogram = [0]*(j+1)
        for src in range(2**j, 2**(j+1)):
            x, q = src, 0
            for _ in range(j):
                odd = x % 2
                q += odd
                x = (3*x+1)//2 if odd else x//2
            histogram[q] += 1
            if 2**j*x+2**j > 3**q*src+3**j:
                raise RuntimeError("affine bound")
        if histogram != [comb(j, q) for q in range(j+1)]:
            raise RuntimeError("dyadic moment")


def main():
    check_moments()
    result = {"ladder": ladder_bound(1250), "physical": [physical_control(x) for x in
              (128, 511, 4096, 10001, 32768, 131072)], "dyadic_shell_depths": [0, 10]}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
