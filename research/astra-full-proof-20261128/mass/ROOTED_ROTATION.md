# A first-hit necklace admits at most one small positive root cut

For an inverse gap block \(A\) of length \(a>0\) and sum \(s_A\), write its real affine map as \(A(z)=(2^{s_A}z-D_A)/3^a\) with positive integer \(D_A\). An integer path is legal only when each affine step is integral. In particular any two integral initial arguments for the entire block differ by a multiple of \(3^a\).

**Written theorem.** Suppose two distinct circular cuts of the same length-\(h\) word produce strictly first-hit inverse paths from the ordinary integer 1, with the immediate return to 1 excluded. Split the necklace into nonempty blocks \(A,B\) at the two cuts. Both \(u=A(1)\) and \(v=B(1)\) are odd and greater than 1. Block \(B\) is legal at 1 and at \(u\), and \(A\) at 1 and at \(v\). Thus \(u\ge1+2\cdot3^{|B|}\) and \(v\ge1+2\cdot3^{|A|}\). Positivity of the two affine offsets gives
\[
 2^{s_A}>3^{|A|}u>2\cdot3^h,\qquad
 2^{s_B}>3^{|B|}v>2\cdot3^h.
\]
Consequently \(2^{s_A+s_B}>4\cdot3^{2h}\). In particular every nonempty word in the [ordinary record flux](RECORD_FLUX.md), whose sum is at most \(7h/4\), has exactly one such cyclic cut, and is primitive. A nontrivial repetition would give a second admissible cut at the repetition period. A ballot or cycle lemma that freely selects a cyclic rotation must retain this root test.

Every first-hit path of length \(h>0\) from 1 back to an integer \(m>1\) also has a periodic rational completion of reduced denominator strictly exceeding \(3^h\). Indeed write its full inverse map as \((2^s z-D)/3^h\), so \(D=2^s-3^hm>0\). Put \(V=2^s-3^h>0\). The fixed point \(D/V\) lies strictly between 0 and 1. Because \(V\) is prime to 3,
\[
 \gcd(D,V)=\gcd(V,m-1),\qquad
 \frac{V}{\gcd(D,V)}\ge \frac{2^s-3^h}{m-1}>3^h .
\]
The bound concerns the word's periodic completion. Its physical path is terminating and has different endpoints.

The empty record is excluded from both statements. Neither the uniqueness nor the denominator floor supplies a lower bound on the number or total weight of rooted necklaces.
