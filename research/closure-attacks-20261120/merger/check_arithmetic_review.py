#!/usr/bin/env python3
"""Independent finite controls for the exact-byte arithmetic review."""

from itertools import product
import json
from math import prod


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    # Enumerate the abstract clock hypotheses directly. Testing h=H/2
    # permits integer-only verification after multiplying the inequality by H.
    states = [(x, z) for x in range(5) for z in range(x + 1)]
    accepted = checked = 0
    for length in range(1, 5):
        for sequence in product(states, repeat=length):
            xs = [item[0] for item in sequence]
            zs = [item[1] for item in sequence]
            if any(xs[i + 1] > xs[i] + 1 for i in range(length - 1)):
                continue
            ts = [3 * i - xs[i] for i in range(length)]
            if any(min(zs[i], zs[j]) >= ts[j] - ts[i]
                   for j in range(length) for i in range(j)):
                continue
            accepted += 1
            for twice_h in range(1, 18):
                marked = sum(2 * z >= twice_h for z in zs)
                high = sum(4 * x >= twice_h for x in xs)
                budget = 10 * high
                if twice_h <= 4 * xs[0]:
                    budget += twice_h + 2 * xs[0]
                require(marked * twice_h <= budget,
                        ("localized tail", sequence, twice_h))
                checked += 1
    # Removing the initial component term would fail on this legal one-state
    # input; there are no pairwise packing hypotheses to impose.
    require(1 * 200 > 10 * 1, "source-term control should fail without its charge")
    rows = [
        ([19, 25, 29, 55, 83], [1, 1, 1, 1, 1], [29, 19, 11, 83, 125], 8),
        ([5, 7, 25, 55, 65, 83, 95], [2, 2, 1, 3, 1, 3, 1],
         [1, 11, 19, 83, 49, 125, 143], 21),
    ]
    circulation_controls = []
    for sources, weights, expected, total in rows:
        targets, exponents = [], []
        for n in sources:
            m, a = 3 * n + 1, 0
            while m % 2 == 0:
                m //= 2
                a += 1
            targets.append(m)
            exponents.append(a)
        require(targets == expected, "ordinary successor mismatch")
        before = prod(n ** w for n, w in zip(sources, weights))
        after = prod(n ** w for n, w in zip(targets, weights))
        require(before == after, "multiplicative balance mismatch")
        require(sum(a * w for a, w in zip(exponents, weights)) == total,
                "total division mismatch")
        require(set(targets) != set(sources), "control unexpectedly a cycle")
        circulation_controls.append({"sources": sources, "common_product": before})
    print(json.dumps({
        "status": "PASS",
        "scope": "independent exact finite controls; universal claims reviewed in writing",
        "abstract_states": "integer 0<=z<=x<=4; lengths 1..4; h=1/2,1,...,17/2",
        "admissible_sequences": accepted,
        "localized_tail_checks": checked,
        "source_term_omission_control": "fails as required at N=1, x0=z0=h=100",
        "circulation_controls": circulation_controls,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
