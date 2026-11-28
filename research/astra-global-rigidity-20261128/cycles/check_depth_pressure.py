"""Exact finite checks of the replica exchange and positive-excursion identities."""

from collections import Counter
from fractions import Fraction
import json


def verify(condition, message):
    if not condition:
        raise ValueError(message)


def floor_log2_fraction(value):
    exponent = value.numerator.bit_length() - value.denominator.bit_length()
    if exponent >= 0:
        return exponent - (value.numerator < value.denominator << exponent)
    return exponent - (value.numerator << -exponent < value.denominator)


def rotation_data(initial_weight, length):
    floors = [floor_log2_fraction(Fraction(3**t, 1) / initial_weight) for t in range(length + 1)]
    caps = tuple(floors[t + 1] - floors[t] - 1 for t in range(length))
    weights = tuple(initial_weight * 2**floors[t] / 3**t for t in range(length))
    verify(floors[0] == 0 and set(caps) <= {0, 1}, "invalid rotation")
    return caps, weights


def pinned_paths(caps):
    partials = [(0,)]
    for cap in caps[:-1]:
        partials = [prefix + (j,) for prefix in partials for j in range(prefix[-1] + cap + 1)]
    return [prefix + (0,) for prefix in partials] if caps else [(0,)]


def reward(path, weights):
    return sum((w / 2**j for w, j in zip(weights, path)), start=Fraction(0))


def usable(x, y, caps, t):
    return max(x[t + 1], y[t + 1]) <= min(x[t], y[t]) + caps[t]


def validate_family(initial_weight, length, totals):
    caps, weights = rotation_data(initial_weight, length)
    paths = pinned_paths(caps)
    universe = set(paths)
    weights_by_path = {path: reward(path, weights) for path in paths}
    totals["cases"] += 1
    totals["pinned_paths"] += len(paths)

    if length >= 2:
        excursions = {path for path in paths if all(j > 0 for j in path[1:-1])}
        shifted_family = set(pinned_paths(caps[1:])) if caps[0] else set()
        shifted = {(tuple(j - 1 for j in path[1:-1]) + (0,)): path for path in excursions}
        verify(set(shifted) == shifted_family and len(shifted) == len(excursions), "excursion bijection")
        expected = Counter(weights[0] + reward(path, weights[1:]) / 2 for path in shifted_family)
        observed = Counter(weights_by_path[path] for path in excursions)
        verify(observed == expected, "excursion reward polynomial")
        totals["strict_excursions"] += len(excursions)

    for ix, x in enumerate(paths):
        for y in paths[ix:]:
            totals["unordered_replica_pairs"] += 1
            low = tuple(map(min, x, y))
            high = tuple(map(max, x, y))
            verify(low in universe and high in universe, "lattice closure")
            pair_reward = weights_by_path[x] + weights_by_path[y]
            verify(weights_by_path[low] + weights_by_path[high] == pair_reward, "lattice reward")
            good = tuple(usable(x, y, caps, t) for t in range(length))
            for i in range(length):
                for j in range(i + 1, length + 1):
                    totals["edge_intervals"] += 1
                    first = next((t for t in range(i, j) if good[t]), None)
                    if 0 in x[i : j + 1] and 0 in y[i : j + 1]:
                        verify(first is not None, "two zero visits without a usable edge")
                        totals["both_visit_zero"] += 1
                    if first is None:
                        totals["no_usable_edge"] += 1
                        continue
                    cut = first + 1
                    u, w = x[:cut] + y[cut:], y[:cut] + x[cut:]
                    verify(u in universe and w in universe, "swapped legality")
                    verify(weights_by_path[u] + weights_by_path[w] == pair_reward, "swapped weight")
                    verify(next(t for t in range(i, j) if usable(u, w, caps, t)) == first, "first edge invariance")
                    verify((u[:cut] + w[cut:], w[:cut] + u[cut:]) == (x, y), "swap involution")
                    verify(u[i] == x[i] and w[i] == y[i] and u[j] == y[j] and w[j] == x[j], "endpoint exchange")
                    totals["first_edge_swaps"] += 1
                    if x[j] == y[j] and all(x[t] != y[t] for t in range(i, j)):
                        totals["right_endpoint_only_equal"] += 1


def main():
    totals = Counter()
    for initial_weight in (Fraction(1), Fraction(3, 4), Fraction(4, 7), Fraction(7, 8)):
        for length in range(2, 8):
            validate_family(initial_weight, length, totals)
    verify(totals["no_usable_edge"] > 0 and totals["right_endpoint_only_equal"] > 0, "missing boundary controls")
    print(json.dumps(dict(sorted(totals.items())), indent=2))


if __name__ == "__main__":
    main()
