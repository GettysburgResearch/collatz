# Independent review of coarse-digit memory and the trace profile

Reviewer: `nov23_cycle_ideal`, 23 November 2026.

Reviewed source:
`research/high-variance-20261123/entropy/COARSE_DIGIT_MEMORY_AND_TRACE_FRONT.md`
at SHA256
`63e80adb5334027afc9b99eb499e7e7f4c4454eae26a6be6076319fb32264d24`.

**Result: PASS for the deductions from the explicitly supplied trace and
retained-orbit premises, including (11), (16), and (21)–(24).**
The external trace construction and its analytic inputs are not re-proved
by this review. No scalar log-odds tightness or escape exclusion has been
established.

## Summable error and accumulated binary entropy

For a fixed tail starting at `J`, a block of length `N` and error sum
`E` satisfies `Σ h_b(epsilon)≤N h_b(E/N)` by concavity. The elementary
inequality `-(1-t)log(1-t)≤t` then gives
`N h_b(E/N)≤E log(N/E)+E`. For fixed `J`, division by `log N` and passage
to the limit have upper limit at most the full tail sum `E_J`. The
initial finite segment contributes zero to this normalized limit, and
`E_J→0`. This proves (11); it does not assert that the total entropy sum
is finite.

The log-odds lower bound (8) uses the tail supremum to bound
`log(1-epsilon)` from below, followed by Jensen on `-log(epsilon)`.
The count bound (10) uses the necessary inequality
`epsilon≥1/(1+exp(T))` for the indicated moderate log-odds. Both keep
the original source clock. The predecessor involution exchanges the two
unit residues and preserves the shifted real phase exactly, so the
two-symbol relative-entropy lower bound (14) follows from data
processing. It need not imply tightness of the log-odds observable.

## Uniform bilateral profile

For `s≥-j`, the longer trace has `k` initial steps in which it retraces
from `q_(j+k)` to `q_j` with probability `d_(j+k)/d_j`. Conditioned on
that event, its remaining `j+s` steps give exactly `f_j(s)`. The
complementary conditional expectation is in `[0,C_g]`. Therefore

    f_(j+k)(s) = [d_(j+k)/d_j] f_j(s) + [1-d_(j+k)/d_j] h,
    0 ≤ h ≤ C_g.

This proves the stated difference bound uniformly over **all** allowed
`s`. For each fixed integer `s`, it is a Cauchy bound and gives a single
limit. Taking the limit in the same bound for each `s` yields (16)
with a common constant, so taking the supremum creates no unjustified
exchange of an infinite sum and a limit.

At `s=-L,j=L`, the finite profile is `g(q_L)`, proving (17).
For (18), use `r=j-m≥L` and directly retrace `m` steps to `q_r`;
the upper bound is `g(q_r)+C_g(1-d_infinity/d_r)`, whose tail supremum
vanishes. The positive mean statement (19) follows by taking the limit
of each finite sum under the supplied uniform moving-trace theorem.
It does not imply pointwise convergence at the positive end.

## Ordinary finite paths and the bounded Poisson primitive

For even `N≥2`, `p_N=2^(N+1)-1` is a positive odd ternary unit. Every
later displayed `q_(N,i)` is also a unit, since it is `-1 mod 3`.
For each `i<N`,

    3 q_(N,i)+1 = 2 [3^(i+1) 2^(N-i)-1],

and the bracket is odd. Thus the exact valuation is one and these are
literal ordinary finite paths. Harmonicity contributes a weight `3/2`
for each actual predecessor, proving (22). The reference row sum is
at most two, and positivity gives `D_(m+1)≤2^(m+1)`. Combining the two
bounds gives precisely (23).

For any fixed `0<c<log_2(3/2)`, its upper bound tends to zero uniformly
on `0≤m<floor(cN)`. Nonnegativity then yields (24). If a bounded
solution of `(I-K)psi=g-1` existed on this full positive-unit state
space, telescoping and the Markov property would bound every such sum
by `2||psi||_infinity`, a contradiction.

The domain qualification is essential and is present in the note:
these witnesses vary with `N`, are finite ordinary paths, and use the
supplied full positive-unit trace. They do not construct a single
infinite path or certify membership in a nonperiodic killed domain.
