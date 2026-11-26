# Which of the 32 earlier Mersenne inputs can meet a normalized checkpoint?

**Unconditional written theorem for every supplied odd cofactor.** The 32 odd factors in the last section of the companion checkpoint note give actual earlier Mersenne trajectories at this same positive source. For the clock ranges below, all of those trajectories except the one of the same polynomial degree are rigorously excluded. A meeting with the same-degree trajectory remains a legitimate positive certificate and is still open for a prescribed exceptional cofactor.

Retain v≥128, v≡4 mod 27, d=v₂(v)≥1, j=66v−5 and W=3^(2v). Write d=3k+r with 0≤r≤2, and put

$$Z_i=(W^i-1)/2^{d+3+v_2(i)},\qquad 1\le i\le32.$$

The valuations follow by factoring 3^(2vi)−1. The trajectory of M_(2vi)=2^(2vi)−1 reaches W^i−1 and then Z_i. All 32 exponents are strictly below j. In the notation of the preceding note, U=Z_22 and V=Z_21. The two post-ascent candidate inputs can be written

$$B_e=3^b(W^e-1)/2^\beta-a,$$

where (e,b,β,a) is either (22,d,d+4,1) or (21,2k,3k+3,5). In particular B_22=3^d U−1 and B_21=2^r3^(2k)V−5.

**Theorem.** Fix either e. For every source clock 0≤h≤v and every 1≤i≤32:

1. No T^h B_e equals any of the values on the entire initial ascent of M_(2vi), including its peak W^i−1.
2. Suppose T^h B_e equals the value obtained t≤v clocks after this Mersenne peak. Then necessarily i=e, t=h+β, and the odd counts p and p' on the h and t postulated words satisfy p'=b+p. These restrictions apply to the actual positive values. In particular they also allow unequal input clocks.
3. For every arbitrary earlier exponent 1≤n<j, no initial ascending phase of M_n can give a meeting while h≤floor(v/8).
4. For the original parent z=(32·2^(66v)−527)/81, each B_e lies above 2^(floor(v/2)−5)·z. A path of fewer than floor(v/2)−5 ordinary shortcut or inverse edges issued at either B_e cannot reach a below-parent tripling query. All 20 values Z_i for i≤20 already lie below the stronger z/2^40 floor, independently of earlier Mersenne information.

These assertions refer to the actual arrow relation of Collatz. A cyclotomic identity equating products of good integers gives no new arrow or basin implication.

## The odd remainder at every source clock

A physical h-word with p odd steps has the form (3^p x+D)/2^h, with integer 0≤D≤3^h−2^h. Substituting B_e gives

$$2^{h+\beta}(T^hB_e+1)=3^{2ve+b+p}+C,\qquad
C=2^\beta(2^h+D-a3^p)-3^{b+p}.$$

Here C is odd, for *every* word, since β≥3. In particular C cannot vanish even if the original signed reference has ceased to predict the parities. One has |C|<3^(h+d+5), since a≤5, β≤d+4, b≤d, and 2^h+D≤3^h. Further d≤v/8, using 2^d≥8d for d≥6 and v≥128 otherwise.

The two positive inputs have the useful exact sizes

$$B_{22}+1=(3/2)^d(W^{22}-1)/16,\qquad
B_{21}+5=(9/8)^k(W^{21}-1)/8.$$

In both cases B_e>W^21/32 for v≥128. Since (2187/2048)^12>2 (use (17/16)^12>2), it follows that W^21=3^(42v)>2^(66v+floor(v/2)); strictness holds also when v is odd. In particular

$$T^h B_e > 2^{66v+\lfloor v/2\rfloor-5-h}.$$

Each positive ordinary edge in either direction changes height by at most a factor two. The displayed bound at h=0 and z<2^(66v) proves the guarded-query statement. For the low comparison indices use 3^5=243<256, so W^20=3^(40v)<2^(64v). Since z>2^(66v−2) for v≥128, every i≤20 gives 2^40 Z_i<z.

## Full Mersenne ascents

At clock l≤n, the ascending phase of M_n is 2^(n−l)3^l−1. If this equals T^hB_e, the nonzero C is divisible by 3^min(l,2ve+b+p). For h≤v, the latter exponent 2ve+b+p is greater than h+d+5. Thus l<h+d+5. The ascending value plus one is 2^n(3/2)^l≤2^(n+l).

For n=2vi≤64v and h≤v the ascending exponent bound is n+l<65v+d+5. The source has height above 2^(65v+floor(v/2)−5), which is larger since d≤v/8 and v≥128. For n<j<66v and h≤floor(v/8), the same inequality follows from 2h+d+10≤3v/8+10≤floor(v/2). This proves both initial-ascent exclusions.

## After each peak

Let the t-word from W^i−1 have p' odd steps and offset D'. Put E=D'−3^p' and C₀=2^β(D−a3^p)−3^(b+p). Then |E|≤3^t and |C₀|≤81·3^(h+d). An actual meeting after the peak forces

$$2^t3^{2ve+b+p}-2^{h+\beta}3^{2vi+p'}=2^{h+\beta}E-2^t C_0.$$

For h,t≤v the right side is at most 97·3^d·6^v in absolute value, whereas the left side is divisible by 3^(2v). To see the strict separation, 3^d≤2^(v/4) and (3/2)^4>4, so (3/2)^v/2^(v/4)>2^(v/4)≥2^32>97. Both sides must therefore vanish. Unique factorization gives t=h+β and 2vi=2ve+b+p−p'. Since 0≤b≤d and 0≤p,p'≤v, the right offset has absolute value at most d+v<2v. This forces i=e and p'=b+p as claimed.

For e=22, the forced t=h+β is exactly the known d+4 halvings of the peak followed by h clocks on U. For e=21, the peak halves d+3 times to V. When h≥r the forced comparison is B_21 at h against V at h−r. After r initial forced steps B_21 is 3^(2k+r)V−b_r with b_0=5, b_1=7, b_2=10. Thus the original 32-way post-peak comparison, on this entire scale, reduces to the two matched-degree ordinary pairs. If h<r, direct substitution of the first zero or one forced steps still before those r steps shows a nonzero additive difference from the required multiple 2^(r−h)V, or a larger nonzero slope times V which cannot cancel an offset at most 7. The possible cases are r=1,h=0; r=2,h=0; r=2,h=1. For k=0 the difference in the first two is −5, while the last difference has odd fixed offset −7 and an even multiple of V.

## Open point

The physical clock bound v is exponentially larger than the logarithmic delay on v=4·2^(18t). The two surviving equal-degree pairs can actually merge within this window, as shown by the companion note's preassigned examples. The comparison with the other 30 factors cannot supply a short physical merger if these two fail. Longer paths, new good points from different constructions or later below-parent queries remain possible. No termination statement for every fixed cofactor follows.
