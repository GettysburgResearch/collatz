# T-8305 — The six-branch quotient chart is the bounded-discrepancy negative-three run highway

Claim ID: `T-8305`  
Status: `PROPOSED / EXACT CONSTRUCTIVE CONJUGACY`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: branch-qualified `PR45/L-8407`; branch-qualified `PR51/O-8001` and its normalized run-highway recurrence  
Scope: positive ordinary intrinsic-core trajectories of the six-branch critical quotient chart  
Related counterexample candidates: none; one forever-defined positive state would immediately provide one

## 1. Six-branch intrinsic-core recurrence

Let

\[
i_n\in\{0,1,2,3,4,5\}
\qquad(n\ge -1)
\tag{1}
\]

be consecutive quotient-chart types.  Branch-qualified `PR45/L-8407` gives the exact intrinsic-core transition

\[
\boxed{
2^{19+3(i_n-i_{n+1})}u_{n+1}
=3^{12+2(i_{n-1}-i_n)}u_n+7.}
\tag{2}
\]

Every quantity is an ordinary integer on a physical chart trajectory.

Define the run address

\[
\boxed{R_n=5+i_n-i_{n+1}.}
\tag{3}
\]

Then `R_n` is an integer in `[0,10]`, and `(2)` becomes

\[
\boxed{
2^{4+3R_n}u_{n+1}
=9^{R_{n-1}+1}u_n+7.}
\tag{4}
\]

This is exactly the intrinsic `+7` maximal-run recurrence in the normalized negative-three chart of PR #51.

If `7|u_n` throughout and `v_n=u_n/7`, then `(4)` reduces to the unit-toll form

\[
\boxed{
2^{4+3R_n}v_{n+1}
=9^{R_{n-1}+1}v_n+1.}
\tag{5}
\]

## 2. Bounded discrepancy is equivalent to six-state realizability

For a finite or infinite run sequence `R_n`, put

\[
S_0=0,
\qquad
S_m=\sum_{n=0}^{m-1}(R_n-5).
\tag{6}
\]

### Theorem 1 — exact address criterion

There exists a type sequence `i_n in {0,...,5}` satisfying `(3)` if and only if

\[
\boxed{
\sup_m S_m-\inf_m S_m\le5.}
\tag{7}
\]

For a finite sequence, the suprema are taken over its finite prefix set.

When `(7)` holds, every integer

\[
i_0\in
[\sup_m S_m,\inf_m S_m+5]
\tag{8}
\]

generates one valid type sequence by

\[
\boxed{i_m=i_0-S_m.}
\tag{9}
\]

### Proof

Summing `(3)` gives

\[
\boxed{
\sum_{n=a}^{b-1}R_n
=5(b-a)+i_a-i_b.}
\tag{10}
\]

In particular, `S_m=i_0-i_m`, so `0<=i_m<=5` implies `(7)`. Conversely, `(7)` makes the interval `(8)` nonempty. Equation `(9)` then stays in `{0,...,5}` and satisfies

\[
i_n-i_{n+1}=S_{n+1}-S_n=R_n-5,
\]

which is `(3)`. **QED**

Thus the six-branch type process is precisely a height-six coding of the negative-three run highway. It is not an unrelated quotient chart.

## 3. Automatic exponential growth after infinite definedness

Discarding the positive toll in `(2)` gives

\[
u_{n+1}
>
{3^{12+2(i_{n-1}-i_n)}
 \over
 2^{19+3(i_n-i_{n+1})}}
 u_n
\tag{11}
\]

for every positive state. Multiplication from `n=0` through `m-1` yields

\[
\boxed{
u_m
>
\left({3^{12}\over2^{19}}\right)^m
3^{2(i_{-1}-i_{m-1})}
2^{-3(i_0-i_m)}u_0.}
\tag{12}
\]

The endpoint factor is bounded below uniformly by

\[
3^{-10}2^{-15}.
\tag{13}
\]

Since

\[
\boxed{3^{12}=531441>524288=2^{19},}
\tag{14}
\]

any positive ordinary trajectory on which `(2)` is defined forever satisfies

\[
u_m\longrightarrow\infty.
\tag{15}
\]

The corresponding physical shortcut-Collatz trajectory is therefore unbounded.

## 4. Exact counterexample criterion

A full unconditional counterexample follows from one finite ordinary initialization

\[
(i_{-1},i_0,u_0)
\tag{16}
\]

with `i_-1,i_0 in {0,...,5}` and `u_0>0`, together with an inductive proof that the deterministic six-branch quotient transition remains integral and selects a type in `{0,...,5}` forever.

No additional drift theorem is required: `(12)`–`(15)` prove divergence automatically.

Equivalently, it is enough to construct one positive ordinary solution of the run recurrence `(4)` whose run-address discrepancy satisfies `(7)` at every depth.

## 5. Constructive significance

This theorem joins the two main positive lanes:

```text
PR #51 negative-three pulse/run chart
  <-> bounded-discrepancy run addresses R_n
  <-> PR #45 six-branch quotient types i_n
  -> automatic exponential growth when defined forever.
```

The unresolved obligation is now purely ordinary and top-boundary based:

```text
one finite positive core
+ all-time exact divisibility/type legality.
```

A modular lasso or a compatible 2-adic address does not satisfy that obligation.

## 6. Gap audit

- The theorem does not produce a forever-defined initial core.
- The run-address criterion controls only the finite type address; the large integer divisibility remains essential.
- A bounded-discrepancy symbolic sequence by itself may select only a nonordinary completion.
- The lower bound `(12)` assumes positive ordinary states and exact legal transitions.
- No positive cycle, divergent seed, or `K-83xx` candidate is asserted.

## 7. Suggested next attack

Carry the actual most-significant boundary through the six-state address. The promising state is

```text
(previous type,
 current type,
 intrinsic core quotient,
 canonical top digit / carry-flush obligation).
```

Search for either:

1. a self-replicating positive cylinder proving all-time integrality; or
2. an exact ranking obstruction for this frozen bounded-discrepancy run class.

A positive invariant plus `(12)` is the requested unconditional Collatz counterexample.
