#!/usr/bin/env python3
"""Exact finite controls for the actual Taylor germ and source collisions.

Run from any directory with Python 3. Every guard survives python -O.
The infinite prime-growth and stationary-limit arguments are written
proofs, not conclusions of this bounded replay.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from replay_jets import run_checks as jet_checks


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def ordinary_odd_states(source):
    x, seen, odd = source, set(), []
    for _ in range(10000):
        require(x > 0 and x not in seen, "ordinary fixture positivity/repetition")
        seen.add(x)
        if x % 2:
            odd.append(x)
        if x == 1:
            return odd
        x = (3 * x + 1) // 2 if x % 2 else x // 2
    raise RuntimeError("ordinary fixture exceeded its explicit finite cap")


def compare_probabilities(pi, mu, packing_bound):
    require(sum(pi.values()) == sum(mu.values()) == 1, "probability normalization")
    require(all(x >= 0 for x in (*pi.values(), *mu.values())), "positive mass")
    support = pi.keys() | mu.keys()
    differences = [pi.get(r, 0) - mu.get(r, 0) for r in support]
    tv = sum(abs(x) for x in differences) / 2
    square_distance = sum(x * x for x in differences)
    require(square_distance <= 2 * tv * tv, "zero-sum L2/TV inequality")
    cpi = sum(x * x for x in pi.values())
    cmu = sum(x * x for x in mu.values())
    require(cpi <= packing_bound, "finite empirical packing bound")
    # Exact radical elimination checks (sqrt(cmu)-sqrt(bound))_+ <= sqrt(2)*TV.
    # When cmu > bound, squaring and rearranging leaves A <= 2*sqrt(cmu*bound).
    for bound in (cpi, packing_bound):
        if cmu > bound:
            a = cmu + bound - 2 * tv * tv
            require(a <= 0 or a * a <= 4 * cmu * bound,
                    "exact collision discrepancy inequality")
    return [str(cpi), str(cmu), str(tv)]


def collision_checks():
    counts = Counter()
    digest = sha256()
    sources = list(range(1, 65)) + [85, 6171, 77031, 837799]
    for source in sources:
        odd = ordinary_odd_states(source)
        require(len(set(odd)) == len(odd), "distinct actual odd states")
        counts["ordinary_sources"] += 1
        for n in sorted({1, min(8, len(odd)), max(1, len(odd) // 2), len(odd)}):
            states = odd[:n]
            height = max(states)
            counts["actual_prefixes"] += 1
            moduli = sorted({1, 2, 4, 8, 16, 3, 9, 27, 81, 243, height + 1})
            for modulus in moduli:
                buckets = Counter(x % modulus for x in states)
                pairs = [(a, b) for a in states for b in states
                         if a % modulus == b % modulus]
                require(len(pairs) == sum(v * v for v in buckets.values()),
                        "independent full ordered-pair and bucket counts")
                images = {(a, b // modulus) for a, b in pairs}
                require(len(images) == len(pairs), "full quotient injection")
                require(sum(a == b for a, b in pairs) == n, "entire diagonal retained")
                require(n <= len(pairs) <= n * (height // modulus + 1),
                        "height packing with full ordinary sources")
                counts["ordered_collision_pairs"] += len(pairs)
                counts["off_diagonal_pairs"] += len(pairs) - n
                counts["source_modulus_cases"] += 1
                if modulus > height:
                    require(len(pairs) == n, "exact below-modulus diagonal")
                    counts["exact_diagonal_cases"] += 1
                pi = {r: Fraction(v, n) for r, v in buckets.items()}
                bound = Fraction(height // modulus + 1, n)
                references = [{0: Fraction(1)}]
                mixed = {r: mass / 3 for r, mass in pi.items()}
                mixed[0] = mixed.get(0, Fraction(0)) + Fraction(2, 3)
                references.append(mixed)
                if modulus <= 243:
                    references.append({r: Fraction(1, modulus) for r in range(modulus)})
                for mu in references:
                    record = [source, n, modulus, len(pairs),
                              compare_probabilities(pi, mu, bound)]
                    digest.update(json.dumps(record, separators=(",", ":")).encode())
                    digest.update(b"\n")
                    counts["exact_probability_comparisons"] += 1
    require(counts["off_diagonal_pairs"] > 0, "off-diagonal controls were exercised")
    require(counts["exact_diagonal_cases"] > 0, "diagonal regime was exercised")
    return {
        "scope": "Literal finite odd-state prefixes of specified convergent sources; all pairs retained. Reference vectors are finite controls, not asserted stationary orbit laws.",
        "sources": sources,
        "counts": dict(sorted(counts.items())),
        "ordered_records_sha256": digest.hexdigest(),
        "infinite_convergence_rate_inferred": False,
    }


def main():
    root = Path(__file__).resolve().parent
    names = {"RATIONAL_SELECTION.md", "CYCLE_ARITHMETIC.md", "COLLISION_CLOSURE.md"}
    bindings = {p.name: sha256(p.read_bytes()).hexdigest()
                for p in sorted(root.iterdir())
                if p.suffix in (".py", ".lean") or p.name in names}
    result = {
        "scope": "Bounded exact arithmetic controls only; no proof of universal arithmetic germs, limiting density, stationary transfer, or full Collatz by execution.",
        "source_sha256": bindings,
        "jets": jet_checks(),
        "collisions": collision_checks(),
        "success": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
