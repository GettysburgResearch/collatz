#!/usr/bin/env python3
"""Exact finite support for the proposed minimum-rank theorems. No closure claim."""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

CUTOFF = 1 << 18
RESIDUES = [139, 427, 571, 859, 1003]
HEIGHTS = [6, 7, 12, 24, 64]
HORIZONS = [1, 2, 3, 8, 16, 32, 64]
LIFTS = [0, 1, 7, 1000, 10**30]


def val(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("zero has no finite valuation")
    n, v = abs(n), 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def rank(n: int) -> int:
    assert n >= 1 and n % 3 == 1
    z = 2*n + 1
    return z*z // 3**val(z, 3)


def ret(n: int) -> tuple[int, str]:
    assert n >= 1 and n % 3 == 1
    if n == 1:
        return 1, ""
    if n % 4 == 0:
        return n//4, "00"
    m = n if n % 2 else n//2
    a = val(m+1, 2)
    return (3**a*((m+1)//2**a)-1)//2, ("" if n % 2 else "0")+"1"*a+"0"


def replay(n: int, word: str) -> int:
    for bit in word:
        assert n % 2 == int(bit)
        n = (3*n+1)//2 if bit == "1" else n//2
    return n


def inverse(n: int) -> list[int]:
    if n == 1:
        return [4]
    h = val(2*n+1, 3)
    u = (2*n+1)//3**h
    out = [2*(2**j*3**(h-j)*u-1) for j in range(h)]
    z = 2**h*u-1
    if z % 3 == 1:
        out.append(z)
    return out


def affine(word: str) -> tuple[int, int, int]:
    q, a = 0, 0
    for j, bit in enumerate(word):
        if bit == "1":
            q += 1
            a = 3*a+2**j
    return len(word), q, a


def crt(r: int, m: int, s: int, n: int) -> int:
    return (r+m*((s-r)*pow(m, -1, n) % n)) % (m*n)


def digest(rows: object) -> str:
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def normal(n: int) -> tuple[str, int, str, str]:
    """Return a checked reduction, or an explicit unresolved label."""
    h, pn = val(2*n+1, 3), rank(n)
    y, w = ret(n)
    if h == 1:
        return "height_one", y, w, ""
    if n % 2 == 0:
        return "even_merge", (n-1)//3, "0", "1"
    if rank(y) < pn:
        return "forward", y, w, ""
    u = (2*n+1)//3**h
    k = val(2**(h+1)*u-1, 3)
    if k:
        x = 2**h*u-1
        if rank(x) < pn:
            return "inverse", x, "", ret(x)[1]
    if h == 2:
        a = val(n+1, 2)
        if a == 1:
            x, v = ret(y)
            return "depth_two_forward", x, w+v, ""
        if a == 2 and n % 16 == 3:
            return "depth_two_merge", (3*n-1)//8, "1100", "1"
    if (128*n-71) % 3**9 == 0:
        return "reverse_six", (64*n-49)//27, "", "100110"
    return "residual", 0, "", ""


def ball(n: int, depth: int = 4) -> list[int] | None:
    seen, front = {n: None}, [n]
    for _ in range(depth):
        nxt = []
        for y in front:
            for x in [ret(y)[0]] + inverse(y):
                if x in seen:
                    continue
                seen[x] = y
                if rank(x) < rank(n):
                    path = [x]
                    while seen[path[-1]] is not None:
                        path.append(seen[path[-1]])
                    return path[::-1]
                nxt.append(x)
        front = nxt
    return None


def meeting(n: int, x: int) -> tuple[str, str, int]:
    endpoints, y, w = {n: ""}, n, ""
    for _ in range(4):
        if y == 1:
            break
        y, v = ret(y)
        w += v
        endpoints.setdefault(y, w)
    y, w = x, ""
    for _ in range(5):
        if y in endpoints:
            return endpoints[y], w, y
        y, v = ret(y)
        w += v
    raise AssertionError("missing common endpoint")


def tile(n: int, x: int) -> dict:
    wn, wx, meet = meeting(n, x)
    j, qn, _ = affine(wn)
    k, qx, _ = affine(wx)
    hn, hx = val(2*n+1, 3), val(2*x+1, 3)
    e = max(0, hn+1-qx, hx+1-qn)
    period_n, period_x = 2**j*3**(qx+e), 2**k*3**(qn+e)
    slope = Fraction(period_x**2*3**hn, period_n**2*3**hx)
    assert rank(x) < rank(n) and slope <= 1
    for t in LIFTS:
        nn, xx = n+period_n*t, x+period_x*t
        assert replay(nn, wn) == replay(xx, wx)
        assert val(2*nn+1, 3) == hn and val(2*xx+1, 3) == hx
        assert rank(xx) < rank(nn)
    return dict(n=n, x=x, wn=wn, wx=wx, meeting=meet,
                hn=hn, hx=hx, period_n=period_n, period_x=period_x,
                slope=[slope.numerator, slope.denominator])


def build() -> dict:
    counts, rows, residual = Counter(), [], []
    h2_count = h2_residual = 0
    for n in range(4, CUTOFF+1, 3):
        label, x, wn, wx = normal(n)
        counts[label] += 1
        if x:
            assert rank(x) < rank(n)
            assert replay(n, wn) == replay(x, wx)
        else:
            residual.append(n)
        if val(2*n+1, 3) == 2:
            h2_count += 1
            assert (label == "residual") == (n % 1296 in RESIDUES)
            h2_residual += label == "residual"
        rows.append([n, label, x, wn, wx])
    core = dict(cutoff=CUTOFF, source_count=len(rows), counts=dict(sorted(counts.items())),
                h2_count=h2_count, h2_residual=h2_residual,
                row_sha256=digest(rows), first_residuals=residual[:20])
    fans = []
    for y in range(4, 388, 3):
        xs = sorted(inverse(y))
        assert len(xs) == len(set(xs))
        assert all(x <= 4*y and ret(x)[0] == y for x in xs)
        fans.append([y, xs])
    fan_summary = dict(endpoints=len(fans), sources=sum(len(r[1]) for r in fans),
                       rows_sha256=digest(fans))
    family_rows, forward_steps = [], 0
    for H in HEIGHTS:
        for L in HORIZONS:
            m2, m3 = 2**(3*L+1), 3**(H+4)
            r2 = (2**(3*L)-5) % m2
            r3 = (71+3**(H+3))*pow(128, -1, m3) % m3
            for t in [0, 1]:
                n = crt(r2, m2, r3, m3) + (t+1)*m2*m3
                x = (64*n-49)//27
                assert x > n and val(2*x+1, 3) == H
                assert val(2*n+1, 3) == 3 and val(128*n-71, 3) == H+3
                assert replay(x, "100110") == n and ret(ret(x)[0])[0] == n
                assert 4*rank(x) < rank(n)
                assert all(rank(z) >= rank(n) for z in [ret(n)[0]]+inverse(n)+inverse(ret(n)[0]))
                y = n
                for i in range(1, L+1):
                    assert val(y+1, 2) == 2
                    y = ret(y)[0]
                    assert y == 9**i*(n+5)//8**i-5
                    assert y > n and rank(y) > 3*rank(n)
                    forward_steps += 1
                family_rows.append([H, L, t, n, x, y])
    fam = dict(heights=HEIGHTS, horizons=HORIZONS, lifts=[0, 1],
               rows=len(family_rows), forward_returns=forward_steps,
               rows_sha256=digest(family_rows), example=family_rows[0])
    search_rows, search_counts, tiles = [], Counter(), []
    for n in residual[:1024]:
        path = ball(n)
        y, first_forward = n, 0
        for d in range(1, 5):
            y = ret(y)[0]
            if rank(y) < rank(n):
                first_forward = d
                break
        if path is None:
            verdict = "unresolved_at_depth_4"
        elif first_forward:
            verdict = "forward_also"
        else:
            verdict = "two_sided_only"
            tiles.append(tile(n, path[-1]))
        search_counts[verdict] += 1
        search_rows.append([n, first_forward, path, verdict])
    assert len(tiles) == 37
    # A finite-domain lookahead can correctly return unresolved; it is not a total solver.
    assert ball(121, 8) is None
    y = 121
    for d in range(1, 17):
        y = ret(y)[0]
        assert (rank(y) < rank(121)) == (d == 16)
    assert y == 40
    bounds = dict(quarter=[4096, 19683], h2_high_a=[3888, 3969],
                  h2_double_one=[361, 363], h2_second_long=[Fraction(81*98**2,256*63**2).numerator,
                                                        Fraction(81*98**2,256*63**2).denominator])
    assert all(Fraction(*z) < 1 for z in bounds.values())
    assert Fraction(*bounds['quarter']) < Fraction(1, 4)
    return dict(schema=1, scope="finite_exact_support_not_Collatz_closure",
                parent="345168de8732f6240e5c926420cee3db3b0fa137",
                residues_mod_1296=RESIDUES, core=core, fan=fan_summary,
                family=fam, rational_bounds=bounds,
                search=dict(sources=1024, radius=4, counts=dict(sorted(search_counts.items())),
                            row_sha256=digest(search_rows), unresolved_radius_8=121,
                            first_forward_drop_121=[16, 40]),
                lift_parameters=LIFTS, tiles=tiles)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError("run without -O: this checker requires assertions")
    payload = build()
    report = dict(payload=payload, sha256=digest(payload))
    if args.check:
        assert json.loads(args.check.read_text()) == report, "canonical report mismatch"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, sort_keys=True, separators=(",", ":"))+"\n")
    print("PASS", report['sha256'])
    print(json.dumps({k: payload[k] for k in ['core', 'fan', 'family', 'search']}, indent=2))


if __name__ == "__main__":
    main()
