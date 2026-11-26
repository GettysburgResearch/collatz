# A critical Hausdorff measure gap for the complete escape boundary

The odd gaps and first strict ladder blocks have the meaning in [RECORD_ENTRANCE.md](RECORD_ENTRANCE.md). Put \(\alpha=\log_2 3\), \(\rho=1/\alpha\), and \(\theta=H_2(\rho)\). Let \(C\subset\mathbb Z_2^\times\) be the dyadic futures obtained from **infinitely many** first ladder blocks of arbitrary finite lengths. Let \(G\) be the pairs of these futures with their inverse-real shadows whenever that real limit is finite. The ordinary embedding uses a literal odd positive source and all its actual gaps, not a random gap draw. Then
\[
 \dim_H C=\theta,\quad \mathcal H^\theta(C)=0,\qquad
 \dim_H G=1+\theta,\quad \mathcal H^{1+\theta}(G)=0 .
\]
The metric on the pair is the maximum metric. Every escaping ordinary odd unit gives a point of \(G\) in precisely this sense. These dimension and critical-measure statements concern the full symbolic boundary containing those points.

## Strict loss at the critical exponent

Give one gap the independent geometric law \(p(e)=\rho(1-\rho)^{e-1}\); this is used only for counting. For a ladder word of odd length \(m\) and total shortcut clock \(s\) its probability is \(P(w)=\rho^m(1-\rho)^{s-m}\). There is a strict surplus \(m-\rho s>0\). Entropy gives the exact ratio
\[
         2^{-\theta s}/P(w)=
             ((1-\rho)/\rho)^{m-\rho s}<1.
\]
First ladder words are prefix-free, so their probabilities sum to at most one. In particular
\[
   \kappa=\sum_{w\in L_\infty} 2^{-\theta s_w}
       \le 1-\bigl(\rho-2^{-\theta}\bigr)<1,
\]
by paying just the explicit single-gap block. The countably many cylinders of \(n\) completed blocks cover \(C\), have diameters at most \(2^{-n}\), and their \(\theta\)-cost is at most \(\kappa^n\). Each exact word of total clock \(s\) fixes a single ordinary odd class modulo \(2^{s+1}\). This proves the critical dyadic null measure directly. On \(G\) restricted to any fixed bounded real interval, cover the entire interval above each dyadic cell at its own diameter. The resulting product cover has \((1+\theta)\)-cost \(O(\kappa^n)\). A countable union over bounded real intervals gives the second null measure.

## Sharp lower dimensions without an ordinary assumption

PR 201 proves that the ternary finite-alphabet roots \(d_J\), defined by \(\sum_{w\in L_J}3^{-d_J m_w}=1\), increase to \(\theta\), and each ladder word has \(s=\lfloor\alpha m\rfloor\). For \(b<\theta\) the full series \(\sum_{w\in L_\infty}3^{-b m_w}\) diverges. Indeed at \(b=\theta\) its value is at most \(\kappa<1\), by \(3^{-\theta m}\le2^{-\theta s}\). If it converged at any smaller exponent, dominated continuity from below near \(\theta\) would contradict \(d_J\uparrow\theta\).

For \(0<b<\theta\), both \(2^{-bs}\) and \((2^s/3^m)2^{-bs}\) are within absolute constant factors of \(3^{-bm}\), since \(0\le\alpha m-s<1\). Hence the finite sums of both weights exceed one for sufficiently large \(J\). The dyadic separated-cylinder dimension for that finite alphabet then exceeds \(b\), and the joint dimension theorem in [RECORD_ENTRANCE.md](RECORD_ENTRANCE.md) gives \(\dim_H G_J>1+b\). Let \(b\uparrow\theta\). Together with the critical null-measure bounds this proves both exact dimensions. The finite-alphabet graph dimensions approach the limiting value from below.

## Why an actual escape lies in this set

Write \(x_i\) for the odd forward trajectory of one escaping ordinary \(a\), with multiplier \(r_i=3^i/2^{S_i}\). The uniform simple-path reciprocal bound in [TILTED_TRACE.md](TILTED_TRACE.md) gives
\[
  r_i^{-1}x_i
     = a\prod_{j<i}(1+1/(3x_j)) \longrightarrow L_a\in (a,\infty).
\]
As \(x_i\to\infty\), also \(r_i\to\infty\). Its strict records yield the required infinitely many first ladder blocks regardless of the intervening waits. The real inverse prefix evaluated at zero is \(a-x_i/r_i\to a-L_a\), and the same inverse gap prefix evaluated on any odd dyadic terminal converges dyadically to the source \(a\). Thus \((a-L_a,a)\in G\) with the clocks of this single ordinary source.

For completeness the real projection of \(G\) is exactly \((-\infty,-1]\). The finite-\(J\) projections are nested intervals ending at \(-1\). For an initial gap \(e\) followed by \(k\) ones, take the least \(k\) giving a strict coefficient record. This is a first ladder word. As \(e\to\infty\), \(k\to\infty\), its slope is at most \(3/2\) and its forward intercept is at least \((3/2)^k-1\), so its fixed point tends to \(-\infty\). Conversely a real limit of inverse prefixes along infinite ladder blocks with finite shadow is at most \(-1\). Each ladder forward map sends \(-1\) to a point at least \(-1\). Also its intercept is at least \(1/2\) from the last gap one. If the real shadow is finite then the product of the inverse-real slopes tends to zero, since otherwise the contributions of these intercepts would force an infinite inverse translation. Applying the inverse prefix to zero and to \(-1\) therefore gives the same limit, at most \(-1\).

Neither critical null measure nor codimension excludes a specified ordinary integer. The countable record alphabet permits arbitrarily late first arrivals, and the complete boundary need not be closed. In particular a positive ordinary density for a component gives no Haar lower volume for this infinite-arrival condition by finite-cylinder equidistribution. The deficiency \(\kappa^n\) is available at the exact completion of \(n\) records; there is no uniform elapsed-time deadline for positive ordinary escapes in the proof.
