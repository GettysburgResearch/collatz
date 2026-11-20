#!/usr/bin/env python3
"""Exact bounded replay and a partial, proof-producing five compiler.

The all-parameter proofs are in CARRY_COMPILER.md. No finite replay is a
universal Collatz proof. All checks use explicit exceptions, including under
python -O/-OO. The production compiler never searches for an unknown target
trajectory: valid unsupported source certificates return UNRESOLVED.
"""

from __future__ import annotations

from fractions import Fraction
import json


ENTRY = (2, 1, 1, 1, 2, 1, 7)
TARGET_ENTRY = (3, 6, 1, 2, 1, 1, 1)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def positive_integer(value: int) -> bool:
    return type(value) is int and value > 0


def valuation_two(value: int) -> int:
    require(positive_integer(value), "valuation needs a positive integer")
    return (value & -value).bit_length() - 1


def word_tuple(word) -> tuple[int, ...]:
    require(type(word) in (tuple, list), "word must be a tuple or list")
    require(all(positive_integer(a) for a in word), "invalid exponent")
    return tuple(word)


def run_odd(source: int, word, *, first_hit: bool = False) -> tuple[int, ...]:
    require(positive_integer(source) and source % 2 == 1,
            "source must be positive and odd")
    word = word_tuple(word)
    state = source
    states = [state]
    for exponent in word:
        if first_hit:
            require(state != 1, "certificate continues after its first hit")
        numerator = 3 * state + 1
        require(valuation_two(numerator) == exponent, "wrong exact valuation")
        state = numerator >> exponent
        require(state > 0 and state % 2 == 1, "nonordinary endpoint")
        states.append(state)
    return tuple(states)


def validate_certificate(source: int, word) -> tuple[int, ...]:
    word = word_tuple(word)
    states = run_odd(source, word, first_hit=True)
    require(states[-1] == 1, "certificate does not end at one")
    return word


def correction(word) -> tuple[int, int, int]:
    word = word_tuple(word)
    value = 0
    clock = 0
    for exponent in word:
        value = 3 * value + (1 << clock)
        clock += exponent
    return value, clock, len(word)


def inverse_word(word, endpoint: int) -> int:
    word = word_tuple(word)
    require(positive_integer(endpoint) and endpoint % 2 == 1,
            "inverse endpoint must be positive and odd")
    state = endpoint
    for exponent in reversed(word):
        numerator = (state << exponent) - 1
        require(numerator % 3 == 0, "nonintegral inverse")
        state = numerator // 3
        require(state > 0 and state % 2 == 1, "nonordinary inverse")
    require(run_odd(state, word)[-1] == endpoint, "inverse replay mismatch")
    return state


def source_for_word(word, lift: int = 0) -> tuple[int, int]:
    """Construct one ordinary fixture, not a search for target convergence."""
    c, clock, rank = correction(word)
    modulus = 3 ** rank
    endpoint = c * pow(pow(2, clock, modulus), -1, modulus) % modulus
    if endpoint % 2 == 0:
        endpoint += modulus
    require(endpoint > 0 and endpoint % 3 != 0, "bad endpoint residue")
    endpoint += 2 * modulus * lift
    return inverse_word(word, endpoint), endpoint


def short_words(b: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    require(positive_integer(b) and b >= 6, "short block requires b>=6")
    return (1, 1, 1, b), (1, 2, 5, b - 5)


def carry_words(r: int, b: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    require(type(r) is int and r >= 0, "run length must be nonnegative")
    require(positive_integer(b) and b >= 2, "carry exit requires b>=2")
    return ENTRY + (1,) * r + (3, b), TARGET_ENTRY + (1,) * r + (4, b - 1)


def two_words(r: int, b: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """PR166 FL1, imported for the explicitly mixed language."""
    require(positive_integer(r), "two-run length must be positive")
    require(positive_integer(b) and b >= 4, "two-run exit requires b>=4")
    target = (5, b - 3) if r == 1 else (4,) + (2,) * (r - 2) + (3, b - 3)
    return (2,) * r + (b,), target


def parse_blocks(word: tuple[int, ...]):
    """Return exact replacements or None; never guess an uncovered exit."""
    output = []
    blocks = []
    i = 0
    while i < len(word):
        if word[i:i + len(ENTRY)] == ENTRY:
            j = i + len(ENTRY)
            while j < len(word) and word[j] == 1:
                j += 1
            if j + 1 >= len(word) or word[j] != 3 or word[j + 1] < 2:
                return None
            r = j - i - len(ENTRY)
            b = word[j + 1]
            source, target = carry_words(r, b)
            kind = "carry_four"
        elif word[i:i + 3] == (1, 1, 1):
            if i + 3 >= len(word) or word[i + 3] < 6:
                return None
            b = word[i + 3]
            r = None
            source, target = short_words(b)
            kind = "three_ones"
        elif word[i] == 2:
            j = i
            while j < len(word) and word[j] == 2:
                j += 1
            if j == len(word) or word[j] < 4:
                return None
            r, b = j - i, word[j]
            source, target = two_words(r, b)
            kind = "pr166_two_run"
        else:
            return None
        require(word[i:i + len(source)] == source, "parser mismatch")
        output.extend(target)
        blocks.append({"kind": kind, "run": r, "last_exponent": b})
        i += len(source)
    return tuple(output), tuple(blocks)


def compile_five(source: int, word) -> dict:
    """Compile exactly the first-hit language D*, otherwise UNRESOLVED."""
    word = validate_certificate(source, word)
    parsed = parse_blocks(word)
    if parsed is None:
        return {"status": "UNRESOLVED", "reason": "valid certificate outside D*"}
    output, blocks = parsed
    output += (4,)
    validate_certificate(5 * source, output)
    require(len(output) == len(word) + 1, "odd-count bookkeeping failed")
    require(sum(output) == sum(word) + 4, "clock bookkeeping failed")
    return {"status": "COMPILED", "word": output, "blocks": blocks,
            "source_rank": len(word), "target_rank": len(output),
            "source_clock": sum(word), "target_clock": sum(output)}


def rank_family(r: int) -> tuple[int, tuple[int, ...], int, int]:
    require(type(r) is int and r >= 0, "rank parameter must be nonnegative")
    t = 88 * pow(pow(2, r, 243), -1, 243) % 243
    b = 2 * 3 ** (r + 4) * t - 2
    word, _ = carry_words(r, b)
    c = 1351 * 3 ** (r + 5) + (1 << (r + 16))
    numerator = (1 << (r + b + 18)) - c
    require(numerator % 3 ** (r + 9) == 0, "rank family not integral")
    source = numerator // 3 ** (r + 9)
    require(source % 3 == 1, "rank family not a ternary unit")
    validate_certificate(source, word)
    return source, word, t, b


def block_ending_at(kind: str, run: int, endpoint: int):
    """Make a bounded test fixture by exact modular selection of its last gap.

    This helper is not part of compile_five, and does not search the target
    orbit. A full period modulo the one extra ternary digit guarantees a
    source unit. The returned word is replayed independently.
    """
    if kind == "carry_four":
        make, minimum = lambda b: carry_words(run, b), 2
    elif kind == "three_ones":
        make, minimum = short_words, 6
    elif kind == "pr166_two_run":
        make, minimum = lambda b: two_words(run, b), 4
    else:
        raise ValueError("unknown fixture block")
    initial, _ = make(minimum)
    c, clock, rank = correction(initial)
    modulus = 3 ** rank
    larger = 3 * modulus
    residue = pow(2, clock, larger) * endpoint % larger
    for offset in range(2 * modulus):
        if (residue - c) % modulus == 0 and (residue - c) % larger != 0:
            word, _ = make(minimum + offset)
            source = inverse_word(word, endpoint)
            require(source % 3 != 0, "fixture source should be a unit")
            return source, word
        residue = 2 * residue % larger
    raise ValueError("full modular period failed to produce a fixture")


def expect_rejected(function, label: str) -> None:
    try:
        function()
    except (ValueError, TypeError):
        return
    raise ValueError("invalid input accepted: " + label)


def main() -> dict:
    report = {
        "schema": "collatz-carry-compiler-replay/v1",
        "scope": "exact finite replay; all-parameter proofs in CARRY_COMPILER.md; Collatz open",
        "arithmetic": "integers and Fractions; no assertion-dependent checks",
    }

    require(correction(ENTRY) == (3709, 15, 7), "entry correction")
    require(correction(TARGET_ENTRY) == (149617, 15, 7), "target entry correction")
    require(149617 - 5 * 3709 == 4 * 2 ** 15, "entry carry")
    base_states = run_odd(25065, ENTRY)
    target_states = run_odd(125325, TARGET_ENTRY)
    require(base_states[-1] == 1673 and target_states[-1] == 8369, "base endpoints")
    for lift in range(65):
        source = 25065 + 65536 * lift
        end = run_odd(source, ENTRY)[-1]
        target = run_odd(5 * source, TARGET_ENTRY)[-1]
        require(target == 5 * end + 4, "lifted entry carry")
    report["entry"] = {"ordinary_lifts": 65, "source_states": base_states,
                       "target_states": target_states}

    loop_cases = 0
    exit_cases = 0
    for z in range(3, 4096, 4):
        source_next = run_odd(z, (1,))[-1]
        target_next = run_odd(5 * z + 4, (1,))[-1]
        require(target_next == 5 * source_next + 4, "carry loop")
        loop_cases += 1
    for b in range(2, 20):
        for lift in (0, 1, 3):
            z, q = source_for_word((3, b), lift)
            require(run_odd(5 * z + 4, (4, b - 1))[-1] == 5 * q, "carry exit")
            exit_cases += 1
    report["carry_loop_and_exit"] = {"loop_inputs": loop_cases,
                                      "exit_instances": exit_cases}

    symbolic = 0
    ordinary = 0
    for r in range(65):
        for b in (2, 3, 4, r + 2, r + 5):
            source_word, target_word = carry_words(r, b)
            c, clock, rank = correction(source_word)
            tc, tclock, trank = correction(target_word)
            require(c == 1351 * 3 ** (r + 5) + (1 << (r + 16)), "closed correction")
            require(tc == 5 * c and tclock == clock and trank == rank, "balanced return")
            require(clock == r + b + 18 and rank == r + 9, "run resources")
            source_affine = (Fraction(3 ** rank, 2 ** clock), Fraction(c, 2 ** clock))
            target_affine = (Fraction(5 * 3 ** trank, 2 ** tclock), Fraction(tc, 2 ** tclock))
            require(target_affine == tuple(5 * v for v in source_affine), "affine equality")
            symbolic += 1
            if r <= 16:
                for lift in (0, 1, 3):
                    source, q = source_for_word(source_word, lift)
                    require(run_odd(5 * source, target_word)[-1] == 5 * q, "ordinary carry return")
                    ordinary += 1
    report["unbounded_ladder_finite_checks"] = {
        "symbolic_pairs": symbolic, "run_range": [0, 64],
        "ordinary_pairs": ordinary, "ordinary_run_range": [0, 16],
        "warning": "finite indices do not establish the universal run quantifier",
    }

    domain_checked = 0
    domain_members = 0
    for source in range(1, 8192, 2):
        state = source
        gaps = []
        for _ in range(4):
            exponent = valuation_two(3 * state + 1)
            gaps.append(exponent)
            state = (3 * state + 1) >> exponent
        belongs = tuple(gaps[:3]) == (1, 1, 1) and gaps[3] >= 6
        require(belongs == (source % 512 == 271), "short cylinder characterization")
        domain_checked += 1
        if belongs:
            _, target_word = short_words(gaps[3])
            require(run_odd(5 * source, target_word)[-1] == 5 * state, "short ordinary return")
            require(6 * state < source, "short block descent")
            domain_members += 1
    short_fibers = 0
    for b in range(6, 80):
        source_word, target_word = short_words(b)
        require(correction(source_word) == (65, b + 3, 4), "short source correction")
        require(correction(target_word) == (325, b + 3, 4), "short target correction")
        for lift in (0, 1, 3):
            source, q = source_for_word(source_word, lift)
            require(source % 512 == 271, "inverse fiber cylinder")
            require(run_odd(5 * source, target_word)[-1] == 5 * q, "inverse fiber target")
            short_fibers += 1
    report["three_ones_block"] = {"domain_inputs": domain_checked,
                                  "domain_members": domain_members,
                                  "inverse_fiber_instances": short_fibers}

    require(pow(4, 81, 3 ** 10) == (1 + 178 * 3 ** 5) % 3 ** 10,
            "base ternary congruence")
    require((178 * 88 * 2 ** 16 - 1351 - 81) % 243 == 0, "unit selection constant")
    for r in range(81):
        t = 88 * pow(pow(2, r, 243), -1, 243) % 243
        b = 2 * 3 ** (r + 4) * t - 2
        mod = 3 ** (r + 10)
        require(0 < t < 243 and t % 3 != 0, "nonunit t")
        require(pow(4, 3 ** (r + 4), mod) == (1 + 178 * 3 ** (r + 5)) % mod,
                "lifted ternary congruence")
        value = (pow(2, r + b + 18, mod) - 1351 * 3 ** (r + 5)
                 - pow(2, r + 16, mod)) % mod
        require(value == 3 ** (r + 9), "whole-rank unit congruence")
    family_rows = []
    for r in range(4):
        source, word, t, b = rank_family(r)
        result = compile_five(source, word)
        require(result["status"] == "COMPILED", "family compiler coverage")
        family_rows.append({"r": r, "t": t, "b": b, "source_bits": source.bit_length(),
                            "source_rank": len(word), "target_rank": result["target_rank"],
                            "source_clock": sum(word), "target_clock": result["target_clock"]})
    report["rank_family"] = {"modular_indices": [0, 80],
                             "ordinary_first_hit_instances": family_rows,
                             "large_integer_values_omitted": True}

    mixed_rows = []
    sequences = (
        (("three_ones", 0),),
        (("pr166_two_run", 2), ("three_ones", 0)),
        (("three_ones", 0), ("carry_four", 0), ("pr166_two_run", 1)),
        (("carry_four", 1), ("three_ones", 0), ("pr166_two_run", 3)),
    )
    for sequence in sequences:
        endpoint = 1
        word = ()
        for kind, run in reversed(sequence):
            endpoint, prefix = block_ending_at(kind, run, endpoint)
            word = prefix + word
        result = compile_five(endpoint, word)
        require(result["status"] == "COMPILED", "mixed compiler coverage")
        require([b["kind"] for b in result["blocks"]] == [k for k, _ in sequence],
                "mixed parser identity")
        mixed_rows.append({"blocks": [k for k, _ in sequence],
                           "source_bits": endpoint.bit_length(), "source_rank": len(word),
                           "target_rank": result["target_rank"],
                           "source_clock": sum(word), "target_clock": result["target_clock"]})
    empty = compile_five(1, ())
    require(empty["status"] == "COMPILED" and empty["word"] == (4,), "empty certificate")
    report["compiler"] = {"mixed_instances": mixed_rows, "empty_source_checked": True}

    malformed = (
        (0, ()), (-1, ()), (2, ()), (True, ()), (5, (0,)),
        (5, (-4,)), (5, (4.0,)), (5, (True,)), (5, (3,)),
        (5, ()), (1, (2,)), (5, (4, 2)), (5, "4"),
    )
    for source, word in malformed:
        expect_rejected(lambda s=source, w=word: compile_five(s, w), "source certificate")
    unresolved = ((3, (1, 4)), (5, (4,)), (17, (2, 3, 4)), (85, (8,)))
    for source, word in unresolved:
        require(compile_five(source, word)["status"] == "UNRESOLVED",
                "unsupported certificate treated as success")
    source, word, _, _ = rank_family(0)
    target_word = carry_words(0, word[-1])[1] + (4,)
    mutations = [target_word[:i] + (target_word[i] + 1,) + target_word[i + 1:]
                 for i in (0, 3, 6, len(target_word) - 1)]
    for mutation in mutations:
        expect_rejected(lambda w=mutation: validate_certificate(5 * source, w), "target mutation")
    expect_rejected(lambda: short_words(5), "invalid short-block guard")
    expect_rejected(lambda: carry_words(-1, 2), "negative loop length")
    expect_rejected(lambda: carry_words(0, 1), "invalid carry exit")
    report["controls"] = {"malformed_first_hit_certificates_rejected": len(malformed),
                           "valid_unsupported_certificates_unresolved": len(unresolved),
                           "target_word_mutations_rejected": len(mutations),
                           "invalid_block_parameters_rejected": 3}
    report["success"] = True
    return report


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
