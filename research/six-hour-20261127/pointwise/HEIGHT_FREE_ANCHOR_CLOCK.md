# A uniform clock for all positive rational height cutoffs

For every starting positive odd integer n and every H≥1, there exists

    0≤j≤ceil(log₂[3(n+1)])

such that every positive reduced p/q with max(p,q)≤H satisfies

    v₃(U^j(n)+p/q) ≤ C log(2H) log(3+log(n+1)).

The clock may depend on H; its maximum delay and the second logarithm do not. On a segment starting at x=U^J(n), any k with 2^k≥3(x+1) forces a discrepancy. In particular the whole positive height ball has a shallow phase between J and 2J whenever (4/3)^J≥3(n+1), regardless of H, with score O(log(2H)log(3+J+log(n+1))). A nonempty subfamily inherits each bound by domination. The analogous signed full-height assertion requires a nonzero starting displacement, which holds at a starting state above H.

To prove this, choose a maximizing phase t_i=p_i/q_i at each clock, with 3∤q_i. If k edges match and E is their full division sum, write u_i=q_i x_i+p_i. The exact displacement gives 2^E q_0 u_k=3^k q_k u_0. Consequently 3^(k+r) divides u_k whenever 3^r divides u_0. The terminal denominator may be even. If u_0≠0 then u_k≠0, and for every 2^s dividing u_k,

    2^(k+s) 3^r ≤ H(x_0+1).                                          (1)

Indeed 2^s 3^(k+r)≤|u_k|≤H(x_k+1) and physical growth gives 2^k(x_k+1)≤3^k(x_0+1). Cancellation of 3^k proves (1). If both p_k and q_k are odd, s≥1. The even-denominator example in the frozen source continues to obstruct an attempted binary divisibility by 2^E at the start with the final denominator removed.

For the full positive ball, put a=floor(log₃ H). Some p in [1,3^a] satisfies p≡−x_0 mod 3^a, and p/1 is available. Thus the maximizing initial score is at least a. In (1) take r=a and s=0. Since H<3^(a+1), any matching run has 2^k<3(x_0+1). The forced discrepancy and the local Yu bound of the reviewed theorem give the claimed clock and precision. For a full signed ball starting above H the same baseline p/1 is available and no initial equality is possible.

The binary scale in the dependence on the initial state is attained within one step: at n=2^(k+1)−1 the positive anchor 1 follows k physical exponent-one steps, ending with positive odd state, and (1) is an equality for H=1,r=0,s=1. At the fixed physical state 1 the length-k signed-magnitude track t_i=3^i 2^(k−2i)−1, 0≤i≤k, has positive rational phases of height ≤3^k and has terminal displacement numerator 3^k when k≥1. It shows how even denominators realize the full transported ternary precision at a bounded ordinary state. It does not select maximizing phases in the whole height ball at the beginning of this example.

TernaryEndpointBudget.lean proves the terminal divisibility, physical growth and inequality (1) from finite cross-denominator data. The elementary choice of p, the ensuing forced edge, and the analytic Yu application are written deductions. The statement supplies an H-dependent shallow clock within one common interval. A single clock satisfying every height cutoff simultaneously is a distinct quantifier order.
