# A uniform obstruction to periodic approximation of an ordinary component

## Status and result

**PROPOSED, source-qualified written theorem. No new Lean verification is
claimed for this note.** The predecessor-population input is the earlier
logarithmic PR180 argument audited in [PREDECESSOR_POPULATION_AUDIT.md](PREDECESSOR_POPULATION_AUDIT.md),
including that audit's separate LOG check. The later joint-clock and
positive-natural-density claim is not needed for this theorem.
Tao's fine-scale mixing is an external analytic theorem. The measure and
mixing argument below is proved here, with the ordinary source retained
through each limiting operation.

Let `T` be the ordinary shortcut Collatz map and let
`f : N_(>0) -> {0,1}` satisfy `f(Tn)=f(n)`. Suppose `f` is nonconstant.
Then there is an `epsilon_f>0` such that **every** periodic function
`p : N_(>0) -> [0,1]` with period `2^a 3^b`, for any nonnegative
integers `a,b`, satisfies

\[
 \boxed{
 \liminf_{X\to\infty}\frac1{H_X}
    \sum_{1\le n\le X}\frac{|f(n)-p(n)|}{n}
 \ge\epsilon_f>0,
 }
 \qquad H_X=\sum_{1\le n\le X}\frac1n.
 \tag{PLR}
\]

In particular, a nonconstant invariant Boolean label cannot be approximated
arbitrarily accurately in logarithmic mean by such periodic functions.
The positive error bound is independent of the period and of the
approximating function. It also implies

\[
 \limsup_{X\to\infty}\frac1X
     \sum_{1\le n\le X}|f(n)-p(n)|\ge\epsilon_f.
 \tag{PLR-N}
\]

This strengthens the *sufficient regularity premise* in PR168: qualitative
periodic approximation in mean would already force constancy; no
stretched-exponential approximation rate is needed. It does not construct
such approximations for an arbitrary ordinary component. Their existence
is not a consequence of density of cylinder functions in a compact
probability space. The label on the ordinary integers has not been assumed
to descend to that space.

The proof also identifies a stronger intermediate statement. Every
subsequential stationary-weighted logarithmic distribution of the actual
sources in an invariant component is a scalar multiple of one fixed
mixing probability measure. The proof does **not** turn that scalar
into zero or one.

## 1. Exact inputs and notation

Put `H_2=Haar(Z_2)`, `H_3=Haar(Z_3)`, each normalized to have mass one,
and let

\[
 \Omega=\mathbb Z_2\times\mathbb Z_3,
 \qquad \iota(n)=(n,n).
\]

For independent positive geometric letters with `Pr(a=e)=2^(-e)`, the
ternary random series

\[
 X_\infty=\sum_{i\ge1}3^{i-1}2^{-(a_1+\cdots+a_i)}
\]

converges in `Z_3`; denote its probability law by `nu`. Its projection
modulo `3^m` depends only on its first `m` letters. Let

\[
 g_m(z)=3^m\Pr(X_\infty\equiv z\pmod {3^m}),
 \qquad g_0=1.
\]

Each `g_m` is a finite nonnegative periodic function, of Haar integral
one. These are the finite densities in PR168, not evaluations of an
unspecified almost-everywhere representative on ordinary integers.

The needed source inputs are exactly:

1. **Stationarity and its finite recurrence.** The law `nu` is stationary
   for the two equally likely maps `F_0(z)=z/2` and `F_1(z)=(3z+1)/2`.
   Its finite densities satisfy

   \[
   g_m(z)=\tfrac12g_m(2z)+
      \tfrac32\mathbf1_{z\equiv2\ (3)}
       g_{m-1}((2z-1)/3).
   \tag{1}
   \]

   This is PR168 TM4, and follows directly by expanding the stationary
   geometric recursion. In particular the second term uses `g_(m-1)`.

2. **An `L^1` density limit.** Tao's Proposition 1.14 and consistency give

   \[
   \|g_n-g_m\|_{L^1(H_3)}\le C_A m^{-A}\quad(n\ge m\ge1).
   \tag{2}
   \]

   Hence `g_m -> g` in `L^1(H_3)` for a nonnegative density `g`, and
   `nu=g H_3`. Only convergence, not its rate, is used below.

3. **A uniform floor on the correct subfamily.** The audited selected-word
   proof in PR180 gives `c_*>0` such that

   \[
   g_m(n)\ge c_*\quad(m\ge1,\ 3\nmid n).
   \tag{3}
   \]

4. **Positive ordinary logarithmic predecessor mass.** The earlier
   marginal atom-floor argument, Section 6, (LOG), gives `c_log>0`
   such that every positive ternary-unit target `q` satisfies

   \[
   \liminf_{X\to\infty}\frac1{H_X}
      \sum_{n\le X,\ n\to q}\frac1n\ge c_{\log}/q.
   \tag{4}
   \]

   This follows from the marginal floor alone: cut the total valuation
   at `6s`, whose discarded normalized mass is at most `(64/81)^s`,
   and add the disjoint inverse depths of a small nonperiodic unit
   parent. The companion audit reconstructs this argument separately.
   Section 5 below converts (4) to unit odd source mass using elementary
   ordinary maps; no joint-clock local limit is required.

The conversion to unit sources is essential to intersect (4) with the
floor (3). Positive ordinary mass alone, or positivity of a density at
just one residue, would not suffice.

Set `mu_m=H_2 x (g_m H_3)` and `mu=H_2 x nu`. Then `mu_m -> mu` in
total variation by (2). Throughout, the total-variation norm of a signed
measure is `sup_(|h|<=1) |integral h|`; for densities it is the full
`L^1` norm. This fixes the factors below.

## 2. The compact system is mixing

Define the continuous map `S : Omega -> Omega` by

\[
 S(x,z)=
 \begin{cases}
 (x/2,z/2),&x\in2\mathbb Z_2,\\
 ((3x+1)/2,(3z+1)/2),&x\in1+2\mathbb Z_2.
 \end{cases}
 \tag{5}
\]

It agrees exactly with the ordinary shortcut map on every positive
integer: `S(iota(n))=iota(Tn)`.

Under `H_2`, the first `r` shortcut parity symbols are independent fair
bits. Moreover, after prescribing those bits, the remaining two-adic
state has Haar distribution independent of them. Here is the finite
arithmetic reason, avoiding an imported symbolic-conjugacy theorem.
Given a next two-adic state `y`, the inverse with prescribed even
symbol is `2y`, while the inverse with prescribed odd symbol is
`(2y-1)/3`. Both have the required parity. Repeating these inverses
identifies each length-`r` parity word with exactly one residue modulo
`2^r`, and gives a Haar-preserving affine parametrization of the
remaining state in that residue after its factor `2^(-r)` is accounted
for. The same argument at modulus `2^(r+s)` proves independence from
any fixed finite number of later binary digits.

Because the two-adic next state is Haar and independent of the current
symbol, stationarity of `nu` under `F_0,F_1` proves that `S` preserves
`mu`.

For mixing, consider two bounded cylinder functions, the first depending
on finitely many initial binary and ternary digits. Let `r` cover its
binary digits. For `N>r`, the symbols at times `r,...,N-1` are fresh
fair bits independent of that initial cylinder. Couple the ternary state
at time `r` to an independent state of law `nu`, using those same
future symbols. The difference of the two ternary states is multiplied
by `1/2` at an even symbol and by `3/2` at an odd symbol. Therefore their
states at time `N` agree modulo `3^s` whenever this suffix contains at
least `s` odd symbols. The probability of failure is at most

\[
 \Pr(\operatorname{Bin}(N-r,1/2)<s)\longrightarrow0.
 \tag{6}
\]

The terminal two-adic digits are independent of the entire preceding
parity block and initial ternary state, by the finite inverse argument.
Thus (6) makes the expectation of a second fixed cylinder function at
time `N`, conditional on the first cylinder, approach its `mu` mean.
This proves mixing for bounded cylinder functions. Cylinder functions
are dense in `L^2(mu)`; invariance and Cauchy--Schwarz extend mixing to
all `L^2(mu)` functions.

One consequence used below is particularly simple:

\[
 0\le\lambda\le\mu,\quad S_*\lambda=\lambda
 \quad\Longrightarrow\quad \lambda=\lambda(\Omega)\mu.
 \tag{7}
\]

Indeed write `lambda=h mu` with `0<=h<=1`. For a bounded continuous
`p`, invariance and mixing give
`integral p d lambda = integral h(p o S^N)d mu -> integral h d mu *
integral p d mu`. This proves (7) even though `S` is not invertible.

## 3. Build measures from the actual ordinary sources

Fix any sequence of positive integer cutoffs tending to infinity. For
each `m>=1`, form the finite empirical measure

\[
 \lambda_{m,X}^{f}=
 \frac1{H_X}\sum_{1\le n\le X}\frac{g_m(n)f(n)}n\,
                           \delta_{\iota(n)}.
 \tag{8}
\]

All evaluations in (8) are of finite periodic `g_m`. **The function `g`
is never evaluated at an ordinary integer.**

Ordinary logarithmic averages of any periodic function of period
`2^a3^b` converge to its uniform residue average, by counting each
residue class and partial summation. Consequently the same measures
without `f` converge weakly to `mu_m`. Compactness and a diagonal
subsequence supply weak limits `lambda_m^f` simultaneously for every
positive `m`. They satisfy `0<=lambda_m^f<=mu_m`.

These limits are coherent in total variation. For every continuous
`h` with `|h|<=1`,

\[
 \left|\int h\,d(\lambda_m^f-\lambda_l^f)\right|
 \le\lim_{X}\frac1{H_X}
      \sum_{n\le X}\frac{|g_m(n)-g_l(n)|}{n}
 =\|g_m-g_l\|_1.
 \tag{9}
\]

The limit is along the chosen common subsequence; the final periodic
average has an ordinary limit along all cutoffs. Taking the supremum
over continuous tests gives the total-variation norm on this compact
space. Thus `lambda_m^f` is Cauchy in total variation and has a limit
`lambda^f` with

\[
 0\le\lambda^f\le\mu,
 \qquad
 \|\lambda_m^f-\lambda^f\|_{\rm TV}\le\|g_m-g\|_1.
 \tag{10}
\]

This step uses domination of the same original label by one, not a
claim that its residues are already equidistributed.

## 4. Actual branch changes make the limit invariant

Let `p` be bounded and continuous on `Omega`. In the empirical sum for
`p o S`, change variables along the even sources `n=2q` and the odd
sources `n=(2q-1)/3`. The latter are exactly the positive integers
`q=2 mod3`. Ordinary invariance supplies `f(n)=f(q)` on both branches.
Changing the resulting cutoff by a fixed factor contributes `o(1)`
after division by `H_X`. Replacing `1/n=3/(2q-1)` on the odd branch
by `3/(2q)` contributes `o(1)` as well, since its error has a summable
`O(q^(-2))` majorant for fixed `m` and `p`.

It follows that

\[
 \int(p\circ S-p)\,d\lambda_m^f
 =\lim_X\frac1{H_X}\sum_{q\le X}
        \frac{f(q)p(\iota(q))}{q}\,e_m(q),
 \tag{11}
\]

where

\[
 e_m(q)=\tfrac12g_m(2q)+
     \tfrac32\mathbf1_{q\equiv2\ (3)}g_m((2q-1)/3)-g_m(q).
\]

The exact stationary recurrence (1) gives

\[
 e_m(q)=\tfrac32\mathbf1_{q\equiv2\ (3)}
                  (g_m-g_{m-1})((2q-1)/3).
\]

The indicated ternary coset has Haar measure `1/3`, and its affine
coordinate `(2q-1)/3` is Haar distributed on `Z_3`. Therefore

\[
 \left|\int(p\circ S-p)\,d\lambda_m^f\right|
 \le\frac{\|p\|_\infty}{2}\|g_m-g_{m-1}\|_1
 \longrightarrow0.
 \tag{12}
\]

Passing to the total-variation limit in (12) proves
`S_*lambda^f=lambda^f`. By (7),

\[
                 \lambda^f=\delta\mu,
                 \qquad0\le\delta\le1.
 \tag{13}
\]

This is the stationary-weighted projection theorem for an ordinary
invariant Boolean label. The scalar `delta` may depend on the chosen
cutoff subsequence. No existence of an ordinary component density has
been assumed or concluded.

## 5. A separating pair keeps both scalar masses positive

Because `f` is nonconstant, choose positive odd ternary units `a,b`
with `f(a)=1` and `f(b)=0`. Such units exist in both classes: strip
powers of two from any positive input, then take an odd accelerated
step if its odd part is divisible by three. These operations are
actual ordinary iterates and preserve the label.

For an odd target `q`, removing the initial powers of two from any
ordinary predecessor leaves an odd predecessor. The sum of the reciprocal
weights of all doublings of one odd source is at most twice its reciprocal
weight. Thus (4) gives lower logarithmic density at least
`c_log/(2q)` for odd predecessors.

For an odd predecessor `n` of the unit target `q`, set `F(n)=n` when
`3` does not divide `n`, and `F(n)=4n+1` otherwise. In the second case
`n` is not the target, so its hitting path has a positive first clock.
The exact identity `T^3(4n+1)=T(n)` proves that `F(n)` is still a
predecessor of `q`. The output is a positive odd unit, satisfies
`F(n)<=5n`, and has at most two preimages under `F`. Consequently

\[
 \sum_{\substack{m\le5X\\m\text{ odd},\ 3\nmid m,\ m\to q}}\frac1m
 \ge\frac1{10}
        \sum_{\substack{n\le X\\n\text{ odd},\ n\to q}}\frac1n.
\]

Since `H_(5X)/H_X -> 1`, the unit odd predecessor set has lower
logarithmic density at least `c_log/(20q)`. This explicit loss uses
the displayed all-source LOG statement; the stronger odd-source form
implicit in its proof would improve the harmless constant.

Every unit predecessor of `a` has label one. Combining this bound with
(3) gives for every `m>=1`

\[
 \lambda_m^f(\Omega)\ge c_*c_{\log}/(20a).
\]

Apply the same argument to `1-f` and `b`. Along the same subsequence,
`lambda_m^(1-f)=mu_m-lambda_m^f`, so the two bounds survive (10).
In particular, with

\[
 \eta=\min\{1/4,c_*c_{\log}/(20a),c_*c_{\log}/(20b)\}>0,
 \qquad \eta\le\delta\le1-\eta.
 \tag{14}
\]

The constant `eta` is independent of every subsequence and every
periodic approximation. This is where both the population and the
floor on **unit** sources are needed. Haar full support alone would
not imply (14).

## 6. Remove the conductor-dependent approximation loss

Let `p` be any periodic function of period `2^a3^b` taking values in
`[0,1]`. Regard it as a continuous cylinder function on `Omega`.
Since `f` is Boolean,

\[
 |f-p|=f(1-p)+(1-f)p.
\]

Along the common subsequence used above, let `L_m(p)` be the limit of
the empirical mean in (8) with `f` replaced by `|f-p|`. Such a limit
exists because it is a linear combination of the already convergent
`lambda_m^f` and `mu_m`. Equations (10) and (13) give

\[
 \begin{aligned}
 L_\infty(p)
 &=\delta\int(1-p)\,d\mu+(1-\delta)\int p\,d\mu\\
 &\ge\min(\delta,1-\delta)\ge\eta.
 \end{aligned}
 \tag{15}
\]

There is a useful exact uniform error bound here. At every finite
cutoff, `0<=|f-p|<=1`; hence the difference between the means using
`g_m` and `g_l` is at most the ordinary logarithmic mean of
`|g_m-g_l|`. Passing first to the common cutoff limit and then to
`l -> infinity` proves

\[
                  |L_m(p)-L_\infty(p)|\le\|g_m-g\|_1.
 \tag{16}
\]

Choose **one fixed** `m_0` such that
`||g_(m_0)-g||_1 < eta/2`, and put
`M_0=max_(z mod3^m_0) g_(m_0)(z)`. It is finite and positive.
The choice depends on the separating label through (14), but not on
the conductor, the values of `p`, or the cutoff subsequence. Since
`g_(m_0)<=M_0`, (15)--(16) imply

\[
 \liminf_{X\to\infty}\frac1{H_X}
       \sum_{n\le X}\frac{|f(n)-p(n)|}{n}
 \ge\frac{\eta}{2M_0}=:\epsilon_f>0.
 \tag{17}
\]

For the quantifier in (17), start with any sequence of cutoffs
realizing the lower limit of its unweighted expression, then take the
common diagonal subsequence of Section 3. Every bound uses the same
`eta,m_0,M_0`; thus this arbitrary lower limit obeys (17). This proves
(PLR) uniformly over all finite conductors.

Finally, for any bounded nonnegative sequence, its logarithmic upper
mean is at most its natural upper mean. This follows by writing the
harmonic sum as its cumulative ordinary sum divided by the endpoint
plus the integral of that cumulative sum against `t^(-2)`. Thus
(PLR-N) follows from (PLR). A lower natural mean is not asserted.

## 7. Consequences for the earlier regularity and mass routes

PR168 TM3 proves a finite-conductor estimate with a factor proportional
to the conductor exponent. Its TM7 converts small ordinary errors to
stationary-weighted errors uniformly, and consequently a sufficiently
fast approximation rate would force a label near one constant. The
present proof passes to an invariant dominated measure before making
that comparison. Mixing then identifies its projection exactly; one
fixed finite density approximation handles all conductors. This removes
the rate requirement rather than optimizing its exponent.

More precisely, if an actual invariant Boolean label `f` satisfies

\[
 \inf_{a,b\ge0}\ \inf_{p\text{ periodic mod }2^a3^b}
 \limsup_{X\to\infty}\frac1X\sum_{n\le X}|f(n)-p(n)|=0,
 \tag{18}
\]

where `p` takes values in `[0,1]`, then `f` is constant. The analogous
statement with logarithmic upper mean also follows. These are
consequences of the uniform error floor, not claims that the infimum
in (18) vanishes for the basin of one or for an arbitrary component.

No transport estimate for the original survivor masses `b_k(y)` or
their resolvents is supplied by (13). If a hypothetical component and
its complement both exist, their projected measures can be
`delta mu` and `(1-delta)mu` with `0<delta<1`. Those diffuse
projections discard the positive weight of any one fixed ordinary
source. Retaining that atom in the survivor route remains essential.

Nor may one infer (18) from `L^1(mu)` density of cylinders. The
ordinary integers form a countable set of `mu` measure zero. Assigning
an arbitrary measurable representative on them says nothing about
their logarithmic sampling averages. The proof avoids that mistake
by constructing every measure from (8), before using compact mixing.

The result is therefore a genuine rigidity theorem for a wider
regularity class, and an obstruction that any hypothetical nonconstant
ordinary invariant label must satisfy. It is not an exclusion of every
ordinary component or of nontrivial cycles.

## 8. Source ledger and evidence level

| Input | Exact source | Role |
|---|---|---|
| Finite stationary densities and recurrence | PR168 `e4599b32e4b1a955ac9315d46782d4ad6a5db96c`, `research/closure-frontier-20261121/TERNARY_STATIONARY_BOUNDARY.md`, TM4 | Equation (1); definitions of the finite periodic weights |
| `L^1` convergence of these densities | Same source, TM6, importing Tao Prop. 1.14, (1.26)--(1.27), and consistency (1.23) | Equations (2), (9), (10), and the fixed truncation in (16) |
| Uniform atom floor | PR180 `f87cb69b3dd86257731ddfbab58c87bf3b5f63d6`, `research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md`, FLOOR | Equation (3) on every unit source at every finite level |
| Logarithmic predecessor populations | The same pinned PR180 `LINEAR_BLOCK_ATOM_FLOOR.md`, Section 6, LOG | Equation (4); Section 5 gives an explicit elementary unit-source conversion |
| Earlier approximation target | The pinned PR168 source, TM3 and TM7 | Identifies the conductor loss and rate premise being removed |

The PR168 file has Git blob `3b5ec5745ec6037bd4cd687877dd34f1e0a5dc03`,
16943 UTF-8 bytes, and SHA-256
`543c0bd7a72d5dec598898850a49a257a9ef3b55cd1fff8741d8699fbad57a7c`.
The PR180 byte pins and the primary Tao version check are in the
companion audit. The primary paper is
[Tao, DOI 10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8),
also [arXiv:1909.03562v7](https://arxiv.org/html/1909.03562v7).

Sections 2--6 are written measure-theoretic proofs, not outputs of a
finite computation or a Lean build. Their reviewed source assumptions
remain distinct from this packet's kernel-checked finite orbit and
Fourier theorems. No numerical value of `epsilon_f` is claimed.
