#!/usr/bin/env python3
"""Exact paired-comparison certificates. Standard library; no conjecture assumption."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def v2(n: int) -> int:
    require(type(n) is int and n > 0, "v2 needs a positive integer")
    return (n & -n).bit_length() - 1


def step(n: int) -> int:
    require(type(n) is int and n > 0, "positive integer state required")
    return (3*n+1)//2 if n & 1 else n//2


def trace(n: int, length: int) -> list[int]:
    require(type(length) is int and length >= 0, "invalid clock")
    out = [n]
    for _ in range(length):
        out.append(step(out[-1]))
    return out


def replay(n: int, word: str) -> int:
    for bit in word:
        require(bit in "01" and (n & 1) == int(bit), "illegal physical word")
        n = step(n)
    return n


def symbolic(a: int, b: int, word: str) -> tuple[int, int]:
    """Prove the word on ALL a*t+b, t>=0, by integer affine coefficients."""
    require(a > 0 and b > 0, "positive affine cylinder required")
    for bit in word:
        require(bit in "01" and a % 2 == 0 and b % 2 == int(bit),
                "word not uniform on entire progression")
        if bit == "1":
            a, b = 3*a, 3*b+1
        a, b = a//2, b//2
    return a, b


def transition(c: int, old: bool = False):
    """None or (status, next_parameter, common_clock, left_word, right_word)."""
    require(type(c) is int and c > 0, "positive parameter required")
    if old:
        r = v2(c+2)-1
        if r < 3:
            return None
        b = (c+2)//2**(r+1)
        z = 3**r*b
        # Derive its physical words independently by forward replay.
        length = r+3
        left = trace(9*c+2, length)
        right = trace(c, length)
        w = "".join(str(n & 1) for n in left[:-1])
        v = "".join(str(n & 1) for n in right[:-1])
        if z % 4 == 1:
            return "MERGE", (z-1)//4, length, w, v
        return "RETURN", (3**(r-1)*b-1)//4, length, w, v
    av, bv = v2(3*c-2), v2(3*c-1)
    if av >= 3 and av % 2 == 1:
        k = (av-3)//2
        b = (3*c-2)//2**(2*k+3)
        d = (3**(k+1)*b+1)//2
        w, v = "00"+"01"*k+"00", "01"+"10"*k+"11"
    elif bv >= 4 and bv % 2 == 0:
        k = (bv-4)//2
        b = (3*c-1)//2**(2*k+4)
        d = (3**(k+2)*b+1)//2
        w, v = "100"+"01"*k+"00", "110"+"10"*k+"11"
    else:
        return None
    require(d > 0, "nonpositive bridge endpoint")
    s = v2(d+1)
    z = 3**s*((d+1)//2**s)
    if z % 4 == 3:
        w, v = w+"1"*s+"01", v+"1"*s+"00"
        return "MERGE", (3*z-1)//4, len(w), w, v
    w, v = w+"1"*s+"00", v+"1"*s+"01"
    return "RETURN", (z-1)//4, len(w), w, v


def classify(c: int, old: bool = False, budget: int = 256) -> dict:
    root, total, orientation = c, 0, 0
    words = ["", ""]
    stages = []
    for _ in range(budget):
        tr = transition(c, old)
        if tr is None:
            return dict(c=root, status="OUTSIDE", terminal=c, clock=total,
                        orientation=orientation, stages=stages, words=words)
        status, d, length, w, v = tr
        require(replay(9*c+2, w) == (d if status == "MERGE" else d),
                "left endpoint failure")
        require(replay(c, v) == (d if status == "MERGE" else 9*d+2),
                "right endpoint failure")
        require(len(w) == len(v) == length, "clock failure")
        words[orientation] += w
        words[1-orientation] += v
        total += length
        stages.append(dict(c=c, status=status, d=d, clock=length))
        if status == "MERGE":
            require(replay(9*root+2, words[0]) == replay(root, words[1]) == d,
                    "whole-certificate failure")
            return dict(c=root, status="MERGE", endpoint=d, clock=total,
                        stages=stages, words=words)
        c, orientation = d, 1-orientation
    return dict(c=root, status="BUDGET", terminal=c, clock=total,
                orientation=orientation, stages=stages, words=words)


def first_exit_checks():
    count = 0
    for r in range(2, 66):
        for u in range(1, 200, 2):
            n, m = 2**r*u-1, 2**(r-1)*u-1
            a, b = trace(n, r+2)[-1], trace(m, r+1)[-1]
            if 3**r*u % 4 == 1:
                require(a == b, "good odd exit")
            else:
                c = (3**(r-1)*u-1)//4
                require((a, b) == (9*c+2, c) and c % 3 == 2, "forced H entry")
            count += 1
    return count


def ladder_checks():
    count = 0
    for r in range(2, 66):
        for j in range((r-2)//2+1):
            for u in range(1, 20, 2):
                if 3**r*u % 4 != 3:
                    continue
                n = 2**r*u-1
                m = (n-(4**(j+1)-1)//3)//2
                c = (3**(r-2*j-1)*u-1)//4
                h = c
                for _ in range(j+1):
                    h = 9*h+2
                word = "1"+"0"*(2*j)+"1"*(r-2*j-2)+"00"
                require(0 < m < n and replay(m, word) == c, "ladder lower arm")
                require(trace(n, r+2)[-1] == h, "ladder upper arm")
                count += 1
    return count


def bridge_checks():
    count = 0
    for k in range(31):
        for b in range(1, 100, 2):
            for family, numer in [("A", 2**(2*k+3)*b+2),
                                  ("B", 2**(2*k+4)*b+1)]:
                if numer % 3:
                    continue
                c = numer//3
                tr = transition(c)
                require(tr is not None, "bridge not admitted")
                status, d, length, w, v = tr
                require(replay(9*c+2, w) == d, "bridge left")
                require(replay(c, v) == (d if status == "MERGE" else 9*d+2),
                        "bridge right")
                count += 1
    return count


def example_checks():
    specs = [(236031, 118015, 18, 17, 478505, True),
             (230319, 115157, 18, 17, 641, False),
             (230319, 76771, 18, 18, 641, False),
             (20530069503, 6843356499, 34, 34, 37500596075, True)]
    rows = []
    for n, m, a, b, endpoint, no_descent in specs:
        x, y = trace(n, a), trace(m, b)
        require(0 < m < n and x[-1] == y[-1] == endpoint, "example merger")
        require(not no_descent or min(x[1:]) > n, "all-state no-descent failure")
        rows.append(dict(n=n, m=m, a=a, b=b, endpoint=endpoint,
                         minimum=min(x[1:]), no_descent=no_descent))
    arrivals=[]
    for n in [230319, 115159]:
        t=0
        while n != 1 and t < 1000:
            n, t = step(n), t+1
        require(n == 1, "phase control unfinished")
        arrivals.append(t)
    require(arrivals == [53, 55], "phase arrivals")
    return rows, arrivals


def self_tests():
    rejected=0
    for f in [lambda: v2(0), lambda: step(True), lambda: trace(7, -1),
              lambda: replay(7, "0"), lambda: symbolic(1, 7, "1"),
              lambda: symbolic(128, 59, "0000000")]:
        try:
            f()
        except ValueError:
            rejected += 1
        else:
            raise ValueError("bad control accepted")
    require(symbolic(1152, 533, "1000001") == symbolic(128, 59, "1101100")
            == (81, 38), "odd seed cylinder")
    require(symbolic(331776, 210944, "0"*11+"1")
            == symbolic(4096, 2604, "001101001100") == (243, 155),
            "H-squared cylinder")
    return rejected


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--limit", type=int, default=65536)
    p.add_argument("--full", type=Path)
    p.add_argument("--output", type=Path)
    p.add_argument("--check", type=Path)
    args=p.parse_args()
    require(1 <= args.limit <= 1048576, "limit outside supported bounded range")
    counts={mode:dict(admitted=0, MERGE=0, OUTSIDE=0, BUDGET=0)
            for mode in ["old", "new"]}
    digest=hashlib.sha256()
    full=args.full.open("w", encoding="utf-8") if args.full else None
    try:
        for c in range(1, args.limit+1):
            row={}
            for mode in ["old", "new"]:
                old=mode == "old"
                row[mode]=classify(c, old)
                counts[mode][row[mode]["status"]] += 1
                counts[mode]["admitted"] += transition(c, old) is not None
            if transition(c, True) is not None:
                require(transition(c, True) == transition(c), "old transition changed")
            require(row["old"]["status"] != "MERGE" or row["new"]["status"] == "MERGE",
                    "old certificate lost")
            data=json.dumps(row, sort_keys=True, separators=(",", ":"))+"\n"
            digest.update(data.encode())
            if full:
                full.write(data)
    finally:
        if full:
            full.close()
    examples, arrivals=example_checks()
    result=dict(schema="paired-valuation-ladder-v1", limit=args.limit, counts=counts,
                rows_sha256=digest.hexdigest(), first_exits=first_exit_checks(),
                ladders=ladder_checks(), bridges=bridge_checks(), examples=examples,
                phase_arrivals=arrivals, rejected_controls=self_tests(),
                status="PROPOSED", complete_collatz_proof=False)
    text=json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.check:
        require(args.check.read_text(encoding="utf-8") == text,
                "canonical output bytes differ")
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
