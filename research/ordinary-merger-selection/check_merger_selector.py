#!/usr/bin/env python3
"""Exact certificate compiler and bounded checks. No universal cover claimed."""

from dataclasses import dataclass
import argparse
from itertools import product
import json
from pathlib import Path

if not __debug__:
    raise RuntimeError("Run this exact checker with Python assertions enabled")

M = 2**37
R = 84997906089
A = 1577799630949
C = 523998152183
U = "1011111111011011110101111011100001100"
V = "1101101101011011100110110110110101101"


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def iterate(n, h):
    assert type(n) is int and n > 0
    assert type(h) is int and h >= 0
    for _ in range(h):
        n = step(n)
    return n


def affine(word):
    odds = offset = 0
    for i, bit in enumerate(word):
        if bit == "1":
            odds += 1
            offset = 3 * offset + 2**i
    return odds, offset


def replay_word(n, word):
    for bit in word:
        assert n % 2 == int(bit), (n, word)
        n = step(n)
    return n


def valuation(n, prime):
    count = 0
    while n % prime == 0:
        count += 1
        n //= prime
    return count


@dataclass(frozen=True)
class Meeting:
    left_clock: int
    right_clock: int
    endpoint: int


def verify_meeting(t, cert):
    assert type(t) is int and t > 0
    assert isinstance(cert, Meeting)
    assert type(cert.left_clock) is int and cert.left_clock >= 0
    assert type(cert.right_clock) is int and cert.right_clock >= 0
    assert type(cert.endpoint) is int and cert.endpoint > 0
    assert iterate(t, cert.left_clock) == cert.endpoint
    assert iterate(5 * t + 1, cert.right_clock) == cert.endpoint


def symbolic_terminal(t):
    q = 3 * t + 1
    if q & (q - 1):
        return None
    e = q.bit_length() - 1
    if e < 2 or e % 2:
        return None
    return Meeting(e + 4, e + 4, 1)


def selector(t, supplied_terminals=None):
    """Return a checked finite certificate, or the exact unresolved residual.

    Optional supplied terminals are individually verified ordinary meetings.
    They are not an assertion about any unlisted source.
    """
    assert type(t) is int and t > 0
    terminals = supplied_terminals or {}
    original, x, frames = t, t, []
    while True:
        cert = symbolic_terminal(x)
        if cert is None and x in terminals:
            cert = terminals[x]
            verify_meeting(x, cert)
        if cert is not None:
            break
        if x % 64 == 11:
            y, kind = (27 * x + 23) // 64, "six_11"
        elif x % 64 == 35:
            y, kind = (9 * x + 5) // 64, "six_35"
        elif x % 4 == 0 and (x // 4) % M == R:
            y, kind = 3 * (x // 4), "bridge_37"
        else:
            return {"status": "UNRESOLVED", "input": original,
                    "residual": x, "reductions": frames}
        assert 1 <= y < x
        frames.append((kind, x, y))
        x = y
    for kind, before, after in reversed(frames):
        if kind.startswith("six"):
            cert = Meeting(cert.left_clock + 6, cert.right_clock + 6,
                           cert.endpoint)
        else:
            cert = Meeting(cert.left_clock + 39, cert.right_clock + 39,
                           iterate(cert.endpoint, 37))
        verify_meeting(before, cert)
    verify_meeting(original, cert)
    return {"status": "CERTIFIED", "input": original,
            "left_clock": cert.left_clock, "right_clock": cert.right_clock,
            "endpoint": cert.endpoint, "reductions": frames}


def finite_meeting(t, cap=10000):
    """A bounded actual orbit calculation; failure is not extrapolated."""
    seen = {}
    n = t
    for a in range(cap + 1):
        if n in seen:
            break
        seen[n] = a
        n = step(n)
    n, right_seen = 5 * t + 1, set()
    for b in range(cap + 1):
        if n in seen:
            cert = Meeting(seen[n], b, n)
            verify_meeting(t, cert)
            return cert
        if n in right_seen:
            break
        right_seen.add(n)
        n = step(n)
    return None


def compile_guard_word(word, terminal_periods=0):
    """Realize any nonempty finite guard word with a terminal at its end.

    The finite search for the first exponent terminates because 4 generates
    the units congruent to 1 modulo 3. Its running time is not claimed small.
    Increasing terminal_periods gives infinitely many realizations.
    """
    assert word and all(type(r) is int and r in (11, 35) for r in word)
    assert type(terminal_periods) is int and terminal_periods >= 0
    e, B = 0, 0
    for j, residue in enumerate(word):
        a, b, odds = (27, 23, 3) if residue == 11 else (9, 5, 2)
        B = a * B + b * 64**j
        e += odds
    k, period = len(word), 3**e
    modulus = 3 * period
    target = (1 + 3 * B * pow(64**k, -1, modulus)) % modulus
    first_m = next(m for m in range(1, period + 1)
                   if pow(4, m, modulus) == target)
    m = first_m + terminal_periods * period
    s = (4**m - 1) // 3
    assert (64**k * s - B) % (3**e) == 0
    t = (64**k * s - B) // (3**e)
    assert 0 < B < 64**k - 3**e and t > s >= 1
    return t, s, m, Meeting(6 * k + 2 * m + 4,
                            6 * k + 2 * m + 4, 1)


def check_three_ray():
    assert len(U) == len(V) == 37
    assert affine(U) == (25, A)
    assert affine(V) == (24, A)
    assert (3**25 * R + A) // M == C
    assert (3**25 * R + A) % M == 0
    b = 0
    for i, bit in enumerate(V, 1):
        b += int(bit)
        assert 3**b > 2**i, (i, b)
    basic = 0
    for t in (0, 1, 2, 17, 100, 2**20 - 1, 2**40 + 1):
        m = R + M * t
        assert replay_word(m, U) == replay_word(3 * m, V) == C + 3**25 * t
        basic += 1
    horizons = 0
    for L in (0, 1, 2, 10, 50, 120):
        binary_mod = 2**L
        binary_t = ((-1 - C) * pow(3**25, -1, binary_mod)) % binary_mod
        for a in (1, 2, 5, 12, 30):
            ternary_mod = 3**a
            ternary_t = ((3**(a - 1) - R) * pow(M, -1, ternary_mod)) % ternary_mod
            t = binary_t + binary_mod * (
                (ternary_t - binary_t) * pow(binary_mod, -1, ternary_mod)
                % ternary_mod)
            m, n = R + M * t, 3 * (R + M * t)
            assert valuation(n, 3) == a
            assert replay_word(m, U) == replay_word(n, V)
            x = n
            for h in range(1, 38 + L):
                x = step(x)
                assert x > n, (a, L, h)
            horizons += 1
    return {"offset_identities": 2, "noncontracting_prefixes": 37,
            "ordinary_lift_pairs": basic,
            "CRT_resistance_fixtures": horizons, "extra_horizon_max": 120,
            "exact_ternary_valuation_max": 30}


def check_six_step_guards():
    rules = [(11, 27, 23, "110100", "000111", 152),
             (35, 9, 5, "110000", "000011", 80)]
    checked = 0
    for residue, slope, offset, left, right, right_offset in rules:
        a, A_left = affine(left)
        b, A_right = affine(right)
        assert a == b and 3**a == slope
        assert A_left == offset and A_right == right_offset
        for q in range(129):
            t = residue + 64 * q
            s = (slope * t + offset) // 64
            assert 1 <= s < t
            assert replay_word(t, left) == s
            assert replay_word(5 * t + 1, right) == 5 * s + 1
            checked += 1
    return checked


def check_runs_and_terminals():
    run_checks = 0
    for k in range(1, 9):
        modulus = 64**k
        least = pow(11, -1, modulus)
        for q in range(3):
            t = least + modulus * q
            x = t
            for _ in range(k):
                assert x % 64 == 35
                y = (9 * x + 5) // 64
                assert 1 <= y < x
                assert iterate(x, 6) == y
                assert iterate(5 * x + 1, 6) == 5 * y + 1
                x = y
                run_checks += 1
    terminal_checks = 0
    for m in range(1, 21):
        t = (4**m - 1) // 3
        cert = symbolic_terminal(t)
        assert cert is not None
        verify_meeting(t, cert)
        terminal_checks += 1
    deep = []
    for k in range(1, 4):
        modulus = 3 ** (2 * k + 1)
        m = next(m for m in range(1, 3 ** (2 * k) + 1)
                 if (11 * pow(4, m, modulus) - 14) % modulus == 0)
        s = (4**m - 1) // 3
        z = (11 * s - 1) // (9**k)
        assert (11 * s - 1) % (9**k) == 0
        assert (64**k * z + 1) % 11 == 0
        t = (64**k * z + 1) // 11
        assert t > s and (11 * t - 1) % (64**k) == 0
        result = selector(t)
        assert result["status"] == "CERTIFIED"
        assert len(result["reductions"]) >= k
        deep.append({"guard_repetitions": k, "terminal_power_index": m,
                     "source_bits": t.bit_length(),
                     "certificate_clock": result["left_clock"]})
    return {"six_step_run_checks": run_checks,
            "symbolic_terminal_checks": terminal_checks,
            "successful_unbounded_family_fixtures": deep}


def check_bridge_composition():
    checked = []
    for q in range(3):
        u = R + M * q
        t, s = 4 * u, 3 * u
        assert iterate(5 * t + 1, 2) == 5 * s + 1
        assert iterate(t, 2) == u
        assert iterate(u, 37) == iterate(s, 37)
        terminal = finite_meeting(s)
        assert terminal is not None, ("bounded fixture unresolved", s)
        result = selector(t, {s: terminal})
        assert result["status"] == "CERTIFIED"
        assert result["reductions"][0][0] == "bridge_37"
        checked.append({"input": t, "smaller_parameter": s,
                        "left_clock": result["left_clock"],
                        "right_clock": result["right_clock"]})
    return checked


def check_mixed_guard_words():
    fixtures = []
    for k in (1, 2):
        source_classes = set()
        for word in product((11, 35), repeat=k):
            t, s, m, cert = compile_guard_word(word)
            x = t
            for residue in word:
                assert x % 64 == residue
                y = ((27 * x + 23) if residue == 11 else (9 * x + 5)) // 64
                assert 1 <= y < x
                assert iterate(x, 6) == y
                assert iterate(5 * x + 1, 6) == 5 * y + 1
                x = y
            assert x == s and symbolic_terminal(s) is not None
            verify_meeting(t, cert)
            assert selector(t)["status"] == "CERTIFIED"
            residue = t % (64**k)
            assert residue not in source_classes
            source_classes.add(residue)
            fixtures.append({"guard_word": word, "terminal_power_index": m,
                             "source_bits": t.bit_length(),
                             "source_residue": residue,
                             "certificate_clock": cert.left_clock})
    return fixtures


def check_invalid_certificates():
    # Negative clocks must not be mistaken for an empty iteration.
    mutations = [
        lambda: selector(2, {2: Meeting(-1, 9, 2)}),
        lambda: verify_meeting(2, Meeting(0, -1, 2)),
        lambda: verify_meeting(2, Meeting(0.0, 9, 2)),
        lambda: verify_meeting(2, Meeting(False, 9, 2)),
        lambda: verify_meeting(2, Meeting(0, 9, 0)),
        lambda: verify_meeting(2, Meeting(0, 9, 2.0)),
        lambda: selector(-2),
        lambda: selector(True),
    ]
    for mutation in mutations:
        try:
            mutation()
        except AssertionError:
            pass
        else:
            raise AssertionError("Malformed certificate or source was accepted")
    return len(mutations)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="Optional JSON receipt path; defaults to stdout")
    args = parser.parse_args()
    result = {"status": "PASS", "three_ray": check_three_ray(),
              "six_step_guard_instances": check_six_step_guards(),
              "runs_and_terminals": check_runs_and_terminals(),
              "bridge_compositions_with_individually_checked_terminals":
                  check_bridge_composition(),
              "mixed_guard_word_compiler_fixtures": check_mixed_guard_words(),
              "malformed_certificate_mutations_rejected":
                  check_invalid_certificates()}
    assert selector(1)["status"] == "CERTIFIED"
    hole = selector(2)
    assert hole["status"] == "UNRESOLVED" and hole["residual"] == 2
    assert finite_meeting(2) is not None
    result["smallest_symbolic_selector_hole"] = 2
    result["scope"] = ("Exact finite certificate checks. The selector terminates "
                       "but returns UNRESOLVED outside its proved guards and terminals. "
                       "No complete ordinary cover is asserted.")
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(payload, end="")
    else:
        args.output.write_text(payload)


if __name__ == "__main__":
    main()
