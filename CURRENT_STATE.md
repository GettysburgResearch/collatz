# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Project maturity

The active branch contains four mathematical research sessions. No claim has yet received independent review, so complete-looking finite theorems and identities remain `PROPOSED`.

There is currently **no positive-integer Collatz counterexample** in the repository.

## Fixed framework

The shortcut map is

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Parity words are chronological. Mixed-radix words are low-order first. For a length-\(L\), weight-\(a\) parity word,

\[
T^L(n)=\frac{3^an+B(w)}{2^L}
\]

on one residue class modulo \(2^L\).

## Collision fibers and induced maps

If a finite digit set \(D\) satisfies

\[
T^L(2^Lq+r+d)=3^aq+s
\qquad(d\in D),
\]

then `T-0002` induces

\[
H_D(2^LB+d)=3^aB+d.
\]

One invariant congruence class of induced states lifts exactly to ordinary positive Collatz integers. An infinite admissible orbit beginning from one finite lifted state would be a counterexample.

## Finite collision atlas

`L-0003` gives an exact \(O(2^L)\) recursion for all pairs

\[
(a_L(r),T^L(r)).
\]

`X-0002` enumerates complete supercritical fibers through depth 22. The largest finite census chart recorded there has eighteen branches.

## Inverse-signature construction

For a word \(w\) of length \(L\), weight \(a\), define

\[
\sigma(w)=2^{-L}B(w)\pmod{3^a}.
\]

`L-0005` proves that equal signatures are exactly the congruence needed to invert several parity words from one common output.

A CRT choice of common output congruent to \(-1\pmod{2^k}\) appends \(k\) forced odd steps. Thus:

- the inverse code supplies branching;
- the common finite odd tail supplies supercritical drift.

## Collision-code composition

For chronological concatenation,

\[
B(uv)=3^{a(v)}B(u)+2^{|u|}B(v).
\]

`L-0006` turns this into a finite 3-adic precision budget. High-surplus suffix codes can absorb independent prefix choices.

## T-0005 — Exponentially unbounded supercritical fibers

If

\[
2^k-1>3^a,
\qquad
3^{a+k}>2^{L+k},
\]

then a supercritical collision fiber exists with at least

\[
\left\lceil\frac{\binom La}{3^a}\right\rceil
\]

branches.

Taking \(L=3m\), \(a=m\), and the shortest supercritical tail gives

\[
|D_m|
\gtrsim
\frac1{\sqrt m}\left(\frac94\right)^m
\]

while the expansion factor remains in \((1,3/2]\). Large mildly supercritical alphabets are therefore abundant by proposed theorem.

## O-0005 — Exact 339-branch chart

`X-0003` verifies

\[
T^{44}(17592186044416q+8952950628352+d)
=22876792454961q+11642373114938
\]

for a reproducible 339-element offset set. Its exact finite geometry includes:

- every residue class modulo 16;
- a seven-term consecutive run;
- \([-934,934]\subseteq D-D\).

## New session: exact geometry transport

### L-0007 — Offset tensor law

For a prefix code \(U\) of weight \(a_1\) and a suffix code \(V\) whose precision is at least \(a_1+a_2\), the inverse-root alphabets satisfy

\[
\boxed{
D_{UV}=D_U+2^{L_1}E_V.
}
\]

This is an exact mixed-radix Minkowski sum. It implies product cardinality and preserves every difference, modular projection, consecutive run, and difference interval already witnessed in the prefix alphabet.

### L-0008 — Arbitrary precision on demand

For every \(p\ge1\), the two weight-one parity words with their unique odd steps at positions

\[
0,\qquad 2\cdot3^{p-1}
\]

have affine constants differing by a number of exact 3-adic valuation \(p\):

\[
v_3\left(2^{2\cdot3^{p-1}}-1\right)=p.
\]

Thus finite collision codes possess an explicit unbounded precision reservoir.

### T-0006 — Geometry-preserving amplification

Starting from any finite collision code \(U_0\), append atomic suffix codes of increasing precision. After \(n\) stages:

\[
|U_n|=|U_0|2^n,
\]

and the inverse-root alphabet contains a translated copy of the original alphabet. Its difference set contains \(D_0-D_0\).

A finite odd tail can then make the chart supercritical without changing the offset geometry.

Consequently `O-0005` embeds into arbitrarily large exact supercritical fibers that still cover every residue modulo 16, retain a seven-term run, and contain \([-934,934]\) in their difference sets.

This is stronger than cardinality growth, but still preserves only **fixed finite geometry**. It does not make the useful scale grow with the boundary.

## Universal local amplification

`L-0004` proves that every nontrivial collision chart has exact finite-horizon carry pumps. Local amplification is universal; it does not imply vertical closure.

## Global form of any hypothetical induced orbit

`T-0003` gives the exact 2-adic coding

\[
A_0=\frac{N-M}{N}\sum_{t\ge0}d_t\left(\frac MN\right)^t
\]

and the real asymptotic law

\[
A_t=C(N/M)^t+O(1).
\]

The base-\(M\) boundary grows at slope \(\log_M(N/M)\), and a nontrivial ordinary-integer orbit cannot have an eventually periodic digit itinerary.

`T-0004` gives the run-length skeleton

\[
d_k+N^{u_k}C_k
=d_{k+1}+M^{u_{k+1}}C_{k+1}.
\]

This remains the cleanest scale-independent global target.

## Computational state

- `X-0001`: consecutive supercritical bundles through depth 17.
- `X-0002`: complete supercritical fibers through depth 22.
- `X-0003`: inverse-signature classes, finite odd tails, and the 339-branch chart.
- `X-0004`: arbitrary-precision atomic codes, exact offset tensors, cardinality doubling, inherited geometry, and finite tail promotion.

All programs use exact Python integers and the standard library only.

## Central unresolved step

The project still lacks a **finite-boundary regeneration theorem**.

A solution must construct one ordinary finite starting state and prove either:

1. a finite aperiodic macro-tile grammar whose rows close vertically; or
2. a finite family of positive cofactor schemas closed under the run-length equations and lifting congruences.

The following are now known to be insufficient by themselves:

- large alphabet cardinality;
- universal finite-horizon pumps;
- arbitrary 3-adic precision;
- preservation of any fixed finite amount of alphabet geometry;
- compatible finite prefixes or adic inverse limits.

## Immediate research priorities

1. **Growing geometry.** Construct code families whose modular coverage or difference intervals increase with code depth at a rate relevant to boundary motion.
2. **Tensorable relay tiles.** Use `L-0007` to preserve and combine exact vertical relay gadgets, not merely digit sets.
3. **Run-length closure.** Convert the large difference intervals of `O-0005` into uniform positive cofactor transformations.
4. **Variable charts.** Use one branching core with several finite odd tails and lifting gauges to manage boundary changes.
5. **Aperiodic address system.** Investigate whether the odd normalized offsets of `L-0008` can encode a finite moving-boundary address grammar.
6. **Independent audit.** Reconstruct `L-0005` through `T-0006`, especially inverse uniqueness, precision consumption, tensor orientation, and preservation of offsets under tail promotion.