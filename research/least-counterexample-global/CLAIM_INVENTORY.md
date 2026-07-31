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
| `Q-6501` | Open question | Close both exhaustive coefficient-stopping lanes | OPEN / GLOBAL BLOCKER | all above; PR #76--#77 |

## Logical chain

```text
least positive counterexample
  -> D-6501
  -> exactly one of:

Lane A: all coefficient prefixes are supercritical
  -> PR77/T-6709: actual orbit tends to +infinity
  -> L-6501: odd correction product <= e^(7/9) k^(1/9)
  -> T-6501: coefficient records >= const*r^(8/9)
  -> T-6503: every fixed low-surplus band has O(k^(1/9)) visits
  -> remaining sparse-return, unbounded-record ordinary orbit

Lane B: finite first coefficient crossing
  -> T-6502: cofinal harmonic rational-approximation window
  -> L-6502: exact finite ordinary candidate list for each word
  -> remaining uniform exclusion of all crossing words and cycles.
```

## Full-objective status

```text
Lane A excluded + Lane B excluded
  -> no least positive counterexample
  -> Collatz true.
```

Neither lane is currently fully excluded. No proof of Collatz, positive cycle, divergent seed, or counterexample is claimed.
