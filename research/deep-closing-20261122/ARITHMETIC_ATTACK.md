# The tail-aware arithmetic attack on the joint counterquery

## Outcome

This pass tried to turn the strongest current **joint minimal counterquery**
into a contradiction, using the integer source certificate rather than only
its contracting coefficients. It did not prove the universal return or
Collatz. No new convergence theorem is claimed here.

The concrete new deduction is an all-length rigidity statement: a permutation
of the entire prefix `[3,2,2,1] ++ [2]^k` cannot give any different integer
source at the same endpoint, for any `k>=0`. This makes precise why the
expanding negative-seventeen window cannot be repaired by rearranging only
its long local two-run. A successful repair must use further source-tail
information, change the grade histogram, change the endpoint, or make actual
target progress. The proof is elementary and written below; it is not Lean
formalized.

A new literature lead supplies substantially stronger finite-ranking
machinery than a scalar drift estimate, but its author explicitly excludes
the full Collatz map from the finite certificate class. Its theorem was not
imported as an axiom or treated as independently verified.

## Frozen inputs

- PR177, `431d858d1ac92e88f4a58f6610c0d67733dc7242`,
  `research/lean-exact-witness-global-20261121/JOINT_MINIMAL_COUNTEREXAMPLE.md`:
  one supplied minimum-grade, maximum-source counterquery, with its original
  target floor and every nonempty source prefix contracting.
- PR176, `5cb67181758186b372944ef60a1bd09416b97f89`,
  `research/lean-global-resolvent-20261121/overview/central/SOURCE_RECORDS.md`:
  cofinally many records have no unchanged-target lower-grade or
  larger-equal-grade source handoff.
- PR180, `a9f471543d7fed0a76f348e6d97a9d6d44fa369e`,
  `research/central-step-20261122/UNIVERSAL_SOURCE.md`:
  the coupled rational example and its precise non-ordinary scope.
- PR185, `4b0c2c27812db555061f5d9006de82a87e7e364f`,
  `research/central-obstruction-20261122/HEAD_THREE_NEGATIVE_CYCLE.md`:
  actual ordinary entrance to the negative-seventeen shadow.

The map is the shortcut map `T(n)=n/2` for even n and `(3n+1)/2` for odd n.
An accelerated odd gap a is the exact relation `3q+1=2^a u`, with q,u odd.

## 1. The strongest source hypotheses were kept together

The PR177 reduction supplies the same query throughout:

- a least bad target t, so every positive y<t converges;
- a complete powered source `S=2^e q`, `1<=e<=3`;
- an actual complete word `W=P++[1,2,3,4]`, with nonempty P and every gap
  at most four;
- `S+1<t<=2S+1` and `t=3 mod4`;
- every arbitrary-target query at a strictly smaller complete source grade;
- every arbitrary-target query from a larger source at the same grade;
- `T^(k+1)(S)<=floor((t-1)/2)` for every k;
- `3^|B|<2^(sum B)` for every nonempty literal prefix B of W.

These are simultaneous hypotheses on the selected supplied certificate.
They are not permissions to select a new certificate for an enlarged carry.

The proposed route was: use maximality to force a structural constraint on W;
use that constraint to obtain a successful contracting target shadow or an
ordinary smaller merger; then invoke the original target or source induction.
The first arrow has not been proved strongly enough. In particular, strict
contraction of prefixes does not imply that a bounded number of periodic
blocks generates the word, and finite alphabet alone does not give that
conclusion.

## 2. An exact local rigidity theorem

Let `R=4/3`. For an odd-gap inverse branch

`I_a(z)=(2^a*z-1)/3`,

the shifted coordinate is

`I_a(z)-1=(2^a/3)*(z-1)+(2^a-4)/3`.

Consider a word of N gaps containing one 3, one 1, and N-2 copies of 2.
Every such word has total gap 2N, so its inverse affine map is

`I_word(z)=1+R^N*(z-1)+beta_word`.

Number positions from zero. If the 3 is at position i and the 1 at position
j, direct affine composition gives

- if i<j, `beta_word=R^(i+1)-R^(j+1)`;
- if j<i, `beta_word=(R^(i+1)-R^(j+1))/2`.

For example, in the first case the gap 3 contributes `R^(i+1)`.
The earlier gap 3 doubles the coefficient multiplying the later gap-1
correction, producing `-R^(j+1)`. In the second case the earlier gap 1
halves the later coefficient instead. Every gap 2 has zero shifted
correction, so trailing copies of 2 do not enter beta.

### Theorem A: integral permutation rigidity

For every `k>=0`, let

`w=[3,2,2,1] ++ [2]^k`.

Suppose w and a permutation v of w are both exact ordinary gap traces from
integer sources q and q' to the **same** integer endpoint z. Then v=w and
q'=q. Positivity is not needed for the algebraic conclusion; it is retained
in the Collatz application.

**Proof.** Here N=k+4 and

`beta_w=R-R^4=-148/81`.

If two sources at the same endpoint are integers, their difference
`beta_v-beta_w` is an integer. For either displayed formula for beta, its
reduced denominator is exactly `3^b`, where

`b=1+max(i,j)`.

Indeed, after clearing that power of three, the term at the larger exponent
has a numerator prime to three, while the other term is divisible by three.
Division by two in the second formula introduces no factor three and no
factor two remains, since each R-power has even numerator.

Adding an integer cannot change a reduced ternary denominator greater than
one. Thus b=4. The last exceptional gap of v is at position three, and the
other exceptional gap is at position zero, one, or two. There are exactly
six possibilities, independent of k:

| Last exceptional gap | Earlier position | beta_v-beta_w |
|---|---:|---:|
| 1 | 3 at 0 | 0 |
| 1 | 3 at 1 | 4/9 |
| 1 | 3 at 2 | 28/27 |
| 3 | 1 at 0 | 74/27 |
| 3 | 1 at 1 | 68/27 |
| 3 | 1 at 2 | 20/9 |

Only the first is an integer. It is the original word. All remaining
positions are twos, so v=w. The common affine formula then gives q'=q.

### Application to the actual negative-seventeen entrance

The PR185 family has source

`q=2048b+429`

and literal prefix

`[3,2,2,1,2]`,

ending at `r=486b+103`. If r then follows k further twos, the entire
prefix is exactly Theorem A's word with k+1 trailing twos. Thus no
permutation confined to this prefix can supply a different integer source
at its actual endpoint, however long the negative shadow lasts.

This is stronger than checking a list of candidate swaps, but weaker than a
source-record theorem. A later gap 1,3 or4 can change the affine correction.
Changing the histogram can change both the slope and correction. An
alternative complete source may have an entirely different suffix. None of
those possibilities is ruled out by Theorem A.

The previously exhibited complete alphabet-four source
`q=58849709` has five gaps equal to four. It is not a useful test of global
source maximality: complete sources with fewer fours already exceed it.
For a concrete replacement, source `439130458=2*219565229` exceeds its
powered source `235398836`; its complete odd word is

```
3,2,2,3,2,3,2,2,2,3,3,2,2,2,2,3,2,3,1,1,2,2,2,3,1,3,2,3,2,2,1,3,3,2,2,4,1,1,2,3,4
```

This word has two fours and no larger gap, so its complete grade is
strictly below the original five-four grade. Each gap and the endpoint one
were replayed exactly with integer arithmetic in this pass. Consequently
the original long window does not refute a maximal-source theorem.
No all-parameter removal of the negative-seventeen windows from the
maximal-source class was proved in this pass.

## 3. Why the rational relaxation still does not close the integer problem

PR180's exact rational example uses

`x=-6005/2187`, `y=8*x+19=-6487/2187`.

The source has complete gap word `[2,2,2,2,2,2,1]` to one, every nonempty
source-prefix coefficient contracts, and its subsequent source gaps are
all two. The target enters the negative-seven cycle and every positive-time
target coefficient expands. This is a counterexample to a rational
coefficient-only bridge, not a positive integer counterexample.

There is an elementary denominator restriction worth retaining when trying
to repair that relaxation. If a rational source x in lowest terms reaches
one after r accelerated odd steps with total gap A, its exact affine
identity is

`3^r*x+C=2^A`,

with C integer. Its denominator therefore divides `3^r`. A prime-to-three
denominator cannot disappear. This explains the denominator 2187 in the
example. It does not give a contradiction for actual integer sources:
positive finite integer lifts may share arbitrarily long finite parity
prefixes, and their remaining complete tails must still be accounted for.
No inference from compatible finite lifts to one all-time ordinary lift is
made here.

The attempted stronger bridge was to combine this denominator restriction
with source maximality. The required conclusion would be an actual larger
same-grade source or a lower-grade complete source that still covers the
original target. Theorem A shows that the long local two-run alone supplies
neither. The missing construction has to use the subsequent actual tail.

## 4. Deep termination machinery: applicability checked, no theorem imported

A relevant fresh primary author source is Hiroyuki Nashida's two-part
preprint and accompanying Lean repository:

1. *Expanding cycles are not enough: a dichotomy for termination certificates
   of generalized Collatz maps*, revision r3, October 2, 2026:
   <https://github.com/harappa/collatz-termination-certificate-dichotomy>
   and DOI <https://doi.org/10.5281/zenodo.23081447>.
2. *Dimension-free barriers for matrix interpretations of the Collatz
   rewriting system, and the maximal one-class weakenings of the modulo-8
   conjectures of Yolcu, Aaronson and Heule provable by finite abstractions*:
   <https://github.com/harappa/collatz-matrix-interpretation-barriers> and
   DOI <https://doi.org/10.5281/zenodo.23081491>.

The author-described mechanism combines logarithmic height, valuations at
rational periodic points, finite-state weights, and a lexicographic stage.
Thus an expanding periodic rational shadow can be paid for by the number
of remaining 2-adic matching digits, rather than incorrectly treated as a
contracting real multiplier.

The relevant boundary is equally precise. The author defines a finite
residue abstraction to be entangled when one strongly connected component
contains both an expanding cycle and a branching vertex. The README states
that the Collatz map is entangled and lies outside this finite staged
certificate class; it also describes dimension-independent barriers for
specified matrix/automaton ranking families. This is not a theorem that
all conceivable ranks or source-aware proofs are impossible.

**Evidence boundary.** The primary author README and its printed Lean
statements were read. The DOI/PDF endpoint was inaccessible in this pass.
The soundness theorem and examples are reported as Lean formalized by the
author. The decision procedure, nonexistence theorems and matrix barriers
are explicitly described as written proofs, not formalized there. They
were not independently replayed or audited here. They remain a qualified
literature lead, not an accepted repository dependency.

For the present problem, a legitimate import would require a finite
abstraction of the **coupled** state including the actual remaining source
certificate, a proved ranking across every admissible transition, and a
proof that the terminal source state forces target success. Consuming the
finite source word by itself proves only that the bookkeeping procedure
stops reading that word. It does not prove that its final carry returns
below the original target. The explicit negative shadows explain why
that terminal implication must be checked separately.

The earlier primary rewriting paper is Yolcu, Aaronson and Heule,
*An Automated Approach to the Collatz Conjecture*:
<https://arxiv.org/abs/2105.14697> and
<https://doi.org/10.1007/s10817-022-09658-8>.
Its full Collatz rewriting system is equivalent to the desired theorem;
termination of its weakened systems is not termination of that full system.

## 5. The exact unfinished arrow

A closure proof still needs a theorem of this form on the simultaneous
JointBadQuery domain:

> The actual original target has a finite ordinary merger with a positive
> integer below that original target, or an actual target return paid by a
> valid complete source certificate at one of the supplied lower ranks.

A putative structural grammar must prove that it covers every actual
complete extremal source word. A well-quasi-order theorem would additionally
need a proved compatibility or upward-closure property for the successful
physical guards. The finite alphabet `{1,2,3,4}` supplies neither fact.
An abstract well-founded source-only rewrite system cannot replace this
arrow: the source-record theorem already produces cofinal unchanged-target
obstructions for that whole architecture.

The source-target arithmetic was attacked at this arrow. It remains open.
The new rigidity calculation is useful for locating which data a successful
repair must use; it is not a universal descent theorem.
