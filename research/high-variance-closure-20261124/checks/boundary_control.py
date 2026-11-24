"""Exact finite controls for the signed-seed and oriented-boundary identities."""

from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    odd = x.numerator % 2
    return ((3 * x + 1) / 2 if odd else x / 2), odd


def entry(x):
    count = 0
    for clock in range(24):
        if x in (0, 1, 2):
            return clock, count, int(x)
        x, odd = step(x)
        count += odd
    raise ValueError(f"seed did not reach the specified finite section: {x}")


def followed(x, steps):
    x = Fraction(x)
    for _ in range(steps):
        x, _ = step(x)
    return x


def check():
    units = (1, 2, 4, 5, 7, 8)
    left = ((2,2,1), (3,2,1), (4,2,1), (2,2,0), (3,2,0), (5,2,1))
    right = ((6,2,1), (6,4,2), (4,2,1), (5,2,1), (4,2,1), (3,2,1))
    for r, l, h in zip(units, left, right):
        require(entry(Fraction(-r, 9)) == l, f"left seed {r}")
        require(entry(Fraction(9-r, 9)) == h, f"right seed {r}")

    gap_count = 0
    for s in range(13):
        k = 2*s+1
        for l in range(40):
            u = 4*l+3
            n = 2**k*u-2
            w = 3**(k-1)*u-1
            a = w//2
            require(a % 2 == 1, "missing odd meeting source")
            require(followed(n, k+2) == followed(n+1, k+2) == (3*a+1)//2,
                    f"physical forbidden-gap meet {(s,l)}")
            gap_count += 1

    transfers = 0
    for l in range(80):
        n = 4*l+2
        m = 6*l+4
        require(followed(n, 2) == followed(m, 1) and
                followed(n+1, 1) == m+1, f"tripling pair at {l}")
        n, a = 3*l+1, 4*l+1
        require(followed(a, 2) == n and
                followed(a+1, 2) == n+1, f"inverse pair at {l}")
        transfers += 2

    return {"signed_seed_pairs": len(units), "forbidden_gap_paths": gap_count,
            "oriented_transfer_pairs": transfers}


if __name__ == "__main__":
    print(json.dumps(check(), sort_keys=True))
