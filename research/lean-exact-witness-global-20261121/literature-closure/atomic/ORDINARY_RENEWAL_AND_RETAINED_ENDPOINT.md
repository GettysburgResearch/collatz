# An ordinary renewal law, conditional ternary Haar, and the exact surviving endpoint

Date: 2026-11-23.

**Status: written theorems on a hypothetical escaping ordinary component.**
The new result derives a geometric renewal decomposition of its finite
pressure measure. A specified average of actual ordinary conditional laws
then becomes ternary Haar **conditionally on the retained ordinary next
state**. The next-state law remains exactly the original ordinary next-state
law \(U_*\mu\). The
Green calculation below exhibits the infinite source contribution that
survives this averaging. These deductions do not exclude escape or
nontrivial cycles and are not claimed as Lean-checked infinite theorems.

## 1. Retained input and normalization

Let

\[
 O=\{n\ge1:n\text{ odd},\ 3\nmid n\},\qquad
 U(n)=\frac{3n+1}{2^{a(n)}},\qquad a(n)=v_2(3n+1).
\]

Fix one escaping eventual-meeting component \(E\subset O\). The input
from `HIGH_VARIANCE_ESCAPE.md` and `ATOMIC_EXCLUSION_CONTINUATION.md` in
the parent packet is

\[
 \Lambda(n)=\prod_{k\ge0}\frac{3U^kn}{3U^kn+1}>0,
 \qquad r(n)=\frac{\Lambda(n)}n,
 \qquad r(n)=\frac3{2^{a(n)}}r(Un).
\tag{1}
\]

For \(s>1\), put

\[
 M_s=\sum_{n\in E}r(n)^s\in(0,\infty),\qquad
 \mu=\frac1{M_s}\sum_{n\in E}r(n)^s\delta_n.
\tag{2}
\]

**Every measure called \(\mu\) below is this probability**, not the
unnormalized component measure. Let

\[
 P_s f(q)=\sum_{\substack{e\ge1\\I_eq\in\mathbb Z_3^\times}}
       (3/2^e)^s f(I_eq),\qquad I_eq=(2^eq-1)/3.
\tag{3}
\]

For ordinary unit roots all legal parents are positive odd units, and
\(\mu P_s=\mu\). We use both the ternary embedding into
\(X=\mathbb Z_3^\times\) and the diagonal embedding into
\(Y=\mathbb Z_2^\times\times\mathbb Z_3^\times\).

The following arguments require no canonical harmonic-flow selection,
population theorem, independent-gap model, or replacement of an ordinary
measure by Haar.

## 2. Exact ordinary decomposition by a same-successor symmetry

Define

\[
 S(n)=64n+21,\qquad t=64^{-s}\in(0,1),\qquad
 C_j=\{n\in E:a(n)\ge6j+1\}.
\tag{4}
\]

The identity \(3S(n)+1=64(3n+1)\) gives

\[
 a(Sn)=a(n)+6,\qquad U(Sn)=Un,\qquad r(Sn)=r(n)/64.
\tag{5}
\]

Also \(S(n)\equiv n\pmod3\), so this symmetry stays in the unit
domain. Its iterates are

\[
 S^j(n)=64^jn+(64^j-1)/3.
\tag{6}
\]

**Ordinary bijection.** \(S^j\) maps \(E\) bijectively onto \(C_j\).
To prove surjectivity, take \(n\in C_j\) and set
\(b=(n-(64^j-1)/3)/64^j\). Divisibility of \(3n+1\) by
\(2\cdot64^j\) makes \(b\) an odd integer. Since
\(3b+1=(3n+1)/64^j\ge2\), it is positive. The offset
\((64^j-1)/3\) is divisible by three, so \(b\equiv n\pmod3\).
Finally \(Ub=Un\), and thus \(b\in E\). Injectivity follows
directly from (6).

Atomwise comparison in (2) now proves the **measure identity**

\[
 \boxed{\mu|_{C_j}=t^j(S^j)_*\mu,\qquad
        \mu(C_j)=t^j,\qquad
        \mu(\,\cdot\mid C_j)=(S^j)_*\mu.}
\tag{7}
\]

Here \(C_j\) is an ordinary set; on the diagonal in \(Y\), it is
the indicated binary valuation cylinder. It is not being called a ternary
cylinder. Nor is (7) a covariance identity for arbitrary ambient sets
under the ternary homeomorphism \(S\): a nonordinary preimage can map
to an ordinary atom.

Let \(B=C_0\setminus C_1=\{n\in E:1\le a(n)\le6\}\). Every
\(n\in E\) has a unique representation

\[
 n=S^Jb,\qquad b\in B,\qquad
 J=\left\lfloor\frac{a(n)-1}{6}\right\rfloor.
\tag{8}
\]

Consequently, under \(\mu\), \(J\) and \(b\) are independent,
with

\[
 \boxed{\Pr(J=j)=(1-t)t^j,\qquad
  \mathcal L(b)=\frac{\mu|_B}{1-t}.}
\tag{9}
\]

For example, the exact valuation tail \(\Pr(a(n)\ge6j+1)=t^j\)
is a statement about this actual pressure law. It is not the valuation
law along its deterministic forward orbit.

There is a finite-gap operator version. Let \(R_s\) be (3) restricted
to \(1\le e\le6\), and let \(C_Sf=f\circ S\). Unit legality
is periodic in \(e\) modulo six and \(I_{e+6j}=S^jI_e\). Hence

\[
 P_s=R_s\sum_{j\ge0}t^jC_S^j,
 \qquad P_s(I-tC_S)=R_s,
 \qquad \mu R_s=\mu-tS_*\mu=\mu|_B.
\tag{10}
\]

The geometric operator series converges on bounded functions.

## 3. Quantitative Haar averaging on the same ordinary component

For \(c\in\{1,2\}\), let \(m_c\) be Haar probability on
\(c+3\mathbb Z_3\), and put \(\pi_c=\mu(c+3\mathbb Z_3)\).
Define the actual conditional laws and their cumulative average by

\[
 \nu_j=(S^j)_*\mu=\mu(\,\cdot\mid C_j),\qquad
 \bar\nu_J=\frac1J\sum_{j=0}^{J-1}\nu_j.
\tag{11}
\]

All atoms of all these measures are positive ordinary members of \(E\).

For \(x\in\mathbb Z_3\) and \(h\ge1\), the elementary
lifting-the-exponent identity gives

\[
 v_3(S^hx-x)=v_3(64^h-1)-1=1+v_3(h).
\tag{12}
\]

Indeed \(3x+1\) is a ternary unit, \(v_3(64-1)=2\), and
\(S^hx-x=(64^h-1)(3x+1)/3\). Thus, modulo \(3^K\), each
\(S\)-orbit traverses every residue in its initial class modulo three
exactly once in a period

\[
 L_K=3^{K-1}.
\tag{13}
\]

Counting complete periods and the last incomplete period proves, for a
residue \(a\pmod{3^K}\) lying over \(c\),

\[
 \boxed{\left|\bar\nu_J(a+3^K\mathbb Z_3)
                 -\frac{\pi_c}{L_K}\right|
          \le\frac{\pi_c}{J}.}
\tag{14}
\]

It follows on continuous ternary tests, by uniform cylinder approximation,
that

\[
 \boxed{\bar\nu_J\ \Longrightarrow\
     \eta:=\pi_1m_1+\pi_2m_2.}
\tag{15}
\]

The limit is full Haar inside each class modulo three, with the original
class weights. It need not be normalized unit-Haar, which would additionally
require \(\pi_1=\pi_2=1/2\).

### The ordinary next state survives as an exact label

Let \(\mu_c=\mu|_{\{n\equiv c\pmod3\}}\). Retain the pair
consisting of the current ternary coordinate and its **ordinary** next
state, by using

\[
 \Gamma_J=\frac1J\sum_{j<J}
       (n\mapsto(S^jn,Un))_*\mu
       \quad\text{on }X\times O.
\tag{16}
\]

This really is the joint law of \((n\bmod3^\infty,Un)\) under
\(\bar\nu_J\), because \(U(S^jn)=Un\). In particular its
second marginal is **exactly** \(U_*\mu\), for every \(J\).

For any bounded function \(f:O\to\mathbb R\) and any function
\(g\) constant on ternary cylinders of depth \(K\), period counting
pointwise before integrating gives

\[
 \left|\int g(x)f(q)\,d\Gamma_J
 -\sum_{c=1,2}\left(\int g\,dm_c\right)
                     \left(\int f(Un)\,d\mu_c(n)\right)\right|
 \le\frac{L_K}{J}\|g\|_\infty\int|f(Un)|\,d\mu(n).
\tag{17}
\]

The fixed second marginal is tight on the countable ordinary space.
Cylinder approximation and truncation of that marginal therefore give

\[
 \boxed{\Gamma_J\ \Longrightarrow\
       \sum_{c=1,2}m_c\otimes U_*\mu_c.}
\tag{18}
\]

Thus the limiting ternary coordinate is Haar conditionally on both its
class \(c\) and the retained ordinary endpoint label. One may retain
the entire deterministic future \((Un,U^2n,\ldots)\) in exactly the
same way. This is a source-preserving derivation of conditional Haar;
the unknown escaping ordinary component remains in the endpoint law.

On the binary coordinate,

\[
 S^jn+1/3=64^j(n+1/3),
\tag{19}
\]

so the joint limit including both local coordinates and the endpoint is

\[
 \boxed{\delta_{-1/3}\otimes
       \left(\sum_{c=1,2}m_c\otimes U_*\mu_c\right).}
\tag{20}
\]

The binary point \(-1/3\) is the pole at which the odd valuation becomes
infinite. The ordinary forward map is not continuous there. Equation (20)
does not turn its retained ordinary endpoint into the forward image of
that pole.

### Retaining the valuation phase resolves the local discontinuity

There is an explicit additional compact coordinate. Regard
\(u(n)=2^{-a(n)}\) as a ternary unit. Along the same ordinary sequence,

\[
 u(S^jn)=64^{-j}u(n),\qquad
 u(S^jn)(3S^jn+1)=Un.
\tag{20a}
\]

Thus the map \((x,u)\mapsto u(3x+1)\) is continuous on these
ternary coordinates and recovers the ternary value of the retained
ordinary endpoint. The averaged joint law of
\((S^jn,u(S^jn),Un)\) has the exact weak limit

\[
 \boxed{\sum_{c=1,2}\int_O
      \left(x\mapsto\left(x,\frac{q}{3x+1},q\right)\right)_*m_c
                 \,d(U_*\mu_c)(q).}
\tag{20b}
\]

To prove this, apply (18) and the continuous map
\((x,q)\mapsto(x,q/(3x+1),q)\); the denominator is a ternary unit.
The valuation phase is therefore explicitly correlated with the Haar
coordinate. The endpoint is preserved on the algebraic graph
\(u(3x+1)=q\), rather than being destroyed by the Haar marginal.

## 4. The Green defect is exact, not an unproved regularity hypothesis

For \(1<s<2\), write

\[
 Z_{s,N}=\sum_{k=0}^NP_s^k1,\qquad
 Z_s=\sum_{k\ge0}P_s^k1,\qquad
 \rho(s)=\frac{3^{s-1}}{2^s-1}<1.
\tag{21}
\]

Harmonicity of the normalized ordinary source gives

\[
 \int Z_{s,N}\,d\mu=N+1,\qquad \int Z_s\,d\mu=\infty.
\tag{22}
\]

This is not caused by an infinite value at one ordinary atom. In an
escaping component the sets \(\{n:U^kn=q\}\), for different
\(k\ge0\), are disjoint. Otherwise \(q\) would be periodic.
Their masses, using (1), give

\[
 \mu(\{q\})Z_s(q)
   =\sum_{k\ge0}\sum_{U^kn=q}\mu(\{n\})\le1.
\tag{23}
\]

In particular \(Z_s(q)<\infty\) at **every** ordinary \(q\in E\).

The averaged conditional law in (11) retains \(\mu/J\). Hence

\[
 \boxed{\int Z_{s,N}\,d\bar\nu_J\ge\frac{N+1}{J},
        \qquad \int Z_s\,d\bar\nu_J=\infty
        \quad(J<\infty).}
\tag{24}
\]

In contrast its ternary limit (15) has an explicit finite Green integral.
Put \(m=(m_1+m_2)/2\). A change of variables in each legal branch
of (3) proves

\[
 m_cP_s=\beta_c(s)m,\qquad
 \beta_1(s)=\frac{2\,3^{s-1}}{2^{2s}-1},\qquad
 \beta_2(s)=2^s\beta_1(s),\qquad mP_s=\rho(s)m.
\tag{25}
\]

For the change of variables, \(q=(3n+1)/2^e\) has ternary Haar
Jacobian \(1/3\), and the density of \(m_c\) relative to \(m\)
on its class is two. The permitted exponents are even for \(c=1\)
and odd for \(c=2\). Summing their geometric weights gives (25).
Therefore, with \(\beta_\pi=\pi_1\beta_1+\pi_2\beta_2\),

\[
 \boxed{\int Z_s\,d\eta
      =1+\frac{\beta_\pi(s)}{1-\rho(s)}<\infty.}
\tag{26}
\]

For each fixed \(N\), (15) applies to the continuous function
\(Z_{s,N}\). More exactly, \(P_s^k1\) depends only on the residue
modulo \(3^{k+1}\). If \(3^N\mid J\), complete periods give

\[
 \int Z_{s,N}\,d\bar\nu_J=\int Z_{s,N}\,d\eta.
\tag{27}
\]

Thus the iterated limits are different:

\[
 \lim_{N\to\infty}\lim_{J\to\infty}
       \int Z_{s,N}\,d\bar\nu_J
   =1+\frac{\beta_\pi}{1-\rho},\qquad
 \lim_{J\to\infty}\lim_{N\to\infty}
       \int Z_{s,N}\,d\bar\nu_J=\infty.
\tag{28}
\]

This rules out a uniform-integrability passage for this precise average.
It does not assert the same result for every shifted block of conditional
laws. For one conditional law, the exact formula is instead

\[
 \boxed{\int Z_s\,d\nu_j
   =t^{-j}\sum_{k\ge0}\mu(U^{-k}C_j)
   =t^{-j}\int\#\{k\ge0:a(U^kn)\ge6j+1\}\,d\mu(n).}
\tag{29}
\]

To check it, expand the nonnegative Green sum and use the atom equality
\(\mu(\{q\})(3^k/2^A)^s=\mu(\{n\})\) for every actual
\(k\)-step predecessor \(n\) of \(q\). Formula (29) identifies
the precise future occupation quantity required for a different choice
of conditioning windows.

The retained ordinary label also keeps an infinite Green integral. Indeed

\[
 U_*\mu=(P_s1)\mu.
\tag{30}
\]

The continuous positive function \(P_s1\) has a positive minimum:
it is a strictly positive function of the finitely many unit classes
modulo nine. Equations (22) and (30) give

\[
 \int Z_s(q)\,d(U_*\mu)(q)=\infty.
\tag{31}
\]

Consequently even the conditional-Haar joint limit (18) has an infinite
Green integral in its **ordinary endpoint coordinate**, while its ternary
coordinate has (26). The two coordinates are not interchangeable.

## 5. Quantified source cost and an arbitrary-averaging bound

By (7), the exact density of (11) relative to the original ordinary
source is

\[
 h_J=\frac{d\bar\nu_J}{d\mu}
    =\frac1J\sum_{j<J}t^{-j}1_{C_j}.
\tag{32}
\]

Each ordinary atom belongs to only finitely many \(C_j\), so
\(h_J\to0\) pointwise, even though \(\int h_Jd\mu=1\).
In fact

\[
 \boxed{\|h_J\|_2^2
  =\frac1{J^2}\sum_{k=0}^{J-1}(2(J-k)-1)t^{-k}.}
\tag{33}
\]

This follows by expanding the square and using
\(\mu(C_i\cap C_j)=t^{\max(i,j)}\). In particular

\[
 \frac{t^{-(J-1)}}{J^2}\le\|h_J\|_2^2
 \le\frac{1+t}{(1-t)^2}\frac{t^{-(J-1)}}{J^2}.
\tag{34}
\]

The ordinary height is also lost explicitly:

\[
 \bar\nu_J\{n\le H\}
 \le\min\left(1,\frac{1+\lfloor\log_{64}H\rfloor}{J}\right)
 \quad(H\ge1),
\tag{35}
\]

because \(S^jn\ge64^j\) for every positive integer \(n\).
Thus (15) has no tight lift in the discrete ordinary current-state
coordinate, even though its ordinary **next-state** coordinate is fixed.

There is a stronger bound for arbitrary nonnegative averaging weights.
Let \(c_j\ge0\), \(\sum_jc_j=1\), and
\(\nu=\sum_jc_j(S^j)_*\mu\). Fix an ordinary atom \(m\) of
mass \(p=\mu(\{m\})>0\). Suppose that at precision \(3^K\)

\[
 \nu(a+3^K\mathbb Z_3)\le D/L_K
 \quad\text{for every unit residue }a,
\tag{36}
\]

where \(D>0\). Since the orbit of \(m\) has exact period \(L_K\),

\[
 \sum_{j\equiv r\ (\mathrm{mod}\ L_K)}c_j
       \le\frac{D}{pL_K}\quad(0\le r<L_K).
\tag{37}
\]

Set \(k=\lfloor pL_K/(2D)\rfloor\). The existence of a
probability satisfying (36) implies \(D\ge1/2\), hence
\(k\le L_K\). Summing (37) over \(0\le j<k\) yields
\(\sum_{j<k}c_j\le1/2\). Because \((S^j)_*\mu\) is supported
on \(C_j\), it follows that \(\nu(C_k)\ge1/2\). For every
\(u>1\), Hölder's inequality now proves

\[
 \boxed{\left\|\frac{d\nu}{d\mu}\right\|_u
       \ge\frac12\,t^{-k(1-1/u)}.}
\tag{38}
\]

The conclusion also holds if the norm is infinite. For fixed \(p,D,s\),
its cost is exponential in \(3^K\), not merely exponential in \(K\).
This applies to **any** averaging of these same ordinary symmetry powers
that meets the specified ternary atom upper bound. It does not exclude
other source-preserving arithmetic constructions.

## 6. The full odd component gives Haar independent of the ordinary endpoint

There is a stronger corollary on a larger, explicitly different domain.
Extend the component to

\[
 E^+=\{n\ge1:n\text{ odd},\ Un\in E\}.
\tag{39}
\]

This includes the possible initial odd multiples of three. Define
\(\Lambda(n)\), \(r(n)\) by (1) on \(E^+\), and renormalize
afresh to the probability
\(\mu^+=\bigl(\sum_{E^+}r(n)^s\bigr)^{-1}\sum_{E^+}r(n)^s\delta_n\).
It is generally different from \(\mu\); its restriction to \(E\)
is proportional to \(\mu\).

Now use \(S_4(n)=4n+1\). It preserves the positive odd component and
the same ordinary successor, while

\[
 a(S_4n)=a(n)+2,\quad r(S_4n)=r(n)/4,\quad
 S_4^jn=4^jn+(4^j-1)/3.
\tag{40}
\]

The preceding decomposition proof, with two in place of six, gives
\(\mu^+(a\ge2j+1)=4^{-sj}\) and
\(\mu^+(\,\cdot\mid a\ge2j+1)=(S_4^j)_*\mu^+\).
In the ternary completion the valuation identity is now

\[
 v_3(S_4^h x-x)=v_3(h)\quad(x\in\mathbb Z_3,h\ge1),
\tag{41}
\]

so each orbit visits **all** residues modulo \(3^K\) once per period
\(3^K\). With \(m_3\) Haar probability on \(\mathbb Z_3\),
the endpoint-retaining conclusion becomes

\[
 \boxed{\frac1J\sum_{j<J}
       (n\mapsto(S_4^jn,Un))_*\mu^+
       \ \Longrightarrow\ m_3\otimes U_*\mu^+.}
\tag{42}
\]

Here full ternary Haar is independent of the exact retained ordinary
endpoint; there is no class mixture. Its finite-cylinder error is (17)
with \(L_K=3^K\). The binary coordinate still tends to \(-1/3\),
and the valuation-phase lift still satisfies \(u=q/(3x+1)\).

For completeness, the appropriate full-domain pressure operator is

\[
 P_s^+f(q)=\sum_{\substack{e\ge1\\(2^eq-1)/3\in\mathbb Z_3}}
       (3/2^e)^sf((2^eq-1)/3),\qquad q\in\mathbb Z_3.
\tag{43}
\]

The parent integrality requirement is retained, but parents divisible by
three are allowed. There are no branches at roots divisible by three.
Direct atomwise comparison gives \(\mu^+P_s^+=\mu^+\), and the
same Haar change of variables gives \(m_3P_s^+=\rho(s)m_3\).
Thus, for \(1<s<2\), the full-domain Green integral under \(m_3\)
is \(1/(1-\rho(s))\), while every finite cumulative conditioned
average in (42) has infinite Green integral, as in (24).

This enlarged-domain form establishes the strongest conditional Haar
statement here. The ordinary endpoint law remains \(U_*\mu^+\)
throughout, supported on the same hypothetical escaping component.

## 7. Relation to the precise literature attempts

The latest peer result in PR175, commit
`53ba1e1ffc46bf022433c2124a62682ad8dd4739`,
`research/lean-global-closure-20261121/risk24/literature/HIGHER_RANK_BOUNDARY_ATTACK.md`,
obtains a positive Haar component from an explicitly enlarged higher-rank
average of the canonical real boundary. It uses Einsiedler--Lindenstrauss,
*Rigidity properties for commuting automorphisms on tori and solenoids*,
Theorem 1.2:
<https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/rigidity-properties-for-commuting-automorphisms-on-tori-and-solenoids/B5B7471AB9A282B5B179E35040809159>.

The present Haar limit follows instead from the explicit finite ternary
orbit (12); no higher-rank invariance or entropy hypothesis is imported.
It retains a complete ordinary endpoint label in (18), and computes its
surviving Green defect in (31).

Sarig's recurrence criterion for countable Markov shifts, as stated in
Theorem 4.9 of his survey, requires conservativity as part of the
positive-recurrence interface; finite conformal mass alone does not supply
it: <https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/tdf-survey.pdf>.
Equations (24)--(31) are direct calculations of the missing integrability
in this particular ordinary-source construction, rather than an appeal
to that criterion under unproved hypotheses.

PR180, commit `a436db7b85f37abafea25f42d6f34afed02a29c0`,
`research/whole-source-20261123/README.md`, retains the same-source
comparison loss in the actual time-limit collision problem. The law in
(11) is a pressure-law conditioning, not that time law. No new upper bound
for the latter is inferred from (14), (26), or (38).

The concrete remaining task is to control the unchanged ordinary endpoint
law or to construct a different arithmetic coupling whose Green source
term is finite. Conditional ternary Haar is now derived here with that
endpoint still present; its removal is not a measure-theoretic consequence
of Haar regularity.
