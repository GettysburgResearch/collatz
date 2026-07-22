#!/usr/bin/env python3
"""Independent verifier for X-8701; does not import build.py."""
from __future__ import annotations
import argparse, hashlib, itertools, json, platform
from fractions import Fraction
from pathlib import Path


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def branch(r, e):
    return {(0, 0): (0, 0), (49, 0): (1, 62),
            (0, 1): (1, 0), (15, 1): (0, 19)}.get((r, e))


def step(B, e):
    item = branch(B % 64, e)
    if item is None:
        return None
    ep, _ = item
    return (81 * B + e - ep) // 64, ep


def direct_residue(word):
    d = len(word) - 1
    if d == 0:
        return 0
    modulus = 64**d
    total = sum((word[i] - word[i + 1]) * 64**i * pow(81, -i - 1, modulus)
                for i in range(d))
    return (-total) % modulus


def terminal_from_residue(word, B):
    current = B
    for i in range(len(word) - 1):
        numerator = 81 * current + word[i] - word[i + 1]
        assert numerator % 64 == 0
        current = numerator // 64
    return current


def periodic_completion(period):
    p = len(period)
    numerator = -sum((period[i] - period[(i + 1) % p]) * 64**i * 81 ** (p - 1 - i)
                     for i in range(p))
    return Fraction(numerator, 81**p - 64**p)


def ambient_graph(d):
    modulus = 64**d
    states = [(b, e) for e in (0, 1) for b in range(modulus)
              if branch(b % 64, e) is not None]
    index = {state: i for i, state in enumerate(states)}
    adjacency = [set() for _ in states]
    labels = [dict() for _ in states]
    for i, (b, e) in enumerate(states):
        ep, _ = branch(b % 64, e)
        for high in range(64):
            exact = step(b + high * modulus, e)
            assert exact is not None and exact[1] == ep
            target = index.get((exact[0] % modulus, ep))
            if target is not None:
                adjacency[i].add(target)
                labels[i].setdefault(target, set()).add(high)
    return states, index, adjacency, labels


def greatest_existential_kernel(adjacency):
    alive = set(range(len(adjacency)))
    while True:
        removed = {v for v in alive if not (adjacency[v] & alive)}
        if not removed:
            return alive
        alive -= removed


def verify_graph_rows(expected_rows):
    actual_rows = []
    for d in (1, 2, 3):
        states, index, adjacency, labels = ambient_graph(d)
        kernel = greatest_existential_kernel(adjacency)
        words = {}
        for word in itertools.product((0, 1), repeat=d + 1):
            residue = direct_residue(word)
            terminal_from_residue(word, residue)
            state = (residue, word[0])
            assert state not in words
            words[state] = word
        cylinder_nodes = {index[state] for state in words}
        assert kernel == cylinder_nodes

        state_payload = [
            {"residue": state[0], "digit": state[1], "word": "".join(map(str, word))}
            for state, word in sorted(words.items())]
        edge_payload = []
        for state, word in sorted(words.items()):
            source = index[state]
            for appended in (0, 1):
                ext = word + (appended,)
                ext_residue = direct_residue(ext)
                high = (ext_residue - state[0]) // (64**d)
                suffix = word[1:] + (appended,)
                target_state = (direct_residue(suffix), suffix[0])
                target = index[target_state]
                assert target in adjacency[source]
                assert high in labels[source][target]
                edge_payload.append({"word": "".join(map(str, word)),
                    "appended": appended, "high_block": high,
                    "target": "".join(map(str, suffix))})

        ghosts = set()
        modulus = 64**d
        for period in itertools.product((0, 1), repeat=d + 1):
            B = periodic_completion(period)
            ghosts.add((B.numerator * pow(B.denominator, -1, modulus) % modulus, period[0]))
        assert ghosts == set(words)

        actual_rows.append({
            "precision": d,
            "ambient_safe_states": len(states),
            "ambient_edges": sum(len(x) for x in labels),
            "scc_count": 1 + len(states) - len(kernel),
            "kernel_states": len(kernel),
            "kernel_state_digest": digest(state_payload),
            "de_bruijn_edges": len(edge_payload),
            "de_bruijn_edge_digest": digest(edge_payload),
            "periodic_ghost_states": len(ghosts)})
    assert actual_rows == expected_rows


def verify_carry(expected):
    initial_max = max((17 * a + offset) // 64
                      for offset in (0, 19, 62) for a in range(64))
    transition_max = max((17 * a + previous + carry) // 64
                         for a, previous, carry in itertools.product(range(64), range(64), range(18)))
    assert initial_max <= 17 and transition_max == 17
    cases = 0
    for offset in (0, 19, 62):
        for q in range(100_000):
            target = 81 * q + offset
            digits = []
            n = q
            while n:
                digits.append(n % 64)
                n //= 64
            digits = digits or [0]
            out = []
            previous = 0
            carry = offset
            for j in range(len(digits) + 3):
                a = digits[j] if j < len(digits) else 0
                raw = 17 * a + previous + carry
                out.append(raw % 64)
                carry = raw // 64
                previous = a
            assert sum(a * 64**j for j, a in enumerate(out)) == target
            cases += 1
    assert cases == expected["exact_digit_cases"]
    assert transition_max == expected["post_first_column_max_carry"]


def verify_scalable(expected):
    for d in range(1, expected["precision"] + 1):
        states = set()
        for word in itertools.product((0, 1), repeat=d + 1):
            state = (direct_residue(word), word[0])
            assert state not in states
            states.add(state)
    assert len(states) == expected["cylinder_states"]
    assert 2 * len(states) == expected["de_bruijn_edges"]


def verify_periodic(expected_total, expected_nonconstant):
    total = nonconstant = 0
    for p in range(1, 16):
        for period in itertools.product((0, 1), repeat=p):
            B = periodic_completion(period)
            total += 1
            if len(set(period)) == 1:
                assert B == 0
            else:
                assert B.denominator != 1
                nonconstant += 1
    assert total == expected_total and nonconstant == expected_nonconstant


def verify_monotonicity_and_scan(expected_invariant, expected_scan):
    checked = 0
    classes = set()
    for B in range(expected_invariant["search_limit"] + 1):
        for e in (0, 1):
            nxt = step(B, e)
            if nxt is None:
                continue
            Bp, ep = nxt
            assert (Bp + 4 * ep) % 17 == (B + 4 * e) % 17
            if B:
                assert Bp > B
            classes.add((B + 4 * e) % 17)
            checked += 1
    assert checked == expected_invariant["exact_steps"]
    assert sorted(classes) == expected_invariant["observed_invariant_classes"]

    best = -1
    witness = None
    histogram = {}
    for B in range(1, expected_scan["limit"] + 1):
        for e in (0, 1):
            x, bit, depth = B, e, 0
            while depth < 256:
                nxt = step(x, bit)
                if nxt is None:
                    break
                x, bit = nxt
                depth += 1
            histogram[str(depth)] = histogram.get(str(depth), 0) + 1
            if depth > best:
                best = depth
                witness = [B, e, x, bit]
    assert best == expected_scan["best_survival"]
    assert witness == expected_scan["best_witness"]
    assert histogram == expected_scan["histogram"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text())
    verify_graph_rows(certificate["pdr"]["fixed_precision_graphs"])
    verify_scalable(certificate["pdr"]["scalable_last"])
    verify_periodic(certificate["pdr"]["periodic_controls_checked"],
                    certificate["pdr"]["nonconstant_periodic_ghosts"])
    verify_carry(certificate["pdr"]["carry_transducer"])
    verify_monotonicity_and_scan(certificate["monotonicity_and_mod17"],
                                 certificate["finite_seed_scan"])
    check = dict(certificate)
    recorded = check.pop("semantic_digest")
    assert digest(check) == recorded
    print("all independent X-8701 certificate checks passed")
    print(json.dumps({"python": platform.python_version(), "platform": platform.platform()}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
