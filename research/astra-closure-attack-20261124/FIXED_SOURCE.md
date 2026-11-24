# A finite-comparison obstruction from the same ordinary source at two places

**Status.** Proposed written proof, 24 November 2026. The global contradiction below applies to fixed positive escaping orbits that admit sparse defects against finite rational comparison sets. Whether every escaping candidate must admit such windows is open. The smooth-part and multiplicative-rank results give additional restrictions on the actual heights. No result here excludes all cycles or proves Collatz. The arguments use external Diophantine theorems and have not been compiled in Lean.

## 1. Normalization and the actual real shadow

Fix a positive odd integer $q_0$, with actual successive odd states $q_i$, gaps $a_i=v_2(3q_i+1)\ge1$, and $A_n=\sum_{i<n}a_i$. Write $u_n=2^{A_n}/3^n$. For all $n$,

$$2^{A_n}q_n=3^n q_0+\sum_{i<n}3^{n-1-i}2^{A_i},\qquad u_nq_n=q_0+\tfrac13\sum_{i<n}u_i.\tag{1}$$

Suppose the orbit is nonperiodic, hence injective and $q_i\to\infty$. The fixed-orbit separated-visit bound in PR182, `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, at `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, gives $\sum 1/q_i<\infty$ (any of the established strict-power global counts suffices). Then $u_nq_n=q_0\prod_{i<n}(1+1/(3q_i))$ converges in the reals to a finite $\Lambda>0$, and $u_n\to0$. In the dyadic field $u_n q_n\to0$ because $A_n\ge n$ and $q_n$ is integral. These are separate limits of the **same rational numbers**. No algebraicity of $\Lambda$ is needed.

## 2. FS1: boundedly many virtual errors cannot hide in a sufficiently long window

Fix any nonempty finite set $T\subset\mathbb Q$. In a window $[N,M)$ choose any comparison states $t_N,\ldots,t_M\in T$. Call $i$ an error if $3t_i+1\ne2^{a_i}t_{i+1}$. The comparison states need not be positive or dyadically odd, and choices for different windows need not agree.

**Theorem.** On a nonperiodic fixed positive ordinary orbit, for any sequence $N\to\infty$, $M>N$ of windows admitting a bounded number of errors,

$$\limsup\frac{A_M\log2-N\log3}{M}\le0.\tag{2}$$

In particular, fix $R>\log_2 3$ and put $M=\lfloor RN\rfloor$. Then the minimum number of errors over **all** assignments in $T$ tends to infinity as $N\to\infty$. Indeed $A_M\ge M$ makes the expression in (2) bounded positively away from zero on these windows. On windows with $\log q_M=o(M)$, the same conclusion holds for every fixed $R>1$ by (1). In source-height terms the numerator in (2) is $(A_M-A_N)\log2-\log q_N+O_{q_0}(1)$.

**Proof.** Suppose instead some $\eta>0$ and arbitrarily late windows satisfy $A_M\log2-N\log3\ge\eta M$, with at most $K$ errors. For each such window put $X_0=3^M$ and $Y=2^{A_M}(q_M-t_M)$. Subtract the virtual affine update from (1) to get the exact identity

$$Y-\sum_{N\le i<M}3^{M-i-1}2^{A_i}(3t_i+1-2^{a_i}t_{i+1})
=3^{M-N}2^{A_N}(q_N-t_N).\tag{3}$$

There are at most $2K$ nonzero signed terms after expanding the summands at the errors. Each is of shape $X=3^M b\,2^B/3^{i+1}$, with fixed finite coefficient menu $b\in\{3t+1,-t:t\in T\}\setminus\{0\}$ and $B=A_i$ or $A_{i+1}$. Pass to a subsequence on which the number $s\le2K$ of terms is constant. Enlarge a fixed prime set $S_0$ to include 2, 3 and all primes in the finitely many nonzero comparison states and coefficients. Thus $X_0,X_1,\ldots,X_s$ are rational $S_0$-units. The denominators of these unnormalized coordinates and $Y$ are bounded independently of the windows. No independence of atom columns is assumed.

Let $S$ contain the real place and the primes $S_0$. Apply the rational finite-place Subspace Theorem to $(X_0,Y,X_1,\ldots,X_s)$. At every place take all coordinate forms, except use $Y-\sum_{h=1}^s X_h$ in place of $Y$ at 3. Each local system has determinant one. The product over the places of the absolute values of every $S_0$-unit column is exactly one. At the real place $|Y|\ll3^M$ by (1). At 2, $|Y|_2\ll_T 2^{-A_M}$. At 3 the replacement form has absolute value $\ll_T3^{-(M-N)}$ by (3). At all other primes in $S$ the $Y$-factor is bounded since its denominator is bounded. The complete linear-form product is therefore

$$\ll 3^N2^{-A_M}\le e^{-\eta M}.\tag{4}$$

Every $X_h/3^M$ tends to zero in the reals, since its absolute value is bounded by a constant times $u_i$ or $u_{i+1}$ at an error $i\ge N$. The maximum norm of the displayed vector is thus between $3^M$ and $C3^M$. Clear its fixed bounded denominator. For any sufficiently small fixed $\delta>0$, (4) is less than the resulting integer norm to the power $-\delta$. Evertse's presentation of Schlickewei's Subspace Theorem, Theorem 4 on p.231 of the paper listed below, puts the integer vectors in finitely many proper rational linear subspaces. One fixed nontrivial rational relation therefore holds on a further infinite subsequence.

Divide the relation by $3^M$. In $\mathbb Q_2$, $Y/3^M\to0$ and every $X_h/3^M\to0$ because $B\ge A_N\to\infty$ and all coefficients are fixed rationals. This forces the coefficient of $X_0$ to vanish. In the reals, $Y/3^M=u_M(q_M-t_M)\to\Lambda>0$, while all $X_h/3^M\to0$. Hence the coefficient of $Y$ also vanishes. If there are no remaining columns, this is the desired contradiction. Otherwise the relation involves only atom columns. Solve it for one atom, substitute that expression into the 3-adic form, and delete the solved column. This changes $Y-\sum X_i$ into $Y-\sum b_i X_i$ with **fixed rational coefficients**, with the same value on the selected subsequence. The new 3-adic linear system still has determinant one. The remaining columns are original $S_0$-units and still tend to zero at both places after normalization. The same inequality (4) therefore gives another fixed relation with zero coefficients at $X_0$ and $Y$. Each application deletes a column; within at most $s+1$ applications a contradiction follows. This dimension descent handles arbitrarily clustered atoms, fixed proportionalities and signed cancellations.

**Corollary.** Let $D_T(n)$ be the minimum number of errors over assignments to the full prefix of $n$ steps. Then $D_T(n)/\log n\to\infty$ on any positive escaping orbit. For an integer $R>\log_2 3$, divide time into $[R^j,R^{j+1})$. FS1 says the minimum cost in those blocks tends to infinity. Adding independent minima gives a lower bound on every shared assignment's cost. Cesàro averaging and monotonicity give the assertion at all $n$. With $T=\{-1\}$, zero error means $a_i=1$, so the count of nonunit actual gaps grows faster than $\log n$. The stronger window statement detects long sparse stretches even if other parts of the orbit have many defects.

A fixed periodically prescribed positive gap word also has a finite rational comparison cycle: its nonempty complete affine map has slope $3^d/2^B\ne1$ and hence a unique rational fixed point. Carry its phases around the word. Every matching letter is a zero-error edge, so FS1 applies even to comparisons against different allowed phases in different windows. It supplies no constraint of positive *linear* defect density.

## 3. FS2: a fixed-prime cofactor obstruction on the actual heights

For a finite set $P$ of primes containing 2 and 3, let $V_P(q)$ be the largest divisor of $q$ coprime to each prime of $P$. For every fixed $k\ge1$, $0\le d<1$ and $c>0$, apart from finitely many positive odd starts $x$, their $k$-step endpoint $y=U^k(x)$, with total gap $B$, satisfies

$$V_P(x)V_P(y)>c(2^B y)^d.\tag{5}$$

To apply Evertse 1984, Corollary 1 (printed p.227, specifically (9)–(12)), use the integer tuple

$$\big(3^k x,\ 3^{k-1},\ 3^{k-2}2^{B_1},\ldots,\ 2^{B_{k-1}},\ -2^B y\big),\quad B_j=\sum_{i<j}a_i.$$

At $k=1$ there is just one carry coordinate, equal to one. The tuple sums to zero, is primitive because the first and last carry coordinates are coprime, and has no vanishing nonempty proper subsum: the last negative entry cancels exactly the entire set of positive entries. Its height is $2^B y$. The outside-$P$ part of the absolute product of all coordinates is precisely $V_P(x)V_P(y)$. Corollary 1 gives only finitely many tuples violating (5); the first coordinate recovers $x$. The threshold is not asserted effective or uniform in $k,P$.

If $0\le\beta<1/2$, on any one positive escaping orbit let $J=\{i:V_P(q_i)\le q_i^\beta\}$. Then gaps between consecutive members of $J$ tend to infinity if it is infinite; in particular $J$ has upper Banach density zero. Indeed choose $2\beta<d<1$. If $i,i+k\in J$ for fixed $k$, then $q_{i+k}+1\le(3/2)^k(q_i+1)$ and (1) gives $2^B q_{i+k}\ge3^k q_i$. These contradict (5) for large $q_i$. Apply this for all $k$ up to any fixed cutoff. This proves a density-one lower bound for outside-$P$ mass at the actual times, stronger than merely unbounded prime support.

If $\Gamma\subset\mathbb Q_{>0}$ is any fixed finite-rank group, its elements have prime supports in one finite $P$: take a rational vector-space basis from $\Gamma$ after tensoring multiplicatively with $\mathbb Q$ and use valuations outside the supports of its representatives. For every $g\in\Gamma$ the numerator of the reduced fraction $q_i/g$ retains $V_P(q_i)$. For fixed algebraic $\lambda\ne0$, absolute logarithmic height consequently gives $h(q_i/(\lambda g))\ge\log V_P(q_i)-h(\lambda)$. By FS2 this is greater than $\beta\log q_i-h(\lambda)$ **simultaneously for all** $g\in\Gamma$ outside the uniformly sparse set $J$. The real estimate $q_i/(\Lambda 3^i/2^{A_i})\to1$ therefore does not give adelic closeness, even if $\Lambda$ happened to be algebraic. For the particular multiplier $3^i/2^{A_i}$ the rational normalized value itself already has denominator exactly $3^i$ when $i\ge1$, since $3\nmid q_i$.

## 4. FS3: a bound uniform in the rank of the prime ledger

Fix a rank-$r$ multiplicative group $\Gamma\subset\mathbb Q_{>0}$ and $c>0$ rational. For fixed $k$, the number of distinct positive odd starts $x$ for which $x,U^k(x)\in c\Gamma$ is at most

$$E_k(r)=\exp\!\big((6(k+1))^{3(k+1)}(2r+k+1)\big).\tag{6}$$

Write $x=cg$, $y=ch$ and divide the complete affine equation by $2^B y$. Its $k+1$ positive terms form a unit equation. Use coefficient $3^k$ for the first coordinate and $3^{k-1-i}/c$ for carry coordinate $i$. The group of coordinate vectors is contained in the group generated by the following independent *types* of factors: $g$ in the first coordinate (rank at most $r$); $h^{-1}$ in every coordinate (rank at most $r$); a common power of 2 in every coordinate (one generator); and separate powers of 2 in carry coordinates $i=1,\ldots,k-1$ ($k-1$ generators). Thus rank is at most $2r+k$. The ratio of the first full term to the first carry term recovers $3x$. Positivity rules out all vanishing subsums. Evertse–Schlickewei–Schmidt, Theorem 1.1, gives (6). For a fixed rank the bound is uniform even when the prime support and rational coset representative change.

For $k=1$, include the coefficient pair as one additional generator and use Beukers–Schlickewei, Theorem 1.1, to obtain the sharper bound $2^{16r+24}$. In particular any $N$ consecutive odd transitions with distinct starting states and all $N+1$ states in one rank-$r$ coset require $r\ge(\log_2 N-24)/16$. More generally, in any $N$-position injective interval let $J$ mark visits to one such coset. For any $K\ge1$, at most $\sum_{k=1}^K E_k(r)$ consecutive visit pairs have separation at most $K$, and all other consecutive visit pairs are disjoint time intervals of length at least $K+1$. Thus $|J|\le1+N/(K+1)+\sum_{k=1}^K E_k(r)$. It follows that the supremum of the visit fraction over **all** orbit intervals and all rank-$r$ cosets tends to zero with $N$.

## 5. FS4: the actual full carry has unbounded positive rational S-unit length

Fix a finite prime set $P\supseteq\{2,3\}$. For a positive rational $z$, let $\ell_P(z)$ be the least number of positive rational $P$-units summing to $z$; set the value to infinity if no such representation exists. Local affine carries here are positive integers and so always have a finite representation (even a sum of ones).

For one fixed positive escaping ordinary orbit, put

$$C_{N,M}=2^{A_M-A_N}q_M-3^{M-N}q_N=\sum_{i=N}^{M-1}3^{M-1-i}2^{A_i-A_N}.$$

**Theorem.** Suppose $N\to\infty$, $M>N$, $\liminf N/M>0$ and $\liminf (A_M\log2-N\log3)/M>0$. Then $\ell_P(C_{N,M})\to\infty$. In particular this holds for every $M=\lfloor RN\rfloor$ with fixed $R>\log_2 3$. The summands in a putative short representation are completely arbitrary positive rational $P$-units. They need not be original carry terms or be associated with positions of the word.

**A denominator bound.** For fixed $P,K$ and every $\epsilon>0$, if an integer $c>0$ is the sum of at most $K$ positive rational $P$-units with least common denominator $U$, then $U\le C_{P,K,\epsilon}c^\epsilon$. To see this write the summands $n_j/U$. The numbers $U,n_j$ have no prime factors outside $P$. Let $g=\gcd(n_j)$; minimality of $U$ ensures $\gcd(g,U)=1$, so $g\mid c$. The integer tuple $(n_1/g,\ldots,n_k/g,-Uc/g)$ is primitive and nondegenerate by positivity. Its largest absolute coordinate is $U(c/g)$ and the outside-$P$ part of the coordinate product is $V_P(c/g)\le c/g$. For $d=1/(1+\epsilon)$ Corollary 1 of Evertse 1984 leaves only finitely many exceptions to $c/g>(U c/g)^d$. This gives $U<(c/g)^\epsilon\le c^\epsilon$. Every exceptional primitive tuple has bounded largest coordinate and hence bounded $U$, even after allowing arbitrary $P$-smooth scaling $g$. Taking the finite union for $1\le k\le K$ gives the assertion.

Now suppose infinitely many of the displayed windows have $C_{N,M}=s_1+\cdots+s_k$ with a fixed $k\le K$ and positive rational $P$-units $s_j$. Put $X_j=2^{A_N}s_j$, $X_0=3^M$, $Y=2^{A_M}q_M$. They satisfy

$$Y-\sum X_j=3^{M-N}2^{A_N}q_N,\qquad \sum X_j/3^M=u_M q_M-u_N q_N\longrightarrow0\quad(\text{real}).$$

Positivity forces **each** $X_j/3^M\to0$ in the reals. Also $C_{N,M}\ll_{q_0}3^M$, and the denominator bound for every $\epsilon>0$ gives $\log U=o(M)$. Since $A_N\ge N\gg M$, the dyadic valuation of each $X_j/3^M$ is at least $A_N-\log_2 U\to\infty$. Thus each normalized atom tends to zero in both fields. The remaining coordinates have $Y/3^M\to\Lambda>0$ in the reals and $Y/3^M\to0$ dyadically. The product calculation (4) applies exactly, including after a column deletion and the consequent change in the 3-adic linear form. Multiply the whole vector by $U$ to clear denominators. This does not change the product, since $U$ is a $P$-unit, and the new integer maximum norm is at most $C3^M e^{o(M)}$. A fixed negative power saving therefore remains. The same finite-dimensional descent proves the contradiction.

**Positive length does not distinguish escape.** The same length diverges on the trivial convergent tail $q_i=1$, and in fact on every positive eventually periodic tail as $M-N\to\infty$. Pass to a repeated pair of endpoint values $x,y$ on that finite tail, and add their prime factors to $P$. A putative bounded positive representation would yield, for fixed $k$ on a subsequence,

$$1=\frac{3^{M-N}x}{2^{A_M-A_N}y}+\sum_{j=1}^k\frac{s_j}{2^{A_M-A_N}y}.$$

All terms are positive units of one fixed prime set. Evertse–Schlickewei–Schmidt gives only finitely many such nondegenerate tuples, whereas the first coordinate's 3-adic valuation tends to infinity. In particular $4^l-3^l$ on the fixed point one has unbounded positive rational $P$-unit length as $l\to\infty$. The positive conclusion of FS4 therefore holds for **every** fixed positive odd source on the stated proportional windows, by the elementary periodic/nonperiodic dichotomy. An upper bound on positive length cannot be a universal descent certificate.

### FS5. A signed version that does distinguish the two cases

Allow nonzero rational $P$-units of either sign. The *cancellation ratio* of a presentation $C=\sum_{j=1}^k s_j>0$ is $L=\sum_j |s_j|/C$. Fix $P,K,B$ and $R>\log_2 3$. On an escaping orbit all sufficiently late windows $[N,\lfloor RN\rfloor)$ exclude signed presentations with both $k\le K$ and $L\le B$.

To check this, delete any nonempty zero-sum sublists. This preserves $C$ and decreases both length and total absolute value. The augmented tuple consisting of the retained terms and $-C$ is then nondegenerate (use the complementary subsum when necessary). The denominator lemma extends to these signed terms: with $g$ the positive gcd of the absolute cleared numerators, the height of the primitive tuple is **at least** $UC/g$. The outside-product bound is still $V_P(C/g)\le C/g$. Evertse again gives $U\ll_{P,K,\epsilon}C^\epsilon$, including the bounded exceptional primitive tuples. The bounded cancellation assumption gives $|X_j|/3^M\le B(u_M q_M-u_N q_N)\to0$; all the other steps of FS4 are unchanged. More generally this proof works on every sequence of windows satisfying the clock and bounded aspect-ratio conditions of FS4, with a uniform bound on $L$.

Conversely, on every positive eventually periodic tail the two signed terms $2^{A_M-A_N}q_M$ and $-3^{M-N}q_N$ lie in one fixed prime group after adding the prime factors of the finitely many tail states. Put $H=\max q_i$ on the tail. The ratio of the positive term to the magnitude of the negative term is at least $(1+1/(3H))^{M-N}$ by the physical edge product, so $L\to1$. Thus for any fixed $R>\log_2 3$, the existence of fixed $P,K,B$ and infinitely many such bounded signed presentations is equivalent to eventual periodicity of the specified actual orbit. This includes hypothetical nontrivial cycles and supplies no independent upper bound for an arbitrary positive source.

**An unrestricted signed consequence for exponential excursions.** Fix $P$ and suppose an escaping orbit has $\limsup_{M\to\infty}(\log q_M)/M=\gamma>0$. There exist proportional windows along which the minimum length of an arbitrary signed rational $P$-unit presentation of $C_{N,M}$ tends to infinity, with no restriction imposed on its cancellation ratio. The same windows work for each fixed $P$.

Indeed, after zero-sum deletion the height is $U\max(C,\max_j|s_j|)/g$. For every fixed $k\le K$ and $d=1/(1+\epsilon)$, Evertse therefore gives, outside finitely many primitive tuples,

$$U\max(C,\max_j|s_j|)/g<(C/g)^{1+\epsilon}.$$

For all bounded-length presentations after pruning, including the finite exceptional primitive shapes by changing the constant, this bounds $U$ and $\max_j |s_j|/C$ by $O_{P,K,\epsilon}(C^\epsilon)$. The latter follows because $U\ge1$ and $g\ge1$; for an exceptional primitive shape $\max_j |s_j|/C$ is a fixed ratio. Since $C\ll 3^M$, their positive logarithms are $o(M)$. This controls unrestricted cancellation subexponentially but would not by itself imply $|X_j|/3^M\to0$ on an arbitrary escaping window.

Choose $M\to\infty$ with $\log q_M/M\to\gamma$, and $N=M-\lfloor\gamma M/(2b)\rfloor$, $b=\log(3/2)$. Here $0<\gamma\le b$ by $q_{i+1}+1\le(3/2)(q_i+1)$. The same inequality read backwards gives $q_i\ge \exp(\gamma M/3)$ throughout $[N,M]$ eventually. Thus

$$0<u_Mq_M-u_Nq_N=\tfrac13\sum_{i=N}^{M-1}u_i\ll M\exp(-\gamma M/3),$$

because the real sequence $u_i q_i$ is bounded. Also $(A_M\log2-N\log3)/M\to\gamma(\log3/(2b)-1)>0$ by (1). Multiplying the exponential bound on the normalized carry by the subexponential upper bound on the cancellation ratio now forces each normalized signed atom to zero in the reals. FS4's denominator control and two-place finite-dimensional descent finish the proof. If the escape has uniformly subexponential height, these exponential savings are unavailable; no unrestricted signed conclusion for that case has been established.

**What unrestricted cancellation would require.** Suppose a sequence of escaping windows satisfies FS4's aspect-ratio and clock margins and admits signed presentations of length at most $K$, without any cancellation bound. After pruning and passing to fixed length $k$, the preceding application of Evertse gives $\log U=o(M)$ and $\max_j|s_j|/C\le\exp(o(M))$. Thus every $X_j=2^{A_N}s_j$ has Archimedean size $O(3^M)\exp(o(M))$, and $X_j/3^M\to0$ at 2. The Subspace Theorem product (4) and denominator clearing continue to work, although individual real ratios need not tend to zero. Every fixed relation obtained has zero $X_0$ coefficient by the dyadic limit. Eliminate atom-only relations exactly as before until some relation involves $Y$; otherwise all columns but $X_0,Y$ would be removed, where a dyadic relation with nonzero $Y$ coefficient would imply $Y=0$, impossible. Re-expressing deleted columns if needed, on an infinite subsequence there exist **fixed rational coefficients** $b_j$ such that

$$2^{A_M-A_N}q_M=\sum_j b_j s_j,\qquad 3^{M-N}q_N=\sum_j(b_j-1)s_j.$$

Consequently both endpoint heights themselves have bounded signed rational unit-sum length for a single finite enlargement $P'$ of $P$ (include the finitely many nonzero coefficient factors). Conversely any two bounded-length signed $P'$-unit presentations of the endpoints give a bounded-length signed $P'$-unit presentation of the carry by its defining formula. Thus the uncontrolled short-sum alternative has a concrete arithmetic consequence on the fixed source's actual endpoints. No theorem putting arbitrary ordinary heights into that endpoint class, or ruling it out on every uniformly subexponential escape, is available here.

## 6. What the direct universal attempt fails to prove

Applying (5) to the entire $n$-step prefix with $P$ containing the prime divisors of $q_0$ leaves $V_P(q_n)\le q_n\le(3/2)^n(q_0+1)$ against tuple height $2^{A_n}q_n\ge3^n q_0$. For $d>\log(3/2)/\log3$, long prefixes are therefore precisely in Evertse's exceptional range. The number of coordinates increases with $n$. Evertse's fixed-dimensional statement has no uniformity excluding a coherent family of those exceptions. Even $q_0=1$ supplies exceptional prefixes in every dimension. FS1 overcomes the increasing dimension on windows with a bounded number of virtual errors by keeping only their atoms and the two endpoints. FS4 shows intrinsically that even arbitrary positive rational $P$-unit compression of the full local carry must fail at bounded length, but this also happens on the fixed point one. FS5 demonstrates that bounded signed length with controlled cancellation separates the cases. The construction of a signed certificate independent of prior convergence, or a universal argument against high signed complexity, remains missing.

A second attempted application would put the unknown $\Lambda$ in an Archimedean linear form, which would require its algebraicity. Even granting that hypothesis, the natural form at infinity $\Lambda3^n-2^{A_n}q_n$, together with the separate dyadic and triadic coordinate factors on $(3^n,2^{A_n}q_n)$, gives the product

$$\frac{\Lambda3^n-2^{A_n}q_n}{2^{A_n}}=\tfrac13\sum_{r\ge0}\frac{2^{A_{n+r}-A_n}}{3^r}\ge\tfrac13\sum_{r\ge0}(2/3)^r=1.$$

Subtracting the first fixed $k$ known future terms leaves at least $(2/3)^k$. The needed negative power of height is absent. FS1 uses rational forms only, moves the subtraction to the 3-adic place and obtains a saving at that place from the **same fixed** genuine endpoint. Its ordinary positivity and injectivity are used for the finite positive Archimedean limit, and ordinary integrality is used at 2.

A closing implication would be that every putative nonperiodic positive least counterexample must violate FS1 or FS2. No proof of that assertion, of universal triadic membership of the actual discounted scalar, or of nontrivial cycle exclusion has been supplied. PR193 `c6cb5e66516a86c33a757154983bbddc822510de` treats translated packing/high-complexity controls, PR194 `b1bf1f151a2da8936f80d229f132d0b7539ba42c` treats finite canonical phase occupation, and PR188 `f98262be4ea40068dc88c779a767a9400a8bcaa3` treats sharp carry charges and finite-completion countermodels. None is substituted here for a missing fixed-source hypothesis.

## Verification

`source_controls.py` checks the integer and rational identities on explicit ordinary segments and tracks, including exact signed cancellation. Both ordinary and optimized Python produced identical counts. The strict Lean 4.34.1 Std-only file `source_VirtualWindow.lean` proves the finite translated telescope after clearing a common denominator. Its theorem `Collatz.FixedSourceWindow.virtual_window` has axiom audit `[propext, Classical.choice, Quot.sound]`. This kernel does not formalize the infinite orbit assumption, prime-part bounds or either application of the Subspace Theorem.

## Primary analytic inputs

- J.-H. Evertse, *On sums of S-units and linear recurrences*, Compositio Math. 53 (1984), 225–244. Corollary 1, p.227 gives the outside-prime product bound. Theorem 4, p.231 states Schlickewei's finite-place Subspace Theorem in the form used for FS1. [Primary paper](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)
- J.-H. Evertse, H. P. Schlickewei and W. M. Schmidt, *Linear equations in variables which lie in a multiplicative group*, Ann. Math. 155 (2002), 807–836, Theorem 1.1, p.808. [Primary paper](https://doi.org/10.2307/3062133)
- F. Beukers and H. P. Schlickewei, *The equation $x+y=1$ in finitely generated groups*, Acta Arith. 78 (1996), 189–199, Theorem 1.1, p.189. [Primary paper](https://doi.org/10.4064/aa-78-2-189-199)
