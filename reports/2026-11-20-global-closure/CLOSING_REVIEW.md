# Independent review of the direct closing attempts

**Verdict: VERIFIED at the three stated local claim boundaries. No correction
is required at the frozen body below.** Neither the physical forward-five
closure nor the infinite root-potential bound is established.

Reviewer: the merger-completion agent. The reviewer independently derived the
inverse-lift and shifted-power identities before reading the root note. The
stopping-grade obstruction, reciprocal-budget argument and source attribution
were then reconstructed independently from their frozen inputs. This is not
an endorsement of every statement in the cited source PRs.

## Exact reviewed artifacts

| Artifact | SHA256 |
|---|---|
| `research/global-closure-20261120/closing-attempts.md` | `956ffcb0d70edfc9caf94cbddeada8259088cd6c187a068fdd798bbfd0da723a` |
| `reports/2026-11-20-global-closure/check_closing_independent.py` | `b9340f7a52bb2b2dbd483b409b2629beb81731da2cd193a86fc598fc8b0fc73c` |
| `reports/2026-11-20-global-closure/closing-independent-report.json` | `7faa3cff2b86dfc069f6647c95387f8e95525277447460d72b610692115f3abb` |

The independent checker requires the reviewed note's exact hash. It uses its
own ordinary and accelerated iterators, exact integer arithmetic and rational
products. It does not import any implementation from the root note or the
merger certificate. The saved numerical scopes are bounded evidence; the
all-parameter conclusions below rest on the written identities and inequalities.

## GCL-001: VERIFIED

For \(x_a=(4^a-1)/3\), \(3x_a+1=4^a\) proves positivity, oddness and
one accelerated step to 1. For \(a\ge2\), its first shortcut hitting time
is exactly \(2a\): after the first odd step the remaining values are the
successive positive powers of two. The congruence
\(4^a\equiv1+3a\pmod9\) proves the ternary-unit condition precisely.

Starting from \(5x_a\), the first odd event has exponent 2 and reaches
\(5\,2^{2a-2}-1\). While the displayed power of two has exponent at
least two, the next odd event has exponent 1. There are exactly \(2a-3\)
such events. The last numerator is
\(2(5\,9^{a-1}-1)\). Because \(9^{a-1}\equiv1\pmod8\), its
2-adic valuation is exactly 3. This proves both the accelerated count
\(2a-1\) and total shortcut count \(2a+2\), with no unverified parity
at the terminal boundary.

Let \(y_a=(5\,9^{a-1}-1)/4\) and \(z_a=5x_a\). The exact recurrences
\(y_{a+1}=9y_a+2\), \(z_{a+1}=4z_a+5\), and the values
\(y_4=911>425=z_4\) prove the stated infinite height obstruction.
The ratio is asymptotic to \((9/4)^a/12\), so it is unbounded. Excluding
\(3\mid a\) still leaves an unbounded infinite sequence of supplied
convergent ternary-unit antecedents.

This refutes only the proposed first-hit-plus-two synchronized height
descent. It does not prove divergence of any member, nor does it prove that
the shifted-power family alone is equivalent to Collatz. The note preserves
both distinctions.

## GCL-002: VERIFIED

On \(x=5+96t\),

\[
3x+1=16(1+18t)
\]

has exact valuation 4 for every integer \(t\ge0\). The two arms are
therefore \(25+480t\) and \(5+90t\). If two fixed legal shortcut words
with respective clocks \(d_1,d_2\) and odd counts \(o_1,o_2\) agreed
on this progression, equality of coefficients would force

\[
\frac{480}{90}=\frac{16}{3}
 =2^{d_1-d_2}3^{o_2-o_1}.
\]

Unique factorization forces \(d_1-d_2=4\), \(o_1-o_2=1\); their
stopping-grade difference must thus be 2.

The actual first-hit data at 25 and 5 are respectively \((16,7)\) and
\((4,1)\), so both have grade \(d-2o=2\). At a common endpoint,
grade telescoping would require the prefix-grade difference to be zero.
This remains true after any number of visits to the \(1,2\) cycle: a full
cycle contributes \((2,1)\) and grade zero. This is a contradiction for
arbitrary fixed clocks, not merely for the clocks searched in a finite test.
Restricting to a nonconstant arithmetic subprogression containing \(t=0\)
preserves the coefficient ratio and the base-point contradiction.

The additional identity (3a) is also correct. For legal
\(x=(2^g z-1)/3\), \(g\ge2\),

\[
T^2(5x)=5\,2^{g-2}z-1.
\]

For the next \(g-2\) shortcut steps, the input is odd until the final
displayed power of two is exhausted. Thus
\(T^g(5x)=5\,3^{g-2}z-1\), while \(T^g(x)=z\). At \(g=2\),
the additional block is empty and the same formula holds. Finally,
\(J^a(x)=4^a x+(4^a-1)/3\) directly gives the stated commutator.

The finite-multiplier and bounded-offset failures concern these specified
return families. They do not exclude a different choice of clocks or a
recursive proof with an unbounded state and a valid decreasing rank. The
review found no broader impossibility claim hidden in the note.

## GCL-003: VERIFIED reconstruction, with the existing result credited

The following inputs were read at their exact pins:

| Source | Frozen SHA and claim boundary |
|---|---|
| main, `research/astra-three-routes/pass3/FINITE_RECORDS.md` | `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, T-A3-651 only; local file SHA256 `82bc394dc7336c43eb38abf13f2bddf837ff227c3d6e85c3bebd3ad327885e3f` |
| PR148, `research/focused-forward-20261120/pressure/PROOF.md` | `55d8968d2ecbc23a91c9c4733929f34be9bf0d28`, H1, root formula (2.9), H3 |
| PR150, `research/pointwise-closure-20261120/STOPPING_BURDEN.md` | `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`, SB1 and SB5 |

The T-A3-651 constant was checked from its argument, rather than assumed
from the title. Its finite-segment terminal correction discards the final
\(q\) odd sources before using injectivity of the endpoint map. The
low-valuation cylinder count and high-valuation endpoint count give

\[
N(X)\le2X\rho^q+\tfrac12(3/2)^q+q,
\qquad \rho^3=3125/3456,
\qquad q=\lfloor(3/5)\log_2X\rfloor.
\]

The exact inequality \(8\,3125^{24}<3456^{24}\), together with the
explicit small-range handling, yields \(N(X)\le5X^{39/40}\).
Integrating this upper bound against \(X^{-2}\) on \([1,\infty)\)
gives the uniform constant 200. A first-hit shortcut path is simple, so
the bound applies to its odd inputs before 1 without assuming convergence
of any source not already under consideration.

Multiplication of the actual odd-step identities gives

\[
2^A=3^h mP,
\qquad P=\prod_{j<h}\left(1+\frac1{3n_j}\right).
\]

Hence

\[
8h-5A=\delta h-5\log_2m-5\log_2P,
\qquad
0\le5\log_2P\le\frac{1000}{3\ln2}.
\]

Both sides of equation (4) follow with their printed signs. At \(m=1\)
the product is empty. Positivity of \(\delta\) is the exact integer
comparison \(3^5<2^8\).

The root supremum has the same domain as the source: every state of an
inverse odd word is a positive odd ternary unit. Reversing such a word
produces a genuine forward first-hit path followed, possibly, by loops at
1. Each appended odd loop contributes score \(-2\). Consequently the
supremum is exactly the supremum of first-hit scores, including zero.
Using the lower side of (4) in one direction and the upper side in the
other proves equation (5) with no limit interchange or empirical extension.

PR150 SB5 already states this constant-error equivalence using its separate
budget 600. The final reviewed note explicitly credits that result. Its
choice of the main-branch budget 200 changes an additive constant and is
not represented as a newly solved root obligation.

## Semigroup boundary

The primary text of Applegate and Lagarias,
[*The 3x+1 Semigroup*, arXiv:math/0411140v2](https://arxiv.org/html/math/0411140v2),
Theorem 1.1 and the surrounding introduction, was inspected. It concerns
the multiplicative semigroup generated by 2 and the listed rational
ratios. In particular, the paper explicitly allows products that do not
correspond to a single ordinary iteration. The note's warning against
using that theorem as pointwise basin closure is correct. The theorem is
not a dependency of the new directed certificate or the three reviewed
local deductions.

## Commands actually executed and their bounded scopes

From the repository root:

```bash
python -X utf8 -B reports/2026-11-20-global-closure/check_closing_independent.py --output reports/2026-11-20-global-closure/closing-independent-report.json
python -X utf8 -B reports/2026-11-20-global-closure/check_closing_independent.py --compare reports/2026-11-20-global-closure/closing-independent-report.json
sha256sum research/global-closure-20261120/closing-attempts.md reports/2026-11-20-global-closure/check_closing_independent.py reports/2026-11-20-global-closure/closing-independent-report.json
```

The exact replay passed:

- 79 shifted-power cases, \(2\le a\le80\), with their full exponent words;
- 3,220 legal unit inverse lifts with odd \(z<1000\), \(2\le g\le30\);
- 800 lift-commutator identities and 512 progression guard checks;
- 3,857 common-endpoint pairs through shortcut clock 96, all with the
  correct grade difference;
- 1,667 first-hit product identities on odd ternary units through 5,001,
  and 6,668 negative-score cycle paddings.

These computations support the implementation-level identities at the
reported finite scopes. The proofs above justify their all-parameter
uses. The unresolved forward-five closure and uniform root bound remain
explicit, and no claimed implication crosses either boundary.
