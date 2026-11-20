# Finite-conductor rigidity with an explicit approximation threshold

**Status: PROPOSED.** The finite inequalities below have elementary proofs.
The exponent `.84` in FC5 uses the explicitly named published predecessor
theorem, not a new replay of its large linear program. Nothing here proves
the required approximation for an actual separating label, and Collatz
remains open.

This is a quantitative continuation of the exact eventual-periodicity
lemma G5 in PR166. It addresses approximations whose moduli grow, rather
than replacing an unknown ordinary component label by a periodic one.
It also supplies a finite-scale version that does not require the stronger
positive-density input used in some harmonic-energy proposals.

## 1. Map, labels, and finite quotients

Throughout,

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n\end{cases}
\quad(n\in\mathbb N_{>0}),\qquad f(Tn)=f(n).
\]

The invariant label `f` may take values in a metric space `(Y,d)`. For a
`q`-periodic label `p`, write

\[
\mathcal O_q(p)=\frac1{q^2}\sum_{a,b\bmod q}d(p(a),p(b)),\qquad
\delta(f,p)=\limsup_{X\to\infty}\frac1X
                 \sum_{1\le n\le X}d(f(n),p(n)).                 \tag{1}
\]

All quotient averages are finite; an asymptotic inequality is meaningful
when its right side is finite. A residue `0` in a computation is just a
representative for positive integers in that residue class. No convergence
claim for an ordinary zero orbit is used.

## 2. FC1: exact dyadic decorrelation

For `q=2^r`, `r>=1`, put

\[
\varepsilon_q(p)=\frac1{2q}\sum_{n\bmod2q}d(p(Tn),p(n)).
\]

Then, for every metric-valued periodic `p`,

\[
\boxed{\mathcal O_{2^r}(p)\le r\varepsilon_{2^r}(p).}          \tag{FC1}
\]

**Proof.** Fix a residue `a mod 2^r`. Its first `r` parity bits are fixed.
Let their odd count be `o(a)` and their affine intercept be `B(a)`. Every
lift `n=a+2^r z` satisfies

\[
T^r(n)=T^r(a)+3^{o(a)}z.                                    \tag{2}
\]

Since `3` is odd, as `z` runs modulo `2^r` the endpoint in (2) runs
bijectively modulo `2^r`. Thus if `n` is uniform modulo `2^(2r)`,
the two residues `n mod2^r` and `T^r(n) mod2^r` are independent and
uniform. Their expected label distance is exactly `O_q(p)`.

The shortcut map sends the uniform distribution modulo `2^(l+1)` to
the uniform distribution modulo `2^l`: the even arm is `2k -> k`,
and the odd arm is `2k+1 -> 3k+2`, both permutations of `k mod2^l`.
Consequently each of the `r` edge distances in

\[
d(p(n),p(T^r n))\le\sum_{j=0}^{r-1}
                         d(p(T^j n),p(T^{j+1}n))
\]

has mean `epsilon_q(p)`. Averaging proves FC1. This proof is a finite
residue calculation and a triangle inequality; it uses neither an
ordinary convergence conjecture nor an external ergodicity theorem.

## 3. FC2: transferring an actual ordinary approximation

For every ordinary-invariant `f`, and every `2^r`-periodic `p`,

\[
\boxed{\varepsilon_{2^r}(p)\le3\delta(f,p),\qquad
       \mathcal O_{2^r}(p)\le3r\delta(f,p).}                  \tag{FC2}
\]

For the first inequality put `e(n)=d(f(n),p(n))` and use ordinary
invariance:

\[
d(p(Tn),p(n))\le e(Tn)+e(n).
\]

The left side is periodic modulo `2^(r+1)`. The average of `e(n)` is
bounded in upper limit by `delta`. The even inputs contribute

\[
\frac1X\sum_{k\le X/2}e(k),
\]

whose upper limit is at most `delta/2`. The odd inputs have distinct
images `3k+2<=3X/2+O(1)` and hence contribute at most `3delta/2`.
These estimates use positivity, not an equidistribution assumption on
the approximation error. FC1 gives the second inequality.

There is a quotient value `c=p(a)` with

\[
\frac1q\sum_{b\bmod q}d(p(b),c)\le\mathcal O_q(p),
\]

because the average of the left side over `a` is `O_q(p)`. Therefore

\[
\boxed{\limsup_{X\to\infty}\frac1X\sum_{n\le X}d(f(n),c)
                   \le(1+3r)\delta(f,p).}                  \tag{3}
\]

For Boolean `f,p`, the value `c` is `0` or `1`. Thus approximations with
`r*delta(f,p)->0` force `f` to be constant in mean, after passing to
one of the two choices of constant. **Constant in mean does not mean
pointwise constant.** An invariant exceptional set of density zero has
not been ruled out by this argument. FC4--FC5 below retain the finite
source count needed for a pointwise conclusion.

## 4. FC3: conductors coprime to six

Let `q>1`, `gcd(q,6)=1`, and `k=ceil(log_2 q)`. Then

\[
\boxed{\mathcal O_q(p)\le28k\delta(f,p).}                   \tag{FC3}
\]

Here is a finite quotient proof with all changes of variable justified.
Put

\[
A=\frac1q\sum_xd(p(2x),p(x)),\quad
B=\frac1q\sum_xd(p(3x+1),p(x)),\quad
D=\frac1q\sum_xd(p(x+1),p(x)).
\]

Doubling invariance and positivity of errors give `A<=3delta`.
To estimate `B`, parameterize the odd ordinary inputs by `n=2j+1`.
They run uniformly through every residue modulo odd `q`; their images
under `n ->3n+1` are `6j+4`. The exact ordinary equality
`f(6j+4)=f(2j+1)` therefore gives `B<=8delta` by counting errors up
to `2X` and `6X`. This is the ordinary-integer source of `B`; the odd
branch is not being applied to even ordinary integers.

Use the following path in the quotient, where division by two is legal:

\[
3x+1\longleftrightarrow x\longleftrightarrow x/2
       \longleftrightarrow 3x/2+1\longleftrightarrow3x+2.
\]

The four mean edge costs are `B,A,B,A`, since multiplication by two
or three and translation are permutations modulo `q`. It follows that

\[
D\le2A+2B.                                                 \tag{4}
\]

Now start uniformly at `x modq`, choose independent fair bits `b_i`,
and repeatedly replace `x` by `2x+b_i`. Each intermediate state is
uniform. Its mean label cost is at most `A+D/2`; after `k` moves the
endpoint is `2^k x+U`, with `U` uniform in `[0,2^k)`. Since
`q<=2^k<2q`, every target residue has probability at least `1/2^k`.
Nonnegative averaging and the triangle inequality give

\[
\mathcal O_q(p)
 \le\frac{2^k}{q}\,k(A+D/2)
 \le2k(2A+B)
 \le28k\delta.
\]

No assertion about the optimal constant 28 is made. For `q=1` the
oscillation is zero. The coprimality condition is essential to this
particular proof; a conductor divisible by three is not silently treated
as a permutation quotient.

## 5. FC4: a finite-scale inequality for actual label errors

Suppose `f,p` are Boolean, `q=2^r`, and `N` is a positive multiple of
`2q`. Define

\[
M_f(N)=\min\bigl(\#\{n\le N:f(n)=0\},
                 \#\{n\le N:f(n)=1\}\bigr),\qquad
E_{f,p}(X)=\#\{n\le X:f(n)\ne p(n)\}.
\]

Then

\[
\boxed{M_f(N)\le(1+3r)E_{f,p}(3N/2).}                     \tag{FC4a}
\]

Indeed the average of the periodic edge defect on `[1,N]` is exactly
`epsilon_q(p)`. Summing `e(Tn)+e(n)` over that interval and bounding
each of the source, even-image, and odd-image sums by `E(3N/2)` gives

\[
N\varepsilon_q(p)\le3E(3N/2).
\]

Choose the quotient anchor `c` as in (3). Since `q|N`, the number of
errors between `p` and `c` on `[1,N]` is at most `N O_q(p)`. Hence

\[
M_f(N)\le\#\{n\le N:f(n)\ne c\}
       \le E(N)+N\mathcal O_q(p)
       \le(1+3r)E(3N/2).
\]

For `gcd(q,6)=1`, `q>1`, and `q|N`, the same reasoning gives

\[
\boxed{M_f(N)\le(1+12\lceil\log_2q\rceil)E_{f,p}(6N).}    \tag{FC4b}
\]

For completeness, in the finite averages defining `A,B`, each of their
two error sums is bounded by `E(6N)`. Thus
`A,B<=2E(6N)/N`. The intermediate bound
`O_q(p)<=2k(2A+B)` proves FC4b. These are finite inequalities for the
same supplied invariant label and the same approximation. No new source
is substituted by a number satisfying convenient congruences.

## 6. FC5: the pointwise threshold supplied by predecessor growth

The published input used here is Krasikov--Lagarias, *Bounds for the
3x+1 Problem using Difference Inequalities*, Theorem 6.1. In the present
notation its bound is `pi_a(X)>=X^.84` once `X>=X_0(a)`, for each fixed
positive ternary-unit target `a`; `pi_a` counts its ordinary predecessors.

The source is [arXiv:math/0205002](https://arxiv.org/abs/math/0205002),
with the displayed theorem on page 16 of the PDF (printed page 16).
Its computational linear-program certificate is an external dependency;
the present finite checker does not rerun it.

PR146, `TWO_SCALE_TRIPLING.md`, already explains the following useful
amplification, which we reconstruct to keep the quantifier visible:
every nonempty ordinary merger component `C` satisfies

\[
\frac{\#(C\cap[1,X])}{X^{.84}}\longrightarrow\infty.         \tag{5}
\]

Choose an odd ternary-unit target `a` in `C` which is off any cycle of
the accelerated odd map. Such a target exists: every component has an
odd ternary unit, and each odd ternary unit has at least two distinct
odd ternary-unit preimages. To see the latter fact, among the three
exponents `1<=v<=6` making `2^v a=1 mod3`, precisely one makes
`2^v a=1 mod9`; the other two give positive odd ternary units
`(2^v a-1)/3`. If `a` is initially on a cycle, at most one of its odd
preimages is the cyclic predecessor, so an off-cycle one can be chosen.

At each fixed depth `h`, choose two such predecessors at every node.
The resulting `2^h` leaves are distinct, and none reaches another under
the accelerated map. Otherwise their common depth-`h` image `a` would
be periodic. Their ordinary predecessor sets are consequently disjoint.
Apply the external theorem to this finite collection of leaves and take
the largest of their finitely many thresholds. The resulting component
count is at least `2^h X^.84` eventually, for each fixed `h`, proving
(5). This is not a uniform threshold over an infinite tree.

If a Boolean invariant `f` is nonconstant, each of its two fibers
contains a merger component, so `M_f(N)/N^.84 -> infinity`. FC4 now
gives the following **uniform lower bound on approximation error**:

- For every dyadic `q=2^r<=N/2` with `2q|N`, and every Boolean
  `q`-periodic `p`,
  \[
  E_{f,p}(3N/2)=\omega\!\left(\frac{N^{.84}}{\log N}\right).
  \tag{FC5a}
  \]
- For every `q<=N`, `q|N`, `gcd(q,6)=1`, and every such periodic
  `p`, the same lower bound holds for `E_{f,p}(6N)`. The case `q=1`
  follows directly from `E(N)>=M_f(N)`.

Uniformity means that the lower factor tending to infinity depends
only on `f`, not on the chosen admissible `q` or `p` at that scale.

In particular, for the actual basin indicator, a construction of dyadic
periodic approximations on arbitrarily large eligible scales with
`E(3N/2)=O(N^.84/log N)` would prove that indicator constant. Its value
at 1 would then prove Collatz. This is a rigorous sufficient threshold,
not a claim that the approximation is available or that the threshold
is sharp.

The currently inspected survival bound in PR146 has exponent about
`.9499555`, even with its logarithmic correction. It does not reach
this `.84` error threshold, and its counted set is not automatically
the mismatch set for a constructed periodic approximation. Both the
numerical gap and the source-identification gap must be addressed.

## 7. FC6: the dyadic conductor loss cannot be uniformly removed

There are periodic real labels `p_r` taking values in `[-1,1]`, for
every even `r>=2`, such that

\[
\boxed{\mathcal O_{2^r}(p_r)\ge\frac9{1024},\qquad
       \varepsilon_{2^r}(p_r)\le\frac{\sqrt{12}}r.}          \tag{FC6}
\]

Thus no inequality `O_(2^r)(p)<=C epsilon_(2^r)(p)` can hold for all
these quotients with a constant independent of `r`. The linear loss in
FC1 has the correct order. These labels are approximate invariants on
finite quotients, **not** ordinary-invariant separating labels.

Write `r=2m` and take the integer tent weights

\[
(w_0,\ldots,w_{r-1})=(1,2,\ldots,m,m,\ldots,2,1),\qquad
V=\sum_iw_i^2=\frac{m(m+1)(2m+1)}3,\quad H=\lceil\sqrt V\rceil.
\]

Let `xi_i(n)=2*(T^i(n) mod2)-1`. Define

\[
X(n)=\sum_{i=0}^{r-1}w_i\xi_i(n),\qquad
p_r(n)=\max(-1,\min(1,X(n)/H)).                            \tag{6}
\]

The first `r` parities are determined by `n mod2^r`, and their words
run bijectively through `{0,1}^r`. This bijection follows inductively
by solving the affine parity condition at each lift; it is also the
finite parity-coordinate form of the calculation used in FC1.
Hence the `xi_i` are independent fair signs under the quotient average.

The centered random sum has `E X^2=V` and
`E X^4=3V^2-2 sum w_i^4<=3V^2`. Cauchy--Schwarz applied to
`X^2 1_(|X|>=sqrt(V)/2)` gives the elementary Paley--Zygmund bound

\[
\Pr(|X|\ge\sqrt V/2)\ge3/16.
\]

By symmetry each sign has probability at least `3/32`. Two independent
copies with opposite such signs have probability at least `9/512`.
Their clipped labels differ by at least `sqrt(V)/H>=1/2`, since
`H<=sqrt(V)+1<=2sqrt(V)`. This proves the first inequality of FC6.

Under one shortcut step the signs shift by one. The coefficients of
`X(Tn)-X(n)` are the two endpoint weights and the successive weight
differences. Their squared sum is exactly `r`. Clipping is
`1/H`-Lipschitz, so Cauchy--Schwarz gives

\[
\varepsilon_{2^r}(p_r)\le\frac{\sqrt r}{H}
 \le\sqrt{r/V}\le\frac{\sqrt{12}}r,
\]

where `V>=r^3/12`. This proves the second inequality.

The construction also works for other odd affine shortcut maps. In
particular the dyadic decorrelation inequality itself does not distinguish
`3n+1` from `3n-1`, whose positive map has the fixed point 1 and the
distinct cycle `5,7,10`. The closing input must concern the actual
arithmetic label, rather than merely small finite-quotient defect.

## 8. Closing attempts and the exact remaining obligation

Three possible closing steps were considered:

1. **Use a periodic or character expansion with growing conductor.**
   FC2--FC5 quantify the error required. Exact invariance of `f` does
   not establish that error. A generic finite Fourier expansion on a
   selected initial interval need not approximate its required enlarged
   interval; extending it periodically is precisely an unproved step.
2. **Remove the conductor factor by a uniform spectral gap.** FC6
   disproves that proposal already on finite dyadic quotients, with
   explicit bounded labels and exact moment formulas.
3. **Use the inspected prefix-survivor power saving as the error bound.**
   The exponent is larger than `.84`, and the survivor predicate is
   not an approximation to the actual basin label without an additional
   transfer argument. No such argument was obtained here.

The positive result is an explicit, source-preserving, finite-conductor
stability theorem and a finite-scale approximation threshold. The first
unsupported step in a full proof by this route is the construction of
the required periodic approximation to the actual invariant label.

## 9. Source pins and checker scope

- PR166, full head `5996b9f525ca50978bc34f423192c36a87765bf3`,
  `research/grh-certificate-closure-20261120/GRH_INTERFACES.md`, G5:
  exact eventual-periodicity rigidity and the missing approximation
  interface for conductors that grow. The present quantitative estimates
  are proved above and do not use GRH.
- PR146, full head `fd991063721e9c157d318e40bb20131762f7d750`,
  `research/upper-bit-mergers/TWO_SCALE_TRIPLING.md`: the predecessor
  antichain amplification reconstructed in FC5. Its
  `LEAST_FAILURE_SIEVE.md` supplies the different prefix-survivor bound;
  no approximation claim is imported from it.
- Krasikov--Lagarias, [arXiv:math/0205002](https://arxiv.org/abs/math/0205002),
  Theorem 6.1: external predecessor bound used only in FC5.
- A literature search located a separate recent proposed automatic-set
  theorem at [rStation paper 64](https://rstation.ai/problems/collatz/papers/64/v2).
  It was not needed for any proof here and is not imported as a verified
  dependency. This note does not claim priority over all automaticity or
  finite-quotient literature.

`check_finite_conductor.py` independently enumerates the finite parity
bijections and endpoint independence, checks all Boolean labels for the
small specified moduli, verifies the affine commutator and averaging
constants, and checks rational tent-label moments and finite instances of
FC6. Its `3n-1` control checks FC4 on a nonconstant actual component
label over the stated finite range. It rejects malformed conductor and
decorrelation inputs with explicit exceptions, also under optimized
Python. The universal statements rest on the proofs, not on these finite
executions. No formal proof assistant verification is claimed.
