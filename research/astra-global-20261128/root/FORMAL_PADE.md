# Finite Padé barriers on actual ordinary Collatz clocks

This development formalizes a connected arithmetic argument: explicit polynomial coefficients, integral linear forms, finite cancellation, exact binary valuation, an ordinary integer size comparison, and remainders supplied by the **same actual Collatz run**. Its positive-clock endpoint has compiled with strict warnings and no implicit variables. The pass replay checks its entire dependency chain and declaration axioms afresh at each checkpoint.

The map is the shortcut map
\[
 T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
 \end{cases}
\]
Let \(t_j(n)\) be the time of its even input numbered \(j\), starting at zero. In the code this is `PinCriterion.clock j n`. Its first value is \(v_2(n+1)\). The code uses natural numbers for physical states and clocks, integers for the cleared forms, and rationals for finite sums. No infinite series or completed p-adic field is needed.

## The actual-clock theorem

For natural \(b,h,s,n\), with \(h>0\), assume the **actual** observed clocks satisfy
\[
 t_j(n)=j(b+1)+h\binom j2\qquad(0\le j\le5s+2).
\]
Then [PadeObserved.lean](PadeObserved.lean), `actual_clock_height_barrier`, proves
\[
 \boxed{\quad 2^{3hs^2+4bs}\le(n+2)^{17}.\quad}
\]
The clock assumption at zero forces the source to be even. All later hypotheses concern a finite initial segment of its real execution. In particular, the final theorem does not assume the required Padé remainders, their valuations, or an abstract approximation property. It derives them from those clocks.

If \(n+2\le2^B\), `actual_clock_exponent_bound` gives the exact integer consequence
\[
                       3hs^2+4bs\le17B.
\]
There is no logarithmic-form theorem or ineffective constant in this proof.

## An arbitrary initial odd run and a physical cutoff

[PadeWindow.lean](PadeWindow.lean) removes the initial-even restriction. Suppose \(h>0\) and
\[
 t_j(n)=a+j(b+1)+h\binom j2\qquad(0\le j\le K),\qquad K\ge12,
\]
and the matching prefix has length
\[
 L\le a+(K+1)(b+1)+h\binom{K+1}{2}.
\]
Here \(K\) is the zero-based last observed even index, so \(K\ge12\) means at least thirteen observed even inputs. The final run can be cut at any time before its next prescribed even input; the ceiling on \(L\) does not require that next actual input to have been observed. The assumption at zero identifies \(a=v_2(n+1)\). Given an integer bit budget \(n+1\le2^B\), `long_window_bound` proves
\[
                  \boxed{\quad L\le579B+289.\quad}
\]
For \(B\ge1\), `long_window_linear_bound` gives \(L\le868B\). This is a theorem about a finite physical window, with every initial-run normalization included.

The normalization uses the elementary formal inequality
\[
 T^{v_2(n+1)}n+1\le(n+1)^2.
\]
It follows from \(2^a(T^a n+1)=3^a(n+1)\), \(2^a\le n+1\), and \(3^a\le4^a\). For the interpolation index \(s=\lfloor(K-2)/5\rfloor\), Lean proves \(5s+2\le K\) and \(K+1\le9s\). The last incomplete run costs at most \(17(3hs^2+4bs)\).

This formal endpoint deliberately states its integer bit budget and the condition \(K\ge12\). The separate [written theorem](../broad/QUADRATIC_CLOCK_PADE.md) treats short windows and gives \(1000\log_2(n+1)\) with a real logarithm. The statement in Lean is not silently identified with that stronger all-window formulation.

## The finite proof chain

Put \(\operatorname{tri}(j)=\binom j2\), \(q=(3/2)^h\), \(z=2^{b+1}/3^b\), and
\[
 p_l=z^lq^{-\operatorname{tri}(l)},\qquad
 R(X)=\prod_{j=1}^{N}(1-q^jX).
\]
The interpolation order \(N\) and shift \(M\) are independent natural parameters until the final choice \(N=2s,M=s\).

| File | What is proved |
| --- | --- |
| [PadeArithmetic.lean](PadeArithmetic.lean) | Triangular-number identities, the explicit polynomial and its degree bound. |
| [FinitePade.lean](FinitePade.lean) | Its prescribed roots, the reindexing of finite sums, cancellation of the first \(N\) groups, and the complete scaled finite identity. |
| [PadeCoefficients.lean](../broad/PadeCoefficients.lean) | An explicit integer recurrence for every coefficient numerator, its oddness, its binomial height bound, and its equality to the coefficient of \(R\). |
| [PadeIntegral.lean](../broad/PadeIntegral.lean) | One clearing denominator, every integer Taylor term, its exact equality to the rational expression, and bounds for both coefficients of the final linear form. |
| [PadeValuations.lean](../broad/PadeValuations.lean) | Exact valuations for the leading term and all weights; every physical tail is strictly higher; the resulting integer form is nonzero and divisible by the required power of two. |
| [PadeHeight.lean](../broad/PadeHeight.lean) | The ordinary size upper bound, the positive exponent margin, and cancellation of the common factor after raising to the seventeenth power. |
| [PadeNative.lean](PadeNative.lean) | Ordinary odd-run arithmetic, evenness at the event clocks, and exact finite telescoping on the original run. |
| [PadeObserved.lean](PadeObserved.lean) | Every tail premise supplied by those observed clocks, and the final source-height and bit-budget bounds. |
| [PadeWindow.lean](PadeWindow.lean) | Initial-run normalization and the physical bound on the whole long matching window. |

For clarity, the finite cancellation statement has the form
\[
 B_*y-A_*=
 D\,R(q^{-(N+1)})p_{N+M+1}
 +\sum_{k=0}^{N}B_k
       \left(y-\sum_{l<N+M+k+2}p_l\right).
\]
All objects here are defined explicitly. The statement holds for any nonzero rational \(q,z\), so its algebra can also be reused for decreasing clocks. It is an equality of finite rational expressions.

On the increasing clock, the actual source gives \(y=-(n+1)\), and native telescoping proves
\[
 y-\sum_{l<j}p_l
 =-\frac{2^{t_j}}{3^{t_j-j}}\bigl(T^{t_j}n+1\bigr).
\]
The terminal state is even. Its shifted value is therefore odd, giving exact valuation \(t_j\). The leading valuation of the cleared form is
\[
 W=(2N+M+1)(b+1)
          +h\left[N(N+M)+\operatorname{tri}(N+M+1)\right].
\]
Every remaining term has strictly larger valuation. This proves nonvanishing before using the integer size bound; cancellation is not ruled out by a numerical experiment.

At \(N=2s,M=s\), the height cost is bounded by
\[
 2^{7s}3^{3bs+h(\operatorname{tri}(s)+6s^2)}.
\]
Lean verifies \(3^{17}\le2^{27}\) and an integer exponent inequality retaining the margin \(3hs^2+4bs\). Combining both sides of the nonzero integer form and cancelling a positive power of two proves the boxed theorem.

## Decreasing clocks on the same actual map

The four `DecliningPade` modules in the broad directory prove the opposite-sign coefficient, integrality, exact valuation and height calculations. [DecliningPadeObserved.lean](DecliningPadeObserved.lean) supplies their remaining tails from the same native telescoping identity.

For \(h,s>0\) and \(b\ge200hs\), suppose the actual clocks satisfy
\[
 t_j(n)=j(b+1)-h\binom j2\qquad(0\le j\le5s+2).
\]
The subtraction is natural-number subtraction in `downSchedule`; the spacing assumption proves that it does not truncate on the required range. The theorem `actual_declining_height` gives
\[
                         \boxed{\quad2^{bs}\le(n+2)^8.\quad}
\]
Its bit-budget consequence is \(bs\le8B\) when \(n+2\le2^B\). These endpoints have also passed strict compilation. The proof uses only finitely many decreasing clocks, with an explicit common power of two removed from every integer coefficient. It makes no assertion that the formally continued infinite decreasing series converges at the binary place.

The complete \(20{,}000\log_2(n+1)\) physical cutoff, including all short and steep decreasing windows, is still the separate [written argument](../broad/FINITE_DECREASING_CLOCKS.md). The formal decreasing endpoint above has the explicit spacing hypothesis; it is not presented as the whole all-window theorem.

## Provenance and scope

The finite polynomial construction comes from [Zudilin's 2005 Tschakaloff argument](https://arxiv.org/abs/math/0506086). The p-adic irrationality background, Fourier Wren's growing-block adaptation and [Weaver's paper70](https://rstation.ai/problems/collatz/papers/70) are credited in the written manuscript. The present formal contribution is the explicit finite chain for the displayed ordinary clock, including the source-dependent remainder and integer margin. It does not assert priority for p-adic Padé approximation or its use in Collatz.

The [arbitrary-word staircase theorem](../broad/ARBITRARY_WORD_STAIRCASES.md) and the complete finite decreasing-window cutoff remain separately scoped written arguments unless their own formal endpoint is explicitly listed. An arbitrary Collatz orbit need not exhibit any long arithmetic staircase. No theorem here supplies the all-arity pin bound or proves universal convergence.
