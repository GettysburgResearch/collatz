# Full ordinary fibres and a logarithmic resolvent interface

Date: 2026-11-28. Status: proved finite identities and an explicit analytic
reduction, with the remaining full-conductor evaluation problem stated in
Section 8. No Collatz convergence theorem is claimed.

This note strengthens the positive import in
[AGGREGATE_PROFILE_TRANSFER.md](AGGREGATE_PROFILE_TRANSFER.md). The normalized
carry has a constant finite matrix for every fixed ternary conductor and
polynomial moment degree. Here the **entire ordinary real window** is reduced
to a controlled collection of nonreal resolvent values. The number of queries
is logarithmic in the real height ratio; computing those values at the **full
growing ternary conductor** remains the essential unsolved input.

The argument is proved here from elementary finite affine identities, bounded
variation, and a contour computation. It does not assume a window
approximation theorem or an unproved distributional independence statement.

## 1. Exact normalization and the positive full fibre

Use the native map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

For a binary word \(w\) of length \(h\) and odd grade \(a\), put

\[
T_w(n)=\frac{3^a n+A(w)}{2^h},\qquad R(w)=\frac{A(w)}{2^h},
\quad Q=3^a,\quad\Delta=\frac{Q}{2^h}.
\tag{1}
\]

Fix positive integers \(y,X\). The full fibre is

\[
\mathcal F_{h,a}(y)=
\{w:|w|=h,\ |w|_1=a,\ A(w)\equiv2^h y\pmod Q\}.
\tag{2}
\]

### Proposition 1: full-fibre positivity and compactness

Every word in (2) is the actual parity word of the positive integer

\[
n_w=\frac{2^h y-A(w)}{Q}.
\tag{3}
\]

Consequently

\[
0\le R(w)<y,\qquad y-R(w)=\Delta n_w\ge\Delta.
\tag{4}
\]

**Proof.** Congruence (2) first makes (3) an integer, possibly signed. For
\(h>0\), the numerator of a word beginning with \(b\in\{0,1\}\) is congruent
to \(b\) modulo 2. The identity \(Qn_w+A(w)=2^hy\) therefore forces the
first actual parity to be \(b\). The first branch gives an integer, and the
same argument applies to the remaining word. Thus the entire signed integer
orbit really follows the specified word and ends at \(y\). The native map
preserves the nonpositive integers, so an orbit ending at positive \(y\)
must have started at positive \(n_w\). Finally \(A(w)\ge0\). This also
handles \(h=0\), where the unique word gives \(n_w=y\). ∎

The hypothesis is the **full** congruence modulo \(3^a\). A congruence only
modulo \(3^k\), \(k<a\), does not give (3) as an integer and does not justify
this compactness argument.

### Proposition 2: no carry multiplicity at fixed length and grade

Distinct words of the same length and grade have distinct \(A(w)\), and
hence distinct \(R(w)\) and \(n_w\).

**Proof.** The parity of \(A\) determines the first bit. For a leading zero,
\(A=2A'\). For a leading one, \(A=3^{a-1}+2A'\), and the suffix grade is
\(a-1\). In either case the suffix carry and grade are recovered. Induction
recovers the word. If \(a=0\), the all-zero word is the only possibility. ∎

The theorem `Collatz.AggregateProfile.word_determined_by_carry` in
[AggregateProfile.lean](AggregateProfile.lean) checks this finite injectivity
statement. It does not formalize the analytic arguments below.

### The exact ordinary window

Put

\[
L=\Delta X,\qquad B=\frac yL.
\tag{5}
\]

The number of ordinary predecessors with this exact clock and grade is

\[
N_{h,a}(y;X)
=\#\{w\in\mathcal F_{h,a}(y):0<y-R(w)\le L\}.
\tag{6}
\]

**If \(L\ge y\), there is no real cutoff:** (4) gives

\[
N_{h,a}(y;X)=|\mathcal F_{h,a}(y)|.
\tag{7}
\]

The remaining case has \(B>1\). The probability-free finite measure

\[
\mu=\frac1X\sum_{w\in\mathcal F_{h,a}(y)}\delta_{q_w},
\qquad q_w=\frac{y-R(w)}L=\frac{n_w}{X}
\tag{8}
\]

is supported on distinct positive points of the grid \(X^{-1}\mathbb Z\)
inside \((0,B]\). In particular

\[
\mu(\mathbb R)\le B,\qquad
\mu(J)\le |J|+\frac1X
\tag{9}
\]

for every bounded interval \(J\), with either endpoint convention. The
desired answer is exactly \(\mu((0,1])=N_{h,a}(y;X)/X\).

These statements do not assert \(\Delta\asymp X^{-1}\). In a Gaussian
clock/grade window it can have additional factors
\(\exp(O(\sqrt{\log X}))\); outside such a window (5) must simply be
retained exactly.

## 2. A uniform Poisson-window inequality

For a nonnegative integrable function \(f\) of bounded variation and any
subset of a lattice coset of spacing \(d\), the corresponding weighted
counting measure satisfies

\[
d\sum f(x_j)\le\int_{\mathbb R}f(t)\,dt+d\operatorname{Var}(f).
\tag{10}
\]

Indeed compare each lattice value to the integral over its adjacent cell;
the error is at most the cell length times the variation on that cell.
Adding the cells proves (10). A subset only decreases the left side.

Let \(I=[y-L,y)\),
\(P_\eta(t)=\eta/[\pi(t^2+\eta^2)]\), and
\(g_\eta=\mathbf1_I*P_\eta\). Then
\(0\le g_\eta\le1\), \(\operatorname{Var}(g_\eta)\le2\), and

\[
\begin{split}
\|\mathbf1_I-g_\eta\|_1
&=\frac{2\eta}{\pi}\log(1+(L/\eta)^2)
 +\frac{4L}{\pi}\arctan(\eta/L)\\
&\le\frac{4\eta}{\pi}\bigl(1+\log(1+L/\eta)\bigr).
\end{split}
\tag{11}
\]

For the equality, integrate the kernel against the symmetric difference of
an interval and its translate: the result is
\(4\int_0^L tP_\eta(t)dt+4L\int_L^\infty P_\eta(t)dt\).
The inequality uses \(\arctan u\le u\) and
\(1+u^2\le(1+u)^2\).

The function \(|\mathbf1_I-g_\eta|\) has variation at most 4. Apply (10)
to the full-fibre carry lattice with spacing \(\Delta\). For
\(\nu=\Delta\sum_{w\in\mathcal F}\delta_{R(w)}\), this proves

\[
\left|\Delta N_{h,a}(y;X)-\nu(g_\eta)\right|
\le\frac{4\eta}{\pi}\bigl(1+\log(1+L/\eta)\bigr)+4\Delta.
\tag{12}
\]

In particular, for every \(\theta>0\),

\[
\boxed{
\left|\frac{N_{h,a}(y;X)}X-
\frac{\nu(g_{\theta L})}L\right|
\le\frac{4\theta}{\pi}\bigl(1+\log(1+1/\theta)\bigr)+\frac4X.}
\tag{13}
\]

This bound is uniform in \(h,a,y,X\). No limit assumption on \(\Delta\)
is needed in the normalized form (13).

## 3. The precise resolvent consumer

For \(\operatorname{Im}s>0\), define

\[
\mathcal R_{h,a,y,X}(s)
=\int\frac{d\mu(q)}{s-q}
=\sum_{w\in\mathcal F_{h,a}(y)}
\frac{Q}{A(w)-2^hy+QXs}.
\tag{14}
\]

This is a **joint** trace: the ternary selector and the real denominator
belong to the same word. Its imaginary part gives the smoothed window:

\[
\frac{\nu(g_{\theta L})}L
=-\frac1\pi\int_0^1\operatorname{Im}\mathcal R(t+i\theta)\,dt.
\tag{15}
\]

The lattice bound gives

\[
0\le-\operatorname{Im}\mathcal R(t+i\theta)
\le\pi+\frac{2}{X\theta},\qquad
|\mathcal R'(t+i\theta)|
\le\frac\pi\theta+\frac{2}{X\theta^2}.
\tag{16}
\]

For the first inequality apply (10) to the Cauchy kernel, whose integral is
\(\pi\) and variation is \(2/\theta\); the second follows termwise.
Thus midpoint quadrature with \(m\) points in (15) incurs error at most

\[
\frac{1}{4m\theta}+\frac{1}{2\pi mX\theta^2}.
\tag{17}
\]

An absolute error \(\tau\) at every queried resolvent adds at most
\(\tau/\pi\). Equations (13), (15), and (17) already provide an explicit
uniform consumer. The next section improves the query count to logarithmic
dependence on the real height ratio and the requested precision.

## 4. Explicit rational approximation with geometric poles

The following construction uses no unproved rational approximation result.
For \(x\ne0\),

\[
\operatorname{sgn}x
=\frac2\pi\int_0^\infty\frac{x}{x^2+t^2}\,dt
=\frac{\operatorname{sgn}x}{\pi}
\int_{\mathbb R}\operatorname{sech}(s-\log|x|)\,ds.
\tag{18}
\]

For \(b\in(0,1]\), the infinite trapezoidal sum satisfies

\[
\frac b\pi\sum_{j\in\mathbb Z}\operatorname{sech}(jb-s)
=1+2\sum_{m\ge1}
\frac{\cos(2\pi ms/b)}{\cosh(\pi^2m/b)}.
\tag{19}
\]

Here is a proof of the Fourier input. For \(\omega\ge0\), integrate
\(\operatorname{sech}z\,e^{-i\omega z}\) around a rectangle lowered by
\(i\pi\). The vertical integrals tend to zero, the lower horizontal
integral supplies \(e^{-\pi\omega}\) times the upper one, and the one pole
at \(-i\pi/2\) gives

\[
(1+e^{-\pi\omega})
\int_{\mathbb R}\operatorname{sech}t\,e^{-i\omega t}\,dt
=2\pi e^{-\pi\omega/2}.
\]

Thus the transform is \(\pi/\cosh(\pi\omega/2)\); the formula for negative
\(\omega\) follows by symmetry. Periodizing the exponentially decaying
function and computing its Fourier coefficients proves (19). The displayed
Fourier series is absolutely convergent, justifying its evaluation at every
real \(s\).

Set \(t_j=e^{jb}\). It follows that

\[
S_b(x)=\frac{2b}\pi\sum_{j\in\mathbb Z}
\frac{t_jx}{x^2+t_j^2}
\]

satisfies the uniform estimate

\[
|S_b(x)-\operatorname{sgn}x|
\le D(b):=\frac{4e^{-\pi^2/b}}{1-e^{-\pi^2/b}}
\quad(x\ne0).
\tag{20}
\]

All summands have the sign of \(x\). Therefore every finite subsum has
absolute value at most \(1+D(b)\), including near \(x=0\); at zero it
vanishes exactly. This global bound is necessary for controlling removed
boundary strips.

Suppose \(B>1\) and \(0<\varepsilon<1\). Choose

\[
\delta=\frac\varepsilon{48},\quad
\zeta=\frac\varepsilon{4B},\quad
b=\min\left\{1,\frac{\pi^2}{\log(1+16/\zeta)}\right\},
\tag{21}
\]

and integer endpoints

\[
j_- =\left\lfloor\frac{\log(\delta\zeta/8)}b\right\rfloor,
\qquad
j_+ =\left\lceil\frac{\log(8B/\zeta)}b\right\rceil.
\tag{22}
\]

Use the finite rational function

\[
S(x)=\frac{2b}\pi\sum_{j=j_-}^{j_+}
\frac{t_jx}{x^2+t_j^2}.
\tag{23}
\]

For \(\delta\le|x|\le B\), the omitted tails are at most

\[
\frac2\pi\left(\frac{t_{j_-}}\delta+
\frac B{t_{j_+}}\right)\le\frac\zeta{2\pi}.
\tag{24}
\]

For example, the lower tail uses
\(b\sum_{j<j_-}t_j=b\,t_{j_-}/(e^b-1)\le t_{j_-}\);
the upper tail is the same geometric calculation. Also (21) gives
\(D(b)\le\zeta/4\). Hence

\[
|S(x)-\operatorname{sgn}x|\le\zeta
\quad(\delta\le|x|\le B),
\qquad |S(x)|\le1+\zeta/4<2\quad(x\in\mathbb R).
\tag{25}
\]

## 5. The logarithmic-query window theorem

Define

\[
J(q)=\tfrac12\bigl(S(1-q)-S(-q)\bigr).
\tag{26}
\]

Outside \(|q|\le\delta\) and \(|q-1|\le\delta\), this differs from
\(\mathbf1_{(0,1]}(q)\) by at most \(\zeta\) on the entire support
\((0,B]\). The two strips have total \(\mu\)-mass at most
\(4\delta+2/X\), by (9). Everywhere \(|J|<2\), so their contribution to
the approximation error is at most three times that mass. Therefore

\[
\left|\frac{N_{h,a}(y;X)}X-\int J\,d\mu\right|
\le\zeta B+12\delta+\frac6X
=\frac\varepsilon2+\frac6X.
\tag{27}
\]

The integral is a finite combination of the **same full-fibre resolvent**:

\[
\boxed{
\int J\,d\mu
=\frac b\pi\sum_{j=j_-}^{j_+}t_j
\operatorname{Re}\bigl(\mathcal R(1+it_j)-\mathcal R(it_j)\bigr).}
\tag{28}
\]

With \(K=j_+-j_-+1\),

\[
K\le3+\frac{\log(64B/(\delta\zeta^2))}{b}
=O\!\left(\log^2((B+1)/\varepsilon)\right).
\tag{29}
\]

There are exactly \(2K\) resolvent queries. The constants in this estimate
are universal. A pointwise approximation error of order \(\varepsilon\)
alone would have lost a factor \(B\); the choice
\(\zeta=\varepsilon/(4B)\) in (21) is essential.

### Pole, coefficient, and oracle precision

The theorem does not hide exact real arithmetic. Let
\(w_j=bt_j/\pi\), and choose positive rational approximations
\(\widetilde t_j,\widetilde w_j\) satisfying relative error at most

\[
r=\frac\varepsilon{128B(K+1)}.
\tag{30}
\]

At every rounded pole, request an absolute complex resolvent error at most

\[
\tau=\frac{\varepsilon\zeta}{2304B}.
\tag{31}
\]

The elementary mass bounds
\(|\mathcal R(x+it)|\le B/t\) and

\[
|\mathcal R(x+i\widetilde t)-\mathcal R(x+it)|
\le\frac{B|\widetilde t-t|}{t\widetilde t}
\le\frac{2Br}{t}
\tag{32}
\]

show that pole rounding changes (28) by at most
\(4bBKr/\pi\); rounding the weights adds at most the same bound.
Their combined error is at most \(\varepsilon/16\), using (30).

Moreover \(t_{j_+}\le24B/\zeta\) and
\(b\sum_jt_j\le3t_{j_+}\). Since
\(\widetilde w_j\le2w_j\), the two oracle errors per node add at most

\[
4\tau\sum_jw_j
\le\frac{288B\tau}{\pi\zeta}\le\frac\varepsilon8.
\tag{33}
\]

Combining (27), (30)–(33), the rounded finite consumer returns a number
\(\widetilde N\) with

\[
\boxed{\left|\widetilde N-\frac{N_{h,a}(y;X)}X\right|
\le\varepsilon+\frac6X.}
\tag{34}
\]

The rescaled pole heights lie between a constant multiple of
\(\varepsilon^2/B\) and a constant multiple of \(B^2/\varepsilon\).
Relative rounding and absolute oracle precision therefore use polynomially
many bits in \(\log((B+1)/\varepsilon)\), in addition to the exact integer
input parameters. The original carry-coordinate imaginary heights are
\(L\widetilde t_j\); these can be very small and must be supplied as such
to any proposed evaluation algorithm. The proof does not replace them by
constant-height queries.

## 6. What exact pole counts do and do not rule out

Carry injectivity implies that an unrestricted fixed-\((h,a)\) resolvent
has \(\binom ha\) distinct simple poles, each with nonzero coefficient.
Among the \(3^a\) full residue fibres, at least one consequently has at
least \(\binom ha/3^a\) poles. For central grades this lower bound grows
exponentially in \(h\). It may concern a target residue that varies with
\(h,a\); it is **not** a pole-count theorem for one fixed target such as 1.

Thus a universal exact rational representation of bounded denominator
degree is unavailable. This does not rule out approximate evaluation at the
nonreal poles of (28), and does not rule out a compact arithmetic circuit or
a different structured representation. The reduction above deliberately
asks for approximate values instead of exact denominators.

## 7. A formal primary selector, with its precise loss

There is also a useful formal identity, distinct from the real approximation
theorem. Put \(c_w=A(w)-2^hy\), \(Q=3^a\), and let \(Z\) be an
indeterminate. In the field \(\mathbb Q_3(Z)\) with the Gauss valuation,
consider

\[
H_\ell(Z)=\sum_{|w|=h,\,|w|_1=a}
\left(\frac Q{c_w+QZ}\right)^\ell.
\tag{35}
\]

If \(Q\mid c_w\), the summand is \((Z+c_w/Q)^{-\ell}\), a Gauss unit.
If \(v_3(c_w)<a\), it has valuation
\(\ell(a-v_3(c_w))\ge\ell\). Consequently for every \(\ell\ge e\),

\[
H_\ell(Z)\equiv
\sum_{w\in\mathcal F_{h,a}(y)}(Z+c_w/Q)^{-\ell}
\pmod{3^e}
\tag{36}
\]

in the Gauss valuation ring. For \(a=0\) every word is selected and the
identity is exact.

This is a projection only at the stated modular precision. Selected
summands can cancel modulo 3; \(c_w/Q\) is retained only to the available
3-adic precision; and (36) does not reconstruct a real Cauchy transform.
Keeping \(\ell=1\) while increasing \(e\) does not work: terms with
\(v_3(c_w)=a-1\) leak at order 3. Substitution \(Z=Xs\) also needs a fresh
denominator valuation check; formal Gauss integrality is not automatically
preserved by every numerical substitution.

The primary Cartier machinery imported from factoring PR 234 handles a
fixed rational generating representation once it is supplied. It does not
provide an efficient representation of (35) for free: this nonlinear
resolvent observable has many distinct poles. Equation (36) records a
possible interface for a future primary functional calculus, not a completed
full-conductor algorithm.

## 8. The exact remaining proof input

A sufficient computational bridge now has a concrete specification:

1. Supply full-fibre values (14) at the rounded nonreal poles in Section 5,
   with the absolute precision (31), uniformly in the exact input
   \((h,a,y,X)\).
2. Establish the necessary uniform arithmetic estimates on those values,
   including their dependence on the full conductor \(3^a\), the grade,
   the target, and the smallest original height \(L\widetilde t_j\).
3. Feed those estimates into the project’s ordinary collision or canonical
   inverse-profile theorem, with its exact clock window and normalization.

The finite matrix/Cartier import supplies exact low-conductor moments in
time polynomial in \(3^k\), moment degree, numerical primary precision,
and the logarithm of the clock. It does not yet perform step 1 with cost
polynomial in \(a\), nor does counting alone supply step 2. The new result
removes a separate real-window approximation obstacle: **only logarithmically
many accurately specified full-conductor resolvent values are needed**.

The unrestricted carry law has mean \(h/4\) and a critical tail. That is
compatible with the compactness of each positive full integer fibre proved
here. Neither the unrestricted moment growth nor coarse-cylinder moment
control may be substituted for the joint, selected trace in (14).

## 9. Verification scope

- `AggregateProfile.lean` and its separate audit certify eight finite roots,
  including carry injectivity and the exact aggregate recurrence. The fresh
  runner is [check_aggregate_lean.py](check_aggregate_lean.py); its receipt is
  [aggregate-lean-receipt.json](../../../reports/astra-collision-factor-bridge-20261128/factoring/aggregate-lean-receipt.json).
- The independent native-orbit guard
  [check_normalized_matrix.py](check_normalized_matrix.py) checks the general
  constant matrix, full-fibre positivity, realization, spacing, and ordinary
  windows; see
  [normalized-matrix-independent.json](../../../reports/astra-collision-factor-bridge-20261128/factoring/normalized-matrix-independent.json).
- Sections 2–7 are written mathematical proofs, not Lean-certified analytic
  results. No finite check is used as evidence for a uniform Collatz estimate.
