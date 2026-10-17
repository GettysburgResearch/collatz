# Restricted rational-base integer search

## Common normal form

Many active maps can be written as

```text
q*x_(n+1)=p*x_n+d_n,
p>q,
d_n in a restricted finite alphabet.                  (1)
```

A finite directive selects one residue cylinder. An ordinary input corresponds to a terminating least-significant address; an infinite forward survivor requires every later digit to stay allowed.

## Current examples

```text
PR35:
  base 5/4, bottom digits restricted to {0,1};

ADEL centered tail:
  base 81/64 with state-dependent digits {-1,0,1}
  and eventual-zero appended input blocks;

PR3 collision chart:
  induced base N/M with a sparse collision digit alphabet;

phase-34 quotient refund:
  nonstationary rational base with a growing exact quotient state.
```

## Literature lesson

The canonical full-digit rational-base system gives every nonnegative integer one finite expansion. Restricted alphabets are different. The integer representation tree is highly nonregular and has pairwise distinct rooted subtrees. Therefore:

- a finite modular automaton is generally only a projection;
- an exact forward machine may genuinely require the current integer as state;
- finite-state failure is not evidence of emptiness;
- an infinite transducer or one-counter nucleus is a natural positive target.

## Proof-producing search interface

At depth `n`, store:

```text
least positive root;
complete residue frontier;
exact meet-in-the-middle composition law;
rooted-subtree signature;
first forbidden digit;
ordinary-height lower bound;
state needed to pass from depth n to n+1.
```

A positive result must provide stabilization of one least root or a forward invariant ordinary root. A negative result must prove the least root tends to infinity or that every exact subtree eventually emits a forbidden digit.

## Conjectural inputs

Recent normality conjectures for minimal/maximal rational-base words would rule out several restricted-digit survivors. They are diagnostics only and must remain labelled conjectural.