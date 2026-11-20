"""Independent exact replay of PR146's frozen directed reverse cover.

Only Python's standard library and the adjacent JSON data are used.  No source
checker, trajectory search, or imported author replay is executed.  All guards
use explicit exceptions and therefore remain active under python -O/-OO.
"""

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import json
import re


SOURCE_COMMIT = "fd991063721e9c157d318e40bb20131762f7d750"
SOURCE_PATH = "research/upper-bit-mergers/check_deep_reverse_basin.py"
SOURCE_BLOB = "0a54986a14afe89162413bab5a238aa1e16f53e2"
DATA_SHA256 = "fac1eb6d3f3217189c6bb9fa8b366428a02ce6bbac67379f6071dc558d95743f"
EXPECTED_HEIGHT = Fraction(213597, 23)


class InvalidCertificate(ValueError):
    """A purported whole-progression certificate fails an exact guard."""


def require(condition, message):
    if not condition:
        raise InvalidCertificate(message)


def load_rows():
    raw = Path(__file__).with_name("reverse-cover.json").read_bytes()
    require(sha256(raw).hexdigest() == DATA_SHA256, "frozen data hash mismatch")
    data = json.loads(raw)
    require(data.get("schema") == "collatz.reverse-cover.v1", "data schema")
    provenance = data.get("source", {})
    require(provenance.get("repository") == "GettysburgResearch/collatz", "repository pin")
    require(provenance.get("pr") == 146, "PR pin")
    require(provenance.get("commit") == SOURCE_COMMIT, "commit pin")
    require(provenance.get("path") == SOURCE_PATH, "path pin")
    require(provenance.get("git_blob") == SOURCE_BLOB, "blob pin")
    require(isinstance(data.get("rows"), list), "row list")
    return data["rows"]


def replay(rows):
    require(bool(rows), "empty cover")
    period = 1
    coverage = set()
    total_moves = total_triplings = longest = 0
    maximum_height = Fraction(0)
    height_witnesses = []

    for row_number, row in enumerate(rows, 1):
        require(isinstance(row, dict), f"row {row_number}: object required")
        modulus, residue = row.get("modulus"), row.get("residue")
        require(type(modulus) is int and type(residue) is int, f"row {row_number}: integers")
        require(modulus > 0 and modulus % 6 == 0, f"row {row_number}: modulus")
        require(0 < residue < modulus and gcd(residue, 6) == 1, f"row {row_number}: residue")
        require(isinstance(row.get("word"), str) and row["word"], f"row {row_number}: word")
        period = lcm(period, modulus)

    for row_number, row in enumerate(rows, 1):
        modulus, residue = row["modulus"], row["residue"]
        a, b = modulus, residue  # current value a*t+b, t>=0
        first_t = 1 if residue == 1 else 0  # the input 1 is the induction base
        moves = 0
        for token_number, token in enumerate(row["word"].split(), 1):
            context = f"row {row_number}, token {token_number} ({token})"
            require(re.fullmatch(r"M|[SI][1-9][0-9]*", token) is not None, context + ": syntax")
            if token == "M":
                require(a % 18 == 0 and b % 18 == 9, context + ": odd multiple of nine")
                # The extra arrow v->3v invokes R at antecedent 3v when read backward.
                candidates = (
                    ("asymptotic", Fraction(3 * a, modulus)),
                    ("first_legal_input", Fraction(3 * (a * first_t + b), modulus * first_t + residue)),
                )
                for location, height in candidates:
                    evidence = {
                        "row": row_number,
                        "token": token_number,
                        "modulus": modulus,
                        "residue": residue,
                        "query_slope": a,
                        "query_intercept": b,
                        "first_t": first_t,
                        "location": location,
                    }
                    if height > maximum_height:
                        maximum_height = height
                        height_witnesses = [evidence]
                    elif height == maximum_height:
                        height_witnesses.append(evidence)
                a, b = 3 * a, 3 * b
                moves += 1
                total_triplings += 1
            else:
                exponent = int(token[1:])
                power = 1 << exponent
                if token[0] == "S":
                    # One odd shortcut step followed by exponent-1 halvings.
                    # The last endpoint is allowed to be even.
                    require(a % 2 == 0 and b % 2 == 1, context + ": odd source")
                    require(3 * a % power == 0 and (3 * b + 1) % power == 0, context + ": exact division")
                    a, b = 3 * a // power, (3 * b + 1) // power
                else:
                    require(power * a % 3 == 0 and (power * b - 1) % 3 == 0, context + ": integral inverse")
                    a, b = power * a // 3, (power * b - 1) // 3
                    require(a % 2 == 0 and b % 2 == 1, context + ": odd inverse source")
                moves += exponent
            require(a > 0 and b > 0, context + ": positivity for every lift")

        require(a % 3 == 0 and b % 3 != 0, f"row {row_number}: terminal ternary unit")
        require(25 * a <= 24 * modulus, f"row {row_number}: contraction slope")
        require(
            25 * (a * first_t + b) <= 24 * (modulus * first_t + residue),
            f"row {row_number}: contraction at first legal input",
        )
        coverage.update(range(residue, period, modulus))
        total_moves += moves
        longest = max(longest, moves)

    expected_coverage = {value for value in range(period) if gcd(value, 6) == 1}
    require(coverage == expected_coverage, "incomplete or excessive residue cover")
    totals = (len(rows), period, len(coverage), total_moves, total_triplings, longest)
    require(totals == (71, 62208, 20736, 3974, 284, 198), "frozen certificate totals")
    require(maximum_height == EXPECTED_HEIGHT, "direct-R height bound")
    require(
        height_witnesses == [{
            "row": 22, "token": 22, "modulus": 432, "residue": 23,
            "query_slope": 1327104, "query_intercept": 71199,
            "first_t": 0, "location": "first_legal_input",
        }],
        "height equality witness",
    )
    return {
        "rows": len(rows), "common_modulus": period, "covered_unit_residues": len(coverage),
        "expanded_graph_moves": total_moves, "eligible_triplings": total_triplings,
        "maximum_word_moves": longest, "contraction": "24/25",
        "maximum_direct_R_antecedent_ratio": str(maximum_height),
        "general_positive_height_factor": str(Fraction(5, 3) * maximum_height),
        "height_equality_witness": height_witnesses[0],
    }


def rejection_checks(rows):
    cases = []
    damaged = deepcopy(rows)
    damaged.pop()
    cases.append(("missing cover row", damaged))
    damaged = deepcopy(rows)
    damaged[0]["residue"] = 3
    cases.append(("nonunit source class", damaged))
    damaged = deepcopy(rows)
    damaged[0]["modulus"] = 13
    cases.append(("invalid class modulus", damaged))
    damaged = deepcopy(rows)
    damaged[0]["word"] = "S0"
    cases.append(("zero division exponent", damaged))
    damaged = deepcopy(rows)
    damaged[0]["word"] = "S4"
    cases.append(("nonintegral forward step", damaged))
    damaged = deepcopy(rows)
    damaged[2]["word"] = "I2"
    cases.append(("nonintegral inverse step", damaged))
    damaged = deepcopy(rows)
    damaged[11]["word"] = "M S3"
    cases.append(("illegal tripling source", damaged))
    damaged = deepcopy(rows)
    damaged[0]["word"] = "I2"
    cases.append(("invalid terminal descent", damaged))
    rejected = []
    for name, candidate in cases:
        try:
            replay(candidate)
        except InvalidCertificate:
            rejected.append(name)
        else:
            raise InvalidCertificate("damaged certificate accepted: " + name)
    return rejected


def paired_five_seed():
    def run(value, clock):
        odds = 0
        for _ in range(clock):
            if value % 2:
                value = (3 * value + 1) // 2
                odds += 1
            else:
                value //= 2
        return value, odds

    source = 6375551795
    left, right = run(source, 71), run(5 * source, 71)
    require(left == (1215835, 37) and right == (6079175, 37), "paired five seed")
    return {"source": source, "clock": 71, "odd_inputs_each": 37, "endpoints": [left[0], right[0]]}


def main():
    rows = load_rows()
    report = {
        "status": "PASS",
        "source_commit": SOURCE_COMMIT,
        "frozen_data_sha256": DATA_SHA256,
        "reverse_cover": replay(rows),
        "paired_five_seed": paired_five_seed(),
        "rejected_damage_controls": rejection_checks(rows),
        "formal_verification": False,
        "full_claim": "OPEN",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
