# Complete-cycle reassessment: an exact multiscale carry attack

Date: 2026-11-23. Baseline: `b78819e95ee7d39f02022de991b42217821e7590`.

**Status: OPEN closing attempt.** The finite identities and matching bound
below have written proofs. They do not improve the existing polynomial
zero-fibre census or exclude unrestricted positive integer cycles. No new
Lean declaration or historical novelty claim is made.

## 1. What the whole-repository reassessment changes

The older compressed-cycle, Smith-form and CRT interfaces already keep
all of the word information. Primitive-root reduction removes repetitions;
the augmented Smith class, not the order-blind determinant, retains the
numerator; local prime-power paths must reconstruct the same monotone
integer word. The reviewed pulse results have fixed support or specified
architectures. None supplies a bounded-complexity description of every
primitive positive cycle.

The newer work preserves the same remaining arithmetic in different forms.
PR175 counts the actual zero fibre by its ordinary cycle minima. PR176
retains that fibre as an exact affine trace coefficient and identifies
why uniform mixing and rotation conservation do not bound it. PR185's
polynomial residual growth occurs before the numerical gcd at evaluation.
PR178's latest torus normalization has degree exactly `D/gcd(C,D)`; its
independent-Mahler attempt does not prove that degree exceeds one.
Our preceding complete-word gcd transport is exact, but local carry
changes do not imply independent information from different word blocks.

This pass therefore tried **successive small-ball bounds for the actual
complete carry**, using all words at every scale. The first split is
rigorous. Repeating its saving after conditioning on the zero residue is
the unsupported step; the conditioned law can be fully correlated.

## 2. Complete word and exact split law

Fix `A>=3`, `1<=p<A`, and `D=2^A-3^p>0`. Let `W(A,p)` be all binary
words of length A and weight p, and put

\[
 C(w)=\sum_{i=0}^{p-1}2^{d_i}3^{p-1-i},\qquad
 N_r(A,p)=\#\{w\in W(A,p):C(w)=r\pmod D\}.
 \tag{1}
\]

The target is `N_0<A`: one primitive period-A integer cycle supplies A
distinct zero words. Repetitions of a shorter cycle supply its shorter
number of distinct rotations. The excluded case `(A,p)=(2,1)` has
`D=1,N_0=2`, so the strict target is not asserted there.

Split a complete word as `w=uv`, with `|u|=h`, `|u|_1=j`, and
`|v|=A-h`, `|v|_1=p-j`. The exact chronological formula is

\[
 \boxed{C(uv)=3^{p-j}C(u)+2^hC(v).}
 \tag{2}
\]

For every admissible `j`, let `mu_(h,j)` be the uniform carry law modulo
this same full D, not modulo a new block denominator. Set

\[
 U_j={h\choose j},\quad V_j={A-h\choose p-j},\quad
 \omega_j=\frac{U_jV_j}{{A\choose p}}.
\]

Conditional on j alone, the two blocks are independent and uniform.
Thus the exact full-word zero probability is

\[
 \boxed{
 \frac{N_0(A,p)}{{A\choose p}}
 =\sum_j\omega_j\sum_{x\bmod D}
  \mu_{h,j}(x)\,
  \mu_{A-h,p-j}(-3^{p-j}2^{-h}x).
 }
 \tag{3}
\]

All coefficients inverted here are units because `gcd(D,6)=1`.
No parity word, carry term or prime-power factor was omitted.

## 3. The available small-scale injection and matching bound

For length l and weight k, the exact carry range is

\[
 3^k-2^k\le C\le2^{l-k}(3^k-2^k).
 \tag{4}
\]

The endpoints are attained by `1^k0^(l-k)` and `0^(l-k)1^k`.
Moving `01` to `10` strictly decreases the complete carry, proving (4).
The pair `(k,C)` determines the length-l word: carry parity recovers its
first bit b, and

\[
 C(bv)=3^{k-b}b+2C(v)
\]

recovers the suffix carry and its weight. Induction finishes the decoder.
Consequently the carry map is injective modulo D whenever

\[
 R(l,k):=(2^{l-k}-1)(3^k-2^k)<D.
 \tag{5}
\]

Suppose (5) holds for both blocks at every admissible j. In each slice j,
the zero equation (2) forms a partial matching between the U_j prefix
words and V_j suffix words: each prefix has at most one matching suffix,
and each suffix has at most one matching prefix. Therefore

\[
 \boxed{N_0(A,p)\le B_h(A,p):=\sum_j\min(U_j,V_j).}
 \tag{6}
\]

This is an all-word bound, and the same proof bounds every residue r.
The easily checked sufficient hypothesis `D>3^max(h,A-h)` implies (5),
although the exact range in (5) is usually smaller.

For example `(A,p,D,h)=(13,8,1631,6)` satisfies (5) for all slices: the
largest range for length seven is 665, and the ranges for length six are
smaller. Formula (6) gives

`1+7+20+15+6+1=50`,

whereas primitive-cycle exclusion requires fewer than 13. This is a
calculation of the bound, not a claim that 50 zero words exist.

## 4. Why the next scale does not inherit the law

The independence used in (3) holds **before conditioning on the complete
zero equation**. In a nonempty slice satisfying (5), conditional on that
equation and on the prefix word, the suffix word is determined. Its
conditional carry atom has probability one. It is not distributed as
`mu_(A-h,p-j)`, and it need not satisfy that law's small-atom estimate.

This distinction already occurs in the known cycle. Take `A=4,p=2,D=7`
and split into two blocks of length two and weight one. Their carries are
`C(10)=1`, `C(01)=2`, and (2) becomes `3C(u)+4C(v)`.
The two zero pairs are exactly

`(10,10)` and `(01,01)`.

The two crossed pairs have residues 4 and 3. Thus the unconditioned blocks
are independent uniform choices, but conditioning on zero makes them
identical. Once either block is known, the other is a point mass.
This four-pair identity retains the allowed repetitions of the trivial
cycle; it is not an invented stochastic countermodel or a new census.

A multiscale proof would need a further arithmetic constraint on these
actual conditioned overlaps. Applying the unconditioned saving again,
or replacing a conditioned suffix by a fresh random word, is invalid.
The same issue occurs in prime-power refinement: L-9914's local paths
must glue to one monotone excess word, rather than being independently
chosen annihilating paths. The earlier adjacent-swap gcd law does not
supply the missing conditional estimate.

## 5. Comparison with the already stronger zero-specific census

Even successful iteration to the single matching bound does not approach
the current numerical threshold. Let `h=floor(A/2)` and let `p/A` stay
in a compact subinterval of `(0,1)`. A central admissible j gives an
exponential lower bound for the numerical expression `B_h`; conversely
Cauchy and Vandermonde give

\[
 B_h\le\sum_j\sqrt{U_jV_j}
 \le\sqrt{(A+1){A\choose p}}.
\]

Stirling's bounds consequently give

\[
 \log B_h=\tfrac12 A\,\mathsf h(p/A)+O(\log A),\qquad
 \mathsf h(t)=-t\log t-(1-t)\log(1-t).
 \tag{7}
\]

Thus (6) remains exponential. At the critical ratio `p/A -> log_3(2)`
its exponent is approximately `0.32923 A`. Under the same source-qualified
logarithmic-form input used by PR175,

\[
 D\ge c2^AA^{-K},
\]

the block-injection hypothesis holds eventually, since `2>sqrt(3)`.
But PR175 already obtains

\[
 \boxed{N_0(A,p)\le A\,
  \#\{1\le m\le\lfloor(p2^A-D)/(3D)\rfloor:\gcd(m,6)=1\}
  =O(A^{K+2}).}
 \tag{8}
\]

The polynomial bound (8) is asymptotically stronger than (6). Its
remaining gap is whether even one eligible ordinary minimum closes.
No improvement over (8) is claimed here. The complete word law being
far from uniform at this clock was already established in PR176; it is
not a new observation of this pass.

**Outcome.** The exact split exposes a legitimate small-scale matching
problem and the precise conditioning needed by an all-scale argument.
No arithmetic estimate for that conditioned overlap was obtained. The
full numerical cancellation, `N_0<A`, and positive-cycle exclusion remain
open; no new Lean wrapper was added for the reused concatenation identity.

## 6. Exact source scope

These are the inspected sources and their roles. Prior review verdicts
remain scoped to their own stated claims; this pass is not a replay of the
historical formal or computational corpus.

- **Old full-word interfaces:** PR34 commit
  `b7eec65ffb13c5a89415a888c0153f36a52f23e3`, under
  `research/cross-direction-lemmas/claims/`:
  `L-9904-compressed-cycle-primitive-root.md`, blob
  `8f2076e6756c62aa339175107a53c22aa751ee62`;
  `L-9907-cycle-circulant-snf-equivalence.md`, blob
  `1cda9ea21d88b8fb594a61fd06d00772370a4a2f`;
  `L-9914-cross-prime-excess-path-crt-compiler.md`, blob
  `383c5f0a5cf364506a9f06ad9287d16c4d7d8dba`.
  The primitive-root and CRT claims were read in full; the Smith statement,
  augmented-class equivalence and method boundary were inspected.
- **Pulse and mixed-place scope:** the resident results catalog at the
  baseline above and the PR49/50/51/53 review at commit
  `c71826d24f21d22a2e13749fb65cc1573e516ffd`,
  `reports/gpt56-h-01/2026-08-01-pre-public-review-prs49-50-51-53.md`,
  blob `bd17100aa512b2941598c0340533b77ef96591bd`.
  Review-summary inspection only; no new certification of pulse caps,
  Matveev constants or large certificates is claimed.
- **Actual minimum census:** PR175 commit
  `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`,
  `research/lean-global-closure-20261121/closing/ZERO_ATOM_CLOSING_ATTEMPT.md`,
  blob `2e96c55e7c3edcc69a0dcc56b4d6adb573fd9a51`. Its external
  logarithmic-form dependency remains attached to (8).
- **Affine trace and failed mixing/antichain routes:** PR176 commit
  `ff3e068fa44eb85bb918580b2e10e18c027a18e6`,
  `research/lean-global-resolvent-20261121/overview/longshot/cycles/IDENTITY_ATOM_ATTEMPT.md`,
  blob `c76c61df5cdfe887bddc50cce0f8ced7dc923211`. Read in full;
  its large enumerations were not rerun.
- **Residual polynomial denominator:** PR185 commit
  `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`, under
  `research/central-closure-20261123/`:
  `PRIMITIVE_DENOMINATOR_GROWTH.md`, blob
  `54b6f161d8a8ce81c32fed6c6166807d5c9f8445`, and
  `PRINCIPAL_FIBER_CONTROL.md`, blob
  `c749ad8f97cd9585a9b251129a79a880ff46d965`. The previous inspection
  and the polynomial-versus-numerical boundary are reused.
- **Latest Mahler/isogeny attempt:** PR178 commit
  `4e204f54136c79cf8c9393b34e3330594f99ae0a`,
  `research/global-closure-20261123/cycles/INTEGRAL_MAHLER_CLOSURE_ATTEMPT.md`,
  blob `6a2564f313ac0ccc506cbe32c4fa2a6c67a137a9`. Read in full.
  Its primary Mahler theorem remains source-qualified; no additional
  independent-base equation is assumed here.
- **Preceding local transport:** baseline commit above,
  `research/closure-round2-20261123/CycleCancellation.lean`, blob
  `8fea237e8ce419920eef4b397e598c7705892a53`, and companion
  `CYCLE_CANCELLATION.md`, blob
  `b0b0fc74431af6d4dbfa4170598ec5be78ff8b55`.
- **Literature guidance:** PR186 commit
  `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493`, under
  `literature/deep-machinery-20261122/`, the arithmetic chapter
  `03_arithmetic_and_logic.md`, blob
  `e3db572abcc9a504ec5110437a02cfec693d4af1`, and rigidity chapter
  `05_rigidity_and_long_shots.md`, blob
  `8b7a6471f014be065f1dc3decc0027ba112cfd33`. Relevant fixed-dimension,
  source-law and reducible-affine-action limitations were inspected.
  No exception-free S-unit or uniform-mixing theorem is imported.
