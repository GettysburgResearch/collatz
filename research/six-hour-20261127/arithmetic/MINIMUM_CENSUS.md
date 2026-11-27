# Direct minimum census below \(2^{71}\)

**PROPOSED finite theorem.** No primitive nontrivial ordinary positive odd cycle with all valuations in \(\{1,2\}\) and maximum at most \((16s+7)/3\), where \(s\) is its minimum, has \(s<2^{71}\). The numerical height range is covered by Barina's general trajectory verification. This separate, restricted computation uses the possible minimum itself and the surrounding native odd edges; it requires no general convergence verification. Together with the [located CRT period exclusion](CRT_PERIOD_EXCLUSION.md) it proves that **every nontrivial ordinary cycle satisfying the stated bounded-branch hypotheses has more than \(10^{1000}\) odd phases**, with no external numerical trajectory input.

The ordinary odd recurrence is \(2^e x'=3x+1\). At a minimum \(s\) every predecessor and successor on a cycle stays between \(s\) and \(U=\lfloor(16s+7)/3\rfloor\). For \(s\ge2^{20}\) and \(j\le30\), the product of the affine correction factors on \(j\) edges lies between one and \(G=3\cdot2^{20}/(3\cdot2^{20}-30)<1001/1000\). This follows from \((1+t)^j\le(1-jt)^{-1}\) for \(0\le jt<1\). Even \(((16+7/2^{20})/3)G<5335/1000\).

Starting at the center, a reversed prefix of \(j\) edges with total exponent \(E\) must have
\[
        1\le 2^E/3^j\le 5335/1000 .
\]
Indeed the homogeneous reverse height is the actual predecessor divided by \(s\), multiplied by the positive correction product. A forward prefix instead needs
\[
        1000/1001\le 3^j/2^E\le 5335/1000 .
\]
These tests are necessary for a whole cycle and allow some extra finite paths.

Enumerate all passing 30-edge words in either direction. The backwards word fixes the center residue \(a\bmod P\), \(P=3^{30}\), by the backward sum from the CRT paper. A future with final grade \(A\) fixes \(b\bmod Q,\ Q=2^{A+1}\), by the exact affine carry and terminal oddness. There are \(2\,510\,811\) past words. The \(2\,714\,175\) futures with \(A=46\) and \(1\,339\,481\) with \(A=47\) exhaust the forward list.

For a fixed \(Q\) sort all \(a Q^{-1}\bmod P\) into an increasing list. Write \(s=b+Qt\) and \(c=bQ^{-1}\bmod P\). Since \(PQ>2^{71}-1\), \(0\le t<P\). At physical upper limit \(H=2^{71}-1\), discard \(b>H\), and set \(T=\lfloor(H-b)/Q\rfloor\). The admissible entries in the sorted list lie exactly in the two closed intervals
\[
 [c,\min(P-1,c+T)]\,,\qquad [0,c+T-P].
\]
Omit an empty second interval. For an entry \(w\), the corresponding \(t\) is \(w-c\) in the first and \(w+P-c\) in the second. Keep the actual integer \(b+Qt\) if it is at least \(2^{20}\). Binary search in the sorted list visits every hit without expanding the Cartesian product. Backward words are distinguishable because the legal incoming exponent in \(\{1,2\}\) at a ternary unit is unique (and a multiple of three has none). Forward words are distinguishable by the ordinary parity path. Even duplicate tests would preserve the exclusion.

| Centers tested | Candidates reaching the physical trace | Latest edge of departure |
|---|---:|---:|
| All odd \(3\le s<2^{20}\) | 524,287 | 24 |
| \(2^{20}\le s<2^{71}\), future grade 46 | 555,231 | 53 |
| \(2^{20}\le s<2^{71}\), future grade 47 | 136,825 | 52 |

For each candidate the trace starts from that actual integer. It stops on an exponent above two or on a successor outside \([s,U]\). A genuine cycle at its minimum could never give either failure. The 692,056 candidates in the two CRT rows all fail within 53 odd edges. An independent direct scanner checks each odd source through 32,767 at short past and future depths against the entire corresponding CRT enumeration. The single excluded initial height \(s=1\) is the ordinary fixed odd cycle with successor \(1\). [Python enumeration and physical traces](check_minimum_census.py) · [Exact output](MINIMUM_CONTROLS.json)

Lean checks the two-run integer arithmetic and the implication from an actual trapped native orbit to survival of every finite exit test. The exhaustive enumeration is computational evidence from the listed exact Python replay. It proves neither a general lower-excursion theorem nor absence of restricted cycles with period above \(10^{1000}\). [Lean kernel](MinimumCensus.lean)
