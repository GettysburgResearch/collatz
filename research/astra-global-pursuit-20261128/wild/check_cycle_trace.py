"""Exact finite checks of the prefix pullback and the ordinary one-cycle lap."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json


def require(claim, detail):
    if not claim:
        raise RuntimeError(detail)


def residue(value, modulus):
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def test(value, root, power):
    return (1 - value / root) ** (-power) if value < root else Q(0)


def prefix(word):
    offset, scale = Q(0), Q(1)
    for exponent in word:
        offset += scale / (1 << exponent)
        scale *= Q(3, 1 << exponent)
    return offset, scale


def inverse(root, word):
    state = root
    residual = Q(1)
    for exponent in word:
        numerator = (state << exponent) - 1
        if numerator % 3:
            return None
        state = numerator // 3
        if state % 3 == 0:
            return None
        require(state > 0 and state % 2, "ordinary parent")
        residual *= Q(3 * state, 3 * state + 1)
    return state, residual


def conductor_checks():
    roots = [a for a in range(1, 35, 2) if a % 3]
    tail_seeds = [(Q(0), Q(1)), (Q(2), Q(2)), (Q(1), Q(1)),
                  (Q(10, 3), Q(5, 2)), (Q(257, 8), Q(5)),
                  (Q(65537, 8), Q(1, 2))]
    counters = {"finite_word_seed_root_tuples": 0, "selected_full_congruences": 0,
                "singular_test_identities": 0, "strict_cutoff_equalities": 0,
                "tail_above_cutoff": 0}
    for length in range(5):
        modulus = 3 ** (length + 1)
        for word in product(range(1, 5), repeat=length):
            offset, scale = prefix(word)
            for root in roots:
                path = inverse(root, word)
                for tail_r, tail_z in tail_seeds:
                    counters["finite_word_seed_root_tuples"] += 1
                    output_z = offset + scale * tail_z
                    left = residue(output_z, modulus) == root % modulus
                    right = path is not None and residue(tail_z, 3) == path[0] % 3
                    require(left == right, "one unpeeled ternary digit")
                    if not left:
                        continue
                    counters["selected_full_congruences"] += 1
                    state, residual = path
                    value = offset + scale * tail_r
                    require(state * scale / root == residual, "physical scaling")
                    require((1 - value / root) == residual * (1 - tail_r / state),
                            "relative deficit")
                    if value == root:
                        counters["strict_cutoff_equalities"] += 1
                    if value > root:
                        counters["tail_above_cutoff"] += 1
                    for power in (0, 1, 2):
                        lhs = Q(modulus, 1 << sum(word)) * test(value, root, power)
                        rhs = 3 * scale * residual ** (-power) * test(tail_r, state, power)
                        require(lhs == rhs, "unbounded power pullback")
                        counters["singular_test_identities"] += 1
    return counters


def lap_checks():
    counts = {"first_exit_prefixes": 0, "ordinary_padded_laps": 0}
    for exit_gap in (4, 8, 10, 14):
        for length in range(4):
            for rest in product(range(1, 7), repeat=length):
                word = (exit_gap,) + rest
                path = inverse(1, word)
                if path is None:
                    continue
                y, residual = path
                require(y != 1, "off-cycle state")
                offset, scale = prefix(word)
                require(1 - offset == residual == scale * y, "base correction")
                require(scale / residual == Q(1, y), "critical cancellation")
                counts["first_exit_prefixes"] += 1
                for laps in range(8):
                    padded = (2,) * laps + word
                    state, padded_residual = inverse(1, padded)
                    new_offset, new_scale = prefix(padded)
                    lap_weight = Q(3, 4) ** laps
                    require(state == y, "true lap endpoint")
                    require(padded_residual == residual * lap_weight, "relative lap scale")
                    require(new_scale == scale * lap_weight, "prefix weight")
                    require(1 - new_offset == padded_residual, "real lap shift")
                    counts["ordinary_padded_laps"] += 1
    return counts



def physical_entrance_partition():
    # A finite odd source population, with a deadline that leaves survivors.
    # Entries are measured through their last off-cycle odd parent. These
    # finite fractions test the normalization only, not limiting densities.
    sources = tuple(range(1001, 5000, 2))
    counts = {}
    arrivals = 0
    for source in sources:
        cur = source
        parent = None
        for _ in range(30):
            numerator = 3 * cur + 1
            next_state = numerator // (numerator & -numerator)
            if next_state == 1:
                parent = cur
                break
            cur = next_state
        if parent is not None:
            arrivals += 1
            counts[parent] = counts.get(parent, 0) + 1
    require(0 < arrivals < len(sources), "nontrivial finite census")
    require(any(y % 3 == 0 for y in counts), "finite nonunit last parents included")
    observed = Q(arrivals, len(sources))
    # Use units L=log(4/3) for both residues: delta/L=1/2 and w(1)/L=1.
    delta_over_L = Q(1, 2)
    root_coefficient = sum(delta_over_L * Q(count, len(sources))
                           for count in counts.values())
    require(root_coefficient == observed / 2, "standard cycle root normalization")
    require(2 * root_coefficient == observed, "summed cycle normalization / delta")
    return {"finite_odd_anchor_sources": len(sources),
            "observed_arrivals_by_deadline": arrivals,
            "distinct_last_parents": len(counts)}


def finite_renewal():
    def parents(a):
        for gap in range(1, 9):
            vals = inverse(a, (gap,))
            if vals is not None:
                yield vals

    @lru_cache(None)
    def value(k, a, u):
        if k == 1:
            return Q(1, a)
        return sum(scale ** u * value(k - 1, y, u)
                   for y, scale in parents(a))

    controls = 0
    for u in (0, 1, 2):
        lap = Q(3, 4) ** u
        exits = [(y, c) for y, c in parents(1) if y != 1]
        for deadline in range(1, 8):
            direct = sum(value(k, 1, u) for k in range(1, deadline + 1))
            repeat_only = sum(lap ** j for j in range(deadline))
            by_exit = sum(c ** u * value(t, y, u)
                          * sum(lap ** j for j in range(deadline - t))
                          for y, c in exits for t in range(1, deadline))
            require(direct == repeat_only + by_exit, "finite conductor lap calendar")
            controls += 1
    return {"exact_finite_lap_calendars": controls}


if __name__ == "__main__":
    print(json.dumps(conductor_checks() | lap_checks() | finite_renewal()
                     | physical_entrance_partition(), indent=2, sort_keys=True))
