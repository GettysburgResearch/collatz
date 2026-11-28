# A computable up-down map with infinitely many cycles and a divergent ray

Let \(U(x)=\lceil3x/2\rceil\) and \(D(x)=\lceil x/2\rceil\). Vasilyev's Question 7.3 asks whether some choice of one outgoing branch at each positive integer yields both infinitely many cycles and a divergent orbit. There is a computable choice with infinitely many cycles and exactly one class of divergent orbits under eventual coalescence. [Vasilyev, v1, Remark 4.4 and Question 7.3](https://borowiecki.dev/pdf/2611.20344)

## A finite region avoiding a growing path

Let \(m\equiv5\pmod6\). In \([m+1,3m-1]\) delete \(2m\) and every point of the upward chain \(m,U(m),U^2(m),\ldots\). The remaining finite set \(K_m\) contains \(m+1\), since \(m+1<U(m)\). It supports a cycle without using any deleted point.

Indeed, for \(z\in K_m\) with \(z\le2m-1\), choose \(U(z)\). This value lies in the prescribed interval. It differs from \(2m\), since \(2m\equiv1\pmod3\) whereas the upward image consists of residues zero and two. The strictly increasing map \(U\) is injective. An upward move into an iterate \(U^j(m)\) with \(j>0\) would therefore come from the preceding chain vertex, which is excluded. When \(z\ge2m+1\), choose \(D(z)\). Since \(m\) is odd,
\[
           m+1\le D(z)\le (3m-1)/2=U(m)-1.
\]
This also avoids \(2m\) and the whole chain. Iterating these choices from \(m+1\) must eventually repeat a vertex in \(K_m\), and its periodic part is a simple cycle.

## Reaching a strict record of the required residue

From every positive odd \(y\), a word of at most six moves ends at a strict record \(m\equiv5\pmod6\). Here a strict record exceeds the starting value and every earlier value of the word. The following table covers all odd residues \(r=y\bmod128\). Read each word from left to right.

| Condition on \(r\) | Word |
|---|---|
| \(r\equiv3\pmod4\) | U |
| \(r\equiv1\pmod{16}\) | UUU |
| \(r\equiv13\pmod{16}\) | DUU |
| \(r\equiv9\pmod{32}\) | UDUU |
| \(r\in\{5,57,69,121\}\) | UUUUU |
| \(r\in\{21,85\}\) | DUUUU |
| \(r=25\) | DUUDUU |
| \(r\in\{37,101\}\) | UUDUU |
| \(r\in\{53,89\}\) | UUUDUU |
| \(r=117\) | UUUUUU |

For completeness the finite arithmetic certificate extends exactly to every positive input. For \(y=r+128q\), the \(j\)th state is the state from \(r\) plus \(q b_j\), where \(b_j=128\cdot3^{a_j}/2^j\) and \(a_j\) counts upward moves in the prefix. Each preterminal \(b_j\) is even, so the formula follows by induction through both ceiling maps. For every one of the 64 residues the terminal state at \(r\) exceeds every preceding state, the terminal \(b_j\) exceeds each earlier coefficient, the terminal state is five modulo six and the terminal coefficient is divisible by six. These are integer checks on words of at most six letters. The smallest excess of a terminal state at \(r\) above the preceding maximum is two. The accompanying checker computes the four conditions directly. [Exact certificate](check_infinite_cycles_and_ray.py)

## One infinite map

Begin the path with \(1,2,3,5\), making \(m=5\) its first record marker. From a marker \(m\), take upward moves until reaching an odd \(y>64(3m+1)\). Such inputs occur arbitrarily far up the chain: from an even integer each upward move decreases the two-adic valuation by one until an odd integer appears, and upward moves strictly increase every positive input. Apply the word in the table to \(y\), obtaining the next marker \(m'\). All states of that word exceed \(3m\), since either branch decreases the input by a factor of at most two, and there are at most six moves. The terminal marker strictly exceeds all earlier states of the entire stage. Each stage interior therefore lies strictly between its endpoints.

Erase loops in this finite stage as they occur, keeping its endpoints and legal directed edges. The initial upward segment through \([m+1,3m-1]\) survives, since the later word lies entirely above \(3m\). Concatenate the resulting simple paths. The ordered endpoint intervals have disjoint interiors, so this gives a simple divergent ray from 1. In every marker interval this ray consists exclusively of vertices of the corresponding upward chain. Future stages lie above the interval.

In each finite \(K_m\) choose the cycle obtained from \(m+1\) by the preceding rule. Different marker intervals are disjoint and every such cycle is disjoint from the entire ray. Assign the indicated choices on these components, and the downward choice at every other positive integer. This defines a single set \(S\) of upward sources. Every unmarked point above one strictly decreases until it encounters a designated component, since 1 belongs to the ray. Hence the selected cycles constitute all finite cycles, and all divergent orbits eventually coincide with the selected ray. Membership in \(S\) is computable by generating finitely many stages until the next marker exceeds the queried input; every later stage lies above it. The construction concerns unrestricted up-down sets, including upward moves at even integers.
