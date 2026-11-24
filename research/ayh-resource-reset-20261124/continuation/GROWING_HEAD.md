# Growing ternary prefix and truncation along a physical orbit

**Written theorem, conditional only on the identified written PR 146 estimate for its counting clause.** Put $D=\lfloor\log_2 n\rfloor$, $X=2^D$, and, for large $D$, set
$$
 H=L=\left\lfloor\frac{\sqrt D}{\log(D+2)}\right\rfloor,\qquad
 b=\lfloor D/2\rfloor .
$$
Here $\log$ is natural. There is a deterministic choice of $0\le j\le H$ for each sufficiently large positive ordinary $n$ such that $x=T^j(n)$ is represented by the PR 183 blocked normal word **c a f**, then $t(H)$ ternary zeroes, then a purely ternary suffix of at least $L$ more digits. Both $t(H)$ and $L$ tend to infinity. Its ordinary partner satisfies
$$
 0<m=\lfloor x/3^L\rfloor <(n+1)2^{-H}.
$$
In every sufficiently high octave $[X,2X)$, all but $O(X/\log(D+2))$ sources further satisfy $T^b(x)=T^b(m)$, at equal physical clocks after selecting the hit. Thus a density-one set of original sources has an actual smaller component partner with this bound. The selected forward hit values themselves form a set of natural density zero. Membership in that sparse section does not ensure fusion on every individual input.

## A deterministic choice using only the high digits

Use the circle coordinate $\log_3 n\bmod 1$. Ignoring the positive additive one on odd steps, a clock advances the coordinate by $-\log_3 2$ regardless of the number of odd steps, because powers of three have zero phase. The rotation angle is irrational by unique prime factorization. For $t\ge0$ take the interior test interval of normalized values
$$
 I_t=[7+3^{-t}/4,\ 7+3^{-t}/2)
$$
and its translates by integer powers of three. Define $t(H)$ as the largest nonnegative $t$ for which every point of the circle has some clock $0\le j\le H$ landing in the projected interval under this ideal rotation. If none exists, use the fallback below. Irrationality makes each fixed open interval a finite covering target: all its backward translates cover the compact circle and a finite subcover suffices. Thus $t(H)\to\infty$. The logarithmic length of the test interval is at most $3^{-t}/(28\log 3)$. Since $H+1$ translates cover the circle, $3^{-t(H)}\ge 28\log 3/(H+1)$ and $t(H)=O(\log(H+1))$. The coverage predicate and the lowest eligible $j$ can be computed with rational endpoint comparisons, using the arcs $2^j I_t3^{\mathbb Z}$. Select the least such $j$ for $n$.

If $s$ odd steps occur, the ideal value is $y=3^s n/2^j$ and $x/y$ is the product of the actual odd-step factors $1+1/(3T^i(n))$. Every preceding state is at least $n/2^H$. Consequently $1\le x/y\le\exp(H2^H/(3X))$. This error minus one is $O(H2^H/X)=o(1/H)$, uniformly in the octave. With the interior margin and width bound just proved it follows that
$$
  7\cdot3^k\le x < (7+3^{-t(H)})3^k
$$
for some integer $k$. Also $x\ge X/2^H$, so $k\ge (D-H)/\log_2 3-O(1)>L+t(H)$ eventually. The actual representation therefore has the required leading and trailing lengths. For a fixed $t$, the upper natural density of the union of these ternary windows is $O(3^{-t})$: up to $Y$, summing their lengths $3^{k-t}$ is a geometric series $O(3^{-t}Y)$, with at most $O(\log Y)$ endpoint-rounding error. Outside the images of finitely many small sources all chosen hits lie in the windows for any prescribed fixed $t$. This proves density zero for the selected hits. Finally $x+1\le(3/2)^j(n+1)$, hence the displayed partner bound from $L=H$. Terminal trit deletion is a written strict decrease of the same mixed-word rank as in the fixed-head proof.

## A finite grid conditional on both ends

PR 146's growing-gap estimate on a complete depth-$b$ binary grid bounds failure of synchronous *affine-profile fusion* of the pair $m,3^L m+r$ by relative fraction
$$
 \epsilon_{L,b}\ \ll\
 \frac{1+L+\sqrt{\log(2+|r|/3^L)}}{\sqrt b}
 \ \ll\ \frac{1+L}{\sqrt b}\qquad(0\le r<3^L).
$$
The finite grid is the one in the proof of its equation (1), before the passage to arbitrary intervals. Affine-profile fusion implies equal ordinary endpoints for every positive lift of a good residue, and equality persists. The absolute constant and the probability estimate are inherited written mathematics. The Lean checks in this packet cover the fixed-head theorem and the specified 81-child progression.

For a **fixed** clock $j\le H$, take a full period $P=2^{b+H}3^L$ of possible original sources. Fix the $j$ low bits $a$ of $n=a+2^j u$. The parity word through clock $j$ is then fixed, and $x=A+3^p u$ for its odd count $p$ and integer $A=T^j(a)$. Further fix $u\bmod3^L$. The residue $r=x\bmod3^L$ stays fixed, while $m=\lfloor x/3^L\rfloor$ progresses by the odd stride $3^p$. There are exactly $2^{b+H-j}$ terms in each such cell of a complete period, supplying each binary residue modulo $2^b$ equally often. This is valid also when $p\ge L$. No division by three modulo a ternary modulus or assumption of independent high and low digits is involved. In the algebraic completion at a boundary, mark bad *binary residues* by the PR 146 symbolic test, then apply the resulting count only to the actual positive pairs. Thus on every full period the relative failure count for this fixed clock is at most $\epsilon_{L,b}$.

The chosen clock depends only on the ideal mantissa. For each $j\le H$, the clock eligibility set on $[X,2X)$ consists of at most two intervals, since the octave's multiplicative length is two and the powers of three are separated by a factor three. Overlaying all interval boundaries gives $O(H+1)$ consecutive intervals on which the **selected** clock is constant. On each such interval tile by full periods of length $P$ and charge at most $2P$ for partial boundary periods. Summing, the count of failed sources is
$$
 \le \epsilon_{L,b} X+O((H+1)P).
$$
Here $P=2^{D/2+O(H)}$ up to fixed factors, so $(H+1)P/X$ decays exponentially in $D$ for sufficiently large $D$. This yields $O(X/\log(D+2))$ exceptions. A finite or partial last octave preserves natural density one by combining the full-octave bound with the geometric series over earlier octaves. Each successful source meets its smaller partner in at most $H+b$ physical clocks from the original source and at most $b$ from the partner.

## Exact global criterion and remaining step

A total deterministic test can use this growing schedule whenever the circle cover exists and the computed actual state has the stated head, sufficient suffix length, and a positive partner strictly below the original source. On any other input, use the fixed ten-clock schedule of [FIXED_HEAD.md](FIXED_HEAD.md), with a direct convergent branch when a state below 600 occurs. Each test is finite, and only finitely many sources can need this fallback. Define $G$ to be the requirement that on every selected non-base edge the actual hit and its prescribed truncation eventually meet (arbitrary finite clocks). Universal convergence implies $G$ by meeting at one. Conversely, strong induction on the original source shows that $G$ implies universal convergence, since the partner is strictly smaller than that source, including on the fallback. This global criterion and its growing-depth estimates are written arguments.

A density bound on the uncertified edges does not show $G$. Even density one of initial sources with a successful edge does not give a new uniform binary grid on the partners reached by following the rule. A least failing ordinary source, if one exists, can lie in the exceptional set. The conditional distribution at that least source is the missing inference.

[PR 146 finite-grid estimate, equation (1) and proof](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) · [PR 146 oriented-state input estimate](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)
