# T-9404 — Finite-state directive-to-output complexity budget

Claim ID: T-9404  
Title: State/output resource lower bound for producing an ordinary survivor code  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: T-9402  
Scope: non-erasing deterministic sequential transductions of an infinite directive word  
Related counterexample candidates: issue #4 S-adic frontier; PR #3 marked grammars; no `K-####` candidate

## Definitions

Let `x=x_0x_1...` be an infinite directive word over a finite alphabet.  A
**non-erasing deterministic sequential transducer** consists of

```text
- a finite state set Qset, |Qset|=Q;
- a transition q_(i+1)=delta(q_i,x_i);
- a nonempty emitted word lambda(q_i,x_i);
- a uniform output-block bound 1 <= |lambda(q,a)| <= B.
```

Its output is

```text
y = lambda(q_0,x_0) lambda(q_1,x_1) lambda(q_2,x_2) ... .
```

Write `p_x(n)` and `p_y(n)` for the factor-complexity functions.

## Statement 1 — universal transducer bound

For every `n>=1`,

```text
p_y(n) <= Q*B*p_x(n).                    (1)
```

## Statement 2 — ordinary-survivor resource inequality

Suppose `y` is a nontrivial ordinary `64 -> 81` survivor code.  Then

```text
Q*B*liminf_(n->infinity) p_x(n)/n
  >= 1/(log_64(81)-1)
  = 17.654847577085... .                 (2)
```

In particular, if `x` is Sturmian or quasi-Sturmian, so that

```text
p_x(n)=n+O(1),
```

then

```text
Q*B >= 17.654847...,
```

and hence the integer resource product satisfies

```text
Q*B >= 18.                               (3)
```

Thus a bounded-output finite-state realization of the surviving Sturmian
directive needs at least eighteen state/output slots in this precise sense.

## Statement 3 — synchronized/local coding bound

Assume additionally that there is a fixed `R>=0` such that, away from the
initial boundary, the state before reading `x_i` is determined by the preceding
length-`R` input factor.  Then

```text
p_y(n) <= B*p_x(n+R) + R*B.              (4)
```

Consequently, for a Sturmian or quasi-Sturmian directive producing an ordinary
survivor,

```text
B >= 18.                                 (5)
```

A letter-to-letter fixed-radius coding has `B=1`, so **no finite-radius local
coding of a Sturmian or quasi-Sturmian directive can be a nontrivial ordinary
survivor code**.

## Proof of Statement 1

Take any length-`n` factor of `y`.  It begins inside a unique emitted block
`lambda(q_i,x_i)` at an offset

```text
0 <= a < |lambda(q_i,x_i)| <= B.
```

Because every input letter emits at least one output symbol, the `n` consecutive
input symbols

```text
x_i x_(i+1) ... x_(i+n-1)
```

emit at least `n` symbols after the chosen starting point: the remainder of the
first block contributes at least one symbol and each of the following `n-1`
blocks contributes at least one.

Therefore the output factor is completely determined by the triple

```text
(q_i, a, x[i:i+n]).
```

There are at most

```text
Q * B * p_x(n)
```

such triples, proving (1).

## Proof of Statement 2

T-9402 gives

```text
liminf p_y(n)/n >= kappa,
kappa = 1/(log_64(81)-1).
```

Divide (1) by `n` and take `liminf`:

```text
kappa
 <= liminf p_y(n)/n
 <= Q*B*liminf p_x(n)/n.
```

This is (2).  The Sturmian/quasi-Sturmian specialization has lower complexity
slope `1`, yielding (3).

## Proof of Statement 3

For a factor beginning in block `i>=R`, the state `q_i` is determined by
`x[i-R:i]`.  The output factor is therefore determined by

```text
(a, x[i-R:i+n]),
```

with at most `B*p_x(n+R)` possibilities.  Factors beginning in the first `R`
input blocks contribute at most `R*B` exceptional starts.  This proves (4).
Taking lower slopes and using T-9402 gives (5).  The fixed-radius
letter-to-letter case has `B=1` and is impossible.  **QED**

## Dependency audit

Only T-9402 is used for the ordinary-code lower bound.  The transducer counting
argument is elementary and independent of Collatz dynamics.

## Gap audit

- Non-erasing output is essential.  With empty emissions, a length-`n` output
  factor may depend on an unbounded input interval.
- The integer `18` is a lower bound on the product `Q*B`, not separately on
  `Q` or `B`.
- Statement 3 requires genuine bounded-context synchronization.  A carry state
  depending on an unbounded counter does not satisfy it.
- Most importantly, the issue-#4 stack emits blocks whose lengths grow with the
  stack height.  It therefore lies outside the bounded-`B` theorem.  T-9406
  proves that this loophole can inflate output complexity quadratically.
- The theorem constrains a concrete transduction architecture; it does not say
  every S-adic system admits such a transducer.

## Adversarial tests

`X-9402` builds 128 deterministic non-erasing transducers with `Q,B<=4` over a
long Fibonacci directive and checks the exact finite factor-key inequality at
896 parameter combinations.  It also exhausts all 256 binary radius-one local
maps and checks the corresponding sliding-block inequality.  These finite
checks validate the proof interface, not the universal theorem.

## Remaining uncertainty

Independent reconstruction is pending.  The principal open case is a
transducer whose output length or carry memory grows with the directive height.

## Suggested next attack

For each proposed grammar, expose a stage-wise resource certificate

```text
(Q_j, B_j, memory_j, fresh arithmetic bits_j)
```

and seek a height-normalized analogue of (2) that cannot be satisfied merely
by padding long runs of zeros.