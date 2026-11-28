"""Exact controls for simple arrivals, the signed pole, and aligned local fields."""

from collections import defaultdict
from fractions import Fraction as Q


def checked(condition, name):
    if not condition:
        raise ValueError(name)


def odd_step(x):
    n = 3 * x + 1
    e = (n & -n).bit_length() - 1
    return n >> e, e


def unit_row(x):
    return (0, 1, 2)[x % 3]


def finite_graph():
    """Enumerate signed genuine streams, with a fixed finite initial weight."""
    starts = list(range(-249, 250, 2))
    full, simple = [], []
    periods = {}
    for n in range(24):
        full.append(defaultdict(Q))
        simple.append(defaultdict(Q))
    for x in starts:
        z, weight, path = x, Q(unit_row(x), abs(x)), []
        first_visits = {}
        for n in range(len(full)):
            full[n][z] += weight
            if z not in first_visits:
                first_visits[z] = n
            else:
                i = first_visits[z]
                lap = path[i:n]
                if z not in periods:
                    lam = Q(1)
                    for v in lap:
                        lam *= Q(3 * v, 3 * v + 1)
                    periods[z] = (len(lap), lam)
            if len(set(path + [z])) == n + 1:
                simple[n][z] += weight
            path.append(z)
            weight *= Q(3 * z, 3 * z + 1)
            z, _ = odd_step(z)
    checks = positive = negative = multistate = 0
    for n, row in enumerate(full):
        for z, total in row.items():
            q, lam = periods.get(z, (n + 1, 0))
            corrected = total - (lam * full[n - q].get(z, 0) if q <= n else 0)
            checked(simple[n].get(z, 0) == corrected, ("lap subtraction", n, z))
            checks += 1
            if q <= n:
                positive += z > 0
                negative += z < 0
                multistate += q > 1
    checked(positive and negative and multistate, "period coverage")
    return checks, multistate


def fair_rows(max_depth):
    """Forward pushforward using the exact periodic infinite gap sums."""
    rows = [[Q(1)]]
    for depth in range(1, max_depth + 1):
        modulus = 3**depth
        period = 2 * modulus // 3
        denominator = 2**period - 1
        new = [Q(0)] * modulus
        old = rows[-1]
        for e in range(1, period + 1):
            mass = Q(2 ** (period - e), denominator)
            inv = pow(2, -e, modulus)
            for r, density in enumerate(old):
                z = ((3 * r + 1) * inv) % modulus
                new[z] += 3 * mass * density
        checked(sum(new) == modulus, ("normalization", depth))
        rows.append(new)
    return rows


def signed_pole(rows):
    checks = 0
    for n, row in enumerate(rows[:-1]):
        q = len(row)
        next_row = rows[n + 1]
        # e=2h+1 uses period q in h modulo 3q; the omitted h=0 is literal.
        secondary = Q(0)
        for h in range(1, q + 1):
            inverse = -((2 ** (2 * h + 1) + 1) // 3)
            mass = Q(4 ** (q - h), 4**q - 1)
            secondary += mass * row[inverse % q]
        checked(Q(2, 3) * next_row[-1] == row[-1] + secondary,
                ("negative pole recurrence", n))
        # On the positive fixed point exactly e=2 must be deleted for a first hit.
        first = Q(0)
        for h in range(2, q + 2):
            inverse = (4**h - 1) // 3
            mass = 3 * Q(4 ** (q + 1 - h), 4 * (4**q - 1))
            first += mass * row[inverse % q]
        checked(first == next_row[1] - Q(3, 4) * row[1 % q],
                ("positive first arrival", n))
        checks += 2
    return checks


def states(x, n):
    result = [(x, 0)]
    for _ in range(n):
        z, e = odd_step(result[-1][0])
        result.append((z, result[-1][1] + e))
    return result


def aligned_charts():
    base = states(27, 19)
    checked(len({y for y, _ in base}) == len(base), "simple physical ray segment")
    inputs = list(range(1, 400, 2))
    histories = {x: states(x, len(base) + 2) for x in inputs}
    checked_rows = mismatches_without_clock = 0
    for k in range(-2, 3):
        previous = {}
        for j in range(3, 18):
            y, clock = base[j]
            n = j + k
            base_slope = Q(3**j, 2**clock)
            for x, hist in histories.items():
                z, word_clock = hist[n]
                if z != y:
                    continue
                relative = Q(3**n, 2**word_clock) / base_slope
                if x in previous:
                    checked(previous[x] == relative, ("stable slope", j, k, x))
                previous[x] = relative
                # Real and ternary symbols coincide on this large integral shift.
                # Its extra binary factor fixes terminal oddness and all original gaps.
                u = 3**max(k, 0) * 2 ** (clock + word_clock + 1)
                shifted = x + Q(u, 1) / relative
                target = y + base_slope * u
                checked(shifted.denominator == target.denominator == 1,
                        ("integral chart", j, k, x))
                hit, marked_clock = states(int(shifted), n)[-1]
                checked((hit, marked_clock) == (target, word_clock),
                        ("actual marked path", j, k, x))
                mismatches_without_clock += hit != y + 3**j * u
                checked_rows += 1
    checked(checked_rows > 100 and mismatches_without_clock > 100,
            "aligned chart coverage")
    return checked_rows, mismatches_without_clock


if __name__ == "__main__":
    rows, long_laps = finite_graph()
    exact_tails = signed_pole(fair_rows(5))
    charts, rejected = aligned_charts()
    print(f"PASS {rows} signed simple rows, {long_laps} longer-cycle rows, "
          f"{exact_tails} infinite-gap identities, {charts} physical charts, "
          f"{rejected} missing-clock controls rejected")
