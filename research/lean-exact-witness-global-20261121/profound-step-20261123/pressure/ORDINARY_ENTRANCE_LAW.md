# An ordinary entrance law from the complete inverse Green potential

23 November 2026. **Written theorem under the unchanged hypothetical
escaping-component setup. Escape exclusion and sibling Harnack remain
OPEN.** The construction below keeps the actual terminal ordinary integer
and its exact hitting clock. It is a potential transform with killing,
not a stationary inverse policy or a Haar replacement.

The complete inverse operator supplies an almost surely finite ordinary
bridge from every moving root. Its terminal integer converges in total
variation to one fixed ordinary source law, while its lifetime minus the
root clock converges to an exact integer phase. The new all-branch capacity
theorem makes these terminal laws have finite total variation after the
nonlinear root embedding, including finite Hellinger length at s=2.
It also gives finite critical Renyi entropy of the complete first-entry
code. Neither result supplies a bound on the chronological entry index.

## 1. Exact objects and literature interface

Use the shortcut T, odd map U, escaping positive odd 3-unit component E,
and original injective ray q_j=U^j(q_0) from
[`BASIN_PRESSURE_PACKING.md`](../../repo-synthesis-20261123/escape/BASIN_PRESSURE_PACKING.md),
BP1--BP3. For s>1 retain

\[
r(n)=\frac1n\prod_{k\ge0}\frac{3U^kn}{3U^kn+1},\quad
0<c_*/n\le r(n)\le1/n,\quad
w_s(q,v)=(3/2^e)^s\quad(Uv=q),
\]

\[
P_sf(q)=\sum_{Uv=q}w_s(q,v)f(v),\quad
Z_s=\sum_{k\ge0}P_s^k1,\quad
D(q)=\{n\in E:U^kn=q\text{ for some }k\},
\]

\[
A_s(q)=\sum_{n\in D(q)}r(n)^s=r(q)^sZ_s(q),\qquad
M_s=\sum_{n\in E}r(n)^s\in(0,\infty).
\tag{EL1}
\]

Every legal exponent is included, and no inverse row is renormalized
independently of its Green value. Nonperiodicity gives unique depth for
each ordinary ancestor. Thus Z_s(q) is finite at every q in E.

Vigon's *[Homogeneous Markovian bridges](https://www.numdam.org/item/10.1214/10-AIHP391.pdf)*,
Sections 2--3 and Proposition 3.3, treats potential transforms of
nonnegative transient matrices, even when the initial matrix is not
substochastic. Its potential-transform mechanism suggested the following
instantiation. We prove the needed formulas directly, including every
ordinary endpoint. The general Martin-boundary extension in that paper
has additional graph hypotheses; it is not being invoked here.

There is a normalization typo in the printed Proposition 3.3 on page 885:
the terminal-law denominator is displayed at the terminal state y; it
must be at the starting state x. This was checked in the rendered PDF.
EL3 below proves the corrected normalization directly. The finite checker
also rejects the printed orientation on a two-state transient matrix.

## 2. The killed Green transform has an exact ordinary terminal law

Define a kernel on E with a cemetery state dagger by

\[
K_s(q,v)=w_s(q,v)\frac{Z_s(v)}{Z_s(q)}\quad(Uv=q),
\qquad K_s(q,\dagger)=\frac1{Z_s(q)}.
\tag{EL2}
\]

All other transitions in E have probability zero, and dagger is absorbing.
The resolvent identity Z_s=1+P_sZ_s proves that these probabilities sum
to one. In particular the killing term cannot be dropped.

Let N_q be the final ordinary state, and let tau_q be the number of
inverse edges before the killing transition. For n in D(q), let k be its
unique depth and let W_s(q,n) be the product of the original w_s weights
on that path. The Z factors telescope, including the killing factor:

\[
\Pr_q\{N_q=n,\tau_q=k\}
=\frac{W_s(q,n)Z_s(n)}{Z_s(q)}\frac1{Z_s(n)}
=\frac{W_s(q,n)}{Z_s(q)}
=\frac{r(n)^s}{A_s(q)}.
\tag{EL3}
\]

The final equality uses the exact edge identity
r(v)^s=w_s(q,v)r(q)^s. Summing EL3 over all n in D(q) gives one.
Hence killing occurs almost surely after finitely many ordinary inverse
edges; no residual mass goes to an infinite backward path. The expectation
of tau_q is not asserted finite.

The terminal law is exactly

\[
\boxed{\nu_q(n)=\frac{r(n)^s1_{D(q)}(n)}{A_s(q)}.}
\tag{EL4}
\]

This almost sure termination concerns the new inverse sampler. It is
not termination of the original forward Collatz trajectory.

## 3. One ordinary source law and an integer phase at infinity

Write D_j=D(q_j), A_j=A_s(q_j), and nu_j=nu_(q_j). The sets D_j
increase to E. For the fixed ordinary probability

\[
\mu_s(n)=r(n)^s/M_s,
\]

EL4 is simply mu_s conditioned on D_j. In the convention
TV(mu,nu)=sup_B|mu(B)-nu(B)|, direct summation gives

\[
\boxed{\operatorname{TV}(\nu_j,\mu_s)=1-A_j/M_s\longrightarrow0,}
\qquad
\operatorname{KL}(\nu_j\Vert\mu_s)=\log(M_s/A_j)\longrightarrow0.
\tag{EL5}
\]

The reverse relative entropy is infinite because every later ray atom is
missing from D_j. This orientation is part of the statement.

For n in E choose any k,m>=0 with U^k n=q_m, and put

\[
h(n)=k-m\in\mathbb Z.
\tag{EL6}
\]

This phase is well defined. If U^l n=q_r also, apply U^l and U^k to
the two equalities. The results q_(m+l)=q_(r+k), together with
injectivity of the original ray, give k-m=l-r. For all j>=m,

\[
\boxed{U^{j+h(n)}n=q_j,\qquad j+h(n)\ge0.}
\tag{EL7}
\]

Thus for the killed chain from q_j,
tau_j-j=h(N_j) exactly. Its joint endpoint and centered lifetime obey

\[
\boxed{
\operatorname{TV}\bigl(\mathcal L(N_j,\tau_j-j),
                         \mathcal L(N,h(N))\bigr)
=1-A_j/M_s\longrightarrow0,
\quad N\sim\mu_s.
}
\tag{EL8}
\]

The equality holds because the retained first coordinate makes the graph
map n -> (n,h(n)) injective. A coupling is explicit: sample N from mu_s;
when N belongs to D_j set N_j=N, and otherwise sample nu_j. This has
the correct marginal because mu_s restricted to D_j is
(A_j/M_s)nu_j. Almost surely, N belongs to every D_j after some finite
random J, so N_j=N and tau_j=j+h(N) for all j>=J in this coupling.

In particular tau_j tends to infinity in probability even though N_j
converges to a tight ordinary integer law. This does not require a finite
moment of h. The finite integer h(N) is tight, and tau_j-j converges
in law to it. This is the precise ordinary entrance law from moving roots.

## 4. The terminal laws have finite total root variation

The preceding checkpoint's complete-kernel theorem AC7 gives

\[
\sum_{j\ge0}(A_{j+1}-A_j)^{1/s}\le160+D_s,
\quad
D_s=\frac{(64\,2^\eta)^{1-1/s}}
           {1-2^{-(1-\eta)(1-1/s)}},\qquad\eta=799/800.
\tag{EL9}
\]

Embed each nu_j into ell^s(E) by f_j(n)=nu_j(n)^(1/s), and put
d_j=1-A_j/A_(j+1). The supports are nested. Summing separately over
D_j and D_(j+1)\D_j gives the exact identity

\[
\|f_{j+1}-f_j\|_s^s
=\left[1-(1-d_j)^{1/s}\right]^s+d_j\le2d_j.
\tag{EL10}
\]

Here 0<=d_j<=1, and (1-d_j)^(1/s)>=1-d_j, so the first term is at
most d_j^s<=d_j. Consequently, with a_s=A_0>0,

\[
\boxed{
\sum_{j\ge0}\|\nu_{j+1}^{1/s}-\nu_j^{1/s}\|_{\ell^s(E)}
\le2^{1/s}a_s^{-1/s}(160+D_s)<\infty.
}
\tag{EL11}
\]

At s=2 this is finite total Hellinger length for the complete ordinary
terminal laws. The limiting vector is mu_s^(1/s), by EL5 or by direct
coordinate convergence and EL11. This controls a nonlinear source-law
variation, not merely the scalar total mass. It gives no chronological
rate for the tail of that variation.

## 5. Critical Renyi entropy of the complete first-entry code

Use the exact disjoint partition AC2: the initial basin D_0, every later
ray atom q_j (j>=1), and every off-spine basin B_(j,e). Let C(n) label
which part contains n. Every legal parent, both ternary colours, and all
exponents occur in this countable alphabet. Under N~mu_s its probabilities
are

\[
\pi_0=a_s/M_s,\qquad
\pi_{j,\mathrm{atom}}=r(q_j)^s/M_s,\qquad
\pi_{j,e}=b_{j,e}/M_s.
\tag{EL12}
\]

The complete source partition and AC6 therefore yield

\[
\boxed{
\sum_c\pi_c^{1/s}
\le M_s^{-1/s}\bigl(a_s^{1/s}+160+D_s\bigr)<\infty.
}
\tag{EL13}
\]

Hence C(N) has finite Renyi entropy of order p=1/s, and finite Shannon
entropy. Explicitly,

\[
H(C(N))\le H_{1/s}(C(N))
\le\frac{s}{s-1}\log\!\left[
M_s^{-1/s}(a_s^{1/s}+160+D_s)\right].
\tag{EL14}
\]

Jensen applied to log under the probabilities pi proves
H<=H_p; the same argument first on finite truncations with an aggregate
remainder justifies the countable case. Equivalently, Shannon lengths
ceil(-log_2 pi_c) satisfy Kraft's inequality and have finite expected
length. These lengths encode the discrete label, not its numerical time.

The endpoint N itself also has finite Shannon entropy, directly from
c_*/n<=r(n)<=1/n and sum n^(-s) log n<infinity. That elementary fact
does not yield EL13 at the critical order: the corresponding ungrouped
sum is M_s^(-1/s) sum_(n in E) r(n), whose finiteness is not asserted.
The first-entry partition and the new sparse-minimum theorem are what
give the critical Renyi estimate.

## 6. The exact sibling transport density and free-energy target

Let Phi_j:D(q_j)->D(Sq_j) be the complete ordinary balanced inverse
bijection from
[`BALANCED_INVERSE_TRANSPORT.md`](../../universal-step-20261123/escape/BALANCED_INVERSE_TRANSPORT.md).
Let Delta_j(n) be its signed exponent cost. Put

\[
R_j=Z_s(Sq_j)/Z_s(q_j),\quad
\widehat\nu_j=(\Phi_j^{-1})_*\nu_{Sq_j},\quad c=s\log2.
\]

The full path-tree bijection retains every depth and every legal exponent.
Its exact weight identity gives

\[
\boxed{
R_j=\mathbb E_{\nu_j}e^{-c\Delta_j},\qquad
\frac{d\widehat\nu_j}{d\nu_j}(n)
=\frac{e^{-c\Delta_j(n)}}{R_j}.
}
\tag{ST1}
\]

Indeed r(Phi_j n)^s=64^(-s)2^(-s Delta_j(n))r(n)^s and
A_s(Sq_j)=64^(-s)R_j A_j. All factors in ST1 refer to the same
ordinary source n and its actual transported ancestor.

### Affinity and fractional moments

For 0<alpha<1 the exact overlap is

\[
\sum_n\nu_j(n)^{1-\alpha}\widehat\nu_j(n)^\alpha
=R_j^{-\alpha}\mathbb E_{\nu_j}e^{-\alpha c\Delta_j}\le1.
\tag{ST2}
\]

Thus Hellinger affinity is
E_(nu_j)2^(-s Delta_j/2)/sqrt(R_j). The inequality is Holder's
inequality on the two complete probability laws. Equivalently,
R_j>=(E_(nu_j)e^(-alpha c Delta_j))^(1/alpha).

The directed relative entropy is

\[
\operatorname{KL}(\nu_j\Vert\widehat\nu_j)
=\log R_j+c\,\mathbb E_{\nu_j}\Delta_j\in[0,\infty].
\tag{ST3}
\]

This extended formula does not hide an integrability assumption:
E_(nu_j)(Delta_j)^- is finite because its exponential moment in ST1
is finite; the positive part may have infinite expectation. In the
opposite direction the positive part is integrable after tilting and
the negative part may have infinite expectation. No cancellation of
two infinite terms is used.

### An exact variational formulation on finite ordinary source sets

Let sigma range over probability distributions of finite support in
D_j. Every Delta_j on such a support is a finite integer. Then

\[
\boxed{
-\log R_j
=\inf_\sigma\left[
s\log2\,\mathbb E_\sigma\Delta_j+
\operatorname{KL}(\sigma\Vert\nu_j)\right].
}
\tag{ST4}
\]

Proof: subtract -log R_j from the bracket. The result is exactly
KL(sigma||widehat_nu_j)>=0 by ST1. For a finite nonempty F choose
sigma=widehat_nu_j conditioned on F. Its resulting gap is
-log widehat_nu_j(F), which tends to zero as finite sets exhaust D_j.
This proves both directions without assuming an integrable whole-tree
cost or invoking compactness of trial distributions.

Consequently the desired Harnack comparison is exactly an upper bound
on the infimum of this **ordinary cost plus entropy penalty**. A
particularly concrete sufficient estimate would use a fixed finite
F subset E of positive mu_s mass. Eventually F subset D_j and
nu_j(F)>=mu_s(F). The trial law sigma_j=nu_j conditioned on F gives

\[
R_j\ge\nu_j(F)\exp\bigl(-s\log2\,
                          \mathbb E_{\sigma_j}\Delta_j\bigr).
\tag{ST5}
\]

Thus an upper bound on this average signed cost of the form

\[
\mathbb E_{\sigma_j}\Delta_j
\le\log_2\bigl[(1+\log(q_j+1))\log(2+\log(q_j+1))\bigr]+C
\tag{ST6}
\]

would prove HC-new and exclude escape. This estimate has not been
proved. The balanced compiler gives actual transported integers, but its
per-edge cost bound alone does not give ST6. The finite trial formulation
also permits changing F and sigma, provided their relative-entropy
penalty is paid; fixed F is sufficient, not necessary.

### Normalized-law agreement cannot determine the Green normalizer

The change Delta_j -> Delta_j+L_j multiplies R_j by 2^(-sL_j),
but leaves widehat_nu_j, both normalized-law relative entropies, and
Hellinger affinity unchanged. In particular take an arbitrary fixed
ordinary probability nu and constant costs Delta_j(n)=L_j. Then
widehat_nu_j=nu exactly, its density is identically one and uniformly
integrable, and its affinity is one, while R_j=2^(-sL_j) can decay at
any prescribed rate obtained from increasing integer L_j.

This is an exact measure-theoretic control example, not a claim that
constant costs occur on an actual Collatz inverse tree. It proves that
even perfect agreement of the normalized transported terminal laws
does not imply the missing lower comparison. Absolute cost, equivalently
the free-energy normalizer in ST4, must still be controlled arithmetically.

The actual compiler also has the anchor Delta_j(q_j)=0 at its empty
address. This gives R_j>=nu_j(q_j)=1/Z_s(q_j), but does not repair the
normalized-law argument. There is an anchored control preserving this
zero cost: take t=2^(-sL), put mass epsilon=t^2 at the root atom, set
its cost to zero, and set every other cost to L. Then

\[
R=t+t^2-t^3,\qquad
\operatorname{TV}(\nu,\widehat\nu)\le t,\qquad
\sum_n\sqrt{\nu(n)\widehat\nu(n)}\ge1-t.
\tag{ST7}
\]

The normalized density is 1/R at the root and t/R<=1 elsewhere.
For any M>1 its large-density integral is either zero or t^2/R; in
the latter case R<1/M and t<=R, so that integral is at most t<1/M.
Thus this whole family is uniformly integrable with an explicit 1/M
tail modulus, and its two terminal laws merge in total variation, while
R tends to zero at the prescribed scale t. This anchored probability
example is not asserted to be realized by Collatz addresses. It isolates
the absolute arithmetic cost that normalized transport cannot detect.

## 7. Testing the proposed closing imports

### What the potential transform supplies

The literature mechanism supplies a correct ordinary bridge and an
explicit entrance law. It does not compare two incomparable basins.
On the escaping ray, D(q_j) and D(Sq_j) are disjoint. There is no path
from q_j to Sq_j using the directed inverse kernel, or in the opposite
direction. Thus a Harnack-chain argument requiring communication in both
directions has no such chain in this operator. Adding forward edges
changes the operator and its potential.

### What thermodynamic recurrence would require

Sarig's [survey, Theorem 4.9](https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/tdf-survey.pdf)
requires a topologically mixing countable Markov shift, summable
variations and finite Gurevich pressure, with conservativity in its
positive-recurrence characterization. The ordinary acyclic inverse graph
does not supply that recurrent system. EL5 and EL8 preserve the original
source and prove a limit, but they do not make it invariant for U or
identify a compact stationary canonical kernel. The prior checkpoint
already recorded this recurrence boundary; the new contribution here is
the explicit potential bridge and its finite root variation.

### Why a large inverse population is not the needed small source

[Krasikov--Lagarias, Theorem 6.1](https://www.impan.pl/shop/en/publication/transaction/download/product/81918)
gives an x^0.84 lower bound for the number of ordinary ancestors of each
fixed positive target a not divisible by three, for x>=x_0(a). That
statement's target-dependent threshold does not by itself produce an
ancestor of Sq_j at height polynomial in j, nor the needed relative
Green lower bound. We do not import any stronger uniform version from
that paper without reconstructing its corresponding constants.

### Finite entropy does not control a chronological index

For a precise control, put p_k=2^(-k-1) at times
J_k=2^(2^k), k>=0. Then sum p_k^alpha is finite for every alpha>0,
yet

\[
\sum_k p_k\log_2 J_k=\sum_k\tfrac12=\infty.
\tag{EL15}
\]

This is an abstract probability example, not a Collatz counterexample.
It shows exactly why EL13 cannot be converted into a bound on the
first-entry clock or into the sibling comparison without arithmetic
information about the labels.

## 8. Formal and computational scope

`EntranceLaw.lean` proves nine finite statements: later merging,
uniqueness of the merge phase, its integer form, the exact later hitting
clock, uniqueness of a hit on an injective ray, telescoping of transformed
path weights, the terminal killing factor, finite row normalization, and
invariance of the normalized tilt under a common positive scaling.
It does not formalize the countable Markov construction, total-variation
limits, real root estimates or entropy inequalities above.

`check_entrance_law.py` independently enumerates finite actual inverse
trees and compares their complete normalized terminal weights with the
finite killed-transform recursion using exact rational arithmetic. It
also checks balanced transport densities and fractional overlap, merge
phases on literal ordinary paths, and omitted-killing and lost-source
controls. These finite convergent examples do
not instantiate an escaping ordinary component.

The lower comparison HC-new remains the direct escape-closing target.
The potential-transform route has now been carried through to an exact
same-source entrance law; the first unsupported step is a quantitative
arithmetic comparison of its incomparable side basins. No universal
Collatz or residue-512 certificate is asserted.
