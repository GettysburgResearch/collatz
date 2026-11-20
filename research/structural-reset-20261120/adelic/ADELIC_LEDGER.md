# Three arithmetic mechanisms and exact stopping points

**Status: exploratory architecture ledger.** Frozen input:
`55d8968d2ecbc23a91c9c4733929f34be9bf0d28`.

## I. Multiply the ordinary, 2-adic, and 3-adic separations

The attractive proposal is to combine common future parity at 2, common
past at 3, and ordinary height at infinity. Its simplest form has an
exact cancellation.

Let two distinct ordinary inputs have a common shortcut parity word of
length \(L\). Write \(q_k\) for its first-\(k\) odd count and
\(\Delta_k\) for the difference of the two states at that cut. Then

\[
 \Delta_k=3^{q_k}2^{-k}\Delta_0.
\]

The common parity word is equivalent to \(2^L\mid\Delta_0\): the
2-adic valuation of a nonzero difference drops by exactly one at every
shared step, and the converse follows by induction. Write
\(\Delta_0=2^Ld\), \(d\ne0\). Then

\[
 \Delta_k=3^{q_k}2^{L-k}d,
 \qquad
 |\Delta_k|_\infty|\Delta_k|_2|\Delta_k|_3
 =\frac{|d|}{2^{v_2(d)}3^{v_3(d)}}\ge1.
 \tag{A}
\]

The product is independent of the cut. The extra 3-adic power is offset
by the real affine scaling. Treating both effects as independent savings
counts the same cocycle twice. This is a finite ordinary identity; no
real and p-adic limits are equated.

The missing ingredient is an independent constraint on the outside-
\(\{2,3\}\) arithmetic of the normalized difference. Matching the
same word does not supply it. Equation (A) does not exclude more
elaborate adelic arguments.

## II. Compress a whole cycle or orbit into a fixed S-unit equation

An odd cycle satisfies

\[
 (2^A-3^m)n_0=
 \sum_{i=0}^{m-1}3^{m-1-i}2^{A_i}.
 \tag{B}
\]

The right side is a sum of \(\{2,3\}\)-units, but its number of terms
grows with the unrestricted odd period. A fixed-dimensional theorem
cannot silently absorb that change. Existing powered-factor theorems
give their stated conclusions only when the required factorization is
present; no fixed cover is inferred here for arbitrary cycles.

Fixing all prime divisors along an orbit gives a classical S-unit
finiteness argument from \(2^a n'-3n=1\). It does not justify such a
fixed prime alphabet on an arbitrary escape. Quantitative S-unit theory
already supplies a uniform period bound for cycles using a bounded
number of primes; the raw finiteness consequence is not novel.

The unresolved representation resource in this mechanism is the number
of terms, the varying coefficient heights, or the prime set. Finite
binary or ternary expansion of each individual state controls none of
those quantities uniformly over an entire infinite history.

## III. Charge shared prime powers to physical height variation

The initial local-window proposal used distinct affine roots and a sharp
S-part theorem, whose normalization is recorded in [SOURCES.md](SOURCES.md).
The joint reconstruction found a proof architecture requiring no
external analytic input:

1. The gcd of two visited states divides their positive affine correction.
   Its logarithm is bounded by the height difference plus three times
   the time gap, with no upper bound on the division exponents.
2. In an \(r\)-state block, each chosen prime can have one unrestricted
   maximal power. Its powers at the other states are paid for by this
   gcd bound.
3. The sum of all block ranges is at most the total variation of
   logarithmic height. Upward increments are at most one, so total
   variation is at most \(x_0+2N\), including all downward jumps.
4. The resulting finite inequality is uniform over sets of a specified
   cardinality. No ineffective cutoff or growing-dimensional theorem is
   needed when taking limits.

The result is [PRIME_HEIGHT_ESCAPE.md](PRIME_HEIGHT_ESCAPE.md): any
ordinary escape must distribute aggregate prime height over an
unbounded number of primes, even if the heaviest primes are selected
afresh after each prefix. Arbitrary long primitive cycles obey the same
dispersion condition. The first unsupported closing step is a persistent
concentration or other incompatible arithmetic principle for a single
ordinary surviving history. No such principle is supplied.

## An ordinary control against pointwise tightness

Fix any finite prime set \(S\). Choose a positive integer \(L\) divisible
by 6 and by \(\operatorname{ord}_p(2)\) for each
\(p\in S\setminus\{2,3\}\). For integers \(k\ge0\), set

\[
 a_k=2+Lk,\qquad n_k=\frac{2^{a_k}-1}{3}.
 \tag{C}
\]

These are positive odd ordinary integers and \(U(n_k)=1\). They tend
to infinity. Since \(a_k\equiv2\pmod6\),
\(2^{a_k}\equiv4\pmod9\), hence \(n_k\equiv1\pmod3\).
For any other \(p\in S\), \(2^{a_k}\equiv4\pmod p\), hence
\(3n_k\equiv3\pmod p\) and \(n_k\equiv1\pmod p\).
They are odd, so in every case

\[
 [n_k]_S=1.
 \tag{D}
\]

Thus there can be no universal positive pointwise lower bound for the
fraction of height carried by a prescribed finite prime set, even on
the genuine ordinary basin of 1. A closing tightness argument must use
the persistent history of a single source. It cannot replace that
history by varying transient predecessors.

## Scope safeguards retained

- One fixed ordinary source is required for any all-time statement.
  Finite witnesses are not promoted to an ordinary p-adic completion.
- The induced \(64\to81\) factor-complexity theorem is not generalized
  to all shortcut itineraries or used as a missing hypothesis.
- The corrected 256-stage architecture and the four-powered-factor
  cycle finiteness results keep their own scopes.
- No larger finite Collatz verification, new constant scan, or search
  for increasingly long candidate cycles is used.
- The new conditions are necessary arithmetic constraints. Their
  satisfaction is compatible with the presently unresolved escape and
  cycle cases.
