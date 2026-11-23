# A finite rational-dual certificate for eventual periodicity

23 November 2026. **Status: written finite certificate with Lean-checked
numerical core. Universal witness construction and full Collatz remain
OPEN.**

The earlier construction sought a complementary point in `Z[1/3]`,
which is strong enough to force the standard cycle. This attack allows
an arbitrary positive odd denominator. It gives a finite, explicitly
bounded test sufficient for eventual periodicity, then uses the new
complementary-denominator capacity bound to control the possible period.
The broader search space removes a genuine arithmetic obstruction to
triadic approximation; it does not yet produce the required witness for
every positive source.

Monks--Yazinski's [primary paper](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
Theorem 2.1 and its proof in Section 4.2, already relates rational
autoconjugacy on positive integers to exclusion of divergent orbits.
That qualitative reduction is credited, not presented as a new result.
The explicit finite horizon and excursion proof below are derived here;
no claim of literature priority is made.

## 1. Literal paired trajectories and the finite statement

Use the shortcut map on positive integers,

\[
T(x)=\begin{cases}x/2,&x\text{ even},\\(3x+1)/2,&x\text{ odd}.
\end{cases}
\]

Fix `n>=1`, `a` an integer, and `q>=1` odd. Define the ordinary numerator
map on all signed integers

\[
S_q(w)=\begin{cases}w/2,&w\text{ even},\\(3w+q)/2,&w\text{ odd}.
\end{cases}
\]

Both divisions are exact. Put `x_k=T^k(n)` and `w_k=S_q^k(a)`.
A paired test at clock `k` means

\[
       x_k\bmod2+w_k\bmod2=1.                         \tag{1}
\]

This is an ordinary finite condition. The rational candidate is `a/q`;
because `q` is odd its 2-adic parity is the numerator's parity, even
when the displayed fraction is not reduced.

For a nonnegative integer `m`, let `bl(m)` be the least positive `L`
such that `m<2^L`. Define integers

\[
\begin{aligned}
J&=2q+2,& B&=n\max(1,|a|),\\
M&=B(4q)^J,& L&=\operatorname{bl}(M),\\
R&=(4q+3)L,& t_*&=J(R+1),\\
H(n,a,q)&=t_*+L
  =\bigl(J(4q+3)+1\bigr)L+J.                         \tag{2}
\end{aligned}
\]

**Finite rational certificate.** If (1) holds for every `0<=k<H`, then
either the original orbit reaches 1 at a clock below `H`, or there are
`0<=i<j<t_*` with

\[
                  (x_i,w_i)=(x_j,w_j).                \tag{3}
\]

In particular, the ordinary input enters a positive integer cycle before
clock `H`. Its primitive cycle length is at most `2q`, by Section 5.
The finite test is sufficient, not asserted to succeed for every input.

## 2. An excursion potential that handles both signs and zero

Put

\[
                 V_k=x_k\max(1,|w_k|).               \tag{4}
\]

This is a positive integer. Call a clock small when `|w_k|<=q`.
There are exactly `2q+1` possible small numerator values, including
zero and both signs. In particular, the fixed numerator zero is not
discarded. The proof needs no separate sign-transition argument.

Until the original orbit reaches 1, its values satisfy `x_k>=2`.
At a large clock write `x=x_k`, `x'=x_(k+1)`, `A=|w_k|`,
`A'=|w_(k+1)|`. Then `A>=q+1`. Under the paired test:

- If `x` is even, `2x'=x` and `2w'=3w+q`. The triangle inequalities
  give `3A-q<=2A'<=3A+q`. In particular `A'>=1`.
- If `x` is odd, `2x'=3x+1` and `2A'=A`, again with `A'>=1`.

Thus `V=xA` and `V'=x'A'` at such a step. In the even case,

\[
4(q+1)V'\le(q+1)x(3A+q)
\le(4q+3)xA,
\]

where the last difference is `xq(A-q-1)>=0`. In the odd case,

\[
4(q+1)V'=(q+1)(3x+1)A\le(4q+3)xA,
\]

where the difference is `A(q(x-1)-1)>=0`. Therefore

\[
\boxed{V_{k+1}\le\rho V_k\quad(|w_k|>q),\qquad
       \rho=\frac{4q+3}{4q+4}<1.}                    \tag{5}
\]

At a small clock, the literal updates instead give
`x_(k+1)<=2x_k` and `|w_(k+1)|<=2q`. Since `q>=1`,

\[
\boxed{V_{k+1}\le4q\,x_k\le4q\,V_k.}             \tag{6}
\]

Equations (5)--(6) are the finite numerator/height estimates used below.
They are valid for negative numerators as well as positive ones.

## 3. A bounded supply of small numerator visits

Let `c=4q+3`. Bernoulli's inequality gives

\[
\left(1+\frac1c\right)^c\ge2,
\qquad \rho^c\le\frac12.                            \tag{7}
\]

Consequently a run of `R=cL` large clocks beginning with `V<=M`
would end with

\[
              V_{\rm end}\le2^{-L}M<1,              \tag{8}
\]

contradicting its positive integrality. This argument uses the exact
finite run and no limiting drift or expectation.

Suppose now that the original orbit has not reached 1 before `H`.
Before the `J`th small visit, there have been at most `J-1` small
updates. Equations (5)--(6) imply at all these clocks

\[
              V_k\le B(4q)^{J-1}\le M.              \tag{9}
\]

There must be at least `J` small clocks among `0,...,t_*-1`. To see
this rigorously, suppose there were fewer. Then (9) holds throughout
this interval. Partition the interval into `J` consecutive blocks of
length `R+1`. A block with no small clock contains `R` consecutive
large updates and contradicts (8). Each block therefore contributes
a small clock, contradicting the supposed count.

Select the first `J=2q+2` small visits. Their values `w_k` lie in a set
of size `2q+1`. Hence there are `i<j<t_*` with `w_i=w_j`, and (9)
holds at both clocks. In particular

\[
                         0<x_i,x_j\le M<2^L.        \tag{10}
\]

## 4. The extra parity window forces an ordinary repeated state

The map `S_q` is deterministic, so `w_i=w_j` implies
`w_(i+t)=w_(j+t)` for every `t>=0`. The assumed paired tests through
`H=t_*+L` therefore give identical original parities for the two
length-`L` windows starting at `i` and `j`.

For completeness, finite parity coding is injective modulo `2^L`.
If two original inputs `u,v` share a length-`L` parity word with `p`
odd letters and complete affine carry `C`, then

\[
2^L T^L(u)=3^p u+C,\qquad
2^L T^L(v)=3^p v+C.
\]

Subtracting and using `gcd(3^p,2^L)=1` gives
`2^L | (u-v)`. Applied to (10), this forces `x_i=x_j`. Together with
the repeated numerator, it proves (3). Future paired tests now hold
on the repeated block forever, by determinism. This completes the
finite certificate proof.

### One equivalent endpoint congruence

Let `e_k=x_k mod2`, `b_k=sum_(i<k)(1-e_i)`, and let the complementary
carry obey

\[
D_0=0,\qquad D_{k+1}=3^{1-e_k}D_k+(1-e_k)2^k.
\]

The first `H` paired tests are equivalent to

\[
\boxed{2^H\mid3^{b_H}a+qD_H.}                        \tag{11}
\]

Indeed, iterating the prescribed complementary affine branches gives
the endpoint `(3^b_H a+qD_H)/(q2^H)`. If this is 2-adically integral,
every earlier prescribed branch is integral: a first parity failure
creates a negative 2-adic valuation, and each subsequent branch lowers
it by one, since multiplication by three and addition of an integer
cannot cancel it. Thus a final integral endpoint rules out every earlier
failure. The converse is the finite affine identity.

The endpoint test in (11) still uses the literal actual prefix from the
one fixed positive source, and its clock depends on the supplied
candidate's own height and denominator.

## 5. What the new complementary-cycle bound adds

The separate [capacity proof](../cycles/COMPLEMENTARY_DENOMINATOR_CAPACITY.md)
shows that a nontrivial positive integer cycle of primitive shortcut
length `K` has full complementary reduced denominator `d>K/2`.
The standard cycle has `K=2,d=1`.

In case (3), the paired numerator is periodic too. Its rational values
are `w_k/q`, so their reduced denominators divide `q`. The full
complementary cycle denominator is therefore at most `q`, giving

\[
                       \boxed{K\le2q.}              \tag{12}
\]

If the certificate instead detects 1, its eventual period is two and
(12) holds because `q>=1`. This use of the capacity bound concerns an
actually proved eventual cycle; finite parity agreement alone is not
silently treated as a periodic dual.

For `q=3^r`, the eventual complementary denominator is prime to three
and divides `3^r`, hence is one. A nontrivial cycle would then have
`K<2`, which is impossible. Thus this coarser certificate also recovers
convergence for triadic witnesses. PR176's pinned amortized triadic
budget is substantially better in that specialized denominator class.

## 6. The attempted universal construction and the remaining gap

Equation (2) has size

\[
H=O\!\left(q^2\bigl(\log n+\log(1+|a|)+q\log(2q)\bigr)\right).
\]

It replaces an unverifiable all-time rationality premise by a finite
arithmetic test allowing all odd denominators. This is a broader
construction target than the triadic test. The source-specific
approximation needed to fund its own horizon is still unproved.

Ordinary rational-approximation pigeonhole arguments do not supply it.
Even their denominator may be even; cancelling a power of two then
loses prefix bits. The [selector attack](../triadic/README.md) retains
that loss and the actual source-height budget. No generic approximation
estimate is promoted to a successful ordinary selector.

Even universal success of the rational certificate would first exclude
escape. The possible denominators and nontrivial cycles would still
need control. This note proves neither a uniform denominator bound nor
unrestricted positive-cycle exclusion.

## Formal and review scope

[RationalExcursions.lean](lean/RationalExcursions.lean) checks the signed
absolute-numerator inequalities, both large-state contraction estimates,
the small-state growth estimate, the Bernoulli half-block bound, finite
geometric decay, and the impossibility of an overlong positive high run.
The full visit-count/pigeonhole argument, parity coding, endpoint
congruence, and use of the cycle capacity result have written-proof
scope. The Lean module does not assert the universal existence of a
candidate or a complete formalization of this finite certificate.
