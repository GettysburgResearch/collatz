# A quadratic height payment under an imported reciprocal bound

23 November 2026. Author: `actual_collision`.

**Status: PROPOSED written deductions, with a primary renewal theorem
applied to its specified iid model and explicit source-qualified
ordinary-trace hypotheses. Collatz and the actual collision upper remain
OPEN. No new infinite theorem in this packet is claimed as Lean-checked.**

The literature supplies a more precise model-to-ordinary interface than
an unspecified point conditioning: the canonical real fibre is a
**trace-weighted Cesaro limit**. The new estimate below shows that this
interface has a compulsory height cost along one original escaping
orbit, under a separate source-qualified hypothesis.

**Separate imported hypothesis for every uniform square-height conclusion:**
the one fixed ordinary source satisfies
`Lambda_* = inf_j product_(i<j) 3q_i/(3q_i+1) > 0`, as in (18).
This packet does not derive that reciprocal-summability input from
escape alone. Without it, the finite original-cylinder lower bound
(17) remains exact, with its full factor `Lambda_j`.

Under that hypothesis, if a finite average through ternary depth `M` approximates its
canonical unnormalized real fibre at ordinary height `q` with `o(q)`
error in the explicit scaled bounded test below, it must pay

\[
\boxed{\frac{3^M}{M}\gtrsim q^2.}
\tag{1}
\]

The implicit constant depends on the one initial ordinary source and its
stated trace data, not on the moving position along that source's orbit.
The proof combines an exact original-prefix contribution with the
`1/x` real tail of the fair affine model. It does not change the ordinary
source with the horizon or replace the trace by an iid path law.

## 1. The two laws and the literature interface

Use the odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd units modulo three. The **model** has independent gaps
`P(G=e)=2^(-e)`, and its common real/ternary series is

\[
R=\sum_{i\ge1}3^{i-1}2^{-(G_1+\cdots+G_i)}\in(0,\infty),\qquad
Y=\sum_{i\ge1}3^{i-1}2^{-(G_1+\cdots+G_i)}\in\mathbb Z_3^\times.
\tag{2}
\]

Write `nu` for this joint probability. It is the model in frozen PR180
`FOURIER_BRIDGE.md`; no ordinary orbit is sampled from it. For a positive
odd unit `q`, let

\[
\eta_m^q(dR)=3^m\nu(dR,\ Y\in q+3^m\mathbb Z_3),\qquad
F_m(q)=\eta_m^q(\mathbb R),\qquad
\overline\eta_M^q=\frac1M\sum_{m=1}^M\eta_m^q.
\tag{3}
\]

These are finite measures, not separately normalized probabilities.

The **ordinary law** is the retained canonical trace law. Its positive
finite harmonic trace `h` has kernel

\[
h(v)=\sum_{Ux=v}3\,2^{-e(x)}h(x),\qquad
K_h(v,x)=3\,2^{-e(x)}\frac{h(x)}{h(v)}.
\tag{4}
\]

Only legal positive odd unit parents occur in these sums. Its inverse
path from `q` has real boundary law `mu_q`, with the exact prefix
probability and identity

\[
\mathbb P_q(W_r=w)=a_w\frac{h(n)}{h(q)},\qquad
q=R_w+a_w n,\quad a_w=3^r2^{-A_w}.
\tag{5}
\]

All prefix terms are positive, so every continuation has real boundary
at least `R_w` and at most `q`. The full carry is contained in `R_w`;
it is never replaced by its residue.

Lyapunov Weaver's primary manuscript
[*Geometry, integer fibres, and dyadic equidistribution of the joint
Collatz affine law*, v2](https://rstation.ai/api/v1/papers/collatz_19/versions/2/download),
Section 9.2, gives the source-qualified interface

\[
\boxed{\overline\eta_M^q\Longrightarrow h(q)\mu_q
\quad\text{for each fixed }q.}
\tag{6}
\]

Its normalization is the actual trace mean
`M^(-1) sum_(m<=M) F_m(q)`, tending to `h(q)`. The proof leaves one
terminal ternary digit in the unused tail, which discards endpoints
divisible by three, and uses the retained bounded selection identity.
We inspected that argument; the imported trace existence and selection
theorems remain source-qualified. There is no individual-depth limit or
root-uniform rate in (6).

The new results below require (4)--(5) and the stated ordinary prefix
data. They do **not** assume (6) has a rate or prove a new trace-existence
theorem.

## 2. The exact real-tail constant of the specified model

The real variable in (2) also satisfies

\[
R\overset d=AR'+B,\qquad
(A,B)=\begin{cases}(1/2,0)&\text{with probability }1/2,\\
(3/2,1/2)&\text{with probability }1/2,
\end{cases}
\tag{7}
\]

where `R'` is independent of `(A,B)` and has the same law as `R`.
The mean logarithmic multiplier is negative, so the affine series
converges almost surely. For every `0<s<1`, strict concavity gives
`E A^s< (E A)^s=1`; subadditivity and the series yield

\[
\mathbb E R^s\le
\frac{\mathbb E B^s}{1-\mathbb E A^s}
=\frac1{2^{1+s}-1-3^s}<\infty.
\tag{8}
\]

**Proposition 1 (renewal-tail application).** For this precise model,

\[
\boxed{
\lim_{x\to\infty}x\mathbb P(R>x)
=\frac1{\log(27/16)}.}
\tag{9}
\]

In particular there is a finite universal constant `K_R` such that

\[
\mathbb P(R\ge x)\le K_R/x\qquad(x>0).
\tag{10}
\]

**Verification of the literature hypotheses.** Apply the one-child,
exponent-one specialization of Jelenkovic--Olvera-Cravioto,
[*Implicit renewal theory and power tails on trees*](https://molvera.web.unc.edu/wp-content/uploads/sites/19443/2019/01/Jelenkovic_Olvera_WBP_AAP_final.pdf),
Theorem 3.1, with `N=1`, `C_1=A`, and `alpha=1`. This is the
classical implicit-renewal mechanism of Goldie. The author-hosted primary
theorem and its hypotheses were directly inspected.

Here `E A=1`, all required subunit moments of `R` are finite by (8),
and the coefficient moments are finite. The renewal drift is

\[
\mathbb E(A\log A)=\frac{3\log3-4\log2}{4}>0.
\tag{11}
\]

The tilted logarithmic increment is nonarithmetic: if
`E[A exp(it log A)]=1`, both positive-weight phases must equal one.
Then `t log2` and `t log3` are integer multiples of `2 pi`, forcing
`t=0`. This verifies the renewal nonarithmetic condition directly.

The tail difference in the theorem is nonnegative, because `B>=0`.
Using the coupling in (7), Tonelli gives its entire integral:

\[
\begin{aligned}
\int_0^\infty\bigl(\mathbb P(R>x)-\mathbb P(AR'>x)\bigr)\,dx
&=\mathbb E\int_0^\infty
 \mathbf1_{\{AR'\le x<AR'+B\}}\,dx\\
&=\mathbb E B=1/4.
\end{aligned}
\tag{12}
\]

This does not subtract two divergent expectations. Dividing (12) by
(11) gives (9). Enlarge a tail bound to a finite initial interval to
obtain (10); using `>=` instead of `>` is harmless by bounding through
`x/2` if necessary. `QED`.

No new priority claim is made for the model's power tail. The new use is
its quantitative comparison with the original-root contribution below.
Even without renewal theory, (8) already gives a weaker budget
`3^M/M >= c_s q^(1+s)` for every fixed `s<1`; the primary theorem
supplies the exact square power without that exponent loss.

## 3. One original forward prefix forces mass at its own height

Fix one hypothetical escaping ordinary orbit `q_j=U^j(q_0)`. Every
state is a positive odd unit, and the source `q_0` is fixed throughout.
Put

\[
g_i=v_2(3q_i+1),\quad A_j=\sum_{i<j}g_i,\quad
\chi_j=3^j2^{-A_j},\quad
\Lambda_j=\prod_{i<j}\frac{3q_i}{3q_i+1}.
\tag{13}
\]

The complete forward affine identity gives

\[
\chi_jq_0=\Lambda_jq_j,\qquad
R_j^{\rm back}=q_j-\chi_jq_0=(1-\Lambda_j)q_j.
\tag{14}
\]

`R_j^back` is the real prefix carry in the *reversed actual gap word*
from root `q_j` back to the literal source `q_0`. It uses every gap and
the complete numerical carry. It is not the forward series with the
word order left unchanged.

For `j>=1`, since every factor in (13) is below one,

\[
R_j^{\rm back}\ge\varepsilon q_j,
\qquad \varepsilon:=\frac1{3q_0+1}>0.
\tag{15}
\]

Under (4), that one inverse prefix has probability
`chi_j h(q_0)/h(q_j)`. Every continued inverse path through it has
real boundary at least (15).

Choose once and for all the continuous function

\[
f(u)=\begin{cases}
0,&u\le\varepsilon/2,\\
2u/\varepsilon-1,&\varepsilon/2<u<\varepsilon,\\
1,&u\ge\varepsilon.
\end{cases}
\tag{16}
\]

It is bounded between zero and one and has fixed Lipschitz constant
`2/epsilon`, independent of `j`.

**Lemma 2 (exact original-cylinder lower bound).** At every `j>=1`,

\[
\boxed{
\frac{h(q_j)}{q_j}\int f(R/q_j)\,d\mu_{q_j}(R)
\ge \frac{h(q_0)}{q_0}\Lambda_j.}
\tag{17}
\]

**Proof.** The integrand equals one on the specified inverse-prefix
event. Multiply its exact probability by `h(q_j)/q_j`, and use
(14). `QED`.

This finite inequality does not need finite spine capacity or a lower
bound on all trace values. For the uniform escaping-spine conclusion,
retain the supplied reciprocal-summability input in the repository:

\[
\Lambda_*:=\inf_j\Lambda_j>0.
\tag{18}
\]

It follows, for example, from the cited distinct-orbit reciprocal bound;
it is not deduced from formal stationarity. Let
`c_0=h(q_0) Lambda_*/q_0>0`. Then (17)'s right side is at least
`c_0` for every position on this one spine.

## 4. Every shallow positive conditioning average misses that mass

For any positive unit `q` and any probability weights
`w_1,...,w_M>=0`, `sum w_m=1`, define the actual finite model measure

\[
\eta_w^q=\sum_{m=1}^M w_m\eta_m^q.
\tag{19}
\]

No separately normalized conditional is substituted for (19).

**Theorem 3 (height cost for the specified model-to-source bridge).**
With `f` from (16),

\[
\boxed{
\frac1q\int f(R/q)\,d\eta_w^q(R)
\le\frac{2K_R}{\varepsilon q^2}
      \sum_{m=1}^M w_m3^m.}
\tag{20}
\]

Consequently, retaining the separate imported hypothesis (18), at every
actual spine root `q_j`,

\[
\boxed{
\frac{h(q_j)}{q_j}\mu_{q_j}[f(R/q_j)]
-\frac1{q_j}\eta_w^{q_j}[f(R/q_j)]
\ge c_0-\frac{2K_R}{\varepsilon q_j^2}
                      \sum_{m=1}^M w_m3^m.}
\tag{21}
\]

**Proof.** The support of the integrand in (20) lies in
`{R>=epsilon q/2}`. Dropping only the ternary restriction in the
nonnegative joint probability and using (10) gives

\[
\eta_m^q[f(R/q)]
\le3^m\mathbb P(R\ge\varepsilon q/2)
\le\frac{2K_R3^m}{\varepsilon q}.
\]

Average with the specified weights, divide by `q`, and combine with
(17)--(18). No independence between `R` and `Y` was asserted. `QED`.

Thus even weights chosen separately at each root cannot approximate
the canonical unnormalized fibre at its natural height scale if
`sum_m w_m3^m=o(q_j^2)`. In particular, a depth cutoff
`3^M=o(q_j^2)` fails for **every** such positive averaging scheme.

For the precise Cesaro weights in the literature interface (6),

\[
\sum_{m=1}^M\frac{3^m}{M}
=\frac{3^{M+1}-3}{2M}\le\frac{3^{M+1}}{2M}.
\]

Writing `C_0=3K_R/epsilon`, (21) becomes

\[
\boxed{
\frac{h(q_j)}{q_j}\mu_{q_j}[f(R/q_j)]
-\frac1{q_j}\overline\eta_M^{q_j}[f(R/q_j)]
\ge c_0-C_0\frac{3^M}{M q_j^2}.}
\tag{22}
\]

To make the absolute discrepancy in this one bounded continuous test
less than `c_0/2`, it is necessary that

\[
\boxed{
M\log3-\log M\ge2\log q_j+\log(c_0/(2C_0)).}
\tag{23}
\]

In particular any successful sequence of such comparisons satisfies

\[
\liminf_{j\to\infty}\frac{M_j}{\log_3 q_j}\ge2.
\tag{24}
\]

The stronger logarithmic correction in (23) comes from Cesaro weighting;
the square-height requirement itself persists for arbitrary positive
weights with the same depth cutoff. This is a necessary lower budget,
not a sufficiency theorem for a choice of `M_j`.

### Normalized probabilities and their normalization cannot both be ignored

Set `bar F_M(q)=bar eta_M^q(R)` and
`widehat mu_(q,M)=bar eta_M^q/bar F_M(q)`. The denominator is positive.
For the displayed test,

\[
\left|\frac{h(q)}q\mu_q[f(R/q)]
-\frac1q\overline\eta_M^q[f(R/q)]\right|
\le\frac{h(q)}q\left(
\|\mu_q-\widehat\mu_{q,M}\|_{\rm TV}
+\left|1-\frac{\overline F_M(q)}{h(q)}\right|\right).
\tag{25}
\]

Here total variation is `sup_A |mu(A)-nu(A)|` for probabilities.
If the supplied trace-flow comparison gives `h(q_j)/q_j<=K` along
the original spine, then whenever the rightmost term in (22) is at
least `c_0/2`,

\[
\boxed{
\|\mu_{q_j}-\widehat\mu_{q_j,M}\|_{\rm TV}
+\left|1-\frac{\overline F_M(q_j)}{h(q_j)}\right|
\ge c_0/(2K).}
\tag{26}
\]

This explicitly separates a possible error in the normalized real law
from a possible error in its canonical trace weight. The upper bound
on `h(q_j)/q_j` is an additional input for (26), not needed in
(17)--(24). The retained local source
`research/high-variance-20261123/entropy/COARSE_DIGIT_MEMORY_AND_TRACE_FRONT.md`,
(2), supplies the source-qualified global bound `h(q)<=M_0 q` for
this canonical trace. Its operator acts on all positive odd integers
before multiplying by the trace, which vanishes on multiples of three;
thus its `D_1=P 1` is the model's `F_1`, not a new unit-renormalized
seed. Another sufficient version is finite capacity for the harmonic
flow `nu_h(n)=r(n)h(n)`, where
`r(n)=n^(-1) product_(k>=0) 3U^k n/(3U^k n+1)` on an escaping
component. Its positive product and the same fixed original orbit
must be retained when invoking that version.

## 5. What the Fourier attack gains, and what remains unsupported

Frozen PR180 `FOURIER_BRIDGE.md`, (26)--(28), controls the model's
normalized depth-`m` real conditional uniformly over positive odd unit
roots when `m=o(log |t|)`. The result is valid for its stated law.
The literature identity (6) improves the description of the target
interface: the correct approximation is the trace-weighted Cesaro
one, with its canonical normalization.

Equations (22)--(26) show that this approximation cannot be uniform
along an escaping ordinary source in a shallow conditioning regime.
For example, if `log |t_j|=O(log q_j)` and `M_j=o(log |t_j|)`, then
`3^(M_j)/(M_j q_j^2)->0`. Such model averages cannot approximate the
canonical unnormalized fibre with `o(q_j)` error in this scaled test.
When the stated upper trace bound is retained, (26) also rules out
simultaneous total-variation approximation of the normalized fibre
and relative accuracy of its trace normalization. This rules out
that proposed use of the uniform shallow-depth Fourier estimate.

There is a second coordinate issue. The physical real boundary at
`q_j` and the retained common boundary obey

\[
R=q_j-\chi_j Z.
\tag{27}
\]

Thus a common-boundary Fourier frequency of size `chi_j` corresponds
to a physical root-fibre frequency of size one. Since `q_j` is an
integer, `exp(2 pi i q_j)=1`; the integer factor does not introduce
high-frequency decay in the model. A high-frequency theorem must
identify which coordinate and frequency it actually controls.

This does **not** disprove a different, sufficiently deep identification,
or a fixed-root high-frequency theorem. At a fixed `q`, the height
budget is fixed, and (6) still has its stated weak-limit meaning. The
unproved assertion needed for a Fourier closure is a comparison with
an adequate frequency-dependent error after paying the actual depth
and normalization cost. Neither fixed-frequency weak convergence nor
the model's marginal regularity supplies that assertion.

PR182's new exact Shannon-dimension theorem retains a different boundary:
it controls typical complete fibres, with no exponential bound on their
omitted mass. We have not converted it into a Renyi-2 estimate. The new
bound here concerns the literal model/canonical comparison on one fixed
ordinary future; it does not give a same-source ternary collision upper,
exclude escape, or exclude positive cycles.

## 6. Evidence boundary

The original-prefix identity and lower bound, positive-weight model
comparison, square-depth deduction, and normalized-law dichotomy have
written proofs above. The power-tail theorem uses a checked primary
renewal theorem with every model hypothesis verified explicitly. The
canonical trace and its selection/convergence inputs retain their
upstream source qualifications. We did not reprove the old trace
construction or reinterpret a finite simulation as an escaping orbit.
In particular, the uniform square-height budget imports (18); the
finite lower bound (17) itself uses no such reciprocal-summability input.

No new Lean module is added: the present advance uses an analytic renewal
theorem and an actual measure comparison. Formalizing only the final
two-number inequality would not formalize those ingredients. Exact source
pins, inspection scopes, and review hashes are recorded under
`reports/2026-11-23-literature-push/boundary-*`.
