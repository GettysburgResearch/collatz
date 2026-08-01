# Strategic outlook at the 2026-08-01 cutoff

**Status:** strategic interpretation, not a proof.  
**Project status:** Collatz remains unsolved.

## Principal spine

The first integration pass adopts the following as the clearest repository-wide organizing framework:

```text
SC* + FC* => Collatz
```

More precisely, in a least-positive-counterexample architecture:

- **Lane A:** every coefficient prefix is supercritical. `SC*` excludes one fixed ordinary source from surviving this lane indefinitely.
- **Lane B:** a first coefficient crossing occurs. `FC*` excludes every complete first-crossing realization, including a minimum rotation of every nontrivial positive cycle.

The reviewed work makes the split and its interfaces serious and logically useful. It does not prove either global obligation.

## SC*: fixed-source ordinary extraction

The verified infrastructure says:

```text
least all-supercritical sources escape
  <=>
every fixed positive integer has finite coefficient stopping.
```

It also says an ordinary all-supercritical orbit would diverge to `+infinity`. The remaining theorem must concern **one fixed positive integer**. It cannot be replaced by:

- one compatible source at each finite depth;
- a 2-adic completion;
- positive drift on prescribed words;
- entropy or dimension of a path family;
- a finite-state controller.

The strongest connection to pursue is a bridge from Lane-A numerator/endpoint prime-rank growth to positive ordinary source or endpoint height. Current unit-equation and cusp results force rank escape but do not yet turn it into source escape.

## FC*: complete first crossing and full denominator

The verified infrastructure gives:

- exact source/endpoint/displacement equations;
- finite decision for a fixed first-crossing word;
- cycle absorption into the first-crossing lane;
- primitive/injective cycle reduction;
- support loss and roughness windows;
- complete-factor synchronization and quotient jets;
- coprime resultant-root normal form;
- several bounded-support or fixed-family exclusions.

The missing result is uniform and global. Every prime-power factor of `2^j-3^q` must return the same ordinary displacement, source, and endpoint, with exact physical replay. Proper-factor hits and independently selected local solutions are not enough.

Two frontier cases remain especially visible:

- **balanced:** two large unitary factor blocks must return identical ordinary data;
- **dominant:** one giant prime-power block returns the small ordinary data and a small cofactor completes divisibility.

The `gcd(j,q)>1` homogeneous components also remain open.

## Cross-program connections worth preserving

### Extraction theorem as a universal firewall

PRs #3, #56, #57, and #60 independently converge on the same ordinary-boundary theorem. This should be a mandatory interface for every schedule-first, automata, completion, or controller construction.

### Periodicity routes directly to the full denominator

Finite-state ordinary foundries collapse to eventual periodicity. Periodic positive tails are exactly cycle/full-denominator objects. Therefore finite-state feedback should route into FC*, not be treated as a separate divergence mechanism.

### Support loss lowers jet-lifting thresholds

PR #81's support-sensitive remainder loss lowers the common fixed-point height. That can reduce the modulus size needed for PR #83's quotient jets to determine exact ordinary data. The proposed post-review `L-7610` develops this connection but remains unreviewed.

### Finite automata need exact safety kernels

Weak SCC or weak-component heuristics are unsafe. For a genuinely finite relation, compute the exact predecessor closure of the bad set and the maximal safety kernel. This is useful locally but does not solve the infinite arithmetic extraction problem.

### Algebraic rigidity is a method boundary

The six-branch rigidity packet and its reviewed generalization show that finite tame algebraic sections do not supply a hidden descent nucleus. This removes a broad method class but does not decide whether an isolated infinite ordinary survivor exists.

### Pulse/resultant families can feed FC*, but are not FC*

Fixed-support and fixed-cycle pulse exclusions are genuine infinite-family results. A resolution-relevant bridge would compile arbitrary first-crossing words into a finite family of resultants that collectively control the complete denominator, including fresh primes and exact replay.

## Assessment

A serious logically exhaustive program is present. It is not a near-proof. Both missing theorems are global:

- SC* is a fixed-source ordinary-extraction theorem.
- FC* is an all-word, all-factor, complete-denominator nonexistence theorem.

The next research should be judged by whether it closes one of these exact gaps or sharpens a lossless interface into them, not merely by the size of another finite census.
