# Many ordinary prefixes before a crossing need almost linearly many short references

**Status: PROPOSED.** Fix $b\ge8$ and $D=40b$. There are $2^{9b}$ explicitly specified ordinary positive sources in $[2^{36b},2^{36b+1})$. For each of them every positive-duration prefix through $D$ has homogeneous coefficient strictly above one, every state after time zero is strictly above its initial value, and all $D+1$ states are distinct. There are at least $9b$ maximal runs of odd departures in the full window. For every $H,K\ge1$, at most

\[
             K\,[9(D+1)^2 H^4]^K                                      \tag{1}
\]

of these windows admit at most $K$ arbitrary affine reference arcs with both endpoint heights at most $H$. The estimate even permits references coinciding with the physical path. In particular, for fixed $A\ge0$, all but an exponentially small proportion require more than a constant times $D/\log D$ arcs of endpoint height at most $D^A$. The result concerns changing finite ordinary starts. It tests an extraction rule based on the lack of a crossing over one observed horizon.

## Physical construction

Choose independently $9b$ four-bit words, each either $1110$ or $1101$. The concatenation has length $m=36b$ and grade $27b$. Every $m$-bit parity word determines a unique source residue modulo $2^m$: the first bit fixes the residue modulo two, and lifting a partial source by $2^j$ flips its parity at time $j$ since the two equal-prefix endpoints differ by the odd multiplier $3^{g_j}$. Pick the unique representative $n\in[2^m,2^{m+1})$. Distinct choices give different ordinary sources and different $D$-words. The last $4b$ bits are whatever their actual orbits produce.

For each possible tile, $3^{g_j}>2^j$ on every nonempty prefix, including the full tile with $3^3>2^4$. Products give the strict inequality through clock $m$. At any later clock through $D$ the homogeneous coefficient is at least $3^{27b}/2^{40b}>1$, since $3^{27}>2^{40}$. The physical affine carry is nonnegative, so $T^j(n)>n$ for $1\le j\le D$. Each tile contains one zero, with every two zeros separated by at least two ones in the controlled portion. Consequently there are at least $9b$ odd runs. The first $90\%$ of the window has at most four consecutive ones and no consecutive zeros. Across the entire window the longest run is at most $4b+1$.

To prove simplicity, a positive integral cycle segment of duration $L$, with grade $s$ and least state $v$, satisfies

\[
 2^{-L}\le \frac{2^L-3^s}{2^L}\le \ln(2^L/3^s)
 =\sum_{\rm odd\ phases}\ln(1+1/(3x))\le\frac{L}{3v}.
\]

The first inequality uses the positive integer $2^L-3^s$, and positivity follows from the product identity since any positive cycle contains an odd state. Thus $v\le L2^L/3$. A return of duration $L\le32b$ in the window would have minimum below $2^{36b}\le n$, since $32b<3\cdot2^{4b}$ for $b\ge8$. For $L>32b$, lose at most $4b$ letters outside the controlled portion and at most six partial-tile letters. Its grade is at least

\[
       \frac34(L-4b-6)\ \ge\ \frac7{11}L,
\]

since $5L\ge132b+198$ for $b\ge8$. The coefficient on this whole segment exceeds one by $3^7>2^{11}$, which again forbids equality of its endpoints.

## Effective count

An arc of specified length $j$, grade $s$, initial reference $u$, and terminal reference $v$ has prescribed carry $C=2^jv-3^su$. If it is the affine map of a physical word, $C$ is an integer, and its initial source class is given by $3^sx+C\equiv0\pmod{2^j}$. Thus at most one such word is possible, even if the references themselves fail to realize its intermediate parities. A rational of height at most $H$ has at most $H(2H+1)\le3H^2$ possible numerator-denominator descriptions, with denominator positive. Two endpoint descriptions, one duration, and one grade give at most $9(D+1)^2H^4$ choices per arc. Summing over the $K$ possible arc counts and using distinct physical words proves (1). This calculation charges the entire description, including the clocks.

For example, put $H=D^A$ and

\[
 K=\left\lfloor\frac{4b}{4+(2+4A)\log_2(D+1)}\right\rfloor .
\]

For $b$ such that $K\ge1$, (1) is at most $K2^{4b}\le 2^{5b}$. Thus at least a fraction $1-2^{-4b}$ require more than $K$ arcs. More generally, whenever $K\ge1$ and $b\ge256K^2$, taking $H=2^{b/K}$ again gives this fraction: $\log_2K+K\log_2 9+2K\log_2(40b+1)\le17K+2K\sqrt b\le b$.

The uncontrolled fraction can be made arbitrarily small while keeping an overhang beyond the starting bit length. Replace $9b$ by $sb$ tiles and $40b$ by $4(s+1)b$, where $s\ge9$ is any fixed integer. The terminal uncontrolled portion is still $4b$. The same positivity and simplicity proof works: the long-cycle threshold $32b$ remains valid while the starting height increases, and the controlled grade $3sb$ pays for the full horizon by $3^{3s}>2^{4(s+1)}$. Thus the maximum run over the whole word is at most $D/(s+1)+1$, with at least $sb$ distinct odd runs. The assertion does not impose an absolute run bound on the final uncontrolled portion.

The first-crossing manuscript of De Jesús concerns an actual *first crossing* and proves descent under an upper bound on the number of maximal odd runs. These windows have not crossed by $D$ and already contain linearly many such runs. Nashida gives upper bounds on counts of long stopping times at specified smaller source scales. The present lower construction makes a finite non-descent history expensive to describe by arbitrary affine references. It does not supply an infinite non-descending trajectory, or constrain a rule that uses information from the unobserved continuation. [De Jesús, current manuscript](https://hexagonmath.org/2611.00459v4) · [Nashida, revision 7 and precise formal hypotheses](https://github.com/harappa/collatz-terras-bound-improvement/blob/master/README.md)

The [checker](check_reference_shadows.py) constructs 192 literal sources for $b=8,11,16$, replaying 89,792 vertices. It checks every prefix multiplier, all strict physical inequalities, run counts, and whole-window simplicity. For the first five length-320 samples, dynamic programming gives height-two affine costs of 80, 82, 81, 80, and 81. The [physical-reference argument](REFERENCE_SHADOWS.md) improves the finite count (1) to $K[3(D+1)H^3]^K$.
