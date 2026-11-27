# A least-source size bound for the directed transfer

**PROPOSED, written proof. Universal directed transfer remains OPEN.** Use the ordinary shortcut map \(T(2n)=n,\ T(2n+1)=3n+2\), and let \(C\) be its basin of 1. Ordinary components allow either direction of a legal \(T\) edge. A failed transfer is a positive \(u=2\bmod 9\) with \(u\in C\) and \(9u+2\notin C\).

## An actual child representative with controlled height

Write
\[
    (4u+1)/9=3^h w,\qquad 3\nmid w,\qquad B(u)=8\cdot2^h w-1.
    \tag{1}
\]
The integer \(w\) is positive and odd. The child \(9u+2\) and \(B(u)\) lie in the same ordinary component. In fact \(T^{h+3}B(u)=27\cdot3^h w-1=12u+2\), by the all-odd formula \(T^j(2^j z-1)=3^j z-1\). Two more steps lead through \(6u+1\) to the child. Thus (1) is available at every eligible ordinary source. [Lean, normalized_reaches_child and adjacent_mersenne](CanonicalSource.lean)

Suppose \(N\) is the least positive number outside \(C\). Some failed transfer satisfies
\[
                N\le B(u)\le JN,\qquad J=20970919/122875<171.
                \tag{2}
\]
Apply the finite directed descent table of PR193 to \(N\). Its endpoint is smaller than \(N\), hence good. A transition from bad to good occurs at an extra edge \(8r-1\to9r-1\), because ordinary edges preserve membership. Every extra-edge input in this table is at most \(JN\). If \(r=2^a b\) with \(b\) odd, replace the parameter by \(r'=3^a b\). Each exchange \(2s\to3s\) preserves the two labels individually, as \(T(16s-1)=24s-1\) and \(T(18s-1)=27s-1\). The PR193 physical merger excludes \(r'=3\bmod4\), so \(u=(9r'-1)/4\) is a failed transfer. Here \(h\ge a\), and \(2^hw=(2/3)^{h-a}r\le r\). Thus \(B(u)\le8r-1\le JN\). The lower bound follows from membership of \(B(u)\) in the bad child component. The argument also gives \(B_{\min}\le JN\), where the minimum is taken over all failed transfers.

The multiplier \(J\) is the exact maximum for an **extra-edge input** in the fixed 291-leaf table. It follows by replaying each affine intermediate form \(At+b\) on its certified progression \(Mt+c\), where the supremum of the ratio is the larger of \(A/M\) and \(b/c\). This existing table bound is used as a dependency. [PR193, 67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e, table, replay, and parameter reductions](https://github.com/GettysburgResearch/collatz/tree/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/rewriting)

A child component containing a positive integer \(z<B(u)/J\) therefore cannot supply a witness for (2). An orbit point is sufficient, as is an ordinary predecessor. It would suffice to obtain this contraction or a hit of 1 from the convergent parent's certificate at each eligible source.

## Actual contraction on dyadic translates

Fix any \(d\ge0\) for which \(9d+2\in C\), including \(d=0\). Let \(u=2^a v+d\) with \(a\ge1,v\ge1\) and \(u=2\bmod9\). Let \(q_a\) count the odd inputs of the first \(a\) steps of \(9d+2\). Matching the first \(a\) parity bits gives the exact ordinary child endpoint
\[
          T^a(9u+2)=T^a(9d+2)+9\cdot 3^{q_a}v .
          \tag{3}
\]
The right side is \(O_d(3^{a/2}v)\), because the reference orbit alternates between 1 and 2 after a fixed stopping time. Formula (3) already discharges every candidate for which \(J\) times its right side is less than \(B(u)\). Call a translate unresolved by this test if its endpoint in (3) is at least \(B(u)/J\). This endpoint comparison makes sense for all eligible inputs, independently of the existence of a least counterexample. From (1), any such translate must have
\[
        (2/\sqrt3)^a \ \ll_d\ (3/2)^h .
        \tag{4}
\]

For each sufficiently small \(\epsilon>0\), one also has
\[
          3^{h+2}\ll_{d,\epsilon} v(4u+1)^\epsilon .
          \tag{5}
\]
Apply Evertse's Corollary 1 to the primitive triple obtained by dividing
\((4\cdot2^a v,\ 4d+1,\ -(4u+1))\) by its common divisor \(g\le4d+1\). It sums to zero and has no vanishing proper subsum. Write \(H=4u+1\). The primitive height is \(H/g\), and the product of the prime-to-six parts of the three entries is at most \(v(4d+1)H/3^{h+2}\). Evertse's lower bound \(c_\epsilon(H/g)^{1-\epsilon}\) gives (5). The constant absorbs the theorem's finitely many exceptions. [Evertse, Corollary 1, printed p. 227](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

In particular along any sequence of translates unresolved by the endpoint test with fixed reference \(d\) and \(a\to\infty\),
\[
     \liminf \frac{\log v}{a}
       \ \ge\ \frac{\log(2/\sqrt3)\log 3}{\log(3/2)} .
       \tag{6}
\]
Indeed (4) and (5) give \(a\log(2/\sqrt3)\le[\log(3/2)/\log3](\log v+\epsilon\log(4u+1))+O_{d,\epsilon}(1)\). Use \(\log(4u+1)=a\log2+\log v+O_d(1)\), divide by \(a\), and let \(\epsilon\) decrease to zero. The constants can depend on the certified reference. This discharges sufficiently deep translates with \(\log v=o(a)\), including all fixed \(d,v\) of the indicated kind. The conclusion concerns which candidates can occur in a least-source proof. It does not certify all of their child orbits individually.

For the formerly unresolved terminal family \(u=2^{6j+1}\), all \(j\ge0\) can be excluded as witnesses for (2) effectively. Here \(h=v_3(2j+1)\) by the odd-exponent lifting identity \(v_3(2^{6j+3}+1)=1+v_3(6j+3)\). Formula (3) gives the child endpoint \(E=9\cdot27^j+1\) at the parent's stopping clock. Since \((2/3)^h\ge1/(2j+1)\), (1) gives \(B(u)\ge3u/(2j+1)\) (use \(5u+8\ge9(2j+1)\)). For \(j\ge10\), \(171 E<1550\cdot27^j<6\cdot64^j/(2j+1)\le B(u)\). The middle strict inequality holds by direct integer comparison at 10 and persists since \(64/27>(2j+3)/(2j+1)\). For \(0\le j<10\), the actual children hit 1 after respectively \(6,23,64,108,114,120,107,319,306,228\) shortcut steps. These finite certificates and the threshold arithmetic are replayed in [check.py](check.py). [Prior terminal family, frozen at 174f5ce593473f49962ab253548693183314391e](../../astra-global-budget-20261124/arithmetic/README.md)

## Reselecting the boundary for a parent with one odd step

Consider the other extreme \(u=(2^\ell-1)/3\), \(\ell=18j+16\). This parent is \(2\bmod9\) and reaches 1 after exactly \(\ell\) steps with one odd input. The child \(3\cdot2^\ell-1\) has \(\ell\) successive odd steps leading to \(3^{\ell+1}-1\). The endpoint at the parent's stopping clock exceeds \(u\). A decrease can instead be sought in a different pair of physical components.

Set \(M_d=2^d-1\). Since \(T(M_{\ell+1})=3\cdot2^\ell-1\), a failed transfer here makes \(M_{\ell+1}\) bad. Choose the smallest positive \(d\le\ell+1\) with \(M_d\) bad. Then \(d\ge3\), and \(M_{d-1}\) is good. At the actual extra-edge input \(M_d=8\cdot2^{d-3}-1\), its target \(9\cdot2^{d-3}-1=T^2(M_{d-1})\) is good. The parameter exchange normalizes to \(r'=3^{d-3}\). Even \(d\) would give \(r'=3\bmod4\) (for \(d\ge4\)), already physically merging. Thus \(d\) is odd, and the new failed transfer is
\[
        U=(3^{d-1}-1)/4,\qquad B(U)=M_d .
        \tag{7}
\]
Indeed \(4U=3^{d-1}-1=T^{d-1}(M_{d-1})\). This certifies the new parent's component from the known smaller Mersenne. The new parent cannot itself have the original form \((2^\ell-1)/3\) with \(\ell\ge1\), since that would require \(3^d+1=2^{\ell+2}\) while \(v_2(3^d+1)=2\). Thus one-odd odd-parent failures could be removed completely if the directed transfer were proved on the other parents. The argument never assumes that the two arms have the same clock.

When the original one-odd parent satisfies (2), the replacement exponent is confined to
\[
       \log_2(1+B(u)/J)\le d\le\ell+1,
       \quad
       B(u)=\frac{8}{27}(2/3)^h(2^{\ell+2}-1)-1,
       \quad h=v_3(j+1).
\]
The valuation follows from \(v_3(2^{\ell+2}-1)=1+v_3((\ell+2)/2)\). The lower bound uses \(M_d\ge N\ge B(u)/J\). Thus the possible transition lies within \(O(\log\ell)\) exponents of the original one. Its own canonical size need not be at most \(JN\).

The surviving fixed-source question is whether every candidate in (2) can be discharged by an ordinary child component representative below \(B(u)/J\), a physical convergence certificate, or a provably descending reselection. In (7) this already asks for a way to pass from an actual certificate of \(M_{d-1}\) to a lower representative or a certificate of \(M_d\) for arbitrary odd \(d\). Neither (3) nor reselection alone establishes this inference.
