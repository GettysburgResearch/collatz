# Final Lean proposal and the still-open universal inference

**OPEN. There is no completed Collatz theorem in this packet.** The deliverable consists of the six concrete Lean modules below, their written mathematical extensions, and a fresh complete-checkout replay. No new Collatz axiom or unfinished proof is used to manufacture a closing theorem.

| Module | Proved endpoint | Universal inference still required |
|---|---|---|
| `carry/MovingOrigin.lean` | Two-reference repair of an actual carry; a strict canonical return with the original upper hit; a quantitative smaller source on another row | An admissible smaller source for every actual residual crossing, including rows with no nonnegative reference hit |
| `carry/IteratedReturn.lean` | Arbitrary prescribed finite chains, ordinary translated chains, terminal progressions and the centered identity | A selection theorem for one given bad source, with known upper goodness and a net decrease in height |
| `carry/PowerBacktrace.lean` | Both ordinary endpoints and exact odd costs of the explicit fixed-component entrance | Goodness of its power-minus-one upper endpoint, or a different paired entrance with a known hit and a smaller terminal |
| `carry/InverseEnvelope.lean` | An arbitrary-word inverse cost bound, sharp realizers, and failure of every nonnegative origin on the stated hard crossing | A return which overcomes those hypotheses rather than silently dropping the certificate budget |
| `source/OriginalWindow.lean` | Finite source-fibre and grade bounds; actual first-passage affine error under block contraction; exact local color and base-81 boundary transport | The full written source transfer plus source hypotheses, and a regeneration inequality whose retained population permits iteration to a contradiction |
| `cycle/InverseOffsets.lean` | Unrolled ordinary distortion, a short source interval, full gcd cancellation and the adjacent-label denominator test | Exclusion of every full ordinary cycle satisfying the least-disagreement basin constraints |

## The direct descent target

For a canonical reverse disagreement, the required output is a concrete smaller positive ordinary representative with the same reverse orientation and a supplied upper certificate. The new row does this literally, with 19 fewer clocks and eight fewer odd departures. Arbitrarily many repetitions on changing sources do not prove that the next repetition exists for an arbitrary fixed source.

The literature-inspired component entrance is explicit enough to identify its missing output: its upper arm reaches `3^(k+1)*x - 1`, while its lower terminal exceeds `x` for `x > 1`. The known hit from `3*x` gives no hit at that new endpoint. Yu's fixed-input estimate also rules out paying for this particular entrance by linear clock savings in the chain depth. The theorem concerns that construction, not every possible adaptive paired entrance.

## The smaller-head target

The new written recurrence reaches a genuine ordinary four-trit head at logarithmic height `Theta(log d)`. The original interval, actual pair colors, and exact ancestor boundary are retained. The gap is now a population estimate: a lower mass of order `d^-3` at the old scale becomes potentially exponential in the new logarithmic height. It cannot be fed back into the present theorem requiring polynomial source mass. A loss small enough to preserve eligibility, an unconditional statement excluding the regenerated heads, or a different closed measure could settle this route. No such estimate is proved here.

## The bounded-cycle target

For ancestors in the cycle's denominator lattice, the label difference and the cycle's unit modulo its reduced denominator give the exact denominator of their difference. The explicit rational control has ordinary odd-integer spacing through four full laps on its floor-clipped inverse tree. The argument leaves open whether every nontrivial ordinary candidate in the least-disagreement branch has a forbidden ancestor or another contradiction. The finite spacing and tested ordinary windows do not settle that assertion.

The newly reviewed Subspace-Theorem route in PR210 requires arithmetic and repetition properties of a limiting critical script which are not forced by integer finite approximants. The Fourier route in PR193 requires a bounded subsequence of total-variation norms which the source estimates do not supply. These are additional explicit options, with their premises still unproved, rather than closing imports.
