# A positive aggregate transfer from the factoring work

**Status (2026-11-28).** This note reconstructs and implements a genuine positive cross-import. The primary Cartier formula in factoring PR #234 computes individual coefficients of a rational generating function when the coefficient addresses are prescribed. A finite-residue, finite-moment Collatz aggregate has exactly the required rational representation.

The resulting theorem computes **joint odd-grade/residue/carry moments**, not merely a coefficient gcd. It retains real polynomial information and allows arbitrary binary clocks. The cost is polynomial in the **numerical ternary modulus** \(3^k\); it is not polynomial in \(k\). A full ordinary inverse profile still requires the growing modulus \(3^a\) and its moving real interval. No Collatz convergence or \(1/8\) collision lower bound is asserted.

## 1. Actual word carries and the full profile

For a chronological parity word \(w\) of length \(h\), write \(a=|w|_1\). Its ordinary affine identity is
\[
2^h T^h(n)=3^a n+A(w)
\]
whenever \(n\) realizes the word. Let
\[
F_{h,a}(z)=\sum_{\substack{|w|=h\\|w|_1=a}}z^{A(w)}.          \tag{A1}
\]
These are integer polynomials, defined from the full ordered carry. Their exact recurrences are
\[
F_{h+1,a+1}(z)
 =F_{h,a+1}(z^2)+z^{3^a}F_{h,a}(z^2),                    \tag{A2}
\]
and, equivalently by appending the last letter,
\[
F_{h+1,a}(z)
 =F_{h,a}(z)+z^{2^h}F_{h,a-1}(z^3),                      \tag{A3}
\]
with the second term zero for \(a=0\). Initial values are \(F_{0,0}=1\), \(F_{0,a}=0\) for \(a>0\), and \(F_{h,0}=1\).

For (A2), prepending zero sends \(A\) to \(2A\); prepending one to a grade-\(a\) suffix sends it to \(3^a+2A\). For (A3), appending zero leaves \(A\) unchanged, while appending one sends it to \(3A+2^h\).

At a single complex frequency \(z=e(t)\), the recursion is triangular. In the prepend version, all entries at row \(j\) use the same argument \(z^{2^{h-j}}\). Computing the grades \(0,\ldots,a\) takes \(O(ha)\) complex arithmetic operations, with no enumeration of \(2^h\) words.

This is also a polynomial-bit approximation algorithm at specified absolute precision for \(2^{-h}F_{h,a}(e(t))\), when \(t\) is rational in binary. Reduce each phase modulo one exactly. Each phase numerator has only \(O(h+a)\) extra bits. Normalizing each recursion level by two keeps every exact entry bounded by one. If each phase has error at most \(\delta\), and each arithmetic node is rounded with error at most \(\delta\), the maximum error satisfies
\[
E_{j+1}\le(1+\delta/2)E_j+3\delta/2.
\]
For \(h\delta\le1\), this is \(E_h\le3h\delta\). Thus only \(O(\log h)\) guard bits beyond the requested precision are needed. Standard rational interval evaluation of sine and cosine supplies the phase approximations.

The real cutoff has an exact short expression, but it remains a **coefficient selector**. Put \(Q=3^a\). The full ordinary inverse count is
\[
\boxed{\displaystyle
N_{h,a}(y;X)
=[z^{2^h y}]\,
F_{h,a}(z)\sum_{n=1}^{X}z^{Qn}
=[z^{2^h y}]\,
F_{h,a}(z)\frac{z^Q(1-z^{QX})}{1-z^Q}.}                 \tag{A4}
\]
Indeed a contributing pair satisfies \(3^a n+A(w)=2^hy\), with \(1\le n\le X\). The full affine divisibility forces the word to be the actual parity word of that integer. Consequently (A4) keeps both the complete ternary divisor and the real source interval.

Cheap evaluation of \(F\) at one frequency does not by itself extract (A4). Full Fourier inversion has \(3^a\) frequencies even before one implements the interval selector.

## 2. Literal bounded-run descriptions cannot cover the population

The aggregate above avoids a genuine obstruction to describing the source population by a fixed number of powered runs.

For \(h\ge1\), the exact number of binary words of length \(h\) with at most \(r\) nonempty runs is
\[
2\sum_{j=0}^{r-1}\binom{h-1}{j}.                         \tag{A5}
\]
Choose the first bit and the locations of the run boundaries.

If \(2^h\ge X\), the actual length-\(h\) parity words of the integers \(1,\ldots,X\) are distinct, by the binary parity-cylinder bijection. Thus if at least \(\eta X\) of those integers have at most \(r\) runs,
\[
\eta X\le2\sum_{j=0}^{r-1}\binom{h-1}{j}.                \tag{A6}
\]
For \(r-1\le(h-1)/2\), the standard binomial entropy bound gives
\[
\log_2(\eta X)\le
1+(h-1)H_2\!\left(\frac{r-1}{h-1}\right).                \tag{A7}
\]
If \(h\sim c\log_2X\), with fixed \(c>1\), every fixed positive source fraction therefore requires
\[
r\ge\bigl(H_2^{-1}(1/c)-o(1)\bigr)h.                    \tag{A8}
\]
At the median clock \(c=2\log2/\log(4/3)\approx4.81884\), the inverse-entropy constant is approximately \(0.0326513\). A positive fraction needs a number of runs **linear** in \(\log X\).

This only excludes literal bounded-run explanations of the population. It does not exclude an aggregate with a compact algebraic representation. Sections 3–5 construct one.

## 3. A constant matrix for the joint normalized profile

The strongest representation uses the same normalized carry in both completions:
\[
R_h(w)=A(w)/2^h\in\mathbb Z[1/2].
\]
In the real coordinate this is an ordinary nonnegative rational number; modulo
\(Q=3^k\), its dyadic denominator is a unit. Appending zero or one applies,
respectively,
\[
R\longmapsto R/2,\qquad R\longmapsto(3R+1)/2.             \tag{N1}
\]
There is no time-dependent coefficient.

Fix \(d\ge0\), and for \(0\le p\le d\) define the **integer** polynomial
\[
W_{h,r,p}(u)=2^{dh}
\sum_{\substack{|w|=h\\R_h(w)\equiv r\ (Q)}}
u^{|w|_1}R_h(w)^p.
\]
Its integrality follows from
\(2^{dh}R_h^p=2^{(d-p)h}A(w)^p\). The exact recurrence is
\[
\begin{aligned}
W_{h+1,r,p}
={}&2^{d-p}W_{h,\,2r,\,p}\\
&+u\,2^{d-p}
\sum_{\substack{s\bmod Q\\3s+1\equiv2r\ (Q)}}
\sum_{j=0}^p\binom pj3^jW_{h,s,j}.                     \tag{N2}
\end{aligned}
\]
All residue indices are reduced modulo \(Q\). At clock zero only the coordinate
\((r,p)=(0,0)\) is one. Formula (N2) is one constant integer matrix
\(C_{k,d}(u)\), of dimension \(Q(d+1)\) and degree at most one in \(u\):
\[
\boxed{\displaystyle
W_h(u)=C_{k,d}(u)^hW_0,\qquad
\sum_{h\ge0}W_h(u)t^h=(I-tC_{k,d}(u))^{-1}W_0.}        \tag{N3}
\]
Consequently the primary coefficient engine below applies directly to a single
matrix power. Clearing by \(2^d\) per step does not lose information modulo
\(3^e\).

For the top coordinate \(p=d\), the coefficient \([u^a]W_{h,y,d}\) is exactly
\[
\sum_{\substack{|w|=h,\ |w|_1=a\\A(w)/2^h\equiv y\ (Q)}}A(w)^d.
\]
For \(p=0\), divide by \(2^{dh}\) to recover the count. For any \(p\), divide by
\(2^{dh}\) to recover the normalized real moment. The required power of two
is invertible modulo \(3^e\), and can be computed at a binary clock by modular
exponentiation.

In these coordinates the complete ordinary profile is particularly transparent:
\[
\boxed{\displaystyle
R_h(w)\equiv y\pmod{3^a},\qquad
0<y-R_h(w)\le\frac{3^a}{2^h}X.}                        \tag{N4}
\]
Both conditions concern the **same** rational number \(R_h(w)\). The matrix
retains joint residue and real moments of that number; it does not introduce an
independent real seed or discard its ordered numerator.

The adjugate in (N3) gives a fixed bivariate rational representation with
constant denominator term one, degrees polynomial in \(3^k,d\), and coefficient
bit sizes polynomial in those numerical parameters. This is the main positive
representation used in the transfer theorem.

### 3.1. A periodic raw-carry representation

For comparison, the following independently checked representation keeps
\(A(w)\bmod Q\) itself. It proves the same coefficient-extraction interface,
but the normalization above removes its time period and reduces its width.

Fix a ternary precision \(k\ge1\), modulus \(Q=3^k\), and moment order \(d\ge0\). For \(r\bmod Q\) and nonnegative \(p,q\) with \(p+q\le d\), define the polynomial in the odd-count marker \(u\)
\[
V_{h,r,p,q}(u)=
\sum_{\substack{|w|=h\\A(w)\equiv r\ (Q)}}
u^{|w|_1}A(w)^p(2^h)^q.                                \tag{A9}
\]
Use the usual convention \(0^0=1\). All coefficients are nonnegative integers.

Set \(B_h=2^h\). Appending zero sends \((A,B_h)\) to \((A,2B_h)\). Appending one sends it to \((3A+B_h,2B_h)\) and contributes a factor \(u\). Therefore
\[
\begin{aligned}
V_{h+1,r,p,q}
={}&2^q V_{h,r,p,q}\\
&+u\,2^q
 \sum_{\substack{s\bmod Q\\3s+2^h\equiv r\ (Q)}}
 \sum_{j=0}^{p}\binom pj3^j
 V_{h,s,j,p-j+q}.                                      \tag{A10}
\end{aligned}
\]
The total moment degree remains \(p+q\), so this system closes in
\[
D=Q\binom{d+2}{2}
\]
coordinates. At \(h=0\), \(V_{0,0,0,q}=1\), and all coordinates with \(p>0\) or \(r\ne0\) vanish.

The only time-dependent quantity in (A10) is \(2^h\bmod Q\). Its period is
\[
M=\operatorname{ord}_{3^k}(2)=2\cdot3^{k-1}.             \tag{A11}
\]
Let \(A_j(u)\), \(0\le j<M\), be the corresponding integer polynomial transition matrices. Each has degree at most one in \(u\). Put
\[
P(u)=A_{M-1}(u)\cdots A_0(u),\qquad
P_\ell(u)=A_{\ell-1}(u)\cdots A_0(u),
\]
where \(P_0=I\). If \(h=mM+\ell\),
\[
V_h(u)=P_\ell(u)P(u)^mV_0.                              \tag{A12}
\]
This is an actual fixed-power representation, not a replacement of independent calendars by commuting matrices.

Summing all clocks gives the rational vector generating function
\[
\boxed{\displaystyle
\sum_{h\ge0}V_h(u)t^h
=\sum_{\ell=0}^{M-1}t^\ell P_\ell(u)
 (I-t^MP(u))^{-1}V_0.}                                 \tag{A13}
\]
Its denominator has constant term one. An adjugate representation produces explicit bivariate integer numerators and denominator with degrees and coefficient bit sizes bounded polynomially in \(Q,d\). The representation is independent of the eventual binary values of \(h,a\).

In particular the joint residue moment
\[
S_{h,a,r}^{(d)}
=\sum_{\substack{|w|=h,\ |w|_1=a\\A(w)\equiv r\ (3^k)}}
 A(w)^d                                                \tag{A14}
\]
is one coefficient \([t^hu^a]\) of an explicitly constructed rational function of controlled size.

The normalized real moment \(2^{-hd}S_{h,a,r}^{(d)}\) is retained exactly. Modulo a power of three, its denominator is a unit; after integer reconstruction it is an ordinary rational number.

## 4. The imported primary coefficient engine, proved directly

The usable ingredient is the **general numerical-characteristic primary algorithm** in
[uniform_frobenius_descent.md, pinned #234 head](https://github.com/gfreund123/factoring-in-p/blob/5006ac6547cc0106909c31cea730de06baf2405a/research/semiprime-relations-2026-11-26/notes/uniform_frobenius_descent.md).
The later
[known-primary matrix theorem](https://github.com/gfreund123/factoring-in-p/blob/5006ac6547cc0106909c31cea730de06baf2405a/research/semiprime-relations-2026-11-26/notes/uniform_primary_matrix_cartier.md)
explicitly invokes the same \(B^{2e}\) formula.

The source uses all free coefficient-address digits and row spans to compute formal content. For the present consumer we prescribe **both** addresses and retain the exact resulting scalar. This simpler specialization can be verified directly, with no geometric or unknown-characteristic input.

Let \(A(t,u),B(t,u)\in\mathbb Z[t,u]\), \(B(0,0)=1\), let \(p\) be a supplied prime, and work modulo \(p^e\). Set
\[
K=2e,\qquad s=\lceil K/p\rceil,\qquad
U(t,u)=\frac{B(t,u)^p-B(t^p,u^p)}p.                      \tag{A15}
\]
The numerator defining \(U\) is coefficientwise divisible by \(p\).

For \(i,j\in\{0,\ldots,p-1\}\), let \(\Lambda_{i,j}\) select exponents congruent to \((i,j)\bmod p\), remove those digits, and divide the exponents by \(p\). Represent the current rational series as \(V/B^K\). Then its selected section has numerator
\[
\boxed{\displaystyle
\mathcal T_{i,j}(V)=
\sum_{\ell=0}^{e-1}
(-p)^\ell\binom{s+\ell-1}{\ell}
B^{K-s-\ell}
\Lambda_{i,j}\!\left(VB^{ps-K}U^\ell\right)
\pmod{p^e},}                                          \tag{A16}
\]
over the same denominator \(B^K\).

**Proof.** Rewrite
\[
B^{-K}=B^{ps-K}\bigl(B(t^p,u^p)+pU\bigr)^{-s}.
\]
Expand the second factor by the negative-binomial series and discard terms with \(\ell\ge e\), which vanish modulo \(p^e\). A section commutes with multiplication by a series in \(t^p,u^p\), after dividing its exponents by \(p\). Multiplying the resulting denominators back to \(B^K\) gives (A16). All exponents of \(B\) are nonnegative because \(s\le e\).

If \(D_t,D_u\) bound the initial partial degrees of \(A,B\), start with
\[
V_0=AB^{K-1}.
\]
Its partial degrees are at most \(KD_t,KD_u\). Inside the \(\ell\)-th section of (A16), the degree in either coordinate is at most \(p(s+\ell)D_\bullet\). Applying the section and the outside power of \(B\) restores the bound \(KD_\bullet\). Thus every intermediate numerator stays in one polynomial-sized box. There is no denominator of numerical degree \(p^{e-1}\).

Read the ordinary base-\(p\) digits of \(h,a\), least significant first, and apply their **single prescribed** transition at every step. Once both remaining addresses are zero, the desired coefficient is the constant term of the resulting numerator, since \(B^K(0,0)=1\).

For fixed number of variables, dense polynomial arithmetic makes this algorithm polynomial in the numerical \(p,e,D_t,D_u\), the input coefficient sizes and the binary lengths of \(h,a\). Here \(p=3\) is fixed. The primary exponent \(e\) is allowed to grow; this is not the earlier square-precision-only theorem. \(\square\)

### Positive transfer theorem

Combining the stronger representation (N3) with (A15)–(A16) gives a deterministic algorithm for
\[
S_{h,a,r}^{(d)}\pmod{3^e}
\]
whose bit complexity is polynomial in
\[
3^k,\ d,\ e,\ \log(h+2),\ \log(a+2).
\]
The construction uses the numerical residue state space and its actual transition maps.
To obtain the raw-residue convention in (A14), choose the normalized residue
\(2^{-h}r\bmod3^k\). The normalized-residue convention in (N4) is available
directly.

For fixed \(d\), precision \(e=O_d(h)\) recovers the full nonnegative integer moment. Indeed \(A(w)<6^h\) is a crude uniform bound, so
\[
S_{h,a,r}^{(d)}\le 2^h6^{dh}.
\]
Choose \(3^e\) larger than this bound; the modular representative then identifies the integer uniquely. This reconstruction is polynomial in \(h\), as required by the possible output length. It is not polynomial in \(\log h\) when the full integer itself has \(\Theta(h)\) bits.

In a Collatz population with \(h=O(\log X)\), this method remains polynomial in \(\log X\) when \(3^k\), \(d\) and the required precision are polynomial in \(\log X\). It has not compressed a full modulus \(3^a\) with \(a\asymp\log X\).

## 5. Concrete formulas retaining the first real moment

For the normalized residue \(R_h=A/2^h\bmod3\), let \(D_r(t,u)\) generate
the counts and \(K_r(t,u)\) generate the sum of the **raw carry** \(A\) on
the same residue fibre. The latter is the \(d=p=1\) coordinate of (N3).
The constant-matrix formulas reduce to
\[
D_1=\frac{ut^2}{(1-t^2)(1-t(1+u))},\qquad
D_2=\frac{ut}{(1-t^2)(1-t(1+u))},                       \tag{N5}
\]
\[
\boxed{\displaystyle
K_1=\frac{ut^2}{(1+t)(1-2t(1+u))(1-t(1+3u))},\qquad
K_2=\frac{ut}{(1+t)(1-2t(1+u))(1-t(1+3u))}.}           \tag{N6}
\]
The generating function for the normalized real first moment is \(K_r(t/2,u)\).
All displayed unscaled denominators have constant term one and are exact
inputs to the integer primary coefficient engine.

For (N5), if the last odd position is \(j=h-e\), then
\(R_h\equiv2^{-e}\pmod3\). Root residue one selects positive even \(e\);
root residue two selects positive odd \(e\). Summing the free prefix gives
(N5). For (N6), the same split applied to
\(R_h=2^{-e}(3R_j+1)\) gives the first moment, after clearing \(2^h\).
The implementation checks these formulas directly against the final residue of
the actual native orbit on every binary cylinder in its finite census.

### 5.1. The raw-carry residue formulas

At \(k=1\), every nonzero grade has
\[
A(w)\equiv2^j\pmod3,
\]
where \(j\) is the last odd position, numbered from zero. The prefix before that position has arbitrary parity, and the suffix consists of zeros.

Let \(C_r(t,u)\) generate counts with \(A\equiv r\bmod3\), and \(M_r(t,u)\) generate the sum of \(A\) over the same words. Put
\[
\alpha(u)=2+2u,\qquad\beta(u)=1+3u.
\]
Then
\[
C_1=\frac{ut}{(1-t)(1-t^2(1+u)^2)},\qquad
C_2=\frac{ut^2(1+u)}{(1-t)(1-t^2(1+u)^2)},              \tag{A17}
\]
and \(C_0=1/(1-t)\).

For the moment, let \(R_j(u)=\sum_{|w|=j}u^{|w|_1}A(w)\). Appending a letter gives
\[
R_{j+1}=(1+3u)R_j+u[2(1+u)]^j,
\quad R_0=0,
\]
hence
\[
R_j=u\frac{\alpha^j-\beta^j}{1-u}.
\]
At the last odd position, the carry is \(3A_{\rm prefix}+2^j\). Sum separately over even and odd \(j\), then cancel the polynomial factor \(1-u\). With
\[
D(t,u)=(1-t)(1-t^2\alpha(u)^2)(1-t^2\beta(u)^2),
\]
the resulting formulas are
\[
\boxed{\displaystyle
M_1=\frac{tu[1-t^2(1-3u-6u^2)]}{D(t,u)},\qquad
M_2=\frac{t^2u[(2+5u)-t^2\alpha(u)\beta(u)]}{D(t,u)}.}   \tag{A18}
\]
These are fixed rational functions with constant term one in the denominator. They provide explicit, non-oracle inputs to the primary coefficient extractor.

## 6. What the aggregate still does not determine

There are two separate remaining costs.

**Growing ternary precision.** The ordinary integrality condition in (A4) or
(N4) needs \(k=a\), not a fixed number of ternary digits. In the median regime
\(a\) is proportional to \(h\), so the state space \(3^k\) is exponential in
\(h\). Normalization eliminates the additional time period, but not this
residue-space cost. The theorem exposes this cost instead of hiding it in
“fixed rank.”

**The real interval.** Fixed moments do not determine a prescribed window, even when every point lies in the same residue class. For any \(d\), the signed measure
\[
\sum_{j=0}^{d+1}(-1)^j\binom{d+1}{j}\delta_{r+Qj}        \tag{A19}
\]
annihilates every polynomial of degree at most \(d\). Split its positive and negative parts and divide each by \(2^d\). This gives two probability measures with identical first \(d\) moments, supported on the same residue \(r\bmod Q\), but different mass in a small interval about \(r\).

This is a counterexample to inference from the retained moments alone; it is not a counterexample to a stronger estimate exploiting additional structure of actual Collatz word measures. The needed stronger structure is precisely the next consumer.

The companion [JOINT_RESOLVENT_WINDOW.md](JOINT_RESOLVENT_WINDOW.md) now proves
that the full positive integer fibre is compact: the full congruence forces an
actual positive integer source, hence \(0\le R<y\). If
\(L=(3^a/2^h)X\ge y\), no real cutoff remains. Otherwise the ordinary window
can be recovered to normalized error \(\varepsilon+6/X\) using
\(O(\log^2((1+y/L)/\varepsilon))\) nonreal full-fibre resolvent queries,
with explicit pole heights, rational rounding, and absolute evaluation
precision. This supplies the real-window consumer; efficient uniform
evaluation of its **full-conductor joint trace** remains open. Fixed
polynomial moments alone do not supply those values.

There is an exact critical-tail check. Under the uniform law on all length-\(h\)
words, the mean of the two multipliers in (N1) is one, so
\[
\mathbb E R_{h+1}=\mathbb E R_h+\frac14,\qquad
\mathbb E R_h=\frac h4.                                \tag{N7}
\]
This unrestricted law is not supported on one fixed compact interval and is
not uniformly integrable. Its moment growth is compatible with the separate
compactness of every full positive integer fibre just proved; coarse residue
conditioning does not give that compactness. For \(0<q<1\), concavity gives
\[
\mathbb E R_{h+1}^{q}
\le \frac{1+3^q}{2^{q+1}}\mathbb E R_h^q+2^{-q-1},
\]
whose multiplier is strictly below one. These fractional moments are uniformly
bounded, but they do not have the finite polynomial closure used in (N2).
Using them to control a moving fibre is an additional analytic step.

## 7. Verification and source scope

The independent implementation is [primary_cartier_profile.py](primary_cartier_profile.py). It uses only exact integer arithmetic and the Python standard library. The committed receipt is
[primary-cartier-profile.json](../../../reports/astra-collision-factor-bridge-20261128/factoring/primary-cartier-profile.json).

Its exact checks include:

- native shortcut iteration of every binary source cylinder through depth eight, followed by the exact ordinary affine identity;
- both raw-carry and normalized-endpoint residue counts and first carry moments,
  with intermediate primary precision rather than only characteristic three;
- larger count profiles through clock \(511\), checked against literal binomial sums;
- 128-bit clocks, checked against an independent prime-power factorial recursion and, at grade one, exact geometric moment sums.

The proof of the general matrix reductions is written above. The primary
Cartier implementation exercises the explicit \(k=1,d\le1\) rational
functions and the full \(p^e\) coefficient engine; it does not construct all
general \(k,d\) matrices. All 544 guards use explicit checks that remain
active under Python's optimized mode; the normal and optimized outputs agree
after removing timestamps, as recorded in
[primary-cartier-optimization-check.json](../../../reports/astra-collision-factor-bridge-20261128/factoring/primary-cartier-optimization-check.json).

A separate native-orbit implementation,
[check_normalized_matrix.py](check_normalized_matrix.py), tests (N2) for
\(k=1,2,3\), \(d=0,1,2,3\), and \(h=0,\ldots,8\), together with full-fibre
positivity, realization, lattice spacing, and ordinary windows. Its receipt is
[normalized-matrix-independent.json](../../../reports/astra-collision-factor-bridge-20261128/factoring/normalized-matrix-independent.json).

[AggregateProfile.lean](AggregateProfile.lean) formalizes the complete
parity-word enumeration, its absence of duplicates, its cardinality, carry
injectivity at fixed length and grade, the exact semiring recurrence (A2),
initial/zero-grade values, and the unrestricted exact first-moment identity.
[check_aggregate_lean.py](check_aggregate_lean.py) freshly compiles its complete
project dependency closure and a separate eight-root import/type/axiom audit.
The [receipt](../../../reports/astra-collision-factor-bridge-20261128/factoring/aggregate-lean-receipt.json)
records only `Classical.choice`, `Quot.sound`, and `propext`; pinned compiled
Mathlib dependencies were reused. The primary Cartier algorithm, entropy
estimate, matrix representations, complexity bounds, and analytic resolvent
consumer remain written proofs.
