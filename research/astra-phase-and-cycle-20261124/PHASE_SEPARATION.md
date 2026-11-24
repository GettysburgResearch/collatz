# Repulsion of the actual centered scalar from the ternary grid

**Status.** Proposed written results, 24 November 2026. The finite lower-end run kernel in `OneRun.lean` was compiled with Lean 4.34.1. The scalar/grid consequences and finite-word realization below are written deductions. Collatz remains open.

## Objects and dependencies

Fix one positive odd integer $q=q_0$. Write $a_i=v_2(3q_i+1)$ and $2^{a_i}q_{i+1}=3q_i+1$. PR182, `research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md`, R10-G1, at `f94a2ae1caba9a1857feda892ee1779695eea9d2` proves for the actual discounted gap series

$$h_i=\sum_{t\ge0}a_{i+t}3^{-t-1},\qquad \tfrac12<h_i\le1+\tfrac13\log_2q_i,\qquad h_{i+1}=3h_i-a_i.$$

Use PR188 `research/scalar-carry-cocycle-20261124/SCALAR_COCYCLE.md`, definitions at `beed685ab713923191ae40c9559bf7400298d2d3`. Set $c_i=\lceil h_i-1/2\rceil-1$, $y_i=h_i-c_i-1/2\in(0,1]$, $b_i=1+3y_i-y_{i+1}\in\{1,2,3\}$. These give the right-closed ternary digits $b_i-1$ and

$$a_i+c_{i+1}=b_i+3c_i.\tag{1}$$

In particular $2^{c_i}\le q_i$. Indeed $c_i<1/2+(\log_2q_i)/3$, which is at most $\log_2q_i$ if $q_i\ge2$, while $q_i=1$ gives $c_i=0$. Put $X_i=q_i/2^{c_i}\ge1$. The exact normalized step is

$$2^{b_i+2c_i}X_{i+1}=3X_i+2^{-c_i}.\tag{2}$$

The normalized contraction is also present in PR182 round 12 at `cbec52dde5bed390a693310dd04e911033ba0cc9`, `research/phase-packing-round12-20261124/README.md`, section 4. Its finite recognition and cycle-classification theorems for contracting rational phases are antecedents. Here we bound closeness of the **actual phase** to each side of the ternary grid at every finite shift. No rationality, escape, stationarity or convergence assumption is used.

## PS1. Two endpoint runs at their actual starting height

If $b_j,\ldots,b_{j+L-1}$ are all 1, then

$$2^{L+1}\le q_j+1.\tag{3}$$

If $c_j=0$, (1) and $a_i\ge1$ force all the carries through the endpoint to be zero and all $L$ actual gaps to be one. Iteration gives $2^L(q_{j+L}+1)=3^L(q_j+1)$. Endpoint oddness and coprimality imply $2^{L+1}\mid q_j+1$.

If $c_j>0$, write $t$ for the time to the first zero carry amongst these states, or $L$ if no zero is reached. During those $t$ steps (2) and $X_i\ge1$ give $X_{i+1}\le X_i/2$. If a zero was reached, the preceding divisibility applied to the $r=L-t$ remaining steps implies $X_{j+t}=q_{j+t}\ge2^{r+1}-1\ge2^r$. If no zero was reached, $r=0$ and $X_{j+t}\ge1=2^r$. Hence $q_j\ge2^{c_j+L}\ge2^{L+1}$. This proves (3), including an empty run. The Lean proof `one_run` proves the zero-carry divisibility and the bound $2^{c_j+L}\le q_j$ together by induction on $L$.

If $b_j,\ldots,b_{j+L-1}$ are all 3, then

$$4\,8^L\le(5q_j-1)3^L.\tag{4}$$

In that run (2) gives $X_{i+1}\le(3X_i+1)/8$, hence $X_{i+1}-1/5\le(3/8)(X_i-1/5)$. Use $X_{j+L}\ge1$ and $X_j\le q_j$. In particular a right-closed ternary tail consisting entirely of twos is impossible at every actual source.

## PS2. Two-sided fixed-source approximation

Let $\alpha=\log_2 3$, $\gamma=\log 3/\log(8/3)$ and $\delta=1+\log(3/2)/\log(8/3)=1.4133901052\ldots$. The maximal initial run of zeros in the ternary digits of $y_j$ has a finite length $L$ by (3). The first nonzero digit implies $y_j>3^{-(L+1)}$, using the right-closed positive remainder. Similarly a maximal run of twos of length $L'$ is finite by (4), and the first smaller digit implies $1-y_j\ge3^{-(L'+1)}$. Thus

$$y_j>(q_j+1)^{-\alpha},\qquad 1-y_j\ge\tfrac13\left((5q_j-1)/4\right)^{-\gamma}.\tag{5}$$

In particular $0<y_j<1$; the centered phase never belongs to the ternary grid, including at powers of three in the denominator. This is distinct from triadic membership of the **uncentered** scalar $h_j$ in the convergence criterion of PR182.

For $n\ge0$, write $3^ny_0=D_n+y_n$ with $D_n$ the integer coded by the first $n$ digits. Since $q_n+1\le(3/2)^n(q_0+1)$, (5) yields, for **every** integer $k$ on the indicated side,

$$\begin{aligned}
y_0-k/3^n&>(q_0+1)^{-\alpha}3^{-\alpha n} &&(k/3^n<y_0),\\
k/3^n-y_0&\ge\tfrac13\bigl(5(q_0+1)/4\bigr)^{-\gamma}3^{-\delta n} &&(k/3^n>y_0).
\end{aligned}\tag{6}$$

Indeed the closest distances are $3^{-n}y_n$ and $3^{-n}(1-y_n)$. For the lower bound use $1+\log_2(3/2)=\alpha$. For the upper bound use $1+\gamma\log_3(3/2)=\delta$. Thus any real with infinitely many closer approximations from the appropriate side at an exponent strictly above the corresponding threshold is excluded as the actual centered phase of any one positive odd starting value. For example $\sum_{s\ge2}3^{-s!}$ is excluded by truncation from below; its complement in one is excluded by truncation from above. The restriction is on denominators $3^n$ only. Equality of an exponent in (6) has not been characterized.

## PS3. The local lower-side exponent is optimal

Take $q=2^k-1$, $k\ge2$. Its first $k-1$ actual gaps are one and $q_{k-1}=2\,3^{k-1}-1$, as follows by iterating $q_i+1=2^{k-i}3^i$ while $i<k-1$. The discounted recurrence gives

$$0<h(q)-1/2=3^{-(k-1)}(h(q_{k-1})-1/2)\le 3^{-(k-1)}(1/2+\log_2(2\,3^{k-1}-1)/3).$$

The bound is $O(k3^{-k})$; for all sufficiently large $k$ the carry therefore vanishes and $y(q)=h(q)-1/2$. For any $s<\alpha$ the product $y(q)(q+1)^s$ tends to zero along these ordinary sources. This proves the sharp exponent in the local, changing-source, lower-side inequality (5). Neither the upper-side exponent nor the fixed-source exponents in (6) are proved optimal.

## PS4. Every finite canonical word occurs at a positive ordinary source

For any $m\ge1$ and $w\in\{1,2,3\}^m$, let $B=\sum w_i$ and $r=\lceil\log_3(8(m+1))\rceil$. There is a positive odd source

$$q<2^{B+r+1}$$

whose first $m$ **actual** canonical letters equal $w$, with zero carries through time $m$. Prescribe the physical gap list $w$ followed by $r$ ones. For completeness, any finite positive gap list of sum $A$ has exactly one odd source class modulo $2^{A+1}$. Starting with terminal odd residue $1\bmod2$, prepend a gap $a$ to a tail class $s\bmod2^t$ by solving $3q+1\equiv 2^a s\pmod {2^{a+t}}$. Since 3 is invertible this has a unique solution, which is odd and has valuation exactly $a$. Choose the positive representative below the modulus.

At the end, $q_{m+r}+1\le(3/2)^{m+r}2^{B+r+1}$, so $\log_2 q_{m+r}\le4m+2r+1$ since $B\le3m$. Also $r\le m+2$ by $3^{m+2}\ge8(m+1)$ for $m\ge1$. Thus $0<h_{m+r}-1/2<8(m+1)\le3^r$. Across the final $r$ unit gaps the exact recurrence gives $0<h_m-1/2<1$. Reading the initial word backwards, $h_i=(w_i+h_{i+1})/3$ maps the open strip $(1/2,3/2)$ into itself for each $w_i$. Every corresponding carry vanishes, and (1) identifies the canonical and actual letters. This proves density in the real unit interval of centered scalar phases of positive odd integers. The representing integer can change with each word; no infinite prescribed word is thereby realized.

## PS5. Every finite canonical word occurs in the predecessor tree of one

Every word $w$ of length $m\ge1$ is also the canonical prefix of an explicitly constructible positive odd source whose first hit of one occurs at odd time $m+2$. If $D_w$ is the base-three integer with digits $w_i-1$, the actual centered phase and raw scalar of this source are exactly

$$y_0=\frac{D_w+7/18}{3^m},\qquad h_0=\frac52+\frac{D_w+7/18}{3^m}.\tag{7}$$

Thus for each $m$ the values are an entire equally spaced grid with one prescribed point in each length-$m$ cylinder. The source bound is larger than in PS4, $q_0<2^{B+5+2\cdot3^{m+2}}$. Here is a direct construction.

**A two-step terminal family.** For $0\le t<3^m$ put $a=2t+1$, $k=2-3t+3^{m+2}>0$, $z=(4^k-1)/3$, and $s=(2^a z-1)/3$. Since $k\equiv2\pmod3$, $z\equiv2\pmod3$ and $2^a z\equiv1\pmod3$. Both $s$ and $z$ are odd positive integers and $s\to z\to1$ has the exact gaps $(a,2k)$. From $h(1)=1$ it follows that

$$h(s)=(3a+2k+1)/9=8/9+2\cdot3^m,$$

independent of $t$. Meanwhile $s$ runs over a complete residue system modulo $3^m$. To see this define the rational function of the integer parameter

$$F(t)=\frac{2\cdot4^{2-2t}-2\cdot4^t-3}{9}.$$

It belongs to $\mathbb Z[1/2]$: the numerator is zero modulo nine because $4^{2-3t}\equiv7\pmod9$. Since $v_3(4^{3^{m+2}}-1)=m+3$, the actual integer $s$ is congruent to $F(t)$ modulo $3^m$. Here and below a rational number with denominator coprime to three has its usual modular interpretation. $F(0)=3$, $F(1)=-1$, $F(2)=-31/8$, representing the three distinct residues modulo three. For $h>0$ divisible by three, the exact difference is

$$F(t+h)-F(t)=-\frac{2\cdot4^t(4^h-1)}9\left(1+4^{2-3t}\frac{4^h+1}{4^{2h}}\right).$$

The bracket is $6\bmod9$, so its valuation is exactly one. Also $v_3(4^h-1)=1+v_3(h)$: for $3\nmid u$, expand $(1+3)^u$ modulo nine, and each cubing raises the valuation once, since $x^2+x+1\equiv3\pmod9$ for $x\equiv1\pmod3$. Therefore $v_3(F(t+h)-F(t))=v_3(h)$. Combined with the three base residues, this proves $F$ induces a permutation at every modulus $3^m$.

**Attaching any prefix.** The list of actual gaps $w$ requires one terminal residue $R\bmod 3^m$. One way to obtain it is to use the positive source from PS4 and take its position-$m$ endpoint modulo $3^m$. If two candidate endpoints agree modulo $3^m$, undoing each gap by $x\mapsto(2^{w_i}x-1)/3$ preserves integrality and reduces the congruence modulus by one power of three. When initialized with $s$ the intermediate values are positive odd integers: if $x$ is positive odd and $2^{w_i}x-1$ is divisible by three, the positive quotient is odd. The permutation supplies $s\equiv R$, hence an ordinary prefix followed by the terminal pair. There is no earlier visit to one because one is fixed and $z>1$.

At time $m$ the actual centered representative $h_m-c_m$ is exactly $8/9$ with $c_m=2\cdot3^m$. Reading backwards through $w$ shows that $c_i=2\cdot3^i$ for $0\le i\le m$: after removing that integer part the update is $f_i=(w_i+f_{i+1})/3$, which preserves $1/2<f_i<3/2$. The physical and canonical letters therefore coincide on the prefix, with $y_m=8/9-1/2=7/18$, giving (7). The size estimate follows from $q_0<2^B s<2^{B+a+2k}$ and $a+2k=5-4t+2\cdot3^{m+2}$. This proof provides a literal complete convergence witness, whereas the more economical bound in PS4 does not constrain the eventual orbit. Even within the known convergent basin, no finite ternary word can be forbidden at every positive source.

## PS6. Exact scalar fibers on the two-step convergence layer

For every integer $d\ge1$, put $H_d=(6d+2)/9$. Exactly $d$ positive odd sources with first hit of one at odd time two have raw scalar $H_d$. Their residues modulo any $3^e$ have counts differing by at most one. This describes every reduced-denominator-nine raw scalar on the two-step layer.

Indeed any such two-step source has gaps $(a,2k)$, where $k\ge1$, $z=(4^k-1)/3>1$, and $2^az\equiv1\pmod3$. Its scalar is $(3a+2k+1)/9$. Since $z\equiv k\pmod3$, even $a$ implies $k\equiv1\pmod3$ and the displayed numerator is divisible by three. Odd $a$ implies $k\equiv2\pmod3$ and the numerator is $2\bmod6$. In the odd case a prescribed $H_d$ forces $a=2t+1$ and $k=3d-1-3t$, for $0\le t<d$. All these values work, are distinct by their initial valuations, and $z\ge5$ so the first hit is exactly two.

Write $F_d(t)=(2\cdot4^{3d-1-2t}-2\cdot4^t-3)/9$. For those $d$ parameters this expression is the actual integer source. For all nonnegative $t$ it belongs to $\mathbb Z[1/2]$. Modulo three $F_d(t)-F(t)$ is constant in $t$: it is $2\cdot4^{2-2t}(4^{3(d-1)}-1)/9$, whose last quotient is integral and whose preceding power of four is always one modulo three. In the difference calculation for PS5, $4^{2-3t}$ is replaced by $4^{3d-1-3t}$, also $7\bmod9$. The valuation argument is unchanged. Thus $v_3(F_d(t)-F_d(u))=v_3(t-u)$ for every pair of distinct nonnegative integers. On a complete interval of length $3^e$ each residue occurs exactly once; the shorter final interval has no collisions. This proves the asserted discrepancy for the entire depth-two fiber.

In particular, choose $d=3^{m+1}+1$ to recover PS5's exact terminal scalar, with three sources in every residue modulo $3^m$ and one additional source in one residue. Knowing the **exact**, unrounded scalar and the exact remaining time to one still does not recover the state modulo $3^m$. This counts different convergent sources, and gives no estimate for the collision law of positions on one putatively escaping orbit.

## Boundary and reproducibility

`phase_controls.py` checks the finite inequalities on literal positive odd trajectories reaching one, includes observed nonzero carries and resets, verifies the exact finite-word witness construction and checks the sharpness family. It uses exact integer or rational arithmetic. Finite testing supports the written deductions and cannot prove bounds at every depth. `OneRun.lean` imports `Std` alone. Lean 4.34.1 accepted `one_run` and `one_run_length`, both with dependencies `[propext, Quot.sound]`. Their inputs are precisely the ordinary equation, valuation positivity, endpoint oddness, carry equation and carry floor displayed above. The identification of these inputs with the actual infinite scalar and the real approximation bounds is written here.

A candidate nonperiodic scalar can avoid long extreme digit runs. For example, arbitrary aperiodic ternary words with digit runs of zeros and twos bounded by one easily satisfy fixed positive separation from the two endpoints at every shift. To decide Collatz by this approach one still needs an arithmetic property of every possible actual nonconvergent orbit that contradicts (5) or (6), or a different global obstruction. The admissibility of every finite prefix in PS4 prevents a finite forbidden-word proof without also using source height or additional state.
