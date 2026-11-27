"""Independent literal replay for the binary two-clock anchor review."""

from collections import Counter
from math import comb
import json


def check(test):
    if not test:
        raise ArithmeticError("binary review condition failed")


def path(n, h):
    odds = 0
    for _ in range(h):
        if n & 1:
            n = (3 * n + 1) >> 1
            odds += 1
        else:
            n >>= 1
    return n, odds


def hit_cycle(n):
    for h in range(512):
        if n in (1, 2):
            return h
        n, _ = path(n, 1)
    raise ArithmeticError("control interval exceeded")


def profiles():
    rows = []
    for h in (5, 10, 15):
        p = 3*h // 5
        buckets = Counter()
        for x in range(2**h, 2**(h+1)):
            y = x
            bits = []
            for _ in range(h):
                bits.append(y % 2)
                y, _ = path(y, 1)
            if sum(bits) != p:
                continue
            trailing = 0
            for length, bit in enumerate(reversed(bits), 1):
                trailing += bit
                if h*trailing > p*length:
                    break
            else:
                carry = 2**h*y - 3**p*x
                check(0 <= carry < 32*2**h and bits[0] == 1)
                buckets[y] += 1
        retained = sum(buckets.values())
        check(h*retained >= comb(h, p))
        check((max(buckets.values())-1)*3**p <= 32*2**h)
        rows.append({"clock": h, "odd_count": p, "retained_words": retained,
                     "distinct_first_endpoints": len(buckets), "maximum_bucket": max(buckets.values())})
    return rows


def critical_profiles():
    rows = []
    for h in (8, 12, 15):
        p = 0
        while 3 ** p < 2 ** h:
            p += 1
        for scale in (1, 3):
            block_rows = []
            for block in (1, 2, 3):
                buckets = Counter()
                unit_buckets = Counter()
                for u in range(block << h, (block + 1) << h):
                    n = scale*u
                    y, count = n, 0
                    floor = n
                    valid = True
                    for j in range(1, h + 1):
                        count += y % 2
                        y = (3*y+1)//2 if y % 2 else y//2
                        floor = min(floor, y)
                        if h*count < p*j:
                            valid = False
                            break
                    if not valid or count != p:
                        continue
                    check(u % 2 and floor >= n)
                    carry = 2**h*y - 3**p*n
                    check(0 <= 2*carry <= h*3**p)
                    buckets[y] += 1
                    if u % 3:
                        unit_buckets[y] += 1
                check(h*sum(buckets.values()) >= comb(h, p))
                check(2*max(buckets.values()) <= 2+h)
                check((h+2)*h*len(buckets) >= 2*comb(h, p))
                block_rows.append((len(buckets), max(buckets.values()), len(unit_buckets)))
            check(3*(h+2)*h*max(row[2] for row in block_rows) >= 4*comb(h, p))
            rows.append({"clock": h, "odd_count": p, "arm_factor": scale,
                         "minimum_endpoints_across_three_blocks": min(row[0] for row in block_rows),
                         "largest_multiplicity": max(row[1] for row in block_rows),
                         "largest_unit_endpoint_count": max(row[2] for row in block_rows)})
    return rows


def main():
    phases = Counter()
    anchors = 0
    exchanges = 0
    unit_inputs = 0
    for r in range(1, 512, 2):
        if r % 3 == 0:
            continue
        anchors += 1
        first = max(1, hit_cycle(r), hit_cycle(3 * r))
        for h in (first, first + 1):
            low, first_count = path(r, h)
            upper, second_count = path(3 * r, h)
            phases[f"{low},{upper}"] += 1
            for steps in range(1, 6):
                for delta in (0, 1):
                    current = r + (5 << (h + 2 * steps + delta))
                    for j in range(steps):
                        t, rem = divmod(current - r, 2 ** (h + 2))
                        check(t > 0 and rem == 0)
                        following = r + (3 * t << h)
                        check(4 * following - 3 * current == r)
                        check(following < current and following % 2 == 1 and following % 3 == r % 3)
                        a, pa = path(current, h + 2)
                        b, pb = path(following, h)
                        c, pc = path(3 * current, h + 2)
                        d, pd = path(3 * following, h)
                        check(a == b and c == d)
                        check(pa == pb + 1 == first_count + 1)
                        check(pc == pd + 1 == second_count + 1)
                        unit_inputs += bool(current % 3)
                        exchanges += 1
                        current = following
                    check(current - r == 5 * 3 ** steps * 2 ** (h + delta))
                    check((current - r) % 2 ** (h + 2) != 0)
    print(json.dumps({"anchors": anchors, "phase_pairs": dict(sorted(phases.items())),
                      "literal_exchanges": exchanges, "exchanges_at_original_ternary_unit": unit_inputs,
                      "maximum_same_anchor_steps": 5, "profile_controls": profiles(),
                      "critical_grade_controls": critical_profiles()}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
