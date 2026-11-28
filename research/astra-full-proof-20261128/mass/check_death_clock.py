"""Verify the signed first-exit identities by two finite enumerations."""
from collections import defaultdict
from fractions import Fraction
import json


def require(test, message):
    if not test:
        raise ValueError(message)


def step(value):
    t = 3 * value + 1
    gap = (t & -t).bit_length() - 1
    return t >> gap, gap


def ordinary_record_sources(qmax):
    bound = 128**qmax // 81**qmax
    rows = defaultdict(set)
    for source in range(1, bound + 1, 2):
        value, total = source, 0
        for h in range(4 * qmax + 1):
            if 4 * total > 7 * h:
                break
            if value == 1:
                q = 2 * h - total
                if q <= qmax:
                    rows[q].add(source)
                    require(81**q * source <= 128**q, "inverse height cap")
                break
            value, gap = step(value)
            total += gap
    return rows


def inverse_record_sources(qmax):
    rows = defaultdict(set)
    rows[0].add(1)
    for q in range(1, qmax + 1):
        for h in range(q, 4 * q + 1):
            total = 2 * h - q
            final_debt = 7 * h - 4 * total

            def visit(value, k, used):
                if k == h:
                    if used == total:
                        require(value not in rows[q], "duplicate inverse history")
                        rows[q].add(value)
                    return
                if value % 3 == 0:
                    return
                max_gap = total - used - (h - k - 1)
                for e in range(1, max_gap + 1):
                    numerator = (value << e) - 1
                    if numerator % 3 != 0:
                        continue
                    x = numerator // 3
                    if x == 1 or 7 * (k + 1) - 4 * (used + e) > final_debt:
                        continue
                    visit(x, k + 1, used + e)

            visit(1, 0, 0)
    return rows


def finite_trace(depth):
    current = [(0, 0, 1)]
    counts = []
    for n in range(depth):
        births = Fraction()
        loss = Fraction()
        represented = []
        nxt = []
        for total, carry, source in current:
            kids = set()
            for e in range(1, 7 * (n + 1) // 4 - total + 1):
                new_total = total + e
                new_carry = 3 * carry + (1 << total)
                modulus = 1 << (new_total + 1)
                m = ((1 << new_total) - new_carry) * pow(3**(n+1), -1, modulus) % modulus
                nxt.append((new_total, new_carry, m))
                kids.add(m)
                if m != source:
                    births += Fraction(1, m)
            if source not in kids:
                loss += Fraction(1, source)
                represented.append(source)
        left = sum((Fraction(1, row[2]) for row in current), Fraction())
        right = sum((Fraction(1, row[2]) for row in nxt), Fraction())
        require(right == left + births - loss, "birth/death ledger")
        record_deaths, anomalies = set(), set()
        for m in represented:
            v, clock, earlier_hit = m, 0, None
            for j in range(n + 1):
                if v == 1 and earlier_hit is None:
                    earlier_hit = (j, clock)
                v, e = step(v)
                clock += e
                require((4 * clock <= 7 * (j + 1)) == (j < n), "wrong physical exit")
            if earlier_hit is None:
                anomalies.add(m)
            else:
                h, a = earlier_hit
                require(8 * h - 4 * a + 1 == n + 1, "death clock")
                record_deaths.add(m)
        counts.append({"date": n + 1, "record_deaths": sorted(record_deaths),
                       "anomalous_count": len(anomalies), "live_count": len(nxt)})
        current = nxt
    return counts


def main():
    qmax = 12
    first = ordinary_record_sources(qmax)
    second = inverse_record_sources(qmax)
    require(first == second, "ordinary / inverse record sets differ")
    require(27 in first[12], "known nontrivial first-hit control")
    ledger = finite_trace(8)
    for row in ledger:
        t = row["date"]
        predicted = first[(t-1)//4] if t % 4 == 1 else set()
        require(set(row["record_deaths"]) == predicted, "full trace / inverse record")
    print(json.dumps({"max_record_grade": qmax,
                      "physical_height_cap": 128**qmax // 81**qmax,
                      "records": {str(q): sorted(first[q]) for q in range(qmax + 1)},
                      "full_trace": ledger}, indent=2))


if __name__ == "__main__":
    main()
