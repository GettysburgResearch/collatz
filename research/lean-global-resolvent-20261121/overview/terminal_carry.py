"""Exact terminal-word carry compiler and ordinary replay.

The unbounded theorems are proved in lean/Collatz/TerminalCarry.lean. This file
constructs concrete programs and checks their transcription against direct
ordinary integer trajectories. It never substitutes a shadow for an orbit.
"""
from __future__ import annotations
from itertools import product
import argparse
import json


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def total(word: tuple[int, ...]) -> int:
    return sum(word)


def correction(word: tuple[int, ...]) -> int:
    value, clock = 0, 0
    for gap in word:
        value = 3 * value + 2**clock
        clock += gap
    return value


def compile_carry(s: int, p: int, normalize_even: bool = True) -> dict:
    if s < 0 or (s > 0 and p % 3 == 0):
        raise ValueError("A positive ternary denominator requires a primitive numerator")
    initial_s, initial_p = s, p
    steps = []
    while s > 0 or (normalize_even and p != 0 and p % 2 == 0):
        old_rank = abs(p) + 3**s
        if p % 2 == 0:
            if p == 0:
                raise AssertionError("A primitive positive denominator cannot carry zero")
            steps.append("E")
            p //= 2
        else:
            if s == 0:
                break
            steps.append("O")
            s -= 1
            p = (p + 3**s) // 2
        if not abs(p) + 3**s < old_rank:
            raise AssertionError("Compiler rank did not decrease")
        if s > 0 and p % 3 == 0:
            raise AssertionError("Primitive denominator invariant was lost")
    if steps.count("O") != initial_s:
        raise AssertionError("Wrong odd-clock count")
    if len(steps) + abs(p) + 1 > abs(initial_p) + 3**initial_s:
        raise AssertionError("Clock budget failed")
    return {"denominator_exponent": initial_s, "numerator": initial_p,
            "clock": len(steps), "carry": p, "branches": "".join(steps)}


def compile_terminal(word: tuple[int, ...], j: int = 1, b: int = 1) -> dict:
    s, B, C = len(word) + 1, total(word), correction(word)
    p = b * 3**s - 2**(B + j) - 3 * 2**j * C
    return {"word": list(word), "dyadic_exponent": j, "shift": b,
            **compile_carry(s, p)}


def replay(word: tuple[int, ...], h: int, j: int, b: int, program: dict) -> dict | None:
    s, B, C = len(word) + 1, total(word), correction(word)
    numerator = 2**(B+h) - 3*C - 2**B
    if numerator <= 0 or numerator % 3**s:
        return None
    m = numerator // 3**s
    n = 2**j * m + b
    L, t, d = B+h+j, program["clock"], program["carry"]
    if n <= 0 or L < t:
        return None
    # Replay the entire supplied source certificate, including its last gap.
    source = m
    for gap in word + (h,):
        if source <= 0 or source % 2 != 1:
            raise AssertionError("Source certificate left positive odd integers")
        numerator = 3*source+1
        if numerator % 2**gap or (numerator // 2**gap) % 2 != 1:
            raise AssertionError("Source gap is not its exact ordinary valuation")
        source = numerator // 2**gap
    if source != 1:
        raise AssertionError("Full source certificate did not reach one")
    # Replay each ordinary target branch separately, with arbitrary-size integers.
    target = n
    for branch in program["branches"]:
        if (target % 2 == 1) != (branch == "O"):
            raise AssertionError("Actual target disagrees with compiled parity")
        target = shortcut(target)
    if target != 2**(L-t)+d:
        raise AssertionError("Compiled ordinary endpoint failed")
    budget = (2**t-3**s)*2**(L-t) > 3**s*d-program["numerator"]
    if (target < n) != budget:
        raise AssertionError("Exact original-floor saving equivalence failed")
    # Independent finite signed continuation and a new exact original-floor test.
    carry, actual, odd = d, target, 0
    for u in range(min(L-t, 12)+1):
        expected = 3**odd * 2**(L-t-u)+carry
        if actual != expected:
            raise AssertionError("Continued signed transfer failed inside its horizon")
        continued_budget = ((2**(t+u)-3**(s+odd))*2**(L-t-u)
                            > 3**s*carry-program["numerator"])
        if (actual < n) != continued_budget:
            raise AssertionError("Continued saving test changed the original floor")
        odd += carry % 2
        carry, actual = shortcut(carry), shortcut(actual)
    return {"source": m, "target": n, "terminal_gap": h,
            "ordinary_endpoint": target, "compiler_clock": t,
            "binary_horizon": L, "strict_descent": budget}


def run_checks() -> dict:
    programs, fibres, zero, negative, positive = 0, 0, 0, 0, 0
    examples = []
    # Exhaustive WORD catalogue only; every listed fibre test is a finite replay.
    # The Lean statements quantify over all words, all dyadic companions, all h.
    for length in range(5):
        for word in product(range(1, 7), repeat=length):
            period = 2 * 3**length
            for j, b in ((1,1),(1,-1),(0,7),(3,-5)):
                prog = compile_terminal(word, j, b)
                programs += 1
                zero += prog["carry"] == 0
                negative += prog["carry"] < 0
                positive += prog["carry"] > 0
                # One full exponent period finds the integrality cell; then
                # test three positive, sufficiently precise ordinary members.
                found = 0
                for h0 in range(2, period+2, 2):
                    B, C, s = total(word), correction(word), len(word)+1
                    if (2**(B+h0)-3*C-2**B) % 3**s:
                        continue
                    h = h0
                    while h+B+j < prog["clock"] or 2**(B+h) <= 3*C+2**B:
                        h += period
                    for _ in range(3):
                        result = replay(word,h,j,b,prog)
                        if result:
                            fibres += 1
                            found += 1
                            if word in ((),(1,),(2,),(3,),(4,)) and j==1 and b==1:
                                examples.append({**prog,**result})
                        h += period
                    break
                if found == 0:
                    raise AssertionError("Failed to replay any valid terminal exponent")
    # The first hard prefix is checked well beyond small machine integers.
    for k in range(20):
        h = 6*k+4
        n = (2**(h+4)-13)//9
        x = n
        for t in range(h+5):
            if x < n:
                raise AssertionError("Mersenne residual unexpectedly descended before horizon")
            if t >= 3 and x != 3**(t-3)*2**(h+4-t)-1:
                raise AssertionError("Mersenne horizon formula failed")
            x = shortcut(x)
    return {"programs": programs, "complete_source_target_replays": fibres,
            "zero_carry_programs": zero, "negative_carry_programs": negative,
            "positive_carry_programs": positive,
            "mersenne_horizons": 20, "examples": examples,
            "scope": "Finite exact replay; unbounded assertions belong to the Lean module."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    result = run_checks()
    if args.output:
        with open(args.output,"w") as stream:
            json.dump(result,stream,indent=2)
    print(json.dumps({key: value for key,value in result.items() if key!="examples"},indent=2))
