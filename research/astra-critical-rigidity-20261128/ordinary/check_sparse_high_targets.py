"""Exact finite tests of the reversed-word count and finite high-trace decomposition."""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def require(condition, label):
    if not condition:
        raise ValueError(label)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def odd_step(n):
    m = 3 * n + 1
    e = (m & -m).bit_length() - 1
    return m >> e, e


def reversed_residue(gaps):
    modulus = 3 ** len(gaps)
    total = 0
    answer = 0
    for j, gap in enumerate(reversed(gaps)):
        total += gap
        answer += 3**j * pow(2, -total, modulus)
    return answer % modulus


def word_count_check():
    small_cases = []
    for b, B, K in [(4096, 2048, 6), (10009, 6001, 8), (12008, 18001, 7)]:
        grids = []
        masks = [
            {y for y in range(B // 2, 2 * B + 1) if y % 65 == 3},
            {y for y in range(B // 2, 2 * B + 1) if y % 27 in {2, 11, 22}},
            set(range(B // 2, 2 * B + 1)),
        ]
        for F in masks:
            rows = [{r: count for r, count in Counter(y % 3**k for y in F).items()}
                    for k in range(K + 1)]
            for k in range(K):
                for r in range(3**k):
                    coarse = rows[k].get(r, 0)
                    fine = sum(rows[k + 1].get(r + i * 3**k, 0) for i in range(3))
                    require(coarse == fine, "conditional-mean target grid")
            seen = set()
            visit_count = 0
            for n in range(b + 1 - b % 2, 2 * b, 2):
                gaps = []
                elapsed = 0
                y = n
                while elapsed <= K:
                    k = len(gaps)
                    if y in F:
                        require(y % 3**k == reversed_residue(gaps), "physical reversed residue")
                        require(Fraction(1, 1) <= Fraction(2**elapsed * y, 3**k * n) <= 2,
                                "short-prefix real correction")
                        require((tuple(gaps), y) not in seen, "word and value have unique source")
                        seen.add((tuple(gaps), y))
                        visit_count += 1
                    y, gap = odd_step(y)
                    elapsed += gap
                    gaps.append(gap)

            numerator = Fraction(0)
            unweighted = 0
            words = [((), 0)]
            while words:
                w, s = words.pop()
                k = len(w)
                ratio = Fraction(2**s, 3**k)
                # Cut only words ruled out by x∈[b,2b), y∈[B/2,2B], correction∈[1,2].
                if Fraction(b, 2 * B) <= ratio <= Fraction(8 * b, B):
                    count = rows[k].get(reversed_residue(w), 0)
                    unweighted += count
                    numerator += Fraction(3**k * count, B * 2**s)
                for g in range(1, K - s + 1):
                    words.append((w + (g,), s + g))
            require(visit_count <= unweighted, "relaxed grid dominates true count")
            require(Fraction(visit_count, b) <= 8 * numerator, "bounded real drift weight")
            grids.append([len(F), visit_count, unweighted, [numerator.numerator, numerator.denominator]])
        small_cases.append({"source": b, "target": B, "native_budget": K, "masks": grids})
    return small_cases


def traces_check():
    paths = {}
    for n in range(1, 1537):
        seen = set()
        path = []
        x = n
        while x not in seen:
            require(len(path) < 1500, "finite control orbit too long")
            seen.add(x)
            path.append(x)
            x = step(x)
        require(x in {1, 2} and min(path) == 1, "controlled orbit and loop closure")
        while len(path) < 100:
            path.append(x)
            x = step(x)
        paths[n] = path
    even_patterns = 0
    pairs_by_probe = []
    for Y in [13, 47, 97, 131, 239]:
        shell = set(range(Y, 2 * Y + 1))
        for n, path in paths.items():
            if n % 2 != 1:
                continue
            last_odd = None
            for j, y in enumerate(path[:60]):
                if y % 2:
                    last_odd = j
                elif y in shell:
                    require(last_odd is not None, "odd start")
                    a = j - last_odd
                    require(2**a * y == 3 * path[last_odd] + 1, "last-odd lift of even target")
                    even_patterns += 1
        source_lists = [list(range(1, 212, 3)), list(range(217, 453, 5))]
        for h1, h2 in [(0, 0), (9, 23), (34, 18), (55, 86)]:
            entries = []
            for inputs, deadline in zip(source_lists, (h1, h2)):
                side = []
                for n in inputs:
                    path = paths[n]
                    t = path.index(1)
                    whole = set(path[:deadline + 1]) & shell
                    early = set(path[:min(deadline, t) + 1]) & shell
                    late = set(path[t:deadline + 1]) & shell
                    require(whole == early | late, "actual finite trace decomposition")
                    side.append((whole, early, late))
                entries.append(side)
            collisions = 0
            with_early = 0
            for left in entries[0]:
                for right in entries[1]:
                    common = left[0] & right[0]
                    early_common = (left[1] & right[0]) | (left[0] & right[1])
                    require(common == early_common | (left[2] & right[2]), "joint pre/post trace")
                    collisions += bool(common)
                    with_early += bool(early_common)
            require(collisions == with_early, "finite controlled components have bounded common tails")
            pairs_by_probe.append([Y, h1, h2, collisions])
    return {"sources": len(paths), "pairs_per_probe": len(source_lists[0]) * len(source_lists[1]),
            "high_even_lifts": even_patterns, "finite_trace_probes": pairs_by_probe}


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    names = ["SPARSE_HIGH_TARGETS.md", "FINITE_HIGH_ORBIT_INTERSECTIONS.md", Path(__file__).name]
    print(json.dumps({"scope": "Finite reversed-word and physical trace identities only",
                      "sha256": {n: sha256((root / n).read_bytes()).hexdigest() for n in names},
                      "word_grids": word_count_check(), "actual_paths": traces_check()},
                     indent=2, sort_keys=True))
