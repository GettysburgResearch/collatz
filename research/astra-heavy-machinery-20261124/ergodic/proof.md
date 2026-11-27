# Higher-rank recurrence of corrected heights on the actual ordinary classes

**PROPOSED written results. Collatz remains OPEN.** The topological theorem below gives uniform logarithmic windows for *every* bounded-clock real trajectory. An arithmetic lifting theorem then specifies an arbitrary finite ordinary gap word and a ternary residue at an exact prescribed corrected level of one actual escaping component. Together they give a finite-window recurrence theorem preserving the least ordinary representative, its phase index, a finite synchronization clock, and a bounded additive error in the physical size. We do not infer convergence from density.

## 1. A finite-window consequence of Furstenberg's theorem

Write $\mathbb T=\mathbb R/\mathbb Z$, $\|t\|$ for distance to an integer, $\alpha=\log_2 3$ and use the maximum of the two circle distances on $\mathbb T^2$.

**E1.** For every $\epsilon>0$ there are integers $B,R\ge0$ depending only on $\epsilon$ with the following property. Suppose $X_0\ge1$ and
$$
X_{j+1}=3X_j/2^{a_j},\qquad a_j\in\{1,2,3,4\}.
$$
Set $N=\lceil\log_2(X_0+1)\rceil+B$. Given the path through time $N$, the points
$$
(2^rX_j\bmod1,\ \log_2 X_j\bmod1),\qquad
0\le j\le N,\quad 0\le r\le R
$$
are $\epsilon$-dense in $\mathbb T^2$. No integrality or Diophantine hypothesis on $X_0$ is required. For rational $\epsilon$ the constants are computable by a terminating finite certificate search. No practical growth rate is established here.

**Escape from a rational grid.** For every positive integer $d$ put $l=\lceil\log_2(dX_0+1)\rceil$. At least one $0\le j\le l$ has $\|dX_j\|\ge1/19$. Otherwise take the nearest integers $b_j$. Since $3+2^{a_j}\le19$, the integer $3b_j-2^{a_j}b_{j+1}$ has absolute value strictly less than one and vanishes. Iterating gives $2^{\sum_{j<l}a_j}\mid b_0$, whereas $1\le b_0<2^l$ and the sum is at least $l$. This argument also explains the logarithmic time scale. For example, $X_0=2^L$ and $a_j=1$ give integral first coordinates for every shift $r$ throughout $0\le j\le L$.

**Survivor sets and effective certificates.** Fix a nonempty rational open rectangle $Q$ in the torus. Define $S(x,t)=(2x,t)$ and $T(x,t)=(3x,t+\alpha)$. For nonnegative integers $R,H$ let $Y_{R,H}$ be the set of starts $p_0$ of paths of length $H$ in the torus satisfying
$$
Tp_j=S^{a_j}p_{j+1},\quad a_j\in\{1,2,3,4\},\qquad S^r p_j\notin Q\quad(0\le r\le R,\ 0\le j\le H).
$$
These sets are compact and nested in both indices. Their intersection $Y$ consists of starts of infinite paths avoiding $Q$ at every shift, by compactness of the sequence space. Along such a path $(Sp_j)$ is another surviving path. Also $Tp_0=S^{a_0}p_1$, a shift of the start of a surviving tail. Hence $SY,TY\subseteq Y$ and $Y$ misses $Q$.

**The two projections cannot miss a rectangle.** The first projection $F$ of $Y$ is compact and forward invariant under multiplication by 2 and 3. If it is infinite, Furstenberg's topological rigidity gives $F=\mathbb T$. To specify exactly the closed-set form being used, the semigroup $\{2^u3^v:u,v\ge0\}$ is nonlacunary. For an infinite closed invariant $F$, its derived set is nonempty and forward invariant (the maps are locally injective). A minimal invariant subset of the derived set contains a rational $b/d$ by Furstenberg's Proposition IV.2. Then $0$ is nonisolated in $dF$, and his Lemma IV.2 gives $dF=\mathbb T$. The finitely many translates $F+j/d$ cover the circle. Baire category gives interior in $F$, and forward doubling expands this to the full circle. This also handles an infinite set consisting solely of rational points. [Furstenberg, 1967, Part IV, especially Lemma IV.2, Proposition IV.2 and Theorem IV.1](https://doi.org/10.1007/BF01692494)

For any closed interval $J$ with nonempty interior in the second circle, let $K_J$ be the first projection of $Y\cap(\mathbb T\times J)$. It is compact and forward doubling-invariant. The irrational rotation by $\alpha$ hits the interior of $J$ within $L_J$ steps from any initial phase, by compactness. For every $x$ there is a $t$ with $(x,t)\in Y$, and one of $(3^sx,t+s\alpha)$ for $0\le s\le L_J$ belongs to $Y\cap(\mathbb T\times J)$. Thus the finitely many closed sets $(\times3^s)^{-1}K_J$ cover the first circle. One has interior; since multiplication by $3^s$ is open, $K_J$ has interior. Its doubling-invariance gives $K_J=\mathbb T$. Shrinking $J$ to any requested second coordinate gives $Y=\mathbb T^2$, contrary to the missed rectangle. Thus $F$ is finite. Its elements are rational since their forward doubling orbits are finite. Take a common denominator $d\ge1$ (or 1 when empty). By nesting and compactness some $R,H$ satisfy
$$
Y_{R,H}\subseteq\{(x,t):\|dx\|<1/19\}. \tag{C}
$$
Compute any such triple by enumerating $R,H,d$ and testing (C). Its failure is a finite union of bounded linear feasibility problems: use coordinates in $[0,1]$, enumerate the four clock choices and the finitely many integer wraps for each multiplication and rotation, then choose one component of the closed complement of the open rectangle for each avoidance. The additional failed-containment condition is $\|dx\|\ge1/19$. Fourier–Motzkin elimination uses rational coefficients and constants in $\mathbb Q+\mathbb Q\alpha$. Signs in this ordered additive group are decidable since $\log_2 3$ is computable and irrational. Endpoints representing the same circle point can each be retained. Thus each finite test terminates, and compactness proves termination of the outer search.

If the actual schedule misses $Q$ at all these shifts through time $N$, each phase $0\le j\le N-H$ belongs to $Y_{R,H}$ and obeys the grid inequality, contradicting the rounding lemma as soon as $N-H\ge\lceil\log_2(dX_0+1)\rceil$. This gives $B=H+\lceil\log_2 d\rceil$ for $Q$. To obtain E1 for rational $\epsilon$, choose finitely many rational open grid rectangles of diameter less than $\epsilon$ whose closures cover the torus; hitting each suffices. Use the maximum $B,R$ from their certificates. No entropy hypothesis on the actual time averages is used.

For comparison, Bourgain, Lindenstrauss, Michel and Venkatesh's Theorem 1.8 gives a rate for the semigroup orbit of one irrational satisfying a uniform lower bound on the quality of its rational approximations. The bounded-clock schedule here may start at a dyadic rational, and different grid-escape witnesses may occur at different phases. Their Theorem 1.10 concerns individual reduced rationals with denominator coprime to both generators. Neither hypothesis is needed by (C). [Bourgain et al., Theorems 1.8 and 1.10](https://math.stanford.edu/~akshay/research/blmv.pdf)

## 2. Prescribing one ordinary inverse arm at an exact dyadic level

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd ordinary integers. For an odd-gap word $g_0,\ldots,g_{h-1}$ of positive integers with $a_j=\sum_{\ell<j}g_\ell$, its full finite equation is
$$
3^h z+C=2^{a_h}t,\qquad C=\sum_{j<h}3^{h-1-j}2^{a_j}.
$$
If $z$ is positive integral, $t$ is odd positive, and this equation holds, it realizes all exact gaps. For length one this is the definition of the valuation. At length greater than one, $C=3^{h-1}+2^{g_0}C_{\rm tail}$, with $C_{\rm tail}$ odd. Reducing the equation modulo $2^{g_0+1}$ forces $v_2(3z+1)=g_0$; division gives the remaining equation. This is the ordinary parity-cylinder argument of PR182, scalar-rigidity-round9-20261123/ACTUAL_SCALAR_LAW.md, R9-L1.

**E2.** Fix a finite word $w$ of positive gaps, of length $h-1\ge0$ and total $G$, and a residue $u\bmod3^b$, $b\ge1$. There is a uniform integer $R_0$ depending only on $w,b$ such that for **every** positive odd $x$ and **every** $r\ge R_0$ there is a positive odd $z$ with:
- initial exact gap word $w$, and $z\equiv u\bmod3^b$;
- $U^{h+1}(z)=U^{h+1}(x)$;
- the sum of the first $h+1$ actual valuations from $z$ exceeds that from $x$ by **exactly** $r$.

This statement is independent of escape. In particular $u$ can be any unit. It prescribes the real corrected height exactly whenever the correction sums of the two paths are finite.

**Proof.** Set $t=U^h(x)$, and let $A$ be the actual binary clock on these first $h$ steps from $x$. Append a yet unspecified final gap $e$ to $w$. Its carry $C$ is independent of $e$. The ordinary lift $t'=4^s t+(4^s-1)/3$ is odd, has $U(t')=U(t)$, and has valuation $v_2(3t+1)+2s$. Choose $s$ so that
$$
4^{-s}\equiv1+3t-3\cdot2^{-(A+r)}(C+3^h u)\pmod {3^{h+b+1}}. \tag{1}
$$
The right side is 1 mod 3. The powers of 4 generate the principal units modulo $3^k$: cubing $1+3^j v$ for $j\ge1$ and $3\nmid v$ increases this valuation by exactly one. Starting from 4 this gives order $3^{k-1}$, the number of residues equal to 1 mod 3. We may therefore take $0\le s<3^{h+b}$.

Take $r\ge R_0=2\cdot3^{h+b}+G+2h+1$ and put $e=A+r-2s-G$. Then $e\ge2h+1$. Equation (1) is precisely the divisibility requirement after multiplying by 3 for
$$
z=\frac{2^{G+e}t'-C}{3^h}\equiv u\pmod {3^b}.
$$
Indeed $3\cdot2^{G+e}t'=2^{A+r}(1+3t-4^{-s})$ in the indicated residue ring. The quotient is positive since $C<2^G3^h$ and $t'\ge1$. It is odd because $C$ is odd. The complete-word criterion realizes $w,e$ exactly, with endpoint $t'$. The extra odd step brings the two paths to the same $U(t)$, and the clock excess is $(G+e-A)+2s=r$.

For any given odd binary residue modulo $2^k$, one can fix an initial gap word $w$ forcing it. Start from its least positive odd representative, take enough ordinary odd steps to cover at least $k$ shortcut parity bits, and include these complete gaps. The parity-bit cylinder fixes the initial residue. Thus E2 allows arbitrary **simultaneous** odd binary and ternary-unit residues, even when their moduli are not small. The rank budget is allowed to depend on the fixed moduli and word.

## 3. Application to the least ordinary representatives of one escaping orbit

Use only §§3–4 of PR193's [class-minimum proof](../../astra-global-synthesis-20261124/section/proof.md), commit d35bdfd9d0c75effda50bbb8040c136482431e24, file SHA-256 cbe95e8adf39ccf90253573005350260ee6ea0d67cb10c206108cbb624c59a02. For an injective positive odd orbit $q_i$, its $i$th synchronous class contains every odd $x$ with $U^t(x)=U^t(q_i)$ for some $t$. Discard one early term if necessary so all $q_i$ are units. Write $n_i$ for its least odd ternary-unit representative, and
$$
M(x)=x\,2^{\sum_{j\ge0}\log_2(1+1/(3U^j x))},\qquad M_i=M(n_i).
$$
The cited class envelope gives $1<M_i/n_i\le2^{D_i}$ with $D_i\to0$. Distinct classes have distinct minima, hence $n_i\to\infty$. All sufficiently late corrected clocks satisfy $M_{i+1}=3M_i/2^{a_i}$ with $1\le a_i\le4$. Also the first $h$ *actual* gaps from $n_i$ have total $A\le\sum_{\ell=i}^{i+h-1}a_\ell\le4h$ by the finite-window minimum-clock inequality (6) there. The last inequality pertains to sources chosen as actual unit minima, not general members of their classes.

**E3.** Prescribe two open arcs $I,J\subseteq\mathbb T$, a finite odd-gap word $w$, and an odd binary and ternary-unit cylinder compatible with $w$ (or just prescribe the two residue cylinders and choose a word as above). Equivalently, for an additional compatible binary cylinder one may choose a common finite extension of $w$ representing both. At every sufficiently late starting phase $i$ there exist
$$
0\le j\le\lceil\log_2(n_i+1)\rceil+B',\qquad R_0\le r\le R'
$$
and an ordinary ternary-unit $z$ in the class of $n_{i+j}$, with the requested initial word and residues, such that
$$
\{M(z)\}\in I,\qquad \{\log_2 z\}\in J,\qquad
M(z)=2^r M_{i+j},\qquad |z-2^r n_{i+j}|\le K .
$$
Here braces denote points modulo one. The constants $B',R',K$ depend only on the requested arcs and cylinder data. The merger with $n_{i+j}$ takes exactly the common observation clock $h+1$ of E2 for the chosen prefix (an earlier meeting is allowed). If the given orbit was escaping, every such $z$ escapes in the same ordinary component.

**Proof.** Apply E1 to $X_j=2^{R_0}M_{i+j}$, taking an interior rectangle with enough room for a small perturbation of the second coordinate. The integer exponent $R_0$ preserves that coordinate. The window length is at most $\lceil\log_2(n_i+1)\rceil+R_0+B+1$ once $D_i<1$. Add $R_0$ to the selected shift to get $r$. E2 then supplies $z$. The identical terminal odd value and exact clock excess give $M(z)=2^rM_{i+j}$ by iterating $M(Ux)=3M(x)/2^{v_2(3x+1)}$. Consequently the actual ordinary log phase of $z$ differs from the selected corrected log phase by at most $D_{i+j}\to0$, uniformly over all choices. This proves the two arc claims.

For the additive estimate, write $x=n_{i+j}$ and $3^h x+C_x=2^A t$. The E2 construction gives the exact identity
$$
3^h(z-2^r x)=2^r C_x-C+(2^{A+r}-2^{A+r-2s})/3.
$$
The original carry $C_x$ is bounded in terms of $h$ alone because $A\le4h$. Both $r$ and $s$ are uniformly bounded in this application. Thus the right side is bounded independently of $i$ and $n_i$, establishing $K$.

In particular, on those logarithmic windows the binary tails of the corrected fractional parts of the minimum representatives cannot all omit a prescribed binary block at every one of a sufficiently large, fixed number of shifts, even if one tests only phases with prescribed ordinary leading bits. The ordinary realizers can also be assigned any fixed admissible low dyadic and ternary digits. The logarithm refers to the schedule of the actual classes of one hypothetical escape.

## 4. What this forces and what it leaves open

A consequence stronger than one-point density is that a single escaping component, if it exists, contains a sequence of ordinary sources sampling any prescribed probability law on the product of these coordinates (fractional corrected height, ordinary leading phase, odd 2-adic source and 3-adic unit source). For the product Haar law, take increasingly fine finite rectangular partitions and select successively later classes approximating the desired masses by finite empirical frequencies using E3. Choose the two arcs and the two cylinders independently in each rectangle; each rectangle has ordinary witnesses. The resulting sequence may be arranged to converge weakly to the target, e.g. by concatenating increasingly accurate finite grids, repeating each stage long enough that incomplete finer grid traversals have negligible weight. These are selected representatives, not a statement about the native time average of the unshifted minima. For example, with the very same two real coordinate targets one may instead impose congruence to the odd 2-adic number $-1/3$ at increasing precisions. Then every chosen source has initial valuation tending to infinity and the 2-adic marginal is a point mass. Neither selection changes the component.

Tao's near-boundedness theorem controls logarithmically sampled ordinary starting values, via stability of its first-passage distribution. E3 provides no positive logarithmic *source mass* for these selected witnesses, nor a downward first passage below a fixed least nonconverger. It allows one to prescribe typical finite initial valuations without asserting a typical remainder for the same source. In E2 the easily forced terminal halving costs almost the added binary rank $r$. No estimate makes its endpoint fall below the original least source. [Tao, Forum of Mathematics, Pi 10 (2022), e12](https://doi.org/10.1017/fmp.2022.8)

One can average $\{2^r M_i\}$ over rectangles of consecutive $i,r$ to get jointly invariant weak limits: shifting a row costs one boundary term for doubling, and tripling moves to the next $i$ with at most four unpaired columns. The grid and Baire argument instead proves full topological support after bounded shifts; a particular empirical weak limit need not have that support or positive entropy. Rudolph's measure theorem requires joint invariance, joint ergodicity and positive entropy in at least one generator to conclude Lebesgue for an ergodic component. Even Lebesgue measure on the corrected real circle by itself gives no bound on the mass of unsolved ordinary sources. [Rudolph, 1990](https://doi.org/10.1017/S0143385700005629)

For a complete contradiction it would suffice, for example, to find a forbidden rectangle for **all** E3 witnesses in the indicated actual classes, with any finite cylinder and a fixed forbidden corrected binary pattern at every allowed rank. The arithmetic lifts show why a prohibition based only on the finite source residues fails. The rank and ordinary size in E3 are bounded relative to the moving class minimum, not smaller than the original global floor. Neither cycles nor escape are eliminated unconditionally here; the harmonic corrected heights in particular are not defined on a repeated positive cycle.

**Rank and precision.** For a late synchronous class, let a unit $z$ have corrected level $M(z)=2^r M_i$. Its $p$th odd image is a unit in the class of $n_{i+p}$. Its level is $r+\sum_{j=i}^{i+p-1}a_j-E_p(z)$, where $E_p(z)$ denotes its actual binary clock. The cited least-unit theorem makes this integer nonnegative. Thus any prescribed initial $p$-gap word of total $G$ requires $G\le r+4p$. In particular a single valuation $e$ costs $r\ge e-4$. For fixed $b$, E2 attains $r=e+O_b(1)$ when prescribing this one valuation.

There is a second obstruction to lowering E2's precision cost. Fix a late phase, one exact rank $r$, a common observation horizon $H>p$, and a prescribed prefix of $p$ positive gaps of total $G$. Every candidate that actually merges at that horizon has the same total clock $E=r+E_H(n_i)\le r+4H$ and the same endpoint. Each completion of the word therefore gives at most one possible source by the full affine equation. If $E-G\ge H-p$, the number of sources is at most
$$
\binom{E-G-1}{H-p-1};
$$
otherwise there are none. To cover all $2\cdot3^{b-1}$ unit residues modulo $3^b$ at one rank, this binomial coefficient must be at least $2\cdot3^{b-1}$. At E2's horizon $H=p+2$, this forces $r\ge G+2\cdot3^{b-1}-4H+1$. The exponential dependence on ternary precision at this horizon holds for every steering construction. Allowing many additional odd steps can change this bound. For example, at fixed $p$ and $r=O(b)$, linear-in-$b$ covering would require $H-p=\Omega(b)$: if $H=o(b)$ the standard estimate $\binom nk\le(en/k)^k$ has logarithm $o(b)$. No matching construction or floor repayment is proved here.

Monks, Monks, Monks and Monks prove that every arithmetic progression can be reached by back tracing from any positive integer coprime to 3, with a bound on the number of inverse odd steps depending on the modulus. In their Theorem 4.1 the bound is $n+1$ for modulus $2^n3^m$. The binary padding chosen by primitivity modulo a power of 3 is outside that odd-step count. E2 specifies the excess binary time and common odd horizon simultaneously. [Monks et al., Theorem 4.1 and its proof](https://arxiv.org/pdf/1204.3904)

**Formal scope.** The companion Std Lean file checks the common-denominator rounded-edge lemma, the forced power-of-two divisibility along an exactly rounded run, its finite contradiction at a positive smaller start, and replay of every intermediate odd gap from the single affine word equation. The compactness, Furstenberg, arithmetic steering and actual-class assembly above are written proofs.
