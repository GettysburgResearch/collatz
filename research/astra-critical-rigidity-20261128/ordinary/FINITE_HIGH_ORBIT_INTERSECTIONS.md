# Common high values of independent finite ordinary trajectories

**Proposed, source-qualified written result.** Use the positive shortcut \(T\) and the component densities \(d_C\) from [Sparse high targets](SPARSE_HIGH_TARGETS.md). Fix any \(k\ge2\). Independently sample \(n_i\) uniformly from the positive integers through \(X_i\). Inspect the actual finite paths \(\{T^j n_i:0\le j\le H_i\}\) for deterministic nonnegative integer deadlines \(H_i\). For each divergent component choose one fixed representative \(x_C\), and let \(a_C(Y)\) be the first date its path visits \([Y,2Y]\), with date \(+\infty\) if there is no visit. Put \(\mu=2/\log(4/3)\), \(\sigma^2=2(\log3)^2/\log^3(4/3)\).

As \(Y,\min_i X_i\to\infty\) independently, uniformly over all deadlines, the probability that **one actual integer in \([Y,2Y]\) occurs on every finite path** equals
\[
 \sum_{C\ {\rm divergent}}d_C^k
    \prod_{i=1}^k\Phi\!\left(
       {H_i-a_C(Y)-\mu\log X_i\over\sigma\sqrt{\log X_i}}
                        \right) +o(1).                                  \tag{1}
\]
The dates of the visits can differ. The trace comparison is a finite search. For any \(\theta>H_2(\log_3 2)=0.9499\ldots\), where \(H_2\) is binary entropy in bits, each fixed representative satisfies \(a_C(Y)\le C_\theta Y^\theta\) at every sufficiently large \(Y\), with the constant uniform over representatives once \(Y>x_C\). In particular set all \(X_i=X\), \(H_i=\lfloor\mu\log X+\sigma u\sqrt{\log X}\rfloor\). If \(Y\to\infty\) and \(Y^\theta=o(\sqrt{\log X})\), the limit of (1) is
\[
             \Phi(u)^k\sum_{C\ {\rm divergent}}d_C^k.                    \tag{2}
\]
For arbitrary independent \(X,Y\to\infty\), a deadline \(\mu\log X+w(X)\sqrt{\log X}+Y^{\theta'}\) with \(w(X)\to\infty\) and \(\theta'>\theta\) gives the same sum without the Gaussian factor. All statements keep the whole population of ordinary starts. Mazur's positive-predecessor theorem then makes the zero limit in (2) equivalent to the absence of divergent trajectories. This criterion leaves nontrivial cycles as a separate possible obstruction.

## Proof

Leen's appendix *Uniform sparsity of orbit sets*, following earlier physical-interval sparsity work of Garcia and Tal, proves the following exact exponent for the native shortcut. It gives
\(\#(O(n)\cap[Y,2Y])\le C_\theta Y^\theta\) uniformly over **every** \(n\), whenever \(H_2(\log_3 2)<\theta<1\). A value seen before or at the global minimum of the first sample belongs to its independent second sample's entire orbit in the high shell with probability \(o(1)\). Indeed, condition on the second sample and use (1) of [Sparse high targets](SPARSE_HIGH_TARGETS.md) for its now deterministic mask. Its relative cardinality is \(O(Y^{\theta-1})\), with a common constant. Apply the same argument for each arm using any different arm and sum the \(k\) errors. With probability \(1-o(1)\), any common high value, if it exists by the chosen deadlines, has a strictly postminimum occurrence in every witnessing trace. This argument requires \(k\ge2\). A single ordinary path can visit a high shell during its typical descent. [Leen, original recurrence and induction for the uniform interval exponent, Appendix A](https://doi.org/10.5281/zenodo.23252397) · [Garcia and Tal, original earlier sparsity result](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf) · [Leen, minimum probabilities and physical minimum clock](https://doi.org/10.5281/zenodo.23269488)

Let \(r_i=m(n_i)\), and keep a finite set of values of \(r_i\) carrying limiting mass \(1-\eta\). Distinct components have disjoint orbits. A fixed bounded orbit misses the high shell for all sufficiently large \(Y\). In a divergent component \(C\), the finite family of paths from retained minima, together with that from \(x_C\), has a common forward tail. Write \(v\) for its first state after chosen finite prefixes of all of them, with respective arrival times \(\ell_r,\ell_*\) from \(r,x_C\). For \(Y\) above the finitely many prefix values, the high shell is first met at the **same actual vertex** on all those paths. Its date from \(r\) is exactly \(a_C(Y)+\ell_r-\ell_*\). Such a vertex exists by the first upcrossing of \(Y\) from below. Thus, for the retained minima of this component, a common postminimum high value occurs before all deadlines precisely when each individual minimum date obeys
\[
            \tau(n_i)\le H_i-a_C(Y)-(\ell_{r_i}-\ell_*).
\]
No cross-arm synchrony condition is imposed. Before the first upcrossing from \(x_C<Y\), all its states are distinct positive integers below \(Y\), so the sparsity bound applied to \([1,Y]\) gives the asserted bound for \(a_C(Y)\).

For each fixed \(r\), the true minimum-time law gives
\[
 \Pr\{m(n_i)=r,\ \tau(n_i)\le\mu\log X_i+\sigma u\sqrt{\log X_i}\}
       \longrightarrow p_r\Phi(u).
\]
The original centering by \(\log n_i\) is interchangeable with \(\log X_i\) because their difference is tight. Convergence is uniform in \(u\in\mathbb R\) by monotonicity and continuity of the limiting subdistribution; a fixed finite arrival-time shift is negligible uniformly. By independence the retained tuple's contribution equals the product of its \(p_{r_i}\)'s and the Gaussian factors in (1), with \(o(1)\) error. Sum over the finitely many retained tuples. Taking \(\eta\to0\) yields \(d_C=\sum_{r\in C}p_r\) in (1). The two deadline specializations follow by truncating first to finitely many components, bounding their \(a_C(Y)\), and releasing the truncation.

The sequence \(s_k=\sum_Cd_C^k\), over the divergent components alone, determines their ranked positive densities including multiplicities. For example \(s_k^{1/k}\) tends to the largest mass if any exists, and after dividing by its \(k\)-th power the limit gives its multiplicity. Subtract these terms to recover successive masses. This offers a comparison with the [same-date periodic-component formula](SYNCHRONOUS_PHASE_DISPERSION.md) at the identical absolute clock when \(Y\) grows slowly. That formula observes only the terminal integer. Formula (2) searches the preceding traces for one shared high value.
