# Positive offsets obstruct uniform affine resets

**Written theorem.** The comparison \(F(q)=(183q+1)/128\) from the two-light theorem need not return to its original affine formula on any later prefix of an infinite positive-growth *symbolic* L/P string. There are uncountably many such strings, including nonperiodic ones. Every finite section has arbitrarily large positive ordinary realizations. These statements do not assert that one ordinary source realizes one of the infinite strings.

## An explicit change of sign

Begin at a boundary with two leading L's, so \(F\) is an ordinary integer. Each of the four displayed source words \(X\) ends in L and is followed by at least two L's. If its terminal boundary is \(q\), the same comparison at the complete source clock is
\[
 Z(q)=\frac{61}{384}(q+7)+2 .
\]
The last L forces \(3\mid q+7\); the next two give \(128\mid q+7\), hence \(Z(q)\) is integral. If the source data of \(X\) are \(A,p,C\), the target uses \(A\) clocks, \(p-2\) odd inputs, and carry
\[
 K=\big(61C+1195\cdot2^A-3\cdot3^{p-2}\big)/384 .
\]
The exact finite parity test computes the initial residue \(-K3^{-(p-2)}\bmod2^A\), follows it for \(A\) clocks, and checks both count and carry. This certifies the trajectory for every ordinary lift. The first three seeds can follow any additional initial lights, and through the fourth one the first paid loop has precisely the formerly missing PLLL exit.

| Seed \(X\) | Source clocks \(A\) | Source odd inputs \(p\) | Target carry |
|---|---:|---:|---:|
| LLPPLLLPLPLLLLLPL | 61 | 34 | 8369972547102266119 |
| LLPLLPPLPLLLLLPL | 58 | 32 | 1040345204821122287 |
| LLPLLPLPLLLLLPL | 53 | 30 | 32641194658480951 |
| LLPLLPLLLPLPLLLLLPL | 67 | 38 | 536649599247780160663 |

Prepending one or more free lights gives at least three initial lights and \(F(q_0)/2\) as the smaller positive odd original source. Its orbit joins the comparison with one clock offset.

## A whole symbolic family with no return

At any later boundary write the comparison chart as \(a(q+7)+c\), \(a>0\). This is always possible for a fixed literal comparison branch on an ordinary cylinder, since the input and target have affine laws over that branch. Denote its normalized constant \(R=c/a\). Over an input \(Dq'=9q+d\) the actual target bits have some odd count \(u\), nonnegative carry \(K\), and the same binary clock. The outgoing slope is \(a'=3^{u-2}a\), and
\[
 R'=\frac{9R-(7D+d-63)}{D}+\frac{K}{D a'} .
\]
Thus \(R'\ge9R/8\) on L and \(R'\ge(9R-166)/32\) on P. At the seed \(R=768/61>12\).

Now append any sequence of groups consisting of at least 37 L's and then three arbitrary L/P letters. Starting at \(R\ge12\), all intermediate values stay positive and the next group starts at \(R\ge12\). Indeed the smallest possible update in the final three steps is three successive paid lower bounds. Writing \(G(t)=(9t-166)/32\), exact substitution gives \(G^3(12(9/8)^{37})>13\). The light lower bound dominates the paid one on this positive interval. In particular the tail can mix infinitely many PPP and PLP bursts. The least possible source multiplier over such a group is \((9/8)^{37}(9/32)^3>1\).

At every prefix after the seed the constant \(c\) is strictly positive. An affine return to \(F(q)= (183/128)(q+7)-10\) has negative constant. Each possible finite choice of target parities is a dyadic subcylinder; if nonempty, translating by a sufficiently large power of two provides infinitely many ordinary lifts of that branch. Therefore equality at all inputs of a cylinder would require equality of affine coefficients. It cannot hold. Even a uniform different prescribed target clock cannot make an \(F\)-to-\(F\) whole-word identity: equality of slopes from original \(F\) to terminal \(F\) forces the target clock and odd count to equal their source counterparts by unique factorization. The argument leaves accidental meetings of single sources, other charts and non-merging nonconvergence comparisons open.

Every finite source word is realized at a positive odd source in an arithmetic progression: if its length in clocks, odd count and carry are \(A,p,C\), the residue \((2^A-C)3^{-p}\bmod2^{A+1}\) gives an odd terminal boundary and hence the prescribed binary word. The branch choices in successive groups allow infinitely many nonperiodic schedules. This distinguishes failure of a uniform reset inference from the open ordinary infinite-path question.

## Why very long light runs do not complete the proof

A proposed argument from the positive offset required the next light run to exceed the cumulative ternary deficit of a hypothetically convergent comparison. It fails a size test for ordinary source realizability. Let \(b\) be the number of source blocks since the positive-offset seed, \(P_b\) the number of paid blocks, \(A=3b+2P_b\), and \(u\) the odd visits in the corresponding target clocks. The slope is \(a_b=(61/384)3^{u-2b}\). A convergent comparison has \(u=A/2+O(1)\). A prospective run of \(r\) actual lights gives \(q_b+7\ge 2\cdot8^r\). Positivity of \(c_b\) makes \(Y_b>a_b(q_b+7)\). The tempting contradiction would require \(3r-(\log_2 3/2)\max(b-2P_b,0)\) to grow without bound, forcing \(Y_b>2\) on that run.

For any ordinary input, however, the centered P update \((9(q+7)+166)/32\) is at most the light update \(9(q+7)/8\) for positive \(q\). Therefore \(3r\le b\log_2(9/8)+O(1)\). On the displayed sparse family \(P_b\le3b/40+O(1)\), making the desired lower threshold at least \(0.67b+O(1)\), whereas the actual upper bound grows at \(0.17b+O(1)\).

There is also an obstruction independent of the sparse grammar. At every ordinary source boundary \(q_i\ge3\), multiplying the raw block equations gives
\[
 q_b\le q_0\,3^{2b}2^{-A}(34/27)^b .
\]
The factor \(34/27\) bounds \(1+d/(9q_i)\) for both block carries. If \(Y\) converges, the quantity \(a_b(q_b+7)\) then tends to zero, with upper bound a source-dependent constant times \((17\sqrt3/36)^b\). Indeed \(q_b+7\le(10/3)q_b\), \(3^u=O(3^{A/2})\), and \(A\ge3b\). A positive offset can coexist with this decay. Thus the long-run criterion contributes no new ordinary nonconvergence theorem. [Finite controls](controls.py)
