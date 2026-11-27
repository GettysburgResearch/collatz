"""Read the literal mixed-radix certificate and reconstruct every ordinary edge."""
import hashlib
import json
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PIN = "1f0f496fbea37792439feada6106eaaff596bcd1"
DEPENDENCIES = {
    "ReverseBasin.lean": ("directed-return/vendor", "633af7b92dc57e2296036d4d3e2a71d74b16207ed7e23a325c11c301be5cdf65"),
    "TwoOddCertificate.lean": ("closing-proposal", "2b5770fa878514a304fe6f6d9fa87152515bdf57612319e0f8d7a805fef55cda"),
    "DirectedEleven.lean": ("directed-return", "7527fb54500831c6cebac3376a3195984d4f414c3df97241a7aa48f91225b677"),
    "UnitResidueExchange.lean": ("unit-exit", "fb2c73495ee942286568deac0fc44fc94151bde3a3451dc2f60ff927d04aebb8"),
    "NonunitExit.lean": ("unit-exit", "0c4e82f09326eacbf9c4517215129d4ac087934474b73cdc42c220b3a75039d0"),
    "QuantitativeReturn.lean": ("closing-proposal", "29385e0b50688db4a09ada4175fdd9a8b335e1a4c1191c112c31fa68e23f7e07"),
}


def require(test, label):
    if not test:
        raise ArithmeticError(label)


def rows():
    text = (ROOT/"ReturnTwentyFour.lean").read_text(encoding="utf-8")
    body = text.split("def certificate : Tree :=", 1)[1].split("set_option", 1)[0]
    token = re.compile(r"\s*(\(\.two|\(\.three|\(\.leaf\s*\[(?:[FB] [0-9]+|C)(?:,(?:[FB] [0-9]+|C))*\]\)|\))")
    collected = []
    while body.strip():
        match = token.match(body)
        require(match is not None, "unexpected tree token")
        collected.append(match[1])
        body = body[match.end():]
    stream = iter(collected)

    def visit(a, b, depth):
        item = next(stream)
        if item.startswith("(.leaf"):
            word = []
            for cell in re.search(r"\[(.*)\]", item)[1].split(","):
                if cell == "C":
                    word.append(0)
                else:
                    op, e = cell.split(" ")
                    word.append(int(e) if op == "F" else -int(e))
            yield a, b, depth, word
            return
        require(item in ("(.two", "(.three"), "finite split or leaf")
        arity = 2 if item == "(.two" else 3
        for i in range(arity):
            yield from visit(arity*a, b+i*a, depth+1)
        require(next(stream) == ")", "exact split arity")

    leaves = list(visit(2, 3, 0))
    require(next(stream, None) is None, "complete mixed-radix certificate")
    return leaves


def shortcut(w):
    return (3*w+1)//2 if w & 1 else w//2


def ordinary(source, e, target):
    require(source % 2 == 1 and source > 0 and target > 0, "positive odd departure")
    x = source
    for i in range(e):
        require(i == 0 or x % 2 == 0, "whole odd block")
        x = shortcut(x)
    require(x == target, "true ordinary terminal")


def verify_word(a, b, word):
    A, B = a, b
    hits = []
    for op in word:
        if op > 0:
            p = 2**op
            require(A % 2 == 0 and B % 2 == 1 and 3*A % p == (3*B+1) % p == 0,
                    "forward parity and two coefficient quotients")
            U, V = 3*A//p, (3*B+1)//p
            for t in (0, 1):
                ordinary(A*t+B, op, U*t+V)
        elif op < 0:
            p = 2**(-op)
            require((p*A) % 3 == (p*B-1) % 3 == 0, "inverse coefficient quotients")
            U, V = p*A//3, (p*B-1)//3
            require(U % 2 == 0 and V % 2 == 1, "inverse positive odd source")
            for t in (0, 1):
                ordinary(U*t+V, -op, A*t+B)
        else:
            require(A % 16 == 0 and B % 16 == 1, "precise directed residue")
            require(A <= 24*a and B <= 24*b, "charge relative to its original source")
            hits.append((max(Fraction(A, a), Fraction(B, b)), a, b, A, B))
            U, V = 3*A, 3*B
        require(U > 0 and V > 0, "positive affine state")
        A, B = U, V
    require(0 < B < b and A <= a, "strict ordinary descent")
    return hits, (A, B)


def main():
    table = rows()
    distribution = Counter()
    depth = Counter()
    charges = []
    finals = []
    for a, b, level, word in table:
        hits, new = verify_word(a, b, word)
        charges.extend(hits)
        finals.append((a, b, word, new))
        distribution[len(hits)] += 1
        depth[level] += 1
    require(len(table) == 140 and sum((Fraction(2, a) for a, _, _, _ in table), Fraction()) == 1,
            "complete disjoint cover of all odd n at least three")
    for n in range(3, 20002, 2):
        active = [(a, b, new) for a, b, _, new in finals if n >= b and (n-b) % a == 0]
        require(len(active) == 1, "unique literal row")
        a, b, (A, B) = active[0]
        require(0 < A*((n-b)//a)+B < n, "original positive integer decreases")
    high, a, b, A, B = max(charges)
    frozen = {}
    for name, (directory, expected) in DEPENDENCIES.items():
        sha = hashlib.sha256((ROOT/"pr197-floor"/name).read_bytes()).hexdigest()
        require(sha == expected, "unchanged upstream dependency "+name)
        frozen[name] = {"path": f"research/ayh-resource-reset-20261124/{directory}/{name}", "sha256": sha}
    print(json.dumps({"root_progression": [2, 3], "leaves": len(table),
          "leaf_mass_within_odd_inputs": [1, 1], "leaves_by_number_of_directed_charges":
              dict(sorted(distribution.items())), "leaves_by_tree_depth": dict(sorted(depth.items())),
          "total_charge_positions": len(charges), "max_word_blocks": max(len(w) for _, _, _, w in table),
          "max_individual_ordinary_clock": max(abs(v) for _, _, _, w in table for v in w),
          "largest_charge_to_original": [high.numerator, high.denominator],
          "maximizing_original_affine_row": [a, b], "maximizing_charged_affine_row": [A, B],
          "literal_input_check": {"first": 3, "last": 20001, "stride": 2, "inputs": 10000},
          "binary_defect_factor": 24, "pr197_from16_factor": 2**23,
          "new_global_canonical_factor": 24*2**23, "previous_global_factor": 2**40,
          "upstream_pr197_commit": PIN, "upstream_sources": frozen}, indent=2))


if __name__ == "__main__":
    main()
