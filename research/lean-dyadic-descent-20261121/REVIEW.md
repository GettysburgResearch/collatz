# Internal mathematical review: phase statistics and selected descending lifts

**Verdict: VERIFIED at the narrow statements below. Full Collatz remains OPEN.**

The `band_route` agent reconstructed these arguments separately from their
authors. This is an internal mathematical review, not external referee
acceptance. The reviewer authored `MarkedOffsetReturn.lean`; its imported
endpoint helper is therefore a disclosed dependency, not an independently
reviewed result in this document. The separate offset review covers that file.
Compilation and axiom receipts are recorded separately from this review.

## Exact source boundary

| File | SHA-256 |
| --- | --- |
| `PhaseFrequency.lean` | `f0afbb1f3ef0f8cb7494963855cfb5dd7cc97d9b9da551af65a31b848bbdce95` |
| `PHASE_FREQUENCY.md` | `df746ec0ce49717665f9d170b10cf0c0d9a31f565fc05dce850240d8b5a146ac` |
| `InfiniteDescent.lean` | `e490eaf11c9dc5d5e78fd49d69a0d20c4619244185925c8d5920fabfb8c39b4f` |

These verdicts do not automatically extend to later source versions.

## Phase statistics

The odd-only map is `(3*x+1)/2^v₂(3*x+1)`. The index counts odd inputs;
it does not count each shortcut step. The exact logarithmic increment is

`log₂(x_next) − log₂(x) = log₂(3) − v₂(3*x+1) + log₂(1+1/(3*x))`.

For an escaping orbit the final correction tends to zero. The finite
telescoping identity for each complex character leaves a bounded endpoint
term and the Cesàro average of a defect tending to zero. Integer-power
separation proves that every positive-frequency rotation factor differs from
one. No summability assumption or growth rate was inserted. A repeated
value in the deterministic orbit gives a finite range; thus unboundedness of
one actual orbit implies escape, as the source states.

The three-bit statistic has values `2,1,3,1` on odd residues `1,3,5,7 mod 8`.
Each is a valid lower bound for the actual valuation. Summing the exact
logarithmic identity and using nonnegative terminal height proves the
finite occupation bound. On an escaping orbit its limiting upper average
cannot exceed `log₂(3)`. Uniform occupation of the four odd residues would
instead give `7/4`, which is strictly larger because `3^4 < 2^7`.

The written fixed-window and zero-frequency consequences also pass. The
Fejér lower bound is `(m+2)/2` on the stated interval, and repeated bounded
visits give infinitely many marks. Zero density of marked odd clocks gives
diverging arithmetic mean of return gaps, not divergence of every gap.

A wording correction was made during review: **fractional binary logarithms**
are uniform. Numeric significands in `[u,v)` have frequency `log₂(v/u)`,
not `v-u`. Fourier cancellation does not establish low-bit uniformity,
independence, a shrinking-target rate, or exclusion of bounded nontrivial
cycles. The formal Fourier result and the written interval consequences
remain distinguished.

## Unbounded selected descents

For a coprime rational grid `a/q`, choosing `a*j = 1+q*b` gives

`q*(j*alpha-b) = 1+j*(q*alpha-a)`.

Since `j<q≤N` and the grid error is at most `1/(N+1)`, this lies strictly
between zero and two. A second use of integer-power separation forces `j`
beyond any prescribed bound. This proves the required one-sided
approximants without assuming bounded or unbounded continued-fraction
partial quotients.

Fix an odd offset `r` and a supplied shortcut certificate `T^h(r)=1`, with
`p` odd inputs. The construction chooses an approximation exponent `q`,
then sets `s=q-p`, `d=h+2*s+1`, and `y=2*3^q+1`. Exact finite high-bit
transport gives `T^(h+2*s)(2^d+r)=y`. The source and endpoint meet the
same marked-section predicate. The coefficient estimate, including its
scaled version, proves both `y<2^d+r` and `C*y<2^d+r`; the additive `+1`
is absorbed explicitly. `captures` places this endpoint at an actual
positive number of first returns. That return index need not be one.

The quantifiers are **fixed certified offset, arbitrary size and contraction
requests, then selected dyadic exponents**. They are not all dyadic exponents
for that offset. The basin equivalence follows from the actual path and
does not assert that either endpoint converges.
The unconditional `power_plus_one_arbitrarily_strong` corollary supplies the
offset certificate at `r=1,h=0` directly; it adds no unproved hypothesis.

In particular, a hypothetical least counterexample `2^d₀+r` would have a
convergent smaller offset `r`. The theorem selects other exponents; it does
not supply descent at the prescribed `d₀`, nor transport failure there to
the selected lifts. Universal marked-return descent remains the unsupported
closing step.
