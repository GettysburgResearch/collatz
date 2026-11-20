# A single residue class suffices for Collatz

**PROPOSED, unconditional.** Use the ordinary positive shortcut map and let $P(x)$ mean that $x$ and $3x$ have a common future iterate at independent clocks. The following are equivalent.

1. Every positive integer reaches 1.
2. $P(x)$ holds for all sufficiently large positive $x\equiv1\pmod{16}$.
3. $P(x)$ holds for all sufficiently large positive $x$ with $v_2(x-1)\in\{4,5\}$.
4. $P(x)$ holds for all sufficiently large positive $x\equiv1\pmod{16}$ with $3\nmid x-1$.

A failed test will be called a defect. A counterexample to Collatz would therefore force unbounded genuine defects in each of the indicated sets. We prove these equivalences by an ordinary integer argument in which the number of comparisons depends on a ternary valuation.

## The comparisons used by a defect

Write $f(n)$ for the ordinary merger component, $g(y)=f(y-1)$, and $J(y)=f(y+1)$. We use $f(2u)=f(u)$, $g(2u)=g(3u)$ and $J(4u)=J(3u)$, all ordinary identities. Two comparisons in the [window proof](THREE_RAY_WINDOWS.md) give the following explicit rules.

- A defect divisible by 3 at an odd $x$ forces a defect at $16x/3+1$ or $32x/3+1$. Indeed, $J(9s)=J(12s)=J(16s)$, and the ordinary paths from $3(16s+1)$ and $18s+1$ meet. Thus $J(9s)=J(18s)$ if $P(16s+1)$. Applying this at $s=x/3,2x/3$ connects $J(3x)$ to $J(12x)=J(9x)$, the two labels of interest.
- For an odd ternary unit $x>1$, choose $L=2$ if $x\equiv1\pmod3$ and $L=3$ if $x\equiv2\pmod3$. Put $z=(2^Lx-1)/3$. Then $z$ is odd with $x<z<3x$. If $P(z)$, its ordinary odd step yields $f(x)=f(z)=f(3z)=g(3^Lx)$. Also $g(9x)=g(27x)$ when $P(8x-1)$, by $g(4x)=g(9x)$, $g(8x)=g(27x)$ and $T(3(8x-1))=4(9x-1)$.

Suppose all sufficiently large tests at $1\bmod16$ pass, and choose a threshold $N\ge2$ above which this holds. Every odd multiple of three exceeding $N$ passes by the first rule. For any odd $x>N$, all the tests $P(3^k x)$ for $k\ge1$ consequently pass. When $x\equiv 7,9,13\pmod{16}$ take $j=3,3,2$, respectively. Then $Y=3^jx$ is $5\bmod8$, $3\bmod16$, or $5\bmod8$, respectively. In these two successful classes $g(Y)=f(Y)$ by the explicit three- and four-step paths in the window proof. The passed tests at multiples of three give $f(Y)=f(3x)$. Thus, for these three residues, a defect at $x$ forces a defect at $z$, or at $8x-1$ if $L\ne j$. No comparison at $8x-1$ is needed when $L=j$.

## Two ternary valuations rule out infinite paths

First take $x\equiv13\pmod{16}$ above $N$. If $x\equiv1\pmod3$ then $L=j=2$ and $z=(4x-1)/3\equiv1\pmod{16}$, so $x$ passes. If $x\equiv2\pmod3$, then $8x-1$ is divisible by three. A defect at $x$ would therefore force another at $z=(8x-1)/3\equiv13\pmod{16}$. This new input exceeds $x$ and satisfies
$$
  5z-1=8(5x-1)/3.
$$
Each forced repetition reduces $v_3(5x-1)$ by one. The integer $5x-1$ is positive, so this cannot repeat indefinitely. The only other ternary cases pass. This rules out defects at $13\bmod16$ above $N$.

Next take $x\equiv7\pmod{16}$. The comparison $P(8x-1)$ always holds here: $8x-1\equiv23\pmod{32}$. At the base parameters $23$ and $69=3\cdot23$, the two paths end at 20 after five steps, with three and two odd inputs respectively. Adding $32t$ to the first input and $96t$ to the second adds the same $27t$ to the common endpoint. A defect at such $x$ therefore forces a defect at $z$, since the other possible test passes.

Finally take $x\equiv9\pmod{16}$. If $x\equiv2\pmod3$ then $L=j=3$ and $z\equiv13\pmod{16}$, which is settled. If $x\equiv1\pmod3$, its candidate $z\equiv1\pmod{16}$ passes. The only possible successor is $w=8x-1\equiv7\pmod{16}$ with $w\equiv1\pmod3$. The preceding paragraph at $w$ forces a defect at
$$
  x'=(4w-1)/3=(32x-5)/3\equiv9\pmod{16},
  \qquad 29x'-5=32(29x-5)/3 .
$$
This time the strictly decreasing nonnegative valuation is $v_3(29x-5)$. Thus there are no defects above $N$ in class 9. This also disposes of class 7, since its only ternary-unit successor $z$ is 9 or 13 modulo 16.

The full window proof supplies, for **any** odd ternary unit defect, a larger defect among $z,8x-1,24x-1,3x,9x,27x$. The first is 1, 9 or 13 modulo 16; the next two are 7 modulo 16, and the final three are multiples of three. All have just been excluded for $x>N$. Hence every sufficiently large odd input passes. The [eventual tripling criterion](THREE_RAY.md) proves full convergence. The converse follows from the common visit to 1.

## Choosing one representative above 1

For $x\equiv1\pmod{16}$ with $x\equiv1\pmod3$, put $z=(4x-1)/3$. Then $z\equiv1\pmod{16}$ and
$$
 f(z)=f(x),\qquad f(3z)=g(4x)=g(6x)=f(6x)=f(3x).
$$
The step from $z$ proves the first identity. The middle equality $g(6x)=f(6x)$ holds since $x=16m+1$ makes $6x-1=96m+5$ and $6x=96m+6$ meet after five steps at $27m+2$. Thus $P(x)$ and $P(z)$ are equivalent unconditionally.

For $x>1$ in the class write $x-1=2^a3^b u$ with $a\ge4$ and $\gcd(u,6)=1$. The comparison just proved connects *every* pair of neighboring representations $1+2^{a+2}3^{b-1}u$ and $1+2^a3^b u$ for $b\ge1$. All have the same truth value of $P$. The orbit of this relation has an upper endpoint at $b=0$ and a lower endpoint at $a=4$ or $5$. Either supplies a complete representative set. For the statements about eventual validity, only finitely many inputs lie in the same orbit as any bounded set of representatives: $a+2b$ and $u$ are fixed throughout a finite orbit. Therefore either eventual test on the chosen representative set implies eventual validity for the whole class $1\bmod16$. This gives statements 3 and 4. The test at $x=1$ itself holds by direct iteration.

## The reduction has bounded multiplicity and linear size

Let $D(X)$ count all odd defects up to $X$, and $D_1(X)$ only those in $1\bmod16$. There are absolute constants $C,C'$ such that
$$
                       D(X)\le C D_1(C'X) .
$$
This stronger statement requires additional finite certificates. The valuation argument above by itself does not give bounded multiplicity or linear size.

While the class-9 loop repeats, its map $A(x)=(32x-5)/3$ fixes $5/29$, and $29A(x)-5=32(29x-5)/3$. Seven repetitions give $29A^7(x)\equiv5\pmod{2^{35}}$. Every integer in this cylinder passes $P$ intrinsically. To check this, extend the ordinary parity words to rationals with denominator 29 by using the parity of the numerator. For the starts $5/29$ and $15/29$, their numerators both reach 22 in 35 steps under the word recurrence $s\mapsto s/2$ on even $s$ and $s\mapsto(3s+29)/2$ on odd $s$. Their odd counts are 19 and 18. For ordinary $w$ in the stated cylinder the first 35 parities on both arms agree with these rational words, by divisibility of $29w-5$ by $2^{35}$. The two affine images at clock 35 have the same slope in $w$, since $3^{19}=3\cdot3^{18}$. They agree at $w=5/29$, hence identically. A path of true class-9 defects cannot contain seven consecutive repetitions.

In class 13 the condition $16\mid5x-1$ holds already. If $27\mid5x-1$, then $x=432t+173$ for an integer $t\ge0$. The following path of ordinary edges and divisions by three joins $x$ to $3x$:
```
DDDDDDDDIIVOEOEOOEOEODDIIVOEOEEI
```
Here $D$ doubles, $I$ takes the odd preimage $(2m-1)/3$, and $O,E$ take the odd and even ordinary steps. Each $V$ divides by three and requires $P$ at the quotient. Propagating the affine coefficients in $t$ gives the two quotients $16384t+6561$ and $6912t+2769$, both $1\bmod16$. The final value is $1296t+519=3x$. The parity and divisibility checks hold on the entire progression. In particular a defect here would force a defect at one of these two parameters. If instead $27\nmid5x-1$, the valuation already bounds the number of class-13 self-transitions by two.

To count without assuming that any classes pass, trace the failed tests in the proof. Whenever a failed multiple of three appears, it immediately gives a failed $1\bmod16$ input by the two native comparisons above. The other initial successors are $1,7,9,13\bmod16$. In class 7 the only possible ternary-unit successor left is $z$ in class 9 or 13. In class 9 a self-transition uses two edges, through class 7, and the only other ternary-unit exits are into 1 or 13. There are fewer than seven self-transitions by the 35-step certificate. In class 13, either the displayed word leads to a failed $1\bmod16$ input, or at most two self-transitions precede an exit. Thus every defect leads to a failed target through a bounded number of choices from a fixed finite list of affine maps of strictly positive slope. The quotients in the displayed word may be regarded as affine functions of $x$ on its stated progression. All the target maps are injective on their domains, and take positive inputs $x\le X$ to values $O(X)$. There are only finitely many compositions of bounded length. Summing their target counts proves the inequality also at the smallest inputs.

In particular a counterexample would force $D_1(X)\gg X^{0.164}$ at every sufficiently large cutoff and $D_1(X)\ge cX^{0.84}$ at arbitrarily large cutoffs. The same argument applies to labels of any partition into unions of ordinary components. [Global counting bounds](THREE_RAY_DENSITY.md) · [Finite certificate replay](check_three_rays.py)
