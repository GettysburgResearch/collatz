# The whole physical first-landing word under native reciprocal-time weighting

Take the shortcut trajectory of each positive rational \(m/3^n\), \(3\nmid m\), through its first integer landing. Denote its length by \(T\), its terminal integer by \(N\), and its actual chronological parity word by \(w\). This word ends with the \(n\)-th odd departure. Give the source weight \(2^{-T}\), before any normalization.

For the integers \(m\) in any interval of \(M\) consecutive positive integers, fix \(a>\log(3/2)/\log(4/3)=1.4094208\ldots\) and assume \(M\ge2^{an}\). Uniformly in its placement and width, the sum of the weights is
\[
           \frac{2M}{3\cdot3^n}(1+O_a(e^{-c_a n})).                    \tag{1}
\]
After division by their sum, the law of the **entire physical word** differs by \(O_a(e^{-c_a n})\) in total variation from independent bits of odd probability \(3/4\), stopped at the \(n\)-th odd. In particular the actual native landing clock obeys a central limit theorem of mean centering \(4n/3\) and variance scaling \(4n/9\). The word comparison applies to every test event, including those depending on the whole word. The underlying probability on physical sources has been multiplied by its native reciprocal time. The unweighted interval law has a different typical clock near \(2n\). [Unweighted physical source theorem](TRANSLATED_LANDING_INTERVALS.md)

## Direct comparison of cylinders and a weighted long-word bound

A given length-\(t\) word ending with its \(n\)-th odd fixes one numerator residue modulo \(2^t\), since \(3^n\) is a dyadic unit. Conversely every numerator in that residue reads it. Among an interval of length \(M\), the number which are ternary units is \(2M/(3\cdot2^t)+O(1)\), with an absolute constant. Every unit has positive reduced ternary height until the last odd. Write \(w^*(w)=3^n4^{-t}\); this is exactly the stopped-bit probability \((3/4)^n(1/4)^{t-n}\). Choose
\[
          \log(3/2)/\log(4/3)<b<a,\qquad l=\lfloor bn\rfloor .
\]
Through \(t\le l\), the actual word weights divided by \(2M/(3\cdot3^n)\) are \(w^*(w)(1+O(2^l/M))\), uniformly.

The ideal tail above \(l\) decays exponentially by the binomial Chernoff bound, since \(b>4/3\). For the physical tail, take an initial \(l\)-bit word with \(g<n\) odds. Every numerator there requires at least \(n-g\) additional native dates, and belongs to a class occupied at most \(M/2^l+1\) times before excluding multiples of three. Its entire contribution to the tail divided by the scale in (1) is bounded, after summing all such histories, by
\[
  \tfrac32(1+2^l/M)\,3^n 2^{-l-n}
             \mathbb E\,2^{\operatorname{Bin}(l,1/2)}
   =\tfrac32(1+2^l/M)(3/2)^n(3/4)^l .
\]
This decays exponentially by the choice of \(b\). Summing the two word errors proves (1) and the total variation bound. The clock limit follows from the usual central limit theorem for a sum of \(n\) independent geometric variables on \(1,2,\ldots\) of success probability \(3/4\).

## Real source and terminal scales

Fix \(0\le u<v<\infty\) and use \(u<m/3^n<v\). The mass tends to \(2(v-u)/3\) exponentially. On a probability space carrying iid tilted inter-odd lengths \(e_i\) of law \(3\cdot4^{-e}\), put
\[
 S_j=\log(3^j/2^{e_1+\cdots+e_j}),\qquad
 Z=\tfrac12\sum_{j\ge1} e^{-S_j},\qquad
 d=\log3-\tfrac43\log2>0 .
\]
Here and below an unsubscripted logarithm is natural. The variable \(Z\) is finite almost surely, since \(S_j/j\to d\). Write \(L=3^n/2^T\) for the actual finite word. If \(U\) is uniform on \((u,v)\), independent of the tilted lengths, then under normalized reciprocal weights
\[
       (m/3^n,N/L)\ \Longrightarrow\ (U,U+Z),\qquad
       \frac{\log_2 N}{n}\ \longrightarrow\ \log_2 3-4/3               \tag{2}
\]
in distribution and probability respectively. The second convergence has exponentially small tails outside each fixed positive tolerance.

Indeed given a word its admitted source representatives have mesh at most \(2\cdot2^t/3^n\); counts in every subinterval differ from the proportional count by an absolute constant. The conditional real source can therefore be coupled to a uniform \(U\) with absolute error \(O(2^t/3^n)\), whenever this error is small. The marginal actual word can first be coupled to the ideal one using (1), with exponentially small failure. Choose \(4/3<b'<\log_2 3\); the ideal clock exceeds \(b'n\) with exponentially small probability. The native affine carry gives exactly \(N/L=m/3^n+\tfrac12\sum_{j\le n}e^{-S_j}\) on a matched ideal word. This proves the weak joint limit; atomic source coordinates are compared to \(U\) by coupling or distribution functions. For \(0<p<1\), \(r_p=\mathbb E e^{-pS_1}<1\), since \(\mathbb E e^{-S_1}=1\) and the multiplier is nonconstant. Subadditivity gives \(\mathbb E Z^p\le2^{-p}\sum_{j\ge1}r_p^j<\infty\), and \(\frac12 e^{-S_1}\ge1/3\). These bounds and a Chernoff bound on \(S_n\) give the exponential part of (2). In particular every fixed bounded set of landing integers receives exponentially small mass at large grades.

## Ordinary future after the certified landing

At a fixed word, the terminal integers form the two classes \(N\not\equiv2\pmod3\) in one interval of length \((v-u)L\). Conditional on the word they are uniform in that set. For a positive integer \(k\), this distribution modulo \(2^k\) is within \(O_{u,v}(2^k/L)\) of uniform when \(L\to\infty\), by elementary progression counts. Therefore its **ordinary future** has fair independent bits for a further \(k=\max(0,\lfloor\log_2 L\rfloor-b_n)\) dates up to total variation \(O_{u,v}(2^{-b_n})\) on \(\log_2 L>b_n\), for every integer \(b_n\to\infty\). This can be coupled jointly with the stopped word; the future fair sequence is independent of the ideal initial word. For \(b_n=o(n)\) the shortened future typically ends near total native date \(n\log_2 3\). Any natural-density-zero set of ordinary integers carries vanishing landing mass: truncate \(N/L\) above by a fixed constant using (2), then count its members below a fixed multiple of \(L\) in an interval of length \((v-u)L\). This statement does not identify the later basin of one specified ordinary mark.

The reciprocal weight here is defined on the actual positive rational numerator grid. The permanent-source reciprocal criterion for ordinary Collatz trajectories in PR213 has a different source set and stopping rule. The fixed-target counterpart of this finite-grade calculation appears in [the first-passage identity](RECIPROCAL_FIXED_TARGETS.md).
