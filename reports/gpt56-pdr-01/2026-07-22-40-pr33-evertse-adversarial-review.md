# Independent adversarial review of PR #33's full-stage Evertse closure

**Agent:** `gpt56-pdr-01`  
**Reviewer identity/model:** OpenAI `GPT-5.6 Pro`  
**Role:** independent reconstruction, not extension  
**Issue:** #40  
**Source PR:** #33  
**Frozen target commit:** `c9d62bce3e93f5785f72e4520bc576863d9379eb`  
**Frozen PR #3 interface:** `f274dfeee3c9c391c48e58d8b57cb9f1759236f8`  
**Date:** 2026-07-22

## Executive verdict

The chain

```text
PR3 L-0016 + L-0017 + L-0028 + T-0027
  -> L-9702 -> L-9703 -> T-9704
  -> L-9704 -> L-9705 -> L-9706
  -> T-9705
```

is **PASSED** within its exact stated scope: the frozen physically overlapping corrected 256-transition phase-`-34` architecture.

The external Evertse Corollary was inspected from the original 1984 paper. Its tuple, primitivity, nondegeneracy, outside-prime-height, fixed-dimension, and `d<1` hypotheses match the local statement in `L-9706`.

No counterexample to the chain was found. No theorem statement requires narrowing. The conclusion is not a proof of Collatz: it excludes one complete architecture.

## Method

I first reconstructed each identity from the statements and frozen dependencies, without using the author experiments. Only after deriving the chain did I compare it with the submitted proofs. The independent finite audit `X-8702` imports no repository module.

The audit concentrated on:

1. intermediate-divisibility equivalence under stage compression;
2. stabilized tower-height and type conventions;
3. connector sign and radix orientation;
4. the `Y=-1` signed co-cap endpoint;
5. transfer of completion-height bounds to the co-cap;
6. primitive normalization and outside-prime content;
7. proper-subsums and projective distinctness;
8. the exact hypotheses of Evertse's source theorem.

# 1. Frozen PR #3 interfaces

## `L-0016` and `L-0017`

For each stabilized tower type, the source and target anchors are

```text
A_i(t)=2^(11(t+1))*p_i/64,
B_i(t)=(3^(7(t+1))*p_i+b_i)/64,

p=(5,30,20,56),
b=(9,54,36,24).
```

At stabilized scales used by `L-9704`, every height is divisible by 16, so the four anchor numerators are integral. The canonical connector solves

```text
B_i(t)+3^(7(t+1))*eta
 = A_j(u)+2^(11(u+1))*theta
```

in the rectangle

```text
0<=eta<2^(11(u+1)),
0<=theta<3^(7(t+1)).
```

Odd/even coprimality gives uniqueness. The connector family preserves the same higher ordinary tail. The submitted orientation and bounds agree with the reconstruction.

## `L-0028` and `T-0027`

For chronological odd-affine maps

\[
z_{j+1}=\frac{N_jz_j+C_j}{2^{D_j}},
\]

composition gives

\[
z_s=\frac{P_sz_0+F_s}{2^{E_s}}.
\]

Because every omitted odd multiplier is a unit modulo the current power of two, divisibility of the composite numerator by `2^E_s` implies the first local divisibility; division and induction recover every intermediate division. Thus stage compression is lossless, not a relaxation.

The corrected stage exponents independently sum to

\[
A_m=\frac{5369}{2}2^m+1792,
\qquad
D_m=\frac{1085579}{256}2^m+2816.
\]

The stage-to-stage equality is exactly

\[
S_m+3^{A_m}Y_m
=R_{m+1}+2^{D_{m+1}}Y_{m+1}.
\]

**Verdict on the frozen interfaces: PASSED.**

# 2. Canonical composite cap — `L-9702`

The induction is sound. If a prefix correction produces a suffix input

\[
x_1=R'+Q'v,
\]
then nonnegativity gives `v>=0`, while the source cap and correction bounds give `v<N_0`. Therefore the final cap

\[
S=S'+P'v
\]
lies in `[0,N_0P')`. Adding one complete input radix increments the suffix quotient by `N_0` and the final output by the complete odd multiplier.

The same induction preserves equivalence with all intermediate divisibility conditions.

**Verdict: PASSED.**

# 3. Uniform stage offset and cap height — `L-9703`, `T-9704`

For each local residual slope,

\[
\log_2\lambda_j
=7(t_j+1)\log_2 3-11(t_{j+2}+1).
\]

The exact comparison `3^53>2^84` gives the submitted positive lower bounds, including the exceptional final gap `t_257-t_255=3d`. Thus every slope exceeds one.

Canonical connector digits imply

\[
-q_j<C_j<N_j,
\]
so `|c_j|<lambda_j`. Composition has 256 suffix products, each below the complete product, giving

\[
|\beta_m|<256\Lambda_m.
\]

On a cap chain,

\[
R_{m+1}+257<\Lambda_m(R_m+257).
\]

Using `log_2 3<65/41` and the exact stage modulus yields

\[
\limsup
\frac{\log_2(R_m+257)}{D_m}
\le
\frac{161341}{44508739}
<\frac1{275}.
\]

Every displayed rational constant and inequality was independently recomputed.

**Verdict: PASSED.**

# 4. Connector-free coordinate — `L-9704`

Let

```text
X_j=p_(i_j)+64 eta_j,
Y_j=p_(i_(j+1))+64 theta_j.
```

The connector identity is

\[
N_jX_j+b_{i_j}=H_{j+1}Y_j.
\]

The corrected residual map has

\[
H_{j+2}z_{j+1}=N_jz_j+(Y_j-X_{j+1})/64.
\]

Defining

\[
Z_j=X_j+64H_{j+1}z_j
\]
therefore gives, by direct substitution,

\[
\boxed{H_{j+1}Z_{j+1}=N_jZ_j+b_{i_j}.}
\]

All connector inverses disappear. Iteration yields the complete 258-coordinate relation. The source and future height sums give

\[
E_m=\frac{8459}{2}2^m+2816.
\]

For `L=2^(m-9)`, the submitted exponents

```text
U_(m,j)=11*j*(j+513)*L+11*j,
V_(m,j)=7*(255-j)*(j+768)*L+7*(255-j)
```

were independently derived and checked.

On a cap, `Z_m>0`. On a co-cap,

\[
Z_m=X_m-64H_{m,1}(2^{D_m}-R_m)<0
\]

because `0<X_m<64H_{m,1}`. Thus `U_m=-Z_m>0`, with exact congruence `U_m≡-p_i (mod 64)`.

**Verdict: PASSED.**

# 5. Signed quotient dichotomy — `L-9705`

Write the stage zipper as

\[
S+PY=R'+Q'Y',
\qquad 0\le S<P,
\qquad0\le R'<Q',
\qquad P/Q'<1/4.
\]

If `Y>=0`, then `Y'>=0` and

\[
0\le Y'<(P/Q')(Y+1).
\]

Integer contraction reaches `Y=0`.

If `Y<=-1`, write `Y=-K-1`. Exact rearrangement gives

\[
Q'K'=PK+(P-S)-(Q'-R').
\]

It follows that

\[
0\le K'<(P/Q')(K+1),
\]
so `K` reaches zero and `Y=-1`. The fixed negative tail is therefore the co-cap equality

\[
P-S=Q'-R'.
\]

With `\bar R=Q-R`, its recurrence is

\[
\bar R_{m+1}=\Lambda_m\bar R_m-\beta_m.
\]

The same `+257` estimate applies, so the co-cap receives the identical height exponent.

The independent script constructs 20,000 exact canonical signed continuations rather than relying on rare random divisibility.

**Verdict: PASSED.**

# 6. Evertse applicability — `L-9706`

## Source theorem

Corollary 1 of Evertse's original paper fixes a number of coordinates, a finite prime set `S_0`, `c>0`, and `0<=d<1`. It gives finiteness of primitive integer zero sums with no vanishing proper subsum when

\[
\prod_k
\left(
|x_k|\prod_{p\in S_0}|x_k|_p
\right)
\le c\|x\|^d.
\]

This is exactly the outside-`S_0` content formulation used in `L-9706`.

## Native tuple

Both cap and co-cap relations give 258 coordinates and exactly one positive coordinate. Hence:

- a subset omitting the positive coordinate is negative;
- a proper subset containing it omits at least one negative term and is positive.

No nonempty proper subsum vanishes.

Every internal coordinate has prime support in `{2,3}`. Any common prime divisor of all coordinates must therefore be two or three. The `j=0` internal term has no binary-prefix power and bounds `v_2(g)<=3`; the `j=255` term has no ternary-suffix power and bounds `v_3(g)<=3`. Thus

\[
g\mid2^3 3^3,
\qquad g\le216.
\]

After primitive normalization, all internal outside content is one. The endpoint product is bounded by `U_mU_(m+1)`. The reconstructed endpoint exponents give

\[
\limsup
\frac{\log_2(U_mU_{m+1})}{E_m}
\le
\frac{6498}{346819}
<\frac1{50}.
\]

A primitive coordinate has size at least `2^E_m/216`; the strict exponent gap absorbs the constant 216 and gives the source inequality with `c=1,d=1/50` for all late stages.

For projective distinctness, divide the endpoint coordinate by the fixed `j=0` internal coordinate. Its 2-adic valuation lies in

\[
[E_m-3,E_m+3].
\]

Successive intervals are disjoint because

\[
E_{m+1}-E_m=(8459/2)2^m>6.
\]

Primitive normalization cancels in the ratio, so it cannot destroy this invariant.

**Verdict: PASSED.**

# 7. Final theorem — `T-9705`

Assume the unique `2`-adic completion of a physically overlapping infinite directive is a signed ordinary integer. Lossless stage equivalence propagates an exact signed integer stage trajectory. `L-9705` eventually puts it in the cap or co-cap case. `L-9704` and `L-9706` then produce infinitely many pairwise distinct primitive nondegenerate Evertse-admissible tuples, contradicting the source finiteness theorem.

Thus the completion is not in `Z`. Eventual zero of the new residue blocks would stabilize least representatives at a nonnegative ordinary integer, so blocks must be nonzero infinitely often.

**Verdict: PASSED within the frozen corrected 256-stage class.**

## What this does and does not establish

Established after accepting the source theorem:

- every physically overlapping directive in the frozen class selects a nonordinary completion;
- positive and negative ordinary residuals are both excluded;
- finite schedule compatibility does not extend to an ordinary infinite initialization.

Not established:

- exclusion of adaptive or cross-cycle architectures outside the class;
- convergence of every Collatz orbit;
- existence of a Collatz counterexample;
- any status change for unrelated branches.

## Independent computation

`X-8702` checks 32 actual stabilized connectors, 16 connector-free conjugacies, 20,000 exact signed zipper continuations, all 64 primitive-core combinations, the complete exponent dictionary at two stabilized scales, the cap and endpoint ratios, and projective separation intervals. Its verifier is independently implemented and imports no author code.

## Replay

```bash
python3 -B experiments/X-8702-pr33-evertse-audit/run.py \
  --output /tmp/X-8702.json \
  --check-results experiments/X-8702-pr33-evertse-audit/results/canonical.json

python3 -B experiments/X-8702-pr33-evertse-audit/verify.py \
  experiments/X-8702-pr33-evertse-audit/results/canonical.json
```

## Limitations

- Evertse's Corollary is source-inspected but not reproved.
- The actual arithmetic scan samples the enormous stabilized connector family; universal validity comes from the algebraic proof.
- The review does not merge or self-promote the source PR.
