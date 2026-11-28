# Multiplicative relations force a smaller physical state

Write \(T(2u)=u\), \(T(2u+1)=3u+2\), and write \(U\) for the map from an odd integer to its next odd iterate. We give a finite, effective descent criterion with no bound on the coefficients of a multiplicative relation. One version tests the shifted heights on the supplied trajectory. Another tests actual positive odd siblings in its ordinary inverse tree. Arbitrarily many independent siblings can have arbitrarily small total basin density, even on a terminating ascending segment.

## A divisibility bound for the physical clock

Let \(z_i=T^i(z_0)\), set \(e_i=z_i\bmod2\), and put \(W_i=az_i+c\), with fixed positive integers \(a>c\). Direct substitution gives
\[
  2W_{i+1}=3^{e_i}W_i+d_i,
  \qquad d_i=\begin{cases}c,&e_i=0,\\ a-c,&e_i=1.\end{cases}
\]
Set \(C=\max(c,a-c)\). For actual native times \(i<j\), \(d=j-i\), composition gives
\[
 2^d W_j=3^{e_i+\cdots+e_{j-1}}W_i+J_{ij},
 \qquad 0<J_{ij}\le C(3^d-2^d).
\]
The positive carry starts at zero and is updated by multiplication by the next \(3^e\) and addition of its positive offset times the current power of two. Replacing every \(3^e\) by three bounds it by \(C\sum_{t=0}^{d-1}3^{d-1-t}2^t=C(3^d-2^d)\). In particular \(\gcd(W_i,W_j)\mid J_{ij}\). Paper 138 uses the corresponding positive carry and prime-power return cost for the unshifted odd map. The shift here ensures a positive carry even through a word consisting entirely of native halvings. [Paper 138, §2](https://rstation.ai/problems/collatz/papers/138)

Suppose that at native times \(t_0<\cdots<t_{k-1}\) there is a nonzero integral relation
\[
                      \prod_{i<k}W_{t_i}^{m_i}=1.
\]
Choose \(i\) with maximal \(|m_i|>0\). For every prime \(p\), the valuation identity and maximality give \(v_p(W_{t_i})\le\sum_{j:\,m_i m_j<0}v_p(W_{t_j})\). Truncating each summand at \(v_p(W_{t_i})\) preserves this inequality. Therefore
\[
 W_{t_i}\mid\prod_{j:\,m_i m_j<0}\gcd(W_{t_i},W_{t_j})
 \quad\text{and}\quad
 W_{t_i}\le \prod_{j\ne i} C(3^{|t_j-t_i|}-2^{|t_j-t_i|}).
 \tag{1}
\]
A certificate may use only the opposite signs and the exact observed carries for a tighter bound. The size of the coefficients does not enter (1).

For \(a=2,c=1\), put \(P_k=\prod_{d=1}^{k-1}(3^d-2^d)\), with \(P_1=1\). On any \(k\) **consecutive native sites**, the right side of (1) is at most \(P_k\): the factors increase with the distance and the largest product occurs at an endpoint. Thus if the shifted heights on any such window anywhere in the future of a supplied \(n\) satisfy a relation and \(P_k<2n+1\), an actual site of that window is smaller than \(n\). In particular the simpler sufficient test \(3^{k(k-1)/2}\le2n+1\) works for \(k\ge2\). Every window wholly at or above \(n\) at those lengths has independent shifted heights. The exact divisibility test also applies to sparse time selections with their true distances. This is independent of the lower bound for a prescribed multiplicative label from logarithmic forms. The latter permits considerably longer windows for its restricted pair test. [Geometric label return](GEOMETRIC_RETURN_DESCENT.md)

## Independent positive ordinary siblings or direct descent

Use \(W(z)=64z+21\), so \(C=43\). For every odd ternary unit \(z\), the integer \(W(z)\) is another odd ternary unit, distinct from \(z\), with
\[
                    3W(z)+1=64(3z+1), \qquad U(W(z))=U(z).
\]
It is an actual ordinary odd predecessor of the very same next odd state, with exactly six extra divisions. The unit condition also ensures positive ordinary predecessor density by the fixed-target density theorem used in this project.

Start from an odd unit \(n\). Fix \(r\ge2\) and inspect the first \(r\) odd states \(z_0=n,z_1,\ldots,z_{r-1}\). If no smaller odd state has yet occurred, their total native duration is at most \(2(r-1)\). Indeed, for the actual total \(t\) of divisions,
\[
 2^t z_{r-1}=n\prod_{i<r-1}(3+1/z_i)\le n4^{r-1}, \qquad z_{r-1}\ge n.
\]
Thus, if
\[
               64n+21>43^{r-1}\,3^{2(r-1)^2},                       \tag{2}
\]
all \(r\) of the actual ordinary siblings \(W(z_i)\) are multiplicatively independent. Otherwise a relation would force some \(64z_i+21<64n+21\) by (1). Consequently, under (2), observing any nonzero relation is a finite certificate of a smaller actual state. All odd states after the first transition are ternary units, so a divisible-by-three first site can be omitted when applying the sibling interpretation. The result gives on the order of \(\sqrt{\log n}\) independent actual sibling roots on every sufficiently high segment with no descent below its source.

On a fixed genuinely escaping odd ray all these sibling roots are off the ray. A sibling at \(z_i\) first joins the selected ray at \(z_{i+1}\): a previous occurrence on that ray would repeat a state, or would say that its immediate predecessor on the ray equals the distinct sibling. Sibling basins from different attachment sites are disjoint, by determinism. Their positive densities sum to at most one over the entire ray. At successive suffix minima of an escape, (2) therefore supplies families of arbitrarily high rank whose aggregate density tends to zero. This uses the ordinary, unconditioned predecessor densities of the selected positive siblings.

## Terminating controls with arbitrarily small total incoming mass

For **each** \(r\ge1\) and \(\epsilon>0\), infinitely many terminating exact ascents have \(r\) independent odd unit siblings of total ordinary predecessor density below \(\epsilon\). Take \(s=r+2\),
\[
       f=(2\ell+1)3^{s-1},\qquad b=(2^f+1)/3^s,
       \qquad n=2^s b-1 .
\]
The integer \(b\) is positive and odd. The divisibility follows by iterating \(u^3+1=(u+1)(u^2-u+1)\) at \(u\equiv-1\pmod 3\), starting from \(2+1=3\), and then using the odd multiplier \(2\ell+1\). The consecutive native sites
\[
            x_i=2^{s-i}3^i b-1\quad(0\le i\le s)
\]
are strictly increasing, the first \(s\) are odd, and \(x_s=2^f\). Thus this actual orbit reaches one. The penultimate odd site
\[
                       q_f=x_{s-1}=(2^{f+1}-1)/3
\]
is an odd ternary unit with \(U(q_f)=1\); for \(s\ge3\), \(f\equiv3\pmod6\) and \(q_f\equiv2\pmod3\). The \(r\) sites \(x_i\), \(1\le i\le s-2\), are odd ternary units because \(3\mid3^i\). Their siblings merge at the different \(x_{i+1}\) and pass through \(q_f\). None of the siblings lies on the main spine: before its own attachment the earlier spine values are smaller, and from the attachment onward the spine never comes back before reaching one. The sibling basins are pairwise disjoint by their different first attachments. Taking \(\ell\) large gives independent siblings by (1), since their native sites are consecutive and their heights tend to infinity.

As \(\ell\) varies, the distinct \(q_f>1\) are different odd children of one. No orbit visits two: each immediately goes to one, and one stays at one on the odd map. The sum of their ordinary predecessor densities is therefore at most one. In particular \(d(q_f)\to0\). The sum of the densities of the \(r\) disjoint sibling basins inside this branch is at most \(d(q_f)\), giving the claimed arbitrarily small bound. These controls rule out any positive lower bound depending only on the number of independent siblings, even with their physical shared-successor and ascent geometry specified. They leave open an estimate that also uses a positive lower bound on the density of the main predecessor along an entire escaping ray.


## Relative mass along an ascent in any supplied component

Prior work of Weaver and Wren formulates the disjoint-sibling criterion for escape and the proposed lower bound of order \(d(z)/\log z\) on a suitable sibling. Paper 200, Theorem B, proves that for each supplied unit target \(t\), positive integer \(r\) and \(\eta>0\), there are arbitrarily high nonperiodic unit inputs \(x\) whose next \(r\) odd steps each use one division, whose endpoint \(y=U^r(x)\) reaches \(t\), and for which \(d(y)<(1+\eta)d(x)\). Its statement uses lower densities; here we use the available fixed-target natural densities to subtract the nested basin masses. The cited theorem does not assert a fixed positive lower bound on \(d(x)\). [Paper 200, Theorem B and literature discussion](https://rstation.ai/problems/collatz/papers/200) · [First-hit densities and the ordinary inverse law, Paper 12](https://rstation.ai/problems/collatz/papers/12)

On each sufficiently high such ascent the \(r\) actual positive unit siblings \(W(U^i x)\), \(0\le i<r\), are independent by (1). Their basins are pairwise disjoint and contained in \(\mathcal P(y)\setminus\mathcal P(x)\). To verify this even for a target with a cycle, first choose \(x\) above that cycle's maximum; the finitely many further sites on \(t\)'s orbit before its cycle cannot cause a repeat through any larger ancestor. If \(t\) escapes there is no cycle. An overlap of two distinct predecessor branches entering the displayed ascent would force one of their first-attachment sites to lie on a cycle, since the odd map is deterministic. The branch of \(x\) is excluded for the same reason. Thus
\[
       \sum_{i=0}^{r-1} d(W(U^ix))\le d(y)-d(x)<\eta d(x).
\]
In every prescribed target basin one can therefore arrange arbitrarily many independent actual siblings with arbitrarily small total mass *relative* to the main input. The preceding explicit terminating family did not need Paper 200 and did not compare the two densities by a ratio. The relative deduction from Paper 200 gives no rate in terms of the selected height. Weaver's subsequent [Paper 202, Theorem 1 and Corollary 2](https://rstation.ai/problems/collatz/papers/202) already refutes the proposed universal logarithmic lower bound, with arbitrarily large fixed logarithmic powers. The separate [larger-parameter construction](../mass/SMALL_SIBLING_DENSITY.md) extends the prescribed climb and ternary depth to order `(log log Y)^2`. A lower bound restricted to a main basin of fixed positive density along a forward ray remains open.
