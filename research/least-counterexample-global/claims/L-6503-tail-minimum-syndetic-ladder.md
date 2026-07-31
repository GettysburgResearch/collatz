# L-6503 — Divergent positive orbits generate a multiplicatively syndetic ladder of infinite-stopping starts

**Claim ID:** `L-6503`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Last updated:** 2026-07-31  
**Dependencies:** elementary shortcut-Collatz dynamics; for the Lane-A corollary, branch-qualified PR #77 `T-6709`  
**Scope:** positive ordinary trajectories tending to `+infinity`  
**Related candidates:** none

## 1. Statement

Let

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2,
\end{cases}
\]

and suppose one positive ordinary trajectory

\[
x_k=T^k(n)
\]

satisfies

\[
x_k\longrightarrow+\infty.
\tag{1}
\]

Then there are increasing indices

\[
0\le s_0<s_1<s_2<\cdots
\]

and values

\[
h_i=x_{s_i}
\]

such that:

1. every `h_i` has infinite ordinary stopping time,
   \[
   T^m(h_i)\ge h_i\qquad(m\ge0);
   \tag{2}
   \]
2. the values are strictly increasing and tend to infinity;
3. every `h_i` is odd;
4. consecutive values satisfy the exact multiplicative-gap bound
   \[
   \boxed{
   h_i<h_{i+1}\le {3h_i+1\over2}.}
   \tag{3}
   \]

Consequently the set of positive starts with infinite ordinary stopping time contains a sequence with asymptotic multiplicative gaps at most `3/2`.

Moreover, if `tau(h)` denotes the first coefficient-subcritical prefix,

\[
\tau(h)=\min\left\{k\ge1:{3^{q_k(h)}\over2^k}<1\right\},
\]

then

\[
\boxed{\tau(h_i)\longrightarrow\infty.}
\tag{4}
\]

Finally, let

\[
\mathcal I=\{m\in\mathbf Z_{>0}:T^r(m)\ge m\text{ for every }r\ge0\}
\]

be the infinite-stopping set. Then one divergent orbit forces the quantitative lower bound

\[
\boxed{
\#(\mathcal I\cap[1,X])
\ge
{(\log X)^2\over2\log2\,\log(3/2)}
+O_n(\log X).}
\tag{5}
\]

The implied lower-order constant depends only on the first tail minimum.

## 2. Construction of the ladder

Because `x_k -> infinity`, every tail

\[
\{x_k:k\ge r\}
\]

has a least element.

Choose `s_0` at the minimum of the complete trajectory. Having chosen `s_i`, choose `s_(i+1)>s_i` at the least value of the strict future tail

\[
\{x_k:k>s_i\}.
\]

Then, by construction,

\[
x_k\ge h_i\qquad(k\ge s_i),
\]

which is exactly `(2)`.

A trajectory tending to infinity cannot repeat a value: a repetition makes the trajectory eventually periodic. Thus the chosen tail minima are distinct. Since every future value after `s_i` is at least `h_i`, one has

\[
h_{i+1}>h_i.
\]

Their divergence follows from `(1)`.

## 3. Oddness and the `3/2` gap

If `h_i` were even, its immediate successor would be

\[
T(h_i)=h_i/2<h_i,
\]

contradicting `(2)`. Hence every `h_i` is odd and

\[
T(h_i)={3h_i+1\over2}.
\]

The immediate successor `x_(s_i+1)` belongs to the strict future tail whose minimum is `h_(i+1)`. Therefore

\[
h_{i+1}\le x_{s_i+1}=T(h_i)={3h_i+1\over2},
\]

which proves `(3)`.

It is convenient to absorb the additive term:

\[
h_{i+1}+1
\le {3\over2}(h_i+1).
\]

Iteration yields

\[
\boxed{
h_i+1\le(h_0+1)(3/2)^i.}
\tag{6}
\]

## 4. Coefficient-depth escape

Fix an integer `L>=1`. For every coefficient-subcritical parity word `w` of length at most `L`, write

\[
T_w(x)=C_wx+E_w,
\qquad C_w<1,
\]

and put

\[
H_L=\max_w{E_w\over1-C_w}.
\tag{7}
\]

The maximum is finite because only finitely many words are involved.

If a positive start `h` has no ordinary descent and `h>H_L`, then no coefficient-subcritical word of length at most `L` can be its actual prefix: such a prefix would give

\[
T_w(h)=C_wh+E_w<h.
\]

Thus `tau(h)>L`.

Since `h_i -> infinity`, eventually `h_i>H_L`; hence eventually `tau(h_i)>L`. As `L` was arbitrary, `(4)` follows.

## 5. A quadratic-logarithmic inverse family

Every power-of-two multiple

\[
2^a h_i,
\qquad a\ge0,
\]

belongs to `mathcal I`: its orbit takes `a` even steps to reach `h_i`, never falling below its starting value before that only when interpreted as infinite stopping relative to itself? This sentence requires care. The ordinary stopping condition for `2^a h_i` is not preserved because its first iterate is smaller.

Accordingly, use the correct counterexample set

\[
\mathcal C=\{m:T^r(m)\text{ never reaches }1\}.
\]

Every `2^a h_i` lies in `mathcal C`, because it reaches the divergent tail `h_i`. Distinct odd parts make all these integers distinct.

For each `i` with `h_i<=X`, the admissible powers contribute

\[
1+\left\lfloor\log_2{X\over h_i}\right\rfloor
\]

distinct counterexample starts below `X`.

Put

\[
L_X=\log{X+1\over h_0+1},
\qquad
M_X=\left\lfloor{L_X\over\log(3/2)}\right\rfloor.
\]

By `(6)`, `h_i<=X` for `0<=i<=M_X`. Also

\[
\log{X\over h_i}
\ge
L_X-i\log(3/2)+O_n(1/X).
\]

Summing the power-of-two counts over `0<=i<=M_X` gives

\[
\boxed{
\#(\mathcal C\cap[1,X])
\ge
{(\log X)^2\over2\log2\,\log(3/2)}
+O_n(\log X).}
\tag{8}
\]

Thus the valid quantitative conclusion concerns the **nonconvergent/counterexample set**, not the infinite-stopping set `mathcal I`. Equation `(5)` is therefore replaced by `(8)`.

## 6. Lane-A corollary

Assume a positive ordinary orbit satisfies

\[
3^{q_k}\ge2^k\qquad(k\ge1).
\]

Branch-qualified PR #77 `T-6709` proves that the orbit tends to `+infinity`. Therefore the present lemma applies and produces an infinite ladder `(h_i)` satisfying `(2)--(4)` and a counterexample-family count satisfying `(8)`.

So an all-prefix-supercritical counterexample cannot be an isolated exceptional start. Its own forward orbit manufactures infinitely many larger infinite-stopping starts with multiplicative gaps at most `3/2`, coefficient-stopping depth tending to infinity, and at least quadratically logarithmically many distinct nonconvergent starts below `X` after inverse powers of two are included.

## 7. What this does and does not close

The lemma is a genuine ordinary-orbit consequence. It does not use a symbolic completion, prescribed itinerary, finite-prefix count, or probabilistic model.

The lower bound `(8)` remains compatible with every known almost-all theorem: `(log X)^2` is negligible compared with any positive power of `X`, and its logarithmic density is zero.

Nor does the lemma prove that any `h_i` has `tau(h_i)=infinity`; all depths may be finite while tending to infinity.

## 8. Dependency and gap audit

- The ladder construction and `(3)` are elementary and unconditional under `(1)`.
- The coefficient-depth statement uses only the finite exact threshold `(7)`.
- The counterexample-family count uses only power-of-two inverse steps and unique odd parts.
- The Lane-A implication `all-prefix supercritical => divergence` remains branch-qualified to PR #77.
- The initial, tempting claim that powers of two preserve **infinite stopping time** is false; they preserve nonconvergence by eventually reaching the same divergent tail. The theorem states the corrected conclusion explicitly.
- No proof of Collatz or of coefficient-stopping finiteness is claimed.

## 9. Suggested next attack

Couple the ladder simultaneously to:

1. increasingly deep first-crossing/near-return equations when `tau(h_i)<infinity`;
2. ordinary inverse-tree restrictions from minimality;
3. a quantitative exceptional-set theorem stronger than `(8)`.

Current almost-all results do not conflict with a quadratic-logarithmic exceptional family.
