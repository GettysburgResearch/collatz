# Transport past the binary shadow, and an unbounded marked-family descent

This checkpoint builds on PR 173 at `fa0c9e2a2851e6324391e39c17afcb5913185aec`.
Its Lean file is `BandTransport.lean`, in namespace
`CollatzShell.BandTransport`. It uses the same shortcut map, ordinary orbits,
basin predicate, and marked section as that source.

The results below are unconditional. The universal clock-saving condition is
not proved, and this checkpoint does not establish full Collatz convergence.

## 1. Exact transport after the binary precision expires

Let `p` be the number of odd shortcut steps among the first `d` steps from an
offset `a`, and put `q = T^d(a)`. The exact high-bit identity is

\[
T^d(2^d u+a)=3^p u+q.
\]

This identity is kernel-checked as `orbit_shift`; `oddCount_shift` proves that
the entire affine family uses the same number of odd steps. In particular, at
`u = 1`, the initial binary difference has become exactly `3^p`. No binary
congruence beyond those `d` clocks is assumed.

There is a total inverse construction for each ternary unit `q`. Select the
exponent `r` by its residue modulo nine:

| `q mod 9` | `r` | inverse source `b` |
| --- | ---: | --- |
| 1 | 2 | `(4q−1)/3` |
| 2 | 1 | `(2q−1)/3` |
| 4 | 2 | `(4q−1)/3` |
| 5 | 3 | `(8q−1)/3` |
| 7 | 4 | `(16q−1)/3` |
| 8 | 1 | `(2q−1)/3` |

The output remains a ternary unit. It is an actual inverse word containing
exactly one odd step, followed by its prescribed halvings. Uniformly for every
nonnegative integer `u`,

\[
T^r(2^r u+b)=3u+q.
\]

Iterating this construction `p` times gives explicit natural numbers
`A = restoredClock p q` and `b = restoredSource p q` satisfying

\[
p\le A\le4p,\qquad T^A(b)=q,
\]

\[
T^A(2^A u+b)=3^p u+q,\qquad 3^p b\le2^A q.
\]

These are `restored_bounds`, `restored_word`, `restored_forward`,
`restored_odd_count`, and `restored_height`. Thus arbitrary exhausted ternary
precision can be converted back to binary precision through genuine ordinary
paths. This construction has no finite depth cutoff. It also does not assert
that its reconstructed clock is shorter than the original clock.

## 2. Saving one clock gives component descent

The useful quantitative bridge is particularly simple in integer form.
For any natural `C`,

\[
n<2^d C\quad\Longrightarrow\quad
T^d(n)<3^{p(n,d)}C,
\]

where `p(n,d)` is the exact number of odd steps. This is `orbit_box`.
The proof proceeds through the first shortcut step: an even step keeps `C`,
and an odd step replaces `C` by `3C`. The strict upper endpoint absorbs all
additive terms in the Collatz map.

Suppose `2^d ≤ n < 2^(d+1)`, and another actual path reaches the same endpoint,
uses the same number `p` of odd steps, and has a shorter total clock `A < d`:

\[
T^A(b)=T^d(n),\qquad p(b,A)=p(n,d).
\]

The ordinary lower affine bound and the box bound give

\[
3^p b\le2^A T^d(n)<2^A\cdot2\cdot3^p
\le2^d3^p.
\]

Hence `b < 2^d ≤ n`. Moreover the two sources have the same basin status,
because they have an actual common ordinary endpoint. This is
`compressed_component_descent`. It is component descent, not a claim that
`b` occurs later on the forward orbit of `n`.

The specialized `restored_tail_descent` connects this directly to the first
section: if `a < 2^d` and the reconstructed clock for `T^d(a)` is shorter than
`d`, then the common ancestor `2^A + b` lies strictly below `2^d` and has the
same basin status as `2^d + a`.

## 3. An arbitrarily long expanding block admits exact half-descent

The inverse construction is not the only way to save a clock. A direct word
exchange handles an unbounded family of long expanding prefixes.

For positive `u`, let

\[
n=2^{r+1}u-1,\qquad m=2^r u-1.
\]

If `3^r u ≡ 3 (mod 4)`, write `3^r u = 4z+3`. The ordinary all-odd prefixes
reach

\[
T^{r+1}(n)=12z+8,\qquad T^r(m)=4z+2.
\]

Both numbers reach `3z+2` in two further shortcut steps. Therefore

\[
T^{r+3}(n)=T^{r+2}(m),\qquad m<n,
\]

and `Basin(n) ↔ Basin(m)`. There is no upper bound on `r`.
The formal statements are `adjacent_odd_block` and
`adjacent_odd_block_descent`.

This applies to the section family

\[
n_k=2^{3k}+2^{2k}-1,\qquad
m_k=2^{3k-1}+2^{2k-1}-1,\qquad k\ge2.
\]

Take `r = 2k−1` and `u = 2^k+1`. The congruence follows from
`3^(2k−1) ≡ 3 (mod 4)` and `2^k+1 ≡ 1 (mod 4)`. The result is

\[
T^{2k+2}(n_k)=T^{2k+1}(m_k),
\]

and, after appending the identical remaining suffix,

\[
T^{3k}(n_k)=T^{3k-1}(m_k).
\]

In addition,

\[
n_k=2m_k+1,\qquad m_k<n_k,
\]

so the known smaller source is exactly `(n_k−1)/2`.

Every `n_k` is marked by PR 173's exact definition. Its binary exponent is
`d = 3k`, its offset is `2^(2k)−1`, and

\[
(3k+1)(2^{2k}-1)\le70\,2^{3k}.
\]

The family is unbounded. These facts are kernel-checked as
`band_common_endpoint`, `band_dyadic_common_endpoint`, `band_half`,
`band_marked`, `band_component_descent`, and `band_family_unbounded`.

This gives an unconditional strict component descent certificate for every
member of the family. It does not separately prove convergence of all the
smaller sources `m_k`.

## 4. The remaining phase is explicit

When the phase is `3^r u = 4z+1`, the corresponding two sources reach
`12z+2` and `4z`. Two further steps give

\[
T^2(12z+2)=9z+2,\qquad T^2(4z)=z.
\]

`complementary_fork` records these exact ordinary identities. A transfer from
the known basin status of `z` to `9z+2` is not proved here. Reducing `r` by two
replaces `z` by `z'` with `z = 9z'+2`; that reproduces the same unresolved
chain and does not supply a decreasing rank.

Likewise, the total ternary inverse selector does not always save a clock.
Its theorem exposes the clock comparison as a hypothesis. Any global closing
argument must prove a suitable unbounded choice of compressed path, or settle
the complementary transfer by another common well-founded measure.

## Validation

`BandTransport.lean` was compiled by Lean 4.34.1 with
`-j1 -DwarningAsError=true`, against PR 173's compiled modules and its pinned
Mathlib environment. The compile exited successfully and produced
`BandTransport.olean`.

Printed axiom audits for the transport, the compression bridge, and all family
theorems contain only the standard `propext`, `Classical.choice`, and
`Quot.sound` axioms, with the smaller subsets where applicable. There are no
`sorry`, `admit`, custom axioms, or computational trust shortcuts in the file.
