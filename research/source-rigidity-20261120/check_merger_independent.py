#!/usr/bin/env python3
"""Independent rational-affine and literal-path reconstruction; finite scope."""

from fractions import Fraction as F
from hashlib import sha256
import json


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def step(n):
    need(type(n) is int and n > 0, "positive ordinary input")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def trajectory(n, length):
    values = [n]
    for _ in range(length):
        values.append(step(values[-1]))
    return values


def hit(n):
    values = [n]
    odd_count = 0
    while values[-1] != 1:
        need(len(values) < 10000, "finite control first-hit guard")
        odd_count += values[-1] % 2
        values.append(step(values[-1]))
    return len(values) - 1, odd_count, values


def valuation(n, p):
    need(n > 0 and p >= 2, "valuation domain")
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count


# Each row is transcribed from the frozen proof, not imported from its checker.
# Last triple is the advertised endpoint (c*n+d)/e.
CELLS = (
    (12, 11, "I", 8, 7, (2, -1, 3)),
    (16, 3, "OOEE", 9, 2, (9, 5, 16)),
    (24, 7, "MOOEVI", 18, 5, (3, -1, 4)),
    (32, 11, "OOEOE", 27, 10, (27, 23, 32)),
    (16, 15, "OMOOEVII", 12, 11, (3, -1, 4)),
    (32, 23, "OOOEE", 27, 20, (27, 19, 32)),
    (96, 91, "MOOVOEE", 81, 77, (27, 7, 32)),
    (20, 3, "OV", 6, 1, (3, 1, 10)),
    (20, 15, "OOV", 9, 7, (9, 5, 20)),
    (60, 51, "ODDIV", 48, 41, (4, 1, 5)),
    (60, 27, "OODMIIVV", 24, 11, (2, 1, 5)),
    (160, 39, "OMOOVOEV", 81, 20, (81, 41, 160)),
    (160, 59, "OOEMOODDVDIVIII", 128, 47, (4, -1, 5)),
)
AFFINE = {
    "D": (F(2), F(0)), "E": (F(1, 2), F(0)),
    "O": (F(3, 2), F(1, 2)), "I": (F(2, 3), F(-1, 3)),
    "M": (F(5), F(0)), "V": (F(1, 5), F(0)),
}


def reconstruct_cells():
    certificates = []
    total = 0
    for modulus, residue, word, end_a, end_b, expression in CELLS:
        need(480 % modulus == 0 and modulus % 4 == 0 and residue % 4 == 3, "common cover grid")
        a, b = F(modulus), F(residue)
        trace = [[int(a), int(b)]]
        for letter in word:
            need(a.denominator == b.denominator == 1 and a > 0 and b > 0, "positive integral affine input")
            aa, bb = int(a), int(b)
            if letter == "E": need(aa % 2 == bb % 2 == 0, "universal even input")
            if letter == "O": need(aa % 2 == 0 and bb % 2 == 1, "universal odd input")
            if letter == "I": need(aa % 3 == 0 and bb % 3 == 2, "universal inverse domain")
            if letter in "MV": need(aa % 3 == 0 and bb % 3 != 0, "universal ternary unit domain")
            if letter == "V": need(aa % 5 == bb % 5 == 0, "universal fifth divisibility")
            c, d = AFFINE[letter]
            a, b = c * a, c * b + d
            need(a.denominator == b.denominator == 1 and a > 0 and b > 0, "positive integral affine output")
            trace.append([int(a), int(b)])
            total += 1
        need((a, b) == (end_a, end_b), "listed affine endpoint")
        c, d, e = expression
        need(a == F(c * modulus, e) and b == F(c * residue + d, e), "listed endpoint in n")
        need(a < modulus and b < residue, "strict all-lift decrease")
        need(11 * a <= 10 * modulus and 11 * b <= 10 * residue, "all-lift 10/11 contraction")
        certificates.append({"modulus": modulus, "residue": residue, "word": word, "trace": trace})
    covered = [r for r in range(480) if any(r % m == a for m, a, *_ in CELLS)]
    need(covered == list(range(3, 480, 4)), "exact complete 120-cell cover")
    need(max(len(row[2]) for row in CELLS) == 15, "maximum augmented word length")
    for u in range(16):
        n = 31 + 48 * u
        y = F(9 * n + 1, 8)
        need(y == 35 + 54 * u and y > n and int(y) % 2 and int(y) % 3, "self/larger unit demand")
    return certificates, total


def reconstruct_carries():
    tested = tuple(range(25)) + (31, 32, 47, 63, 64, 97)
    targets = odd_prefixes = nondescents = unit_sources = 0
    for r in tested:
        k, ell = 6 * r + 3, 2 * r + 1
        need((2 ** (k + 2) - 5) % 9 == 0, "ordinary antecedent integrality")
        x = (2 ** (k + 2) - 5) // 9
        M = 2**k - 1
        z = (9**ell - 1) // 8
        need(x % 4 == 3 and x % 3 == 2 * r % 3, "exact antecedent residues")
        unit_sources += int(x % 3 != 0)
        d, h, source_path = hit(x)
        need((d, h) == (k + 2, 2), "supplied path first-hit clocks")
        need(source_path[1] == (2 ** (k + 1) - 1) // 3 and source_path[2] == 2**k, "two literal odd source steps")
        path = trajectory(5 * x, 6 * r + 8)
        targets += len(path) - 1
        need(path[2] == 5 * M and source_path[2] == M + 1, "CD1 exact carry debt")
        for j in range(ell + 1):
            cut = 2 + 3 * j
            need(path[cut] == 5 * 9**j * 2 ** (3 * (ell - j)) - 5, "all physical three-step block endpoints")
            if j < ell:
                need([v % 2 for v in path[cut:cut + 3]] == [1, 1, 0], "all block parity guards")
        need(valuation(9**ell - 1, 2) == 3 and path[-1] == 5 * z, "three final halvings and full reset")
        need(z % 2 == 1 and z % 3 == 1, "new antecedent is an odd ternary unit")
        need(all(v % 2 == 0 for v in path[-4:-1]), "three final even inputs")

        w = M
        for j in range(k):
            need(w == 3**j * 2 ** (k - j) - 1 and w > 1, "Mersenne ordinary odd prefix")
            raw = 3 * w + 1
            exponent = valuation(raw, 2)
            need(exponent == (1 if j < k - 1 else 2), "Mersenne exact division word")
            w = raw // (2**exponent)
            odd_prefixes += 1
        need(w == (3**k - 1) // 2 and w > 1, "Mersenne endpoint before first hit")
        lower_d = k + (3**k - 2).bit_length()
        need(lower_d >= 2 * k + 1 > d and M > x, "conditional reset depth lower bound")

        need(72 * (z - x) == 81 ** (r + 1) - 256 * 64**r + 31, "exact full-reset height difference")
        if r >= 5:
            need(z > x and all(v > 5 * x for v in path[1:]), "every nonempty target prefix remains above its source")
            nondescents += 1
        if r >= 15: need(z > 2 ** (6 * r + 5), "large-index first-hit depth comparison")
        if r % 4 == 3:
            need(z % 8 == 7 and [v % 2 for v in trajectory(z, 2)] == [1, 1, 1], "three odd input lower bound")
    return {"parameters": list(tested), "physical_target_edges": targets,
            "odd_Mersenne_edges": odd_prefixes, "all_prefix_nondescent_cases": nondescents,
            "F5_eligible_sources": unit_sources}


def controls():
    rows = []
    for x, y, clock in ((227, 511, 2), (15637498706147, 25736391511831, 50)):
        dx, hx, px = hit(x)
        dy, hy, py = hit(y)
        need(x % 2 and x % 3 and y % 2 and y % 3, "eligible convergent antecedents")
        need(y > x and dy > dx and hy > hx, "all three proposed rank coordinates increase")
        target = trajectory(5 * x, clock)
        need(target[-1] == 5 * y, "literal control reset")
        d5x, h5x, _ = hit(5 * x)
        d5y, h5y, _ = hit(5 * y)
        need(d5x == clock + d5y and h5x == sum(v % 2 for v in target[:-1]) + h5y, "target first-hit clock composition")
        rows.append({"x": x, "y": y, "reset_clock": clock,
                     "x_first_hit": [dx, hx], "y_first_hit": [dy, hy],
                     "five_x_first_hit": [d5x, h5x], "five_y_first_hit": [d5y, h5y],
                     "literal_antecedent_paths_sha256": sha256(json.dumps([px, py], separators=(",", ":")).encode()).hexdigest()})
    need(rows[0]["x_first_hit"] == [11, 2] and rows[0]["y_first_hit"] == [41, 20], "small reset reported clocks")
    need(rows[1]["x_first_hit"] == [47, 2] and rows[1]["y_first_hit"] == [254, 132], "r=7 reported clocks")
    return rows


def main():
    cells, affine_edges = reconstruct_cells()
    report = {"status": "independent exact reconstruction passed",
              "scope": "Conditional affine certificate and finite physical controls, not F5 or Collatz.",
              "author_module_imported": False,
              "affine_cells": len(cells), "universal_affine_edges": affine_edges,
              "covered_residues_mod480": 120, "maximum_word_length": 15,
              "affine_trace_sha256": sha256(json.dumps(cells, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
              "carry_checks": reconstruct_carries(), "convergent_controls": controls()}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
