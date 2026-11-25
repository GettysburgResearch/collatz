"""Independent integer replay of full anchor formulas and both scale bounds."""
from collections import Counter
import json


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def run(x, h):
    for _ in range(h):
        x = step(x)
    return x


def hit_one(a):
    h = 0
    while a != 1:
        a = step(a)
        h += 1
        if h > 1000:
            raise RuntimeError("positive sample did not hit one")
    return h


def powers(n):
    """All representations n = 3**r * base with positive base."""
    r = 0
    while True:
        yield r, n
        if n % 3:
            break
        n //= 3
        r += 1


def cycle_phases(m):
    seen = {}
    states = []
    x = -m
    while x not in seen:
        seen[x] = len(states)
        states.append(x)
        x = step(x)
        if len(states) > 1000:
            raise RuntimeError("negative sample did not repeat")
    entry = seen[x]
    lap = states[entry:]
    odds = sum(z % 2 for z in lap)
    for i, phase in enumerate(lap):
        yield entry + i, -phase, len(lap), odds


def check_pairs(x, y, end, stats, negative_phase=None):
    for r, w in powers(x):
        for _, b in powers(y):
            stats["representations"] += 1
            if b > w:
                continue
            if b == w:
                stats["same_base_representations"] += 1
            else:
                stats["lower_base_representations"] += 1
            if negative_phase is None:
                assert 3**r < w
                if b < w:
                    assert end < w
            else:
                assert 3**r <= negative_phase * w


def main():
    positive = Counter()
    for a in range(1, 97):
        h = hit_one(a)
        for d in range(1, 5):
            for t in range(1, 25):
                x = a + (1 << h) * 4**d * t
                y = a + (1 << h) * 3**d * t
                end = run(x, h + 2 * d)
                assert end == run(y, h) and a * end <= y
                positive["physical_meetings"] += 1
                check_pairs(x, y, end, positive)
    negative = Counter()
    phases = set()
    for m in range(1, 49):
        for h, phase, period, odd in cycle_phases(m):
            phases.add(phase)
            for laps in (1, 2):
                e, p = period * laps, odd * laps
                assert 2**e < 3**p
                for t in range(1, 17):
                    x = (1 << (h + e)) * t - m
                    y = (1 << h) * 3**p * t - m
                    if x <= 0:
                        continue
                    end = run(x, h + e)
                    assert end == run(y, h)
                    negative["physical_meetings"] += 1
                    check_pairs(x, y, end, negative, phase)
    constructive = Counter()
    for r in range(5):
        for d in range(1, 4):
            h = 2 * 3 ** (r + d)
            b, rem = divmod(2**h - 1, 3 ** (r + d + 1))
            assert rem == 0 and b > 0 and run(3 ** (r + d) * b, h) == 1
            for t in (0, 1, 2, 5, 17):
                w = 3**d * b + (1 << h) * 4**d * t
                v = b + (1 << h) * t
                x, y = 3**r * w, 3 ** (r + d) * v
                assert 0 < v < w and run(x, h) < w
                assert run(x, h + 2 * d) == run(y, h)
                constructive["grade_gains"] += 1
                constructive["largest_anchor_clock"] = max(constructive["largest_anchor_clock"], h)
    path = [3**6 * 5]
    while path[-1] >= 5:
        path.append(step(path[-1]))
    assert len(path) == 30 and path[-1] == 4 and 3**6 > max(phases) * 5
    print(json.dumps({
        "positive": positive, "negative": negative, "negative_phases": sorted(phases),
        "constructive": constructive, "control": path,
        "scope": "Finite ordinary integer checks. Each claimed infinite family has a separate Lean theorem."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
