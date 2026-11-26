# Three-hour reevaluation: results and the remaining proof obligations

**Collatz remains open.** This is the final research handoff from the sprint
begun at 18:50 UTC on 26 November 2026. Nine GPT-6.2 Astra workers, in three
successive teams, attacked ordinary arithmetic, positive rational cycles,
inverse dynamics, operator spectra and first-passage observables. The root
agent reconstructed the principal arguments, assigned cross-reviews and
ran the integrated finite and Lean checks. This is a research proposal with
explicit evidence boundaries, not a completed Lean proof of Collatz.

The strongest fully written operator result is the exact biased inverse
pressure. The strongest new restrictions on one supplied ordinary trajectory
concern common factors and squareclasses at complete reset boundaries. The
most concrete remaining escape target is now a sequence of finite positive
rational exit weights. None of these supplies the missing universal bound.

[First-wave overview](README.md) · [second-wave results](SECOND_WAVE.md) ·
[final root review](../../reports/unconventional-20261126/ROOT_THIRD_REVIEW.md) ·
[late repository intake](../../reports/unconventional-20261126/LATE_INTAKE.md).

## 1. Exact pressure is established in the written proposal

For \(0<p<1\), let \(B_p\) act on \(C(\mathbb Z_3)\) with the supremum norm as the legal ternary inverse operator with exponent weights
\(3p(1-p)^{e-1}\), with the spaces and normalization fixed in the linked
proof. Its radius is

\[
                         r(B_p)=\max\{1,3p\}.
\]

For the classical Bergman coefficient transfer attached to the shortcut
map, on the quotient by degrees 0, 1 and 2, this gives

\[
                         r(\mathcal T)=\sqrt{20}/3.
\]

The full and Fredholm essential spectra are the corresponding disk on each
ordinary component. The proof retains endpoint legality and uniformity;
an average over residues alone would only give the lower bound. The upper
bound uses stationary path measures, conditional entropy, injective
fixed-clock carries, and an entropy increment on finite cyclic groups. Two
independent reconstructions and the root review found no gap in that written
argument. Its analytic proof is not formalized in Lean.

This resolves the specified radius question in Béhani's paper within this
proposal; no priority claim over unexamined subsequent literature is made.
The same componentwise spectral data occur in the known basin of 1, so they
do not count components or eliminate escape.

[Exact pressure proof](operator/EXACT_BERGMAN_PRESSURE.md) ·
[second root review](../../reports/unconventional-20261126/ROOT_SECOND_REVIEW.md) ·
[Béhani, Question 4.1](https://arxiv.org/pdf/2303.03203).

## 2. A common factor cannot survive many resets at high density

For one actual positive odd trajectory, let \(x_0,\ldots,x_r\) be consecutive
complete ascent-and-reset boundaries. Put

\[
 Y_j=x_j+1=2^{t_j}w_j,\quad w_j\text{ odd},\qquad
 2^{b_j}x_{j+1}=3^{t_j}w_j-1,
\]

where \(t_j\ge1\) counts the odd transitions in the block and \(b_j\ge1\)
is the excess halving depth. Write \(Y=Y_0\), \(T=\sum_{j<r}t_j\),
\(g=\gcd(w_0,\ldots,w_r)\). For fixed \(r\) and every \(\epsilon>0\),
the proposed written theorem proves

\[
                  g^{r+1}2^{T+t_r}\le C_{r,\epsilon}Y^{1+\epsilon}.
\]

It follows for the **full** gcd \(G=\gcd(Y_0,\ldots,Y_r)\) that
\(G^{r+1}\le C_{r,\epsilon}Y^{1+\epsilon}\). If the number of complete
blocks grows with the starting height at any rate, their common gcd is
\(Y^{o(1)}\). This last statement first fixes a number of blocks and only
then lets that number grow; it does not use a uniform constant in a
growing-dimensional Diophantine theorem.

The proof converts the physical block identities into a positive sum of
integers and applies Evertse's published inequality at infinity, 2 and 3.
Every nonempty subsum is nonzero because all coordinates are positive.
The root checked the original theorem on printed page 228, including the
absence of an unstated primitivity requirement. Matching constructions are
ordinary integers obtained from parity cylinders and the Chinese remainder
theorem. They vary the source; they are not a construction of an escaping
orbit.

The refinement using reset depths is also informative. Let
\(e=\operatorname{ord}_g(2)\) for \(g>1\), let \(e=1\) for \(g=1\), and
put \(K=(\sum b_j)/e\). Then, uniformly in the possible value of \(K\),

\[
                  g^{K+1}2^{T+t_r}\le C_{r,\epsilon}Y^{1+\epsilon}.
\]

The proof treats bounded \(K\) by splitting each positive geometric sum,
and treats large \(K\) by a fixed-fragment duration bound already present
in Paper 147. The exact arithmetic identity behind it is
\(g=\gcd(Y,2^{\gcd(b_0,\ldots,b_{r-1})}-1)\). The duration input is
independently reconstructed in a separate addendum and credited as prior
work.

The gap is precise: an exceptional trajectory need not retain a large
common factor. A strong upper bound on a factor does not supply a lower
bound on the factor along every hypothetical bad path.

[Persistent divisor](defects/PERSISTENT_RESET_DIVISOR.md) ·
[full gcd profile](defects/FULL_RESET_GCD_PROFILE.md) ·
[reset-depth refinement](defects/RESET_DEPTH_RATIOS.md) ·
[duration reconstruction](defects/DURATION_SOURCE_ADDENDUM.md) ·
[Evertse (1984), Theorem 2](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf).

## 3. Shifted squareclasses give a single-trajectory criterion

There is a distinct condition which does characterize eventual periodicity:
the squareclasses of the **shifted reset entrances** \(x_j+1\) have finite
rank in \(\mathbb Q_{>0}^{*}/(\mathbb Q_{>0}^{*})^2\) if and only if that
ordinary trajectory is eventually periodic. For each fixed rank bound,
only finitely many ordinary cycles satisfy the bound, independently of the
prime generators. This does not identify the eventual cycle.

The new PR192 supplies an elementary bound excluding squares of products
of distinct large integer translates. A fixed number of complete blocks
has logarithmic total duration. Taking sufficiently many consecutive
groups therefore produces one short group with many distinct reset
offsets. A low-rank relation, with three additional binary coordinates for
the two clocks and the number of factors, would make a forbidden square
product. A future minimum on an escaping trajectory makes this applicable
arbitrarily far out. The argument requires no bound on individual ascent
lengths or reset depths.

This is different from the first-wave finite **multiplicative** rank
condition on centered endpoint distances. Squareclass rank permits
arbitrary square multipliers. It is also different from PR192's raw
odd-state squareclasses: the shift by one and restriction to resets require
the short-group argument. The PR192 dependency is pinned to its new head.
No argument here bounds this shifted rank for every starting integer.

[Shifted squareclass theorem](defects/SHIFTED_SQUARECLASS_CLOSURE.md) ·
[PR192 cross-review and elementary no-successive-shifted-squares lemma](../../reports/unconventional-20261126/reviews/PR192_LATE_HEAD_REVIEW.md).

## 4. A plausible elementary merger route is blocked

Suppose two complete blocks take an ordinary odd source \(x\) to \(z\),
with \(3(z+1)\ge x+1\). If their parameter pairs differ, reversing their
order cannot give a second integral entrance with the same terminal.
The source required by the reversed affine composition is nonintegral.

The proof combines two exact ternary divisibility constraints with the
physical terminal floor. It reduces the parameters to 2,880 tuples;
the final exclusion is checked by Lean kernel reduction. The real
inequalities and the unbounded-to-finite reduction remain written
mathematics. The floor is essential: the sources 1893 and 1891 execute
the opposite orders of blocks \((1,3),(2,5)\), and both land at 25.

Thus a least-tripling-disagreement strategy cannot obtain its first smaller
ordinary merger by this protected two-block swap. Other merger words are
not excluded by this result. Plain block noncommutation already appears
in Paper 201; the extra statement here concerns an integral compensating
entrance at a common protected terminal.

[Proof and scope](defects/TWO_BLOCK_SWAP_EXCLUSION.md) ·
[kernel certificate](defects/TwoBlockSwap.lean).

## 5. Finite positive exit gates isolate the remaining escape bound

For \(X\ge2\), start each \(1\le x<X\) and follow the shortcut orbit
until its first state \(z\ge X\), or until a state repeats below \(X\).
The latter case has no exit. Along an exiting path multiply
\(3a/(3a+1)\) over odd departures; call this product \(w_z(x)\). Define

\[
 J_X(z)=\frac1{H_{X-1}}
       \sum_{\substack{x<X\\\text{first exit}=z}}\frac{w_z(x)}x,
 \qquad H_N=\sum_{x=1}^N\frac1x.
\]

This is a finite, exactly computable vector of positive rational numbers.
Using the pinned external component-density and first-passage results,
its decreasing rearrangement converges in \(\ell^1\) to the weighted
escape charges \((b_C/c_*)_C\), where \(c_*=\tfrac12\log(4/3)\).
The total consequently converges to \(\sum_C b_C/c_*\).

This extends PR201's summable-source exit gates to the harmonic endpoint.
The essential extra input is a bound on the prelanding peak, transported
down a scale ladder by total variation. The exceptional probability tends
to zero after fixing and then enlarging a finite bottom set. For fixed
bottom states, future mergers occur before sufficiently large gates.
The proof does not make an unjustified interchange of these limits.

These are **source-qualified** conclusions: the full analytic density and
first-passage dependency chain from the pinned Valbuena/Weaver work was
not rebuilt in this sprint. The source statements and the needed
quantifiers were checked, including the original TeX's simultaneous
path estimate and default-valued landing laws.

One concrete missing bound is now

\[
        \exists X_j\longrightarrow\infty\quad
                         \|J_{X_j}\|_1\longrightarrow0.
\]

Given the cited positive-charge theorem, this would exclude **all escape**.
It would still leave nontrivial cycles. A small finite computed total
does not establish the displayed limit, and no effective convergence
rate is claimed.

An equivalent scalar target uses the original finite ternary cylinder
density \(\rho_k\), with the normalization specified in the linked proof:

\[
 \lim_{k\to\infty}\left[
  \frac1k\sum_{\substack{a\le2\cdot3^k\\a\text{ odd}}}\frac{\rho_k(a)}a
                   -\frac{\log3}{2}\right]=\sum_C b_C.
\]

The scalar identity is already in [Weaver, Paper 176](https://rstation.ai/problems/collatz/papers/176/v1); our note independently reconstructs it.

The sharp upper coefficient \(\log3/2\) is unproved. A proposed monotonicity
shortcut is false: an exact integer certificate proves \(B_{14}>B_{13}\)
for the centered harmonic sums. Reflected dynamics preserve the entire
pressure family while producing a positive fixed cycle and exponential
harmonic-head growth. Scalar pressure alone therefore cannot provide the
required sign-sensitive upper bound.

[Critical exit gates](trace/CRITICAL_EXIT_GATES.md) ·
[Dirichlet charge identity](trace/DIRICHLET_CHARGE.md) ·
[reflection control](trace/REFLECTED_PRESSURE.md) ·
[physical annular current](trace/ANNULAR_ESCAPE_CURRENT.md).

## 6. Full denominators remain the cycle obstruction

For fixed \(M>1\) coprime to six, write the subgroup generated by 2 and 3
modulo \(M\) as \(C_u\times C_v\), \(u\mid v\). Clock pairs with
\(\gcd(A,p)=g\) and \(M\mid2^A-3^p\) exist exactly when \(u\mid g\).
The written construction realizes every prescribed carry class on
primitive positive rational cycles. Their near-critical real phase values are all of order \(p^2\) while their full reduced denominators retain
\(\log d=p\log3-o(p)\).

Thus many fixed-prime or fixed-modulus cancellations are compatible with
genuine positive rational cycles. This is a test of a proposed ordinary
cycle proof, not an ordinary counterexample. A successful integer argument
must control the entire reduced denominator for an arbitrary candidate,
or use an obstruction valid across all squareclass ranks. The construction
does not prove that such an obstruction is impossible.

[Complete modular carry theorem](arithmetic/COMPLETE_MODULAR_CARRY.md).

## 7. Verification and what is actually formalized

The integrated packet contains **22 Lean modules and 147 audited local
theorem declarations**, including private lemmas. The strict replay creates
fresh project objects with warnings treated as errors and checks every
reported axiom set. Only the standard axioms `propext`, `Classical.choice`
and `Quot.sound`, or no axioms, occur. The pinned Mathlib dependency build
is reused, with two missing pinned dependency modules rebuilt separately.

The third wave adds 26 declarations across modular carries, relative and
persistent reset arithmetic, arbitrary finite reset-divisor propagation,
two-block swaps and finite annular divergence. The large analytic,
Diophantine and asymptotic conclusions remain written proofs. In particular
the existing closing interfaces retain their unproved universal premises.
Counting an interface as a theorem does not discharge its assumptions.

Ten third-wave finite controls, including two separately written root
reviewers, pass complete-record comparison in normal and optimized Python.
The eight primary controls include two independent implementations of the
finite exit gates. Earlier first- and second-wave receipts remain in the
packet. Structural validation is reported separately from mathematics.

```bash
python -B research/unconventional-20261126/replay_lean.py \
  --mathlib /path/to/pinned/mathlib4 --lean /path/to/pinned/lean \
  --check reports/unconventional-20261126/THIRD_LEAN_RECEIPT.json
python -B research/unconventional-20261126/replay_third_wave.py
```

[Lean receipt](../../reports/unconventional-20261126/THIRD_LEAN_RECEIPT.json) ·
[complete finite replay](../../reports/unconventional-20261126/THIRD_CONTROL_REPLAY.json) ·
[source and integration hashes](../../reports/unconventional-20261126/THIRD_WAVE_SOURCE_MAP.json).

The next decisive step must supply a new universal inequality for the
finite harmonic head or the exit-gate totals, or force a contradictory
arithmetic structure on one fixed exceptional trajectory. The work above
does not justify replacing that step by a finite experiment, a density-one
statement, rational approximation, or the existence of a formal consumer.

## Closing challenge after the main freeze

The last focused review strengthened the swap theorem to an arbitrary shared
physical prefix and isolated an exact gate-loss telescoping identity. It also
identified the precise full-period factor allocation that still leaves the
relative squareclass rank uncontrolled. These results and their limitations
are in [the closing checks](CLOSING_CHECKS.md). The prefix extension adds a
written proof and an independently reproduced finite exhaustion, with no
additional Lean declaration.
