#!/usr/bin/env python3
"""Exact finite support for CLOCK_DEFECT.md; no claim of a complete cover."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

DEPTH = 18
SCOPE = "finite corpus; unbounded ordinary heights, fixed h=2; full closure OPEN"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def valuation(n: int, p: int = 3) -> int:
    require(n != 0, "zero valuation argument")
    n = abs(n)
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def step(n: int) -> int:
    return (3*n+1)//2 if n & 1 else n//2


def rank(n: int) -> int:
    require(n > 0, "nonpositive source")
    return (2*n+1)**2 // 3**valuation(2*n+1)


def data(word: str) -> tuple[int, int, int, int]:
    q = A = B = 0
    for i, s in enumerate(word):
        bit = int(s)
        q += bit
        A = 3**bit*A + bit*2**i
        B = 3**bit*B + 2**i
    return len(word), q, A, B


def replay(n: int, word: str) -> int:
    for s in word:
        require(n % 2 == int(s), "physical parity mismatch")
        n = step(n)
    return n


def crt(a: int, m: int, b: int, q: int) -> int:
    return a + m*((b-a)*pow(m, -1, q) % q)


def bases(res: int, j: int) -> list[int]:
    return sorted(crt(res, 2**j, b, 27) for b in (4, 22))


def candidate(word: str, res: int, kind: str) -> dict | None:
    j, q, A, B = data(word)
    if kind == "forward":
        D = B
        delta = valuation(D)
        hx = delta
        alpha, beta = Fraction(3**q, 2**j), Fraction(B, 2**j)
    else:
        trailing = len(word)-len(word.rstrip("0"))
        if trailing < 2 or trailing % 2:
            return None
        D = B-2**(j-1)
        if not D:
            return None
        delta = valuation(D)
        if delta < 1:
            return None
        hx = delta-1
        alpha = Fraction(3**(q-1), 2**(j-1))
        beta = Fraction(D, 3*2**(j-1))
    if delta >= q+2:
        return None  # Unfrozen ternary cancellation is not assumed generic.
    limit = Fraction(9, 3**hx)*alpha**2
    if limit >= 1:
        return None
    n = bases(res, j)[0]
    zx = alpha*(2*n+1)+beta
    if zx.denominator != 1 or zx.numerator % 2 != 1:
        return None
    x = (zx.numerator-1)//2
    if x <= 0 or rank(x) >= rank(n):
        return None
    return dict(word=word, residue=res, j=j, q=q, A=A, B=B,
                kind=kind, D=D, delta=delta, hx=hx, minimum_n=n,
                witness=x, limit_num=limit.numerator, limit_den=limit.denominator)


def corpus() -> list[dict]:
    active = [("1101", 11)]
    rules = []
    for j in range(4, DEPTH+1):
        nxt = []
        for word, res in sorted(active, key=lambda z: z[1]):
            row = candidate(word, res, "forward") or candidate(word, res, "odd_predecessor")
            if row:
                rules.append(row)
                continue
            if j < DEPTH:
                for lift in (res, res+2**j):
                    endpoint = replay(lift, word)
                    nxt.append((word+str(endpoint % 2), lift))
        active = nxt
    return rules


def rule_replays(rules: list[dict]) -> list[list[int]]:
    rows = []
    for i, row in enumerate(rules):
        j, word = row["j"], row["word"]
        for base in bases(row["residue"], j):
            for t in (0, 1, 7, 10**6):
                n = base + 27*2**j*t
                y = replay(n, word)
                x = y if row["kind"] == "forward" else (2*y-1)//3
                require(valuation(2*n+1) == 2 and rank(x) < rank(n), "rank ray")
                if row["kind"] != "forward":
                    require(x % 2 == 1 and step(x) == y, "unequal-clock merge")
                require(valuation(2*x+1) == row["hx"], "frozen output valuation")
                rows.append([i, n, x, y])
    return rows


def inverse(y: int) -> list[int]:
    ans = [2*y]
    if y % 3 == 2:
        ans.append((2*y-1)//3)
    return ans


def rigidity() -> tuple[list[list], int, int]:
    rows, pairs, lower = [], 0, 0
    for M in range(1, 9):
        H = 0
        while 3**H < 12**M:
            H += 1
        for label, res in (("odd_run", 2**M-1), ("mixed", 21 % 2**M)):
            for unit in (1, 2):
                b = (unit*3**H-1)*pow(2, -1, 3**(H+1)) % 3**(H+1)
                n = crt(res, 2**M, b, 3**(H+1)) + 2**M*3**(H+1)
                require(valuation(2*n+1) == H, "CRT precision")
                y, v = n, ""
                local_pairs = local_lower = 0
                for j in range(M+1):
                    front = {y: ""}
                    qv, Bv = data(v)[1], data(v)[3]
                    for k in range(M+1):
                        for x, w in sorted(front.items()):
                            qw, Bw = data(w)[1], data(w)[3]
                            d = min(j, k)
                            D = 2**(k-d)*Bv-2**(j-d)*Bw
                            require(abs(D) < 3**M, "defect size")
                            if D:
                                require(rank(x)*3 > rank(n)*4, "nonzero defect barrier")
                            if rank(x) < rank(n):
                                p = qw-qv
                                require(j == k and Bv == Bw and p > 0, "rigidity")
                                require(2*n+1 == 3**p*(2*x+1), "homogeneous rank strip")
                                require(label != "odd_run", "all-odd lower-clock obstruction")
                                local_lower += 1
                            local_pairs += 1
                        if k < M:
                            front = {z: str(z % 2)+w for x, w in front.items() for z in inverse(x)}
                    v += str(y % 2)
                    y = step(y)
                rows.append([M, H, label, unit, n, local_pairs, local_lower])
                pairs += local_pairs
                lower += local_lower
    return rows, pairs, lower


def cost_family() -> tuple[list[list[int]], int]:
    rows, steps = [], 0
    for H in (3, 6, 12, 24, 48, 96):
        a = 4*H
        M = 0
        while 12**(M+1) <= 3**H:
            M += 1
        for unit in (1, 2):
            b = (unit*3**H-1)*pow(2, -1, 3**(H+1)) % 3**(H+1)
            base = crt(2**a-1, 2**(a+1), b, 3**(H+1))
            for t in (1, 2):
                n = base + t*2**(a+1)*3**(H+1)
                require(valuation(2*n+1) == H and valuation(n+1, 2) == a, "cost CRT")
                y = replay(n, "1"*a+"0")
                require(rank(y)*256**H < rank(n)*243**H, "adaptive rank bound")
                rows.append([H, a, M+1, unit, t, n, y])
                steps += a+1
    return rows, steps


def named_cases() -> list[list[int]]:
    v = "1101110101011100"
    rows = []
    for t in (0, 1, 7, 1000, 10**30):
        n, x = 859+1769472*t, 517+1062882*t
        require(replay(n, v) == step(x) == 776+1594323*t, "named tile")
        require(rank(x)*8 < rank(n)*3, "named rank factor")
        rows.append([2, t, n, x])
    for H in (3, 4, 10, 30):
        for unit in (1, 2):
            b = (unit*3**H-1)*pow(2, -1, 3**(H+1)) % 3**(H+1)
            n = crt(859, 2**16, b, 3**(H+1)) + 2**16*3**(H+1)
            y = replay(n, v)
            x = (2*y-1)//3
            require(step(x) == y and rank(x) > rank(n), "false all-height extension")
            rows.append([H, unit, n, x])
    return rows


def digest(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def build() -> tuple[dict, dict]:
    rules = corpus()
    residual = [n for n in range(11, 2**DEPTH, 16)
                if not any(n % 2**r["j"] == r["residue"] for r in rules)]
    ordinary = sorted(crt(r, 2**DEPTH, b, 81) for r in residual for b in (4, 22, 31, 49, 58))
    replays = rule_replays(rules)
    rigid, pairs, lower = rigidity()
    costs, steps = cost_family()
    full = dict(rules=rules, residual_dyadic=residual, residual_ordinary=ordinary, rule_replays=replays,
                rigidity=rigid, cost_family=costs, named_cases=named_cases())
    report = dict(schema=1, scope=SCOPE, depth=DEPTH, rules=len(rules),
                  forward_rules=sum(r["kind"] == "forward" for r in rules),
                  asymmetric_rules=sum(r["kind"] == "odd_predecessor" for r in rules),
                  covered_dyadic=2**(DEPTH-4)-len(residual), residual_dyadic=len(residual),
                  old_residual_modulus=81*2**DEPTH, old_residual_classes=5*len(residual), first_old_residual=ordinary[0],
                  rule_replays=len(replays), rigidity_cases=len(rigid), rigidity_pairs=pairs,
                  homogeneous_lower_pairs=lower, cost_cases=len(costs), cost_forward_steps=steps,
                  named_cases=len(full["named_cases"]),
                  parts={k:digest(v) for k,v in full.items()}, full_sha256=digest(full))
    report["semantic_sha256"] = digest(report)
    return report, full


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--full-output", type=Path)
    args = parser.parse_args()
    report, full = build()
    if args.check:
        require(json.loads(args.check.read_text()) == report, "canonical report mismatch")
    for path, obj in ((args.output, report), (args.full_output, full)):
        if path:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(obj, sort_keys=True, separators=(",", ":"))+"\n")
    print("PASS", report["semantic_sha256"])
    print(json.dumps({k:v for k,v in report.items() if k not in ("parts", "semantic_sha256")}, sort_keys=True))


if __name__ == "__main__":
    main()
