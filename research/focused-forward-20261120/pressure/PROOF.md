# The ordinary height cutoff for the all-word root potential

**Status:** PROPOSED elementary theorems, accompanied by exact finite replay.
The proof does not establish finiteness of the infinite-horizon potential, a
pointwise pressure limit, exclusion of an escaping orbit, or Collatz.

The height reduction and the quantitative oscillation argument were developed
jointly in the current investigation and reconstructed independently before
implementation. The starting definition is frozen at:

- PR 149, head `92c0129e794dde3ec55ceec470a12d51ba3f7e2f`,
  `research/forward-inverse-defect/PROOF.md`, definition of `W` and all-action
  Bellman inequality;
- the same head, `research/forward-inverse-defect/CLOSURE_BOUNDARY.md`, the
  distinction between Collatz and the additional root condition `W(1)<infinity`.

No external analytic or ergodic input is used below.

## 1. Map, domain, and finite potential

Let

\[
\mathcal U=\{n\in\mathbb N:n\text{ is odd},\ 3\nmid n\},\qquad
U(n)=\frac{3n+1}{2^{g(n)}},\quad g(n)=v_2(3n+1).
\]

Every forward image of a positive odd integer belongs to \(\mathcal U\).
An inverse letter is

\[
I_g(z)=\frac{2^g z-1}{3},\qquad g\ge1,
\]

and is legal when its value belongs to \(\mathcal U\). All intermediate and
terminal states are required to belong to \(\mathcal U\). For a legal word
of length \(k\), write \(A\) for its total exponent and assign the score
\(8k-5A\). Define

\[
W_N(1)=\max\bigl(\{0\}\cup
 \{8k-5A:0\le k\le N,\ \text{legal inverse words from }1\}\bigr).
\tag{1.1}
\]

Although the collection of words is infinite because individual letters have
no cap, only finitely many can have positive score at a fixed horizon.
The infinite potential is \(W(1)=\sup_N W_N(1)\).
The notation \(W_N(z)\) means the same finite-horizon supremum with
the legal inverse words starting at \(z\) instead of `1`.

For \(m\in\mathcal U\), let \(h(m)\) be its first odd hitting time of `1`,
when that time exists, and put

\[
A_*(m)=\sum_{j<h(m)}g(U^j m),\qquad
S_*(m)=8h(m)-5A_*(m).
\tag{1.2}
\]

Here \(h(1)=A_*(1)=S_*(1)=0\). An assertion restricted to
\(h(m)\le N\) is decidable by replaying at most \(N\) odd steps. It does
not presume eventual convergence of any other source.

## 2. Exact reduction to a finite interval of ordinary integers

### Theorem H1: finite ordinary height formula

For every integer \(N\ge0\), define

\[
H_N=\left\lfloor
 \sqrt[5]{\left\lfloor\frac{256^N-1}{2\cdot243^N}\right\rfloor}
\right\rfloor.
\tag{2.1}
\]

Then

\[
\boxed{
W_N(1)=\max\Bigl(\{0\}\cup
\{S_*(m):m\in\mathcal U,\ m\le H_N,\ h(m)\le N\}\Bigr).
}
\tag{2.2}
\]

Thus the complete inverse tree through depth \(N\), with every legal exponent
allowed, can be replaced by bounded forward replay on a finite interval.
The size of the interval is approximately

\[
2^{-1/5}\left(\frac{2^{8/5}}3\right)^N,
\qquad \frac{2^{8/5}}3\approx1.010477711.
\tag{2.3}
\]

**Proof.** For a nonempty inverse word from `1` to an ordinary positive
endpoint \(m\), affine composition gives

\[
m=\frac{2^A-C}{3^k},\qquad C\text{ a positive integer}.
\tag{2.4}
\]

Consequently \(3^k m<2^A\). A positive score is an integer at least `1`,
so \(5A\le8k-1\). Raising the strict height inequality to the fifth power
gives

\[
2\cdot243^k m^5<2^{5A+1}\le256^k.
\tag{2.5}
\]

Since \(256/243>1\), if \(k\le N\) then

\[
2\cdot243^N m^5<256^N.
\tag{2.6}
\]

Both sides are integers. This is equivalent to
\(m^5\le\lfloor(256^N-1)/(2\cdot243^N)\rfloor\), which yields
\(m\le H_N\). This establishes the cutoff with its strict rounding.

The reversed inverse word is the actual forward orbit of its ordinary
endpoint, with precisely the specified odd exponents. If its first visit to
`1` occurs at time \(h\le k\), all the remaining \(k-h\) odd steps are the
self-loop \(U(1)=1\), whose exponent is `2` and whose score is `-2`.
The word's score therefore equals

\[
S_*(m)-2(k-h)\le S_*(m).
\tag{2.7}
\]

Conversely, every first-hit path with \(h(m)\le N\) reverses to a legal
inverse word from `1`. All its states are units, and its score is
\(S_*(m)\). Taking maxima, and retaining `0` for all nonpositive scores,
proves (2.2). For \(N=0\), \(H_0=0\), the displayed set is empty, and the
same formula gives `0`. The approximation (2.3) follows directly from (2.1).
\(\square\)

### Corollary H2: transfer of the finite root certificate

Suppose \(W_L(1)=0\), and an ordinary \(n\in\mathcal U\) first reaches
`1` in \(h\le L\) odd steps, with total exponent \(A_*\). Then

\[
W_{L-h}(n)\le5A_*-8h.
\tag{2.8}
\]

Indeed, prepend to any inverse word from \(n\) the reversed first-hit path
from `1` to \(n\). The resulting legal inverse word from `1` has length at
most \(L\), so its total score is nonpositive. This is a finite-horizon
ordinary bound. It does not provide the corresponding all-horizon inequality.

### What an all-horizon upgrade would require

The formula does not supply a uniform bound on the right side of (2.2) as
\(N\to\infty\). The cutoff grows with \(N\). In particular,

\[
W(1)=\max\bigl(0,\sup_{m\in\mathcal U:\ h(m)<\infty}S_*(m)\bigr)
\tag{2.9}
\]

is a uniform quantitative question over **all terminating ancestors** of `1`.
Convergence of each inspected integer cannot replace this supremum. Neither
the theorem nor its replay proves that this additional quantitative statement
follows from qualitative Collatz convergence.

### Theorem H3: the stopping-time content of the root condition

Put \(\delta=8-5\log_2 3>0\). Every \(m\in\mathcal U\setminus\{1\}\)
which first reaches `1` in \(h\ge1\) odd steps satisfies

\[
\delta h-5\log_2 m-\frac59\log_2 h-\frac5{9\ln2}
\le S_*(m)\le\delta h-5\log_2 m.
\tag{2.10}
\]

Consequently, if \(W(1)\le B<\infty\), then every such terminating source
obeys

\[
h(m)\le\frac5\delta\log_2 m+
\frac5{9\delta}\log_2(1+\log_2 m)+C_B,
\tag{2.11}
\]

for a constant \(C_B\) independent of the source. The leading coefficient
\(5/\delta\) is approximately `66.500419`. Conversely, a uniform bound
\(h(m)\le(5/\delta)\log_2 m+C\) on this terminating basin implies
\(W(1)\le\max(0,\delta C)\).

**Proof.** Write the first-hit odd states as \(n_0=m,\ldots,n_{h-1}\), and
let

\[
P=\prod_{j<h}\left(1+\frac1{3n_j}\right).
\]

The exact product identity
\(1=3^h mP/2^{A_*}\) gives

\[
S_*(m)=\delta h-5\log_2 m-5\log_2 P.
\tag{2.12}
\]

The \(h\) states before the first visit to `1` are distinct positive odd
units greater than `1`: a repeated state would trap the subsequent orbit in
a cycle before its first visit. If these states are ordered increasingly,
their \(j\)-th member is at least \(3j+1\), for \(1\le j\le h\).
Using \(\ln(1+x)\le x\) and the harmonic-sum bound gives

\[
0\le\ln P\le\sum_{j=1}^h\frac1{9j+3}
\le\frac19\sum_{j=1}^h\frac1j
\le\frac{1+\ln h}{9}.
\tag{2.13}
\]

Substitution into (2.12) proves (2.10). If \(W(1)\le B\), use
\(S_*(m)\le B\) in the lower side of (2.10), obtaining

\[
h\le a\log_2m+b\log_2h+C'_B,
\qquad a=5/\delta,\quad b=5/(9\delta).
\tag{2.14}
\]

The elementary inequality \(b\log_2h\le h/2+C_b\) first gives
\(h\le 2a\log_2m+C''_B\). Inserting this coarse bound back into the
logarithm of (2.14) yields (2.11), with the same leading coefficients.
For the converse, use the upper side of (2.10), or simply \(P\ge1\) in
(2.12), then take the supremum in (2.9). \(\square\)

This result quantifies the additional root obligation using only elementary
arithmetic. It concerns terminating sources and does not assert convergence
of a source outside that basin.

## 3. Every finite all-action certificate needs logarithmic downward oscillations

This section concerns a proposed *global* certificate, not a conclusion that
such a certificate exists.

Let \(V:\mathcal U\to[0,\infty)\) be finite at every point and satisfy all
legal inverse inequalities

\[
V(z)\ge8-5g+V(I_gz).
\tag{3.1}
\]

For real \(X\ge1\), set

\[
D_V(X)=\max\{V(u)-V(v):u,v\in\mathcal U,\ u\le v\le X\}.
\tag{3.2}
\]

The maximum is nonnegative because \(u=v\) is allowed. It measures a
downward change in the potential as the ordinary integer increases. It is
finite for every finite \(X\).

### Theorem O1: quantitative oscillation lower bound

Put \(c=\log_2 3\). Every such \(V\) satisfies

\[
\boxed{
\limsup_{X\to\infty}\frac{D_V(X)}{\log_2 X}
\ge\frac8{\log_2 3}-5>0.
}
\tag{3.3}
\]

In particular, eventual monotonicity, monotonicity up to a fixed additive
error, and a downward oscillation bound \(D_V(X)=o(\log X)\) are all
incompatible with the all-action inequalities and finiteness of \(V(1)\).

**Proof.** Suppose, for a contradiction, that there is a real number

\[
0\le d<\frac8c-5
\tag{3.4}
\]

such that \(D_V(X)\le d\log_2 X\) for all sufficiently large \(X\).
If the limsup in (3.3) were smaller than its asserted lower bound, such a
\(d\) could be chosen strictly between the two.

For every positive **even** integer \(k\), define

\[
n_k=2\cdot3^k-1,\qquad m_k=2^{k+1}-1.
\tag{3.5}
\]

There is a legal inverse word of \(k\) exponent-one letters from \(n_k\)
to \(m_k\). Its intermediate states are

\[
2^{j+1}3^{k-j}-1,\qquad 0\le j\le k.
\tag{3.6}
\]

For \(j<k\), these are `-1 mod3`. The final state is `1 mod3` because
\(k\) is even. All are positive odd units, so (3.1) gives

\[
V(n_k)\ge3k+V(m_k).
\tag{3.7}
\]

Choose \(\ell(k)\) to be the largest nonnegative even integer for which
\(3^{\ell(k)}\le2^k\). Equivalently,

\[
\ell(k)=2\left\lfloor\frac{k}{2c}\right\rfloor
          =\frac{k}{c}+O(1),\qquad n_{\ell(k)}\le m_k.
\tag{3.8}
\]

For all sufficiently large even \(k\), this even integer is positive.
The definition of \(D_V\), with \(X=m_k\), gives

\[
V(m_k)\ge V(n_{\ell(k)})-d\log_2 m_k
          \ge V(n_{\ell(k)})-d(k+1).
\tag{3.9}
\]

Combining (3.7) and (3.9),

\[
V(n_k)\ge(3-d)k+V(n_{\ell(k)})-d.
\tag{3.10}
\]

Iterate this inequality until the decreasing even integer parameter enters
a fixed bounded interval. If \(k_0=k\) and \(k_{j+1}=\ell(k_j)\), the
number of iterations is \(O(\log k)\), and (3.8) implies

\[
\sum_j k_j=\frac{c}{c-1}k+O(\log k).
\tag{3.11}
\]

For completeness, multiply each equality
\(k_j=c k_{j+1}+O(1)\) by `1` and sum. The resulting telescope gives
\((c-1)\sum_j k_j=c k_0+O(\log k)\), because the terminal parameter is
bounded. Nonnegativity of the terminal potential then yields

\[
V(n_k)\ge\frac{(3-d)c}{c-1}k-O(\log k).
\tag{3.12}
\]

For an upper bound, choose the least positive exponent \(a\) with
\(a\equiv2\) or \(4\pmod6\) for which

\[
u_a=\frac{2^a-1}{3}\ge n_k.
\tag{3.13}
\]

These exponents have gaps at most `4`. Hence
\(a=ck+O(1)\), and \(\log_2 u_a=ck+O(1)\). The number \(u_a\) is a
positive odd unit: \(a\) is even, and the excluded class \(a\equiv0\pmod6\)
is precisely the class for which \(3\mid u_a\). The inverse edge from `1`
to \(u_a\) is legal. Applying (3.1) at this edge gives

\[
V(u_a)\le V(1)+5a-8.
\tag{3.14}
\]

Because \(n_k\le u_a\), the downward oscillation bound gives

\[
V(n_k)\le V(u_a)+D_V(u_a)
        \le(5+d)c k+O(1).
\tag{3.15}
\]

Combine (3.12) and (3.15), divide by \(ck\), and let the even integer
\(k\) tend to infinity. The result is

\[
\frac{3-d}{c-1}\le5+d,
\quad\text{hence}\quad
d\ge\frac{8-5c}{c}=\frac8c-5,
\tag{3.16}
\]

contrary to (3.4). Positivity of this constant follows from the exact
inequality \(3^5=243<256=2^8\). This proves (3.3). \(\square\)

### Theorem O1-local: the same oscillation occurs within a fixed height ratio

The conclusion strengthens to

\[
D_{V,16}(X)=\max\{V(u)-V(v):u,v\in\mathcal U,
                       \ u\le v\le\min(16u,X)\},
\qquad
\limsup_{X\to\infty}\frac{D_{V,16}(X)}{\log_2 X}
\ge\frac8{\log_2 3}-5.
\tag{3.17}
\]

**Proof.** The proof of O1 only compares two pairs in the ordinary
ordering. Both pairs have height ratio below `16` for all sufficiently
large even \(k\), as follows.

For the lower comparison, maximality of the even integer \(\ell(k)\)
gives \(2^k<3^{\ell(k)+2}\). Therefore

\[
1\le\frac{m_k}{n_{\ell(k)}}
<9+\frac8{n_{\ell(k)}}<10
\quad\text{when }\ell(k)\ge2.
\tag{3.18}
\]

For the upper comparison, let \(a'\) be the permitted exponent immediately
before the least one chosen in (3.13). Such an exponent exists when
\(k\ge2\). The gap \(a-a'\) is `2` or `4`, and minimality gives
\(u_{a'}<n_k\). Since both are odd integers, \(u_{a'}\le n_k-2\).
The exact recurrences are

\[
u_a=4u_{a'}+1\quad(a-a'=2),\qquad
u_a=16u_{a'}+5\quad(a-a'=4).
\tag{3.19}
\]

Consequently \(n_k\le u_a<16n_k\), including the case in which the
least upper ancestor equals \(n_k\). Replacing \(D_V\) by
\(D_{V,16}\) in (3.9) and (3.15) is now justified. Every subsequent
step of the contradiction is unchanged. This proves (3.17), and O1
also follows because \(D_V\ge D_{V,16}\). \(\square\)

### Theorem O2: a positive oscillation bound at every large height

With the same hypotheses and \(c=\log_2 3\), let

\[
\beta_{12}=
\frac{3\sum_{j=1}^{12}c^{-j}-5}{13}
=\frac{\frac3{c-1}(1-c^{-12})-5}{13}
\approx0.008317501854.
\tag{3.20}
\]

There is a constant \(C_V\) such that, for all sufficiently large real
\(X\),

\[
\boxed{D_{V,16}(X)\ge\beta_{12}\log_2 X-C_V.}
\tag{3.21}
\]

In particular, the liminf of the normalized local oscillation is at least
\(\beta_{12}>1/125\). The larger coefficient in O1-local remains a
limsup assertion; the two claims have different frequency quantifiers.

**Proof.** Fix a positive integer \(r\). Write \(k_0=k\) and
\(k_{j+1}=\ell(k_j)\), and take the even integer \(k\) sufficiently
large that the first \(r\) comparisons in O1-local are available. If
\(X\ge u_a\), all their endpoints are at most \(X\), since the
parameters decrease and \(m_{k_j}<n_k\le u_a\).

Use the single quantity \(D=D_{V,16}(X)\) for every comparison.
The exact inverse-one inequality and the local order comparison give

\[
V(n_{k_j})\ge3k_j+V(n_{k_{j+1}})-D.
\]

After exactly \(r\) iterations, nonnegativity of the terminal value
therefore implies

\[
V(n_k)\ge3\sum_{j=0}^{r-1}k_j-rD
=\frac{3c}{c-1}(1-c^{-r})k-rD-O_r(1).
\tag{3.22}
\]

Here \(k_j=c^{-j}k+O_j(1)\), so the error is bounded when \(r\) is
fixed. At the one-step upper ancestor, (3.14) and the local ratio guard
give

\[
V(n_k)\le V(1)+5a-8+D\le5ck+D+O_V(1).
\tag{3.23}
\]

Combining them and putting \(r=12\) yields
\(D\ge\beta_{12}ck-O_V(1)\).

For each sufficiently large \(X\), choose the largest even integer
\(k\) satisfying \(32\cdot3^k\le X\). The local upper-ancestor
bound shows
\(u_a<16n_k<32\cdot3^k\le X\). Maximality gives
\(X<32\cdot3^{k+2}\), so \(ck=\log_2 X+O(1)\). Substitution proves
(3.21).

The positive lower bound uses only integer comparisons. The exact
inequality \(3^{41}<2^{65}\) gives \(c<65/41\), hence

\[
\beta_{12}>
\frac{3\sum_{j=1}^{12}(41/65)^j-5}{13}
=\frac{595363245098837407663}{73944117820374267578125}
>\frac1{125}.
\tag{3.24}
\]

This also verifies positivity without a floating-point assumption.
\(\square\)

### Scope of O1

The theorem rules out a broad family of simple all-action certificates. It
does **not** rule out the global upper envelope
\(W(n)\le5\log_2 n+C\): an irregular function can obey an upper envelope
while having the downward oscillations forced by (3.3). It also does not prove
\(W(1)=\infty\), nor the nonexistence of every finite all-action potential.

The needed oscillations concern the ordinary integer ordering. Haar tails or
regularity of typical ternary points do not supply their values at any fixed
ordinary integer.

## 4. Computation and remaining obligation

`height_certificate.py` computes the exact fifth-root cutoff using arbitrary
integers and checks both neighboring endpoint inequalities. It then either
uses an independent uncached Python replay or invokes `height_replay.cpp`.
The latter memoizes exact first-hit depths and total division exponents;
it checks arithmetic overflow before every forward multiplication. A path
which has not hit `1` within the horizon is excluded from the finite maximum,
with no assertion about its later behavior. The program is therefore a finite
procedure even without assuming Collatz.

The saved JSON receipts record the actual finite scopes. `README.md` gives
commands and explains the independent controls. A bounded replay supports H1
at its reported horizon; it does not validate an infinite-time extrapolation.

The root-potential route still lacks a uniform ordinary bound on (2.9).
Neither the height cutoff nor the oscillation theorem provides that bound.
A complete Collatz proof must additionally cover any hypothetical component
outside the basin of `1`: root finiteness alone is not that coverage.
