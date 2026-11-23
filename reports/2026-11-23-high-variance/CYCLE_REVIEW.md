# Reconstruction review: the complete-word congruence construction

Reviewer: the in-session `escape_rigidity` agent, 2026-11-23.

**Verdict: PASS on the base arbitrary-modulus/height construction and
the declared finite-algebra interface.** The strengthened height argument
is also mathematically checked below, but this reviewer suggested its
integer amplification mechanism; that section requires the disclosed
contributor-review classification rather than an independence claim.
This is internal mathematical reconstruction, not external peer review.

## Exact reviewed sources

| File in `research/high-variance-20261123/` | SHA256 |
|---|---|
| `CYCLE_IDEAL.md` | `62c26992a194ee1b53f8b7eba8a1d00cdc1e37ffe78692795b427c05ae947681` |
| `cycle_ideal_control.py` | `d5f53019433b2551ed996103d2c163ca9a9f43c8cca2280e22eca68cda96df1b` |
| `CycleWordAlgebra.lean` | `fc42bf2a602592c7f7ebbe42ca3c21bb96b58f7ce2dc93aed2cafdbac47f984e` |

These hashes bind the inspected bytes. A later status-only edit needs
separate accounting; the verdict does not silently extend to changed
mathematics.

The final note hash is
`373de11d5e0a9bd4b9678f58b711a2ae1aba5c02592d41b8cffe3a832416f392`.
After the review, its author changed only the opening review-status
sentence and the closing checker/replay-status paragraph. The reviewer
independently reversed those two exact replacements in memory and
recovered the reviewed `62c26992...` hash above. The mathematical text,
checker and Lean source are unchanged.

## Base construction reconstructed independently

1. The carry convention agrees with chronological shortcut composition.
   For `AB`, the complete carry is
   `3^(ones B) C(A) + 2^(length A) C(B)`. The swapped second one changes
   the complete block carry by exactly `2*3^(p-2)`; no prefix, suffix or
   denominator factor is omitted.
2. Mechanical words with the selected rational density have discrepancy
   strictly below one on every cyclic interval. Density above one half
   excludes `00`; density below two thirds forces a cyclic `10101`.
   The chosen swap creates exactly one `00`, and the block boundaries
   cannot create another one.
3. The common exponent is valid for both the prescribed modulus and the
   new prime. The two possible carry residues cannot both vanish at the
   new prime. Repeating with multiplicity `M` therefore gives exactly
   `M|D`, `M|C`, `ell|D`, `ell` not dividing `C`.
4. The `M` markers have one uniquely long cyclic spacing. Every rotation
   preserving the word must fix the marker after that spacing, hence
   have zero shift modulo the complete length. The single-marker case
   `M=1` is covered separately. This proves word primitivity.
5. The common denominator is odd and coprime to three. At every rotation
   the numerator's parity equals the first word bit, even after reducing
   the fraction. Therefore the displayed rational cycle follows the
   actual rational shortcut rule. A smaller state period would induce a
   smaller parity-word period, so its least state period is the word
   length. The uncancelled prime `ell` proves nonintegrality.
6. The modified block-prefix discrepancy lies in `(-1,2)`. Subtracting
   two such discrepancies gives the stated cyclic bound of three,
   including wraparound and intervals exceeding one period. Every group
   of three preceding bits contains a one.
7. Expanding the preceding affine recurrences gives the displayed
   positive series; the homogeneous remainder tends to zero because the
   full-period slope is strictly below one. Each selected term is at
   least `lambda^(j-1)/54`. Grouping in triples gives
   `x >= lambda^2/(54*(1-lambda^3))`. The exact geometric sum gives
   `1-lambda < 1/a0`, while `lambda^2 > 3/4`; together these imply
   `x > a0/216` at **every state of this same complete cycle**.

The written statement correctly limits the congruence conclusion to
prescribed finite precisions. It does not prove that the full valuation
at each selected prime cancels, nor exclude adaptive prime/precision
tests. It makes no positive-integer cycle claim.

## Strengthened height: contribution disclosed

The reviewer suggested replacing the geometric-sum exponent `a0` by
`B*a0` under the exact condition `2^(B*a0) < 2*3^(B*q)`.
This directly gives `x_min > B*a0/216` and
`x_min/L > B/(648*M*t)`.

The author's subsequent continued-fraction corollary was reconstructed:
the displayed convergent determinant and tail formula have the correct
sign; odd-indexed upper convergents have unbounded denominators and
`0 < A-q*log_2(3) < 1/q`. Thus `A=a0`, and `B=q` satisfies the exact
integer condition. Since `a0<2q` and `L<=3*M*t*a0`, the arithmetic yields

`x_min > a0*q/216 > L^2/(3888*M^2*t^2)`.

All constants and strict inequalities check. This section is a
contributor's verification, not an independent-review claim. The
continued-fraction proof is supplied in the note; no unread theorem is
needed to justify the inference here.

## Lean interface and exact finite controls

All twelve public theorem statements and their bodies in
`CycleWordAlgebra.lean` were inspected. They prove whole-word counts,
complete carry composition and adjacent exchange, repeated carries in
ring quotients, complete denominator payment, and the two-choice
nonzero selector. They do not formalize balanced-word existence,
primitivity, the rational dynamical interpretation or the infinite
height subsequence. Compilation and axiom checks are separate execution
evidence supplied by the principal research agent.

The checker was read rather than treated as evidence for its own
unbounded theorem. It checks the complete carry/denominator and every
rational and ordinary step. Its KMP criterion correctly tests whether
the finite word is a proper power. The verifier now checks the parameter
domain explicitly. Its uses of `require`, rather than `assert`, keep
the checks active under Python optimization.

On the final checker bytes, the reviewer additionally ran a separate
`Fraction`-based replay. At every step it independently reduced the
rational state and compared it with the carry of the corresponding
rotated word, as well as checking reduced parity, closure and the
height bound. The four cases were:

| M | ell | q | B | k | Complete period | Floor of cycle minimum |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 12 | 1 | 1 | 160 | 4 |
| 1 | 5 | 17 | 1 | 2 | 324 | 107 |
| 5 | 7 | 12 | 1 | 1 | 2400 | 4 |
| 1 | 5 | 41 | 41 | 1 | 520 | 865 |

All four passed, including both selector branches and the amplified
height condition. These are finite cross-checks, not a census or the
proof of the quantified construction.
