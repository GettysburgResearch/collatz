# Sparse conductor structure and a uniform stationary-seed transfer

Date: 2026-11-28. **Positive finite and analytic reductions; the full
conductor estimate remains open.** This note continues the attempt to make
the factoring repository's common-spectrum and primary coefficient tools
evaluate the joint resolvent in
[JOINT_RESOLVENT_WINDOW.md](JOINT_RESOLVENT_WINDOW.md).

Two useful structures survive the growing conductor. The normalized matrix
has an explicit lacunary determinant, and a full ordinary fibre can be
replaced by a jointly stationary real/ternary seed with a uniform error that
vanishes in the ordinary source cutoff. Neither fact permits discarding the
correlation between the odd grade and the selected endpoint.

## 1. The conductor filtration gives the exact determinant

Let \(Q=3^k\). On functions on \(\mathbb Z/Q\mathbb Z\), the transpose of
the count transition matrix is

\[
(\mathcal T_k(u)f)(r)=f(r/2)+u f((3r+1)/2).
\tag{1}
\]

For \(\chi_m(r)=\exp(2\pi i mr/Q)\),

\[
\mathcal T_k(u)\chi_m
=\chi_{m/2}+u\exp(2\pi i\,\overline{m2^{-1}}/Q)\chi_{3m/2},
\tag{2}
\]

where the divisions by 2 in the subscripts and phase are interpreted modulo
\(Q\). In particular the phase means
\(\exp(2\pi i (m\cdot2^{-1}\bmod Q)/Q)\), not division of a real angle
without its modular correction.

Characters of conductor at most \(3^j\) span an invariant subspace. On the
quotient of exact conductor \(3^j\), \(j\ge1\), the odd term drops to a
lower conductor and the even term permutes the characters by multiplication
by \(2^{-1}\).

The element 2 has order

\[
M_j=2\cdot3^{j-1}\pmod{3^j}.
\tag{3}
\]

For completeness, \(v_3(4^{3^m}-1)=m+1\) follows by binomial induction;
raising to an exponent prime to 3 does not change this valuation. Any
exponent with \(2^n\equiv1\pmod3\) is even, which proves (3). Thus the
nonzero exact-conductor quotient is one cycle of length \(M_j\), and
conductor zero has the eigenvalue \(1+u\). Therefore

\[
\boxed{
\det(I-tC_{k,0}(u))=
\bigl(1-(1+u)t\bigr)\prod_{j=1}^k(1-t^{M_j}).}
\tag{4}
\]

This is an exact polynomial identity, not merely a description of the
locations of possible eigenvalues.

### All retained real polynomial moments

For the integer-cleared moment matrix \(C_{k,d}(u)\) from (N2) of
[AGGREGATE_PROFILE_TRANSFER.md](AGGREGATE_PROFILE_TRANSFER.md), the same
filtration applies. At moment degree \(p\), the even branch has scalar
\(2^{d-p}\); at nonzero conductor every odd branch lowers the conductor.
On conductor zero the moment block is triangular with diagonal
\(2^{d-p}(1+3^pu)\). Consequently

\[
\boxed{
\det(I-tC_{k,d}(u))=
\prod_{p=0}^d
\left[
\bigl(1-2^{d-p}(1+3^pu)t\bigr)
\prod_{j=1}^k\bigl(1-(2^{d-p}t)^{M_j}\bigr)
\right].}
\tag{5}
\]

There are only \((d+1)(k+1)\) lacunary factors, although their total degree
is \((d+1)3^k\). This provides a genuinely sparse common denominator.
Factoring PR 234's primary coefficient engine can consume a supplied
rational function, but a sparse denominator alone does not supply its
target-dependent numerator.

### Uniform spectral gap and its scope

At \(u=1,d=0\), the normalized finite residue chain \(C_{k,0}(1)/2\) has
one eigenvalue 1; every other eigenvalue has modulus \(1/2\). Thus its
spectral-radius gap is \(1/2\), independent of \(k\). Repeated roots at
different conductors and the associated transient constants still matter.
The chain is directed and generally nonnormal; this statement is not an
\(L^2\) operator-norm contraction with uniform point-evaluation constants.

It is also a chain on **finite ternary residues**, not a sampler whose
transitions are certified ordinary integer mergers. It does not contradict
the finite-affine or actual-integer spectral obstructions elsewhere in this
pass.

## 2. An exact rank-one fact, and what it leaves to compute

Every word of grade \(a\) acts on an initial ternary coordinate by

\[
z\longmapsto 3^a2^{-h}z+R(w)\pmod{3^k}.
\tag{6}
\]

If \(a\ge k\), this map is independent of \(z\). Hence the coefficient
of \(u^a\) in \(C_{k,0}(u)^h\) has identical columns and rank at most one.
Its column sum is \(\binom ha\). The rank statement is exact even at
\(a=k\), the full-conductor grade.

This compresses dependence on the initial state. The common output column
still contains the complete endpoint distribution over \(3^k\) residues.
It does not give one requested entry of that column without an additional
representation or evaluation argument.

The same coupling proves the uniform bound

\[
\sup_{z,z'}\left\|
\mathcal L(Z_h\mid Z_0=z)-\mathcal L(Z_h\mid Z_0=z')
\right\|_{\rm TV}
\le\Pr\{\operatorname{Bin}(h,1/2)<k\}.
\tag{7}
\]

Once the common driving word contains \(k\) odd letters, its two ternary
outputs agree. At \(k\) comparable to \(h/2\), (7) is not an estimate at
the tiny mass scale of one full cylinder. The spectral gap in Section 1
cannot silently replace that missing scale.

## 3. The target numerator is a weighted discrete-log trace

Let

\[
G_{k,r}(t,u)=\sum_{h\ge0}t^h
\sum_{|w|=h,\ R(w)\equiv r\ (3^k)}u^{|w|_1}.
\tag{8}
\]

Summing all three preimages of the odd branch is exactly a lower-conductor
marginal. The constant matrix therefore gives the pointwise identity

\[
G_{k,r}=\mathbf1_{r=0}+tG_{k,2r}
+tu\mathbf1_{r\equiv2\ (3)}
G_{k-1,(2r-1)/3}.
\tag{9}
\]

The lower subscript is a residue modulo \(3^{k-1}\). The boundary data are

\[
G_{0,0}=\frac1{1-(1+u)t},\qquad
G_{k,0}=\frac1{1-t};
\quad G_{k,r}=0\text{ for }r\ne0,\ 3\mid r.
\tag{10}
\]

For a unit \(r\), unroll (9) around its complete doubling cycle of length
\(M=2\cdot3^{k-1}\). For each \(s\bmod3^{k-1}\), let \(j_r(s)\) be the
unique integer in \([0,M)\) satisfying

\[
2^{j_r(s)+1}r\equiv3s+1\pmod{3^k}.
\tag{11}
\]

The indices at which the odd term is available traverse all lower residues
exactly once. Thus

\[
\boxed{
G_{k,r}(t,u)=\frac{tu}{1-t^M}
\sum_{s\bmod3^{k-1}}t^{j_r(s)}G_{k-1,s}(t,u).}
\tag{12}
\]

This is a precise candidate for a weighted-lattice or common-spectrum
import. It asks for a **joint weighted trace** of the lower target profile
and a discrete logarithm. Computing either one without their correlation
does not evaluate (12).

### The smooth discrete logarithm is individually easy

Each index in (11) can be computed with polynomially many operations on
\(O(k)\)-bit integers. Given a unit \(v\), its residue modulo 3 determines
the parity \(\epsilon\) of a solution to \(2^n=v\). Write
\(n=\epsilon+2m\) and solve \(4^m=v2^{-\epsilon}\).
Starting modulo 3, lift one base-three digit of \(m\) at a time. If
\(m_j\) is correct modulo \(3^{j+1}\), exactly one of
\(m_j+d3^j\), \(d=0,1,2\), is correct modulo \(3^{j+2}\), because
\(4^{3^j}\equiv1+3^{j+1}\pmod{3^{j+2}}\).

The remaining sum in (12) has \(3^{k-1}\) correlated lower targets. For a
coefficient at clock \(h\), terms with \(j_r(s)+1>h\) can be dropped.
If \(M>h\), the denominator contributes only its constant term. This gives
at most \(h\) lower-target calls at one level; recursively their number
still grows, and no polynomial bound in \(h,k\) follows from (12).

At exact grade \(a=k\), each descent consumes one odd letter. The
remaining object is a collection of ordered gap compositions with a common
total budget. The entropy calculation in the aggregate note is precisely
why replacing this growing ordered family by a fixed number of literal
blocks does not cover the full ordinary population.

The moment analogue of (12) is equally explicit. Put
\(\alpha_p=2^{d-p}t\), and write \(G_{k,r,p}\) for the generating function
of the cleared \(p\)-th moment. For unit \(r\),

\[
G_{k,r,p}=
\frac{u\alpha_p}{1-\alpha_p^M}
\sum_{s\bmod3^{k-1}}\alpha_p^{j_r(s)}
\sum_{j=0}^p\binom pj3^jG_{k-1,s,j}.
\tag{13}
\]

The same selected lower real moments are retained in this formula. It is
not a replacement by independent residue and height marginals.

## 4. Full-conductor cancellation of an arbitrary joint seed

Fix \(h,a,y,X\) as in the resolvent note, with \(y,X\) positive integers,
\(Q=3^a\), \(\Delta=Q/2^h\), and \(L=\Delta X\). Let
\((R_0,Z_0)\) be any random pair in
\([0,\infty)\times\mathbb Z_3\), independent of the subsequent word.
Drive both coordinates with the **same** affine branches

\[
F_0(x)=x/2,\qquad F_1(x)=(3x+1)/2.
\tag{14}
\]

For a fixed word of grade \(a\), its outputs are

\[
R_h=R(w)+\Delta R_0,\qquad
Z_h=R(w)+3^a2^{-h}Z_0.
\tag{15}
\]

Therefore \(Z_h\equiv y\pmod{3^a}\) selects **exactly the same words** as
the zero seed, regardless of \(Z_0\). This is where membership of the
seed's second coordinate in \(\mathbb Z_3\) is used.

Define the seeded count by expectation over the seed:

\[
N^{\rm seed}_{h,a}(y;X)=
\mathbb E\sum_{|w|=h,\,|w|_1=a}
\mathbf1_{Z_h\equiv y\ (Q)}\mathbf1_{0<y-R_h\le L}.
\tag{16}
\]

### Theorem 3: uniform ordinary error for stationary replacement

For every such seed,

\[
\boxed{
|N^{\rm seed}_{h,a}(y;X)-N_{h,a}(y;X)|
\le\mathbb E\min(R_0,X).}
\tag{17}
\]

Consequently, for \(0<q<1\),

\[
\boxed{
\left|\frac{N^{\rm seed}_{h,a}(y;X)}X-
\frac{N_{h,a}(y;X)}X\right|
\le X^{-q}\mathbb E R_0^q.}
\tag{18}
\]

**Proof.** On the full fibre, the distinct ordinary sources
\(n_w=(y-R(w))/\Delta\) are positive integers. For a fixed real seed
\(r\ge0\), the last indicator in (16) becomes
\(r<n_w\le X+r\). Since \(X\) is an integer, this selects the integer
window \(\{\lfloor r\rfloor+1,\ldots,\lfloor r\rfloor+X\}\).
The original window is \(\{1,\ldots,X\}\). If \(\lfloor r\rfloor<X\),
at most \(\lfloor r\rfloor\) points leave and at most that many enter,
so the absolute difference of the two counts is at most
\(\lfloor r\rfloor\), not their sum. In general both windows contain
at most \(X\) selected points. The absolute difference is therefore
at most \(\min(\lfloor r\rfloor,X)\le\min(r,X)\). Average over the
seed, then use \(\min(r,X)\le X^{1-q}r^q\). ∎

There is no extra endpoint error in this theorem, and its constant is
independent of \(h,a,y\). It applies even when the selected ternary cylinder
is extremely small. The integral source lattice is doing the work that a
generic total-variation comparison of rare events would not provide.

## 5. A stationary trace that recovers the exact integer count

The most useful version uses a biased stationary seed. Let
\(0<p<1/2\), and let independent past bits have odd probability \(p\).
The same construction as (24) below gives a joint stationary pair in
\([0,\infty)\times\mathbb Z_3\). Its real mean is finite and exactly

\[
\mathbb E R_{*,p}
=\frac{\mathbb E(b/2)}{1-\mathbb E(3^b/2)}
=\frac{p/2}{1-(1/2+p)}=\frac p{1-2p}.
\tag{19}
\]

This follows directly by summing the expectations of the nonnegative series,
so it does not assume the first moment in order to solve a formal fixed-point
equation. Theorem 3 proves

\[
\boxed{|N^{\rm stat,p}_{h,a}(y;X)-N_{h,a}(y;X)|
\le\frac p{1-2p}.}
\tag{20}
\]

Independently drive the future word with the same bias \(p\), so the endpoint
pair remains stationary. All words of fixed length \(h\) and grade \(a\)
have the same probability \(p^a(1-p)^{h-a}\). Thus, with \(A_h\) the future
grade,

\[
N^{\rm stat,p}_{h,a}(y;X)
=\frac{\Pr_p\{A_h=a,\ Z_h\equiv y\pmod{3^a},
\ 0<y-R_h\le L\}}{p^a(1-p)^{h-a}}.
\tag{21}
\]

### Corollary 4: an exact rounding reduction

For \(p=1/8\), define the joint stationary probability in (21) to be
\(\Pi_{h,a,y,X}\). Then

\[
\left|\frac{8^h}{7^{h-a}}\Pi_{h,a,y,X}-N_{h,a}(y;X)\right|
\le\frac16.
\tag{22}
\]

If an approximation \(\widetilde\Pi\) has absolute error at most

\[
\frac1{12}\frac{7^{h-a}}{8^h},
\tag{23}
\]

the scaled value is within \(1/4\) of the integer count. Its unique nearest
integer is therefore **exactly** \(N_{h,a}(y;X)\). The probability tolerance
requires \(O(h)\) bits of absolute precision, not an exponentially large
number of precision bits. The effort to evaluate the joint probability is
still unbounded by the present argument; rare-event sampling does not become
efficient merely because its requested bit precision is moderate.

The parameters \(0\le a\le h\), \(y,X\ge1\), and the exact
\(L=3^a2^{-h}X\) are retained in this reduction. Outside \(0\le a\le h\)
the ordinary count is zero and no query is needed. This is a reduction to a
**grade-conditioned, full-cylinder, real-window stationary trace**. An
endpoint marginal alone is insufficient.

## 6. The critical fair seed and its quantitative error

Here the standard affine perpetuity can be constructed in both completions
at once. Let \(b_1,b_2,\ldots\) be independent fair bits and put
\(\lambda_b=3^b/2\). The same series

\[
S=\sum_{j\ge1}\frac{b_j}{2}
\prod_{i<j}\lambda_{b_i}
\tag{24}
\]

defines a nonnegative real variable \(R_*\) and a ternary integer
\(Z_*\). In the real completion the products decay exponentially almost
surely, since
\(\mathbb E\log\lambda_b=\tfrac12\log3-\log2<0\).
In the ternary completion the valuations of the nonzero terms tend to
infinity because the number of preceding ones tends to infinity. Splitting
off the first bit proves that the pair is stationary for (14), with the
same bit in both coordinates.

For \(0<q<1\), define

\[
\rho_q=\frac{1+3^q}{2^{q+1}}<1,\qquad
M_q=\frac{2^{-q-1}}{1-\rho_q}.
\tag{25}
\]

Strict concavity applied to the nonconstant positive multiplier of mean one
gives \(\rho_q<1\). Applying \((x+y)^q\le x^q+y^q\) to (24), then
summing the nonnegative expectations, proves
\(\mathbb E R_*^q\le M_q\). Theorem 3 therefore gives the explicit
uniform estimate

\[
\boxed{
\left|\frac{N^{\rm stat}_{h,a}(y;X)}X-
\frac{N_{h,a}(y;X)}X\right|\le M_qX^{-q}.}
\tag{26}
\]

This also gives a uniform logarithmic absolute-count error without importing
an asymptotic tail theorem. Convexity of \(\rho_q\), and its endpoint
values at \(1/2\) and 1, imply

\[
1-\rho_q\ge2(1-\rho_{1/2})(1-q),\qquad
M_q\le\frac{C_0}{1-q},\quad
C_0=\frac{2^{-3/2}}{2(1-\rho_{1/2})}
\quad(1/2\le q<1).
\tag{26a}
\]

For \(X\ge e^2\), choose \(q=1-1/\log X\). Then

\[
\boxed{
|N^{\rm stat}_{h,a}(y;X)-N_{h,a}(y;X)|
\le eC_0\log X.}
\tag{26b}
\]

All constants in (26b) are absolute and independent of the clock, grade,
target, and full conductor. The estimate still leaves the joint stationary
event below to be evaluated; it does not assert that event factorizes.

Stationary real/ternary affine laws are existing objects in
[Weaver 9](https://rstation.ai/problems/collatz/papers/9/v1) and
[Weaver 19](https://rstation.ai/problems/collatz/papers/19/v2). The construction
and bound needed for (26) have been proved explicitly here; no assertion
about a pointwise stationary density is imported.

For independent fair future bits, let \(A_h\) denote their number of ones.
The stationary-seeded count has the exact probability representation

\[
\frac{N^{\rm stat}_{h,a}(y;X)}X
=\frac{2^h}X\Pr\{A_h=a,\ Z_h\equiv y\pmod{3^a},
\ 0<y-R_h\le L\}.
\tag{27}
\]

Although \((R_h,Z_h)\) has the stationary marginal law, the grade \(A_h\)
in this event cannot be dropped or made independent of the endpoint.

### A finite calibration of the remaining correlation

For the fair stationary ternary marginal modulo 3, the masses at
\(0,1,2\) are \(0,1/3,2/3\). This follows directly from (14): mass at
zero is halved, the even branch sends class 2 to 1, and every odd branch
sends its input to 2. If \(b\) is one future bit, then

\[
\Pr(b=1\mid Z_1\equiv2\pmod3)=\frac34\ne\frac12.
\tag{28}
\]

Thus even one ternary digit changes the conditional odd-count law. At the
shrinking full cylinder, an endpoint-only stationary estimate is not the
joint grade estimate required by (27).

### Optional tilt, with its cost retained

The same construction works with bits of bias \(p\) whenever
\(p\log3<\log2\). Choose \(q>0\) small enough that
\(\rho_{p,q}=(1-p)2^{-q}+p(3/2)^q<1\). Then
\(\mathbb E R_{*,p}^q\le p2^{-q}/(1-\rho_{p,q})\), and the error in
(18) is unchanged except for this constant. Formula (27) replaces
\(2^h\) by \(p^{-a}(1-p)^{-(h-a)}\). This allows a central grade to be
matched by a tilt, but preserves its correlation with the full endpoint and
preserves the small-cylinder normalization.

## 7. What this adds to the factoring import

The common-spectrum route now has explicit input, not an analogy:

- the full moment denominator is the sparse product (5);
- its requested target numerator is the weighted discrete-log trace
  (12), or the joint moment version (13);
- the zero-start ordinary window differs by at most (26) from a fair jointly
  stationary grade-and-endpoint observable, and can be recovered **exactly
  by rounding** from a biased stationary trace with the precision (23);
- the complete real selector is already reducible to logarithmically many
  accurately specified full-fibre Cauchy values.

The unproved step is a **uniform joint evaluation or estimate** for these
correlated target traces when the conductor grows with the grade. A smooth
discrete logarithm at one point, a sparse common denominator, rank one in
the initial state, or the stationary endpoint marginal alone does not
establish it. No presently inspected factoring PR provides that step.

The finite interval kernel behind (17) is certified in
[StationaryWindow.lean](StationaryWindow.lean): its three public roots prove
interval splitting, the bound of one selected point per integer, and the
two-sided shift discrepancy at most the smaller of the shift and the window
length. The standalone [check_stationary_lean.py](check_stationary_lean.py)
freshly compiles both project modules, including a separate import/type/axiom
audit, using only Lean core Omega. Its
[receipt](../../../reports/astra-collision-factor-bridge-20261128/factoring/stationary-window-lean-receipt.json)
records only `Classical.choice`, `Quot.sound`, and `propext`.

The aggregate recurrence and carry injectivity are separately covered by the
eight-root aggregate Lean packet. The spectral filtration, discrete-log
trace, probability construction, expectation estimates, and exact rounding
reduction are written proofs; they are not claimed as Lean-certified here.
