#!/usr/bin/env python3
"""Exact, dependency-free certificates for the witness-closure experiment.

This module does not decide the full closure assertion.  ``transform`` returns
UNRESOLVED whenever its explicit certificates do not finish the construction.
Bounded trajectory searches are used only to construct self-test fixtures.
Running this file writes a concise JSON report to stdout and writes no files.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Optional


class WitnessError(ValueError):
    """An alleged positive-integer witness or certificate is invalid."""


class TrajectoryBoundExceeded(RuntimeError):
    """A bounded fixture search ended without a witness; no disproof follows."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise WitnessError(message)


def is_integer(value: object) -> bool:
    return type(value) is int


def v2(n: int) -> int:
    require(is_integer(n) and n > 0, "v2 requires a positive integer")
    return (n & -n).bit_length() - 1


def walk(start: int, increments: Iterable[int]) -> tuple[int, ...]:
    """Check exact odd steps, including exactness of every division."""
    require(is_integer(start) and start > 0 and start % 2 == 1,
            "trajectory start must be a positive odd integer")
    values = [start]
    for exponent in increments:
        require(is_integer(exponent) and exponent >= 1,
                "each exponent increment must be a positive integer")
        numerator = 3 * values[-1] + 1
        require(v2(numerator) == exponent, "increment is not the exact valuation")
        values.append(numerator >> exponent)
    return tuple(values)


@dataclass(frozen=True)
class Witness:
    """Validated witness in the question's cumulative-exponent notation."""

    x: int
    A: tuple[int, ...]

    def __post_init__(self) -> None:
        require(type(self.A) is tuple and len(self.A) >= 1,
                "A must be a nonempty tuple")
        require(all(is_integer(a) for a in self.A), "A entries must be integers")
        require(self.A[0] == 0, "A[0] must be zero")
        require(all(a < b for a, b in zip(self.A, self.A[1:])),
                "A must be strictly increasing")
        values = walk(self.x, self.increments)
        require(values[-1] == 1, "witness does not end at one")
        numerator = self.x
        for a in self.A[:-1]:
            numerator = 3 * numerator + (1 << a)
        require(numerator == 1 << self.A[-1], "closed witness identity fails")

    @property
    def increments(self) -> tuple[int, ...]:
        return tuple(b - a for a, b in zip(self.A, self.A[1:]))

    @property
    def length(self) -> int:
        return len(self.A) - 1

    @property
    def values(self) -> tuple[int, ...]:
        return walk(self.x, self.increments)

    @classmethod
    def from_increments(cls, x: int, increments: Iterable[int]) -> Witness:
        cumulative = [0]
        for exponent in increments:
            require(is_integer(exponent) and exponent >= 1,
                    "increment must be a positive integer")
            cumulative.append(cumulative[-1] + exponent)
        return cls(x, tuple(cumulative))

    @classmethod
    def from_trajectory(cls, x: int, max_steps: int = 10000) -> Witness:
        """Bounded fixture builder; not used by the transformation algorithm."""
        require(is_integer(max_steps) and max_steps >= 0,
                "max_steps must be a nonnegative integer")
        walk(x, ())
        current, increments = x, []
        for _ in range(max_steps):
            if current == 1:
                return cls.from_increments(x, increments)
            exponent = v2(3 * current + 1)
            increments.append(exponent)
            current = (3 * current + 1) >> exponent
        if current == 1:
            return cls.from_increments(x, increments)
        raise TrajectoryBoundExceeded("step bound reached; membership unresolved")

    def padded(self, minimum_length: int) -> Witness:
        require(is_integer(minimum_length) and minimum_length >= 0,
                "minimum length must be nonnegative")
        extra = max(0, minimum_length - self.length)
        return Witness.from_increments(self.x, self.increments + (2,) * extra)

    def tail(self, steps: int) -> Witness:
        require(is_integer(steps) and steps >= 0, "tail index must be nonnegative")
        padded = self.padded(steps)
        return Witness.from_increments(padded.values[steps], padded.increments[steps:])


def prepend(start: int, prefix: Iterable[int], tail: Witness) -> Witness:
    prefix = tuple(prefix)
    require(walk(start, prefix)[-1] == tail.x, "prefix does not reach tail start")
    return Witness.from_increments(start, prefix + tail.increments)


def jump(witness: Witness) -> Witness:
    """Transfer a witness for n to J(n)=4n+1, including n=1."""
    padded = witness.padded(1)
    increments = padded.increments
    return Witness.from_increments(4 * witness.x + 1,
                                   (increments[0] + 2,) + increments[1:])


def unjump(witness: Witness) -> Witness:
    """Transfer a witness for J(n) to positive odd n."""
    require(witness.x > 1 and (witness.x - 1) % 4 == 0, "start is not J(n)")
    n = (witness.x - 1) // 4
    require(n % 2 == 1 and witness.length >= 1, "J preimage must be positive odd")
    increments = witness.increments
    require(increments[0] >= 3, "J witness first increment is too small")
    return Witness.from_increments(n, (increments[0] - 2,) + increments[1:])


def splice(source: Witness, target_start: int, target_prefix: Iterable[int],
           source_steps: Optional[int] = None) -> Witness:
    """Pad at 1 if needed, check the actual merger, then copy the source tail."""
    target_prefix = tuple(target_prefix)
    if source_steps is None:
        source_steps = len(target_prefix)
    require(is_integer(source_steps) and source_steps >= 0,
            "source_steps must be nonnegative")
    padded = source.padded(source_steps)
    require(walk(target_start, target_prefix)[-1] == padded.values[source_steps],
            "the proposed prefixes do not merge")
    return Witness.from_increments(target_start,
                                   target_prefix + padded.increments[source_steps:])


@dataclass(frozen=True)
class Affine:
    """The exact polynomial a*t+b, with rational coefficients."""

    a: Fraction
    b: Fraction

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", Fraction(self.a))
        object.__setattr__(self, "b", Fraction(self.b))

    def at(self, t: int) -> Fraction:
        return self.a * t + self.b

    def step(self, exponent: int) -> Affine:
        return Affine(3 * self.a / (1 << exponent),
                      (3 * self.b + 1) / (1 << exponent))

    def positive_odd(self) -> bool:
        return (self.a.denominator == self.b.denominator == 1
                and self.a >= 0 and self.a.numerator % 2 == 0
                and self.b > 0 and self.b.numerator % 2 == 1)


def affine_walk(start: Affine, increments: Iterable[int]) -> Affine:
    """Prove each exact step for every integer t>=0, not by sampling t."""
    require(start.positive_odd(), "initial affine polynomial is not always positive odd")
    current = start
    for exponent in increments:
        require(is_integer(exponent) and exponent >= 1, "invalid symbolic exponent")
        current = current.step(exponent)
        require(current.positive_odd(), "symbolic quotient is not always positive odd")
    return current


@dataclass(frozen=True)
class MergerCertificate:
    name: str
    modulus: int
    residue: int
    source_prefix: tuple[int, ...]
    target_prefix: tuple[int, ...]

    def verify(self) -> Affine:
        require(self.modulus > 0 and 0 < self.residue < self.modulus,
                "invalid parameter cylinder")
        require(len(self.source_prefix) == len(self.target_prefix),
                "certificate prefixes have unequal lengths")
        source = affine_walk(Affine(128 * self.modulus, 128 * self.residue + 1),
                             self.source_prefix)
        target = affine_walk(Affine(64 * self.modulus, 64 * self.residue + 1),
                             self.target_prefix)
        require(target == Affine(4 * source.a, 4 * source.b + 1),
                "universal affine merger identity fails")
        return source

    def applies(self, m: int) -> bool:
        return m > 0 and m % self.modulus == self.residue

    def apply(self, source: Witness, m: int) -> Witness:
        require(self.applies(m) and source.x == 128 * m + 1,
                "source does not match certificate cylinder")
        q_polynomial = self.verify()
        q = q_polynomial.at((m - self.residue) // self.modulus)
        require(q.denominator == 1, "q is not integral")
        exponent = v2(3 * q.numerator + 1)
        source_word = self.source_prefix + (exponent,)
        padded = source.padded(len(source_word))
        require(padded.increments[:len(source_word)] == source_word,
                "source witness disagrees with certified exact prefix")
        return splice(padded, 64 * m + 1, self.target_prefix + (exponent + 2,))


FIXED_CERTIFICATES = (
    MergerCertificate("m=6 mod 16", 16, 6, (2, 2, 2, 4), (2, 2, 2, 1)),
    MergerCertificate("m=35 mod 128", 128, 35, (2, 2, 2, 1, 6),
                      (2, 2, 3, 2, 1)),
    MergerCertificate("m=401 mod 1024", 1024, 401, (2, 2, 2, 1, 1, 8),
                      (2, 2, 4, 1, 3, 1)),
)


def infinite_certificate(k: int) -> MergerCertificate:
    """27m+2 == 3^k*2^(k+2) mod 2^(k+4), for any integer k>=1."""
    require(is_integer(k) and k >= 1, "family index must be positive")
    modulus = 1 << (k + 4)
    residue = ((pow(3, k, 4) * (1 << (k + 2)) - 2)
               * pow(27, -1, modulus)) % modulus
    return MergerCertificate(
        "infinite k family, k=" + str(k), modulus, residue,
        (2, 2, 2, 3) + (1,) * (k - 1) + (2,),
        (2, 2, 2, 1) + (1,) * k,
    )


def choose_certificate(m: int) -> Optional[MergerCertificate]:
    for certificate in FIXED_CERTIFICATES:
        if certificate.applies(m):
            return certificate
    if m > 0 and m % 8 == 2:
        k = v2(27 * m + 2) - 2
        if k >= 1:
            certificate = infinite_certificate(k)
            if certificate.applies(m):
                return certificate
    return None


def verify_merger_schema() -> None:
    """Exact polynomial induction identities underlying all k, not a k sample."""
    # (3(2z-1)+1)/2 = 3z-1: the repeated exponent-one transition.
    require(Affine(2, -1).step(1) == Affine(3, -1), "induction step fails")
    # With z=3^k*w, the critical source state is 2z/3-1.
    q = Affine(Fraction(1, 2), Fraction(-1, 2))
    require(Affine(Fraction(2, 3), -1).step(2) == q,
            "critical exponent-two identity fails")
    require(Affine(2, -1) == Affine(4 * q.a, 4 * q.b + 1),
            "critical target identity fails")
    # 3J(q)+1 = 4(3q+1), independent of its eventual exact valuation.
    require(Affine(12, 4) == Affine(4 * 3, 4 * 1), "J identity fails")


@dataclass(frozen=True)
class Q19Reduction:
    m: int
    h: int
    b: int
    p: int
    child_kind: str
    child_source: Witness
    target_prefix: tuple[int, ...]

    def finish(self, child_target: Witness) -> Witness:
        expected = 9 * self.p if self.child_kind == "Q" else 54 * self.p + 1
        require(child_target.x == expected, "wrong child target witness")
        tail = jump(child_target) if self.child_kind == "Q" else child_target
        return prepend(9 * self.m, self.target_prefix, tail)


def reduce_q19(m: int, source: Witness) -> Q19Reduction:
    """Q(m): E(54m+1)=>E(9m), m=19 mod128, to strictly smaller P/Q."""
    require(is_integer(m) and m > 0 and m % 128 == 19,
            "Q19 requires m=19 mod128")
    require(source.x == 54 * m + 1, "incorrect Q source witness")
    h = (27 * m - 1) // 128
    b = v2(h)
    s, odd_part = b // 2, h >> b
    p = (3 ** s) * odd_part
    require(0 < p <= h < m and p % 2 == 1, "strict descent bound fails")
    source_prefix = (1, 4, 2) + (2,) * s
    require(source.increments[:len(source_prefix)] == source_prefix,
            "Q19 source prefix is not exact")
    child_source = source.tail(len(source_prefix))
    target_prefix = (1, 2, 2) + (2,) * s
    if b % 2 == 0:
        require(child_source.x == 54 * p + 1, "even Q19 source endpoint fails")
        require(walk(9 * m, target_prefix)[-1] == 36 * p + 1,
                "even Q19 target endpoint fails")
        return Q19Reduction(m, h, b, p, "Q", child_source, target_prefix)
    require(child_source.x == 108 * p + 1, "odd Q19 source endpoint fails")
    child_source = unjump(child_source)
    target_prefix += (2,)
    require(child_source.x == 27 * p, "odd Q19 J inverse fails")
    require(walk(9 * m, target_prefix)[-1] == 54 * p + 1,
            "odd Q19 target endpoint fails")
    return Q19Reduction(m, h, b, p, "P", child_source, target_prefix)


def verify_q19_schema() -> None:
    h = Affine(27, 4)  # m=128t+19
    require(affine_walk(Affine(6912, 1027), (1, 4, 2))
            == Affine(54 * h.a, 54 * h.b + 1), "Q19 source polynomial fails")
    require(affine_walk(Affine(1152, 171), (1, 2, 2))
            == Affine(36 * h.a, 36 * h.b + 1), "Q19 target polynomial fails")
    # Each iteration consumes h divisible by four, replacing h by 3h/4.
    require(affine_walk(Affine(216, 1), (2,)) == Affine(162, 1),
            "Q19 source quarter induction fails")
    require(affine_walk(Affine(144, 1), (2,)) == Affine(108, 1),
            "Q19 target quarter induction fails")
    require(affine_walk(Affine(144, 73), (2,)) == Affine(108, 55),
            "Q19 odd terminal quarter step fails")  # p=2t+1


@dataclass(frozen=True)
class TransformResult:
    status: str
    witness: Optional[Witness]
    trace: tuple[str, ...]


def _solve_bridge(kind: str, m: int, source: Witness, depth: int = 0) -> TransformResult:
    require(kind in ("P", "Q") and m > 0 and m % 2 == 1, "invalid bridge")
    expected = 27 * m if kind == "P" else 54 * m + 1
    require(source.x == expected, "bridge source mismatch")
    original_m = 2 * m if kind == "P" else m
    certificate = choose_certificate(original_m)
    if certificate is not None:
        embedded_tail = jump(source) if kind == "P" else source
        embedded = prepend(128 * original_m + 1, (2, 2, 2), embedded_tail)
        output = certificate.apply(embedded, original_m)
        target = output.tail(3) if kind == "P" else unjump(output.tail(2))
        return TransformResult("PROVED", target, (kind + ": " + certificate.name,))
    if depth >= 128:
        return TransformResult("UNRESOLVED", None, ("recursion resource limit",))
    if kind == "Q" and m % 128 == 19:
        reduction = reduce_q19(m, source)
        child = _solve_bridge(reduction.child_kind, reduction.p,
                              reduction.child_source, depth + 1)
        trace = ("Q19: Q(" + str(m) + ")->" + reduction.child_kind
                 + "(" + str(reduction.p) + ")",) + child.trace
        if child.witness is None:
            return TransformResult("UNRESOLVED", None, trace)
        return TransformResult("PROVED", reduction.finish(child.witness), trace)
    return TransformResult("UNRESOLVED", None,
                           ("no certificate for " + kind + "(" + str(m) + ")",))


def transform(source: Witness) -> TransformResult:
    """Construct the requested witness, or explicitly leave the case unresolved."""
    require(isinstance(source, Witness), "a validated Witness is required")
    if source.x % 128 != 1:
        return TransformResult("UNRESOLVED", None, ("input is outside requested classes",))
    m = (source.x - 1) // 128
    if m <= 0 or m % 4 == 0:
        return TransformResult("UNRESOLVED", None, ("input is outside requested classes",))
    certificate = choose_certificate(m)
    if certificate is not None:
        return TransformResult("PROVED", certificate.apply(source, m),
                               (certificate.name,))
    if m % 2 == 1:
        child = _solve_bridge("Q", m, source.tail(3))
        target = None if child.witness is None else prepend(
            64 * m + 1, (2, 2), jump(child.witness))
    else:
        child = _solve_bridge("P", m // 2, unjump(source.tail(3)))
        target = None if child.witness is None else prepend(
            64 * m + 1, (2, 2, 2), child.witness)
    return TransformResult(child.status, target, child.trace)


def self_test() -> dict[str, object]:
    verify_merger_schema()
    verify_q19_schema()
    certificates = FIXED_CERTIFICATES + tuple(infinite_certificate(k) for k in range(1, 9))
    witness_checks = 0
    for certificate in certificates:
        certificate.verify()
        for t in (0, 1, 2):
            m = certificate.modulus * t + certificate.residue
            source = Witness.from_trajectory(128 * m + 1)
            result = transform(source)
            require(result.status == "PROVED" and result.witness is not None,
                    "certified fixture was not proved")
            require(result.witness.x == 64 * m + 1, "wrong transformed target")
            witness_checks += 1
    # Both descent parities; targets are searched only as independent test fixtures.
    descent_checks = 0
    for m in (19, 147, 275, 787, 9875):
        source = Witness.from_trajectory(54 * m + 1)
        reduction = reduce_q19(m, source)
        child_target_x = (9 * reduction.p if reduction.child_kind == "Q"
                          else 54 * reduction.p + 1)
        output = reduction.finish(Witness.from_trajectory(child_target_x))
        require(output.x == 9 * m, "Q19 reconstruction target mismatch")
        require(reduction.child_source.length < source.length,
                "Q19 did not shorten its known source witness")
        descent_checks += 1
    for m in (787, 9875):
        result = transform(Witness.from_trajectory(128 * m + 1))
        require(result.status == "PROVED" and result.witness is not None,
                "recursive descent fixture was not proved")
        require(result.witness.x == 64 * m + 1, "recursive target mismatch")
        witness_checks += 1
    unresolved = transform(Witness.from_trajectory(129))
    require(unresolved.status == "UNRESOLVED" and unresolved.witness is None,
            "unsupported case was silently treated as proved")
    one = Witness(1, (0,))
    require(jump(one).x == 5 and unjump(jump(one)).x == 1, "J boundary failed")
    require(splice(one, 3, (1, 4)).x == 3, "padding/splicing at one failed")
    for u in (1, 7, 41):
        k, w = v2(u + 1), (u + 1) >> v2(u + 1)
        require((3 ** k * w) % 4 == 3, "bad generic lemma fixture")
        q = (3 ** k * w - 1) // 2
        lam = v2(3 * q + 1)
        require(walk(u, (1,) * (k - 1) + (2, lam))[-1]
                == walk(2 * u + 1, (1,) * k + (lam + 2,))[-1],
                "generic lemma boundary failed")
    malformed = (
        (1, ()), (1, (1,)), (1, (0, 0)), (1, (0, -1)),
        (1, (0, True)), (True, (0,)), (0, (0,)), (2, (0,)),
        (3, (0,)), (3, (0, 2, 5)), (3, (0, 1, 4)),
    )
    rejected = 0
    for x, cumulative in malformed:
        try:
            Witness(x, cumulative)
        except WitnessError:
            rejected += 1
        else:
            raise WitnessError("malformed witness was accepted")
    try:
        Witness.from_trajectory(3, max_steps=0)
    except TrajectoryBoundExceeded:
        pass
    else:
        raise WitnessError("bounded fixture search did not report its limit")
    return {
        "status": "PASS",
        "full_claim": "UNRESOLVED",
        "universal_fixed_affine_certificates": len(FIXED_CERTIFICATES),
        "unbounded_k_family_induction_schema": "PASS",
        "additional_affine_k_instantiations": 8,
        "q19_descent_schema": "PASS",
        "transformed_fixture_witnesses": witness_checks,
        "q19_reconstruction_fixtures": descent_checks,
        "malformed_witnesses_rejected": rejected,
        "unsupported_case": "UNRESOLVED",
        "evidence_limit": "Exact certificate identities and stated fixtures; no exhaustive search or full proof.",
    }


if __name__ == "__main__":
    print(json.dumps(self_test(), sort_keys=True, separators=(",", ":")))
