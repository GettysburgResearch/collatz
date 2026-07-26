#!/usr/bin/env python3
"""Exact transported search for the bounded synchronized high-run language.

The default computation partitions every nonempty legal high-branch prefix
with 0 <= X_0 < 2^512.  All arithmetic is integral; in particular, the
per-node label bound is obtained from ``int.bit_length()``, never a floating
point logarithm.
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
from typing import Iterable

sys.set_int_max_str_digits(0)

EXPERIMENT_ID = "X-8256"
SCHEMA = "x-8256-transported-exit-trie-v1"
CAP_BITS = 512
MIN_LABEL = 44

# L-8251/L-8252 constants, rederived and checked by ``audit_constants``.
D9 = 68_332_056_247
OMEGA = 37_933_813_917
A = 215_072_362
B = 38_148_886_279
NINE9 = 9**9
SIXTEEN9 = 16**9

PR53_HEAD = "8b63eb7dda864430ad64c46ae6f8f58d399ef7b8"
PR51_SOURCE_HEAD = "bf00552e5054fd8e5d1692648911b377c5624e56"


@dataclass(frozen=True)
class Branch:
    label: int
    height: int
    radix: int
    multiplier: int
    toll: int
    residue: int


@dataclass
class Node:
    node_id: int
    parent: int | None
    label: int | None
    depth: int
    theta: int
    K: int
    C: int
    P: int
    q_max: int
    rho: int | None
    s_upper: int = -1
    candidate_count: int = 0
    children: list[int] = field(default_factory=list)
    status: str = "unvisited"
    exit_seed_count: int = 0
    survivor_seed_count: int = 0


@dataclass(frozen=True)
class InitialState:
    """One transported family.

    The represented points are

        X_0 = theta + K*q,
        X_d = C + P*q,
        0 <= q <= q_max.

    ``P`` must be odd so every dyadic child congruence has one residue in q.
    """

    theta: int
    K: int
    C: int
    P: int
    q_max: int


def audit_constants() -> dict[str, object]:
    """Reconstruct every imported synchronizer constant from source formulas."""
    derived_d9 = SIXTEEN9 - NINE9
    if derived_d9 != D9:
        raise AssertionError("D9 does not equal 16^9-9^9")
    derived_omega = (-pow(NINE9, -1, D9)) % D9
    if derived_omega != OMEGA:
        raise AssertionError("omega is not the declared inverse residue")
    if (NINE9 * OMEGA + 1) % D9:
        raise AssertionError("9^9 boundary quotient is not integral")
    if (SIXTEEN9 * OMEGA + 1) % D9:
        raise AssertionError("16^9 boundary quotient is not integral")
    derived_a = (NINE9 * OMEGA + 1) // D9
    derived_b = (SIXTEEN9 * OMEGA + 1) // D9
    if (derived_a, derived_b) != (A, B):
        raise AssertionError("a/b quotient constants disagree with source")
    if B - A != OMEGA:
        raise AssertionError("b-a != omega")
    if (1 << 36) * A - NINE9 * B != 1:
        raise AssertionError("36-bit Bezout identity failed")
    if OMEGA % 7 != 6:
        raise AssertionError("divisible-seven boundary residue failed")
    return {
        "D9": D9,
        "omega": OMEGA,
        "a": A,
        "b": B,
        "identities": {
            "D9_equals_16_pow_9_minus_9_pow_9": True,
            "omega_equals_minus_inverse_9_pow_9_mod_D9": True,
            "a_equals_boundary_quotient": True,
            "b_equals_boundary_quotient": True,
            "b_minus_a_equals_omega": True,
            "2_pow_36_a_minus_9_pow_9_b_equals_1": True,
            "omega_mod_7": OMEGA % 7,
        },
    }


def v2(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0) is undefined")
    value = abs(value)
    return (value & -value).bit_length() - 1


@lru_cache(maxsize=None)
def branch(label: int) -> Branch:
    if label < 0:
        raise ValueError("negative branch label")
    height = 3 * label + 36
    radix = 1 << height
    multiplier = 9 ** (label + 9)
    toll = 9**label * A - 8**label * B
    residue = (-toll * pow(multiplier, -1, radix)) & (radix - 1)
    if (multiplier * residue + toll) % radix:
        raise AssertionError("branch residue is not integral")
    return Branch(label, height, radix, multiplier, toll, residue)


def intrinsic_label(x: int, minimum: int = 0) -> int | None:
    """Return the actual synchronized label, including the fixed 36-bit gate."""
    y = NINE9 * x + A
    if y == 0:
        return None
    valuation = v2(y)
    if valuation % 3:
        return None
    label = valuation // 3
    if label < minimum:
        return None
    row = branch(label)
    numerator = row.multiplier * x + row.toll
    if numerator % row.radix:
        return None
    return label


def centered_step(x: int, label: int) -> int | None:
    row = branch(label)
    if intrinsic_label(x) != label:
        return None
    numerator = row.multiplier * x + row.toll
    if numerator % row.radix:
        return None
    return numerator // row.radix


def physical_replay(x: int, x_next: int, label: int) -> None:
    """Replay the PR #51 A/B chart for one L-8251 synchronized block."""
    W = OMEGA + D9 * x
    W_next = OMEGA + D9 * x_next
    if W <= 0 or W_next <= 0:
        raise AssertionError("physical boundary is not positive")

    z = 1 + SIXTEEN9 * W
    for _ in range(9):
        if z % 16 != 1:
            raise AssertionError("physical B edge is not legal")
        z = (9 * z + 7) // 16
    if z != 1 + NINE9 * W:
        raise AssertionError("B^9 source formula failed")
    if v2(z) != 3 * label:
        raise AssertionError("physical intrinsic high-run label failed")

    for _ in range(label):
        if z % 8:
            raise AssertionError("physical A edge is not legal")
        z = 9 * z // 8
    if z != 1 + SIXTEEN9 * W_next:
        raise AssertionError("physical synchronized output failed")

    source_numerator = 9**label * (1 + NINE9 * W) - 2 ** (3 * label)
    row = branch(label)
    if source_numerator != row.radix * W_next:
        raise AssertionError("L-8251 source formula failed")


def exact_label_upper(C: int, P: int, q_max: int) -> int:
    """Complete intrinsic-label bound for C+P*q, 0<=q<=q_max.

    If Y=9^9(C+Pq)+a is nonzero and v2(Y)=3s, then 2^(3s)<=|Y|.
    The affine absolute value attains its maximum at an endpoint.  Therefore
    ``(max_abs.bit_length()-1)//3`` is a finite exact upper bound.
    """
    if P <= 0 or q_max < 0:
        raise ValueError("invalid transported interval")
    y0 = NINE9 * C + A
    y1 = NINE9 * (C + P * q_max) + A
    max_abs = max(abs(y0), abs(y1))
    if max_abs == 0:
        return -1
    return (max_abs.bit_length() - 1) // 3


def _check_retained_edge(
    parent: Node,
    child_C: int,
    child_P: int,
    child_q_max: int,
    rho: int,
    row: Branch,
) -> None:
    """Check intrinsic, centered, and physical formulas for one retained edge."""
    if not 0 <= rho <= parent.q_max:
        raise AssertionError("retained rho is outside the parent interval")
    if (parent.C + parent.P * rho - row.residue) % row.radix:
        raise AssertionError("retained input misses the branch cylinder")
    if child_P != row.multiplier * parent.P:
        raise AssertionError("transported slope update failed")

    # The endpoints establish the affine identity on the full retained family.
    lifts = {0, child_q_max}
    for lift in lifts:
        parent_q = rho + row.radix * lift
        x = parent.C + parent.P * parent_q
        x_next = child_C + child_P * lift
        if intrinsic_label(x) != row.label:
            raise AssertionError("intrinsic label check failed")
        numerator = row.multiplier * x + row.toll
        if numerator != row.radix * x_next:
            raise AssertionError("centered source formula failed")

    representative_x = parent.C + parent.P * rho
    physical_replay(representative_x, child_C, row.label)


def _word(nodes: list[Node], node_id: int) -> tuple[int, ...]:
    labels: list[int] = []
    current = nodes[node_id]
    while current.parent is not None:
        if current.label is None:
            raise AssertionError("nonroot node lacks an edge label")
        labels.append(current.label)
        current = nodes[current.parent]
    labels.reverse()
    return tuple(labels)


def _assert_prefix_free(words: Iterable[tuple[str, ...]]) -> None:
    ordered = sorted(words)
    for left, right in zip(ordered, ordered[1:]):
        if len(left) <= len(right) and right[: len(left)] == left:
            raise AssertionError(f"non-prefix-free leaves: {left}, {right}")


def transported_closure(
    *,
    cap_exclusive: int,
    minimum_label: int,
    initial: InitialState,
    max_transitions: int | None = None,
) -> tuple[list[Node], dict[str, int]]:
    """Enumerate the exact finite transported trie.

    ``max_transitions`` is only a testing/diagnostic option.  Nodes at that
    boundary are recorded exactly as survivors instead of being extrapolated.
    The canonical 512-bit computation supplies no depth cutoff.
    """
    if cap_exclusive <= 0:
        raise ValueError("nonpositive cap")
    if minimum_label < 0:
        raise ValueError("negative minimum label")
    if initial.K <= 0 or initial.P <= 0 or initial.P % 2 == 0:
        raise ValueError("K must be positive and P must be positive odd")
    if initial.q_max < 0:
        raise ValueError("empty initial state")
    if initial.theta < 0:
        raise ValueError("negative initial seed")
    if initial.theta + initial.K * initial.q_max >= cap_exclusive:
        raise ValueError("initial state exceeds cap")
    if initial.theta + initial.K * (initial.q_max + 1) < cap_exclusive:
        raise ValueError("initial q_max does not close the capped family")

    nodes = [
        Node(
            node_id=0,
            parent=None,
            label=None,
            depth=0,
            theta=initial.theta,
            K=initial.K,
            C=initial.C,
            P=initial.P,
            q_max=initial.q_max,
            rho=None,
        )
    ]
    pending: deque[int] = deque([0])
    checks = {
        "retained_edges": 0,
        "intrinsic_label_checks": 0,
        "centered_formula_checks": 0,
        "physical_source_replays": 0,
    }

    while pending:
        node = nodes[pending.popleft()]
        node.s_upper = exact_label_upper(node.C, node.P, node.q_max)
        node.candidate_count = max(0, node.s_upper - minimum_label + 1)

        if max_transitions is not None and node.depth >= max_transitions:
            node.status = "survivor"
            node.survivor_seed_count = node.q_max + 1
            continue

        if node.s_upper >= minimum_label:
            largest_radix = 1 << (3 * node.s_upper + 36)
            # One inverse at the largest modulus supplies every lower power of
            # two by masking.  This is an optimization, not an extra premise.
            inverse_at_top = pow(node.P, -1, largest_radix)
        else:
            inverse_at_top = 0

        for label in range(minimum_label, node.s_upper + 1):
            row = branch(label)
            rho = ((row.residue - node.C) * inverse_at_top) & (row.radix - 1)
            if rho > node.q_max:
                continue

            theta_next = node.theta + node.K * rho
            K_next = node.K * row.radix
            q_max_next = (node.q_max - rho) // row.radix
            numerator = row.multiplier * (node.C + node.P * rho) + row.toll
            if numerator % row.radix:
                raise AssertionError("transported intercept is not integral")
            C_next = numerator // row.radix
            P_next = row.multiplier * node.P

            if theta_next + K_next * q_max_next >= cap_exclusive:
                raise AssertionError("child exceeds initial-height cap")
            if theta_next + K_next * (q_max_next + 1) < cap_exclusive:
                raise AssertionError("child q_max is not maximal")

            # Labels are scanned upward, so every prior child has a smaller
            # power-of-two modulus.  Congruence here would mean overlap.
            for prior_id in node.children:
                prior = nodes[prior_id]
                if prior.label is None or prior.rho is None:
                    raise AssertionError("malformed prior child")
                prior_radix = branch(prior.label).radix
                if (rho - prior.rho) % prior_radix == 0:
                    raise AssertionError("different intrinsic labels overlap")

            _check_retained_edge(
                node, C_next, P_next, q_max_next, rho, row
            )
            child_id = len(nodes)
            child = Node(
                node_id=child_id,
                parent=node.node_id,
                label=label,
                depth=node.depth + 1,
                theta=theta_next,
                K=K_next,
                C=C_next,
                P=P_next,
                q_max=q_max_next,
                rho=rho,
            )
            nodes.append(child)
            node.children.append(child_id)
            pending.append(child_id)
            checks["retained_edges"] += 1
            checks["intrinsic_label_checks"] += 1
            checks["centered_formula_checks"] += 1
            checks["physical_source_replays"] += 1

        continued = sum(nodes[child_id].q_max + 1 for child_id in node.children)
        node.exit_seed_count = node.q_max + 1 - continued
        if node.exit_seed_count < 0:
            raise AssertionError("child cylinders overlap or exceed parent")
        node.status = "internal" if node.children else "exit"

    return nodes, checks


def _node_record(node: Node) -> dict[str, object]:
    return {
        "id": node.node_id,
        "parent": node.parent,
        "label": node.label,
        "depth": node.depth,
        "theta": str(node.theta),
        "K": str(node.K),
        "C": str(node.C),
        "P": str(node.P),
        "q_max": str(node.q_max),
        "rho": None if node.rho is None else str(node.rho),
        "intrinsic_s_upper": node.s_upper,
        "candidate_label_range": (
            None if node.candidate_count == 0 else [MIN_LABEL, node.s_upper]
        ),
        "children": node.children,
        "status": node.status,
        "exit_seed_count": str(node.exit_seed_count),
        "survivor_seed_count": str(node.survivor_seed_count),
    }


def stable_json(payload: object) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def build_default_outputs() -> tuple[dict[str, object], dict[str, object]]:
    constants = audit_constants()
    cap = 1 << CAP_BITS
    initial = InitialState(theta=0, K=1, C=0, P=1, q_max=cap - 1)
    nodes, checks = transported_closure(
        cap_exclusive=cap,
        minimum_label=MIN_LABEL,
        initial=initial,
    )

    dead_end_ids = [node.node_id for node in nodes if node.status == "exit"]
    survivor_ids = [node.node_id for node in nodes if node.status == "survivor"]
    exit_terminal_ids = [
        node.node_id for node in nodes if node.exit_seed_count > 0
    ]
    dead_end_words = [_word(nodes, node_id) for node_id in dead_end_ids]
    survivor_words = [_word(nodes, node_id) for node_id in survivor_ids]
    exit_terminal_words = [
        tuple(f"s:{label}" for label in _word(nodes, node_id)) + ("EXIT",)
        for node_id in exit_terminal_ids
    ]
    survivor_terminal_words = [
        tuple(f"s:{label}" for label in _word(nodes, node_id)) + ("SURVIVOR",)
        for node_id in survivor_ids
    ]
    _assert_prefix_free(exit_terminal_words + survivor_terminal_words)

    # Terminal edges, rather than only dead-end branch nodes, partition every
    # initial seed: an internal branch prefix also has seeds that exit there.
    root_seed_count = sum(nodes[i].q_max + 1 for i in nodes[0].children)
    partitioned_exit_count = sum(
        nodes[i].exit_seed_count for i in exit_terminal_ids
    )
    partitioned_survivor_count = sum(
        nodes[i].survivor_seed_count for i in survivor_ids
    )
    if partitioned_exit_count + partitioned_survivor_count != cap:
        raise AssertionError("terminal trie does not partition initial interval")

    trie: dict[str, object] = {
        "schema": SCHEMA,
        "experiment_id": EXPERIMENT_ID,
        "scope": {
            "initial_X_lower": "0",
            "initial_X_upper_exclusive": str(cap),
            "initial_height_bits": CAP_BITS,
            "minimum_intrinsic_label": MIN_LABEL,
            "depth_cutoff": None,
        },
        "transported_semantics": {
            "initial": "X_0=theta+K*q",
            "current": "X_d=C+P*q",
            "q_interval": "0<=q<=q_max",
            "child_residue": "rho=(xi_s-C)*P^{-1} mod R_s",
        },
        "root": 0,
        "nodes": [_node_record(node) for node in nodes],
        "dead_end_branch_node_ids": dead_end_ids,
        "dead_end_branch_words": [list(word) for word in dead_end_words],
        "exit_terminals": [
            {
                "node": node_id,
                "labels": list(_word(nodes, node_id)),
                "terminal": "EXIT",
                "seed_count": str(nodes[node_id].exit_seed_count),
            }
            for node_id in exit_terminal_ids
        ],
        "survivor_terminals": [
            {
                "node": node_id,
                "labels": list(_word(nodes, node_id)),
                "terminal": "SURVIVOR",
                "seed_count": str(nodes[node_id].survivor_seed_count),
            }
            for node_id in survivor_ids
        ],
        "prefix_free_terminal_words": True,
    }
    trie_text = stable_json(trie)
    trie_sha256 = hashlib.sha256(trie_text.encode("utf-8")).hexdigest()

    depth_histogram = Counter(node.depth for node in nodes)
    dead_end_depth_histogram = Counter(nodes[i].depth for i in dead_end_ids)
    exit_terminal_depth_histogram = Counter(
        nodes[i].depth for i in exit_terminal_ids
    )
    label_histogram = Counter(
        node.label for node in nodes if node.label is not None
    )
    bound_histogram = Counter(node.s_upper for node in nodes)
    deepest = max((node.depth for node in nodes), default=0)
    deepest_exit_words = sorted(
        list(word) for word in dead_end_words if len(word) == deepest
    )
    candidate_scans = sum(node.candidate_count for node in nodes)
    retained_labels = [int(label) for label in label_histogram]

    canonical: dict[str, object] = {
        "experiment_id": EXPERIMENT_ID,
        "status": (
            "exact finite bounded synchronized-sublanguage closure; "
            "no full Collatz exclusion"
        ),
        "agent": "gpt56-sol-03",
        "issue": 52,
        "source_snapshot": {
            "pr_53_outlier_bridges_head": PR53_HEAD,
            "pr_51_physical_chart_head": PR51_SOURCE_HEAD,
        },
        "constants": constants,
        "scope": {
            "initial_X_interval": f"0<=X_0<2^{CAP_BITS}",
            "initial_height_bits": CAP_BITS,
            "minimum_intrinsic_label": MIN_LABEL,
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
            "root_s_upper": nodes[0].s_upper,
            "largest_s_upper_over_all_nodes": max(node.s_upper for node in nodes),
        },
        "counts": {
            "nodes_including_root": len(nodes),
            "retained_edges": len(nodes) - 1,
            "candidate_labels_tested": candidate_scans,
            "dead_end_branch_nodes": len(dead_end_ids),
            "exit_terminals": len(exit_terminal_ids),
            "survivor_terminals": len(survivor_ids),
            "legal_entry_seed_count": str(root_seed_count),
            "immediate_entry_exit_seed_count": str(nodes[0].exit_seed_count),
            "partitioned_exit_seed_count": str(partitioned_exit_count),
            "partitioned_survivor_seed_count": str(partitioned_survivor_count),
            "all_initial_seed_count": str(cap),
        },
        "checks": checks,
        "tree": {
            "depth_histogram": {
                str(k): depth_histogram[k] for k in sorted(depth_histogram)
            },
            "dead_end_depth_histogram": {
                str(k): dead_end_depth_histogram[k]
                for k in sorted(dead_end_depth_histogram)
            },
            "exit_terminal_depth_histogram": {
                str(k): exit_terminal_depth_histogram[k]
                for k in sorted(exit_terminal_depth_histogram)
            },
            "bound_histogram": {
                str(k): bound_histogram[k] for k in sorted(bound_histogram)
            },
            "root_child_labels": [
                nodes[i].label for i in nodes[0].children
            ],
            "retained_label_min": min(retained_labels),
            "retained_label_max": max(retained_labels),
            "retained_label_histogram": {
                str(k): label_histogram[k] for k in sorted(label_histogram)
            },
            "maximum_retained_depth": deepest,
            "deepest_exit_words": deepest_exit_words,
            "prefix_free_terminal_exit_trie": True,
        },
        "result": {
            "maximum_consecutive_defined_labels_at_least_44": deepest,
            "length_four_prefixes": 0,
            "length_three_prefixes": len(deepest_exit_words),
            "all_length_three_prefixes_exit_before_a_fourth": not survivor_ids,
            "bounded_statement_only": True,
        },
        "exit_trie": {
            "path": "results/exit-trie.json",
            "sha256": trie_sha256,
            "schema": SCHEMA,
        },
    }
    return canonical, trie


def _resolve_results(path: Path) -> tuple[Path, Path]:
    if path.suffix == ".json":
        return path, path.with_name("exit-trie.json")
    return path / "canonical.json", path / "exit-trie.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--write-results",
        type=Path,
        help="canonical JSON path or results directory",
    )
    group.add_argument(
        "--check-results",
        type=Path,
        help="canonical JSON path or results directory",
    )
    args = parser.parse_args()

    canonical, trie = build_default_outputs()
    selected = args.write_results or args.check_results
    canonical_path, trie_path = _resolve_results(selected)
    if args.write_results:
        canonical_path.parent.mkdir(parents=True, exist_ok=True)
        canonical_path.write_text(stable_json(canonical), encoding="utf-8")
        trie_path.write_text(stable_json(trie), encoding="utf-8")
        print(f"wrote {canonical_path}")
        print(f"wrote {trie_path}")
    else:
        frozen_canonical = json.loads(canonical_path.read_text(encoding="utf-8"))
        frozen_trie = json.loads(trie_path.read_text(encoding="utf-8"))
        if frozen_canonical != canonical:
            raise SystemExit(f"result mismatch: {canonical_path}")
        if frozen_trie != trie:
            raise SystemExit(f"result mismatch: {trie_path}")
        print("frozen results verified")

    print(json.dumps(canonical["counts"], sort_keys=True))
    print(
        "max_consecutive_high_branches="
        f"{canonical['result']['maximum_consecutive_defined_labels_at_least_44']}"
    )
    print(f"exit_trie_sha256={canonical['exit_trie']['sha256']}")


if __name__ == "__main__":
    main()
