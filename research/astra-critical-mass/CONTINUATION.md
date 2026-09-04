# Continuation: finite affine repairs fail, including bounded adaptive blocks

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05, Asia/Jerusalem.
Base: PR #90 at `aeb69ce631370be36fd1f80b472ab448e7df2a73`.

**All new theorem-level claims are PROPOSED pending independent review.**
A full closure was attempted again and was not obtained. This continuation does
not change any verdict on the first packet. The uniform Green bound is still
open. The main new result is a quantitative obstruction to the suggested next
repair: *any finite positive dictionary of affine ternary-valuation terms*,
even after summing all even rays, fails at one ordinary endpoint simultaneously
for every block length up to any fixed bound. Finite full-history Green
truncations are included, with their physical congruence guards retained.

The obstruction is not a disproof of the Green target. Its witness families
carry summable mass. It rules out uniform pointwise finite-dictionary closure,
not an integrated estimate on an infinite family of transported terms.

## 0. Setup and claim map

Use the one-division map T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n.
Let tau(n) be the first hitting time of 1, possibly infinity. On D={2,3,...},
L is the inverse transfer killed on first reaching 1:

    (Lw)(y) = w(2y) + 1_{y == 2 mod 3, y >= 5} w((2y-1)/3).

For a fixed integer H>=1, L_H instead retains only sources, endpoints, and
intermediate states greater than H. A path is killed as soon as it enters
[1,H], even if it would subsequently leave that set. Only for H=1 is the
operator's inverse formula above the definition without additional restrictions.
No convergence claim for [1,H] is needed in the obstruction theorem.

| Claim | Result | Scope |
|---|---|---|
| T-ASTRA-008 | Exact quantitative burden of the fixed Green target | Necessary logarithmic hitting bound; sufficient moment condition is conditional |
| T-ASTRA-009 | Collatz iff a positive summable strict inverse supersolution exists | Equivalence only; converse construction assumes convergence and is not a solution |
| L-ASTRA-010 | Finite affine dictionary tail and even-ray summability | Elementary, with finite ordinary modifications allowed |
| T-ASTRA-011 | Polynomial failure simultaneously for all blocks 1..B | Finite valuation dictionaries and specified lower/upper sandwiches |
| C-ASTRA-012 | Every finite full-history Green truncation has the same obstruction | Includes exact inverse congruence and killing guards |
| C-ASTRA-013 | One deeper history defeats any uniform relative truncation bound | Does not exclude summable integrated remainders |
| X-ASTRA-002 | Exact dictionary, CRT, physical replay, and infinite-ray bounds | Finite cases support the implementations, not the all-parameter proofs |

All proofs are below. The original [PROOF.md](PROOF.md) remains unchanged.

## 1. T-ASTRA-008 — what the previous Green target actually demands

Put w0(n)=3^v3(n+1)/(n+1)^2 and lambda=65/64, and let

\[
G_K=\sum_{n\ge2}w_0(n)\sum_{k=0}^{\min(K,\tau(n)-1)}\lambda^k.
\tag{1.1}
\]

If sup_K G_K<=M<infinity, then every source converges and, for every n>=2,

\[
\boxed{\tau(n)\le
\frac{\log\left(1+M(\lambda-1)(n+1)^2/3^{\nu_3(n+1)}\right)}{\log\lambda}.}
\tag{1.2}
\]

In particular this is a *universal logarithmic* total-stopping bound, not just
pointwise convergence. The earlier proposed working constant M=16 would give

\[
\lambda^{\tau(n)}\le1+\frac{(n+1)^2}{4\,3^{\nu_3(n+1)}}.
\tag{1.3}
\]

### Proof and a converse sufficient estimate

A nonconvergent source makes its single geometric sum diverge. For a convergent
source, its contribution is w0(n)(lambda^tau(n)-1)/(lambda-1), which cannot
exceed M. Rearrangement proves (1.2).

Conversely, if tau(n)<=C log(n+1)+D for all n and C log(lambda)<1, then sup G_K
is finite. This is a conditional sufficient estimate, not a theorem about the
actual stopping times. Indeed lambda^tau(n)<=lambda^D(n+1)^p with p<1. For s>1,
unique factorization m=3^r u with 3 not dividing u gives the exact identity

\[
\sum_{m\ge1}\frac{3^{\nu_3(m)}}{m^s}
=\frac{1-3^{-s}}{1-3^{1-s}}\,\zeta(s)<\infty.
\tag{1.4}
\]

Apply this at s=2-p. This proves summability of the geometric occupation mass.
At s=2, the exact seed mass is (4/3)zeta(2)-5/4 after excluding m=1,2.
There is no assertion that (1.2) and the sufficient estimate have equal constants.

### Consequence for the research strategy

The Green target remains legitimate, but it should not be mistaken for the
weakest closure obligation. A small numerical plateau does not supply the
universal logarithmic estimate (1.2). The following inverse-weight criterion
has no prescribed polynomial lower bound and therefore avoids that extra
quantitative requirement.

## 2. T-ASTRA-009 — the qualitative inverse-weight criterion is exact

The following are equivalent:

1. Every positive Collatz source reaches 1.
2. There is a positive summable W on D with LW<W pointwise.
3. For each fixed rho in (0,1), there is a positive summable W on D with LW<rho W.

The implication 2 -> 1 is the exceptional-set argument of T-ASTRA-002: summing
LW over a nonempty fully invariant exceptional set returns exactly the same
finite mass as summing W, contradicting positive deficits. Thus 3 -> 2 -> 1.

For the converse, **assume** every tau(n) is finite. Set

\[
c(n)=2^{-n}\rho^{\tau(n)},\qquad
W=\sum_{k\ge0}\rho^{-k}L^k c.
\tag{2.1}
\]

Nonnegative summation gives

\[
\|W\|_1
=\sum_{n\ge2}2^{-n}\sum_{r=1}^{\tau(n)}\rho^r
\le\frac{\rho}{2(1-\rho)}.
\tag{2.2}
\]

Moreover W>=c>0 and LW=rho(W-c)<rho W. This proves 1 -> 3.

**The converse uses the unknown stopping times.** It is not an unconditional
construction and is not presented as progress in proving convergence itself.
Its purpose is to separate two targets that the earlier narrative might blur:
existence of a summable inverse supersolution is an exact qualitative criterion;
existence of one dominating the specified w0 with a fixed discount demands
additional quantitative control.

## 3. L-ASTRA-010 — a finite affine dictionary and its even-ray envelope

Let a finite nonempty dictionary contain triples (A_i,B_i,c_i), where A_i is a
positive integer coprime to 3, B_i is an integer, and c_i>0. For sufficiently
large n, all A_i n+B_i are positive. Define

\[
f_i(n)=\frac{3^{\nu_3(A_i n+B_i)}}{(A_i n+B_i)^2},\qquad
F(n)=\frac{c_0}{n^2}+\sum_i c_i f_i(n),\quad c_0\ge0.
\tag{3.1}
\]

A finite initial range can be assigned any positive finite values; no zero
of an affine form is evaluated by this definition. Suppose a positive U obeys,
beyond a fixed ordinary threshold,

\[
d f_*(n)\le U(n)\le F(n),\qquad d>0,
\tag{3.2}
\]

where the selected form * is in the dictionary. Require either B_* != 0 or
all B_i=0. Every exact positive dictionary sum is covered: choose a nonzero
B_* when one exists, and otherwise use the all-zero case. Finite Green
truncations below are covered by the nonzero form n+1.

For 1<a<2, put

\[
W_a(n)=\sum_{j\ge0}a^j U(2^j n).
\tag{3.3}
\]

Then U and W_a are summable over n>=2, and

\[
W_a(2n)=\frac{W_a(n)-U(n)}a<\frac{W_a(n)}a.
\tag{3.4}
\]

### Proof of the source tail

On an integer dyadic block [X,2X), all large X satisfy A_i n+B_i >= A_i X/2
and |A_i n+B_i|<=C_i X. Also

\[
3^{\nu_3(m)}=1+2\sum_{r=1}^{\nu_3(m)}3^{r-1}.
\tag{3.5}
\]

For each r, A_i n+B_i==0 mod 3^r selects exactly one class, so there are at
most X/3^r+1 representatives in the block. Summing (3.5) through
R=floor(log_3(C_i X)) gives O_i(X(1+log X)). Division by (A_i X/2)^2 yields

\[
\sum_{n\ge X}U(n)=O_F((1+\log X)/X).
\tag{3.6}
\]

The finite initial modifications cause no difficulty. Consequently

\[
\sum_{n\ge2}W_a(n)
\le\sum_{j\ge0}a^j\sum_{m\ge2^{j+1}}U(m)
=O_F\!\left(\sum_{j\ge0}(j+1)(a/2)^j\right)<\infty.
\tag{3.7}
\]

Reindexing the nonnegative convergent ray series proves (3.4).

### Exact pointwise truncation bound

Above a fixed threshold, A_i 2^j n+B_i >= A_i 2^j n/2. Since 3^v3(m)<=m for
positive integers m, one has U(2^j n)<=C_F/(2^j n), where one can take
C_F=c_0+sum_i 2c_i/A_i for n>=1 in that threshold range. Hence

\[
0\le W_a(n)-\sum_{j<J}a^j U(2^j n)
\le\frac{C_F(a/2)^J}{n(1-a/2)}.
\tag{3.8}
\]

This is a deterministic bound for the entire omitted infinite ray.

## 4. T-ASTRA-011 — simultaneous polynomial obstruction

For every fixed positive integer B and every finite floor H, there are a
constant c>0 and positive ordinary endpoints y_h tending to infinity such that

\[
\boxed{
\min_{1\le\ell\le B}
\frac{(L_H^\ell W_a)(y_h)}{W_a(y_h)}
\ge c\,y_h^{\theta},\qquad \theta=1-\log_2 a>0,
}
\tag{4.1}
\]

for all sufficiently large h. Constants may depend on the dictionary, a, B,
and the finite initial modifications. In particular even choosing the block
length as an arbitrary endpoint-dependent function ell(y) in {1,...,B}
cannot give an eventual finite upper bound for the transfer ratio.

This is stronger than showing failure for each fixed length separately: the
*same endpoint* defeats all the allowed lengths at once.

### Step 1: a transported centre outside the entire finite union of rays

Let

\[
\mathcal R=\{-B_i/(A_i2^j):i\text{ in the dictionary},\ j\ge0\}.
\tag{4.2}
\]

As a set of real rational numbers, R has no accumulation point except possibly
0. If B_* != 0, the distinct numbers

\[
r_j=-B_*/(A_*2^j),\qquad z_j=(3r_j+1)/2
\tag{4.3}
\]

tend to 1/2. Since R has only finitely many points in a sufficiently small
closed neighborhood of 1/2, some j>=B-1 has z_j not in R. Fix such a j and
write r=r_j, z=z_j. In the all-zero case, R={0}; take any j>=B-1, r=0, z=1/2.

The chosen rational denominators are coprime to 3. No ordinary orbit of these
rational centres is assumed. They specify congruences; the witnesses below
are positive integers.

### Step 2: explicit ordinary source and simultaneous paths

For h>=1 let R_h be the unique residue in [0,3^h) satisfying

\[
A_*2^jR_h+B_*\equiv0\pmod{3^h}.
\]

Set

\[
u_h=R_h+((1-R_h)\bmod2)3^h+2\cdot3^h,
\qquad y_h=(3u_h+1)/2.
\tag{4.4}
\]

Then u_h is odd, 2*3^h<=u_h<4*3^h, and
v3(A_*2^j u_h+B_*)>=h. For every 1<=ell<=B, the actual source

\[
n_{h,\ell}=2^{\ell-1}u_h
\tag{4.5}
\]

follows ell-1 even steps and one odd step to the *same* y_h. All intermediate
states tend to infinity, so every fixed killing floor is avoided eventually.

The ray defining W_a(n_{h,ell}) contains the term at index j-ell+1. By (3.2),

\[
W_a(n_{h,\ell})\ge
 a^{j-\ell+1}d\frac{3^h}{(A_*2^j u_h+B_*)^2}
\ge\frac{c_1}{y_h}
\tag{4.6}
\]

uniformly for ell<=B and large h. These are genuine predecessor contributions
to L_H^ell W_a(y_h).

### Step 3: quantitative control of the endpoint's whole infinite ray

Take D to be a positive denominator of z coprime to 3. For every dictionary
form and k>=0,

\[
C_{i,k}=D(A_i2^k z+B_i)
\]

is a nonzero integer, because z not in R. There is a constant C_*>0 with
|C_{i,k}|<=C_*2^k for every i,k. Also D(y_h-z) is an integer divisible by 3^h
(in fact by 3^(h+1)). Therefore whenever C_*2^k<3^h,

\[
\nu_3(A_i2^k y_h+B_i)=\nu_3(C_{i,k}),
\qquad
3^{\nu_3(A_i2^k y_h+B_i)}\le C_*2^k.
\tag{4.7}
\]

Let J be the nonnegative integer with 2^J<=3^h/C_*<2^(J+1), for h large
enough that it exists. Equation (4.7) bounds the sum over k<J by C_2/y_h^2,
using the convergent series sum(a/2)^k. Equation (3.8) bounds the rest by
C_3(a/2)^J/y_h. Since y_h is comparable to 3^h,

\[
\boxed{W_a(y_h)\le C_4 y_h^{-1-\theta},\qquad \theta=1-\log_2 a.}
\tag{4.8}
\]

Combining (4.6) and (4.8) proves (4.1). QED.

### Precisely what is excluded

The theorem excludes this class of summable finite affine-valuation envelopes,
finite ordinary patching, bounded multiplicative corrections that preserve
(3.2), and bounded adaptive block lengths. It does not exclude signed methods,
unbounded-depth state, nonlinear arithmetic not covered by (3.2), arbitrary
summable weights, or global L1 estimates that tolerate large local ratios.
The case a=3/2 has theta=1-log_2(3/2), but the theorem holds for every 1<a<2.

## 5. C-ASTRA-012 — exact finite Green histories do not repair the problem

Fix N>=0 and lambda>0, and define, using the actual killed operator,

\[
V_N=\sum_{k=0}^N\lambda^k L^k w_0,\qquad
W_{N,a}(y)=\sum_{j\ge0}a^j V_N(2^j y),\quad1<a<2.
\tag{5.1}
\]

Then (4.1) holds with W_{N,a}, for every fixed N, B, and H. Thus adding any
finite number of exact inverse histories, and then repairing *all* even rays,
cannot yield bounded adaptive-block contraction.

### Proof with the guards retained

For a word w of length k, weight q, and affine constant A_w, the only possible
source at endpoint y is n=(2^k y-A_w)/3^q. Include it only when it is an integer,
its actual parity word is w, and all k+1 states exceed 1. This is an exact
guard, not a residue-only replacement. For a valid contribution,

\[
w_0(n)=
\frac{3^{q+\nu_3(2^k y+3^q-A_w)}}{(2^k y+3^q-A_w)^2}.
\tag{5.2}
\]

This follows by substituting n+1=(2^k y+3^q-A_w)/3^q. Its numerator is divisible
by 3^q whenever the source is integral.

For all sufficiently large y, each affine denominator is positive. Dropping
only the guards gives the finite nonnegative majorant

\[
V_N(y)\le
\sum_{k=0}^N\sum_{w\in\{0,1\}^k}
\lambda^k3^q
\frac{3^{\nu_3(2^k y+3^q-A_w)}}{(2^k y+3^q-A_w)^2}.
\tag{5.3}
\]

And V_N(y)>=w0(y). Thus the sandwich (3.2) holds, with selected lower form n+1
and a finite dictionary of A_i=2^k, B_i=3^q-A_w, c_i=lambda^k3^q.
Theorem T-ASTRA-011 applies without claiming that the unguarded majorant is
itself the physical transfer. QED.

## 6. C-ASTRA-013 — the missing tail cannot be uniformly relatively small

For every fixed N and 1<a<2 there is a fixed M>N and an infinite ordinary
endpoint sequence y_h for which

\[
\frac{V_M(y_h)}{W_{N,a}(y_h)}\ge c y_h^{1-\log_2 a}.
\tag{6.1}
\]

In particular the extended full Green potential V_infinity cannot obey
V_infinity<=C W_{N,a} eventually for any fixed finite C. This conclusion is
valid whether V_infinity is finite or infinite.

### Proof

Use the dictionary in (5.3) and select j>=N with
r=-1/2^j and z=(3r+1)/2 not in its ray set. Set M=j+1 and use (4.4).
The positive integer 2^j u_h follows j even steps and one odd step to y_h,
with no visit to 1 for large h. Hence one term of V_M gives

\[
V_M(y_h)\ge\lambda^{j+1}w_0(2^j u_h)\ge c_5/y_h.
\tag{6.2}
\]

Equation (4.8) for the upper dictionary proves (6.1). The chosen history is
necessarily beyond the truncated dictionary; choosing j>=N makes this explicit.

Crucially, the exhibited contributions do *not* prove divergence of the total
Green mass: w0(2^j u_h)<=1/(2^j u_h+1)=O(3^-h), so their sum over h is finite.
Large local relative error and a small integrated mass are compatible.

## 7. What the second closure attempt tried, and where it stops

The proposed next step after the first packet was to add transported affine
forms and certify a remainder. I examined that proposal at its exact scope,
rather than assume a finite dictionary would eventually stabilize.

A first repair adds the displaced forms 8n-1 and 16n-5 to n+1. A second keeps
*every* formal inverse word through a chosen depth, with the actual arithmetic
guards. Both fail for a reason now proved for the entire finite class. The
same endpoint defeats all bounded block choices, so an adaptive choice from
a finite menu is not an escape.

The positive all-history construction is still available. What changed is the
required nature of its tail estimate. A successful certificate cannot assert
that the omitted histories are everywhere a bounded multiple of one fixed
finite dictionary. C-ASTRA-013 disproves that even using just one additional
fixed history. It must control an *integrated* remainder, or use genuinely
unbounded adaptive depth/other arithmetic information.

The current strongest elementary end-to-end target remains

    sup_K sum_{k=0}^K (65/64)^k sum_{tau(n)>k} w0(n) < infinity.

It is **not proved**. The broader qualitative alternative is to construct an
explicit positive summable W with LW<W without imposing the w0 lower profile.
T-ASTRA-009 explains why that alternative does not secretly require a universal
logarithmic stopping bound; its existence proof under Collatz is not usable as
a construction before Collatz is known.

### A precise integrated target, not an established estimate

Let Delta_k=lambda^k L^k w0. Then a sufficient finishing bound is any explicit
summable sequence b_k with ||Delta_k||_1<=b_k for all k. The finite form theorem
allows pointwise spikes in Delta_k, so trying to dominate every Delta_k by a
single fixed W_{N,a} is the wrong uniformity. One can instead seek a partition
by transported centres and *prove* a summable total charge over the partition.
No such all-depth charge estimate was found in this continuation.

## 8. Validation and sources

The new [experiment](../../experiments/X-ASTRA-002-transport-closure/README.md)
constructs ordinary CRT witnesses and bounds every omitted even-ray term using
(3.8). Its exact positive lower bounds are simultaneous for all block lengths
in the declared menu. It separately checks the guarded affine compiler against
inverse enumeration and checks the inverse-potential identity on finite
terminating systems. No experiment is extrapolated into the proofs above.

Two separately written standard-library implementations are used. Their
agreement is implementation independence, not independent mathematical review.
The first packet's proofs, artifacts, and frozen SHA remain intact; no old
claim is silently promoted or amended.

External context consulted, not imported as a proof dependency:

- M. Neklyudov, *Functional analysis approach to the Collatz conjecture*,
  arXiv:2106.11859v9, 2022-06-01, HTML read 2026-09-05:
  https://arxiv.org/html/2106.11859v9 . Operator, resolvent, and stopping-time
  formulations have substantial prior literature; no general priority claim
  is made for adopting an operator viewpoint or for the elementary equivalence.
- M. Inselmann, *An approximation of the Collatz map and a lower bound for the
  average total stopping time*, arXiv:2402.03276, abstract read 2026-09-05:
  https://arxiv.org/abs/2402.03276 . The distinction between ordinary Collatz
  and the stronger universal O(log n) stopping assertion is explicit there.
  No density theorem from that work is used here to claim a fixed-source bound.

The all-parameter finite-dictionary theorem is proved locally, without an
external Diophantine approximation, predecessor-count, or computation premise.
Its external novelty has not been comprehensively established.
