#!/usr/bin/env python3
"""Exact fifth-pass certificate generator; standard library, no orbit conjecture."""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

DEPTH = 16
CORE = 1 << 16


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def valuation(n: int, p: int) -> int:
    need(n > 0, "valuation domain")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def rank(n: int) -> int:
    need(n >= 1, "rank domain")
    z = 2*n+1
    return z*z // 3**valuation(z, 3)


def step(n: int) -> int:
    return (3*n+1)//2 if n & 1 else n//2


def walk(n: int, word: str) -> int:
    for bit in word:
        need(n % 2 == int(bit), "physical parity guard")
        n = step(n)
        need(n > 0, "positive physical state")
    return n


def word(code: int, length: int) -> str:
    return "".join(str((code >> i) & 1) for i in range(length))


def crt(r: int, modulus: int, s: int, other: int) -> int:
    return (r + modulus * ((s-r)*pow(modulus, -1, other) % other)) % (modulus*other)


def ordinary_lift(r: int, j: int, h: int, unit: int, lift: int) -> int:
    m = 3**(h+1)
    s = ((unit*3**h-1)*pow(2, -1, m)) % m
    n = crt(r, 1 << j, s, m)
    if n == 0:
        n += (1 << j)*m
    return n + lift*(1 << j)*m


def section_return(n: int) -> tuple[int, str]:
    need(n > 1 and n % 3 == 1, "section domain")
    if n % 4 == 0:
        return n//4, "00"
    m = n if n & 1 else n//2
    a = valuation(m+1, 2)
    y = (3**a*((m+1) >> a)-1)//2
    return y, ("" if n & 1 else "0") + "1"*a + "0"


def first_section_from_odd(n: int) -> tuple[int, str]:
    need(n > 0 and n & 1, "odd section entry")
    a = valuation(n+1, 2)
    return (3**a*((n+1) >> a)-1)//2, "1"*a+"0"


def compile_rules() -> tuple[list[dict], list[list[int]]]:
    # Each tuple is (shifted remainder, odd count, low-bit-first word code).
    rows = [(1, 1, 1)]
    prefixes: list[tuple[int, int]] = []
    tiles: list[dict] = []
    layers: list[list[int]] = []
    for j in range(1, DEPTH+1):
        by_b: dict[int, dict[int, int]] = defaultdict(dict)
        for b, q, code in rows:
            choices = by_b[b]
            choices[q] = min(code, choices.get(q, code))
        hits = 0
        fresh = []
        for b, q, code in rows:
            if q+2 not in by_b[b]:
                continue
            hits += 1
            if any(code & ((1 << k)-1) == old for k, old in prefixes):
                continue
            a = (b-(1 << j)+3**q)//2
            r = -a*pow(3**q, -1, 1 << j) % (1 << j)
            n0 = crt(r, 1 << j, 4, 9)
            need(n0 >= 13, "positive quotient progression")
            fresh.append(dict(j=j, r=r, v=word(code, j),
                              w=word(by_b[b][q+2], j), B=b, q=q,
                              n0=n0, x0=(n0-4)//9,
                              source_step=9*(1 << j), quotient_step=1 << j))
        fresh.sort(key=lambda t: t["r"])
        for t in fresh:
            prefixes.append((j, sum(int(b) << i for i, b in enumerate(t["v"]))))
        tiles.extend(fresh)
        layers.append([j, len(rows), len(by_b), hits, len(fresh)])
        if j < DEPTH:
            rows = ([(b+(1 << j), q, c) for b, q, c in rows] +
                    [(3*b+(1 << j), q+1, c+(1 << j)) for b, q, c in rows])
    return tiles, layers


def test_rules(tiles: list[dict]) -> dict:
    rows = []
    for index, tile in enumerate(tiles):
        for h in (2, 3, 12):
            for unit in (1, 2):
                for lift in (0, 1):
                    n = ordinary_lift(tile["r"], tile["j"], h, unit, lift)
                    x = (n-4)//9
                    need(n == 9*x+4 and x > 0 and x & 1, "ordinary quotient")
                    need(valuation(2*n+1, 3) == h, "exact ternary depth")
                    endpoint = walk(n, tile["v"])
                    need(endpoint == walk(x, tile["w"]), "shared endpoint")
                    need(rank(n) == 9*rank(x), "exact rank cancellation")
                    if h == 2:
                        y, w = first_section_from_odd(x)
                        need(walk(x, w) == y and y % 3 == 1 and rank(y) < rank(x),
                             "depth-zero witness returns to section with lower rank")
                    rows.append([index, h, unit, lift, n, x, endpoint])
    return dict(cases=len(rows), sha256=digest(rows))


def core_check(tiles: list[dict]) -> dict:
    counts: Counter = Counter()
    rows = []
    old_h2_hits = []
    for n in range(1, CORE+1):
        h = valuation(2*n+1, 3)
        v = w = ""
        if n == 1:
            tag, x = "base", 1
        elif h == 0:
            tag = "h0"
            if n & 1:
                x, v = first_section_from_odd(n)
            else:
                x, v = step(n), "0"
        elif h == 1:
            tag = "h1"
            x, v = section_return(n)
        elif n % 2 == 0:
            tag, x, v, w = "even_high", (n-1)//3, "0", "1"
        else:
            x = (n-4)//9
            tile = next((t for t in tiles if n % (1 << t["j"]) == t["r"]), None)
            tag = "homogeneous" if tile is not None else "unresolved_lift"
            if tile is not None:
                v, w = tile["v"], tile["w"]
                if h == 2 and n % 1296 in (139, 427, 571, 859, 1003):
                    old_h2_hits.append(n)
            need(x > 0 and rank(n) == 9*rank(x), "candidate quotient rank")
        if tag not in ("base", "unresolved_lift"):
            need(rank(x) < rank(n), "certified decrease")
            need(walk(n, v) == walk(x, w), "normalization diagram")
        counts[tag] += 1
        rows.append([n, tag, x, v, w])
    return dict(cutoff=CORE, counts=dict(sorted(counts.items())), sha256=digest(rows),
                previous_h2_residual_hits=old_h2_hits)


def shield_check() -> dict:
    rows = []
    for length in (1, 2, 4, 8, 16, 32, 64):
        h = 3*length
        for lift in (0, 1, 7):
            n = ordinary_lift(21, 7, h, 1, lift)
            x = (n-4)//9
            need(valuation(2*n+1, 3) == h, "shield exact depth")
            need(walk(n, "1000001") == walk(x, "1011100"), "shield merger")
            need(rank(n) == 9*rank(x), "shield quotient")
            y = n
            for j in range(1, length+1):
                y = step(y)
                need(valuation(2*y+1, 3) <= j-1, "prefix valuation bound")
                need(4**length*rank(y) > 3*9**length*rank(n), "uniform forward barrier")
            rows.append([length, h, lift, n, x, y])
    return dict(cases=len(rows), forward_steps=sum(r[0] for r in rows),
                sha256=digest(rows), rows=rows)


def phase_check() -> list[dict]:
    def trajectory(n: int) -> list[int]:
        out = [n]
        for _ in range(1000):
            if out[-1] == 1:
                return out
            out.append(step(out[-1]))
        raise ValueError("phase test exhausted finite guard")
    out = []
    for n in (13, 859):
        x = (n-4)//9
        left, right = trajectory(n), trajectory(x)
        positions = {a: i for i, a in enumerate(right)}
        i = next(i for i, y in enumerate(left) if y in positions)
        k = positions[left[i]]
        need((len(left)-len(right)) % 2 == 1, "opposite eventual two-cycle phases")
        # Check the finite portion as well as recording the parity proof input.
        a, b = n, x
        for _ in range(max(len(left), len(right))+2):
            need(a != b, "unexpected synchronous meeting")
            a, b = step(a), step(b)
        out.append(dict(n=n, x=x, Pn=rank(n), Px=rank(x),
                        tau_n=len(left)-1, tau_x=len(right)-1,
                        first_merge=[i, k, left[i]],
                        paths_sha256=digest([left, right])))
    return out


def build() -> tuple[dict, dict]:
    tiles, layers = compile_rules()
    rule_tests, core, shield, phases = test_rules(tiles), core_check(tiles), shield_check(), phase_check()
    coverage = sum(1 << (DEPTH-t["j"]) for t in tiles)
    h2_coverage = sum(1 << (DEPTH-t["j"]) for t in tiles if t["r"] % 16 == 11)
    scope = dict(collatz_proved=False, complete_merging_cover=False,
                 max_word_length=DEPTH, rank_domain="all positive integers",
                 quotient="(n-4)/9", exact_depths_for_rule_replay=[2, 3, 12])
    counts = dict(prefix_free_rules=len(tiles), covered_odd_residues=coverage,
                  odd_residues=1 << (DEPTH-1), covered_h2_dyadic_factor=h2_coverage,
                  h2_dyadic_factor=1 << (DEPTH-4), rule_replay_cases=rule_tests["cases"],
                  shield_cases=shield["cases"], shield_forward_steps=shield["forward_steps"])
    full = dict(schema=1, scope=scope, counts=counts, word_layers=layers, tiles=tiles,
                rule_tests=rule_tests, core=core, shield=shield, phase_controls=phases)
    examples = [next(t for t in tiles if t["j"] == j and t["r"] == r)
                for j, r in ((7, 21), (10, 587))]
    compact = dict(schema=1, scope=scope, counts=counts, word_layers=layers,
                   examples=examples, core=core, rule_tests=rule_tests,
                   shield={k: v for k, v in shield.items() if k != "rows"},
                   phase_controls=phases, tiles_sha256=digest(tiles),
                   full_payload_sha256=digest(full))
    compact["semantic_sha256"] = digest(compact)
    return compact, full


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--full-output", type=Path)
    args = parser.parse_args()
    compact, full = build()
    if args.check:
        need(json.loads(args.check.read_text()) == compact, "canonical report mismatch")
    for path, obj in ((args.output, compact), (args.full_output, full)):
        if path:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(obj, sort_keys=True, separators=(",", ":"))+"\n")
    print("PASS", compact["semantic_sha256"])
    print(json.dumps(compact["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
