# Proof program: from averaged cusp decay to an all-depth theorem

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Status:** research program; every unproved step is labeled

## 1. Exact boundary after this packet

The packet separates the problem into the following implication graph:

```text
D-9301  fixed Z_2 measure
   |
   v
L-9301  moving-character identity
   |
   +--------------------------+
   |                          |
   v                          v
L-9303 phase energy       D-9302 adelic natural extension
   |                          |
   v                          v
C-9301 / energy target    Q-9301 integer-section intersection
   |
   v
T-9301 polynomial-window reduction
   ^
   |
L-9302 weighted shell tail  <--- frequency block mean (branch-qualified)

frequency block mean + depth block mean
   |
   v
T-9302 full weighted EQ on density-one depths
```

The all-depth EQ problem is now concentrated in one sentence:

> Exclude a polynomial-height rational character whose phase energy stays `O(log K)` at infinitely many depths.

The direct M1 problem is concentrated in a different sentence:

> Determine whether the symbolic stable leaf `Phi(Omega)` meets the ordinary-integer section `I` outside the two trivial endpoints.

These are related by duality but should not be conflated. EQ can hold while one exceptional M1 point survives.

## 2. Offense A: exceptional-frequency amplification

### Target inverse lemma

Prove a statement of the following form.

> **Exceptional-frequency amplification, tentative.** There are constants `u,v>0` such that if
> \[
> 1\le\theta\le K^A,
> \qquad
> F_K(\theta)\ge K^{-u},
> \]
> then there is an interval `I` of at least `K^v` consecutive numerators near a controlled affine image of `theta` for which
> \[
> \frac1{|I|}\sum_{h\in I}F_K(h)
> \ge K^{-O(u)}.
> \]

If `I` contains a full `81^r` block with `r` proportional to `log K`, the frequency block mean gives exponential decay in `r`, contradicting the lower bound for suitable constants.

### Why this might be true

By `L-9303`, a large coefficient forces

\[
\sum_t x_{K,t}(\theta)^2=O(\log K).
\]

Most levels therefore have very small phase distance. A small perturbation of the numerator preserves a phase whenever the exact modular increment stays inside its available margin. The obstacle is that the sensitivity changes with `t`; ordinary Euclidean closeness of numerators is not enough.

The desired proof should build an interval through the common carry coordinates rather than through a naive Lipschitz estimate.

### Proposed robustness-or-loss dichotomy

For each level, record both

\[
x_{K,t}(\theta)
\]

and its distance from the boundary of a chosen degeneracy window. Then prove:

1. either at least `c log K` levels lie in boundary annuli, in which case their moderate cosine losses already prove polynomial decay;
2. or a large collection of degenerate levels has robust margins, and their exact congruences persist for a structured block of nearby numerators.

The second case should create forbidden block mass.

### Main danger

The intersection of the stability congruences may be one thin arithmetic progression rather than a consecutive interval. A successful lemma may therefore need to apply the issue-#4 block mean after a multiplicative change of variable or after grouping several adjacent scales. No such transference is presently proved.

## 3. Offense B: S-unit carry height

For every phase, `C-9301` gives the exact equation

\[
17\theta
=81^{t+1}s_t+64^{K-t}m_t. \tag{1}
\]

Adjacent signed representatives satisfy

\[
s_t\equiv81s_{t+1}\pmod{64^{K-t-1}}. \tag{2}
\]

A low-energy exception has many `s_t` small relative to `64^(K-t)`. The proposed arithmetic strategy is:

1. choose a logarithmic set of well-separated levels;
2. eliminate `theta` between their equations `(1)`;
3. obtain a family of exact four-term `{2,3}`-unit relations;
4. prove a height gap: unless the relations fall into one of finitely many degenerate templates, at least one normalized `s_t` is macroscopic;
5. classify the degenerate templates and show that a polynomially bounded positive `theta` cannot follow one for all selected levels.

### Candidate specialized height lemma

A useful statement would be:

> Given `L` separated levels and a common nonzero integer `theta`, the equations `(1)` cannot all have
> \[
> |s_t|\le64^{K-t}/L^C
> \]
> unless `theta` is divisible by a power of `81` or `64` whose size is exponential in `L`.

Since `theta <= K^A`, an exponential divisibility conclusion with `L` proportional to `log K` would close the target.

### What must not happen

Invoking the general phrase “S-unit theorem” is not enough. Classical finiteness theorems often provide no effective uniform bound in the moving exponents `K,t`. The packet needs a specialized, quantitative argument using the two-term structure and the exact gcd facts

\[
\gcd(64,81)=1,
\qquad
17\nmid64\cdot81.
\]

## 4. Offense C: an adelic shrinking-target theorem

`D-9302` places the coding in

\[
\mathbb X_S
=(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)/\Delta\mathbb Z[1/6]
\]

under the hyperbolic automorphism `alpha` induced by `81/64`.

On the dual side, `L-9301` samples one fixed measure along rational characters with:

- small real height `theta/64^K`;
- large 2-adic height;
- correlated 3-adic rotation through powers of `81`.

### Desired dynamical theorem

Prove uniform nonconcentration for low-height rational characters entering a shrinking neighborhood of the annihilator of the digit difference at too many times.

A deliberately concrete formulation is:

> For some `A,c>0`, every nonzero rational character with numerator at most `K^A` spends total squared distance at least `c log K` from the annihilator over its first `K` inverse iterates.

This is exactly the energy version of `C-9301`.

### Why generic rigidity does not automatically apply

The coded measure lies on a symbolic stable leaf with third coordinate fixed at zero. A hypothetical integer witness is one orbit, not a positive-entropy invariant measure. Standard measure-rigidity, mixing, and real self-similar Fourier-decay theorems therefore remain analogies until their hypotheses are reconstructed in this S-arithmetic setting with constants uniform in the cusp height.

### Product-formula hope

The action expands at the real and 2-adic places and contracts at the 3-adic place:

\[
|\beta|_\infty\,|\beta|_2\,|\beta|_3=1.
\]

A character that is simultaneously too resonant in the 2-adic phase and too low in real height may be forced to acquire 3-adic complexity. Turning that conservation law into a quantitative return bound is the conceptual reason to retain all three places.

## 5. Direct offense on M1

The exact open intersection is

\[
\Phi(\Omega)\cap\mathcal I.
\]

Two opposite programs are legitimate.

### Constructive program

Seek a finitely generated but nonautomatic itinerary whose solenoid point lies in the integer section. Any candidate must provide:

1. an exact infinite digit rule;
2. proof that its 2-adic sum is one ordinary positive integer;
3. proof of the required chart congruence;
4. an independent reconstruction of the induced-to-Collatz translation.

The branch literature audit already warns that compatible finite prefixes can converge only to a 2-adic ghost. The third-coordinate section test in `D-9302` makes that failure visible but does not prevent it.

### Rigidity program

Assume a nontrivial integer intersection and form empirical measures of its `alpha`-orbit in `X_S`. Determine whether the shared symbolic itinerary forces:

- positive entropy at one expanding place;
- simultaneous invariance under a second multiplicatively independent action;
- or a forbidden concentration on a rational subsolenoid.

None of these consequences is currently proved. Producing the invariant object is the prerequisite before measure rigidity can engage.

## 6. Minimal exact computation

Computation is limited to lemma discovery and falsification.

The first probe should scan only

\[
K\le80,
\qquad
1\le\theta\le K^2,
\]

using exact modular arithmetic. For fixed rational thresholds `delta`, record:

- the minimum number of `delta`-scattered levels;
- the minimizing numerator;
- the complete signed carry path for the worst cases.

The count is exact; no floating-point Fourier magnitude is needed. The purposes are:

1. refute an overstrong fixed-threshold claim quickly;
2. identify recurrent carry templates for a proposed height lemma;
3. decide whether fixed-threshold scattering or quadratic energy is the more stable target.

Even perfect behavior through depth `80` is only `EMPIRICAL`. The output must never be cited as evidence that all-depth EQ holds.

## 7. Falsification criteria

This program should be revised or abandoned if any of the following occurs:

1. an exact polynomial-height family has bounded phase energy along infinitely many symbolic depths;
2. a single exceptional frequency can remain isolated, defeating every plausible amplification lemma while respecting the block mean;
3. the issue-#4 block means fail the arbitrary-consecutive-block quantifiers required by `L-9302` or `T-9302`;
4. the stationary character identity uses a different digit order from the live subsystem;
5. a direct nontrivial integer-section point is constructed, in which case the priority shifts immediately from EQ to adversarial verification of that candidate.

## 8. Best next theorem

The highest-leverage next result is not a broad mixing theorem. It is the following finite, exact inverse statement:

> **Low-energy inverse theorem.** Every polynomial-height pair `(K,theta)` with phase energy `O(log K)` admits a bounded-complexity carry description, and every such description either forces `theta=0`, reduces by an exact power of `64`, or amplifies to a full `81^r` block of comparably low energy.

The first two outcomes are harmless; the third contradicts the frequency block mean. Proving this theorem would close `C-9301` in an energy form and therefore close all-depth EQ through `T-9301`.
