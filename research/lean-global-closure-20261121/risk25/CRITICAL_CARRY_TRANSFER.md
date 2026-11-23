# Critical exact-total laws with the integer carry retained

Date: 2026-11-23.

**Status: written finite theorems, a source-qualified actual-law consumer,
and an attempted escape closure that remains OPEN.** The new positive
estimate is a critical-exponent collision upper bound at the *full*
ternary precision for a specified uniform family of finite positive gap
words. The proof keeps the complete carry. A cyclic rotation is used only
to count that reference family, never to rotate a word on the original
ordinary orbit.

An exact comparison then applies to the complete ordinary endpoint law
`zeta_(M,r)`, with its original source, weights, inverse clock, and omitted
mass retained. It expresses the remaining cost as the squared density of
the actual word submeasure relative to the reference family. PR180's new
strict stationary collision gap forces an exponential cost in this
comparison, or an explicitly large omitted mass. No estimate removing
either cost is proved. In particular no conditional theorem here proves
Collatz.

## 1. Frozen sources and the law that must be controlled

The checkout read in this lane was PR175 at
`53ba1e1ffc46bf022433c2124a62682ad8dd4739`. Its
`research/lean-global-closure-20261121/risk24/literature/HIGHER_RANK_BOUNDARY_ATTACK.md`
is the preceding Haar-component construction. That construction does not
retain the ordinary integer carry in its compact coordinate.

The precise additional dependencies are:

| Source | Pin and exact role |
|---|---|
| PR185 | `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`, `research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md`, Sections 1–2: the ordinary harmonic kernel and exact retained atoms. |
| PR185 | Same head, `research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`, Theorem 3: the finite critical collision lower bound, including the square-root gain. |
| PR180 | `a436db7b85f37abafea25f42d6f34afed02a29c0`, `research/whole-source-20261123/COLLISION_CORE.md`, Sections 3–7: stationary backward-gap lifts of the unchanged orbit law and the strict, process-dependent collision-exponent gap. |
| PR182 | `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, `research/whole-repo-round3-20261123/ACTUAL_COLLISION.md`, Sections 2–6: complete-carry decoding, quotient channels, actual source boxes, and the weighted full-law collision accounting. The decoder and weighted Cauchy mechanism are credited to this source. |
| PR178 | `e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`, `research/profound-step-20261123/dynamics/COALESCENCE_AND_CRITICAL_COLLISIONS.md`, (5a)–(5b): asymptotically full high-profile mass in the actual inverse endpoint law. |

Use the accelerated odd map

\[
 U(n)=(3n+1)/2^{v_2(3n+1)},\qquad q_j=U^j(q_0).
\]

For the infinite actual-law application, `q_0` is one fixed hypothetical
escaping positive odd ternary-unit source. Write

\[
 2^{g_j}q_j=3q_{j-1}+1,\qquad
 \ell=\log_2 3,\qquad
 \Phi(b)=b\log b-(b-1)\log(b-1),\qquad
 \theta=\Phi(\ell)/\log3.
 \tag{1}
\]

All logarithms in entropy exponents are natural. Numerically
`theta=0.949955527188...`. No gap is independently resampled on this orbit.

Retain the source-qualified ordinary harmonic flow

\[
 \nu(q)=\sum_{Un=q}\nu(n),\quad
 v_j=\nu(q_j)\uparrow C>0,\quad
 K(q,n)=\mathbf1_{Un=q}\nu(n)/\nu(q).
\]

For `N=M+1` and every finite `r>=0`, the exact target is

\[
 \zeta_{M,r}=\frac1N\sum_{j=0}^M K^r(q_{r+j},\cdot),\qquad
 t_j=\zeta_{M,r}(\{q_j\})=\frac{v_j}{Nv_{r+j}}.
 \tag{2}
\]

Thus `0<t_j<=1/N`. Every atom outside the original forward ray is retained
in the positive remainder used below. The canonical-flow construction is
not reverified here. The elementary word theorems in Sections 2–4 need no
harmonic flow and no escaping orbit.

## 2. A large exact-total family with bounded complete carry

For a positive chronological gap word `w=(g_1,...,g_m)`, set

\[
 A=\sum_{j=1}^m g_j,\quad a_i=\sum_{j=1}^i g_j,\quad a_0=0,
 \qquad C_w=\sum_{i=0}^{m-1}3^{m-1-i}2^{a_i},\quad Q=3^m.
 \tag{3}
\]

Its endpoint residue is the exact map

\[
 \rho_m(w)=2^{-A}C_w\pmod Q.
 \tag{4}
\]

Indeed every supplied actual segment with this word, source `p`, and
endpoint `q` satisfies `2^A q=Qp+C_w`. The ordinary source is removed
only from the modular equation (4); its occurrences and weights are not
removed from the actual-law comparison.

Let `W_(m,A)` be all positive words with this exact total. Its size is

\[
 T_{m,A}=\binom{A-1}{m-1}\qquad(A\ge m).
\]

Define the balanced subfamily

\[
 B_{m,A}=\{w\in W_{m,A}:a_i\le (A/m)i\text{ for every }0\le i\le m\}.
 \tag{5}
\]

**Lemma 1 (reference-family count).** `|B_(m,A)| >= T_(m,A)/m`.

**Proof.** For a word put `s_i=a_i-(A/m)i`. Its centered increments
sum to zero. Choose an index `k` maximizing `s_k` among
`0,...,m-1`, and cyclically begin the word after `k`. Every centered
prefix of the resulting word is at most zero. For a prefix that wraps
around, use `s_m=0`; its centered sum is again `s_h-s_k<=0`.
Consequently the union of the `m` rotation images of `B_(m,A)` contains
all of `W_(m,A)`, and counting this union gives the inequality. A
periodic word only reduces the size of its rotation orbit and causes no
problem. This is counting in the explicitly declared reference family.
It asserts no cyclic-rotation invariance of an actual time law. ∎

If `A<=ell*m`, every word in (5) has the literal complete-carry bound

\[
 \frac{C_w}{Q}
 =\frac13\sum_{i=0}^{m-1}2^{a_i-\ell i}\le\frac m3.
 \tag{6}
\]

The integer quotient `floor(C_w/Q)` therefore has at most

\[
 R_m=1+\lfloor m/3\rfloor
 \tag{7}
\]

possible values. It has not been discarded by a compact quotient.

At fixed `(m,A)`, the complete carry decodes the word: in shortcut
notation its chronological recursion is
`C_(bu)=3^(#1(u))*b+2*C_u`; parity recovers the first bit, after which
subtracting the first term and dividing by two repeats the procedure.
The fixed total length is essential. Hence fixing the endpoint residue
in (4) and the integer quotient in (7) fixes the word. Each residue has
at most `R_m` words in `B_(m,A)`. This is the PR182 decoding mechanism,
applied here to the quantitatively large family supplied by Lemma 1.

## 3. A critical collision upper at the full ternary resolution

Take

\[
 A_m=\lfloor\ell m\rfloor,\qquad L_m=|B_{m,A_m}|,
 \qquad u_m=\text{uniform probability on }B_{m,A_m},
 \qquad \rho_m^B=(\rho_m)_*u_m.
\]

**Theorem 2 (balanced exact-total reference).** For every `m>=1`,

\[
 \boxed{
 \|\rho_m^B\|_\infty\le\frac{R_m}{L_m}
 \le\frac{mR_m}{\binom{A_m-1}{m-1}},\qquad
 \operatorname{Col}_{3^m}(\rho_m^B)\le\frac{R_m}{L_m}.}
 \tag{8}
\]

There is an absolute constant `C_1` such that

\[
 \boxed{\operatorname{Col}_{3^m}(\rho_m^B)
 \le \|\rho_m^B\|_\infty
 \le C_1m^{5/2}\,3^{-\theta m}.}
 \tag{9}
\]

**Proof.** The fiber count just proved gives the first bound in (8).
Lemma 1 gives the second. Collision is at most the largest atom for a
probability. Finally, uniform Stirling bounds and
`A_m=ell*m+O(1)` give

\[
 \binom{A_m-1}{m-1}\ge c_1m^{-1/2}\exp(m\Phi(\ell)).
\]

The `O(1)` displacement of the first binomial argument changes its
exponential estimate only by a fixed factor, since `ell` is strictly
between one and two. Absorb the finitely many small `m`. Combining
this with `R_m=O(m)` proves (9). ∎

This is a full-resolution statement: the modulus is `3^m` for a word of
`m` odd steps. It is not an invocation of a theorem restricted to a small
fraction of the word length. It is also not the iid geometric law of
mean `ell`, whose word collision exponent is instead
`log(2*ell-1)<Phi(ell)`.

Every word in this reference family has positive ordinary realizations.
For example, take an odd positive `p` in the residue class

\[
 p\equiv(2^A-C_w)(3^m)^{-1}\pmod{2^{A+1}},
 \tag{10}
\]

and choose a representative coprime to three. Finite parity decoding
gives exactly the supplied gaps and an odd final endpoint. All subsequent
odd endpoints are ternary units. The prefix inequalities in (5) additionally
give `3^i/2^(a_i)>=1`, so these finite actual paths stay above their
starting value at every odd prefix. The starting integer in (10) depends
on the word and the length. This supplies finite ordinary witnesses, not
one fixed all-time source.

## 4. A widening strip still has the critical exponent

For an integer `s>=0`, let `G_(m,s)` consist of the positive words such
that

\[
 |A-A_m|\le s,
 \qquad 2^{a_i}\le2^s3^i\quad(0\le i\le m).
 \tag{11}
\]

The second condition is an exact integer test; no rounded floating-point
logarithm is needed. Write `L_(m,s)=|G_(m,s)|` and

\[
 R_{m,s}=(2s+1)\left(1+\left\lfloor\frac{m2^s}{3}\right\rfloor\right).
 \tag{12}
\]

The set contains `B_(m,A_m)`, and it is finite. For a word in it,
`C_w/Q<=m2^s/3`. At each fixed total there are at most the second
factor of (12) words over an endpoint residue, and there are at most
`2s+1` totals. Thus every fiber has size at most `R_(m,s)`. In
particular the uniform endpoint law on this family has maximum atom
and collision at most

\[
 \boxed{\frac{R_{m,s}}{L_{m,s}}
 \le C_2(2s+1)(1+m2^s)m^{3/2}\,3^{-\theta m}.}
 \tag{13}
\]

For every integer schedule `s_m=o(m)`, this is
`exp(o(m))*3^(-theta*m)`. This wider reference is useful because
restricting to one exact total would ordinarily omit most of a word
law. Even a strip whose omitted probability tends to zero is not enough
for collision transfer: the required rate is stated next.

## 5. An exact same-source upper, including repetitions and all omitted mass

Fix `1<=m<=M`, `s>=0`, and a finite inverse clock `r`. For each
`m<=j<=M`, take the **unchanged chronological past word**

`W_j=(g_(j-m+1),...,g_j)`

and its weight `t_j` in (2). Keep precisely the indices for which
`W_j in G_(m,s)`. Combine every occurrence of the same word into

\[
 p_w=\sum_{\substack{m\le j\le M\\W_j=w}}t_j
 \quad(w\in G_{m,s}),\qquad
 \alpha=\sum_wp_w,\quad \tau=1-\alpha,
 \quad J=L_{m,s}\sum_wp_w^2.
 \tag{14}
\]

There is **no renormalization** of these weights. In particular

\[
 \tau=
 \underbrace{\left(1-\sum_{j=0}^Mt_j\right)}_{
   \text{all off-spine inverse mass}}
 +\sum_{j<m}t_j
 +\sum_{\substack{m\le j\le M\\W_j\notin G_{m,s}}}t_j.
 \tag{15}
\]

Every term is nonnegative. No low-profile cutoff has been introduced.

**Theorem 3 (complete-source transfer).** The full law (2) satisfies

\[
 \boxed{
 \operatorname{Col}_{3^m}(\zeta_{M,r})
 \le\left(
       \sqrt{\frac{R_{m,s}}{L_{m,s}}J}+\tau
      \right)^2.}
 \tag{16}
\]

**Proof.** The retained endpoint submeasure is the pushforward of
the word submeasure `(p_w)`. Every residue fiber has at most `R_(m,s)`
words. Cauchy's inequality inside each fiber therefore gives its
collision at most `R_(m,s)*sum_w p_w^2`. Every repeated actual word
was already combined in `p_w`; repeated occurrences have not been
replaced by a distinct-word count. The omitted endpoint measure has
total mass `tau`, so the Euclidean norm of its residue vector is at
most `tau`. Apply the triangle inequality to the two residue vectors.
This proves (16), including all cross terms. ∎

Relative to uniform measure on `G_(m,s)`, the retained word submeasure
has density `f(w)=L_(m,s)*p_w`. Thus

\[
 J=\mathbb E_{u_{m,s}}f^2.
 \tag{17}
\]

If `alpha>0`, the ordinary Rényi divergence of its normalized word law is

`D_2((p_w/alpha)||u_(m,s))=log(J/alpha^2)`.

This quantity retains the actual original-source repetitions. For a
uniform finite time window with `r=0`, it is explicitly
`L_(m,s)*sum_w c_w^2/N^2`, where `c_w` counts its unchanged
occurrences. The PR182 source-box identity explains why different
occurrences of a word can occupy different source quotients; it does
not bound this sum. If `f<=D`, then `J<=D*alpha<=D`, so (16)
uses only one power of that *word-density* bound.

The high-profile issue has not gone away. At the frozen PR178 head,
`inf_r zeta_(M,r){F>B_N}->1` for every `B_N=o(N)` under the specified
trace comparison. Formula (15) would charge the entire omitted mass if
one attempted such a cutoff. Equations (14)–(16) instead allow high-profile
endpoints, with their literal `t_j`, in the same word energy `J`.

## 6. The stationary gap forces an exponential comparison cost

Fix one ternary weak limit `mu` of the original time laws
`pi_M=N^(-1) sum_(j<=M) delta_(q_j)`. PR180 supplies a stationary
backward-gap lift. Reverse each length-`m` block to chronological order
and call its law `P_m`. Then its endpoint factor is exactly `mu mod 3^m`.
This reversal is only notation for the actual past word; it is not a
cyclic rotation or a change of measure.

For `G_(m,s_m)`, define `p_w=P_m(w)` on the retained family,
`tau_m=P_m(G_(m,s_m)^c)`, and `J_m=L_(m,s_m)*sum p_w^2`.
The same finite proof as Theorem 3 gives

\[
 \sqrt{\operatorname{Col}_{3^m}(\mu)}
 \le \sqrt{(R_{m,s_m}/L_{m,s_m})J_m}+\tau_m.
 \tag{18}
\]

The strict stationary theorem supplies `epsilon_mu>0` and `m_mu`
such that

\[
 \operatorname{Col}_{3^m}(\mu)
 \ge\exp[-(\Phi(\ell)-\epsilon_\mu)m]
 \quad(m\ge m_\mu).
 \tag{19}
\]

For any `s_m=o(m)`, write the explicit upper in (13) as
`exp(-Phi(ell)*m+u_m)`, where `u_m=o(m)`.

**Corollary 4 (actual distortion-or-remainder alternative).** At every
sufficiently large `m`, at least one of the following holds:

\[
 \boxed{
 \tau_m\ge\frac12
       \exp[-(\Phi(\ell)-\epsilon_\mu)m/2],
 \quad\text{or}\quad
 J_m\ge\frac14\exp[\epsilon_\mu m-u_m].}
 \tag{20}
\]

**Proof.** Insert (19) and (13) into (18). If the first alternative
fails, the first term on the right of (18) must exceed half its lower
left-hand bound. Squaring and cancelling `exp(-Phi(ell)*m)` gives
the second alternative. ∎

Thus a subexponential `L^2` word comparison together with an omitted
mass of order `exp(-Phi(ell)*m/2+o(m))` would close the escape
argument. Conversely (20) proves that an actual escaping stationary law
must defeat this proposed transfer at a positive exponential rate in at
least one of its two *literal* quantities. This is a theorem about the
same actual stationary limit, not merely about a countermodel law.
It is not an upper bound for either quantity.

For the finite PR185 square-root target, (16) would require

`sqrt((R/L)*J)+tau=o(m^(1/4)*3^(-theta*m/2))`

on a compatible sequence. The ordinary diagonal also requires
`N*sqrt(m)/3^(theta*m)->infinity`; `m^2=O(M)` alone is insufficient.
The stationary version (18)–(20) takes the original time limit first and
the resolution limit second. No quantitative exchange of those limits
is asserted.

## 7. Why the attempted closing estimate is still missing

The reference estimate itself is now available, with the carry retained,
at the precise critical exponent. The unproved step is to control
`J_m` and `tau_m` for the actual chronological past words. Their values
are not controlled by the number of legal words in the reference family.

In particular, a stationary process is not cyclically invariant on each
finite block. Rotating the actual blocks to enforce (5) would change their
ordinary source and endpoint. Lemma 1 did not perform that operation.
The complete source boxes remove repetitions *inside* each translated
box, but occurrences in different source quotients can still have the
same word. A time Følner argument supplies block stationarity, not a
subexponential upper bound for their combined squared masses in (14).

The iid critical geometric process illustrates a separate rate issue:
conditioning its word on one exact total gives a uniform type law, but
the original process has its own random total. Ignoring the probability
outside a sublinear strip loses the rare words that can dominate a
collision sum. It cannot be substituted for the actual `P_m`, and mere
`tau_m->0` is much weaker than the rate in (20).

The closing attempt therefore reaches a genuine carry-preserving
critical reference estimate and an exact full-source transfer inequality.
It does not establish the arithmetic comparison needed on the original
word distribution. The integer source and all high-profile mass remain
in that comparison, rather than disappearing into a compact quotient.

## 8. Primary literature and evidence boundary

The following primary sources were inspected to test deeper entropy
mechanisms before deriving the elementary reference estimate above:

1. Michael Hochman, *On self-similar sets with overlaps and inverse
   theorems for entropy*, Annals of Mathematics 180 (2014), 773–822,
   DOI `10.4007/annals.2014.180.2.7`, especially the convolution identity
   in the introduction and the inverse-theorem setup in Section 2.
   <https://annals.math.princeton.edu/wp-content/uploads/annals-v180-n2-p07-p.pdf>.
   Its independent convolution inputs are not supplied by the actual
   source-conditioned word submeasure `(p_w)`; no inverse theorem is
   applied to that submeasure without proving those hypotheses.
2. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded
   values*, Forum of Mathematics, Pi 10 (2022), e12, Propositions
   1.14 and 1.17. The fine-scale and Fourier estimates concern the
   independent geometric Syracuse word law. They are not an estimate
   for the unchanged stationary lift `P_m`.
   <https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F>.
3. Lyapunov Weaver, *A power improvement for uniform Collatz interval
   compression*, rStation Paper 28, version 3 (26 October 2026),
   Sections 7.10–7.11, in particular (J23)–(J26).
   <https://rstation.ai/problems/collatz/papers/28>.
   These give joint source/endpoint and averaged conditional bounds
   for their specified geometric/exact-total reference laws. Their
   actual-law change of measure is not assumed. The finite proof in
   Sections 2–6 above does not depend on this manuscript's deep
   arithmetic inputs.

`check_critical_carry.py` is a bounded exact-arithmetic control of the
rotation count, complete-carry fiber bound, positive ordinary replay, and
the weighted consumer. Its range and output are recorded in the separate
receipt. It is not a proof of the infinite statements. No new Lean
formalization of probability, the stationary gap theorem, or the analytic
canonical flow is claimed. Full Collatz remains unresolved.
