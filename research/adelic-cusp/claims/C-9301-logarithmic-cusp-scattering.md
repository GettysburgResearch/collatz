# C-9301 — All-depth harmonic control of low-energy cylinders

**Claim ID:** C-9301  
**Title:** Sparse low-energy reciprocal cylinders have vanishing harmonic mass in a growing low-frequency window  
**Status:** IDEA  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9301`, `L-9303`, `L-9309`, `T-9307`, `T-9308`  
**Scope:** proposed all-depth closure theorem for the issue-#4 EQ target  
**Related counterexample candidates:** none

## Exact setup

For depth `K` and integer `h`, define the reciprocal residues

\[
q_\ell(h)
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}},
\qquad
0\le q_\ell(h)<81^{\ell+1},
\]

and the normalized phases

\[
y_\ell(h)
=
\frac{q_\ell(h)}{81^{\ell+1}}.
\]

For a prefix length `L`, put

\[
\mathcal E_{K,L}(h)
=
\sum_{\ell=0}^{L-1}
\|y_\ell(h)\|^2.
\]

`L-9309` proves that exact length-`L` lift data are in bijection with `h mod81^L`. `T-9307` proves that the low-energy condition

\[
\mathcal E_{K,L}(h)
\le
L/64
\]

selects only a power-small collection of residue classes in every interval. `T-9308` proves that all frequencies outside any growing low window already have vanishing total harmonic mass.

## Conjecture: harmonic exceptional-cylinder bound

There exist growing integer sequences

\[
L_K\longrightarrow\infty,
\qquad
H_K\longrightarrow\infty,
\qquad
H_K\le2^K,
\]

with

\[
L_K\le K,
\]

such that

\[
\boxed{
\sum_{\substack{1\le h\le H_K\\
\mathcal E_{K,L_K}(h)\le L_K/64}}
\frac1h
\longrightarrow0.
}
\tag{1}
\]

A stronger useful form would give a power saving

\[
\sum_{\substack{1\le h\le H\\
\mathcal E_{K,L}(h)\le L/64}}
\frac1h
\le
C H^{-c}
\tag{2}
\]

in one nontrivial all-depth relation between `H`, `L`, and `K`.

## Consequence: full all-depth EQ

For every nonexceptional `h<=H_K`, `L-9303` and the definition of the exceptional set give

\[
F_K(h)
\le
\exp(-L_K/32).
\]

Hence

\[
\sum_{\substack{1\le h\le H_K\\
\mathcal E_{K,L_K}(h)>L_K/64}}
\frac{F_K(h)}h
\le
\exp(-L_K/32)
(1+\log H_K),
\]

which tends to zero whenever

\[
L_K-32\log\log H_K
\longrightarrow+\infty.
\tag{3}
\]

The exceptional contribution is bounded by `(1)` because `F_K(h)<=1`.

Finally, `T-9308` gives

\[
\sum_{H_K<h\le2^K}
\frac{F_K(h)}h
\le
C H_K^{-\delta}
+
\pi2^{-5K}.
\]

Thus `(1)` and `(3)` imply

\[
\boxed{
E_K
=
\sum_{1\le h\le2^K}
\frac{F_K(h)}h
\longrightarrow0
}
\]

for **every** depth `K`.

This is now the packet's exact all-depth closure interface.

## Stronger pointwise sufficient condition

The earlier version of `C-9301` proposed fixed-threshold scattering: there exist `A,c,epsilon>0` such that every

\[
1\le h\le K^A
\]

has at least `c log K` phases with distance at least `epsilon` from an integer.

That statement remains a sufficient but stronger route. It gives polynomial pointwise decay in a polynomial window, and `T-9308` then closes the high tail unconditionally.

The present harmonic formulation is weaker and better matched to `T-9307`: it allows a sparse exceptional set, provided those exceptional residue classes do not cluster at harmonically expensive small representatives.

## Arithmetic reformulations

### Terminal residue location

A length-`L` prefix reconstructs

\[
q_{L-1}(h)
\pmod{81^L}
\]

and

\[
\boxed{
h
\equiv
-17^{-1}64^{K-L+1}q_{L-1}(h)
\pmod{81^L}.}
\tag{4}
\]

Therefore `(1)` is a real-location theorem for a low-energy subset of terminal reciprocal residues after multiplication by one explicit unit.

### Lift-digit path

The normalized recurrence is

\[
\boxed{
y_{\ell+1}
=
\frac{\{64y_\ell\}+d_\ell}{81},
\qquad
0\le d_\ell<81.}
\tag{5}
\]

The conjecture asks whether low-energy paths of `(5)` can have too many unusually small least positive frequency representatives.

### Dyadic carry equations

The signed dyadic representatives obey

\[
17h
=
81^{\ell+1}s_\ell
+
64^{K-\ell}m_\ell.
\tag{6}
\]

Eliminating `h` between separated levels produces explicit `{2,3}`-unit relations. An effective height gap may prove `(1)` by classifying the possible low-energy carry templates.

## Proposed proof routes

### Route A — least-representative dispersion

Use `(4)` to show that the low-energy terminal residues cannot all map to small positive integers. A discrepancy or sum-product estimate for multiplication by

\[
64^{K-L+1}\pmod{81^L}
\]

would directly control the harmonic mass.

### Route B — valuation and first-loss stratification

Separate exact initial zero phases caused by powers of `81`, then stratify by the first level at which a phase exits a small degeneracy window. The valuation classes are sparse enough that a modest location theorem may suffice.

### Route C — carry-template classification

Show that a low-energy path has a bounded-complexity lift word. Prove that every such word either reduces by a power of `64` or `81`, is arithmetically impossible, or has a large least representative.

### Route D — positive room-tower operator

Translate the exceptional cylinders into room-wrap paths and prove contraction of interval mass or relative entropy across the inverse-limit tower. This route can use positivity rather than absolute Fourier majorants.

### Route E — rational-diagonal renewal

View `(4)` as a low-height orbit in the dual `{2,3,infinity}` solenoid and prove a shrinking-target theorem uniform in rational height.

## Dependency audit

- `L-9301` supplies the survivor Fourier product.
- `L-9303` supplies the deterministic energy-to-product bound.
- `L-9309` supplies exact prefix cylinders and terminal reconstruction.
- `T-9307` supplies the power-small count of low-energy classes.
- `T-9308` removes the entire high-frequency tail.
- The conjecture itself is open and is not used as a premise in any proved claim.
- No branch-qualified average theorem is required for the stated implication.

## Gap audit

- Power-small cardinality does not imply small harmonic mass.
- The exceptional classes may depend adversarially on `K`.
- Exact-prefix interval amplification is refuted by `R-9301`.
- An arithmetic-progression estimate does not automatically imply a consecutive-interval estimate.
- Density-one depth results do not imply `(1)` for all depths.
- Even full all-depth EQ would not decide whether one infinite ordinary integer lies in the survivor attractor.

## Adversarial tests

1. A single exceptional class with least representative `1` contributes harmonic mass `1`, regardless of how sparse the rest are.
2. Multiplication by powers of `81` creates exact initial zero phases and must be removed before claiming generic energy.
3. Multiplication by powers of `64` gives exact depth self-similarity and can shift the effective problem to a smaller depth.
4. The empty prefix has no entropy deficit; `L_K` must grow.
5. Choosing `H_K` too slowly can make the high tail vanish but leave no useful room for averaging; choosing it too quickly may make harmonic location harder.

## Remaining uncertainty

The central uncertainty is whether terminal-residue multiplication has enough real dispersion uniformly in the depth-dependent unit. The exact entropy theorem strongly suggests that only a thin structured set can fail, but its location—not its count—is the unresolved arithmetic wall.

## Suggested next attack

Prove a first-moment bound for least positive representatives of the low-energy prefix set. Even a weak theorem excluding concentration in `[1,H^epsilon]` for one fixed `epsilon>0` would combine with dyadic shelling and `T-9307` to improve the all-depth low-frequency bound substantially.