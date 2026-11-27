"""Exact integer replay of the smaller-parent cost rows and their full interval."""

import json


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


def child(parent, gap):
    power = 1 << gap
    partner = 3 * parent + (2 if gap % 2 else -2)
    numerator = power * partner - 1
    require(numerator % 3 == 0, ("inverse divisibility", parent, gap))
    result = numerator // 3
    require(result > 0 and result % 2 == 1, ("positive odd", result))
    require((3 * result + 1) >> gap == partner, ("exact edge", parent, gap))
    return result


def check_row(seed, max_cost):
    rows = [[seed]]
    interval_total = 0
    checked = 0
    for cost in range(1, max_cost + 1):
        power = 1 << cost
        row = [child(parent, gap) for gap in range(1, cost + 1)
               for parent in rows[cost - gap]]
        endpoints = set(row)
        require(len(endpoints) == power // 2, ("distinct endpoints", seed, cost))
        require({v % power for v in endpoints} == set(range(1, power, 2)),
                ("odd residue cover", seed, cost))
        for value in row:
            shifted = 3 * (value - power * seed) + 1
            require((-3 * power <= shifted and 2 * shifted <= -3 * power)
                    or 0 <= shifted <= 3 * power, ("two real bands", seed, cost, value))
        first = power * seed + power // 2
        full_interval = range(first + 1 + (first % 2), power * (seed + 1), 2)
        require(all(v in endpoints for v in full_interval), ("full interval", seed, cost))
        interval_total += len(full_interval)
        checked += len(endpoints)
        rows.append(row)
    return {"seed": seed, "max_cost": max_cost, "row_points": checked,
            "required_interval_points": interval_total}


if __name__ == "__main__":
    result = [check_row(seed, 15) for seed in (1, 3, 5, 17, 65, 463)]
    print(json.dumps(result, indent=2))
