# An actual-orbit compact joining, and the zero-entropy boundary

**Status, 22 November 2026.** Written proofs of a compact joining obtained
from one fixed hypothetical escaping ordinary source, an explicit ergodic
zero-entropy control for the same coupled map, and a full-denominator
bound on residence near a negative rational cycle. No positive global
closing estimate, entropy lower bound, or Collatz proof was obtained.
These arguments are not claimed as Lean formalizations.

The purpose was to construct the invariant probability required by a
rigidity argument rather than assuming that a single ordinary source
already produces a suitable random law. The construction succeeds, but
the resulting exact constraints still admit zero-entropy systems. The
control below is not an ordinary Collatz counterexample.

## 1. A compact law produced by one fixed escaping source

Put

\[
\alpha=\log_2 3,\qquad
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

Assume that one positive odd ternary unit `n_0` has an escaping orbit
`n_j=U^j(n_0)`. Every term is a positive odd ternary unit and
`n_j -> infinity`. No ensemble of different initial sources is used.
Set

\[
a_j=v_2(3n_j+1),\quad A_N=\sum_{j<N}a_j,\quad
\epsilon_j=\log_2\left(1+\frac1{3n_j}\right).
\]

The exact real identity is

\[
\log_2n_N=\log_2n_0+N\alpha-A_N+\sum_{j<N}\epsilon_j.
\tag{1}
\]

Since `n_j -> infinity`, `epsilon_j -> 0`. Cesaro averaging and
`log_2 n_N >= 0` therefore give

\[
\limsup_{N\to\infty}\frac{A_N}{N}\le\alpha.
\tag{2}
\]

Only the vanishing **mean** correction is used. No summability of
`1/n_j`, predecessor-population statement, or canonical Green input is
needed.

Consider the compact metrizable space

\[
\Omega=(1+2\mathbb Z_2)\times\mathbb Z_3^\times
                 \times\mathbb T,
\qquad \mathbb T=\mathbb R/\mathbb Z.
\]

For `x != -1/3` put `a(x)=v_2(3x+1)`, a positive integer, and define

\[
S(x,z,\theta)=
\left(\frac{3x+1}{2^{a(x)}},
      \frac{3z+1}{2^{a(x)}},\theta+\alpha\right).
\tag{3}
\]

The first output is odd and the second a ternary unit. On every clopen
set where `a(x)` has a fixed finite value, this map is continuous. Its
only possible discontinuities lie over the pole `x=-1/3`. Define `S`
arbitrarily on that pole; it will have measure zero.

Retain the actual arithmetic embeddings and phase:

\[
y_j=(n_j,n_j,\log_2n_j\bmod1),\qquad
\mu_N=\frac1N\sum_{j<N}\delta_{y_j}.
\tag{4}
\]

### Theorem A

Every weak subsequential limit `mu` of `(mu_N)` is an `S`-invariant
probability measure with

\[
\mu\{x=-1/3\}=0,\qquad
\int a(x)\,d\mu\le\alpha,
\qquad (\operatorname{pr}_{\mathbb T})_*\mu=m_{\mathbb T}.
\tag{5}
\]

**Proof.** Compactness gives a weak subsequential limit. For every
integer `M>=1`,

\[
C_M=\{x:3x+1\equiv0\pmod{2^M}\}
\]

is clopen, contains the pole, and on the actual orbit is the event
`a_j>=M`. Equations (2) and Markov's inequality give

\[
\mu(C_M)=\lim\mu_N(C_M)\le\frac\alpha M.
\tag{6}
\]

The `C_M` decrease to the pole, which proves zero pole mass. The
bounded continuous function `min(a(x),M)`, defined as `M` at the pole,
has integral at most `alpha` by (2). Monotone convergence proves the
middle assertion of (5). This is a bound on the first moment of the
limit; uniform integrability of the untruncated empirical gaps is not
asserted.

The first two coordinates of `S y_j` and `y_(j+1)` agree exactly. Their
circle coordinates differ by `epsilon_j mod1`, which tends to zero.
For every continuous `f` on `Omega`, uniform continuity and telescoping
therefore give

\[
\frac1N\sum_{j<N}\bigl(f(Sy_j)-f(y_j)\bigr)\longrightarrow0.
\tag{7}
\]

To pass to the weak limit, restrict first to `Omega minus C_M`. There
`f o S` is continuous on finitely many clopen branches. The omitted
part is bounded in absolute value by a constant times `mu_N(C_M)`,
whose limiting upper bound is `alpha/M`. Letting `M` tend to infinity
proves `S_*mu=mu` without assuming continuity at the pole.

The circle marginal is invariant under the irrational rotation by
`alpha`. Irrationality follows from `2^u != 3^v` for positive integers
`u,v`. Irrational rotations have a unique invariant probability,
namely Haar measure. This proves the last assertion. Equivalently,
every nonzero Fourier coefficient is killed by invariance. ∎

Thus a fixed source really does produce a joined binary, ternary and
leading-phase law with a controlled valuation moment. What is not
retained automatically is a restriction excluding invariant laws that
live entirely on nonordinary compact points.

## 2. A correlated ergodic zero-entropy control

The constraints in Theorem A admit a particularly explicit aperiodic
control. It couples all three coordinates to **one** irrational rotation;
it does not assume that the arithmetic and phase coordinates are
independent.

Let

\[
\rho=\alpha/3,\qquad R\beta=\beta+\rho\pmod1.
\]

For `beta in [0,1)` and every integer `i`, set

\[
a_i(\beta)=1+\lfloor\beta+(i+1)\rho\rfloor
                  -\lfloor\beta+i\rho\rfloor\in\{1,2\}.
\tag{8}
\]

The code is shift covariant: `a_i(R beta)=a_(i+1)(beta)`. Its
frequency of the value two is `rho`; this follows directly by
telescoping the floor differences. Define

\[
A_k(\beta)=\sum_{i=0}^{k-1}a_i(\beta),\quad A_0=0,
\qquad B_k(\beta)=\sum_{i=-k}^{-1}a_i(\beta).
\]

The two convergent local series are

\[
x(\beta)=-\sum_{k=0}^{\infty}\frac{2^{A_k(\beta)}}{3^{k+1}}
                    \quad\text{in }\mathbb Z_2,
\qquad
z(\beta)=\sum_{k=1}^{\infty}\frac{3^{k-1}}{2^{B_k(\beta)}}
                    \quad\text{in }\mathbb Z_3.
\tag{9}
\]

Their tails converge uniformly in the respective local metrics because
`A_k>=k` and the ternary valuation of the second summand is `k-1`.
The first series is odd. The second is a ternary unit, since its first
term is a unit and all subsequent terms are divisible by three.

Shifting the series gives the exact identities

\[
3x(\beta)+1=2^{a_0(\beta)}x(R\beta),\qquad
z(R\beta)=\frac{3z(\beta)+1}{2^{a_0(\beta)}}.
\tag{10}
\]

Because `x(R beta)` is odd, the binary valuation in (10) is exactly
`a_0(beta)`. In particular the pole never occurs. Finally put

\[
\Phi(\beta)=(x(\beta),z(\beta),3\beta\bmod1).
\tag{11}
\]

Since `3 rho=alpha`, equations (3), (10) and (11) give

\[
S\Phi(\beta)=\Phi(R\beta).
\tag{12}
\]

Push circle Haar measure through `Phi`, obtaining `mu_*`.

### Theorem B

The measure `mu_*` is invariant and ergodic for the exact compact map
`S`, has zero measure-theoretic entropy, and satisfies

\[
(\operatorname{pr}_{\mathbb T})_*\mu_*=m_{\mathbb T},
\qquad
\int a\,d\mu_*=1+\frac\alpha3<\alpha.
\tag{13}
\]

It is nonatomic and its arithmetic gap itineraries are aperiodic.

**Proof.** It is a measurable factor of the irrational rotation `R`,
so it is invariant, ergodic and has entropy zero. Multiplication by
three preserves Haar measure, giving the circle marginal. The mean
gap is `1+rho` by (8). The strict inequality follows from
`alpha>3/2`, equivalently `9>8`.

Haar circle marginal implies that the whole measure has no atoms. More
specifically, the future gap code determines `beta`: for distinct
circle points, irrational rotation eventually enters an open part of
the symmetric difference of the two coding intervals. Their future
codes then differ. The exact binary itinerary in (10) determines its
future code, so `x(beta)` is injective. Consequently the countable set
of positive ordinary integers in the binary coordinate has `mu_*`
measure zero. The irrational frequency `rho` of gap two rules out
eventual periodicity of the gap itinerary. ∎

This is a control for a proposed application of rigidity, not a claim
that any positive integer follows the code (8). In particular, a weak
limit of ordinary empirical measures can be supported off the
countable set of ordinary points. That fact cannot be excluded by
pointwise membership of every term before taking the limit.

The control is stronger than a freely chosen biased binary measure:
the ternary coordinate is transported by the same actual valuation,
the real phase is correlated with the gap process, the resulting law
is ergodic, and the valuation moment is strictly on the side required
by an escaping positive orbit. Yet its entropy is zero.

### Binary-run growth also coexists with this zero entropy

Let `r_m(x)` count the nonempty one-runs in the first `m` binary digits
of `x`, read from the least significant end. If a 2-adic expansion has
only finitely many one-runs in total, it is eventually all zeros or
eventually all ones. It is therefore an ordinary integer, possibly
negative. The injectivity of `beta -> x(beta)` shows that this countable
set has zero mass under the binary marginal of `mu_*`.

Consequently, for every fixed natural `s`,

\[
\mu_*\{r_m(x)>s\}\longrightarrow1\qquad(m\to\infty).
\tag{13a}
\]

Each event in (13a) is a finite binary cylinder. If actual positive
orbit occupation measures had `mu_*` as a weak subsequential limit,
their whole-integer run counts would therefore exceed each fixed `s`
with limiting frequency one along that subsequence: first fix `m`,
pass to the weak limit, and only then increase `m`.

Thus even strong run-count growth at the compact level does not imply
positive metric entropy. This observation does not construct such an
ordinary orbit, bound its canonical Dirichlet energy, or identify that
energy with the control measure.

## 3. Full-denominator residence near a negative rational cycle

Let `w=(a_0,...,a_(s-1))` be an actual negative rational odd cycle word,
with total binary clock `A` and affine composition

\[
F_w(X)=\frac{3^sX+C}{2^A},\qquad C>0.
\]

Assume all its rational cycle states are odd in `Z_2`, and their exact
valuations are the displayed positive gaps. A negative fixed point
requires

\[
D=3^s-2^A>0,\qquad c=-C/D.
\tag{14}
\]

The integer `D` is odd. The complete denominator is retained; no
individual factor test is substituted for it. For a positive odd
ordinary `n`, the following equivalence holds for every `r>=0`:

\[
\boxed{n\text{ follows }w^r\text{ with the same exact odd gaps}
\iff v_2(Dn+C)\ge rA+1.}
\tag{15}
\]

**Proof.** The inverse-branch cylinder of an odd word with total clock
`K` fixes its source modulo `2^(K+1)`, including the final odd digit.
This can also be checked directly: if two odd sources follow the word,
their endpoint difference is `3^ell/2^K` times their source difference,
so the difference of the odd endpoints is even. Conversely, a source
change divisible by `2^(K+1)` changes every intermediate odd endpoint
by an even integral amount, retaining every exact valuation. For a
positive ordinary source all actual iterates remain positive.

Apply this to the rational cycle source `c` and the word `w^r`.
Since `D` is odd, `n-c` is divisible by `2^(rA+1)` in `Z_2` exactly
when the ordinary positive integer `Dn+C` is. This proves (15). ∎

Consequently any such residence satisfies

\[
rA+1\le\log_2(Dn+C).
\tag{16}
\]

On a fixed positive orbit, the elementary inequality
`U(n)+1 <= (3/2)(n+1)` gives

\[
n_j+1\le(3/2)^j(n_0+1).
\]

Thus a residence starting at odd clock `j` has length `rs` bounded by

\[
rs\le\frac{s}{A}
 \left(j\log_2(3/2)+
       \log_2\bigl((D+C)(n_0+1)\bigr)-1\right).
\tag{17}
\]

This rules out an infinite residence at that negative rational cycle
from one positive source. It does not give a uniform occupation bound
over repeated returns: a rare interruption can replenish a large binary
valuation, and no bound on that replenishment was proved.

### An actual positive finite-shadow control

For the negative odd cycle `-5 -> -7 -> -5`, the word is `[1,2]`,
`s=2`, `A=3`, `C=5`, and `D=1`. For each odd `R>=1`, take the different
positive source

\[
n_R=2^{3R+1}-5.
\]

The oddness of `R` ensures `3` does not divide `n_R`, so every state
used in this control lies in the same ternary-unit domain `Omega`.

It follows `R` complete repetitions with

\[
U^{2r}(n_R)=2\,8^{R-r}9^r-5\quad(0\le r\le R),
\]

\[
U^{2r+1}(n_R)=3\,8^{R-r}9^r-7\quad(0\le r<R).
\tag{18}
\]

The formulas show positivity, oddness and the exact valuations directly.
On the middle of the block, both local coordinates approach `-5` or
`-7`: binary closeness grows with `R-r`, and ternary closeness with
`r`. The real phases approach `2r alpha` and `(2r+1)alpha`, respectively.
Irrational rotation averaging then shows that the empirical measures
of these positive finite blocks converge to

\[
\tfrac12\bigl(\delta_{(-5,-5)}+\delta_{(-7,-7)}\bigr)
                   \times m_{\mathbb T}.
\tag{19}
\]

This supplies a second zero-entropy control, now approached by actual
positive ordinary trajectory segments. Its starting source changes
with `R`. It does not construct one ordinary escaping orbit.

## 4. What the literature does and does not supply here

Einsiedler--Lindenstrauss, *Rigidity properties for commuting automorphisms
on tori and solenoids*, Theorems 1.2--1.3, concern higher-rank commuting
algebraic actions, with the stated irreducibility/factor hypotheses.
Positive entropy is what forces algebraic translation invariance; the
zero-entropy alternative remains. Our `S` is one selected-branch map,
not such a commuting action. Theorem B additionally shows that positive
entropy cannot be inferred just from the coupled invariance, Haar phase
and drift bound proved in Theorem A.

Primary source: [arXiv:2101.11120v1, Introduction and main results](https://arxiv.org/html/2101.11120v1).

Frantzikinakis, *The Structure of Strongly Stationary Systems*,
Theorems 6.6 and 6.9, separates Bernoulli and pro-nilsystem structure
after strong stationarity has been established. It does not assert that
the process constructed from one ordinary Collatz orbit is strongly
stationary. A rotation factor like Theorem B is a genuine zero-entropy
possibility, rather than an exception the theorem removes.

Primary source: [arXiv:math/0403453v1](https://arxiv.org/html/math/0403453v1).

Dubickas's Theorem 5 gives a lower bound greater than `1.70951129 L`
for the number of distinct length-`L` shortcut parity blocks in any
escaping positive orbit, for all sufficiently large `L`. This is a
factor-complexity bound, not a positive metric-entropy theorem for each
occupation limit. Rare exceptional blocks can increase the global word
complexity while having zero limiting frequency. It therefore does not
remove Theorem B as a possible occupation-limit obstruction.

Primary source: [Dubickas, Glasgow Math. J. 51 (2009), Theorem 5](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf).

The first unsupported step of the attempted completion is now explicit:
prove an additional arithmetic restriction on the occupation laws of
**one fixed ordinary source** that excludes controls of this kind, or
construct a genuine higher-rank invariance with an applicable entropy
bound. Neither follows from the contiguous residence estimate (17).
Even zero occupation of all negative periodic strata would leave the
aperiodic rotation control in Theorem B.

## Scope and provenance

Theorem A uses only exact ordinary iteration, compactness, a first-moment
bound and irrational circle rotation. Theorems B and (15)--(19) are
explicit constructions and arithmetic proofs. They import no canonical
harmonic or predecessor-density assumptions. No new Lean declaration or
empirical computation is claimed.

The fresh repository comparisons were PR177
`431d858d1ac92e88f4a58f6610c0d67733dc7242`, especially
`TERMINAL_DIRICHLET_RUN_MASS.md`; PR182
`9dacd610ba7735e89e2e29e4ab01795983317980`, especially
`PROFINITE_LABEL_RIGIDITY.md`, `INVARIANT_CORRELATION.md` and
`CANONICAL_ESCAPE_LABEL.md`; and the literature packet in PR186
`1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493`. Those references identify
the active interface and the previously documented limitations. The
constructed compact joining does not prove a bound on the canonical
run-weighted terminal energy or exclude additional positive cycles.
