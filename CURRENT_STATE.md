# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Project maturity

The active branch contains five mathematical research sessions. No claim has yet received independent review, so complete-looking finite theorems and identities remain `PROPOSED`.

There is currently **no positive-integer Collatz counterexample** in the repository.

## Fixed framework

For the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\]

a length-\(L\), weight-\(a\) parity word has exact affine action

\[
T^L(n)=\frac{3^an+B(w)}{2^L}
\]

on one residue class modulo \(2^L\).

A finite collision fiber

\[
T^L(2^Lq+r+d)=3^aq+s\qquad(d\in D)
\]

induces

\[
H_D(2^LB+d)=3^aB+d.
\]

One invariant congruence class lifts exactly to ordinary positive Collatz integers. An infinite admissible orbit from one finite lifted state would be a counterexample.

## Results before the current session

The repository already contains:

- exact finite collision atlases and sparse collision fibers;
- universal finite-horizon carry pumping;
- dual 2-adic/real coding and an aperiodicity obstruction;
- the exact run-length/cofactor skeleton
  \[
  d_k+N^{u_k}C_k=d_{k+1}+M^{u_{k+1}}C_{k+1};
  \]
- inverse-signature collision codes;
- exponentially unbounded mildly supercritical fiber cardinality;
- an exact 339-branch chart with full projection modulo 16 and a long difference interval;
- exact tensor transport preserving any fixed finite alphabet geometry;
- arbitrary finite 3-adic precision from explicit atomic codes.

These remove alphabet size, local pumping, and finite precision as principal scarcities.

## New session: complete dyadic projection at arbitrary scale

### L-0009 — Universal one-hot signature correction

Let \(\mathcal U\) be any finite family of binary words of common length \(L\) and weight \(a\). For any \(p\ge a+1\), append a length

\[
S=2\cdot3^{p-1}
\]

weight-one suffix. Since \(2\) generates \((\mathbb Z/3^p\mathbb Z)^\times\), the position of that single one can be chosen independently for every prefix so that every completed word has the same affine constant modulo \(3^p\).

Thus **every fixed-length, fixed-weight prefix family can be completed into one exact inverse collision code without discarding any prefix choices**.

### L-0010 — Fixed-weight prefixes carry all dyadic residues

For every \(b\ge1\), take all \(2^b\) binary patterns in the first \(b\) positions and add compensating ones in positions \(b,\ldots,2b-1\) so that every word has total weight \(b\).

The map

\[
x\longmapsto B(u_x)\pmod{2^b}
\]

is bijective. The proof is triangular: modulo \(2^{j+1}\), the next bit is determined because its coefficient is an odd multiple of \(2^j\).

### T-0007 — Complete dyadic projection theorem

Combine the two constructions:

1. begin with the \(2^b\) fixed-weight prefixes of `L-0010`;
2. correct all signatures with `L-0009` at precision \(b+1\);
3. choose a finite CRT root and append the shortest forced all-odd tail making the block supercritical.

The resulting finite supercritical collision fiber has exactly \(2^b\) branches and offset alphabet \(D_b\) satisfying

\[
\boxed{D_b\bmod2^b=\mathbb Z/2^b\mathbb Z.}
\]

The expansion ratio can simultaneously be kept in

\[
1<N/M\le3/2.
\]

This is the first proposed theorem giving closure-relevant alphabet geometry that genuinely grows without bound.

## Exact computation

`X-0005` directly constructs and verifies the theorem for \(1\le b\le5\). It checks every corrected parity word, every common inverse output, every forced odd tail, and complete residue projection. The tested branch counts are

```text
2, 4, 8, 16, 32.
```

The corresponding corrected core lengths are

```text
8, 22, 60, 170, 496.
```

All computations use exact Python integers and the standard library only.

## Strategic consequence

For arbitrarily large \(b\), every possible low-order correction modulo \(2^b\) is represented by some induced digit. Low-order modular freedom is therefore not a finite-scale accident.

This sharply advances the run-length target. In

\[
d_k+N^{u_k}C_k=d_{k+1}+M^{u_{k+1}}C_{k+1},
\]

the alphabet can now supply every desired dyadic residue correction up to an arbitrarily chosen scale.

However, modular solvability is not yet a uniform positive relay. The selected next digit must also:

- keep the next cofactor positive;
- enforce the required exact divisibility depth;
- preserve the lifting congruence;
- fit one finite aperiodic schema for all future stages.

## Central unresolved step

The project still lacks a **finite-boundary regeneration theorem**.

The strongest next target is now:

> Convert complete dyadic projection into a finite family of uniform positive run-length/cofactor relays, or prove a finite aperiodic macro-grammar that uses the modular correction digits while preserving one ordinary finite high-order boundary.

## Immediate priorities

1. Derive a one-step cofactor relay theorem using complete projection modulo \(2^b\), with quantitative positivity bounds.
2. Determine whether bounded cofactor ratios can be maintained by choosing \(b\) as a function of the current boundary scale.
3. Compress that adaptive choice into finitely many schemas or an aperiodic substitution.
4. Combine dyadic correction with variable collision charts to preserve lifting congruences.
5. Independently audit `L-0009`, `L-0010`, and `T-0007`, especially the triangular bijection, signature correction, positivity, and tail promotion.
