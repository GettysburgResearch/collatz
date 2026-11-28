"""Enumerate finite multiplier resonance graphs and verify their exact centers."""
from fractions import Fraction
from itertools import product
import hashlib
import json


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def v2(n):
    return (n & -n).bit_length() - 1


def analyze(start, step, length, height, precision):
    modulus = 1 << precision
    require((1 << (precision - v2(step))) > 8 * length * 3 ** (2 * height),
            "finite integer-dominance guard")
    slopes = [start + step * i for i in range(length)]
    rows = {}
    for i, slope in enumerate(slopes):
        slot = rows.setdefault(slope % modulus, [])
        slot.append(i)
    edges = []
    for i, slope in enumerate(slopes):
        for h in range(1, height + 1):
            residue = 3 ** h * slope % modulus
            edges.extend((i, j, h) for j in rows.get(residue, []) if j != i)
    centers = {Fraction(i) - Fraction(j - i, 3 ** h - 1) for i, j, h in edges}
    require(len(centers) <= 1, (start, step, length, centers))
    if centers:
        center = centers.pop()
        require(center.denominator % 3 != 0, center)
        discarded = (center.numerator * pow(center.denominator, -1, 3)) % 3
        for i, j, h in edges:
            require(j - center == 3 ** h * (i - center) and j % 3 == discarded,
                    (i, j, h, center))
    neighbors = [set() for _ in slopes]
    for i, j, h in edges:
        neighbors[i].add(j)
        neighbors[j].add(i)
    # Integer form of deg <= 2 + log_3(2m+1).
    for ns in neighbors:
        require(len(ns) < 2 or 3 ** (len(ns) - 2) <= 2 * length + 1, len(ns))
    return edges


def run():
    families = edges_seen = vertices = near_only = zero_edges = 0
    max_digit_length = max_edges = 0
    hashed = hashlib.sha256()
    for length in (5, 12, 29, 60, 101):
        for height in (2, 4, 7):
            for binary_order, odd_step in product((1, 2, 4), (1, 5)):
                # Deliberately lift a small two-adic progression by huge,
                # independent multiples of its full word modulus.
                small_step = (1 << binary_order) * odd_step
                precision = binary_order + (8 * length * 3 ** (2 * height)).bit_length()
                modulus = 1 << precision
                for small_start in (1, 3, 7, 19, -1, -9, 1 - small_step * (length // 2)):
                    start = small_start + modulus * (1 << (81 + length))
                    step = small_step + modulus * ((1 << (60 + height)) + 3)
                    require(start > 0 and start % 2 == 1 and v2(step) == binary_order, "lift")
                    edges = analyze(start, step, length, height, precision)
                    families += 1
                    vertices += length
                    edges_seen += len(edges)
                    zero_edges += not edges
                    max_edges = max(max_edges, len(edges))
                    max_digit_length = max(max_digit_length, (start + (length - 1) * step).bit_length())
                    for i, j, h in edges:
                        if start + j * step != 3 ** h * (start + i * step):
                            near_only += 1
                    hashed.update(f"{length} {height} {binary_order} {odd_step} {small_start} {edges}\n".encode())
    require(near_only > 100 and zero_edges > 0 and max_edges >= 40, "fixture diversity")
    # At small precision the four-term rigidity can fail. Exhibit one collision
    # graph without a common rational center when the finite guard is omitted.
    low = None
    for start in range(1, 32, 2):
        slopes = [start + 2 * i for i in range(12)]
        edges = [(i, j, h) for i, a in enumerate(slopes) for j, b in enumerate(slopes)
                 for h in range(1, 4) if i != j and (3 ** h * a - b) % 32 == 0]
        centers = {Fraction(i) - Fraction(j-i, 3 ** h-1) for i,j,h in edges}
        if len(centers) > 1:
            low = {"start": start, "step": 2, "length": 12, "modulus": 32,
                   "distinct_centers": len(centers)}
            break
    require(low is not None, "low-precision negative control")
    return {"families": families, "vertices": vertices, "positive_exponent_edges": edges_seen,
            "edges_not_equalities_between_original_slopes": near_only, "empty_graphs": zero_edges,
            "largest_edge_count": max_edges, "largest_actual_multiplier_bits": max_digit_length,
            "sorted_edge_tables_sha256": hashed.hexdigest(), "negative_control": low,
            "scope": "Finite full-modulus graph and index-center arithmetic. The asymptotic Subspace Theorem and Brownian convergence are written inputs."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
