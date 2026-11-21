#!/usr/bin/env python3
"""Replay exact asynchronous-reset rows without importing the search code.

This checks the finite output and two positive ordinary lifts per row. The
arbitrary-word/all-parent statement is proved in AsyncReset.lean, not inferred
from these replays. Python assertions are deliberately not used.
"""
from __future__ import annotations

import csv
from fractions import Fraction
from pathlib import Path
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def profile(n: int, clock: int) -> tuple[int, int, int, list[int]]:
    start = n
    odds = 0
    correction = 0
    positions = []
    for t in range(clock):
        if n & 1:
            positions.append(t)
            correction = 3 * correction + 2**t
            odds += 1
        n = step(n)
    require(2**clock * n == 3**odds * start + correction, "profile identity")
    gaps = [b-a for a,b in zip(positions, positions[1:])]
    if positions:
        gaps.append(clock - positions[-1])
    return n, odds, correction, gaps


def verify(path: Path, even_run: int = 22) -> None:
    with path.open() as handle:
        rows = [{key: int(value) for key, value in row.items()}
                for row in csv.DictReader(handle)]
    previous: dict[int, set[int]] = {}
    density = Fraction()
    threshold = Fraction()
    for index, row in enumerate(rows):
        h,k,p,delta,peak,C,D,r,res,mod = (
            row[key] for key in ("h","k","p","delta","peak","C","D","r","res","mod"))
        require(h >= k >= 1 and delta == h-k+1, f"clock row {index}")
        require(r > 0 and r & 1 and r < 2**h, f"source row {index}")
        x,ps,cs,source = profile(r,h)
        y,pt,ct,target = profile(2*r-1,k)
        require(ps == p and pt == p+1 and cs == C and ct == D, "counts/corrections")
        require(source[-1] == 1, "source prefix ends immediately after odd step")
        require(max(source[:-1],default=0) == peak, "source gap maximum")
        require(D + 2**k == 6*C + 3**(p+1), "paired correction")
        require(y == 3*2**delta*x-1, "paired endpoint")
        require(mod == 3**p and 0 < res < mod and res % 3, "ternary modulus")
        require((2**(k-1)*res-C) % mod == 0, "parent guard")
        require(delta <= even_run and peak <= even_run, "grade budget")
        for smaller, seen in previous.items():
            require(res % smaller not in seen, "nonnested guard cells")
        previous.setdefault(mod,set()).add(res)
        density += Fraction(1,mod)
        threshold = max(threshold,Fraction(C,2**(k-1)))
        q0 = res * pow(2**even_run,-1,mod) % mod
        if q0 % 2 == 0:
            q0 += mod
        for lift in (0,1):
            q = q0+2*mod*lift
            parent = 2**even_run*q
            numerator = 2**(k-1)*parent-C
            require(numerator > 0 and numerator % mod == 0, "positive integral child")
            child = numerator // mod
            endpoint,child_odds,_,child_word = profile(child,h+even_run-delta)
            require(endpoint == q and child_odds == p, "whole source prefix")
            require(child_word == source[:-1]+[even_run-delta+1], "literal source splice")
            require(all(1 <= a <= even_run for a in child_word), "all gaps paid")
            target_endpoint,target_odds,_,target_word = profile(2*child-1,k)
            require(target_endpoint == 3*parent-1 and target_odds == p+1, "ordinary target merger")
            require(target_word == target, "literal target word")
    unit_density = density * Fraction(3,2)
    print(f"rows={len(rows)} ordinary_lifts={2*len(rows)} even_run={even_run}")
    print(f"unit_guard_density={unit_density} decimal={float(unit_density):.15f}")
    print(f"positive_child_threshold={threshold} max_gap={max(r['peak'] for r in rows)}")


if __name__ == "__main__":
    if len(sys.argv) not in (2,3):
        raise SystemExit("usage: replay_async.py ROWS.csv [even_run]")
    verify(Path(sys.argv[1]),int(sys.argv[2]) if len(sys.argv) == 3 else 22)
