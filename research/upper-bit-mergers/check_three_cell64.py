"""Verify the finite ordinary words and residue transitions for the 9-multiple criterion."""

from collections import defaultdict
from functools import cache

from check import walk


SEEDS = [(369, 9, 20, 3), (3, 4, 2, 2), (5, 3, 2, 1), (23, 5, 20, 3)]
BINARY = 256
TERNARY = 27
INV3 = pow(3, -1, BINARY)


@cache
def native_pass(base):
    """A pass on either member of a required failed doublet excludes the class."""
    for multiplier in (1, 3):
        low = multiplier * base
        for clock in range(1, 9):
            left, first_odds = walk(low, clock)
            right, second_odds = walk(3 * low, clock)
            if left == right and first_odds == second_odds + 1:
                return True
    return False


def allowed(binary, ternary):
    if ternary % 3 == 0 or native_pass(binary):
        return False
    if binary % 16 != 1 or ternary % 3 != 2:
        return True
    z = 8 * ternary - 1
    if z % TERNARY == 0:
        return False
    divisor = 9 if z % 9 == 0 else 3
    aux = (8 * binary - 1) * pow(divisor, -1, BINARY) % BINARY
    return not native_pass(aux)


def returns(binary, ternary):
    """The return map is (slope*u+offset)/3; all outputs record one division."""
    slope, offset = 1, 0
    out = set()
    visited = set()
    while allowed(binary, ternary):
        if (binary, ternary) in visited:
            raise AssertionError("an infinite sequence without a division is possible")
        visited.add((binary, ternary))
        divide = 16 if ternary % 3 == 2 else 32
        new_b = (1 + divide * binary) * INV3 % BINARY
        rem = ((1 + divide * ternary) // 3) % 9
        for digit in range(3):
            new_t = rem + 9 * digit
            if allowed(new_b, new_t):
                out.add((new_b, new_t, divide * slope, 1 + divide * offset))
        keep = 48 - divide
        binary = (1 + keep * binary) % BINARY
        ternary = (1 + keep * ternary) % TERNARY
        slope, offset = keep * slope, 1 + keep * offset
    return out


def replay():
    for base, clock, endpoint, odds in SEEDS:
        if walk(base - 1, clock) != (endpoint, odds) or walk(base, clock) != (endpoint, odds):
            raise AssertionError(("adjacent seed", base))

    # Two transformations kill the input coefficient modulo 256, even after
    # division by the odd number three. Zero represents any initial residue.
    reachable = {0}
    for _ in range(2):
        reachable = {(1 + c * b) * d % BINARY for b in reachable
                     for c in (16, 32) for d in (1, INV3)}
    after_division = sorted(b for b in reachable if b % 16 == INV3 % 16 and not native_pass(b))
    if after_division != [91, 203]:
        raise AssertionError(("postdivision states", after_division))
    graph = defaultdict(set)
    labels = defaultdict(set)
    for b in after_division:
        for t in range(TERNARY):
            if not allowed(b, t):
                continue
            for new_b, new_t, slope, offset in returns(b, t):
                if new_b not in after_division:
                    raise AssertionError(("unlisted destination", new_b))
                graph[t].add(new_t)
                labels[t, new_t].add((slope, offset))
    # Remove dead ends. A missing binary constraint when projecting to t can
    # only add edges, so every path of actual failures survives this pruning.
    live = {t for t in range(TERNARY) if t % 3}
    while True:
        kept = {t for t in live if graph[t] & live}
        if kept == live:
            break
        live = kept
    edges = {t: sorted(graph[t] & live) for t in sorted(live)}
    if edges != {1: [11], 11: [11], 13: [13, 22], 22: [1, 11]}:
        raise AssertionError(("infinite-path graph", edges))
    if labels[11, 11] != {(512, 17)} or labels[13, 13] != {(32, 1)}:
        raise AssertionError(("loop labels", labels[11, 11], labels[13, 13]))
    return after_division, edges


if __name__ == "__main__":
    states, edges = replay()
    print("4 adjacent words verified; postdivision residues modulo 256:", states)
    print("surviving ternary edges:", edges)
    print("both recurrent affine maps verified")
