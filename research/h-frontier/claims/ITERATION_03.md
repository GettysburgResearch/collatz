# Iteration 03: plastic-pressure ghosts, critical kernels, and completion height

All theorem-level claims below are `PROPOSED` pending independent review. The
finite audit `X-9503` is `EMPIRICAL` only. No claim here proves termination of
`H` or constructs an infinite positive orbit.

This iteration uses four methodological interfaces from other repository work,
without importing their theorem status:

- PR #13 observed that the H ghost system is a countable separated `2`-adic IFS;
- PR #20 emphasized completion-height and repetition obstructions;
- PR #33 supplied a general finite-trap paradigm for nested cylinders;
- PR #3 separated unmarked escape pressure from one marked ordinary spine.

The first two interfaces yield self-contained H-specific results below. The
last two clarify the exact remaining boundary: pressure and finite
compatibility do not decide ordinary initialization, and the raw H state is not
uniformly contracting.

---

## L-9513: Exact intermediate-state threshold at a first crossing

**Claim ID:** `L-9513`  
**Title:** A first-contracting extension is governed by one exact intermediate-state inequality  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** `L-9502`, `L-9511`  
**Experiment:** `X-9503`

### Statement

Let `u` be a nonempty expanding exact word. Write

\[
 m=\frac{V_u}{U_u}>1,
 \qquad
 \Sigma_u=\sum_{k=1}^{|u|}\frac1{M_k}.
\]

Append a one-letter contracting block `r in {0,1,2}` and assume the complete
word `ur` is contracting. Put

\[
 a_r=\frac{V_r}{U_r}<1.
\]

Let `h` be the exact input carry in the concatenation and let

\[
 N=Y_u+hV_u=A_r+jU_r
\]

be the canonical normalized state immediately before the final letter. Then

\[
 \boxed{
 \Delta_{ur}
 =\left(\frac1m-a_r\right)N-\frac{1+\Sigma_u}{4}.
 }
 \tag{1}
\]

Since `m a_r<1`, the coefficient of `N` is positive. Thus exact descent is
equivalent to

\[
 \boxed{
 N>N_u^*(r):=
 \frac{1+\Sigma_u}{4(1/m-a_r)}.
 }
 \tag{2}
\]

If `h>=1`, then `N>=V_u`. Consequently a sufficient condition for descent is

\[
 \boxed{
 \frac{4D_{ur}}{U_r}>1+\Sigma_u,
 \qquad
 D_{ur}=U_uU_r-V_uV_r.
 }
 \tag{3}
\]

If every proper prefix of `ur` is expanding, then `Sigma_u<|u|`. Hence the
still simpler powers-gap condition

\[
 \boxed{
 D_{ur}>2^{3r}(|u|+1)
 }
 \tag{4}
\]

is sufficient whenever `h>=1`.

The zero-carry case is exactly

\[
 \boxed{
 Y_u>N_u^*(r).
 }
 \tag{5}
\]

Thus the unresolved finite descent theorem and the unresolved infinite
stabilization theorem meet at the same zero-carry interface.

### Proof

In normalized coordinates the prefix map is

\[
 N=f_u(x)=mx+\frac{m\Sigma_u}{4}.
\]

Therefore

\[
 x=\frac Nm-\frac{\Sigma_u}{4}.
\]

The final one-letter map is

\[
 f_r(N)=a_rN+\frac14.
\]

Subtracting gives (1), and (2) follows because `1/m-a_r>0`.

For `h>=1`, canonical endpoint nonnegativity gives

\[
 N=Y_u+hV_u\ge V_u.
\]

Also

\[
 \frac1m-a_r
 =\frac{U_u}{V_u}-\frac{V_r}{U_r}
 =\frac{D_{ur}}{V_uU_r}.
\]

Substitution into (2) shows that `V_u>N_u^*(r)` is precisely (3). If every
proper prefix expands, every `M_k>1`, so every reciprocal is below one and
`Sigma_u<|u|`. Since `U_r/4=2^(3r)`, condition (4) implies (3).

### Gap audit

- Equation (1) is exact and closes no inequality by itself.
- Condition (4) is only sufficient. No universal powers-gap proof is supplied.
- The case `h=0` remains the sharp actual-word phase problem `Q-9503`.

---

## L-9514: Separated ghost IFS and plastic recurrence

**Claim ID:** `L-9514`  
**Title:** H ghosts form a separated countable `2`-adic IFS with plastic residue growth  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** `L-9502`, `L-9503`  
**Experiment:** `X-9503`

### Definitions

For `r>=0`, put

\[
 e_r=3r+2,
 \qquad
 s_r=2r+1,
\]

and define the contraction

\[
 \phi_r(x)=2^{e_r}3^{-s_r}(x-1)
 \qquad (x\in\mathbb Z_2).
 \tag{6}
\]

Let `G_*` be the set of ghost values of all infinite itineraries and let

\[
 G=\overline{G_*}\subset\mathbb Z_2.
\]

For `K>=1`, let

\[
 N(K)=\#(G\bmod 2^K).
\]

### Statement

One has

\[
 G=\{0\}\cup\bigcup_{r\ge0}\phi_r(G),
 \qquad G\subset4\mathbb Z_2.
 \tag{7}
\]

Every point of `phi_r(G)` has exact valuation `e_r`, so the nonzero branch
images are pairwise disjoint. The residue counts obey

\[
 N(1)=1,
 \qquad N(2)=1,
 \qquad N(3)=2,
\]

and

\[
 \boxed{N(K)=N(K-2)+N(K-3)\qquad(K\ge4).}
 \tag{8}
\]

Let `rho` be the plastic constant, the positive root of

\[
 \rho^3=\rho+1.
\]

Then

\[
 \boxed{N(K)=\Theta(\rho^K).}
 \tag{9}
\]

Moreover

\[
 \boxed{
 \dim_H(G)=\log_2\rho
 =0.405685231375824\ldots .
 }
 \tag{10}
\]

### Proof

Split the ghost series after its first letter. If `x` is the tail ghost, the
full ghost is exactly `phi_r(x)`. Every tail ghost is divisible by four, so
`x-1` is odd. Hence

\[
 v_2(\phi_r(x))=e_r.
\]

This proves separation. The only closure point created by sending the first
letter to infinity is zero, giving (7).

Modulo `2^K`, every branch with `e_r>=K` collapses to the common residue zero.
If `e_r<K`, multiplication by the odd unit `3^(-s_r)` and the translation
`x -> x-1` identify its residue set with `G mod 2^(K-e_r)`. Separation by exact
valuation gives

\[
 N(K)=1+\sum_{3r+2<K}N(K-(3r+2)).
 \tag{11}
\]

Subtracting the same formula at `K-3` leaves exactly the `r=0` term, proving
(8). The positive recurrence gives (9).

Put `s=log_2(rho)`. Then

\[
 \sum_{r\ge0}2^{-s(3r+2)}=1
\]

because `rho^3=rho+1`. The standard stopping-line cover gives the upper
Hausdorff bound. For the reverse bound, assign branch mass

\[
 q_r=2^{-s(3r+2)}.
\]

The masses sum to one. Strong ultrametric separation gives a Frostman estimate

\[
 \mu(B(x,2^{-K}))\le C2^{-sK},
\]

which proves (10).

### Gap audit

- `G` is the closure of itinerary ghosts; zero need not itself be an itinerary
  value. This distinction does not affect residue upper bounds.
- The dimension statement concerns the full ghost closure, not the ordinary
  positive-integer section.

---

## T-9506: Plastic power bound for ordinary survivors

**Claim ID:** `T-9506`  
**Title:** Infinite exact survivors have plastic-exponent counting and harmonic convergence  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** `L-9503`, `L-9514`

### Statement

Let `I` be the set of positive ordinary exact states with infinite future and
put

\[
 s=\log_2\rho.
\]

Then

\[
 \boxed{
 \#\{p\le X:p\in\mathcal I\}=O(X^s).
 }
 \tag{12}
\]

Consequently

\[
 \boxed{
 \sum_{p\in\mathcal I}\frac1p<\infty.
 }
 \tag{13}
\]

This strengthens the stretched-exponential-density estimate proposed in
`T-9501` and removes its growing-depth word-count interface.

### Proof

By `L-9503`, every ordinary infinite survivor is its itinerary ghost, hence lies
in `G`. Choose `K` with `2^K>X`. Each residue modulo `2^K` contains at most one
integer in `[1,X]`. Therefore

\[
 \#\{p\le X:p\in\mathcal I\}
 \le N(K)
 \ll\rho^K
 \ll X^s.
\]

Since `s<1`, partial summation proves (13).

### Consequences

All uses of harmonic summability in `T-9502` and `T-9503` may instead depend on
this theorem. In particular, every nonperiodic infinite exact orbit still
satisfies

\[
 \sum_i\frac1{M_i}<\infty,
 \qquad K_i\to+\infty.
\]

If `p_0,...,p_(N-1)` are the first `N` states of such an orbit and

\[
 H_N=\max_{0\le i<N}K_i,
\]

then distinctness and (12) give

\[
 \boxed{
 H_N\ge
 \frac{\log N}{s\log(9/8)}-O(1).
 }
 \tag{14}
\]

The coefficient is approximately `20.9280`.

---

## T-9507: Branchwise critical harmonic kernel

**Claim ID:** `T-9507`  
**Title:** Every valuation branch has a uniform odd-core reciprocal budget  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** `L-9514`, `T-9506`

### Statement

Let

\[
 \mathcal I_r=\{p\in\mathcal I:v_2(p)=e_r\}.
\]

There is an absolute constant `C` such that

\[
 \boxed{
 \sum_{p\in\mathcal I_r}\frac1p\le C2^{-e_r}
 \qquad(r\ge0).
 }
 \tag{15}
\]

Hence, for every nonnegative weight sequence `g_r` satisfying

\[
 \sum_{r\ge0}g_r2^{-e_r}<\infty,
\]

one has

\[
 \boxed{
 \sum_{p\in\mathcal I}\frac{g_{r(p)}}p<\infty.
 }
 \tag{16}
\]

In particular, all subcritical exponential moments `g_r=lambda^r`, `lambda<8`,
converge.

More sharply, let `p_i=2^(e_(r_i))u_i` be any nonperiodic infinite exact orbit.
For every nonnegative summable sequence `(c_r)`,

\[
 \boxed{
 \sum_i\frac{c_{r_i}}{u_i}<\infty.
 }
 \tag{17}
\]

There is a universal constant `C_0` such that

\[
 \boxed{
 \sup_{r\ge0}\sum_{i:r_i=r}\frac1{u_i}\le C_0.
 }
 \tag{18}
\]

Consequently

\[
 \boxed{
 \#\{i:r_i=r,\ u_i\le U\}\le C_0U
 }
 \tag{19}
\]

uniformly in `r`.

### Proof

A survivor in branch `r` lies in `phi_r(G)`. If `2^K>X` and `e_r<K`, that
branch has exactly `N(K-e_r)` possible residues modulo `2^K`; if `e_r>=K`, no
positive integer at most `X` lies in the branch. Therefore

\[
 A_r(X):=\#\{p\le X:p\in\mathcal I_r\}
 \ll X^s2^{-e_rs}.
 \tag{20}
\]

Partition the branch into dyadic intervals

\[
 2^{e_r+j}\le p<2^{e_r+j+1}.
\]

The number of points in the `j`th interval is `O(2^(sj))`; multiplying by the
largest reciprocal and summing gives

\[
 \sum_{p\in\mathcal I_r}\frac1p
 \ll 2^{-e_r}\sum_{j\ge0}2^{-(1-s)j}
 \ll2^{-e_r}.
\]

This proves (15) and (16). For `g_r=2^(e_r)c_r`, equation (16) becomes (17).
Taking one branch at a time gives

\[
 \sum_{i:r_i=r}\frac1{u_i}
 =2^{e_r}\sum_{i:r_i=r}\frac1{p_i}\le C_0,
\]

which proves (18); (19) follows because every counted term is at least `1/U`.

### Interpretation

The critical value `8` is no longer merely a divergent generating series.
Arbitrary critical weights are allowed after multiplication by any summable
kernel `c_r`. A hypothetical survivor may visit every valuation scale, but it
has a uniform reciprocal budget at each scale.

---

## L-9515: Repetition forces completion height

**Claim ID:** `L-9515`  
**Title:** Repeated itinerary factors require exponentially large ordinary separation  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** `D-9501`; capital corollaries use `T-9502`

### Statement

Let `p_i` be an exact orbit. Suppose the same itinerary factor `w` of length
`ell` begins at two positions `i<j`:

\[
 (r_i,\ldots,r_{i+\ell-1})
 =(r_j,\ldots,r_{j+\ell-1})=w.
\]

Then

\[
 \boxed{
 2^{E_w}\mid p_j-p_i.
 }
 \tag{21}
\]

If the orbit is nonperiodic, the difference is nonzero, so

\[
 \boxed{
 2^{E_w}\le|p_j-p_i|.
 }
 \tag{22}
\]

Since `E_w>=2ell`, every repeated length-`ell` factor requires

\[
 \boxed{4^\ell\le|p_j-p_i|.}
 \tag{23}
\]

For a hypothetical nonperiodic survivor, put

\[
 Q_\infty=\lim_n p_n/M_n,
 \qquad
 H_N=\max_{0\le n<N}K_n.
\]

If two length-`ell` factors beginning before `N` coincide, then

\[
 \boxed{
 4^\ell\le2Q_\infty(9/8)^{H_N}.
 }
 \tag{24}
\]

Thus every length satisfying the reverse strict inequality has pairwise
distinct factors among the first `N` positions.

If `H_N=o(N)`, there are lengths `ell_N=o(N)` for which the first `N-ell_N`
factors are all distinct. Hence the factor complexity obeys

\[
 \boxed{
 \frac{p_{\mathbf r}(\ell_N)}{\ell_N}\to\infty
 }
 \tag{25}
\]

along a subsequence. In particular, a sublinear-capital survivor cannot have
Sturmian, quasi-Sturmian, or uniformly linear factor complexity.

### Proof

The two copies of `w` have the same affine offset, so subtraction gives

\[
 p_{j+\ell}-p_{i+\ell}
 =\frac{3^{S_w}}{2^{E_w}}(p_j-p_i).
\]

The left side is an integer and `gcd(3^(S_w),2^(E_w))=1`, proving (21).
Nonperiodicity makes distinct orbit states unequal. This proves (22)--(23).

For a real-escaping survivor, `p_n=M_nQ_n` with `Q_n<=Q_infinity`. Therefore

\[
 |p_j-p_i|\le p_i+p_j
 \le2Q_\infty(9/8)^{H_N},
\]

which proves (24). Choose `ell_N` just above the logarithmic threshold in (24).
If `H_N=o(N)`, then `ell_N=o(N)`, and all corresponding factors are distinct,
proving (25).

### Gap audit

This is a rigidity theorem, not a nonexistence theorem. A critical survivor may
have capital large enough to pay for high symbolic novelty.

---

## T-9508: Critical versus subcritical real escape

**Claim ID:** `T-9508`  
**Title:** Every real-escaping survivor is either a critical near-Pillai chain or subcritical  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** `T-9505`

### Statement

For a hypothetical nonperiodic survivor, let

\[
 c_*=\frac{\log9}{\log8},
 \qquad
 Z_i=K_i/c_*^i,
 \qquad
 Z_i\to Z_\infty\ge0.
\]

If `Z_infinity>0`, then

\[
 \boxed{
 K_i\sim Z_\infty c_*^i,
 \qquad
 r_i\sim(c_*-1)Z_\infty c_*^i,
 \qquad
 \frac{r_{i+1}}{r_i}\to c_*.
 }
 \tag{26}
\]

Moreover

\[
 \boxed{
 \sum_i\frac{\log u_i}{r_i}<\infty,
 \qquad
 \frac{\log u_i}{r_i}\to0.
 }
 \tag{27}
\]

Thus the core equation

\[
 2^{3r_{i+1}+2}u_{i+1}-3^{2r_i+1}u_i=1
\]

would be an infinite critical near-Pillai chain with subexponential cofactors.

Let

\[
 G_i=-\sum_{k=1}^i2^{E_k}3^{-S_k}
\]

be the direct ghost truncation. Its reduced denominator is `3^(S_i)` and

\[
 v_2(p_0-G_i)=E_{i+1}.
\]

In the critical regime,

\[
 \boxed{
 \frac{E_{i+1}\log2}{S_i\log3}\to1.
 }
 \tag{28}
\]

Therefore the direct rational truncations lie exactly at approximation exponent
one; they do not cross a supercritical rational-approximation threshold.

If `Z_infinity=0`, then

\[
 \boxed{K_i=o(c_*^i),\qquad r_i=o(c_*^i).}
 \tag{29}
\]

### Proof

Equation (26) follows from `K_i=Z_i c_*^i` and

\[
 r_i=K_{i+1}-K_i+\kappa.
\]

The discounted core budget in `T-9505` is

\[
 \sum_i c_*^{-(i+1)}\log u_i<\infty.
\]

Since `r_i` is asymptotic to a positive constant times `c_*^i`, this proves
(27).

The exact truncation identity is

\[
 p_0-G_i=\frac{2^{E_i}p_i}{3^{S_i}}.
\]

Because `p_i=1 mod 3`, this fraction has reduced denominator `3^(S_i)` and
valuation `E_i+v_2(p_i)=E_(i+1)`. In the critical regime `R_i=K_i+\kappa i`
is asymptotic to `K_i`, so

\[
 E_{i+1}\sim3(K_i+r_i)\sim3c_*K_i,
 \qquad
 S_i\sim2K_i.
\]

The definition `c_*=2log3/(3log2)` gives (28). Equation (29) is immediate from
`Z_infinity=0`.

---

## Q-9504: A `2`-adic logarithm route to exclude the critical regime

**Claim ID:** `Q-9504`  
**Title:** Obtain a uniform valuation bound strong enough to kill critical near-Pillai chains  
**Status:** `IDEA`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `T-9508`

### Target

The core recurrence gives

\[
 v_2(3^{2r_i+1}u_i+1)=3r_{i+1}+2.
\]

A bound of the qualitative shape

\[
 \boxed{
 v_2(3^{2r+1}u+1)
 \le C\log(2r)\log(2u)
 }
 \tag{30}
\]

uniformly for the admissible odd cores would eliminate `Z_infinity>0`.
Indeed, in that regime `r_(i+1)` is comparable to `r_i`, so (30) would force

\[
 \frac{\log u_i}{r_i}\gg\frac1{\log r_i}\asymp\frac1i,
\]

contradicting the convergent series in (27).

No theorem with the exact hypotheses and constants of (30) is imported here.
The next task is to audit explicit two-term `2`-adic logarithmic-form bounds and
verify that varying `u` enters only through its logarithmic height in a strong
enough way.

The case `u=1` causes no critical exception: for odd `2r+1`, LTE gives
`v_2(3^(2r+1)+1)=2`, so the next letter is zero.

---

## Q-9505: Completion-height exclusion of the subcritical regime

**Claim ID:** `Q-9505`  
**Title:** Find a transformed integer height for zero-carry real escape  
**Status:** `IDEA`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `L-9503`, `T-9508`

### Target

PR #33 shows that an ordinary completion is impossible when its induced integer
height is uniformly contracted into a finite forbidden trap. The raw H state is
supercritical and does not satisfy that hypothesis. The remaining task is to
find a transformed integer or finite-state-corrected height on an eventual
zero-carry tail such that either:

1. every sufficiently long subcritical-capital block contracts it into a finite
   exact trap; or
2. failure of contraction forces the critical regime `Z_infinity>0`, which is
   then attacked by `Q-9504`.

Candidate coordinates include the odd core `u_i`, a signed residual numerator
from the nested ghost cylinders, or a finite-state potential correcting
`log(u_i)` by the capital bank. Any valid theorem must retain integrality; a
purely real normalized height is insufficient.

---

## Cross-program conclusion

The repository peek changes the H strategy in three concrete ways.

1. The countable-IFS interface replaces the weaker survivor count by an exact
   plastic recurrence and power-law bound.
2. The repetition/completion-height interface supplies a native H factor
   rigidity theorem and rules out low-complexity sublinear-capital ghosts.
3. The finite-trap theorem identifies the missing feature of the infinite
   problem: a transformed **integer** height, not another real pressure bound.

The remaining frontier is now:

```text
finite side:
  actual-word zero-carry mixed-sign inequality

infinite side:
  critical near-Pillai chain exclusion
  OR
  subcritical transformed-height finite trap
```
