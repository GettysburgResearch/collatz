# Positive smaller partners at arbitrary ternary height

**PROPOSED. Collatz remains OPEN.** Use the shortcut T(x)=x/2 on even integers, T(x)=(3x+1)/2 on odd integers. A smaller partner of n is an ordinary positive m<n with T^b(m)=T^a(n) for finite clocks. Its convergence implies that of n.

The open target is the complete-merging obligation in `research/integrated/rank-merging/README.md`. PR 182, head `cbec52dde5bed390a693310dd04e911033ba0cc9`, `research/phase-packing-round12-20261124/README.md`, studies phase-conditioned expansion. PR 191, head `37b3916633cd32a0c173b20bb18ec3a7ec290a63`, `research/two-sided-cycle-packing-20261124/README.md`, gives a two-return guarded shadow. Neither result is assumed here. Our competitor words are unrestricted and the comparison rank is ordinary size.

## S1. A changing-length physical partner at every ternary height

Write n=3^h u where u>0 is odd and coprime to 3. Put d=h+4. If 3^d divides 1+2·4^h u, set z=(1+2·4^h u)/3^d and m=2^(d+1)z−1. Then

**0<m<n and T^(3h+7)(m)=T(n).**

The first d letters on m are odd, reaching 2·3^d z−1=1+4^(h+1)u. Each physical pair odd, even sends 1+4q to 1+3q. Applying h+1 pairs gives 1+3^(h+1)u=3n+1. One even step finishes the meeting. The affine formula for m has coefficient (64/81)(8/9)^h on n and constant 2^(d+1)/3^d−1<0. Its coefficient is below one and z is a positive integer. More generally the same word works at every d passing the divisibility and size tests.

The guard selects one unit class modulo 3^(h+4). At each h the Chinese remainder theorem independently permits 3^h u ≡ −1 modulo 2^A for any requested initial odd-run length A. Hence infinitely many ordinary sources of every such type receive a smaller partner, including sources arbitrarily far inside the obstruction below. Example: h=0,u=121 gives m=95 and the seven-step path ends at 182.

## S2. An obstruction for every competitor word

Suppose 2^a divides n+1, h=v₃(n), and m<n meets T^a(n) at clock b. Let k count the odd letters from m. Then **b>a and k>a+h**. In particular no fixed finite list of words, including asynchronous pairs, gives a smaller partner for all sources. For a cap H>0, choose n≡−1 modulo 2^H and n≡0 modulo 3^H. Every pair of clocks ≤H fails. A positive representative n<6^H exists.

For any prescribed word F, compose its affine rational maps without requiring parity. F has nonnegative intercept. From a nonnegative input the all-odd word gives the unique maximum at fixed length, since at each stage the odd letter gives a strictly larger next value than the even letter, and both are strictly increasing. From any negative input every word gives strictly less than the maximum from zero by comparing the same word from the two inputs. In particular b≤a cannot reach T^a(n) from a smaller positive source.

Put t=b−a, L=2^t·3^(a−k) and v=m−Ln. For the competitor word F, subtracting the slope contribution gives F(v)=(3/2)^a−1. Also v=L(1−(2/3)^a)−(2^b/3^k)F(0)<L. If k≤a+h then m−v is an integer multiple of 2^t. The first t letters on v are therefore ordinary by parity induction. A negative integer stays strictly negative through that prefix, making the remaining a-letter maximum from zero unattainable. Thus v≥0. If v≥1 then L>v≥1 contradicts m<n. If v=0, the t prefix letters are even and the a suffix letters all odd by uniqueness of the maximum. Thus k=a and L=2^t, again impossible.

## S3. Exact first eligible tier

For n>1, if k=a+h+1 in S2, then h=0, b=a+1, and m=(2n−1)/3. This is possible precisely when n≡2 modulo 3; the witness steps directly to n.

Here v is a noninteger third. The first t prescribed steps are physical on rationals with odd denominator: their parity is the residue modulo 2, and m−v belongs to 2^t times the rationals with odd denominator. Each letter preserves the prescribed parity agreement for the remaining clocks. At least one of the t prefix letters is odd since k>a. Its first odd step makes the comparison state integral, and the state after t must be nonnegative by the suffix maximum. A negative v can reach nonnegativity only from −1/3 to zero on its first odd step. All later prefix letters are even and all suffix letters odd. Hence h=0, v=−2^j/3 with 0≤j<t, and 3m=2^t n−2^j. If t≥2, n≥2 implies this is at least 2^t(n−1/2)≥3n. Thus t=1 as claimed.

For positive v, descent forces 0<v<L<1. The two possibilities are 1/3 and 2/3, each landing in the cycle 1,2 on its first odd step. The first t letters contain at most 1+floor(t/2) odds. The state then is positive and cannot attain the required maximum from zero with an all-odd suffix. Thus at least h+2 odds occur in the prefix, requiring t≥2(h+1), so L=2^t/3^(h+1)>1. When a=0 a positive comparison state already contradicts the empty suffix endpoint zero.

## S4. A finite ordinary-orbit test for higher excess

Let k=a+h+d, d≥1, h≥1. Then v=m−2^t u/3^d has exact denominator 3^d and v<1 (if positive, use m<n and v<L). Each odd letter in the physical prefix cancels exactly one 3 from the denominator while it exceeds one. Let s be the clock at the d-th odd letter and r the resulting ordinary integer. This occurs within t since the prefix has at least h+d odds. If r<0 the negative integer stays negative and the suffix maximum is unattainable. If r=0, total odd count is exactly d+a, contradicting h≥1. Thus **1≤r<2(3/2)^d**: the affine prefix sends v<1 below its value from 1. Applied from 1, deleting the even letters can only increase the endpoint, yielding the bound. A negative v can turn positive before clearing its denominator. In the ordinary diagram n=81,m=27,a=1,b=55, one has d=31 and v<0.

Let B_d bound 2K−ℓ for every ordinary ℓ-step prefix with K odd letters from those r. If the finitely many seeds converge, such a B_d follows by tracing to 1 and accounting for its cycle. Put p=t−s. Since the state after t is positive, the suffix cannot consist entirely of odds. Thus p≥h+1. The first t letters contain at least h+d+1 odds, and their balance is at most d+B_d. Hence t≥2h+d+2−B_d. The affine s-letter prefix from zero reaches at most (3/2)^d−1, so v≥−(2^s/3^d)((3/2)^d−1). Therefore

    m/n ≥ L (1 − ((3/2)^d−1)/(2^p u)).

When 2^(h+1)≥2((3/2)^d−1), a smaller partner requires L<2, or 2^t<2·3^(h+d). This conflicts with the lower bound for all sufficiently large h at fixed d,B_d. Once the two powers conflict the ratio increases by 4/3 per increment of h. The finite controls use the stronger first test 2^(h+1)≥4(3/2)^d.

| d | largest ordinary r tested | B_d | every h at least this is excluded |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 2 |
| 2 | 4 | 2 | 6 |
| 4 | 10 | 3 | 11 |
| 8 | 51 | 21 | 60 |
| 12 | 259 | 21 | 66 |
| 16 | 1313 | 26 | 83 |

## S5. Exact smaller-partner search at the first odd endpoint

Fix odd n=3^h u with h≥1. Every smaller partner at T(n) can be constructed as follows.

1. Choose d≥1 and a prefix word α of length s ending at its d-th odd letter. Write its affine map as (3^d x+C)/2^s.
2. Choose a positive ordinary r<2(3/2)^d and a physical length-p path from r to 1 with exactly h+1 odd letters. The path may revisit 1.
3. Form m=(2^s(r+2^p u)−C)/3^d. Accept if it is a positive integer less than n.

Every acceptance gives T^(s+p+1)(m)=T(n); every smaller partner and clock at this endpoint has such a description. For necessity apply S4 at a=1. The positive integer at the end of the t=b−1 comparison prefix must reach 1/2 by its single formal suffix letter. Thus it is 1 and the letter is even. The comparison state r after the d-th odd then reaches 1 with exactly k−d=h+1 odds. Undoing the affine prefix gives the displayed m.

Conversely the prefix formula ends at the integer r+2^p u. Starting at integer m and ending at an integer makes every formal prefix letter physical: after a wrong parity letter the reduced denominator is 2, and every subsequent letter doubles that denominator. The ordinary p-step tail of r lifts to the same word from r+2^p u, ending at 1+3^(h+1)u=3n+1. An even step meets T(n). This shows sufficiency directly. S1 chooses r=1, p=2(h+1) and α consisting solely of odd letters. A general r and varying α give other candidate residues, with their actual length costs retained.

This characterization only handles the endpoint T(n); even an unlimited search here may fail. For n=3 the only smaller positive integers are 1 and 2, and neither ever reaches T(3)=5.

## S6. Unbounded excess even at fixed dyadic and ternary heights

Let n>3, n≡3 modulo 8, H=v₃(n−3). For each a=0,1,2, every smaller partner at T^a(n) requires k>a+H. Indeed if k≤a+H then m₀=m−L(n−3) is an integer since b>a. By the same affine identity its prescribed word ends at T^a(3), one of 3,5,8. Since both endpoints are integral, the word is physical as in S5. No integer m₀≤3 reaches that endpoint at clock b>a: nonpositive integers stay nonpositive, 1 and 2 cycle, and the orbit from 3 is 3,5,8,4,2,1,2,…, visiting each indicated endpoint only once. Hence m₀≥4. But v=m₀−3L<L implies 4≤m₀<4L, so L>1. This makes m=m₀+L(n−3)>n, the required contradiction.

There are such n with arbitrarily large H. For H≥2 they have exactly v₃(n)=1 and v₂(n+1)=2. Thus even those two heights together do not bound the odd-count excess needed across all endpoints of the initial odd run. This argument neither precludes arbitrarily long successful words nor controls later endpoints. For instance n≡3 modulo 16 has T⁴(n)=(9n+5)/16<n for n>1.

## Limits and controls

S1 proves a sufficient physical certificate on one unit class per height. S2–S4 and S6 restrict all competitors meeting within the specified initial odd run, and S5 describes the one-step endpoint exactly. Later forward endpoints remain available. The first unsupported global step is showing that every remaining fixed ordinary source receives a smaller partner or converges by another argument. Varying the source to satisfy an S1 guard cannot establish this.

`shadow_check.py` replayed S1 at 63 points, checked 2,188 smaller diagrams (329 first-tier) for n≤500 and clocks≤16, reconstructed all 38 S5 diagrams for odd multiples of 3 below 350 and clocks at most 90, and computed the displayed B_d. Those counts include diagrams with different clocks for the same pair. They certify no universal coverage.

Lean 4.34.1 accepted all ten public theorems in `ShadowCore.lean` with `import Std`. The aggregate S1 theorem `ShadowCore.guarded_certificate` assumes a positive u, odd n=3^h u and the divisibility guard, and concludes existence of an ordinary positive smaller m with the exact clock 3h+7. Its printed axioms are propext, Classical.choice, and Quot.sound. No public declaration printed sorryAx. S2–S6 are written arguments outside this Lean scope.
