# An additive change of one on a ternary-multiple trajectory

Let \(T\) be the positive shortcut. Consider maps \(U:\mathbb N_{>0}\to\mathbb N_{>0}\) with exact even halving and \(|U(n)-T(n)|\le1\) everywhere. If a \(U\)-trajectory stays in \(3\mathbb N\) from a date \(t_0\) onward, then its entire tail, divided by three, is a genuine \(T\)-trajectory. Consequently existence of a divergent \(U\)-trajectory eventually in \(3\mathbb N\) for such a map is equivalent to existence of a divergent positive trajectory of \(T\). The [explicit two-unit construction](ONE_SPARSE_DIVERGENT_ORBIT.md) produces the shielded divergent trajectory unconditionally, preserving the known \(1,2\) cycle.

For even \(y\) we have \(U(3y)=3T(y)\). For odd \(y\) the true \(T(3y)=(9y+1)/2\) is \(2\bmod3\); the unique multiple of three within distance one of this value is
\[
                           T(3y)+1=3(3y+1)/2=3T(y).
\]
This proves the assertion at each date of the tail. In the converse direction the explicit computable rule that takes \(U(3y)=3T(y)\) for all \(y\), and otherwise keeps \(T\), meets both requirements. Each true divergent orbit then supplies a divergent scaled orbit. That particular rule changes all odd multiples of three.

## A sparse converse when a true divergent orbit exists

Suppose \(T\) has a divergent trajectory. Some state \(s\) on a divergent tail satisfies \(s\equiv1\bmod3\) and \(s>1\). After one odd departure all states are ternary units. If a later state has residue one we are done. If the states remain \(2\bmod3\), an even halving would yield residue one. They would therefore be odd forever, impossible: \(j\) successive odd departures give \(T^j(n)+1=(3/2)^j(n+1)\), which cannot be integral for every \(j\). The same argument applies after removing any finite prefix.

Write \(D_s=\{T^j s:j\ge0\}\) and \(a=2s-1\), so \(a\) is odd and \(a\equiv1\bmod3\). Change the outgoing edge of \(a\) to \(3s=T(a)+1\). At exactly the vertices \(3y\) with \(y\in D_s\) odd, change the outgoing edge to \(3T(y)=T(3y)+1\); elsewhere keep \(T\). The anchor is separate from all the scaled states. The entire change set now lies on the single genuine \(U\)-orbit
\[
                              a,\ 3s,\ 3T(s),\ 3T^2(s),\ldots .
\]
It diverges and the \(1,2\) cycle stays intact. Every genuine predecessor of \(a\) either arrives unchanged at \(a\) or first encounters an earlier changed scaled source and enters the divergent tail there. Thus the new component has positive lower density by Mazur's theorem at this ternary-unit anchor. In fact its density equals the true predecessor density of \(a\): the extra captured starts can only lie on the original dyadic rays of the changed ternary multiples, a null set.

For a quantitative count, Leen's uniform orbit-set theorem bounds \(|D_s\cap[1,X]|\ll_\theta X^\theta\) for every fixed \(H_2(\log_3 2)<\theta<1\), for all \(s\), by applying the theorem on an interval of length \(X\) (or summing dyadic shells). It bounds the number of changed vertices through \(X\) by the same order. Their high dyadic rays have size \(O_\theta(\sum_{v\ge0}(X/2^v)^\theta)=O_\theta(X^\theta)\), using the true preimage identity for multiples of three. Positive genuine density exists by Leen's invariant-set theorem. This sparse converse is conditional, and no algorithm deciding membership in \(D_s\) has been assumed. Generation of an arbitrary diverging integer orbit until it first exceeds an input does not establish that it cannot return below that input later. The computable rule changing every odd multiple of three requires no such decision. [Leen, uniform sparsity proof, appendix «Uniform sparsity of orbit sets»](https://doi.org/10.5281/zenodo.23252397) · [Mazur, positive lower predecessor density and map conversion](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf) · [Leen, invariant-set densities](https://doi.org/10.5281/zenodo.23269488)

The equivalence requires a tail confined to multiples of three. It supplies no exclusion of unit-size changes on trajectories that leave and return to this congruence class.
