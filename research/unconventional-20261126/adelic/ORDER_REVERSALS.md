# Exactly which fixed-clock, fixed-grade classes preserve integer order?

**Status.** Proposed theorem for all positive integer inputs, with complete proof and finite checks. It extends the synchronized-switch cycle exclusion, identifies its sharp uniform cutoff, and exhibits unbounded sequences of genuine order reversals in the known basin. A general positive cycle remains subject to the full determinant divisibility.

Let $T$ be the shortcut map. Say the class $(p,r)$ is order preserving when $T^{p+r}x\le T^{p+r}y$ for all positive integers $x<y$ whose respective scripts have exactly $p$ odd and $r$ even departures. Equality is allowed. Two different phases on a single cycle can never merge at the same time, so on them this is strict.

**Theorem O.** A class admits an order reversal if and only if
\[
           (p\ge2\text{ and }r\ge4)\quad\text{or}\quad
           (p\ge5\text{ and }r\ge3).                                  \tag{1}
\]
In particular all classes through clock five preserve order. Clock six first fails at grade two. The result includes all arbitrarily long words with at most two even letters.

## Proof for the order-preserving classes

Write $h=p+r$. At grade zero there is only one increasing branch. At grade one the carry in $2^hT^h x=3x+A$ is a power of two at most $2^{h-1}$. A reversal between distinct integer endpoints would cost a difference of at least $2^h$ after clearing the clock, which is impossible. For $r=0$ there is again a single branch.

For the remaining arguments use the shifted coordinate $x+1$. An odd step acts on this coordinate by $3/2$ and an even step acts by $z\mapsto(z+1)/2$. Thus
\[
 T^h x+1=\frac{3^p}{2^h}\bigl(x+1+H(w)\bigr),\qquad
 H(w)=\sum_{i=1}^r 2^{i-1}(2/3)^{q_i},                                \tag{2}
\]
where $q_i$ is the number of odds strictly before the $i$th even. In particular $0<H(w)\le2^r-1$ for $r>0$. This proves the one-even row. For $r=2$ it also rules out reversal at differences at least three. At difference two, a common odd first step makes the difference three; a common even first step reduces to the one-even row. It remains to check $y=x+1$.

If $x$ is odd and $x\equiv3\pmod4$, then $y$ starts with both its even steps and $H(w_y)=3$. If $x\equiv1\pmod4$ then $H(w_x)\le2$ since both of its evens follow at least one odd, whereas $H(w_y)\ge1$. Either case excludes a reversal by (2). Suppose now that $x$ is even. Write $x/2+1=2^k u$ with $u$ odd. After $k+1$ steps the two states are $v=3^ku-1$ and $3v+2$. The smaller input first used an even followed by $k$ odds, and the larger used $k+1$ odds. These prefixes occur inside the two scripts because the smaller has another even departure and the larger has two. Thus $p\ge k+1$. Both current states are even. After their common even departure the states are $b=v/2$ and $3b+1$. The smaller trajectory has used both even steps and has at least one odd step left, so $b$ is odd. The next step sends both to $(3b+1)/2$. A reversal is impossible.

For $r=3$, only $p=2,3,4$ remain for the claimed positive result. For each pair enumerate $0\le x<2^h$ at the stated grade. A lift $x+2^ht$ has endpoint $T^hx+3^pt$. Therefore it suffices to check the consecutive endpoint differences in residue order **including the wrap**, where the repeated first endpoint is increased by $3^p$. The respective numbers of residues are $10,20,35$, and the minima of these integer differences are $0,0,0$ (maxima $3,4,15$). A complete check uses only the single-step rule and the indicated ranges. At arbitrary fixed $h$ this same finite sorted-residue and wrap test is necessary and sufficient for *any subset* of words of a given grade.

## Producing every remaining reversal

The six-step grade-two inputs $48,49$ have words `000011`, `101000` and endpoints $8,7$. The eight-step grade-five inputs $248,249$ have words `00011111`, `10110110` and endpoints $242,238$. Both smaller inputs are divisible by four. Prepending common even steps to the two inputs (multiplying both by a power of two) adds any desired number of even letters and keeps the endpoint reversal.

There is also an insertion which adds any desired number of *odd* letters to each script while leaving the endpoint difference unchanged. Let the seed inputs be $a,a+1$ with $4\mid a$, of length $h$ and common grade $p$. After their first step the states are $t_0=a/2$ and $3t_0+2$. Fix $k\ge0$. Start instead at $x=2^{k+1}u-2$ and $x+1$, choosing large odd $u$ with
\[
                       3^ku-1\equiv t_0\pmod{2^{h-1}}.
\]
The smaller input first takes one even and $k$ odd steps, while the larger takes $k+1$ odd steps. The resulting states are $t=3^ku-1=t_0+2^{h-1}v$ and $3t+2$. The remaining $h-1$ parity digits of each seed are then genuine. Their two final outputs are the corresponding old outputs plus the *same* $3^p v$, because the two remaining grades are $p$ and $p-1$, and the second input lift is $3\cdot2^{h-1}v$. This proves the insertion. Applying it to each stated seed, and prepending extra evens when needed, proves all of (1).

## What a synchronized comparison can eliminate

If every position in a repeated macro has a fixed duration and fixed grade falling outside (1), its alternatives may be *arbitrary* words in that whole grade class. Composing the order-preserving maps on the marked cycle phases makes the macro advance increasing. An increasing permutation of a finite ordered set is the identity. This extends the [synchronized 01/10 argument](../AlignedCycles.lean) to an exact library of entire grade classes.

Two limitations are structural. First, in any finite family of alternatives including two different slopes, a uniform increasing map on all its positive integer cylinders is impossible. Each word accepts a residue modulo a power of two. Place the word of larger slope at the smaller of two positive inputs and the other word at a larger input a fixed distance away. Translating both by common multiples of the largest dyadic modulus preserves both words, and their different endpoint slopes reverse the ordering for all sufficiently large lifts. Equal slopes under the shortcut branches require both equal clock and equal grade by unique factorization.

Second, let an ordinary primitive cycle have clock $n$ and odd grade $P$. Suppose a common clock-$h$, grade-$p$ macro advances the marked phases in one orbit of the $h$-step permutation. There are $n/\gcd(n,h)$ such phases. Concatenating their macros travels around the native cycle $h/\gcd(n,h)$ times. Consequently $np=hP$. If $\gcd(n,P)=1$, then $n\mid h$ and that macro already fixes the phase. This obstruction holds regardless of the strength of any order theorem at fixed grade. It applies also to the true clock-two grade-one cycle. Variable-duration alternatives do not circumvent the preceding different-slope obstruction to a *universal* comparison. These statements leave open comparisons exploiting additional arithmetic relations between a particular cycle's phases.

## Arbitrarily many nearcritical reversals inside the ordinary basin of one

The first seed and its insertion give, for every $p\ge2$, a clock-$p+4$ pair of words realized on adjacent integers that maps them to adjacent integers in *reverse order*. For one such pair fix its smaller starting residue $a\pmod{2^{p+4}}$. Increasing the source by $2^{p+4}$ shifts the smaller terminal state by the odd number $3^p$. Thus after reading any finite list of these gadgets, the sorted output pair is $z,z+1$, and increasing the original smaller start by $2^H$ shifts $z$ by $3^P$, where $H,P$ are the total clock and grade. As $3^P$ is invertible at two, the next prescribed gadget's smaller input residue may always be imposed. Induction gives a single arithmetic progression of positive *genuine* initial pairs realizing the full list, with one reversal at each boundary.

Every such list has arbitrarily large realizations in the basin of one. Impose $z\equiv12\pmod8$ by another lift. The three-step paths from $12,13$ are $(12,6,3,5)$ and $(13,20,10,5)$, each with one odd departure. After the lift the two actual paths therefore meet at a common $c$, a unit modulo three. Increasing the original source by $8\cdot2^H$ shifts that common state by $3^{P+1}$. Since two generates the units modulo $3^{P+1}$, we may take the common state to be $2^m$ for arbitrarily large $m$. Such actual pairs follow all the reversals, counted-merge, and then reach one. Before the appended fusion segment the two states at any common time are distinct, since a merger would force them to stay equal at the next gadget boundary. Across distinct times their slopes in the original lifting parameter differ by unique factorization; finitely many accidental equalities are avoided by taking a sufficiently large admissible $m$. Hence all physical states of the two finite prefixes at times $0,\ldots,H$ can be required distinct and at arbitrarily large positive heights, with their genuine integral spacing.

For a nearcritical schedule use $p_j\in\{6,7\}$ with $\sum_{j<l}p_j=\lfloor lq\rfloor$, $q=4/(\log_2 3-1)\in(6,7)$. The prefix binary logarithm of the multiplicative coefficient at each boundary is $(\log_2 3-1)(\lfloor lq\rfloor-lq)$, bounded independently of $l$; inside a gadget the clock is at most eleven. The lists may be arbitrarily long and have an odd number of reversals. The real homogeneous drift remains bounded throughout these actual finite scripts. Their ultimate fusion is an arithmetic realization and supplies no positive nontrivial cycle.

## The full determinant at a proposed two-phase closure

For any concatenation with an odd number of reversals write $Q=2^H$, $A=3^P$. Let the smaller member of an accepted starting pair be $a$ and its smaller terminal member be $b$. Let the word followed by the smaller starting member have carry $C_0$, and the word followed by the larger have carry $C_1$. Exact reversal into an adjacent pair says
\[
 Aa+C_0=Q(b+1),\qquad A(a+1)+C_1=Qb,
 \qquad C_0-C_1=Q+A.
\]
Closing the two paths into a cycle would swap the two marked phases. The repeated clock is $2H$ and its **full** determinant is $Q^2-A^2$. Its two-word carry is
\[
              A C_0+Q C_1=(Q+A)(C_0-Q).
\]
Thus the entire factor $Q+A$ cancels identically. The rational lower fixed phase is $x=(C_0-Q)/(Q-A)$, and a positive integral closure of these particular words occurs exactly when $Q-A\mid b-a$ and this $x$ is positive. Indeed $C_0-Q=Qb-Aa$ and $\gcd(Q,Q-A)=1$. If this is an integer it lies in the original residue $a\pmod Q$ by the fixed equation, so both actual scripts are genuinely realized. The factor $Q-A$ remains after all local reversals. Removing it in one family would still not cover the coprime grade-clock sector above. This is the precise residual obstruction to this order argument.
