# Compensated prefixes and synchronized steps in the low interval domain

**Status: PROVED coverage families in Lean core. The remaining low interval
coverage, full Collatz, and the original residue implication remain OPEN.**

Formal source: [`Collatz/LowIntervalRefinement.lean`](lean/Collatz/LowIntervalRefinement.lean).
The common active domain is the `Interval` of `BoundedGapCofinal`:

\[
 0<t\le2s+1.
\]

## 1. Keep the even run and consume a growing odd prefix

Suppose the supplied source certificate is

\[
 s=2^e q,\qquad \operatorname{Certificate}(q,w\Vert\tau),
\]

where `w` is nonempty. Let `r=length(w)`, `A=total(w)`, and `C=C(w)`.
Assume the finite, exact coefficient condition

\[
 2^A\le3^r.
\]

The source prefix identity gives an integer endpoint `u` with

\[
 3^rq+C=2^Au,\qquad\operatorname{Certificate}(u,\tau).
\]

Since the nonempty positive prefix has `C>0`, this forces `u>q`.
Consequently the new known source `s'=2^e u` is strictly larger than `s`,
while retaining **the same initial even exponent** and the literal supplied
suffix. Its complete grade is strictly lower:

\[
 \Gamma(e;\tau)\prec\Gamma(e;w\Vert\tau).
\]

Every old wanted target stays in the interval: `t<=2s+1<2s'+1`.
`scaled_prefix_rewrite` proves the complete arithmetic and rank data;
`coefficient_interval_rule` invokes exactly that lower-ranked interval
query. It neither moves the target nor obtains a new source witness from
an already proved target.

## 2. Entire unbounded languages covered

The following are direct proved instances:

- `first_gap_one_rule`: every source word starting with gap one, at every
  initial even valuation. The new odd core is `(3q+1)/2>q`.
- `balanced_runs_rule`: every word beginning with `k` twos followed by `k`
  ones, for arbitrary `k>=1`. Its prefix coefficient is `(9/8)^k`.
- `compensated_gap_rule`: a gap `a>=2` followed by `2a-3` ones. Its prefix
  coefficient is `(9/8)^(a-1)`. For the remaining alphabet this includes
  `(2,1)`, `(3,1,1,1)`, and `(4,1,1,1,1,1)`.

Thus a residual source certificate may be assumed to start with gap two,
three, or four, and no nonempty supplied prefix satisfying the displayed
coefficient condition can remain untreated by these interval rules.
The lengths in the two-run rule are unrestricted; this is not a larger
finite numerical search.

## 3. Consume a source gap and a paid target step

Suppose `e>=1` and the literal first source gap is `a`:

\[
 s=2^e q,\qquad 3q+1=2^a u,\qquad
 \operatorname{Certificate}(u,\tau).
\]

Set `b=min(a,e+1)`. Whenever

\[
 3t+1=2^b v,
\]

the target has an actual one-gap prefix to the positive integer `v`. The
endpoint may be even. Define the child source as follows:

| Condition | Child source | Child initial even exponent |
|---|---|---|
| `a<=e+1` | `2^e u` | `e` |
| `e+1<a` | `2^(a-1) u` | `a-1` |

In both cases, with the displayed child denoted by `s'`, the exact identity is

\[
 2^b(2s')=6s+2^{e+1}.
\]

The old interval bound and `e>=1` therefore give

\[
 2^b v=3t+1\le6s+4\le6s+2^{e+1}=2^b(2s').
\]

Cancellation shows `0<v<=2s'`, a stronger bound than the child interval
requires. In the first case, deleting the old source gap while retaining
`e` strictly lowers the complete rank. In the second case, remove the
old grades `2e+1` and `2a`, and insert `2a-1`. The inserted grade is strictly
below the removed grade `2a`; the literal supplied suffix is unchanged.
This again strictly lowers the same complete source rank.

Theorems `matched_gap_rule` and `shortened_gap_rule` formalize these two
cases; `synchronized_gap_rule` combines them with the single divisibility
condition `2^min(a,e+1) | (3t+1)`. The proof only uses the lower-rank
interval hypothesis, the original supplied source tail, and the explicit
target prefix.

For example, when `e=1`, every residual first source gap in `{2,3,4}` needs
only two target halvings. Thus all such states with `t=1 mod 4` close,
regardless of the first source gap. For `e=2` and `a` in `{3,4}`, the rule
closes every target `t=5 mod 8`. There is no upper bound on `e`, `a`, the
tail length, or the target in the synchronized theorems themselves.

## 4. The exact finite terminal case

An empty odd source certificate forces `q=1`. After the already proved
elimination of initial valuations at least four, the remaining source is
`2^e<=8`, so its entire interval lies in `1..17`.
`terminal_range` supplies a hitting time at most13 for each member of this
finite set, using ordinary kernel `decide` on an explicitly recursive
bounded-clock decision procedure. `terminal_even_rule` applies it to the
empty-certificate case.

The value17 is forced by the residual domain and `e<=3`; it is a complete
terminal case, not an adjustable verification threshold. No `native_decide`,
custom axiom, or universal convergence premise is used.

## 5. Remaining states

Together with the cofinal gap-four reduction, the unhandled interval states
have a nonempty odd certificate over gaps at most four, initial even
valuation one through three, and an odd wanted target satisfying

\[
 s+1<t\le2s+1.
\]

The first odd gap is no longer one, and all compensated-prefix languages
above are discharged. Writing `a` for the first odd gap, every remaining
state also fails the synchronized divisibility condition:

\[
 2^{\min(a,e+1)}\nmid3t+1.
\]

There is still no proof that every remaining supplied certificate admits a
successful lower-ranked interval query or a target merger. The module
proves the listed coverage families rather than assuming that final
selection theorem.
