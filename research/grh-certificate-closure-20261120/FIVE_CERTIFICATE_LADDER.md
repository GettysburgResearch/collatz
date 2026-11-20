# An unbounded physical certificate rewrite for multiplication by five

**PROPOSED elementary result. No full five-closure theorem or Collatz proof.**
The rewrite below handles an unbounded certificate language and every source
odd rank at least two. Its missing cases are identified explicitly.

Use the positive shortcut map T and accelerated odd map

\[
U(n)=(3n+1)/2^{v_2(3n+1)}.
\]

Write \(I_a(q)=(2^a q-1)/3\) only when it is a positive odd integer.
An exponent word lists accelerated division exponents in forward order.
Let C be the actual basin of 1. All words here are actual positive paths,
not merely affine identities on unrestricted rationals.

## Source and scope

PR157 at `64361ecca770092d6c8242dc6211e38818af2e50`,
`research/global-closure-20261120/merger.md`, proves that

\[
x\text{ odd},\ 3\nmid x,\ x\in C\Longrightarrow5x\in C             \tag{F5}
\]

would imply full Collatz. That universal physical implication remains open.
The same PR's `closing-attempts.md`, GCL-001/002, already gives the
rank-one shifted-power obligation and the failure of a uniform inverse-lift
propagator. We credit those boundaries rather than rediscovering them.

PR162 at `2279da37ac612dbe049777354cdedb3c0aa03282`,
`research/creative-closure-20261120/five_closure.md`, C5-001/002, proves

\[
5I_2 I_b(q)=I_5 I_{b-3}(5q),\qquad b\ge4.                       \tag{S}
\]

The contribution below extends this to an arbitrary run of valuation-two
steps, proves the corresponding full certificate compiler, classifies its
ordinary source cylinders, and gives closed families at every source rank.
It does not establish a better global coverage theorem. No GRH consequence
is used in these elementary identities.

## FL1. The unbounded commutation ladder

Let \(r\ge2\), \(b\ge4\), and suppose the source word
\((\underbrace{2,\ldots,2}_{r},b)\) is a legal positive odd path from x to q.
Then

\[
\boxed{
5I_2^r I_b(q)=I_4 I_2^{r-2}I_3 I_{b-3}(5q).
}                                                               \tag{1}
\]

Thus the exact target exponent word is

\[
(4,\underbrace{2,\ldots,2}_{r-2},3,b-3).
\]

For r=1, use the previously known word \((5,b-3)\). Both sides use r+1
odd inputs and the same shortcut clock \(L=2r+b\). Every intermediate
value on both arms is a positive odd integer. In particular,

\[
T^L(x)=q,\qquad T^L(5x)=5q.                                    \tag{2}
\]

### Proof, including integrality and positivity

The r-fold inverse \(I_2\) fixes 1 and has slope \(4/3\), so

\[
x=1+\frac{4^r}{3^{r+1}}(2^bq-4)
  =\frac{2^{L}q-B_r}{3^{r+1}},\qquad
B_r=4^{r+1}-3^{r+1}.                                            \tag{3}
\]

For an odd-step word with p odd inputs at shortcut positions
\(d_0=0<d_1<\cdots<d_{p-1}\), its affine correction is
\(\sum_{j=0}^{p-1}3^{p-1-j}2^{d_j}\).
The source positions are \(0,2,\ldots,2r\), giving \(B_r\).
For r>=2 the target positions are

\[
0,4,6,\ldots,2r,2r+3.
\]

Their correction equals

\[
3^r+4\sum_{j=1}^{r-1}3^{r-j}4^j+8\cdot4^r
=5(4^{r+1}-3^{r+1})=5B_r.                                     \tag{4}
\]

For r=1 the positions \(0,5\) give correction \(3+32=35=5B_1\).
Both target words therefore have the full inverse numerator
\(2^L(5q)-5B_r=3^{r+1}(5x)\).

Full numerator divisibility implies each successive inverse division is
integral: reduce modulo 3 to obtain the final inverse division, divide that
congruence by 3, and continue. Every exponent is positive, so each inverse
output is odd. Starting at positive odd 5q, every integral inverse output
is positive. In fact none can be 1: an odd input u>1 cannot satisfy
\(I_a(u)=1\), because that would give \(2^a u=4\). Thus the target
prefix contains no 1. The source prefix contains no 1 either because
\(I_b(q)>q\) for b>=4 and \(I_2(v)>v\) for v>1.
This proves ordinary legality and (1)--(2), rather than only slope matching.

## FL2. A compiler for a whole unbounded certificate language

Suppose a supplied first-hit certificate for x has its exponent word in

\[
\mathcal L=(2^{+}\,[4,\infty))^*.
\]

Here \(2^{+}\) means one or more consecutive *letters equal to two*.
The notation is a language of exponent words, not a power of an integer.
The empty word is permitted only for x=1.

Parse the word into its unique blocks \((2^r,b)\), r>=1, b>=4.
Replace each block by FL1's corresponding target block and append the
single final exponent 4, the known edge \(5\to1\). Then the output
is a complete first-hit certificate for 5x. If p and N are the source's
odd count and shortcut clock, the output has exactly

\[
\boxed{\quad\omega(5x)=p+1,\qquad\tau(5x)=N+4.\quad}             \tag{5}
\]

To prove this, apply (2) to the first block, then to the next block on its
actual endpoint q. Every step is an ordinary positive step, so composition
preserves both arms. The input certificate has finitely many blocks, and
the compiler consumes one complete block at each iteration. Its termination
on this language therefore uses the finite input length, not a guessed
bound on the target orbit. Every target prefix avoids 1 by FL1, and the
last \(5\to1\) edge is its first arrival. This gives (5).

The algorithm explicitly returns UNRESOLVED on a valid certificate outside
this language. A malformed supplied certificate is rejected separately.
No claim about the convergence of the unresolved target is inferred.

## FL3. The ordinary source cylinders and a genuine smaller antecedent

For r>=1, the source word beginning \((2^r,b)\) with b>=4 is equivalent to

\[
x\equiv1+c_r2^{2r+2}\pmod{2^{2r+4}},\qquad
c_r=\begin{cases}1&r\text{ even},\\3&r\text{ odd}.\end{cases}     \tag{6}
\]

Indeed set \(z=U^r(x)\). The last exponent is at least four exactly when
\(z\equiv5\pmod{16}\). Using
\(x=1+(4/3)^r(z-1)\) gives (6); conversely that congruence makes the
first r exponents exactly two and gives z=5 mod16. All these sources exceed
1. Their endpoint q is an odd ternary unit and obeys

\[
q\le x/7<x.                                                     \tag{7}
\]

For (7), (3) and b>=4 give

\[
q\le\frac3{16}(3/4)^r(x-1)+\frac14
\le\frac{9x+7}{64}\le\frac x7,
\]

because the smallest possible source in these cylinders is 49.

The cylinders are disjoint: their values of \(v_2(x-1)=2r+2\) differ.
Their natural density among all positive integers is
\(\sum_{r\ge1}2^{-2r-4}=1/48\), and their relative density among odd
ternary units is 1/24. The r=1 cylinder is the earlier 49 mod64 block;
r=2 gives 65 mod256; r=3 gives 769 mod1024.
For the infinite union, the tail r>=R is contained in x=1 modulo
\(2^{2R+2}\), whose upper density tends to zero. This justifies passing
from the finite disjoint sums to the stated natural density.

If a least failed antecedent for (F5) exists, it cannot belong to any of
these cylinders: (2) and (7) would produce a smaller actual failed
antecedent q. This is a true descent on the stated union, not a claim that
the union covers all inputs.

## FL4. Explicit closed families at every source odd rank

For r>=1 and k>=1 put

\[
b=2+2\cdot3^r k,\qquad
x_{r,k}=1+\frac{4^{r+1}(4^{3^r k}-1)}{3^{r+1}}.                 \tag{8}
\]

The quotient is integral. The exact source first-hit word is
\((2^r,b)\), so its rank is r+1 and its shortcut clock is 2r+b.
FL1 followed by \(5\to1\) gives the exact target first-hit word and
rank r+2, with clock 2r+b+4. Hence this is an unconditional closed family
for every source rank at least two, with no upper bound on either r or k.

Moreover \(x_{r,k}\equiv1+k\pmod3\). One proof is the elementary lifting
identity \(4^{3^r}\equiv1+3^{r+1}\pmod{3^{r+2}}\).
Thus k=0 or 1 mod3 gives the unit members required by (F5).
At r=1, this specializes to the already known PR162 family; the larger-r
ladder and its compiler are the additional statements here.

## The attempted completion and its first unsupported step

All of FL3's source cylinders lie in x=1 mod16. There is already the much
simpler four-clock ordinary identity

\[
T^4(5x)=(15x+1)/16<x\qquad(x>1,\ x\equiv1\pmod{16}).            \tag{9}
\]

Its parities are odd, even, even, even. Thus the new content of FL1 is
transport to the *specific known-path endpoint* 5q, not discovery of ordinary
height decrease on that source class. Formula (9) does not by itself prove
(F5) there: knowing x belongs to C does not imply that every smaller integer
does. In a least-global-counterexample argument, the target in (9) is known
good only if its height is below that actual global floor. A larger oracle
antecedent arising elsewhere in a directed certificate has no automatic
access to that hypothesis.

The compiler's input word is the actual complete first-hit certificate.
It cannot alter its first division exponent or omit a letter one or three.
Expanding the rewrite dictionary can cover further patterns, but the
rank-one family from PR157 remains a terminal obstruction to this approach:

\[
x_a=(4^a-1)/3,\qquad a\ge2,\quad3\nmid a,
\]

has a one-letter source certificate (2a), while its multiplied target
reaches \((5\,9^{a-1}-1)/4\) after exactly 2a-1 odd steps.
PR157 proves that identity. No universal convergence of that residual
family is obtained here. Adding turns around 1 only appends letters two;
it does not transform the actual first exponent into a covered block.

A different attempted repair tracks a signed rational offset while consuming
the supplied inverse word. For a template
\(x_N=(2^N-B)/3^p\), run the signed shortcut on \(-5B/3^p\) until its
denominator disappears. If this takes L steps and ends at integer z, then
for every sufficiently large admissible N the actual target satisfies

\[
T^L(5x_N)=5\,2^{N-L}+z.
\]

The zero case z=0 provides a physical commutation, including FL1.
The general signed offset need not be zero or even negative. For example,
the one-letter template has initial offset -5/3 and ends at -2 after one
step. It leaves precisely a shifted-power problem. Therefore denominator
removal is not completion of the target certificate. The general signed
template idea is already used for the different target 2x-1 in PR146's
`BOUNDED_RANK_TRANSFER.md`; it is not claimed as a new general architecture.

No standard consequence of GRH is invoked to fill this ordinary all-parameter
termination gap. These results establish a larger exact certificate language,
not the universal physical law (F5).

## Verification scope

`check_five_certificate_ladder.py` independently iterates both ordinary maps,
checks the exact exponent words, the cylinder characterization, compositional
first-hit certificates, unit guards, and malformed/unresolved controls.
It uses explicit failures and remains active with optimized Python. Its
finite output is implementation evidence; the proofs above establish the
unbounded claims.
