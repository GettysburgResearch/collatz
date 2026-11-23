# The full complementary denominator pays for the cycle period

23 November 2026. **Status: written capacity theorem and an unclosed
cycle-symmetry attack. Unrestricted positive-cycle exclusion remains OPEN.**

The attempted closing step was to force the complementary periodic point
of an ordinary integer cycle into the triadic class. The argument below
does not supply that arithmetic cancellation. It instead proves an
explicit period bound in terms of the complementary point's **fully
reduced numerical denominator**:

> If a nontrivial positive integer shortcut cycle has least period `K`
> and its complementary cycle has reduced denominator `q`, then `K<2q`.
> The core has `K=2,q=1`. Thus every such integer cycle has `K<=2q`.

This can be used after an arbitrary-rational dual certificate establishes
an eventual paired cycle. It does not construct that certificate or give
an upper bound on `q` over all integer cycles. The proof uses distinct
ordinary numerator values in a rational cycle, not independent rotations
or a replacement random-word law. No historical novelty is asserted for
the general cycle-product method or finite-denominator cycle bounds.

## 1. A capacity inequality for any positive rational cycle

Use the shortcut map `T(x)=x/2` for even rational 2-adic integers and
`T(x)=(3x+1)/2` for odd ones. Let a positive rational cycle have least
shortcut period `L`, exactly `h>=1` odd states, and common reduced
denominator `q>=1`, with `gcd(q,6)=1`.

The common-denominator assumption is automatic for a rational cycle:
an odd step removes a factor of three if the reduced denominator still
contains one, so periodicity excludes that factor. Once the denominator
is prime to six, neither legal branch changes it. Positivity excludes
the all-even orbit. Write the odd states as `y_i/q`, where the `y_i`
are distinct positive odd integers. Multiplication of all `L` branch
ratios gives

\[
 2^L=\prod_{i=1}^h\left(3+\frac q{y_i}\right).
 \tag{1}
\]

After sorting, `y_i>=2i-1`. Define, for real `t>0`,

\[
 f(t)=(1+t)\log(1+t)-t\log t.
 \tag{2}
\]

**Theorem 1 (full-denominator capacity).** One has the strict inequality

\[
 \boxed{L\log2-h\log3<h f\!\left(\frac q{6h}\right).}
 \tag{3}
\]

**Proof.** From (1) and the sorted numerator bound,

\[
 L\log2-h\log3
 \le\sum_{i=1}^h\log\left(1+\frac{q/6}{i-1/2}\right).
 \tag{4}
\]

For `a=q/6>0`, the function `g(x)=log(1+a/x)` is strictly convex on
the positive real axis:

\[
 g''(x)=\frac{a(2x+a)}{x^2(x+a)^2}>0.
\]

Its midpoint value on each interval `(i-1,i)` is strictly smaller
than its integral average there. The improper integral at zero exists;
alternatively, integrate the strict symmetric midpoint inequality over
the open interval. Therefore

\[
 \sum_{i=1}^h g(i-1/2)
 <\int_0^h g(x)\,dx
 =h\log(1+a/h)+a\log(1+h/a)
 =h f(a/h).
\]

This proves (3). Only distinctness and positive odd integer numerators
were used in the estimate. Additional coprimality restrictions could
shrink the admissible set but are not assumed to provide a further
saving. \(\square\)

The theorem concerns `q` after **every integer gcd** has been removed.
It is not a bound on a polynomial denominator before evaluation.

## 2. Apply the inequality to the complementary cycle

Let an actual nontrivial positive integer cycle have least shortcut
period `K`, `p` odd states, and `b=K-p` even states. Its minimum `m`
is at least five. Indeed the minimum must be odd, a periodic positive
state is prime to three, and a cycle containing one is the core.

The ordinary cycle product gives

\[
 2^K=\prod_{\text{ordinary odd states }x}
      \left(3+\frac1x\right)
 \le(16/5)^p.
 \tag{5}
\]

Since `(16/5)^7<2^12`, equivalently `2^16<5^7`,

\[
 \frac pK\ge\frac{\log2}{\log(16/5)}>\frac7{12},
 \qquad 0<\beta:=\frac bK<\frac5{12}.
 \tag{6}
\]

Complement the actual primitive parity word. Its complete affine carry
is `C_*`, its odd count is `b`, and its fixed rational value is

\[
 y=\frac{C_*}{\Delta_*},\qquad
 \Delta_*=2^K-3^b>0,\qquad
 \boxed{q=\frac{\Delta_*}{\gcd(\Delta_*,C_*)}.}
 \tag{7}
\]

The sign follows already from `b<K/2`; its numerator is positive.
Both `b` and `p` are nonzero. The denominator is prime to six.
The standard parity coding, or the finite affine fixed-word calculation,
gives the legal complementary rational cycle. Its least period is `K`:
complementing letters preserves the least word period, and repetition
of an affine block with slope different from one has the same unique
fixed point as that block. A shorter state period would give a shorter
parity period. Thus the `b` odd states used below are distinct.

Theorem 1, applied to this complementary cycle, gives

\[
 \log2<\beta\log3+\beta f\!\left(\frac q{6\beta K}\right).
 \tag{8}
\]

**Theorem 2 (a period bound for an integer cycle and its rational dual).**
For every nontrivial positive integer cycle,

\[
                         \boxed{q>K/2.}                 \tag{9}
\]

**Proof.** Suppose `q<=K/2`. Since `f'(t)=log(1+1/t)>0`, (8) implies

\[
 \log2<G(\beta),\qquad
 G(\beta)=\beta\left(\log3+f\!\left(\frac1{12\beta}\right)\right).
\]

Using `f(t)-tf'(t)=log(1+t)` gives

\[
 G'(\beta)=\log3+\log\left(1+\frac1{12\beta}\right)>0.
\]

But (6) and the exact numerical comparison `3^11<2^6*5^5` give

\[
\begin{aligned}
 G(\beta)&<G(5/12),\\
 \log2-G(5/12)
 &=\frac1{12}\log\frac{2^6 5^5}{3^{11}}
 =\frac1{12}\log\frac{200000}{177147}>0.
\end{aligned}
\]

This contradicts (8). \(\square\)

For the core, the complementary cycle is the same `1,2` cycle, so
`K=2,q=1`. Hence the non-strict conclusion `K<=2q` covers every
positive integer cycle. No claim is made that there exists a nontrivial
cycle realizing the remaining parameter range.

## 3. The stronger continuous envelope

The same argument retains the actual minimum. Put

\[
 \beta_m=1-\frac{\log2}{\log(3+1/m)}.
\]

For `0<beta<=1/2`, let `t_beta>0` be the unique solution of

\[
 f(t_\beta)=\frac{\log2}{\beta}-\log3,
 \qquad c(\beta)=6\beta t_\beta.
 \tag{10}
\]

Existence and uniqueness follow because `f` is strictly increasing from
zero to infinity. Differentiation yields

\[
 c'(\beta)
 =-6\frac{\log3+\log(1+t_\beta)}{f'(t_\beta)}<0.
\]

Thus (8) and `b/K<=beta_m` imply the exact bound

\[
                     \boxed{q/K>c(\beta_m).}             \tag{11}
\]

For orientation, numerical evaluation of this explicit function gives
`c(beta_5)=0.5930284976...`, and as `m` tends to infinity its value tends
to `0.7864098721...`. These decimals are illustrations, not constants
used in Theorem 2.

There is a uniform large-period version even without assuming that the
minimum increases. Apply Theorem 1 to the original integer cycle, with
denominator one and `h=p`. Since `log(1+t)<t`,

\[
 0<K\log2-p\log3
 <p f(1/(6p))
 <\frac{1+\log(6p+1)}6
 \le\frac{1+\log(6K+1)}6.
 \tag{12}
\]

Consequently, writing `beta_0=1-log(2)/log(3)`,

\[
 \beta_0<\frac bK<
 \beta_0+\frac{1+\log(6K+1)}{6K\log3}.
 \tag{13}
\]

Combining (8), (10), and (13) shows that along any hypothetical sequence
of primitive positive integer cycles with periods tending to infinity,

\[
 \liminf \frac qK\ge c(\beta_0)=0.7864098721\ldots .
 \tag{14}
\]

This is a conditional statement about such a sequence, not an existence
claim. Its denominator remains the full numerical denominator in (7).

## 4. Use in an arbitrary-rational certificate

Suppose a matching complementary rational trajectory begins with an
odd denominator `Q`, and a separate argument proves an eventual paired
cycle with a positive ordinary integer orbit. The rational map does not
introduce denominator factors, so the eventual complementary denominator
`q` divides `Q`. Theorem 2 therefore gives

\[
                   K\le2q\le2Q.                         \tag{15}
\]

This supplies a period bound once the eventual cycle is established.
A finite agreement prefix alone is not silently promoted to an all-time
rational dual here; that promotion or a repeated paired state must be
proved by the separate certificate argument. Formula (15) does not bound
the preperiod or construct a matching rational candidate for an arbitrary
positive input.

## 5. The symmetry attack and the exact remaining line

The intended arithmetic closure was `q=1`, or more generally enough
complementary cancellation to contradict (9). The original integer-cycle
condition is `2^K-3^p | C`, whereas (7) involves the different complete
carry and denominator of the complementary word. Cyclic rotations
preserve each reduced denominator; they do not turn one of these
divisibility conditions into the other.

Monks--Yazinski already proved that the only self-conjugate integer cycle
is the core. Their Example 5 also supplies a useful boundary control:
the negative integer cycle `-5,-7,-10` has complementary positive cycle
`4/5,2/5,1/5`. In the word `110`, the original denominator is `8-9=-1`
and the complementary denominator is `8-3=5`. Thus a purported purely
unsigned integrality/rotation identity forcing `q=1` is false. A closing
argument must use the original positivity in an additional way.

Here positivity gives the lower bound (9), not an upper bound on `q`.
The raw `Delta_*` can grow exponentially with `K`, and the available
ordinary integrality identity has not forced a sufficiently large gcd
with `C_*`. Neither `q<=K/2` nor triadic duality was proved. The cycle
problem is not closed by this capacity calculation.

## Sources and formal scope

The classical parity coding, autoconjugacy, and the self-conjugate-cycle
facts were read in Kenneth G. Monks and Jonathan Yazinski,
*The autoconjugacy of the 3x+1 function*, Sections 1--3, Theorems
2.3--2.5 and Example 5, [primary author PDF](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf).
The capacity proofs above are self-contained real inequalities for
finite actual cycles. No external mixing, unit-equation or logarithmic
form theorem is used in them.

The current PR182 complete-word matching attempt and PR175 Hankel
attempt were inspected to keep the full-denominator and rotation
dependencies explicit. Their independent unresolved estimates are not
assumed here; exact source heads and paths are recorded in the
accompanying source ledger.

All new claims in this note have written-proof scope. No new Lean
declaration, unrestricted cycle exclusion, or finite search over unknown
periods is claimed.
