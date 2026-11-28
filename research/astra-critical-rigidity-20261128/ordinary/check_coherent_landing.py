"""Replay ternary transplantation and both continued-clock constructions."""

from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3 * x + 1) / 2 if x.numerator % 2 else x / 2


def landing(x):
    clock = 0
    while x.denominator != 1:
        x = step(x)
        clock += 1
    return clock


def low_predecessor(x):
    return 2 * x if 2 * x <= 1 else (2 * x - 1) / 3


def high_predecessor(x):
    e = 1
    scale = 2
    while scale * x <= 2:
        scale *= 2
        e += 1
    y = (scale * x - 1) / 3
    require(Fraction(1, 3) < y <= 1, "high-predecessor range")
    z = y
    for date in range(e):
        require(z.numerator % 2 == (date == 0), "high native word")
        z = step(z)
    require(z == x, "high native endpoint")
    return y, e


def transplant():
    targets = 0
    inverse_dates = 0
    physical_landing_replays = 0
    maximal_delay = 0
    exact_log_costs = 0
    for n in range(1, 6):
        q = 3**n
        full_log_costs = set()
        for m in range(1, q):
            if not m % 3:
                continue
            old = Fraction(m, q)
            old_time = landing(old)
            full_order = 2 * q // 3
            if n <= 4:
                dlog = 0
                residue = m
                while residue != 1 and dlog <= full_order:
                    residue = (2 * residue) % q
                    dlog += 1
                require(dlog < full_order, "full-height dlog exists")
                full_log_costs.add(dlog)
            for k in range(1, min(n, 3) + 1):
                modulus = 3**k
                order = 2 * modulus // 3
                seen = set()
                x = old
                for e in range(order):
                    a = x.numerator % modulus
                    require(a not in seen and a == pow(2, e, modulus) * m % modulus,
                            "transplanted ternary digit")
                    seen.add(a)
                    require(x.denominator % q == 0 and 0 < x <= 1, "admissible lift")
                    require(landing(x) == old_time + e, "preserved entire physical landing")
                    targets += 1
                    physical_landing_replays += 1
                    maximal_delay = max(maximal_delay, e)
                    y = low_predecessor(x)
                    require(step(y) == x, "native inverse identity")
                    x = y
                    inverse_dates += 1
                require(seen == {a for a in range(modulus) if a % 3},
                        "complete cylinder cover")
        if n <= 4:
            require(full_log_costs == set(range(2 * q // 3)), "all necessary costs")
            exact_log_costs += len(full_log_costs)
    return {"transplanted_targets": targets, "native_inverse_dates": inverse_dates,
            "landing_replays": physical_landing_replays, "max_checked_delay": maximal_delay,
            "distinct_full_height_dlog_costs_by_height": exact_log_costs}


def extensions():
    raw = 0
    accelerated = 0
    triple_guards = 0
    all_odd = 0
    for n in range(1, 7):
        q = 3**n
        for m in range(1, q):
            if not m % 3:
                continue
            old = Fraction(m, q)
            x = old
            odd = 0
            for e in range(1, 73):
                y = low_predecessor(x)
                require(step(y) == x, "native preimage")
                odd += int(y.denominator != x.denominator)
                require(y.denominator == q * 3**odd and 3 * odd <= e + 6,
                        "low inverse grade budget")
                x = y
                raw += 1
            x = old
            previous = 0
            for index in range(12):
                y, e = high_predecessor(x)
                require(y.denominator == 3 * x.denominator, "high denominator advance")
                if index:
                    require(e in (2, 3), "high division pair range")
                if index >= 2 and previous == 3:
                    require(e == 2, "high triple must be followed by double")
                    triple_guards += 1
                previous = e
                x = y
                accelerated += 1
    for n in range(3, 41):
        q = 3**n
        for k in range(1, 4):
            modulus = 3**k
            if q < (1 << n) * modulus:
                continue
            for a in range(1, modulus):
                if not a % 3:
                    continue
                dyadic = 1 << n
                m = -q % dyadic
                m += dyadic * (((a - m) * pow(dyadic, -1, modulus)) % modulus)
                require(0 < m <= q and m % modulus == a and landing(Fraction(m, q)) == n,
                        "all-odd CRT fast landing")
                all_odd += 1
    return {"unit_interval_reverse_dates": raw, "upper_odd_inverse_steps": accelerated,
            "three_then_two_guards": triple_guards, "exact_minimum_crt_witnesses": all_odd}


if __name__ == "__main__":
    print(json.dumps({"transplant": transplant(), "extension": extensions()},
                     sort_keys=True, indent=2))
