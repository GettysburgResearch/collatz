"""Exact three-dimensional certificates for a quartic or quintic descent."""
from fractions import Fraction
from itertools import combinations, product
from math import lcm
from check_power_coverage import require


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(a, factor):
    return tuple(x*factor for x in a)


def sub(a, b):
    return add(a, scale(b, -1))


def integral(row):
    den = lcm(*(x.denominator for x in row))
    return tuple(int(x*den) for x in row)


def cross(x, y):
    return (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0])


def dot(x, y):
    return sum(i*j for i, j in zip(x, y))


def feasible(constraints):
    # Each affine row is constant plus a dot product, constrained >=0.
    # All queried regions are bounded, hence a nonempty one has a vertex.
    rows = list(map(integral, constraints))
    for a, b, c in combinations(rows, 3):
        u, v, w = cross(b[1:], c[1:]), cross(c[1:], a[1:]), cross(a[1:], b[1:])
        den = dot(a[1:], u)
        if den:
            nums = tuple(-a[0]*i-b[0]*j-c[0]*k for i,j,k in zip(u,v,w))
            if all((den*r[0]+dot(r[1:], nums))*den >= 0 for r in rows):
                return True
    return False


def check(exponents, drop, tests):
    c = Fraction(485, 306)
    gamma = c-1
    unit, *gains = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    heights = [unit]
    costs = []
    for exponent, gain in zip(exponents, gains):
        costs.append(sub(heights[-1], scale(gain, (exponent-c)/gamma)))
        heights.append(add(heights[-1], scale(gain, exponent)))
    floor = 1-drop+drop*(drop-1)*c/gamma
    domain = gains+costs+[sub(heights[-1], scale(unit, floor))]
    failures = []
    for i, j, count in tests:
        savings = [scale(gains[i], count), gains[j], scale(heights[i+1], 1/c)]
        cost = add(scale(costs[i], count), costs[j])
        margins = [sub(saving, cost) for saving in savings]
        if count == 2:
            margins += [sub(saving, gains[i]) for saving in savings]
        divisibility = sub(scale(gains[j], exponents[j]/gamma), costs[i])
        require(not feasible(domain+[scale(divisibility, -1)]))
        failures.append([scale(margin, -1) for margin in margins])
    require(all(not feasible(domain+list(cuts)) for cuts in product(*failures)))


if __name__ == "__main__":
    c = Fraction(485, 306)
    def amp(e):
        return 1+(c-1)/(1-c/e)
    require(amp(2)**2*amp(3) < 20*c/(c-1)-4)
    require(max(amp(2)**2*amp(4), amp(2)*amp(3)**2, amp(2)**2) < 12*c/(c-1)-3)
    for exponents, drop in [((2,2,2),5), ((3,2,2),4), ((2,3,2),4), ((2,2,3),4)]:
        check(exponents, drop, [(0,1,1)])
    check((2,2,2), 4, [(0,1,2), (1,2,1), (0,2,1)])
    print("five three-rise configurations excluded by exact rational halfspaces")
