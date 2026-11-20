# Global arithmetic closure attempt: ordered prime-height accounting

**Collatz remains unresolved.** This packet first tests exact flux at
every prime, preserves small counterexamples to that relaxation, then
retains time order to obtain a stronger necessary condition on arbitrary
positive ordinary cycles.

- [CLOCK_HEIGHT.md](CLOCK_HEIGHT.md): a localized prime-power return
  bound; quantitative height-weighted dispersion for growing prime pools;
  and the all-cycle inequality
  \(\log_2\max n\le s[8+12\ln(1+\log_2\max n)]\), where \(s\)
  is the number of primes across the whole cycle. A finite-prefix version
  retains the source explicitly. Proof status: PROPOSED pending review.
- [PRIME_CIRCULATIONS.md](PRIME_CIRCULATIONS.md): an extremal five-edge
  ordinary all-prime balance that is not a cycle, and a seven-source
  certificate forcing every globally nonincreasing completely additive
  potential to vanish on every power of five. Classical semigroup prior
  art is explicitly credited.
- [check_arithmetic_closure.py](check_arithmetic_closure.py) and
  [arithmetic-closure-report.json](arithmetic-closure-report.json): exact
  finite controls and rational clock-lemma checks; separately labeled
  floating-point diagnostics on actual ordinary trajectory prefixes.

The new maximum-height statement concerns **prime support**, not
multiplicative rank. Its peak-window proof is also a corollary of the
return-tail method in rStation Paper 138; no broad novelty claim is made.
The specific localization to \(\sum\ln^+\log_2 n_i\) is compared with
Papers 137--138 in the main note. All proofs here are elementary and do
not depend on the external papers' larger theorem stacks.

The first unsupported closing step is now explicit: the inequalities
require support to grow with height, but nothing supplied forces a
contradictory upper support bound or excludes the full cycle denominator.
Finite-prime observations, changing rational cycles, and an unordered
product identity do not discharge that obligation.

To replay the finite checks from this directory:

```text
python -X utf8 -B check_arithmetic_closure.py
```

The script uses explicit checks rather than Python assertions, so its
checks remain active under optimized execution. The written proof,
independent review, exact arithmetic controls, and floating-point sanity
checks are separate evidence levels.
