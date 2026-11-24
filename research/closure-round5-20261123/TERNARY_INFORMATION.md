# No entropy-rate loss in the nonnegative-drift ternary coding

23 November 2026. Parent checkpoint:
`cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

**Status: written theorem, with explicit classical entropy inputs and
an elementary complete-carry core. Full Collatz and the required
collision upper remain OPEN.** This result treats arbitrary ergodic
stationary gap laws of finite mean at most `log_2(3)`. It requires no
independence or mixing assumption. An additional same-source consequence
retains an explicit ergodicity hypothesis on the actual backward-gap limit.

The result identifies the information that the ternary projection retains.
The total clock and carry quotient can create ambiguity, but on typical
words in this drift range they create only subexponentially many choices.
The projection therefore loses zero Shannon entropy per gap. This is
not a uniform bound on all residue masses or on their second moment.

## 1. Statement and normalization

Let `eta` be an ergodic stationary probability on sequences of positive
integer gaps `G_1,G_2,...`, with

\[
 g=\mathbb E_\eta G_1\le\ell:=\log_2 3<\infty.
\tag{1}
\]

Write `h=h(eta)` for its entropy rate in natural logarithms. Finite mean
implies finite one-letter entropy: comparison with any positive geometric
reference law gives `H(G_1)<infinity`. Hence the countable-alphabet
Shannon--McMillan--Breiman theorem applies.

Set `A_i=G_1+...+G_i` and define the always convergent ternary series

\[
 Z=\sum_{i\ge1}3^{i-1}2^{-A_i}\in\mathbb Z_3^\times,
 \qquad \mu=Z_*\eta.
\tag{2}
\]

Let `mu_m` be its residue law modulo `3^m`. Then

\[
\boxed{
 \lim_{m\to\infty}
 \frac{-\log\mu(Z+3^m\mathbb Z_3)}{m\log3}
 =\frac h{\log3}\quad\mu\text{-almost everywhere},
}
\tag{3}
\]

and

\[
\boxed{
 \lim_{m\to\infty}\frac{H(\mu_m)}m=h,
 \qquad H(G_1,\ldots,G_m\mid Z\bmod3^m)=o(m).
}
\tag{4}
\]

Thus `mu` is exact dimensional and has information dimension `h/log3`.
The maximum possible value under (1) is
`H(Geom(mean ell))/log3 = H_binary(1/ell)/log2`, the previously used
critical exponent `theta=0.949955527...`.

## 2. Exact finite arithmetic and the typical fibre count

For a length-`m` gap word, retain its complete numerator

\[
 C_m=\sum_{i=1}^m3^{i-1}2^{A_m-A_i}>0.
\]

Both its real partial sum and its ternary residue use this same integer:

\[
 R_m=C_m/2^{A_m},\qquad
 Z\equiv C_m2^{-A_m}\pmod{3^m}.
\tag{5}
\]

For fixed `m`, `A_m` and `C_m`, the gap word is unique. One can decode
the associated complete shortcut word of length `A_m` and odd count `m`
using its full carry, then read the gaps in reverse chronological order.
This is exactly the earlier fixed-clock carry decoder in
[`CarryFibers.lean`](../whole-repo-round3-20261123/CarryFibers.lean).
The reversal is important: `(G_1,...,G_m)` lists the most recent gap
first in the inverse coding, so its forward odd-gap list is reversed.

For any fixed ternary residue `z` and total `A`, equation (5) fixes
`C_m mod 3^m`. Restrict also `0<C_m/3^m<=Q`. There are at most
`floor(Q)+1` possible integer carries, hence at most that many words.
If there are at most `D+1` allowed total clocks, the entire fibre has at
most `(D+1)(floor(Q)+1)` words. No uniformity of word weights, source
equidistribution or independence is used.

To apply this at typical words, put

\[
 S_j=j\log3-A_j\log2,\qquad
 d=\log3-g\log2\ge0.
\]

Ergodicity and integrability give `S_j=dj+o(j)` almost surely, and hence

\[
 \max_{0\le i\le m}|S_i-di|=o(m).
\tag{6}
\]

The last assertion follows by separating a fixed initial segment from
the indices where the relative error is uniformly small. Now

\[
 \frac{C_m}{3^m}
 =\frac13\sum_{i=1}^m e^{S_i-S_m}
 \le\frac m3\exp\!\left(
       2\max_{0\le i\le m}|S_i-di|\right).
\tag{7}
\]

The term `d(i-m)` has the required nonpositive sign. Therefore

\[
 A_m=O(m),\qquad
 \log^+(C_m/3^m)=o(m)
\quad\eta\text{-almost surely}.
\tag{8}
\]

This bounds ambiguity after retaining **both** the total clock and full
carry quotient. The analogous assertion with neither coordinate retained
would not follow just from fixed-clock injectivity.

## 3. Uniform restrictions and the lower local dimension

Fix `epsilon>0`. By (8) and Shannon--McMillan--Breiman, the increasing
measurable sets `E_N` on which, for every `m>=N`,

\[
 A_m\le(\ell+1)m,\qquad
 C_m/3^m\le e^{\epsilon m},\qquad
 \eta[G_1,\ldots,G_m]\le e^{-(h-\epsilon)m}
\tag{9}
\]

have measures tending to one. Use unnormalized restrictions
`nu_N=Z_*(eta|E_N)<=mu`. For every ternary depth-`m` ball, the finite
fibre count gives, for `m>=N`,

\[
 \nu_N(z+3^m\mathbb Z_3)
 \le (\lfloor(\ell+1)m\rfloor+1)
      (\lfloor e^{\epsilon m}\rfloor+1)
      e^{-(h-\epsilon)m}
 =e^{-m(h-2\epsilon)+o(m)}.
\tag{10}
\]

Restriction alone has the wrong inequality direction for a conclusion
about the larger measure `mu`. The needed transfer is explicit. Let
`f_N=dnu_N/dmu`. On the increasing finite residue partitions,

\[
 \frac{\nu_N(z+3^m\mathbb Z_3)}
      {\mu(z+3^m\mathbb Z_3)}
 =\mathbb E_\mu[f_N\mid z\bmod3^m]
 \longrightarrow f_N(z)
\tag{11}
\]

almost surely by martingale convergence. The residue sigma-algebras
generate the Borel sigma-algebra. Also `f_N` increases to one almost
everywhere, since `nu_N` increases to `mu`. Thus almost every point has
`f_N(z)>0` for at least one `N`. At that point (11) transfers (10) to
an upper bound on its original `mu`-ball mass with only a fixed
multiplicative constant. Consequently the lower local dimension is at
least `(h-2epsilon)/log3`. Let epsilon decrease through a countable
sequence to zero.

This step does not assume a uniform convergence rate, and it does not
discard a fixed amount of mass when asserting an almost-everywhere result.

## 4. The matching upper bound and entropy identities

Every infinite continuation of a given gap prefix maps into the same
ternary depth-`m` ball. Therefore, for eta-almost every word,

\[
 \mu(Z+3^m\mathbb Z_3)\ge\eta[G_1,\ldots,G_m].
\tag{12}
\]

Shannon--McMillan--Breiman makes the upper local dimension at most
`h/log3`. Together with Section 3, this proves (3).

For (4), the residue is a function of the word, so
`H(mu_m)<=H(G_1,...,G_m)`, and the latter divided by `m` tends to `h`.
Fatou's lemma applied to the nonnegative normalized ball information
from (3) gives the reverse liminf for `H(mu_m)/m`. Both entropy rates
are therefore `h`. Subtracting them gives the conditional entropy in
(4). All finite block entropies are finite.

## 5. A direct consequence on the same ordinary odd clock

Let `q_j` be the distinct positive odd states of one hypothetical
injective ordinary orbit, with actual gaps `g_j` and prefix height
`H_M=max_{0<=j<=M}q_j`. Along a subsequence `M_i`, suppose the
empirical laws of its reversed gap words converge, at every fixed
depth, to an **ergodic** stationary law `eta`, and

\[
 \beta=\liminf_i\frac{\log(H_{M_i}+1)}{\log M_i}<\infty.
\tag{13}
\]

Use exactly this gap law in (2). Theorem 3 of
[`FIXED_SOURCE_PRESSURE.md`](FIXED_SOURCE_PRESSURE.md) proves directly
on the same endpoints that

\[
 1\le a:=\mathbb E_\eta G_1\le\ell,\qquad
 h(\eta)\ge\frac{a\log2}{\beta}.
\tag{14}
\]

The proof retains the full original source congruence. It establishes
growing-window concentration by first passing bounded fixed-window
averages to the ergodic limit, then increasing the window length.
It also proves the needed continuity of fixed-block Shannon entropy
on this countable alphabet from a bounded first moment. No return-map
identification between separately chosen binary and odd-clock limits
is required.

The ternary factor `mu=Z_*eta` is the corresponding actual odd-time
residue limit. The exact past affine identity at an endpoint `q_j` is

\[
 q_j=\frac{3^m q_{j-m}+C_m}{2^{A_m}}
 \equiv C_m2^{-A_m}\pmod{3^m},\qquad j\ge m,
\tag{15}
\]

where the same reversed gap word gives `A_m,C_m` as in (5).
For each fixed `m`, pushing its empirical law through this finite
residue map and passing to the limit therefore gives `mu mod 3^m`.
The initial `m` endpoints have vanishing weight. This identification
uses only fixed-depth limits and retains the original ordinary source.

Equations (3)--(4) and (14) now give

\[
\boxed{
 \dim_{\rm info}\mu=\dim\mu=\frac{h(\eta)}{\log3}
 \ge\frac{a}{\ell\beta}>0.
}
\tag{16}
\]

If this actual gap law is critical, meaning `a=ell`, the lower bound
is `1/beta`. More generally its one-letter entropy is at most
`H(Geom(mean a))`, giving the further necessary height constraint

\[
 \beta\ge\frac{a\log2}{H(\operatorname{Geom}(\text{mean }a))}.
\tag{17}
\]

Here `a=1` would force a constant gap process and zero entropy, which
contradicts (14) at finite beta. Thus any law satisfying these finite
height hypotheses has `a>1` and the denominator in (17) is positive.
At `a=ell`, (17) recovers the existing critical exponent constraint
`beta>=1/theta`. This is not asserted to improve the strongest known
general height estimates; it ties the necessary growth to the actual
limiting entropy and mean of this source.

We have not silently set `a=ell`. Even when the original empirical
average gap tends to ell, its limiting first moment can lose mass.
The direct estimate (16) includes that case. Ergodicity of the chosen
gap limit, the finite height exponent, and the same-source limit
identification remain explicit hypotheses. The theorem makes no
claim that every escaping ordinary orbit satisfies those hypotheses.

## 6. What this does and does not supply for collision closure

Equations (3)--(4) identify information dimension, not order-two Renyi
dimension. The restrictions `E_N` give uniform small-ball bounds for
their own submeasures, but provide no exponential rate for the omitted
mass. They therefore cannot be inserted into the untrimmed collision
upper bound without an additional estimate.

For example, a biased Bernoulli measure with disjoint equal-scale
branches is exact dimensional with Shannon dimension
`[-p log p-(1-p)log(1-p)]/log3`, while its order-two dimension is
`-log(p^2+(1-p)^2)/log3`, strictly smaller when `p!=1/2`.
The distinction survives exact dimensionality. A critical Sturmian law
has zero entropy and dimension zero, consistent with (3) and with the
separate critical nonatomic control in `FIXED_SOURCE_PRESSURE.md`.

Thus the new theorem replaces an unknown projection-entropy loss by an
exact formula in the stated ergodic drift range. It does not establish
polynomial height, ergodicity, maximal entropy, exponential typical-set
tails, or the same-source critical collision upper. None of those
missing implications is assumed in the proof.

## 7. Literature and proof boundary

- K. L. Chung, [*A note on the ergodic theorem of information theory*](https://doi.org/10.1214/aoms/1177705069),
  Annals of Mathematical Statistics 32 (1961), 612--614, is the
  countable-alphabet extension of the Shannon--McMillan--Breiman theorem.
  The finite one-letter entropy hypothesis is verified above.
- Feng--Hu, [*Dimension theory of iterated function systems*](https://arxiv.org/abs/1002.2036),
  motivates the distinction between symbolic entropy and projection
  entropy. Its finite-alphabet Euclidean theorem is not asserted to
  cover this countable ternary system automatically; Sections 2--4
  give the required arithmetic proof directly.
- Lyapunov Weaver, [rStation Paper 9, v2](https://rstation.ai/problems/collatz/papers/9),
  Theorem 5 and Corollary 6, already give bounded decoding entropy and
  exact dimension for a specified tilted iid Syracuse law. Its
  fixed-total carry mechanism is credited. The proof here treats the
  stated general ergodic finite-mean range, using sublinear rather than
  bounded information loss. No historical priority claim is made.
- [rStation Paper 150, v2](https://rstation.ai/problems/collatz/papers/150),
  Section 4, gives source-entropy inequalities for stationary legal
  inverse laws under Haar absolute continuity. No such absolute
  continuity is assumed or deduced here.

This file is a written proof. No new infinite entropy or dimension
theorem is claimed as formalized in Lean. The earlier complete-carry
decoder and new finite same-source parity core have their own compiled
scope; finite replay checks the arithmetic fibre count, not the
ergodic theorems or the infinite dimension conclusion.
