# T-8508 — Every noncanonical top-boundary lift is uniformly refunded

**Claim ID:** `T-8508`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8507`; the exact integer inequality `3^665>2^1054`  
**Scope:** every continuation cylinder of the intrinsic linear-height core decoder

## Statement

Use the notation of `L-8507`. Thus one complete top-boundary transition has

\[
\boxed{
m=\rho+H_t\ell
\longmapsto
m'=\sigma+3^G\ell,
}
\tag{1}
\]

where

\[
0\le\rho<H_t,
\qquad
\sigma\ge0,
\qquad
H_t=2^{11(t+33)},
\]

and

\[
G=7(t+1)+\gamma-\beta_i.
\]

Since

\[
\gamma\in\{1,2,3\},
\qquad
\beta_i\in\{1,2,3\},
\]

one always has

\[
G\ge7(t+1)-2=7t+5.
\tag{2}
\]

Then:

### 1. Strict refund

For every multiple of `16` with

\[
\boxed{t\ge3760,}
\]

one has, uniformly over all finite states and all four continuation cylinders,

\[
\boxed{3^G>2H_t.}
\tag{3}
\]

Consequently every noncanonical lift `ell>=1` satisfies

\[
\boxed{m'>m.}
\tag{4}
\]

### 2. Doubling refund

For every multiple of `16` with

\[
\boxed{t\ge3776,}
\]

one has

\[
\boxed{3^G>4H_t.}
\tag{5}
\]

Consequently every noncanonical lift satisfies

\[
\boxed{m'>2m.}
\tag{6}
\]

### 3. Exact canonical/noncanonical dichotomy

At every sufficiently late legal step, exactly one of the following occurs:

```text
canonical top boundary:      ell=0 and m=rho;
refunded top boundary:       ell>=1 and m_next>2m.
```

Therefore a hypothetical infinite ordinary path can avoid repeated multiplicative top-boundary refund only by using the canonical representative at those exceptional steps. Local expansion cannot be lost inside a positive free lift.

## Proof

The direct exact integer comparison

\[
\boxed{3^{665}>2^{1054}}
\tag{7}
\]

implies

\[
\log_2 3>\frac{1054}{665}.
\]

For the worst finite-state correction `(2)`, inequality `(3)` follows from

\[
1054(7t+5)>665(11(t+33)+1).
\]

The difference between the two sides is

\[
\boxed{63t-236790.}
\tag{8}
\]

At `t=3760` it equals `90`, and it increases with `t`. This proves `(3)`.

Likewise `(5)` follows from

\[
1054(7t+5)>665(11(t+33)+2),
\]

whose exact difference is

\[
\boxed{63t-237455.}
\tag{9}
\]

At `t=3776` it equals `433`, and it again increases with `t`.

Now let `ell>=1`. Because `0<=rho<H_t`,

\[
m=\rho+H_t\ell
<H_t(\ell+1)
\le2H_t\ell.
\tag{10}
\]

Also `sigma>=0`, so `(1)` gives

\[
m'\ge3^G\ell.
\tag{11}
\]

Under `(3)`, equations `(10)--(11)` yield `m'>m`. Under `(5)`, they yield

\[
m'>4H_t\ell>2m.
\]

This proves `(4)` and `(6)`. The dichotomy is simply the unique Euclidean decomposition `(1)` with `0<=rho<H_t`. ∎

## Significance

The full top boundary is not merely archimedean-expanding in the limit. Once the current quotient uses one complete lift beyond its canonical residue, the exact next ordinary quotient is already larger, and after height `3776` it more than doubles.

The negative-three-cycle run-core map in PR #51 has the same structure with a variable run modulus. `L-8507` and this theorem isolate the shared constructive interface:

```text
one changing dyadic cylinder
+ one canonical carry
+ one odd multiplier larger than the complete cylinder
+ one ordinary refunded quotient.
```

The remaining problem is not drift. It is proving that one written integer continues to land in one of the four changing cylinders forever.

## Gap audit

- Canonical steps `ell=0` are not excluded.
- Infinitely many refunded finite transitions do not by themselves produce one infinite ordinary orbit.
- The theorem does not promote a compatible `2`-adic completion to an integer.
- The large exact multiplier does not choose the required residue `rho`.
