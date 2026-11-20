# Elementary dispersion of prime height

**Status: PROPOSED, with a complete elementary written proof. Not yet part
of the accepted baseline.** Collatz remains open. Frozen input:
`55d8968d2ecbc23a91c9c4733929f34be9bf0d28`, 20 November 2026.

This route replaces a fixed-dimensional S-unit argument by an ordinary
arithmetic budget: common prime powers divide the correction between two
physical orbit states, and the correction is controlled by logarithmic
height variation. The resulting theorem needs no bound on the valuation
alphabet, number of powered factors, word complexity, or prime support.
It uses no deep external analytic theorem and no new finite verification.

Write the odd accelerated orbit as

\[
 n_{j+1}=\frac{3n_j+1}{2^{a_j}},\qquad a_j=v_2(3n_j+1)\ge1.
\]

For a finite prime set \(S\), write
\([n]_S=\prod_{p\in S}p^{v_p(n)}\).

## Strongest results

1. **Uniform dispersion on every hypothetical ordinary escape.** For each
   fixed integer \(s\ge1\),
   \[
   \sup_{|S|\le s}
   \frac{\sum_{j<N}\log[n_j]_S}{\sum_{j<N}\log n_j}
   \longrightarrow0
   \]
   on every non-eventually-periodic positive orbit. The set \(S\) may be
   chosen after seeing the entire prefix and may change with \(N\).
   There is also a count-weighted version: for every \(\varepsilon>0\),
   the maximum proportion of states with \([n_j]_S\ge n_j^\varepsilon\)
   tends to zero, uniformly over sets of at most \(s\) primes.
2. **An explicit finite-history inequality.** Put
   \(x_j=\log_2 n_j\), \(W_N=\sum_{j<N}x_j\). For every integer
   \(r\ge2\) and every \(|S|\le s\),
   \[
   \sum_{j<N}\log_2[n_j]_S
   \le\frac{s}{r}W_N+sr x_0+5srN+B_{N,r},
   \]
   where \(B_{N,r}\) is the total logarithmic height of the final fewer
   than \(r\) states. This is a theorem for actual finite ordinary
   trajectories, including trajectories with arbitrarily large divisions.
3. **Unrestricted positive cycles.** If a primitive cycle has mean
   logarithmic height \(H>0\), then
   \[
   \frac{\sum\log_2[n_j]_S}{\sum\log_2 n_j}
   \le \frac{s}{r}+\frac{5sr}{H}\qquad(r\ge2).
   \]
   Thus every long primitive cycle must distribute its aggregate height
   over an unbounded number of primes, uniformly over which primes are
   chosen. If all its odd states together use at most \(s\) primes, then
   \(H\le20s^2\) and its odd period is less than \(3\cdot2^{20s^2}\).
   This supplies an elementary effective finiteness result for that
   restricted class, not an exclusion of arbitrary cycles. Quantitative
   S-unit theory already gives bounded-prime-support cycle finiteness;
   no priority claim is made for that corollary.

The complete proof is in [PRIME_HEIGHT_ESCAPE.md](PRIME_HEIGHT_ESCAPE.md).
The central inequality is

\[
 \log_2\gcd(n_i,n_j)<x_i-x_j+3(j-i),\qquad i<j.
\]

At most one state in a short block can hold a large power of each chosen
prime unless the block pays for a large change in height. Total variation
of logarithmic height is at most \(x_0+2N\), making that payment summable.

## First unsupported step

The theorem forces a particular arithmetic behavior on any escape; it
does not prove that behavior impossible. A closing argument would have
to establish some persistent concentration, return, or conflicting
arithmetic constraint for one ordinary surviving history. Finite prime
support at each individual time supplies no such bound on the whole
history. Arbitrary positive cycles may also use arbitrarily many primes.

[ADELIC_LEDGER.md](ADELIC_LEDGER.md) gives the exact cancellation that
blocks the naive three-place product argument, the discarded compression
route, and the stronger mechanism used here. It also proves an ordinary
control: for every fixed finite \(S\), there are arbitrarily large
one-step convergers with \([n]_S=1\). Uniform pointwise concentration is
therefore not a possible closing lemma.

## Provenance and evidence

The local-window idea began with a sharp S-part theorem. During joint
checking, the root agent supplied the elementary gcd replacement and the
height-variation charging argument; the adelic agent independently
reconstructed the inequalities and assembled the proof. Exact
primary-source comparisons, including closely related recent
multiplicative-rank work, appear in [SOURCES.md](SOURCES.md). No external
theorem is a dependency of the main result.

[CLOSING_ATTEMPT.md](CLOSING_ATTEMPT.md) attacks the remaining bridge
through prime-factor flux, growing p-adic valuations, and ordinary
representation complexity. It records the exact identities and a
fixed-source arithmetic control that prevent those attempted shortcuts
from supplying the missing retention statement.

These are written proofs. No numerical census, expanded verification
range, computation of hypothetical cycles, or empirical inference is
used. The full Collatz conclusion remains OPEN.
