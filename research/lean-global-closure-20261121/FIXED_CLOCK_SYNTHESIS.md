# A global fixed-clock rank search

**Status:** no global ranking certificate was found. This is a constructive
full-theorem synthesis attempt and reusable exact verification code. The
numerical optimization outcomes are not formal impossibility theorems.
The earlier `RelativeParityBarrier.lean` checkpoint is unchanged.

## The full theorem being sought

Fix an even shortcut clock `q`. Scan the ordinary positive binary digits
of `n` from least significant to most significant, retaining the previous
`k−1` digits and optionally the position modulo `h`. The candidate rank is

\[
 P(n)=\sum_{j=0}^{\ell(n)-1}
 w(j\bmod h,\operatorname{context}_j,\operatorname{bit}_j)
 +G(\ell(n)\bmod h,\operatorname{finalContext}(n)).
\]

The search uses nonnegative rational edge costs `w` and arbitrary rational
terminal corrections `G`. Consequently `P` is bounded below on *every*
positive integer by the least of finitely many terminal corrections, and
its values lie in a rational lattice. A strict inequality

\[
                  P(T^q n)<P(n)\qquad(n>2)
\]

would therefore prove termination of every positive Collatz orbit: an
infinite orbit avoiding `{1,2}` would give an infinite strictly decreasing
sequence in a bounded-below discrete set. For even `q`, the two ordinary
cycle values are fixed by `T^q`, and hitting either reaches one.

This target is stronger than a finite trajectory check and permits
temporary ordinary value growth. It does not presuppose five closure,
an average parity law, or a bound on the input's bit length.

Signed local costs with a finite graph coboundary lower bound do not
expand this class when `G` is free. If

\[
w(c,b)\ge B(\operatorname{next}(c,b))-B(c),
\]

replace `w` by its nonnegative reduced cost and replace `G` by
`G+B(final)−B(initial)`. The represented total potential is unchanged.
The same argument includes the position phase in the context.

## Exact arbitrary-length compiler

For each residue `0≤r<2^q`, write

\[
n=2^q a+r,\qquad T^q(n)=3^{p_r}a+c_r,
\]

where `p_r` is the odd count of the `q`-step trajectory of `r`, and
`c_r=T^q(r)`. This is the exact usual affine branch identity. A state
records the constant odd multiplier `3^p_r`, input and output contexts,
the nonnegative multiplication carry, the current position phase, and
whether the high input word is nonempty and ends in one.

The low `q` source bits are charged at initialization. Each high input bit
`b` emits the bit

\[
o=(3^{p_r}b+\operatorname{carry})\bmod2,
\qquad
\operatorname{carry}'=
\left\lfloor\frac{3^{p_r}b+\operatorname{carry}}2\right\rfloor.
\]

At every legal last high bit, the remaining carry is flushed and the two
terminal corrections are charged. The finite inputs `3≤n<2^q`, which
have no high word, are separate exact boundary cases. There is no
arbitrary maximum accepted input length.

A global node-potential certificate has three types of inequalities:

1. The initialized cost is at most the corresponding node potential.
2. Every edge cost plus its source potential is at most its destination
   potential.
3. Every legal terminal potential plus its final cost is at most `−1`.

Induction along *any* input word proves the desired rank drop. Repeated
automaton states do not create an unverified loop: every edge in the
finite graph participates in the inequalities.

## Two synthesis implementations

`search/fixed_clock_ranking.py` builds the complete finite transducer LP for
position-independent weights, with optional terminal corrections and
coboundary lower bounds. `search/periodic_position_ranking.py` adds the bit
position modulo an arbitrary positive `h`.

`search/counterexample_rank_synthesis.py` separates candidate generation from
global verification. It first fits concrete input constraints in a compact
LP, maximizing a common drop margin. This finite fit supplies no theorem.
The candidate is rounded to a common rational grid and every fitted
inequality is then checked exactly. The verifier uses integer costs and
propagates maximum accumulated costs through the exact global transducer.

A violated legal terminal supplies a concrete new integer and its exact
nonnegative rank change. An exhausted work queue would instead supply all
node potentials, every edge inequality, every terminal inequality, and
every short-input inequality as an exact global certificate. A resource
limit remains an undecided search. A global certificate would still need
the stated transducer correspondence formalized in Lean before being
reported as a kernel-checked Collatz proof.

All three reusable scripts cap BLAS/OpenMP and HiGHS to one thread. Large
solver jobs should be run sequentially alongside Lean compilation.

## Results from this attempt

The complete-state LPs found no solution in the following searched
instances. Here `k` is the local window width, including the current bit.

| Clock and rank class | Outcome |
|---|---|
| `q=6`, position-independent, padded context, `k≤5` | LP solver reported infeasible |
| `q=6`, independent terminal correction, `k≤6` | LP solver reported infeasible |
| `q=8`, position-independent, padded context, `k≤4` | LP solver reported infeasible |
| `q=10`, position-independent, padded context, `k≤2` | LP solver reported infeasible |
| `q=6`, terminal correction, position period `2`, `k≤5` | LP solver reported infeasible |
| `q=6`, terminal correction, position period `3`, `k≤4` | LP solver reported infeasible |
| Larger complete-state systems in these runs | Time or state limits; undecided |

These are solver reports, without an exact Farkas certificate or a Lean
proof of nonexistence. They do not rule out larger windows, other clocks,
other rank architectures, or Collatz itself.

The stable compact candidate-generation runs gave:

| Clock, width, period | Concrete constraints | Outcome |
|---|---:|---|
| `6,10,1` | 8,545 | Optimal floating common margin `0`; no candidate |
| `8,8,1` | 8,646 | Optimal floating common margin `0`; no candidate |
| `10,8,1` | 9,414 | Optimal floating common margin `0`; no candidate |
| `6,12,1`, first candidate | 3,545 | Exact fitted candidate rejected at actual input `129` |
| `6,12,1`, next candidate | 3,546 | Exact fitted candidate rejected at actual input `131` |

For the last two rows, `T^6(129)=55` and `T^6(131)=56`. The candidate
rank changes were respectively `5352` and `2937` in their reconstructed
integer scales. Thus the verifier rejected their claimed rank property
even though the ordinary numbers happened to decrease. That search was
interrupted after those saved iterations for shared-resource coordination;
no terminal certificate was produced.

The final single-thread control fits every input `3,…,127`, then obtains
the unsupplied integer `197` from the global transducer. It verifies
`T^6(197)=28` and integer rank change `+1`, rejecting the fitted candidate.
The receipt records an actual process thread count of one. The control is
evidence for the candidate/verifier boundary, not a Collatz theorem.

## Reproducible files and current scope

The four `candidate_compact_*_report.json` files retain actual saved
outcomes. Their exact source snapshots are retained under
`../../reports/lean-global-closure-20261121/rank_source_snapshots/` with content-addressed names; the current scripts
add the explicit thread limits. `single_thread_verifier_control.json`
records the final current-source execution.

No candidate passed global verification. No new universal rank or
universal `RelativeBudgetReturns` proof is supplied by this attempt.

Actual reports are in `../../reports/lean-global-closure-20261121/`.
