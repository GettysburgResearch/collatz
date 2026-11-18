# A clock barrier for forward repayment of the moving rank

**Status: PROPOSED.** Consider any odd ordinary n with H=v3(n)>=1. Let T be the positive shortcut map and R the moving rank of [the return-domain theorem](README.md). The first-edge excursion obstruction in PR #92, [T-A3-1051 in MERGING_BARRIERS.md](../astra-three-routes/pass5/MERGING_BARRIERS.md), gives R(n)=n²/3^H and the rank at T(n). Here a lower bound persists at *every physical time* up to a linear multiple of H, across all intervening mode changes. It applies to forward repayment. A lower-rank source on another branch can meet the given orbit without causing a forward rank drop.

Let t>=1, let q count the odd source states through time t-1, and suppose

    15 * 4^t < 3^H.

Then y=T^t(n) is greater than 1 and

    R(y) >= n² 6^q / (20 * 8^t).                            (1)

In particular any adaptive rule that returns a positive physical time t with 20*8^t<3^H lands at a strictly larger rank. A forward drop from this one ternary stratum requires at least H log(3)/log(8) - O(1) shortcut steps, independently of the initial dyadic residues and intervening modes.

## Proof

Write 2^t y=3^q n+C. With odd positions 0=i_0<i_1<...<i_{q-1}<t, the constant is C=sum_j 3^{q-1-j}2^{i_j}. Thus C is odd. Replacing i_j by t-q+j in this positive sum gives

    C <= 2^{t-q}(3^q-2^q),      C+2^t <= B=2^t(3/2)^q.

The stated clock bound gives y>=n/2^t>2. Also

    2^t(2y+1)=2*3^q n+(2C+2^t).

Because 0<2C+2^t<=2B<3^{H+q}, we have 3^{h(y)}<=2B for h(y)=v3(2y+1). The four-entry formula T-A3-902 in PR #92 restricts the minimizing index a to 0, 1, 2 and possibly h(y). Hence 3^a<=max(9,2B)<=3B (here t,q>=1).

For such an index write d=3^a-2^{a+1}, c=3^a-2^a and z_a(y)=dy+c. Directly for a=0,1,2 and by c/d=1+2^a/d<=5 for a>=2, we have |c|<=5|d| and |d|<=3^a. Consequently

    2^t z_a(y)=d 3^q n+D,        D=d C+2^t c,
    0<|D| <= 5 |d| B <=15 B² < 3^{H+q}.

The strict nonzero follows because d and C are odd. The last strict inequality uses B²/3^q=4^t(3/4)^q. Thus the valuation of z_a(y) is exactly the valuation of D, and its ternary part is at most 5|d|B.

For a>=2, d and c are positive, so |z_a(y)|>=|d|y. At a=0 we have equality and at a=1 the absolute value is y-1>=y/2. Therefore every candidate satisfies

    R_a(y) >= |d| y²/(20 B) >= n² 6^q/(20 * 8^t),

using y>=3^q n/2^t in the last step. Taking the minimum gives (1).

## Two consequences and the scope of the constants

**No bounded physical sampling rule restores the first moment.** Take the enlarged unsafe set U from the [return-domain result](README.md) and initialize with f=1_U R^{-2}. Its first rank moment is finite. For every cap L>=1, choose at each source x in U any positive shortcut time in [1,L], with only physical killing on a fixed floor H_0. Project the surviving mass onto all ordinary endpoints above H_0. The output first rank moment is infinite.

Indeed x=3^H for H=4 modulo 16, H>=4, belongs to U by the source PR's [R-A3-1004](../astra-three-routes/pass5-spectrum-switch/INDUCED_MASS.md). Here R(x)=x. For all sufficiently large H the first L states clear H_0 since T^j(x)>=x/2^j. At the selected time inequality (1) gives a contribution at least 1/(20*8^L) for each such x. If a selector additionally promises to land in U, the same conclusion applies with that output projection. Projection onto arbitrary subsets could delete the witnesses. For unbounded clocks t=o(H) the single-source rank ratio tends to infinity, without a conclusion about this particular summed moment.

**The shortest possible repayment clock has linear order.** For each H>=1 put t=floor(log_4(16*3^H))+1. Choose by CRT infinitely many n congruent to 3^H modulo 3^{H+1} and to -3^{-1} modulo 2^t. The first odd step and t-1 subsequent even steps are legal, and the endpoint has

    y=(3n+1)/2^t,       R(y)<=y²<=16 n²/4^t < R(n).

Thus if t_min(H) is the minimum over all odd positive sources of exact ternary order H of their first positive-time strict rank drop (infinite allowed for an individual source), then

    log(3)/log(8) <= liminf t_min(H)/H
                   <= limsup t_min(H)/H <= log(3)/log(4).

The construction chooses sources depending on H. The exact sharp rate and universal eventual repayment remain open.

The [clock replay](check_clock.py) verifies the inequality, its domain and the explicit CRT path against direct shortcuts and the resident rank evaluator on finite examples.
