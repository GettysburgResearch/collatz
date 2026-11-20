#!/usr/bin/env python3
"""Exact rational controls for the asymptotic-operator note.

This checks finite algebraic identities and arithmetic witnesses. The infinite
operator claims are proved in SHIFT_CONTROLS.md and ASYMPTOTIC_OPERATOR.md.
There are no floating-point computations or optional dependencies.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


class CheckFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def require_equal(actual: object, expected: object, message: str) -> None:
    if actual != expected:
        raise CheckFailure(f"{message}: {actual!r} != {expected!r}")


def weight(family: str, index: int) -> Fraction:
    require(index >= 0, "negative weight index")
    if family == "vanishing":
        return Fraction(index + 1, index + 2)
    if family == "retained":
        return Fraction((index + 1) * (index + 3), (index + 2) ** 2)
    raise CheckFailure(f"unknown family {family}")


def direct_product(family: str, start: int, length: int) -> Fraction:
    value = Fraction(1)
    for index in range(start, start + length):
        value *= weight(family, index)
    return value


def closed_product(family: str, start: int, length: int) -> Fraction:
    if family == "vanishing":
        return Fraction(start + 1, start + length + 1)
    if family == "retained":
        return Fraction(
            (start + 1) * (start + length + 2),
            (start + 2) * (start + length + 1),
        )
    raise CheckFailure(f"unknown family {family}")


def product_of(values: list[Fraction] | tuple[Fraction, ...]) -> Fraction:
    value = Fraction(1)
    for item in values:
        value *= item
    return value


def extension_weight(
    prefix: tuple[Fraction, ...], family: str, index: int
) -> Fraction:
    if index < len(prefix):
        return prefix[index]
    return weight(family, index - len(prefix))


def extension_product(
    prefix: tuple[Fraction, ...], family: str, start: int, length: int
) -> Fraction:
    value = Fraction(1)
    for index in range(start, start + length):
        value *= extension_weight(prefix, family, index)
    return value


def extension_closed_product(
    prefix: tuple[Fraction, ...], family: str, start: int, length: int
) -> Fraction:
    end = start + length
    cut = len(prefix)
    prefix_factor = product_of(prefix[start:min(end, cut)])
    tail_start = max(start, cut) - cut
    tail_length = max(0, end - max(start, cut))
    return prefix_factor * closed_product(family, tail_start, tail_length)


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def next_odd_unit(value: int) -> int:
    value = max(1, value)
    while value % 2 == 0 or value % 3 == 0:
        value += 1
    return value


def odd_map(value: int) -> int:
    require(value > 0 and value % 2 == 1, "odd map needs positive odd input")
    value = 3 * value + 1
    while value % 2 == 0:
        value //= 2
    return value


def legal_children(target: int, cap: int = 6) -> list[tuple[int, int]]:
    children = []
    for exponent in range(1, cap + 1):
        numerator = (1 << exponent) * target - 1
        if numerator % 3:
            continue
        child = numerator // 3
        if child > 0 and child % 3:
            require(child % 2 == 1, "inverse child was not odd")
            require_equal(odd_map(child), target, "inverse arithmetic")
            children.append((exponent, child))
    return children


def arithmetic_witness(
    length: int, cutoff: int, epsilon: Fraction
) -> dict[str, object]:
    wanted_floor = max(Fraction(cutoff + 1), Fraction(length, 3) / epsilon + 1)
    wanted_target = Fraction(3, 2) ** length * (wanted_floor + 1) - 1
    target = next_odd_unit(ceil_fraction(wanted_target))
    lower_state = Fraction(2, 3) ** length * (target + 1) - 1
    lower_product = (3 * lower_state / (3 * lower_state + 1)) ** length
    bernoulli = 1 - Fraction(length) / (3 * lower_state + 1)
    require(lower_state > cutoff, "support witness missed the cutoff")
    require(lower_product >= bernoulli > 1 - epsilon, "near-isometry bound")
    paths = [(target, Fraction(1))]
    edges = 0
    for _ in range(length):
        new_paths = []
        for current, value in paths:
            children = legal_children(current)
            require_equal(len(children), 2, "cap six legal unit branching")
            for _, child in children:
                edges += 1
                require(child >= lower_state, "inverse path fell below floor")
                new_value = value * Fraction(3 * child, 3 * child + 1)
                new_paths.append((child, new_value))
        paths = new_paths
    for child, value in paths:
        require(child > cutoff, "terminal witness below cutoff")
        require(value >= lower_product, "path product below uniform bound")
    return {
        "n": length,
        "cutoff": cutoff,
        "target": target,
        "epsilon": str(epsilon),
        "state_floor": str(lower_state),
        "bernoulli_bound": str(bernoulli),
        "terminal_paths": len(paths),
        "checked_edges": edges,
    }


def rejects(action, name: str) -> str:
    try:
        action()
    except CheckFailure:
        return name
    raise CheckFailure(f"negative control was not rejected: {name}")


def verify() -> dict[str, object]:
    product_checks = 0
    for family in ("vanishing", "retained"):
        for start in range(32):
            require(0 < weight(family, start) < 1, "weight not strictly contractive")
            for length in range(65):
                require_equal(
                    direct_product(family, start, length),
                    closed_product(family, start, length),
                    "telescoping product",
                )
                product_checks += 1

    prefix = (
        Fraction(7, 8),
        Fraction(8, 9),
        Fraction(5, 7),
        Fraction(13, 17),
        Fraction(3, 4),
    )
    shared_checks = 0
    for start in range(len(prefix) + 1):
        for length in range(len(prefix) - start + 1):
            require_equal(
                extension_product(prefix, "vanishing", start, length),
                extension_product(prefix, "retained", start, length),
                "shared finite path",
            )
            shared_checks += 1

    extension_checks = 0
    for family in ("vanishing", "retained"):
        for start in range(len(prefix) + 13):
            for length in range(33):
                require_equal(
                    extension_product(prefix, family, start, length),
                    extension_closed_product(prefix, family, start, length),
                    "prefix-extension product",
                )
                extension_checks += 1

    shift_witnesses = []
    for cutoff in (0, 15, 255, 65535):
        for length in (1, 4, 16, 64):
            start = max(cutoff + 1, 200 * length)
            for family in ("vanishing", "retained"):
                norm_squared = closed_product(family, start, length) ** 2
                require(norm_squared > Fraction(99, 100), "shift tail witness")
                require(start > cutoff and start + length > cutoff, "shift support")
                shift_witnesses.append({
                    "family": family,
                    "n": length,
                    "cutoff": cutoff,
                    "start": start,
                    "norm_squared": str(norm_squared),
                })

    arithmetic_witnesses = [
        arithmetic_witness(length, cutoff, Fraction(1, 100))
        for cutoff in (0, 100, 10000)
        for length in (1, 2, 4, 8)
    ]

    wrong_retained_formula = Fraction((4 + 1) * (4 + 7 + 1), (4 + 2) * (4 + 7 + 2))
    changed_prefix = prefix[:-1] + (prefix[-1] / 2,)
    mutation_controls = [
        rejects(
            lambda: require_equal(
                direct_product("retained", 4, 7),
                wrong_retained_formula,
                "mutated retained endpoint",
            ),
            "wrong telescoping endpoint",
        ),
        rejects(
            lambda: require_equal(
                extension_product(prefix, "vanishing", len(prefix) - 1, 1),
                extension_product(changed_prefix, "retained", len(prefix) - 1, 1),
                "mutated shared prefix",
            ),
            "changed shared-prefix weight",
        ),
        rejects(
            lambda: require(
                min(child for _, child in legal_children(17))
                >= Fraction(3, 2) * (17 + 1) - 1,
                "mutated inverse floor",
            ),
            "reversed inverse-floor factor",
        ),
    ]

    return {
        "status": "PASS",
        "arithmetic": "fractions.Fraction and integer operations only",
        "scope": (
            "Finite identity and witness replay; infinite limits are proved "
            "analytically in the accompanying notes. No Collatz proof."
        ),
        "telescoping_identity_checks": product_checks,
        "shared_prefix_path_checks": shared_checks,
        "prefix_extension_identity_checks": extension_checks,
        "shift_tail_witnesses_checked": len(shift_witnesses),
        "shift_tail_witness_samples": shift_witnesses[:4] + shift_witnesses[-4:],
        "arithmetic_inverse_witnesses": arithmetic_witnesses,
        "total_checked_inverse_edges": sum(
            item["checked_edges"] for item in arithmetic_witnesses
        ),
        "negative_controls_rejected": mutation_controls,
        "shared_prefix_retained_limit_at_zero_squared": str(
            (product_of(prefix) / 2) ** 2
        ),
        "shared_prefix_vanishing_limit_at_zero_squared": "0",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the JSON receipt here")
    args = parser.parse_args()
    report = verify()
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output is not None:
        args.output.write_text(rendered + chr(10))
    print(rendered)


if __name__ == "__main__":
    main()
