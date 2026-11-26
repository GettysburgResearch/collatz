"""Replay the directed source substitutions and their whole-source query costs."""

from fractions import Fraction
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
RULES = {
    "E": (2, 0, 1, 0),
    "D": (1, 0, 2, 0),
    "O": (2, 1, 3, 2),
    "I": (3, 2, 2, 1),
    "M": (32, 11, 96, 33),
}


def require(statement, message):
    if not statement:
        raise ValueError(message)


def replay(row, moves):
    """Apply ordinary comparisons on the entire progression, retaining all jumps."""
    queries = []
    for letter in moves:
        modulus, residue, slope, base = RULES[letter]
        a, b = row
        require(a % modulus == 0 and b % modulus == residue,
                f"illegal {letter} at row {row}")
        if letter == "M":
            queries.append(row)
        row = slope * (a // modulus), slope * (b // modulus) + base
        require(min(row) > 0, "nonpositive physical affine row")
    return row, queries


def affine(word):
    """Refine the single original parameter and every prior row by the same trit."""
    rows = [(16, 1)]
    for digit in word:
        a, b = rows[-1]
        power = 2 ** int(digit)
        offset = -1 if digit == "2" else 3
        trits = [k for k in range(3) if (power * (b + k*a) + offset) % 3 == 0]
        require(len(trits) == 1, "nonunique ternary refinement")
        trit = trits[0]
        rows = [(3*c, d + c*trit) for c, d in rows]
        a, b = rows[-1]
        rows.append((power*a // 3, (power*b + offset) // 3))
    return rows


def read_motifs():
    data = json.loads((HERE / "Directed11Motifs.json").read_text())
    require(data["height"] == 10 and data["remaining"] == [], "unexpected certificate header")
    proofs = data["proof"]
    source = (HERE / "DirectedEleven.lean").read_text()
    pattern = r'^def motif(\d+) : Motif := ⟨"([245]+)",(\d+),\((\d+),(\d+)\),"([DEOIM]+)"⟩$'
    kernel_rows = re.findall(pattern, source, flags=re.MULTILINE)
    records = []
    for expected, (index, word, clock, modulus, residue, moves) in enumerate(kernel_rows):
        require(int(index) == expected, "Lean motif order changed")
        records.append([word, int(modulus), int(residue), int(clock), moves])
    require(records == proofs, "Lean/JSON motif data differ")
    by_word = {w: (m, b, i, p) for w, m, b, i, p in proofs}
    require(len(by_word) == len(proofs) == 116, "duplicate or missing motif")
    for word, (modulus, residue, clock, moves) in by_word.items():
        a, b = affine(word)[clock]
        require(a % modulus == 0 and b % modulus == residue, "source midpoint mismatch")
        endpoint, _ = replay((modulus, residue), moves)
        require(endpoint == (3*modulus, 3*residue), "incorrect local tripling endpoint")
    return by_word


def main():
    motifs = read_motifs()
    active = [""]
    counts = []
    terminals = blocked = ordinary = 0
    positions = 0
    maximum = Fraction(0)
    maximizer = None

    def record(query, source, tag):
        nonlocal maximum, maximizer, positions
        a, b = query
        u, v = source
        require(min(a, b, u, v) > 0 and a % 32 == 0 and b % 32 == 11,
                "invalid original-source query")
        ratio = max(Fraction(a, u), Fraction(b, v))
        if ratio > maximum:
            maximum, maximizer = ratio, tag
        positions += 1

    for _ in range(10):
        counts.append(len(active))
        successors = []
        for prefix in active:
            rows = affine(prefix)
            a, b = rows[-1]
            trit = next(k for k in range(3) if (a*k+b) % 3 == 2)
            direct = 2*a, (2*(a*trit+b)-1) // 3
            u, v = rows[0]
            record(direct, (3*u, v+trit*u), ("terminal", prefix))
            terminals += 1
            for digit in "245":
                word = prefix + digit
                suffixes = [w for w in motifs if word.endswith(w)]
                if not suffixes:
                    successors.append(word)
                    continue
                suffix = min(suffixes, key=lambda w: (len(w), w))
                modulus, residue, clock, moves = motifs[suffix]
                rows = affine(word)
                midpoint = rows[len(word) - len(suffix) + clock]
                a, b = midpoint
                require(a % modulus == 0 and b % modulus == residue,
                        "marked suffix does not embed on the full original row")
                endpoint, queries = replay(midpoint, moves)
                require(endpoint == (3*a, 3*b), "incorrect lifted tripling endpoint")
                for index, query in enumerate(queries):
                    record(query, rows[0], ("motif", word, suffix, index))
                ordinary += not queries
                blocked += 1
        active = successors
    require(not active, "uncovered length-ten source word")
    require(positions == 1007 and maximum == Fraction(574854143371, 219537),
            "height or query-position certificate changed")
    require((3125**10) < 2**49 * 108**10 and 3**15 < 2**24, "first return exponents")
    require(3**94 < 2**149 and 149**(20*149) < 2**(19*149) * 94**(20*94) * 55**(20*55),
            "second return exponents")
    return {
        "motifs": len(motifs),
        "distinct_routes": len({m[3] for m in motifs.values()}),
        "route_letters": sum(len(m[3]) for m in motifs.values()),
        "longest_route": max(len(m[3]) for m in motifs.values()),
        "motif_forward_positions": sum(m[3].count("M") for m in motifs.values()),
        "allowed_by_depth": counts + [0],
        "terminal_positions": terminals,
        "first_blocked_prefixes": blocked,
        "first_blocked_intrinsic": ordinary,
        "total_affine_query_positions": positions,
        "largest_query_to_source": str(maximum),
        "maximizing_case": maximizer,
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
