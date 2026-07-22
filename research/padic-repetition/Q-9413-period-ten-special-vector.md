# Q-9413 — Period-ten special-vector irrationality

Claim ID: `Q-9413`  
Title: Can the native period-ten coefficient vector be excluded more cheaply than full ten-dimensional independence?  
Status: `IDEA / PRIMARY FIXED-PERIOD TARGET`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-9412`, `L-9413`, `L-9414`, `T-9417`, `R-9406`, `R-9407`  
Scope: primitive positive periodic stack words of minimal period ten

## Exact starting point

For

```text
W=d_1...d_10
```

with minimal period ten,

```text
Theta(m;W^infinity)
 =sum_(j=0)^9 C_j f_R(Z lambda^j).                    (1)
```

The ten points are in distinct `R^Z`-orbits.

The Väänänen–Wallisser full-independence condition applies through nine points
and fails at ten. This does not decide (1), whose coefficient vector is fixed by
the transfer polynomial.

## Route A — one-phase elimination

Use

```text
alpha_j=f_R(Z lambda^j), 0<=j<=8,
beta=f_R(Z lambda^9).
```

Extract the dimension-nine quantitative source estimate in the valuation form

```text
v_2(a_0+sum_(j=0)^8 a_(j+1)alpha_j)
 <=(omega_9+o(1))log_2 H(a).                          (2)
```

`L-9413` gives scalar approximants to `beta` with exponent

```text
tau=9/log_2(81)=1.419591945535779... .                (3)
```

By `L-9414`, condition

```text
omega_9<tau                                             (4)
```

would prove full independence after adding `beta`, and in particular
irrationality of (1).

### Deliverable

Transcribe the source's exact measure, including all height conventions, into
(2) and decide (4). Qualitative independence is not enough.

## Route B — the native two-dimensional `q`-difference orbit

Define the scalar periodic-tail function in the starting-height variable:

```text
F_W(X)=Theta(m;W^infinity),
X=T^(9m).
```

`L-9408` gives the first-order skew equation

```text
F_W(X)
 =P_W(X)+T^e X^10 F_W(lambda X).                      (5)
```

Equivalently,

```text
[1      ]   [1       0       ][1             ]
[F_W(X)] = [P_W(X) T^e X^10 ][F_W(lambda X)].         (6)
```

The native target is therefore one value in a two-dimensional homogeneous
`q`-difference system, despite its ten-phase diagonalization.

### Deliverable

Construct a Padé or determinant theorem directly for (6), or verify a source
theorem whose hypotheses cover this triangular system. The exact coefficient
polynomial `P_W` must remain visible.

Matala-aho's work on Diophantine approximation for `q`-functional equations is
a high-priority source lead, but no black-box application is claimed before its
full hypotheses are inspected.

## Route C — combined-moment Padé

The block coefficients of (1) are

```text
u_N
 =R^[N(N-1)/2] Z^N P_W(X lambda^N).                   (7)
```

A direct scalar Padé system for the sequence `(u_N)` can spend one degree of
freedom per **combined** coefficient, rather than cancelling ten phases
separately.

The naive exact linear solve has severe height growth, so a useful construction
must expose structure:

```text
- a Christoffel or q-orthogonal transform of the pure Tschakaloff moments;
- symbolic maximal-minor factors;
- a phase-sensitive Hermite–Padé system;
- or a Cartier/q-Lucas recurrence with controlled global height.
```

## Route D — period-uniform objective

A fixed period-ten theorem is a milestone, not the end. The balanced
nonperiodic `17/18` directive is approached by standard words whose lengths grow.
Every successful construction should report its dependence on period `r` and
Padé order `n`.

The desired endpoint is a lower bound that remains useful as `r->infinity`.

## Closed shortcuts

- Full-independence import stops at nine (`R-9406`).
- Unequal phasewise root allocation is closed by `T-9416`.
- Scalar adjacent-order Casoratians remain below one at period ten even with
  zero cofactor-height cost (`R-9407`).
- Cancelling only `O(1)` additional blocks cannot change a quadratic exponent.

## Success criteria

### Obstruction

Prove (1) irrational for every primitive positive period-ten word and propagate
the result through arbitrary finite prefixes.

### Construction

If one word instead yields eventual active-cylinder stabilization, reconstruct
the exact ordinary context, prove positivity at every stage, check the chart
class modulo `17`, replay the full Collatz lift, and only then create a
`K-####` candidate.

## Falsification criteria

- A source theorem is not applicable until every place and height convention is
  checked.
- A determinant with no nonvanishing proof is not an approximant.
- Pre-reduction height is not reduced height.
- Bounded numerical Padé orders are evidence only.
- A period-ten theorem alone does not settle the growing S-adic frontier.
