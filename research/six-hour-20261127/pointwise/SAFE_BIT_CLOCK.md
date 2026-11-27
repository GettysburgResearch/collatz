# A kernel-checked eighty-bit entrance clock for every bad ordinary source

Let $U(n)$ be the ordinary odd Collatz map, $E_j(n)$ its cumulative division clock, and $\mathcal P=\{x:4E_j(x)\le7j\text{ for every }j\ge0\}$. For each positive odd $n$ and each natural $B$ with $n\le2^B$,
$$
 U^j n\ne1\ \text{for all }j
 \quad\Longrightarrow\quad
 \min\{t:U^tn\in\mathcal P\}\le80B.
$$
Consequently $n$ never reaches one if and only if some $t\le80(\lfloor\log_2 n\rfloor+1)$ has $U^tn\in\mathcal P$. The new Lean module is `PermanentSafeBitClock.lean`. Its theorem `first_bad_suffix_bits` bounds the genuine first such date, with separate proofs of both safety and minimality of the classically defined first date. The intrinsic logarithmic equivalence is `bad_iff_bounded_safe_suffix`.

Every state of a bad odd source is at least three. Then $3(3x+1)\le10x$ and the fourth powers retain the quantitative gap
$$
81(3x+1)^4\le10000x^4,qquad
81^j2^{4E_j(n)}(U^jn)^4\le10000^j n^4.
$$
Exact kernel reduction verifies $2\cdot10000^{20}\le10368^{20}$, where $10368=81\cdot2^7$. At $j\ge80B$ there are enough twenty-step groups to absorb $n^4\le2^{4B}$, giving $10000^j n^4\le10368^j$. Cancelling $81^j$ and using $U^jn\ge1$ yields $4E_j(n)\le7j$ at every date after the explicit cutoff. Since the debt $7j-4E_j$ starts at zero, its minimum among the first $80B+1$ debts is also a global minimum. Translating the true clock at a minimizing date yields the required permanent suffix. The reverse implication follows from the exact fixed point at one with exponent two, as proved in the imported ordinary-source module.

This is a finite bound on the search for a starting date of an infinite future predicate. Determining whether a candidate actually belongs to $\mathcal P$ remains unbounded. The first date uses classical minimization on the assumption of a bad source. The module establishes no bad source, computable escape certificate, or universal termination.

The reproducible build starts in an empty output directory with copies of the frozen two parent sources and this module. It checks 10 new theorems and 30 parent theorems at their own source builds, then checks all 40 again through a separate import of the fresh objects. Every declaration uses only standard Lean axioms from the set $\{\mathrm{propext},\mathrm{Classical.choice},\mathrm{Quot.sound}\}$. The module uses natural and integer arithmetic, with no external density or Diophantine premise. The accompanying receipt pins source hashes, fresh object hashes, Lean and Mathlib.

Prepared by the independent all-height auditor, 27 November 2026 UTC.
