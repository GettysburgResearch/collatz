# Aaronson–Yolcu–Heule swarm: explicit orders and critical carry returns

**Collatz remains unresolved. All new claims are PROPOSED at project level.**
This pass develops concrete alternative orders for the exact eleven-rule
binary/ternary SRS, implements their transitions, and proves obstructions to
several plausible extensions. Its strongest positive result is an explicit
boundary-sensitive order and an exact reduction to critical-event returns,
together with a second ordinal order covering every microscopic rule under
an exact arithmetic source guard.

## Read first

1. [Synthesis and the microscopic ordinal rank](synthesis.md).
2. [Positional order, reset budget, and critical frontier](orders.md).
3. [Carry flux, maximal rank guard, and unbounded event debt](carry-geometry.md).
4. [Exact administrative cost and the published-chart obstruction](srs-semantics.md).
5. [Complete representation DAG and the all-weight impossibility theorem](representation-dag.md).

The [source ledger](SOURCES.md) separates the published AYH baseline from
this pass and pins the earlier project context. The [review report](../../reports/ay-swarm-20261030/REVIEW.md)
records actual in-session reconstruction and its limits; mathematical acceptance
is not inferred from a successful script or from a repository merge.

## The concrete advances

| Result | What it establishes | Exact remaining boundary |
|---|---|---|
| `rho=(E,F,A,Q,J)` in `N^5` | Strict contextual descent for the ten rules other than `ag -> fa`, with an elementary proof and no matrix search | One-rule deletion termination was already published; the new order exposes the precise reset |
| `54(L+k)^2+18(L+k)` | Bounds all literal rewrites in terms of initial length and the number of `ag` events | No bound on `k` for an arbitrary fixed source |
| Regular critical frontier | An exact, computable relation after normalizing the other ten rules; a frontier rank lifts to the full system | The global frontier rank is open |
| Single-`g` return section | Every intervening administrative burst terminates by `(#g, first-g position)`, leaving an exact section of values `6p+2` | The induced return operation is total; its iteration is not proved terminating |
| `55L^2+18L+1` per section return | Bounds one complete return's literal rewriting cost from its current word length | Does not bound the number of returns |
| `R=(K(oddpart(n)),v2(n),H(word))` | A well-founded ordinal order for all nine auxiliary rules, all even rules, and an exact class of odd sources | Guarded termination/exit, not universal convergence |
| `pop(U(n))-pop(n)=P-M` | Exact ordered carry accounting, with a maximal guard for `K=binom(pop,2)+v2(n+1)` | The guard is not forward invariant |
| A one-event damage family | A single critical `ag` can increase popcount by any prescribed size | Rules out fixed popcount credit per event; retains positional carry intervals |
| All-weight additive obstruction | Five actual odd edges defeat every nonnegative real additive complete-fibre minimum with the `(pop,r)` tie breaker | Does not exclude stateful or nonlinear costs |
| Fibonacci obstruction | The exact all-representation minimum of one published matrix chart fails on an infinite family, even after fixed polynomial administrative penalties | Specific to AYH Example 4.3, not all matrix interpretations |
| Exact finite-fibre DAG | Counts and scalar-optimizes every representation through `O(log^2 n)` quotient nodes | Vector correlation must be retained; compression is not a decrease theorem |

The pass also proves that total context-compatible orders and strictly
monotone interpretations into a single well-order cannot orient even two of
the full system's rules. This explains why an ordinal label alone is not
enough; boundary state and the actual comparison relation matter.

## Why the frontier is worth pursuing

The deterministic binary-start frontier uses only `a,b,g` and the two
boundaries. All noncritical normalization has an explicit polynomial budget.
The remaining state is an ordered sequence of binary blocks and ternary
carry runs. A companion compressed transducer evaluates ordinary binary odd
macros with run lengths as large as `10^80` without expanding them; frontier
and section returns have their own literal replay. These are distinct clocks,
as explained in the synthesis. Together they give a definite order-search
problem with exact transitions and counterexamples.

A further proved reduction removes the purely administrative bursts and
restricts the unresolved return comparison to the single-`g` words `c u a g d`,
where `u` is binary. Their values are exactly `6p+2`, `p>=1`. This is an
induced SRS return, with its own physical replay; no identification with an
earlier H-map or rank is assumed.

The most promising next proof target is an order on the **ordered carry
intervals** that handles complete critical returns. Their order and length
cannot be replaced by just the number of events or a scalar digit cost.
The alternative finite-chart approach has an exact exposed-winner criterion;
its universal coverage is also open.

These are research judgments, not evidence that a full proof is imminent.
No global convergence, nontrivial cycle exclusion, or divergent ordinary
source is established in this pass.

## Reproduce

All four programs use standard Python and explicit checks that survive `-O`:

```bash
python -X utf8 -B experiments/ay-swarm-20261030/orders.py --output /tmp/ay-orders.json
python -X utf8 -B experiments/ay-swarm-20261030/carry_geometry.py --output /tmp/ay-carry.json
python -X utf8 -B experiments/ay-swarm-20261030/srs_semantics.py --output /tmp/ay-semantics.json
python -X utf8 -B experiments/ay-swarm-20261030/representation_dag.py --output /tmp/ay-representations.json
```

The representation replay includes a 4,096-bit input and over five million
quotient nodes. Its exact arithmetic work is larger than the other checks;
it does not enumerate the astronomically larger number of represented words.
The root [verification program](../../experiments/ay-swarm-20261030/verify_packet.py)
checks the cross-track invariants and the finite-fibre cost table independently.

The result records include failure counts and representative counterexamples.
In particular, the count of
18,510 successful rank decreases among 32,768 tested odd sources is not a
percentage of Collatz solved. The 1,024 fully replayed frontier examples are
implementation checks, not a new verification record or an all-input proof.
