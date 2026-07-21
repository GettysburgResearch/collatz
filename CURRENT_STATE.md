# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Project maturity

The active branch contains six mathematical research sessions. No claim has yet received independent review, so complete-looking finite theorems and identities remain `PROPOSED`.

There is currently **no positive-integer Collatz counterexample** in the repository.

## Fixed map and affine calculus

The shortcut map is

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For a length-\(L\), weight-\(a\) parity word \(w\),

\[
T^L(n)=\frac{3^an+B(w)}{2^L}
\]

on one residue class modulo \(2^L\).

The repository has developed three mutually equivalent finite descriptions of useful Collatz blocks:

1. positive collision fibers;
2. partial induced radix maps;
3. negative-template return families.

The third is now the principal global viewpoint.

## Results from the first five sessions

The branch already contains:

- exact finite collision atlases and sparse collision fibers;
- induced maps
  \[
  H_D(MB+d)=NB+d;
  \]
- universal finite-horizon carry pumping;
- exact 2-adic/real coding and an aperiodicity obstruction;
- the run-length skeleton
  \[
  d_k+N^{u_k}C_k=d_{k+1}+M^{u_{k+1}}C_{k+1};
  \]
- inverse-signature collision codes and an exact composition algebra;
- exponentially unbounded mildly supercritical fiber cardinality;
- the exact 339-branch chart `O-0005`;
- arbitrary finite 3-adic precision;
- geometry-preserving tensor amplification;
- complete collision-alphabet projection modulo \(2^b\) for every \(b\).

These results remove branch count, finite precision, local pumping, and finite-scale dyadic correction as principal scarcities. They do **not** provide one infinite ordinary trajectory.

# New principal framework: negative shadows

## T-0008 — Every collision chart is a negative return system

Suppose

\[
T^L(MQ+r_i)=NQ+s,
\qquad
M=2^L,
\qquad
N=3^a.
\]

Define

\[
u_i=M-r_i,
\qquad
v=N-s.
\]

Then the same finite block satisfies

\[
\boxed{
T^L(-u_i)=-v
}
\]

and, more generally,

\[
\boxed{
T^L(Mq-u_i)=Nq-v
}
\]

for every integer \(q\).

Thus the positive collision fiber is exactly an affine family of shadows of several ordinary negative integers coalescing to one negative target.

At a positive chart boundary write

\[
n(q)=Nq-v.
\]

The next return block is selected by the intrinsic signed equation

\[
\boxed{
Nq_t=Mq_{t+1}+a_t,
\qquad
a_t\in A:=\{v-u_i\}.
}
\]

This is a rational-base \(N/M\) return system with a finite signed alphabet. The separate lifting congruence of the earlier induced coordinate is absorbed into the integral quotient equation.

A finite itinerary obeys the exact address identity

\[
N^kq_0-M^kq_k
=
\sum_{t=0}^{k-1}
a_tN^{k-1-t}M^t.
\]

An infinite admissible chain above an explicit growth threshold gives a divergent positive Collatz trajectory.

## L-0012 — Inverse signatures are negative targets

For a parity word \(w\), put

\[
M=2^L,
\qquad
N=3^a,
\qquad
\sigma(w)=M^{-1}B(w)\pmod N.
\]

The negative return identity

\[
T^L(-u)=-v
\]

is equivalent to

\[
B(w)+Mv=Nu,
\]

and hence to

\[
\boxed{
v\equiv-\sigma(w)\pmod N.
}
\]

Therefore the inverse-signature codes from `L-0005`--`T-0007` are exactly finite negative-preimage fibers of one negative target. The code-composition algebra and the negative renewal graph are the same construction viewed from opposite ends.

# Variable-length renewal systems

## T-0009 — Renewal-code counterexample criterion

Let negative templates return to one target at possibly different depths:

\[
T^{L_i}(-u_i)=-v,
\]

with \(a_i\) odd steps. On the cylinder

\[
q\equiv v-u_i\pmod{2^{L_i}},
\]

the exact quotient map is

\[
\boxed{
F_i(q)=3^{a_i}\frac{q-v+u_i}{2^{L_i}}.
}
\]

If one can exhibit a nonempty set of ordinary quotients above \(v\), a deterministic return selector, forward invariance, and strict growth on every selected branch, then every starting quotient in that set yields a positive Collatz counterexample.

This is now a direct finite-certificate target: construct an infinite but finitely generated renewal language, or a finite graph of negative targets, with one explicit ordinary starting quotient.

## Finite complete one-target obstruction

A finite one-target return family covering every sufficiently large integer quotient cannot have every branch supercritical.

Reason: its finite union of dyadic cylinders is clopen in \(\mathbb Z_2\). Since all sufficiently large ordinary integers are dense in \(\mathbb Z_2\), the union must cover the target quotient \(q=v\). The branch covering that point has

\[
u_i=2^{L_i}v,
\qquad
a_i=0,
\]

so it is the all-even contracting return.

Consequently a successful return construction must use at least one of:

- an infinite regular code with an exceptional 2-adic boundary path;
- a proper invariant survivor set rather than all large quotients;
- several negative targets or charts;
- compensated grammar cycles containing locally subcritical returns.

This explains structurally why a finite stationary all-expanding table has not emerged.

# Real geometry of the return system

## T-0010 — Fractional-window law

For an infinite signed return chain

\[
Nq_t=Mq_{t+1}+a_t,
\qquad
\beta=N/M,
\qquad
\rho=M/N,
\]

there is a real constant \(C\) such that

\[
\boxed{
q_t=C\beta^t+x_t,
}
\]

where

\[
x_t=
\frac1N
\sum_{j\ge0}a_{t+j}\rho^j.
\]

The error is a convex combination of the normalized digits:

\[
\frac{\min A}{N-M}
\le x_t\le
\frac{\max A}{N-M}.
\]

Since \(q_t\) is integral, the multiplicative fractional-part orbit

\[
\{C(N/M)^t\}
\]

must remain forever in a fixed circle arc of length at most

\[
\boxed{
\Delta=
\frac{\operatorname{diam}A}{N-M}
=
\frac{\operatorname{diam}D}{N-M}.
}
\]

The new dimensionless quantity \(\Delta\) is the chart's **normalized aspect ratio**. It measures real rounding freedom and is independent of raw branch count.

## L-0011 — Common odd-tail aspect tax

For a collision core of length \(L\), residue span \(W\), and a common odd tail of length \(k\), the final aspect ratio is exactly

\[
\boxed{
\Delta_k
=
\frac{W/2^L}{2^k(\lambda_k-1)},
}
\]

where \(\lambda_k=N_k/M_k\).

If the final expansion margin satisfies \(\lambda_k\ge1+\varepsilon\), then

\[
\Delta_k<2^{-k}/\varepsilon.
\]

Thus the earlier separation of branching from drift is algebraically correct but incomplete for closure: a long post-merger tail can make the real control window exponentially narrow while leaving all branch offsets unchanged.

## O-0006 — Exact aspect audit

The principal recorded stationary charts have:

```text
chart    branches    diameter/(N-M)
O-0001       2       5.88235294118e-2
O-0002       3       9.21658986175e-3
O-0003       6       1.08518719479e-4
O-0004      18       1.59683351312e-4
O-0005     339       3.25606084224e-9
```

The 339-branch chart is symbolically rich but has a stationary real window more than seven orders of magnitude narrower than the original two-branch chart.

The complete-dyadic-projection examples contract still more sharply. Their exact aspect ratios for \(b=1,\ldots,5\) are approximately

```text
2.17e-5, 2.29e-12, 5.44e-30, 1.10e-93, 4.72e-264.
```

This does not refute those charts. It corrects the optimization objective.

# Computational state

- `X-0001`: consecutive collision bundles.
- `X-0002`: complete finite collision fibers through depth 22.
- `X-0003`: inverse-signature construction and the 339-branch chart.
- `X-0004`: offset tensors and arbitrary-precision atomic codes.
- `X-0005`: complete dyadic projection through \(b=5\).
- `X-0006`: negative-template identities for `O-0001`--`O-0005`, all 339 committed offsets, signed address equations, the finite renewal obstruction witness, and exact aspect-ratio checks.

All programs use exact Python integers and the standard library only.

# Central unresolved step

The project still lacks a **finite-boundary regeneration theorem**.

The strongest current formulations are:

1. construct a regular infinite negative-template renewal code with a positive forward-invariant quotient set;
2. construct a finite multi-target negative return graph whose accepted grammar cycles have net expansion;
3. close finitely many run-length/cofactor schemas;
4. build a graph-directed rounding system whose effective normalized windows stay macroscopic while its 2-adic boundary is one ordinary finite integer.

# Immediate priorities

1. **Negative preimage automata.** Build the reverse Collatz tree of a small negative target or negative cycle, recording return depth, odd count, signed displacement, and cylinder.
2. **Regular renewal language.** Seek a finitely generated infinite return code whose only uncovered 2-adic path is the zero shadow, or whose selected survivor set contains one explicit ordinary quotient.
3. **Multi-target graph.** Use target changes to route around the all-even contracting boundary branch forced by `T-0009`.
4. **Macroscopic aspect ratio.** Search near critical pairs \(2^L\approx3^a\) for negative coalescence fibers whose displacement diameter is comparable to \(N-M\).
5. **Co-designed drift.** Insert expansion before complete coalescence or between return decisions, rather than appending one very long common odd tail.
6. **Independent audit.** Reconstruct `T-0008`--`T-0010`, `L-0011`--`L-0012`, and `X-0006`, especially extension to negative residue classes, the renewal obstruction, and the real-window calculation.
