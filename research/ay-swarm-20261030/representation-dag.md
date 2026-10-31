# Complete mixed-base fibres, and an all-weight obstruction

**Status: PROPOSED.** The statements below have complete elementary proofs;
the accompanying executions check their implementation. They do not give a
global Collatz order. No external priority claim is made for the elementary
mixed-radix division algorithm or its dynamic programming specialization.

Use the AYH digit actions `a(x)=2x`, `b(x)=2x+1`, `e(x)=3x`,
`f(x)=3x+1`, `g(x)=3x+2`, with the leading `c` fixed at 1 and final `d`
the identity. The exact upstream system and pins are in [the source ledger](SOURCES.md).
The arithmetic map in the obstruction is the **accelerated odd map**

\[
U(n)=(3n+1)/2^{\nu_2(3n+1)},\qquad n\text{ positive and odd}.
\]

This is different from the shortcut map `T` used in the other packet.

## DAG-01: a small exact graph represents the entire finite fibre

Let `R(n)` be the set of all well-formed words representing the fixed positive
ordinary integer `n`. The following recursion is exact:

\[
R(1)=\{cd\},\qquad
R(n)=\bigcup_{b\in\{2,3\},\ \lfloor n/b\rfloor\ge1}
\{\text{append the base-}b\text{ digit }n\bmod b
   \text{ to }w:w\in R(\lfloor n/b\rfloor)\},\quad n>1.
\tag{1}
\]

Here appending means insertion immediately before the final `d`.

**Proof.** A last digit in base `b` is forced to be `n mod b`; the preceding
positive prefix is forced to be `floor(n/b)`. Conversely every such prefix
and digit reconstruct `n`. Every digit at least doubles the positive prefix,
so a word representing 1 is just `cd`, and all other paths terminate under
division. The two branches in (1) use different final symbols and are disjoint.
This proves both directions and finiteness without running Collatz. ∎

All recursive arguments belong to

\[
Q(n)=\{\lfloor n/(2^a3^b)\rfloor\ge1:a,b\ge0\}.
\tag{2}
\]

This follows from `floor(floor(n/p)/q)=floor(n/(pq))`. Consequently the
number of distinct quotient nodes is at most

\[
(\lfloor\log_2 n\rfloor+1)(\lfloor\log_3 n\rfloor+1).
\tag{3}
\]

The graph has at most two outgoing edges per node and is acyclic. In fact (2)
is exactly its node set, after duplicate quotients are identified. Any division
ordering for a product with positive final quotient cannot hit 1 before a
remaining divisor: that would make the final quotient zero. Thus stopping at
1 removes no positive quotient in (2). Bound (3) counts exponent pairs before
identifying duplicates.

Counting all representations takes one integer addition per internal graph
node. This is a bound on graph operations, **not** a unit-cost bit-complexity
claim for arbitrarily large counts. Explicitly listing every representation
can still take exponentially many words in the input bit length.

## DAG-02: exact scalar optimization, with a correlation boundary

Let each digit `s` act on a natural-valued cost by a nondecreasing function
`F_s`. Fix a seed cost at 1 and read a representation from left to right.
Then its minimum over all representations satisfies

\[
E(1)=e_0,\qquad
E(n)=\min_{b\in\{2,3\},\ n\ge b}
 F_{s(b,n\bmod b)}(E(\lfloor n/b\rfloor)).
\tag{4}
\]

**Proof.** Use (1), and commute a scalar minimum through each nondecreasing
`F_s`. Every minimum is attained because the fibre is finite. Store the
chosen edge to reconstruct an actual winning word. ∎

The implementation supports nonnegative integer affine functions, including
constant maps, and returns a concrete word. It never replaces a matrix-valued
profile by independent coordinate minima. That replacement is unsound:
vectors `(0,10)` and `(10,0)` have coordinate minimum `(0,0)`, which is
unattainable and has a smaller sum than either legal vector. A vector
interpretation needs a correlated frontier or a proof that its particular
continuation maps preserve the chosen scalar optimization. The graph-size
bound does not bound the size of every such frontier.

## DAG-03: no nonnegative additive fibre minimum supplies the desired order

Assign arbitrary **nonnegative real** costs `a,b,e,f,g` to the five digits.
Let `C(n)` be the least sum of those costs over **all** representations in
`R(n)`. Let `s(n)` be binary popcount and `r(n)=nu_2(n+1)` for odd `n`.

There is no choice of these costs for which

\[
(C(U(n)),s(U(n)),r(U(n)))
  <_{\rm lex}(C(n),s(n),r(n))
\tag{5}
\]

holds simultaneously at `n=3,7,9,15,17`.

For integer costs this rules out an entire family of well-founded candidate
orders. Allowing arbitrary nonnegative real coefficients does not even solve
the five necessary orientation conditions, regardless of well-foundedness.
It also rules out a strictly decreasing additive fibre minimum alone.

### Complete small fibres and necessary inequalities

Write

\[
x=\min(b,e),\quad z=\min(2b,b+e,a+f).
\]

Equation (1), or direct enumeration, gives the following exact costs:

| n | C(n) |
|---:|---|
| 3 | `x` |
| 5 | `min(a+b,g)` |
| 7 | `z` |
| 9 | `min(2e,b+f,b+e,2a+b)` |
| 11 | `min(g+x,a+2b)` |
| 13 | `min(2f,a+b+x,2a+f)` |
| 15 | `min(e+g,3b,2b+e,a+b+f,a+b+e)` |
| 17 | `min(2g,a+b+g,a+b+f,3a+b)` |
| 23 | `min(g+z,a+3b)` |

The odd edges are `3->5`, `7->11`, `9->7`, `15->23`, `17->13`.
On the first, second, and fourth edges, popcount is unchanged and `r`
decreases by one, so (5) requires weak cost decrease. On the other two edges
popcount increases from 2 to 3, so it requires **strict** cost decrease.
In particular, all five conditions imply

\[
C(3)\ge C(5),\quad C(7)\ge C(11),\quad C(9)>C(7),
\quad C(15)\ge C(23),\quad C(17)>C(13).
\tag{6}
\]

### Proof when b <= e

Here `x=b` and `z=min(2b,a+f)`. First `a>0`: if `a=0`, then
`C(9)<=b`, and the third condition forces `z<b`, whereas
`C(11)=min(g+b,2b)>=b`, contradicting the second condition.
The first condition now implies `g<=b`, because `a+b>b`.

If `z=2b`, then `C(9)>2b`, together with `C(9)<=b+f` and
`C(9)<=2a+b`, gives `f>b` and `2a>b`. Each of

\[
2f,\qquad a+2b,\qquad 2a+f
\]

is then strictly greater than `2b`. Hence `C(13)>2b>=2g>=C(17)`,
contradicting the fifth condition.

Otherwise `z=a+f<2b`. The strict inequality `C(9)>z` and upper bound
`C(9)<=b+f` imply `a<b`. Also `f<2b`, so `a+2b>z`.
The second condition therefore forces

\[
g+b\le a+f,\qquad g\le a+f-b<f.
\]

It follows that `2f>2g`, `a+2b>2g`, and

\[
2g\le2a+2f-2b<2a+f.
\]

Again all three terms defining `C(13)` exceed `2g>=C(17)`, a
contradiction. This includes zero costs without dividing by a coefficient.

### Proof when e < b

Now `x=e`. The first condition implies `g<=e`, because `a+b>e`.
Since `C(9)<=2e<b+e`, its strict decrease to `z` forces
`z=a+f<2e`. Thus `f<2e<2b`, and the second condition forces

\[
g+e\le z.
\tag{7}
\]

The fourth condition and the table give

\[
\min(g+z,a+3b)=C(23)\le C(15)\le e+g.
\]

But `a+3b>2e>=e+g`. Therefore `g+z<=e+g`, or `z<=e`.
Combining with (7) and nonnegativity gives `g=0` and `z=e`.
Consequently `C(17)=0`, while `C(13)>=0`, contradicting the last
strict condition in (6). This completes the proof. ∎

### What the theorem excludes, and what it leaves

The result is not merely UNSAT at a coefficient ceiling. It covers every
nonnegative additive assignment after optimizing over the entire mixed-base
fibre, even with the useful popcount/trailing-one tie breaker appended.

It does not exclude position-dependent costs, finite-state costs, nonlinear
monotone digit maps, correlated matrix frontiers, signed costs with a separate
well-foundedness proof, or the critical-event order in [orders.md](orders.md).
Those are actual changes in the proof object, rather than a larger coefficient
search for this ruled-out family.

## Experiments and the next use of the graph

The [implementation](../../experiments/ay-swarm-20261030/representation_dag.py)
was checked against an independent forward construction of **83,788 words**,
covering every fibre at values 1 through 1,024. It checked 384 scalar-affine
minima against literal enumeration. The all-weight theorem above was found
after, and is logically independent of, the finite search over 1,023 nonzero
digit-cost tuples in `{0,1,2,3}^5`; every tuple fails by source 17.

The large graph check used `n=2^k-1`:

| Input bits k | Distinct quotient nodes | Bits in exact representation count |
|---:|---:|---:|
| 64 | 1,166 | 50 |
| 256 | 19,794 | 202 |
| 1,024 | 326,198 | 807 |
| 4,096 | 5,265,223 | 3,227 |

The complete count is computed, not all its represented words. These are
arithmetic compiler checks, not Collatz trajectories or convergence evidence.

The useful next search object is a correlated boundary-state profile over
this graph. Any proposed pruning must preserve all continuation comparisons.
The unresolved proof obligation is a globally decreasing order or universally
successful exposed winner; graph compression alone establishes neither.
