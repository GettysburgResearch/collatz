"""Min-plus recurrence on all ternary cells and fixed ordinary controls."""
import hashlib
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def odd_step(x):
    numerator = 3*x + 1
    e = (abs(numerator) & -abs(numerator)).bit_length() - 1
    return numerator // (1 << e), e


def tropical_step(prev):
    q = 3*len(prev)
    p = 2*q//3
    units = [1]
    for _ in range(1, p):
        units.append(2*units[-1] % q)
    require(len(set(units)) == p and 2*units[-1] % q == 1, "unit cycle")
    first = []
    for r in units:
        v = prev[(2*r-1)//3 % len(prev)] if r % 3 == 2 else None
        first.append(None if v is None else 1+v)
    # Shortest forward distance on the doubling cycle to an allowed e=1 edge.
    costs = first + first
    for i in range(2*p-2, -1, -1):
        if costs[i+1] is not None:
            routed = 1+costs[i+1]
            if costs[i] is None or routed < costs[i]:
                costs[i] = routed
    out = [None]*q
    for i, r in enumerate(units):
        require(costs[i] is not None, "finite unit minimum")
        out[r] = costs[i]
    return out


def direct_step(prev):
    q = 3*len(prev)
    p = 2*q//3
    out = []
    for z in range(q):
        power = z
        best = None
        for e in range(1, p+1):
            power = 2*power % q
            if power % 3 == 1:
                cost = prev[(power-1)//3]
                if cost is not None and (best is None or cost+e < best):
                    best = cost+e
        out.append(best)
    return out


def sibling(y, j):
    s = 4**j
    return s*y+(s-1)//3


def main():
    sources = (1, 3, 27, 97, 703, 871, 6171, 77031)
    current = {x: (x, 0, 0) for x in sources}
    stop = {}
    for x in sources:
        y = x
        k = 0
        while y != 1 and k < 2000:
            y, _ = odd_step(y)
            k += 1
        require(y == 1, "known-good source")
        stop[x] = k
    prev = [0]
    rows = []
    for n in range(1, 13):
        table = tropical_step(prev)
        if n <= 4:
            require(table == direct_step(prev), "independent full period search")
        q = len(table)
        digest = hashlib.sha256()
        for v in table:
            digest.update((65535 if v is None else v).to_bytes(2, 'big'))
        tracked = []
        for x, (a, total, defect) in list(current.items()):
            a, e = odd_step(a)
            total += e
            minimum = table[a % q]
            new_defect = total-minimum
            require(new_defect >= defect, "persistent defect")
            current[x] = (a, total, new_defect)
            near = [table[sibling(a,j) % q] for j in range(1, 4)]
            tracked.append([x,a,total,minimum,near])
        signed = {}
        for a in (-1, -5, -7):
            row = [table[sibling(a,j) % q] for j in range(5)]
            signed[a] = row
        require(signed[-1][0] == n, "all-one exact optimum")
        vals = [v for v in table if v is not None]
        rows.append({"n": n, "finite_cells": len(vals),
                     "min_max": [min(vals), max(vals)],
                     "all_cell_minima_sha256": digest.hexdigest(),
                     "positive_source_target_total_min_near_siblings": tracked,
                     "signed_target_and_four_siblings_minima": signed})
        prev = table
    print(json.dumps({"scope": "finite tropical recurrence only",
                      "nonunit_minimum": None, "verified_odd_times_to_one": stop,
                      "layers": rows}, indent=2))


if __name__ == "__main__":
    main()
