"""Realize both order-six signs with actual positive odd integers in a band above three."""
from collections import Counter
from math import gcd
import json


POS = (0, 3, 5, 11, 13, 16)
NEG = (1, 8, 15)
PLUS = ((1, 1, 0), (1, 1, 0), (0, 0, 0))
MINUS = ((0, 0, 0), (1, 0, 0), (1, 1, 1))


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def stencil(values, start):
    return sum(values[start+j] for j in POS)-2*sum(values[start+j] for j in NEG)


def calendar(top, bottom, padding, gap):
    num, den = 1000001, 1000000
    letters, visits = [], []
    while len(visits) < 2 or len(letters) < visits[1]+3+padding:
        date = len(letters)
        if (len(visits) < 2 and 3*num*bottom < top*den and 100*num < 101*den
                and date > padding and (not visits or date > visits[0]+3+gap)):
            visits.append(date)
        b = 1 if 3*num < 4*den else 2
        letters.append(b)
        num, den = 3*num, den << b
    for t in visits:
        require(letters[t-1:t+3] == [2, 1, 2, 1], "actual irrational mechanical calendar")
    return letters, visits


def fixture(top, bottom, padding, gap, slots, start, counts):
    letters, visits = calendar(top, bottom, padding, gap)
    n, B = len(letters), sum(letters)
    tags = [[2]*slots for _ in range(n+1)]
    signed = [0]*(n+1)
    for t, positive, negative, sign in ((visits[0], PLUS, MINUS, 1),
                                        (visits[1], MINUS, PLUS, -1)):
        for j in range(3):
            for k, kpos in enumerate(POS):
                tags[t+j][start+kpos] = 1+positive[j][k//2]
            for k, kneg in enumerate(NEG):
                tags[t+j][start+kneg] = 1+negative[j][k]
        signed[t+1:t+3] = [2*sign]*2
    require(all((1 << b)*signed[t+1] == 3*signed[t]+stencil(tags[t], start)
                for t, b in enumerate(letters)), "full scalar signed transfer")

    K, E = [0]*slots, [0]*slots
    for t, b in enumerate(letters):
        for j in range(slots):
            e = b+tags[t+1][j].bit_length()-tags[t][j].bit_length()
            require(1 <= e <= 3, "all native valuations are ordinary")
            K[j] = 3*K[j]+(1 << E[j])
            E[j] += e
    require(all(e == B for e in E) and stencil(K, start) == 0,
            "physical endpoints and exact full affine carries")
    two, power = 1 << (B+1), 3**n
    M = 3*two
    inv = pow(power, -1, two)
    origins = [((1 << B)-k)*inv % two for k in K]
    origins = [v+two*((1-v)*pow(two, -1, 3) % 3) for v in origins]
    total = stencil(origins, start)
    require(total % M == 0, "simultaneous ternary and exact native parity cylinders")
    origins[start+16] -= total
    C = 10000*(n+1)
    amplitude = 10**13*C*(slots+1)**6
    x = [v+M*(amplitude+C*(j+1)**5) for j, v in enumerate(origins)]
    seen = set()
    lo, hi = min(x), max(x)
    for t in range(n+1):
        for val in x:
            require(val > 0 and val % 2 and gcd(val, 3) == 1 and val not in seen,
                    "all positive distinct odd ternary-unit phases")
            seen.add(val)
        lo, hi = min(lo, min(x)), max(hi, max(x))
        folded = [xx*tag for xx, tag in zip(x, tags[t])]
        require(stencil(folded, start) == signed[t], "literal order-six physical stencil")
        diffs = folded
        for _ in range(5):
            diffs = [v-u for u, v in zip(diffs, diffs[1:])]
            require(min(diffs) > 0, "strict spatial differences through order five")
            counts["positive_spatial_differences"] += len(diffs)
        if t == n:
            break
        for j in range(slots):
            exp = letters[t]+tags[t+1][j].bit_length()-tags[t][j].bit_length()
            xx, rem = divmod(3*x[j]+1, 1 << exp)
            require(rem == 0 and xx % 2 == 1, "true v2 of every odd edge")
            x[j] = xx
        counts["ordinary_odd_edges"] += slots
    require(3*lo < hi and hi*bottom < lo*top, "strict native width bounds")
    counts["fixtures"] += 1
    counts["distinct_phases_across_fixtures_counted_separately"] += len(seen)
    counts["largest_minimum_bit_length"] = max(counts["largest_minimum_bit_length"], lo.bit_length())
    counts["longest_calendar"] = max(counts["longest_calendar"], n)
    counts["both_sign_gadgets"] += 2


def main():
    counts = Counter()
    for args in ((31, 10, 9, 24, 17, 0), (301, 100, 60, 100, 31, 4),
                 (3001, 1000, 5, 12, 21, 2)):
        fixture(*args, counts)
    return counts


if __name__ == "__main__":
    print(json.dumps(main(), sort_keys=True, indent=2))
