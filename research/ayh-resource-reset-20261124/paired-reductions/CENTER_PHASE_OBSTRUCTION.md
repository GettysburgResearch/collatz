# A missing ordinary source for the rational center language

Use the rank-three family j=11+162m, 81z+271=2^(j+7). The ordinary shortcut map T takes z to M_j=2^j−1 after seven steps. The paired signed-reference construction in *MersenneTwoCenter.lean* aligns the lower cycles at −1 and the upper cycles at 0. A signed comparison has center b=−B/3^d in lowest terms, a positive ordinary output w≡17 modulo 48, and displacement w−b=λ(z−a), with a=−271/81. Both arms must have enough original binary precision to realize their specified signed words. A shrinking alignment has λ<1.

## All clocks and all denominators at m=0

For j=11 and z=3233, **no** positive w<3233 in the required residue visits any of the twelve values T^u(2047), 0≤u≤11, at any ordinary clock. There are 67 possible w. Their complete paths up to 1 take at most 99 clocks apiece and avoid every target. Their subsequent values are 1 and 2; the smallest target is 2047. The parent 3233 itself visits the twelve phases exactly at clocks 7+u, then reaches 1 at clock 107. The triple first reaches 1 at clock 18.

Consequently no rational center of any denominator can produce the specified strict lower-phase meeting at this source. On the source side z−a=2^18/81, so only the eleven lower −1 turns following the first seven steps are available: each shortcut consumes exactly one binary digit of displacement on a matched branch. This is a counterexample to total coverage of all ordinary m by those phase-aligned queries. The source itself converges. The example supplies no counterexample to convergence or to an assertion restricted to exceptional sources.

*CenterPhaseObstruction.lean* proves the whole 67-source obstruction, uniqueness of the parent clock, and the arithmetic contradiction used below. The kernel checks are finite only through each first visit to 1; the public conclusions quantify over all clocks. *check_center_phase.py* independently checks all ordinary traces and the terminal cycle.

## Denominator growth on actual positive indices

**Written theorem.** Let m>0 be divisible by 3^k. Suppose a shrinking center b as above produces a valid positive ordinary w≡17 modulo 48 at m. Write d for the reduced ternary denominator exponent. Count p odd and E even inputs in the signed lower word from b to −1. Then at least one inequality holds:

- d≥k+5.
- p−d≥12.

In particular, a finite bank restricted to p−d≤11 misses arbitrarily large ordinary m, even if its words may have arbitrarily many initial odd inputs. Every one of the thirteen displayed positive rows has p=d. An unbounded-depth choice and centers with more extra odd steps remain possible.

**Normalization.** A signed value above −1 stays above −1 under either branch. Thus b≤−1 and B≥3^d. On 3b the first arrival at zero uses exactly d−1 odd inputs: each odd step cancels exactly one denominator factor before integrality, and no nonzero signed integer can reach zero. On b the lower odd count p is at least d. On the source reference a the lower and upper entry records are respectively (4,7) at −1 and (3,9) at zero, written as (odd count, clock). Extra lower turns use one odd input and one clock, whereas extra upper turns add clocks only. Matching the ternary powers in both ratios forces exactly u=p−d extra turns on the lower source side. If redundant turns are present on both lower arms they can be removed together. Matching the powers of two then gives

$$
\lambda=3^{4-d}2^{d+E-7},\qquad
3^d w+B=2^{j+d+E},\qquad
h=d+E+u
$$

with h the lower comparison clock. Its intended source target is T^u(M_j)=2^(j−u)3^u−1. The written theorem applies if the lower word is realizable on the original source. The formulas do not require the two upper entry clocks to differ by two.

**Transfer to the small parent.** Suppose d≤k+4 and u≤11. Since 4=1+3, cubing four times shows v₃(2^162−1)=5. Successive cubing gives 3^(k+5) dividing 2^(162m)−1. The expression

$$
w_0=\frac{2^{11+d+E}-B}{3^d}
$$

is an integer congruent to w modulo 48, by subtracting its numerator from the ordinary m identity. Its signed difference from b has binary valuation 11+d+E≥h. The same h parities are therefore legal at w₀, even before its sign has been determined, and direct affine transport gives

$$
T^h(w_0)=-1+\frac{3^{d+u}}{2^{d+E+u}}
               \frac{2^{11+d+E}}{3^d}
         =2^{11-u}3^u-1>0.
$$

Here T is temporarily extended to the signed integers. Nonpositive integers stay nonpositive, so w₀ is positive. Also w₀=b+λ·2^18/81<−1+2^18/81<3236. Its mod-48 residue leaves two possibilities. If w₀<3233 the all-clock theorem gives a contradiction. If w₀=3233, the parent-phase uniqueness forces h=7+u and hence d+E=7. Strict λ<1 gives d≥5. Now 3^d·3233+B=2^18 is impossible, since already 3^5·3233>2^18. The final small-source arithmetic is the Lean theorem `limiting_query_impossible`.

This argument bounds the denominator or the extra lower odd count at a supplied ordinary m; it does not identify a specific successful center. In particular the determinant-one matching of abstract cycle vectors supplies neither the target residue nor the required positive smaller output.

**Pinned dependencies.** PR197 at 156652e03fe7a78f9cd4442039779cc622fdf3de, research/ayh-resource-reset-20261124/closing-proposal/MersenneBarrier.lean, claims mersenne_family and three_odd_upper. The current two-center construction supplies the signed entry records, with ordinary rows in *MersenneTwoCenter.lean* and their scope in *SIGNED_ROUTES.md*.
