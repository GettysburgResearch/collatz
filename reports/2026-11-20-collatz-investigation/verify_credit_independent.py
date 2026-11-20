"""Independent scalar replay of a ternary inverse-credit certificate.

This reads the symbolic agent's JSON, checks every row and all three lifts,
and does not import the NumPy synthesis code.  The finite arithmetic check
supports the separately stated all-lift theorem; it does not prove Collatz.
"""

import argparse
import collections
import gzip
import hashlib
import json
from pathlib import Path


def verify(document):
    summary = document.get("summary") or {
        "digits": document["digits"], "p": document["p"],
        "q": document["q"], "amax": document["max_action"],
    }
    digits, p, q, amax = (
        summary[key] for key in ("digits", "p", "q", "amax")
    )
    assert all(type(x) is int and x > 0 for x in (digits, p, q, amax))
    modulus = 3**digits
    values = document["values"]
    assert len(values) == 2 * 3 ** (digits - 1)
    assert all(type(v) is int and v >= 0 for v in values)

    def value(residue):
        assert 0 < residue < modulus and residue % 3
        return values[residue - residue // 3 - 1]

    counts = collections.Counter()
    minimum_slack = None
    minimum_terminal_slack = None
    policy = {}
    for residue in range(1, modulus):
        if residue % 3 == 0:
            continue
        budget = p + value(residue)
        terminal_a = 1 if residue % 3 == 2 else 2
        terminal_slack = budget - q * terminal_a
        minimum_terminal_slack = (
            terminal_slack if minimum_terminal_slack is None
            else min(minimum_terminal_slack, terminal_slack)
        )
        for exponent in range(1, amax + 1):
            successor_values = []
            for high_digit in range(3):
                constant = residue + high_digit * modulus
                numerator = (1 << exponent) * constant - 1
                if numerator % 3:
                    break
                child = numerator // 3
                if child <= 0 or child % 3 == 0:
                    break
                successor_values.append(value(child % modulus))
            if len(successor_values) != 3:
                continue
            slack = budget - q * exponent - max(successor_values)
            if slack < 0:
                continue
            policy[residue] = exponent
            counts[exponent] += 1
            minimum_slack = slack if minimum_slack is None else min(
                minimum_slack, slack
            )
            break
        else:
            raise AssertionError(f"No valid all-lift action at residue {residue}")

    return {
        "digits": digits,
        "modulus": modulus,
        "p": p,
        "q": q,
        "amax": amax,
        "rows": len(values),
        "lifts_of_selected_actions": 3 * len(values),
        "maximum_potential": max(values),
        "minimum_credit_slack": minimum_slack,
        "minimum_terminal_slack": minimum_terminal_slack,
        "selected_action_counts": dict(sorted(counts.items())),
        "all_rows_pass": True,
    }


def main():
    if not __debug__:
        raise RuntimeError("This independent checker requires Python assertions; omit -O.")
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    document = json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)
    result = verify(document)
    result["certificate_sha256"] = hashlib.sha256(raw).hexdigest()
    result["certificate"] = args.certificate.name

    # A zero potential fails the credit inequality at some legal states.
    mutated = dict(document, values=[0] * len(document["values"]))
    try:
        verify(mutated)
    except AssertionError as error:
        result["zero_potential_rejected"] = str(error)
    else:
        raise AssertionError("Zero-potential mutation unexpectedly passed")
    output = json.dumps(result, sort_keys=True, indent=2) + "\n"
    print(output, end="")
    if args.report:
        args.report.write_text(output)


if __name__ == "__main__":
    main()
