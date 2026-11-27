# Actual hit costs at the original floor and fixed-endpoint word finiteness

**PROPOSED, written.** These statements concern actual positive integers. The bounded-cycle conclusions use the existing bounded alternative and its good-neighbor theorem. They give necessary conditions at inputs strictly below the original least bad point. The fixed-terminal lemma below applies to every positive terminal, in either alternative. Universal closure remains open.

## Two exact sums of smaller-source certificate costs

Let \(s\) be the global least positive bad integer in the bounded alternative. Let \(x\) traverse the odd phases of its bad cycle, with \(2^a x'=3x+1\), \(a\in\{1,2\}\), and \(x<8q\), where \(3q=2s+1\). Write \(N_1,N_2\) for the respective numbers of the two exponents, and \(h=N_1+2N_2\). The pinned neighbor theorem gives goodness of \(x-1,x+1,2x-1\) at every phase. For good \(t\), let \(H(t)\) and \(P(t)\) be its actual first hitting time and corresponding odd count in the shortcut map, and write \(J(t)=H(t)-2P(t)\). Use \(\Delta W(t)=W(3t)-W(t)\) only when both arguments are good. [Pinned lower floor and genuine good marks](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md)

At each exponent-one phase set \(u=(x+1)/4\), and at each exponent-two phase set \(v=(x-1)/8\). In the first case \(x'=6u-1<8q\), so \(u<s\) for \(s>3\). In the second, \(x=8v+1<8q\) gives \(v<q<s\). Both \(3u\) and \(3v\) are good. The following identities count phases with their native multiplicities.

| set of inputs | sum of \(\Delta H\) | sum of \(\Delta P\) | sum of \(\Delta J\) |
|---|---:|---:|---:|
| \(u\) from exponent one | \(h\) | \(N_2\) | \(N_1\) |
| \(v\) from exponent two | \(h\) | \(N_1\) | \(2N_2-N_1\) |

Follow \(Y=(x+1)/2\). On an exponent-one edge the two marked values are \(2u,3u\). On an exponent-two edge \(Y=4v+1\) reaches the next \(Y'=3v+1\) in two shortcuts with one odd departure. Summing the changes of \(H,P\) around the complete finite cycle gives the first row. For the second row follow \(Z=(x-1)/2\). On an exponent-one edge \(Z=2u-1\) takes one ordinary odd shortcut to \(3u-1=Z'\). On an exponent-two edge \(Z=4v\) and \(Z'=3v\). All marked values and intermediate points of those displayed nonempty paths exceed one in the putative ordinary branch. Thus first-hit costs subtract exactly. Goodness of \(Y'\) or \(Z'\) at the respective virtual step gives the required good triples.

The table uses all the original good hitting certificates without a uniform budget. In particular the two sums of actual clock differences agree, although their total odd differences generally differ. At a single smaller input the two differences can have either sign. On the ordinary controls \(u=9,41\), \((\Delta J,\Delta P)\) is respectively \((-13,35)\) and \((12,-25)\). For \(9,27,41,123\), the respective \((H,P)\) are \((13,6),(70,41),(69,40),(31,15)\). All four follow directly by iterating the positive shortcut to its first one. No contradiction to the two aggregate identities has been established.

## A fixed positive terminal has finitely many inverse words at bounded leading cost

Let \(X\) be a fixed positive integer and \(C>0\) finite. There are finitely many actual forward words ending at \(X\) and obeying \(2^t\le C3^b\), where \(t,b\) are their shortcut clock and odd grade. Intermediate heights can be arbitrary.

Indeed, the positive affine formula \(2^tX=3^b y+B\), \(B\ge0\), bounds every initial positive integer by \(y\le CX\). For each such \(y\), its successive hits of \(X\) are unique unless \(X\) is periodic. In the periodic case all later hits differ from the first by full primitive laps. If \((h_X,p_X)\) is its lap clock and grade, \(2^{h_X}/3^{p_X}>1\) since a positive cycle has an odd departure with strictly positive additive correction. Each extra lap multiplies the cost by this same factor, leaving finitely many hits below the prescribed cap. If every reversed prefix also satisfies that cap, every vertex is at most \(CX\). Enumeration on this finite graph terminates because repeated full laps eventually exceed the cap.

This argument supplies a termination test for an algorithm able to force new distinct words at **one fixed actual terminal** with a uniform leading cost. It presently supplies no rule forcing such a new word from a given least reverse disagreement. Allowing the terminal or its cost cap to change at successive trials discards the finiteness conclusion.

## What the cycle geometry leaves open

Every canonical bad \(z\equiv17\bmod48\) has \(T^4z=(9z+7)/16\) bad. Thus \(z\ge(16s-7)/9\). A proposed application of earlier canonical cuts up to this guaranteed threshold adds no new implication in the bounded alternative: the first four ordinary shortcuts already rule out every bad canonical query below it. An improvement requires information about the particular original \(z\).

Along a restricted native inverse edge \(x\mapsto x'=(2^a x-1)/3\), an alternative ordinary odd inverse of \(y=2^D x+C\) with exponent \(b\) produces \(y'=2^{D'}x'+C'\), where
\[
D'=D+b-a,\qquad C'=(2^b C+2^{D'}-1)/3.
\]
This formula is used only for actual positive integral odd predecessors. Starting at the same endpoint, the first departure from the native choice has \(b\ge a+2\). While \(D'\ge0\), its initially positive offset remains nonnegative. At a first crossing to \(D'=-1\) one must have \(a=2,b=1,D=0\) and \(y'=(x'+(4C-1)/3)/2\). The original floor can make this specific ancestor too small. No universal crossing, stronger ceiling, or pressure sufficient for the proposed arithmetic threshold has been proved. The synchronized competitors before a saving cannot directly equal the known good mark \(2x-1\), whose offset at \(D=1\) is negative.
