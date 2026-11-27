"""Exact certificate for the fourth energy of the sixfold merger-free language."""
import csv
import os
import subprocess
import sys
import tempfile
from collections import deque
from functools import cmp_to_key
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
BAND = HERE.parent / "band"
sys.path.insert(0, str(BAND))
from band_energy import compare, reduce_phase, require


CELL = 60
CELLS_PER_BLOCK = 24


def phase_intervals(groups):
    # The phase of group i is (r + i*q) mod 1. Its length is the
    # difference of consecutive integer parts, plus two.
    points = {(0, 0), (1, 0)}
    for i in range(groups + 1):
        points.add(reduce_phase((0, -i), 1))
    return sorted(points, key=cmp_to_key(compare))


def midpoint(left, right):
    # All midpoints and rotated midpoints have denominator two.
    return left[0] + right[0], left[1] + right[1]


def cell_word(phase, groups):
    a, b = phase
    word = []
    for _ in range(groups):
        b += 2
        if compare((a, b), (2, 0)) >= 0:
            a -= 2
            word.append(3)
        else:
            word.append(2)
    return tuple(word)


class ForbiddenWords:
    def __init__(self, words):
        trie = [{}]
        failure = [0]
        banned = [False]
        for word in sorted(set(words) | {"EE"}):
            node = 0
            for letter in word:
                if letter not in trie[node]:
                    trie[node][letter] = len(trie)
                    trie.append({})
                    failure.append(0)
                    banned.append(False)
                node = trie[node][letter]
            banned[node] = True
        pending = deque(trie[0].values())
        while pending:
            node = pending.popleft()
            banned[node] |= banned[failure[node]]
            for letter, child in trie[node].items():
                previous = failure[node]
                while previous and letter not in trie[previous]:
                    previous = failure[previous]
                failure[child] = trie[previous].get(letter, 0)
                pending.append(child)
        transitions = []
        for node in range(len(trie)):
            row = {}
            for letter in "EO":
                previous = node
                while previous and letter not in trie[previous]:
                    previous = failure[previous]
                row[letter] = trie[previous].get(letter, 0)
            transitions.append(row)
        self.group = {}
        for length in (2, 3):
            rows = []
            for node in range(len(trie)):
                row = []
                for slot in range(length):
                    state = node
                    for i in range(length):
                        state = transitions[state]["E" if i == slot else "O"]
                        if banned[state]:
                            state = -1
                            break
                    row.append(state)
                rows.append(tuple(row))
            self.group[length] = rows

    def layers(self, word):
        reachable = [[0]]
        for length in word:
            transitions = self.group[length]
            reachable.append(sorted({x for node in reachable[-1]
                                     for x in transitions[node] if x >= 0}))
        # On a fixed suffix, states with identical labeled continuations
        # accept exactly the same residual language.
        classes = dict.fromkeys(reachable[-1], 0)
        result = []
        for length, nodes in zip(reversed(word), reversed(reachable[:-1])):
            vectors = []
            numbers = {}
            previous = {}
            for node in nodes:
                key = tuple(-1 if x == -1 else classes[x] for x in self.group[length][node])
                if key not in numbers:
                    numbers[key] = len(vectors)
                    vectors.append(key)
                previous[node] = numbers[key]
            classes = previous
            result.append((length, vectors))
        return list(reversed(result))


def cell_matrix(binary, automaton, word):
    lines = [str(len(word))]
    for length, rows in automaton.layers(word):
        lines.append(f"{length} {len(rows)}")
        lines.extend(" ".join(map(str, row)) for row in rows)
    run = subprocess.run([binary], input="\n".join(lines), capture_output=True,
                         text=True, check=False)
    require(run.returncode == 0, f"cell counter exited {run.returncode}: {run.stderr.strip()}")
    rows = [tuple(map(int, line.split())) for line in run.stdout.splitlines()]
    require(len(rows) == 3 and all(len(row) == 3 and min(row) >= 0 for row in rows),
            "invalid boundary matrix")
    return tuple(rows)


def boundary_class(flags):
    if flags == 0:
        return 0
    if flags == 15:
        return 1
    return 2


def direct_small(word, patterns):
    # Independent labeled enumeration. With h bad copies the upper
    # indicator is 1-h+choose(h,2), including h=3,4.
    options = []
    for length in word:
        rows = []
        for a, b in product(range(length), repeat=2):
            for c, d in {(a, b), (b, a)}:
                slots = (a, b, c, d)
                rows.append(tuple("O" * j + "E" + "O" * (length - j - 1) for j in slots))
        options.append(rows)
    matrix = [[0] * 3 for _ in range(3)]
    for choices in product(*options):
        copies = ["".join(segment[i] for segment in choices) for i in range(4)]
        if any("EE" in w for w in copies):
            continue
        bad = sum(any(p in w for p in patterns) for w in copies)
        weight = 1 - bad + bad * (bad - 1) // 2
        first = sum((w[0] == "E") << i for i, w in enumerate(copies))
        last = sum((w[-1] == "E") << i for i, w in enumerate(copies))
        for row, initial in enumerate((0, 15, 5)):
            if first & initial == 0:
                matrix[row][boundary_class(last)] += weight
    return tuple(tuple(row) for row in matrix)


def phase_cell_index(phase, points):
    low, high = 0, len(points) - 1
    while high - low > 1:
        j = (low + high) // 2
        pt = points[j]
        if compare(phase, (2 * pt[0], 2 * pt[1])) >= 0:
            low = j
        else:
            high = j
    return low


def verify(binary):
    tests = [((2, 3, 2, 3), ("EOO", "OOE")),
             ((3, 3, 2, 3), ("OEOE", "OOEOO"))]
    for word, patterns in tests:
        matrix = cell_matrix(binary, ForbiddenWords(patterns), word)
        require(matrix == direct_small(word, patterns), "direct Bonferroni enumeration disagrees")
    print("direct quadruple checks", len(tests), flush=True)

    with (BAND / "SIXFOLD_MOTIFS.tsv").open() as stream:
        patterns = {r["upper"] for r in csv.DictReader(stream, delimiter="\t")}
    require(len(patterns) == 446, "unexpected motif bank")
    automaton = ForbiddenWords(patterns)
    points = phase_intervals(CELL)
    matrices, clocks = [], []
    for left, right in zip(points, points[1:]):
        word = cell_word(midpoint(left, right), CELL)
        matrices.append(cell_matrix(binary, automaton, word))
        clocks.append(sum(word))
    require(len(matrices) == CELL + 1, "unexpected number of cell phase intervals")
    print("motifs", len(patterns), "cell groups", CELL, "cell matrices", len(matrices), flush=True)

    groups = CELL * CELLS_PER_BLOCK
    large_points = phase_intervals(groups)
    shortest, longest = 3 * groups, 0
    for left, right in zip(large_points, large_points[1:]):
        phase = midpoint(left, right)
        v, clock = (1, 0, 0), 0
        for _ in range(CELLS_PER_BLOCK):
            index = phase_cell_index(phase, points)
            mat = matrices[index]
            v = tuple(sum(v[i] * mat[i][j] for i in range(3)) for j in range(3))
            clock += clocks[index]
            phase = reduce_phase((phase[0], phase[1] + 2 * CELL), 2)
        energy = sum(v)
        require(16 * energy**5 < 1 << (5 * clock), "superblock misses the four-fifths bit saving")
        require(clock <= 4000, "clock exceeds the four-fifths to 1/5000 conversion")
        shortest, longest = min(shortest, clock), max(longest, clock)
    require(len(large_points) - 1 == groups + 1, "unexpected superblock phase partition")
    print("superblock groups", groups, "open phase intervals", len(large_points) - 1,
          "physical clocks", shortest, longest)
    print("all 16*energy^5 < 2^(5*clock), checked rate cap 4999/5000")


def main():
    with tempfile.TemporaryDirectory() as temp:
        binary = Path(temp) / "cell_energy"
        subprocess.run([os.environ.get("CXX", "c++"), "-std=c++17", "-O3", "-Wall", "-Wextra",
                        str(HERE / "cell_energy.cpp"), "-lgmpxx", "-lgmp", "-o", str(binary)], check=True)
        verify(binary)


if __name__ == "__main__":
    main()
