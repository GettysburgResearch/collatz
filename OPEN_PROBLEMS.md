# Open problems

Last updated: 2026-07-21  
Active packet: issue `#2`  
Active draft PR: `#3`

## Q-0001 — Finite-boundary regeneration

Status: `IDEA` / central target

Construct one ordinary finite lifted state whose induced orbit remains admissible forever. Neither finite experiments, adic points, large alphabets, arbitrary precision, nor complete modular projection alone are sufficient.

Equivalent targets:

1. a finite aperiodic vertical macro-grammar with one finite moving boundary;
2. a finite family of positive run-length/cofactor schemas closed under
   \[
   d_k+N^{u_k}C_k=d_{k+1}+M^{u_{k+1}}C_{k+1}.
   \]

## Q-0002 — Analytic fiber growth

Status: `PROPOSED RESOLUTION` by `T-0005`

Supercritical collision fibers have exponentially unbounded cardinality while retaining expansion ratio in `(1,3/2]`.

## Q-0003 — Carry grammar for the width-three chart

Status: `IDEA`

Classify finite vertical relays for

\[
H(512B+d)=729B+d,\qquad d\in\{0,1,2\}.
\]

The known short horizontal tile does not close vertically.

## Q-0004 — Multi-chart transition groupoid

Status: `IDEA`

Construct exact finite bridges among collision charts, including changes of affine gauge, lifting class, run-length cofactor, and finite boundary.

## Q-0005 — Finite versus adic closure

Status: `IDEA`

Give a usable criterion deciding when an aperiodic finitely generated itinerary encodes one ordinary nonnegative integer rather than only a 2-adic point.

## Q-0006 — Independent verification

Status: `IDEA`

Independently reconstruct all proposed claims, now especially:

- the one-hot signature correction `L-0009`;
- the triangular dyadic bijection `L-0010`;
- positivity, CRT tail selection, and complete projection in `T-0007`;
- exact reproduction of `X-0005`.

## Q-0007 — Vertical macro-tile closure

Status: `IDEA`

Build a finite collection of mixed-radix tiles whose emitted rows remain parseable while the ordinary high-order boundary grows at slope `log_M(N/M)`.

## Q-0008 — Parameterized S-unit skeleton schemas

Status: `IDEA`

Find finitely many positive cofactor schemas closed under

\[
d+N^uC=d'+M^{u'}C'.
\]

The construction must preserve admissible digits, exact valuation, positivity, lifting congruences, and one finite initial state.

## Q-0009 — Structured collision codes

Status: `PARTIAL`

The following are now proposed:

- exponentially large mildly supercritical fibers (`T-0005`);
- arbitrary finite precision (`L-0008`);
- preservation of fixed geometry (`T-0006`);
- complete projection modulo `2^b` for every `b` (`T-0007`).

Still open: growing difference intervals with useful quantitative bounds, scale-independent carry relays, and direct cofactor closure.

## Q-0010 — Growing complete dyadic projection

Status: `PROPOSED RESOLUTION` by `L-0009`, `L-0010`, `T-0007`

For every `b >= 1`, there is a mildly supercritical collision fiber with `2^b` branches whose offsets meet every residue modulo `2^b` exactly once.

The construction uses:

1. all low binary patterns embedded into fixed-weight prefixes;
2. one-hot suffixes that correct every prefix to a common inverse signature;
3. a finite CRT-selected odd tail that supplies supercritical drift without changing offsets.

## Q-0011 — Convert dyadic freedom into a positive relay

Status: `IDEA` / primary next target

Use a complete-projection alphabet to prove a quantitative one-step relay for

\[
d+N^uC=d'+M^{u'}C'.
\]

Desired theorem:

- for every cofactor `C` in a controlled positive interval, choose `d'` from the alphabet so that the numerator has a prescribed dyadic valuation;
- obtain a positive next cofactor `C'` lying in another controlled interval;
- preserve the active lifting congruence;
- make the interval transition close under finitely many schemas.

Complete modular projection guarantees residue correction. The missing work is simultaneous positivity, exact valuation, bounded distortion, and infinite finite-schema closure.
