# Root reconstruction and integration review

**Scope: independently reconstructed written arguments and bounded executions;
no complete Collatz proof, external peer acceptance, or formal verification.**
The exact scientific files are identified in `CONTENT_MANIFEST.json` and in
the narrower cross-reviews. The packet remains PROPOSED research.

## Prime-height arithmetic

I reconstructed the original P1--P12 argument from the literal odd-map
recurrence, then checked the P13 strengthening against the second agent's
independent reconstruction.

For a segment of length d and division sum A, the positive affine correction
satisfies `2^A n_j = 3^d n_i + C`, and every common divisor of the endpoints
divides C. Bounding `C/2^A` by `(3/2)^d-1` and using
`2^A n_j/n_i <= 4^d` gives

    gcd(n_i,n_j) n_j < 6^d n_i.

Products of consecutive prime-power returns telescope the endpoint ratio.
This gives the valuation tail with its explicit first-occurrence term.
At a record peak, backward height control uses only the actual bound of
one bit per upward odd step. The local-prime lower bound follows from
layer integration; it does not bound how many new primes an orbit may use.

For P13, the short maximum-ending window permits the stronger exact cost
`d log2(3)+(A-d)`. Every edge cost is positive. Deleting one valuation
maximizer per prime removes at most s of the 2s+1 states and removes the
first-occurrence term at every positive level. The original return intervals,
not an artificially compressed trajectory, pay for the remaining levels.
The peak-window division budget is `A<=4s`, so the cost is below 6s.
Integration and inversion give the displayed `(s+1)^(64s)` bound. The source
alternative and the cyclic unrolling are distinct and correctly separated.

I also inspected the primary Paper137 and Paper138 statements. The note
credits the prior return and deletion mechanism, compares only the
prime-support subclass, and does not claim the general rank result is
improved. See `REVIEW_PRIME_SUPPORT.md` for the independently implemented
P13 replay and exact constants.

## Directed circulation and analytic scope

I reconstructed the high and low returns from the pinned PR146 construction,
including the role of ordinary edges traversed in either direction and
forward tripling. The arithmetic choices give a finite family of injective
affine source labels. Keeping labels with multiplicity is essential: equal
numerical sources from different slots must not be discarded.

For each source, the finite cycle has total defect zero. Its two nonnegative
inequalities can be summed by Tonelli before any absolute convergence is
known. Weight comparability and the uniform incoming multiplicity first
transfer finiteness between orientations. Only then is signed rearrangement
used to obtain exact flux balance. This is a positive circulation on the
augmented graph; it does not establish ordinary orbit merger.

The one-sided functional estimates retain OD2/OD3 from PR155. The Liouville
extension retains a divergent component moment as an explicit hypothesis.
The clipping proof is valid because each orientation separately decreases
under a monotone 1-Lipschitz clipping. The exponent 0.84 specializes this
conditional statement using the imported predecessor-count theorem. No
external proof-assistant build is claimed.

Both independent agent reviews agree at these stated scopes. Their reports
distinguish the circulation review's reused path producer from its separate
edge and flow acceptance code.

## Depth-two classification and separation

I solved the two odd steps directly. For `n=1 mod 16`, the first division
exponent is two. Requiring the second odd iterate to be 1 yields
`n=(2^(b+2)-7)/9`; integrality forces `b=6m+2`. Excluding n=1 gives exactly
the stated family with m>=1. Four literal steps on `2n-1` produce
`2^(6m+1)-1`.

The full known orbit is explicit, including its eventual 1,2 cycle. Its
maximum is `(8*64^m-2)/3`. Every displayed target value exceeds that maximum,
so the separation permits an arbitrary clock on the known arm, not just
equal clocks. The target formula is used only while its parities make each
step legal. The odd-clock lower bound grows with m while the source depth
stays two. This refutes a uniform clock bound depending on that depth alone;
it does not refute height-dependent transport or prove nonconvergence.

The root implementation imports no author routines. It reconstructs the
whole known orbit, both target clocks, the Mersenne endpoint, and the converse
classification on a separate bounded fixture set. The normal and optimized
outputs are compared by `replay_packet.py`.

## Integration boundary

No combination above supplies a bound on the creation of primes, a finite
oriented defect moment for a hypothetical separating invariant, or a
well-founded target-certificate recursion. Those remain precise missing
mathematical inputs. Neither checks of large integers nor repository
integrity validation can substitute for them.
