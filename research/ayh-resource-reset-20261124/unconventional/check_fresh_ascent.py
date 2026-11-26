"""Exact finite checks for signed inverse transport and the finite-orbit fork count."""

from fractions import Fraction
from itertools import product
import json
import math


def require(condition, message):
    if not condition:
        raise ValueError(message)


def subsets(items):
    items = tuple(items)
    for mask in range(1 << len(items)):
        yield {item for index, item in enumerate(items) if (mask >> index) & 1}


def orbit_set(mapping, seeds):
    states = set(seeds)
    active = list(seeds)
    while active:
        image = mapping[active.pop()]
        if image not in states:
            states.add(image)
            active.append(image)
    return states


def forks():
    maps = 0
    budgets = 0
    tests = 0
    for size in range(1, 5):
        for mapping in product(range(size), repeat=size):
            maps += 1
            for seeds in subsets(range(size)):
                states = orbit_set(mapping, seeds)
                forks = sum(max(0, sum(mapping[x] == z for x in states) - 1) for z in states)
                require(forks <= len(seeds), "total indegree excess budget")
                budgets += 1
                for restricted in subsets(states):
                    images = restricted
                    for clock in range(1, 5):
                        images = {mapping[x] for x in images}
                        require(len(restricted) <= len(images) + clock * len(seeds),
                                "iterated subset deficit")
                        tests += 1
    return {"maps": maps, "origin_sets": budgets, "iterated_subset_checks": tests}


def signed_words(max_depth, max_gap):
    layers = [[(1, 0, Fraction(1))]]
    used = {1}
    for depth in range(1, max_depth + 1):
        current = []
        for s, clock, correction in layers[-1]:
            for e in range(1, max_gap + 1):
                if depth == 1 and e == 1:
                    continue
                numerator = 2**e * s + 1
                if numerator % 3:
                    continue
                parent = numerator // 3
                require(parent > 1 and parent % 2, "fresh signed exact odd parent")
                require(parent not in used, "distinct first-hit signed words and layers")
                used.add(parent)
                weight = correction * Fraction(3 * parent, 3 * parent - 1)
                require(Fraction(3**depth, 2**(clock + e)) == weight / parent,
                        "signed correction identity")
                current.append((parent, clock + e, weight))
        layers.append(current)
    return layers


def ordinary(layers, max_gap):
    count = 0
    initial_rises = 0
    for j in range(1, len(layers)):
        for off in (2, 10, 22, 46, 122):
            q = 3**j * off - 1
            a = 2**j * off - 1
            v = a
            for _ in range(j):
                require(v % 2, "ordinary odd ascent departure")
                v = (3*v + 1) // 2
            require(v == q, "ordinary ascent has named terminal")
            initial_rises += 1
            current = [(q, 0)]
            for depth in range(1, j + 1):
                new = []
                for parent, clock in current:
                    for e in range(1, max_gap + 1):
                        if depth == 1 and e == 1:
                            continue
                        num = 2**e*parent-1
                        if num % 3 == 0:
                            new.append((num // 3, clock + e))
                predicted = sorted((2**h * ((q + 1) // 3**depth) - s, h)
                                   for s, h, _ in layers[depth])
                require(sorted(new) == predicted, "complete signed/positive first-entry transport")
                count += len(new)
                current = new
    return {"initial_rises": initial_rises, "positive_signed_endpoint_pairs": count}


def shell_bound():
    total = Fraction()
    for k in range(1, 400):
        high = 2**(k-1)
        best = high
        for p in range(k + 1):
            if p:
                high -= math.comb(k-1, p-1)
            best = min(best, 2 * 3**p + k + high)
        total += Fraction(best, 2**k)
    require(total < 22, "finite signed reciprocal sum")
    require(5**200 < 2**275 * 3**120 and 3**24 < 2**39, "entropy tail exponents")
    return {"first_shell": 1, "last_shell": 399, "exact_weighted_sum": str(total),
            "upper_bound": 22}


def signed_winners():
    # Beyond this cutoff, e^9 < 3^9 and therefore g < 3/8.
    cap = 8 * 3**8
    memory = {1: (0, 0)}
    ranked = []
    terminated = 0
    max_seen = 0
    for s in range(3, cap, 2):
        value = s
        chain = []
        local = set()
        while value not in memory and value not in local:
            local.add(value)
            m = 3 * value - 1
            e = (m & -m).bit_length() - 1
            chain.append((value, e))
            value = m >> e
        result = memory.get(value)
        for item, gap in reversed(chain):
            if result is not None:
                result = (result[0] + 1, result[1] + gap)
            memory[item] = result
        result = memory[s]
        if result is not None:
            terminated += 1
            grade, clock = result
            if 8 * 3**grade >= 3 * 2**clock:
                ranked.append((s, grade, clock))
        max_seen = max([max_seen] + [item for item, _ in chain])
    require(ranked == [(3, 1, 3)], "unique signed first-visit gain at least 3/8")

    # Independent ordinary shortcut replay with no coalescence memoization.
    replay = []
    replay_terminated = 0
    for s in range(3, cap, 2):
        value, grade, clock = s, 0, 0
        history = set()
        while value != 1 and value not in history:
            history.add(value)
            if value % 2 == 1:
                value = (3 * value - 1) // 2
                grade += 1
            else:
                value //= 2
            clock += 1
        if value == 1:
            replay_terminated += 1
            if 8 * 3**grade >= 3 * 2**clock:
                replay.append((s, grade, clock))
    require(replay == ranked and replay_terminated == terminated, "independent signed shortcut census")
    return {"magnitude_cutoff_exclusive": cap, "odd_origins": len(range(3, cap, 2)),
            "first_hits_one": terminated, "certified_other_cycle": len(range(3, cap, 2)) - terminated,
            "max_odd_state_in_accelerated_census": max_seen, "maximizers": ranked}


if __name__ == "__main__":
    max_depth, max_gap = 8, 8
    layers = signed_words(max_depth, max_gap)
    diagnostics = {"max_odd_grade": max_depth, "max_gap": max_gap,
                   "capped_layer_sizes": [len(layer) for layer in layers[1:]],
                   "capped_minimum_magnitudes": [min(s for s, _, _ in layer) for layer in layers[1:]]}
    print(json.dumps({"signed_capped": diagnostics, "ordinary": ordinary(layers, max_gap),
                      "forks": forks(), "reciprocal_shells": shell_bound(),
                      "signed_winners": signed_winners()}, indent=2))
