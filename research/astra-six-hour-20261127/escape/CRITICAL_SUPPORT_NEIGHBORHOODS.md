# Critical neighborhood size for the closed correction support at 1

Use the defect coordinate \(u=x3^j/2^d\) on a first-hit word into 1 with odd clock \(j\) and native clock \(d\). Let \(K\) be the closure of all these defects and let \(K_\epsilon=\{t:\operatorname{dist}(t,K)\le\epsilon\}\). The [closed support theorem](CLOSED_CORRECTION_SUPPORT.md) gives \(|K|=0\) under the stated ordinary inputs. Write \(E\) for the stationary exit measure in the [first-return theorem](FIRST_RETURN_POISSON.md), and \(D=\log(4/3)\). For every nonnegative continuous compactly supported \(f\),
\[
 \liminf_{\epsilon\downarrow0}\sqrt{\log(1/\epsilon)}
       \int_{K_\epsilon}f(t)\,dt
               \ \ge\ \sqrt{D/\pi}\int f\,dE.                         \tag{1}
\]
In particular the closed null set has neighborhood length at least a positive constant times \(1/\sqrt{\log(1/\epsilon)}\) at every sufficiently small scale. Equation (1) is a statement about neighborhoods of the entire closed support. Its proof does not give a lower Hausdorff-measure bound at the critical gauge.

For the genuine first-hit cell \((j,d)=(n,2n)\), put \(p_n=(4/3)^n\), \(\epsilon_n=1/p_n\). The real-marked local limit and the central negative-binomial atom give
\[
    \frac{\sqrt n}{p_n}
       \sum_{\substack{J(x)=n\\S(x)=2n}} f(x/p_n)
           \longrightarrow \frac1{\sqrt{4\pi}}\int f\,dE.             \tag{2}
\]
Continuous tests follow from the Lipschitz version by approximation, using the uniform mass bound from (2) for the constant test. Around each of these points take the interval of radius \(1/p_n\). The points lie in \(K\), and distinct positive odd numerators have spacing at least \(2/p_n\). Their intervals thus have disjoint interiors. Write \(V_n\) for their union. By uniform continuity, (2) yields
\[
                 \sqrt n\int_{V_n} f(t)\,dt
                       \longrightarrow \frac1{\sqrt\pi}\int f\,dE .
\]
For \(\epsilon_{n+1}\le\epsilon<\epsilon_n\) one has \(V_{n+1}\subset K_\epsilon\) and \(\log(1/\epsilon)=Dn+O(1)\). Nonnegativity proves (1), including the displayed constant. [Marked first-hit local limit](CRITICAL_POISSON_PROFILE.md)

There is a corresponding divergence for the complementary intervals of this fixed ordinary set. Write their lengths inside the convex hull of \(K\) as \(b_i\). Then
\[
                 \sum_i b_i\sqrt{\log(e/b_i)}=\infty .                 \tag{3}
\]
Indeed the length of the \(\epsilon\)-neighborhood inside that hull is \(\sum_i\min(2\epsilon,b_i)\), since \(K\) has zero length. The difference from the full neighborhood length is at most \(2\epsilon\). Integrate its lower bound from (1) at \(\epsilon=e^{-s}\) against \(s^{-1/2}\,ds\) for large \(s\). The lower integral diverges logarithmically. On one gap the corresponding integral is \(O(b_i\sqrt{\log(e/b_i)})\), by splitting at \(s=\log(2/b_i)\). Tonelli gives (3). This conclusion uses the exact integer mesh and positive first-hit exit mass.

For a hypothetical escaping component fix a base height \(P_0\), put \(p_n=P_0(4/3)^n\), and consider all its points of corrected height \(p_n\). PR195's local limit gives their number asymptotic to \(H_C p_n/\sqrt{4\pi n}\). Their distinct odd numerators again supply disjoint intervals of radius \(1/p_n\) inside the neighborhood of the component's closed defect set. It follows that its neighborhood length times \(\sqrt{\log(1/\epsilon)}\) has lower limit at least \(H_C\sqrt{D/\pi}\). Its complementary intervals likewise satisfy (3). Both root 1 and a putative escaping component therefore meet the critical lower size at the same order, with different charge constants. [PR195, corrected-height local law](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/LOCAL_HEIGHT_LAW.md) · [Component closed-support theorem](CLOSED_CORRECTION_SUPPORT.md)
