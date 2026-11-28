# Every finite inverse window admits a strictly better finite window

Use the ordinary unit inverse gaps $I_e(x)=(2^e x-1)/3$. Let $c_W$ be the minimum average gap for a rolling controller observing $W\ge2$ ternary digits, with a uniform fresh top trit after each inverse gap. Put $L=\inf_W c_W$. For the physical doubling/odd-inverse gain $\gamma_W$, $c_W=1/\gamma_W$. For every $W\ge2$ there is an explicit larger width with
$$
 c_{W+n}\ \le\ c_W-\frac{3^{-n}}n,\qquad
 H=3^{32W},\qquad n=32W\left\lceil\frac{256H}{32W}\right\rceil .     \tag{1}
$$
In particular **no finite window attains the unrestricted optimal cost $L$**. Every finite optimal policy can be improved, irrespective of whether $L$ equals the Shannon bound $a_*$. The estimate does not require adjacent widths to have different values. Its guaranteed gain is very small. The strict inequality concerns genuine original-source finite controllers; the comparison cycles in the construction are signed rationals.

## 1. The finite control and its bias

Put $N_W=2\cdot3^{W-1}$. At a residue $s$ and gap $e$, the two lower digits determine legality, and the successor is uniform on the three lifts of $I_e(s)\bmod3^{W-1}$. Only the least positive $e$ in a class modulo $N_W$ is needed because the successor is unchanged under adding $N_W$. Given any target low residue $v$, a positive gap $e\le N_W$ satisfying $2^e s=1+3v\pmod{3^W}$ exists since 2 generates the unit group. Thus from any initial row one can reach any target **full** row in mean at most three trials and mean total gap at most $3N_W$ by repeating this selection. The fresh top trit succeeds with probability $1/3$ at each trial.

The finite average-cost Bellman equation has a deterministic minimizing selector $f$ and a bias $V$ of span at most $3N_W$, with
$$
 c_W+V(s)=f(s)+\mathbb E[V(s')\mid s,f(s)].                       \tag{2}
$$
For the span bound apply the preceding hitting policy to nonnegative discounted costs and then follow the optimum from the target. The discount can only decrease the target value. Hence the difference of any two optimal discounted values is at most $3N_W$. Subtract the value at one row and let the discount tend up to one along a convergent subsequence. One-step costs are uniformly bounded, and the average gain is the limit of the discounted value multiplied by one minus the discount. Integration of the resulting Bellman inequality gives the average lower bound, and equality under the selector gives attainment.

Grouping the deterministic doublings before each legal physical odd inverse gives this gap problem. A finite physical optimal selector has positive gain (one legal gap of size at most four always exists), so its deterministic doubling stretches have finite length: an infinite doubling stretch would give a closed zero-gain cycle, contrary to the constant positive Bellman gain. Conversely a chosen finite gap can be executed by storing its deterministic doublings up to the next odd inverse. A stored finite plan is an admissible history-dependent window controller. Average finite occupations also give a stationary randomized rule with the same reward. Thus the reciprocal normalization agrees with Weaver's physical-window formulation. [Weaver 127, Theorem 11, especially equations (53)–(57)](https://rstation.ai/problems/collatz/papers/127/v1).

## 2. A cheap rational cycle that the row cannot follow

Fix any initial unit row $s\bmod3^W$. Choose $W$ legal gaps at most four from a positive odd representative of $s$, each leaving a unit. Such a gap always exists by the six unit residues modulo nine. These $W$ labels determine the starting residue $s$ irrespective of the unit continuation, since the forward contractions $A_e(y)=2^{-e}(1+3y)$ increase matching depth by one.

For a second length-$W$ block, start from the signed unit $-1$, take gap five to $-11$, and follow $W-1$ arbitrary legal gaps at most four. This block determines starting residue $-1\bmod3^W$ and has initial compulsory label five along the chosen word. Finish the period with $30W$ ones. Its total length is $m=32W$, and its total gap $S$ satisfies $S\le38W+1\le39W$. Repeat the period. The first $W$ ones also determine residue $-1\bmod3^W$, since $A_1(-1)=-1$.

The unique exact periodic source is the actual rational
$$
 r=\frac{C(w)}{2^S-3^m},\qquad
 C(w)=\sum_{j=1}^m3^{j-1}2^{S-S_j} .                             \tag{3}
$$
Indeed the contraction along the word has this fixed point and produces every shifted phase. All those states are ternary units, because each is a contraction applied to the remaining tail. The positive integer $D=3^m-2^S$ is odd and prime to three, since $S/m\le39/32<3/2<\log_2 3$. The numerator in (3), and in each cyclic shift, is odd. The comparison cycle therefore lies in the negative rational lattice $D^{-1}\mathbb Z$ and all its points have dyadic valuation zero. The displayed denominator need not be reduced.

From each such rational point $y$ there is a **unique true forward odd predecessor** for the inverse path: the previous label is $v_2(1+3y)$, since $1+3y=2^e x$ and the previous rational $x$ has dyadic valuation zero. The value $1+3y=0$ is excluded for a ternary unit. Thus a periodic orbit of these points has just one inverse edge staying on that cycle from every phase. This remains true when the written word is a multiple of its primitive period. In particular, the two phases with labels one and five are different rational states despite having the same observed row.

Run the deterministic selector $f$ on this **exact** starting rational $r$. It cannot follow a complete lap: at both marked phases it sees $-1\bmod3^W$ but would have to choose different labels. Once it exits, it cannot re-enter the cycle or reach any other periodic cycle. Indeed true forward iteration from every visited point goes back to the original cycle, whereas a true periodic point never leaves its own cycle in the forward direction. Any repeated state on the selected inverse path would create a true cycle. A repetition before exit would also mean that the complete primitive lap had been followed; the incompatible row recurs on each primitive lap. Hence **the entire baseline path has distinct states**.

## 3. A uniform finite cost separation

Every selected state is still of the form $z_j=-u_j/D$, with $u_j$ a positive odd integer: inverse integrality at three preserves the denominator, the sign stays negative, and $2^{e_j}u_j+D$ is odd. The $u_j$ are distinct. With $T_n$ the baseline total across $n$ steps, multiplication of the exact identities $3u_{j+1}=2^{e_j}u_j+D$ gives
$$
 3^n\le 3^n u_n
 =2^{T_n}u_0\prod_{j=0}^{n-1}\left(1+\frac D{2^{e_j}u_j}\right)
 \le 2^{T_n}u_0\prod_{j=1}^{n}(1+D/j)
 =2^{T_n}u_0\binom{n+D}{D}.                                      \tag{4}
$$
The inequality sorts the distinct positive $u_j$ and uses that the $j$th smallest is at least $j$. In particular any such infinite path has $\liminf T_n/n\ge\log_2 3$ for fixed $D$ and $u_0$. This is the real cost of choosing a wrong edge on the cheap rational cycle.

Take $H,n$ from (1), so $256H\le n\le257H$ and $D\le H$. The crude bound $u_0=C(w)\le3^{32W}2^{39W}\le2^{103W}\le2^H$ follows directly from (3) and $3<4$. Also
$$
 \binom{n+D}{D}\le\binom{n+H}H
 \le256^H(1+1/256)^{n+H}\le 2^{10H},
$$
since $(1+1/256)^{258}\le e^{258/256}<4$. From (4) and $3>2^{3/2}$, $T_n\ge 3n/2-11H$. The alternative periodic path on the same source has total $T'_n=(S/m)n\le39n/32$ because $n$ is a multiple of $m$. Consequently
$$
             T_n-T'_n\ge61H>3N_W+1.                              \tag{5}
$$
This proof uses the negative lattice only to produce an explicit finite witness. A sufficiently close positive odd lift executes both finite words with exactly the same integer exponents.

## 4. Improving the actual block policy

Start in any low $W$-row $s$ with its remaining trits Haar. Under $f$, (2) telescopes for $n$ steps to expected total plus terminal bias equal to $nc_W+V(s)$. Its full chosen $n$-word and terminal $W$ digits are determined by the first $W+n$ source trits. This follows by the exact affine multiplier of each fixed inverse gap; from the observed row the choice is fixed. On the single full cell $r_s+3^{W+n}\mathbb Z_3$ inside $s$, the baseline executes the word of Section 3. Replace it there by the periodic $n$-word from that section; keep the original baseline on every other cell. The alternative is legal and has fixed terminal $W$-row on that cell as well. The decrease in cost plus terminal bias on the replaced cell is at least one by (5) and the span bound. Its conditional Haar probability within row $s$ is exactly $3^{-n}$. Therefore each row of the modified stored block has
$$
 \mathbb E[\mathrm{cost}+V(\mathrm{terminal})\mid s]
       \le nc_W+V(s)-3^{-n}.                                       \tag{6}
$$
On each complete initial cell of depth $W+n$, either chosen word is fixed and its inverse affine image is Haar on the corresponding terminal $W$-cell. Thus a stationary distribution of the finite block-boundary chain, lifted by Haar, truly regenerates at every boundary. Average (6) over that law and cancel the bias. Divide the summed occupations of all $n$ phases by $n$ and disintegrate by state. The phase state/action densities are locally constant at depth at most $W+n$. Their initial and terminal state marginals telescope to equality, so disintegration gives a genuine finite stationary rolling policy of that width with the same mean. This proves (1). Every tested ternary cell has ordinary positive odd representatives, and the cost improvement is an average over actual Haar lifts of every starting row.

Weaver 127 establishes monotonicity and the limit of the finite optimal gains. Weaver 150 gives a quantitative strict gap from the entropy ceiling at every width. The asserted new gap in (1) is instead from the **actual unrestricted limit**, whose identification with that ceiling remains open. We found no primary predecessor for this strict nonattainment in those sources. [Weaver 127, Theorem 11](https://rstation.ai/problems/collatz/papers/127/v1) · [Weaver 150, Theorem 1](https://rstation.ai/problems/collatz/papers/150/v2) · [Weaver 229, worst-root cost](https://rstation.ai/problems/collatz/papers/229).
