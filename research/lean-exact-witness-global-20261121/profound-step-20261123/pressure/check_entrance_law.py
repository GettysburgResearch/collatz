#!/usr/bin/env python3
"""Exact finite controls for the ordinary entrance-law packet.

Actual inverse trees are truncated by depth and complete address quotient.
This is not a computation on an escaping component or a proof by census.
No assertions are used, so optimization cannot disable the checks.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path

TABLE = {
    1: {1: 2, 2: 4}, 2: {1: 1, 2: 3},
    4: {1: 6, 2: 2}, 5: {1: 3, 2: 5},
    7: {1: 4, 2: 6}, 8: {1: 5, 2: 1},
}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def odd_step(n: int) -> tuple[int, int]:
    need(n > 0 and n % 2 == 1, "positive odd source required")
    value, exponent = 3 * n + 1, 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return value, exponent


def parents(q: int, quotient_cap: int):
    for colour in (1, 2):
        for quotient in range(quotient_cap + 1):
            exponent = TABLE[q % 9][colour] + 6 * quotient
            value = (2**exponent * q - 1) // 3
            need(value > 0 and value % 2 == 1 and value % 3 == colour,
                 "illegal ordinary parent")
            need(odd_step(value) == (q, exponent), "wrong literal odd edge")
            yield (colour, quotient), exponent, value


def raw_tree(root: int, depth: int, quotient_cap: int, s: int):
    """Forward-independent enumeration by ordinary inverse addresses."""
    result = {}
    frontier = [(root, (), 0)]
    for k in range(depth + 1):
        following = []
        for n, address, exponent_sum in frontier:
            need(address not in result, "duplicate address")
            result[address] = (n, Fraction(3**(s*k), 2**(s*exponent_sum)),
                               exponent_sum)
            if k < depth:
                for branch, exponent, parent in parents(n, quotient_cap):
                    following.append((parent, address + (branch,),
                                      exponent_sum + exponent))
        frontier = following
    need(len({entry[0] for entry in result.values()}) == len(result),
         "nonperiodic control tree repeated a source")
    return result


def killed_law(root: int, depth: int, quotient_cap: int, s: int):
    """Independent recursive potential and killed-chain recursion."""
    @lru_cache(None)
    def z(q: int, d: int) -> Fraction:
        if d == 0:
            return Fraction(1)
        return 1 + sum((Fraction(3, 2**a)**s * z(v, d-1)
                        for _, a, v in parents(q, quotient_cap)), Fraction())

    @lru_cache(None)
    def terminal(q: int, d: int):
        answer = defaultdict(Fraction)
        answer[q] += 1 / z(q, d)
        row = 1 / z(q, d)
        if d:
            for _, a, v in parents(q, quotient_cap):
                probability = Fraction(3, 2**a)**s * z(v, d-1) / z(q, d)
                row += probability
                for n, value in terminal(v, d-1):
                    answer[n] += probability * value
        need(row == 1, "killed row lost probability")
        return tuple(sorted(answer.items()))
    return z(root, depth), dict(terminal(root, depth))


def main() -> None:
    counts = defaultdict(int)
    rows = []
    for root in (5, 7, 41, 65, 193):
        for s in (2, 3):
            tree = raw_tree(root, 4, 1, s)
            z, actual = killed_law(root, 4, 1, s)
            direct_z = sum((v[1] for v in tree.values()), Fraction())
            need(z == direct_z, "independent potential disagreement")
            direct = {n: w/z for n, w, _ in tree.values()}
            need(actual == direct, "terminal law disagrees with full path sum")
            need(sum(actual.values()) == 1, "terminal law is not a probability")
            counts['ordinary_tree_cases'] += 1
            counts['terminal_atoms_compared'] += len(actual)

            sibling = raw_tree(64*root+21, 4, 1, s)
            sibling_z = sum((v[1] for v in sibling.values()), Fraction())
            ratio = sibling_z / z
            normalizer, fractional = Fraction(), Fraction()
            tilted = {}
            for address, (n, w, a) in tree.items():
                n2, w2, a2 = sibling[address]
                delta = a2-a
                cost = Fraction(2)**(-s*delta)
                need(w2 == cost*w, "wrong exact signed pressure cost")
                original = w/z
                target = w2/sibling_z
                need(target == original*cost/ratio, "wrong transported density")
                tilted[address] = target
                normalizer += original*cost
                fractional += original*Fraction(2)**(-delta)
                counts['balanced_density_atoms'] += 1
                if delta and not counts['wrong_cost_sign_rejected']:
                    need(w2 != Fraction(2)**(s*delta)*w,
                         "wrong-sign control failed to discriminate")
                    counts['wrong_cost_sign_rejected'] += 1
            need(normalizer == ratio, "lost a full finite address")
            need(fractional**s <= ratio, "fractional moment bound failed")
            counts['fractional_moment_cases'] += 1
            for shift in (0, 1, 10, 100):
                shifted_ratio = Fraction(2)**(-s*shift)*ratio
                for address, (n, w, a) in tree.items():
                    delta = sibling[address][2]-a
                    value = (w/z)*Fraction(2)**(-s*(delta+shift))/shifted_ratio
                    need(value == tilted[address], "normalized tilt changed under scale")
                    counts['normalizer_blindness_atoms'] += 1
            need(sum(actual.values())-actual[root] != 1,
                 "omitted killing was not detected")
            need(sum(actual.values())-next(iter(actual.values())) != 1,
                 "lost source was not detected")
            counts['omitted_killing_rejected'] += 1
            counts['lost_source_rejected'] += 1
            rows.append({'root': root, 's': s, 'atoms': len(actual),
                         'green_ratio': str(ratio),
                         'fractional_moment': str(fractional)})

    # Literal ordinary phase controls. Only an injective finite ray is used.
    ray = [65]
    for _ in range(6):
        ray.append(odd_step(ray[-1])[0])
    need(len(set(ray)) == len(ray), "phase control ray must be injective")
    ray_index = {q: j for j, q in enumerate(ray)}
    pool = set()
    for root in ray:
        pool.update(v[0] for v in raw_tree(root, 3, 1, 2).values())
    phases = {}
    for n in sorted(pool):
        x, k = n, 0
        while x not in ray_index:
            x = odd_step(x)[0]
            k += 1
            need(k <= 3, "generated source missed its guaranteed ray hit")
        m = ray_index[x]
        phase = k-m
        phases[n] = (phase, m)
        for j in range(m, len(ray)):
            tau = j+phase
            need(tau >= 0, "negative actual hitting time")
            x = n
            for _ in range(tau):
                x = odd_step(x)[0]
            need(x == ray[j] and tau-j == phase, "ordinary phase changed")
            counts['ordinary_phase_hits'] += 1
    # The phase identity fails without injectivity: U(1)=1 has hits at 0 and 1.
    need(odd_step(1)[0] == 1 and 0-0 != 1-0,
         "periodic-ray rejection control failed")
    counts['periodic_phase_control'] += 1

    # Generic finite source conditioning, not the infinite r of an escaping ray.
    weights = {n: Fraction(1, n*n) for n in pool}
    total = sum(weights.values(), Fraction())
    reference = {n: w/total for n, w in weights.items()}
    for j in range(len(ray)):
        selected = {n for n in pool if phases[n][1] <= j}
        mass = sum((weights[n] for n in selected), Fraction())
        law = {n: weights[n]/mass if n in selected else Fraction() for n in pool}
        tv = sum((abs(law[n]-reference[n]) for n in pool), Fraction())/2
        need(tv == 1-mass/total, "source conditioning TV identity failed")
        counts['finite_conditioning_cases'] += 1

    for terms in range(1, 33):
        chronological_log_moment = sum((Fraction(1, 2**(k+1))*2**k
                                       for k in range(terms)), Fraction())
        need(chronological_log_moment == Fraction(terms, 2),
             "finite entropy versus clock control failed")
        counts['chronological_entropy_controls'] += 1

    # The empty-word cost stays zero in this normalization control.
    # It is an abstract two-part probability law, not a Collatz realization.
    for s in (2, 3):
        for length in (1, 2, 5, 10, 50, 100):
            t = Fraction(1, 2**(s*length))
            epsilon = t*t
            ratio = epsilon + (1-epsilon)*t
            root_density, other_density = 1/ratio, t/ratio
            need(ratio == t+t*t-t*t*t and t <= ratio,
                 "anchored normalizer identity failed")
            tv = epsilon*(root_density-1)
            need(0 <= tv <= t and other_density <= 1,
                 "anchored law did not merge")
            for cutoff in (Fraction(2), Fraction(10), Fraction(1000), 1/t):
                tail = epsilon*root_density if root_density > cutoff else Fraction()
                need(tail <= 1/cutoff, "uniform-integrability modulus failed")
                counts['anchored_uniform_integrability_cases'] += 1

    # Vigon Prop. 3.3, p.885, prints the terminal-state denominator.
    # The transient two-state matrix P(x,y)=1/2 rejects that orientation.
    edge = Fraction(1, 2)
    zx, zy = 1+edge, Fraction(1)
    need(1/zx + edge/zx == 1, "starting-state normalization failed")
    need(1/zx + edge/zy != 1, "printed terminal-state typo not detected")
    counts['literature_denominator_control'] += 1

    here = Path(__file__).resolve().parent
    print(json.dumps({
        'status': 'PASS',
        'scope': ('finite actual inverse trees and ordinary phases; finite generic '
                  'conditioning and normalization controls; no escaping source '
                  'or infinite analytic theorem is tested by census'),
        'counts': dict(sorted(counts.items())),
        'phase_ray': ray,
        'ordinary_phase_sources': len(pool),
        'finite_tree_rows': rows,
        'source_sha256': {name: sha256((here/name).read_bytes()).hexdigest()
                          for name in ('ORDINARY_ENTRANCE_LAW.md', 'EntranceLaw.lean',
                                       'check_entrance_law.py')},
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
