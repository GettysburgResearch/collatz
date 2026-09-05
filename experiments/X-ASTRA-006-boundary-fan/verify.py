#!/usr/bin/env python3
"""Separate physical replay. Imports no generator or repository module."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)

def encoding(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()

def sha(value: object) -> str:
    return hashlib.sha256(encoding(value)).hexdigest()

def valuation(x: int, p: int) -> int:
    require(x > 0, "valuation must be finite")
    power = p
    e = 0
    while x % power == 0:
        e += 1
        power *= p
    return e

def P(n: int) -> int:
    require(n > 0, "ordinary positive rank")
    z = 2*n+1
    return z*z//(3**valuation(z, 3))

def T(n: int) -> int:
    if n & 1:
        return (n+n+n+1)//2
    return n//2

def path(n: int, count: int) -> tuple[str, int]:
    out = []
    for _ in range(count):
        out.append(str(n & 1))
        n = T(n)
        require(n > 0, "positive orbit state")
    return "".join(out), n

def R(n: int) -> int:
    require(n > 1 and n % 3 == 1, "section source")
    y = n
    for _ in range(2*n.bit_length()+5):
        y = T(y)
        if y % 3 == 1:
            return y
    raise ValueError("finite first-return formula violated")

def inverse(y: int) -> list[int]:
    """Walk actual reverse shortcut branches until their first section exit."""
    require(y > 1 and y % 3 == 1, "inverse endpoint")
    result = []
    cur = 2*y
    while True:
        even = 2*cur
        require(even % 3 == 1 and T(even) == cur, "even inverse edge")
        result.append(even)
        num = 2*cur-1
        require(num % 3 == 0, "class-2 odd inverse edge")
        odd = num//3
        require(odd > 0 and odd & 1 and T(odd) == cur, "odd inverse edge")
        if odd % 3 == 1:
            result.append(odd)
            break
        if odd % 3 == 0:
            break
        require(odd < cur, "reverse walk must terminate")
        cur = odd
    require(len(set(result)) == len(result), "duplicate fan source")
    return result

def minimum(y: int) -> int:
    return min(inverse(y), key=P)

def all_two(y: int) -> tuple[int, int]:
    level1 = inverse(y)
    nodes = {y, *level1}
    for s in level1:
        nodes.update(inverse(s))
    return min(nodes, key=P), len(nodes)

def invmod(a: int, m: int) -> int:
    r0, r1, s0, s1 = a, m, 1, 0
    while r1:
        q = r0//r1
        r0, r1, s0, s1 = r1, r0-q*r1, s1, s0-q*s1
    require(r0 == 1, "coprime CRT moduli")
    return s0 % m

def word_residue(word: str) -> int:
    """Construct the source one binary digit at a time, not by final inversion."""
    residue = image = odds = 0
    for i, symbol in enumerate(word):
        bit = int(symbol)
        if image % 2 != bit:
            residue += 1 << i
            image += 3**odds
        require(image % 2 == bit, "parity lift")
        image = T(image)
        odds += bit
    return residue

def family(a: int, H: int, L: int, lift: int) -> list[object]:
    guard = ("1"*a+"0")*L+"1"
    r2 = word_residue(guard)
    m2 = 1 << len(guard)
    m3 = 3**(a+H+2)
    coeff = 1 << (a+4)
    rhs = 3**(a+H+1)+7*3**a-(1 << (a+3))
    r3 = rhs*invmod(coeff, m3) % m3
    base = r2 + m2*((r3-r2)*invmod(m2, m3) % m3)
    n = base+(lift+1)*m2*m3
    num = (1 << (a+3))*n-5*3**a+(1 << (a+2))
    require(num % 3**(a+1) == 0, "ancestor integral")
    x = num//3**(a+1)
    actual_word, endpoint = path(x, a+3)
    require(actual_word == "10"+"1"*a+"0" and endpoint == n, "physical two-return bridge")
    require(R(R(x)) == n, "exact section clock")
    require(valuation(2*x+1, 3) == H and valuation(2*n+1, 3) == a, "exact source depths")
    require(4*P(x) < P(n), "strict quarter gain")
    require(P(x)*3**(H+a+2) < P(n)*4**(a+3), "analytic ancestor bound")
    u = (2*n+1)//3**a
    require(valuation((1 << (a+1))*u-1, 3) == 1, "second endpoint valuation")
    values = []
    y = n
    for _ in range(L):
        bits, nxt = path(y, a+1)
        require(bits == "1"*a+"0" and nxt == R(y), "whole expanding return")
        require(nxt > y and P(nxt) > P(n), "rank delay")
        require(valuation(2*nxt+1, 3) == a, "forward depth")
        y = nxt
        values.append(y)
    return [a, H, L, lift, n, x, actual_word, values]

def reconstruct() -> dict:
    prior = {139, 427, 571, 859, 1003}
    core = []
    total_fall = ng_count = residual = removed = 0
    by_rule = [0, 0, 0]
    for n in range(4, 262145, 3):
        winner, _ = all_two(n)  # full fan, not the boundary shortcut
        lower = P(winner) < P(n)
        g = minimum(n)
        nongreedy = lower and min(P(g), P(minimum(g))) >= P(n)
        total_fall += int(lower)
        ng_count += int(nongreedy)
        if n % 1296 in prior:
            residual += 1
            # Independent progression form, not the generator's valuation tests.
            bits = [(n-30379) % 34992 == 0,
                    (n-3019) % 11664 == 0,
                    (n-29371) % 34992 == 0]
            require(lower == any(bits) and sum(bits) <= 1, "all-height residual rule comparison")
            removed += int(lower)
            by_rule = [v+int(b) for v, b in zip(by_rule, bits)]
        core.append([n, winner, P(winner), int(nongreedy)])
    large = []
    for h in (1, 2, 3, 4, 8, 16, 32, 64):
        for u in (1, 5, 7, 11, 23, 95, 191):
            n = (3**h*u-1)//2
            if n <= 1:
                continue
            winner, size = all_two(n)
            # Verify the claimed pruning formula independently against the entire ball.
            e = 3*2**h*u-2
            bs = [e]
            z = 2**h*u-1
            if z % 3 == 1:
                bs.append(z)
            pruned = min([n]+bs+[minimum(s) for s in bs], key=P)
            require(winner == pruned, "boundary-only minimization")
            large.append([h, u, n, winner, size])
    aas, lengths = (2, 3, 4, 5, 8, 12), (1, 2, 4, 8, 16, 32)
    families = [family(a, H, L, lift) for a in aas for H in (a+2, a+7, 2*a+9)
                for L in lengths for lift in (0, 1)]
    specs = ((30379, 34992, 32, 11, 9, "10010", 5, 1024, 2187),
             (3019, 11664, 32, 29, 27, "10110", 3, 1024, 2187),
             (29371, 34992, 64, 31, 27, "110010", 4, 4096, 6561))
    tiles = []
    for r, mod, c, d, den, expected, Hmin, bn, bd in specs:
        for lift in (0, 1, 7, 1000, 10**30, 3**100):
            n = r+mod*lift
            require((c*n-d) % den == 0, "ordinary tile integrality")
            x = (c*n-d)//den
            bits, end = path(x, len(expected))
            require(bits == expected and end == n and R(R(x)) == n, "physical tile")
            require(valuation(2*n+1, 3) == 2 and valuation(2*x+1, 3) >= Hmin, "tile valuations")
            require(bd*P(x) < bn*P(n), "strict tile rank bound")
            tiles.append([r, mod, lift, n, x, bits])
    cycle_rows = []
    seen = set()
    for residue in range(32):
        n = residue
        bits = []
        for _ in range(5):
            bits.append(str(n % 2))
            n = T(n)
        word = "".join(bits)
        q = word.count("1")
        A = 32*n-3**q*residue  # from actual physical endpoints
        den = 32-3**q
        require(not (den > 0 and A > 0 and A % den == 0), "positive T^5 fixed point")
        cycle_rows.append([word, q, A, den])
        seen.add(word)
    require(len(seen) == 32, "all five-bit physical cylinders")
    cycle_rows.sort()
    n = 29371
    g1, g2 = minimum(n), minimum(minimum(n))
    winner, _ = all_two(n)
    require((g1, g2, winner) == (26107, 104428, 69619), "nongreedy example")
    require(min(P(g1), P(g2)) >= P(n) > P(winner), "nongreedy inequality")
    root = 208363
    # Build the full and the proposed pruned trees independently at depth three.
    all_nodes, boundary_nodes = {root}, {root}
    all_front, boundary_front = [root], [root]
    for _ in range(3):
        all_front = [x for y in all_front for x in inverse(y)]
        all_nodes.update(all_front)
        nxt = []
        for y in boundary_front:
            fs = inverse(y)
            # Last even exit and optional odd exit, identified by physical parity.
            nxt.append([x for x in fs if x % 2 == 0][-1])
            nxt.extend(x for x in fs if x % 2 == 1)
        boundary_front = nxt
        boundary_nodes.update(nxt)
    winner3, pruned_min = min(all_nodes, key=P), min(boundary_nodes, key=P)
    require((winner3, pruned_min) == (4445077, root), "recursive pruning is false")
    require(path(winner3, 6) == ("100000", root) and R(R(R(winner3))) == root, "three-return path")
    third_tiles = []
    for lift in (0, 1, 7, 1000, 10**30, 3**100):
        n3 = 208363+314928*lift
        require((64*n3-1) % 3 == 0, "third-tile integrality")
        x3 = (64*n3-1)//3
        require(path(x3, 6) == ("100000", n3), "third-tile physical path")
        require(n3 % 1296 == 1003 and valuation(2*x3+1, 3) >= 8, "third-tile valuations")
        require(6561*P(x3) < 4096*P(n3), "third-tile strict rank bound")
        third_tiles.append([lift, n3, x3])
    third = {"root": root, "full_min": winner3, "boundary_only_min": pruned_min,
             "ranks": [P(root), P(winner3)],
             "full_nodes": sorted(all_nodes), "boundary_nodes": sorted(boundary_nodes),
             "tiles": third_tiles}
    full = {"core": core, "large": large, "families": families, "tiles": tiles,
            "cycle5": cycle_rows, "third_radius": third, "nongreedy": [n, g1, g2, winner, P(n), P(winner)]}
    body = {
        "schema": "X-ASTRA-006-v1", "parent": "908fdca1fe21456f8c6d476b31b74c8552670395",
        "scope": "finite checks; all-parameter proofs PROPOSED; complete cover OPEN",
        "core": {"cutoff": 262144, "sources": len(core), "inverse_depth_le_2_descents": total_fall,
                 "no_inverse_depth_le_2_descent": len(core)-total_fall,
                 "nongreedy_successes": ng_count, "rows_sha256": sha(core)},
        "prior_depth_two_residual": {"sources": residual, "newly_removed": removed,
                 "remaining": residual-removed, "by_rule": by_rule},
        "large_fans": {"cases": len(large), "rows_sha256": sha(large)},
        "families": {"cases": len(families), "forward_returns": sum(x[2] for x in families),
                 "parameter_a": list(aas), "parameter_L": list(lengths), "rows_sha256": sha(families)},
        "tiles": {"cases": len(tiles), "rows_sha256": sha(tiles)},
        "cycle5": {"words": 32, "positive_fixed_points": 0, "rows_sha256": sha(cycle_rows)},
        "nongreedy": full["nongreedy"],
        "third_radius": {"root": root, "full_min": winner3, "boundary_only_min": pruned_min,
                         "tile_cases": len(third_tiles), "rows_sha256": sha(third)},
        "full_payload_sha256": sha(full),
    }
    return {"body": body, "sha256": sha(body)}

def validate(report: dict, expected: dict) -> None:
    require(set(report) == {"body", "sha256"}, "unexpected schema keys")
    require(report["sha256"] == sha(report["body"]), "digest failure")
    require(report == expected, "physical reconstruction or scope mismatch")

def self_test(expected: dict) -> int:
    mutations = [
        lambda b: b.update(scope="Collatz proved"),
        lambda b: b["core"].update(cutoff=131072),
        lambda b: b["prior_depth_two_residual"].update(remaining=0),
        lambda b: b["families"].update(cases=215),
        lambda b: b["families"].update(parameter_a=[2]),
        lambda b: b["cycle5"].update(positive_fixed_points=1),
        lambda b: b["nongreedy"].__setitem__(3, 104428),
        lambda b: b["third_radius"].update(boundary_only_min=4445077),
    ]
    count = 0
    for change in mutations:
        altered = copy.deepcopy(expected)
        change(altered["body"])
        altered["sha256"] = sha(altered["body"])
        try:
            validate(altered, expected)
        except ValueError:
            count += 1
        else:
            raise ValueError("resealed corruption accepted")
    return count

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("report", type=Path)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    expected = reconstruct()
    validate(json.loads(args.report.read_text()), expected)
    print("INDEPENDENT IMPLEMENTATION REPLAY PASS", expected["sha256"])
    if args.self_test:
        print("RESEALED CORRUPT REPORTS REJECTED", self_test(expected))

if __name__ == "__main__":
    main()
