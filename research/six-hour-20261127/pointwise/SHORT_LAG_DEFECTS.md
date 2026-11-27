# A pointwise lower bound for short-lag block-sum defects

Consider a fixed non-eventually-periodic positive odd trajectory x_i=U^i(n), with full division exponents e_i. For h≥1 and any nonnegative integer A, let m be the number of indices 0≤i≤T for which the sum of e_i,…,e_(i+h−1) differs from A. The observed word extends h clocks beyond the counted prefix. Using the adaptive dictionary inequality of Weaver's Paper 15/v2, one obtains an absolute effective C such that

    T+1 ≤ exp[C(m+1)/log(m+2)] [log(n+1)+A+2].                         (L1)

For a primitive positive ordinary cycle of period P≥2 and 1≤h<P, let m count the P cyclic windows. With a different absolute C,

    P ≤ exp[C(m+1)/log(m+2)] [log(P+2)+A+2].                           (L2)

For the proof call an index good when its length-h sum equals A. At consecutive good indices i,i+1 subtraction gives e_(i+h)=e_i. In a good interval of start indices [a,b], the word on physical edges a,…,b−1 therefore follows the periodic repetition of (e_a,…,e_(a+h−1)), including short intervals and partial terminal periods. Store one such word per good interval if its word contains a nonone. The number of intervals on a linear cut is ≤m+1, each stored word costs A, and the at most 2m edges incident to nongood indices can be counted as singletons or free ones. Add the word (2) if none were stored. The resulting dictionary budget is ≤(m+1)A+2, and the actual piece count is at most 3m+1. The fixed nonperiodic source never starts a step on a positive template cycle or at one, so (A1) applies. The multiplicative m+1 from the dictionary budget can be incorporated in exp[C(m+1)/log(m+2)] because log(m+1)=O((m+1)/log(m+2)). This proves (L1). For cyclic data cut through a bad clock if there is one, using its repeated endpoint and at most one additional piece. When all windows are good, their differences give exponent period h, impossible on a primitive ordinary cycle of longer least period. A representing positive cycle would have least period at most the length of a stored template, h<P, so (C6) applies with denominator one and gives (L2). [Weaver, adaptive dictionary (A1) and (C6)](https://rstation.ai/problems/collatz/papers/15)

When m≤(T+1)/2, summing all window sums bounds (T+1−m)A by h times the division sum on the first T+h steps. Positivity gives that division sum ≤2(T+h)+log₂ n, by multiplying 2^e x_next=3x+1≤4x. For 1≤h≤T on a fixed source, A=O(h) for large T. Thus for T/(h+log(n+1)+2)→∞,

    m ≫ log[T/(h+log(n+1)+2)] · log log[T/(h+log(n+1)+2)].

The case m>(T+1)/2 is immediate. On a cycle apply the same argument with total ≤2P. The complementary lag P−h has the same defect count against total sum minus A, up to rotation, so the reduced lag min(h,P−h) may be used. If A exceeds the total all clocks are defects. The cyclic ratio is P/[min(h,P−h)+log(P+2)+2]. In particular all h≤T^(1−δ) (or reduced cyclic h≤P^(1−δ)) force ≫_δ log T log log T (respectively ≫_δ log P log log P) defects. These counts concern every comparison sum, independent of its rounding convention. Weaver and coauthors give stronger bounds under arithmetic conditions on an upper or Farey window and a distinct sparse-numerator method. [Paper 22](https://rstation.ai/problems/collatz/papers/22)

There is also a direct bridge to rational tracks. On a good window, write 2^A x_(i+h)=3^h x_i+B_i, and set t_i=B_i/(3^h−2^A). Then

    x_i+t_i = 2^A(x_(i+h)−x_i)/(3^h−2^A).

The displacement is nonzero on an injective orbit and at a proper lag of a primitive cycle. At adjacent good phases e_(i+h)=e_i, giving 2^e_i t_(i+1)=3t_i−1. The denominator of each reduced t_i is prime to three, and its log height is O(h+A) since 0<B_i≤3^h 2^A. The moving-shadow theorem (M1) thus supplies an alternative finite bound with the same order. This bridge propagates the hypothesis of constant lag sums through genuine rational phase centers. It gives no theorem forcing those sums to concentrate on an arbitrary escaping trajectory.
