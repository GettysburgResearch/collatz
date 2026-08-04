# Q-8402 — Ordinary path in a near-critical pulse fiber

Claim ID: `Q-8402`  
Title: Can one finite ordinary marker survive a supercritical fixed-weight negative-cycle fiber forever?  
Status: `IDEA / PRIMARY DIVERGENT-ORBIT TARGET`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-8405`, `T-8402`; branch-qualified PR #51 `L-8002/T-8002`; branch-qualified PR #49 `T-8504`  
Scope: ordinary positive paths in the negative-three-cycle pulse chart

## Exact target

For one supercritical pair `(L,b)`, let

```text
M=2^(3L+b),
N=9^L,
D_(L,b)={d_w : w in {A,B}^L, |w|_B=b},
```

with output digits `e_w` from `L-8405`.

Construct one explicit finite integer

```text
h_0>3
```

such that, for every `r>=0`, there is one branch word `w_r` satisfying

```text
h_r=M q_r+d_(w_r),
h_(r+1)=N q_r+e_(w_r).                                (1)
```

Then

```text
n_0=-5+2h_0
```

is an unconditional positive Collatz counterexample by `T-8402`.

The smallest laboratory is

```text
(L,b)=(6,1),
M=524,288,
N=531,441,
|D|=6.                                                 (2)
```

The first very large near-critical laboratory is

```text
(L,b)=(53,9),
M=2^168,
N=9^53,
|D|=4,431,613,550.                                    (3)
```

## Equivalent quotient map

For a current branch `i` and prospective next branch `j`, write

```text
h=Mq+d_i.
```

Continuation is the exact congruence

```text
(N-M)q+e_i congruent d_j mod M.                        (4)
```

Because `N-M` is odd, every ordered branch pair has one quotient class

```text
q=rho_(i,j) mod M.                                    (5)
```

Writing

```text
q=rho_(i,j)+M ell
```

gives an exact refunded successor

```text
q'=sigma_(i,j)+N ell.                                 (6)
```

Thus `(2)` is a constant-modulus sibling of the changing-modulus quotient maps
in PR #51 and PR #49:

```text
one exact cylinder
+ one ordinary quotient
+ one odd multiplicative refund
+ infinite definedness as the sole positive gap.
```

A finite-state projection of `(5)`--`(6)` is not enough. The certificate must
retain the actual most-significant boundary of the finite integer quotient.

## Candidate approaches

### A. Proof-carrying one-counter nucleus

Find finitely many quotient cones

```text
(type i, low exact block, lower bound on ell, top-boundary state)
```

that are closed under `(5)`--`(6)`. The top-boundary component must prove that
leading digits are created by the odd refund rather than supplied by an inverse
limit.

### B. Run-core transfer

Use PR #51's maximal-run quotient normal form. Its update

```text
k=rho+2^E ell -> k+=sigma+9^(r+1)ell
```

has the same architecture. A top-boundary lemma proved for either map should be
translated to the other. The run-five condition gives pointwise physical growth;
`T-8402` gives macro growth for every branch of the fixed-weight chart.

### C. Integer-first synthesis

Search forward from a finite quotient, not backward from an infinite directive.
Every proposed state must directly replay the physical accelerated valuations.
A long prefix is useful only if its surviving top block admits an inductive
description.

### D. Completion-height obstruction as adversary

If no invariant is found, prove that every finite top-boundary machine forces
ultimately periodic or efficiently recurrent branch output and invoke the
ordinary repetition/value obstructions. Such a theorem must explicitly retain
unbounded quotient growth; a residue-only lasso is merely a `2`-adic ghost.

## Mandatory positive certificate

Before assigning a `K-84xx` identifier:

1. publish the finite integer `h_0` and physical seed `n_0=-5+2h_0`;
2. state the finite inductive state and transition rule;
3. prove every branch domain and all advertised accelerated valuations;
4. prove the top boundary remains finite and canonical at every step;
5. prove all-time definedness;
6. invoke the strict macro growth from `T-8402`;
7. replay an independently checkable prefix and the symbolic induction;
8. request an adversarial review independent of the construction.

## Current finite evidence

`X-8403` computes the complete least positive cylinders of `(2)` through depth
`8`. They grow from `19,416` to a `129`-bit integer. This neither proves
nonexistence nor supplies a candidate.

PR #51 supplies explicit reset highways of unbounded finite depth and a sharper
changing-modulus run-core quotient. PR #49 supplies a second exact refunded
one-counter map whose legal states at least double. None currently contains a
forever-defined finite state.

## Failure boundaries

- a compatible `Z_2` point is not an ordinary integer;
- a periodic branch word is not a growing ordinary initialization;
- an SCC in a fixed residue quotient is not a top-boundary proof;
- exponential branch count is not ordinary realization;
- a finite reset family with a changing initial seed is not one infinite orbit;
- no counterexample is claimed until every item in the positive certificate is
  met.
