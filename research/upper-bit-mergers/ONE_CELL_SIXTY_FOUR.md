# One residue modulo 64 suffices

**PROPOSED, unconditional.** For the ordinary positive shortcut map $T$, write $f(n)$ for the eventual-merger component of $n$ and $P(n)$ for $f(n)=f(3n)$. The following conditions are equivalent.

1. Every positive integer reaches 1.
2. Every sufficiently large odd multiple of 9 satisfies $P$.
3. Every sufficiently large $n\equiv1\pmod{64}$ satisfies $P$.

The proof removes the exceptional odd inputs by ordinary affine identities and a finite residue graph. The graph allows two infinite formal paths. Neither can be the path of positive integers. No density estimate or limiting distribution of Collatz trajectories is required. The unrestricted equivalence between universal $P$ and full convergence is proved separately. [Tripling and descent](THREE_RAY.md)

## Stabilizing high ternary multiples

Suppose (2) holds above $N$. Doubling preserves the component, so for every $x$ the sequence $f(3^j x)$ is eventually constant. Denote its eventual label by $F(x)$. Then $F(2x)=F(3x)=F(x)$. For odd $x>N$ divisible by 9 we have $f(x)=F(x)$.

In fact $f(u)=F(u)$ for **every** odd $u$ prime to three. Choose arbitrarily large $a$ with $2^a u\equiv1\pmod{27}$. These exponents form one class modulo 18 since 2 has order 18 modulo 27. The positive odd $z=(2^a u-1)/3$ is divisible by 9 and exceeds $N$. Therefore $f(u)=f(z)=f(3z)$, using $T(z)=2^{a-1}u$. Write $g(y)=f(y-1)$. The identity $T(2v-1)=3v-1$ gives $g(2v)=g(3v)$, hence
$$
 f(u)=g(2^a u)=g(3^a u).
$$

Along the indicated exponent class, $Y=3^a u$ runs through every residue in its fixed class modulo 8 at any higher binary precision. Indeed $v_2(3^{18}-1)=3$ and $v_2((3^{18})^{2^j}-1)=3+j$ by repeated squaring. The following four ordinary words supply $g(Y)=f(Y)$ for one binary subclass of each odd residue modulo 8. Equal clock and equal odd count propagate the common endpoint under shifts of $2^h$, where $h$ is the clock.

| $Y\bmod8$ | Required $Y$ modulo $2^h$ | $h$ | Endpoint at base for $Y-1,Y$ | Odd inputs on each path |
|---:|---:|---:|---:|---:|
| 1 | 369 | 9 | 20 | 3 |
| 3 | 3 | 4 | 2 | 2 |
| 5 | 5 | 3 | 2 | 1 |
| 7 | 23 | 5 | 20 | 3 |

At arbitrarily large such $a$, $f(Y)=F(u)$, which proves the assertion. In particular for every sufficiently large odd ternary unit $u$ we have $f(u)=f(9u)$. Thus $P(u)$ and $P(3u)$ have the same truth value. Call $u$ a *failed unit* if both fail. All sufficiently large odd failures are failed units or their triples.

## Two forced comparisons

For every failed unit $u$ above the threshold at least one of $16u+1,32u+1$ fails $P$. This is the ordinary two-successor identity at $3u$ in the [window proof](THREE_RAY_WINDOWS.md#when-three-divides-the-defect). One can check it by writing $J(y)=f(y+1)$. The equality $J(4v)=J(3v)$ always holds. If $16s+1$ passes, two steps from $3(16s+1)$ reach $4(27s+2)$, and $T(18s+1)=27s+2$. Hence $J(9s)=J(18s)$. If both inputs passed, applying this at $s=u,2u$ would give $J(9u)=J(36u)=J(27u)$ and therefore $P(3u)$.

Choose a failed $v=cu+1$ with $c\in\{16,32\}$. It cannot be divisible by 9. If it is divisible by three, its unit part $v/3$ is a failed unit by the paired property. Otherwise $v$ itself is a failed unit. The new unit in either case is strictly larger than $u$. At each step one possible $c$ gives a ternary unit, and the other gives a multiple of three. In the first case that unit equals 2 modulo 3, because $c=16,32$ give opposite nonzero residues there.

A second necessary comparison applies to a failed unit $v\equiv1\pmod{16}$ and $v\equiv2\pmod3$. At least one of $w=(8v-1)/3$ and $3w$ must fail $P$. Indeed $T(w)=4v$. If $P(w)$ holds then $f(v)=g(8v)$. If $P(3w)$ holds, then $g(8v)=g(9v)$ since $T(3(8v-1))=4(9v-1)$. Also $g(9v)=g(6v)$. For $v\equiv1\pmod{16}$ the pair $6v-1,6v$ meets after five steps by the ordinary word at $5,6$ lifted by a multiple of 32. Thus $g(6v)=f(6v)=f(3v)$, a contradiction. In particular $27\nmid8v-1$. The ternary-unit part of $8v-1$ must be a failed unit, by the paired property and cleanness of high multiples of 9. All auxiliary uses are valid by starting sufficiently far above $N$ (for instance $u>10(N+1)$), since these auxiliary units are at least $(8v-1)/9$.

## The two recurrent transitions

Here is the full finite rule for tracing any such failed units. A unit has state $(b,t)$, its residues modulo 256 and 27. Reject a binary residue $b$ whenever one of the pairs $b,3b$ or $3b,9b$ has a common endpoint in the same clock $h\le8$ with the lower arm using exactly one more odd input. The two affine slopes then agree on every shift of the original unit by 256, so one of the required failed pairs is known to meet. Also reject $t\equiv0\pmod3$. If $b\equiv1\pmod{16}$ and $t\equiv2\pmod3$, apply the second necessary comparison: reject if $27\mid 8t-1$, or if the binary residue $(8b-1)/d$ is rejected by the same ordinary-word test, where $d=3$ or 9 is the exact ternary power in $8t-1$. Division by $d$ here uses its inverse modulo 256.

At an allowed state try $c=16,32$. If $cu+1$ is a ternary unit, update to $cu+1$ and continue. This branch is unique. It cannot continue indefinitely without dividing: after the first such step its input is always 2 modulo 3, so its next multiplier is always 32. Two successive applications of $u\mapsto32u+1$ give $33\bmod256$, and $33$ and $99$ have a common endpoint at clock 8, with four and three odd inputs. For the other branch update to $(cu+1)/3$, discarding it if it fails the allowed-state test. Its possible ternary residues modulo 27 are the three lifts of $(ct+1)/3\bmod9$. Record each such division as one return, with its full affine map $u\mapsto(Au+B)/3$ including any preceding steps without division.

After two steps, the binary residue is independent of the initial input for any specified two branch choices: each slope is divisible by 16 in the binary integers. At returns following this initial segment the only binary residues passing the ordinary-word test are 91 and 203. The [short exact verifier](check_three_cell64.py) enumerates the return edges from these two residues and all 18 ternary units modulo 27. Project to the ternary residue, retaining every allowed destination from either binary state, and iteratively remove vertices with no outgoing edge to the remaining set. The resulting graph is

| Current ternary residue | Possible next residues on an infinite path |
|---:|:---|
| 1 | 11 |
| 11 | 11 |
| 13 | 13, 22 |
| 22 | 1, 11 |

All infinite paths eventually repeat one of two affine maps. At residue 11 the recurrent map is $(512u+17)/3$; at residue 13 it is $(32u+1)/3$. For a map $u'=(Au+B)/3$ we have
$$
 3\big((A-3)u'+B\big)=A\big((A-3)u+B\big).
$$
In each case $A$ is prime to three and $(A-3)u+B$ is a strictly positive integer. An infinite integral iteration would make it divisible by every power of three. This contradiction excludes every sufficiently large failed unit. Thus all sufficiently large odd parameters pass, and the earlier tripling theorem gives full convergence. This proves (2) implies (1).

## Restricting to the single binary class

For every positive $h$, $P(16h+1)$ is precisely the equality $J(9h)=J(18h)$, by the ordinary paths above, even without any assumption on $P$. Using $J(4v)=J(3v)$ on each side gives $P(1+48h)\Longleftrightarrow P(1+64h)$. Likewise $P(1+96h)\Longleftrightarrow P(1+128h)$. If (3) holds then both $1+48h$ and $1+96h$ pass for all sufficiently large $h$. Apply the two-successor identity at $9h$ for odd $h$. It gives $P(9h)$, establishing (2). Full convergence implies (3) directly. This completes the equivalence. The proof does not establish eventual merger on the remaining class.

## The count transfers without loss of exponent

Write $D(X)$ for all failed odd tripling parameters up to $X$, $D_9(X)$ for the failed odd multiples of 9 and $D_{64}(X)$ for failed parameters congruent to 1 modulo 64. There are absolute finite constants $C,C'$ such that for all $X\ge2$,
$$
 D(X)\le C D_9(C'X)\le C D_{64}(16C'X+1). \tag{1}
$$
The same estimates hold for an arbitrary fixed labeling invariant along actual steps. In a fixed-ratio interval $[R,bR]$ of initial failures all the charged failures occur in $[c_bR,C_bR]$ once $R$ is large. The two possible charged congruence classes in the last count can be restricted to $65\bmod128$ and $129\bmod256$.

To prove (1) we give the previous argument a uniform finite depth without any hypothesis about inputs outside its finite collection of tests. At any queried odd ternary unit $u$, we can establish $f(u)=f(9u)$ by testing a bounded list of odd multiples of 9. In the adjacent-word argument, choose $a\ge2$ such that $2^au\equiv1\pmod{27}$ and $3^au$ matches the appropriate binary seed. This uses a complete exponent period modulo 27 and at most 64 consecutive choices within that progression, since all seed moduli divide 512 and $3^{18}$ generates the 1 modulo 8 subgroup there. Thus $a$ has an absolute upper bound. The needed tests are at $(2^a u-1)/3$ and $3^j u$ for $2\le j<a$. They are positive odd multiples of 9. If they all pass, the calculation above gives $f(u)=f(3^au)=f(9u)$. In particular, at any such $u$ we can justify the paired-failure rule locally with this finite list.

Starting from a failed odd input $x$, stop if $9\mid x$. Otherwise start a paired trace at $u=x$ or $x/3$ and use this local rule whenever needed. A proposed failed $v=cu+1$ with $9\mid v$ is already an eligible charged input. On the auxiliary branch using $w=(8v-1)/3$, if $27\mid 8v-1$, test $w,3w$ directly. Otherwise the ternary-unit part requires at most two divisions by three. Apply the local paired rule there and test a multiple of 9 directly whenever one is needed. Thus each of the state exclusions in the finite table is valid if its finite list of high-multiple tests passes.

The further input for a bounded depth consists of two finite words near the recurrent rational fixed points. The [pivot certificates](THREE_RAY_PIVOT_WORDS.md) show that five consecutive traversals of either recurrent loop suffice to locate an intermediate $u$ for which $P(u)$ follows from a single comparison at an odd multiple of 9. In detail, at each loop the difference from its fixed point is multiplied by $A/3$ with $16\mid A$ and $3\nmid A$. After one iteration the binary congruence of its certificate holds, and four more integral iterations force the needed ternary congruence already at that intermediate vertex. Its two failed arms then contradict the certificate unless the indicated high-multiple test fails.

The finite ternary graph contains no other directed cycles, since any vertex on a cycle survives deletion of dead ends. A path avoiding five repetitions of either loop therefore has bounded length (at most 18 distinct vertices and four extra repetitions at each of two vertices). The first two individual steps, and the bounded runs without division before and between returns, add only a constant. Consequently every failed $x$ charges a failed odd multiple of 9 at one of a **fixed finite list** of positive-slope rational affine functions of $x$, using only forms integral on the branches where they are applied. This finiteness includes the bounded exponent choice and the finitely many pivot words. Each fixed affine function is injective and all its used values are positive and $O(X)$ for $x\le X$. The union bound proves the first inequality and the asserted fixed-ratio localization. For the second inequality, a failing $x=9h$ with $h$ odd forces a failure at $1+64h$ or $1+128h$ by the final binary-class argument above. These two maps are injective and their images have different binary valuations of the offset from 1.

It follows that a counterexample would force at least $cX^{0.84}$ failed odd multiples of 9 at arbitrarily large cutoffs, and at least $c'X^{0.164}$ at every sufficiently large cutoff; the same two assertions hold within the indicated binary classes collectively. Here the finite transfer is elementary. The exponents are supplied by the preceding [dyadic-limit and predecessor argument](THREE_RAY_DENSITY.md) and the [every-scale estimate](THREE_RAY_VARIATION.md).
