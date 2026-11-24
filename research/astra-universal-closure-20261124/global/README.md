# A least bad power of three over the smallest base

**PROPOSED. The Collatz conjecture remains open.** All fourteen public theorems in [SmoothCore.lean](SmoothCore.lean) were checked using Lean 4.34.1, warnings as errors, and automatic implicit arguments disabled. Its theorem `universal_iff_frontier_merger` gives a formal closing target. The target `FrontierMerger` remains unproved.

Let \(T(2k)=k\) and \(T(2k+1)=3k+2\). Call a positive integer good when one of its ordinary forward iterates is 1. The proof imports the actual basin and elementary smaller-source theorem from [PR 192 at 26f070c](https://github.com/GettysburgResearch/collatz/tree/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124).

## A rank that survives a large intermediate value

If a bad positive integer exists, choose the least positive \(w\) with any bad power \(3^rw\). Then choose the least such \(r\) at this base. Every earlier power at \(w\) is good. Every \(2^i3^j b\) with \(0<b<w\) is good for every pair of nonnegative exponents. Dividing out a factor of two or three in \(w\) would give a smaller bad base, so \(w\) is odd and prime to three. The PR 192 smaller-source theorem gives \(w\) itself good because every smaller odd source and its triple are good. Consequently \(r>0\). The case \(w=1\) is included.

Write the first maximal odd run as

\[
 n=3^r w=2^M a-1,\qquad M\ge1,\quad a\text{ odd},\qquad
 T^M(n)=A-1,\quad A=3^M a.
\]

The preceding power \(3^{r-1}w\) is good, and its next odd state is \(a\), since \(3(3^{r-1}w)+1=2^M a\). Thus \(a\) is good for every size of the run. If \(2^M>3^r\), we have the stronger conclusion \(a<w\), which makes all the powers of three above \(a\) good. Indeed, \(a\ge w\) would imply \(w=a=1\) and \(3^r+1=2^M\). Powers of three are 1 or 3 modulo 8, so \(M\le2\). Both possible positive starts 1 and 3 reach 1.

Under this strict clock inequality, four ordinary comparisons rule out six of the eight odd residue classes modulo 16. Here the two starts in each row have identical iterates at the displayed time. Their sizes can exceed \(3^r w\).

| Condition on \(A\) | First start | Second, good start | Clock | Common endpoint |
|---|---|---|---:|---|
| \(A=8k+5\) | \(8k+4\) | \(A\) | 3 | \(3k+2\) |
| \(A=8k+7\) | \(8k+6\) | \(3A\) | 3 | \(9k+8\) |
| \(A=16k+3\) | \(16k+2\) | \(A\) | 4 | \(9k+2\) |
| \(A=48k+9\) | \(48k+8\) | \(A/3\) | 4 | \(9k+2\) |

In the last row \(A\equiv9\pmod{16}\) and \(3\mid A\) force the displayed representation. The bad state \(A-1\) would reach a good endpoint in each of the four cases. The surviving possibilities above the strict clock threshold are therefore \(A\equiv1,11\pmod{16}\).

For a concrete high excursion, take \(n=111=3\cdot37\), so \(n+1=2^4\cdot7\). Four odd shortcuts reach \(566>2n\). The two paths are \(566\to283\to425\to638\) and \(1701\to2552\to1276\to638\). The comparison \(1701=7\cdot3^5\) has base \(7<37\). More generally, take \(M=6t+4\) and \(n=7\cdot2^M-1\). Then \(n\equiv3\pmod9\), so \(w=n/3\) is odd and prime to three, and \(A=7\cdot3^M\equiv7\pmod8\). The row compares \(n\) with \(7\cdot3^{M+1}\). The ratio of these two inputs grows without bound with \(t\). This family illustrates the physical merger. It does not assume any of its members are counterexamples.

A separate comparison applies at any clock size when \(r\ge2\). If \(n\equiv85\pmod{512}\), write \(n/9=237+512k\). The two starts \(n/9\) and \(n=2133+4608k\) both reach \(38+81k\) after nine shortcuts. This contradicts the goodness of the earlier power \(n/9\). The argument allows arbitrarily large \(r\).

## The remaining merger

For every positive odd \(w\) prime to three and every positive \(r\), form \(n,M,a,A\) as above. Retain the inputs satisfying

\[
 2^M\le3^r\quad\text{or}\quad A\equiv1,11\pmod{16},
 \qquad r\ge2\implies n\not\equiv85\pmod{512}.
\]

The proposition `FrontierMerger` asks that each retained \(n\) have an ordinary forward iterate equal to a forward iterate of some \(3^j b\), with \(0<b<w\) or with \(b=w\) and \(j<r\). It imposes no bound on either clock and makes no assumption about the basin of any start.

If all positive starts reach 1, take \(b=w,j=0\) and match at 1. Conversely, a counterexample would give the least pair above, whose input survives the proved comparisons. Any merger promised there would reach the same future as a known good power. This proves the two implications in Lean. The missing step is to produce such a merger for every surviving input. When \(2^M\le3^r\), goodness of \(a\) alone does not establish goodness of all its higher powers. When \(2^M>3^r\), the two surviving residue classes still require an ordinary meeting.

## Replay

Use the three source files from the same checkout, in this order, with the matching Mathlib environment on `LEAN_PATH`. Set `OUT` to an existing empty scratch directory.

```sh
export LEAN_PATH="$OUT:$LEAN_PATH"
lean -DwarningAsError=true -DautoImplicit=false -o "$OUT/SourceDeletion.olean" research/astra-minimum-source-20261124/arithmetic/SourceDeletion.lean
lean -DwarningAsError=true -DautoImplicit=false -o "$OUT/MinimumFailure.olean" research/astra-minimum-source-20261124/minimal/MinimumFailure.lean
lean -DwarningAsError=true -DautoImplicit=false -o "$OUT/SmoothCore.olean" research/astra-universal-closure-20261124/global/SmoothCore.lean
```

All fourteen public theorem audits in the last file use only a subset of `propext`, `Classical.choice` and `Quot.sound`.
