# Independent arithmetic review: offset descent and marked endpoints

**Verdict: VERIFIED at the statement and arithmetic level for the files below.**
This review reconstructs the arguments independently of their authors. It does
not claim an independent compiler run: the authors' Lean execution has a separate
receipt. Scope is the exact SHA256-pinned source content, not later edits or a
claim of full Collatz convergence.

Reviewer: the `band_hitting` research agent, whose authoring assignment was
`PhaseFrequency.lean`. No reviewed offset or marked-return proof was authored
by this reviewer.

| File | SHA256 |
|---|---|
| [OffsetDescent.lean](../../research/lean-dyadic-descent-20261121/OffsetDescent.lean) | `e0af0b1cbe4c4d90b34272bbbc45f25f6a084072dd17c2eb24be9e31641fde8b` |
| [MarkedOffsetReturn.lean](../../research/lean-dyadic-descent-20261121/MarkedOffsetReturn.lean) | `e9455233935c582084e73bd5f73d17553bab8b1a76bdb774485f38b33e81ed8f` |

## Exact threshold and its edge cases

Write `u=T^t(r)`, `A=3^(oddCount t r)`, and `D=2^t-A`. The exact finite
ordinary identity is `T^t(2^t q+r)=Aq+u`. The offset need not be the canonical
remainder modulo `2^t`: adding an integer multiple of `2^t` still preserves
the entire first `t` parity choices.

The nonnegative affine correction gives `Ar <= 2^t u`. Hence an actual
strict descent of `r` forces `A<2^t`. The same implication follows from a
strict descent of any lift: otherwise `Aq>=2^t q` forces `u<r`, contradicting
the previous inequality.

Under `D>0`, descent of the lift is exactly `u<r+Dq`. On the declared domain
`q>0`, this is equivalent to

`q >= floor((u-r)_+ / D)+1`.

The use of truncated natural subtraction is correct. If `u<r`, the
threshold becomes one and every positive quotient succeeds. If `u=r`, the
same threshold is correct because `Dq>0`. If `u>r`, ordinary integer division
gives the stated exact strict threshold. Quotient zero is deliberately
excluded: it can descend when `u<r`, although the positive-quotient threshold
is still one. Every theorem advertised as exact carries this domain guard.

The zero offset is handled soundly: `T^t(0)=0` and its odd count is zero;
for `t>0`, each positive lift contracts from `2^t q` to `q`. At `t=0` the
coefficient condition is false. The offset one has no strict descent of its
own but its actual `1 -> 2 -> 1` cycle yields the first contracting lifted
prefix at `t=2`; the supplied-basin theorem handles this case separately.

Every exponent difference `d-t` used to represent a high-bit lift has an
explicit `t<=d` hypothesis. No truncated subtraction is silently treated as
an integer inverse.

## Marked endpoint transport

If `T^t(r)=1`, appending `s` full terminal cycles produces exactly `2s`
additional shortcut clocks and `s` additional odd inputs. Its high-bit lift
therefore has the exact endpoint

`T^(t+2s)(2^(t+2s+e)+r)=3^(oddCount t r+s) 2^e+1`.

The source conditions retain oddness, the exact dyadic exponent, and the
actual offset-width inequality. For the endpoint, the hypothesis `e>0` is
essential and is present. It makes the endpoint odd and ensures that adding
one cannot cross the proposed octave's upper endpoint. The inequalities
`2^a <= 3^q < 2^(a+1)` then fix its exponent at `a+e`.

The target-width guard is explicitly sufficient, rather than exact. It
replaces the endpoint offset
`(3^q-2^a) 2^e+1` by the larger value
`(3^q-2^a+1) 2^e`. This explains the conservative guard and the need to keep
the additive one. Natural subtraction is justified by `2^a<=3^q`.

The coefficient contraction, positivity of `2^e`, and oddness of `r` give
strict endpoint descent. The frozen `captures` theorem converts a marked
endpoint at an ordinary clock into an actual induced-return index. Strict
descent excludes index zero. No assertion that the index is one is made.
The basin equivalence concerns that one exact ordinary path; it supplies no
certificate that either endpoint reaches one.

The phase-based endpoint lemma also checks: its assumed one-sided rational
approximation charges the logarithmic correction from the additive one,
then applies the frozen section conversion. It does not assume the displayed
integer `a` is already the floor of `j log_2 3`.

## Independent integer replay of the three windows

The reviewer separately evaluated the coefficient inequalities and the coarse
maximum `b=floor(70*2^a/(3^q-2^a+1))-a-1` with exact Python integers.

| `q` | `a` | Certified `b` | Source exponent interval |
|---:|---:|---:|---|
| 1 | 1 | 68 | `[3,70]` |
| 12 | 19 | 5110 | `[25,5134]` |
| 665 | 1054 | 1602424 | `[1331,1603754]` |

In every row, `2^a<=3^q<2^(a+1)` and `3^q<2^(2q)` hold. The first row's
width budget has zero slack, the second has slack 140, and the third has
positive exact integer slack. The displayed `b` is the maximum allowed by
this particular coarse guard in each row. The intervals overlap with no
gap, so their union covers every integer exponent from 3 through 1603754.
The branches using `d-24` and `d-1330` carry lower bounds sufficient to make
those subtractions exact.

## Scope boundary

No missing guard or arithmetic defect was found in the inspected statements.
These results certify strict descents, exact endpoint transport, marked
membership, and basin equivalences. A descent to an arbitrary smaller
integer proves convergence only when that smaller integer is already known
to converge, or within a valid induction whose other cases are covered.
Neither finite exponent coverage nor the supplied offset-basin hypothesis
is an unconditional coverage theorem for every marked ordinary input.
