#!/usr/bin/env python3
"""Independent exact replay for CERTIFICATE_CARRY.md; no conjectural claims."""

import json


def valuation2(n):
    if n <= 0:
        raise ValueError("valuation requires a positive integer")
    return (n & -n).bit_length() - 1


def oddpart(n):
    return n >> valuation2(n)


def odd_step(n):
    if n <= 0 or not n & 1:
        raise ValueError("positive odd source required")
    return oddpart(3 * n + 1)


def iterate(n, clocks):
    for _ in range(clocks):
        n = odd_step(n)
    return n


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate_certificate(n, gaps):
    """Check a supplied finite valuation word, with no convergence search."""
    if not isinstance(n, int) or n <= 0 or not n & 1:
        raise ValueError("source must be a positive odd integer")
    values = [n]
    for a in gaps:
        if not isinstance(a, int) or a < 1:
            raise ValueError("certificate gaps must be positive integers")
        if valuation2(3 * n + 1) != a:
            raise ValueError("supplied valuation differs from the actual source")
        n = (3 * n + 1) >> a
        values.append(n)
    if n != 1:
        raise ValueError("supplied finite word does not end at 1")
    return values


def replay_edge(edge):
    for key in ("from", "to"):
        if not isinstance(edge[key], int) or edge[key] <= 0 or not edge[key] & 1:
            raise ValueError("meeting endpoints must be positive odd integers")
    for key in ("left_clock", "right_clock"):
        if not isinstance(edge[key], int) or edge[key] < 0:
            raise ValueError("meeting clocks must be nonnegative integers")
    common = iterate(edge["from"], edge["left_clock"])
    require(common == iterate(edge["to"], edge["right_clock"]),
            "ordinary meeting edge failed")
    if "common" in edge:
        require(edge["common"] == common, "declared meeting value failed")
    return common


def transform(n, gaps, initial_state=1):
    """Compile supplied source certificates; every accepted output is replayable."""
    gaps = list(gaps)
    values = validate_certificate(n, gaps)
    if initial_state not in (1, 2):
        raise ValueError("the proved finite subgrammar has only states 1 and 2")
    i, state, trace, edges = 0, initial_state, [], []
    target = (1 << state) * n - 1
    terminal = None

    def add_edge(event, destination, left, right):
        edge = {"rule": event["rule"],
                "from": (1 << event["state"]) * event["source"] - 1,
                "to": destination,
                "left_clock": left, "right_clock": right}
        edge["common"] = replay_edge(edge)
        edges.append(edge)
        event["edge_index"] = len(edges) - 1

    while i < len(gaps):
        a = gaps[i]
        b = gaps[i + 1] if i + 1 < len(gaps) else None
        event = {"source": values[i], "state": state, "gap": a}
        if a in (2, 3):
            event["rule"] = "single_gap"
            destination = (1 << (a - 1)) * values[i + 1] - 1
            add_edge(event, destination, 1 if state == 1 else a,
                     0 if state == 1 else a - 1)
            state, i = a - 1, i + 1
        elif state == 1 and a == 1 and b == 1:
            event["rule"] = "delete_one_before_one"
            add_edge(event, 2 * values[i + 1] - 1, 2, 1)
            i += 1
        elif state == 1 and a == 1 and b is not None and b >= 3:
            event["rule"] = "absorbed_into_certified_suffix"
            event["suffix"] = values[i + 2]
            add_edge(event, values[i + 2], 2, 0)
            trace.append(event)
            terminal = {"value": values[i + 2],
                        "hitting_clock": len(gaps) - (i + 2),
                        "valuation_word": gaps[i + 2:],
                        "kind": "supplied_source_suffix"}
            break
        elif state == 2 and a == 1 and b in (3, 4):
            event["rule"] = "two_gap"
            add_edge(event, (1 << (b - 2)) * values[i + 2] - 1, b, b - 2)
            state, i = b - 2, i + 2
        else:
            event["rule"] = "unhandled_carry"
            event["next_gap"] = b
            if a >= 4:
                z = values[i + 1]
                destination = (1 << (a - 1)) * z - 1
                add_edge(event, destination, 1 if state == 1 else a,
                         0 if state == 1 else a - 1)
                residual = {"kind": "R", "power": a - 1,
                            "source_suffix": z, "value": destination}
                consumed = 1
            elif state == 1 and a == 1 and b == 2:
                w = values[i + 2]
                destination = oddpart((w - 1) // 3)
                add_edge(event, destination, 1, 0)
                residual = {"kind": "B", "ternary_denominator_power": 1,
                            "source_suffix": w, "value": destination}
                consumed = 2
            elif state == 2 and a == 1 and b in (1, 2):
                w = values[i + 2]
                destination = (1 << b) * w - 3
                add_edge(event, destination, 2, 0)
                residual = {"kind": "affine", "binary_exponent": b,
                            "offset": 3, "source_suffix": w,
                            "value": destination}
                consumed = 2
            elif state == 2 and a == 1 and b is not None and b >= 5:
                w = values[i + 2]
                destination = (1 << (b - 2)) * w - 1
                add_edge(event, destination, b, b - 2)
                residual = {"kind": "R", "power": b - 2,
                            "source_suffix": w, "value": destination}
                consumed = 2
            else:
                raise RuntimeError("validated source reached an unclassified branch")
            trace.append(event)
            return {"accepted": False, "source": n, "target": target,
                    "source_valuation_word": gaps, "trace": trace,
                    "meeting_edges": edges,
                    "unhandled_residual": residual,
                    "remaining_source_valuation_word": gaps[i + consumed:]}
        trace.append(event)
    if terminal is None:
        require(values[i] == 1, "parser exhausted away from terminal certificate")
        terminal = {"value": (1 << state) - 1,
                    "hitting_clock": 0 if state == 1 else 2,
                    "valuation_word": [] if state == 1 else [1, 4],
                    "kind": "proved_root_state"}
    validate_certificate(terminal["value"], terminal["valuation_word"])

    # U(1)=1. If U^L(p)=U^R(q) and U^D(q)=1, then
    # U^(L+max(D-R,0))(p)=1. This compiles proof clocks without target search.
    duration = terminal["hitting_clock"]
    continuation = terminal["value"]
    for edge in reversed(edges):
        require(edge["to"] == continuation, "proof edges do not compose")
        edge["known_right_hitting_clock"] = duration
        duration = edge["left_clock"] + max(duration - edge["right_clock"], 0)
        edge["compiled_left_hitting_clock"] = duration
        continuation = edge["from"]
    require(continuation == target, "compiled proof does not start at target")

    # Extract exactly the compiled number of steps, then independently validate
    # the resulting finite target certificate. This has no search ceiling or
    # assumption that an unknown target eventually reaches 1.
    target_word, current = [], target
    for _ in range(duration):
        target_word.append(valuation2(3 * current + 1))
        current = odd_step(current)
    validate_certificate(target, target_word)
    return {"accepted": True, "source": n, "target": target,
            "source_valuation_word": gaps, "trace": trace,
            "meeting_edges": edges, "terminal": terminal,
            "compiled_target_hitting_clock": duration,
            "compiled_target_valuation_word": target_word}


def check():
    counts = {"odd_sources": 0, "general_carry": 0, "A_11": 0,
              "A_1b_absorption": 0, "B_1b": 0, "A_12": 0}
    for x in range(1, 20000, 2):
        counts["odd_sources"] += 1
        a = valuation2(3 * x + 1)
        z = odd_step(x)
        for k in range(1, 10):
            require(iterate((1 << k) * x - 1, k) == oddpart(3**k * x - 1),
                    "universal carry identity")
            require(oddpart(3**k * x - 1)
                    == oddpart((1 << a) * 3**(k - 1) * z - (3**(k - 1) + 1)),
                    "source-consumption identity")
            counts["general_carry"] += 1
        if a >= 2:
            target = (1 << (a - 1)) * z - 1
            require(odd_step(2 * x - 1) == target, "R1 source gap")
            common = oddpart(9 * x - 1)
            require(iterate(2 * x - 1, 2) == common
                    == iterate(4 * x - 1, 2), "two-state merger")
            require(iterate(4 * x - 1, a) == iterate(target, a - 1),
                    "two-state explicit clocks")
        else:
            b = valuation2(3 * z + 1)
            w = odd_step(z)
            require(odd_step(2 * x - 1) == oddpart(z - 1), "gap-one carry")
            if b == 1:
                require(iterate(2 * x - 1, 2) == odd_step(2 * z - 1),
                        "one-one deletion")
                counts["A_11"] += 1
            elif b == 2:
                require((w - 1) % 3 == 0, "ternary carry integrality")
                require(odd_step(2 * x - 1) == oddpart((w - 1) // 3),
                        "one-two retained carry")
                counts["A_12"] += 1
            else:
                require(iterate(2 * x - 1, 2) == w, "A absorption")
                counts["A_1b_absorption"] += 1
                target = (1 << (b - 2)) * w - 1
                require(iterate(4 * x - 1, b) == iterate(target, b - 2),
                        "B two-gap explicit clocks")
                counts["B_1b"] += 1

    family = []
    for r in range(1, 50):
        h = 6 * r + 1
        x = ((1 << (h + 3)) - 7) // 9
        y = 2 * x - 1
        require(x % 16 == 1, "boundary residue")
        require(valuation2(3 * x + 1) == 2 and iterate(x, 2) == 1,
                "exact depth-two certificate")
        require(valuation2(3 * odd_step(x) + 1) == h + 1, "terminal gap")
        m = (1 << h) - 1
        require(iterate(y, 2) == m, "Mersenne residual")
        for j in range(h):
            require(iterate(m, j) == 3**j * (1 << (h - j)) - 1,
                    "Mersenne excursion")
        require(iterate(m, h) == (3**h - 1) // 2, "Mersenne endpoint")
        require(not transform(x, [2, h + 1])["accepted"],
                "hard branch must remain unresolved")
        if r <= 3:
            family.append({"r": r, "source": x, "companion": y,
                           "known_valuation_word": [2, h + 1],
                           "Mersenne": m,
                           "forced_peak": 2 * 3**(h - 1) - 1})

    # Independent enumeration confirms the exhaustive formula at a finite range;
    # the unbounded classification is the elementary proof in the note.
    actual_depth_two = []
    for x in range(17, 1000000, 16):
        if iterate(x, 2) == 1 and odd_step(x) != 1:
            actual_depth_two.append(x)
    predicted_depth_two = [((1 << (6 * r + 4)) - 7) // 9 for r in range(1, 10)
                           if ((1 << (6 * r + 4)) - 7) // 9 < 1000000]
    require(actual_depth_two == predicted_depth_two, "depth-two exhaustive replay")

    for h in range(2, 202, 2):
        common = oddpart(3**h - 1)
        require(iterate((1 << h) - 1, h) == common
                == iterate((1 << (h - 1)) - 1, h),
                "even terminal exponent reduction")

    supplied_fixtures = {1: [], 3: [1, 4], 15: [1, 1, 1, 5, 4],
                         17: [2, 3, 4], 33: [2, 2, 1, 3, 1, 2, 3, 4],
                         113: [2, 8], 7281: [2, 14]}
    examples = {str(x): transform(x, gaps) for x, gaps in supplied_fixtures.items()}
    examples["R2(3)"] = transform(3, supplied_fixtures[3], initial_state=2)
    examples["R2(33)"] = transform(33, supplied_fixtures[33], initial_state=2)
    for bad_source, bad_word in [(0, []), (2, [1]), (3, [2, 4]),
                                  (3, [1]), (3, [1, 0, 4])]:
        try:
            transform(bad_source, bad_word)
        except ValueError:
            pass
        else:
            raise RuntimeError("corrupted source certificate was accepted")
    corrupted = dict(examples["33"]["meeting_edges"][0])
    corrupted["left_clock"] += 1
    try:
        replay_edge(corrupted)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("corrupted meeting edge was accepted")
    for changed in ({"left_clock": -1}, {"to": 2}, {"common": 0}):
        corrupted = dict(examples["33"]["meeting_edges"][0])
        corrupted.update(changed)
        try:
            replay_edge(corrupted)
        except (ValueError, RuntimeError):
            pass
        else:
            raise RuntimeError("malformed meeting edge was accepted")
    return {"status": "exact replay passed; global transfer remains unproved",
            "counts": counts, "depth_two_below_one_million": actual_depth_two,
            "family": family, "grammar_examples": examples}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
