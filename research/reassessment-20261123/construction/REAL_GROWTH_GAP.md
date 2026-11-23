# The actual-source boundary stream has an exponential growth gap

23 November 2026. Author: `source_construction`.

**Status: PROPOSED written quantitative consequence and attempted central
construction. No universal upper bound or Collatz proof is obtained.**
The boundary stream and its defect identities below are inherited from
PR178. The new deduction is that, at one fixed positive ordinary source,
failure to reach the standard cycle forces exponential growth of the
stream's running real maximum. Boundedness is already enough for exact
stabilization; denominator bounds are not needed for this implication.

This was an attempt to use the simultaneous original and complementary
carries to construct a witness. The attempt stops at a specific missing
real upper estimate. It does not count a new formulation of that estimate
as its proof, or claim a faster algorithm than following the original orbit.

## 1. One ordinary source and the inherited complete carries

Fix `n>=1`, set `x_k=T^k(n)` for the shortcut map, and write
`e_k=x_k mod 2`, `p_k=sum_(j<k)e_j`, `b_k=k-p_k`. Let

\[
C_0=D_0=0,\qquad
C_{k+1}=3^{e_k}C_k+e_k2^k,\qquad
D_{k+1}=3^{1-e_k}D_k+(1-e_k)2^k.
\]

Use the actual terminal parity to choose the two standard-cycle values:

\[
c_k=1+e_k,\qquad d_k=2-e_k,\qquad
\eta_k=\frac{2^kc_k-D_k}{3^{b_k}},\qquad
\xi_k=\frac{2^kd_k-C_k}{3^{p_k}}.
\tag{1}
\]

PR178, commit `c91b80a3156e640ad471cf30c47721145ae21eb1`,
`research/profound-step-20261123/arithmetic/TRIADIC_CONSTRUCTION_ATTEMPT.md`,
equations (4)--(9), supplies these definitions and proves, for
`sigma_k=e_k+e_(k+1)-1`,

\[
\eta_{k+1}-\eta_k=\frac{2^{k+1}\sigma_k}{3^{b_{k+1}}},\qquad
\xi_{k+1}-\xi_k=-\frac{2^{k+1}\sigma_k}{3^{p_{k+1}}}.
\tag{2}
\]

A defect means `sigma_k!=0`, namely an actual `00` or `11` pair. The
same source supplies every prefix. Each `eta_k` matches its first `k+1`
complementary bits, but it is a changing candidate. Once the orbit reaches
the standard cycle, these candidates become exactly constant. None of
these inherited statements is counted as new here.

Put `N=bl(n)`, the least positive integer with `n<2^N`, and

\[
M_K=\max_{0\le j\le K}|\eta_j|,\qquad
\alpha=\frac{\log(4/3)}{\log3}>0.
\tag{3}
\]

This `M_K` is a real-amplitude maximum of the single canonical stream.
It is not the earlier optimization over all triadic candidates. In
particular `M_K>=1`, since `eta_0` is either one or two.

## 2. Every late defect has a large real jump

**Lemma 1.** If `t>=1` and `sigma_(t-1)!=0`, then

\[
\boxed{3^N|\eta_t-\eta_{t-1}|^2\ge(4/3)^t.}
\tag{4}
\]

**Proof.** A positive odd step satisfies `T(x)<=2x`; an even step is
exact halving. Multiplying these literal bounds gives

\[
x_t2^{b_t}\le n2^{p_t}.
\]

Since `x_t>=1` and `n<2^N`, we obtain `b_t<=p_t+N` and hence
`2b_t<=t+N`. At a defect, (2) gives

\[
|\eta_t-\eta_{t-1}|^2
=\frac{4^t}{3^{2b_t}}
\ge\frac{4^t}{3^{t+N}}.
\]

This proves (4). Positivity of the unchanged ordinary source is used in
the count inequality. It cannot be replaced by arbitrary finite parity
words with changing ordinary realizers. `QED`.

## 3. A nonterminal prefix must have a sufficiently late defect

**Lemma 2.** Suppose `K>=N` and none of `x_0,...,x_K` belongs to
`{1,2}`. There is a last defect `h-1` in `0,...,K-1`, and

\[
\boxed{2^{K+1}<(n+1)3^h.}
\tag{5}
\]

**Proof.** Let `h` be one plus the last defect index, or let `h=0` if
there is no defect. The parities at clocks `h,...,K` alternate. Thus
`x_h` has the same first `K-h+1` parity bits as `d_h`, the standard-cycle
value with its parity. Finite parity coding gives

\[
2^{K-h+1}\mid x_h-d_h.
\]

Here `x_h>d_h`: the source is positive and the prefix avoids both core
states. Therefore `x_h>=d_h+2^{K-h+1}`.

The literal map also satisfies

\[
T(x)+1\le\tfrac32(x+1)\qquad(x\ge1),
\]

so `x_h+1<=(n+1)(3/2)^h`. Combining the two estimates gives (5).
If `h=0`, this would say `2^(K+1)<n+1<=2^N`, contrary to `K>=N`.
Thus a defect exists and `h>=1`. No assumption about the parity word
after clock `K` was used. `QED`.

## 4. A finite quantitative gap and its all-time consequence

**Theorem 3.** Under the hypotheses of Lemma 2,

\[
\boxed{
M_K>
\frac1{2\,3^{N/2}}
\left(\frac{2^{K+1}}{n+1}\right)^{\alpha/2}.}
\tag{6}
\]

**Proof.** Both sides of the jump at the last defect occur among the
indices defining `M_K`, so `2M_K>=|eta_h-eta_(h-1)|`. Lemma 1 gives
`4M_K^2 3^N >= (4/3)^h`. Raising (5) to the positive exponent
`alpha=log_3(4/3)` and taking square roots proves (6). `QED`.

Consequently, if the fixed positive source never reaches the standard
cycle, then

\[
\boxed{
\liminf_{K\to\infty}\frac{\log M_K}{K}
\ge\frac{\log2\,\log(4/3)}{2\log3}>0.}
\tag{7}
\]

Conversely, a convergent source has an eventually constant boundary
stream, and hence bounded `M_K`. Thus for this literal stream,

\[
\begin{aligned}
n\text{ reaches }1
&\iff (\eta_k)\text{ is bounded in the real absolute value}\\
&\iff M_K=\exp(o(K)).
\end{aligned}
\tag{8}
\]

The running maximum is essential to the proof: individual jumps can
have opposite signs, and no pointwise lower bound for every `|eta_K|`
is asserted. The theorem controls real amplitude, not numerator height
or the uncancelled exponent of three.

For the escaping case, one can strengthen (7). Monks--Yazinski's
Theorem 2.7(b) gives `liminf p_t/t>=log_3 2` for a divergent rational
orbit. Hence (2) implies, at defect clocks,

\[
\log|\eta_t-\eta_{t-1}|\ge t\log(4/3)-o(t).
\]

Using the same late defect from Lemma 2 yields

\[
\boxed{
\liminf_{K\to\infty}\frac{\log M_K}{K}
\ge\frac{\log2\,\log(4/3)}{\log3}}
\tag{9}
\]

for an escaping positive orbit. This stronger bound is not applied to
a hypothetical nontrivial positive cycle.

## 5. Why the simultaneous-carry attempt does not yet bound the stream

The known original-source identity is

\[
n-\xi_k=\frac{2^k(x_k-d_k)}{3^{p_k}}\ge0.
\tag{10}
\]

It bounds `xi_k` above by the same ordinary `n`, but does not give an
upper bound for `eta_k`. At every defect the inherited exact relation is

\[
(\xi_{k+1}-\xi_k)(\eta_{k+1}-\eta_k)=-(4/3)^{k+1}.
\tag{11}
\]

Thus replacing the second carry by a small difference of the first
does not provide simultaneous small increments. Lemma 1 makes the
consequence quantitative at the actual positive source.

The fresh PR176 fixed-source adelic attempt was inspected at
`4171e1fe40e41842af9f800bd821084b724cf8f9`,
`research/lean-global-resolvent-20261121/overview/source-construction/INFINITE_OPTIMAL_RAY_ATTEMPT.md`.
Its product at `(3^k,C_k)`, including the real, binary and ternary
places, is exactly the later correction `S(q_k)>=1`. Even its additional
algebraicity premise would not give the strict negative-power height
saving required by that Subspace-Theorem test. This prior obstruction
is credited, not proved again or strengthened here. I obtained no
different two-carry approximation that supplies an upper bound
contradicting (7).

The direct missing estimate is explicit: prove, for every fixed
positive `n`, an upper bound on this actual running maximum whose
exponential rate is strictly below the constant in (7). In particular,
`M_K=exp(o(K))` would suffice. Equation (8) shows that this is an
equivalent unresolved task, not an independently established regularity
property. It has not been inferred from averaging over other sources,
from rational approximation without the source-height budget, or from
boundedness of an unrelated real boundary law.

## 6. The polynomial formulation uses the same parity defects

Monks's 2025 paper considers the map `T_(1,1+z^2)` on `F_2[[z]]` and
its parity-preserving conjugacy `H` with the ordinary Collatz map.
Unrolling its affine branches gives directly

\[
H(n)=(1+z^2)\sum_{k\ge0}e_kz^k.
\tag{12}
\]

Its coefficient at `k>=2` is `e_k+e_(k-2)` in `F_2`. Equivalently it
is `sigma_(k-1)+sigma_(k-2)` modulo two. Thus the polynomial target
tracks the same eventual parity defects. For a positive source that
first hits one at `tau`, the terminal `4,2,1` segment gives
`deg H(n)=tau`; the inputs one and two give degrees zero and one.
This is an elementary interpretation of the paper's polynomiality
criterion, not a new polynomiality theorem or a recurrence construction.
No implication from finite ordinary binary support to finite support
of (12) was obtained.

## Evidence boundary

All new conclusions here have written-proof scope. The prior finite
boundary recurrences already have their separate Lean module and audit;
they were not rebuilt. No new Lean declaration, numerical census,
universal upper bound, witness selector, or full Collatz theorem is
claimed. The accompanying source ledger records immutable repository
inputs and the primary-paper sections actually inspected.
