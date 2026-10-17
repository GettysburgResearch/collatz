# Independent in-session reconstruction of the source-budget packet

Date: 2026-10-18 (Asia/Jerusalem).

**Verdict: the audited claims are VERIFIED for their stated scope. No blocking
mathematical issue was found. The global coverage problem remains OPEN.**

Here, VERIFIED is a scoped review label: the reviewer independently reconstructed
the displayed arguments and checked the identified physical witnesses. This is
an in-session agent review, not a formal proof build, an external peer review,
or a project acceptance decision. The packet's project status remains PROPOSED.
No verdict on an entire older PR is imported by citing one of its interfaces.

## Frozen material reviewed

The complete text of each file below was read. Its Git blob identifier was
independently recomputed from its bytes and matched to the supplied identifier.
All paths are relative to the repository root.

| File | Verified Git blob |
|---|---|
| `research/paired-comparison/source-budget/TERNARY_SPLICE.md` | `e970c4fcff6f925c809a81963030585b525cbde1` |
| `research/paired-comparison/source-budget/RESTART_BUDGET.md` | `367f7ec96b9b51056f26570a9d33edc42624ab36` |
| `research/paired-comparison/source-budget/README.md` | `a03714ba0947d2c74704764779dfbe627ad2d4b6` |

The complete reviewed content commit is
`cf1186fd414b365bf9fad68fc9f3b7b2a02cd3a7`, tree
`833c6f70cf79a40a90379e746a9c1559225a302d`. These blob identifiers bind
this review to the exact proof bytes even after an additive publication receipt.
`SOURCES.json` was read to check the scope of the credits. In particular, the
packet retains the prior distinction between the 4N+3 and 8N+3 guards, credits
the point-preserving affine lift, and does not transfer the R-return rank or
the persistent-clock theorem to a reset comparison without justification.

## Claim-level disposition

| Claim | Disposition | What was reconstructed and what remains outside its scope |
|---|---|---|
| TSB-001 | VERIFIED for stated scope | Both physical words and their different clocks; positivity and integrality; the exact immutable-root inequality; the sharp threshold a>=4 at the original source; and the obstruction to reusing this guard after an odd shortcut step. It is an initial-source exclusion, not a recurrent return theorem. |
| TSB-002 | VERIFIED for stated scope | The CRT compatibility for every r>=6 and a>=4; exact first-run length and v2(C)=1; failure of the specified older candidate; success of the new candidate; and the minimum of the entire displayed original arm. The congruences are conditions on the original input, not a theorem forcing every input to satisfy them. |
| TSB-003 | VERIFIED for stated scope | The literal 90303/14847 witness and its full affine lift, including all source parities, endpoint equality, 6m<N, every upper state>N, and failure of both specified valuation tests. No claim of failure of all earlier methods is inferred. |
| TSB-004 | VERIFIED for stated scope | The complete 34-state smaller-source bank below 27, its closure under the unabsorbed map, and first intersection with the 27 arm at time 59. The quantifier over all companion clocks is justified by finite closure. This disproves a universal requirement of merger strictly before ordinary descent. |
| RSB-001 | VERIFIED for stated scope | The complete odd/even valuation alternatives and the exact companion attached to the original root. A physically legal companion is still subject to its own root-order test. |
| RSB-002: ledger | VERIFIED for stated scope | The exact affine recurrence, positive correction sum, normalized increasing quantity, necessary accumulated valuation balance, and bounded loss of root safety within the odd-parameter corridor. The strict accumulated inequality is stated for a nonempty chain. |
| RSB-002: guarded normalizer | VERIFIED for stated scope | One common contracting integer rank M-3 under the actual guard; the M=3 core certificates; termination in MERGE or FAILED_DEBT_GUARD; the explicit upper-clock bound including the preexisting clock; and actual admission of arbitrarily large valuation types. The guard is not proved universal. |
| RSB-003 | VERIFIED for stated scope | The upper bound with exponent log_2(3), the exact unbounded family attaining that order, the failure of a fixed multiplicative slack bound, and every-state no-descent. Sharpness refers to the exponent, not an optimal numerical constant. |
| RSB-004 | VERIFIED for stated scope | The expanding five-step words; exact valuation countdown; CRT families with all displayed parameters odd, including the terminal one; and whole-prefix no-descent. Increasing the prescribed length changes the ordinary source. |
| RSB-005 and the README's full-proof target | OPEN | No argument forces entry into a successful initial guard or gives a valid continuation at every failed debt or initial root-order guard. Neither nontrivial positive cycles nor divergent positive orbits are excluded globally. |

The README is consistent with these scoped statements. It does not claim a
full proof or treat a terminating partial normalizer as a universally successful
merger algorithm.

## Main reconstruction details

### Physical splice and its root-order boundary

For the 4Z+3 construction, b is odd. The successive lower-arm block endpoints
are therefore obtained with exact parity information:

    2^a b-1 -> 4Z+2 -> 2Z+1 -> 3^(r+1)u-1 -> E.

The block lengths are a, 1, r+1, and 2. The hard first-exit assumption makes
the final two steps actual halvings and identifies E with T^(r+2)(Z).

The comparison against the immutable root is exact:

    m<N  iff  2^a(4Z+3)<3^a(N+1).

At Z=N, the three exceptional small exponents were checked separately;
they make m>N. Every admissible a>=4 makes m<N. A later checkpoint Z>N does
not inherit this conclusion merely from a>=4. Moreover, 3^a|4Z+3 with a>=1
forces 3|Z. After any actual odd shortcut step all subsequent states remain
units modulo three. The frozen text explicitly records this limitation.

For TSB-002, the two conditions on u have coprime moduli 16 and 3^a. The
dyadic condition supplies an odd u and exact v2(C)=1. The order failure of
the old candidate is the strictly positive quantity

    ((3^r-8*2^r)u+5)/8,  r>=6.

The endpoint and all intermediate upper states were reconstructed, rather
than inferring whole-arm no-descent from the last endpoint alone.

### Common rank and physical clock bound

For a hard H return, normalize its output with k and epsilon and write

    gamma=3^(k+1)/2^(2k+epsilon),
    A=gamma*3^s/2^(s+2).

The exact formula is M'=A(M+1)-gamma/4. The stated guard gives A<=3/4, so

    0<=M'-3<(3/4)(M-3).

This is a genuine common integer rank for admitted returns. It directly
preserves M<N and does not depend on spending an old companion-clock slot
again. The guard cannot hold at M=3. The two explicit core certificates
cover precisely its possible parameters C=1 and C=2.

The clock estimate was checked including both final failure and final merger
cases. At every admitted input, 3^(k+1)<=M<=M_0 and 2^s<=M+1<=M_0+1.
These bound each iteration by B_0. At most J admitted hard iterations plus
one final iteration give advance at most (J+1)B_0 from the supplied H
checkpoint. The original clock is at most a+(J+1)B_0. The earlier a steps
are not omitted or counted as part of the new logarithmic bound.

The construction with output k=2s was also checked symbolically. Its guard
reduces to 27^s<=32^s*2^epsilon. For epsilon=1 the final odd-valuation merger
adds exactly 4s+2 upper steps, giving total 5s+8 from the stated original
source. This establishes actual unbounded valuation types within the partial
language; it does not establish their eventual occurrence for every source.

### Exact obstruction families and complete clock control

The sharp-exponent family has the exact identities

    9N+13=208*2^s,   4M_1+3=39*3^s.

They prove the asserted growth order independently of floating-point logarithm
calculations. The finite expanding-run family uses exact valuation 5K+1,
which is necessary for the stated odd terminal parameter. A weaker condition
of merely at least 5K would not supply that parity.

For the stronger positive affine family, independent parity induction gives

    T^8(90303+1632586752t)
      =T^26(14847+268435456t)
      =771464+13947137604t,  t>=0.

Every upper-prefix slope and intercept exceeds its corresponding original
source coefficient and intercept. The exact margins N-6m and M_old-N are
the positive expressions printed in the proof. The common endpoint at the
base sources is the only intersection of the two displayed finite prefixes.

For 27, each source 1 through 26 was independently followed to 1. The union
was reconstructed as exactly

    {1,...,26} union {29,32,35,38,40,44,53,80}.

Every element's unabsorbed successor is in that set. The 27 arm misses it
at all times 0 through 58 and reaches 23 at time 59. The smaller witnesses
there are 23 at clock zero and 15 at clock one. This supplies the all-clock
quantifier without a truncation assumption on companion stopping times.

## Independent finite evidence and its limits

The reviewer's standalone `independent_checks.py` imports no repository
generator or proof kernel. It uses raw shortcut steps and affine parity
induction, with explicit exceptions rather than optimizable assertions. It
was run normally and under -OO with identical passing output. The frozen copy
in `experiments/paired-comparison/source-budget/` was byte-compared against
the executed copy; both have SHA-256
`b76a1a735a1411616f4eef2e5551551bfc3339f22a083f45c5fc63a7886f17cb`.

Its recorded scope is 2,000 odd-valuation and 2,000 even-valuation raw cases;
1,999 old R-return cases; 435 finite expanding-return stages; 6,667 exact
hard-return ledger cases including 1,426 guarded contractions; 14
sharp-exponent members; and 126 complete 4Z+3 CRT affine families. It also
checks the additional whole families identified in its output and rejects a
changed source-parity word. The final 90303 family and complete 27 bank were
additionally reconstructed separately during this frozen-version review.

These checks supplement the algebraic arguments. They do not promote finite
enumeration to an all-input proof, certify every repository artifact, or
constitute a formal theorem-prover build. The integrating execution report
records the separate certificate-verifier, mutation-control, and checkout
validation results; this review does not substitute for those execution
receipts.

## Remaining proof obligation

The global obligation is still to provide an ordinary descent or a physically
certified merger with a smaller original source for every N>1. This packet
proves additional initial-source exclusions and a terminating partial return
language. Its failed guards remain real, explicitly preserved outcomes.

A replacement companion must be below the same original N. Reusing a finite
bank does not itself advance its members' actual clocks. A rank proved only
inside one comparison relation cannot be reset at another relation without
a justified interface. The frozen packet respects these restrictions; it
does not yet resolve them for every possible continuation.
