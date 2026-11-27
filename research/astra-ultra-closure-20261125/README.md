# Actual certificate descent and complete-lap gap arithmetic

**OPEN: this packet does not prove Collatz.** It proves new ordinary certificate transports, connects their rank-one base to the least smooth tower, and derives a whole-cycle integer-gap bound. The universal chain of transports and unrestricted ordinary cycle exclusion remain unproved. All claims below use the ordinary shortcut map

\[
 T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
 \qquad \operatorname{Good}(n)\iff \exists h,\ T^h(n)=1.
\]

An upper certificate is the actual finite trajectory from its specified input to 1. Its odd count includes the odd inputs to its steps and excludes the terminal endpoint. A proof that another value is good does not, by itself, bound that value's certificate cost.

## Transports may grow the source while removing actual odd inputs

For positive integers $d,t$, put

\[
 X=8\,2^d t-1,\qquad Y=8\,3^d t-1.
\]

Then $T^d(X)=Y$ and

\[
 T^{d+3}(3X)=T^3(3Y)=9\,3^d t-1.
\]

The first upper prefix has exactly $d$ more odd inputs than the second. The common endpoint exceeds 2, so every supplied hitting certificate from $3X$ passes through the displayed prefix: an earlier hit would trap the orbit in the cycle $1,2$. Copying its actual remaining suffix gives a certificate from $3Y$ with exactly $d$ fewer odd inputs. Badness of the lower source is preserved. Here $Y>X$, and the exact height charge is

\[
 2^d(Y+1)=3^d(X+1).
\]

Positive-anchor lifts give paired transports that shrink the source; their basic mechanism is prior work. The new packet records both arms and the change in the supplied certificate, and proves a composable height bound. [Ordinary clocks, counts, and transport](bridge/PairedReturn.lean) · [Proof and scope](bridge/README.md)

## The base of the certificate induction is a pure-power problem

All odd sources whose triples have a certificate with exactly one odd input are

\[
 Z_m=\frac{2^{6(m+1)}-1}{9},\quad m\ge0.
\]

Every $3Z_m$ has the advertised one-odd certificate. Literal lower paths and an immediate shared successor prove

\[
 \operatorname{Good}(Z_m)\iff \operatorname{Good}(3^{3m+2}+1)
 \iff \operatorname{Good}(3^{3m+1}).
\]

Consequently, if a `FirstTower w r` from the parent packet exists and some $Z_m$ is bad, then $w=1$ and $r\le3m+1$. This yields the exact floor

\[
                 9Z_m+1\ge 2^{2r+4}.
\]

The floor gives a possible joint descent budget. Define $\operatorname{Cost}(x,y,d)$ by $2^d(y+1)\le3^d(x+1)$. Costs compose by adding $d$. If a bad source $z$ is transported to a bad rank-one destination with cumulative cost $d$, then the inequality

\[
             9\,3^d(z+1)<2^d2^{2r+4}
\]

contradicts that floor. This statement is kernel checked. It allows intermediate height increases. It still requires a chain covering the actual source and a proof of its total charge. PR197's bounded return supplies a numerical height bound, but its tests can introduce a new existential good certificate with no corresponding odd-count bound. The two missing estimates cannot be inferred from that return theorem.

Two residue classes of $m$ also admit an actual rank-one descent to the previous exponent, checked uniformly by a lifted 14-clock equality. They do not cover all exponents. [Full rank-one classification, floor, budget, and residue descent](bridge/PairedReturn.lean)

## Changing the upper ternary exponent saves certificate cost

For $x=32t+17$ and $Y=24t+13$, the lower path has $T^2(x)=Y$, while

\[
                 T^5(3x)=T^3(9Y)=81t+44.
\]

The upper paths use respectively three and one odd inputs. Thus every supplied certificate from $3x$ transports to one from $9Y$ with two fewer odd inputs, preserving badness below. The output has upper multiplier 9. After three more clocks its lower and upper states are $Q=9t+5$ and $9Q-1$; the certificate is at $9Q-1$, with no resulting certificate at $9Q$. Generalized upper multipliers therefore need their own exhaustive treatment. [Exact certificate transfer](core/ExponentTransport.lean)

At the least-base slice $w=1$, the earlier arithmetic frontier guards do not eliminate the powers $3^r$ for $r\ge2$. A separate arithmetic lemma shows that repeating any positive number of standard $1,2$ laps after a common prefix about one positive integral anchor cannot merge two distinct pure powers: the necessary equations force $w>3^k$. It does not exclude mergers using different words or more general endpoints. [Precise mechanism and proof](core/README.md) · [Lean arithmetic](core/TowerLaps.lean)

## The complete cycle denominator controls ordered gaps

For a positive primitive accelerated cycle with odd period $p$, minimum $s$, reduced common denominator $d$, and the stated ordered dyadic recurrence, let $B$ count changes in the sorted octave corrections, including the doubled seam. For every $k\ge0$,

\[
                    3^k\max(p-kB,0)\le4ds.
\]

The kernel proof derives the adjacent-gap recurrence from the affine rank equations. A terminal gap following $k$ unchanged corrections is divisible by $3^k$; at most $kB$ terminals encounter a changed correction. The positive integer gaps sum to $4ds$. For the restricted ordinary cycle, the ordering follows from the quarter-integer grid. For rational cycles it must be assumed or separately proved.

The external mixed-log bound of Wu and Wang gives $s=O_\epsilon(p^{5.1163051+\epsilon})$. Hence bounded $B$ forces exponential growth of the actual reduced denominator $d=(2^h-3^p)/\gcd(2^h-3^p,C)$, and ordinary denominator one forces $B\gg p/\log p$. These are written consequences of the kernel theorem and the external estimate. [Proof, exact hypotheses and citations](cycle/README.md) · [RankGaps.lean](cycle/RankGaps.lean)

A separate written construction gives arbitrarily long positive rational cycles with both actual circle orders, positive high-phase occupation, synchronized past records, and linearly many sorted changes. Exact controls at odd periods 41 and 306 independently reconstruct the trajectories, orders, records and reduced denominators. The construction does not satisfy the ordinary denominator-one requirement or assert the stronger approximation rate used in PR200. The cycle bound therefore leaves a definite high-variation ordinary case open. [Construction](cycle/RATIONAL_ORDERS.md) · [Finite replay](cycle/check.py)

## Lean intake and the closing obligation

The packet also compiles PR207's eleven finite statements without changing their proof bodies, and repairs PR200's six-statement candidate while preserving all its original theorem headers. The original analytic and universal premises remain explicit. [Intake changes](intake/README.md) · [Frozen source pins](SOURCES.md)

The closing proposition in PR197 still asks every residue-17 source with a finite upper certificate of at least three odd inputs to converge, or to have a positive same-basin representative $n$ with $2^{40}n<z$. No result here proves that assertion for all such sources. The least-smooth-tower frontier is likewise open at pure powers and the other surviving sources. The checked transports, rank floor and whole-lap bound are substantive necessary or sufficient components; their coverage is not a completed induction.

[Independent reviews and clean replay](../../reports/astra-ultra-closure-20261125/VERIFICATION.md)
