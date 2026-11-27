# A nineteen-odd-step path excludes the entire joint construction from a least bad basin

**PROPOSED ordinary exclusion, with a Lean proof of the physical merger.** For every positive odd integer
$$
                s\equiv187605073\pmod{3^{19}},
$$
there exists a positive multiple of three $y<2s+1$ such that $T^{30}(y)=T(s)$ for the ordinary shortcut map. In particular $s$ cannot belong to a bad component when every smaller multiple of three below $2s+1$ is good. This applies to the bounded least-disagreement branch. It excludes the distinguished ternary past of the **entire** rational family in [JOINT.md](JOINT.md) once the full least-basin requirement is imposed. It does not exclude other pasts.

Read the inverse odd exponents from $T(s)$ in order:
$$
 (3,3,2,1,3,4,1,1,2,1,1,1,1,1,1,1,1,1,1).
$$
Their sum is 30. The cumulative reverse carry starts at $C_0=0$ and obeys $C_{j+1}=2^{a_{j+1}}C_j+3^j$. It ends at $C_{19}=1467890651$. Hence the source of this path is
$$
 y=\frac{2^{30}T(s)-1467890651}{3^{19}}
   =\frac{2^{29}s-310339913}{3^{18}}.
$$
The specified residue is exactly the class making this $y$ a multiple of three. For an ordinary odd $s$ write $s=187605073+2\cdot3^{19}t$, $t\ge0$. Then $y=259975167+3\cdot2^{30}t$. The base point $y=259975167$ has chronological shortcut parities
`111111111110111000100110100100`, with 19 odd inputs, and ends at 281407610. An increment $2^kz$ at the start preserves a length-$k$ parity word and increments the endpoint by $3^u z$ for that word's odd count $u$. Apply it with $k=30$, $u=19$ and $z=3t$ to obtain the actual common endpoint for the entire progression. The displayed affine expression for $y$ is positive and strictly below $2s+1$. The base endpoint is even. Taking $t=1$ gives $s=2512128007$, $y=3481200639$, and the common endpoint is an odd successor. [NineteenMerger.lean](NineteenMerger.lean) proves the parity lift and the physical whole-residue conclusion for ordinary naturals, through `run 30 y = step s`.

**Why this kills the constructed model.** At each sufficiently large clock in the joint family, the 19 chronological gaps immediately before its distinguished minimum are
$$
 (2,2,1,2,1,2,1,2,2,1,2,1,2,2,1,2,2,2,2).
$$
This follows directly from the fixed anchor, its protected neighborhood and the wraps of $i\log_2 3$ for $-19\le i\le-1$. Iterating $x\mapsto(3x+1)2^{-a}\pmod {3^{19}}$ from zero along this list gives the terminal residue 187605073. The rational phases are integral at 3, so the same residue and all the reverse divisions hold in their common denominator lattice. Their first gap from $s$ is one. Their physical minimum grows, and the affine source above is positive, ternary-divisible and smaller than $2s+1$. Thus the bounded-depth examples fail a concrete additional condition of the genuine least bad basin. The rational path is obtained by the affine equations and local divisibilities; the Lean theorem is about ordinary integer sources.

The previous PR195 certificate at depth 16 at $s$ selects $s\equiv116582680\pmod{3^{17}}$. Here the new class reduces to $58464910\pmod{3^{17}}$. The deeper word ends at $T(s)$, allowing both the ternary class and a distinct merger to be identified. [PR195 frozen shallow-ancestor proof](https://github.com/GettysburgResearch/collatz/blob/5b2bdcb6e4e60da15c29eadff8bd08b3991c5b57/research/astra-global-closure-20261124/round9/critical/SHALLOW_ANCESTORS.md)

## Attempt to cover the other minimum pasts

The new merger does not cover the mechanical two-sided minimum pattern. Write $B_i=\lfloor i\log_2 3\rfloor$ for all integer $i$ and take reference gaps $b_i=B_{i+1}-B_i$ around time zero. For every fixed finite past and future, positive odd ordinary $s$ can be chosen arbitrarily large in the simultaneous cylinders. The past prescribes one residue modulo $3^v$ for $v$ past odd gaps. For a future word of total $A$, its exact odd valuations prescribe an odd dyadic class modulo $2^{A+1}$: pull back the odd endpoint class using the odd unit 3. CRT gives the stated ordinary family. The first two reverse gaps are 2, so $s=1\bmod9$; the first two forward gaps are 1 and 2, so $s=11\bmod16$. Thus $q=(2s+1)/3=1\bmod12$ and $T^5(2s+1)=T^4(s)$ on these finite lifts. The finitely many physical sites other than time zero are strictly between $s$ and $2s$ for large $s$: their leading ratios are $3^i/2^{B_i}\in(1,2)$ and all intercepts remain fixed. This argument does not supply badness or an all-time bounded trajectory. [Prior CRT construction at PR195](https://github.com/GettysburgResearch/collatz/blob/5b2bdcb6e4e60da15c29eadff8bd08b3991c5b57/research/astra-global-closure-20261124/round9/critical/README.md)

We tested every reverse word of depths one through **60**, ending at any of the eight ordinary odd phases at times $0,\ldots,7$ in these cylinders. For each of the aggregate tests, the smaller multiple-three ancestor and the smaller ordinary ancestor were both absent for all sufficiently large $s$ in the resulting progression. This prevents a complete cover by these eight endpoints and this depth.

For the exact enumeration let $x_i=as+b$ denote a target, with its rational affine coefficients. Compute its representative $R\bmod3^{61}$ from its 61 preceding reference gaps. At each reverse node of depth $j$ store the cumulative exponent $A$ and the integer $Y=(2^A R-C_j)/3^j$. These specify local legality at all remaining depths. If $Y=0\bmod3$, a next step is impossible and the floor there is $2s+1$. Otherwise the floor is $(3s+1)/4$. The parity of the next exponent is forced by $Y\bmod3$; every positive exponent of that parity is explored within the remaining budget.

For $f=2$ or $3/4$, a cheap candidate at fixed $j$ must have $2^A a\le f3^j$ at leading order. Any equality triggers the exact comparison of $(2^A b-C_j)/3^j$ with the floor intercept. The bound $\eta\le(3/2)^j-1$ in [BASIN.md](BASIN.md) handles arbitrarily large exponents: above the first power exceeding the leading cutoff, increasing $A$ only improves the uniform lower estimate $(2^A/3^j)(x_i-\eta_{\max})$. Hence only finitely many strict comparisons per target need an onset in $s$. To prune the tree at maximum depth $K$, the cumulative surplus $A-j$ cannot decrease. The largest affordable surplus, even allowing the larger floor $f=2$, is $\lfloor\log_2(2\cdot3^K/a)\rfloor-K$, since $3/2>1$. A node above this bound cannot lead to a qualifying candidate. [check_merger.py](check_merger.py) computes all powers, logarithmic floors and affine ties by integers and fractions. Running it with argument 60 explored 46,966,151 nodes across the eight roots and found no cheaper rival. The routine replay defaults to 40.

**The attempted induction.** Compare any reverse path to the same-length reference path, with respective valuation totals $A,B$. Set $d=A-B$ and write its site as $y=2^d x+c$ for the reference site $x$. At the common start $(d,c)=(0,0)$. Replacing a reference reverse gap $b\in\{1,2\}$ by a legal rival gap $a$ gives exactly
$$
       d'=d+a-b,\qquad c'=(2^a c+2^{d'}-1)/3.
$$
The first differing gap adds $2u$, $u\ge1$, since the reference uses the smallest exponent of the legal parity. Its new state is $(2u,(4^u-1)/3)$. As long as $d'\ge1$ the offset remains a positive integer on an ordinary path. It follows that $y\ge2s+1$ when the reference is above $s$. A profitable detour must first return to $d=0$. The decrease per step is at most one. A first such return therefore uses $d=1,b=2,a=1$ and a positive odd $c$ divisible by 3. At that point $c'=2c/3$ is positive. A still later first transition to $d=-1$ would likewise require $b=2,a=1$ with the old even $c=1\bmod3$, by ternary integrality of the formula. This reduces the induction to a specific offset and reference-gap synchronization problem. For unbounded depth the offsets and earlier gap choices are unbounded, and no forced return, subsequent target-height bound, or viable alternative invariant has been proved. The 60-depth computation cannot establish avoidance at every depth.
