#!/usr/bin/env python3
"""Exact bounded evidence for BOUNDARY_FAN.md; not a Collatz proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

PARENT = "908fdca1fe21456f8c6d476b31b74c8552670395"
CORE = 1 << 18
FIVE = {139, 427, 571, 859, 1003}
AS = (2, 3, 4, 5, 8, 12)
LS = (1, 2, 4, 8, 16, 32)
TILES = (
    (30379, 34992, 32, 11, 9, "10010", 5, 1024, 2187),
    (3019, 11664, 32, 29, 27, "10110", 3, 1024, 2187),
    (29371, 34992, 64, 31, 27, "110010", 4, 4096, 6561),
)
LIFTS = (0, 1, 7, 1000, 10**30, 3**100)

def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)

def enc(x: object) -> bytes:
    return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()

def digest(x: object) -> str:
    return hashlib.sha256(enc(x)).hexdigest()

def vp(n: int, p: int) -> int:
    need(n > 0 and p > 1, "valuation domain")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e

def rank(n: int) -> int:
    need(n > 0, "positive rank input")
    z = 2*n+1
    return z*z // 3**vp(z, 3)

def step(n: int) -> int:
    return (3*n+1)//2 if n % 2 else n//2

def replay(n: int, word: str) -> int:
    for bit in word:
        need(n % 2 == int(bit), "wrong physical parity")
        n = step(n)
        need(n > 0, "nonpositive physical state")
    return n

def ret(n: int) -> int:
    need(n > 1 and n % 3 == 1, "section-return input")
    if n % 4 == 0:
        return n//4
    m = n if n % 2 else n//2
    a = vp(m+1, 2)
    return (3**a*((m+1)//2**a)-1)//2

def fan(n: int) -> list[int]:
    h = vp(2*n+1, 3)
    need(n > 1 and h >= 1, "fan input")
    u = (2*n+1)//3**h
    out = [2*(2**j*3**(h-j)*u-1) for j in range(h)]
    z = 2**h*u-1
    if z % 3 == 1:
        out.append(z)
    return out

def least(n: int) -> int:
    h = vp(2*n+1, 3)
    u = (2*n+1)//3**h
    return 2**h*u-1 if (2**(h+1)*u-1) % 3 == 0 else 3*2**h*u-2

def boundary(n: int) -> list[int]:
    h = vp(2*n+1, 3)
    u = (2*n+1)//3**h
    e = 3*2**h*u-2
    out = [e]
    if (2**(h+1)*u-1) % 3 == 0:
        out.append(2**h*u-1)
    return out

def best(n: int) -> int:
    bs = boundary(n)
    return min([n, *bs, *(least(x) for x in bs)], key=rank)

def affine(word: str) -> tuple[int, int, int]:
    q = A = 0
    for i, bit in enumerate(word):
        if bit == "1":
            q += 1
            A = 3*A + 2**i
    return q, A, 2*A+2**len(word)-3**q

def proof_family(a: int, H: int, L: int, lift: int) -> list[object]:
    j = a+3
    m2 = 2**((a+1)*L+1)
    D = 3**a-2**(a+1)
    b = 3**a-2**a
    r2 = (-b*pow(D, -1, m2)) % m2
    m3 = 3**(a+H+2)
    c = 2**(a+3)-7*3**a
    r3 = ((3**(a+H+1)-c)*pow(2**(a+4), -1, m3)) % m3
    mod = m2*m3
    n = r2 + m2*((r3-r2)*pow(m2, -1, m3) % m3) + (lift+1)*mod
    A = 5*3**a-2**(a+2)
    need((2**j*n-A) % 3**(a+1) == 0, "ancestor integrality")
    x = (2**j*n-A)//3**(a+1)
    word = "10"+"1"*a+"0"
    need(x > 1 and x % 2 == 1 and n % 2 == 1, "positive odd family")
    need(vp(2*x+1, 3) == H and vp(2*n+1, 3) == a, "exact family depths")
    u = (2*n+1)//3**a
    need(vp(2**(a+1)*u-1, 3) == 1, "second valuation")
    need(replay(x, word) == n and ret(ret(x)) == n, "ancestor path")
    need(4*rank(x) < rank(n), "quarter-rank gain")
    need(rank(x)*3**(H+a+2) < rank(n)*4**(a+3), "strict analytic gain")
    y = n
    forward = []
    for i in range(1, L+1):
        y = replay(y, "1"*a+"0")
        need(D*y+b == 3**(a*i)*(D*n+b)//2**((a+1)*i), "return formula")
        need(vp(2*y+1, 3) == a and y > n and rank(y) > rank(n), "forward barrier")
        forward.append(y)
    return [a, H, L, lift, n, x, word, forward]

def build() -> dict:
    core_rows = []
    falls = residual = removed = nongreedy = 0
    by_rule = [0, 0, 0]
    for n in range(4, CORE+1, 3):
        z = best(n)
        fall = rank(z) < rank(n)
        falls += int(fall)
        g = least(n)
        ng = fall and min(rank(g), rank(least(g))) >= rank(n)
        nongreedy += int(ng)
        if n % 1296 in FIVE:
            residual += 1
            bits = [(64*n-13) % 3**7 == 0,
                    (64*n-31) % 3**6 == 0,
                    (128*n-35) % 3**7 == 0]
            need(fall == any(bits), "exact depth-two residual classification")
            need(sum(bits) <= 1, "disjoint new cylinders")
            removed += int(fall)
            by_rule = [x+int(b) for x, b in zip(by_rule, bits)]
        core_rows.append([n, z, rank(z), int(ng)])
    # Complete direct two-generation comparison at unbounded-size test inputs.
    large = []
    for h in (1, 2, 3, 4, 8, 16, 32, 64):
        for u in (1, 5, 7, 11, 23, 95, 191):
            n = (3**h*u-1)//2
            if n <= 1:
                continue
            fs = fan(n)
            all_nodes = {n, *fs}
            for s in fs:
                all_nodes.update(fan(s))
            exact = min(all_nodes, key=rank)
            need(best(n) == exact, "large complete-fan comparison")
            large.append([h, u, n, exact, len(all_nodes)])
    families = [proof_family(a, H, L, t) for a in AS
                for H in (a+2, a+7, 2*a+9) for L in LS for t in (0, 1)]
    tile_rows = []
    for r, M, c, d, den, word, Hmin, bnum, bden in TILES:
        for t in LIFTS:
            n = r+M*t
            need((c*n-d) % den == 0, "tile integer")
            x = (c*n-d)//den
            need(n % 1296 in FIVE and vp(2*n+1, 3) == 2, "tile residual")
            need(vp(2*x+1, 3) >= Hmin, "tile depth")
            need(replay(x, word) == n and ret(ret(x)) == n, "tile path")
            need(bden*rank(x) < bnum*rank(n), "tile rank ratio")
            tile_rows.append([r, M, t, n, x, word])
    cycle_rows = []
    for code in range(32):
        word = "".join(str((code >> i) & 1) for i in range(5))
        q, A, B = affine(word)
        den = 32-3**q
        need(not (den > 0 and A > 0 and A % den == 0), "unexpected positive T^5 fixed point")
        cycle_rows.append([word, q, A, den])
    n = 29371
    g1, g2 = least(n), least(least(n))
    winner = best(n)
    need((g1, g2, winner) == (26107, 104428, 69619), "nongreedy countertest")
    need(min(rank(g1), rank(g2)) >= rank(n) > rank(winner), "nongreedy ranks")
    need(replay(winner, "110010") == n, "nongreedy physical merger")
    # Countertest: pruning every generation by the radius-two rule is unsound.
    def ball(root: int, depth: int, children) -> set[int]:
        nodes = frontier = {root}
        for _ in range(depth):
            frontier = {x for y in frontier for x in children(y)}
            nodes = nodes | frontier
        return nodes
    root = 208363
    complete3, pruned3 = ball(root, 3, fan), ball(root, 3, boundary)
    winner3, pruned_min = min(complete3, key=rank), min(pruned3, key=rank)
    need((winner3, pruned_min) == (4445077, root), "false recursive pruning countertest")
    need(replay(winner3, "100000") == root and ret(ret(ret(winner3))) == root, "three-return path")
    third_tiles = []
    for t in LIFTS:
        n3 = 208363+314928*t
        x3 = (64*n3-1)//3
        need((64*n3-1) % 3 == 0 and vp(2*x3+1, 3) >= 8, "third tile depth")
        need(n3 % 1296 == 1003 and replay(x3, "100000") == n3, "third tile parity")
        need(6561*rank(x3) < 4096*rank(n3), "third tile rank")
        third_tiles.append([t, n3, x3])
    third = {"root": root, "full_min": winner3, "boundary_only_min": pruned_min,
             "ranks": [rank(root), rank(winner3)],
             "full_nodes": sorted(complete3), "boundary_nodes": sorted(pruned3),
             "tiles": third_tiles}
    full = {"core": core_rows, "large": large, "families": families,
            "tiles": tile_rows, "cycle5": sorted(cycle_rows), "third_radius": third,
            "nongreedy": [n, g1, g2, winner, rank(n), rank(winner)]}
    body = {
        "schema": "X-ASTRA-006-v1", "parent": PARENT,
        "scope": "finite checks; all-parameter proofs PROPOSED; complete cover OPEN",
        "core": {"cutoff": CORE, "sources": len(core_rows), "inverse_depth_le_2_descents": falls,
                 "no_inverse_depth_le_2_descent": len(core_rows)-falls,
                 "nongreedy_successes": nongreedy, "rows_sha256": digest(core_rows)},
        "prior_depth_two_residual": {"sources": residual, "newly_removed": removed,
                 "remaining": residual-removed, "by_rule": by_rule},
        "large_fans": {"cases": len(large), "rows_sha256": digest(large)},
        "families": {"cases": len(families), "forward_returns": sum(r[2] for r in families),
                 "parameter_a": list(AS), "parameter_L": list(LS), "rows_sha256": digest(families)},
        "tiles": {"cases": len(tile_rows), "rows_sha256": digest(tile_rows)},
        "cycle5": {"words": 32, "positive_fixed_points": 0, "rows_sha256": digest(sorted(cycle_rows))},
        "nongreedy": full["nongreedy"],
        "third_radius": {"root": root, "full_min": winner3, "boundary_only_min": pruned_min,
                         "tile_cases": len(third_tiles), "rows_sha256": digest(third)},
        "full_payload_sha256": digest(full),
    }
    return {"body": body, "sha256": digest(body), "full": full}

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--check", type=Path)
    ap.add_argument("--full-output", type=Path)
    args = ap.parse_args()
    report = build()
    compact = {k: report[k] for k in ("body", "sha256")}
    if args.check:
        need(json.loads(args.check.read_text()) == compact, "committed report mismatch")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(enc(compact)+b"\n")
    if args.full_output:
        args.full_output.write_bytes(enc(report["full"])+b"\n")
    print("PASS", compact["sha256"])
    print(json.dumps(report["body"], indent=2))

if __name__ == "__main__":
    main()
