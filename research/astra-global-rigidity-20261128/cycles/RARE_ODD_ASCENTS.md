# A decidable sparse set that must supply the expansion of every escaping orbit

Let \(T\) be the positive shortcut map, \(U\) the map from one odd state to the next, and \(b_t(n)=2Q_t(n)-t\). The elementary finite-record theorem computes
\[
 g(n)=-\min_{t\ge0} b_t(n),\qquad W(n)=n2^{-g(n)},\qquad
 \mathcal P=\{n:b_t(n)>0\ \text{at every positive time}\}.
\]
The scan uses at most \(\lceil D^{-1}\log_2(2n)\rceil\) native steps to compute \(g(n)\), where \(D=1-\tfrac12\log_2 3\). In particular \(\mathcal P\) is decidable, since \(n\in\mathcal P\) exactly when \(n\) is odd and \(g(Tn)=0\). The ordinary count through \(N\) is \(O(N/\sqrt{1+\log N})\), by the elementary ballot bound in the finite-record theorem. The normalized height \(W\) is a positive rational, invariant under all initial halvings, with \(1\le W(n)\le n\). [Exact parity-record horizon](EXACT_PARITY_RECORD_HORIZON.md)

For an odd input, the exact formula is
\[
 \boxed{\frac{W(Un)}{W(n)}=(3+1/n)2^{-2+\mathbf1_{\mathcal P}(n)}.}   \tag{1}
\]
Every odd input \(n>1\) outside this sparse set strictly contracts \(W\). For an odd start \(x\), let \(A_j(x)\) count visits to \(\mathcal P\) among \(x,Ux,\ldots,U^{j-1}x\). Set \(\gamma=2-\log_2 3\). Then there is a dichotomy at an explicitly specified straight line:

* Every escaping positive orbit satisfies \(A_j(x)-\gamma j\to+\infty\).
* Every eventually periodic positive orbit satisfies \(A_j(x)-\gamma j=-c_x j+O_x(1)\) for some \(c_x>0\).

These are necessary and sufficient asymptotic classifications because a bounded subsequence of a positive orbit forces repetition. They provide no upper occupation bound on an escaping ray. Testing \(\mathcal P\) at one supplied state is a finite algorithm. Determining which asymptotic alternative holds for a supplied infinite path still requires control of that path.

## The exact height and visit identity

Removing the first letter in the definition of \(g\) gives
\[
 g(2y)=1+g(y),\qquad g(n)=\max(0,g(Tn)-1)\quad(n\ \text{odd}).        \tag{2}
\]
Thus \(W(2y)=W(y)\), and an odd input has \(g(Tn)=g(n)+1\) unless it belongs to \(\mathcal P\), in which case both values vanish. The equation \(Tn=(3n+1)/2\) proves (1), including \(n=1\). In the native clock (2) also gives the pointwise identity
\[
 b_t(n)=g(T^t n)-g(n)+\sum_{i<t}\mathbf1_{\mathcal P}(T^i n).          \tag{3}
\]
To see \(W(n)\ge1\), the height inequality \(1\le T^t n\le n2^{b_t(n)}\) gives \(g(n)\le\log_2 n\). If \(g(n)>0\), let \(v\) be the first deepest record and \(q=Q_v(n)\). Its endpoint satisfies
\[
 T^v n<\tfrac12+(3/4)^q W(n)\le\tfrac12+W(n).                        \tag{4}
\]
For \(g(n)=0\) the source itself has \(W(n)=n\). On a positive escape, the minimum of each remaining tail tends to infinity. Applied at every source on that tail, (4) proves \(W(U^j x)\to\infty\). An ordinary path is therefore bounded if \(W\) has a bounded subsequence along it. Telescoping (1) now gives
\[
 A_j-\gamma j=\log_2\frac{W(U^j x)}{W(x)}
       -\sum_{i<j}\log_2(1+1/(3U^i x)).                                \tag{5}
\]
On an escape the last sum is bounded by the simple-path packing below. On a periodic tail \(W\) is bounded and the correction has a strictly positive mean on its finite lap. This proves both claims. In particular the normalized density lower bound \(\gamma=0.415037\ldots\) on the odd clock is strengthened to divergence of its unnormalized excess along every end date. Simplicity without a packing estimate would give only a harmonic majorant for this correction.

For completeness an elementary packing proof suffices. On a dyadic octave \([Y,2Y)\) set \(h=\lfloor\log_2Y\rfloor\) and \(F=Y^{0.99}\). Except for \(O(Y^{1-c})\) starts, for some absolute \(c>0\), the first \(h\) native departures have at most \(0.55h\) odds. This is the true length-\(h\) parity bijection, the ordinary binomial Chernoff bound, and the bounded number of representatives of each residue. Every such start has a visit below \(F\) within \(h\) steps for large \(Y\): otherwise its terminal state is at most \(2Y\,2^{-h}(3+F^{-1})^{0.55h}<F\), since \(0.55\log_2 3<0.99\). On any fixed simple segment, the good starts with complete future windows lie within \(h\) dates before one of at most \(F+1\) distinct small states. At most \(h\) terminal positions lack a complete window. Thus the number of octave visits is \(O(Y^{1-c'} )\) for some \(c'>0\), uniformly in the segment. Summing the reciprocal bound over dyadic octaves gives an absolute finite upper bound. This packing mechanism is established prior work. [Weaver 176, §5.1 after (26)](https://rstation.ai/problems/collatz/papers/176) · [PR195, source occupation at 3fa7ef4a](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/SOURCE_OCCUPATION.md)

## The map on states with nonnegative future discrepancy

Write \(\mathcal B=\{n:g(n)=0\}\). From \(n\in\mathcal B\) take its first odd step to \(y=Tn\), then follow \(y\) through the first attainment of its own deepest deficit; call the result \(\Phi(n)\). It is in \(\mathcal B\) by count additivity. Since \(g(y)\le1\), precisely two cases occur. If \(g(y)=0\), then \(n\in\mathcal P\), the transition uses a single odd departure, and the total discrepancy increases by one. If \(g(y)=1\), then \(n\notin\mathcal P\), and the path from \(n\) through \(\Phi(n)\) is its first positive-time return to discrepancy zero, strictly positive at internal dates. It has \(q\ge1\) odd departures and \(2q\) total departures; its weak-record affine bound gives
\[
                \Phi(n)-1\le(3/4)^q(n-1).                              \tag{6}
\]
In particular every balanced return outside one strictly decreases its integer starting state. Iterating only balanced returns therefore reaches one or a member of \(\mathcal P\) after finitely many steps, and the number of native steps through those returns is \(O(1+\log n)\). Indeed their cumulative \(Q\) satisfies \(1\le x_{\rm end}-1\le(3/4)^Q(n-1)\) up to any endpoint above one. For a last return ending at one, its internal strict ballot shape provides an independent bound: just before the end the state is two, and all previous grades were positive except the initial zero. Equivalently, from \(Tn\) that return goes to its first negative record, whose supplied integer time is already bounded by the finite horizon. To implement a balanced transition, stop the scan at its first negative crossing from the successor: the incoming promise of membership in the nonnegative set already rules out any deeper deficit there. Only the final positive decision needs a full additional horizon scan. Thus detecting the next strict ascent or reaching one uses a total logarithmic native clock. If \(n\in\mathcal P\), its first step is odd and goes to \(\mathcal B\), which consists of odd states. This gives \(n\equiv3\bmod4\).

Starting at \(n\in\mathcal P\), make that one increasing step and then all balanced returns at the new level. The endpoint is either one or the next strict ascent site. If these returns use \(q\) odd departures, its height \(n'\) satisfies
\[
                n'-1\le (3/4)^q(3n-1)/2.                              \tag{7}
\]
The case \(q=0\) is \(n'=(3n+1)/2\). For \(q=1\) the only balanced block is \(10\), giving \(n'=(9n+5)/8\). For \(q\ge2\) and \(n\ge5\), (7) forces \(n'<n\). As a result any least nonconvergent source would start at a member of \(\mathcal P\), and its first transition to the next member would have \(q\le1\). This specific residue restriction can also be checked by ordinary short stopping-time sieves. The finite induced map gives no proof that successive transitions must ultimately descend below the initially supplied source.
