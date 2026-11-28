# A lifetime lower parity bound and the complete lower half at long observation clocks

For an ordinary source \(1\le n\le N\) write
\[
 L=\log_2 N,\qquad f_t(n)=Q_t(n)-t/2\quad (t\ge0)
\]
for the centered count of odd shortcuts on its actual path. There are absolute \(C,A_0>0\) such that, with \(L\) sufficiently large and \(A_0\sqrt L\le a\le L/2\),
\[
 \#\{1\le n\le N:\ \inf_{t\ge0} f_t(n)\le-a\}
     \le C N L^3\exp\!\left[-\frac{32}{25\cdot68^2}\frac{a^2}{L}\right].  \tag{1}
\]
For \(a>L/2\) this set is empty. Upper deviations of the centered count play no part in the lifetime claim.

Consequently for **every fixed** \(\kappa\ge8192\) and **every fixed** \(0\le p<1/2\), at \(t=\lfloor\kappa\log_2N\rfloor\) the full ordinary \(t\)-bit type satisfies the fair-coin Chernoff upper bound
\[
 \Pr_{1\le n\le N}(Q_t(n)\le pt)\le 2^{-t(1-H_2(p))}
                                                                    \tag{2}
\]
for all sufficiently large \(N\). The numerical multiplier is sufficient, not an asserted transition. This gives the entire lower half of the book's R6 upper bound at long clocks; it is compatible with any future of the physically visited integers. The earlier sparse-edge result covers explicit sectors also at \(\kappa=1.01,2,4.82\) and every other fixed \(\kappa>1\). The general upper half, and the full two-sided bound at the book's suggested clocks, remain open. [Polson–Sokolov, R6](https://github.com/VadimSokolov/collatz/blob/5840497a23fc0d64127b850aea68862d7c93f2b7/book/chapters/ch10h_ratchets.tex#L783-L785) · [Sparse ordinary lower edge](NATIVE_LOWER_TYPE.md).

## Source-qualified finite record input

Use Weaver 191 **v2**, §§2–4, specifically its adaptive proof through equation (7). Write \(\theta=\log_2 3,\ D=1-\theta/2\) and
\[
 m_0=\frac{D-1/8}{2\theta\sqrt3},\qquad \rho=47/48,\qquad
 E=\frac{1}{2(1-2^{-1/16})}<12 .
\]
For \(B_0\le B\le L/2\), the paper starts a positive ordinary source interval of length \(N\) at time zero with slope one. Reject a source when the next inspected word of length \(h_i\) at its record has a prefix with centered count of absolute value larger than \(m_0\sqrt{B h_i}\). Its equation (7) counts all rejected original sources, even though inspections can overlap, by
\[
                          O(NL^3e^{-2m_0^2B}).                         \tag{3}
\]
The argument pools the actual source multiplicities at each common time and odd count. We retain that input with its time-dependent test. Its text after (7) gives \(h_i\le L\rho^i/2\), and each traversed portion of the retained path satisfies its own prefix test. At the final record \(v\), the affine representation is \(T^v n=s_v n+e_v\) with \(0\le e_v\le E\), \(s_v N\le2^B\). Those two inequalities are the record definition and the cutoff \(U_v\le B\). The later small-source discard in the proof of the **relative** first-passage theorem is unnecessary for our initial interval: each \(n\le N\) already gives \(T^v n\le2^B+E\). [Weaver, *Collatz first passage in translated intervals*, v2, §§2–4](https://rstation.ai/problems/collatz/papers/191/v2).

## Ordinary continuation through every future clock

For a retained actual start the prefix tests in (3) and a geometric series give
\[
      |f_u(n)|\le A\sqrt{LB},\qquad
      A=\frac{m_0}{\sqrt2(1-\sqrt\rho)}<1.04,\quad 0\le u\le v.         \tag{4}
\]
The shortcut height product gives \(1\le T^r y\le y2^{-r}4^{Q_r(y)}\) at every ordinary positive \(y\). In particular \(Q_r(y)-r/2\ge-\log_2(y)/2\), irrespective of how long its orbit continues. Exact additivity after \(v\) yields
\[
   \inf_{t\ge0} f_t(n)\ge -A\sqrt{LB}-\tfrac12\log_2(2^B+E)
                    \ge -A\sqrt{LB}-\tfrac12(B+1)                    \tag{5}
\]
for \(B\ge\log_2 E\). Applying the same product at the initial state gives the deterministic cap \(-L/2\) over its entire lifetime.

Choose \(B=(16/25)a^2/L\). For \(a\le L/2\),
\[
 A\sqrt{LB}+(B+1)/2
 < (1.04\cdot0.8+0.16)a+1/2 < a
\]
once \(a\) exceeds a fixed absolute constant. Choose \(A_0\) to cover \(B_0\) and \(\log_2 E\). Inequalities \(1/68<m_0<0.0152\), \(1-\sqrt{47/48}\ge1/96\), and \(\sqrt2>1.41\) suffice for the constants above. For example \(1.5849<\theta<1.5850\) and \(1.7320<\sqrt3<1.7321\) verify the bounds on \(m_0\). Substituting in (3) proves (1).

For (2) put \(a=t(1/2-p)\). The deterministic cap settles \(a>L/2\). Otherwise \(0\le1/2-p\le L/(2t)<0.0001\) for all large \(N\). In this interval the binary divergence in natural units satisfies
\[
 d(p\Vert1/2)\le 2.01(1/2-p)^2 ,
\]
by its second derivative \(1/[p(1-p)]\), zero value and zero derivative at \(1/2\). Thus \(t d(p\Vert1/2)\le (2.01/8191)a^2/L\), strictly less than the decay exponent in (1). At fixed \(p<1/2,\kappa\), \(a^2/L\) grows linearly in \(L\), absorbing the polynomial prefactor with a strict margin. At \(p=1/2\) the fair upper bound is the trivial bound one. All dates in (1)–(2) are true native dates on the original positive trajectories. The record clock is used only inside the proof of the all-time event.
