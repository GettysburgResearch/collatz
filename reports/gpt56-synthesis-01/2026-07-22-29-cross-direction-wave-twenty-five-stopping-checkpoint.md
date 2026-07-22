# Cross-direction lemma forge -- wave twenty-five stopping checkpoint

Date: 2026-07-22
Agent: `gpt56-synthesis-01`
Issue: #29
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Status: four proposed lemmas; constructive counterexample lanes recorded; no counterexample claimed

## Checkpoint posture

The wave remained aimed at a full unconditional Collatz resolution.  A
nontrivial positive cycle and an ordinary divergent orbit were treated as the
two admissible counterexample targets.  This stopping checkpoint publishes
only exact intermediate results that can be reused without mistaking a
modular, rational, negative, or completion object for a positive integer
counterexample.

No candidate integer was found.  In particular, none of the divisor searches
below produced a nontrivial hit.

## Result 1 -- the five-defect frontier is empty

[`L-9912`](../../research/cross-direction-lemmas/claims/L-9912-five-defect-positive-cycle-exclusion.md)
uses the centered numerator

\[
 E_w=C_w-(2^A-3^k)
 =\sum_j3^{k-1-j}2^{A_j}(4-2^{a_j}).
\]

Valuation `2` is neutral in this coordinate.  Centered monotonicity reduces
every word with exactly five non-neutral valuations to finitely many low-core
types.  Rotating a largest neutral gap to the terminal position gives

\[
 E_w=3^tE_u,
 \qquad
 \gcd(2^A-3^k,3)=1.
\]

Parity then makes every positive exact hit satisfy `E_u>=2D`.  Monotone
largest-gap bounds leave ten finite rows, and the exact checker finds no
divisor hit.  Consequently a nontrivial positive cycle needs at least six
non-`2` valuations at this stage.

## Result 2 -- the six-defect frontier is also empty

[`L-9913`](../../research/cross-direction-lemmas/claims/L-9913-six-defect-positive-cycle-exclusion.md)
classifies all six-defect cores by the number of letters at least three.
Centered deletion and lowering exclude all but

\[
 (1^6),\qquad (1^5,3),\qquad (1^5,4),\qquad
 (1^4,3,3)\ \hbox{with nonadjacent threes}.
\]

The same largest-gap mechanism makes every surviving family finite.  The
checker enumerates every chronological placement and every residual weak
composition, independently recomputes both forms of `E`, and tests
divisibility before the height sieve.  There are no hits.  Combined with the
previous centered exclusions, every nontrivial positive cycle must therefore
contain at least seven valuations different from two.

This is a genuine new support floor, not an induction: unbounded-support
families remain completely open.

## Result 3 -- a lossless cross-prime compiler

[`L-9914`](../../research/cross-direction-lemmas/claims/L-9914-cross-prime-excess-path-crt-compiler.md)
factorizes a prospective denominator

\[
 D=2^A-3^k=\prod_sQ_s
\]

and writes `h_s=ord_(Q_s)(2)`.  For prefix excesses

\[
 e_j=A_j-j,\qquad 0=e_0\le\cdots\le e_k=A-k,
\]

the strict full-denominator order bound from `L-9909` gives

\[
 \operatorname{lcm}_s h_s=\operatorname{ord}_D(2)>A-k.
\]

Compatible local paths `e_j mod h_s` therefore have at most one lift in the
entire monotone excess window.  The claim proves an if-and-only-if generalized
CRT reconstruction, including all noncoprime-order compatibility conditions,
and shows that numerator vanishing at every full prime power is exactly
`D|C_w`.

It also proves that if the residue word has least cyclic period `d_s` at each
prime power, then the integer word has period `lcm_s d_s`.  A primitive word
must satisfy

\[
 \operatorname{lcm}_s d_s=k.
\]

Thus factor-dependent local powered aliases are not independent choices.
Constant aliases collapse to the trivial all-`2` word.  The compiler is
lossless, but no compatible nonconstant full-factor tuple was constructed.

## Result 4 -- additive one-counter controllers are periodic

[`L-9915`](../../research/cross-direction-lemmas/claims/L-9915-additive-one-counter-periodic-output-obstruction.md)
considers a deterministic finite control `q_n`, a nonnegative counter `c_n`,
and updates depending only on `q_n` and whether `c_n` is zero.  Fixed residue
observations can be folded into the finite state.

If zero is visited infinitely often, an exact state `(q,0)` repeats and the
whole output tail repeats.  If zero is visited only finitely often, the
positive-control orbit enters a finite cycle.  Negative net counter drift is
incompatible with an infinite legal run; zero or positive drift still emits a
periodic output.  Hence every infinite output is ultimately periodic.

Together with `L-9908`, this excludes that restricted controller architecture
from producing a positive centered forced tail.  It closes only additive,
zero/fixed-residue-observed subcases of issue #43 `ACL-N076` and issue #40
`ACL-N077`; exact top-boundary access, nonlinear updates, changing moduli,
stacks, and multiple unbounded registers remain open.

## Constructive counterexample notes retained for the next wave

Two exact constructive calculations were completed after the four claims
were frozen.  They are recorded here as starting points, not promoted to
theorem entries.

### Arbitrary distributed pulses on a negative cycle

Let a negative cycle word have length `N`, exponent total `B`, negative states
`z_i`, and prefix exponents `A_i`.  Add pulses `delta_i>=0` to its valuations,
put

\[
 \Delta_i=\sum_{t<i}\delta_t,
 \qquad \Delta=\sum_i\delta_i,
 \qquad b_i=-(3z_i+1)>0,
\]

and set `D_Delta=2^(B+Delta)-3^N`.  Direct telescoping gives the exact pulsed
numerator

\[
 C_{\boldsymbol\delta}=z_0D_\Delta+R_{\boldsymbol\delta},
\]

\[
 R_{\boldsymbol\delta}
 =\sum_i b_i(2^{\delta_i}-1)
   2^{A_i+\Delta_i}3^{N-i-1}.
\]

Thus integrality is the full-denominator condition `D_Delta|R_delta`, and
positivity is `z_0+R_delta/D_Delta>0`.  For two pulses of sizes `delta` and
`epsilon` at `i<j`, define

\[
 U_t=b_t2^{A_t}3^{N-t-1},\qquad T=\delta+\epsilon.
\]

Then

\[
 R=U_j2^T+(U_i-U_j)2^\delta-U_i.
\]

At fixed total pulse this reduces the exact two-pulse search to one
exponential congruence modulo the full denominator.  No hit was obtained.

### Powered negative three-cycle with neutral padding

For

\[
 w_{m,r}=(1,2)^m(2)^r,
\]

the negative seed has fixed point `-5`, and

\[
 D_{m,r}=8^m4^r-9^m3^r,
 \qquad
 E_{(1,2)^m}=6(9^m-8^m).
\]

Since `gcd(D_(m,r),6)=1`, a positive exact hit would force

\[
 D_{m,r}\mid(9^m-8^m).
\]

Reducing the denominator with this relation and using its coprimality to
three sharpens the condition to

\[
 \boxed{D_{m,r}\mid\gcd(9^m-8^m,\ 4^r-3^r).}
\]

The complete first-positive/height windows for `1<=m<=1000` contain only
three candidates, at `(m,r)=(2,1),(4,2),(7,3)`, and all fail divisibility.
This is a failed constructive ansatz, not an all-parameter exclusion.

## Audit and reproducibility

- A nonauthoring cold reviewer reconstructed `L-9912` and `L-9913`, including
  every contraction class, largest-gap cutoff, residual range, chronological
  placement, and parity-height implication.  Both checkers independently
  returned `PASS` with zero divisor hits.
- A different nonauthoring reviewer reconstructed every CRT, order-window,
  local-affine, and period-span step of `L-9914`; the 792-word orientation
  packet at `(A,k)=(13,8)` also matched.
- The integrating review reconstructed both branches of the elementary
  finite-control proof in `L-9915` and checked the stated escape boundary.
- The two Python artifacts use exact integer arithmetic and pass
  `py_compile`.
- Claim links, IDs, math delimiters, equation tags, whitespace, and repository
  status are checked at publication.

Run:

```text
python research/cross-direction-lemmas/proofs/L-9912-five-defect-certificate.py
python research/cross-direction-lemmas/proofs/L-9913-six-defect-certificate.py
```

## Stopping boundary

This wave proves neither the Collatz conjecture nor a counterexample.  It
raises the positive-cycle centered-support floor from five to seven, makes
the cross-prime construction exact, and removes one restricted causal
controller class.  The actual resolution still requires either a compatible
full-denominator positive word, a positive divergent seed, or a universal
argument excluding all such objects.  Work stops here at a clean published
checkpoint.
