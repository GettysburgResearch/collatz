# Claim inventory — six-branch ordinary extraction

This isolated `74xx` namespace belongs to issue #58. It does not modify any canonical or competing root ledger.

| ID | Kind | Title | Status | Dependencies |
|---|---|---|---|---|
| `D-7401` | Definition | Six-branch minimal-word extraction system | PROPOSED | elementary arithmetic; branch-qualified physical mapping only |
| `L-7401` | Lemma | Exact high-quotient section and immediate language exit | PROPOSED | `D-7401` |
| `T-7401` | Theorem | Affine high-quotient section rigidity | PROPOSED | `D-7401`, `L-7401` |
| `Q-7401` | Open question | Boundedness versus escape of the least ordinary roots | IDEA / GLOBAL BLOCKER | `D-7401`, `T-7401`, PR #57 `T-7601/T-7603` |

## Logical chain

```text
fixed six-branch physical chart
  -> exact stationary rational-base system D-7401
  -> nested positive root sets S_n
  -> ordinary survivor iff least roots m_n stabilize

positive decision:
  stable m_n
  -> one written ordinary root
  -> branch-qualified physical replay
  -> K-candidate;

negative decision:
  m_n -> infinity
  -> no ordinary root in the complete language
  -> entire fixed architecture eliminated.
```

## New obstruction

```text
L-7401:
  direct high quotient exits the language immediately;

T-7401:
  every six-state integer-affine self-section
  is forced to be the original forward map.
```

The obvious recursive extraction mechanism is therefore unavailable. The remaining target is ordinary height, not another local encoding.