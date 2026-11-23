#!/usr/bin/env python3
"""Exact finite complement-budget certificates; no Collatz convergence oracle.

An affine target is A*r+B.  Its positive complement is d=A-B.  The
certificate stops at ceil(log_3 A) negative even steps or the fixed value1.
Every stage records an entire forced odd block and one actual halving.
The mathematical all-parameter semantics are proved in NegativeCarry.lean.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    """Proof and input checks remain active under Python's -O option."""
    if not condition:
        raise ValueError(message)


def budget_for(multiplier: int) -> int:
    require(type(multiplier) is int and multiplier >= 1,
            "multiplier must be a positive integer")
    p, power = 0, 1
    while power < multiplier:
        p, power = p + 1, power * 3
    return p


def valuation_two(n: int) -> int:
    require(type(n) is int and n > 0,
            "valuation input must be a positive integer")
    return (n & -n).bit_length() - 1


def build(multiplier: int, intercept: int) -> dict:
    require(type(multiplier) is int and type(intercept) is int,
            "affine parameters must be integers")
    require(multiplier >= 1 and multiplier - intercept >= 1,
            "multiplier and complement must be positive")
    initial = multiplier - intercept
    p = budget_for(multiplier)
    d, clock = initial, 0
    blocks = []
    while len(blocks) < p and d != 1:
        odd_steps = valuation_two(d - 1)
        odd_part = (d - 1) >> odd_steps
        even_endpoint = 3**odd_steps * odd_part + 1
        require(even_endpoint % 2 == 0, "odd block must reach an even endpoint")
        after = even_endpoint // 2
        blocks.append({"before": d, "odd_steps": odd_steps,
                       "odd_part": odd_part, "even_endpoint": even_endpoint,
                       "after": after})
        d = after
        clock += odd_steps + 1
    result = {
        "schema": "negative-complement-budget-v1",
        "multiplier": multiplier,
        "intercept": intercept,
        "initial_complement": initial,
        "budget": p,
        "clock": clock,
        "even_steps": len(blocks),
        "final_complement": d,
        "outcome": "paid" if len(blocks) == p else "unit_obstruction",
        "blocks": blocks,
        "dyadic_height": (initial - 1).bit_length(),
    }
    result["guaranteed_budget_condition"] = 2**p <= initial
    result["theorem_clock_bound"] = (2**p - 1) * result["dyadic_height"]
    if result["outcome"] == "paid":
        result["source_endpoint_coefficient"] = 3**clock
        result["target_endpoint_coefficient"] = multiplier * 3**(clock-p)
        result["identity"] = (
            "For every u>=1 with A*(2^clock*u-1)+B>0, "
            "T^clock(A*(2^clock*u-1)+B)="
            "target_endpoint_coefficient*u-final_complement."
        )
    else:
        result["identity"] = (
            "For every k>=clock and positive admissible target, "
            "T^k(A*(2^k*u-1)+B)=A*3^(k-even_steps)*u-1 "
            "> 3^k*u-1."
        )
    verify(result)
    return result


def verify(cert: dict) -> None:
    require(type(cert) is dict, "certificate must be an object")
    integer_fields = {
        "multiplier", "intercept", "initial_complement", "budget", "clock",
        "even_steps", "final_complement", "dyadic_height", "theorem_clock_bound",
    }
    required = integer_fields | {"schema", "blocks", "outcome", "guaranteed_budget_condition"}
    require(required <= cert.keys(), "certificate is missing required fields")
    require(all(type(cert[field]) is int for field in integer_fields),
            "certificate arithmetic fields must be integers")
    require(type(cert["guaranteed_budget_condition"]) is bool,
            "guaranteed budget condition must be Boolean")
    require(cert["schema"] == "negative-complement-budget-v1", "unsupported schema")
    A, B = cert["multiplier"], cert["intercept"]
    require(A >= 1 and A-B >= 1, "multiplier and complement must be positive")
    p = budget_for(A)
    require(cert["budget"] == p, "incorrect multiplier budget")
    d, clock, evens = A-B, 0, 0
    require(cert["initial_complement"] == d, "incorrect initial complement")
    require(type(cert["blocks"]) is list, "blocks must be a list")
    for block in cert["blocks"]:
        fields = {"before", "odd_steps", "odd_part", "even_endpoint", "after"}
        require(type(block) is dict and fields <= block.keys(),
                "block is missing required fields")
        require(all(type(block[field]) is int for field in fields),
                "block arithmetic fields must be integers")
        require(evens < p and d > 1 and block["before"] == d,
                "block is not a legal continuation of the current state")
        s, v = block["odd_steps"], block["odd_part"]
        require(s >= 0 and v > 0 and v % 2 == 1 and 2**s*v+1 == d,
                "incorrect exact odd-block decomposition")
        endpoint = 3**s*v+1
        require(endpoint % 2 == 0 and block["even_endpoint"] == endpoint,
                "incorrect odd-block endpoint")
        require(block["after"] * 2 == endpoint, "incorrect halving endpoint")
        require(endpoint >= d, "odd block violates the nondecrease bound")
        d, clock, evens = block["after"], clock+s+1, evens+1
    require((cert["clock"], cert["even_steps"], cert["final_complement"]) == (clock, evens, d),
            "recorded totals do not match the replayed blocks")
    L = (A-B-1).bit_length()
    require(cert["dyadic_height"] == L, "incorrect dyadic height")
    require(cert["theorem_clock_bound"] == (2**p-1)*L, "incorrect theorem clock bound")
    require(cert["guaranteed_budget_condition"] == (2**p <= A-B),
            "incorrect guaranteed-budget condition")
    if evens == p:
        require(cert["outcome"] == "paid" and d >= 1, "incorrect paid outcome")
        coefficient_fields = {"source_endpoint_coefficient", "target_endpoint_coefficient"}
        require(coefficient_fields <= cert.keys() and
                all(type(cert[field]) is int for field in coefficient_fields),
                "paid outcome requires integer endpoint coefficients")
        require(cert["source_endpoint_coefficient"] == 3**clock,
                "incorrect source endpoint coefficient")
        require(cert["target_endpoint_coefficient"] == A*3**(clock-p),
                "incorrect target endpoint coefficient")
        require(cert["target_endpoint_coefficient"] <= cert["source_endpoint_coefficient"],
                "target multiplier was not paid")
        if 2**p <= A-B:
            require(clock <= (2**p-1)*L, "clock exceeds the proved bound")
    else:
        require(cert["outcome"] == "unit_obstruction" and d == 1 and evens < p,
                "unpaid budget has not reached the unit obstruction")
        require(A > 3**evens, "claimed obstruction lacks a multiplier excess")
        require(A-B < 2**p, "claimed obstruction contradicts the guaranteed-budget condition")


def self_test() -> dict:
    """Controls target semantic corruption and checks that -O cannot bypass it."""
    valid = [build(9, 2), build(27, -1), build(9, 8)]
    for certificate in valid:
        verify(certificate)
    damaged = {}
    damaged["missing_block"] = copy.deepcopy(valid[0])
    damaged["missing_block"]["blocks"].pop()
    damaged["wrong_endpoint"] = copy.deepcopy(valid[0])
    damaged["wrong_endpoint"]["blocks"][0]["even_endpoint"] += 2
    damaged["wrong_clock"] = copy.deepcopy(valid[0])
    damaged["wrong_clock"]["clock"] += 1
    damaged["false_payment"] = copy.deepcopy(valid[2])
    damaged["false_payment"]["outcome"] = "paid"
    for name, certificate in damaged.items():
        try:
            verify(certificate)
        except ValueError:
            continue
        raise ValueError(f"damaged-certificate control was accepted: {name}")
    invalid_inputs = [lambda: budget_for(0), lambda: valuation_two(0), lambda: build(9, 9)]
    for check in invalid_inputs:
        try:
            check()
        except ValueError:
            continue
        raise ValueError("invalid-input control was accepted")
    return {"status": "PASS", "valid_certificates": len(valid),
            "rejected_damaged_certificates": list(damaged),
            "rejected_invalid_inputs": len(invalid_inputs)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--multiplier", type=int, default=27)
    parser.add_argument("--intercept", type=int, default=-1)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--check", type=Path)
    action.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps(self_test()))
    elif args.check:
        value = json.loads(args.check.read_text())
        certificates = value if isinstance(value, list) else [value]
        for certificate in certificates:
            verify(certificate)
        print(json.dumps({"status": "PASS", "certificates": len(certificates)}))
    else:
        print(json.dumps(build(args.multiplier, args.intercept), indent=2))


if __name__ == "__main__":
    main()
