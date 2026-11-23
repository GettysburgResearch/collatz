# Effective cycle classification in bounded power languages

**Date:** 2026-11-22 UTC.  
**Repository baseline supplied by the coordinating agent:** PR 185,
`276be8154f4e867acc0230466b34d9cb224aacf5`.  
**Status:** complete written proof using a published effective logarithm bound;
the accompanying Lean file verifies the finite bit-budget argument, not
Matveev's theorem. This is a cycle theorem for a specified language. It does
not assert that all Collatz trajectories or all cycle words belong to one
bounded language.

## 1. Statement

Use the shortcut Collatz map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

Let \(V_1,\ldots,V_r\) be a specified finite list of **nonempty binary parity
words**, with \(r\ge1\). An exponent vector consists of independently chosen
integers \(e_i\ge0\). Consider nonempty words

\[
W=V_1^{e_1}\cdots V_r^{e_r}.
\]

For a block \(V_i\), write its formal affine map, length, and odd count as

\[
F_i(x)=\frac{a_i x+C_i}{2^{L_i}},\qquad
a_i=3^{s_i},\quad C_i\in\mathbb Z_{\ge0},\quad L_i>0.
\]

Put

\[
D_i=2^{L_i}-a_i,\qquad c_i=C_i/D_i.
\]

Every \(D_i\) is a nonzero odd integer. Let \(\mathcal E\) be the finite set
of positive Collatz cycles obtained from those \(c_i\) that are positive
integers. An integral fixed point of a formal parity word realizes that word;
this fact is proved below. Consequently these are actual cycles, not formal
rational candidates.

**Theorem.** The set of positive integer cycles admitting a period word in
\(V_1^*\cdots V_r^*\), or a cyclic rotation of such a word, is effectively
computable. More explicitly, define

\[
\begin{aligned}
K&=2^{33},& B&=2\sum_{i=1}^r|c_i|,\\
b&=\min\{j\ge0:B+1\le2^j\},&
d&=\min\{j\ge0:\max_i(|D_i|+C_i)\le2^j\},\\
A&=2^r-1,& C&=b+3K+1+d,\\
J&=AC.
\end{aligned}
\]

Choose any integer \(q\ge0\) with

\[
2^q\ge J(q+2). \tag{1}
\]

Every actual cycle word \(W\) whose underlying cycle is not in
\(\mathcal E\) has total shortcut length

\[
\boxed{\quad N=\sum_i L_i e_i<2^q.\quad} \tag{2}
\]

All exponents are independent. Blocks with no odd steps and zero exponents
are allowed. Empty base blocks can first be deleted. A full empty word is
excluded, since it imposes no periodicity condition.

This strengthens the previous packet's one-parameter schema result:
there is no requirement \(e_i=a_i k+b_i\), no common parameter, and no
dominant-root classification of a one-variable power sum.

## 2. Exact physical divisibility of a repeated block

For any binary word, start with the rational branch maps
\(f_0(x)=x/2\) and \(f_1(x)=(3x+1)/2\). Their composition has an odd
coefficient \(a=3^s\), denominator \(2^L\), and integral nonnegative
translation numerator \(C\).

**Integrality detects the entire word.** Starting from an integer, suppose
the first chosen branch with the wrong parity occurs. Its output has odd
numerator and denominator 2. Thereafter an even branch doubles this
denominator, while an odd branch changes an odd numerator \(u\) over
\(2^j\), \(j\ge1\), to \(3u+2^j\) over \(2^{j+1}\). The numerator
remains odd. The final value therefore cannot be an integer. Conversely,
a correct parity word clearly ends at an integer. Starting positive keeps
all its actual iterates positive.

For one block, let \(D=2^L-a\), \(c=C/D\), and \(\mu=a/2^L\). Then

\[
F^e(x)=c+\mu^e(x-c),\qquad
D2^{Le}F^e(x)=a^e(Dx-C)+C2^{Le}. \tag{3}
\]

Since both \(a\) and \(D\) are odd, and the denominator of the composed
word is a power of 2, (3) proves the exact equivalence

\[
V^e\text{ is physically legal at an integer }x
\quad\Longleftrightarrow\quad 2^{Le}\mid Dx-C. \tag{4}
\]

The reverse implication can also be checked directly: write the composed
word as \((a^e x+C_e)/2^{Le}\), where
\(DC_e=C(2^{Le}-a^e)\). Multiplication by the odd integer \(D\)
does not change divisibility by \(2^{Le}\).

For \(e>0\), there are exactly two possibilities:

* If \(Dx-C=0\), the block already fixes the actual positive state \(x=c\).
* Otherwise,
  \[
  2^{Le}\le |Dx-C|\le(|D|+C)(x+1). \tag{5}
  \]

The first case must be removed **before** estimating total word length.
If an actually traversed block fixes its entry state, determinism says that
the whole closed orbit is precisely that block's finite cycle. It belongs
to \(\mathcal E\), even if other blocks and the full word traverse it many
times. Arbitrarily large exponents of a fixed block cannot create new
cycles. In every cycle outside \(\mathcal E\), (5) holds at every used
block. A zero exponent has zero duration and needs no such premise.

## 3. A rotation with uniformly bounded translation

Fix an actual exponent vector and put
\(m_i=(a_i/2^{L_i})^{e_i}>0\). Let

\[
N=\sum L_i e_i,\qquad S=\sum s_i e_i,\qquad
M=\prod m_i=3^S/2^N.
\]

A positive cycle has \(M<1\). Indeed its complete affine map is
\(x\mapsto Mx+Q\) with \(Q\ge0\). If there is an odd step, \(Q>0\), so
\(x=Mx+Q\) implies \(M<1\). If there are no odd steps, the map is
\(x\mapsto x/2^N\), which has no positive fixed point. Equality \(M=1\)
is also impossible for \(N>0\), by the distinct prime factors 2 and 3.

Let \(P_0=1\) and \(P_j=m_1\cdots m_j\). Choose an index
\(j\in\{0,\ldots,r-1\}\) minimizing \(P_j\), and rotate the blocks to
start after that boundary. Every suffix product in this rotated list is
at most 1. For a suffix starting before the wrap, its product is
\(MP_j/P_{\ell-1}\le M\); for one after the wrap, it is
\(P_j/P_{\ell-1}\le1\).

Write \(x_0\) for the actual cycle value at the selected boundary. Since
the translation of \(F_i^{e_i}\) is \(c_i(1-m_i)\), its full rotated
translation is

\[
Q=\sum_i c_i\left(\prod_{j>i}m_j-\prod_{j\ge i}m_j\right).
\]

Both products in each summand lie in \((0,1]\). The triangle inequality
therefore gives the deliberately loose but uniform bound

\[
0<Q\le B=2\sum_i|c_i|,\qquad x_0=Q/(1-M). \tag{6}
\]

This rotation is allowed to depend on the exponent vector. Only the bound
\(B\), which is unchanged by rotation, is used. A start inside a block
does not cause a loophole: a cyclic rotation of a realized full word is
realized by another point of the same positive cycle, and can be rotated
back to the displayed block boundaries.

## 4. An explicit lower bound for the full multiplier gap

The external input is Matveev's **Corollary 2.3**, printed page 1219 of
his 2000 paper. We use the actual linear-form version, not a rounded
numerical approximation to \(\log 3/\log 2\). Its bound is

\[
\log|\Lambda|>
-C_1(n)D^2\Omega\log(eD)\log(eB^*),
\]

with \(C_1(2)\le2^{32}\). For \(\alpha_1=2\), \(\alpha_2=3\),
field degree \(D=1\), admissible height parameters \(A_1=1,A_2=2\),
and integer coefficients \(N,-S\), we have \(\Omega=2\) and
\(B^*=N\), since \(0\le S\le N\). Thus

\[
\Lambda=N\log2-S\log3>0,\qquad
\Lambda>e^{-K}N^{-K},\quad K=2^{33}. \tag{7}
\]

For \(0<\Lambda\le1\), use
\(1-e^{-\Lambda}\ge\Lambda/2\); for \(\Lambda>1\), use
\(1-e^{-\Lambda}>1/2\). Since \(e<4\), both cases imply

\[
1-M>2^{-(2K+1)}N^{-K}. \tag{8}
\]

Equations (6) and (8) give

\[
x_0+1<(B+1)2^{2K+1}N^K. \tag{9}
\]

No enormous number of size \(2^{2K}\) needs to be constructed by the
algorithm: only its exponent enters the next bit-length estimate.

## 5. The dyadic budget closes

For a positive integer \(x\), let
\(H(x)=\lfloor\log_2(x+1)\rfloor+1\), so \(x+1<2^{H(x)}\).
Let the duration of a block be \(\ell_i=L_i e_i\). From (5) and the
definition of \(d\), every nonfixed used block satisfies

\[
2^{\ell_i}\le |D_i x_i-C_i|
\le2^d(x_i+1)<2^{d+H(x_i)},
\qquad\ell_i\le H(x_i)+d. \tag{10}
\]

The same final inequality holds for a zero duration. Every actual shortcut
step satisfies \(T(x)+1\le2(x+1)\). If the preceding blocks have consumed
\(P\) steps, their next boundary has
\(H(x_i)\le H(x_0)+P\). Therefore

\[
\ell_i\le H(x_0)+d+P,
\qquad P_{\rm next}\le2P+H(x_0)+d.
\]

Induction over at most \(r\) blocks proves

\[
N\le(2^r-1)\bigl(H(x_0)+d\bigr). \tag{11}
\]

Put \(p=\lfloor\log_2N\rfloor\), so \(2^p\le N<2^{p+1}\). By (9),
the definition of \(b\), and \(K>0\),

\[
x_0+1<2^{b+3K+1+Kp},\qquad
H(x_0)\le b+3K+1+Kp.
\]

Since \(C=b+3K+1+d\ge K\), (11) yields

\[
N\le A(C+Kp)\le AC(p+1)=J(p+1). \tag{12}
\]

If (1) holds at \(q\), it holds with \(p\) in place of \(q\) for every
\(p\ge q\): doubling its right-hand comparison easily dominates the
increase from \(p+2\) to \(p+3\). If \(p\ge q\), then

\[
2^p\le N\le J(p+1)<J(p+2)\le2^p,
\]

a contradiction. Hence \(p<q\), and \(N<2^q\), proving the theorem.
An admissible \(q\) is found by increasing integers and comparing exact
integers in (1). Exponential growth ensures that this search terminates.

## 6. Complete effective algorithm and its honest computational scope

1. Compute \((L_i,s_i,C_i,D_i)\) exactly for each base word.
2. For every positive integral \(c_i=C_i/D_i\), replay \(V_i\) at that
   value. Record its primitive cycle, identifying cyclic rotations. These
   are the exceptional cycles \(\mathcal E\).
3. Compute \(B,b,d,J\) and a certified \(q\) from (1).
4. Enumerate every exponent vector with
   \(0<\sum L_i e_i<2^q\). Compose the affine maps over the **full word**.
   If its result is \((3^Sx+C_W)/2^N\), its only candidate fixed point is
   \(C_W/(2^N-3^S)\). Keep only positive integral candidates and physically
   replay the full word, including its closing edge.
5. Deduplicate the resulting primitive cycles together with \(\mathcal E\).

All loops are finite. Every exception belongs to the unrestricted-star
language, by taking that one exponent to be 1 and the others to be 0.
Every other represented cycle is found in step 4. This is a complete
decision procedure for the specified bounded language; it is not a claim
that a naive enumeration up to the very conservative bound is practical.

The accompanying certificate program computes and checks the exact
language-dependent bound, the block data, and the exceptional cycles. It
does **not** pretend to have executed step 4 at the Matveev bound. The
coordinating agent's separate \(P^mQ^n\) argument uses continued fractions
and the exact periodic denominator to eliminate that family efficiently.

If an application requires all \(e_i>0\), the same bound remains valid.
Exceptional cycles must then additionally be checked for membership in
that restricted language; the unrestricted-star classification stated
here deliberately allows zero exponents.

## 7. Uniform theorem for bounded power-block complexity

Fix integers \(r,h\ge1\). Consider any positive cycle having a period
word that is the concatenation of at most \(r\) powers of binary words of
length at most \(h\), with arbitrary block order and independent exponents.
There are finitely many possible base-word lists, but there is also a direct
uniform bound.

For every length-\(L\le h\) block,

\[
0\le C_i\le3^L-2^L<3^h,
\qquad |D_i|\le3^h,
\qquad |c_i|\le3^h.
\]

The first inequality follows by evaluating the formal maps at zero: at
each step the odd branch gives at least as large a value as the even
branch, so the all-odd word maximizes the translation. Hence the previous
proof works with

\[
B=2r3^h,\qquad d=2h+1,
\qquad 2^b\ge1+2r3^h.
\]

A cycle fixed by a used base block has primitive period at most \(h\).
Consequently **every cycle of primitive period greater than \(h\) with
such a representation has the computable length bound (2)**. Short-period
cycles are independently finite and effectively enumerable from binary
words of length at most \(h\).

This also states an explicit obstruction to an indefinitely compressible
cycle word: at fixed \(h\), the number of power blocks required by a long
new cycle must grow. It supplies no universal bound on that number, and
does not address unbounded nonperiodic orbits.

## 8. Exact constants for the repository's mixed block

Convert an odd-gap block \((a_1,\ldots,a_s)\) into the shortcut parity
word \(10^{a_1-1}\cdots10^{a_s-1}\). For

\[
P=(1,1,4,1,1,1,2),\qquad Q=(2),
\]

the affine block data are

\[
F_P(x)=-41+\frac{2187}{2048}(x+41),
\qquad F_Q(x)=1+\frac34(x-1).
\]

Thus \(c_P=-41\), \(c_Q=1\), \(B=84\), \(b=7\), \(d=13\), and

\[
J=3(3\cdot2^{33}+21)=77\,309\,411\,391.
\]

The exact comparison

\[
2^{42}=4\,398\,046\,511\,104
\ge44J=3\,401\,614\,101\,204
\]

therefore proves that **any cycle represented by \(P^mQ^n\) which is not
the trivial cycle has \(11m+2n<2^{42}\)**, with \(m,n\) independent.
The only prelisted block-fixed cycle is \(1\leftrightarrow2\), from \(Q\).
This statement is a length bound, not by itself the exclusion of every
positive pair \((m,n)\).

## 9. Relation to the literature and to the remaining global problem

Simons and de Weger define an \(m\)-cycle by its number of local minima.
Their approach compares an exponentially small dynamical upper estimate
for a linear form in \(\log2,\log3\) with a transcendence lower bound,
then uses continued fractions or lattice methods for effective exclusions.
Their paper also explains the earlier fixed-\(m\) finiteness result of
Brox. The present proof uses the same broad mechanism, with arbitrary
repeated composite parity blocks and the exact divisibility (4). A fixed
number of such power blocks need not bound the number of local minima,
because repeating a mixed block creates more minima. No claim of
historical priority for this formulation is made.

The decisive gain over the previous one-parameter work is independent
exponents. The decisive uncovered quantifier is still the number and
length of the base blocks: a hypothetical general cycle can have
unbounded power-block complexity, and an escaping trajectory need not
have a periodic word at all. The argument does not silently replace
those possibilities by a bounded language.

### Primary sources actually inspected

1. E. M. Matveev, *An explicit lower bound for a homogeneous rational linear
   form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics
   64:6 (2000), 1217–1269, DOI
   [10.1070/IM2000v064n06ABEH000314](https://doi.org/10.1070/IM2000v064n06ABEH000314).
   [Stable primary landing page](https://www.mathnet.ru/eng/im314).
   Corollary 2.3 on printed page 1219 was read from the full English PDF;
   both its logarithm form and its explicit constant were checked.
2. J. Simons and B. de Weger, *Theoretical and computational bounds for
   m-cycles of the 3n+1 problem*, Acta Arithmetica 117 (2005), 51–70,
   DOI [10.4064/aa117-1-3](https://doi.org/10.4064/aa117-1-3).
   The [authors' version 1.43 of July 31, 2007](https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf)
   was inspected, especially its definition, introduction, Theorem 3,
   chain equation, and logarithm-form setup. Historical computation bounds
   in that revision are not inputs to this theorem.
