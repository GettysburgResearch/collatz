#!/usr/bin/env python3
"""Independent verifier for X-8256.

This file deliberately imports neither ``run.py`` nor any project module.  It
rederives the constants, uses the L-8253 reset-coordinate expression for each
branch residue, implements its own inverse modulo powers of two, rebuilds the
complete transported trie, and checks both frozen artifacts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, deque
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

sys.set_int_max_str_digits(0)

IDENT = "X-8256"
TRIE_SCHEMA = "x-8256-transported-exit-trie-v1"
HEIGHT = 512
LOW_LABEL = 44
PR53 = "8b63eb7dda864430ad64c46ae6f8f58d399ef7b8"
PR51 = "bf00552e5054fd8e5d1692648911b377c5624e56"


def egcd(x: int, y: int) -> tuple[int, int, int]:
    if y == 0:
        return x, 1, 0
    g, u, v = egcd(y, x % y)
    return g, v, u - (x // y) * v


def ordinary_inverse(x: int, modulus: int) -> int:
    g, u, _ = egcd(x % modulus, modulus)
    if g != 1:
        raise AssertionError("nonunit")
    return u % modulus


DELTA = 16**9 - 9**9
ROOT = (-ordinary_inverse(9**9, DELTA)) % DELTA
QA = (9**9 * ROOT + 1) // DELTA
QB = (16**9 * ROOT + 1) // DELTA
POW9 = 9**9
POW16 = 16**9


def inverse_two_power(odd: int, bits: int) -> int:
    """Newton-Hensel inverse of an odd integer modulo 2**bits."""
    if odd % 2 == 0 or bits < 1:
        raise AssertionError("invalid dyadic inverse")
    value = 1
    width = 1
    while width < bits:
        width = min(2 * width, bits)
        value = value * (2 - odd * value) & ((1 << width) - 1)
    if odd * value & ((1 << bits) - 1) != 1:
        raise AssertionError("dyadic inverse failed")
    return value


def valuation_two(value: int) -> int:
    if value == 0:
        raise AssertionError("undefined valuation")
    value = abs(value)
    count = 0
    while value % 2 == 0:
        value //= 2
        count += 1
    return count


def binary_floor(value: int) -> int:
    """Return floor(log2(value)) by shifts, with no logarithm call."""
    if value <= 0:
        raise AssertionError("nonpositive binary height")
    answer = -1
    while value:
        answer += 1
        value >>= 1
    return answer


@dataclass(frozen=True)
class Row:
    s: int
    h: int
    R: int
    M: int
    T: int
    xi: int


@lru_cache(maxsize=None)
def reset_row(s: int) -> Row:
    """Build xi_s from the reset-coordinate residue in L-8253 (20)."""
    h = 3 * s + 36
    R = 1 << h
    mask = R - 1
    inverse_base = inverse_two_power(POW9, h)
    inverse_unit = inverse_two_power(9 ** (s + 9), h)
    xi = (
        -QA * inverse_base
        + (1 << (3 * s)) * QB * inverse_unit
    ) & mask
    M = 9 ** (s + 9)
    T = 9**s * QA - 8**s * QB
    if (M * xi + T) & mask:
        raise AssertionError("reset residue misses centered branch")
    # This cross-check compares two independently stated source formulas.
    direct = (-T * inverse_two_power(M, h)) & mask
    if direct != xi:
        raise AssertionError("L-8252 and L-8253 residues disagree")
    return Row(s, h, R, M, T, xi)


@dataclass
class VNode:
    i: int
    parent: int | None
    label: int | None
    depth: int
    theta: int
    K: int
    C: int
    P: int
    qmax: int
    rho: int | None
    upper: int = -1
    tested: int = 0
    children: list[int] = field(default_factory=list)
    status: str = "unvisited"
    exit_count: int = 0


def exact_upper(C: int, P: int, qmax: int) -> int:
    left = POW9 * C + QA
    right = POW9 * (C + P * qmax) + QA
    magnitude = max(abs(left), abs(right))
    return -1 if magnitude == 0 else binary_floor(magnitude) // 3


def replay_source(x: int, xp: int, s: int) -> None:
    """Check reset, centered, raw-boundary, and physical A/B formulas."""
    y = POW9 * x + QA
    if valuation_two(y) != 3 * s:
        raise AssertionError("wrong intrinsic label")
    u = y >> (3 * s)
    reset_top = 9 ** (s + 9) * u + 1
    if reset_top % (1 << 36):
        raise AssertionError("fixed 36-bit gate failed")
    yp = reset_top >> 36
    if yp != POW9 * xp + QA:
        raise AssertionError("reset output failed")

    row = reset_row(s)
    if row.M * x + row.T != row.R * xp:
        raise AssertionError("centered formula failed")

    W = ROOT + DELTA * x
    Wp = ROOT + DELTA * xp
    raw = 9**s * (1 + POW9 * W) - (1 << (3 * s))
    if raw != row.R * Wp:
        raise AssertionError("raw source formula failed")

    z = 1 + POW16 * W
    for _ in range(9):
        if z % 16 != 1:
            raise AssertionError("illegal B edge")
        z = (9 * z + 7) // 16
    if z != 1 + POW9 * W or valuation_two(z) != 3 * s:
        raise AssertionError("B^9 replay failed")
    for _ in range(s):
        if z % 8:
            raise AssertionError("illegal A edge")
        z = 9 * z // 8
    if z != 1 + POW16 * Wp:
        raise AssertionError("physical output failed")


def word(nodes: list[VNode], node_id: int) -> tuple[int, ...]:
    output: list[int] = []
    node = nodes[node_id]
    while node.parent is not None:
        if node.label is None:
            raise AssertionError("missing edge label")
        output.append(node.label)
        node = nodes[node.parent]
    return tuple(reversed(output))


def reconstruct_nodes() -> list[VNode]:
    cap = 1 << HEIGHT
    nodes = [VNode(0, None, None, 0, 0, 1, 0, 1, cap - 1, None)]
    queue: deque[int] = deque([0])
    while queue:
        node = nodes[queue.popleft()]
        node.upper = exact_upper(node.C, node.P, node.qmax)
        node.tested = max(0, node.upper - LOW_LABEL + 1)
        if node.upper >= LOW_LABEL:
            top_bits = 3 * node.upper + 36
            inverse_top = inverse_two_power(node.P, top_bits)
        else:
            inverse_top = 0

        for s in range(LOW_LABEL, node.upper + 1):
            row = reset_row(s)
            rho = (row.xi - node.C) * inverse_top & (row.R - 1)
            if rho > node.qmax:
                continue
            theta = node.theta + node.K * rho
            K = node.K * row.R
            qmax = (node.qmax - rho) // row.R
            source = node.C + node.P * rho
            top = row.M * source + row.T
            if top % row.R:
                raise AssertionError("nonintegral transported intercept")
            C = top // row.R
            P = row.M * node.P
            if theta + K * qmax >= cap:
                raise AssertionError("child outside cap")
            if theta + K * (qmax + 1) < cap:
                raise AssertionError("nonmaximal child quotient")

            for prior_id in node.children:
                prior = nodes[prior_id]
                if prior.label is None or prior.rho is None:
                    raise AssertionError("malformed prior child")
                prior_modulus = reset_row(prior.label).R
                if (rho - prior.rho) % prior_modulus == 0:
                    raise AssertionError("overlapping intrinsic cylinders")

            # Check both affine endpoints and physically replay one point.
            for lift in {0, qmax}:
                x = node.C + node.P * (rho + row.R * lift)
                xp = C + P * lift
                if valuation_two(POW9 * x + QA) != 3 * s:
                    raise AssertionError("endpoint intrinsic label failed")
                if row.M * x + row.T != row.R * xp:
                    raise AssertionError("endpoint centered formula failed")
            replay_source(source, C, s)

            child_id = len(nodes)
            nodes.append(
                VNode(
                    child_id,
                    node.i,
                    s,
                    node.depth + 1,
                    theta,
                    K,
                    C,
                    P,
                    qmax,
                    rho,
                )
            )
            node.children.append(child_id)
            queue.append(child_id)

        continued = sum(nodes[i].qmax + 1 for i in node.children)
        node.exit_count = node.qmax + 1 - continued
        if node.exit_count < 0:
            raise AssertionError("overlapping child cylinders")
        node.status = "internal" if node.children else "exit"
    return nodes


def node_record(node: VNode) -> dict[str, object]:
    return {
        "id": node.i,
        "parent": node.parent,
        "label": node.label,
        "depth": node.depth,
        "theta": str(node.theta),
        "K": str(node.K),
        "C": str(node.C),
        "P": str(node.P),
        "q_max": str(node.qmax),
        "rho": None if node.rho is None else str(node.rho),
        "intrinsic_s_upper": node.upper,
        "candidate_label_range": (
            None if node.tested == 0 else [LOW_LABEL, node.upper]
        ),
        "children": node.children,
        "status": node.status,
        "exit_seed_count": str(node.exit_count),
        "survivor_seed_count": "0",
    }


def stable(payload: object) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def reconstruct() -> tuple[dict[str, object], dict[str, object]]:
    if DELTA != 68_332_056_247:
        raise AssertionError("D9 regression")
    if ROOT != 37_933_813_917:
        raise AssertionError("omega regression")
    if QA != 215_072_362 or QB != 38_148_886_279:
        raise AssertionError("a/b regression")
    if QB - QA != ROOT:
        raise AssertionError("quotient difference")
    if (1 << 36) * QA - POW9 * QB != 1:
        raise AssertionError("Bezout regression")

    nodes = reconstruct_nodes()
    cap = 1 << HEIGHT
    dead = [n.i for n in nodes if n.status == "exit"]
    terminals = [n.i for n in nodes if n.exit_count]
    dead_words = [word(nodes, i) for i in dead]
    terminal_tokens = [
        tuple(f"s:{s}" for s in word(nodes, i)) + ("EXIT",)
        for i in terminals
    ]
    ordered = sorted(terminal_tokens)
    for left, right in zip(ordered, ordered[1:]):
        if right[: len(left)] == left:
            raise AssertionError("terminal words are not prefix-free")

    exit_total = sum(nodes[i].exit_count for i in terminals)
    if exit_total != cap:
        raise AssertionError("exit terminals do not partition cap")
    legal_entries = sum(nodes[i].qmax + 1 for i in nodes[0].children)

    trie: dict[str, object] = {
        "schema": TRIE_SCHEMA,
        "experiment_id": IDENT,
        "scope": {
            "initial_X_lower": "0",
            "initial_X_upper_exclusive": str(cap),
            "initial_height_bits": HEIGHT,
            "minimum_intrinsic_label": LOW_LABEL,
            "depth_cutoff": None,
        },
        "transported_semantics": {
            "initial": "X_0=theta+K*q",
            "current": "X_d=C+P*q",
            "q_interval": "0<=q<=q_max",
            "child_residue": "rho=(xi_s-C)*P^{-1} mod R_s",
        },
        "root": 0,
        "nodes": [node_record(n) for n in nodes],
        "dead_end_branch_node_ids": dead,
        "dead_end_branch_words": [list(w) for w in dead_words],
        "exit_terminals": [
            {
                "node": i,
                "labels": list(word(nodes, i)),
                "terminal": "EXIT",
                "seed_count": str(nodes[i].exit_count),
            }
            for i in terminals
        ],
        "survivor_terminals": [],
        "prefix_free_terminal_words": True,
    }
    trie_hash = hashlib.sha256(stable(trie).encode()).hexdigest()

    depth_counts = Counter(n.depth for n in nodes)
    dead_depths = Counter(nodes[i].depth for i in dead)
    terminal_depths = Counter(nodes[i].depth for i in terminals)
    upper_counts = Counter(n.upper for n in nodes)
    label_counts = Counter(n.label for n in nodes if n.label is not None)
    deepest = max(n.depth for n in nodes)
    deepest_words = sorted(
        list(w) for w in dead_words if len(w) == deepest
    )

    constants = {
        "D9": DELTA,
        "omega": ROOT,
        "a": QA,
        "b": QB,
        "identities": {
            "D9_equals_16_pow_9_minus_9_pow_9": True,
            "omega_equals_minus_inverse_9_pow_9_mod_D9": True,
            "a_equals_boundary_quotient": True,
            "b_equals_boundary_quotient": True,
            "b_minus_a_equals_omega": True,
            "2_pow_36_a_minus_9_pow_9_b_equals_1": True,
            "omega_mod_7": ROOT % 7,
        },
    }
    edge_count = len(nodes) - 1
    canonical: dict[str, object] = {
        "experiment_id": IDENT,
        "status": (
            "exact finite bounded synchronized-sublanguage closure; "
            "no full Collatz exclusion"
        ),
        "agent": "gpt56-sol-03",
        "issue": 52,
        "source_snapshot": {
            "pr_53_outlier_bridges_head": PR53,
            "pr_51_physical_chart_head": PR51,
        },
        "constants": constants,
        "scope": {
            "initial_X_interval": "0<=X_0<2^512",
            "initial_height_bits": HEIGHT,
            "minimum_intrinsic_label": LOW_LABEL,
            "branch_height": "h_s=3s+36",
            "depth_cutoff": None,
        },
        "exact_finiteness_bound": {
            "definition": (
                "Y_max=9^9*(C+P*q_max)+a; "
                "s_upper=(Y_max.bit_length()-1)//3"
            ),
            "proof": (
                "v2(9^9*X_d+a)=3s and Y>0 imply "
                "2^(3s)<=Y<=Y_max"
            ),
            "floating_logarithms_used": False,
            "root_s_upper": nodes[0].upper,
            "largest_s_upper_over_all_nodes": max(n.upper for n in nodes),
        },
        "counts": {
            "nodes_including_root": len(nodes),
            "retained_edges": edge_count,
            "candidate_labels_tested": sum(n.tested for n in nodes),
            "dead_end_branch_nodes": len(dead),
            "exit_terminals": len(terminals),
            "survivor_terminals": 0,
            "legal_entry_seed_count": str(legal_entries),
            "immediate_entry_exit_seed_count": str(nodes[0].exit_count),
            "partitioned_exit_seed_count": str(exit_total),
            "partitioned_survivor_seed_count": "0",
            "all_initial_seed_count": str(cap),
        },
        "checks": {
            "retained_edges": edge_count,
            "intrinsic_label_checks": edge_count,
            "centered_formula_checks": edge_count,
            "physical_source_replays": edge_count,
        },
        "tree": {
            "depth_histogram": {
                str(k): depth_counts[k] for k in sorted(depth_counts)
            },
            "dead_end_depth_histogram": {
                str(k): dead_depths[k] for k in sorted(dead_depths)
            },
            "exit_terminal_depth_histogram": {
                str(k): terminal_depths[k] for k in sorted(terminal_depths)
            },
            "bound_histogram": {
                str(k): upper_counts[k] for k in sorted(upper_counts)
            },
            "root_child_labels": [
                nodes[i].label for i in nodes[0].children
            ],
            "retained_label_min": min(label_counts),
            "retained_label_max": max(label_counts),
            "retained_label_histogram": {
                str(k): label_counts[k] for k in sorted(label_counts)
            },
            "maximum_retained_depth": deepest,
            "deepest_exit_words": deepest_words,
            "prefix_free_terminal_exit_trie": True,
        },
        "result": {
            "maximum_consecutive_defined_labels_at_least_44": deepest,
            "length_four_prefixes": 0,
            "length_three_prefixes": len(deepest_words),
            "all_length_three_prefixes_exit_before_a_fourth": True,
            "bounded_statement_only": True,
        },
        "exit_trie": {
            "path": "results/exit-trie.json",
            "sha256": trie_hash,
            "schema": TRIE_SCHEMA,
        },
    }
    return canonical, trie


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    parser.add_argument("trie", type=Path, nargs="?")
    args = parser.parse_args()
    trie_path = args.trie or args.canonical.with_name("exit-trie.json")

    frozen_canonical = json.loads(args.canonical.read_text(encoding="utf-8"))
    frozen_trie = json.loads(trie_path.read_text(encoding="utf-8"))
    rebuilt_canonical, rebuilt_trie = reconstruct()
    if frozen_trie != rebuilt_trie:
        raise SystemExit("independent exit-trie reconstruction mismatch")
    if frozen_canonical != rebuilt_canonical:
        raise SystemExit("independent canonical reconstruction mismatch")

    print("independent reconstruction matches both artifacts")
    print(json.dumps(rebuilt_canonical["counts"], sort_keys=True))
    print(
        "max_consecutive_high_branches="
        f"{rebuilt_canonical['result']['maximum_consecutive_defined_labels_at_least_44']}"
    )
    print(f"exit_trie_sha256={rebuilt_canonical['exit_trie']['sha256']}")


if __name__ == "__main__":
    main()
