# L-9888 -- The cap-stitch defect is an isometric Hensel block

Claim ID: `L-9888`
Title: The two-cell cross-stage mismatch survives Montgomery normalization with its exact valuation
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-c`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `L-9876`, `L-9887`, `PR33/L-9702`, `PR33/T-9704`
Scope: the two-cell terminal/head boundary isolated by `L-9887`
Related counterexample candidates: none

## Setup

At the boundary from stage `m` to `m+1`, put

\[
N=N(T_m),
\qquad
Q=Q(H_{m+1})=2^D,
\tag{1}
\]

\[
s=S(T_m),
\qquad
r=R(H_{m+1}),
\qquad
d=r-s.
\tag{2}
\]

Canonical bounds and the collar estimates give

\[
0\le s<N<Q,
\qquad
0\le r<Q.
\tag{3}
\]

Define the cross-boundary correction and output quotient

\[
\boxed{
a=[dN^{-1}]_Q,
\qquad
b={Na-d\over Q}={s+Na-r\over Q}.
}
\tag{4}
\]

## Statement 1 -- exact boundary tile

The data in (4) satisfy

\[
\boxed{s+Na=r+Qb,}
\tag{5}
\]

\[
\boxed{0\le a<Q,\qquad0\le b<N.}
\tag{6}
\]

Moreover,

\[
\boxed{
a=0
\iff d=0
\iff s=r.
}
\tag{7}
\]

For completeness, the output-quotient zero case is instead

\[
\boxed{
b=0
\iff d\ge0\text{ and }N\mid d
\iff r\ge s\text{ and }r\equiv s\pmod N,
}
\tag{7a}
\]

and then `a=d/N` may be positive.

Thus no final Montgomery normalization can turn a nonzero raw mismatch into a
zero stitch correction. The output quotient `b` need not be nonzero when
`d` is nonzero; it is not part of equivalence (7).

### Proof

The congruence defining `a` makes `b` integral and proves (5). If `a=0`, then
`Q` divides `d`. But (3) gives

\[
-Q<d<Q,
\tag{8}
\]

so `d=0`. The converse is immediate.

If `a>0`, the numerator `Na-d` is a multiple of `Q` strictly greater than
`-Q`, hence is nonnegative. The case `a=0` was just shown to have numerator
zero. Finally,

\[
s+Na-r<N+N(Q-1)=NQ,
\tag{9}
\]

so `b<N`. Finally, `b=0` is exactly `Na=d`; with `a>=0` this is equivalent to
(7a), and the canonical correction is then `a=d/N`. This proves (6)--(7a).
**QED**

## Statement 2 -- one-bit Hensel recurrence

For `0<=k<=D`, put

\[
a_k=[dN^{-1}]_{2^k},
\qquad
b_k={Na_k-d\over2^k}.
\tag{10}
\]

Start with

\[
a_0=0,
\qquad
b_0=-d,
\tag{11}
\]

and let

\[
\epsilon_k=[b_k]_2\in\{0,1\}.
\tag{12}
\]

Then

\[
\boxed{
a_{k+1}=a_k+2^k\epsilon_k,
\qquad
b_{k+1}={b_k+N\epsilon_k\over2}.
}
\tag{13}
\]

At full precision, `a_D=a` and `b_D=b`. If `d!=0`, then

\[
\boxed{v_2(a)=v_2(d).}
\tag{14}
\]

More generally, for any signed mismatches `d,d'`,

\[
\boxed{
\min\{v_2(a(d)-a(d')),D\}
=
\min\{v_2(d-d'),D\}.
}
\tag{15}
\]

Thus `d -> [dN^(-1)]_(2^D)` is a truncated `2`-adic isometry.

### Proof

Because `N` is odd and `epsilon_k=b_k mod2`, the numerator in the second
formula of (13) is even. Direct substitution in (10) proves both recurrences.

If `v=v_2(d)<D`, then `a_k=0` through `k=v`. At that point

\[
b_v=-d/2^v
\tag{16}
\]

is odd, so (13) gives `a_(v+1)=2^v`; subsequent lifts preserve that lowest
one bit. This proves (14). Equation (15) follows directly because
multiplication by the odd unit `N^(-1)` preserves truncated valuation. **QED**

## Statement 3 -- cusp-height certification

Suppose two candidate boundary values obey

\[
0\le r,s<2^h\le Q.
\tag{17}
\]

Then

\[
\boxed{
a=0
\iff
a\equiv0\pmod {2^h}.
}
\tag{18}
\]

Indeed, the isometry makes the right side equivalent to `d=0 mod2^h`, while
`|d|<2^h` forces exact equality.

For an actual `PR33/T-9704` cap chain define

\[
\mathcal H_m
=
\left\lceil
\log_2(R_M+257)
+\gamma(2^{m+1}-2^M)
+c_0(m+1-M)
\right\rceil,
\tag{19}
\]

where

\[
\gamma={161341\over10496},
\qquad
c_0={1024\over41}.
\tag{20}
\]

The chain equality makes

\[
r=s<2^{\mathcal H_m}.
\tag{21}
\]

The full next-head precision is

\[
D={5687\over128}2^m+22,
\tag{22}
\]

whereas

\[
\mathcal H_m={161341\over5248}2^m+O_M(m).
\tag{23}
\]

Their exact leading gap is

\[
\boxed{
{5687\over128}-{161341\over5248}
={35913\over2624}.
}
\tag{24}
\]

Consequently exact stitch equality on a hypothetical chain is certified by
only its first `H_m` defect bits, leaving

\[
\boxed{
{35913\over2624}2^m-O_M(m)
}
\tag{25}
\]

unused high precision bits. A scale-stable nonzero low defect bit below this
certification depth would exclude every cap chain.

## Statement 4 -- generic synchronous state cost

For a fixed odd positive integer `N`, the all-precision isometry

\[
F_N(x)=N^{-1}x
\quad\text{on }\mathbb Z_2
\tag{26}
\]

has exactly `N` rooted-tree sections. More precisely, for an input prefix
`p` of length `k`, let `r` be its output prefix and write

\[
Nr=p+2^kt,
\qquad0\le t<N.
\tag{27}
\]

Then

\[
\boxed{F_N|_p(z)={z-t\over N}.}
\tag{28}
\]

Once `2^k>=N`, every `t in {0,...,N-1}` occurs and the sections are distinct.

For the truncated `D`-bit map, put

\[
k=\lceil\log_2N\rceil,
\qquad L=D-k.
\tag{29}
\]

If `2^L<=N`, every synchronous least-significant-first transducer computing
the unrestricted map through all `D` bits needs at least

\[
\boxed{2^{D-\lceil\log_2N\rceil}}
\tag{30}
\]

states. At depth `k`, all `N` carries occur, and at least `2^L` of their
residual functions are distinct modulo the remaining `2^L` output precision.

For the two-cell collar,

\[
N=3^{(7147/256)2^m+14}.
\tag{31}
\]

Using `log_2(3)<65/41`,

\[
D-\lceil\log_2N\rceil
>
{1779\over10496}2^m-{8\over41}-1.
\tag{32}
\]

The lower bound for `log_2 N` in `L-9887/(20)` also gives
`D-ceil(log_2 N)<=log_2 N` for `m>=8`, so the condition `2^L<=N` holds.

Hence the generic unrestricted normalization requires at least

\[
\boxed{
2^{(1779/10496)2^m-O(1)}
}
\tag{33}
\]

states. A bounded physical controller must therefore exploit a structural
identity in the mismatch language; it cannot implement the final Montgomery
inverse as a generic bounded component.

### Proof of the section count

Substitute

\[
x=p+2^kz,
\qquad
F_N(x)=r+2^kw
\tag{34}
\]

into `NF_N(x)=x`. Equation (27) gives `w=(z-t)/N`, proving (28). For fixed
`t`, the interval

\[
{2^kt\over N}\le r<{2^k(t+1)\over N}
\tag{35}
\]

has length at least one when `2^k>=N`, so every carry occurs. Distinct `t`
give distinct affine sections. The truncated count follows by reducing those
sections modulo `2^L`. Equation (32) is the exact difference between (22) and
the elementary upper bound for (31). **QED**

## What this advances

- `L-9887/(7)` is now the single raw equality `d=0`; Montgomery division
  preserves every nonzero mismatch valuation.
- Only cusp-height many low bits are needed to certify exact equality on a
  hypothetical chain, far fewer than the full head modulus.
- `L-9876`'s infinite-section obstruction becomes quantitative for the
  unrestricted boundary inverse.
- The unresolved work is structural nonvanishing of `R(H_(m+1))-S(T_m)`, not
  carry bookkeeping after that difference is formed.

## Dependency audit

- `L-9887` supplies the two-cell boundary and the inequalities in (3).
- `PR33/L-9702` supplies canonical cap bounds.
- `PR33/T-9704` supplies the cusp-height budget (19).
- `L-9876` supplies the rooted-tree-section context; the exact section count
  is rederived here.
- No finite experiment is a proof dependency.

## Gap audit

- No physical mismatch is proved nonzero.
- The state lower bound is for unrestricted mismatch inputs. A sparse physical
  language can be easier if it satisfies a special identity.
- Low-bit certification assumes both candidates lie below the same cusp-height
  bound; this holds under the hypothesized chain equality and is not asserted
  for arbitrary terminal caps.
- The 252-cell middle bridge from `L-9887` remains independent.
- The adaptive `PR3/T-0029` prefix router exposes only `O(m)` bits; it could
  still help by forcing a symbolic identity, but coverage alone is below the
  `Theta(2^m)` certification depth.

## Adversarial checks

- The implication `b=0 => d=0` is false in general and is deliberately not
  claimed; only the input correction `a` detects exact stitching.
- Signed negative mismatches are allowed in (4) and throughout the Hensel
  recurrence.
- A nonzero mismatch has valuation below `D` because `|d|<Q`.
- Ceiling the logarithm in (29) costs the explicit final `-1` in (32).

## Remaining uncertainty

Does every physically compatible boundary pattern have a nonzero defect bit
below `H_m`, uniformly in scale? Exact two-cell evaluations suggest a small
modulus may suffice, but no finite observation is extrapolated here.

## Suggested next attack

Derive the scale recurrence of `d_m mod 2^h` for each boundary-symbol pattern.
A proof that its first nonzero Hensel digit persists under scale doubling would
exclude every cap-correction chain.
