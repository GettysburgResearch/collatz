# Every positive polynomial offset scale can change the ordinary critical merger profile

Use \(t=\lfloor\log_2 N\rfloor\), the ordinary positive pairs \(x,3^s x+D\), and \(s/\sqrt t\to\lambda>0\) from the [affine interval theorem](ORDINARY_AFFINE_INTERVAL_PROFILE.md). Its universal nonmerger profile at subpolynomial normalized offsets is
\[
                    H(\lambda,1),\qquad H(z,v)=2\Phi(\sqrt{2/v}\,z)-1 .
\]
For every fixed \(0<d<1\) set \(h=\lfloor dt\rfloor\). There are constants \(c_{\lambda,d},e_{\lambda,d}>0\) such that for every sufficiently large \(N\), a fraction at least \(e_{\lambda,d}\) of all the positive offsets
\[
                              2^h\le D<2^{h+1}
\]
satisfy the following assertion **simultaneously for every interval \(I\) of \(N\) consecutive positive integers**:
\[
 \frac1N\#\{x\in I:T^t(x)\ne T^t(3^s x+D)\}
                              \ge H(\lambda,1)+c_{\lambda,d}.            \tag{1}
\]
Every such offset has \(\log(D/3^s)/\log N\to d\), uniformly on the given offset interval. In particular no bound \(|D|/3^s\le N^\delta\) with any fixed \(\delta>0\) ensures the subpolynomial-offset profile uniformly. This asserts existence of many actual positive offsets at every large scale. It does not specify the limiting profile of each individual polynomial-size offset.

## A signed grade can reverse during an independent initial window

Give \(D\) the uniform law on its displayed integer interval, independent of a Haar base \(x\in\mathbb Z_2\). Then \(x\bmod2^h\) and \((3^s x+D)\bmod2^h\) are independently uniform, because \(D\) runs exactly once through all residues. Their first \(h\) parity words are therefore independent fair words. Denote their odd counts by \(g_1,g_2\). At date \(h\) the *signed* adjusted grade difference is
\[
             L=s+g_2-g_1,\qquad L/\sqrt t\Longrightarrow
                    Z\sim\mathcal N(\lambda,d/2).                       \tag{2}
\]
This comparison uses the joint offset and base law and is made before selecting absorbed or surviving histories. If canonical absorption has already taken place then \(L=0\); negative \(L\) in (2) records a genuine reversal of the slopes.

For \(u\ge h\) let \(E_u(D)\) be the event that the signed grade differences at all dates \(h,h+1,\dots,u\) are nonzero. This event is a sufficient certificate of canonical nonabsorption at \(u\), even when there was an earlier unabsorbed visit to equal grades. For fixed \(D\) and fixed initial parity history, the remaining oriented base is Haar: writing the original base as \(r+2^h y\), either endpoint is an integer constant plus an odd multiple of the unrestricted Haar variable \(y\). If \(L\ne0\), orient by the larger slope and start the pair at positive level \(|L|\). Its new offset is an integer, with no size bound needed. Conditional on that history, \(E_u\) is exactly avoidance of a first zero level for the next \(u-h\) dates.

The [moving-level native-clock theorem, (3) and the reflection argument](CRITICAL_TOWER_ENDPOINT_PROFILE.md) gives the following probability for a first zero return, uniformly in the incoming integer offset: along any sequence with \(|L|/\sqrt t\to z>0\) and \((u-h)/t\to v>0\), the probability of avoidance tends to \(H(z,v)\). This first-return assertion alone suffices; the possibly large new real offset would preclude simply applying a full-absorption statement. The convergence is uniform over scaled starting levels in any compact subinterval of \((0,\infty)\) for a given limiting \(v\), by sequential compactness and continuity. The tails and a vanishing neighborhood of zero in (2) allow us to integrate this conditional law. It follows both for \(u=t\) and for \(u=j=t-\lceil2\log_2(t+2)\rceil\), with the *same* \(h\) and random \(D\), that
\[
               \mathbb E_D\Pr_x(E_u(D))\longrightarrow
               B_{\lambda,d}:=\mathbb E[H(|Z|,1-d)].                    \tag{3}
\]
The original uniform fixed-test expected-occupation theorem supporting the moving-level clock is Leen's. His sharpness result for a moving *level-zero initial offset* uses a different normalization and does not supply (2) or (3) at a growing initial slope. [Leen, exact rates and uniform occupation](https://doi.org/10.5281/zenodo.23268751) · [Leen, moving level-zero absorption and its linear log-moment obstruction](https://doi.org/10.5281/zenodo.23268753)

The Gaussian semigroup gives \(\mathbb EH(Z,1-d)=H(\lambda,1)\). Indeed if \(U\sim\mathcal N(0,(1-d)/2)\) is independent, then \(\mathbb E\Phi(\sqrt{2/(1-d)}Z)=\Pr(U\le Z)=\Phi(\sqrt2\lambda)\). The function \(H(\cdot,1-d)\) is odd, strictly negative on the negative half-line. Since \(\Pr(Z<0)>0\),
\[
             B_{\lambda,d}-H(\lambda,1)=
             2\mathbb E[-H(Z,1-d)\boldsymbol1_{Z<0}]>0.                \tag{4}
\]
Passing from the signed rank to the first future zero of its absolute value is the source of the strict excess.

## Selecting offsets before the positive integer interval is chosen

Write \(p_u(D)=\Pr_x(E_u(D))\) under Haar base. For each \(D\), \(E_t\subseteq E_j\); (3) gives \(\mathbb E_D[p_j(D)-p_t(D)]\to0\). Let \(b_0=B_{\lambda,d}-H(\lambda,1)>0\). Because \(0\le p_t\le1\) and the average tends to \(B_{\lambda,d}\), a positive fraction (depending only on \(b_0\)) of offsets has \(p_t(D)\ge H(\lambda,1)+b_0/2\) for large \(N\). Exclude the \(o(1)\) fraction with \(p_j(D)-p_t(D)>b_0/16\) by Markov.

For any remaining offset and *every* allowed interval \(I\), the empirical proportion of \(E_j\) differs from \(p_j\) by at most \(2^j/N\), using its exact dyadic residue period. The empirical loss from \(E_j\) to \(E_t\) is at most \((1+2^t/N)(p_j-p_t)\le2(p_j-p_t)\), uniformly in the placement of \(I\). Thus the empirical proportion of \(E_t\) exceeds \(H(\lambda,1)+b_0/4\) for large \(N\). At most \(O(N^{-c})\) of those sources can nevertheless be numerical coincidences of unequal slopes, by (4) in the affine interval theorem, uniformly over all offsets and interval positions. This proves (1), for instance with \(c_{\lambda,d}=b_0/8\). For a prescribed positive polynomial envelope one may choose any \(d<\min(\delta,1)\); all selected offsets then lie strictly inside it for large \(N\).
