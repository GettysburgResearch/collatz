# A stopped fair size walk carrying the complete true endpoint

**PROPOSED, source-qualified ordinary-source theorem.** Write \(T\) for the genuine shortcut map. For uniform \(n\le Y\) put \(F_t(n)=\sum_{j<t}1_{T^j n\ {\rm odd}}\), and let \(P_t(Y)\) be the joint probability law of \((F_t(n),T^t n)\). Use real cutoffs, normalized by \(\lfloor Y\rfloor\). Take iid fair bits \(\xi_j\), \(B_j=\sum_{i=1}^j\xi_i\), and define
\[
   L_j=\log X-j\log2+B_j\log3,\qquad
   \tau_H=\inf\{j\ge0:L_j\le H\}.
\]
Choose \(\log X>H\ge2\), integers \(t\ge d\ge2\), and set \(J=(t-d)\wedge\tau_H\). Conditional on the entire fair path, choose a fresh uniform ordinary integer \(m\le e^{L_J}\). Then
\[
 \left\|P_t(X)-
    \mathcal L\big(B_J+F_{t-J}(m),\,T^{t-J}m\big)\right\|_{\rm TV}
           \le C_A\big(H^{-A}+d^{-A}\big)                           \tag{1}
\]
for every fixed \(A>0\), **uniformly in the tested time and initial source size**. On the crossing branch \(e^{L_J}\in(e^H/2,e^H]\). On the other branch the true residual time is exactly \(d\). This is a distributional replacement at a stopping line in a fair auxiliary size walk. The walk's bits are not asserted to be the initial bits of the sampled Collatz path. The terminal pair on each side is defined by genuine positive-integer trajectories.

For the count marginal alone there is a simpler all-time estimate. Put \(D=\log(4/3)\), \(a_1=D/2\), \(\mu=1/a_1\), \(L=\log X\), and \(g=\mu L-t\). For \(g\ge1\),
\[
  \|\mathcal L(F_t(n))-\operatorname{Bin}(t,1/2)\|_{\rm TV}
     \le C_A(1+g)^{-A}+C\exp[-c g^2/(1+t)].                           \tag{2}
\]
In particular the **raw integer count**, before any scaling or smoothing, is asymptotically binomial in total variation throughout \(t\le\mu L-g_X\), \(g_X/\sqrt L\to\infty\). The weak Gaussian limit immediately before the critical window is already in the concurrent PR213 packet. Formula (2) additionally controls arbitrary moving subsets of lattice counts. The proof of (1)–(2) uses signed short-time transport and elementary parity arithmetic, with no fixed-target Gaussian, minimum law or hypothesis on the fates of positive trajectories. [PR213, earlier weak precritical and critical distinctions, a743bd04](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/mass/CRITICAL_NATIVE_COUNT.md)

## The signed starting trit at any residual time

Let \(\psi\) have mean zero mod three and \(|\psi|\le1\). For each \(t\ge1\) and \(Y\ge2\),
\[
 \left\|Y^{-1}\sum_{n\le Y}\psi(n)
                 \delta_{(F_t(n),T^t n)}\right\|_1
       \ll_A (1+\log Y)^{-A}+(1+t)^{-A}.                               \tag{3}
\]
For the count marginal alone the second term can be dropped, also at \(t=0\).

First use odd sources on any subinterval of \([Z,2Z)\). Set \(k=\lfloor\min(\log_2 Z,t)/64\rfloor\); bounded \(k\) is covered by the trivial bound in (3). The signed native short-time estimate gives \(O_A(k^{-A})\) for the sum norm of the joint true odd endpoint \(U^k x\) and physical total \(S_k\), weighted by \(\psi(x)f_k(x)/x\), where \(f_k\) is the genuine product of \(3v/(3v+1)\) on these odd departures. It applies to every subinterval with the same constants. The exceptional original mass where \(S_k>4k\) is \(O(e^{-c k}+2^{4k}/Z)\) in reciprocal normalization, by native binary cylinders. On the good paths all visited sites exceed \(Z2^{-4k}\), so \(1-f_k\ll k2^{4k}/Z\). Push the joint signed measure on good cells through
\[
       (s,y)\longmapsto(k+F_{t-s}(y),T^{t-s}y).
\]
This contracts the sum norm and supplies the exact desired label on the good sources because \(s\le4k\le t\). Restore the discarded sources by their unsigned mass, and remove \(f_k\) using its displayed estimate. Partial summation on the original intervals now removes \(1/x\) at a cost \(O(Z)\) before normalizing by \(Z\). This proves (3)'s bounds on odd octaves and their subintervals. [PR195 signed physical endpoint and total, (3), 3fa7ef4a](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/MARKED_FIBRES.md) · [Original short-time and large-total estimates, same pin](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/PHYSICAL_SOURCE.md)

For all inputs write \(n=2^e x\), \(x\) odd. Discard \(n<\sqrt Y\) and exponents \(e>\min((\log_2Y)/4,t/2)\), with normalized cost \(O(Y^{-1/4}+2^{-t/2})\) after rounding. Split the remainder into original octaves. The odd inputs then have log scale comparable to \(\log Y\) and remaining time \(t-e\ge t/2\). Their residue function \(\psi(2^e x)\) still has ternary mean zero, and geometric normalization at each split gives a bounded total factor. This proves (3). For the count-only version when \(t\le(\log_2Y)/8\), use complete periods modulo \(3\cdot2^t\) directly: each native length-\(t\) parity cylinder is a single class modulo \(2^t\), and in complete periods its signed ternary total is zero. The unfinished period costs \(O(2^t/Y)\) in sum norm. At larger \(t\) the right side of (3) already has the desired one-term bound.

## Size recursion and occupation

Let \(S\) add one to the count coordinate and leave the endpoint fixed. Split source integers by their genuine first update. The even part is the lower-scale population. The odd map from positive odd \(n\) onto positive \(y=2\bmod3\), \(y=(3n+1)/2\), is a bijection. Apply (3) at the latter source scale with \(\psi=1_{2\bmod3}-1/3\). Replacing its cutoff \((3Y+1)/2\) by \(3Y/2\) and adjusting floor normalizations costs \(O(1/Y)\). Thus, for \(r\ge2\),
\[
 P_r(Y)=\tfrac12P_{r-1}(Y/2)+\tfrac12 S P_{r-1}(3Y/2)+R_r(Y),
 \quad \|R_r(Y)\|_1\ll_A(1+\log Y)^{-A}+(1+r)^{-A}.                  \tag{4}
\]
For count-only (4) holds also at \(r=1\) without the time remainder. The two appearances of the scale and the coefficient of the odd branch use the exact positive \(+1\) formula through its image class.

Uniformly over the initial real \(L_0\) and the position \(h\) of a unit strip,
\[
         \sum_{j\ge0}\Pr(h\le L_j<h+1)\le C.                          \tag{5}
\]
Indeed at time \(j>0\) there are \(O(1)\) possible grades \(k\) with \(j\log2-k\log3=L_0-h+O(1)\). The binomial local upper bound, with \(w=L_0-h\), gives
\(Cj^{-1/2}\exp[-c(j-\mu w)^2/j]\) after summing them. For \(\mu w\le2\) the large-\(j\) tail is exponential. For \(\mu w>2\), sum the central range \([\mu w/2,2\mu w]\) by a discretized Gaussian, the lower range by \(O(\sqrt{\mu w}\,e^{-c\mu w})\), and the upper range by an exponential. The zero time term costs one. [Detailed identical strip bounds for the shifted negative-binomial kernel](../UNIFORM_EARLY_ARRIVALS.md)

Iterate (4) down the fair branching tree through \(J\). Every preceding shift is a contraction in sum norm. By (5) the expected accumulated state-dependent errors are bounded by \(C_p\sum_{k\ge\lfloor H\rfloor}(1+k)^{-p}\). The time-dependent errors cost at most \(C_p\sum_{k\ge d}(1+k)^{-p}\), because the residual time decreases by one at every step. Take \(p>A+2\) to prove (1). No factor proportional to the original clock appears.

For (2) use the count-only recursion, stopping at \(\tau_H\wedge t\), now with \(H=a_1g/2\) at large \(g\). On no crossing the remaining time is zero. Replacing the count after a crossing by an independent binomial continuation costs at most its probability in total variation. A crossing before \(t\) forces some centered fair sum \(B_j-j/2\), \(j\le t\), below \(-a_1g/(2\log3)\). The bounded-increment maximal Hoeffding inequality gives the exponential term in (2); it also follows by stopping the usual exponential supermartingale and optimizing its parameter. Increase constants for the bounded parameter range. Equation (5) supplies the first term.

## Recovery of the known every-target clock from the same input

For a fixed odd \(a\) use the vector \(V_a(Y)\) of the genuine first physical time to \(a\), including \(\infty\). Its signed starting-trit estimate needs only the state error \(O_A((1+\log Y)^{-A})\). In the preceding proof take \(k=\lfloor(\log_2 Z)/64\rfloor\), and on the good cells send \((s,y)\) to \(s+\tau_a(y)\), fixing infinity. Incorrect early hits before reaching that cell cost \(O(2^{4k}/Z)\), because every binary word of length at most \(4k\) determines at most one positive start ending at the specified target. Leading twos add their actual time. The one-step recursion now adds **one** to the clock in either branch; the first visit at \(n=a\) costs at most \(O(1/Y)\) as a boundary exception. Iterating first to a finite time and then sending that horizon to infinity gives
\[
   \left\|V_a(X)-
      \mathcal L\big(\tau_H+\tau_a(m)\big)\right\|_{\rm TV}
            \ll_A H^{-A},\quad
      m\text{ uniform through }e^{L_{\tau_H}}\text{ given the walk}.    \tag{6}
\]
The stopping time is finite almost surely by the negative mean size increment \(-a_1\). Equation (5) bounds the unlimited expected error. The usual convention for infinite clocks applies.

Let \(b=\sigma\sqrt L\), \(\sigma^2=2(\log3)^2/D^3\). Choose \(H\to\infty\) so slowly that \(H=o(b)\) and every **finite** first time to \(a\) among the finitely many sources through \(e^H\) is \(o(b)\). This choice always exists by a diagonal argument; no computable rate is claimed. The complete basin has density \(d_a\) by the sparse-exception theorem (2) in the [moving-target note](MOVING_CLOCKS.md), independently of any Gaussian statement. On the stopping strip the conditional finite mass therefore tends uniformly to \(d_a\). Meanwhile
\[
                     (\tau_H-\mu L)/b\ \Rightarrow\ G                 \tag{7}
\]
for a standard normal \(G\). At \(t=\lfloor\mu L+ub\rfloor\), the difference \(L_t-\min_{j\le t}L_j\) is tight uniformly in \(t\), since by reversal its law is the maximum through \(t\) of a negative-drift bounded-increment walk starting at zero. Its infinite maximum has an exponential tail by an exponential supermartingale with small positive parameter. The ordinary fair binomial CLT thus evaluates \(\Pr(\tau_H\le t)\) as \(\Phi(u)+o(1)\), using \(a_1b\sim(\log3)\sqrt t/2\). This proves (7). Combining with (6), the finite part of the centered genuine first clock has weak Gaussian mass \(d_a\Phi(u)\). Centering and scaling at the sampled \(n\) instead of \(X\) has the same limit since \(\log(X/n)=O_P(1)\). This recovers the previously stated every-target shortcut corollary (A.8) from the specified signed native source estimate and basin densities, rather than assuming (A.8). [Leen's theorem as displayed in Weaver 179/v1, Appendix A.5](https://rstation.ai/problems/collatz/papers/179/v1)

## The arithmetic remaining at the critical clock

For each ordinary component \(C\), choose its least positive vertex \(c\) as a fixed representative. Every \(z\in C\) merges with \(c\) at some pair of finite times \(i_z,j_z\). The vector of component frequencies through a source cutoff tends in total variation to \(\nu=(d_C)\): apply PR213's countable-label theorem at \(r=1\) to exact component labels, with no exceptional edges. This use of signed transfer and its renewal conclusion does not require the Gaussian at any minimum. [PR213, sparse and countable labels, (1), (7)](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/renewal_landing.md)

At \(t=\lfloor\mu L+ub\rfloor\), choose \(H,d\to\infty\) slowly enough that \(H+d+\max_{z\le e^H}(i_z+j_z)=o(b)\). Put \(\gamma=a_1/\log3\). Along any subsequence extract uniform-on-compact limits \(f_C\) of the interpolated functions \((F_{\lfloor sb\rfloor}(c)-\lfloor sb\rfloor/2)/b\), simultaneously in the countably many \(C\), by their Lipschitz bounds. Write \(A_C=0\) on escape, and \(A_C=\log2-\beta_C\log3\) on an eventual cycle of odd fraction \(\beta_C\). Define \(\ell_C=0\) on bounded components, and \(\ell_C(s)=-a_1s+(\log3)f_C(s)\) on escape. For one fixed \(u\), the genuine joint limit from (1) is
\[
 \left(\frac{F_t-t/2}{\gamma b},\frac{\log T^t n}{b},
                \frac{E_t}{b}, C(n)\right)
 \Rightarrow
 \left(G+\frac{f_C(s)}\gamma,       a_1(G-u)_++\ell_C(s),\ A_Cs,\ C\right),\qquad s=(u-G)_+ ,       \tag{8}
\]
where \(C\) has law \(\nu\) independently of \(G\). The exact affine correction \(E_t\) is the log of \(2^tT^tn/(3^{F_t}n)\). The integer clock remains deterministic on the left.

Here are the details at the stopping boundary. With \(G_X=(\tau_H-\mu L)/b\), equation (7) gives \(\tau_H-t=O_P(b)\). At \(\tau_H\), the identity for \(L_j\) shows \((B_{\tau_H}-\tau_H/2)/(\gamma b)=G_X+o(1)\) since \(L_{\tau_H}=H+O(1)\). The centered Bernoulli increments between \(t\) and \(\tau_H\) are \(o_P(b)\), by restricting to a deterministic interval \([t-Kb,t+Kb]\), applying the maximal variance inequality there, and then increasing fixed \(K\). Hence the same assertion holds at \(t\) and at \(J\), with the final \(d=o(b)\) steps harmless if \(J=t-d\). Also \((t-J)/b=(u-G_X)_++o_P(1)\).

Conditional on any stopped path, \(C(m)\) differs in total variation from \(\nu\) by \(o(1)\) uniformly, because \(e^{L_J}\ge e^H/2\). On crossing, \(m\le e^H\). The centered counts from \(m\) and its representative over any common duration differ by \(O(i_m+j_m)\), by aligning at their actual merger and compensating the finite time shift. Their endpoint log heights differ by \(O(H+i_m+j_m)\) uniformly in the duration: past both merger clocks use the same trajectory with shift at most \(i_m+j_m\), and before those clocks both starts are at most \(e^H\). Each genuine log-height step changes by at most \(\log2\). These errors are \(o(b)\). On the noncrossing part \(J=t-d\), the residual count costs \(O(d)\), and \(\log T^d m=L_J+O_P(1+d)\) by uniform sampling through \(e^{L_J}\). The fair identity gives \(L_J/b=a_1(G_X-u)+o_P(1)\) there. The equality boundary has limiting Gaussian probability zero. Truncate the countable components and the compact range of \(G_X\) before using the simultaneous profile limits. On escape the representative's log correction on a simple prefix is \(O(\log(2+t))\), so its normalized height profile is exactly \(\ell_C\ge0\). On a bounded component the representative has bounded height and centered count slope \(\beta_C-1/2\). This proves the count and endpoint limits. Finally substitute them in the genuine log product, with \(\log n=L+O_P(1)\), to obtain the correction coordinate in (8).

In particular (8) implies the strict lower-parity-tail law (7) and the affine-correction distribution (1) of [the first checkpoint](../CRITICAL_CORRECTION.md) for each fixed \(u\), without importing a target or minimum Gaussian or the macroscopic height theorem. The prior joint finite-window result in [the terminal-window note](../TERMINAL_WINDOWS.md) is a different functional statement. The physical endpoint bound and periodic atom limits from the concurrent packet are also separate. [PR213, deterministic endpoint atoms, a743bd04](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/mass/NATIVE_ENDPOINT_ATOMS.md)

The bounded residual in (1) remains a genuine count and endpoint from the sampled low source. At the critical clock its available duration is of order \(b\) on the crossing event of probability \(\Phi(u)+o(1)\). Sending the threshold to infinity arbitrarily slowly identifies the full contribution in (8); it does not force the ordinary forward profiles of those low sources to be the alternating-cycle profile. Thus fair precritical total variation alone does not evaluate the critical lower-tail test.

## Finite formal interface and independent controls

[NativeSizeRecursion.lean](../../NativeSizeRecursion.lean) proves the
exact unnormalized population split for every integer-valued test of the
actual count and endpoint, including both finite source cutoffs and the
odd image class modulo three. It imports no analytic mixing assumption.
The [independent bounded checker](../../check_native_size_recursion.py)
compares literal trajectories with a complete affine ledger and checks
the signed recurrence. The analytic estimates and limits above remain
written source-qualified arguments; their formal status is not inferred
from this finite kernel.
