# Uniform inverse-density bounds through every fixed polylogarithmic horizon

**Date:** 2026-11-22 UTC.  
**Coordinating repository baseline:** PR185,
`276be8154f4e867acc0230466b34d9cb224aacf5`.  
**Status:** a complete written deduction from the source-qualified finite
ordinary counting and marginal mixing inputs below. This document does not
claim a Lean formalization of those analytic inputs, or a proof of Collatz.

The new result is an upper bound on the *actual finite ordinary inverse
densities*, simultaneously through any fixed power of the logarithm of an
inverse-basin floor. It is stronger than comparing one pair of depths. It
also bounds every canonical obstacle iterate in that horizon. The last
section identifies the specific estimate still needed before an unbounded
inverse depth can be admitted.

## 1. Objects and exact scope

Let

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd integers. A **unit** below means an integer not divisible by
3. The positive ordinary inverse operator is

\[
 Pf(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\pmod3}}
          \frac3{2^e}f\!\left(\frac{2^e q-1}{3}\right).
 \tag{1}
\]

Each displayed parent is a positive odd integer. Put

\[
 D_s=P^s1,\qquad D_0=1.
 \tag{2}
\]

These are the canonically defined finite Syracuse densities, periodic
modulo \(3^s\). No almost-everywhere density is evaluated at an ordinary
integer. In particular,

\[
 0\le D_s(q)\le3^s,\qquad
 D_s(q)=0\quad(3\mid q,\ s\ge1).
 \tag{3}
\]

Fix a positive odd unit target \(q\). An **inverse-unit floor** \(b\ge1\)
means

\[
 \forall j\ge0\ \forall n>0\text{ odd},\quad
 [3\nmid n\ \land\ U^j(n)=q]\ \Longrightarrow\ n\ge b.
 \tag{F}
\]

In particular \(q\ge b\). The least odd unit in an ordinary component
provides such a floor simultaneously for every target in that component.
The result is also valid with a floor for just the inverse basin of one
target. It does not require the component to escape, or the target to be
nonperiodic.

For a legal inverse word \(w\) of depth \(d\), with initial source \(n_w\),
write its actual affine identity as

\[
 q=\omega_w n_w+\beta_w,\qquad
 \omega_w=3^d2^{-A(w)},\qquad \beta_w\ge0.
 \tag{4}
\]

If the retained source \(n_w\) is a unit, (F) gives the crucial bound

\[
                 \omega_w\le q/b.
 \tag{5}
\]

The factor is \(q/b\), not 1 unless the target itself is an inverse-basin
minimum. Keeping this factor makes the theorem uniform on a component
rather than just at its least unit.

## 2. The two supplied inputs

The following finite-resolution counting estimate is Theorem E4, equations
(E14)--(E16), of PR180's `ENERGY_SYNTHESIS.md` at
`bfba8feaefb3d0910456cdd92d2afcf9e8785b4d`. It follows by counting distinct
ordinary sources separately at each total binary valuation and then
bounding the whole geometric clock tail. For a function \(H\) periodic
modulo \(3^t\), and a retained inverse family with coefficients at most
\(\Omega\),

\[
 |P^d_{\mathcal F}H(q)|
 \le C\,[q(d+t+1)+3^t\Omega],\|H\|_{1,3^t},
 \qquad d\ge1,
 \tag{6}
\]

where \(C\) is absolute and
\(\|H\|_{1,3^t}=3^{-t}\sum_{a\bmod3^t}|H(a)|\).

The second input is Tao's marginal fine-scale estimate, in the normalized
density notation used in that source:

\[
 \|D_t-D_m\|_{1,3^t}\le C_A m^{-A},
 \qquad t\ge m\ge1,
 \tag{7}
\]

for every fixed \(A>0\). Here \(D_m\) is lifted to the finer quotient.
The constants may depend on \(A\), but do not depend on \(t,m,q\).
The primary published source is Tao, *Almost all orbits of the Collatz map
attain almost bounded values*, Proposition 1.14, equations (1.26)--(1.27),
together with consistency (1.23). The corrected author text is
<https://arxiv.org/html/1909.03562v7>.

Since \(D_t-D_m\) vanishes on multiples of three, every nonzero source in
(6) is a unit. Equations (5)--(7) and the exact semigroup identity give

\[
 \boxed{
 \frac{|D_{d+t}(q)-D_{d+m}(q)|}{q}
 \le C_A\,[d+t+1+3^t/b]m^{-A}
 }
 \quad(d\ge1, t\ge m\ge1).
 \tag{8}
\]

This is a statement about finite positive ordinary sums. No passage from
Haar almost everywhere to every integer occurs in (8). The total-valuation
clock has already been summed in (6); it is not silently truncated.

## 3. Quantitative horizon theorem

### Theorem 1

Suppose (F). Let \(m\ge1\) be an integer with
\(3^{4m}\le b\), and let \(K\ge0\) be an integer. For every fixed
\(A>0\),

\[
 \boxed{
 \max_{0\le s\le K}\frac{D_s(q)}q
 \le b^{-1/2}
       +C_A K(K+2)m^{-A-1}.
 }
 \tag{9}
\]

The constants are uniform in the target, the floor, and the horizon.

**Proof.** For \(s\le2m\), (3) gives

\[
 \frac{D_s(q)}q\le\frac{3^{2m}}q
                \le\frac{\sqrt b}{b}=b^{-1/2}.
 \tag{10}
\]

For \(s>2m\), repeatedly subtract \(m\) until the remaining depth lies
between \(m+1\) and \(2m\). Thus choose \(J\ge1\) and
\(r=s-Jm\) with \(m<r\le2m\). Put \(k_j=s-jm\),
\(0\le j<J\). Then \(k_j\ge2m+1\), so (8) applies with

\[
 d=k_j-2m\ge1,\qquad t=2m.
\]

It yields

\[
 \frac{|D_{k_j}(q)-D_{k_j-m}(q)|}{q}
 \le C_A[k_j+1+3^{2m}/b]m^{-A}
 \le C_A(s+2)m^{-A},
 \tag{11}
\]

because \(3^{2m}\le\sqrt b\le b\). There are at most \(s/m\)
such comparisons. Telescoping **at this same target** gives

\[
 \frac{D_s(q)}q
 \le\frac{D_r(q)}q+C_A s(s+2)m^{-A-1}
 \le b^{-1/2}+C_A K(K+2)m^{-A-1}.
\]

No original source is replaced by an independent random source in this
argument. It is an algebraic telescope of the actual finite inverse
densities. This proves (9). \(\square\)

### Corollary 2: every fixed polylogarithmic horizon

For every fixed \(B,R>0\), there are constants \(C_{B,R},b_{B,R}\)
such that, whenever (F) and \(b\ge b_{B,R}\),

\[
 \boxed{
 \sup_{0\le s\le(\log b)^B}\frac{D_s(q)}q
 \le\frac{C_{B,R}}{(\log b)^R}.
 }
 \tag{12}
\]

The supremum is over integer depths, and logarithms are natural.

**Proof.** Choose

\[
 m=\left\lfloor\frac{\log b}{4\log3}\right\rfloor.
\]

For sufficiently large \(b\), \(m\ge c\log b\) with an absolute
\(c>0\). Choose the *fixed* mixing exponent, for example,
\(A=2B+R+3\), before allowing \(b\) to grow. The second term of
(9) is then \(O_{B,R}((\log b)^{-R})\), as is \(b^{-1/2}\).
This proves (12). The proof does not let \(A\) vary with \(b\) or suppress
its constant. \(\square\)

In particular, at a least odd unit \(q\) of a component, take \(b=q\):

\[
 \sup_{s\le(\log q)^B}D_s(q)
     =O_{B,R}\!\left(\frac q{(\log q)^R}\right).
 \tag{13}
\]

More generally, if a whole component has least odd unit \(b\), (12)
holds simultaneously for **every** target \(q\) in it. The horizon depends
on \(b\), not on a larger moving target \(q\).

## 4. Canonical obstacle iterates have the same bound

Let \(g=\mathbf1_{3\nmid q}\) and

\[
 V_0=g,\qquad V_{k+1}=\max(g,PV_k),\qquad V=\sup_kV_k.
 \tag{14}
\]

PR180's finite-cylinder comparison, Theorem E2, proves for a fixed finite
normalizing constant \(\kappa\ge1\)

\[
                  V_k(q)\le\kappa D_{k+1}(q)
                  \quad\text{at every ordinary }q.
 \tag{15}
\]

This comparison is derived there by integrating an almost-everywhere
inequality over the cylinder on which \(V_k\) is constant. It is not a
pointwise use of the almost-everywhere identity \(V=\kappa D\).

Using (9) with \(K+1\), we obtain

\[
 \boxed{
 \max_{0\le k\le K}\frac{V_k(q)}q
 \le\kappa b^{-1/2}
       +\kappa C_A(K+1)(K+3)m^{-A-1}.
 }
 \tag{16}
\]

Consequently, for every fixed \(B,R>0\),

\[
 \sup_{k\le(\log b)^B}\frac{V_k(q)}q
       =O_{B,R,\kappa}((\log b)^{-R})
 \tag{17}
\]

uniformly under (F).

Here is a useful precise interpretation. Fix \(\eta>0\) and \(B>0\).
For all sufficiently large least-unit targets \(q\), **any** finite
certificate of

\[
                  V_k(q)\ge\eta q/\log(q+2)
 \tag{18}
\]

must have \(k>(\log q)^B\). If \(V(q)\ge2\eta q/\log(q+2)\),
monotonicity guarantees that such a finite \(k\) eventually exists; the
theorem bounds how late it must occur. It does not assert that there is a
sequence of least-unit targets with such large canonical values.

## 5. Consequence for the new canonical contact process

This section additionally uses the written contact representation in
PR176 at `8aeb843bba254f065743b6fa277a70906b51d520`.
Fix \(\epsilon>0\), set

\[
 C_\epsilon=\{q>0\text{ odd unit}:V(q)\le1+\epsilon\},
 \quad A_\epsilon=\{q>0\text{ odd unit}\}\setminus C_\epsilon,
\]

and let \(Q=1_{A_\epsilon}P\), \(B_\epsilon=1_{C_\epsilon}V\).
Under the stopped \(V\)-Doob process of that source,

\[
 F_L(q)=\sum_{j=0}^{L-1}Q^jB_\epsilon(q),\qquad
 p_L(q)=\Pr_q(\tau<L)=F_L(q)/V(q).
 \tag{19}
\]

Because \(0\le B_\epsilon\le(1+\epsilon)1\) and \(Q\le P\),

\[
 F_L(q)\le(1+\epsilon)\sum_{j<L}D_j(q).
 \tag{20}
\]

At a least-unit target \(q\), suppose the stated, possibly empty, condition

\[
                  V(q)\ge\eta q/\log(q+2)
 \tag{21}
\]

holds. For every fixed \(B,R>0\), (12), (19), and (20), with a larger
fixed power in (12), give

\[
 \boxed{
 \sup_{1\le L\le(\log q)^B}p_L(q)
       =O_{B,R,\epsilon,\eta}((\log q)^{-R})
 }
 \tag{22}
\]

as \(q\to\infty\) among targets satisfying (21).

To check the powers directly, use (12) with exponent \(R+B+2\).
Then the numerator of (19) is at most
\((1+\epsilon)Cq(\log q)^{-R-2}\), while (21) supplies the
denominator \(\eta q/\log(q+2)\). This proves the asserted (slightly
weaker) bound (22).

Thus a hypothetical sequence of critical-size spikes at least component
units would force contact to be very unlikely through *every* fixed
polylogarithmic clock, even though the fixed-root contact probability tends
to 1 as the clock tends to infinity. This strengthens the location of the
uncontrolled tail. It is compatible with the current contact theorem; its
limits are in a different order. It does not establish the lower capture
bound proposed in PR176.

## 6. Why an adaptive path telescope has not closed the limit

The exact normalized error in (8) is

\[
 C_A[d+t+1+3^t/b]m^{-A}.
 \tag{23}
\]

Its principal clock-count term has **no reciprocal-height factor**. If
\(G\) is the positive harmonic envelope and \(h(q)=G(q)/q\), dividing
instead by \(G(q)\) changes (23) by the factor \(1/h(q)\). It does not
produce a summable \(1/q\).

The previous packet's deterministic finite-chain estimate pays
\(\sum n^{-s}\) for \(s>39/40\). It does not pay
\(\sum(\log n)^{-A}\) along an arbitrary admissible chain. In particular,
the numerical sequence \(n_j=\lceil j^2\rceil\), \(j\ge2\), has counting function
\(O(X^{1/2})\), satisfies that style of power counting bound, but has
\(\sum_j(\log n_j)^{-A}=\infty\) for every fixed \(A\). This is only a
counterexample to the implication between bounds, not an asserted Collatz
orbit.

There is also an exact measure issue in a proposed drift shortcut. For the
actual ordinary harmonic inverse kernel

\[
 K_\nu(q,n)=\nu(n)/\nu(q)\quad\text{when }U(n)=q,
\]

where \(L\nu=\nu\), the inverse edge satisfies

\[
 \log n-\log q
       =e\log2-\log3+\log\lambda(n),
 \qquad \lambda(n)=\frac{3n}{3n+1}.
 \tag{24}
\]

Therefore any drift statement must use the exponent distribution of
\(K_\nu\) (or the explicitly comparable harmonic Doob law). The geometric
letter law in Tao's forward random-word construction is not that
distribution. No uniform positive drift for (24) has been established here.

For completeness, writing \(W(n)=n\nu(n)\), one has the elementary
pointwise identity on each inverse edge with positive \(K_\nu\)-mass

\[
 \log n-\log q
 =\log W(n)-\log W(q)-\log K_\nu(q,n).
 \tag{25}
\]

When the expectations are integrable, (25) identifies the missing drift
as a change in \(\log W\) plus the entropy of the *actual* kernel. Positive
branching at every vertex alone supplies no uniform positive entropy lower
bound. Equation (25) is not being used to assert one.

### First unsupported inference

The result proved is

\[
 \forall B,R>0\quad
 \sup_{k\le(\log b)^B}V_k(q)/q
             =O_{B,R}((\log b)^{-R}).
\]

The currently unsupported next inference would replace that finite
supremum by \(\sup_{k\ge0}V_k(q)=V(q)\), or would assert sufficient
uniform contact capture to pay the complementary depths. The constants
and horizons above do not authorize that replacement. The exact
uncontrolled possibility is a critical-size certificate appearing only at
a depth larger than every fixed power of \(\log b\), with its original
source/ancestor contributions still retained.

This packet supplies a new actual-source upper bound and a quantitative
description of that tail. It does not exclude an escaping component or a
nontrivial cycle.

## 7. Source ledger and evidence level

| Input | Exact source | Used here |
|---|---|---|
| Marginal finite-scale mixing | Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum Math. Pi 10 (2022), e12, Prop. 1.14 and (1.23); corrected author version v7, 16 July 2026, <https://arxiv.org/html/1909.03562v7> | Equation (7), for every fixed power, with no conditional-clock mixing assertion |
| Full-clock ordinary counting; finite obstacle comparison | PR180 `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d`, `research/lean-wide-pass-20261122/ENERGY_SYNTHESIS.md`, SHA256 `2d9e9b1c166b4010852b926de708c8f6c4afbc0b6a08d1a3731d6fba87e7a363` | Equations (6), (15); written analytic source, not an imported Lean theorem |
| Exact canonical contact process | PR176 `8aeb843bba254f065743b6fa277a70906b51d520`, `research/lean-global-resolvent-20261121/overview/parallel/OBSTACLE_ENTRANCE_RENEWAL.md`, SHA256 `3282a797044b54690e6ff40977aaa2e73c013bda17d66809a281089cd00ba78d` | Section 5 only; fixed-root representation and stopped-law interpretation |
| Selective capture target and its open status | Same PR176 head, `CONTACT_CAPTURE_SYNTHESIS.md`, SHA256 `d531fe841cbd5740540e871c69d35629dd9e75197b65ae07638dcfc0c4a2a134` | Comparison of the proved upper bound with the still missing lower capture bound |
| Ordinary harmonic flow and power-weighted chain estimates | PR185 baseline `276be8154f4e867acc0230466b34d9cb224aacf5`, `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md` | Section 6's explanation of what the existing path estimate and actual kernel do and do not supply |

The new deductions are (9), (12), (16)--(18), and (22). They use fixed
original inverse trees and moving targets with an explicitly stated floor.
They neither resample sources after a failed passage nor exchange an
ordinary point with a Haar-almost-everywhere representative.
