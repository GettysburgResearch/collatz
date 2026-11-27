# Independent review of the signed-cycle merger

Base checkout `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, with the following worktree files frozen by SHA-256. PR #174 is used only to identify the reverse-closure section. Its possible all-source conclusion is not an input.

| File under `research/astra-global-closure-20261124/structural/` | Reviewed SHA-256 |
|---|---|
| `README.md` | `0a9770d5ce4b15f73574d7f8ac3c28e1d3e8470f2fc09ed99a08e044a8308d55` |
| `CycleShadows.lean` | `05ef6b77b2ce9d571c598e5a0e4a526be3412b844349476ec72408b0bf145e99` |
| `controls.py` | `779803c6e14b1698469b416616a13cedd751f15951713b8f4ed5f5459dfdf23c` |
| `OFFSET_BOUND.md`, final sharpened CS4 | `8158421e26c3573a96adb03f79e4b9feaad474efc52c6e86fde4478f64aee6fe` |
| `OFFSET_BOUND.md`, initial CS4 | `bbd1f04f95cf83867785ed7d5c3df91e35cbe1641b04e5e80c040696d8166bcd` |

| Clause | Verdict |
|---|---|
| CS1, genuine smaller partner and certified member arm | VERIFIED for the displayed guard and exact clocks. |
| CS2, no descent at either mixed point and the finite ordinary consequence | VERIFIED by written reconstruction. The all-walk statement is not among the Lean declarations. |
| CS2, existence and growth of shortest walks | VERIFIED on the constructed sequence with the specified choice of exponent range. |
| CS3, obstruction to a fixed-depth four-offset menu | VERIFIED for the stated menu. |
| CS4, necessary off-cycle offset | VERIFIED for the initial estimate and the final sixth-root estimate. The latter was suggested during this review and independently checked by the structural author. |

## CS1 and the prescribed ordinary sources

For an ordinary lift with $x+c=2^p w$, the sums after each matched parity step are divided by two and multiplied by three exactly on odd input steps. Thus $T^p(x)+S^p(c)=3^{a_p(c)}w$. The $-17$ cycle has seven odd inputs in eleven steps. The $-52$ arm has twenty odd inputs in its first thirty-three steps and then twenty-two in each block of thirty-three. The extra factor three in the member sum comes from $(3n-1)+52=3(n+17)$. This gives the stated exponent $22k-1$ on the member endpoint, even though its signed shadow count is $22k-2$. The magnitude-one arm gives the partner's endpoint $X+16$. The residual identity is $3^{k-1}(X+17)=Y+7$. Its mod-1024 guard gives $X=52$ modulo 1024, and 52 and 68 both reach 2 in ten steps with three odd inputs. Their lifts therefore meet at the same ordinary integer. The inequality $0<m<n$ follows from the two different binary powers and $k\ge148$. It does not require that $m$ has already been proved convergent.

For $p=33k,b=22k-1$, one unit congruence modulo $3^{b+L}$ simultaneously makes $(2^e+7)/3^b$ integral and $2^pu=18$ modulo $3^L$. The exact order of 2 is $2\cdot3^{b+L-1}$ by lifting $v_3(4-1)=1$ through cubing. Hence an ordinary positive exponent exists in each full period. This gives one integer $n$ with both local residues, the smaller partner, and a genuine power-of-two endpoint of the member arm. The witnesses can increase with $L$, as the statement requires. The construction gives no selector for an independently prescribed $n$.

## CS2 and the all-walk quantifiers

On a walk, an inverse followed by a forward move retraces algebraically. After cancellations the word is a forward prefix followed by an inverse prefix, and the first inverse step, if preceded by a forward step, uses the other branch. This makes the exit from the signed cycle immediate. A reverse branch off a cycle cannot return to it while it is an integral path in the signed inverse tree, since forward iterates of a cycle point stay on that cycle.

Until the reverse odd count equals the forward odd count $a$, the signed negative magnitude $B$ is an integer in the $17$-cycle's basin. While $i<a$, the first and second shadows differ by $(17+z)\alpha$ with $v_3(\alpha)>0$. The inverse-odd test therefore gives $B=1$ modulo 3, making $(2B+1)/3$ a genuine integral backward step. No integrality of the first shadow is needed after the equal-count level.

For $p>0$ there is at least one forward odd step since the first is at $17$. The product for $17\alpha/B$ charges each forward odd at its **target** and each reverse odd at its **starting magnitude**. The off-cycle starting magnitudes below 137 fall in the three displayed rows according to their first entrance edge. They cannot repeat on one branch. The possible on-cycle factor with argument 34 is compatible only with the row entering through $23\to34$, since it arises from that exact inverse exit. This last restriction is essential to the joint sorted comparison. It gives the common majorant on the first four inverse factors with arguments $31,34,46,124$. The ratios of the forward to majorant products through lengths one to four are, respectively,
$$
527/525,\qquad17918/17871,\qquad1156/1155,\qquad71672/71463.
$$
Every later forward argument is at most 136 and every later sorted reverse argument is at least 137. Fewer inverse odd factors only improve the comparison. Thus $17\alpha>B\ge17$ throughout this phase, so $\alpha>1$ and $(17+z)\alpha-B>z$.

At the equal-count level, $\alpha=2^m$ with integer $m\ge1$. The level shadow $y'=(17+z)2^m-B$ is a positive integer and $B$ is off the cycle. Thereafter the inverse path of $y'$ is an actual positive integer inverse path and the first shadow keeps magnitude at least one over the reals. A later $\alpha<1$ therefore requires an integer $1\le y''<17+z$ with $T^t(y'')=y'$ and $3^o>2^{m+t}$. The supplied table uses the harmless weaker non-strict inequality. At clock 23 every candidate $y''$ has reached 1 or 2. At all later clocks nonnegative forward additive terms bound the coefficient by $2/y''$; for $y''=1$ direct alternation bounds it by $3/2$. Those bounds are below the required $2^m$. The finite table for the other clocks yields only the cycle point 17 or the three magnitudes 26, 19, 28 in the 5-basin. All contradict the required off-cycle 17-basin level. The case $p=0$ separately works for $z=0$ by doubling alone, and for $z=1$ because the positive forward path back to 1 has multiplicative coefficient at most one.

For the ordinary lift, each forward step reduces binary precision by at most one, and an inverse step preserves it or improves it. Each inverse odd step reduces ternary precision by at most one, and forward/doubling steps preserve it or improve it. Hence all necessary guards remain available **before** each of at most $L$ steps. The two resulting affine evaluations differ by $\alpha(n-z)$, and $y\ge z$ and $\alpha\ge1$ give the claimed ordinary lower bound. This controls the full graph of shorter walks to any positive smaller value.

For $L=p=33k$ the all-walk obstruction needs only $p$ binary digits. The separate two-forward-arm obstruction then gives only $p-8$ protected clocks on each arm; these statements use different precisions. Reversing the true partner path after the common endpoint costs $21k+10$ steps in addition to $33k+10$ forward steps. Thus $33k<D(n)\le54k+20$. Choosing the exponent in one multiplicative-order interval starting at the order gives $\log_2e=(55k-2)\log_2 3+O(1)$ and $\log_2 n=e+O(k)$. This proves the asserted order of $D(n)$ on those lifts alone. Allowing arbitrarily large exponents for the same $k$ would invalidate that two-sided growth interpretation.

## CS3 and CS4

For CS3, $X+17\equiv7\cdot3^{1-k}$ at the stated binary precision. The obstructing progression thus lifts $-10$ in the main arm and $6,2,0,-3$ in the four tested arms. The four signed orbits are disjoint from the $-5$ cycle and remain separated mod 256. Binary valuation drops exactly once per matched forward step. With $d=k-1>0$ even and $e>2+v_2(d)$, the initial separation valuation is $2+v_2(d)$ by the standard squared-power valuation. This addresses the four-offset menu; it leaves arbitrary other partner choices open.

For initial CS4, an off-cycle target precludes any repeated state on the forward path. Inverting its odd steps gives the displayed product, and $(1+1/(2j))^2\le(2j+1)/(2j-1)$ proves the claimed square-root estimate. A sharper estimate also follows. Each distinct odd-step target $B_j=(3c-1)/2$ satisfies $B_j\equiv1\pmod3$. It cannot be 1, which is fixed by $S$. After sorting, $B_j\ge3j+1$ for $1\le j\le a$. Set $x=1/(6j+2)$. Bernoulli gives $(1+x)^{-6}\ge(1-x)^6\ge1-6x$, so
$$
 (1+1/(2B_j))^6\le(3j+1)/(3j-2).
$$
Multiplication gives a bound $(3a+1)^{1/6}$ on the entire product, including the empty product. Repeating the source-size inequality yields $b\ge(2187/2048)^{3k}/(63k+1)^{1/6}$ for the matched off-cycle partner. The proof is independent of the actual lengths of the reverse branches. Arbitrary other shapes of merger remain outside it.

## Independent computation and formal scope

The reviewer wrote a separate finite checker. It enumerated legal reduced mixed-coordinate words of total length at most 30 using rational arithmetic (49,549 words at $z=0$, 78,293 at $z=1$), confirming the multiplier and shadow inequalities. It independently recovered all three small entrance rows, the global maximum entrance time of 27, both post-level candidate tables and the four exact prefix ratios above. It followed nine full ordinary forward merger paths at $k=148,404,660$ with three positive $u$ values in each residue class. These nine physical checks use the broader member-divisible-by-1024 guard; they do not materialize a doubly exponential pure-power-family input. The root-unit congruence proves existence of that latter family. [Reviewer code](review_structural_controls.py) · [Executed counts](structural_review_counts.json)

The Lean source was inspected for what its declarations actually assert. Its signed-rail separation is all-clock under the indicated binary precision. The graph normal form, product domination, all-walk lower bound and double-logarithmic asymptotic are written results. The reviewer independently recompiled the frozen source with Lean 4.34.1 and warnings as errors. The command exited 0, printed nine axiom reports, and reported no `sorryAx`. Only `propext` and `Quot.sound` appeared. [Independent Lean replay](structural_lean_review.json)
