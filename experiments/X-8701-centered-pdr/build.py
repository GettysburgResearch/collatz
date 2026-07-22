#!/usr/bin/env python3
"""Build the proof-carrying fixed-precision centered-tail certificate.

This program is independent of repository/author code. It constructs the
forced zero-block map, its fixed-modulus existential PDR graphs, the exact
cylinder/de Bruijn kernel, the bounded base-64 carry transducer, and finite
ordinary-seed diagnostics. Finite computations corroborate the accompanying
universal proofs; they are not substitutes for them.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json, platform, sys
from collections import deque
from fractions import Fraction
from pathlib import Path

SEED = 0x870040


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def branch(residue, digit):
    if residue == 0:
        return digit, 0
    if digit == 1 and residue == 15:
        return 0, 19
    if digit == 0 and residue == 49:
        return 1, 62
    return None


def step(B, digit):
    rule = branch(B % 64, digit)
    if rule is None:
        return None
    next_digit, offset = rule
    return 81 * ((B - B % 64) // 64) + offset, next_digit


def cylinder(word):
    R = C = 0
    m_pow = n_pow = 1
    inv = pow(81, -1, 64)
    blocks = []
    for k in range(len(word) - 1):
        d = word[k] - word[k + 1]
        q = (-pow(inv, k + 1, 64) * (81 * C + d)) % 64
        numerator = 81 * (C + q * n_pow) + d
        assert numerator % 64 == 0
        blocks.append(q)
        R += q * m_pow
        C = numerator // 64
        m_pow *= 64
        n_pow *= 81
    return R, C, tuple(blocks)


def periodic_completion(period):
    p = len(period)
    one_period = sum(
        Fraction(-(period[j] - period[(j + 1) % p]) * 64**j, 81 ** (j + 1))
        for j in range(p)
    )
    return one_period / (1 - Fraction(64**p, 81**p))


def build_graph(precision):
    modulus = 64**precision
    states = []
    index = {}
    for digit in (0, 1):
        for residue in range(modulus):
            if branch(residue % 64, digit) is not None:
                index[(residue, digit)] = len(states)
                states.append((residue, digit))
    adjacency = [[] for _ in states]
    for i, (residue, digit) in enumerate(states):
        next_digit, offset = branch(residue % 64, digit)
        low = residue % 64
        for high in range(64):
            B = residue + high * modulus
            target_residue = (81 * ((B - low) // 64) + offset) % modulus
            target = index.get((target_residue, next_digit))
            if target is not None:
                adjacency[i].append((target, high))
    return states, index, adjacency


def strongly_connected_components(adjacency):
    n = len(adjacency)
    sys.setrecursionlimit(max(10000, 2 * n))
    counter = 0
    index = [-1] * n
    low = [0] * n
    stack = []
    on_stack = [False] * n
    components = []

    def dfs(v):
        nonlocal counter
        index[v] = low[v] = counter
        counter += 1
        stack.append(v)
        on_stack[v] = True
        for w, _ in adjacency[v]:
            if index[w] < 0:
                dfs(w)
                low[v] = min(low[v], low[w])
            elif on_stack[w]:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == v:
                    break
            components.append(component)

    for v in range(n):
        if index[v] < 0:
            dfs(v)
    return components


def infinite_path_kernel(adjacency, cyclic_nodes):
    reverse = [set() for _ in adjacency]
    for v, edges in enumerate(adjacency):
        for w, _ in edges:
            reverse[w].add(v)
    kernel = set(cyclic_nodes)
    queue = deque(cyclic_nodes)
    while queue:
        w = queue.popleft()
        for v in reverse[w]:
            if v not in kernel:
                kernel.add(v)
                queue.append(v)
    return kernel


def carry_certificate():
    cases = 0
    max_carry = 0
    for offset in (0, 19, 62):
        stop = False
        for length in range(1, 6):
            for digits in itertools.product(range(64), repeat=length):
                Q = sum(a * 64**j for j, a in enumerate(digits))
                target = 81 * Q + offset
                output = []
                carry = offset
                previous = 0
                for j in range(length + 3):
                    a = digits[j] if j < length else 0
                    raw = 17 * a + previous + carry
                    output.append(raw % 64)
                    carry = raw // 64
                    if j >= 1:
                        max_carry = max(max_carry, carry)
                    previous = a
                assert sum(a * 64**j for j, a in enumerate(output)) == target
                cases += 1
                if cases >= 300_000:
                    stop = True
                    break
            if stop:
                break
        if stop:
            break
    assert max_carry <= 17
    return {"exact_digit_cases": cases, "post_first_column_max_carry": max_carry}


def pdr_certificate():
    rows = []
    for precision in (1, 2, 3):
        states, state_index, adjacency = build_graph(precision)
        components = strongly_connected_components(adjacency)
        cyclic = []
        for component in components:
            if len(component) > 1 or any(w == component[0] for w, _ in adjacency[component[0]]):
                cyclic.extend(component)
        kernel = infinite_path_kernel(adjacency, cyclic)
        word_by_state = {}
        for word in itertools.product((0, 1), repeat=precision + 1):
            residue, _, _ = cylinder(word)
            state = (residue, word[0])
            assert state not in word_by_state
            word_by_state[state] = word
        cylinder_nodes = {state_index[state] for state in word_by_state}
        assert kernel == cylinder_nodes == set(cyclic)
        assert len(kernel) == 2 ** (precision + 1)

        debruijn_edges = []
        for state, word in sorted(word_by_state.items()):
            source = state_index[state]
            for appended in (0, 1):
                extended = word + (appended,)
                extended_residue, _, _ = cylinder(extended)
                high = (extended_residue - state[0]) // (64**precision)
                assert 0 <= high < 64
                suffix = word[1:] + (appended,)
                target_residue, _, _ = cylinder(suffix)
                target = state_index[(target_residue, suffix[0])]
                assert (target, high) in adjacency[source]
                exact_target = step(extended_residue, word[0])
                assert exact_target is not None
                assert exact_target[1] == suffix[0]
                assert exact_target[0] % (64**precision) == target_residue
                debruijn_edges.append((word, appended, high, suffix))

        ghosts = set()
        modulus = 64**precision
        for period in itertools.product((0, 1), repeat=precision + 1):
            completion = periodic_completion(period)
            residue = completion.numerator * pow(completion.denominator, -1, modulus) % modulus
            ghosts.add((residue, period[0]))
        assert ghosts == set(word_by_state)

        state_payload = [
            {"residue": state[0], "digit": state[1], "word": "".join(map(str, word))}
            for state, word in sorted(word_by_state.items())
        ]
        edge_payload = [
            {"word": "".join(map(str, word)), "appended": appended,
             "high_block": high, "target": "".join(map(str, suffix))}
            for word, appended, high, suffix in debruijn_edges
        ]
        rows.append({
            "precision": precision,
            "ambient_safe_states": len(states),
            "ambient_edges": sum(map(len, adjacency)),
            "scc_count": len(components),
            "kernel_states": len(kernel),
            "kernel_state_digest": digest(state_payload),
            "de_bruijn_edges": len(edge_payload),
            "de_bruijn_edge_digest": digest(edge_payload),
            "periodic_ghost_states": len(ghosts),
        })

    scalable = []
    for precision in range(1, 16):
        states = set()
        for word in itertools.product((0, 1), repeat=precision + 1):
            residue, _, _ = cylinder(word)
            state = (residue, word[0])
            assert state not in states
            states.add(state)
        scalable.append({"precision": precision, "cylinder_states": len(states),
                         "de_bruijn_edges": 2 * len(states)})

    total = nonconstant = 0
    for p in range(1, 16):
        for period in itertools.product((0, 1), repeat=p):
            completion = periodic_completion(period)
            total += 1
            if len(set(period)) == 1:
                assert completion == 0
            else:
                assert completion.denominator != 1
                nonconstant += 1
    return {"fixed_precision_graphs": rows, "scalable_last": scalable[-1],
            "periodic_controls_checked": total,
            "nonconstant_periodic_ghosts": nonconstant,
            "carry_transducer": carry_certificate()}


def invariant_and_monotonicity(limit):
    checked = 0
    classes = set()
    for B in range(limit + 1):
        for digit in (0, 1):
            nxt = step(B, digit)
            if nxt is None:
                continue
            next_B, next_digit = nxt
            assert (next_B + 4 * next_digit - B - 4 * digit) % 17 == 0
            if B > 0:
                assert next_B > B
            classes.add((B + 4 * digit) % 17)
            checked += 1
    return {"exact_steps": checked, "search_limit": limit,
            "observed_invariant_classes": sorted(classes),
            "positive_steps_strictly_increasing": True}


def finite_seed_scan(limit):
    best_depth = -1
    best_witness = None
    histogram = {}
    for B in range(1, limit + 1):
        for digit in (0, 1):
            current_B, current_digit = B, digit
            depth = 0
            while depth < 256:
                nxt = step(current_B, current_digit)
                if nxt is None:
                    break
                current_B, current_digit = nxt
                depth += 1
            histogram[depth] = histogram.get(depth, 0) + 1
            if depth > best_depth:
                best_depth = depth
                best_witness = [B, digit, current_B, current_digit]
    return {"limit": limit, "best_survival": best_depth, "best_witness": best_witness,
            "histogram": {str(k): histogram[k] for k in sorted(histogram)}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-limit", type=int, default=1_000_000)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()
    payload = {
        "experiment_id": "X-8701", "agent": "gpt56-pdr-01", "issue": 40,
        "frozen_pr16": "87478352e65c7b816dfc8b3b30894b71fb50f662", "seed": SEED,
        "forced_system": {"equation": "64*B_next = 81*B + e - e_next",
            "branches": [
                {"e": 0, "residue": 0, "e_next": 0, "offset": 0},
                {"e": 0, "residue": 49, "e_next": 1, "offset": 62},
                {"e": 1, "residue": 0, "e_next": 1, "offset": 0},
                {"e": 1, "residue": 15, "e_next": 0, "offset": 19}]},
        "pdr": pdr_certificate(),
        "monotonicity_and_mod17": invariant_and_monotonicity(1_000_000),
        "finite_seed_scan": finite_seed_scan(args.seed_limit),
    }
    payload["semantic_digest"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    if args.check_results and payload != json.loads(args.check_results.read_text()):
        print("frozen result mismatch", file=sys.stderr)
        return 1
    print(text, end="")
    print(json.dumps({"python": platform.python_version(), "platform": platform.platform()}, sort_keys=True), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
