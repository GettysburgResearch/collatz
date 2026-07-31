# Claim inventory — least-counterexample global proof attack

This isolated `65xx` namespace belongs to issue #78. It does not modify canonical or competing root ledgers.

| ID | Kind | Title | Status | Dependencies |
|---|---|---|---|---|
| `D-6501` | Definition | Least-counterexample two-lane coefficient framework | PROPOSED | elementary algebra; branch-qualified PR #76--#77 |
| `L-6501` | Lemma | Distinct odd-source product bound | PROPOSED | `D-6501` |
| `T-6501` | Theorem | Polynomial coefficient-record growth | PROPOSED | `D-6501`, `L-6501` |
| `T-6502` | Theorem | Distinct-orbit paradoxical harmonic window | PROPOSED | `D-6501`, `L-6501` |
| `L-6502` | Lemma | Exact finite decision for every first-crossing cylinder | PROPOSED | `D-6501` |
| `T-6503` | Theorem | Fixed low-surplus bands have density zero | PROPOSED | `L-6501`, `T-6501` |
| `T-6504` | Theorem | Distinct-state packing forces `8/9` logarithmic mean surplus | PROPOSED | `L-6501` |
| `T-6505` | Theorem | Bounded-bank low-complexity first crossings are finite | PROPOSED / SOURCE-DEPENDENT | PR #81 repeated-factor separation; effective logarithmic forms |
| `L-6503` | Lemma | Divergent orbits generate a `3/2`-syndetic tail-minimum ladder | PROPOSED | elementary dynamics; PR #77 for Lane-A divergence |
| `T-6506` | Theorem | Ordinary Lane A lies on the critical-density boundary and has subexponential cusp returns | PROPOSED / SOURCE-DEPENDENT | López--Stoll Theorem 1; `L-6501`, `T-6503`, `T-6504` |
| `L-6504` | Lemma | Zero-rate canonical source/end cusp subsequence | PROPOSED / SOURCE-DEPENDENT | `T-6506`; parity-cylinder source/end duality |
| `R-6501` | Refutation | The four scalar Lane-A estimates do not imply ordinary exclusion | PROVED | elementary explicit binary construction |
| `Q-6501` | Open question | Close both exhaustive coefficient-stopping lanes | OPEN / GLOBAL BLOCKER | all above; PR #76--#77 |

## Logical chain

```text
least positive counterexample
  -> D-6501
  -> exactly one of:

Lane A: all coefficient prefixes are supercritical
  -> PR77/T-6709: actual orbit tends to +infinity
  -> L-6501: odd correction product <= e^(7/9) k^(1/9)
  -> T-6504: mean D >= (8/9) log_3 k - O_n(1)
  -> T-6503: every fixed low-surplus band has O(k^(1/9)) visits
  -> T-6506: liminf D_k/k = 0 and subexponential physical cusp returns
  -> L-6504: both canonical source and endpoint rates vanish on a subsequence
  -> L-6503: infinitely many tail-minimum counterexamples with gap <= 3/2
  -> remaining zero-rate 2--3 boundary / pointwise mixing obstruction

Lane B: finite first coefficient crossing
  -> T-6502: cofinal harmonic rational-approximation window
  -> L-6502: exact finite ordinary candidate list for each word
  -> T-6505: bounded-bank low-complexity cofinal families excluded
  -> remaining high-bank, high-complexity crossing words and cycles.
```

## Critical nonreduction

`R-6501` constructs an explicit binary word with

```text
D_k >= 0,
mean D >= (8/9) log_3 k - O(1),
max 3^D >= const*k^(8/9),
fixed low bands finite,
D_k/k -> 0.
```

Every finite prefix has positive ordinary representatives and the complete word has one exact `2`-adic realization. Therefore these scalar conditions, even with finite compatibility and inverse-limit completion, do not exclude ordinary realization. A closing proof must use the ordinary canonical boundaries, inverse-tree minimality, or pointwise orbit mixing.

## Full-objective status

```text
Lane A excluded + Lane B excluded
  -> no least positive counterexample
  -> Collatz true.
```

Neither lane is currently fully excluded. No proof of Collatz, positive cycle, divergent seed, or counterexample is claimed.
