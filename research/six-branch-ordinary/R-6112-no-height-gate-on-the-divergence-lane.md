```text
Claim ID:            R-6112
Title:               Cycle-side height gates cannot transfer to the divergence lane
Status:              PROVED (a no-go: it refutes a proposed method, not a claim)
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        T-6103(a)
Scope:               the six-branch chart; the argument is generic for expanding charts
Related counterexample candidates: none
Refutes (as a method): applying PR #50 `L-8310`-style remainder-height arguments to
                       divergent-orbit architectures
```

## Statement

Let `x_0 > 0` be legal for `N` steps in the six-branch chart, with
`c_N = sum_{j<N} a_j P^(N-1-j) Q^j`. Then the exact identity

```text
Q^N x_N  =  P^N x_0 + c_N
```

holds, and:

**(a)** `c_N / P^N` increases to a limit `C` in `[a_0/(P-Q), a_5/(P-Q)] = [32.067, 57.786]`,
so `c_N` is *never* comparable in size to `Q^N`; it is `Theta(P^N)`.

**(b)** `(Q/P)^N x_N = x_0 + c_N/P^N -> x_0 + C >= 1 + 32.067 > 0`, so the orbit grows at the
exact rate `x_N ~ (x_0 + C) (P/Q)^N`, with no cancellation.

**(c)** Consequently the divisible quantity `P^N x_0 + c_N` is a positive integer of size
`~(x_0 + C) P^N`, while the required divisor is `Q^N < P^N`. The ratio
`(P^N x_0 + c_N)/Q^N = x_N >= 1` for every `N`, so the "divisor exceeds the Archimedean
absolute value, hence the quantity vanishes" step is unavailable **at every depth** — not
merely quantitatively far away, but structurally inapplicable.

## Why this matters

The cycle lane has a genuine height gate: a cycle forces `R = C - N(2^A - 3^K) = 0`, and a
nonzero `R` divisible by something larger than `|R|` is a contradiction. PR #50 `L-8310`
formalises this correctly. The recurring temptation — visible across several open PRs — is to
port the same machinery to the divergence lane, where the analogous object is `P^N x_0 + c_N`.

(a)-(c) show the port is impossible in principle. In the cycle case the target quantity is
*forced to vanish* and its size is therefore an obstruction. In the divergence case the target
quantity is *forced to be a large positive integer* whose quotient by the divisor is precisely
the next orbit value. There is nothing to contradict: `Q^N | P^N x_0 + c_N` is a congruence
condition with `~(P/Q)^N` admissible quotients, and it is satisfiable at every finite depth by
`6^N` classes (L-6105(a)).

Equivalently: **the divergence lane has no small quantity.** Every height, remainder,
near-integrality, or full-denominator gate needs one.

## Proof

**(a)** `c_N/P^N = sum_{j<N} a_j (Q/P)^j / P`. Each term is positive so the partial sums
increase; and since `a_0 <= a_j <= a_5`,

```text
(a_0/P) * sum_{j<N}(Q/P)^j  <=  c_N/P^N  <=  (a_5/P) * sum_{j<N}(Q/P)^j,
```

and `sum_{j>=0}(Q/P)^j = P/(P-Q)`, giving the limit interval `[a_0/(P-Q), a_5/(P-Q)]`.
Numerically `[229376/7153, 413343/7153] = [32.067105, 57.785964]`.

**(b)** Divide the identity by `P^N` and apply (a). Positivity of `x_0` gives the bound.

**(c)** `x_N = (P^N x_0 + c_N)/Q^N` is a positive integer by legality, and `x_N >= 1` since
`x_0 >= 1` and the map is nondecreasing on positive integers. `QED`

## Gap audit

* *Does this refute L-8310 itself?* **No.** L-8310 is a cycle-side result and is untouched.
  This claim refutes only the *transfer* of that method to divergence architectures.
* *Is the argument specific to the six-branch digit set?* No — it uses only `P > Q > 0`,
  `a_j > 0` bounded, and legality. It applies verbatim to any expanding chart, including
  PR #45's, PR #49's, PR #51's and the centered `64 -> 81` chart, whenever the divergence
  (rather than the cycle) branch is being attacked.
* *Could a height gate apply to a derived quantity rather than `P^N x_0 + c_N`?* Possibly;
  this claim does not exclude every conceivable use of heights, only the direct analogue.
  Any proposal of that kind must first exhibit a quantity that is forced to vanish.

## Suggested next attack

Treat R-6112 as a filter. Before investing in a height/denominator gate for a divergent-orbit
architecture, state which quantity is forced to vanish. If there is none, the gate cannot
exist.
