# Long ordinary residence below a factor of four forces a continued-fraction gap

**Proposed written theorem.** Fix \(2<R<4\), let \(\gamma=\log_2 3\), and put \(\theta=0.3197044778974\ldots,\ a=1-3\theta\), as in the [native binary rate bound](GLOBAL_DYADIC_PAIR_ABUNDANCE.md). Take any segment of \(T\) **distinct** positive odd states of an ordinary Collatz orbit in \([M,RM]\), with \(M\to\infty\). If \(q_-\le T<q_+\) are the consecutive continued-fraction denominators of \(\gamma\) at this length, then
\[
                         q_-\le M^{\theta+o(1)}.                       \tag{1}
\]
Uniformly on sequences with \(T\ge M^{\theta+\epsilon}\) for some fixed \(\epsilon>0\),
\[
                       q_+\ge T\,M^{a/2-o(1)}.                         \tag{2}
\]
In particular, residence through a convergent-denominator scale \(q\) requires \(M\ge q^{3.12788862\ldots-o(1)}\). Both bounds use classical continued fractions and the stated narrow-band source estimates. They do not need the exponent-three logarithm theorem, cycle closure, a bounded future orbit, or an assertion about typical partial quotients.

Equivalently, for any fixed \(\epsilon>0\) and large enough \(M\), each such trajectory must exit or repeat an odd state before it contains as many distinct states as the first denominator \(q>M^{\theta+\epsilon}\). Weaver's [Theorem 6, physical-band residence](https://rstation.ai/problems/collatz/papers/145/v1) already gives \(T\le M^{v+o(1)}\), \(v=0.4333973955184\ldots\), with no condition on the convergent gaps. Both restrictions apply; (1) supplies a stronger power at convergent scales. This conclusion also distinguishes the native length \(T\) of the actual run from the logarithmic coding length in the [source-population theorem](../literature/CONFINED_SOURCE_ENTROPY.md).

## Two grids for one nonperiodic segment

It suffices to consider \(\log T/\log M\to\lambda>\theta\) for (2), and to rule out \(\limsup\log q_-/\log M>\theta\) for (1). In both proofs we may pass to convergent subsequences of exponent ratios; \(T\le M^{v+o(1)}\) by the primary source above, with \(v<1/2\). Let \(h/q\) be a reduced convergent of \(\gamma\) and let \(q'\) be its next denominator. In (1) take \(q=q_-\); in (2) take \(q=q_+\). In either case \(q\ge M^{\theta+o(1)}\) on a sequence where the desired conclusion fails. Assume \(q\le M^{O(1)}\), as is immediate on either failed conclusion. Define the true-time sampling scale
\[
      U=\left\lfloor\frac{\min(T,q,M/q)}{1000(\log M)^3}\right\rfloor.
\]
For \(q=q_-\) we have \(U=qM^{o(1)}\), since \(q\le T\) and \(T^2=o(M)\). For \(q=q_+\), when testing failure of (2), we have \(q\le T M^{a/2}\) eventually on the offending subsequence. This implies \(qT\le M^{2v+a/2+o(1)}=o(M)\) and hence \(U=TM^{o(1)}\). In either use \(U\) grows polynomially. We will obtain
\[
  \frac{\log U}{\log M}
     -\frac13\left(\frac{2\log q+\log U}{\log M}-1\right)_+
                           \le\theta+o(1).                              \tag{3}
\]

Choose the integers \(0\le s\le U\) as genuine native offset times and write \(j_s\equiv hs\bmod q\), \(0\le j_s<q\). They give distinct reduced ranks. Partition the rank circle into \(O((\log M)^3)\) consecutive cells of length \(O(q/(\log M)^3)\). One cell contains \(U M^{-o(1)}\) times. Subtract the time and rank of its smallest spatial member from all its members. The resulting time offsets may have either sign, with \(|s|\le U\); their spatial representatives now satisfy \(0\le j_s\le O(q/(\log M)^3)\). Put \(k_s=(hs-j_s)/q\in\mathbb Z\). On the actual open segment form \(V_t=2^{E_t}x_t\) and \(D_s=2^{-k_s}\operatorname{shift}^{s}\), where \(E_t\) is the cumulative true native division. The operators commute. All later compositions contain at most eleven shifts, staying within \(11U\) native dates of their base. We use them only inside the given segment. There is no continuation by a rational cycle.

With \(L=M(1+R/4)\) and \(F_t=\lfloor\log_2(V_t/L)\rfloor\), set \(Z_{t,s}=2^{-F_t}(D_sV)(t)\) and \(C_{t,s}=Z_{t,s}/x_{t+s}\). For the complete sample and the shifts occurring in the eleventh powers, the true log increment on \(|s|\) native dates gives
\[
 \log_2\!\left(\frac{Z_{t,s}}{2^{-F_t}V_t}\right)
   =s\gamma-k_s+O(U/M)
   =j_s/q+O\!\left(U/M+\frac{U}{q q'}\right).
\]
Denote the latter error bound by \(\Delta\), choosing an absolute constant for up to eleven offsets. The definition of \(U\) and \(q'\ge q\) imply \(q\Delta=o(1)\). The interval \(RM/2<L<2M\) therefore makes all these tags one or two, exactly as in the [finite native prime-dilation proof](FROBENIUS_BAND_EXITS.md).

Suppose two different unordered pairs of starts give equal normalized integer label sums at an anchor in the middle of the segment. The signed operator \(Q=D_i+D_j-D_u-D_v\) then annihilates \(V\) on the preceding third of the segment, by the backward integer sign rule on these binary tags. Its action on \(2^{E_t}\) also vanishes there by the original native affine relation. The first ten shifts move by at most \(10U\), so \(Q^{11}(2^{E_t})=0\) on a fixed smaller interval. Reducing in the dyadic shift ring modulo 11 gives the exact vanishing of \((D_i^{11}+D_j^{11}-D_u^{11}-D_v^{11})(2^{E_t})\) there: multiplication by \(2^{-F_t}\) gives an integer of absolute value at most eight. The corresponding operator on \(V\) vanishes at an interior point by full dyadic divisibility over \(O(\log M)\) consecutive forward dates, available since \(T\) grows polynomially. This supplies two actual equalities at a common date.

The \(j_s/q\) shape error is \(o(1/q)\). Thus the labels increase strictly with \(j_s\), and equal sums from different pairs have nested ranks \(i<i+d\le i+b<i+b+f\), with \(d,b,f\) positive integers and \(d\le b\). For the rank polynomial in \(z=2^{1/q}\), after translation these two equalities give errors \(O(\Delta)\) at \(z\) and \(z^{11}\). The same positive difference identity as in the native-tube proof gives \(bf\ll q^2\Delta\) and \(|d-f|\ll q\Delta=o(1)\). In particular \(d=f\) as integers. This intermediate bound still contains the convergent-slope error.

## Removing that error with chronology

The rank rectangle gives equality of the sums of the two pairs of \(j_s\)'s. As \(hs\equiv j_s\bmod q\) and \(\gcd(h,q)=1\), the two sums of their true time offsets agree modulo \(q\). Each \(|s|\le U=o(q)\), so they agree **exactly as integers**. Their two sums of \(k_s\)'s then agree as well. Consequently the four exact homogeneous factors \(w_s=2^{s\gamma-k_s}\) satisfy the multiplicative rectangle law \(w_iw_l=w_jw_k\) at the four increasing ranks. Here subscripts list the sample members in rank order. The error in replacing their normalized labels by \(w_s\) times one common base label is now \(O(U/M)\) relative to that base, regardless of \(q'\). At the common date where the original comparison vanishes, factor the homogeneous comparison:
\[
 0< w_i(w_j/w_i-1)(w_k/w_i-1)
                       =w_i+w_l-w_j-w_k\ll U/M .
\]
Indeed \(|s\gamma-k_s-j_s/q|\le U/(q q')=o(1/q)\), so each of the two multiplicative increments is positive and at least a constant times its positive rank gap divided by \(q\). We have proved that every potential collision is a rank rectangle of integer side lengths satisfying
\[
                                 db\ll q^2 U/M .                        \tag{4}
\]
This step uses the original irrational slope after identifying the exact chronological rectangle. Treating \(h/q\) as the true orbit rotation throughout would retain an extra error depending on \(q'\).

There are \(O(E\log(2+E))\) four-distinct and \(O(\sqrt E)\) three-distinct candidate rectangles per smallest rank, with \(E=C q^2 U/M\). The independent sampling and deletion argument in the tube proof gives a subset of at least \(U M^{-o(1)}(1+E)^{-1/3}\) starts on which the true integer pair sums distinguish every unordered pair. Its actual binary tag words from the future \(n=\lceil\log_3(32M)\rceil+3\) dates distinguish all pair sums by the full affine cylinder. Its native winding sum is \(n\gamma+O(1+n/M)\); the [ordered-difference chain entropy estimate](GLOBAL_DYADIC_PAIR_ABUNDANCE.md) bounds its cardinality by \(M^{\theta+o(1)}\). This proves (3).

For \(q=q_-\), put \(\xi=\lim\log q/\log M\). Equation (3) says \(\xi-(3\xi-1)_+/3\le\theta\). The left side is \(\min(\xi,1/3)\), and \(\theta<1/3\), giving (1). For \(q=q_+\), if (2) fails then on a subsequence \(\xi=\lim\log q/\log M<\lambda+a/2\) and \(U=TM^{o(1)}\). As \(\lambda>\theta\), (3) requires \(2\xi+\lambda-1>0\) and yields \(2(\xi-\lambda)\ge1-3\theta=a\), a contradiction. This proves the gap statement.
