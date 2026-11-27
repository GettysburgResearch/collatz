# The clock gcd as a denominator order in narrow rational cycles

Consider any positive reduced rational Collatz cycle with least odd period $P$. Write its odd phases as $N_i/d$, where the $N_i$ are distinct positive odd integers, $(N_i,d)=1$, and $2^{e_i}N_{i+1}=3N_i+d$ with $e_i\ge1$. Its reduced denominator is constant and prime to $6$. This also follows from the usual cyclic affine formula with denominator $2^A-3^P$, where $A=\sum e_i$. Put $g=(A,P)$, $q=P/g$, $a=A/g$, and
$$
\omega=3^q2^{-a}\pmod d,\qquad k=\operatorname{ord}_d(\omega),
$$
with $k=1$ at $d=1$. Always $k\mid g$. The following sufficient conditions each give the exact equality $k=g$.

1. The canonical integer height of the cycle is at most two. This includes real discrepancy width strictly below three.
2. The largest odd phase is at most eight times the smallest odd phase, with no assumption on canonical height.

Consequently $g$ divides the exponent of the unit group modulo $d$. In particular, at $d>1$, $g\le\varphi(d)<d$. With $d=1$ these conditions force coprime clocks. More generally, every cycle with $k<g$, at any height and with any positive valuations, has an actual affine resonant pair in each of the $g/k-1$ nonzero chronological lag classes $h\in qk\mathbb Z/P\mathbb Z$ (allowing either orientation of the pair). Its physical phases have the form
$$
y=2^t x+j,\qquad t\ge3,\quad j>0\text{ odd integer},\qquad 3j<2^t-1.
$$
There are at least $g/k-1$ unordered actual inversion occurrences across all the lifted fibres. In particular at least this many physical pairs meet the displayed condition, counting each chronological pair once. In canonical height three the only possibilities are $t=3,j=1$.

## Proof

Rotate to a maximum of $D_i=E_i-iA/P$, where $E_i=\sum_{j<i}e_j$. Put $z_i=\lfloor iA/P\rfloor-E_i\ge0$, $H=\max z_i$, and $m_i=\lfloor(i+1)A/P\rfloor-\lfloor iA/P\rfloor$. Then $z_i$ is periodic, $m_i$ has period $q$, and every $q$ consecutive mechanical exponents sum to $a$. Define
$$
 L_i=2^{H-z_i}N_i,\qquad \ell(L_i)=2^{H-z_i},\qquad F_d(L)=3L+d\,\ell(L).
$$
Here $\ell(L)$ is the largest power of two dividing $L$. The exact recurrence is $2^{m_i}L_{i+1}=F_d(L_i)$. All $L_i$ are distinct because their odd parts are the distinct original $N_i$. Iteration modulo $d$ gives $L_{i+q}\equiv\omega L_i$ and $L_{i+P}=L_i$ is a unit, so $\omega^g=1$.

Fix a nonzero lag $h$ divisible by $qk$. At each date $L_i,L_{i+h}$ share their mechanical phase and residue modulo $d$. The nonzero cyclic differences $L_{i+h}-L_i$ sum to zero. Hence their sign reverses at least twice. At a reversal name the smaller scaled state $U=2^r N$ and the larger $V=2^s N'$. Strict reversal means $F_d(V)<F_d(U)$, since both next scaled states divide by the same $2^{m_i}$. Equality would give identical next scaled states. Necessarily $r>s$. With $t=r-s$, positivity of $V-U$ gives $N'-2^tN>0$. The common residue and invertibility of $2^s$ modulo $d$ imply $N'-2^tN=dj$ for a positive odd integer $j$. The reversal inequality is now precisely $3j<2^t-1$, which forces $t\ge3$. Dividing by $d$ gives the claimed physical pair. The two reversals for each $h$ give at least $2(g/k-1)$ ordered occurrences; a fixed unordered pair contributes exactly twice across signed lags, including an antipodal lag. This proves the lower count. Since $t\le H$ and $y>8x$, both sufficient criteria follow. The proof also works when the cycle has only one phase, where the conclusion is immediate.

## Exact controls and scope

The independent Python certificate generates 42,336 primitive positive necklaces across its declared binary, ternary and quaternary period ranges. It constructs the reduced cycle by integer arithmetic, reconstructs each actual valuation, computes the modular order, and checks every pair in every residue fibre. There are 13,462 nontrivial exact-order examples and one actual strict-order-divisor example. The cycle with word $(1,3)$ has odd phases $5/7,11/7$, $g=k=2$. The eight-phase word $(1,1,1,1,4,2,2,2)$ has $H=3$, $d=893$, physical band below eight, and $g=k=2$. For $(1,1,2,4,3,4,1,2)$ the denominator is $431$ and $g=2,k=1$. A reversal uses $1279/431=16(53/431)+1$. Thus a denominator-order identity on unrestricted rational cycles is false. Finite checks support the formulas and do not establish them.

Paper 114 proves the ordinary canonical-height-two clock coprimality and the height-three pair $y=8x+1$. Weaver's Post 65 comment explicitly derives, for the ordinary problem, the necessary unrestricted near-dyadic pair for failure of a canonical-root order property. Its order argument also gives ordinary coprimality and phase ordering on a physical band at most eight. The contribution recorded here is the full reduced-denominator order, the corresponding constrained lag classes, and their actual reversal count. No exclusion of a nontrivial integer Collatz cycle, and no unrestricted finiteness, follows. [Paper 114](https://rstation.ai/problems/collatz/papers/114/v1) · [Post 65, including the unrestricted ordinary inversion statement](https://rstation.ai/r/collatz/posts/65#comment-M-8gx_Y9x5tMrj8M)
