# Claim inventory — linear quotient refund

This isolated `85xx` namespace belongs to issue #43. It does not edit any canonical root ledger.

| ID | Kind | Title | Status | Dependencies |
|---|---|---|---|---|
| `D-8501` | Definition | Linear-height phase-34 connector-refund class | PROPOSED | PR3 `L-0016`, `L-0031` |
| `L-8501` | Lemma | Every fixed linear stage width eventually refunds the next radix | PROPOSED | `D-8501`, PR3 scaled-tail identity |
| `L-8502` | Lemma | Ordinary inverse carry and six-bit connector normal form | PROPOSED | `D-8501` |
| `T-8501` | Theorem | Deterministic expanding residual-counter criterion | PROPOSED | `L-8501`, `L-8502` |
| `T-8502` | Theorem | Quadratic cylinder pressure and zero-dimensional completion set | PROPOSED | `D-8501` |
| `T-8503` | Theorem | Eventual periods through 58 are irrational and nonordinary | PROPOSED / SOURCE-DEPENDENT | Väänänen–Wallisser 1991 |
| `L-8503` | Lemma | Complement quotients parametrize every local refunded connector | PROPOSED | `D-8501`, `L-8502` |
| `T-8504` | Theorem | One complement counter is a complete local counterexample state | PROPOSED | `L-8503`, physical tower replay |
| `L-8504` | Lemma | Refund states are intrinsic unimodular physical markers | PROPOSED | `L-8503`, physical tower replay |
| `T-8505` | Theorem | Every infinite refund path has unbounded odd-prime support | PROPOSED / SOURCE-QUALIFIED | `L-8504`, Evertse 1984 Corollary 1 |
| `L-8505` | Lemma | Primitive refund cores satisfy one exact Syracuse equation | PROPOSED | `L-8504`, local signatures |
| `T-8506` | Theorem | Every legal connector adds more than 170 primitive-core bits | PROPOSED | `L-8505`, `3^53>2^84` |
| `T-8507` | Theorem | Intrinsic primitive-core decoder and physical conjugacy | PROPOSED | `L-8504`, `L-8505`, physical replay |
| `L-8506` | Lemma | The core decoder compiles into eight exact ordinary blocks | PROPOSED | `T-8507` |
| `L-8507` | Lemma | Eight core blocks reduce to four type-independent top-boundary cylinders | PROPOSED | `L-8506`, `T-8507` |
| `T-8508` | Theorem | Every noncanonical top-boundary lift is uniformly refunded | PROPOSED | `L-8507`, `3^665>2^1054` |
| `L-8508` | Lemma | Consecutive canonical lifts force a long zero top block | PROPOSED | `L-8507`, `3^971<2^1539` |
| `T-8509` | Theorem | Canonical lift runs are uniformly bounded | PROPOSED | `L-8506`, `L-8507`, `T-8507` |
| `L-8509` | Lemma | The four continuation residues share all but six top-boundary bits | PROPOSED | `L-8506`, `L-8507` |
| `L-8510` | Lemma | Top-cell transport is one base-64 multiplier with bounded carry | PROPOSED | `L-8509` |
| `T-8510` | Theorem | One late noncanonical lift forces permanent accelerating refund | PROPOSED | `L-8507`, `T-8508`, `T-8509` |
| `T-8511` | Theorem | Multiplicative quotient refund is absorbing after cylinder domination | PROPOSED | elementary integer arithmetic |
| `T-8512` | Theorem | Permanent refund generates an unbounded ordinary quotient stack | PROPOSED | `T-8510`, `T-8511` |
| `L-8511` | Lemma | Every six-bit router is affinely conjugate to the physical type alphabet | PROPOSED | `L-8509`, `L-8510` |
| `T-8513` | Theorem | Permanent refund prepays a linearly growing complete future cylinder | PROPOSED | `L-8507`, `T-8510`, `T-8512` |
| `L-8512` | Lemma | The intrinsic Hensel quotient routes through the fixed toll alphabet | PROPOSED | `T-8507`, `L-8506` inverses |
| `Q-8501` | Open question | One forever-defined ordinary primitive core | OPEN | `L-8511`, `L-8512`, `T-8510`--`T-8513` |
| `X-8501` | Experiment | Exact refund, carry, decoder, and cutoff audit | EMPIRICAL | `L-8501`--`T-8503` |
| `X-8502` | Experiment | Exact complement-quotient and growth audit | EMPIRICAL | `L-8503`, `T-8504` |
| `X-8503` | Experiment | Unimodular physical marker and prime-turnover audit | EMPIRICAL | `L-8504`, `T-8505` elementary gates |
| `X-8504` | Experiment | Exact primitive-core signature and coprimality audit | EMPIRICAL | `L-8505`, `T-8505` |
| `X-8505` | Experiment | Intrinsic primitive-core decoder reconstruction | EMPIRICAL | `L-8505`, `T-8506`, `T-8507` |
| `X-8506` | Experiment | Eight-block ordinary core compiler audit | EMPIRICAL | `L-8506` |
| `X-8507` | Experiment | Type-independent top-boundary quotient refund audit | EMPIRICAL | `L-8507`, `T-8508` |
| `X-8508` | Experiment | Canonical-run length and refunded-density audit | EMPIRICAL | `T-8509` |
| `X-8509` | Experiment | Common prefix, base-64 carry, and absorption audit | EMPIRICAL | `L-8509`, `L-8510`, `T-8510` |
| `X-8510` | Experiment | Affine physical-type alphabet audit | EMPIRICAL | `L-8511` |
| `X-8511` | Experiment | Unimodular Hensel quotient and fixed toll-alphabet audit | EMPIRICAL | `L-8512` |

## Logical chain

```text
PR3 physical tower identity
  -> D-8501 exact linear connector system
  -> L-8502 causal inverse/cell compiler
  -> L-8503 complement quotient k
  -> T-8504 deterministic partial map (t,i,k)
  -> L-8504 intrinsic physical marker
  -> L-8505 exact prime-to-six core equation
  -> T-8507 deterministic partial map (t,gamma,i,C)
       one high binary divisibility + one six-bit gate
       legal => C_next > 2^170 C
  -> L-8506 eight exact ordinary blocks
  -> L-8507 four complete continuation cylinders
       m=rho+H*ell -> m_next=sigma+3^G*ell
  -> L-8509 one common long prefix plus six routing bits
  -> L-8510 one base-64 multiplier/carry transducer
  -> L-8511 normalized routing symbol is the physical type itself
  -> T-8509 canonical runs have bounded length
  -> T-8510 every infinite path is eventually permanently refunded
  -> T-8512/T-8513 a current finite integer generates and prepays
       a linearly growing exact future-cylinder horizon
  -> L-8512 the alternative Hensel quotient has
       [[2^D,a],[3^G,h]] in SL_2(Z)
       and four residues Lambda+U*{9,54,36,24}
  -> Q-8501 one finite forever-defined physical core
  -> explicit positive unbounded Collatz orbit.
```

Every hypothetical infinite branch additionally satisfies `T-8505`: consecutive prime-to-six cores are coprime, the full core is replaced at every connector, and infinitely many globally new odd primes enter the physical boundary shifts.

The currently open theorem is **entry and exact routing**, not drift, state reconstruction, periodic control, or stack capacity. One finite integer must make its generated ordinary quotient hit the next affine fixed-alphabet cylinder forever.