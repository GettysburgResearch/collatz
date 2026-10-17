# L-9108 - Finite-lasso obstruction

- **Claim ID:** L-9108
- **Title:** Forward-invariant finite unions of binary affine-geometric rays have only eventually periodic orbits
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101; the slender corollary additionally uses the classical slender-regular decomposition theorem
- **Scope:** finite unions of exact rays; regular slender languages only through the stated external decomposition
- **Related counterexample candidates:** none

## Statement

Let `S` be a finite set together with a finite union of exact rays

$$
R_i=\{A_i+B_i2^{h_i k}:k\geq K_i\},
$$

where `h_i >= 1`, `B_i>0`, `A_i,B_i` are rational with odd denominators, and
every displayed value is a positive integer.  If `T(S) subset S`, then every
shortcut orbit starting in `S` is eventually periodic.

Therefore any nonempty safe forward-invariant `S` of this form contains a
nontrivial positive Collatz cycle.

As a carefully scoped corollary, the same conclusion holds for a slender
regular language of canonical LSD-first words, using the classical theorem
that every slender regular language is a finite union of languages `u v* w`.

## Definitions

For nonzero rational `x`, define its 2-adic unit part by

$$
\operatorname{unit}_2(x)=2^{-\nu_2(x)}x.
$$

A language is slender if a fixed constant bounds the number of its words of
each length.  This is substantially narrower than an arbitrary regular
language.

## Motivation

The regular pumping lemma always places at least one lasso family inside an
infinite regular language.  This result identifies the exact point at which
that observation becomes an obstruction: the entire invariant set must be
covered by finitely many such families.  It also records why pumping one ray
inside a general branching DFA is not enough.

## Proof or construction

For large `k`, parity on `R_i` is constant, say `epsilon_i in {0,1}`, because
`B_i2^(h_i k)` tends to zero 2-adically.  On that tail,

$$
T(A_i+B_i2^{h_i k})=C_i+D_i2^{h_i k},
\qquad
D_i=\frac{3^{\epsilon_i}}{2}B_i.
$$

First consider an image ray `C+D2^(hk)` and a target ray
`A+B2^(g ell)`.  If they have infinitely many common values, their indices
both tend to infinity.  Equality along that sequence and passage to the
2-adic limit give `C=A`.  The remaining equality

$$
D2^{hk}=B2^{g\ell}
$$

then gives `unit_2(D)=unit_2(B)`.  Thus every source-target pair with infinite
intersection satisfies

$$
\operatorname{unit}_2(B_j)
=3^{\epsilon_i}\operatorname{unit}_2(B_i). \tag{1}
$$

This infinite-intersection step is what permits one source ray to split among
several target rays; no unique eventual target is assumed.

Suppose an orbit in `S` were not eventually periodic.  Its values are all
distinct, so it eventually leaves the finite exceptional set and every finite
initial segment of every ray.  Choose one representing ray for each late orbit
value.  There are only finitely many ordered source-target ray pairs.  A pair
whose image and target have finite intersection can occur only finitely often
along a distinct-value orbit.  After discarding another finite prefix, every
transition therefore obeys (1).

The finite collection of positive rational unit parts
`{unit_2(B_i)}` cannot support infinitely many strict multiplications by
three.  Hence only finitely many late transitions have `epsilon_i=1`.
Eventually every shortcut step on the orbit is a halving.  But a fixed
positive integer permits only `nu_2(n)` consecutive halvings before becoming
odd, a contradiction.  Every orbit in `S` is therefore eventually periodic.

For the slender corollary, write the regular language as a finite union of
`u v* w`.  If `p=|u|` and `h=|v|>0`, the values in one component are

$$
[uv^kw]
=[u]-\frac{2^p[v]}{2^h-1}
+2^{hk}\left(2^p[w]+\frac{2^p[v]}{2^h-1}\right).
$$

After discarding finite or degenerate components, this is a ray of the stated
form with positive coefficient and odd denominator.  Finite components join
the exceptional set.  The ray theorem applies.

## Dependency audit

- The finite-ray theorem is self-contained apart from elementary arithmetic
  in the 2-adic valuation.
- The slender corollary depends on the published characterization of slender
  regular languages as finite unions of `u v* w`; one primary source is
  Păun--Salomaa, *Thin and slender languages*,
  https://doi.org/10.1016/0166-218X(94)00014-5.
- Admission and exact attribution of that external theorem remain subject to
  issue #7.

## Gap audit

- A pumping-lemma lasso contained in a general regular language need not be
  forward invariant by itself.  Its image may enter the language's other,
  genuinely branching regions.
- The theorem excludes slender sanctuaries unless they already certify a
  nontrivial cycle.  It does not exclude nonslender regular sanctuaries.
- No conclusion about the existence or nonexistence of a nontrivial positive
  Collatz cycle is imported.

## Adversarial tests

- Splitting `{2^k}` into its even-`k` and odd-`k` subrays shows why an image
  ray cannot simply be assigned one target ray.  The infinite-intersection
  argument handles both target phases.
- A finite nontrivial cycle would satisfy the theorem rather than contradict
  it; this is why the conclusion is eventual periodicity, not emptiness.

## Remaining uncertainty

The finite-ray proof appears complete.  The external slender-language
decomposition has not been independently reconstructed in this repository.

## Suggested next attack

Restrict serious synthesis to nonslender transition structures with genuine
branching at arbitrarily large word lengths, and use the finite-ray unit-part
argument as a rejection certificate for lasso-only learned templates.
