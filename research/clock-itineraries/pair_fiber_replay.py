"""Replay the exact-clock cover by direct ordinary iteration and inverse search."""
from itertools import combinations
from pathlib import Path
import re

CLOCK = 18
MODULUS = 3**8


def step(n):
    return (3*n + 1)//2 if n % 2 else n//2


def trace(n, h):
    odd = 0
    for _ in range(h):
        odd += n % 2
        n = step(n)
    return n, odd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def target(i):
    return 6*(i//2) + 1 + 4*(i % 2)


def representatives():
    table = {}
    for j in range(6):
        modulus = 3**(j+3)
        inv = pow(2, -CLOCK, modulus)
        for positions in combinations(range(CLOCK), j):
            carry = sum(3**(j-1-i)*2**e for i,e in enumerate(positions))
            residue = (20*3**j + carry)*inv % modulus
            if residue % 3 == 0:
                continue
            for b in range(residue, 2*MODULUS, modulus):
                if b % 2 == 0 or b in table:
                    continue
                z = ((b << CLOCK)-carry)//3**j
                if z < 20:
                    continue
                require(z % 27 == 20 and trace(z,CLOCK) == (b,j), (b,z,j))
                table[b] = (z-20)//27
    require(len(table) == 4374, len(table))
    return [table[target(i)] for i in range(4374)]


def predecessors(b, h):
    frontier = {b}
    for _ in range(h):
        frontier = {2*y for y in frontier} | {(2*y-1)//3 for y in frontier if y%3 == 2}
    return frontier


def earlier_misses():
    return [next(b for b in range(1,20001,2) if b%3 and
                 all(z < 20 or z%27 != 20 for z in predecessors(b,h))) for h in range(CLOCK)]


def replay_gate_counts():
    times = {1: 0}

    def time_to_one(n):
        trail = []
        while n not in times:
            trail.append(n)
            n = step(n)
        clock = times[n]
        for x in reversed(trail):
            clock += 1
            times[x] = clock
        return clock

    for k, expected in enumerate(((237, 8911), (329, 78543))):
        window = 2**(4*k + 2*(k//2)) * (k+1) // 3**k + 1
        count = 9710*window + 1
        last = (0, 0)
        for u in range(count):
            w = 23 + 32*u
            last = max(last, (min(time_to_one(w), time_to_one(3*w)), u))
        require(last == expected, (k, last))
        print(f"stage {k}, {count} parameters, zero misses at clock {last[0]}")


def replay():
    src = Path(__file__).with_name("PairCoverData.lean").read_text(encoding="utf8")
    groups = re.findall(r"\| \d+ => #\[(.*?)\]", src, re.S)
    actual = [int(x) for group in groups for x in group.split(",")]
    expected = representatives()
    require(expected == actual, "Lean representatives differ from regeneration")
    checked = 0
    for i,t in enumerate(actual):
        b = target(i)
        count = trace(20+27*t,CLOCK)[1]
        for lift in (0,1,12345):
            t1 = t + (1 << (CLOCK+1))*3**(5-count)*lift
            w = 23+32*t1
            want = b+2*MODULUS*lift
            for n in (w,3*w):
                require(trace(n,23)[0] == want, (i,t,lift,n))
                checked += 1
    misses = earlier_misses()
    require(misses[-1] == 8161, misses)
    print(f"{len(actual)} classes, {checked} forward trajectories, earlier missing targets {misses}")
    replay_gate_counts()


if __name__ == "__main__":
    replay()
