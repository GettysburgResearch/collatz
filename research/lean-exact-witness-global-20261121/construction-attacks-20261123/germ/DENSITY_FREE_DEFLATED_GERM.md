# A quantitative arithmetic-germ criterion without a density assumption

23 November 2026. **SOURCE-QUALIFIED written theorem.** The analytic
consumer uses Chambert-Loir--Nous, *Potentiel et rationalite*,
arXiv:2305.17210v2, Theorem 4.3, with its full local-realization and
integral-model hypotheses. The finite capacity certificate is checked in
Lean. **The required germ is not constructed for an arbitrary source;
full Collatz and the original residue-512 implication remain OPEN.**

This is an alternative to the limiting-density consumer in PR178 at
`398b3a04da071e96362005792417bd5cf8cc6497`,
`research/literature-push-20261123/rigidity/GENERAL_DENSITY_JET.md`.
It replaces the density assumption by explicit stronger analytic bounds
on a deflated germ. It does not claim that the earlier qualitative Jet
hypothesis alone implies the new bounds.

## DG1. The actual source, both germs, and unconditional radii

Use the shortcut map `T(x)=x/2` on even inputs and `(3x+1)/2` on odd
inputs. Fix a positive ordinary integer `n`, and set

\[
x_k=T^k(n),\qquad e_k=x_k\bmod2,\qquad
p_k=\sum_{i<k}e_i,
\]
\[
B_n(z)=\sum_{k\ge0} e_k3^{-p_{k+1}}z^k.
\]

An odd step is at most doubling and an even step halves exactly.
Consequently

\[
1\le x_k\le n\,2^{2p_k-k},\qquad
p_k\ge\frac{k-\log_2 n}{2}.                 \tag{1}
\]

This bound was already used in the frozen PR178 finite-filter note;
it is an actual-positive-source bound, not a statistical density claim.
Together with `p_(k+1)<=k+1`, it gives convergence of `B_n` in

\[
|z|<\sqrt3,\qquad |z|_3<1/3,\qquad |z|_2<1.
                                                        \tag{2}
\]

At every other finite place its coefficients are integral, so its radius
is at least one. No limit of `p_k/k` is used. These are guaranteed lower
bounds on radii, not claims of exact radii.

The binary affine identity gives `B_n(2)=-n`. Define the **literal**
binary germs

\[
J_n(t)=B_n(2+t),\qquad
K_n(t)=(1+4t+t^2)J_n(t).                         \tag{3}
\]

Thus `K_n` is the germ at two of

\[
F_n(z)=(z^2-3)B_n(z).                            \tag{4}
\]

Multiplying by this polynomial preserves all convergence lower bounds
in (2). In particular `F_n` is one binary analytic function realizing
both its germ at zero and the full actual germ `K_n` at two. An arbitrary
rational series with constant term `-n` is not a substitute for (3).

## DG2. A strict two-center capacity margin

The centers are zero and two on the projective line over the rationals.
At two, use the single binary unit disc containing both centers. Its
diagonal Green constants are zero and its off-diagonal Green constant is

\[
L=\log2.
\]

At three, take disjoint discs of radii approaching `1/3` at zero and
`1` at two from below. At infinity take disjoint discs of radii
approaching `4/3` and `2/3`. Slightly shrinking the discs makes their
closures disjoint and keeps all local functions within their stated
domains. At primes other than two and three use the two disjoint unit
residue discs. Their diagonal and off-diagonal contributions are zero.

If the germ `K_n` has complex radius at least `2/3` and ternary radius
at least one, the resulting global potential matrices approach

\[
G_*=
\begin{pmatrix}
\log(4/9)&\log2\\
\log2&\log(2/3)
\end{pmatrix}.                                  \tag{5}
\]

The explicit mixed strategy `(2/5,3/5)` has the two column payoffs

\[
\frac15\log\frac{128}{81}>0,
\qquad
\frac15\log\frac{32}{27}>0.                      \tag{6}
\]

Hence every sufficiently small perturbation caused by shrinking the
discs still has strictly positive game value. The finite certificate is
the strict inequalities `128>81` and `32>27`, not an asserted numerical
capacity approximation. `GermCapacity.lean` checks the real logarithmic
payoffs and their positive lower bound against every mixed column.

## DG3. The radius threshold can be lowered to one half

Suppose instead that the complex radius of `K_n` is merely greater
than `1/2`. Choose

\[
1/2<b<\min(1,R_\infty(K_n)),\qquad a<2-b
\]

with `a` sufficiently close to `2-b`. Then `a<3/2<sqrt3`, so the
original germ realizes the complex disc at zero. The disc at two of
radius `b` is realized by `K_n`. Before the arbitrarily small shrinkage
at three, the global matrix approaches

\[
\begin{pmatrix}-A&L\\L&-B\end{pmatrix},
\qquad A=\log\frac3{2-b},\quad B=\log\frac1b,
\quad L=\log2.                                  \tag{7}
\]

For `1/2<b<1`,

\[
AB<(\log2)^2.                                    \tag{8}
\]

Here is a direct proof of the strict inequality. Let
`f(b)=log(3/(2-b))*log(1/b)`. It equals `(log2)^2` at `b=1/2`, and

\[
f'(b)=\frac{\log(1/b)}{2-b}
      -\frac{\log(3/(2-b))}{b}<0.
\]

Indeed `b log(1/b) <= b log2 < log2`, whereas
`(2-b)log(3/(2-b)) > log2` on this interval. The mean value theorem
proves (8). The mixed strategy with first coordinate
`(L+B)/(2L+A+B)` has constant payoff

\[
\frac{L^2-AB}{2L+A+B}>0.                          \tag{9}
\]

Continuity preserves the strict margin after taking `a<2-b` and the
ternary radii strictly below their bounds. This calculus step and the
analytic domain construction are written mathematics, not claimed as
Lean formalizations.

## DG4. The full arithmetic hypotheses and the rationality conclusion

Assume

1. every coefficient of the actual binary germ `K_n` lies in
   `Z[1/3]`;
2. `R_infinity(K_n)>1/2`;
3. `R_3(K_n)>=1`.

The two formal germs are defined over the rationals. Their graphs have
an integral formal model on the projective line over `Z[1/6]` because
both coefficient rings lie there. At primes outside two and three,
the chosen domains are precisely the required residue discs. At two
the same actual analytic function `F_n` realizes both germs. At three
and infinity the components are disjoint, and the separate specified
germs give one meromorphic function on their union. All local analytic
and integral-model hypotheses of Sections 4.1--4.2 of the primary
theorem are therefore present.

DG3 gives strictly positive potential-game value. Theorem 4.3 of
Chambert-Loir--Nous supplies a single rational function having the two
formal germs. Its germ at zero is `F_n`, so `F_n` and hence `B_n` are
rational functions.

The retained rational-series consumer gives eventual ordinary
periodicity. Its elementary mechanism can also be recalled directly.
A rational `B_n` supplies a fixed linear recurrence for the coefficients
`e_k 3^(-p_(k+1))`. After multiplying a recurrence beginning at `k` by
`3^p_k`, the last parity bit is uniquely determined by the preceding
finitely many parity bits: its nonzero leading-coefficient contribution
is either zero or `q_d 3^(-s-1)`, two distinct values. The tail parity
sequence is therefore a deterministic finite-state sequence and is
eventually periodic. For an actual integer source with a repeated
tail word `(P,Q,C)`, all powers `Q^j` divide the fixed integer
`(Q-P)x-C`. This integer is zero, so the actual states are periodic too.
This recalled consumer is credited, not claimed as new here.

## DG5. The criterion reaches the standard cycle

The polynomial `D(t)=1+4t+t^2` has constant coefficient one. Its formal
inverse has integer coefficients, by the recurrence

\[
b_0=1,\quad b_1=-4,\quad b_{j+2}=-4b_{j+1}-b_j.
\]

Consequently `K_n in Z[1/3][[t]]` implies

\[
J_n=K_n/D\in\mathbb Z[1/3][[t]].                  \tag{10}
\]

Apply the actual-cycle obstruction in PR182 at
`e4367dd2c4406c1041e66d82dfba822908747fa3`,
`research/profound-round6-20261123/RATIONAL_SELECTION.md`, R6-SEL-4:
among eventually periodic positive ordinary sources, (10) excludes
every nonstandard cycle. Therefore the source reaches one.

Conversely, suppose an actual prefix `a` of length `tau` and odd count
`s` reaches one. Its complete chronological carry polynomial gives

\[
B_n(z)=\frac{C_a(z)}{3^s}
       +\frac{z^\tau}{3^s(3-z^2)}.
\]

Hence

\[
3^s K_n(t)
=(1+4t+t^2)C_a(2+t)-(2+t)^\tau\in\mathbb Z[t].    \tag{11}
\]

Thus `K_n` is a polynomial with one common ternary denominator and
infinite convergence radius at every place. The standard-cycle
deflation and this prefix identity were already explicit in the peer
packet; the new step is the density-free fixed-radius consumer.

**Theorem DG5.** For every fixed positive ordinary integer `n`,

\[
\boxed{
n\text{ reaches }1
\quad\Longleftrightarrow\quad
\begin{cases}
K_n\in\mathbb Z[1/3][[t]],\\
R_\infty(K_n)>1/2,\\
R_3(K_n)\ge1,
\end{cases}
}                                                \tag{12}
\]

with `K_n` the complete actual binary germ (3). No limiting-density
hypothesis appears. The forward direction gives a polynomial; the
reverse direction uses the external rationality theorem and the frozen
actual-cycle obstruction with the explicit boundaries above.

## DG6. What this does and does not construct

The older J3 condition plus a density limit and the new condition (12)
are different analytic packages. The new package makes its radius
costs explicit and covers all convergent sources; it does not infer
those costs from the older qualitative germ assumptions. In particular
deflation is not asserted to improve an unknown germ's convergence
radius or denominator support automatically.

The remaining task is to construct the **actual** rational coefficients
and establish these two bounds for arbitrary sources. Proving the
constant value `K_n(0)=-n`, fitting finitely many coefficients, or
choosing a separate polynomial for each tested prefix does not do so.
The finite-filter obstruction at the frozen PR178 concerns coefficient
denominators at zero; it is preserved and does not supply the second
arithmetic germ used here.

## Sources and evidence scope

- Chambert-Loir--Nous, *Potentiel et rationalite*,
  <https://arxiv.org/pdf/2305.17210>, v2 (31 August 2026),
  Sections 4.1--4.3 and the game definition in Section 2.7:
  primary text read directly. The general theorem is an external
  source-qualified input, not a new proof or Lean axiom here.
- PR178 at `398b3a04da071e96362005792417bd5cf8cc6497`,
  `GENERAL_DENSITY_JET.md` and `FINITE_FILTER_TEST.md`: complete
  relevant notes read. The unconditional positive-source inequality
  and the earlier multipoint interface are credited.
- PR182 at `e4367dd2c4406c1041e66d82dfba822908747fa3`,
  `RATIONAL_SELECTION.md`: complete note read; R6-SEL-4 and the
  actual-prefix deflation formula are retained with their written
  arithmetic scope.
- Bell--Gunn--Nguyen--Saunders, arXiv:2206.00862v1, and
  Breuer--Simon, *Natural boundaries and spectral theory*: primary
  texts were opened for alternative-route orientation. Their
  hypotheses were not established here and neither theorem is used
  in DG5.

The finite Lean module checks the explicit strict game strategy and
the integer inverse-coefficient recurrence. It does not formalize
adelic analytic geometry, infinite Taylor translation, the variable
radius optimization, or the universal germ construction.
