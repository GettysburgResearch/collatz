# Global proof search: joint comparisons, affine closure, and rank compatibility

**Status: no complete Collatz proof was obtained.** These searches seek a finite,
globally valid induction scheme, not a finite range of convergent inputs. Every
unresolved progression is retained as an explicit proof obligation. Counts below
describe search output; the accompanying Lean modules determine which exported
certificates have been checked by the kernel.

## 1. What a successful complete search would prove

Write `B(n)` for ordinary Collatz convergence to 1 and define

\[
C_3(n): B(n)\leftrightarrow B(3n),\qquad
C_5(n): B(n)\leftrightarrow B(5n),\qquad
C_\psi(n): B(n)\leftrightarrow B(2n-1).
\]

A row has a positive affine source `n=M*t+r`, for every natural parameter
`t>=0`. It records two words joining the two arms of its comparison at the same
affine endpoint. Ordinary forward and inverse Collatz edges preserve `B`.
Additional edges may invoke another comparison only at a source with a strictly
smaller, common natural-number rank.

For constant positive integer weights `w`, a query of kind `q` at `u=a*t+b`
inside a row of kind `p` is accepted only if

\[
0<b,\qquad w_q a\le w_pM,\qquad w_qb<w_pr.
\]

These inequalities imply `w_q*u < w_p*n` for **every** parameter. A complete
cover, plus the source-1 base cases, would therefore prove all active comparisons
by simultaneous strong induction. Universal tripling comparison implies Collatz
through the repository's reverse-generation theorem. Universal psi comparison
implies Collatz through the existing psi-closure theorem. No equal-clock or
equal-odd-count condition is imposed on either arm.

The ordinary word alphabet is `D` (double), `E` (halve an even form), `O`
(`(3*x+1)/2` on an odd form), and `I` (`(2*x-1)/3` when positive and integral).
`M3`/`V3` and `M5`/`V5` are multiplier queries in the homogeneous search.
The affine search uses `+3`, `-3`, `+5`, `-5`, `+psi`, and `-psi`. In a reverse
query the smaller-rank source is the resulting form. Paths are equivalences in
both directions.

## 2. Main search checkpoints

| System | Source modulus | Successful cells | Explicit unresolved cells |
| --- | ---: | ---: | ---: |
| Joint 3/5, weights 8/5, odd sources | 1440 | 605/720 triples; 398/720 fives | 437 total |
| Pure psi, rank `n`, every positive source | 1440 | 1265/1440 | 175, all even |
| Joint 3/psi, weights 2/1, every positive source | 1440 | 1440/1440 triples; 1265/1440 psi | The same 175 psi cells |
| Pure psi, rank `n` if odd and `2n` if even | 1440 | 1290/1440 | 150, all odd |
| Pure psi, rank `n*2^v2(n)` | 1440 | 1290/1440 | 150, all odd |
| Pure psi, rank `n^5*8^v2(n)` | 1440 | 1290/1440 | 150, all odd |
| Pure psi, rank `n^12*130^v2(n)` | 1440 | 1290/1440 | 150, all odd |
| Joint 3/5/7, weights 8/5/5, odd sources | 10080 | 11509/15120 | 3611 total |

The triple type is redundant in the constant 2/1 affine checkpoint: for odd `u`,
the ordinary step `u -> a=(3u+1)/2`, followed by a psi query at `a`, reaches
`2a-1=3u`. Even sources first halve. Running the pure-psi search independently
reproduced all 1265 psi rows.

Residue-dependent integer weights were also searched. A full-source, modulo-6
two-type rank found all 1440 triple cells and 1350 psi cells, leaving 90 psi
cells. Its weights, indexed by source residue 0 through 5, are

```
triple = [114, 1666, 16384, 440, 13653, 75]
psi    = [24, 41, 250, 32, 71, 215]
```

This remains an incomplete search checkpoint. It includes **both even and odd**
source cells. In contrast, an earlier odd-source-only 3/5 residue experiment
allowed even queries without proving that halving decreased the residue rank;
that earlier coverage count is not a valid complete-induction antecedent and
must not be used as one. The corrected homogeneous variant restricts every
recursive query to an affine source that is identically odd.

## 3. A uniform new parity mechanism

There is an exact rule valid for every positive `m`:

\[
C_\psi(m)\ \land\ C_\psi(4m-1)
\quad\Longrightarrow\quad C_\psi(2m).
\]

The two root arms are `2m` and `4m-1`. On the first arm, halve, use
`Cpsi(m)`, then take an odd step. On the second arm, use `Cpsi(4m-1)`, take an
odd step, and halve twice. Both arrive at `3m-1`:

```
left word:  E, +psi, O
right word: +psi, O, E, E
```

This rule uses no tripling query. The simplest sufficient natural-number rank is

\[
R(n)=\begin{cases}n&n\text{ odd},\\2n&n\text{ even}.\end{cases}
\]

Both calls strictly decrease it: `R(m)<=2m<4m=R(2m)` and
`R(4m-1)=4m-1<4m`. The direct search with parity weights `[2,1]` left **exactly
the same set of 150 odd residues** as the stronger valuation ranks, rather than
merely the same number. Thus the valuation penalty is unnecessary for the
uniform even rule and did not improve this frontier.

The initially tested rank

\[
\mu(n)=n\,2^{v_2(n)},
\]

also makes both calls strictly decrease:

\[
\mu(m)=\mu(2m)/4,
\qquad
\mu(4m-1)=4m-1<\mu(2m).
\]

It consequently handles **all even psi sources by one unbounded schema**.
It also gives an exact global reduction: Collatz is equivalent to two-way psi
invariance on every positive **odd** source. If all odd comparisons hold, strong
induction on `n` supplies the even comparison from `n/2` and the assumed odd
comparison at `2n-1`. This is a reduction, not a proof of the odd condition.
The two-way qualification matters: the rule uses the reverse direction of
`Cpsi(4m-1)`; no claim is made about forward-only odd-source closure.

## 4. Why the complementary rank covers do not close the proof

Linear rank handles all odd cells in the recorded modulus, while the valuation
rank handles all even cells. Their union is not a well-founded proof. A concrete
infinite family exhibits the obstruction.

For any `t>=0`, let

\[
n=6t+4,\qquad u=8t+5=\frac{4n-1}{3}.
\]

The valuation-row proof of `Cpsi(n)` queries `Cpsi(u)`. Since `n` is even and
`u` is odd, `mu(u)=u<2n<=mu(n)`. The linear-row proof of `Cpsi(u)` queries

\[
C_\psi\!\left(\frac{3u+1}{4}\right)=C_\psi(n).
\]

The two transports are exact inverses. Their slope product is
`(4/3)*(3/4)=1`, and the affine offsets cancel exactly. Both individual rank
claims are correct, but selecting the two proofs together creates a cycle.
`search/affine-reciprocal-cycle.json` records both words and their exact affine forms.
This is an obstruction to these **selected proof choices**, not a theorem
excluding other certificates or other global ranks.

## 5. Exact valuation guards and attempts to break the cycle

For a whole affine cell, the valuation search uses

\[
v_2(Mt+r)\ge\min(v_2(M),v_2(r)).
\]

For a query `a*t+b`, if `v2(b)<v2(a)`, its valuation is exactly `v2(b)` for
every parameter. Proportional source forms are handled separately with the exact
valuation difference, so unbounded-valuation cells are not replaced by a finite
parity assumption.

For ranks `n^k*c^v2(n)`, the checker tests every binomial coefficient of the
weighted query polynomial against the root polynomial, with a strict constant
term. It uses integer arithmetic throughout. The effective valuation factors
just above `3/2`, including `(k,c)=(5,8)` and `(12,130)`, retained the same 150
odd unresolved cells. The pair `(12,129)`, just below the threshold, left 165
mixed-parity cells.

As a separate global test, every source progression was shifted by `K*1440`,
for `K=1,10,100`, to remove small-intercept obstructions. Neither the linear nor
the interpolated-rank coverage changed. Thus a finite checked base interval
alone does not close this recorded frontier.

A focused attempt to bypass the reciprocal cycle enlarged ordinary excursions
from 100 times the source-cell coefficients to 1000, 10000, and 1000000 times
those coefficients. It found no additional linear-rank or interpolated-rank
rows. The largest visited graph had 13144 nodes, below the 200000-node cap.
This is a bounded-search result, not a proof that alternative words do not exist.

Other attempts included adaptive refinement by 2, 3, and 5; additional multiplier
types; and directed reverse-tripling/forward-five rules with restricted source
classes. None supplied a complete cover. Large raw adaptive tables are not
needed to preserve these findings.

The remaining global target is a set of alternative odd-source transports whose
entire composed query graph has one well-founded order, or whose reciprocal
components have a proved exit. The existing exact even-source schema can then
be reused. Mere coverage percentages or separate local ranks do not discharge
that obligation.

## 6. Reproduction

Run these commands from the `search/` directory. The JSON outputs
retain successful words and all unresolved cells.

```bash
python3 search_joint_descent.py --modulus 1440 --height 100 --cap 30000 > joint-descent-1440.json
python3 search_affine_types.py --weights psi:1 --output pure-psi.json
python3 search_affine_types.py --weights 3:2,psi:1 --output joint-3-psi.json
python3 search_affine_types.py --weights psi:2/1 --rank-modulus 2 --output pure-psi-parity-2-1.json
python3 search_valuation_rank.py --factors '' --output valuation-psi.json
python3 search_valuation_rank.py --power 5 --base 8 --factors '' --output valuation-5-8.json
python3 search_valuation_rank.py --power 12 --base 130 --factors '' --output valuation-12-130.json
python3 search_multiset.py --output joint-3-5-7.json
python3 diagnose_rank_cycles.py --output selected-rank-cycles.json
```

`diagnose_rank_cycles.py` selects a linear certificate at odd sources and a
valuation certificate at even sources and records actual cycles in the resulting
integer query graph. Its output is explicitly a diagnosis of the selected
templates, not a convergence test or a proof of impossibility.

For a compact publication checkpoint, retain this note, the relevant search
scripts, the small affine cycle data, and the kernel-checked Lean exports.
The 50 MB adaptive raw table is reproducible and need not be committed.
