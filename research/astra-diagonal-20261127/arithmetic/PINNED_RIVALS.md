# True smaller and ternary-multiple rivals on a bounded least-bad cycle

**PROPOSED pointwise restrictions.** Assume the bounded alternative of
the least-tripling-disagreement argument. Its minimum odd phase \(s\)
is the least bad positive integer, the least bad positive multiple of
three equals \(2s+1\), and every phase \(x\) has \(s\le x\le(16s+7)/3\).
Its accelerated exponents are one or two and its neighbors \(x\pm1\)
are good. All the exclusions below are for this bounded alternative.
[Prior floor and neighbor theorem](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md)

The ordinary shortcut is \(T(2n)=n,\ T(2n+1)=3n+2\). A word below
lists positive *odd* exponents in forward chronological order. Each
listed binary cylinder is realized by arbitrarily large ordinary
integers. Its homogeneous real spread, the largest divided by the
smallest of the prefix multipliers \(3^j/2^{E_j}\), is
\(65536/19683=3.32957\ldots\) in each of the three rows. Thus the
words satisfy the necessary real spread bound on a finite segment.

| Native word | Actual arithmetic conclusion | Forbidden placement |
|---|---|---|
| \(121212121222212122\) | \(T^{30}(x)=T^{30}(x+1)\) | Every phase |
| \(12211212222121221\) | \(T^{27}(x)=T^{27}(x+4)\) | Any phase with incoming exponent one and \(x+4<2s+1\) |
| \(21212121212222121221\) | \(T^{32}(x)=T^{29}((x-1)/8)\) | Every phase |

For the first row \(x=2^{30}t+613089275\). The common terminal
is \(3^{19}t+663632570\). The upper neighbor of the source is good.
For the second \(x=2^{28}t+260560107\); the rival odd exponents
are \(11121111111221433\). The common terminal is
\(2\cdot3^{17}t+250702913\). An incoming exponent one forces
\(x\equiv2\bmod3\), so \(x+4\) is itself a bad multiple of three.
The exact exclusion applies to \(x\le2s-5\) among odd phases; more
generally just use its displayed strict inequality. For the third
\(x=2^{33}t+7975731193\) and \((x-1)/8=2^{30}t+996966399\);
the rival word is \(11111111111111221433\). The common terminal is
\(2\cdot3^{20}t+6474939905\). The competing positive source is
strictly below \(s\) since the given upper bound implies \(x<8s+1\)
for \(s\ge2\).

In each row the native class follows by starting with an odd terminal
modulo 2 and inverting the native letters from the end. An inverse odd
edge multiplies the known terminal by \(2^a\), subtracts one, and
divides by the unit three modulo the enlarged dyadic modulus.
The three actual shortcut identities on these full infinite classes
are machine-checked. The generic replay proof keeps the slope and
constant of the entire arithmetic progression at each step, verifies
the common parity, and proves the result for every \(t\ge0\).
[Lean proof, including all three ordinary mergers](PinnedRivals.lean)

## Arithmetic of an extinct competitor

At a common endpoint, compare an arbitrarily shifted odd inverse path
\(y\) with its actual native path \(x\). In a pair of current states
write \(Qy=Px+c\) with \(Q,P\) powers of two. At first \(P=Q,c=0\).
Let the native reverse edge be \(2^a x=3u+1\). Choose a rival
exponent \(b\ge1\) and put
\[
   P'=2^{b-a}P,\qquad 3c'=2^b c+P'-Q .
\]
One may enlarge the fixed initial power \(Q\) to make \(P'\)
integral throughout any proposed finite comparison. The exact equation
\[
      Q(2^b y-1)=3(P'u+c')
\]
makes an integer \(c'\) sufficient for a true positive odd predecessor
\(v=(2^b y-1)/3\), and then \(Qv=P'u+c'\). Conversely any such
edge has the indicated carry when its scale is integral. This is the
standard affine discrepancy comparison in cleared coordinates.

If \(3\mid P+2^a c\), then \(3\mid y\), and conversely. Indeed
\(2^aQy=3Pu+P+2^ac\), with \(2^aQ\) a unit modulo three. At this
cut *no* odd predecessor of \(y\) exists. But \(y\) is already an
actual member of the bad basin. The second ordinary floor therefore
enforces
\[
                Px+c=Qy\ \ge Q(2s+1).
\]
All competitors, including ternary units, also satisfy \(Px+c\ge Qs\).
Thus a ternary-dead rival contributes a further physical inequality
on the same native phase and letter. Simply dropping this branch
loses information. The second table row exhibits this stronger test
at relative dyadic grade zero. Existing division-minimum work provides
the affine engine and extensive rigidity results for balanced words.
[Weaver, paper 1](https://rstation.ai/problems/collatz/papers/1/v3)
· [Critical-slope binary rigidity, paper 139](https://rstation.ai/problems/collatz/papers/139/v2)
· [Mahler, unrestricted inverse minima, paper 148](https://rstation.ai/problems/collatz/papers/148/v1)

## What all-depth positivity alone allows

The genuine reduced denominator-five cycle with numerator phases
\(23,37,29\) has the additional following property. Color a positive
numerator bad when it reaches this cycle under the ordinary
numerator dynamics with odd affine correction \(+5\).
Its least positive bad numerator is 23 and its least positive bad
multiple of three is \(51=2\cdot23+5\), without an inverse depth
or height cutoff. Here is a finite *forward* proof of both all-depth
claims. Even factors can be stripped. Every positive odd numerator
below 23 eventually lands in \(\{1\},\{5\}\) or
\(\{19,31,49\}\), all cycles disjoint from 23. For odd multiples of
three below 51 the source list is \(3,9,15,21,27,33,39,45\).
In addition to the preceding list, \(27\to43\to67\to103\to157
\to119\to181\to137\to13\), \(33\to13\), \(39\to61\to47\to73
\to7\), and \(45\to35\to55\to85\to65\to25\to5\), with repetitions
of even divisions suppressed. The short forward verifier linked below
checks these assertions using the actual odd-numerator map. The
numerator 51 reaches the target cycle, so the lower bound is sharp.
Every odd inverse realization from the cycle has therefore stayed
above its numerator minimum at *every* step. Every ternary-compatible reverse word is positive here as well: from an already positive member with numerator at least 23 the next integral numerator is at least \((2\cdot23-5)/3>0\), so induction never crosses zero. In particular the
normalized 3-adic root \(23/5\) permits no compatible odd inverse
word with \(2^B\le3^k\): that word would give a positive numerator
strictly below 23 by the positive affine intercept. This example
has real minimum \(23/5\), and its other colors can contain different
cycles. It verifies the basin-indicator and two-floor obstruction;
it does not furnish a single reference basin for every good mark
or the very large physical minimum required of an ordinary candidate.

For any positive rational cycle, an alternative odd inverse branch
that departs its cycle can take only finitely many steps in a fixed
bounded physical interval. Otherwise two predecessor vertices recur
on the fixed denominator lattice. A periodic trajectory containing
that repeated vertex cannot join the original cycle at a nonperiodic
off-cycle predecessor. Quantitatively a branch all of whose off-cycle
vertices lie in \((0,M]\) has at most \(\lceil dM/2\rceil\) distinct
odd numerator vertices for common odd denominator \(d\). This is one
place where an actual numerator count distinguishes \(d=1\).
The currently obtained local rival restrictions do not force a
contradiction at all orientations of a bounded ordinary cycle.

[Independent integer replay](check_pinned_rivals.py)
· [Checked cycle and residue data](../../../reports/astra-diagonal-20261127/arithmetic/pinned-rivals.json)
