# A single ternary point obstructs finite fixed-word covers of the last Mersenne row

**Written theorem with exact finite replay; not Lean-certified.** This is a negative result on a specified method, independently reconstructed by the coordinating and cycle agents after the main science checkpoint. Let \(j=11+162m,\ m\ge0,\ N=2^j,\ z=(128N-271)/81\). Work on the large-\(j\) tail. The two bad Mersenne forms under consideration are \(N-1\) and \(2N-1\). A route takes finitely many ordinary forward or legal inverse shortcut edges, in a word independent of \(j\) on its ternary cylinder. Both starting forms are supplied; obtaining the second from the first uses an already established source-dependent Mersenne merger. Other source-dependent peak operations are outside the word grammar.

The integer \(590\) belongs to the ternary closure of \(N\). Indeed \(590=2^{11}\bmod3^5\), and \(v_3(2^{162}-1)=5\) by the elementary lifting of \(4-1\) through powers of three. Therefore the powers of \(2^{162}\) generate every quotient of \(1+3^5\mathbb Z_3\). Take the putative ternary coordinate \(N_*=590\) and the dyadic coordinate \(N=0\) (the actual real values still tend to infinity). A finite legal affine word on a ternary cylinder remains ternary-integral at every point of that cylinder. Its dyadic decisions eventually agree with its signed center.

**Result.** Among all such words from either supplied Mersenne form which are legal at \(590\), the possible endpoint forms \(\alpha N-b\) with \(\alpha\le128/81\) are exactly the following. The last column gives the number of true shortcut steps from the form to \(N-1\) and the number of odd departures. Each applies at sufficiently large \(j\) in an appropriate ternary cylinder containing \(590\).

| \(\alpha\) | \(b\) | \(x=590\alpha-b\) | \(-b\bmod16\) | ordinary path |
|---|---|---:|---:|---|
| \(8/9\) | \(13/9\) | 523 | 11 | 3,2 |
| \(1\) | \(1\) | 589 | 15 | 0,0 |
| \(256/243\) | \(623/243\) | 619 | 11 | 8,5 |
| \(32/27\) | \(61/27\) | 697 | 9 | 5,3 |
| \(4/3\) | \(5/3\) | 785 | 9 | 2,1 |
| \(1024/729\) | \(2735/729\) | 825 | 9 | 10,6 |
| \(3/2\) | \(1\) | 884 | 15 | one forward edge *from* \(N-1\) |
| \(128/81\) | \(271/81\) | 929 | 1 | 7,4 |

**All-word reduction.** Fix the starting form \(2^U N-1,\ U\in\{0,1\}\). An inverse step followed by a forward step cancels by determinism. The reduced route therefore goes forward \(h\) steps from the Mersenne source and then backwards. Its signed center stays at \(-1\) throughout its forward part. If the backward part has \(o\) odd letters and \(E\) even letters, put \(d=o-h\). The relative coefficient and center satisfy
\[
     \alpha=2^{E+U}(2/3)^d,\qquad b\ge1 .
\]
Both reflected inverse maps \(y\mapsto2y,\ y\mapsto(2y+1)/3\) preserve \(y\ge1\). Going forward from \(b\) by the reflected signed map \(S\) takes it to 1, with exactly \(E\) even departures. Here \(S(y)=y/2\) on even numerators and \((3y-1)/2\) on odd numerators; all denominators are odd powers of 3.

For \(d\le0,\ \alpha\le128/81\) forces \(E=U=0,\ d=0\) or \(-1\). Then \(b=1\), giving two displayed rows. For \(d>0\), the ternary integrality of \(x=590\alpha-b\), together with \(3\nmid590\), forces the denominator of \(b\) in lowest terms to be exactly \(3^d\). Then \(x\) is an ordinary integer, with no finite denominator remaining. Follow the signed center \(-b\) until exactly \(d\) odd forward steps have occurred. At that time \(t\) the denominator has cleared: at any odd step it loses one factor 3 and at an even step it stays constant. There are \(t-d\le E\) even steps so far. The true integer \(x\) undergoes the same first \(t\) steps, since its difference from the center has dyadic valuation at least \(E+U+d\ge t\). The resulting true ordinary integer is
\[
               T^t x=590\,2^{E'+U}-y,\qquad E'=E-(t-d),
\]
with \(y\) a positive integer which reaches 1 with exactly \(E'\) even departures under \(S\). Thus \(1\le y\le2^{E'}\): each odd departure is nondecreasing in the positive range and each even departure halves. It follows that \(T^t x\ge589\). Nonpositive integers stay nonpositive under true shortcuts, so \(1\le x\le\lfloor590(128/81)\rfloor=932\).

**Finite reduction and exact check.** For each \(x=1,\dots,932\), follow its entire ordinary orbit through its first visit to 1. The largest such time is 113 shortcuts and the largest height is 125252. The only later vertices are 1 and 2 and both are below 589. At each recorded time \(t\), let \(p\) be the number of odd departures through that time. For \(U=0,1\), test all \(E'\ge0\) with
\[
      (590\,2^U-1)2^{E'}\le T^t x <590\,2^{E'+U}.
\]
This is finite and the peak implies \(E'\le7\). Set \(y=590\,2^{E'+U}-T^t x\). Check that the ordinary reflected orbit of \(y\) reaches 1 with exactly \(E'\) even steps. Stop with failure as soon as the remaining budget is negative or the current \(y>2^{\rm remaining}\). Positivity and the strict increase of every odd step at \(y>1\) make this a finite procedure. Recover \(\alpha=2^{t+E'+U}/3^p,\ b=590\alpha-x\); discard candidates with \(\alpha>128/81,\ b<1\), or \(b>2^{t-p+E'}\). The last discard is valid since the signed source \(b\) reaches 1 with \(t-p+E'\) even steps. This enumerates a superset of every possible word with \(d>0\), allowing even times other than the exact denominator-clearing time. The seven survivors before the extra \(3/2\) row are precisely the table, including the identity row. Each affirmative row is verified directly by the short signed path shown in the final column and its slope. Each row's integrality holds on a ternary cylinder of \(590\), and binary parity lifting gives genuine positive paths for large \(j\) in that cylinder. The independently executable [checker](check_finite_cover.py) exhausts that complete finite reduction. [Replay receipt](../../../reports/astra-unconventional-20261126/finite-cover-replay.json)

**Consequence and boundary.** In the bounded branch the strongest of the surviving \(r=3,4,5\) lower thresholds for \(s/N\) has limiting slope \(2/3\). The corresponding bad-multiple-of-three threshold is \(3q=2s+1\), with limiting slope \(4/3\); this uses the least-tripling global floor, not three times the ordinary floor. Every listed slope exceeds \(2/3\); the sole ternary-divisible listed form has slope \(1024/729>4/3\). The only canonical source (\(1\bmod16\) and \(2\bmod3\)) is the original \(z\), not a smaller one. Hence no finite cover of all ordinary \(m\) by ternary cylinders carrying these fixed words can force descent by one of the three advertised tests (ordinary lower floor, triple floor, smaller canonical query). Otherwise some cylinder from that finite union would contain the limiting parameter, and using arbitrarily large ordinary members there gives the contradicted slope or residue. This argument leaves open an unbounded ternary selector which terminates on each ordinary \(m\) but does not terminate at the nonordinary limiting parameter. It also leaves source-dependent ascent lengths, additional logical comparisons, and the actual convergence of each Mersenne source open.
