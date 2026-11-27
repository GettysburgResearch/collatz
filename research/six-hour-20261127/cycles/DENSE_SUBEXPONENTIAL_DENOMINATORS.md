# Subexponential complete denominators with linear defects at every lag

**PROPOSED elementary counterfamily.** There are primitive positive rational cycles of growing odd period \(p=aqr\), with distinct primes \(q,r\to\infty\), such that
\[
 c\,a(q+r)\le\log d\le C\,a(q+r)=o(p)
\]
for their full reduced phase denominator d. Every gap lies in \(\{1,2\}\), cumulative native-clock discrepancy has width less than two, every odd phase has real size comparable with \(a^2\) with absolute constants, and the total drift tends to zero. Yet for **every** proper window length v and integer clock u, at least \(p/64\) starts have a different window total. In particular subexponential complete denominator, bounded discrepancy and uniformly high real phases do not force a sparse lag, even simultaneously.

This combines the earlier independent-period switch construction with disjoint free date switches from the project's mechanical-carry theorem. The additional ingredient is a simultaneous lower bound on all cyclic Hamming distances with the actual repetitions of the random switches taken into account. [Prior independent switches](https://github.com/GettysburgResearch/collatz/blob/ebf2682a0cefb8d66ef43c822f19ac4c1c97bbd4/research/unrestricted-cycle-denominator/NEAR_FULL_GCD.md) · [PR200, complete modular carry MC1–MC2](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/arithmetic/COMPLETE_MODULAR_CARRY.md)

## Clock, heights and actual denominator

Put \(n=qr\). Let \(b_0/a_0>\lambda=\log_2 3\) be an arbitrarily late upper continued-fraction convergent, and \(b_1/a_1<\lambda\) its preceding convergent. Take \(b=2b_0-b_1,\ a=2a_0-a_1\). Consecutive convergents give \(ba_0-ab_0=1\), hence \(\gcd(a,b)=1\) and
\[
 1/a < b-a\lambda<6/a .
\]
For the lower bound, \(b-a\lambda=1/a_0+(a/a_0)(b_0-a_0\lambda)>1/a_0\). For the upper bound use \(b_0-a_0\lambda<1/a_0,\ a<2a_0\). Choose \(a>n^2\) sufficiently large at every stage. The full drift \(n(b-a\lambda)\to0^+\). All constants below are absolute.

Every block initially has the a mechanical odd gaps determined by dates \(E_i^0=\lceil ib/a\rceil\) for \(0\le i\le a\). There are \(2a-b\) ones, all isolated since \(2b/a>3\), so each one is followed by a two cyclically. Keep the internal centers \(i\in[1,a-1]\) with incoming/outgoing pair \(12\). These pairs are disjoint and there are at least \(2a-b-1\) centers. Split the centers into two groups as equally as possible. Each has at least \(a/7\) elements for all sufficiently large a. In a block \(j\bmod n\), each chosen center has a bit \(s_{i,j}\); add this bit to the native date \(E_i^0\). Its pair of odd gaps becomes \(1+s_{i,j},\,2-s_{i,j}\). No other gap depends on that bit.

For a center in the first group, its bit depends only on \(j\bmod q\); in the second, only on \(j\bmod r\). The absolute period discrepancy relative to \(\theta=b/a\) always lies in \([0,2)\). Thus every rotated native prefix date differs from \(\theta k\) by less than two. Put \(D=2^{bn}-3^{an}>0\). In every odd phase numerator the summands \(3^{p-1-k}2^{E_k}\) are consequently within a factor four of \(3^{p-1-k}2^{\theta k}\). The geometric sum divided by D equals \(1/(2^\theta-3)\). Since \(\theta-\lambda\) is between positive absolute multiples of \(a^{-2}\), every odd phase is between positive absolute multiples of \(a^2\). The rotated odd numerators and odd D give the exact prescribed gaps. All intermediate shortcut phases satisfy the same bounds up to an absolute further factor because gaps are at most two.

Write \(P=3^a,\ Q=2^b\). The exact block recurrence is \(Qx_{j+1}=P x_j+c+C_q(j)+C_r(j)\), where c is its baseline offset and \(C_q,C_r\) are functions of periods q,r. This follows by changing a selected term \(3^{a-1-i}2^{E_i^0}\) to twice its value, independently for every internal center. The solution is the sum of the constant-offset solution of denominator dividing \(Q-P\), the q-periodic solution of denominator dividing \(Q^q-P^q\), and the r-periodic solution of denominator dividing \(Q^r-P^r\). Uniqueness follows from \(Q^n>P^n\). The full common reduced denominator therefore divides \(\operatorname{lcm}(Q^q-P^q,Q^r-P^r)\), and \(\log d=O(a(q+r))\).

## Uniformly many defects

Choose independently, with equal probability, the bits for all pairs (center, residue modulo its assigned prime). Let \(D_v\) be the cyclic Hamming distance between the odd gap word and its shift by \(1\le v<p\). If \(a\nmid v\), any gap controlled by a bit is compared to either a deterministic gap, an independent bit, or the opposite member of that same bit's pair. A comparison to the same member of the same pair would require the same offset modulo a. In the first two cases the probability of mismatch is \(1/2\); opposite members with the same bit always differ. If \(v=at\), either \(q\nmid t\) or \(r\nmid t\). Every gap controlled by a center in at least one of the two groups is then compared with an independent choice. These cases give \(\mathbb E D_v\ge p/16\) in either regime.

Changing one first-group bit affects two gaps in each of \(n/q=r\) blocks, hence at most \(4r\) comparisons in \(D_v\). The second group's bound is \(4q\). The sum of squared bounded-difference constants is at most \(16a n(q+r)\). The standard bounded-differences estimate gives
\[
 \mathbb P\{D_v<p/32\}
 \le \exp[-a n/(8192(q+r))].
\]
For completeness, reveal the independent bits in order. Each increment of the conditional-expectation martingale has conditional mean zero and lies in an interval of the stated length. Convexity gives its conditional exponential moment at parameter t at most \(\exp(t^2 c_i^2/8)\): for a mean-zero variable of range \(c_i\), the second derivative of its log moment-generating function is the variance under the tilted law, at most \(c_i^2/4\). Integrate twice from zero. Multiplying the bounds and optimizing t gives the displayed inequality. A union bound over p−1 shifts tends to zero since \(a>n^2\) and the primes tend to infinity. With probability tending to one every \(D_v\ge p/32\); in particular the physical odd word is primitive. If \(e_{i+v}\ne e_i\), at least one of \(B_i=E_{i+v}-E_i\) and \(B_{i+1}\) differs from u. Thus there are at least \(D_v/2\ge p/64\) exceptional starts for *every* u and v.

## Positive lower bound for the actual reduced denominator

There are at least \(a(q+r)/7\) independent bits. The map from their assignments to the labeled gap word is injective: the incoming gap of each switched center gives the bit in each block and every residue appears. At fixed clocks, the number of such labeled words with \(d\le Y\) is \(O(p a^2Y^2)\). Indeed the smallest positive phase is a reduced fraction with numerator at most \(C a^2 d\), and its denominator is at most Y. Each such fraction determines one forward orbit; there are at most p choices of initial odd phase in a length-p presentation. Take for example \(Y=\exp[(\log 2)a(q+r)/32]\). The proportion of all assignments with \(d\le Y\) tends to zero, since \(\log(pa^2)=o(a(q+r))\). Intersect this event's complement with the simultaneous Hamming-distance event. This proves the lower denominator bound and all claimed properties.

These are physically realized rational cycles, not positive ordinary cycles. A proof of \(d>1\) for every ordinary candidate could still use the exact endpoint \(d=1\). The construction rules out inferring the requisite lag, or any period-independent positive exponential rate for d, from the stated phase bounds, binary alphabet, critical clock mean, bounded discrepancy and linear defect complexity.
