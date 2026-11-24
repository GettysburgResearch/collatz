# Ordinary descent after an LPP history and at ternary heights above 1

Use the shortcut map T(x)=x/2 for even x and T(x)=(3x+1)/2 for odd x. An actual light block L has odd gaps (2,1), clock 3, and boundary equation 8q′=9q+7. A paid block P has gaps (1,4), clock 5, and 32q′=9q+5. All sources and shared endpoints below are on positive ordinary integer trajectories. A smaller source reaching the same endpoint excludes the prescribed floor as the globally least positive nonconverger.

## D1. An actual prior LPP covers two residual words at every light-run length

Let an ordinary LPP run from x to q₀. Suppose q₀ then has r initial L blocks and one of W=PLLPP or PLLPL. The same odd integer

$$m=(128q₀+349)/243=(3x+101)/64$$

lies strictly below q₀ and the integer floor of (3q₀+1)/4. It reaches the final boundary of W after 3r+28 clocks for PLLPP, or 3r+26 clocks for PLLPL. For r≥1 the second floor is the first light intermediate itself. This applies with arbitrary ordinary finite history before x. The six disjoint prefixes from PR192 cover thirteen other continuations when r≥3. Consequently fifteen of the sixteen five-letter words beginning with P are covered at an LPP boundary, with **PPLLL** the outstanding case for these certificates. Small r is handled by the paid boundary itself as described below. [SustainedResidual.lean](SustainedResidual.lean)

To see which ternary digits the past fixes, put ξ=(q₀+7)/2. On a light block the coordinate maps to 9ξ/8, and on a paid block it maps to (9ξ+83)/32. Each block adds two ternary digits independent of the earlier input. LPP forces ξ≡229 modulo 729, equivalently q₀=451+1458h. Hence m=239+768h. Composition gives 8192q₀=729x+2207. The eight comparison bits 11110111 yield

$$T^8m=9ξ-10,\qquad 256(9ξ-10)=2187m+2363.$$

The difference between the rational light floor and m is (217q₀−1153)/972, which exceeds one on the stated class. Given 8q′=9q+7 with q′ odd, any positive y with 2(y+10)=9(q+7) satisfies 2(T³y+10)=9(q′+7). Indeed y+10=8(q′+7)/2, and the signed magnitude 10 traverses 10,5,7,10 in three steps with two odd inputs under the reflected shortcut map. Induction carries the same m across all r initial lights. Writing q for the final light boundary and Y for the comparison at that point, one has 2(Y+10)=9(q+7). Composition of the five blocks and the last two rows of the next table give the identical ordinary final boundary w. All of these steps, including strict size and positivity, are in the Lean theorem.

| W | Source clocks A | Source carry C in 2ᴬw=59049q+C | Comparison anchor b | Comparison clocks B=A−1 | Carry K in 2ᴮw=6561Y+K | Y modulo 2ᴮ |
|---|---:|---:|---:|---:|---:|---:|
| PPLLL | 19 | 1704901 | 7 | 18 | 691706 | 28742 |
| PLLPP | 21 | 761093 | 10 | 20 | 239485 | 305059 |
| PLLPL | 19 | 892165 | 10 | 18 | 305021 | 239523 |

Each last-column representative has exactly eight odd inputs over B clocks and gives the indicated carry. The reflected induction for b=7 follows the same three-cycle. When r≥1 the intermediate f=(3ξ−10)/2 of this LPP class has exact v₃(f−1)=3 and (f−1)/27≡26 modulo 27. This differs from the D3 basic height-three progression.

## D2. Two entry conditions cover the third residual word as well

For an ordinary run LʳW starting at q₀ with any of the three table rows, each of the following conditions gives an odd source m below both prescribed floors. The row labeled 7 applies to PPLLL. Both other words use the row labeled 10. The source goes from m to 9ξ−b in the indicated initial clocks, then across 3r reflected-cycle clocks and the B literal target clocks. No incoming history hypothesis is needed. [ResidualDescent.lean](ResidualDescent.lean)

| Condition | b | m | Initial clocks |
|---|---:|---|---:|
| ξ=3¹¹h+3418 | 7 | 248832h+4799 | 10 |
| ξ=3¹¹h+3418 | 10 | 262144h+5055 | 18 |
| ξ=3¹³h+9148 | 7 | 2097152h+12031 | 21 |
| ξ=3¹³h+9148 | 10 | 1990656h+11419 | 13 |

The first condition admits no previous L or P, since ξ≡7 modulo 9 while a previous L or P produces 0 or 4. The second admits a prior LP, but no three consecutive prior L/P blocks. Enumerating the two affine maps modulo 729 gives eight possible last-three-letter residues, all different from 9148 modulo 729. Its P-compatible congruence q₀≡1 modulo 9 gives the positive paid predecessor (32q₀−5)/9. When r≥1 the first light intermediate has exact height 3 and (f−1)/27≡22 modulo 27. Both entry conditions have infinitely many positive inputs for every fixed r and W by the Chinese remainder theorem applied to the ternary coordinate condition and the finite dyadic parity word.

The earlier six prefix tests apply to PPP and PPLP with the fixed-half partner, and PLPP, PLPL, PLLL, PPLLP with ramp exponents 1,1,3,1. Their five-letter extensions have disjoint counts 4,2,2,2,2,1. For r=0 the first P drops below q₀>1. For r=1,2 its endpoint is respectively (81q₀+103)/256 and (729q₀+1391)/2048, below the initial light intermediate. Thus for either entry condition all 16 continuations have a descent or smaller merging source. Our Lean module formalizes the three new rows; the six earlier prefixes retain their original written/Lean/finite-table evidence split. [PR192 descent extension at d2081d1](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/DESCENT_EXTENSION.md)

## D3. A smaller predecessor on every ternary height above 1

Write n=1+3ᴴv with H≥1, v>0. Choose d≥1 such that 3ᵈ divides 2+4ᴴv and 2ᵈ4ᴴ≤3ᵈ3ᴴ. Then

$$m=2^d(2+4^Hv)/3^d-1,\qquad T^{d+2H}(m)=n,\qquad 0<m<n.$$

The first d comparison inputs are odd and finish at 1+4ᴴv. Repeating T²(1+4u)=1+3u gives the last 2H clocks. After multiplication by 3ᵈ the strict difference n−m equals 2(3ᵈ−2ᵈ)+v(3ᴴ⁺ᵈ−2ᵈ4ᴴ). The divisibility condition forces v≡1 modulo 3, so the original height is exact. This proof applies beyond the two-letter alphabet. [HeightPartner.lean](HeightPartner.lean)

Let a=log(4/3)/log(3/2), d_H=ceil(aH). At every H there is one class v≡−2·4⁻ᴴ modulo 3 to the power d_H. For H≥3 and v≡2 modulo 4, n belongs to the odd PR174 section n≡55 modulo 108. The class occupies one n residue modulo 4·3 to the power H+d_H. Different heights are disjoint. Their union has **relative ordinary natural density** Σ(H≥3) 27/3^(H+d_H)=0.050964047368156957… in that section. The remaining heights above K satisfy n≡1 modulo 3^(K+1), whose density tends to zero. The count includes overlaps with older descent theorems. At H=3 one gets v≡16 modulo 27 and n≡1891 modulo 2916. The base source 1891 has smaller predecessor 1327 in nine clocks.

At every H≥3 there are also genuine sources obeying this condition whose PR174 member arm reaches one. Let M=H+1+d_H. Two generates the ternary units modulo 3ᴹ: v₃(4^(3ʲ)−1)=j+1 follows by expanding a cube and induction. Choose arbitrarily large e solving 2ᵉ≡2−2·3^(H+1)·4⁻ᴴ modulo 3ᴹ. Then v=(2ᵉ−2)/3^(H+1) is positive, is 2 modulo 4 and has the required ternary class. Now n=(2ᵉ+1)/3 and 3n−1=2ᵉ. This family of witnessed examples supplies no positive-density assertion for the power-of-two members themselves. [PR174 at c92cd47](https://github.com/GettysburgResearch/collatz/tree/c92cd473de3b85ceb945702a726d2eb7350a6af8)

Allowing any number of inverse tours, then any number of inverse doublings and any number of consecutive odd predecessors improves coverage by at most a constant factor as H grows. The exponent and ordinary-density proof are in [the free-clock count](HEIGHT_CLOCKS.md).

At n=55 the member 3n−1=164 reaches one in 71 shortcut steps, and T⁵(55)=47. Every m from 1 through 54 avoids 55 through clock 72 and is then at 1 or 2. That two-cycle is closed. The kernel thus proves that no positive m<55 ever reaches 55 directly, even with arbitrary backward choices. A universal method must allow shared later endpoints or other descent mechanisms at some sources.

## D4. A shorter clock with overlapping coverage

For a legal LLLLPLP running from x to q, followed by the two-clock intermediate f=(3q+1)/4, the odd m=(3x−11)/32=(2²²f−5293177)/3¹⁴ reaches f in 22 clocks. It is below x, its first light intermediate, q and f. The literal comparison bits are 1111111101110101001000. For this same partial word, truncating PR192's PLPL ramp yields T²³((x−9)/16)=f. Its earlier partner is smaller by (x+7)/32. The 22-clock identity supplies a different preimage with the same coverage. [PastCylinder.lean](PastCylinder.lean)

An independent search found a different compulsory predecessor after the twelve-block past PLPPPLPPLPPP. Its construction, history comparison, and executable verification are documented separately in [the long-past supplement](LONG_PAST.md).

## Which forcing inference survives

The finite-parity correspondence of Bernstein and Lagarias applies to the same shortcut normalization. A finite binary word of length k specifies one residue modulo 2ᵏ. The converse used in our kernel proof takes an exact integer endpoint equation 2ᵏw=3ᵖx+C, with C computed from that word, and proves its first-bit parity and remaining endpoint recursively. This permits the ordinary integer synthesis at an exact endpoint and proves that every finite block history can be extended on its own positive source class. Conjugacy on the 2-adic integers does not supply one ordinary integer realizing every prefix of an infinite sequence. [Bernstein and Lagarias, The 3x+1 conjugacy map](https://doi.org/10.4153/CJM-1996-060-x)

There is a local forcing statement for the old six-prefix code. On an infinite L/P path that avoids the code at every P, a final tail of all L is impossible on positive integers since 8ᵏ divides q+7 for every k. On a tail with infinitely many P, consecutive PP would have to begin PPLLL, whose second P then begins the forbidden PLLL. Hence PP never occurs. The only remaining length-five possibility at any P is PLLPL, forcing a periodic (PLL) tail. Its complete transformation is q↦(729q+4213)/2048. Iteration converges in the real metric to the noninteger 4213/1319, impossible for a sequence of positive integers. Thus any actual infinite L/P trajectory has local code hits arbitrarily late. The missing inference is comparison below the fixed original floor: a partner smaller than the entry to a later code is insufficient if that entry has grown. PR192 already exhibited a long light run with a subsequent close pair remaining above its original intermediate. The seven-block and three-past conditions also cannot be forced merely by occurrence of letters. For instance the languages with separated P and long light runs avoid both LPP and LLLLPLP, and every finite prefix is ordinarily realizable. PR192 handles infinite six-separated paths through a different shadow. Our finite result leaves PPLLL on the sustained LPP cylinder, sources without those histories, and arbitrary odd-gap trajectories open. [PR192 separated-shadow theorem](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/DESCENT.md)

For r=3 on the LPP class, the PLLPP example q₀=37466289145 has m=19735329263 and endpoint 1502037883 at comparison clock 37. The PLLPL example q₀=184233374713 has m=97044740591 and endpoint 29543946239 at clock 35.

The file [controls.py](controls.py) reconstructs finite positive histories and the density independently of Lean reflection. The [execution record](../../../../reports/astra-global-closure-20261124/closing/descent/EXECUTION.md) distinguishes the kernel-checked declarations from written arguments and finite controls.
