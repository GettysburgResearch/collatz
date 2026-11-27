"""Finite ordinary controls for the comparable-ancestor and component-window proofs."""
from collections import Counter
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def odd_step(x):
    t = 3*x+1
    e = (t & -t).bit_length()-1
    return t >> e, e


def reverse_rows(y, deadline):
    """All legal shortcut words, including repeated sites and full intermediate peaks."""
    rows = [[(y, 0)]]
    for _ in range(deadline):
        next_row = []
        for site, r in rows[-1]:
            next_row.append((2*site, r))
            if site % 3 == 2:
                next_row.append(((2*site-1)//3, r+1))
        rows.append(next_row)
    return rows


def population():
    low, high, c = 4096, 8192, 3
    counts = Counter()
    late_counts = Counter()
    max_clock = 0
    for x in range(1, c*(high-1)+1):
        v, t = x, 0
        while v != 1 and t <= 2000:
            if low <= v < high and x <= c*v:
                counts[v] += 1
                if t >= 12:
                    late_counts[v] += 1
            v = step(v)
            t += 1
        require(v == 1, "complete small ordinary trajectory failed")
        max_clock = max(t, max_clock)
    missed = Counter()
    for y in range(low, high):
        rows = reverse_rows(y, 11)
        short = {u for row in rows for u, _ in row if u <= c*y}
        require(len(short) == counts[y]-late_counts[y], "early/late count versus reverse tree")
        missed[len(short)] += 1
    return {
        "targets": [low, high-1], "inclusive_source_cap_factor": c,
        "every_start_through": c*(high-1), "max_shortcut_steps_to_one": max_clock,
        "complete_count_histogram_by_floor_log2": sorted(Counter(
            counts[y].bit_length()-1 for y in range(low, high)).items()),
        "deadline_11_histogram": sorted(missed.items()),
        "targets_with_an_arrival_after_11": len(late_counts),
        "largest_complete_count": max(counts.values()),
    }


def haar_cutoff():
    j, c, lifts = 7, 3, 0
    mod = 3**j
    histogram = Counter()
    for v in range(mod):
        # A large ordinary root on this fixed ternary residue, beyond all
        # finite comparison and coincidence thresholds used in the proof.
        y = v + mod * (4*36**j+1)
        rows = reverse_rows(y, j)
        gain_count = sum(1 for t, row in enumerate(rows)
                         for _, r in row if c*3**r >= 2**t)
        actual = {u for row in rows for u, _ in row if u <= c*y}
        require(len(actual) == gain_count, "finite Haar transfer")
        histogram[gain_count] += 1
        lifts += 1
    return {"deadline": j, "cap_factor": c, "all_ternary_roots": lifts,
            "complete_finite_clock_histogram": sorted(histogram.items())}


def words(n, prefix=()):
    if len(prefix) == n:
        yield prefix
    else:
        yield from words(n, prefix+(1,))
        if prefix and prefix[-1] == 1:
            yield from words(n, prefix+(2,))


def script_affine(w):
    a, intercept = 0, 0
    for e in w:
        intercept = 3*intercept + 2**a
        a += e
    return a, intercept


def protected_ball():
    data = []
    for n in range(1, 8):
        largest_count = 0
        tested = 0
        for w in words(n):
            a, c = script_affine(w)
            q, ball = 2**(a+1), 3**128
            residue = ((2**a-c)*pow(3**n, -1, q)) % q
            x = 1 + ball*(((residue-1)*pow(ball, -1, q)) % q)
            if x == 1:
                x += ball*q
            u = x
            for e in w:
                u, measured = odd_step(u)
                require(measured == e, "wrong ordinary exact script")
            require(2**a*u == 3**n*x+c and x % ball == 1, "terminal affine")
            for k in (1, 2, 11):
                shift = q*3**7*k
                lifted = x + shift
                for e in w:
                    lifted, measured = odd_step(lifted)
                    require(measured == e, "word changed on a full lift")
                require(lifted-u == 2*3**(7+n)*k, "endpoint period")
            rows = reverse_rows(u, a+7)
            affordable = {v for row in rows for v, _ in row if v <= 4*x}
            require(min(affordable) == x, "unexpected smaller visitor on the unit lift")
            largest_count = max(largest_count, len(affordable))
            tested += 1
        data.append({"n": n, "words": tested, "largest_count_at_cap_4": largest_count})
    return {"ternary_depth": 128, "tested_visitor_shortcut_deadline": "total word cost + 7",
            "all_finite_words": data}


def periodic_label():
    # Labels are membership in the actual predecessor set of 7. The
    # complete small trajectories all hit 1. The chosen fusion horizon
    # is too short to reach 7 from this entire physical interval.
    lo, length, ell, d, t = 8192, 4096, 2, 5, 7
    p = 2**ell*d
    selected = {1, 3, 4, 7, 12, 15, 19}
    def label(x):
        for _ in range(2000):
            if x in (1, 7):
                return int(x == 7)
            x = step(x)
        raise ValueError("unknown fixed-target label")
    def profile(x):
        grade = 0
        for _ in range(t):
            grade += x % 2
            x = step(x)
        return x, grade
    labels = {x: label(x) for x in range(lo, lo+length+p)}
    profiles = {x: profile(x) for x in labels}
    xs = [x for x in range(lo, lo+length) if x % p in selected]
    total = sum(labels[x] for x in range(lo, lo+length))
    baseline = sum(labels[x] for x in xs)
    shifted = sum(labels[x+j] for x in xs for j in range(p))
    failed = sum(profiles[x] != profiles[x+j] for x in xs for j in range(p))
    require(abs(p*baseline-shifted) <= failed, "label propagation by counted fusion")
    require(abs(shifted-len(selected)*total) <= 2*p*len(selected), "cyclic boundary average")
    return {"interval": [lo, lo+length-1], "target": 7, "period": p, "selected": sorted(selected),
            "clock": t, "selected_starts": len(xs), "target_population": total,
            "selected_target_population": baseline, "sum_over_shifts": shifted,
            "total_unfused_shifted_pairs": failed}


def main():
    fail = 2*Fraction(3,4)**82 + Fraction(49,8190)
    require(fail < Fraction(1,100), "anchor probability budget")
    print(json.dumps({"scope": "finite exact checks; no asymptotic or pointwise extinction claim",
                      "all_time_complete_small_window": population(), "finite_law": haar_cutoff(),
                      "unit_anchors": protected_ball(), "periodic_label": periodic_label(),
                      "unit_anchor_failure_budget": str(fail)}, indent=2))


if __name__ == "__main__":
    main()

