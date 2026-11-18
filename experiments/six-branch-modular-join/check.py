"""Independent small-depth least roots and adversarial circular interval joins."""
import itertools
import random
import subprocess
import sys
from pathlib import Path

from search import DIGITS, P, Q, UNIT, search


def physical_min(n):
    frontier = [(0, 0)]
    for j in range(n):
        enlarged = []
        for root, endpoint in frontier:
            for digit in DIGITS:
                source_class = -digit * pow(P, -1, Q) % Q
                lift = (source_class - endpoint) * pow(P, -j, Q) % Q
                current = endpoint + P**j * lift
                nxt, remainder = divmod(P*current + digit, Q)
                assert not remainder
                enlarged.append((root + Q**j * lift, nxt))
        frontier = enlarged
    return min(root for root, _ in frontier)


def candidates(rows, binary, bits, base_length):
    n = len(rows)
    k = n // 2
    bound = 33
    text = [f"{n} {k} {bits} {base_length} {bound}"]
    text.extend(" ".join(map(str, row)) for row in rows)
    output = subprocess.check_output([binary], input="\n".join(text), text=True)
    actual = sorted(tuple(map(int, line.split())) for line in output.splitlines())
    expected = []
    for idx, word in enumerate(itertools.product(range(6), repeat=n)):
        delta = sum(rows[j][d] for j, d in enumerate(word)) % UNIT
        if delta <= bound or delta >= UNIT - n:
            expected.append(divmod(idx, 6**(n-k)))
    assert actual == expected, (len(actual), len(expected))


if __name__ == "__main__":
    binary = str(Path(sys.argv[1]).resolve())
    for n in range(2, 8):
        assert int(search(n, binary)["root"]) == physical_min(n)
    rng = random.Random(8675309)
    for bits in (1, 4, 8):
        width = UNIT >> bits
        rows = [[(rng.randrange(1 << bits)*width + rng.randrange(-20,21)) % UNIT
                 for _ in range(6)] for _ in range(5)]
        candidates(rows, binary, bits, 1)
        candidates([[0]*6, [UNIT-2, UNIT-1, 0, 1, 33, 34]], binary, bits, 2)
    print("Passed six independent least-root depths and six exhaustive circular joins.")
