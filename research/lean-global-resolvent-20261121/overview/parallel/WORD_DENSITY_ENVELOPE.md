# An explicit complete-clock density envelope

## Outcome and scope

For every inverse depth `k>=0` and every ternary residue `q`, the complete
finite-level Syracuse density satisfies

\[
\boxed{D_k(q)\le(4k+2)(3/2)^k.}                    \tag{1}
\]

All positive inverse exponents and all total clocks are included. The
constant is explicit and independent of the target and depth. No
predecessor-density hypothesis, uniform `L^p` estimate, stationarity
identification, or unproved pointwise mixing statement is used in the proof.

The companion `ClockSliceBound.lean` formalizes the arithmetic core for
arbitrary finite families: fixed-length/fixed-total numerator injectivity,
the exact numerator range, the complete fixed-total cardinal bound, and
the corresponding normalized mass bound. The geometric tail and its
infinite-sum passage below are written proofs, not claimed as Lean theorems
in that file. All seven public lemmas/theorems are explicitly audited.

This is a quantitative reconstruction and formal checkpoint, not a claim
to a new maximum-density exponent. Tao's Lemma 6.2 supplies the classical
fixed-total offset injectivity. The author-primary manuscript *Ternary
Syracuse laws: real localization, clock stability, and critical regularity*,
Theorem 9, already gives the maximum-density exponential rate `log(3/2)`.
Its Appendix B.2 proves a real-truncated prefix bound
`C(1+B)k` by fixed-total counting and a full clock tail; taking
`B=(3/2)^k-1` already gives the order in (1). The present proof supplies
the explicit constant `(4k+2)`, a checked finite arithmetic core, and the
contact-front interface used in this checkpoint.

Primary source: <https://rstation.ai/problems/collatz/papers/9>.
No asymptotic result from that manuscript is a dependency of the proof below.

## 1. Exact words and their integer numerators

For a positive-letter word `a=(a_1,...,a_k)`, put

\[
A_j=a_1+\cdots+a_j,\qquad A=A_k,\qquad
\beta_a=\sum_{j=1}^k3^{j-1}2^{-A_j},
\qquad C_a=2^A\beta_a.
\]

For nonempty words, `C_a` is a positive odd integer. If `a'` is the word
with its last letter removed, then

\[
C_a=2^{a_k}C_{a'}+3^{k-1}.                         \tag{2}
\]

For `k=1`, `C_a=1`, independently of the sole letter; the supplied total
`A` determines that letter. For `k>=2`, `C_{a'}` is positive and odd.
Consequently the exact two-adic valuation of `C_a-3^{k-1}` is `a_k`.
It recovers the last letter, then (2) recovers the preceding numerator.
Repeating recovers all letters except the first, which is fixed by `A`.

Thus, for each fixed pair `(k,A)`, distinct words have distinct integer
numerators. This argument permits arbitrary positive letters.

The formal file stores the exponents minus one in reverse order. For a
natural list `w`, its original clock is `length(w)+sum(w)`, and the formal
numerator recurrence is exactly (2). Hence no positivity assumption or
hidden exponent cap is needed in the formal statements.

## 2. One complete clock slice costs at most `(3/2)^k`

Since `A_j>=j`,

\[
\beta_a\le\sum_{j=1}^k3^{j-1}2^{-j}=(3/2)^k-1.
\]

Writing `B=A-k>=0`, this is the exact integer inequality

\[
\boxed{C_a+2^A\le3^k2^B,\qquad 0\le C_a<3^k2^B.}             \tag{3}
\]

The residue condition defining the finite density is

\[
\beta_a\equiv q\pmod{3^k}
\quad\Longleftrightarrow\quad
C_a\equiv2^Aq\pmod{3^k}.                          \tag{4}
\]

The interval `0<=C<3^k 2^B` contains at most `2^B` integers in any one
residue class modulo `3^k`. Numerator injectivity therefore shows that
the number of compatible words of total `A` is at most `2^(A-k)`.
Every such word has normalized density weight `3^k 2^(-A)`, so

\[
\boxed{D_{k,A}(q)\le2^{A-k}3^k2^{-A}=(3/2)^k.}    \tag{5}
\]

Lean proves the stronger finite-family form: any finite collection of
words with the same length, total, and residue has the displayed cardinal
and mass bounds. It does not assume that the collection has been generated
with a bounded alphabet.

## 3. Sum every clock, including the full tail

For `k>=1`, the clocks from `k` through `5k` number `4k+1`. Their entire
contribution is at most

\[
(4k+1)(3/2)^k.                                    \tag{6}
\]

For the remaining clocks, discard only the residue restriction in an upper
bound. Under independent geometric letters with `Pr(a_j=e)=2^(-e)`,

\[
\mathbb E(4/3)^{a_j}
=\sum_{e\ge1}(2/3)^e=2,
\qquad
\mathbb E(4/3)^{A_k}=2^k.
\]

Markov's elementary exponential bound gives

\[
\begin{aligned}
\sum_{A>5k}D_{k,A}(q)
&\le3^k\Pr(A_k>5k)\\
&\le3^k(3/4)^{5k}\mathbb E(4/3)^{A_k}\\
&=\left(6(3/4)^5\right)^k
=(729/512)^k
\le(3/2)^k.                                      \tag{7}
\end{aligned}
\]

Combining (6) and (7) proves (1). The empty depth satisfies `D_0=1<=2`
directly. All terms are nonnegative, so the argument also follows by
finite clock truncations and monotone passage to the complete sum.
There is no remaining clock-tail hypothesis.

## 4. The exponential rate is attained, including along marked targets

The all-one word has

\[
\beta=(3/2)^k-1,
\qquad \omega=(3/2)^k,
\qquad \beta\equiv-1\pmod{3^k}.
\]

Thus `D_k(-1)>=(3/2)^k`. It can be realized at the actual positive odd
unit target

\[
Q_k=2\cdot3^k-1,
\qquad X_k=2^{k+1}-1,
\qquad T^k(X_k)=Q_k.
\]

For even `k`, the initial source is also a ternary unit. Therefore the
exponential factor in (1) cannot be uniformly reduced.

There are infinitely many even `k` for which these targets lie in the
constant-70 marked band. To see this, put `alpha=log_2 3` and take infinitely
many continued-fraction approximants `p/n<alpha` with
`0<n alpha-p<1/n`. Set `k=2n`, `d=2p+1`, and
`u=k alpha-2p`. For `n>=3`, `0<u<2/n=4/k<1`.
Then

\[
2^d<Q_k,
\qquad
\frac{Q_k-2^d}{2^d}<2^u-1\le u<4/k.
\]

The strict lower inequality follows also from the integrality
`3^k>2^(2p)`. Since `alpha<2` and `k>=6`,

\[
(d+1)\frac{Q_k-2^d}{2^d}
<\frac{4(k\alpha+2)}k<10<70.                       \tag{8}
\]

Also `Q_k<2^(d+1)`, so `d` is its actual dyadic octave. Hence the marked
domain itself permits density spikes of size comparable to

\[
Q_k^\gamma,\qquad \gamma=\log_3(3/2)\approx0.36907.
\]

This leaves a substantial sublinear range, but rules out a bounded marked
profile or a uniform power exponent below `gamma`.

## 5. What the estimate supplies for full capture

For any fixed `b<1/gamma=log(3)/log(3/2)`, (1) gives

\[
\max_{0\le k\le b\log_3 q}D_k(q)
\ll_b(1+\log q)q^{b\gamma}=o(q).                  \tag{9}
\]

In particular the bound covers twice the native ternary resolution,
`k<=2 log_3 q`, with exponent `2gamma<1`, without an external `L^p` input.
The numerical limiting multiplier is about `2.70951`.

For the inverse contact expansion supplied by the parallel attack, let
`C_epsilon V` be the contact payoff, which is at most `1+epsilon`, and let
`Q_epsilon` be the positive operator killed on that contact set. Then

\[
\sum_{j<L}Q_\varepsilon^j(C_\varepsilon V)(q)
\le(1+\varepsilon)\sum_{j<L}D_j(q)
\le8(1+\varepsilon)L(3/2)^L.                       \tag{10}
\]

The last inequality follows from the finite geometric sum and is valid
also at `L=0`. With

\[
L(q)=\max\left(0,
\left\lfloor\log_{3/2}q-3\log_{3/2}\log(q+2)\right\rfloor\right),
\]

the contact front is `O_epsilon(q/(log q)^2)`. If `p_L(q)` denotes the
actual stopped `V`-Doob contact probability, the exact contact identity
is `front=V(q) p_L(q)`. Consequently either of the following lower estimates, if proved,

\[
p_{L(q)}(q)\ge c/\log q,
\qquad\text{or more generally}\qquad
p_{L(q)}(q)(\log q)^2\longrightarrow\infty
\]

uniformly on moving marked units would imply the remaining marked
sublinearity of `V`, and hence of the equivalent critical profiles.

**No such lower contact estimate was proved in this arithmetic pass.**
Pointwise eventual contact at each fixed root is already available by
minimality; it does not supply the uniform onset in this last display.
Likewise (9) controls every depth in its stated range, but cannot be
silently extended to `sup_k D_k(q)` over unbounded depth.

The rigorous output is the explicit complete-clock density bound, its
formal finite arithmetic core, and the resulting contact-front estimate.
The full theorem remains contingent on the actual moving-root capture
estimate, which is retained as an explicit open step.
