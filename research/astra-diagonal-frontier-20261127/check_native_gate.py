#!/usr/bin/env python3
"""Independent finite controls for the actual native gate; no all-time claim.

The direct orbit enumerator and the affine cylinder tree use different paths.
Every comparison raises explicitly and is active under python -O.
"""
from collections import Counter
from fractions import Fraction
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3*x+1)//2 if x & 1 else x//2


def direct(x, n):
    y, q, passed = x, 0, True
    for j in range(1, n+1):
        q += y & 1
        y = step(y)
        passed = passed and 4*j <= 7*q
    return y, q, passed


def rational(value):
    return f"{value.numerator}/{value.denominator}"


def digest_rational(value):
    # Avoid decimal conversion limits for large exact denominators.
    encoded = f"{value.numerator:x}/{value.denominator:x}".encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def run():
    nodes = {1: (1, 0)}
    debt_counts = Counter({0: 1})
    previous_mass = Fraction(1)
    previous_reserve = Fraction(8)
    reserves = [previous_reserve]
    fixed_cutoff_checks = 0
    losses = Fraction(0)
    rows = [{"clock": 0, "count": 1, "mass": "1/1", "reserve": "8/1"}]
    for n in range(15):
        brute = {x: (y, q) for x in range(1, 2**n+1)
                 for y, q, passed in [direct(x, n)] if passed}
        require(nodes == brute, f"actual source tree mismatch at {n}")
        require(Counter(7*q-4*n for _, q in nodes.values()) == debt_counts,
                f"Bernoulli debt counts mismatch at {n}")
        exponential_reserve = sum((Fraction(25,24)**(7*q-4*n)
                                   for _, q in nodes.values()), Fraction())/2**n
        require(exponential_reserve <= Fraction(99,100)**n, "exponential reserve")
        require(previous_reserve <= 48*Fraction(99,100)**n, "linear reserve decay")
        descending = iter(sorted(nodes, reverse=True))
        current = next(descending, None)
        high_mass = Fraction()
        for old_clock in range(n, -1, -1):
            while current is not None and current > 2**old_clock:
                high_mass += Fraction(1, current)
                current = next(descending, None)
            require(high_mass+previous_reserve <= reserves[old_clock],
                    "future sources charged to the old reserve")
            fixed_cutoff_checks += 1
        if n == 14:
            break
        children = {}
        for x, (y, q) in nodes.items():
            for side in (0, 1):
                source = x + side*2**n
                terminal = y + side*3**q
                q_next = q + (terminal & 1)
                if 4*(n+1) <= 7*q_next:
                    require(source not in children, "duplicate physical source")
                    children[source] = (step(terminal), q_next)
        birth = sum((Fraction(1, x) for x in children if x not in nodes), Fraction())
        death = sum((Fraction(1, x) for x in nodes if x not in children), Fraction())
        mass = sum((Fraction(1, x) for x in children), Fraction())
        reserve = sum((Fraction(2*(7*q-4*(n+1))+8, 2**(n+1))
                       for _, q in children.values()), Fraction())
        require(mass == previous_mass + birth-death, "same-source mass identity")
        require(birth <= Fraction(len(nodes), 2**n), "principal newborn bound")
        require(reserve+Fraction(len(nodes), 2**n) <= previous_reserve,
                "reserve discharge bound")
        losses += death
        require(mass+reserve+losses <= 9, "global loss budget")
        rows.append({"clock": n+1, "count": len(children),
                     "mass_float": float(mass), "mass_sha256_hex": digest_rational(mass),
                     "birth_float": float(birth), "death_float": float(death),
                     "reserve": rational(reserve), "envelope_float": float(mass+reserve),
                     "cumulative_loss_float": float(losses)})
        next_debts = Counter()
        for d, count in debt_counts.items():
            next_debts[d+3] += count
            if d >= 4:
                next_debts[d-4] += count
        debt_counts = next_debts
        nodes, previous_mass, previous_reserve = children, mass, reserve
        reserves.append(reserve)

    lift_checks = 0
    for x in range(1, 49):
        for n in range(11):
            y, q, passed = direct(x, n)
            for t in (0, 1, 2, 3, 17):
                yt, qt, pt = direct(x+2**n*t, n)
                require((yt, qt, pt) == (y+3**q*t, q, passed), "cylinder lift")
                lift_checks += 1

    death27 = next(n for n in range(1, 200) if not direct(27, n)[2])
    require(death27 == 86, "27 native first-failure clock changed")
    require(direct(27, 85)[2], "27 must pass all first 85 native prefixes")
    return {"status": "PASS", "scope": "finite exact controls, not universal extinction",
            "direct_tree_max_clock": 14, "cylinder_lift_checks": lift_checks,
            "exponential_reserve_clocks": 15, "fixed_cutoff_checks": fixed_cutoff_checks,
            "source27_first_gate_failure": death27, "rows": rows}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
