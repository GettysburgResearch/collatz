#!/usr/bin/env python3
"""Independent literal-T replay of K1--K3, without author-code imports."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def T(n: int) -> int:
    need(type(n) is int and n > 0, "positive ordinary integer required")
    return (3*n+1)//2 if n % 2 else n//2


def iterate(n: int, steps: int) -> int:
    need(type(steps) is int and steps >= 0, "nonnegative clock required")
    for _ in range(steps):
        n = T(n)
    return n


def vp2(n: int) -> int:
    need(type(n) is int and n > 0, "positive valuation input required")
    return (n & -n).bit_length()-1


def replay_gaps(n: int, gaps: tuple[int, ...]) -> int:
    need(n % 2 == 1, "odd gap source required")
    for a in gaps:
        need(n > 1, "claimed first-hit rank contains 1 early")
        need(a == vp2(3*n+1), "wrong actual odd gap")
        n = iterate(n, a)
        need(n % 2 == 1, "odd gap endpoint is not odd")
    return n


def check_pair(k: int) -> tuple[int, int]:
    need(type(k) is int and k > 0 and k % 4 != 0, "ineligible pair index")
    x, y = 128*k+1, 64*k+1
    w = iterate(x, 6)
    need(w == 54*k+1, "upper three-pair endpoint")
    need(iterate(y, 6) == 27*k+1, "lower three-pair endpoint")
    c = vp2(3*w+1)
    z = iterate(w, c)
    need(z > 0 and z % 2 == 1 and z % 3 != 0, "wrong certified tail domain")
    need(81*x == 2**(c+6)*z-175, "upper affine reconstruction")
    need(81*y == 2**(c+5)*z-47, "lower affine reconstruction")
    if c == 1:
        need(z % 162 == 83, "odd-index congruence")
        need(iterate(y, 7) == (z+1)//6, "A target identity")
    else:
        need(c >= 3 and k % 4 == 2, "wrong even-index valuation")
        need((2**(c-2)*z-1) % 81 == 0, "even-index congruence")
        if c % 2 == 0:
            r = (c-4)//2
            need(iterate(y, c+6) == T(3**r*z), "B target identity")
        else:
            r = (c-3)//2
            need(iterate(y, c+4) == 2*3**r*z+1, "C target identity")
    return c, z


def run(proof_path: Path) -> dict[str, object]:
    counts = {"A": 0, "B": 0, "C": 0}
    for k in range(1, 8193):
        if k % 4 == 0:
            continue
        c, _ = check_pair(k)
        counts["A" if c == 1 else "B" if c % 2 == 0 else "C"] += 1
    rank_five_cases = 0
    last_gap_residues: dict[str, int] = {}
    for c in (1, *range(3, 65)):
        candidates = []
        for a in range(2, 164, 2):
            condition = (pow(2, a, 243) == 7) if c == 1 else (
                pow(2, c-2, 243)*(pow(2, a, 243)-1) % 243 == 3)
            if condition:
                candidates.append(a)
        need(len(candidates) == 1, "not one allowed even residue")
        residue = candidates[0] % 162
        need(residue != 0, "forbidden last-gap residue zero")
        last_gap_residues[str(c)] = residue
        for repeat in range(3):
            a = residue + 162*repeat
            if a == 2:
                continue
            z = (2**a-1)//3
            need(3*z+1 == 2**a and z > 1, "rank-one tail is wrong")
            numerator = 2**(c+6)*z-175
            need(numerator % 81 == 0, "nonintegral affine source")
            x = numerator//81
            need((x-1) % 128 == 0, "wrong upper congruence")
            k = (x-1)//128
            check_pair(k)
            need(replay_gaps(x, (2,2,2,c,a)) == 1,
                 "rank-five certificate does not reach one")
            y = 64*k+1
            if c >= 3:
                need(iterate(y, 8) == 2**(c-3)*(2**a-1)+2,
                     "short rank-five endpoint")
            rank_five_cases += 1
    need({c:last_gap_residues[str(c)] for c in (1,3,4,5)} ==
         {1:70,3:22,4:68,5:118}, "four subfamily residues")
    subfamily_cases = 0
    for c, a0 in ((1,70),(3,22),(4,68),(5,118)):
        for j in range(4):
            a = a0+162*j
            z = (2**a-1)//3
            x = (2**(c+6)*z-175)//81
            y = (x+1)//2
            if c == 1:
                h = a-4
                need(iterate(y, 10) == 2**h+1, "c1 binary shadow entry")
                need(iterate(y, 10+h+1) == T(3**(81*j+32)),
                     "c1 pure-power endpoint")
            elif c == 3:
                need(iterate(y, 8) == 2**a+1, "c3 binary shadow entry")
                need(iterate(y, 8+a+1) == T(3**(81*j+10)),
                     "c3 pure-power endpoint")
            elif c == 4:
                value, odd_count = y, 0
                while value != 1:
                    odd_count += value % 2
                    value = T(value)
                need(odd_count == 5, "c4 lower rank must be five")
                need(iterate(y, 8) == 2**(a+1), "c4 power-two endpoint")
            else:
                need(iterate(y, 9) == 2**(162*j+119)-1,
                     "c5 Mersenne endpoint")
            subfamily_cases += 1
    controls = 0
    for k in (0,-1,4,128):
        try:
            check_pair(k)
        except ValueError:
            controls += 1
        else:
            raise ValueError("ineligible pair accepted")
    z = (2**68-1)//3
    x = (2**10*z-175)//81
    try:
        replay_gaps(x, (2,2,2,5,68))
    except ValueError:
        controls += 1
    else:
        raise ValueError("corrupted supplied certificate accepted")
    return {
        "status": "PASS",
        "scope": "independent finite literal shortcut checks; no kernel closure or Collatz proof",
        "proof_sha256": hashlib.sha256(proof_path.read_bytes()).hexdigest(),
        "small_pair_counts": counts,
        "rank_five_cases": rank_five_cases,
        "allowed_fourth_gaps": len(last_gap_residues),
        "subfamily_cases": subfamily_cases,
        "negative_controls": controls,
        "last_gap_residues": last_gap_residues,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(run(args.proof), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(result, encoding="utf-8")
    else:
        print(result, end="")
