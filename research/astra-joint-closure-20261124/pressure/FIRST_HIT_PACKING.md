# Bounded carry excludes a completed nontrivial lap

**Status: PROPOSED elementary theorem.** Use the positive shortcut map
\(T(2n)=n,\ T(2n+1)=3n+2\) and odd map \(U(x)=(3x+1)/2^{v_2(3x+1)}\).
In the paired rows of PR 200 let \(N_{e,p}(q)\) count distinct positive odd unit
sources \(x\) taking \((x,5x)\) to \((q,5q)\) in \(e\) shortcuts with the
same \(p\) odd inputs on each arm, and first-arm real offset
\(0\le\beta\le1/2\). Thus \(q=x/G+\beta\), where \(G=2^e/3^p\).
The arguments work on the actual integers, including hypothetical cycles.

**First-hit theorem.** For every odd unit \(q>1\), every such first-arm
path hits \(q\) for the first time at the terminal clock (for positive
clock it does not start at \(q\)). This holds even without the companion
arm. For every positive odd unit \(q\), including 1, the paired path has
its first simultaneous hit of \((q,5q)\) at the terminal clock.

**Proof.** A second hit of \(q\) would append a positive loop from \(q\)
to itself. Write \(q_0=q,q_1,\ldots,q_b=q\) for the odd vertices of
that loop. Its inverse affine multiplier is
\[
 D=2^{s}/3^b=\prod_{j=0}^{b-1}(1+1/(3q_j)).
\]
Here \(s\) is its physical clock; this identity follows by multiplying
the odd transitions and cancelling the vertex ratios. A one-odd-input
loop gives \((2^s-3)q=1\), so for \(q>1\) there are at least two terms.
The second odd input satisfies \(q_1\le(3q+1)/2\). Consequently
\[
 D\ge(1+1/(3q))(1+2/[3(3q+1)])=1+5/(9q).
\]
The loop alone contributes real offset \(q(1-1/D)\ge5q/(9q+5)>1/2\)
when \(q>5\). Appending it to a path of nonnegative offset only increases
the final offset above the cutoff. For \(q=5\) the path
\(5,8,4,2,1,2,1,\ldots\) rules out return. These cases exhaust \(q>1\).
When \(q=1\) a second simultaneous hit would return the second arm to
5, which the same trajectory excludes. This proves both statements.

**Octave packing.** Counts from distinct rows for one fixed \(q\) count
disjoint ordinary sources: a source determines its unique simultaneous
hit and its grade at that clock. For any \(H\ge1\), all sources in rows
with \(H\le G<2H\) lie in \([(q-1/2)H,2qH)\). Hence
\[
 \sum_{(e,p):\ H\le 2^e/3^p<2H} N_{e,p}(q)/G
 \le q+1/2+1/H .
\]
This involves every clock with inverse scale in the octave; it does not
require restricting to central rows or assuming a stationary law.

For instance, put \(H=2^h\), \(d=2-\log_2 3>0\). For every positive
integer \(p\) with \(|h-dp|\le\sqrt h-1\), set
\(e=\lceil h+p\log_2 3\rceil\). Then \(G\in[H,2H)\) and
\(|e-2p|\le\sqrt h\). There are \(\gg\sqrt h\) distinct rows of this
form as \(h\) tends to infinity. Their average normalized pressure is
\(O_q(1/\sqrt h)\); for any \(t>0\), at most
\((q+1/2+1/H)/t\) rows in the entire octave can have pressure at least
\(t\). This excludes a pointwise central lower bound
\(\omega(1/\sqrt h)\) imposed on every such row at the same target.

**Scope.** This packing estimate allows a bounded number of rows per
octave with constant pressure, or a central bank with pressure of order
\(1/\sqrt h\) per row. It gives no cofinal pointwise lower bound and no
upper bound of exponentially small order. PT in PR 200 only requests a
subexponential loss on a sequence, so the argument neither proves nor
refutes PT. The overlap issue addressed here differs from the large-carry
test in PR 201. The count uses distinct sources at a bounded real offset;
the large-carry test can count complete laps on purpose.

**Source interface.** [PR 200, fixed paired count and PT](https://github.com/GettysburgResearch/collatz/blob/9fc000d840f365340539e426c9beb05a34edbd82/research/regularity-rigidity-20261124/pointwise-fibers/PAIRED_FIBERS.md).
PR 203 uses nonperiodicity to sum depths for a one-arm inverse floor with
a different offset cutoff. The first-hit proof above uses the specific
absolute cutoff one half.
