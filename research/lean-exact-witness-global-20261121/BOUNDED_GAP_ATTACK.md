# Cofinal certified predecessors and the alphabet-four reduction

**Status: unconditional Lean theorems for the predecessor construction and
all high-gap comparison cases; the final low-gap interval step remains OPEN.**
The map is the ordinary shortcut map, with one halving per clock. A complete
odd certificate is the actual supplied positive gap word ending at one.
The construction never assumes convergence of the wanted target.

## 1. A fixed four-letter inverse alphabet is cofinal

Let \(q\) be a positive odd integer not divisible by three, with a supplied
complete certificate \(\tau\). For every bound \(N\), there are \(p>N\)
and a finite word \(W\), all of whose letters lie in \(\{1,2,3,4\}\), such
that

\[
 \operatorname{Certificate}(p;W\Vert\tau).
 \tag{B1}
\]

The tail is literally the supplied word. Its length and exponents are
unrestricted. The new prefix can be arbitrarily long.

Here is the exact inverse table. Write \(q=18v+r\):

| \(r\) | Gap \(a\) | Selected predecessor \(p\) |
|---|---:|---|
| 1 | 4 | \(96v+5\) |
| 5 | 3 | \(48v+13\) |
| 7 | 4 | \(96v+37\) |
| 11 | 3 | \(48v+29\) |
| 13 | 2 | \(24v+17\) |
| 17 | 1 | \(12v+11\) |

Every row satisfies \(3p+1=2^a q\), with \(p>1\) odd and prime to three.
At \(q=1\), it chooses the nonterminal predecessor five. Thus the table
can be iterated indefinitely, and each iteration adds an actual positive
ordinary path to the supplied certificate.

To prove these predecessors exceed every bound, no growth assumption on
individual inverse edges is used. Any finite interval has a common upper
bound \(K\) on the hitting clocks of its members that are already in the
basin. This is finite induction with a case split on basin membership; it
does not assert that every integer in the interval converges. On the other
hand, every hitting clock for a predecessor obtained after \(K+1\) table
steps has length at least \(K+1\): peel off each nonterminal ordinary prefix.
That predecessor is certified, so it cannot remain in the chosen interval.

The Lean declarations are `unit_predecessor`, `predecessor_clock`,
`bounded_basin_clocks`, `long_predecessor`, and `cofinal_predecessors` in
[`BoundedGapCofinal.lean`](lean/Collatz/BoundedGapCofinal.lean).

### Four is the exact threshold

Every complete certificate with all gaps at most three represents one.
Indeed, induct from the terminal end: if the next odd endpoint is one,
then \(3n+1=2^a\), for \(1\le a\le3\), forces \(a=2\) and \(n=1\).
Combining this with B1 at \(q=1\) proves the exact equivalence

\[
 \left[\forall N\ \exists p>N\ \exists W:\quad
  \operatorname{Certificate}(p;W),\quad \forall a\in W,\ a\le H\right]
  \quad\Longleftrightarrow\quad H\ge4.
 \tag{B2}
\]

This is `gaps_at_most_three` and `cofinal_alphabet_iff`. The alphabet bound
is not an experimental cutoff.

## 2. An arbitrary high gap pays for any required source height

Recall the complete-source grade multiset

\[
 \Gamma(e;A)=\bigl(\{2e+1\}\text{ if }e>0\bigr)
              \uplus\{2a:a\in A\}.
\]

At the largest grade whose multiplicity changes, a lower multiplicity is
a strict decrease. This well-founded order was proved in the earlier
`GapMultiset.lean`. It allows one high grade to pay for any finite number
of lower grades.

Suppose a supplied source word has the form \(U\Vert(a)\Vert\tau\), with
\(a\ge5\). Peel its actual prefix through this gap, obtaining an odd
endpoint \(q\) and the literal certificate \(\tau\). The identity
\(3u+1=2^a q\) implies \(3\nmid q\). Apply B1 at any requested bound
\(N\). Then

\[
 \operatorname{Certificate}(p;W\Vert\tau),\qquad p>N,
 \qquad
 \Gamma(0;W\Vert\tau)<\Gamma(0;U\Vert(a)\Vert\tau).
 \tag{B3}
\]

Every inserted odd grade is at most eight; the removed gap supplies a
grade at least ten. The complete tail cancels in the comparison. No
arithmetic entrance guard or limit on the new prefix length remains.
The same construction works if the source also has an initial even run.

An initial even run \(e\ge4\) supplies a grade at least nine and therefore
also pays for a cofinal four-letter prefix. If the current odd source is
divisible by three, first peel its actual first odd edge to reach a unit
tail. The empty word represents one and is treated directly. This gives
`large_even_replacement` for every supplied powered certificate.

These are source rewrites. They do not construct a convergence certificate
for an arbitrary wanted target by themselves.

## 3. The interval comparison program and its precise residual

Use the active comparison domain

\[
 \operatorname{Interval}(S,t):\quad 0<t\le2S+1.
 \tag{B4}
\]

The claim is that a supplied certificate for \(S\) transfers convergence
to \(t\), using the existing common multiset induction. This larger domain
contains every mandatory psi pair \((S,2S-1)\) and reverse-tripling pair
\((3n,n)\). It also contains additional pairs, which must be proved.

For B3 or the large-even rewrite, choose the new known source above the
unchanged target. The child pair is automatically active and the complete
source grade strictly decreases. These close every interval case with an
odd gap at least five anywhere, or an initial even run at least four.

The other unconditional branches are as follows:

- Source one leaves only targets one, two, and three, with explicit paths.
- A nonterminal odd source can take one ordinary shortcut step. The known
  source increases and its certificate grade decreases, so its entire old
  interval remains active.
- An even source can take one halving step whenever \(t\le S+1\).
- If the target is even, halve it too. Its basin membership is unchanged,
  and the smaller target lies in the halved source's active interval.

Consequently the sole premise of `collatz_of_low_interval` is the explicitly
defined `LowIntervalStep` on the following states:

\[
\boxed{
 S=2^e q,\quad e\in\{1,2,3\},\quad
 \operatorname{Certificate}(q;A),\quad A_i\le4,
 \quad t\text{ odd},\quad S+1<t\le2S+1.
}
\tag{B5}
\]

For each such state, the required step may use every already-established
interval claim with a strictly smaller complete-source grade. Its word
length, integer values, and number of gap-four letters are all unbounded.
`interval_complete_of_low` proves that closing B5 covers the entire active
domain; the earlier common induction then yields full Collatz and hence
the original residue implication. **B5 is an unproved premise, not an axiom
or an established dispatcher.**

The simultaneous suffix and retained-even attacks sharpen parts of B5.
Their separate modules state their exact guards; the broader B5 definition
keeps the main reduction independent of those refinements.

### Actual refinements inside the low alphabet

[`LowIntervalRefinement.lean`](lean/Collatz/LowIntervalRefinement.lean)
consumes any nonempty supplied odd prefix \(W\) satisfying
\(2^{\sum W}\le3^{|W|}\), while keeping the same initial even run. The
positive affine correction makes the odd endpoint strictly larger than
the old odd core. Thus the known powered source grows, the unchanged
target stays active, and deleting the actual prefix strictly lowers the
complete-source grade. This covers every leading one, every balanced
prefix \((2^{[k]},1^{[k]})\) with \(k>0\), and every compensated prefix
\((a,1^{[2a-3]})\) with \(a\ge2\). The empty odd word with \(e\le3\)
leaves only targets up to seventeen and is handled by explicit kernel
hitting certificates.

[`RetainedEvenReset.lean`](lean/Collatz/RetainedEvenReset.lean) keeps two
initial halvings while removing an initial run of three. For \(S=8q\),
its four exact inverse words yield \(p\ge2q\), so the child source
\(4p\ge S\) retains every old interval target. It replaces grade seven
by grade five and odd grades at most six. The cover includes every unit
odd core except one, \(q=7\bmod9\), and \(q=19\bmod27\).

[`RetainedEvenBoundary.lean`](lean/Collatz/RetainedEvenBoundary.lean)
closes every initial-run-one case whose first odd gap is at least four.
Writing \(q=4p+1\), it uses the child source \(8p=S-2\), with initial
run three and the first odd gap reduced by two. The only two odd targets
above that child's interval ceiling are handled exactly:

\[
 16p+3\xrightarrow{(1,3)}9p+2\le16p+1,
 \qquad B(16p+5)=B(4q+1)=B(q).
\]

The complete tail is retained and the new initial grade seven is below
the removed first-gap grade. There is no extra residue condition on this
case. The [retained-even note](MERGER_RETAINED_EVEN.md) gives both
constructions and the precise meaning of the exceptional cells.

Finally, `synchronized_gap_rule` puts \(b=\min(a,e+1)\), where \(a\)
is the first supplied source gap. If \(2^b\) divides \(3t+1\), write
\(3t+1=2^b v\). With the actual source endpoint \(u\), use the known
child \(S'=2^e u\) if \(a\le e+1\), and \(S'=2^{a-1}u\) otherwise.
The exact identity

\[
 2^b(2S')=6S+2^{e+1}\ge3t+1
\]

places \(v\) in the child's interval. The target has the genuine ordinary
prefix of gap \(b\); the full source tail is retained; and the initial
grade plus consumed odd grade strictly decreases. In particular, every
remaining initial-run-one case with \(t=1\bmod4\) closes.

Combining these proved rules leaves the following necessary low-valuation
shapes for an uncovered state. Write \(c=\nu_2(3t+1)\):

| Initial run \(e\) | First source gap \(a\) | Remaining target gaps \(c\) |
|---|---|---|
| 1 | 2 or 3 | 1 |
| 2 | 2 | 1 |
| 2 | 3 or 4 | 1 or 2 |
| 3 | 2 | 1 |
| 3 | 3 | 1 or 2 |
| 3 | 4 | 1, 2, or 3 |

The source word is nonempty, all its gaps are at most four, and it has no
nonempty prefix with a noncontracting coefficient. For \(e=3\), the known
odd core must additionally be divisible by three or belong to one of the
two excluded ternary cells. This table is a consequence of the proved case
rules, not a claim that the remaining infinite word languages close. The
formal general closing theorem keeps the explicit `LowIntervalStep`
premise. See [LOW_INTERVAL_REFINEMENT.md](LOW_INTERVAL_REFINEMENT.md).

## 4. Executable complete-source construction

[`cofinal_rewrite.py`](gap-search/high/cofinal_rewrite.py) accepts the actual
complete source certificate, its initial even run, and an arbitrary integer
bound. It validates every supplied odd edge and the terminal one, selects a
high gap or a sufficiently long initial even run, applies the six-row table
until the bound is exceeded, and checks the full new certificate and strict
grade decrease. It never follows the wanted target's orbit.

The construction has no search cutoff or `UNRESOLVED` return on valid inputs
meeting its high-gap/even-run premise. Termination follows from B1's clock
argument. The exact Python replay uses six complete certificates, including
a ternary-nonunit odd source and a high gap inside the word, at five requested
bounds up to \(2^{1024}\). It checks both normal and optimized execution.
Those runs validate the implementation; the all-bound theorem is the Lean
proof, not the finite list of fixtures.

```sh
python -B gap-search/high/cofinal_rewrite.py --source 35 --gaps 1,5,4 --bound 1000
python -B gap-search/high/cofinal_rewrite.py --replay
```

The new results remove the high-grade guard coverage problem in this
specific interval program. The remaining task is to close B5, using its
actual suffix information or a target-changing merger that respects the
same well-founded source order.
