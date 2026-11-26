# Smaller tripling queries from two signed reference orbits

**Status.** The finite guarded cover, paired positive-ordinary mergers and 13 full exponent progressions below are unconditional Lean theorems. The determinant characterization and the all-clock exclusion of integer reference pairs have written proofs. The numerical inequality used for the denominator bound is also a Lean theorem. A proof for every remaining ordinary source is open.

Use the shortcut map, write $C(x)$ when a positive ordinary input reaches 1, and use the previously proved existence of a least reverse defect if Collatz fails. Such a defect $z$ is $17\bmod 48$, has $C(3z)$, and fails $C(z)$. A positive $w<z$ with the same residue and both ordered basin labels would violate minimality.

## Sixteen residue rows at every upper rank

[GuardedResidueCover.lean](GuardedResidueCover.lean) contains sixteen short paths $z\longrightarrow3z$ on full positive affine progressions. Eleven use only ordinary shortcut or inverse edges. The other five also use one forward tripling at an affine integer $w\equiv17\bmod48$ strictly smaller than the original $z$ for every row parameter. If $z$ were the least reverse defect, its lower nonbasin label would persist across every ordinary edge and across this guarded query. It would therefore reach the known basin value $3z$. The paths use the existing sound checker for ordinary edges in DirectedEleven.lean. This is a sourcewise exclusion at all upper ranks.

Modulo $12288$ the sixteen disjoint rows account for **55 of the 256** possible residues $17\bmod48$. The eleven direct rows cover 42, and the five paths using a smaller query cover 13. The census measures this particular bank. A missing row may have other proofs. For example, the direct path for $z=768t+545$ is in the bank, while the remaining residue set contains every sufficiently late member of the Mersenne family in the following sections.

## Ordinary lift around a signed reference

Extend the shortcut to rationals of odd denominator using the parity of the reduced numerator. Write $S$ for this signed map, $p_h$ for the count of odd inputs in the first $h$ steps, and $G_h(a)=3^{p_h(a)}/2^h$. For $z-a$ divisible by $2^h$ in the rationals of odd denominator,
$$
T^h(z)=S^h(a)+G_h(a)(z-a).
$$
At each shared parity the difference is multiplied by $1/2$ or $3/2$, which proves this finite identity. Each use below has an ordinary positive starting point where an actual basin assertion is made.

Suppose that two signed references $a,b$ reach the same cycle on their lower arms and that $3a,3b$ reach the same cycle on their upper arms. The two cycles can differ. At a selected phase on each cycle record each reference's entry clock and grade. For the lower arm let the difference from the $b$ record to the $a$ record be $(p,h)$, in the order (odd count, clock), and use $(P,H)$ for the upper arm. Denote the period vectors of their cycles by $(v,l),(V,L)$. An alignment through these phases with the same slope ratio $\lambda$ on both arms exists exactly when
$$
 (p,h)+n(v,l)=(P,H)+m(V,L),\qquad n,m\in\mathbb Z.
$$
Each signed integer number of turns can be realized by adding turns on the appropriate reference. Equality follows from unique factorization of powers of two and three. If the common pair is $(e,g)$, set $\lambda=3^e/2^g$. Every ordinary lift $z,w=b+\lambda(z-a)$ having the required precision then has two physical meetings. The required precisions concern all four prescribed clocks. Positivity, residues and strict height are further checks on the ordinary lifts. Determinant $vL-lV=\pm1$ guarantees an integer solution to the alignment equation, leaving these further requirements in force.

A shared cycle on the two arms gives a centered construction. At $a=-1183$ both arms have returned after three steps with two odd inputs from clock 28. For every positive $t$ take
$$
 z+1183=7247757312t,\qquad w+1183=6442450944t .
$$
Then $w\equiv17\bmod48$, $0<w<z$, and each arm meets its partner, by inverse scaling with $8/9$. The signed references need not meet each other at a common clock. More generally, a positive reference $a\equiv17\bmod48$ with both $a,3a$ reaching 1 by the supplied clock bound $H$ yields $w=a+3(z-a)/4$ for every $z>a$ in the same residue with $2^{H+6}\mid z-a$. Independent entry clocks are permitted. [SignedCycleDilation.lean](SignedCycleDilation.lean) checks the signed lifting and common-period statements and the full $-1183$ row.

For different centers $a=-1807,b=-127$, the common lower phase is $-1$ at counts and clocks $(9,25),(8,19)$, and the common upper phase is $-5$ at $(12,29),(11,23)$. Both ratios are $3/64$. On
$$
 z+1807=1610612736t,\qquad w+127=75497472t
$$
the two ordinary mergers and strict residue-preserving reduction hold at every positive parameter. These lower and upper cycles have different odd densities. [DifferentCycleAnchors.lean](DifferentCycleAnchors.lean)

## Thirteen rational reference pairs on the rank-three Mersenne family

Use the actual PR197 family
$$
 j=11+162m,\qquad 81z+271=2^{j+7}.
$$
The first seven lower steps have four odd inputs and give $T^7 z=2^j-1$. The upper triple first reaches 1 after three odd inputs. For the first reference $a=-271/81$, the lower arm reaches $-1$ after seven steps and the upper arm reaches zero after nine. Their cycle vectors are $(1,1)$ and $(0,1)$, with determinant one.

Write the second rational reference as $b=-B/3^d$. In each row below, a finite signed calculation gives
$$
 S^s b=-1,\quad p_s(b)=d,\qquad S^{s+2}(3b)=0,\quad p_{s+2}(3b)=d-1 .
$$
For $m=m_0+P t$, the query is
$$
 3^d w=2^{j+s}-B,\qquad T^s w=2^j-1,\qquad T^{s+2}(3w)=2^{j-2}.
$$
It is an ordinary positive integer strictly below $z$ and congruent to 17 modulo 48. Thus $C(w)\leftrightarrow C(z)$ and $C(3w)$ on the entire supplied progression. The last equality gives an actual finite upper orbit even when nothing is assumed about $C(z)$.

| $d$ | $B$ | $s$ | $m_0$ | $P$ |
|---:|---:|---:|---:|---:|
| 12 | 2692031 | 18 | 5903 | 6561 |
| 12 | 4970719 | 19 | 1286 | 6561 |
| 13 | 7686973 | 19 | 2258 | 19683 |
| 13 | 8962877 | 20 | 11889 | 19683 |
| 13 | 10144829 | 20 | 44 | 19683 |
| 13 | 10984637 | 20 | 1124 | 19683 |
| 13 | 11299565 | 20 | 1529 | 19683 |
| 13 | 14133917 | 20 | 5174 | 19683 |
| 13 | 16685725 | 21 | 13347 | 19683 |
| 13 | 19049629 | 21 | 1502 | 19683 |
| 13 | 20414317 | 21 | 12221 | 19683 |
| 13 | 20729245 | 21 | 2582 | 19683 |
| 13 | 21359101 | 21 | 2987 | 19683 |

The two period-6561 rows each contribute three residues modulo 19683. All seventeen resulting parameter residues are distinct. This is an explicit bank, without any claim of exhaustiveness over other references or degrees.

[MersenneTwoCenter.lean](MersenneTwoCenter.lean) constructs the physical queries directly on nonnegative affine lifts. For each row put $N=2^{j-2}$, $D=3^d$ and $R=2^{s+2}$. Fast modular powering gives $N=48Dq+c$ on the whole progression. The code uses $w=48Rq+(Rc-B)/D$ and $81z+271=512N$, checking the two affine words on their entire common domain. Its public theorem returns the strict smaller query, lower basin equivalence and upper basin membership. [check_signed_routes.py](check_signed_routes.py) independently checks the signed rational equations, modular periods, positive affine bases and disjointness.

## A bound applying at every chosen clock

Let $u=j+7$, take a rational first reference $a=z+2^H K/D$ with $D$ positive odd and $K$ a nonzero integer, and suppose $|S^H(a)|\le M$ for $M\ge1$. Exclude $a=-271/81$. If $H\ge u$, then
$$
                         81\,3^j\le81D+2MD^2.                         \tag{1}
$$
In particular, a different reference of denominator $3^d$ used after the entire ascent requires $d\ge j/2-O_M(1)$, regardless of the horizon or the choice of a second reference.

**Proof.** Write $H=u+v$, $Q=2^v$. The actual lower orbit has $T^u z=3^j-1$ with $j+4$ odd steps. Hence
$$
 S^u(a)+1=3^j(D+81QK)/D .
$$
The integer inside the parentheses is nonzero precisely because $a\ne-271/81$. Along an inverse orbit from $|y|\le R$ with $R\ge1$, an even inverse has magnitude at most $2R$ and an odd inverse $(2y-1)/3$ has magnitude at most $(2R+1)/3\le2R$. This holds for signed rationals throughout. Consequently $|S^u(a)|\le QM$ and
$$
 3^j |D+81QK| \le D(MQ+1).
$$
If $81Q\le2D$, use the nonzero integer lower bound one to obtain (1). Otherwise $|D+81QK|\ge81Q-D>81Q/2$ and $81\,3^j\le2D(M+1)\le81D+2MD^2$. This proves (1). The algebraic implication, with the explicit separation and budget hypotheses, is checked by DifferentCycleAnchors.height_debt. The orbit-to-budget argument is a written proof.

**Integer references.** Consider two ordinary-integer signed anchors whose comparison clocks end in the union of the cycles through $0,1,-1,-5,-17$. They may use different lower and upper cycles. Use $H$ for the larger source-alignment clock, require $2^H\mid z-a$, and permit arbitrary target clocks. The initial source reference $a$ must differ from the positive input $z$. No such pair gives an ordinary $0<w<z$ with $w\equiv17\bmod48$ by the affine alignment above.

The absolute cycle bound is 136, so (1) excludes $H\ge u$ at $D=1$. For $7\le H<u$, seven lower steps reach $2^j-1$, whose next $j$ inputs are odd. Signed lifting yields
$$
 S^H(a)+1=3^{H-7}\,(81a+271)/2^H.
$$
The ratio on the right is a nonzero integer because $a$ is integral and congruent to $z$ at this precision. Therefore $3^{H-7}\le137$ and $H\le11$. For $0\le H\le11$ let $r\equiv-271/81\bmod2^H$ be the least nonnegative representative. For each possible lower cycle value $x$ the only candidate is
$$
 a=r+2^H(x-S^H(r))/3^{p_H(r)} .
$$
Discard noninteger quotients and test whether $S^H(3a)$ is in the cycle list. The complete resulting pairs $(H,a)$ are $(0,0),(4,1),(5,1)$. In particular there is no such first reference in $17\bmod48$. The replay performs this finite inversion without a magnitude cutoff.

At $H=0,a=0$ the only integer with an iterate zero is zero. Both references would be zero, and with source clock zero the slope ratio is at least one. At $a=1$ the upper source $3$ can align on its positive cycle only at clock four or five. The terminal value divided by its affine slope is $32/9$ at either clock. A target reference $b$ leading to this positive upper phase must be a positive integer. The positive forward affine intercept is nonnegative, so a matching ratio obeys $\lambda\ge27b/32$. If $b\ge2$, then $w=b+\lambda(z-1)>z$. For $b=1$ equal lower phases give $\lambda=(3/4)^k$ for some integer $k$. Shrinking requires $k\ge1$, while $v_2(z-1)=5$ gives $v_2(w-1)=5-2k\le3$, incompatible with the required residue. This handles the exceptional first references. It does not restrict pairs of rational centers such as those proved above, other cycles, or general source-dependent physical paths.

## Remaining scope and provenance

On any fixed binary precision all sufficiently late exponents in this family occupy one row. A uniform finite directed path to a strictly smaller residue-17 query on all those exponents would give a uniform first query from $2^j-1$ by the seven-step equivalence. PR197's earlier whole-progression quotient proves that there is no such first query in this family, including paths with arbitrary fixed word lengths. The thirteen successful cases use different ternary refinements. A source-dependent process could refine until $j+7$ or later, but its guaranteed ordinary endpoints at that clock are $3^j-1$ and 1. A recurrence reducing these to another certified strictly smaller reverse-defect comparison remains open. The 201 uncovered binary rows come with no such recurrence.

The normalization, rank-three family and uniform-query obstruction come from PR197 at 156652e03fe7a78f9cd4442039779cc622fdf3de, in closing-proposal/MersenneBarrier.lean and source-progress/UNIFORM_MERSENNE_QUOTIENT.md. The directed trace checker is directed-return/DirectedEleven.lean at the same commit. Yolcu, Aaronson and Heule, *An Automated Approach to the Collatz Conjecture*, Theorem 3.17, proves equivalence between termination of its complete unrestricted mixed-base presentation and ordinary convergence. The present guarded comparisons use ordinary integers and leastness; they supply no decreasing interpretation of all eleven rules. Nashida's frozen primary source at de961be6671b2084ae0189a3572b674c60788456 states an all-dimensional natural-matrix no-removal theorem with top-left entries at least one, and its corresponding arctic barrier with finite top-left entries. Those model classes and their particular preprocessing results leave the guarded constructions here available. The external Lean development was inspected, not independently rebuilt for this packet. [AYH paper](https://emreyolcu.com/research/rewriting-collatz.pdf) · [Nashida source](https://github.com/harappa/collatz-arctic-interpretation-barriers/tree/de961be6671b2084ae0189a3572b674c60788456)
