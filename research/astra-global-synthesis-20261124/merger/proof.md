# An ordinary comparison for paired paid blocks

**Status.** The paired-language descent below is a Lean-checked conditional theorem about every fixed positive ordinary source following that language forever. There is also an asynchronous finite reset on an arbitrary continuation, and a written obstruction to one proposed mixed-cluster controller. None establishes universal Collatz descent.

Use the shortcut map T, even x to x/2 and odd x to (3x+1)/2. At an odd block boundary q, light L means the exact successive odd gaps (2,1), giving 8q'=9q+7. Paid P means (1,4), giving 32q'=9q+5. An intermediate is the odd state after the first gap, (3q+1)/4 on L and (3q+1)/2 on P.

## 1. A whole class outside six-separated descent

**PP1.** Suppose the paid blocks on an infinite ordinary L/P path come in adjacent pairs, separated from the next pair by at least four light blocks. The initial segment may start anywhere in a pair or in a light run. At every block there is a single positive odd integer below both its boundary and its intermediate whose ordinary T-orbit never hits 1. Thus the global least positive nonconverger cannot lie at either position of such a tail.

The quantifier permits arbitrary variation in the light gaps, including consecutive contracting and expanding returns. A pair with four intervening L blocks has multiplier (9/32)^2(9/8)^4<1; a pair with twenty-four L blocks has multiplier >1. This also includes the residual prefix PPLLL with arbitrarily long succeeding light runs. A convergent source cannot have an infinite sequence of such blocks. The smaller partner is an ordinary nonconverger; a shared endpoint with the original source is not required for PP1.

Number the seven phases as free L, four L's remaining, three, two, one, first P, second P. A free L can lead to another free L or to four. Four through second P follow in order, and second P leads to free or four. Reading the next four labels determines an L phase. An initial P is first or second according to whether the next label is P.

Let D=4096, M=3123 and y=(Mq+K)/D at the current phase. Here N is the input block divisor, c its input carry, and c' its target carry.

| Phase | N | c | K | c' | Target gap pair |
|---|---:|---:|---:|---:|---|
| free | 8 | 7 | 1381 | 5 | (1,2) |
| four | 8 | 7 | 1381 | 7 | (2,1) |
| three | 8 | 7 | 2405 | 7 | (2,1) |
| two | 8 | 7 | 3557 | 7 | (2,1) |
| one | 8 | 7 | 4853 | 5 | (1,2) |
| first P | 32 | 5 | 5287 | 5 | (1,4) |
| second P | 32 | 5 | 1639 | 11 | (3,2) |

For every allowed successor K' the identity is NK'=9K+Dc'−Mc. Thus Ny'=9y+c' over the rationals. Since four actual edges have total binary length at least twelve and 9 is odd, iterating the numerator identity along these four edges gives D|(Mq+K). This applies at every position of the **same** input. Reducing the equations modulo 2 now proves every y is odd. If c'=3+2^a and N=2^(a+b), then 3(3y+1)=2^a(2^b y'−1). The factor in parentheses is odd. Dividing verifies both exact accelerator gaps, including the (3,2) split. Two successive input equations and oddness at the second endpoint imply q≥17 by checking the four possible pairs of letters; hence 2<y<q in every phase. The unbounded sequence of literal target clocks stays above 2 at its boundaries, so it cannot enter the T-cycle 1,2.

The intermediate floor needs additional work, since M/D exceeds 3/4. At a free or four L, y≡4 mod 9 because 3123≡0, 4096≡1 and 1381≡4 mod 9. The positive odd m=(8y−5)/9 has the three ordinary iterates (4y−1)/3, 2y, y. At any of the other three L phases, y≡2 mod 3 and m=(2y−1)/3 reaches y in one clock. Each m is below (3q+1)/4 by substitution of the corresponding row, using q≥17. For example in the free and four phases the real-valued comparison simplifies to 32(3123q+1381)−20D<9D(3q+1). In the other L phases it suffices that 8(3123q+4853)−4D<3D(3q+1). Both hold for q≥17. On a P take y itself as the smaller source. These comparisons also put m below q. This proves PP1. The second P uses a target gap of 3, so PP1 does not supply the same paired P/L script on its output.

The public Lean theorem `Collatz.PaidPairs.paired_descent` starts with raw Boolean input labels, their local pairing and spacing rule, exact input equations, and oddness; it constructs the phase marking internally. `smaller_both` is the phase-track version. Both conclude with the literal non-hit predicate for the new ordinary integer.

## 2. A finite asynchronous reset returning to the original floor

**PP2.** Let an actual finite prefix be L^r PP L^s with r,s≥2. Write q0 for its first boundary and z for the last. A fixed partner

    m = (q0+7)/16 − 7

is positive, odd, below q0 and below its first odd intermediate. It reaches (z−7)/2 after 3r+3s+7 shortcut clocks. The original uses 3r+3s+10 clocks to reach z. The suffix after z is unrestricted. Any ordinary merger between z and its fixed half (z−7)/2 now gives a merger back to the smaller source m at the original floor.

Write q0+7=2·8^r v and q+7=2·9^r v at the first P. The centered L equation and the final odd boundary give these with integer v≥1. The P congruence implies v odd. Through the first 3(r−1) clocks the partner follows the signed three-cycle starting at −7, reaching y=9^(r−1)v−7=(q+7)/18−7. This uses the ordinary parity lifting identity: varying a signed seed by 2^h t changes its h-clock image by 3^u t with u odd visits. Here m=8^(r−1)v−7 is positive, odd and below both floors since r≥2.

After the two P's, call the source boundary u, so 1024u=81q+205. Substitution gives 512(u−6)=729y+1850, hence y≡310 mod512. The nine literal clocks from 310 have six odd inputs and carry 1850. Thus the partner reaches u−6. The two next L's end at v2 with 64(v2+7)=81(u+7). Write u+7=64t, so u−6=64t−13. The signed seed −13 follows six clocks to −5 with three odd inputs. Consequently the partner has reached 27t−5=(v2+7)/3−5. As v2+7 is even, t is even, and one ordinary odd step takes this value to (v2−7)/2. On each remaining L, the half partner transfers to the next half in three clocks (start q=16k+9, half=8k+1, yielding 9k+2). This proves the stated clock and floor.

In particular every L^r PP L^s P(LPL)^j P(P or LP), r,s≥2, j≥0, has an exact smaller ordinary merger, with no condition on the remainder of the orbit. This follows by applying the fixed-half return table of PR192 at z. The PP2 packet itself reaches the half, not z. In combination with its known PPP suffix this covers *all* second light-run lengths s≥2, including s arbitrarily larger or smaller than r.

## 3. Why the natural singleton/pair switch fails

**PP3 (restricted no-glue theorem).** Start on an arbitrarily long free L stretch with a common dyadic slope 0<λ<1. The free boundary chart is y=λ(q+7)−a with a either 5 or 7. To prepare a paid cluster of size k=1 or 2, allow arbitrary finitely many target L carry switches (between 5 and 7) with the same light clock and two odd visits per L. The choices, the number of preparing L's, and even a may depend on k. On the paid cluster allow an *arbitrary finite* ordinary target parity word of any clock and odd count, fixed for that package. Demand a coefficient identity returning at the other end of the cluster to some free chart λ'(q'+7)−b, where b=5 or 7 and the outgoing slope may depend on k. Require literal legality on arbitrarily long positive finite input lifts with arbitrarily long following L's. No common incoming λ serves both packages.

After the last preparing L the correction to the starting chart is

    E = σ/4 Σ ε_j (9/8)^j,   ε_j∈{0,1},   σ=+1 if a=5 and −1 if a=7.

Let H_1=1,H_2=41. Composing the centered paid map gives 32^k(q'+7)=9^k(q+7)+166H_k. At the signed free output q'=−7, the target's signed input at the start of the cluster is therefore

    z_k = −a_k + E_k − 166 H_k λ / 9^k.

It must be 2-adically odd and its ordinary rational shortcut orbit must reach −b. To justify this signed comparison, positive input lifts exist for each finite prescribed exact gap word. In the limit of arbitrarily many following L's, q' tends 2-adically to −7. The anchored q and target entry tend to the values above. Every fixed finite target parity is determined by a finite binary residue, including the parity and integrality of its initial point. The endpoint identity gives −b at the signed limit. This is a necessary condition on a uniform package, with no claim of an ordinary source realizing the infinite limiting word.

If λ has reduced denominator 2^d, d≥2, then the two E_k have the exact same denominator 2^(d−1), since the remaining odd-denominator terms cannot cancel negative binary valuation in z_k. For a nonempty switch set with largest lag h−1, its denominator is exactly 2^(3h−1); the numerator's leading summand 9^(h−1) is odd and every other summand is divisible by 8. Hence d=3h for both packages. Write E_k=σ_k S_k/2^(3h−1), S_k=Σ ε_j9^j 8^(h−1−j) and ε_(h−1)=1. Odd-denominator integrality of z_1,z_2 implies

    41 σ_1 S_1 − 9 σ_2 S_2 ≡ 0 mod 2^(3h−1).

For h≥3, reduction mod 8 forces equal signs. Mod 64 the leading-digit contribution is 32·9^(h−1)≡32. The next digit contributes 8·9^(h−2)(41ε−9η), which modulo 64 is 0 or ±8. All remaining contributions vanish. This contradicts the displayed congruence.

The remaining d are 1, 3 and 6. At d=1, integrality requires E=0; at d=3,6 only the first one or two switch positions can enter. Testing odd numerators between zero and 2^d, both centers and these at most four masks leaves only the following possibilities for the two seeds to be 2-adically odd.

| λ | z_1 | z_2 |
|---:|---:|---:|
| 3/8 | −35/3 | −979/27 |
| 5/8 | −169/9 | −4841/81 |

For λ=3/8 the singleton seed goes in one odd step to −17. For λ=5/8 it goes to −83/3, then −41. Both are on the negative cycle of magnitudes 17,25,37,55,82,41,61,91,136,68,34, so neither reaches −5 or −7. This proves PP3 even though the target word within each paid packet could change its clock, odd count and outgoing slope.

The first unproved switch is a rule with different incoming slopes determined by future cluster types, or asynchronous preparation already on the leading light segment. A general finite ordinary affine transition between positive slopes can change their ratio only by powers of two and three (compare coefficients); this alone supplies no working controller. Other gap pairs and ordinary orbits with no forced prefix remain outside all three results.

## Dependencies and replay

The map and exact L/P normalization agree with PR191 TCP-5 at `37b3916633cd32a0c173b20bb18ec3a7ec290a63`, `research/two-sided-cycle-packing-20261124/README.md`. The earlier single-P separation result and fixed-half return table are PR192 at `d2081d1cd2410e6004eaee9f9b13c5553afaf3f4`, `research/astra-closure-attack-20261124/DESCENT.md` and `DESCENT_EXTENSION.md`. The generic literal clock, parity, and cofinal boundary traversal lemmas in PaidPairs.lean adapt the Std-only code at that pin, `descent_Separated.lean`. PP1 has a different frame, target gap table and smaller intermediate source. PP2 and PP3 are written proofs, with controls in check.py. The lookahead obstruction in PR195 at `a24ef018147a1e16bf314d14085e2d0d6c620d32`, `research/astra-global-closure-20261124/audit/SHADOW_RIGIDITY.md`, concerns uniform full-language rules; PP3 uses only the two isolated cluster types.

Run Lean 4.34.1 with `lean -j1 -DwarningAsError=true PaidPairs.lean`. The independent runs `python -B check.py` and `python -O -B check.py` each exercised 92 marked phase paths, 1,840 ordinary shadow edges, 72 asynchronous resets and the two small common odd rational seeds. Finite examples supplement the fixed-input arguments.
