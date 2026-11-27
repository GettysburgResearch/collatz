"""Exact finite controls for the original-law global prefix traces."""
from collections import Counter
from fractions import Fraction
import json


DEPTH = 12
SCALE = 2**64


def require(value, message):
    if not value:
        raise RuntimeError(message)


def odd_step(x):
    numerator = 3*x+1
    power = numerator & -numerator
    return numerator//power, power.bit_length()-1


def independent_sources(n):
    rows = set()
    for m in range(1, 2**(7*n//4+1), 2):
        x, h = m, 0
        for j in range(1, n+1):
            x, e = odd_step(x)
            h += e
            if 4*h > 7*j:
                break
        else:
            if m < 2**(h+1):
                rows.add((m, x, h))
    return rows


def sibling_check():
    max_sum = Fraction()
    for k in range(11):
        for r in range(2**k):
            points = []
            for i in range(k):
                # The least j agreeing with r below bit i and disagreeing at i.
                j = (r % (2**i)) + (1-((r >> i) & 1))*2**i
                require((j-r) % 2**(i+1) == 2**i, "exact sibling valuation")
                points.append(j)
            require(len(points) == len(set(points)), "disjoint sibling minima")
            value = sum((Fraction(1, j) for j in points if j), Fraction())
            require(value <= 2, "sibling harmonic bound")
            max_sum = max(max_sum, value)
    return str(max_sum)


def enclosure(lo, count):
    return [lo, lo+count]


def main():
    parents = [(1, 1, 0)]
    rows = []
    previous_envelope = Fraction(9)
    for n in range(1, DEPTH+1):
        cap = 7*n // 4
        ternary = 3**n
        inverse = pow(ternary, -1, 2**cap)
        children = []
        paid = Counter()
        jlo = rawlo = cyclelo = birthlo = 0
        birth_count = actual_deaths = 0
        for m, y, h in parents:
            new_mass = Fraction()
            kept = False
            for e in range(1, cap-h+1):
                j = ((2**(e-1) - (3*y+1)//2)*inverse) % 2**e
                seed = m + 2**(h+1)*j
                old_terminal = y + 2*3**(n-1)*j
                endpoint, exponent = odd_step(old_terminal)
                require(exponent == e and 0 < endpoint < 2*ternary,
                        "word lift and principal odd endpoint")
                clock = h+e
                carry = 2**clock*endpoint - ternary*seed
                require(carry > 0, "positive intercept")
                children.append((seed, endpoint, clock))
                paid[clock] += 1
                jlo += SCALE // seed
                rawlo += (SCALE*ternary) // (2**clock*endpoint)
                cyclelo += (SCALE*carry) // (seed*(n*seed*ternary+carry))
                if j == 0:
                    kept = True
                else:
                    birth_count += 1
                    birthlo += SCALE // seed
                    new_mass += Fraction(1, seed)
            require(new_mass <= Fraction(1, 2**h), "new reciprocal cost per parent")
            actual_deaths += int(not kept)
        require(len({m for m, _, _ in children}) == len(children), "distinct seeds by depth")
        if n <= 7:
            require(set(children) == independent_sources(n), "direct ordinary enumeration")
        prob = sum((Fraction(count, 2**h) for h, count in paid.items()), Fraction())
        reserve = sum((Fraction(count*(7*n-4*h+8), 2**h)
                       for h, count in paid.items()), Fraction())
        upper = Fraction(jlo+len(children), SCALE) + reserve
        require(upper <= previous_envelope, "monotone augmented centered mass")
        previous_envelope = Fraction(jlo, SCALE) + reserve
        rows.append({"depth": n, "words": len(children), "new_seeds": birth_count,
                     "departed_seeds": actual_deaths, "gate_probability": str(prob),
                     "debt_reserve": str(reserve), "centered": enclosure(jlo, len(children)),
                     "uncentered": enclosure(rawlo, len(children)),
                     "centered_minus_parameter_1_over_n": enclosure(cyclelo, len(children)),
                     "birth_reciprocals": enclosure(birthlo, birth_count)})
        parents = children
    print(json.dumps({"scope": "finite prefix laws and rational outward enclosures only",
                      "scale": SCALE, "depth_zero_centered": 1, "depth_zero_debt_reserve": 8,
                      "sibling_max_through_ten_bits": sibling_check(), "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
