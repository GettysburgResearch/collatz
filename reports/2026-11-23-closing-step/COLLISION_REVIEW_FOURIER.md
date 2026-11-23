# Review of FOURIER_BRIDGE.md

Reviewer: source-collision lane. Date: 2026-11-23.

**Verdict: PASS for the repaired written theorems and their stated iid
model scope. No Collatz closure or pointwise ordinary-source transfer is
certified.**

Reviewed file:
`research/closing-step-20261123/FOURIER_BRIDGE.md`

Reviewed SHA256:

`1677ce2685f693363df82e3e30a141d09a164a4eaeed8ff3a169ac119eafc29e`

The reviewer rederived the displayed arguments and checked the primary
analytic hypotheses. The reviewer previously supplied the complete-carry
and endpoint-overlap ideas, so this is an independent check of the
root lane's written deductions, not a claim of independent discovery.

## 1. Narrow correction made before this verdict

The initial frozen hash
`c8e4e4340ac1caeb3c66c9cfb46591a0e2042545143f6819ca527cf1c7d41fff`
allowed a positive odd root divisible by three in the discussion
preceding the normalized conditional law. At positive depth that
cylinder has mass zero, so division by `Z_m(q)` is undefined.

The author repaired the domain: normalized conditioning is now restricted
explicitly to positive odd roots with `3` not dividing `q`.
The repair does **not** discard an inverse chain whose final endpoint
is divisible by three. Both features were checked in the repaired bytes.
No other repair was required.

## 2. Probability law, orientation, and normalization

The gap law is the specified iid geometric mean-two law. Its real
series converges by the strong law, and its ternary series converges
because the \(j\)-th summand has ternary valuation \(j-1\).

The chronological reversal used to import the companion carry theorem
is justified by iid gaps. It is not applied to a merely stationary law.

Haar measure is probability on all of \(\mathbb Z_3\). A depth-\(m\)
residue cylinder therefore has mass \(3^{-m}\), so

\[
 \int F_m^q\,dH=3^{m(q-1)}\sum_rp_m(r)^q.
\]

The mass outside the units is retained as zero density. No
renormalization to the unit group occurs.

## 3. Generalized Holder and the complete Renyi spectrum

For a fixed residue, generalized weighted Holder gives

\[
 \left(\sum_iw_i\right)^q
 \le
 \left(\sum_iL_i^{-1/(q-1)}\right)^{q-1}
 \sum_iL_iw_i^q.
\]

The exact injection into \((A,K,\text{residue})\) permits replacing the
first sum by the full box sum. This preserves cross-box terms; it does
not replace the collision of a mixture by the mixture of collisions.

For \(q>2\), direct normalization of \(P_m(w)^q\) gives

\[
 Z_{q,m}=(2^q-1)^{-m},\qquad
 {\mathbb P}_q(G=e)=(2^q-1)2^{-qe}.
\]

Under that tilt,

\[
 {\mathbb E}_q(2^G/3)^{q-1}
 =\frac{2^q-1}{3^{q-1}}<1.
\]

The derivative argument establishing the strict inequality is correct.
The moment generating expression is finite in an open neighborhood
below exponent \(q\), so one can choose \(u>t>q-1\) with a contracting
\(u\)-moment. Minkowski then bounds the complete-carry \(u\)-moment
uniformly in depth.

With the stated centered total-clock penalty, the reciprocal-power sum
is \(O_q(\sqrt m)\). The remaining Holder factor uses fixed finite
moments of a centered iid geometric sum; the even-moment expansion
supplies them. Raising the reciprocal sum to \(q-1\) gives precisely
the polynomial factor \(m^{(q-1)/2}\). The ungrouped word moment supplies
the matching exponential lower bound.

For \(1<q\le2\), interpolation between \(\ell^1\) and \(\ell^2\) of
the probability vector gives the upper bound in equation (6), and
Jensen on \(3^m\) residues gives its lower bound. These prove the stated
limits. No uniformity in \(q\downarrow2\) is claimed or needed.

## 4. Primary check of Tao's input and the Lp interpolation

The reviewer opened the
[published primary paper](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F)
and checked Proposition 1.14 and equations (1.26)--(1.27).
The estimate is uniform for all \(1\le m\le n\), with an arbitrarily
large fixed polynomial exponent.

Projective consistency converts the proposition's oscillation exactly
to \(\|F_n-F_m\|_1\). Forming densities multiplies by \(3^n\);
integrating over the depth-\(n\) Haar atoms cancels that factor.
The coarse average is \(3^{m-n}p_m\), as used in the note.

Interpolation with the companion bound \(\|F_m\|_2=O(m^2)\) gives
the exponent
\(-A(2/p-1)+4(1-1/p)\). For each fixed \(1<p<2\), choose \(A\)
to make it negative and sum at dyadic depths. The resulting \(L^p\)
limit equals the \(L^1\) limit. The cylinder integrals identify that
limit as a density of the same ternary law.

## 5. The critical L2 endpoint and linear lower growth

For the ternary maps \(f_e(x)=(1+3x)/2^e\), the Haar Jacobian is \(1/3\).
Consequently

\[
 \|T_eh\|_2^2=3\,4^{-e}\|h\|_2^2,\qquad
 \sum_{e\ge1}3\,4^{-e}=1.
\]

Each \(f_e\) sends a depth-\(m\) cylinder bijectively to a
depth-\(m+1\) cylinder. This proves the finite recursion
\(PF_m=F_{m+1}\), including the Haar-filled depth-zero starting law.
The \(L^1\) contraction of \(P\) gives \(PF=F\).

If \(F\) belonged to \(L^2\), expanding the nonnegative square by
Tonelli would leave its squared norm unchanged in the diagonal sum,
forcing every cross product to vanish. This is impossible:
if \(\{F>0\}\) has measure \(s>0\), every branch image of that set
has measure \(s/3\), and a finite number greater than \(3/s\) of such
sets already forces a pair with positive-measure overlap.

The same pair remains available without assuming \(F\in L^2\).
For that pair, \(L^1\) convergence of the two transferred densities
implies the all-sequence lower-semicontinuity statement for their
product integral. To verify the quantifier, take a subsequence
attaining the lower limit, pass to a further common almost-everywhere
convergent subsequence, and apply Fatou.

Thus a fixed positive cross term persists for all sufficiently large
depths. The exact squared-norm increment identity gives
\(Q_{m+1}-Q_m\ge c>0\) eventually. Summation proves the linear lower
bound. Its constant need not be explicit for the asserted theorem.

Together these arguments establish the exact integrability threshold,
including failure at \(p=2\). The upper \(O(m^4)\) and lower
\(\Omega(m)\) rates are not asserted equal.

## 6. Primary check of Bremont's theorem

The reviewer opened
[the primary arXiv v8 manuscript](https://arxiv.org/html/1910.03463v8)
and checked its introduction, Definition 2.2, and Theorem 2.3.
The theorem permits positive affine slopes with negative average
logarithmic slope; it does not require each map to contract.

For the two maps in the note, both probabilities are positive when
\(b>\log_2 3\); the mean logarithmic slope is
\((\log3)/b-\log2<0\), and the fixed points are distinct.
Grouping initial even choices before the next odd choice gives the
geometric gap map with exactly the stated probabilities.

Affine conjugacy preserves slopes. Their logarithms have irrational
ratio, so they cannot both be integral powers of a common base.
This excludes the theorem's necessary non-Rajchman form and proves
the claimed qualitative decay. No quantitative rate or real absolute
continuity is imported.

The bounded-weight consequence uses the standard band property of
Rajchman measures: the projected signed measure has bounded density
with respect to the real marginal, and its density can be approximated
in \(L^1\) by finite character combinations. This is an averaged
weighted-projection conclusion, as stated.

## 7. Ordinary finite-cylinder legality and the denominator

For a legal length-\(m\) residue word, its terminal congruence implies
every prefix congruence, because all omitted summands are divisible
by the required power of three. The inverse recursion is

\[
 n_i=(2^{e_i}n_{i-1}-1)/3,\qquad n_0=q.
\]

Integrality follows from the prefix congruence. The numerator is odd,
so the quotient is odd. Positivity follows because it is a positive
integer: \(2^{e_i}n_{i-1}-1>0\). An intermediate endpoint supporting a
further inverse step must be a ternary unit; the final endpoint need
not be one.

For each unit root, \(2\) generates the six units modulo \(9\).
Among exponents \(1,\ldots,6\), three give an integral parent, and
exactly one of those three gives a parent divisible by three.
The two remaining exponents therefore give positive odd unit parents,
each with model mass at least \(2^{-6}\). Iterating those choices gives
\(2^m\) distinct words, each of mass at least \(2^{-6m}\), hence

\[
                        Z_m(q)\ge32^{-m}.
\]

This is a valid conservative bound independent of the ordinary root's
size.

## 8. Conditional Fourier bound and its retained limitation

The event defining the depth-\(m\) cylinder depends only on the first
\(m\) gaps. The unused iid tail is independent and has the original
joint law, giving equation (26) with the actual model weights.

For the small-frequency remainder,

\[
 |a_wt|<\tau
 \ \Longrightarrow\
 2^{A_m}>3^m|t|/\tau.
\]

Markov's inequality with \(0<\delta<1\) and
\({\mathbb E}2^{\delta G}=(2^{1-\delta}-1)^{-1}\) gives equation (27).
Discarding the word restriction occurs only in a nonnegative upper
bound. The denominator remains and is then bounded by \(32^m\).

For \(\tau=|t|^{1/2}\), any depth \(m=o(\log|t|)\) makes the remainder
vanish. The other term vanishes by the unconditional Rajchman theorem.
This gives the stated uniform result for positive odd unit roots,
with the depth/frequency order preserved.

The final section correctly leaves open both identification of the
actual canonical trace boundary with these model conditionals and a
comparison error valid at the needed joint depths and frequencies.
Neither averaged ternary integrability nor bounded weighted real
projection decay determines a conditional law at one ordinary
ternary point.

The conditional solenoid consequence of an **actual** Rajchman boundary
also checks: for each nontrivial fixed dual character, its coefficient
is evaluated at a real frequency tending to infinity; total variation
control preserves this. Bounded deterministic time weights preserve
vanishing of those coefficients and their Cesaro averages. This does
not convert a solenoid conclusion into a statement about the original
integer residues without the retained floor-carry arithmetic.

## 9. Scope of the pass

This review certifies the written model theorems and the conditional
implications at the reviewed hash. It is not a Lean verification of
the analytic arguments, a revalidation of all earlier repository
packets, or a proof of either missing original-source assertion.
