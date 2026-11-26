# Exactly two uniform affine queries on the last Mersenne row

**Written theorem with exact finite replay.** Set \(N=2^j\), \(j=97+162m\), and \(81z=1024N-527\). A hypothetical least reverse defect in this family makes both \(M_j=N-1\) and \(M_{j+1}=2N-1\) nonbasin. Allow fixed finite words of ordinary shortcut edges, legal inverse edges, and forward comparisons \(w\to 3w\) at \(w\equiv17\pmod{48}\), \(w<z\). Require legality on all sufficiently large members of this exponent progression. The length and branches of a word are fixed across that progression. There is no upper bound on the lengths of the words under consideration.

Exactly two affine query sources are reachable from the two supplied Mersenne starts. One is reachable from each start. The components reached after those comparisons admit no further uniform query, at any word length. None of these four components contains an earlier fixed-offset Mersenne start, a positive-cycle shadow, or a uniformly integral affine endpoint \(n\) with \(2^{40}n<z\) throughout the progression. A separate ordinary odd-count lower bound below applies even to source-dependent paths along the \(-17\) cycle. Ternary subdivision and post-ascent clocks remain available for the general problem.

## State invariant

Along a fixed ordinary word the positive source has the form \(\alpha N+c\), where \(\alpha=2^u3^v>0\) for integers \(u,v\). Its signed center \(c\) has odd denominator a power of three. Indeed arbitrarily large exponents have enough binary precision to fix the parity of each center. A legal forward division by two preserves odd denominator, and an inverse odd step introduces at most one factor of three. All ordinary endpoints of a fixed legal affine path are positive at large \(j\). Each projects to the prescribed signed edge on centers. Two centers connected by an undirected finite ordinary path have intersecting forward signed orbits, by determinism.

Choose a phase \(c_*\) of a negative signed cycle with period \(h_0\) and \(q_0\) odd inputs. If \(c\) reaches \(c_*\) in \(h\) steps with \(o\) odd inputs, the actual affine point at that phase has exponents \(u-h,v+o\). The ternary exponent is nonnegative by ordinary integrality. Write \(v+o=q_0 k+V\), \(0\le V<q_0\). Define the state
\[
                 (c_*,U,V),\qquad U=u-h+h_0k .
\]
Following additional full turns leaves the state unchanged. It is invariant under every ordinary edge in the component. Conversely, given agreement of the normalized states, follow both centers to the designated phase and make up the difference in turns. The resulting affine forms agree and the ordinary paths meet for every sufficiently large input. This uses a finite parity statement about the original positive input.

## A length-independent bound

Reflect negative integers to the positive map \(S(y)=y/2\) on evens, \((3y-1)/2\) on odds. For \(c_*=-1,-5,-17\) respectively, take
\[
 (h_0,q_0,A)=(1,1,1),\quad(3,2,5),\quad(11,7,18).
\]
Every integer path \(S^h(y)=-c_*\) with \(o\) odd inputs satisfies
\[
                      y\le A\,2^{h-h_0o/q_0}.                           \tag{1}
\]
At 1 each odd step has \(S(y)\ge y\). For the first hit of 5, no input is below 5, since \(\{1,2,3,4\}\) is invariant. Above 5, \((3-1/y)^2\ge8\) on odds. Multiply this and the even-step identities. Later visits append complete turns with \(h_0=3,q_0=2\).

At 17, \((3-1/y)^7\ge2^{11}\) for \(y\ge36\). The integers from 1 to 35 that reach 17 are \(17,21,23,25,31,33,34\). At their first arrival the values \(7h-11o\) respectively are \(0,2,3,4,6,7,7\), and each \(y^7\le18^7\,2^{7h-11o}\). The other positive integers up to 35 enter the cycles through 1 or 5. Stop at the first small integer and multiply the inequalities above it. Subsequent turns have eleven steps and seven odd inputs. [SignedSeventeenPotential.lean](SignedSeventeenPotential.lean) proves the seventh-power version of (1) for all heights and clocks. Its finite closed-set check also certifies these small exclusions.

Write a nonintegral center as \(c=-m/3^d\) in lowest terms. Ordinary integrality forces \(v=-d\). During the first \(d\) odd inputs its denominator loses one factor of three per odd input. Let \(J\) be the clock just after the last factor disappears. Each reflected value on this path is at least one, since the inverse branches from values at least one preserve that interval. On reversing the first \(J\) steps every even inverse doubles the magnitude and the odd inverse \(y\mapsto(2y+1)/3\) cannot increase it. Consequently \(|c|\le 2^{J-d}S^J(|c|)\), using the reflected rational branches only on this prefix. Apply (1) to the remaining integer path and substitute the state invariant. This gives
\[
 |c|\le {A\alpha\over 2^{U+h_0V/q_0}}\left({3\over2}\right)^d,\qquad
 m\le {A\alpha\over 2^{U+h_0V/q_0}}\left({9\over2}\right)^d.            \tag{2}
\]
For an integer center, \(v\ge0\) and the first bound holds at \(d=0\). The additional factor in its derivation is \((2^{h_0/q_0}/3)^v\le1\) for all three cycles. Bound (2) is independent of the lengths of all forward and inverse words.

## Exhausting the uniform queries

For a nonintegral center the query is \(w=(2^{j+u}-m)/3^d\). Its residue \(17\bmod48\) at consecutive exponents \(j,j+162\) forces \(3^{d+1}\mid 2^{162}-1\), since \(2^{j+u}\) is a ternary unit at large \(j\). Precisely \(3^5\) divides \(2^{162}-1\), so \(d\le4\) for every uniform query. Ordinary integrality alone gives \(d\le5\). The strict height condition gives \(\alpha\le 1024/81\); equality additionally requires \(c<-527/81\).

For each state and \(1\le d\le4\), (2) bounds \(m\). Retain \(m\) coprime to 3 and \(-m\equiv17\cdot3^d\bmod16\). Follow each surviving signed rational to its first cycle phase. For the prescribed state its normalization uniquely fixes \(u\), after which a single mod-48 test is exact on all sufficiently large exponents. For integer centers, check \(y=-c\equiv15\bmod16\) under (2). The [finite replay](check_uniform_mersenne_quotient.py) checks every candidate and raises an error on an unclassified trajectory.

| Initial normalized state | Only query | Upper normalized state |
|---|---|---|
| \((-1,0,0)\), the \(M_j\) state | \((256N-341)/27\) | \((-17,-1,3)\), represented by \(27N/2-17\) |
| \((-1,1,0)\), the \(M_{j+1}\) state | \((32N-13)/3\) | \((-5,2,1)\), represented by \(12N-5\) |
| \((-17,-1,3)\) | none | |
| \((-5,2,1)\) | none | |

The known source-dependent even-index merger between the two initial starts is accounted for by supplying both. An earlier Mersenne start \(M_{j-r}\) for fixed \(r>0\) has state \((-1,-r,0)\). Positive-cycle centers are disjoint from these negative components. Finally \(|c|\ge1\), \(d\le5\), and (2) bound the slope \(\alpha\) of every uniformly integral endpoint in the four components. Here \(2^{U+\lfloor h_0V/q_0\rfloor}/A\ge4/9\), so \(\alpha\ge(4/9)(2/3)^5>1/32\). This excludes \(2^{40}n<z\) at all sufficiently large exponents. These conclusions apply to the fixed-word grammar and height stated above.

## The separate rank-three family with even gap six

For \(j=11+162m,\ N=2^j,\ 81z=128N-271\), the original lower source reaches \(M_j\) after seven ordinary steps. The same replay uses cap \(128/81\) and excludes equality unless \(c<-271/81\). It finds **zero** uniform query sources in either of the states for \(M_j\) and \(M_{j+1}\). This includes all fixed legal ordinary inverse and forward words, and uses the smaller parent height specific to this family. An endpoint that is uniformly integral without the query residue still has \(d\le5\), so (2) at these two states gives \(\alpha\ge(2/3)^5\). Thus no fixed affine ordinary path from either start achieves the required contraction at all sufficiently large exponents. This extends the separate ordinary upper-clock barrier by accounting for inverse edges at every fixed word length.

## Ordinary ancestors at source-dependent cycle checkpoints

Let \(Q=27N/2,\ P=Q-17\), and let \(11k\le j-1\). Suppose a positive integer \(w\) reaches \(T^{11k}(P)\) in \(L\) ordinary steps with \(o\) odd inputs. Then
\[
                       w<P \quad\Longrightarrow\quad o\ge7k+4.           \tag{3}
\]
The competing clock \(L\) is unrestricted. The checkpoint equals \(3^{3+7k}2^{j-1-11k}-17\). If \(o\le3+7k\), run the same inverse word from this checkpoint and from \(-17\). All signed inverses are integral: before each odd inverse the difference is divisible by three, and an integral odd inverse gives an odd input. Even inverses double the difference. The signed starting value is \(-y\), where \(S^L(y)=17\), and
\[
 w+y=Q\,{2^L\over3^o}\left({2187\over2048}\right)^k
 \ \ge\ Q\,{y\over18}\left({2187\over2048}\right)^{-3/7}
 \ \ge\ Q\,{4y\over75}.
\]
The first bound uses (1) and \(o\le7k+3\); the second follows by seventh powers. If \(y\ne17\), then \(y\ge21\) by the small signed orbits. Since \(Q\ge75\) on the progression, \(w-P\ge Q(4y/75-1)-y+17\ge3y-58>0\). If \(y=17\), the path makes an integral number \(\ell\) of turns of the eleven-step cycle, so \(o=7\ell,\ L=11\ell,\ \ell\le k\). Thus \(w+y=Q(2187/2048)^{k-\ell}\ge Q\). Both conclusions contradict \(w<P\). A meeting during a partial turn can be continued to a complete checkpoint whenever that checkpoint is within the binary budget, appending the same tail on both paths.

## Remaining positive obligation

On a finer progression \(j=j_0+162\cdot3^r t\), the same argument gives \(d\le4+r\) for every uniform query, since \(v_3(2^{162\cdot3^r}-1)=5+r\) by factorization into successive cubes. Formula (2) again bounds its signed candidates independently of the word length. To obtain descent for every original integer still requires an admissible branch for its actual ternary digits, with a proved finite stopping clock and the strict height at that source. The quotient at \(r=0\) excludes one uniform fixed word as a solution. Coverage and termination for unrestricted \(r\) remain open.
