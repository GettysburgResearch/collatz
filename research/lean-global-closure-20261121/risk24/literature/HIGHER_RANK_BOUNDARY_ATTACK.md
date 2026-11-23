# Higher-rank rigidity from the actual boundary: a Haar component and the remaining endpoint gap

Date: 2026-11-23.

**Status: source-qualified written theorems and a direct closing attempt.**
The new positive information dimension of the actual canonical real boundary
can be used with published measure rigidity. A specified dyadic thickening
of the retained orbit gives jointly invariant limit measures with a Haar
component of uniformly positive mass. Separately, the actual real boundary
gives zero mass to the exceptional sets in the mixed Littlewood theorem.

Neither conclusion proves Collatz. The thickening changes the averaging,
the rigidity theorem permits a zero-entropy remainder, and its compact
coordinate does not determine the original ordinary endpoint. The
Diophantine approximation theorem supplies unrestricted integer pairs;
their conversion into legal inverse words remains unproved. All these
distinctions are explicit below.

## 1. Retained inputs and primary theorems

Fix one hypothetical escaping ordinary odd-unit source \(p\). Write

\[
 q_j=U^jp,\qquad a_j=v_2(3q_j+1),\qquad
 A_j=\sum_{i<j}a_i,\qquad \chi_j=3^j2^{-A_j}.
 \tag{1}
\]

The common component boundary \(Z\) and its canonical trace whole-path
law are those of PR180, `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`,
`research/high-variance-20261123/ANALYTIC_GLUING.md` and
`ENTROPY_RIGIDITY.md`. Use \(\chi(p)=1\). Its real boundary marginal
\(\mu\) has compact support in \([a,b]\subset(0,\infty)\).

Let \(E_j\) be the event that the common path passes through \(q_j\),
and \(p_j=\mathsf P(E_j)\). The exact source comparison is

\[
 E_j\uparrow\Omega,\qquad p_j\uparrow1,\qquad p_0>0,
 \qquad \mu\ge p_j\mu_j,
 \quad\mu_j=\mathcal L(Z\mid E_j).                      \tag{2}
\]

Under this conditional law, the physical real intercept at \(q_j\) is
\(B_\infty=q_j-\chi_j Z\). Thus (2) retains the actual inverse law
at the supplied moving root. The common law is not claimed equal to each
conditional law.

The new input is PR180, `fcdcdbadc6172e414f7282442a8a6b85587d7e70`,
`research/source-clock-20261123/EXTENSIONS.md`, (E12)--(E15): for an
explicit \(d_0=d_B>0\),

\[
 \liminf_{k\to\infty}\frac{H_k(\mu)}{k\log2}\ge d_0.
 \tag{3}
\]

Here \(H_k\) is entropy of the real partition of mesh \(2^{-k}\).
The same positive lower bound holds for every fixed absolutely continuous
reweighting of a fixed-root trace path law. Its canonical trace, positive
floor, full-event selection, and path-count qualifications remain in force.
No new analytic premise is hidden in the use of (3).

The actual product gives, with \(\Lambda_j=\prod_{i<j}3q_i/(3q_i+1)\),

\[
 \chi_j=q_j\Lambda_j/p,\qquad
 \chi_*:=\Lambda(p)/p\le\chi_j\le(3/2)^j,
 \qquad A_N/N\le\log_2 3+O_p(N^{-1}).                  \tag{4}
\]

The positive product follows from the elementary path count in PR177
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
`research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`.

The two published inputs inspected directly are:

1. Einsiedler--Lindenstrauss, *Rigidity properties for commuting
   automorphisms on tori and solenoids*, ETDS 42 (2022), 691--736,
   **Theorem 1.2**. A jointly invariant ergodic probability for a totally
   irreducible, non-virtually-cyclic higher-rank solenoid action is Haar
   if an action element has positive entropy. Theorem 1.1 records the
   corresponding Rudolph circle theorem.
   [Primary published PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B5B7471AB9A282B5B179E35040809159/S0143385721000742a.pdf/div-class-title-rigidity-properties-for-commuting-automorphisms-on-tori-and-solenoids-div.pdf),
   DOI `10.1017/etds.2021.74`.
2. Einsiedler--Kleinbock, *Measure rigidity and p-adic Littlewood-type
   problems*, Compositio Math. 143 (2007), 689--702,
   **Theorems 1.1--1.2**. Each specified exceptional set is a countable
   union of sets of box dimension zero. Proposition 2.2 identifies the
   full diagonal-cone bounded-orbit condition involved.
   [Primary published PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1CADF1EAA4DF66CA39C84B8ED71C1118/S0010437X07002801a.pdf/measure-rigidity-and-p-adic-littlewood-type-problems.pdf),
   DOI `10.1112/S0010437X07002801`.

The finite entropy estimates needed for the new application are proved
below. No classification theorem is applied before its invariance and
entropy hypotheses have been established for the specified measure.

## 2. The exact compact group and its actual edge relation

Use the compact solenoid

\[
 X_6=(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)
       /\operatorname{diag}\mathbb Z[1/6].
 \tag{5}
\]

Equivalently its character group is \(\mathbb Z[1/6]\). Multiplication
by two and three induces commuting automorphisms \(T_2,T_3\).
The real-leaf embedding is

\[
 \iota(t)=[(t,0,0)].
\]

It is injective and has dense image. The character indexed by one gives
a continuous factor \(\pi:X_6\to\mathbb R/\mathbb Z\), with
\(\pi\iota(t)=t\pmod1\), intertwining \(T_2,T_3\) with ordinary
circle multiplication.

An actual fibre point has the exact class

\[
 [(B_\infty,q_j,q_j)]
 =\iota(B_\infty-q_j)=\iota(-\chi_j Z).                 \tag{6}
\]

Define the common-boundary measures and the actual conditional fibres by

\[
 \sigma_j=(z\mapsto\iota(-\chi_jz))_*\mu,
 \qquad \kappa_j=(z\mapsto\iota(-\chi_jz))_*\mu_j.
 \tag{7}
\]

Equation (2) yields \(\sigma_j\ge p_j\kappa_j\) and
\(d_{\rm TV}(\sigma_j,\kappa_j)\le1-p_j\).
The exact action identity is

\[
 \boxed{\sigma_{j+1}=(T_3T_2^{-a_j})_*\sigma_j.}        \tag{8}
\]

It is one state-dependent action along the retained valuation word.
It is not separate invariance under \(T_2\) and \(T_3\).

The action on \(X_6\) meets the algebraic hypothesis of the primary
rigidity theorem. Indeed, the annihilator of an invariant closed subgroup
is an additive subgroup of \(\mathbb Z[1/6]\) stable under multiplication
and division by two and three. A nonzero such subgroup is an ideal
\(d\mathbb Z[1/6]\), and its quotient is finite. Thus the original
closed subgroup is finite or the whole solenoid. A finite-index subaction
contains powers \(T_2^k,T_3^k\); stability under division by \(2^k,3^k\)
implies stability under division by two and three using integer
multiplication. This proves total irreducibility. The action is faithful
of rank two by unique factorization, so it is not virtually cyclic.

## 3. An exact division-tower identity and quantitative invariance

Put

\[
 \overline\sigma_N=\frac1N\sum_{j=0}^{N-1}\sigma_j,
 \qquad
 \tau_N=\frac1N\sum_{j=0}^{N-1}
       \sum_{\ell=0}^{a_j-1}(T_2^\ell)_*\sigma_{j+1}.
 \tag{9}
\]

The second object is a finite positive measure of mass \(A_N/N\),
not a probability substituted for the first. From (8),

\[
 \boxed{((T_3)_*-I)\overline\sigma_N
 =((T_2)_*-I)\tau_N+\frac{\sigma_N-\sigma_0}{N}.}        \tag{10}
\]

To check the identity, use
\((T_3)_*\sigma_j=(T_2^{a_j})_*\sigma_{j+1}\), telescope
the \(a_j\) successive doublings, and then telescope in \(j\).
Before any additional averaging, (10) supplies a relation between two
different measures. Its limiting version does not make either side zero.

Now make the averaging change explicit:

\[
 \lambda_{N,L}=\frac1L\sum_{\ell=0}^{L-1}
                 (T_2^\ell)_*\overline\sigma_N.
 \tag{11}
\]

Use \(d_{\rm TV}(\rho,\eta)=\sup_A|\rho(A)-\eta(A)|\).
Telescoping (11), and then averaging (10), gives

\[
 \boxed{
 d_{\rm TV}((T_2)_*\lambda_{N,L},\lambda_{N,L})\le1/L,
 \quad
 d_{\rm TV}((T_3)_*\lambda_{N,L},\lambda_{N,L})
 \le\frac{A_N}{NL}+\frac1N.}
 \tag{12}
\]

For the second bound, the tower term becomes
\(((T_2^L)_*-I)\tau_N/L\), with total-variation bound
\(\tau_N(X_6)/L=A_N/(NL)\). The remaining averaged difference
of two probabilities costs at most \(1/N\).

Consequently every weak limit of \(\lambda_{N,L_N}\), with
\(N,L_N\to\infty\), is separately invariant under both generators.
This is a derived invariance statement for a precisely identified law.

The original conditional fibres have not been silently discarded:

\[
 \boxed{\lambda_{N,L}\ge
       \frac{p_0}{L}\left(\frac1N\sum_{j<N}\kappa_j\right).}
 \tag{13}
\]

The coefficient is explicit and tends to zero as the thickening grows.
This remains relevant when assessing what the eventual classification
does and does not say about the retained law.

## 4. Positive entropy survives the explicit schedule \(L=N^2\)

Let \(\rho_N=\pi_*\overline\sigma_N\). On the circle, \(H_k\)
denotes entropy of its usual \(2^k\) half-open dyadic cells.
There is a constant \(C_p\), also depending on the fixed support of
\(\mu\), such that for every \(j<N\) and every precision \(k\),

\[
 H_k((-\chi_j Z)\bmod1)
 \ge H_k(\mu)-N\log(3/2)-C_p.                          \tag{14}
\]

Here is the uniform partition comparison. A real cell for \(-\chi_jZ\)
pulls back to an interval of length \(2^{-k}/\chi_j\), meeting at
most \(\lceil\chi_*^{-1}\rceil+2\) original mesh cells. Therefore
scaling loses at most the logarithm of that fixed number. Reducing the
scaled value modulo one loses at most the entropy of its integer part.
That integer part takes at most
\(\chi_j(b-a)+2\le(b-a+2)(3/2)^N\) values. This proves (14),
including its uniformity in the moving root and the precision.

Finite-mixture entropy concavity gives

\[
 H_k(\rho_N)\ge H_k(\mu)-N\log(3/2)-C_p.              \tag{15}
\]

We next use a finite block inequality. For any circle probability \(\rho\),
let \(\eta_L=L^{-1}\sum_{\ell<L}(\times2^\ell)_*\rho\).
For \(1\le m\le L\),

\[
 \boxed{\frac{H_m(\eta_L)}m
 \ge\frac{H_L(\rho)}L-\frac{2m\log2}{L}.}              \tag{16}
\]

To prove it, split the binary block of length \(L\) into blocks of
length \(m\), first using each of the \(m\) possible starting offsets.
The initial and terminal incomplete blocks cost at most \(2m\log2\)
for each offset. Sum these subadditivity inequalities and use entropy
concavity on the complete blocks. Adding the remaining nonnegative
block entropies gives
\(mH_L(\rho)\le L H_m(\eta_L)+2m^2\log2\), as required.

Take \(L=N^2\) in (15)--(16). Equation (3) then gives, for every
fixed \(m\),

\[
 \liminf_{N\to\infty}
 H_m(\pi_*\lambda_{N,N^2})\ge m d_0\log2.             \tag{17}
\]

This is a diagonal schedule, not an exchange of two unspecified limits.
The moving-source entropy loss is \(O_p(N)\), while the supplied
real entropy is evaluated at precision \(N^2\).

Let \(\lambda\) be any weak limit of \(\lambda_{N,N^2}\), and
\(\eta=\pi_*\lambda\). Equation (12) makes both invariant under
their two multiplication maps. To handle dyadic boundary atoms without
assuming entropy continuity, observe the elementary bound

\[
 H_m(\eta)\ge
 \limsup_i H_m(\eta_i)-\log2\qquad(\eta_i\Rightarrow\eta).
 \tag{18}
\]

Indeed a limiting cell label can differ from the containing cell only
at a boundary point, where at most two adjacent labels are possible.
Keep that label in a joint weak limit; its conditional entropy is at
most \(\log2\). This proves (18). Combining (17)--(18), and using
the generating binary partition for the invariant doubling map, gives

\[
 \boxed{h_\eta(\times2)\ge d_0\log2>0.}                \tag{19}
\]

### Theorem HR: a positive Haar component

Every weak limit \(\lambda\) of the explicit sequence
\(\lambda_{N,N^2}\) has a decomposition

\[
 \boxed{\lambda=c\,m_{X_6}+(1-c)\lambda_0,
             \qquad c\ge d_0,}                        \tag{20}
\]

where \(\lambda_0\) is jointly invariant and all its jointly ergodic
components have zero entropy for every action element.

**Proof.** Apply ergodic decomposition for the now-established joint
action. Total irreducibility and non-virtual-cyclicity were checked in
Section 2. The primary Einsiedler--Lindenstrauss theorem says each
ergodic component is Haar or has zero action entropy. A zero-entropy
component has a zero-entropy circle factor. Haar projects to Lebesgue
measure on the circle, whose doubling entropy is \(\log2\).
Entropy is affine on invariant measures, so
\(h_\eta(\times2)=c\log2\). Equation (19) proves \(c\ge d_0\).
\(\square\)

Thus the published rigidity theorem is genuinely applicable to a measure
derived from the actual common boundary. It gives a positive Haar
component, not a claim of pure Haar or of equidistribution along the
unthickened ordinary orbit.

## 5. Testing the handoff to the original endpoint

There are separate issues after Theorem HR.

First, (13) retains the unthickened actual fibres with coefficient
\(p_0/N^2\). No theorem here places this particular shrinking
submeasure inside the Haar component rather than the zero-entropy
remainder. A positive Haar component in the enlarged average is not
an upper bound for the original law.

Second, even pure Haar identification would initially be qualitative
weak convergence at fixed continuous tests. The required collision bound
has growing ternary resolution and a specified inverse clock. No rate
or conditional endpoint estimate follows from the classification theorem.

Third, the ordinary endpoint is not determined by the compact class in
(6). The lost arithmetic is visible before taking the quotient. On the
three-coordinate cover put

\[
 D(x)=2x,\qquad A(x)=3x+(1,1,1).
\]

Then

\[
 \boxed{DA(x)=AD(x)+(1,1,1).}                           \tag{21}
\]

The diagonal translation disappears in \(X_6\), making the two
induced maps commute. It changes an ordinary endpoint by one, which
does not disappear modulo \(3^m\). Thus restoring the endpoint label
does not give the commuting action to which the joining classification
applies. In a real fundamental domain this is the integer-part carry
already retained by the earlier quotient-entropy calculation.

Consequently Theorem HR does not identify the actual ternary time
marginal, or the whole \(\zeta_{M,r}\) in PR185
`research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`.
The growing-resolution estimate
\(o(\sqrt m\,3^{-0.949955527188\ldots m})\), with \(m^2=O(M)\),
is still not proved. Haar limits on the compact quotient can coexist
with every finite fibre being supported on its dense real leaf.

## 6. The exceptional-set theorem does apply to the actual boundary

There is also a direct consequence of the second primary theorem which
does not require the dyadic thickening.

**Lemma.** A fixed-root canonical real boundary law gives zero mass to
every countable union of sets of upper box dimension zero.

**Proof.** Suppose a bounded such set has positive mass. Replace it by
its closure, which has the same upper box dimension, and condition the
path law on its boundary lying in that closed set. This is a fixed
absolutely continuous reweighting. The retained result (E14) in PR180
gives its real marginal lower information dimension at least \(d_0\).
But a set of box dimension zero meets \(\exp(o(k))\) mesh cells of
size \(2^{-k}\), so every probability supported there has
\(H_k\le o(k)\). This is a contradiction. Bounded pieces and
countable unions finish the proof. \(\square\)

Fixed affine changes preserve zero box dimension. Conditioning the common
component law on its countably many clock-zero roots therefore proves
the same zero-mass conclusion for \(\mu\).

Einsiedler--Kleinbock, Theorem 1.1, now yields the genuine almost-sure
consequence, for each prime \(\ell\),

\[
 \boxed{\liminf_{Q\to\infty}Q|Q|_\ell\,\|QZ\|=0
        \quad\text{for }\mu\text{-almost every }Z.}     \tag{22}
\]

It holds simultaneously for all primes by countability. Here
\(\|x\|\) is distance to the nearest integer. The stronger primary
Theorem 1.2 also gives, for every **fixed** \(v\in\mathbb Q_\ell\),

\[
 \liminf_{Q,C\to\infty}
 |Q|\,|QR-C|\,|Qv-C|_\ell=0                           \tag{23}
\]

almost surely under a fixed-root canonical real intercept law. In
particular choose \(\ell=3\) and \(v=q\), the original ordinary
root itself. The exceptional-set input is countable-union box dimension
zero; Hausdorff dimension zero alone would not justify this deduction
from the available information-dimension statement.

This also shows why a proof that the entire actual boundary lay in the
corresponding bounded-diagonal-orbit exceptional set would close the
escape case under these analytic inputs. Such an inclusion is not supplied
by the current whole-cone floor.

## 7. Testing the unrestricted approximants against literal inverse words

At the fixed original root \(q\), retain the actual inverse path notation
from PR180: total \(A_r\), multiplier \(a_r=3^r2^{-A_r}\),
prefix intercept \(R_r\), endpoint \(X_r\), and limit \(R\).
Write

\[
 C_r=2^{A_r}R_r
     =\sum_{j=1}^r3^{j-1}2^{A_r-A_j}\in\mathbb Z,
 \qquad 2^{A_r}q-C_r=3^rX_r.                           \tag{24}
\]

Because \(X_r\) is a ternary unit, the last difference has exact
3-adic valuation \(r\). Let \(T_r\) be the real intercept of the
continued inverse path viewed from \(X_r\). Then
\(R-R_r=a_rT_r\). The exact quantity in (23), evaluated on these
particular legal approximants, is

\[
 \boxed{
 2^{A_r}|2^{A_r}R-C_r|\,|2^{A_r}q-C_r|_3
 =2^{A_r}T_r.}                                         \tag{25}
\]

Thus the published theorem cannot be invoked by merely identifying
\((2^{A_r},C_r)\) as rational approximants. It asserts the existence
of unrestricted good pairs; it does not require their denominator to
be dyadic, their numerator to have the precise sum in (24), or their
successive intermediate inverses to be integral odd units.

The new whole-cone floor says that at \(F(X_r)\le B\), every legal
continued ancestor exceeds \((\alpha\delta/B)X_r\). Its consequence
for the real tail is an **upper** bound
\(T_r\le C_B X_r^{1-1/40}\). This neither gives a positive lower
bound for (23) over all integer pairs nor converts its good pairs into
the legal words in (24). The full-event selection theorem selects
infinitely many, and positive expected proportions of, suitable
canonical return depths. It has no quantifier over arbitrary integer
approximation pairs.

The first unproved bridge in this version of the closing attempt is
therefore a source-preserving legalization result: obtain sufficiently
good pairs in (23) with the exact dyadic denominator, numerator form,
ordinary intermediate states, and useful endpoint conclusion. Neither
the whole-cone floor nor the published exceptional-set theorem establishes
that bridge. No exceptional-set containment has been asserted from a
single admissible Collatz ray.

## 8. Outcome and proof status

The route did reach two places where deep machinery applies with verified
hypotheses: Theorem HR gives a positive Haar component for the explicit
\(N^2\)-thickened actual-boundary average, and (22)--(23) give
Diophantine approximation properties of the actual canonical boundary
itself. The remaining endpoint gap is identified in (13), (21), and
(24)--(25), with the source, law, and clock unchanged in their statements.

The finite calculations and entropy argument are written proofs. The
source-qualified canonical boundary input and the two cited published
rigidity theorems are not new Lean axioms. No new Lean formalization of
the measure-rigidity or information-dimension conclusions is claimed,
and no Collatz proof has been obtained.
