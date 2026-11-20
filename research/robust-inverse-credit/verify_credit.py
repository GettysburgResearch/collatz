#!/usr/bin/env python3
"""Independent integer verifier for the 13/6 inverse-cone certificate.

The verifier uses only Python's standard library.  It neither imports the
synthesis program nor assumes that its dynamic-programming iteration converged.
"""

from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path


DIGITS = 12
MODULUS = 3**DIGITS
P, Q = 13, 6
MAX_ACTION = 10
VALUES_SHA256 = "2f12342f3a4a25ff8ed31c03ddba77b66a17d8bfea62dfaac0c0ea1cbb3273dc"


def index(residue: int) -> int:
    """Index in 1,2,4,5,7,8,...,MODULUS-2,MODULUS-1."""
    if not 0 < residue < MODULUS or residue % 3 == 0:
        raise ValueError(f"not a unit residue: {residue}")
    return residue - residue // 3 - 1


def load_values(path: Path) -> list[int]:
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        data = json.load(stream)
    expected = {
        "format": 1,
        "digits": DIGITS,
        "modulus": MODULUS,
        "p": P,
        "q": Q,
        "max_action": MAX_ACTION,
        "max_credit": 66,
    }
    for key, value in expected.items():
        if type(data.get(key)) is not int or data[key] != value:
            raise ValueError(f"bad certificate field {key}")
    values = data["values"]
    if not isinstance(values, list) or len(values) != 2 * 3 ** (DIGITS - 1):
        raise ValueError("wrong credit-table length")
    if any(type(value) is not int or not 0 <= value <= 66 for value in values):
        raise ValueError("credits must be integers in [0,66]")
    if hashlib.sha256(bytes(values)).hexdigest() != VALUES_SHA256:
        raise ValueError("unexpected credit-table checksum")
    return values


def action_works(residue: int, credit: int, action: int, values: list[int]) -> bool:
    """Check all three ordinary lifts directly, using scalar integer arithmetic."""
    for high_digit in (0, 1, 2):
        constant = residue + MODULUS * high_digit
        numerator = (1 << action) * constant - 1
        if numerator % 3:
            return False
        child = numerator // 3
        if child <= 0 or child % 3 == 0:
            return False
        if Q * action + values[index(child % MODULUS)] > P + credit:
            return False
    return True


def verify(values: list[int]) -> tuple[list[int], dict]:
    policy: list[int] = []
    counts: Counter[int] = Counter()
    terminal_min = None
    for residue in range(1, MODULUS):
        if residue % 3 == 0:
            continue
        credit = values[index(residue)]
        chosen = next(
            (a for a in range(1, MAX_ACTION + 1)
             if action_works(residue, credit, a, values)),
            None,
        )
        if chosen is None:
            raise ValueError(f"no uniformly valid action at residue {residue}")
        policy.append(chosen)
        counts[chosen] += 1
        last_action = 1 if residue % 3 == 2 else 2
        terminal_credit = P + credit - Q * last_action
        terminal_min = terminal_credit if terminal_min is None else min(
            terminal_min, terminal_credit
        )
    if terminal_min != 1:
        raise ValueError(f"unexpected terminal minimum: {terminal_min}")
    return policy, {
        "status": "PASS",
        "modulus": MODULUS,
        "rows": len(policy),
        "selected_action_lifts_checked": 3 * len(policy),
        "min_credit": min(values),
        "max_credit": max(values),
        "terminal_credit_minimum": terminal_min,
        "selected_actions": dict(sorted(counts.items())),
        "values_sha256": hashlib.sha256(bytes(values)).hexdigest(),
    }


def compile_cone(t: int, constant: int, policy: list[int]) -> tuple[int, int, list[int]]:
    if t < 1 or not 0 < constant < 3**t or constant % 3 == 0:
        raise ValueError("need t >= 1 and a positive unit tail below 3^t")
    reverse_actions: list[int] = []
    child = constant
    for _ in range(t - 1):
        a = policy[index(child % MODULUS)]
        child = ((1 << a) * child - 1) // 3
        reverse_actions.append(a)
    a = 1 if child % 3 == 2 else 2
    child = ((1 << a) * child - 1) // 3
    reverse_actions.append(a)
    return sum(reverse_actions), child, reverse_actions


def check_cone(t: int, constant: int, values: list[int], policy: list[int]) -> None:
    """Replay the forward affine map; this checks every prefix x simultaneously."""
    k, tail, reverse_actions = compile_cone(t, constant, policy)
    if not 0 < tail < 1 << k:
        raise ValueError("compiled tail is not a binary suffix")
    if Q * k > P * t + values[index(constant % MODULUS)] - 1:
        raise ValueError("compiled cost violates its state-dependent bound")
    coefficient, intercept = 1 << k, tail
    odd_events = 0
    for a in reversed(reverse_actions):
        if coefficient % 2 or intercept % 2 != 1:
            raise ValueError("odd action is not uniform in the prefix")
        coefficient, intercept = 3 * coefficient // 2, (3 * intercept + 1) // 2
        odd_events += 1
        for _ in range(a - 1):
            if coefficient % 2 or intercept % 2:
                raise ValueError("even action is not uniform in the prefix")
            coefficient //= 2
            intercept //= 2
    if (coefficient, intercept, odd_events) != (3**t, constant, t):
        raise ValueError("forward affine replay does not reach the specified cone")


def regressions(values: list[int], policy: list[int]) -> dict:
    # A deliberately invalid potential must fail the actual inequality check,
    # independently of the checksum and JSON validation.
    zero_values = [0] * len(values)
    zero_failure = next(
        residue for residue in range(1, MODULUS) if residue % 3
        and not any(action_works(residue, 0, a, zero_values)
                    for a in range(1, MAX_ACTION + 1))
    )
    checked = 0
    for t in range(1, 9):
        for constant in range(1, 3**t):
            if constant % 3:
                check_cone(t, constant, values, policy)
                checked += 1
    for t in (40, 100, 1000):
        for constant in (1, 2, (3**t - 1) // 2, 3**t - 2, 3**t - 1):
            check_cone(t, constant, values, policy)
            checked += 1
    return {
        "all_zero_mutation_rejected_at": zero_failure,
        "forward_affine_cones_checked": checked,
        "complete_tail_regression_through_t": 8,
        "large_t_regressions": [40, 100, 1000],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "certificate", nargs="?", type=Path,
        default=Path(__file__).with_name("credit_13_6.json.gz"),
    )
    parser.add_argument("--skip-regressions", action="store_true")
    args = parser.parse_args()
    values = load_values(args.certificate)
    policy, result = verify(values)
    if not args.skip_regressions:
        result.update(regressions(values, policy))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
