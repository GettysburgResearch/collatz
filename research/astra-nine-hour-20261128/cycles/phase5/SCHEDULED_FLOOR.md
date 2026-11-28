# A scheduled floor test and its exact physical inverse

Let a primitive positive rational shortcut cycle have length $n$, $u$ odd steps, $v=n-u$, $D=2^n-3^u>0$, and $\gcd(n,u)=1$. Write $S\subset\mathbb N$ for its normalized Apéry semimodule, with $0\in S$ and $S+u,S+v\subset S$. In each residue class $0\le j<u$ its holes are exactly
$$ j,j+u,\ldots,j+(L_j-1)u . $$
In particular $L_0=0$. Write $c=1+\max(\mathbb N\setminus S)$, taking $c=0$ for the empty hole set. The points $j+uL_j$ are precisely the minimal $+u$ rays. Their translates $v+j+uL_j$ are the normalized physical heights of the odd dates. Thus the spread of the odd heights, divided by $u$ and rounded down, is $W=\max L_j$. The condition $W\le1$ is equivalent to $c\le u$. The latter is an additional restriction. The physical conductor formula makes it roughly a bound of six on the full maximum-to-minimum ratio at the critical slope. [Phase two, full semimodule dictionary](../phase2/SEMIGROUP_BOUNDARY.md) · [Phase three, physical conductor](../phase3/PHYSICAL_CONDUCTOR.md)

### The quotient coefficients

Put $R=\mathbb Z[t]/(t^u-2)$, $[u]_t=1+t+\cdots+t^{u-1}$, $H(t)=\sum_{h\notin S}t^h$, and $J=1+(t-1)H$. In $R$, $[u]_t(t-1)=1$, so
$$ [u]_t J=[u]_t+H=\sum_{j=0}^{u-1}2^{L_j}t^j=P(t). $$
Evaluation gives $R/(t^n-3)\cong\mathbb Z/D$. Indeed $2^n=3^u$ and $D$ is odd and coprime to three, so both 2 and 3 are invertible in the quotient. For $au+bn=1$ we get $t=2^a3^b$ there. Conversely $2^a3^b$ taken modulo $D$ satisfies both defining relations. The full native denominator equals the additive order of $P$ in this quotient by the physical boundary identity. Thus an ordinary cycle is equivalent to integral coefficients for the unique rational solution
$$ (t^n-3)\sum_{j=0}^{u-1} k_jt^j=P(t)\quad\text{in }R\otimes\mathbb Q. $$
The uniqueness is also immediate from the determinant $\pm D$. These order and boundary representations extend the rank-$u$ order in PR188. The independent semimodule formula and two torsion-coordinate evaluations in concurrent PR213 give another all-gcd denominator proof. [PR188, beed685ab713923191ae40c9559bf7400298d2d3, RESIDUE_NORM.md](https://github.com/GettysburgResearch/collatz/blob/beed685ab713923191ae40c9559bf7400298d2d3/research/scalar-carry-cocycle-20261124/RESIDUE_NORM.md) · [PR213, ca48af42546268771e34297872783631f61e8f02, cycles/SEMIMODULE_DENOMINATOR.md](https://github.com/GettysburgResearch/collatz/blob/ca48af42546268771e34297872783631f61e8f02/research/astra-global-rigidity-20261128/cycles/SEMIMODULE_DENOMINATOR.md)

The schedule visits each index once. Set $j'=(j+n)\bmod u$, $d_j=\lfloor(j+n)/u\rfloor$, and $e_j=d_j+L_j-L_{j'}$. Closure under $+v$ gives $L_{j'}\le L_j+d_j-1$, hence $e_j\ge1$. Matching quotient coefficients gives
$$ 2^{d_j}k_j-3 k_{j'}=2^{L_{j'}}.\tag{1} $$
Every $k_j$ is positive. Unroll (1) around the whole rotation, whose multiplier is $X=2^n/3^u>1$ and whose additive terms are strictly negative. For integral coefficients one has $2^{L_j}\mid k_j$ at every index. To see this directly, suppose the minimum $b$ of $v_2(k_j)-L_j$ were negative. At an index $j'$ attaining it the summands $3k_{j'}$ and $2^{L_{j'}}$ on the right of (1) have distinct valuations. Their sum gives $v_2(k_j)-L_j=b-e_j<b$, impossible. Now $y_j=k_j/2^{L_j}$ solves
$$ 3y_{j'}+1=2^{e_j}y_j.\tag{2} $$
All $y_j$ are odd by reduction modulo two. This is the physical odd cycle read backwards. Indeed the odd date of height $v+j'+uL_{j'}$ goes to height $v+j+uL_j$ after $e_j$ shortcut steps because $j+n=j'+ud_j$. The $n$ clock and the exact native word are recovered by inserting the corresponding even stretches. For rational $k_j$, first multiply (1) by their common denominator $q$, coprime to 6 because it divides $D$. The same valuation argument and (2) recover all odd numerators with affine constant $q$. [BalancedCarry.lean](BalancedCarry.lean)

### The binary-level case

If $W\le1$, equation (1) becomes
$$ k_{j'}=\left\lfloor 2^{d_j}k_j/3\right\rfloor,\qquad
   r_{j'}=2^{d_j}k_j\bmod3\in\{1,2\}.\tag{3} $$
Conversely, a positive integral periodic floor path (3) represents an ordinary cycle if its labels describe a legal normalized semimodule. Explicitly $r_0=1$ and the hole set $B=\{j:r_j=2\}\subset[0,u)$ must have $h-v\in B$ whenever $h\in B$ and $h\ge v$. This is exactly closure of its complement under $+u,+v$. In particular $r_j=1$ at $j\ge c$; either value may occur at $j<c$. The recovered coefficients avoid multiples of three and four. Higher levels permit several powers of two with the same ternary remainder, so (3) only covers $W\le1$.

The search at a fixed coprime type is effective. Along any segment of $h\le u$ successive indices the product of its multipliers is
$$ 2^{\lfloor(j+hn)/u\rfloor}/3^h=X^{h/u}2^{(j-j_h)/u}\in[1/2,2X]. $$
Here $j_h=(j+hn)\bmod u$. Unrolling (3) yields
$$ \frac{u}{6(X-1)}\le k_j\le\frac{4Xu}{3(X-1)}=\frac{4u2^n}{3D}. $$
At the critical slope this bound is polynomial in $n$ by the lower bound for the linear form in two logarithms. It provides no uniform exclusion over all types. Earlier height-one computations verify individual convergent rungs in different coordinates. [Wren, rStation paper 119](https://rstation.ai/problems/collatz/papers/119/v3) · [Voyager, rStation paper 123](https://rstation.ai/problems/collatz/papers/123/v1)

The exact control below compares every reconstructed odd phase with its independent affine numerator. It also tests whether periodicity and the two nonzero digits force the normalization conditions. Among 54,065 candidate initial coefficients at coprime types with $3/2<n/u<2$, $D>0$ and $n\le120$, the three positive all-nonzero-digit solutions have $(n,u,k_0)=(5,3,13),(8,5,61),(8,5,70)$. All fail downward closure. A separate $(2,1)$ anchor with $k_0=2$ gives a downward-closed hole set containing zero, whereas $k_0=1$ recovers the true ordinary anchor. Both legality conditions therefore matter. The control also recovers every odd phase of 1,068 positive coprime necklaces through length fourteen, including 295 of height at most one. [scheduled_floor_controls.py](scheduled_floor_controls.py)
