# Independent review: certifying semiprime representatives

**VERIFIED at the stated written, source-qualified scope**, with an independent finite replay. The existence and termination theorem remains conditional on the named analytic inputs in the source packet; the replay does not certify those inputs or prove Collatz convergence.

## Frozen review boundary

- `research/astra-collision-factor-bridge-20261128/SEMIPRIME_REPRESENTATIVES.md`: SHA-256 `fc7e34ce599ccbcb73c9fd85ab4116b282640e2ef2932a95b282db0f699af51f`.
- `research/astra-collision-factor-bridge-20261128/semiprime_representative.py`: SHA-256 `43e2af9c7c647ff139343e9f1c552f9e134d0870f7cc6840d8c296fc3d34dab3`.
- `reports/astra-collision-factor-bridge-20261128/semiprime-representatives.json`: SHA-256 `2402c22eaa5d751b82d6c2a119b4dacf73241121c583d0d750fcdd6e86095fe1`.

## Mathematical reconstruction

The exact family B has binary length b≥4, smaller prime p>b and 4p≤b². Since log n < b log 2 < b, the lower S inequality holds. The estimate log n≥(b−1)log2≥b/2 follows from log2>2/3 and b≥4, proving the upper S inequality. Conversely, every Matomäki–Teräväinen interval witness used by the incidence proof eventually lies in B: its factor between log^1.09 x and log^1.1 x eventually dominates b and is below b²/4, while b is asymptotic to log x/log2. The exact family retains the same short-interval lower supply and inherits the S residue-class upper bound. Mere containment B⊂S would not have sufficed; the note correctly includes the extra supply check.

The fixed-target conclusion is stronger than mere component intersection, and the proof handles that distinction. At the native comparison clock t≈(1/4)log₂X, every state in either relevant source prefix is at least X/2^t, up to the bounded source interval adjustment, hence is above any fixed target v for large X. Thus a successful prefix merger occurs before any visit to v. If one source later visits v, the other follows the same tail to v. The target indicator is invariant above v, which is sufficient here; global invariance is not silently assumed. Mazur is applied at full-map target 2v to obtain positive shortcut predecessor density.

The initial source normalization terminates because the 2-adic valuation of a positive multiple of three is finite; its eventual odd departure is prime to three. No convergence to one is needed. A fixed semiprime predecessor s of the resulting v and its finite visit time t are both inspected at every sufficiently large dovetail stage k≥max(bitlength(s),t). This establishes source-qualified totality without a uniform bound on s, t or runtime. From the genuine certificate n→v←s, convergence of s implies convergence of n by forward invariance of the known cycle.

## Finite consumer reconstruction

Candidate enumeration is complete at the stated finite cutoff: each possible p is at most bitlength(maximum)²/4, p is odd, and all eligible q>p are odd and appear in the enumerated range. Stopping an arm on its first repeated state cannot miss a new target, since every state on the future cycle was already inspected. Search bounds remain explicit and unresolved inputs are reported.

An independent replay read the existing JSON, tested primality by a separate exhaustive divisor loop, reconstructed binary length with integer powers, checked the exact family inequalities, origins and common endpoint, and verified every edge by the equations 2y=x for even x and 2y=3x+1 for odd x. It did not import the producer, call its checker, or run a new source search. The accompanying JSON records all reviewed hashes and witnesses.

The replay passed **7 certificates and 214 actual edges**. Its evidence is limited to those finite witnesses.
