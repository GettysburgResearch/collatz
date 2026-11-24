# A simultaneous linear-clock obstruction on residual marked ordinary sources

For each T≥6 there is an explicitly computable marked source of binary octave d=4T on which (i) the canonical half-partner grammar rejects immediately, (ii) strict forward descent fails throughout the first 3T+1 shortcut clocks, and (iii) the two finite orbit sets of the source and its half partner through 3T+1 and 3T clocks, respectively, are disjoint. Clocks in (iii) may be chosen independently. This also obstructs tests on the post-rise arm pair through T clocks per arm.

Set k=2T, choose 1≤r<2^T representing the inverse of 3^k modulo 2^T, and put
    u=2^(2T−1)+r, n=2^(k+1)u−1, x=2^k u−1, b=3^k u−1.
The source lies in octave 4T, with offset between 0 and 2^(3T+1). The marked condition follows from 2(4T+1)≤70·2^T. The cofactor u is odd, so k is canonical. Since 64 divides b, no initial grammar rule applies.

Use the shortcut map F. Through j=k clocks on x the affine expressions are 2^(k−j)3^j u−1; through i=k+1 on n they are 2^(k+1−i)3^i u−1. The two final values are b and 3b+2 respectively. Every positive rising clock increases n strictly. The ratio of its final rising value to n exceeds (3/2)^(k+1), since the exact final value is (3/2)^(k+1)(n+1)−1. Each subsequent clock loses a factor of at most two. Thus through T further clocks n stays strictly above its start because (3/2)^(2T+1)>2^T.

For 0≤h≤T, the two post-rise affine expressions are
    b/2^h,   c_h + (3b)3^floor(h/2)/2^h,
where c_h=2 for even h and 1 for odd h. Indeed the first path follows 0's parity prefix and the second follows 2,1,2,1,… through T clocks, by divisibility of b. Regard all displayed pre- and post-rise expressions as affine functions of u. Every slope belongs to 2^(−T) Z. Every intercept is between −2 and 2: pre-rise intercepts are −1, the x post-rise intercept is −1/2^h, and the n post-rise intercept is c_h−3(3/4)^floor(h/2)/2^(h mod 2), which is at least −1.

No affine function on one list is identical to a function on the other. Evaluate the formulas algebraically at u*=3^(−k). All x values are nonpositive: its pre-rise values are (2/3)^(k−j)−1, and its post-rise values are zero. Every n post-rise value is 1 or 2. For an n pre-rise value to equal any x value, it would have to satisfy
    2 (2/3)^(k−i)=(2/3)^(k−j)
for some 0≤j≤k (including j=k for zero). Its 3-adic valuation forces i=j and hence 2=1. Evaluation here compares affine expressions only and does not require u* to be an ordinary positive input.

Finally, any two different slopes differ by at least 2^(−T). Thus at the actual u>4·2^T their slope contribution exceeds the maximum intercept difference. Equal slopes with distinct intercepts never coincide. This proves disjointness for all cross-clock pairs simultaneously.

This excludes any universal residual rule requiring descent within the displayed horizon or requiring a merger with the canonical half partner within it. Other partners, longer paths, and convergence itself remain open.
