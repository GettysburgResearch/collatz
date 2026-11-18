# Direction-sensitive two-power coverage

**PROPOSED, with the same source-qualified length and height inputs
as the [coverage proof](TWO_POWER_COVERAGE.md).** Any two disjoint
cyclic factors U^a,V^b, a,b>=2, in a primitive nontrivial ordinary
positive shortcut cycle leave at least L/55 positions uncovered.

Keep the orientation, symbols and local estimates of the coverage
proof. Let P=au and R=bv for the full lengths, and let d=L-P-R.
In the opposite-direction case the global correction gives the sharper

    R <= gamma P + b c p + gamma d + s,                        (1)

since the gaps contain at most d odd steps. Here c=log_2 3, gamma=c-1,
Z=log_2(2m+2), and s=log_2(L+1).

If the minimum lies in a gap, both lower boundaries x and w have
logarithm at most log_2 m+d. If it lies in the first U copy,
log_2 x<=u-q+log_2 m and log_2 w<=u-q+log_2 m+d. In either case
the starting 2-divisibility gives P<=c u+Z+d. This follows from
P<=c q+log_2(x+2^(u-q)). Thus P<=5(Z+d), using c<8/5.
The ending 3-divisibility gives b c p<=v+u+Z+d. With (1) and b>=2,

    L <= 2c P + 2Z + (2c+1)d + 2s.

If the minimum lies in the last V copy, then
log_2(w+1)<=gamma p+log_2(m+1). Along the lower gap J each odd
step multiplies the state plus one by at most 3/2, and every even
step is nonincreasing. Consequently
log_2(x+1)<=gamma(p+d)+log_2(m+1). In this case the two local
divisibilities give

    P <= c q + max(u-q,gamma(p+d)) + Z,
    b c p <= R/b + gamma p + Z.                                (2)

Insert (1) in the second inequality. Since (b-1)c-gamma=(b-2)c+1
is both at least one and at least b/2, this gives

    p <= gamma(P+d)/2 + Z + s/2,
    b c p <= c gamma(P+d) + 2c Z + c s.

In the first inequality of (2), the u-q branch gives P<=5Z; the
other branch combined with the bound for p gives

    k P <= (gamma+gamma²/2)d + c Z + gamma s/2,
    k=1-(c+gamma²)/2.

This last inequality also covers P<=5Z, since k>0 and 5k<c.
Finally (1) gives L<=c²(P+d)+2cZ+(1+c)s. Thus the coefficients
of d, Z, and s are bounded, respectively, by

    c² (1+(gamma+gamma²/2)/k),  c³/k+2c,  c² gamma/(2k)+1+c.

All three expressions increase with c in the range here.
Using c<485/306 (checked by 3^306<2^485) makes them respectively
less than 547/10, 113 and 23 by rational arithmetic. These same
bounds dominate the earlier gap/first-copy case, and also the
identical-direction bound L<=8Z+33d+16s+8 (Z>=2). Therefore

    L <= (547/10)d + 113Z + 23s.

The established estimates Z<=16 log_2 L, s<=2 log_2 L and L>=2^24
give (113Z+23s)/L<=1854*24/2^24<1-(547/10)/55. This proves the
claim. The [bounded replay and rational constants](check_power_coverage.py)
are independent of the unrestricted identities above.
