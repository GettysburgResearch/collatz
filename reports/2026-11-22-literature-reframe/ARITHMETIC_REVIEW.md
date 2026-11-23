# Independent review: fixed-source words and prime-rank budgets

**Result: the stated finite theorems and written applications check out. No
full Collatz closure is asserted or supplied.** This review checks the new
argument and its literature interfaces; it does not rerun the earlier
repository proofs or claim an independent Lean execution.

## Reviewed snapshot

| File | SHA256 |
| --- | --- |
| `research/literature-reframe-20261122/ARITHMETIC_WORDS.md` | `06d0984a2be9c49dde162140d35a3023020dffb9a265760a4279d890d8e8d9ce` |
| `research/literature-reframe-20261122/lean/SourceCollision.lean` | `b8edb0f0388e3e8d785233343e06bb2376dab079e0a7c2e3d2e6c0df2d4327a7` |

The Lean source was read in full. It uses the ordinary shortcut map,
recursively defined actual orbit states, and recursively checked actual
parity windows. No surrogate symbolic orbit, conjectural conjugacy,
`sorry`, custom axiom, or external import appears in this file. Compilation
and the printed axiom receipts are maintained by the author and combined
publication build.

## 1. The finite collision threshold retains the original source

The induction proving `parity_prefix_divisibility` is valid in both
branches. Equal even parities convert twice the next-state difference to
the original difference. Equal odd parities introduce a factor of three,
which can be canceled against a power of two. Distinct ordinary states
therefore have separation at least `2^L` if their length-`L` windows agree.

The source-height inequality

\[
2^K(T^j(n)+1)\le 3^K(n+1)\qquad(j\le K)
\]

does not rely on a monotone trajectory. The proof first establishes the
bound at the actual clock `j`, then multiplies by `2^(K-j)` and uses
`2^(K-j)<=3^(K-j)`. Comparing the separation with the larger endpoint
gives the **strict** collision budget

\[
2^{L+K}<3^K(n+1).
\]

The strictness is supplied by the extra one in the height envelope. Thus
the weak reverse inequality in `no_distinct_collision` really forces an
actual repeated state, including equality at the numerical threshold.
For the doubled prefix, the substitution `i=0`, `j=K=L` gives exactly
`(4/3)^L>=n+1`. The conclusion is periodicity of the source; the source
is not asserted to be one.

I independently read Dubickas's Theorem 5 and its proof from the
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf).
The same divisibility and height mechanism gives the asymptotic constant
`log(2)/log(3/2)` there under divergence. The note correctly credits this
mechanism and does not claim a new asymptotic complexity theorem.

## 2. The prime-rank calculation is uniform over changing words

I independently checked Theorem 1.1 in the
[Beukers–Schlickewei author PDF](https://webspace.science.uu.nl/~beuke106/s-units.pdf).
It gives at most `2^(8r+8)` solutions to `X+Y=1` in the rational closure
of a rank-`r` multiplicative subgroup of `(C*)^2`.

For a fixed set of `s` rational primes including two and three, the two
coordinates of each pair `(-3x_i,2^a_i x_(i+1))` lie in the corresponding
unit group. Its direct square has rank `2s`; signs contribute torsion.
Distinct transition sources yield distinct pairs. The claimed bound
`N<=2^(16s+8)` follows with no fixed-exponent or fixed-word condition.

This proves eventual periodicity when one finite prime set supports the
whole positive orbit. It does not exclude nontrivial cycles. For an
aperiodic orbit the transition sources are distinct, so applying the same
bound to the prime pool of each observed prefix gives the stated
logarithmic lower bound on `s_N`. Choosing a different pool for every
prefix does not invalidate the finite inequality; it prevents that
inequality from supplying a fixed stopping budget.

## 3. The attempted composition does not conceal a new upper bound

The accelerated odd height envelope follows because every valuation is
at least one. Hence sufficiently long shortcut-parity windows label
distinct odd states injectively. The unit equation counts those same
states. Counting their labels adds no second, smaller upper bound when
the prime pool grows.

The unproved condition

\[
s_N\le(1/16-\epsilon)\log_2 N
\]

does contradict the finite unit-equation bound for large `N`. Conversely,
an eventually periodic orbit has an eventually constant prime pool and
satisfies that condition for any fixed `0<epsilon<1/16`. The note therefore
correctly presents this as another formulation of eventual periodicity,
not as a known weaker bridge to it.

The elementary upper bound from orbit heights also checks: the product
of all distinct observed primes other than two and three divides the
product of the odd orbit values, and each such prime is at least five.
The resulting quadratic bound on the number of primes is compatible
with the logarithmic lower bound. No contradiction was lost in composing
the two estimates.

## 4. The rationality and dimension interfaces remain explicit

The
[Bernstein–Lagarias author PDF](https://websites.umich.edu/~lagarias/doc/bernstein.pdf)
states the established rationality inclusion for the inverse conjugacy
in the direction used by the note; the reverse inclusion is its
Periodicity Conjecture. An algebraic ordinary source therefore does not
provide the missing algebraicity of its parity code.

The rational-shadow divisibility test counts both numerator and
denominator height. The full affine-word identity has the correct odd
position weights `2^d_i 3^(p-1-i)`. Expanding it into a unit equation lets
the number of variables grow, while compressing its correction into one
integer loses membership in a fixed unit group. Neither rewriting removes
the stated open parameter.

No correction to the reviewed source or argument was required. The
remaining global assertions are explicitly unproved and are absent from
the Lean assumptions.
