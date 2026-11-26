"""Direct integer controls for the lifted finite graphs; standard library only."""
from collections import Counter
from functools import lru_cache
from itertools import product
import json


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


@lru_cache(maxsize=200000)
def ancestry(x, h):
    path = [x]
    grades = [0]
    for _ in range(h):
        grades.append(grades[-1] + x % 2)
        x = (3 * x + 1) // 2 if x % 2 else x // 2
        path.append(x)
    return tuple(path), tuple(grades)


def labels(sites, h):
    return [(path[-1], grade[-1]) for path, grade in
            (ancestry(x, h) for x in sites)]


def components(sites, h):
    """Undirected connected components from literal sets of visited vertices."""
    parent = list(range(len(sites)))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    owner = {}
    for i, x in enumerate(sites):
        for y in ancestry(x, h)[0]:
            if y in owner:
                parent[root(i)] = root(owner[y])
            else:
                owner[y] = i
    return [root(i) for i in range(len(sites))]


def different(labels_):
    return {(i, j) for i in range(len(labels_)) for j in range(i)
            if labels_[i] != labels_[j]}


def crossings(sites, h):
    equations = []
    for x in sites:
        path, grades = ancestry(x, h)
        equations.extend((2**(h-i)*3**grades[i], y) for i, y in enumerate(path))
    result = set()
    for (a, x), (b, y) in product(equations, repeat=2):
        if a != b and (y-x) % (a-b) == 0:
            k = (y-x) // (a-b)
            if k >= 0:
                result.add(k)
    return result


def run():
    counts = Counter()
    for h in range(1, 7):
        for stride in (1, 3, 9, 27):
            for origin in range(1, 8):
                sites = [origin + stride*i for i in range(7)]
                part = different(labels(sites, h))
                bad = crossings(sites, h)
                check(len(bad) <= len(sites)**2*(h+1)**2, "crossing count")
                counts["base_windows"] += 1
                for k in range(10):
                    lifted = [x + 2**h*k for x in sites]
                    actual = different(components(lifted, h))
                    check(actual <= part, "one-sided inclusion")
                    counts["literal_graphs"] += 1
                    if k not in bad:
                        check(actual == part, "clean partition")
                        counts["clean_graphs"] += 1
                    elif actual != part:
                        counts["extra_merger_graphs"] += 1
            for size in (6, 9, 18):
                sites = [stride*i for i in range(1, size+1)]
                k = 2**h*max(sites)+1
                comps = components([x + 2**h*k for x in sites], h)
                check(max(Counter(comps).values()) <= (size+1)//2, "dyadic obstruction")
                counts["half_obstructions"] += 1

    histograms = []
    for h in (6, 9, 12):
        for r in (2, 3):
            for stride in (1, 3, 27, 243):
                m = 2**r
                hist = Counter()
                for b in range(0, 2**h, m):
                    sites = [1+stride*(b+i) for i in range(m)]
                    multiplicities = Counter(labels(sites, h))
                    hist[m - max(multiplicities.values())] += 1
                histograms.append(dict(h=h,r=r,stride=stride,blocks=2**(h-r),
                                       deficiency_histogram=dict(sorted(hist.items()))))
    return {"counts": dict(sorted(counts.items())), "exact_labelled_grids": histograms}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
