# L-8401 — Exact critical product gate for a positive cycle

Claim ID: `L-8401`  
Title: Every positive accelerated cycle lies in an explicitly tiny upper rational-approximation window to `log_2(3)`  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: elementary accelerated Collatz algebra  
Scope: every positive periodic orbit of the accelerated odd Collatz map

## Setup

Let

```text
n_0,n_1,...,n_(k-1)
```

be the odd members of a positive cycle, indexed cyclically, and put

```text
a_i=v_2(3n_i+1)>=1,
2^a_i n_(i+1)=3n_i+1,
A=sum_i a_i.
```

## Statement 1 — exact product identity

```text
boxed:
2^A/3^k=product_(i=0)^(k-1)(1+1/(3n_i)).             (1)
```

In particular,

```text
A/k>log_2(3).                                         (2)
```

### Proof

Rewrite each local equation as

```text
2^a_i n_(i+1)=3n_i(1+1/(3n_i)).
```

Multiply all `k` equations.  The cyclic products of the `n_i` cancel, leaving
(1).  Every factor on the right is greater than one, proving (2). **QED**

## Statement 2 — a lower state bound forces critical slope

If

```text
n_i>=X>0
```

for every member of the cycle, then

```text
boxed:
0<A/k-log_2(3)
 <=log_2(1+1/(3X)).                                  (3)
```

The weaker elementary estimate

```text
A/k-log_2(3)
 <1/(3X log(2))                                      (4)
```

also follows.

### Proof

Every factor in (1) is at most `1+1/(3X)`.  Take base-two logarithms and divide
by `k`.  The inequality `log(1+t)<t` gives (4). **QED**

## Statement 3 — fixed ratio two is trivial

If `A=2k`, then the cycle is the trivial cycle at `1`.

### Proof

Equation (1) becomes

```text
(4/3)^k=product_i(1+1/(3n_i)).
```

For a positive integer `n_i`, every factor is at most `4/3`, with equality only
at `n_i=1`.  Equality of the products forces every `n_i=1`. **QED**

## Consequence for search

A valid cycle search cannot select `(k,A)` merely because `D=2^A-3^k` is
smooth.  It must first prove that the ratio satisfies (3) for the certified
ordinary lower bound being used.

The repository's cycle literature distinguishes:

```text
k = number of accelerated odd steps,
m = number of local minima.
```

Neither is a substitute for the other.  Both the slope window and the relevant
minimum-count/odd-step bounds must be reported in a candidate certificate.

## Dependency audit

The identities above are self-contained.  Any numerical value for `X`, any
lower bound on `k`, and any lower bound on the local-minimum parameter remain
external inputs and must be cited separately.

## Gap audit

- The critical window is necessary, not sufficient.
- A good rational approximation to `log_2(3)` does not imply numerator
  divisibility.
- The lemma does not construct an orbit.
- It does not replace exact valuation replay.

## Adversarial tests

`X-8401` checks (1) on small exact cyclic controls and uses (3) only as a search
screen, never as a counterexample certificate.

## Suggested next attack

Use upper continued-fraction approximants satisfying the chosen `X`-window,
then compile valuation grammars at that scale without expanding their
trillion-symbol words.