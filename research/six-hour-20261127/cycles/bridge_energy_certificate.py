"""Exact rational itinerary certificate for binary four-copy bridges at width 1.98."""
from fractions import Fraction
import json

WIDTH_FRACTION = Fraction(49, 50)
STEPS = 53
LO = Fraction(584961, 10**6)
HI = Fraction(584964, 10**6)

def require(condition, label):
    if not condition:
        raise ValueError(label)

def arrangement(alpha):
    entries = [(Fraction(0), ('endpoint', 0)), (Fraction(1), ('endpoint', 1))]
    for k in range(STEPS + 1):
        for shift, tag in [(Fraction(0), 'int'), (WIDTH_FRACTION, 'cap')]:
            if k == 0 and shift == 0:
                continue
            raw = shift - k * alpha
            floor = raw.numerator // raw.denominator
            entries.append((raw - floor, (tag, k, floor)))
    entries.sort()
    require(len(set(f for f, _ in entries)) == len(entries), 'coincident interior breakpoints')
    return entries

def visit(alpha, f):
    forced = f > WIDTH_FRACTION
    v = (1, 0, 0)
    for j in range(1, STEPS + 1):
        x, y, z = v
        f += alpha
        if f >= 1:
            f -= 1
            v = (x, 4 * x + y, x + y + z)
        else:
            v = (x + y + z, y + 4 * z, z)
        if f > WIDTH_FRACTION:
            if forced:
                return 0, (j, v[0])
            return j, None
    raise ValueError(('uncovered orbit', forced))

def run():
    # The two elementary large-integer power comparisons straddle log_2(3)-1.
    require(2 ** 1584961 < 3 ** 1000000 < 2 ** 1584964, 'slope bracket')
    lo, hi = arrangement(LO), arrangement(HI)
    require([name for _, name in lo] == [name for _, name in hi], 'changing arrangement')
    # All cuts vary affinely in the enclosed slope and none cross: each open cell
    # and each isolated boundary point has the same complete labeled itinerary.
    slope = (LO + HI) / 2
    cells = [f for f, _ in arrangement(slope)]
    points = cells[:-1] + [(a+b)/2 for a, b in zip(cells, cells[1:])]
    returns = set()
    max_delay = 0
    for f in points:
        delay, stats = visit(slope, f)
        max_delay = max(max_delay, delay)
        if stats:
            returns.add(stats)
    require({n for n, e in returns} == {12, 41, 53}, 'unexpected forced-return lengths')
    # Uniform energy <= (3^(999/1000))^n on every forced-return segment.
    for n, e in returns:
        require(e**1000 < 3**(999*n), 'insufficient strict exponent margin')
    return {'slope_bracket': [str(LO), str(HI)], 'width':'99/50',
            'cells_including_isolated_endpoints': len(points),
            'max_initial_delay': max_delay, 'returns': sorted(returns),
            'energy_exponent_over_log3': '999/1000'}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
