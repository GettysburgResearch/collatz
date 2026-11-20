# Translated interval occupancy and the cost of coefficient records

**Status: PROPOSED, with local proofs and bounded exact replay.** No Collatz
proof, universal coefficient stop, or cycle exclusion is claimed. The core
result is a finite-path theorem. Its application improves the number of
coefficient records that can fit in the existing near-source window; it
does not establish that the next coefficient crossing exists.

Use the shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

All paths below consist of positive **ordinary integers**. A simple path
means that all of its listed states are distinct, including the endpoint.
Counts are of states, without time multiplicity after a repetition.

## 1. An exact finite interval bound

For integers \(X\ge1\), \(k\ge0\), and \(0\le h\le k\), define

\[
\begin{split}
\mathcal B(X;k,h)={}&k+
 \left\lceil\frac X{2^k}\right\rceil
 \sum_{q=h+1}^{k}\binom{k}{q}\\
&+\sum_{q=0}^{h}
 \left\lfloor
 \frac{3^q(X+2^{k-q})-1}{2^k}
 \right\rfloor .                                      \tag{1}
\end{split}
\]

Empty sums are zero. In particular \(\mathcal B(X;0,0)=X\).
The finite computable choice

\[
\widehat{\mathcal B}(X)=
 \min_{0\le k\le\operatorname{bitlength}(X),\ 0\le h\le k}
 \mathcal B(X;k,h)                                      \tag{2}
\]

is therefore always at most \(X\). No logarithm or real-number comparison
is needed to evaluate it.

**FID-DRIFT-001.** If \(x_0,\ldots,x_L\) is a finite simple shortcut path,
then for every integer \(a\ge1\),

\[
\#\{0\le i\le L:a\le x_i<a+X\}
 \le\mathcal B(X;k,h).                                  \tag{3}
\]

The bound is uniform in the location \(a\), the length of the path, its
initial value, and its maximum height.

### Proof

Discard the last \(k\) listed states, or all states if there are fewer than
\(k\). This costs at most \(k\) states. For every remaining state, its
\(k\)-step image is still in the simple path. These images are distinct:
different time indices have different values in a simple path.

A length-\(k\) parity word with \(q\) odd inputs has affine form

\[
T_w(x)=\frac{3^qx}{2^k}+E_w,
\qquad 0\le E_w\le(3/2)^q-1.                            \tag{4}
\]

The upper bound follows by moving each odd letter to the right past an even
letter. The interchange \(10\mapsto01\) increases the affine constant,
since the two maps are \((3x+1)/4\) and \((3x+2)/4\), respectively.
The maximal word is therefore \(0^{k-q}1^q\), whose remainder is exactly
\((3/2)^q-1\). For \(q=0\), the remainder is zero.

Words with more than \(h\) odd inputs occupy exactly
\(\sum_{q>h}\binom{k}{q}\) residue classes modulo \(2^k\), by the elementary
parity-cylinder bijection. Each class supplies at most
\(\lceil X/2^k\rceil\) sources in \([a,a+X)\). This gives the second term
of (1), without any equidistribution assumption.

For a fixed \(q\le h\), (4) puts every corresponding image in the
half-open real interval

\[
\left[
 \frac{3^qa}{2^k},
 \frac{3^q(a+X)}{2^k}+(3/2)^q-1
\right).
\]

An interval of width \(D\) contains at most \(\lceil D\rceil\) integers.
Here that integer is exactly

\[
\left\lceil \frac{3^qX}{2^k}+\frac{3^q}{2^q}-1\right\rceil
=\left\lfloor\frac{3^q(X+2^{k-q})-1}{2^k}\right\rfloor . \tag{5}
\]

Images are distinct, so this bounds the number of retained path states
with that odd count. Summing over \(q\le h\), then restoring the discarded
terminal states, proves (3). The image intervals need not be disjoint;
summing their separate bounds is an upper bound. \(\square\)

The terminal term \(k\) is essential to this proof: finite paths do not
provide \(k\)-step internal images for their last \(k\) states. This is
not a theorem about all starting integers in a predecessor basin.

## 2. A power bound, with no logarithmic loss

Let \(H_2(t)=-t\log_2t-(1-t)\log_2(1-t)\), and choose
\(1/2<\theta<\log_3 2\). Put

\[
\beta(\theta)=\max\{H_2(\theta),\theta\log_2 3\}<1.
\]

**FID-DRIFT-002.** Every finite simple shortcut path satisfies

\[
\boxed{\#\{i:a\le x_i<a+X\}\le10X^{\beta(\theta)}}.       \tag{6}
\]

In particular, the completely rational exponent

\[
\boxed{\#\{i:a\le x_i<a+X\}\le10X^{29/30}}               \tag{7}
\]

is valid. The result is a translated-interval version of the orbit-sparsity
mechanism of Garcia--Tal, with an explicit finite terminal correction. No
claim of priority for orbit sparsity, or for an optimal exponent, is made.

### Proof

Take \(k=\lfloor\log_2X\rfloor\), \(h=\lfloor\theta k\rfloor\), and
\(z=\theta/(1-\theta)>1\). Because \(q>h\) implies \(q>\theta k\),

\[
\sum_{q>h}\binom{k}{q}
 \le z^{-\theta k}(1+z)^k
 =2^{H_2(\theta)k}.
\]

Also \(\lceil X/2^k\rceil\le2\). The high-odd-count contribution is
therefore at most \(2X^\beta\). In (5), replace the ceiling by the width
plus one and sum the resulting geometric series. Since \(X/2^k<2\),
the low-odd-count contribution is at most

\[
3\cdot3^h+3\cdot(3/2)^h\le6X^{\theta\log_2 3}
\le6X^\beta.
\]

Finally \(k\le2\sqrt X\le2X^\beta\). This proves (6). The geometric sum,
rather than a bound of each summand by the largest one times \(k+1\),
avoids an additional factor of \(\log X\).

For (7), take \(\theta=39/64\). Both required strict comparisons are
certified by the finite integer inequalities

\[
3^{1170}<2^{1856},\qquad
2^{9664}<39^{1170}25^{750}.                              \tag{8}
\]

They are respectively equivalent to
\(\theta\log_2 3<29/30\) and \(H_2(\theta)<29/30\).
The replay evaluates (8) using integers. \(\square\)

Within this parameter family, the two exponents meet at approximately
\(\theta=0.6090897679\), \(\beta=0.9653844417\). These decimal values
are explanatory; no proof or check uses them.

## 3. Coefficient records consume a superlinear correction budget

For a finite simple path beginning at \(n=x_0\), put

\[
C_i=3^{q_i}/2^i,\quad
P_i=\prod_{0\le j<i,\ x_j\text{ odd}}
 \left(1+\frac1{3x_j}\right),\quad x_i=nC_iP_i.
\]

Time zero is a coefficient record. A later time is a record if its
coefficient is strictly smaller than every earlier coefficient. Let \(r\)
be the number of records, including zero, and assume that every path state
is at least \(n\).

**FID-DRIFT-003.** Define the exact rational budget and integer width

\[
V=n(P_L-1),\qquad W=\lfloor V\rfloor+1.
\]

Then

\[
r\le\widehat{\mathcal B}(W)\le10W^{29/30},              \tag{9}
\]

and hence

\[
\boxed{n(P_L-1)\ge(r/10)^{30/29}-1.}                    \tag{10}
\]

### Proof

At every record, \(C_i\le1\) and \(P_i\le P_L\), so its ordinary value
is an integer in \([n,n+V]\), equivalently in \([n,n+W)\). Apply
(3), minimize to obtain (2), and apply (7). Since \(W\le V+1\),
rearrangement gives (10). \(\square\)

The exponent \(30/29>1\) is the gain over charging one unit of interval
width per distinct record. With the symbolic exponent of (6), the exponent
is \(1/\beta(\theta)\). For a general simple path with minimum \(m\le n\),
the same proof uses \(W=\lfloor nP_L\rfloor-m+1\); this version is also
replayed on paths with many coefficient records.

The claim does not assert that multiple records actually occur before
the first ordinary descent. That assertion would touch the separate
coefficient-stopping-time conjecture. The theorem is an implication for
every finite path satisfying its stated hypotheses.

## 4. An improved finite stopping-or-repetition clock

Suppose an integer \(W_n\ge1\) has been proved to contain every coefficient
record source of every finite simple path from \(n\) staying at least
\(n\), in the interval \([n,n+W_n)\). Suppose also that a finite certificate
proves coefficient stopping within \(N\ge1\) shortcut steps for **every**
integer in that interval. Put

\[
K_n=\widehat{\mathcal B}(W_n).
\]

**FID-DRIFT-004.** By time \(K_nN\), the actual orbit from \(n\) either
goes below \(n\) or repeats a state.

Indeed, otherwise the first \(K_nN+1\) states form a simple no-descent
path. From each coefficient record, its certified relative coefficient
crossing supplies the next strict global record within \(N\) steps. This
constructs \(K_n+1\) records, whereas (3) allows at most \(K_n\) in the
same interval. The contradiction proves the claim.

This replaces the factor \(W_n\) in the existing finite record clock by
the generally smaller exact number \(\widehat{\mathcal B}(W_n)\). It uses
the **same** finite all-source stopping premise; it does not prove it.
Repetition remains a separate alternative and is not called convergence.

### Explicit source-dependent comparison

The resident finite-path estimate
[T-A3-651--653](../astra-three-routes/pass3/FINITE_RECORDS.md), at main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, gives

\[
P_L\le\exp\left(\frac{200}{3}n^{-1/40}\right)
\]

for simple no-descent paths from \(n\). For \(n\ge67^{40}\), an integer
window is therefore

\[
W_n=134\left\lceil n^{39/40}\right\rceil+1.              \tag{11}
\]

Here the ceiling is computed by an integer fortieth root of \(n^{39}\).
The inequality \(e^u-1\le2u\) for \(0\le u\le1\) proves (11).
Since \(n^{39/40}\ge135\) at this threshold, \(W_n\le135n^{39/40}\).
Consequently

\[
K_n\le10\,135^{29/30}n^{377/400}
\le1350n^{377/400}.                                     \tag{12}
\]

The exact formula (2) is normally more useful than the coarse constant in
(12). The threshold is enormous and is not described as a practical
verification range. The exponent improves the old trivial record count
\(O(n^{39/40})\) to \(O(n^{377/400})\).

The same resident source provides a non-explicit window of width
\(O(n^{19/20})\). Using that qualified input gives
\(K_n=O(n^{551/600})\). Allowing the optimized parameter in (6) gives
approximately \(O(n^{0.9171153})\). These are refinements of a **conditional
finite clock**, not global Collatz stopping-time bounds.

## 5. Recursive interval compression improves the exponent

The low-odd-count images in the proof of (3) are themselves states of the
same simple path. They can therefore be bounded by a smaller-interval
occupancy theorem, rather than by the number of all integers in their
interval. This is a second use of injectivity on an actual path; it does
not assume a comparable bound for its predecessor basin.

For \(0\le q\le k\), put

\[
L_q(X,k)=
\left\lfloor\frac{3^q(X+2^{k-q})-1}{2^k}\right\rfloor.
\]

These lengths are positive and nondecreasing in \(q\). Define an integer
function recursively, beginning with \(F(1)=1\):

\[
\begin{split}
F(X)=\min\Bigg(&X,\\
&\min_{\substack{0\le k\le\operatorname{bitlength}(X),\ 0\le h\le k\\
                  L_h(X,k)<X}}
\left[k+\left\lceil\frac X{2^k}\right\rceil
 \sum_{q=h+1}^k\binom{k}{q}
 +\sum_{q=0}^{h}F(L_q(X,k))\right]\Bigg).                \tag{13}
\end{split}
\]

If the inner menu is empty, the result is \(X\). Every recursive argument
is smaller than \(X\), so (13) is a terminating, finite integer procedure.
No cost or practical efficiency is asserted for exhaustive minimization.
A restricted menu is also a valid upper envelope, provided the fallback
\(X\) and the same strict smaller-width guard are retained; its numerical
values must not be labeled as the full minimum (13).

**FID-DRIFT-005.** Every finite simple shortcut path satisfies

\[
\#\{i:a\le x_i<a+X\}\le F(X)\le\widehat{\mathcal B}(X).
                                                               \tag{14}
\]

Moreover, for each

\[
H_2(\log_3 2)<\alpha<1,
\]

there is a finite constant \(C_\alpha\), independent of the path and
interval location, such that

\[
\boxed{F(X)\le C_\alpha X^\alpha.}                       \tag{15}
\]

For rational parameters with a specified strict margin the constant is
effective. In particular \(\alpha=19/20\) is valid. Its constant is not
numerically evaluated here, and the small strict margins must not be
represented as a practical cutoff.

### Proof of the recursive bound

Proceed by strong induction on integer \(X\). The trivial bound \(X\)
uses distinct positive integer values. Choose any menu entry in (13),
discard the final \(k\) states, and split by odd count exactly as in the
proof of (3). High-count sources have the same cylinder bound.

For a low count \(q\), the real image interval \([A,B)\) in that proof
has \(\lceil B-A\rceil=L_q(X,k)\). Its integer points are contained in
the integer interval

\[
[\lceil A\rceil,\ \lceil A\rceil+L_q(X,k)).
\]

Indeed \(\lceil B\rceil-\lceil A\rceil\le\lceil B-A\rceil\).
Thus no additional alignment unit is needed. Its lower endpoint is at
least one. All its images are distinct states of the same finite path,
and \(L_q\le L_h<X\). Apply the induction hypothesis to obtain the term
\(F(L_q)\). This proves every menu bound and hence (14)'s first inequality.

For the second inequality, a menu giving \(\mathcal B(X;k,h)<X\) must
have \(L_h<X\), since that length is already one of its nonnegative
summands. It is therefore eligible in (13); using \(F(L_q)\le L_q\)
gives its recursive bound no larger than its bound in (1). If no menu
beats \(X\), the fallback suffices. This proves \(F\le\widehat{\mathcal B}\).

### Proof of the power bound, including the induction constant

Choose \(1/2<\theta<\log_3 2\) close enough to \(\log_3 2\) that

\[
H=H_2(\theta)<\alpha,\qquad u=\theta\log_2 3<1.
\]

Set \(k=\lfloor\log_2X\rfloor\), \(h=\lfloor\theta k\rfloor\).
The earlier binomial estimate gives a high-count contribution at most
\(2X^H\). Also

\[
1\le L_q(X,k)\le3\cdot3^q,
\qquad L_h(X,k)\le3X^u.
\]

Let

\[
D_\alpha=\frac{3^\alpha}{1-3^{-\alpha}}.
\]

Choose an integer \(X_0\ge2\) so large that, for every \(X\ge X_0\),

\[
3X^u<X,\qquad D_\alpha X^{-\alpha(1-u)}\le\frac12.
                                                               \tag{16}
\]

Both are eventual inequalities between fixed positive powers; a finite
\(X_0\) exists and is effective for explicit parameters. Choose

\[
C_\alpha\ge\max\{8,X_0^{1-\alpha}\}.
\]

For \(X<X_0\), \(F(X)\le X\le C_\alpha X^\alpha\). For larger \(X\),
the selected menu is eligible by (16). Its low-count contribution, using
the strong induction hypothesis, is at most

\[
\begin{split}
\sum_{q=0}^{h}C_\alpha L_q^\alpha
&\le C_\alpha3^\alpha\sum_{q=0}^{h}3^{\alpha q}\\
&\le C_\alpha D_\alpha X^{\alpha u}
\le\tfrac12 C_\alpha X^\alpha.
\end{split}
\]

For the remaining contribution, \(k\le2\sqrt X\) and \(H>1/2\), so

\[
k+2X^H\le4X^H\le4X^\alpha
\le\tfrac12 C_\alpha X^\alpha.
\]

The two halves close the induction, proving (15). In this range
\(H>1/2\) follows, for example, from
\(\theta<\log_3 2<2/3\) and the monotonicity of binary entropy on
\([1/2,1]\). \(\square\)

For the advertised rational exponent, choose \(\theta=200/317\). The
two exact inequalities

\[
3^{200}<2^{317},\qquad
317^{6340}<2^{6023}200^{4000}117^{2340}                    \tag{17}
\]

give \(u<1\) and \(H_2(\theta)<19/20\), respectively. These are the same
elementary comparisons used in the resident origin-centered occupancy
argument; the translated recursive proof above retains the terminal
boundary and image-interval alignment explicitly.

### Consequences for the record mechanism

Equations (9)--(10) strengthen to

\[
r\le F(W)\le C_\alpha W^\alpha,
\qquad n(P_L-1)\ge(r/C_\alpha)^{1/\alpha}-1.
\]

The clock in FID-DRIFT-004 can use \(K_n=F(W_n)\), with exactly the same
all-source stopping premise. With \(\alpha=19/20\), the explicit
source-window exponent \(39/40\) from (11) yields

\[
K_n=O(n^{741/800}),
\]

and the qualified \(O(n^{19/20})\) window yields

\[
K_n=O(n^{361/400}).                                     \tag{18}
\]

The constants in these two comparisons have not been evaluated. The
one-pass estimate (12) retains its explicit coefficient and remains
useful when a fully displayed constant is desired. Neither recursive
compression nor (18) supplies the missing coefficient stop or turns the
record clock into an unconditional Collatz running-time bound.

The separate
[recursive-envelope replay](../../experiments/fixed_integer_interval_bootstrap.py)
computes the full recurrence (13) through width 4096, where
\(F(4096)=2565\), compared with the one-pass value 2720. A separate,
explicitly restricted depth-three policy gives valid bounds 55681 at
width 100000 and 2841764210 at width \(10^{10}\). The latter values are
not asserted to be the full minima of (13).

Its [frozen report](../../reports/2026-11-20-fixed-integer-descent/interval-bootstrap-report.json)
records 195322 recurrence comparisons, 6720 integer-envelope checks,
and 55296 translated-window checks on 2048 literal simple paths.
Reproduce without overwriting that evidence:

```bash
python -X utf8 -B experiments/fixed_integer_interval_bootstrap.py --compare reports/2026-11-20-fixed-integer-descent/interval-bootstrap-report.json
```

## 6. Exact replay and boundaries

Run from the repository root:

```bash
python -X utf8 -B experiments/fixed_integer_drift.py --compare reports/2026-11-20-fixed-integer-descent/drift-report.json
```

The standard-library program reconstructs every parity cylinder through
length twelve, checks the sharp remainder by literal stepping, compares
image-set counts for translated integer intervals, checks window occupancy
on complete simple paths through source 4096, and checks exact coefficient
records and products on a separate prefix corpus. It rejects a repeated
cycle counted with multiplicity, a wrong parity residue, an omitted affine
correction, and a zero-width record-window mutation. It does not instantiate
the enormous universal window (11) or the all-source premise of Section 4.

For example, minimizing (1) gives these exact finite upper bounds:

| Interval width \(X\) | \(\widehat{\mathcal B}(X)\) | A minimizing \((k,h)\) |
|---:|---:|---:|
| 128 | 117 | (7, 3) |
| 4096 | 2720 | (12, 6) |
| 100000 | 63875 | (17, 9) |
| 10000000000 | 3442132111 | (31, 17) |

The analytic statements are proved above; these finite replays do not
establish any missing infinite ordinary-source assertion.

## 7. Sources and exact scope of reuse

- M. V. P. Garcia and F. A. Tal, *A note on the generalized 3n+1 problem*,
  Acta Arithmetica **90** (1999), 245--250,
  [DOI](https://doi.org/10.4064/aa-90-3-245-250),
  [publisher-hosted PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf),
  [author publication page](https://users.ime.usp.br/~mane/collatz.html).
  Their orbit-sparsity mechanism is credited; Sections 1--3 here have
  complete local proofs and do not import an uninspected constant.
- Resident [finite simple-path and coefficient-record packet](../astra-three-routes/pass3/FINITE_RECORDS.md),
  main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, claims T-A3-651--653.
  Only the explicit reciprocal budget and its stated non-explicit
  refinement are used for (11)--(12) and the subsequent comparison.

The unclosed task is still to prove a coefficient stop for each required
fixed ordinary source, or to give a different complete descent mechanism.
Making a finite record budget smaller does not establish block totality.
