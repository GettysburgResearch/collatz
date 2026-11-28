# Half-logarithmic cell density at a specified ordinary real fibre

Fix a positive odd unit $a$ whose odd orbit is nonperiodic in the sense that $a$ itself never returns to $a$. Let $R$ have its canonical inverse-law probability $\mu_a$ on the absolute real affine intercept. Let $I_r(R)$ be the cell containing $R$ in any grid of width $r$ on the line, with any deterministic origin that may depend on $r$. Under the counted-synchronization, local passage and trace inputs specified below,
\[
     \frac{\log(\mu_a(I_r(R))/r)}{\log\log(1/r)}
                        \longrightarrow \tfrac12
                \quad\text{in }\mu_a\text{-probability as }r\downarrow0.       \tag{1}
\]
Moreover $\mu_a$ has a countable exhaustion up to null sets by restrictions $\lambda$ for which, with a fixed finite exponent $C$ and a constant depending on the restriction,
\[
          \lambda(I)\ll_\lambda |I|\,[1+\log(1/|I|)]^C
                    \qquad(0<|I|\le1/2) .                               \tag{2}
\]
These statements concern individual, prescribed integer roots of ternary Haar measure zero. Estimate (1) specifies a typical bin under the real fibre itself. It gives no uniform integrability assertion for the squared cell densities.

Use the [canonical inverse-path proof, PR193 at aa686899](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md) and the [resulting real-fibre identification at that pin](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md). The former proves the fixed-root canonical path bounds and supplies its precise stopped-rung transfer from Valbuena's ordinary first-passage law. The physical trace upper used here is [the good-site sparse-set estimate (3) and omitted-hull size](TRACE_POWER_SETS_AND_OFFSET_WINDOW.md), including its Weaver 102/v1 and 9/v2 sources. The real cover for the lower bound is [Weaver, Paper 175/v1, §7, (11) and the grid construction after (11)](https://rstation.ai/problems/collatz/papers/175).

## Subsegments on genuine inverse paths

Use reverse gaps $E_i$, totals $S_n$, $A_n=3^n2^{-S_n}$, inverse states $X_n$, partial real intercepts $R_n=a-A_nX_n$ and $D=\log(4/3)$. The pinned theorem gives almost surely
\[
 \log A_n=-Dn+O_\omega(\sqrt{n\log\log n}),\qquad
 h(X_n)\le n^{5/2+\epsilon}\text{ eventually for every fixed }\epsilon>0.
                                                                         \tag{3}
\]
At fixed $n$ each legal word has probability $A_n h(X_n)/h(a)$. For every nonperiodic true inverse segment $a-R_n\in[c_0a,a]$ by uniform simple-path packing.

There are absolute $d,C>0$ such that almost surely for all sufficiently large $n$, simultaneously for all $l\ge0$,
\[
       \log(A_{n+l}/A_n)\le-dl+C\log(n+2),\qquad E_n\le C\log(n+2).  \tag{4}
\]
Here is the transfer. In the frozen construction put $x_i=M^{\alpha^i}$, $s_i=\log x_i$, $\alpha=1.001$. The inverse stage runs between the last backward visits through $x_{i-1}$ and $x_i$. In physical forward time these are the first upper and lower landings, in the opposite order. On the local logarithmic reference source $V_i$ in $[x_i^\alpha,x_i^{\alpha^2}]$, the first $L_i=\lfloor0.1s_{i-1}\rfloor$ forward gaps couple to iid geometric gaps with exponential-in-$s_{i-1}$ failure. Outside $O((\log s_i)^{-3})$ reference failure both passages occur within $L_i$, the stage length is $(s_i-s_{i-1})/D+O(\sqrt{s_i\log\log s_i})$, and its earlier source-prefix states through each such visit are above $e^{s_{i-1}/2}$. These are the local stage estimates proved at the frozen pin.

For a single iid increment $Y=\log(3/2^E)$ choose $0<d_0<D$ and small $v>0$ so $b=\mathbb E e^{v(Y+d_0)}<1$. For a proposed subsegment of length $l\ge1$, the probability it has sum greater than $-d_0 l+B\log s_i$ is at most $s_i^{-vB}b^l$. Sum over $O(s_i)$ starting positions and all lengths. Also bound the probability of a gap exceeding $B\log s_i$ by $O(s_i 2^{-B\log s_i})$. Taking $B$ sufficiently large makes both errors $O(s_i^{-2})$. These subsegment properties persist on chronological reversal.

The bounded test transferred from $V_i$ is whether the actual path from the upper landing to the lower landing violates these estimates, with the same passage-failure handling as in the pinned proof. Valbuena's equation ct-stage-TV adds $O(s_i^{-c})$ from arbitrarily high sources. Conditioning on the fixed root basin divides the upper bound by its positive natural density $d_a$. The resulting natural inverse law $Q_a$ and $P_{h,a}$ have globally bounded Radon–Nikodym derivative in both directions. All errors are summable in $i$ since $s_i$ grows geometrically. Thus almost every canonical path has these inequalities on every subsegment of every sufficiently late stage. [Valbuena, ct-stage-TV and ct-time-law at a7275d5](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex).

For a segment crossing stage boundaries, every complete interior stage has length comparable to its $s_i$, and its $B\log s_i$ error is absorbed into half its negative linear term. The first and last partial stages cost $O(\log(n+2)+\log(n+l+2))$, because the endpoint indices of stage $i$ are $s_i/D+O_\omega(\sqrt{s_i\log\log s_i})$ and $s_{i-1}/D+O_\omega(\sqrt{s_i\log\log s_i})$. The elementary bound $\log(n+l+2)\le\log(n+2)+\delta l+O_\delta(1)$ with small fixed $\delta$ absorbs the last linear error. Within one stage the same statement follows directly. This proves (4).

## A bounded-tail prefix at each real resolution

Let $N=\log(1/r)$. On a fixed high-probability path set impose uniform constants and starting thresholds on (3), (4), and the preceding endpoint estimates; these sets exhaust probability one. Let $\tau-1$ be the last index with $A_{\tau-1}>r$. It exists by (3), and at large $N$, $r N^{-C_1}\le A_\tau\le r$ by the gap bound in (4) and $\tau\asymp N$. Choose $0<d_1<d$ and take $n_*$ minimizing $-\log A_n-d_1 n$ over $n\ge\tau$, using its first minimum in case of a tie. It exists by (3). Equation (4) bounds $n_*-\tau\ll\log(N+2)$. By the defining minimum, $A_{n_*+l}/A_{n_*}\le e^{-d_1 l}$ for every $l\ge0$, so the real remainder obeys $0\le R-R_{n_*}\le C_1 A_{n_*}$. Moreover
\[
 rN^{-C_2}\le A_{n_*}\le r,\qquad
 n_*=N/D+O(\sqrt{N\log\log N}),\qquad
                      c_0a/r\le X_{n_*}\le aN^{C_2}/r .                \tag{5}
\]
The upper bound on $A_{n_*}$ uses the last exit, since all $n\ge\tau$ have $A_n\le r$. The lower bound follows from the minimum being no larger than its value at $\tau$, hence $A_{n_*}\ge A_\tau e^{-d_1(n_*-\tau)}$. Insert these bounds in (3) to obtain the index range. The integer height assertion follows from $X_n=(a-R_n)/A_n$.

At each $r$-cell there are $O(\sqrt{N\log\log N})$ possible $n_*$ and $O(\log N)$ totals $S_{n_*}$ per index by (5). At a fixed index and total, put $A=3^{n_*}2^{-S_{n_*}}$. The compatible real prefixes whose endpoints can contribute to the cell lie in an interval of length $r+C_1 A$. Their spacing is at least $A$ since $R_{n_*}=a-AX_{n_*}$ and each ordinary endpoint determines its word at that depth. Each such cylinder has mass $A h(X_{n_*})/h(a)$. Thus restricting the selected paths to $h(X_{n_*})\le H$ gives cell mass at most
\[
              C_a r H\sqrt{N\log\log N}\log(2+N).                     \tag{6}
\]
This is a union bound over whole cylinders containing the selected paths. The index $n_*$ need not be a stopping time. Taking $H=N^3$ with a fixed constant enlargement using the pathwise (3) gives (2), for instance with $C=4$ at large $N$, on each uniform high-probability set. The finitely larger radii only modify its constant.

## Ordinary sparse sites control the selected trace in probability

For each fixed $\epsilon>0$, at the selected index in (5) the mass with $h(X_{n_*})>N^\epsilon$ tends to zero on each fixed uniform path set. This estimate uses a bounded visit test through natural first passage; the canonical path is not sampled by unweighted spatial density.

For an octave $[Y,2Y]$ in the physical range of (5), $\log Y\asymp N$. Write $A_Y$ for **all** unit sites there with $h>H$, $H=N^\epsilon$. For fixed $1<p<2$ the good-site mass bound (3) of the cited physical sparse-set paper, evaluated on $A_Y\cap G_Y$, gives
\[
 |A_Y|/Y\ll_p H^{-p}+O_J(N^{-J}/H)+O(Y^{-1/64}\log Y).              \tag{7}
\]
Indeed if the fraction on $G_Y$ is $u$, then $Hu\ll u^{1-1/p}+O_J(N^{-J})$; the last term in (7) includes the whole omitted set. This use needs no bound on the amplitudes at its omitted sites.

By (5) and the endpoint-index bounds, $n_*$ lies in one of $O(1)$ predetermined ladder stages whose $s_i$ are comparable to $N$. More precisely the intervals $[s_{i-1},s_i]$ enlarged by $O(\sqrt{N\log\log N})$ must contain $N+O(\sqrt{N\log\log N})$. Their spacing is a fixed positive multiple of $N$ for $s_i\asymp N$. The constants here may depend on the fixed uniform path set. Use the actual indicator that the stage, from its upper landing to its lower landing, visits any site in the union of the $A_Y$ for the $O(\log N)$ octaves in (5). This is a bounded function of the upper landing label and its actual future. Under the local reference $V_i$, discard failure of the good local passage, whose probability tends to zero. Its individual source weights are at most $C/(s_i v)$ at each actual start $v$. At each forward time $j\le L_i$ of a retained visit $v\mapsto z$ the source correction $b_j(v)\ge1/2$, as all earlier heights exceed $e^{s_{i-1}/2}$. Hence the probability contributed at that time in the indicated octave is at most
\[
   \frac C{s_i}\sum_{z\in A_Y}\rho_j(z)/z
          \ll_{p'} s_i^{-1}(|A_Y|/Y)^{1-1/p'},\qquad 1<p'<2 .
\]
This is the positive integer column bound and the finite-quotient Haar moment from PR193's proof (3). Here $3^j\le 3^{0.1s_{i-1}}<Y$, so the full-period comparison applies. If an endpoint octave in (5) only partially intersects its range, using the whole octave remains an upper bound. Summing $O(s_i)$ clocks and $O(\log N)$ octaves costs at most $C\log(2+N)\sup_Y(|A_Y|/Y)^{1-1/p'}$, tending to zero by (7). Stage-TV adds $O(s_i^{-c})$ before conditioning on $B_a$ and passage to its inverse law, as above. A finite number of stages, the fixed $1/d_a$ factor, and the equibounded change from $Q_a$ to $P_{h,a}$ preserve convergence to zero. The event $h(X_{n_*})>H$ on the uniform path set implies one of these actual visits. No unbounded trace test has been transferred through a total-variation error.

## Matching typical cell bounds

Given any small error tolerance, choose a uniform path set of mass at least one minus that tolerance. At every sufficiently fine scale the restriction on $h(X_{n_*})\le N^\epsilon$ then omits at most this tolerance plus $o(1)$. By (6) each cell of this restricted submeasure has mass at most $C_a r N^{1/2+\epsilon}\sqrt{\log\log N}\log(2+N)$. The number of cells with *full* mass greater than $rN^{1/2+2\epsilon}$ is at most $1/(rN^{1/2+2\epsilon})$. Their restricted mass tends to zero, and the full mass there has upper limit at most the omitted tolerance. Send the tolerance to zero. This proves the upper half of (1).

For the other direction, Weaver's sets $V_{L,1/i}(a)$ consist of cells of mesh $2^{-8L}$ with total length $O_a(i/\sqrt L)$. Almost surely the real endpoint belongs to all those sets beyond an eventual $L_0$ for some $i$. By fixing $i,L_0$ large enough this property has probability arbitrarily close to one, using nesting as $i$ increases. For $r$ choose $L$ so the mesh is comparable to $r$ within a factor $2^8$. The set meets at most $O_{a,i}(1/(r\sqrt N))$ grid cells of width $r$, at any origin. Those among them with full mass at most $rN^{1/2-\epsilon}$ have combined mass $O_{a,i}(N^{-\epsilon})$. Let the omitted tolerance vanish to obtain the lower half of (1).

## Periodic unit roots

The same conclusions (1), (2) hold at a periodic positive odd unit. Under the canonical law each full reverse circuit through the root has the same probability $\omega<1$, so almost surely there is a finite first exit into a nonperiodic inverse branch. Conditional on any fixed such finite prefix, the subsequent mark is the canonical mark at its nonperiodic child transformed by the fixed real affine map $r\mapsto B+A r$, $A>0$. The entire periodic fibre is therefore a countable probability mixture of these fixed affine images. [Weaver 19/v2, (F9)–(F12)](https://rstation.ai/problems/collatz/papers/19).

For (2) keep finitely many components and high-mass restrictions in each, then exhaust the mixture. For the lower half of (1) the full cell mass is at least the individual component weight times its own cell mass. The affine map only changes the width by a fixed factor and translates the grid. For the upper half fix a finite submixture of mass near one. In each of its members, discard samples lying in cells where its own mass exceeds $rN^{1/2+\epsilon}$, absorbing the fixed scale in the exponent, with $N=\log(1/r)$. The loss tends to zero by the nonperiodic result. Each cell of the resulting combined submeasure has mass at most $rN^{1/2+\epsilon}$, since its component weights sum to at most one. The number of cells in which the full mixture exceeds $rN^{1/2+2\epsilon}$ is at most its reciprocal. The retained mass there is $o(1)$, and the initially omitted mass may be arbitrarily small. This proves the periodic statement. The same argument works for any countable mixture of fixed affine images of these probability laws.
