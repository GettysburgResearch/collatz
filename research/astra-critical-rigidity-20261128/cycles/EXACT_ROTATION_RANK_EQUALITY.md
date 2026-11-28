# The native rotation–rank bound is attained at every even period

**Proposed written theorem.** For every \(n\ge1\) a genuine positive rational odd cycle has primitive period \(p=2n\), exactly \(u=2\) valuation mismatches under rotation by \(n\), chronological degree \(r=n+1\), and complete reduced denominator \(q=4^n+3^n\). In particular \(u(r-1)=p\) at unbounded periods. This attains the constant one in the [universal finite rotation–rank bound](OPTIMAL_ROTATION_DENOMINATOR_ORDER.md). These examples have mean valuation two and physical widths tending to four.

Take the cyclic valuation word
\[
                    (1,\underbrace{2,\ldots,2}_{n-1},
                       3,\underbrace{2,\ldots,2}_{n-1}).
\]
Its unique entry \(1\) makes it primitive, and its half-turn interchanges exactly the two exceptional entries. With the cut before the entry \(1\), its cumulative sum \(E_i\) equals \(2i-1\) for \(1\le i\le n\) and \(2i\) at all other dates in \(0\le i\le 2n\). Thus its positive fixed point is given by
\[
 x_0=\frac{\sum_{i=0}^{2n-1}3^{2n-1-i}2^{E_i}}{4^{2n}-3^{2n}}
    =1-\frac{2\,3^{n-1}}{4^n+3^n}.
\]
Indeed the unmodified sum with \(2^{E_i}=4^i\) is \(4^{2n}-3^{2n}\). Half of the terms on \(1\le i\le n\) must be subtracted; their half-sum is \(2\,3^{n-1}(4^n-3^n)\). The displayed \(q\) is odd and prime to three, so this fraction is reduced. At every rotated cut the affine closure has odd numerator over the odd raw determinant; the odd-to-odd updates therefore reproduce the given valuations exactly. The affine word has contraction factor \((3/4)^{2n}\), so its positive fixed point and primitive valuation word give least odd period \(2n\).

For all \(i\), \(2^{E_i}/4^i\) is periodic with period \(2n\), equal to \(1/2\) on one consecutive interval of length \(n\) and one elsewhere. Its Fourier transform has positive constant term. At a nontrivial character it is proportional to the sum of \(n\) consecutive powers of a \(2n\)-th root \(\zeta\), nonzero exactly when \(\zeta^n=-1\). The minimal rational shift polynomial of \(U_i=2^{E_i}\) is therefore \((T-4)(T^n+4^n)\). The unfolded physical state \(V_i=2^{E_i}x_i\) has the same modes: \(U=(S-3)V\), and \(S^{2n}V=4^{2n}V\) excludes three from its spectrum. Thus \(r=n+1\), and the full denominator even equals the absolute minimal polynomial evaluated at three. [Dyadic input and minimal denominator formula](MINIMAL_RECURRENCE_DENOMINATOR.md)

The maximum is \(x_1=2-3^n/q\) and the minimum is \(x_{n+1}=1/2+3^n/(2q)\), with indices read cyclically. The intervening valuation-two steps send \(x\) to \(1+(3/4)(x-1)\), decreasing to one on the first half and increasing to one on the second. These formulas give the claimed width limit.
