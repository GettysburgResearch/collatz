# Which two prescribed targets can occur with positive frequency?

**PROPOSED.** Section 4 is an unconditional construction on positive ordinary integers. The density classification and linear lower estimate additionally use qualified analytic inputs. Use the shortcut map $T(2n)=n$, $T(2n+1)=3n+2$. The two actual residual arms
$$
 A(k)=9k+2,\qquad B(k)=81k+20=9A(k)+2,\qquad k\ge0
$$
are the iterates at clocks two and three of $36k+8$ and $72k+17$, respectively. Their required directed convergence implication remains open.

For positive odd units $a,b$ (odd integers prime to three), define
$$
 J(a,b)=\{k:\exists i,j\ge0,\ T^i A(k)=a,\ T^j B(k)=b\}.
$$
The clocks may differ. Call two targets comparable if one belongs to the forward orbit of the other.

1. **Joint hitting criterion.** $J(a,b)$ has positive natural density exactly when the targets are comparable. In that case its density equals the ordinary predecessor density of the upstream target. If each target reaches the other, their predecessor sets agree. For incomparable targets the count below $X$ is $O_{a,b}(X/\sqrt{\log(2X)})$.
2. **Uniform common first landings.** Fix any window ratio $1+\delta>1$ and clock modulus $d\ge1$. For every odd unit $a\le M$, every residue class $r\bmod d$, and every $X\ge C_{d,\delta}M$, at least $c_{d,\delta}X/M$ original parameters $k\in[X,(1+\delta)X]$ have both arms first landing at odd height at most $M$ at the same value $a$ and the same shortcut clock $t\equiv r\pmod d$. Landings and clocks start at $A(k),B(k)$. Section 3 gives a growing-target version in windows of relative width $O_{d,\varepsilon}(1/\log X)$ at an unbounded sequence of scales. Section 4 proves an unconditional lower count $c_{d,\delta}(X/M)^{2/5}$ at every fixed window ratio.
3. **Occupied joint atom of density zero.** The fixed ordinary parameter $k=3$ belongs to $J(29,263)$. Both targets reach one and have positive individual predecessor density in their respective residual arms. Nevertheless $J(29,263)$ has density zero, even with arbitrary independent hit times. Thus an existing physical pair, positive single-target masses and common basin membership can coexist with zero joint mass.

The finite arithmetic and the two concrete trajectories are certified in [PairedLanding.lean](PairedLanding.lean). The general density results use the written inputs identified below; the power lower bound (6) only uses the finite arithmetic and the elementary arguments here.

## 1. Classification at arbitrary independent clocks

The fixed-coefficient synchronization input says that $k$ and $3^ak+c$ synchronously merge by shortcut clock $h$ outside $O_{a,c}(2^h/\sqrt{1+h})$ residue classes on a complete binary grid. Success holds for every positive lift. Apply it separately to $(a,c)=(2,2),(4,20)$ on the same original parameters. On $[X,2X)$ take $h=\lfloor\frac12\log_2 X\rfloor$. An interval of length $X$ is covered by $O(X/2^h)$ complete grids. Except on $O(X/\sqrt{\log X})$ parameters, all three ordinary trajectories agree by $h$. Until then each is at least $k/2^h\ge\sqrt X$. Neither fixed target could already have been reached for large $X$.

On these same parameters, the paired test is exactly the scalar test that the orbit of $k$ visits both $a,b$. A deterministic trajectory can visit both only in their forward order. If $b$ is downstream of $a$, this scalar event is precisely membership in the predecessor set of $a$. Interchange the targets for the other order. For incomparable targets it is empty. Summing dyadically over $\sqrt X<k\le X$ and adding back the omitted parameters gives error $O_{a,b}(X/\sqrt{\log(2X)})$. The cited fixed-target result gives actual positive natural density at each odd unit. Summing over the initial dyadic valuation identifies this odd-relative density with the all-integer natural density for any fixed odd target.

The same argument bounds the total mass of all off-diagonal first-landing pairs together by $O(1/\sqrt{\log(X/M)})$ on $[X,2X)$ when $X/M\to\infty$. Use $h=\lfloor(\log_2(X/M))/2\rfloor$ and one common failure symbol for a missed floor. More generally, if either of two independently timed target visits occurs after a synchronous merger, that target and the other arm's target lie on one trajectory. The other visit may even precede the merger. This last assertion is kernel-checked.

At $k=3$ the two initial targets are $29,263$. They first reach one after 13 and 51 steps, respectively. Their finite closed forward traces show that neither reaches the other. At floor $M=263$ this source also occupies the off-diagonal first-landing atom $(29,263)$. Its limiting original mass is zero. Both corresponding diagonal atoms have positive lower mass by Section 3.

## 2. Routing each actual scalar source into a merged residual cylinder

The entire cylinder $k=64w+12$, $w\ge0$, satisfies
$$
 T^6 A(k)=T^6 B(k)=243w+47. \tag{1}
$$
The first arm consumes three odd inputs and the second consumes one. We need a positive $m\equiv47\bmod243$ that subsequently reaches a selected odd unit $y$. Its original parameter is $k=(64m-92)/243$.

Write $I_e(y)=(2^e y-1)/3$. From any positive odd unit $y$, at **every** prescribed total $E\ge1461$, two legal inverse steps of exponents $u,v\ge2$, in that order going backwards, give $u+v=E$ and
$$
 m=I_v(I_u(y))=(2^E y-2^v-3)/9\equiv47\pmod{243}. \tag{2}
$$
Indeed $2^E y-3-9\cdot47$ is a unit modulo $3^7$. Two has order $2\cdot3^6=1458$ modulo $3^7$. Its order modulo three is two, and $v_3(4^{3^j}-1)=1+j$ follows by cubing $1+3^{j+1}t$ with $3\nmid t$. Choose $2\le v\le1459$ representing that unit as $2^v\bmod3^7$, and put $u=E-v\ge2$. Reduction modulo three proves $I_u(y)$ is integral. Reduction modulo nine makes the second inverse integral, which forces $I_u(y)$ also to be prime to three. Both new states are odd, positive and at least $y$. The final state is a unit by its prescribed residue. The forward valuations are exact since both parent states are odd. In particular $T^E(m)=y$. The kernel checks ordinary legality of the two shortcut segments from the single full affine equation.

We may also prescribe the inverse odd depth $s\ge2$ and total $E\ge6(s-2)+1461$. Take $s-2$ legal inverse steps of exponents in $\{2,3,4,5,6\}$, then apply (2) to the remaining total. At $1\bmod3$ the candidates $2,4$ are integral, and at $2\bmod3$ use $3,5$. The larger candidate value is four times the smaller plus one, so one is a unit. All inverse states are nondecreasing. For $y\ge2$ the final size satisfies uniformly
$$
 m=(2^E/3^s)y(1+O(1/y)). \tag{3}
$$
Indeed after $j$ inverse steps the state $y_j$ satisfies $y_j-1\ge(4/3)^j(y-1)$. The relative correction factors are $1-1/(2^{e_j}y_{j-1})$. The sum of their deficits is $O(1/y)$, which bounds the product error for every $s,E$. General fixed-total modular routing with better budgets as precision grows is prior work. Here the ternary precision is a fixed consequence of (1).

## 3. Prescribing the common landing and its clock in a shrinking window

The sole density input here is Weaver's *First-landing bounds and canonical inverse laws for Collatz*, Theorem 14 under its written selected-block and averaged joint-mixing assumptions. For absolute $c>0,C\ge4$, there are at least $cY/M$ odd $n\in(Y/4,Y]$ whose first odd iterate at or below $M$ is the prescribed odd unit $a\le M$, for every $Y\ge CM$. The proof includes periodic targets. Fourier Wren's valuation-slice atom floor for unmarked Syracuse words is an input to that source. [Weaver, Theorem 14 and Appendix A](https://rstation.ai/problems/collatz/papers/12) · [Wren, Theorem 2](https://rstation.ai/problems/collatz/papers/10/v3)

Fix $d\ge1$. There are constants $K_d,C_d,c_d>0$ with the following property. For any continued-fraction denominator $Q$ of $\theta=\log_2(3)/d$, put
$$
 Y=X2^{-(K_d+7Q)}.
$$
Whenever $Y\ge C_d\max(M,Q,1)$, the interval $[X,2^{C_d/Q}X]$ contains at least
$$
 c_d\,\frac{Y}{M(Q+1)} \tag{4}
$$
different original parameters satisfying the paired first-landing and clock conditions in result 2 above.

Take every one of the incoming $n$ from the stated theorem. Set $y=n$ if it is a unit, and $y=4n+1$ otherwise. We have $Y/4<y\le4Y+1$ and $y$ is an odd unit. In the latter case $3(4n+1)+1=4(3n+1)$ shows the two sources have the same next odd iterate. Both stand above the floor, so the first odd landing of $y$ is still $a$. Denote its actual shortcut clock by $t_y$, which is allowed to depend on the full future of this $n$.

For a convergent $p/Q$, the $Q$ residues $j\theta\bmod1$, $0\le j<Q$, come within $2/Q$ of every circle point by comparison with the equally spaced grid $jp/Q$. Every translate has the same property. Write $H=\log_2(243X/(64y))$. Choose $s\in\{2,\ldots,Q+1\}$ and an integer $E\equiv r-6-t_y\pmod d$ so that
$$
 |E-s\log_2 3-H-5d/Q|\le 2d/Q. \tag{5}
$$
This requires rounding $s\theta+(H+5d/Q-r+6+t_y)/d$ to an integer. Since $H=K_d+7Q+O(1)$ over the entire initial source range, increasing $K_d$ once makes the depth and total admissible in (3).

Construct $m$ from this depth and total. Equation (3) and $k=(64m-92)/243$ give an additive error in $\log_2 k$ of at most $d/Q$ for large enough $C_d$, since $m\ge y\ge C_dQ/4$. Equation (5) then puts $k\in[X,2^{8d/Q}X]$. Both initial arms exceed $M$ throughout the first six clocks since $T^i z\ge z/2^i$ and $k\ge X$. They coincide at $m$. Every odd state on the route from $m$ to $y$ is at least $y>M$. The first landing on both arms is therefore exactly $a$ at shortcut clock $6+E+t_y\equiv r\bmod d$.

For multiplicity a given $k$ determines $m$. For each possible $s$, its actual $s$-th accelerated odd iterate determines $y$, and there are at most two original $n$ for that $y$. The $Q$ allowed depths give at most $2Q$ preimages, proving (4). This argument also permits a different requested residue $r$ for each incoming $n$, retaining the same lower count for the resulting family.

For fixed $\delta>0$, take one $Q$ large enough to fit the requested window and absorb its finite cost into the constants. For the shrinking example, fix $0<\varepsilon<1$, take unbounded denominators $Q$, and put $X=2^{DQ}$ with $D=16/\varepsilon$. For large $Q$, $Y\ge X^{1-\varepsilon/2}$ and all $M\le X^{1-\varepsilon}$ are admissible. The relative window width is $O_{d,\varepsilon}(1/\log X)$ and the lower count is $\gg_{d,\varepsilon}X^{1-\varepsilon/2}/(M\log X)$.

## 4. An unconditional supply from a monotone inverse tree

**PROPOSED written theorem; the finite cut inequality is kernel-checked.** Without analytic inputs, the same paired first-landing and clock conclusion holds at every fixed ratio, with lower count
$$
              c_{d,\delta}(X/M)^{2/5},\qquad X\ge C_{d,\delta}M. \tag{6}
$$
For the shrinking windows of Section 3, put $S=\max(M,Q,2)$. For $Y\ge C_d S$ an unconditional lower count is
$$
              \frac{c_d}{Q}\left(\frac{Y}{S}\right)^{2/5}. \tag{7}
$$
Only (4) and its linear fixed-ratio consequence use the cited first-landing theorem.

To see the elementary supply, use every legal odd inverse exponent $2\le e\le20$ that gives a unit. Relative to a positive unit $z$, each such child has height below $\lambda_e z$ with $\lambda_e=2^e/3>1$. For $z>1$ each child strictly exceeds its parent. Set $\gamma=2/5$. For each starting unit $z$, the **complete four-step legal words**, with all four new states units, satisfy
$$
             \sum_w\left(\prod_{e\in w}\lambda_e\right)^{-\gamma}>1. \tag{8}
$$
Here is an exact finite certificate. Take $D=10000$ and $W_e=\lfloor D(3/2^e)^\gamma\rfloor$. The bound $W_e^5\,2^{2e}\le 9D^5$ is checked for each letter. Start with $N_0=(0,1,1)$ on residues modulo three. In going from $j-1$ to $j$, evaluate on representatives $0\le r<3^{j+1}$. Set $N_j(r)=0$ on nonunits, and otherwise take
$$
 N_j(r)=\sum_{\substack{2\le e\le20\\ 2^er\equiv1\bmod 3}}
   W_e\,N_{j-1}\!\left(\frac{2^er-1}{3}\bmod 3^j\right).
$$
A unit lift of $r$ has exactly this integrality test and this child residue at the preceding precision. A nonunit child contributes zero, including at the last step. Thus $N_4(r)/D^4$ is the sum of the rounded lower products on actual legal words. The least numerators on unit classes at depths $1,2,3,4$ are respectively
$$
  7482,\quad 83\,609\,556,\quad 873\,163\,981\,825,\quad
  10\,261\,932\,046\,877\,717.
$$
The last exceeds $D^4=10^{16}$. Lean checks all 243 final residues and every edge-weight inequality by kernel reduction. The separate integer Python control reconstructs the weights by fifth-power bisection and returns the displayed minima. This proves (8).

Choose a single odd unit child $z=I_e(a)>C'_d S$ with $z\le C''_d S$, independently of $a\le M$. For example choose the least $e\ge2$ of the parity giving integrality for which $I_e(a)>C'_d S$. The resulting height is $O_d(S)$ since $a\le S$ and a move from $e$ to $e+2$ multiplies height by four and adds one. If the chosen value is a multiple of three, increase $e$ by two once. The child $z$ first lands below the odd floor at $a$. Every strictly increasing outward path from $z$ retains that same first landing, irrespective of whether $a$ itself is periodic.

On the tree from $z$, give each four-step child probability proportional to $\Lambda_w^{-\gamma}$, where $\Lambda_w=\prod_{e\in w}\lambda_e$. By (8) the conditional probability is at most $\Lambda_w^{-\gamma}$. Write $F=(2^{20}/3)^4$ and assume $Y\ge Fz$, increasing $C_d$ in (7) to guarantee this. Stop on first exceeding the budget $B=Y/(Fz)$ in the cumulative product of the $\Lambda_w$. It is a finite cut because each multiplier is at least $(4/3)^4$. At a stopped word the product is at most $FB$ and its probability at most $B^{-\gamma}$. Therefore there are at least $B^\gamma$ leaves, all of height $\le zFB=Y$. Distinct stopped words give distinct ordinary heights. The forward odd path and its exact valuations uniquely decode a word ending at $z$, and strict growth in the inverse tree prevents two different depths for one height.

Each of these unit leaves is a permissible $y$ with $C'_dS<y\le Y$ and the prescribed first landing. Apply exactly the phase adjustment (5) and the same six-step cylinder. The original proof of (5) only needs the **lower** estimate $H\ge K_d+7Q-O(1)$ to guarantee enough valuation for the route. Smaller $y$ merely permits a larger total. The height approximation in (3) is uniform in that total, and now $y>C'_dQ$. Each resulting $k$ determines $m$ and can come from at most $Q$ leaves, one per permitted depth $s$. This gives (7) uniformly over $a,M$. With $Q$ fixed as a function of $d,\delta$, we have $S\ll_{d,\delta}M$ and $Y\gg_{d,\delta}X$, giving (6).

## 5. Where the fixed-source proof stops

If a specific $k_0$ violates the directed implication, the two entire futures of $A(k_0),B(k_0)$ are disjoint. In particular their ordered pair of fixed initial targets is incomparable, as are the two first odd states reached by stripping their initial powers of two. Those odd states are ternary units. Result 1 permits that occupied joint atom to have zero limiting mass. Our routed first-landing cohort lies in a merged cylinder and cannot meet a fiber retaining disjoint labeled futures. A large cardinality for one exact ordered future fiber supplies many witnesses of that same record, with no lower proportion in growing original cutoffs. Section 1's concrete example rules out deriving that proportion merely from fixed-source existence and marginal densities even when the targets share a component. No original witness in distinct components is known.

A positive joint hitting density for the fixed targets of any hypothetical violating pair would contradict Section 1. No such lower bound for that special class follows from the routed equal-target estimates. The [pointwise grade bound](../transfer/README.md) constrains histories at a fixed source. It does not itself supply a positive fraction of original parameters realizing the same distinct targets.

### Inputs and relationships

* PR146, commit f431078244e868dc699fad011044f0d5e7f76437, supplies the finite-grid estimate at the two fixed affine comparisons. Its ordinary use appears at PR197, commit 6eb986b0ce0b1836a356474d25d709ed4e948b67. [Growing additive gaps, (1)](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) · [Macroscopic pair closure](https://github.com/GettysburgResearch/collatz/blob/6eb986b0ce0b1836a356474d25d709ed4e948b67/research/ayh-resource-reset-20261124/literature-step/MACROSCOPIC_PAIR_CLOSURE.md)
* For scalar predecessor natural densities at fixed odd units, Weaver's paper 12, sections 1 and 8–9, uses the stated Valbuena component and first-passage results. Its Theorem 14 yields positivity. These are imported analytic results. [Primary account](https://rstation.ai/problems/collatz/papers/12)
* PR195, commit 1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97, requires whole ratio-five return words for its ordinary descendant target. PR192, commit 301b84491ffafe283bd63d104c1b60ddf0e97f06, treats the singular marked law and its electrical side cut. Our construction enters a merged ratio-nine cylinder, which supplies a different ordered terminal event. [PR195, §5](https://github.com/GettysburgResearch/collatz/blob/1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97/research/astra-global-closure-20261124/round5/renewal/README.md) · [PR192](https://github.com/GettysburgResearch/collatz/blob/301b84491ffafe283bd63d104c1b60ddf0e97f06/research/astra-two-centre-20261124/basin.md)
* PR197, commit 6eb986b0ce0b1836a356474d25d709ed4e948b67, retains ordered futures on original source fibers. PR193, commit 67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e, gives the actual directed reduction. [Head incidence](https://github.com/GettysburgResearch/collatz/blob/6eb986b0ce0b1836a356474d25d709ed4e948b67/research/ayh-resource-reset-20261124/two-class-descent/HEAD_INCIDENCE.md) · [Paired projection](https://github.com/GettysburgResearch/collatz/blob/6eb986b0ce0b1836a356474d25d709ed4e948b67/research/ayh-resource-reset-20261124/two-class-descent/ADAPTIVE_PAIRED_PROJECTION.md) · [Directed reduction](../../astra-global-resolution-20261124/rewriting/SingleReturn.lean)
* For general fixed-total modular routing at varying ternary precision, see Weaver, Theorem D. The elementary fixed-precision route (2) permits arbitrary large total with just two inverse odd steps. [Primary manuscript](https://rstation.ai/problems/collatz/papers/37)
