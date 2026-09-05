# Critical mass, killed transfer, and an explicit failed global certificate

**Agent:** `astra-critical-mass-01` (GPT-6 Pro). **Date:** 2026-09-05, Asia/Jerusalem.

**Status:** All new theorem-level claims are **PROPOSED pending independent review**.
Proofs are supplied below; author reconstruction and finite replay are not independent
mathematical acceptance. The end-to-end target remains **OPEN / GAP-BLOCKED**.
No proof of Collatz, SC*, or FC* is claimed.

This packet attempts two complete routes, rather than assuming an exceptional set
can be replaced by its sparse set of minima. The first sharpens the imported
exponent race at its critical endpoint. The second does not need the imported
predecessor theorem: it constructs a positive summable transfer weight, attempts
to prove global contraction, and derives an explicit all-length obstruction to
the proposed repair. A finite-time Green-mass enclosure retains the entire infinite
source population through a proved analytic tail bound.

## 0. Normalization and dependencies

Throughout,

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\qquad n\in\mathbb N_{>0}.
\]

Let

\[
\tau(n)=\min\{k\ge0:T^k(n)=1\},\qquad
\mathcal E=\{n:\tau(n)=\infty\},\qquad E(X)=\#(\mathcal E\cap[1,X]).
\]

The value infinity is allowed. No finite search is used to assume that an
unexamined source converges. The identities

\[
n\in\mathcal E\iff T(n)\in\mathcal E,
\qquad 2n\in\mathcal E\iff n\in\mathcal E
\tag{0.1}
\]

are immediate from the definition and the fact that the orbit of 1 is the cycle
1,2,1. In particular 1 and 2 are not exceptional.

Only Section 1's final implication invokes the following external hypothesis:

> **P(gamma).** For every fixed positive b with 3 not dividing b, there are
> c_b>0 and X_b such that the number of positive sources at most X that ever
> reach b is at least c_b X^gamma for every X>=X_b.

The source-qualified Mazur import supplies gamma=901/1000. Its published exact
scope, frozen source, and unreplayed certificate boundary are in [SOURCES.md](SOURCES.md).
The transfer theorems in Sections 2-6 are elementary and independent of P(gamma).

## 1. T-ASTRA-001 — critical endpoint and logarithmic-mass closure

For gamma>0 put

\[
D_\gamma(X)=\sum_{\substack{n\le X\\n\in\mathcal E}}n^{-\gamma},
\qquad D_\gamma^{\rm odd}(X)=
\sum_{\substack{n\le X\\n\in\mathcal E,\ n\text{ odd}}}n^{-\gamma}.
\]

Assume P(gamma). Each of the following is sufficient for Collatz:

\[
\liminf_{X\to\infty}\frac{E(X)}{X^\gamma}=0;
\tag{1.1}
\]

\[
\liminf_{X\to\infty}\frac{D_\gamma(X)}{\log X}=0;
\tag{1.2}
\]

\[
\liminf_{X\to\infty}\frac{D_\gamma^{\rm odd}(X)}{\log X}=0.
\tag{1.3}
\]

In particular either E(X)=o(X^gamma) or E_odd(X)=o(X^gamma) suffices. The
strictly smaller power used in PR #87 is sufficient, but not necessary.
No logarithmic loss in the odd-core exponent bridge is necessary at this endpoint.
We do **not** assert that a liminf condition on the *odd count alone* suffices.

### Proof

If E is nonempty, take a fixed exceptional source, divide by powers of two until
it is odd, and call the resulting source a. Then b=T(a) is exceptional and
b is not divisible by 3. Every predecessor of b is exceptional. P(gamma) gives

\[
E(X)\ge c_bX^\gamma\quad(X\ge X_b).
\tag{1.4}
\]

This contradicts (1.1). Partial summation gives

\[
D_\gamma(X)=X^{-\gamma}E(X)
+\gamma\int_1^X E(t)t^{-\gamma-1}\,dt
\ge c_b\gamma\log X-O_b(1).
\tag{1.5}
\]

Thus (1.2) also contradicts nonemptiness.

Every positive integer is uniquely 2^r m with m odd. By (0.1), exactly, with
terms below 1 interpreted as zero,

\[
E(X)=\sum_{r\ge0}E_{\rm odd}(X/2^r),
\qquad
D_\gamma(X)=\sum_{r\ge0}2^{-r\gamma}
D_\gamma^{\rm odd}(X/2^r).
\tag{1.6}
\]

Monotonicity therefore gives

\[
D_\gamma^{\rm odd}(X)\le D_\gamma(X)
\le\frac{D_\gamma^{\rm odd}(X)}{1-2^{-\gamma}}.
\tag{1.7}
\]

Equation (1.5) consequently supplies an eventual positive logarithmic lower
bound for the odd mass too, contradicting (1.3).

Finally, E_odd(X)=o(X^gamma), followed by the same partial-summation formula,
implies D_odd(X)=o(log X): for any epsilon>0, bound the integrand above a fixed
threshold by epsilon/t and absorb the finite initial integral. Alternatively,
the unweighted identity in (1.6) and the convergent geometric series show
E(X)=o(X^gamma) directly. This proves the assertions. QED.

### What has and has not improved

The new target permits a critical logarithmic improvement, for example
E(X)=O(X^0.901/log X). It also permits sublogarithmic weighted mass, or a
cofinal subsequence with vanishing normalized mass. It does not supply any of
these estimates for the actual exceptional set. It does not upgrade the
0.949955... no-descent/root exponent to an exceptional-basin estimate.

### T-ASTRA-007 — a critical recurrence can spend constants instead of an exponent

Let B be nonnegative and locally bounded. Suppose for all sufficiently large X,

\[
B(X)\le A\frac{X^\gamma}{(\log X)^q}
+\kappa X^{\gamma(1-r)}B(X^r),
\quad 0<r,\kappa<1,\quad q>0.
\tag{1.8}
\]

For every p>0 with p<=q and kappa*r^(-p)<1,

\[
B(X)=O\bigl(X^\gamma/(\log X)^p\bigr).
\tag{1.9}
\]

Indeed substitute C X^gamma/(log X)^p into the right side: its recursive term
is kappa*r^(-p) times that expression. Choose C large enough to absorb the
additive term and a finite initial range. Induction along the descending scales
X,X^r,X^(r^2),... proves (1.9).

For the PR #88 fiber notation, the recursive power in (1.8) corresponds exactly
to delta=(1-r)(1-gamma), not a strict improvement over it. A prefactor and a
logarithmic local-error saving can therefore close the critical boundary.
Neither (1.8) nor its required local-error estimate is established here. In
particular the one-native-horizon no-descent kernel cannot simply be used as
that local error; its known entropy exponent is too large.

## 2. T-ASTRA-002 — an unconditional end-to-end positive-mass criterion

On D={2,3,...}, define the killed inverse operator

\[
(\mathcal Lw)(y)=w(2y)+
\mathbf1_{\{y\equiv2\pmod3,\ y\ge5\}}
 w((2y-1)/3).
\tag{2.1}
\]

The omission of the inverse source 1 at y=2 is essential. This is the operator
for trajectories killed on first visiting 1, not for a trajectory that is
allowed to re-enter D from the trivial cycle.

If w(y)>0, sum_{y>=2}w(y)<infinity, and

\[
\mathcal Lw(y)<w(y)\qquad(y\ge2),
\tag{2.2}
\]

then Collatz holds. The same conclusion follows from Lw<=rho*w with rho<1.

### Proof

If E is nonempty, its forward and backward invariance gives, by nonnegative
summation and the finite total mass,

\[
\sum_{y\in\mathcal E}\mathcal Lw(y)
=\sum_{n\in\mathcal E}w(n).
\tag{2.3}
\]

Equation (2.2) makes the left side strictly smaller: the nonnegative deficits
have at least one strictly positive summand. Contradiction. This covers both
nontrivial positive cycles and nonperiodic exceptional orbits. QED.

### A concrete all-history candidate

Set

\[
w_0(n)=\frac{3^{\nu_3(n+1)}}{(n+1)^2},\quad n\ge2,
\qquad \lambda=\frac{65}{64},
\]

and define the increasing partial Green potentials and masses

\[
V_K=\sum_{j=0}^K\lambda^j\mathcal L^j w_0,
\qquad G_K=\sum_{y\ge2}V_K(y).
\tag{2.4}
\]

These use exact finite physical histories; no stopping-time oracle enters
their definition. Section 4 proves w_0 summable. Iterated preimage counting
and nonnegative summation give

\[
G_K=\sum_{j=0}^K\lambda^j
\sum_{\substack{n\ge2\\\tau(n)>j}}w_0(n)
=\sum_{n\ge2}w_0(n)
\sum_{j=0}^{\min(K,\tau(n)-1)}\lambda^j,
\tag{2.5}
\]

with min(K,infinity)=K.

Consequently the single assertion

\[
\boxed{\sup_K G_K<\infty}
\tag{G}
\]

would prove Collatz without P(gamma). One proof is that an exceptional source
contributes w_0(n) sum_{j=0}^K lambda^j, which diverges. Equivalently, (G)
produces a positive summable V=lim V_K satisfying

\[
V=w_0+\lambda\mathcal LV,
\qquad \mathcal LV=(V-w_0)/\lambda<V.
\tag{2.6}
\]

The explicit working target G_K<=16 for every K is **OPEN**, not a verified
bound. Even the existence of some finite uniform bound remains open. This
particular exponential-moment target is stronger than merely asserting finite
stopping separately for each source; no converse is claimed for this fixed
w_0 and lambda.

## 3. T-ASTRA-003 — power-like pointwise weights cannot close this criterion

Suppose w is positive and

\[
\frac{\log w(n)}{\log n}\longrightarrow-s\quad(s>0).
\tag{3.1}
\]

There is no eventual inequality Lw<=rho*w with rho<(3/2)^s. In particular
there is no eventual nonexpansion Lw<=w for such a weight. This includes
n^(-s) times a positive bounded periodic factor, and n^(-s+o(1)) corrections.
For any fixed block length ell, the corresponding impossible range for
L^ell w<=rho*w is rho<(3/2)^(s*ell).

### Proof

For fixed integer b>=2 and arbitrary k, there is a completely ordinary all-odd
path of length k,

\[
x_j=3^j2^{k-j}b-1\quad(0\le j\le k),
\qquad T(x_j)=x_{j+1}.
\tag{3.2}
\]

All its states exceed any fixed floor when k is sufficiently large. The
nonnegative inverse operator includes each path edge. An eventual inequality
Lw<=rho*w would imply

\[
w(2^kb-1)\le\rho^k w(3^kb-1).
\tag{3.3}
\]

By (3.1), the logarithm of the ratio on the left to the final weight, divided
by k, tends to s*log(3/2). This contradicts rho<(3/2)^s. Taking k a multiple
of ell proves the fixed-block statement. QED.

This is a statement about pointwise inverse supersolutions with the displayed
asymptotics. It does not exclude source-conditioned aggregate inequalities,
height-dependent growing blocks, or strongly oscillating arithmetic weights.
The next construction deliberately introduces such oscillation.

## 4. L-ASTRA-004 — a summable ternary-valuation weight and two successful classes

For w_0 from Section 2,

\[
\sum_{n\ge2}w_0(n)\le3.
\tag{4.1}
\]

More precisely, for an integer M>=2 and K=floor(log_3(M+1)),

\[
\sum_{n\ge M}w_0(n)\le\frac{2K+5}{M+1}.
\tag{4.2}
\]

The following exact pointwise drift inequalities hold:

\[
\mathcal Lw_0(y)\le\frac{16}{49}w_0(y)
\quad(y\equiv0\pmod3),
\tag{4.3}
\]

\[
\mathcal Lw_0(y)\le\frac{87}{100}w_0(y)
\quad(y\equiv2\pmod3).
\tag{4.4}
\]

They do not cover y congruent to 1 modulo 3.

### Proof of summability and the tail

Write n+1=3^k t with 3 not dividing t. Then w_0(n)=3^(-k)t^(-2).
Enlarging the sum and using sum_{t>=1}t^(-2)<=2 proves (4.1).
For k<=K, t>=(M+1)/3^k and

\[
\sum_{t\ge A}t^{-2}\le2/A\qquad(A\ge1).
\]

Each such k contributes at most 2/(M+1). For k>K, use the full t sum:
2 sum_{k>K}3^(-k)=3^(-K)<=3/(M+1). This proves (4.2).
The estimates use inequalities in the safe direction and need no decimal logs.

### Proof of the drift

For y congruent to 0 modulo 3, neither y+1 nor 2y+1 is divisible by 3 and
there is no odd inverse. Thus the ratio is ((y+1)/(2y+1))^2<=16/49.

For y congruent to 2 modulo 3, let k=nu_3(y+1)>=1. Its odd inverse u, when
u>1, satisfies u+1=2(y+1)/3. Therefore

\[
w_0(u)=\frac34w_0(y).
\]

The even inverse has valuation zero, and

\[
\frac{w_0(2y)}{w_0(y)}
=3^{-k}\left(\frac{y+1}{2y+1}\right)^2
\le\frac3{25}.
\]

Their sum is 87/100. At y=2 the odd inverse is omitted, improving the bound.

Finally, on y_k=(3^k-1)/2, k>=2, the only inverse is even and

\[
\frac{\mathcal Lw_0(y_k)}{w_0(y_k)}
=\frac{(3^k+1)^2}{4\,3^k}\longrightarrow\infty.
\tag{4.5}
\]

Thus the obvious third-class extension is false. QED.

## 5. T-ASTRA-005 — the infinite even-ray repair is summable, but every fixed block fails

For any 1<a<2 define

\[
W_a(y)=\sum_{j\ge0}a^j w_0(2^j y),\qquad y\ge2.
\tag{5.1}
\]

This is positive and summable. It repairs all even inverse edges exactly:

\[
W_a(2y)=\frac{W_a(y)-w_0(y)}a<\frac{W_a(y)}a.
\tag{5.2}
\]

Nevertheless

\[
\sup_{y>H}\frac{\mathcal L^\ell W_a(y)}{W_a(y)}=\infty
\qquad\text{for every fixed }H\text{ and }\ell\ge1.
\tag{5.3}
\]

Thus neither enlarging a finite verification floor nor choosing any fixed
block length turns this entire candidate family into an end-to-end certificate.

### Summability and a useful exact truncation bound

Since 3^nu_3(n+1)<=n+1, w_0(n)<=1/(n+1). In particular

\[
0\le W_a(y)-\sum_{j<J}a^jw_0(2^jy)
\le\frac{(a/2)^J}{y(1-a/2)}.
\tag{5.4}
\]

For global summability, (4.2) gives

\[
\sum_{y\ge2}w_0(2^j y)
\le\sum_{n\ge2^{j+1}}w_0(n)
\le\frac{2j+7}{2^{j+1}}.
\]

Here floor(log_3(2^(j+1)+1))<=j+1. Hence

\[
\sum_{y\ge2}W_a(y)
\le\frac12\sum_{j\ge0}(2j+7)(a/2)^j<\infty.
\tag{5.5}
\]

For a=3/2 this bound is 26. Shifting the absolutely nonnegative convergent
series proves (5.2).

### An explicit one-step ordinary obstruction

For h>=1 put

\[
u_h=\frac{3^{4h+2}-1}{8},
\qquad z_h=\frac{3^{4h+3}+5}{16}.
\tag{5.6}
\]

The congruences modulo 16 show that u_h is a positive odd integer, z_h is a
positive integer, and T(u_h)=z_h. No completion is substituted for an integer.
Moreover

\[
W_a(u_h)\ge a^3w_0(8u_h)=a^3 3^{-(4h+2)},
\qquad
z_hW_a(u_h)\ge\frac{3a^3}{16}+o(1).
\tag{5.7}
\]

For every fixed j,

\[
16(2^jz_h+1)=2^j3^{4h+3}+5\,2^j+16.
\]

The second term is a fixed nonzero integer. For large h its 3-adic valuation
is the valuation of the whole right side. It follows that
z_h*a^j*w_0(2^j z_h) tends to zero for every fixed j. Each term is bounded by
(a/2)^j. Splitting off a finite initial segment and applying (5.4) to the tail
therefore proves

\[
z_hW_a(z_h)\longrightarrow0.
\tag{5.8}
\]

Equations (5.7)-(5.8) show

\[
\frac{\mathcal LW_a(z_h)}{W_a(z_h)}
\ge\frac{W_a(u_h)}{W_a(z_h)}\longrightarrow\infty.
\tag{5.9}
\]

This is stronger than a single numerically failed inequality: the obstruction
persists beyond every finite ordinary floor.

### Why no fixed block repairs it

Fix ell>=1. Pass to an infinite subsequence of h on which the first ell
parities from u_h agree. There are only 2^ell words, so such a subsequence
exists. Write z=T^ell(u_h). For this fixed word,

\[
8\,2^\ell z=3^{4h+2+q}+C,
\qquad C>0.
\tag{5.10}
\]

After the first odd step C=5. An even step leaves C unchanged; an odd step
replaces it by 3C+8*2^i at prefix length i. Thus C stays strictly positive.
For any fixed j the numerator of 2^j z+1 has a fixed positive nonzero constant
term, so the same valuation argument gives z*W_a(z)->0.
Meanwhile z*W_a(u_h) has a positive lower limit, and the actual ell-step path
contributes W_a(u_h) to L^ell W_a(z). All intermediate states tend to infinity
on this fixed-word subsequence. This proves (5.3), including any additional
fixed killing floor. QED.

### Interpretation

The initial ternary valuation repairs long odd inverse runs. Summing along
even rays repairs even edges. But one subsequent affine shift produces a
new high-valuation family not represented by those two pieces of state.
This suggests retaining more transported affine forms than the current
nu_3(n+1) and an even-ray index. The theorem does not prove that every finite
collection of forms fails, or that every richer arithmetic weight is impossible. The all-history potential
in (2.4) retains precisely the histories omitted by this failed repair.

## 6. X-ASTRA-001 — finite-time Green mass, including every source

For a source cutoff X and horizon K, define d_n=min(K+1,tau(n)), with d_n=K+1
when no visit to 1 occurs by time K. The finite source contribution in (2.5) is

\[
S_{K,X}=\sum_{2\le n\le X}w_0(n)
\frac{65^{d_n}-64^{d_n}}{64^{d_n-1}}.
\tag{6.1}
\]

This is a finite rational sum. By (4.2), with L=floor(log_3(X+2)),

\[
0\le G_K-S_{K,X}
\le\frac{2L+5}{X+2}
\frac{65^{K+1}-64^{K+1}}{64^K}.
\tag{6.2}
\]

The formula sums all sources beyond X, whether or not they ever converge.
It is not a statistical tail estimate.

The implementation rounds each term of (6.1) down to a multiple of 2^(-80).
If the sum of these integer floors is A, the finite rational contribution lies
between A/2^80 and (A+X-1)/2^80. Adding (6.2) gives a completely rational
interval for the full G_K. At X=262144, deterministic generation and a
separately written replay give the following deliberately outward-rounded
intervals:

| K | Lower bound for G_K | Upper bound for G_K |
|---|---:|---:|
| 16 | 5.0856 | 5.0877 |
| 32 | 6.0883 | 6.0928 |
| 64 | 8.3049 | 8.3165 |
| 128 | 8.6121 | 8.6543 |
| 256 | 8.6140 | 8.9619 |

The exact rational endpoints, not these decimals, are authoritative. See
[the experiment](../../experiments/X-ASTRA-001-critical-mass/README.md).
One source within the finite cutoff remains unresolved at the time-256 cap;
it is conservatively assigned the full finite geometric sum. No convergence
claim is inferred for that source from this calculation.

**These intervals cover infinitely many sources but only finitely many times.**
The bound (6.2) grows with K at a fixed source cutoff. Therefore the table does
not prove (G), nor license extrapolating the apparent numerical plateau.

## 7. Exact remaining proof obligations

The two available completion routes are deliberately kept separate:

1. **Critical-mass route, source-qualified:** prove (1.1), (1.2), or (1.3)
   for the actual exceptional set, then apply P(901/1000). A conditional
   recurrence such as (1.8) is not yet a derivation of those bounds.
2. **Green route, elementary:** prove a uniform-in-K bound in (G) for the
   explicit w_0 and lambda=65/64. The construction and its finite-time
   enclosures are valid, but neither the valuation weight nor its even-ray
   repair supplies the needed uniform inequality.

The exact first-passage fiber compiler in [FIRST_PASSAGE.md](FIRST_PASSAGE.md)
provides a finite ordinary interface for either a source-mass argument or a
more expressive history-dependent certificate. The history of the attempted
closure, its failures, and the proposed next attack are in [ATTEMPT.md](ATTEMPT.md).
