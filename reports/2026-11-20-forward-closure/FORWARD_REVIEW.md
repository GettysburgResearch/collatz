# Independent audit of the forward defect argument

Scope: `/workspace/scratch/c6766c1207a3/collatz_forward/research/forward-inverse-defect/PROOF.md`,
as inspected during this research turn. This is a local file review, not a
verdict on a later commit or the full repository. **The closing estimate
remains OPEN.**

## Checked interfaces

- The inverse source domain is exactly \(F_w(\mathbb Z_3^\times)\), with
  normalized Haar mass \(3^{-|w|}\), including the terminal-unit guard.
- The displayed subprobability sum is exactly
  \(1679616/1744125<1\). The prefix-free first-crossing argument therefore
  proves the stated tail, without independence of arithmetic cylinders.
- The dense \(G_\delta\) argument follows by prepending any legal word to
  the fixed inverse orbit at \(-1\). It does not classify positive ordinary
  points of the Haar-null exceptional set.
- The forward inequalities retain the actual inverse past. The cycle
  argument uses finiteness backwards around a finite cycle; it does not
  infer finiteness at a forward successor from a lower bound alone.
- The refined coefficient \(c_*=3/\log_2(3/2)\) cancels exponent-one growth
  exactly. For exponents at least two, the supplied uniform positive-gain
  proof and the explicit constants \(M=56\cdot2^{43}\), \(1/16\) check.
  A positive ordinary path cannot have an eventual all-one exponent tail.
- The coefficient-5 hypothesis yields the quantitative first-small-hit
  estimate. The coefficient-\(c_*\) hypothesis excludes escape but does
  not itself provide that quantitative estimate by the same local drift.
- The one-odd-step terminating examples have the stated ternary depth and
  supply large finite scores. They do not refute a height-normalized bound.

No proof of finiteness of \(W(1)\), of either global height bound, or of
Collatz was found in the argument or is asserted by this audit.

## A further exact relation between the proposed hypotheses

There is a useful distinction between a pointwise formula being weaker and
the existential closing statements being logically different. The following
three statements are equivalent, using the proved dynamics in the inspected
note:

1. Some \(C\) satisfies \(W(n)\le5\log_2n+C\) at every positive odd
   ordinary ternary unit.
2. Some \(C\) satisfies \(W(n)\le c_*\log_2(n+1)+C\) on that same domain.
3. Collatz holds and \(W(1)<\infty\).

The implication 1 to 2 is immediate because \(c_*>5\). The inspected proof
gives 2 to Collatz, and evaluating at 1 gives \(W(1)<\infty\).
Here is the reverse implication with an explicit additive constant.

For a positive odd unit \(t\) in the basin of 1, write \(d(t),a(t)\) for its shortcut
first-hit time and odd count. Its reversed ordinary path gives

\[
W(t)\le W(1)+5d(t)-8a(t).                           \tag{A}
\]

If \(W(1)\) is finite, this is a genuine finite bound on every such \(t\).
For the eleven odd ternary units below 33, exact integer checks give

\[
5d(t)-8a(t)-5\log_2t\le1.                          \tag{B}
\]

No numerical logarithm is needed: if \(q=5d(t)-8a(t)>1\), check
\(2^{q-1}\le t^5\); if \(q\le1\), the inequality is immediate.

For any other unit \(n\) in the basin, follow its actual odd orbit to its
first value \(t<33\). The inspected positive drift of
\(R=W-5\log_2 n\) gives \(R(n)\le R(t)\). Combining (A) and (B),

\[
\boxed{W(n)\le5\log_2n+W(1)+1
\quad\text{for every positive odd unit }n\text{ in the basin of 1}.} \tag{C}
\]

Under Collatz, that is the whole required domain, proving 3 to 1.
The distinction in scope is indispensable: (C) does not bound any hypothetical
nonconvergent component. Finiteness of \(W(1)\) alone has not been shown to
exclude such a component.

This equivalence says that the closing obligation includes the additional
uniform all-ancestor statement \(W(1)<\infty\). It does not show whether
Collatz alone implies that statement, so it is not a proved strict logical
strengthening of Collatz.

The finite table used in (B) is:

| \(t\) | \(d(t)\) | \(a(t)\) | \(5d-8a\) |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 5 | 4 | 1 | 12 |
| 7 | 11 | 5 | 15 |
| 11 | 10 | 4 | 18 |
| 13 | 7 | 2 | 19 |
| 17 | 9 | 3 | 21 |
| 19 | 14 | 6 | 22 |
| 23 | 11 | 4 | 23 |
| 25 | 16 | 7 | 24 |
| 29 | 13 | 5 | 25 |
| 31 | 67 | 39 | 23 |

The integer checks are included in `check_persistent_defects.py` under
`check_forward_closing_fixture`.
