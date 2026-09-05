# L-9803 — Completion–height wedge

Claim ID: `L-9803`  
Title: One product-formula wedge controls both zero-carry runs and repeated survivor blocks  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: none  
Scope: coprime expanding radix pairs `1 < M < N`  
Related counterexample candidates: none

## Definitions

All logarithms are real logarithms; `log_M` denotes logarithm to base `M`.
Divisibility is ordinary integer divisibility, and `|z|` is the usual
archimedean absolute value. The parameters `delta` and `kappa` below are the
reciprocal critical slopes associated with the expanding pair `M<N`.

## Statement

Let `1<M<N` and define

\[
\delta=\log_M(N/M),
\qquad
\kappa=\frac1\delta
=\frac{\log M}{\log(N/M)}.
\tag{1}
\]

Let `z` be a nonzero ordinary integer.

### 1. Completion run versus terminal height

Suppose `b,r,t` are nonnegative integers, `0<theta<1`, `H>0`, and

\[
N^{b+r}\mid z,
\qquad
|z|\le \theta N^bM^{r+t}+H.
\tag{2}
\]

Then either

\[
\boxed{N^r\le\frac{H}{1-\theta}}
\tag{3}
\]

or

\[
\boxed{r<\kappa t}.
\tag{4}
\]

### 2. Repetition length versus rational height

Suppose `t,ell` are nonnegative integers and

\[
M^{t+\ell}\mid z,
\qquad
|z|<HN^t.
\tag{5}
\]

Then

\[
\boxed{
\ell<\delta t+\log_M H.
}
\tag{6}
\]

The slopes in (4) and (6) are reciprocal. This is the structural reason the
same constant

\[
\kappa=\frac1{\log_MN-1}
\tag{7}
\]

appears in both `PR16/L-9310` completion-height carry rigidity and
`PR20/T-9401`--`T-9402` ordinary-code repetition rigidity.

## Proof

Since `N^(b+r)` divides the nonzero integer `z`,

\[
N^{b+r}\le|z|.
\]

Combining this with (2) and dividing by `N^b` gives

\[
N^r\le\theta M^{r+t}+H.
\tag{8}
\]

If (3) fails, then `H<(1-theta)N^r`. Substitution in (8) yields

\[
\theta N^r<\theta M^{r+t},
\]

so `N^r<M^(r+t)`. Taking logarithms gives

\[
r\log(N/M)<t\log M,
\]

which is (4).

For part 2, divisibility and nonvanishing give

\[
M^{t+\ell}\le|z|<HN^t.
\]

After taking logarithms to base `M` and subtracting `t`,

\[
\ell<t(\log_MN-1)+\log_MH
=\delta t+\log_MH.
\]

This proves (6). ∎

## Carry-rigidity specialization

For completeness, assume additionally that `gcd(M,N)=1`, and consider signed
residues

\[
s_j\equiv-chM^{j-K}\pmod{N^{j+1}},
\qquad
|s_j|\le\frac12N^{j+1},
\]

with `gcd(c,M)=1` and `M` not dividing `h`; negative powers of `M` denote
modular inverses. Put `x_j=s_j/N^(j+1)` and

\[
a_j=Mx_j-Nx_{j+1}.
\]

If `r>=1` adjacent carries vanish starting at level `ell`, put
`t=K-ell-r>=1`. Exact vanishing gives
`s_(ell+r)=M^r s_ell`. The cross-numerator

\[
Z=M^{K-\ell}s_\ell+ch
\]

is divisible by `N^(ell+r+1)` and is nonzero: equality to zero would force
`M` to divide `h`. Its signed-representative height satisfies

\[
|Z|\le\frac12N^{\ell+1}M^{r+t}+|ch|.
\]

Part 1 with `b=ell+1`, `theta=1/2`, and `H=|ch|` gives the sharper dichotomy

\[
N^r\le2|ch|
\quad\text{or}\quad
r<\kappa t.
\tag{9}
\]

This reconstructs the load-bearing zero-run squeeze in `PR16/L-9310`.

## Repetition-rigidity specialization

When a common radix-`M` prefix of length `t+ell` makes the nonzero
cross-numerator between an ordinary value and an odd-denominator periodic
approximant divisible by `M^(t+ell)`, while the approximant's denominator and
ordinary height give `|z|<HN^t`, part 2 yields (6). Pigeonhole inversion turns
the slope `delta` into the factor-complexity lower slope `kappa`.

The two applications use different mathematical objects. The lemma explains
their shared constant; it does not identify Fourier-frequency digits with a
survivor itinerary.

## Motivation

Strong agreement in a completion is useful only while its required
divisibility remains compatible with ordinary archimedean height. Parts 1 and
2 are the two orientations of that same constraint.

## Dependency audit

The proof uses only

\[
Q^d\mid z,\ z\ne0\Longrightarrow Q^d\le|z|.
\]

The branch specializations are explanatory corollaries and are not proof
dependencies.

## Gap audit

- The lemma does not couple the frequency parameter `h` in PR #16 to the
  survivor digit sequence in PR #20.
- The nonzero cross-numerator condition is essential.
- A height estimate with an uncontrolled `H` can make the conclusion vacuous.
- This is a finite quantitative obstruction, not an ordinary-section theorem.

## Adversarial tests

- At `theta=1`, part 1 loses its wedge; the strict energy gap is essential.
- If `z=0`, arbitrarily long agreement is possible and both conclusions can
  fail.
- Setting `M=64,N=81` gives `kappa=17.654847577085...`, matching both source
  packets.

## Remaining uncertainty

None in the abstract lemma. A direct complexity–carry incompatibility still
needs a proved coupling between the two source objects.

## Suggested next attack

Find a Collatz-specific cross-numerator in which the same ordinary survivor
simultaneously controls a carry-zero run and a repeated itinerary block.
