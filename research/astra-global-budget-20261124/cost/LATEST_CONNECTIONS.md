# Exact comparison with a smaller converger and the selected phase window

**SOURCE-QUALIFIED written deductions. Universal closure OPEN.** Use the ordinary shortcut map. The base packet's cost files are frozen. PR203 is frozen at 3f2c89f12b057b8bb8655bd6fc794c772aa8b65d, specifically research/mixed-adic-basin-density-20261124/README.md (Git blob cef4fd6353912a1c8c780be6694d78db592cef8d) and fixed_target_depth_bank.md (86e77570121079a5fefffc65ad23442604bb0f44). The selected third-phase question is PR195 at 1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97, research/astra-global-closure-20261124/round5/head/README.md (e213b8205301b6040b9689cda0f07f627717287e).

The two deductions below use PR203's extracted joint fixed-total floor (F'). For an odd unit target $q$, a unit class $z\bmod3^p$, $1\le p\le\delta_*(b-1)$, and $|s-2b|\le\sqrt b$, there are at least
\[
 c\,2^s/(3^{b+p}\sqrt b)
\]
distinct physical odd predecessors $Y$ in that class. Each reaches $q$ in exactly $b$ odd steps and $s$ shortcut steps, with $Y=(2^s/3^b)(q-\beta)$ and $0<\beta\le F_*$. All constants are absolute at large $b$. The source for the analytic bound is [Weaver and Wren, paper 48 v2, Lemma 7 (76) and Theorem 8 (80)–(83)](https://rstation.ai/problems/collatz/papers/48). I inspected the cited interface; I did not independently establish the underlying analytic floor.

**Uniformity in the supplied ordinary target.** In (76) the random object is the gap word and there is no integer target parameter. Its lower bound holds for every beta residue above one fixed cylinder. To reach an arbitrary unit residue $r_\beta\bmod 3^{b+p}$, the proof of (80)–(83) prepends one gap $v\le2\cdot3^{h_0}$ placing $(2^vr_\beta-1)/3$ in that cylinder. At length $b-1$ the exact total $s-v$ is within $2\sqrt{b-1}$ of $2(b-1)$ for all large $b$ uniformly over this finite list of gaps. Multiplication by $2^{s-v}$ converts the fixed-total probability to a word count, and the central total has probability $\gg1/\sqrt b$. The resulting (F') holds simultaneously for all unit residues, with an absolute onset, whenever $p\le\delta_*(b-1)$. Now substitute $r_\beta=q-3^b2^{-s}z\bmod3^{b+p}$. This is a unit class for every positive odd unit $q$. Consequently there is no real-size restriction on $q$ in the floor. In the construction below the separate upper bound on $q$ is used only to control the size of the resulting ordinary lifts.

## Many true lifts that eventually match the exact clock and odd count of a fixed smaller source

Fix a positive integer $n$ and any fixed converger $y$, for example $y=1<n$. Write $\lambda(y)=2P_{\tau(y)}(y)-\tau(y)$, where $P_i$ counts the first $i$ odd inputs. At every sufficiently large precision $h$ there are at least $\exp(c h)$ different positive $m>n$, all at most $\exp(C h)$, such that

* $v_2(m-n)=h$ and their physical orbits share the initial $h$ parity bits with $n$.
* Every chosen $m$ first reaches 1 at the **same** clock $\tau=O(h)$ with the **same** odd count. At that very clock the fixed $y$ is also at 1 with precisely that odd count.
* These actual certificates have $\Theta(h)$ odd inputs after the original shared prefix.

Constants/onset may depend on $n,y$ and the imported floor. No convergence hypothesis is made on $n$.

Choose the residue $n+2^h\bmod 2^{h+1}$, forcing exact precision $h$ for every member. Refine by one bit so that the next, final input of the prefix is odd. This is possible since two lifts differing by $2^{h+1}$ have endpoints at clock $h+1$ differing by an odd power of three. For the refined residue $r\bmod 2^H$ with $H=h+2$ and $0\le r<2^H$, write its literal common affine profile
\[
 T^H(r+2^H t)=z+3^p t.
\]
Here $p\ge1$ is the actual odd count, $3\nmid z$ by the final odd step, and $z+1\le3^H$ by $2(Tx+1)\le3(x+1)$. Also $|p-P_h(n)|\le2$. The ordinary bound $T^h(n)\le 2^{2P_h(n)-h}n$ and positivity imply $2P_h(n)-h\ge-\log_2 n$ at **every** clock.

Let $e$ be the least eligible integer above or equal to $\max(e_*,\,2p-H+2-\lambda(y))$ with $e=2$ or $4\bmod6$, where $e_*$ is a fixed constant large enough that $q=(2^e-1)/3>F_*+1$ and $q>2$. This $q$ is an odd ternary unit, with first-hit clock $e$ and exactly one odd input before 1. Put
\[
 d=2p-H+2-e-\lambda(y),\qquad b=\lceil K H\rceil,\qquad s=2b+d .
\]
The lower score bound makes $d=O_{n,y}(1)$, and $e\le H+O_{n,y}(1)$. Choose $K$ with $\delta_*K>2$ and $K\log(4/3)>\log3+1$. Then (F') applies to the exact total $s$ and unit residue $z\bmod3^p$. Every counted $Y$ satisfies $Y\ge 2^d(4/3)^b(q-F_*)>3^H$, so $t=(Y-z)/3^p$ is a positive integer. Each gives a distinct $m=r+2^H t$ in the refined physical cylinder. The number of choices is at least $c\,2^d(4/3)^b/(3^p\sqrt b)\ge\exp(c' h)$, and $m\le2^H(1+2^s q)\le\exp(C h)$. For large $h$ all these sources exceed the fixed $n$.

Before first hitting 1 the path goes through the nontrivial $q$. Consequently its first-hit clock and odd count are
\[
 \tau=H+s+e=2(p+b+1)-\lambda(y),\qquad P_\tau(m)=p+b+1.
\]
In particular $\tau$ has the same parity as $\tau(y)$ and eventually exceeds it, so the trivial two-cycle gives $T^\tau(y)=1$ and $P_\tau(y)=P_\tau(m)$. This comparison achieves exact equality of integer grades, beyond congruences modulo a prescribed modulus.

There is also an unconditional lower bound on the necessary time after the shared prefix. For **any** certified $m>n$ of exact precision $h$, its state there exceeds $3^{P_h(n)}$ and the first hit is later than $h$ since $2^{\tau(m)}\ge m>2^h$. Thus
\[
 \tau(m)-h>P_h(n)\log_2 3
   \ \ge\ (h-\log_2 n)(\log_2 3)/2.
\]
The construction achieves the correct linear order in this clock. As one finite illustration at $n=27,h=4$, each of $189099,189867,190187$ first reaches 1 at clock 86 with 43 odd inputs, exactly the score of the source 1 at that clock. They fit $H=6,p=4,b=38,s=76,e=4,q=5$. This direct trace checks the algebra in one case, independently of the asymptotic floor.

At the common-prefix endpoint the original $n$ and the certified $m$ differ by $3^{P_h(n)}(m-n)/2^h$, which is strictly positive. Exact later synchronization was obtained for $m$ and $y$. The comparison therefore leaves this single $n$ out of the later meeting. Its $\Theta(h)$ tail odd steps also put the lifts outside the bounded-odd-tail Evertse theorem. Neither a fixed-source height budget nor closure of the equal-grade merger relation under this dyadic limit has been proved.

## A true third-phase lower bound in prescribed shorter real windows

Add PR203's optional source-qualified Diophantine input (D), namely $\|j\log_2 3\|\ge c_Dj^{-\kappa}$ with $\kappa=13.3$. For any fixed $0<\rho<1/(2\kappa)=5/133$, let $V=(\log X)^\rho$ and $W=X/V$. For every $Z\in[X,2X]$, the interval $[Z,Z+W]$ contains at least $c_\rho X/V^2$ ordinary sources of either **specified** first-hit parity to 1, for all sufficiently large $X$. This uses F' and D, with no separate predecessor-density assumption. PR202 at 3b10b24d12d4b349cb20f4cbc83086c8a09f807e already obtained a mesoscopic fixed-basin block statement over the wider range $\sigma<10/133$. The present claim concerns a quantitative count of a specified first-hit phase.

Choose $q=(2^e-1)/3\asymp V$ with $e=2$ or $4\bmod6$, large enough that $q\ge100(F_*+1)V$. The eligible exponents have bounded gaps, so both inequalities can hold with absolute implied constants. Then $q$ is nonperiodic and its first-hit clock is exactly $e$. Set $\alpha=\log_2 3$, and take consecutive depths $b$ starting at $\lfloor\log_2(Z/q)/(2-\alpha)\rfloor$ over a window of $N=\lfloor c\sqrt{\log X}\rfloor$ depths. For a sufficiently small absolute $c>0$, any integer $s$ satisfying
\[
             Z+W/3\le (2^s/3^b)q\le Z+2W/3
\]
automatically has $|s-2b|\le\sqrt b$. Requiring $s+e$ to have the desired parity gives an arc of length comparable with $1/V$ for the phase $b\alpha\bmod 2$. Restrict to even $b$ and divide this circle by two. The resulting consecutive indices rotate by the same $\alpha\bmod1$, with a fixed positive fraction of the original $N$ steps.

For completeness, take the first continued-fraction convergent denominator $Q\ge C_1 V$ of $\alpha$, with $C_1$ large enough for that arc. By (D) at the previous denominator, $Q=O(V^\kappa)$. Each block of $Q$ consecutive indices is within $1/Q$ of a translate of the $Q$-grid pointwise up to permutation, by the convergent error. It has $\gg Q/V$ hits of the arc. Since $V^\kappa=o(N)$, full blocks supply $\gg\sqrt{\log X}/V$ eligible depths uniformly over $Z$. For each choose one such $s$.

Use (F') with residue $1\bmod3$, hence $p=1$ in the floor. The predecessor $Y=(2^s/3^b)(q-\beta)$ then lies in $[Z,Z+W]$, since the correction is at most $(Z+2W/3)F_*/q<W/3$. Each eligible depth contributes $\gg X/(q\sqrt{\log X})$ distinct such sources. Different depths are disjoint because $q$ is nonperiodic under the odd map. Every source first hits 1 after $s+e$ steps, with the prescribed sign. Summing gives the claimed count. The Diophantine dependency is [Simons and de Weger, Lemma 12, citing Rhin](https://www.impan.pl/shop/publication/transaction/download/product/82263?download.pdf=).

For PR195 the permitted starting radius is only $\exp(j^\beta)$, $\beta<1/12$, at $X\asymp81^j$. The proven interval length here is of order $81^j/j^\rho$. At the smaller width the rotation arc would have length of order $\exp(j^\beta)/81^j$. The same depth bank has only $O(\sqrt j)$ phases: the total length of their inverse translates of such an arc tends to zero. Uniform placement for an arbitrary center cannot come from those depth choices alone. Taking $q$ fixed also leaves an allowed real offset on scale $X/q$; the cap in F' supplies no distribution for its position inside an exponentially thinner real interval.

There is a direct physical check on the quantifiers. Under F and PR203's synchronization input S, a positive fraction of ordinary block starts give all-$+$ blocks of length $\lfloor\exp(c\sqrt{\log X})\rfloor$ by the first-hit phase marking. Translating each start by half the block length is injective. For large $j$, every resulting distinct center has no minus label within radius $\exp(j^\beta)$. A nonconvergent target, if one exists, similarly supplies genuine all-bad interiors. Neither statement jointly enforces the required $(B,+)$ labels at both $x$ and $\lfloor x/81\rfloor$. A lower bound in the much shorter interval *conditional on that selected pair*, or some other transfer including both original endpoints, is still missing.
