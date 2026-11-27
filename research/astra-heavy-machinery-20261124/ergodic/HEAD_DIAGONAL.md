# Positive mass on the literal first-passage diagonal at every head level

Use the shortcut map $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. Write $U$ for the odd map, $A(b)=\{n:T^t(n)=b\text{ for some }t\ge0\}$, and $h_M(n)$ for the first actual orbit value at most $M$, when defined. PR197 introduced the parent comparison on $H_j=[7R_j,8R_j)\cap\mathbb N$, $R_j=81^j$. PR199 counts failed joint first-passage comparisons on these same bands. We assume its input **M**: $A(b)$ has positive lower natural density for each fixed odd positive $b$ coprime to three. The reported external result is an assumption here. [PR197, fixed head-edge criterion at 9ed095c](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/HEAD_EDGE_RIGIDITY.md) · [PR199, input M at d868f8e](https://github.com/GettysburgResearch/collatz/blob/d868f8e8405c08b8c501236853bea495ca593824/research/optimal-critical-ancestors-20261124/README.md) · [PR199, joint first-passage criterion](https://github.com/GettysburgResearch/collatz/blob/d868f8e8405c08b8c501236853bea495ca593824/research/optimal-critical-ancestors-20261124/FIRST_PASSAGE.md)

**Theorem (conditional on M).** For each such fixed $b$ there are constants $c_b,\eta_b>0$ such that, at every sufficiently large $j$, at least $c_bR_j$ distinct $x\in H_j$ have the following property simultaneously for every $b\le M<\eta_b R_j$. The starts $x$ and $m=\lfloor x/81\rfloor$ hit $[1,M]$ for the first time at the same shortcut clock and at the same integer, which belongs to $A(b)$. In particular this applies on every sufficiently high level to any prescribed $M_j\to\infty$ with $M_j=o(R_j)$. The constants may depend on the fixed target. Only M is used.

**Positive-density unit seeds.** Odd ternary units in $A(b)$ have positive lower density. Let $\delta>0$ be a lower bound for $\#(A(b)\cap[1,Y])/Y$ for all large $Y$. Write $n=2^i v$ with $v$ odd and discard $i>K$, costing at most $2^{-K}Y$. Keep $v$ itself if it is a ternary unit. Otherwise keep $U(v)$ provided $v_2(3v+1)\le K'$. At each $i\le K$ the excluded $v$ occupy one class modulo $2^{K'}$, costing in total at most $2^{1-K'}Y+O(K+1)$. Choose the cutoffs so the total discarded density is smaller than $\delta/2$. The retained seed is an odd unit of $A(b)$: a nonunit $v$ precedes the fixed odd unit $b$ on its orbit. There are at most $(K+1)(1+K')$ original $n$ per seed, by the inverse formula for each possible first gap. All seeds are at most $2Y$, which proves the claim at all sufficiently large cutoffs. Write $\delta_b>0$ for a lower bound for their resulting density.

**Choosing a seed in the specified head.** Put $X=R_j$. From each unit seed $q$ take legal unit inverse steps to $y_s$, starting with $y_0=q$. At each step choose a gap $a\le4$ so $(2^a y-1)/3$ is a positive odd unit: choose the legal parity $a_0\in\{1,2\}$, then use $a_0$ or $a_0+2$, whose outputs are siblings $v,4v+1$. Thus $U^s(y_s)=q$ and $q/3^s\le y_s\le(16/3)^s q$. For any fixed $S$ one has uniformly for $s\le S$
$$
\log_2 y_s=\log_2 q-s\log_2 3+\text{integer}+O_S(1/q).
$$
This follows by adding the errors $\log_2(1-1/(2^a y))$ along the bounded inverse path.

Take the fixed rank $r=2\cdot3^5+3$ from [E2](proof.md), using its empty prescribed word and ternary modulus $81$. A finite net of the irrational rotation by $-\log_2 3$ supplies an absolute $S$ such that some $2\le s\le S$ puts the phase of $\log_2 q-s\log_2 3$ in a strictly interior subarc of $[\log_2(7.25X),\log_2(7.75X)]\bmod1$, uniformly in $X,q$. Choose a fixed $C>2^{r+6}(16/3)^S$ and use the seeds
$$
\delta_b X/(2C)\le q\le X/C .
$$
There are at least $\delta_b X/(2C)-O(1)$ of them for all large $X$. The logarithmic error fits the interior margin. For each chosen $s$ there is consequently an integer $L$ with
$$
7.25X\le 2^{L+r}y_s\le7.75X.
$$
The upper and lower bounds on $y_s/q$ give $4\le L\le L_b$ for a constant $L_b$ independent of $j$.

**Constructing the actual pair.** Apply E2 to $y_s$ at rank $r$, prescribing $z\equiv65\cdot2^{-L}\bmod81$. It gives a positive odd unit $z$ with $U^2(z)=U^2(y_s)$, so $U^s(z)=q$ since $s\ge2$. In E2's affine identity the one-step carries for both initial arms are 1 and the actual first gap $A$ from $y_s$ is at most four. Its sibling parameter $t\ge0$ therefore gives
$$
3(2^{-r}z-y_s)=1-2^{-r}+(2^A-2^{A-2t})/3,
\qquad |2^{-r}z-y_s|<3.
$$
Set $x=2^Lz$. Its distance from $2^{L+r}y_s$ is bounded by $3\cdot 2^{L_b+r}$, a fixed constant. For large $j$, $x\in H_j$. Its residue modulo 81 is 65, so the actual integer parent satisfies $81m+65=2^L z$. The four-gap word $(1,1,1,L-3)$ has carry $27+18+12+8=65$. Full-word replay gives $U^4(m)=z$, precisely $L$ shortcut steps. The child also reaches $z$ at shortcut clock $L$.

Every child state before that meeting is at least $z$. On the parent arm four odd shortcut steps increase the value, followed by $L-4$ even steps ending at $z$. All parent states through the meeting are at least $\min(m,z)$. Here $m\ge7X/81-1$ and $z\ge7X/2^{L_b}$, so both bounds exceed $\eta_bX$ for some fixed $\eta_b>0$. Both starts then follow the same path through $q$ to the *original* fixed $b$. For $b\le M<\eta_bX$, the two first hits therefore occur at the same clock and at the same point on the common prefix ending at $b$. Finally each $x$ determines its odd part $z$, and the original seed must be one of $U^s(z)$ for $2\le s\le S$. Dividing the seed count by $S$ proves the lower bound.

**Scope.** PR199 obtains optimal counting exponent $1-1/k$ for ancestors in its relaxed critical section under M and its phase bound R. Its first-passage criterion, under M and its uniform barrier input N, would give universal convergence if the normalized off-diagonal component failures were summable over head levels. The present theorem supplies a positive lower bound on *equal first-passage roots* in each fixed target's ancestor set at each level. It leaves the mass of the other head pairs uncontrolled. Even for a least nonconvergent target the certified children and parents meet before reaching that target, so their equality supplies no source below it.
