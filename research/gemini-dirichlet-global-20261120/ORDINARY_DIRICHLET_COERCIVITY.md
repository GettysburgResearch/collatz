# Ordinary Dirichlet coercivity from tripling defects

**PROPOSED mathematical result; no Collatz resolution is claimed.** This note
derives a weighted norm inequality directly from ordinary integer trajectories.
It does not use a finite residue relaxation, a floating point LP certificate, a
fresh distribution of hidden digits, or an assumption that a Dirichlet series
diverges at its abscissa. Its input is the homogeneous finite variation lemma
proved in PR146. A reconstruction of that input is given in Section 8.

The main conclusions are:

* For every real exponent `0 < s < 1`, a summable invariant labeling is controlled
  in the same weighted norm by its multiplication-by-three defect.
* The same inequality holds modulo one constant for bounded invariant real or
  complex labelings whose defect has finite weighted norm.
* For every subcritical invariant set, its ordinary Dirichlet series, tripling
  boundary series, and five-ray boundary series have the same abscissa. At a
  positive subcritical abscissa their critical moments converge or diverge
  together.

This extends the analytic consequence across the entire open strip `0 < s < 1`.
It does **not** prove infeasibility of every abstract residue LP in that strip.
PR146 already proves a power-0.84 boundary lower bound along an unbounded
sequence and divergence of the corresponding critical boundary moment under
its published predecessor input. Those earlier results are not new claims of
this note.

## 1. Definitions and the finite ordinary input

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

An invariant labeling satisfies `f(T(n)) = f(n)` for every positive integer.
In particular `f(2n) = f(n)`. Put

\[
\begin{split}
\delta_3f(n)&=f(3n)-f(n),\\
\delta_5f(n)&=f(5n+1)-f(n),\\
N_s(f)&=\sum_{n\ge1}|f(n)|n^{-s},\\
E_s^{\rm odd}(f)&=\sum_{\substack{n\ge1\\n\ {
\rm odd}}}|\delta_3f(n)|n^{-s},\\
D_f^{\rm odd}(X)&=\sum_{\substack{n\le X\\n\ {
\rm odd}}}|\delta_3f(n)|.
\end{split}
\tag{1}
\]

Sums may initially have value `+infinity`. Because the tripling defect also
obeys exact doubling invariance, Tonelli gives, for `s > 0`,

\[
N_s(\delta_3 f)=\frac{E_s^{\rm odd}(f)}{1-2^{-s}}.
\tag{2}
\]

**Finite ordinary variation lemma.** There are finite absolute constants
`C,C' >= 1` such that every nonnegative real invariant labeling `h` satisfies

\[
\sum_{R\le n\le2R}|h(n+1)-h(n)|
\le C D_h^{\rm odd}(C'R),\qquad R\ge1.
\tag{3}
\]

The sum is over integer `n`; real endpoints are allowed. The same constants
work for every such labeling and every scale. In particular there is no
additive error independent of the labeling.

The binary version is the `b=2` case of PR146's
`research/upper-bit-mergers/TRIPLING_VARIATION.md`. Its constants are uniform
over the labels. Apply it to `1_{h>t}` and integrate over `t >= 0`; the identity

\[
|a-b|=\int_0^\infty
 |1_{a>t}-1_{b>t}|\,dt\qquad(a,b\ge0)
\]

proves (3). For real labelings the same argument integrates over all real
thresholds. For complex labelings, integrate the real result for
`Re(exp(i theta) f)` and use

\[
|z|=\frac14\int_0^{2\pi}|\operatorname{Re}(e^{i\theta}z)|\,d\theta.
\tag{4}
\]

Thus (3) also holds with `h` replaced by a real or complex invariant labeling
and absolute values retained. No extra constant is required. Each finite
interval and its finite defect list suffice for these integrations.

Set

\[
Q=2C',\qquad
K_s=\frac{C Q^s}{2(1-2^{s-1})}\quad(0<s<1).
\tag{5}
\]

We keep the constants of the independently checked finite variation argument;
no optimized numerical value is asserted for them.

## 2. The dyadic inequality with no prior summability assumption

**Theorem OD1.** Let `h >= 0` be invariant. Suppose its dyadic means tend to
zero:

\[
a_k=2^{-k}\sum_{2^k\le n<2^{k+1}}h(n)\longrightarrow0.
\tag{6}
\]

Then for every `0 < s < 1`, as an inequality between extended nonnegative
quantities,

\[
N_s(h)\le K_s N_s(\delta_3 h)
 =\frac{K_s}{1-2^{-s}}E_s^{\rm odd}(h).
\tag{7}
\]

In particular, finiteness of the right side proves finiteness of the left
side; it is not an additional hypothesis.

**Proof.** Pair the even and odd terms in the next shell. Exact doubling
invariance gives the exact identity

\[
a_{k+1}-a_k
=2^{-k-1}\sum_{n=2^k}^{2^{k+1}-1}
       \bigl(h(2n+1)-h(2n)\bigr).
\tag{8}
\]

The edges in this sum belong to the variation interval with `R=2^{k+1}`.
Consequently (3) gives

\[
|a_{k+1}-a_k|
\le \frac C2\,2^{-k}D_h^{\rm odd}(Q2^k).
\tag{9}
\]

Telescoping to the limit in (6) is valid even if the nonnegative series on the
right diverges. It gives

\[
a_k\le\frac C2\sum_{j\ge k}2^{-j}D_h^{\rm odd}(Q2^j).
\tag{10}
\]

Now sum shell by shell, interchange only nonnegative sums, and use a geometric
series:

\[
\begin{split}
N_s(h)
&\le\sum_{k\ge0}2^{(1-s)k}a_k\\
&\le\frac C2\sum_{j\ge0}2^{-j}D_h^{\rm odd}(Q2^j)
                         \sum_{k=0}^j2^{(1-s)k}\\
&\le\frac{C}{2(1-2^{s-1})}
                         \sum_{j\ge0}2^{-sj}D_h^{\rm odd}(Q2^j).
\end{split}
\tag{11}
\]

For each positive integer `m`,

\[
\sum_{\substack{j\ge0\\m\le Q2^j}}2^{-sj}
\le\frac{(Q/m)^s}{1-2^{-s}}.
\tag{12}
\]

Indeed, if `m <= Q`, the full geometric sum is bounded by the displayed right
side. Otherwise start the sum at `ceil(log_2(m/Q))`. Applying (12) to each odd
defect in (11), then using (2), proves (7). The factor `(1-2^{-s})^{-1}` cancels
when the result is expressed in terms of the full tripling norm. This proves
the precise constant in (5). QED.

## 3. A weighted coercivity inequality

**Corollary OD2.** If `f` is real or complex, invariant, and
`N_s(f) < infinity` for some `0 < s < 1`, then

\[
N_s(f)\le K_s N_s(\delta_3 f).
\tag{13}
\]

**Proof.** Apply OD1 to `h=|f|`. Its dyadic means satisfy

\[
a_k\le2^s2^{(s-1)k}N_s(f)\longrightarrow0,
\]

and `|delta_3 |f|(n)| <= |delta_3 f(n)|`. QED.

There is no uniform finite bound for `K_s` as `s` increases to one in this
argument. The denominator `1-2^{s-1}` is the dyadic summation obstruction at the
critical strip boundary. The inequality is an ordinary norm estimate for
invariant functions, not a claim about all abstract residue vectors satisfying
finitely or infinitely many formal linear constraints.

## 4. Bounded labelings modulo constants

**Theorem OD3.** Let `f` be a bounded real or complex invariant labeling, and
let `0 < s < 1`. If `N_s(delta_3 f) < infinity`, there is a unique constant `c`
such that

\[
N_s(f-c)\le K_sN_s(\delta_3 f)<\infty.
\tag{14}
\]

If `f` is binary valued, then `c` is zero or one.

**Proof.** Put `R=2^k`, and on the unit circle define

\[
g_k(t)=f(\lfloor R2^t\rfloor),\qquad0\le t<1.
\]

For `x=R2^t` in one unit interval `[n,n+1)`, the integers `floor(2x)` and
`2 floor(x)` differ by zero or one. Each such interval has logarithmic measure
at most `1/(R log 2)`. By (3),

\[
\|g_{k+1}-g_k\|_{L^1}
\le\frac{C}{R\log2}D_f^{\rm odd}(QR).
\tag{15}
\]

Here and below the weighted variation extension established in (4) handles
complex values. Since

\[
D_f^{\rm odd}(X)\le X^sE_s^{\rm odd}(f),
\tag{16}
\]

the right side of (15) is summable over `k`. Thus `g_k` has an `L^1` limit `g`.

Let `theta=log_2 3`, and interpret translation modulo one. Rotation sends
`x` to `3x/2^j` in `[R,2R)`, with `j=1` or `2`. The integers

\[
3\lfloor x\rfloor\quad\hbox{and}\quad
2^j\left\lfloor\frac{3x}{2^j}\right\rfloor
\]

differ by at most four. Comparing their labels costs at most the adjacent
variation within four of `3 floor(x)`. Each adjacent edge can be associated
with at most four integers `floor(x)`. For `R >= 4`, all these edges lie in
`[2R,8R]`, covered by two intervals to which (3) applies.

The remaining comparison is between `f(n)` and `f(3n)`, with
`R <= n < 2R`. Each odd part has at most one dyadic lift in this half-open
interval. Thus this part costs at most `D_f^{odd}(2R)`. These observations give,
for example,

\[
\|g_k(\cdot+\theta)-g_k\|_{L^1}
\le\frac{1+8C}{R\log2}
       D_f^{\rm odd}(Q_*R),\qquad Q_* =\max(2,4C').
\tag{17}
\]

By (16), this tends to zero. Therefore `g(t+theta)=g(t)` in `L^1`. Unique
factorization makes `theta` irrational. Every nonconstant Fourier coefficient
of `g` is multiplied by `exp(2 pi i m theta) != 1` under this rotation and must
vanish. Hence `g=c` almost everywhere. This argument applies to real and
complex functions. If `f` is binary, an almost everywhere convergent subsequence
of the `L^1` convergence shows `c in {0,1}`.

Each integer in `[R,2R)` has logarithmic measure at least `1/(2R log2)`.
Consequently

\[
R^{-1}\sum_{R\le n<2R}|f(n)-c|
\le2\log2\,\|g_k-c\|_{L^1}\longrightarrow0.
\tag{18}
\]

Apply OD1 to `h=|f-c|` and use
`|delta_3 |f-c|| <= |delta_3 f|` to obtain (14), with the same `K_s` as before.
If two constants satisfied the conclusion, their difference would have finite
`N_s` norm. A nonzero constant has infinite norm for `s<1`, proving uniqueness.
QED.

This is the weighted version of the ordinary logarithmic-circle mechanism
already present in PR146. Boundedness is part of the stated scope; no extension
to arbitrary unbounded labelings modulo constants is needed here.

## 5. Five-ray comparison with no multiplicity loss

For every positive integer `x`, ordinary trajectories give

\[
T^2(20x+1)=15x+1.
\tag{19}
\]

Therefore `f(20x+1)=f(15x+1)` and `f(4x)=f(x)`. The triangle inequality yields

\[
|\delta_3 f(x)|
\le |\delta_5 f(3x)|+|\delta_5 f(4x)|.
\tag{20}
\]

When `x` is odd, the two parameter sets `{3x}` and `{4x}` are disjoint: the
first is odd and the second has 2-adic valuation exactly two. Both maps are
injective. Multiplying (20) by `x^{-s}` and summing over odd `x` proves

\[
E_s^{\rm odd}(f)\le4^s N_s(\delta_5 f),\qquad s>0.
\tag{21}
\]

No factor two from collisions is needed. For nonnegative `f` satisfying OD1,
or whenever the dyadic means of `|f|` tend to zero (in particular for `f` as in
OD2), this gives

\[
N_s(f)\le
\frac{K_s4^s}{1-2^{-s}}N_s(\delta_5 f),\qquad0<s<1.
\tag{22}
\]

For a bounded invariant labeling whose five-ray defect has finite norm, (21)
and OD3 similarly give (22) with `f-c` on the left for a unique constant `c`.

## 6. Equal abscissae and critical moments for a fixed ordinary set

Let `K` be an invariant subset of the positive integers, put `f=1_K`, and define

\[
\partial_3K=\{n:f(3n)\ne f(n)\},\qquad
\partial_5K=\{n:f(5n+1)\ne f(n)\}.
\]

Write `D_A(s)=sum_{n in A} n^{-s}` and define its nonnegative convergence
abscissa by `sigma_A=inf {s>0 : D_A(s)<infinity}`. This convention clips the
classical abscissa at zero for an empty or finite set. For a nonempty ordinary
invariant set, the elementary predecessor branching argument recalled in
PR146 gives a positive convergence abscissa, so the distinction is immaterial
in the intended component application. Suppose `sigma_K < 1`. For some exponent
`0<t<1`, the series
`D_K(t)` is finite, so the dyadic means of `1_K` tend to zero. OD1 therefore
applies at **every** `s in (0,1)`, independently of whether `D_K(s)` is already
known to converge.

The reverse comparisons are elementary:

\[
\begin{split}
D_{\partial_3K}(s)&\le(1+3^s)D_K(s),\\
D_{\partial_5K}(s)&\le(1+6^s)D_K(s),\qquad s>0.
\end{split}
\tag{23}
\]

For the second bound use `5n+1 <= 6n` and injectivity of `n -> 5n+1`. Together
with (7) and (22), these give the extended norm comparisons

\[
\begin{split}
K_s^{-1}D_K(s)&\le D_{\partial_3K}(s)
                     \le(1+3^s)D_K(s),\\
\frac{1-2^{-s}}{K_s4^s}D_K(s)&\le D_{\partial_5K}(s)
                     \le(1+6^s)D_K(s),\qquad0<s<1.
\end{split}
\tag{24}
\]

**Corollary OD4.** Under this subcritical hypothesis,

\[
\sigma_K=\sigma_{\partial_3K}=\sigma_{\partial_5K}.
\tag{25}
\]

At a positive common abscissa `0 < sigma < 1`, the three critical moments
`D_K(sigma)`, `D_{partial_3K}(sigma)`, and `D_{partial_5K}(sigma)` are either all
finite or all infinite. This follows either by applying the extended
inequalities (24) directly at `sigma`, or by monotone convergence as
`s` decreases to `sigma`; the constants have finite positive limits there.

For any nonempty `K` in this range, the same inequalities imply, on the interval
of convergence `sigma < s < 1`,

\[
\begin{split}
\liminf_{s\downarrow\sigma}
 \frac{D_{\partial_3K}(s)}{D_K(s)}&\ge K_\sigma^{-1}>0,\\
\liminf_{s\downarrow\sigma}
 \frac{D_{\partial_5K}(s)}{D_K(s)}&\ge
 \frac{1-2^{-\sigma}}{K_\sigma4^\sigma}>0.
\end{split}
\tag{26}
\]

No hypothesis of divergence at the critical abscissa was used. The endpoint
`sigma=0` is excluded only from the critical-moment and ratio assertions, whose
displayed constants contain `1-2^{-sigma}`. Equality of the nonnegative
abscissae in (25) still holds at zero.

## 7. What this settles, and the first missing global inference

The ordinary implication extends beyond the proposed finite-LP crossover
`0.950131`: every fixed invariant set with abscissa strictly below one satisfies
the full weighted comparisons (24). The proof is homogeneous and uses all
ordinary scales at once. It does not interpolate between a finite selection of
tested exponents.

There remain two separate gaps between these conclusions and Collatz:

1. No argument here proves that the basin of a hypothetical counterexample has
   abscissa below one, or that an ordinary separating boundary has a finite
   moment strong enough to contradict a known predecessor lower bound.
2. Equality or a lower bound for an abscissa controls a limsup counting exponent.
   It does not by itself prove an `Omega(X^gamma)` count at every sufficiently
   large cutoff. Additional distribution across scales would be needed for
   such a conclusion.

The source-persistent mathematical target is consequently an **upper** estimate
on an actual ordinary separating boundary or component, or another mechanism
excluding an invariant binary separation. A formal residue vector may satisfy
all residue balance constraints without carrying the ordinary adjacent
variation geometry used here. No inference about all-level LP infeasibility
is justified by (24).

For context, PR146 already uses the same ordinary variation and rotation
mechanism with a predecessor lower bound to exclude a boundary count
`o(X^0.84)` and to force divergence of its critical `0.84` moment if there is a
second component. The new result in this note is the general weighted norm
inequality, its modulo-constants extension, and the fixed-set equal-abscissa
and critical-moment statements. It is not a first polynomial boundary
amplification theorem.

## 8. Reconstruction and source pin of the finite variation input

This section supplies the finite ordinary construction behind (3), rather than
assuming a statistical model for it. Work first with an arbitrary binary
invariant labeling, and call an odd `u` defective when `f(3u) != f(u)`.
Removing a factor two always preserves the label. Removing one factor three
costs a test at the odd part of the smaller argument.

### 8.1 Neighbor comparisons

Put `g(y)=f(y-1)` and `J(y)=f(y+1)`. The identities of ordinary trajectories give

\[
g(2u)=g(3u),\quad g(4u)=g(9u),\quad J(4u)=J(3u).
\tag{27}
\]

If the odd input `8u-1` passes its tripling test, its ordinary paths also give
`g(4u)=g(8u)`. Write `h=2^v w` with `w` odd. Repeatedly using this comparison
strips the twos from `g(4h)`, with tests `8*2^a*w-1`, `0 <= a < v`. Starting
from `g(4w)=g(9w)`, the chain

\[
g(9u)=g(4u)=g(8u)=g(27u)
\]

raises a ternary exponent at the cost of the same single test. For every odd
`w`, some `j in {2,3,4,5}` makes `Y=3^j w` congruent to 3 or 5 modulo 16. In
these classes `f(Y-1)=f(Y)` by the finite cylinder meetings below. Removing the
bounded number of factors three from `f(Y)` proves `f(4h-1)=f(h)` unless one of
the indicated tripling tests fails.

For the plus sign, passing the test at `16u+1` gives
`J(9u)=J(18u)`, hence `J(16u)=J(32u)` after the two-step exchanges in (27).
It strips the twos from `J(16h)` with tests `16*2^a*w+1`. The chain

\[
J(9u)=J(16u)=J(32u)=J(64u)=J(27u)
\]

raises the ternary exponent with tests `16u+1` and `32u+1`. Some
`j in {2,...,33}` makes `Y=3^j w` congruent to 49 modulo 128 or to 5 modulo 32.
This is a finite statement about all odd residues modulo 128. At these residues
`f(Y+1)=f(Y)`. Remove the bounded number of ternary factors to prove
`f(16h+1)=f(h)` unless one of the tests fails.

The required whole-cylinder meetings are:

| Residue of `Y` | Two starts at its base | Shortcut clock | Common endpoint | Odd inputs on each arm |
|---|---:|---:|---:|---:|
| `3 mod 16` | `2,3` | 4 | 2 | 2 |
| `5 mod 8` | `4,5` | 3 | 2 | 1 |
| `49 mod 128` | `49,50` | 7 | 11 | 3 |
| `5 mod 32` | `5,6` | 5 | 2 | 2 |

Equal clocks and equal counts of odd inputs make the two affine iterate slopes
equal. The displayed moduli preserve each finite parity word. Thus these are
identities on the complete positive cylinders, not a test of finitely many
starting integers.

All test arguments are bounded by a fixed multiple of `h`. For a fixed-ratio
interval `h in [R,bR]`, the multiplicity is bounded independently of `R`:
a failed stripping test recovers its odd `w` uniquely, and that `w` has at most
`1+ceil(log_2 b)` lifts `h=2^v w` in the interval. The other tests are a fixed
finite list of injective affine functions of `w`. A union bound therefore
proves that each neighbor comparison fails at at most
`O_b(D_f^{odd}(O_b(R)))` values of `h`. There is no `log R` loss.

### 8.2 The 17-edge chain

Starting at `288n`, use these offsets in order:

\[
0,18,24,32,33,36,48,64,63,72,96,99,108,144,192,198,216,288.
\tag{28}
\]

The magnitude of each offset difference is a `2,3`-smooth number. Divide both
arguments of an edge by this difference, paying the bounded number of ternary
tests needed to remove it. Each resulting pair has one of the following forms:

| Edges by offsets | Reduced comparison |
|---|---|
| `(0,18),(32,33),(96,99),(192,198)` | `16h,16h+1` |
| `(18,24),(24,32),(33,36),(36,48),(64,63),(63,72),(72,96),(99,108),(108,144),(198,216),(216,288)` | `4h,4h-1`, in either order |
| `(48,64),(144,192)` | `3h,3h+1`, with `h` odd |

For the last two edges, `h=6n+1` and `h=2n+1`. Their comparison follows from the
ordinary step at odd `h` and one tripling test. The first two rows use the
neighbor comparisons above, since doubling identifies `f(16h)` and `f(4h)`
with `f(h)`.

Every affine parameter is injective in `n` and stays in a fixed-ratio interval
when `n in [R,2R]`. Dividing any fixed smooth multiplier costs finitely many
tests at odd parts of injective affine functions. Each fixed odd part has only
a bounded number of dyadic lifts in such an interval. The endpoint comparisons
from `n` to `288n` and from `288(n+1)` to `n+1` have the same property.
Charging every failed adjacent comparison along (28) to a failed odd tripling
test proves the binary form of (3), with finite uniform `C,C'`. Coarea then
gives the weighted form used in this note.

### 8.3 Exact source identification and verification scope

The source revision is PR146 commit
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`.

| Source path in that revision | SHA-256 of the source bytes |
|---|---|
| `research/upper-bit-mergers/TRIPLING_VARIATION.md` | `1a3aef543f1ec76db6b585041108eaa105f1d4ceb0c04fe421f1b15ed47d21bb` |
| `research/upper-bit-mergers/THREE_RAY_VARIATION.md` | `f7f2d0b5803e9ec8c302402e5b7a53fbc06c2ec1cdf92f8d4e816a1c3de5c0d0` |
| `research/upper-bit-mergers/THREE_RAY_DENSITY.md` | `567ecc84a34d41d01ca9bf63a4b4074a92b350c1cbbdc77060927fb1ed72f3b5` |

The companion checker `check_ordinary_dirichlet.py` independently reconstructs
the finite path data, checks complete residue coverage and affine parity
cylinders using exact integers, checks the two geometric-kernel inequalities
using exact rational models, and records source hashes. Its finite arithmetic
replay does not certify the infinite Tonelli, Fourier, or limiting arguments;
those are the proofs in Sections 2 and 4. It does not search for, or claim, an
ordinary counterexample or a Collatz proof.

The canonical JSON of its four cylinder identities, 72 residue-coverage
witnesses, eight affine trajectory identities, and 17 chain edges has SHA-256
`910e57bc8bed1d1fff97f60619f3884a6175c2ed69cbaf302fa34af73d0dfff9`.
The receipt also records 2,079 exact rational scalar-kernel checks and a
negative control showing why the odd-defect version requires both geometric
denominators.
