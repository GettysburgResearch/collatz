#!/usr/bin/env python3
"""Exact finite replay for Q_SECTION_GUARDS.md; no all-source termination claim."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path


class VerificationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def step(n: int) -> int:
    require(integer(n), "ordinary or signed source must be an integer")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def oddpart(n: int) -> int:
    require(integer(n) and n > 0, "oddpart needs a positive integer")
    while n % 2 == 0:
        n //= 2
    return n


@dataclass(frozen=True)
class State:
    s: int = 1
    d: int = -1
    h: int = 0
    ac: int = 1
    bc: int = 0
    r: int = 0
    word: str = ""
    swap: bool = False
    ax: int = 1
    bx: int = 0
    ay: int = 3
    by: int = -1


def extend(z: State, bit: int) -> State:
    require(integer(bit) and bit in (0, 1), "bit must be 0 or 1")
    require(z.s >= 0 and z.h >= 0, "negative state level or depth")
    require((z.ac * z.r + z.bc) % (1 << z.h) == 0, "invalid old cylinder")
    r = z.r + ((bit - ((z.ac * z.r + z.bc) >> z.h)) & 1) * (1 << z.h)
    require(0 <= r < (1 << (z.h + 1)), "noncanonical residue")
    px = ((z.ax * r + z.bx) >> z.h) & 1
    py = ((z.ay * r + z.by) >> z.h) & 1
    ax, bx = 3 ** px * z.ax, 3 ** px * z.bx + px * (1 << z.h)
    ay, by = 3 ** py * z.ay, 3 ** py * z.by + py * (1 << z.h)
    swap = z.swap
    if z.d % 2 == 0:
        s = z.s
        d = z.d // 2 if bit == 0 else (3 * z.d + 1 - 3 ** z.s) // 2
    elif z.s > 0:
        s = z.s + 1 if bit == 0 else z.s - 1
        d = (3 * z.d + 1) // 2 if bit == 0 else (z.d - 3 ** (z.s - 1)) // 2
    else:
        s = 1
        d = (3 * z.d + 1) // 2 if bit == 0 else (1 - 3 * z.d) // 2
        if bit:
            swap = not swap
    if bit == 0:
        ac, bc = z.ac, z.bc
    elif z.d % 2 and z.s == 0:
        ac, bc = z.ac, z.bc + z.d * (1 << z.h)
    else:
        ac, bc = 3 * z.ac, 3 * z.bc + (1 << z.h)
    h = z.h + 1
    require((ac, bc) == ((ay, by) if swap else (ax, bx)), "base orientation failed")
    other = (3 ** s * ac, 3 ** s * bc + d * (1 << h))
    require((ax, bx) == (other if swap else (ac, bc)), "physical X invariant failed")
    require((ay, by) == ((ac, bc) if swap else other), "physical Y invariant failed")
    return State(s, d, h, ac, bc, r, z.word + str(bit), swap, ax, bx, ay, by)


def word_states(word: str) -> list[State]:
    require(isinstance(word, str) and word and set(word) <= {"0", "1"}, "nonempty binary word required")
    states = [State()]
    for bit in word:
        states.append(extend(states[-1], int(bit)))
    return states


def verify_return(certificate: dict) -> State:
    require(isinstance(certificate, dict), "return certificate must be a mapping")
    for field in ("r", "modulus", "A", "C"):
        require(integer(certificate.get(field)), f"integer field required: {field}")
    require(certificate["A"] > 0 and certificate["C"] > 0, "positive affine slope and constant required")
    require(isinstance(certificate.get("swap"), bool), "orientation must be boolean")
    states = word_states(certificate.get("word"))
    z = states[-1]
    require((z.s, z.d) == (1, -1), "word does not return to Q section")
    require(certificate["modulus"] == 1 << z.h, "wrong source modulus")
    require(certificate["r"] == z.r, "wrong source residue")
    require((certificate["A"], certificate["C"], certificate["swap"]) == (z.ac, z.bc, z.swap), "wrong return map or orientation")
    if certificate.get("first", False):
        require(all((v.s, v.d) != (1, -1) for v in states[1:-1]), "claimed first return has an earlier return")
    return z


RETURNS = [
    dict(word="10", r=1, modulus=4, A=3, C=1, swap=False, first=True),
    dict(word="010", r=2, modulus=8, A=3, C=2, swap=False, first=True),
    dict(word="01100", r=6, modulus=32, A=9, C=10, swap=False, first=True),
    dict(word="001100", r=12, modulus=64, A=9, C=20, swap=False, first=True),
    dict(word="110001", r=11, modulus=64, A=9, C=29, swap=True, first=True),
    dict(word="01111011011101110", r=121310, modulus=131072, A=177147, C=469334, swap=True, first=True),
    dict(word="0111101101110111010", r=121310, modulus=524288, A=531441, C=1539074, swap=True, first=False),
]


def replay_word(z: State, a: int) -> int:
    require(integer(a) and a > 0 and a % (1 << z.h) == z.r, "source outside positive cylinder")
    x, y = a, 3 * a - 1
    v = State()
    edges = 0
    for bit in z.word:
        base = y if v.swap else x
        require(base % 2 == int(bit), "canonical word not physically legal")
        x, y = step(x), step(y)
        v = extend(v, int(bit))
        require(x * (1 << v.h) == v.ax * a + v.bx, "X affine replay failed")
        require(y * (1 << v.h) == v.ay * a + v.by, "Y affine replay failed")
        edges += 2
    base = y if z.swap else x
    other = x if z.swap else y
    require(other == 3 * base - 1, "literal endpoint not a Q pair")
    require(base * (1 << z.h) == z.ac * a + z.bc, "literal return formula failed")
    return edges


def horizon_formula(H: int, t: int) -> tuple[list[int], list[int]]:
    require(integer(H) and H >= 3, "H must be an integer at least 3")
    require(integer(t) and t >= 1, "t must be a positive integer")
    N = (1 << H) * t
    xs = [N - 2] + [3 ** (i - 1) * (1 << (H - i)) * t - 1 for i in range(1, H + 1)]
    ys = []
    for j in range(H + 1):
        r, c = divmod(j, 3)
        exponent = 2 * r + (1 if c == 0 else 2)
        ys.append(3 ** exponent * (1 << (H - j)) * t - (7, 10, 5)[c])
    return xs, ys


def signed_expected(h: int) -> tuple[int, int, bool]:
    prefix = [(1, -1), (2, -1), (1, -2), (1, -4), (1, -7), (0, -4), (0, -6), (0, -9)]
    if h < 8:
        return *prefix[h], False
    r, c = divmod(h - 8, 3)
    s = r + 1
    return s, (5, 7, 10)[c] * 3 ** s - 1, True


def run() -> dict:
    return_edges = 0
    for row in RETURNS:
        z = verify_return(row)
        for u in (0, 1, 2, 3, 17, 257, 65537):
            a = z.r + (1 << z.h) * u
            if a == 0:
                a += 1 << z.h
            return_edges += replay_word(z, a)
    # Guard corruption controls concern the mathematical artifact interface.
    rejected = []
    for name, changes in (
        ("empty word", {"word": ""}),
        ("wrong residue", {"r": 2}),
        ("zero slope", {"A": 0}),
        ("wrong offset", {"C": 2}),
        ("wrong orientation", {"swap": True}),
        ("boolean modulus", {"modulus": True}),
    ):
        corrupt = dict(RETURNS[0]); corrupt.update(changes)
        try:
            verify_return(corrupt)
        except VerificationError:
            rejected.append(name)
        else:
            raise VerificationError(f"corruption accepted: {name}")
    # New smaller-P implications are identities of literal ordinary endpoints.
    comparison_cases = 0
    for u in range(256):
        for n, small, word in ((25 + 64 * u, 7 + 18 * u, "01100"), (93 + 128 * u, 13 + 18 * u, "001100")):
            a = (3 * n + 1) // 2
            require(step(n) == a and step(3 * n) == 3 * a - 1, "P-to-Q conversion failed")
            z = word_states(word)[-1]
            b = (z.ac * a + z.bc) // (1 << z.h)
            require(2 * b - 1 == 3 * small and small < n, "smaller-P formula failed")
            return_edges += replay_word(z, a)
            comparison_cases += 1
    for u in range(256):
        a = 121310 + 131072 * u
        b = 163957 + 177147 * u
        require(a < b < 2 * a - 1, "orientation control failed")
        a = 121310 + 1048576 * u
        b = 122968 + 1062882 * u
        require(a % 2 == b % 2 == 0 and a < b < 2 * a - 1, "even scalar control failed")
    # Actual equality can occur at a nonabsorbed symbolic state.
    a, x, y, z = 4, 4, 11, State()
    isolated_states = []
    for h in range(13):
        if h:
            require((z.s, z.d) != (1, -1), "a=4 unexpectedly returned to section")
        if h == 10:
            require(x == y == 1 and (z.s, z.d) == (1, -2), "isolated equality control failed")
        isolated_states.append([h, x, y, z.s, z.d, z.swap])
        bit = (y if z.swap else x) % 2
        x, y, z = step(x), step(y), extend(z, bit)
    # The signed infinite code is used as a boundary control, never as a positive source.
    signed = State()
    for h in range(193):
        require((signed.s, signed.d, signed.swap) == signed_expected(h), "signed state formula failed")
        base = (signed.ac * -2 + signed.bc) // (1 << h)
        signed = extend(signed, base % 2)
    expected_code = "0" + "1" * 7 + "110" * 62
    require(signed.word == expected_code[:193], "signed canonical code failed")
    H_values = range(3, 193)
    t_values = (1, 2, 3, 4, 5, 17, 131073, 131074)
    cases = oddpart_cases = horizon_edges = meeting_pairs = 0
    for H in H_values:
        for t in t_values:
            xs, ys = horizon_formula(H, t)
            a, m = xs[0], 2 * xs[0] - 1
            z = State()
            for h in range(H + 1):
                require(ys[h] > m, "bad-arm floor inequality failed")
                require(xs[h] > 1, "good arm reached 1 inside claimed horizon")
                require((z.s, z.d, z.swap) == signed_expected(h), "positive cylinder state failed")
                if h:
                    require(ys[h] != 3 * xs[h] - 1 and xs[h] != 3 * ys[h] - 1, "specialized numerical Q section found")
                    require((z.s, z.d) not in ((1, -1), (0, 0)), "forbidden canonical terminal found")
                if h < H:
                    require(step(xs[h]) == xs[h + 1] and step(ys[h]) == ys[h + 1], "literal horizon step failed")
                    bit = (ys[h] if z.swap else xs[h]) % 2
                    z = extend(z, bit)
                    horizon_edges += 2
            require(set(xs).isdisjoint(ys), "independent-clock meeting found")
            meeting_pairs += (H + 1) ** 2
            endpoint_parity = (t % 2 == 1) if H % 3 == 1 else (t % 2 == 0)
            if endpoint_parity:
                require(ys[-1] % 2 == 1, "endpoint oddness condition failed")
                require(all(oddpart(y) > m for y in ys), "odd-part guard escaped floor")
                oddpart_cases += 1
            cases += 1
    return {
        "status": "PASS",
        "scope": "Finite exact replay of QG1-QG4 interfaces and examples; the all-H theorem rests on the written proof; no Collatz proof or universal guard termination claim.",
        "return_certificates": len(RETURNS),
        "literal_return_edges": return_edges,
        "smaller_tripling_cases": comparison_cases,
        "orientation_control_cases": 512,
        "rejected_corruptions": rejected,
        "horizon_min": 3,
        "horizon_max": 192,
        "t_values": list(t_values),
        "horizon_cases": cases,
        "horizon_literal_edges": horizon_edges,
        "independent_clock_pairs_excluded_in_finite_replay": meeting_pairs,
        "oddpart_guard_cases": oddpart_cases,
        "signed_states_checked": 193,
        "isolated_positive_meeting_trace": isolated_states,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    body = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(body, encoding="utf-8")
    print(body, end="")


if __name__ == "__main__":
    main()
