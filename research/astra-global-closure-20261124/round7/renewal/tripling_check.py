"""Check the empty tripling endpoint and the ordinary five-clock common cylinder."""

import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def trace(x, h):
    p = 0
    for _ in range(h):
        p += x % 2
        x = step(x)
    return x, p


def main():
    checks = 0
    for x in range(1, 1024, 2):
        z = 3*x
        for _ in range(64):
            z = step(z)
            require(z % 3 != 0, "positive clock at a multiple of three")
            checks += 1
    for t in range(512):
        x = 32*t+23
        y = 27*t+20
        require(trace(x, 5) == (y, 3) and trace(3*x, 5) == (y, 2), "five-clock prefix")
        for h in (0, 1, 7, 23):
            z, a = trace(y, h)
            require(trace(x, 5+h) == (z, 3+a) and trace(3*x, 5+h) == (z, 2+a),
                    "common suffix")
    rows = []
    for q, p in ((1, 52), (5, 52), (7, 52), (11, 52)):
        e = 2*p
        A, B = 3**p, 2**e
        lo, hi = ((2*q-1)*B+2*A-1)//(2*A), q*B//A
        count = 0
        for x in range(lo+(55-lo)%192, hi+1, 192):
            if trace(x, e) == (q, p):
                require(x % 6 == 1 and trace(3*x, e) == (q, p-1), "central pair")
                count += 1
        require(count > 0, "empty tested central row")
        rows.append({"q": q, "clock": e, "source_odd_count": p,
                     "companion_odd_count": p-1, "ordinary_pairs": count})
    return {"status": "PASS", "positive_clock_unit_checks": checks,
            "five_clock_cylinder_lifts": 512, "common_suffix_checks": 2048,
            "bounded_offset_fixed_target_rows": rows}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
