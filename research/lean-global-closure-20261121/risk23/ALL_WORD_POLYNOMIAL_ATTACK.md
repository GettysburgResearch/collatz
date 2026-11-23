# All-word cycle attack: polynomial rigidity and the exact loss under prime flow

Date: 2026-11-23.

Status: the attempted unrestricted cycle proof did not close. The checkpoint
contains an exact obstruction to a proposed multiplicative-potential route, a
written account of the full polynomial route and its first unresolved step,
and a small Lean certificate. It does not exclude all nontrivial positive
cycles. No novelty claim is made for the polynomial encoding or the classical
cycle-minimum estimate.

The companion `HARDY_INVERSE_TREE.md` contains the stronger result obtained
while pursuing this route: an explicit infinite-dimensional eigenspace in
unweighted Hardy space throughout \(|\lambda|<2^{1/16}\), ruling out a finite
Hardy index as a cycle-count mechanism. That infinite-dimensional theorem is
a written proof supported by a separate formal universal branching lemma.

## 1. Target and the new input being attacked

Use the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For an actual word of length \(A\), with \(p\) odd steps in positions
\(0\le d_0<\cdots<d_{p-1}<A\), retain the complete quantities

\[
D=2^A-3^p,\qquad
C=\sum_{j=0}^{p-1}3^{p-1-j}2^{d_j}.
\]

In the positive-cycle regime \(D>0\), the exact integer-cycle question is
\(D\mid C\), with the actual itinerary and primitive period retained.
The source for the current distinguished-evaluation-ideal formulation is
[PR185, pinned cycle note](https://github.com/GettysburgResearch/collatz/blob/39ba48e6a8af781193e28c679ea8ab64663c3aa6/research/rigidity-closing-20261122/CYCLOTOMIC_ZERO_FIBER.md).
Its wrong-conjugate example rules out replacing the distinguished evaluation
at \(X=3\) by a total norm, even when the norm is nonzero. Its rotation identity
also prevents treating rotated norms as independent equations.

The attempted replacement here was to keep the complete finite state set,
turn it into one positive polynomial, and try mixed-dilation rigidity. A
second attempt sought a strict arithmetic potential by resolving every prime
valuation instead of using an undifferentiated norm. The second attempt has a
short exact counterexample; the first remains an equivalent all-cycle problem
after its apparent cancellation is fully evaluated.

## 2. The full polynomial retains every state

For a finite positive shortcut cycle \(S\), define

\[
G(z)=\sum_{n\in S}z^n,\qquad
\mathcal T G(z)=\sum_{n\in S}z^{T(n)}.
\]

Then \(\mathcal T G=G\), equivalently

\[
2G(z^2)=G(z)+G(-z)+zG(z^3)-zG(-z^3). \tag{1}
\]

This encoding is prior art: Neklyudov's operator and Lemma 1.1 associate cycle
polynomials with fixed points. The same paper's operator-index bound leaves
the needed index unevaluated. The companion inverse-tree construction proves
that the unweighted Hardy operator has infinite-dimensional fixed space, so
this index cannot yield a finite cycle-count bound. It is not an
unconditional cycle exclusion.
See [Neklyudov, arXiv:2106.11859v9, pp. 1–3 and Theorem 4.4](https://arxiv.org/pdf/2106.11859).

Conversely, a finite polynomial with coefficients zero or one and zero
constant term satisfying \(\mathcal T G=G\) encodes a finite set on which
\(T\) is a permutation: every image is in the set, and a collision would
produce a coefficient at least two. The set therefore splits into actual
cycles. This converse is precisely why the identity preserves the problem;
it does not classify the possible positive supports.

Write

\[
G(z)=E(z^2)+zO(z^2).
\]

Both \(E\) and \(O\) have nonnegative coefficients. Equation (1) becomes

\[
E(z^2)-E(z)=z^2O(z^3)-zO(z^2). \tag{2}
\]

The proposed strong step was that mixed 2/3 dilation, polynomiality and
positivity might force \(G\) to be a multiple of \(z+z^2\). No such rigidity
step was proved. Two natural ways to obtain it fail for identifiable reasons.

### 2.1 Leading degree does not force the trivial cycle

If \(a=\deg O\) and \(b=\deg E\), nonnegative leading coefficients in (2)
give \(2b=3a+2\). In terms of state values, the maximum even state \(2b\)
is the odd successor of the maximum odd state \(2a+1\). This is a valid
maximum-state constraint, but does not bound either degree. Replacing the
full identity by this relation discards the lower support where closure is
decided.

### 2.2 The exact dyadic cancellation returns the entire odd-cycle problem

Since \(E(0)=0\), iteration of (2) gives, for \(|z|<1\),

\[
E(z)=\sum_{k\ge0}\left[
 z^{2^k}O(z^{2^{k+1}})
 -z^{2^{k+1}}O(z^{3\cdot2^k})\right]. \tag{3}
\]

A monomial \(c_bz^b\) of \(O\) contributes the two dyadic rays

\[
c_b\sum_{k\ge0}z^{2^k(2b+1)}
-c_b\sum_{k\ge0}z^{2^k(3b+2)}. \tag{4}
\]

Dyadic rays with different odd parts have disjoint eventual supports. It is
therefore tempting to apply their independence and conclude that only the
trivial ray can cancel. That inference is false: the second ray of one odd
state can cancel the first ray of a different odd state.

Let \(U(n)=(3n+1)/2^{v_2(3n+1)}\) on odd positive integers, and let \(c_n\)
be the coefficient attached to odd state \(n\). Cancellation of every tail
in (3) is exactly

\[
c_q=\sum_{\substack{n\ \mathrm{odd}\\U(n)=q}}c_n
\quad\text{for every odd }q. \tag{5}
\]

For finite nonnegative support, (5) is the invariant-flow equation on the
actual odd Collatz graph. Thus the lacunary-polynomial attack has not obtained
a new inequality; it has returned the same all-state matching condition in a
different basis. No independence theorem has been substituted for (5).

## 3. Exact obstruction to completely additive arithmetic descent

The attempted prime-flow route is ruled out by the two genuine odd paths

\[
25\longrightarrow19\longrightarrow29\longrightarrow11,
\qquad
55\longrightarrow83\longrightarrow125. \tag{6}
\]

Their exact division exponents are respectively \((2,1,3)\) and \((1,1)\).
All five sources are distinct, all five images are distinct, and all are
positive odd integers greater than one and coprime to three. Nevertheless,

\[
\begin{aligned}
19\cdot25\cdot29\cdot55\cdot83
&=29\cdot19\cdot11\cdot83\cdot125\\
&=62\,882\,875. \tag{7}
\end{aligned}
\]

After cancellation the identity is simply

\[
25\cdot55=11\cdot125=1375. \tag{8}
\]

Hence **every prime valuation balances exactly**, not merely their weighted
sum or a total field norm. The obstruction also defeats an arbitrary
completely additive arithmetic potential: if
\(v(ab)=v(a)+v(b)\) for positive integers, strict decrease on the five genuine
edges would give

\[
v(11)<v(25),\quad v(125)<v(55),
\]

and therefore

\[
v(11)+v(125)<v(25)+v(55),
\]

contradicting (8). This argument works in any ordered additive group in which
these strict inequalities can be added. It includes arbitrary real prime
weights and logarithms of completely multiplicative positive weights. The
Lean theorem certifies the integer-valued version; its proof uses only the
five exact edges and the endpoint-product identity.

This does not rule out arithmetic potentials depending on more than prime
valuation sums, nor does it rule out a non-strict potential with plateaus.
It rules out the proposed strictly decreasing, completely additive route.

### 3.1 The complete denominator and the minimum bound are still present

There are \(p=5\) odd edges and \(A=8\) divisions, so

\[
D=2^8-3^5=13.
\]

The minimum of the five odd sources is \(m=19\), and it satisfies the all-cycle estimate used in
[PR175's cycle-minimum checkpoint](https://github.com/GettysburgResearch/collatz/blob/8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73/research/lean-global-closure-20261121/closing/ZERO_ATOM_CLOSING_ATTEMPT.md):

\[
D(3m+1)=13\cdot58=754\le5\cdot256=1280.
\]

The resulting upper bound on a cycle minimum is \(M=32\), so this witness is
not rejected by that inequality.

Expanding the two paths into shortcut edges gives sources

\[
(25,38,19,29,44,22,55,83)
\]

and actual images

\[
(38,19,29,44,22,11,83,125).
\]

The concatenated parity word is \(10110011\), with one positions
\((0,2,3,6,7)\). Its counts are coprime, so the word is primitive. Its
**full** word numerator is

\[
C=3^4+3^3 2^2+3^2 2^3+3\cdot2^6+2^7=581,
\]

and

\[
C\equiv9\pmod{13},\qquad\gcd(C,D)=1. \tag{9}
\]

Thus the distinguished divisibility test correctly rejects the word. The
two paths must not be silently spliced: after 22 the actual next state is
11, not 55. Equation (9) is the remaining full-denominator information that
product/prime-flow balance has lost.

### 3.2 The exact polynomial residual exhibits the lost information

For the full shortcut source polynomial, the defect is

\[
R(z)=\mathcal T G(z)-G(z)
=z^{11}+z^{125}-z^{25}-z^{55}\ne0. \tag{10}
\]

It vanishes on every fourth root of unity and on every fourteenth root of
unity, because the source and image multisets agree modulo 4 and modulo 14.
It also has zero total coefficient sum and zero pairing with every completely
additive arithmetic function. These exact cancellations do not imply
\(R=0\).

The witness is not a hypothetical cycle, not a cycle exclusion and not an
additional small family of cycles being classified. It is a counterexample
to replacing full state matching by the proposed all-prime balance test.

## 4. Why finitely many Fourier tests do not repair the loss automatically

Here is the precise lifting mechanism. Suppose
\(r_i=a_i/D\), \(0\le i<A\), is a positive rational shortcut cycle with odd
denominator \(D\), and \(\gcd(D,6q)=1\). Choose positive integers

\[
n_i\equiv a_iD^{-1}\pmod{6q}.
\]

The lifts have the same parity as the rational states. The exact rational
edge relation, reduced modulo \(6q\) and then divided by two, gives

\[
T(n_i)\equiv n_{i+1}\pmod{3q}.
\]

Consequently the positive polynomial \(G_q(z)=\sum_i z^{n_i}\) satisfies

\[
\mathcal T G_q-G_q\equiv0\pmod{z^{3q}-1}. \tag{11}
\]

Lifts may be made distinct and greater than one by adding different multiples
of \(6q\). If the rational states are three-adic units, the lifts also avoid
multiples of three. The congruence does not make the integer lifts a cycle.

For the primitive word in (9), the rational cycle is

\[
\frac1{13}(581,878,439,665,1004,502,251,383).
\]

With \(q=8\), its representatives modulo 48 are

\[
(41,38,19,29,44,46,23,11),
\]

whose actual images are

\[
(62,19,29,44,22,23,35,17).
\]

Both lists have eight distinct positive entries greater than one, their
residue multisets agree modulo 24, their source parity word is exactly
\(10110011\), and the source minimum 11 is below \(M=32\). Yet their source
and image multisets differ. This example passes all the corresponding
root-of-unity tests while preserving the complete denominator 13 in the
rational construction.

More generally, for any fixed finite set of root orders, choose their least
common multiple \(q\). There are positive rational cycle words whose full
denominator is coprime to \(6q\): for example choose \(A\ge3\) so that
\(2^A\equiv1\) modulo the odd part of \(q\), and use the primitive word with
one odd step and \(A-1\) even steps. Its denominator is \(2^A-3\), coprime
to \(6q\), and (11) applies. This last family establishes the limitation of
fixed finite Fourier sampling only; it is not claimed to satisfy the cycle
minimum estimate. The explicit eight-state example above does satisfy that
estimate.

Therefore the proposed replacement of the entire positive polynomial by a
fixed finite collection of its Fourier values has no automatic closure
theorem. A method choosing its frequencies from the full denominator, using
growing precision, or adding a separately proved support estimate is not
excluded by this argument.

## 5. What was actually proved and what is still needed

The exact affirmative result of this attempt is a no-go theorem for
completely additive strict arithmetic descent, with a five-edge integer
certificate. The polynomial and lifting calculations explain why two
apparently stronger replacements for the total norm still omit actual state
matching. None gives \(N_0<A\), an upper bound on all primitive periods, or a
classification of finite positive fixed polynomials.

For the polynomial route to continue, an additional theorem must control the
**entire** residual \(\mathcal T G-G\) for arbitrary finite positive support.
The dyadic-tail calculation (5), prime valuations, and a fixed finite set of
Fourier samples do not provide that theorem. No such estimate is assumed in
this checkpoint.

## 6. Verification scope

- `PrimeBalanceObstruction.lean` uses only Lean core/Std. It checks all five
  odd edges, exact product balance, distinctness, the full denominator and
  nondivisibility, and the minimum bound. It proves that no integer-valued
  completely additive potential strictly decreases on every actual odd edge
  from an input greater than one.
- The audited edge, product equality and minimum inequality use no axioms.
  The audited nondivisibility theorem uses `propext`; the two ordered-integer
  contradiction proofs use `propext` and `Quot.sound`. None uses `sorryAx`, a
  custom axiom, or `native_decide`.
- `check_cycle_obstructions.py` independently verifies the displayed integer
  and rational calculations, the complete polynomial residuals, and the
  finite Fourier congruences using exact standard-library arithmetic.
- Equations (1)–(5), the general lifting argument, and the real/ordered-group
  potential statement are written mathematics. They are not represented as
  machine-checked general theorems.

The Lean check used version 4.34.1. No older repository modules were rebuilt.
