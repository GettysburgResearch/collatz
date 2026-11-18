# Exact minimum merger clocks for high moving indices

**Status: PROPOSED.** The [short-merger dichotomy](SHORT_MERGERS.md) classifies all lower-rank diagrams in its precision range. Two consequences turn the classification into lower bounds on the *minimum over all positive witness sources and both physical clocks*, including arbitrary adaptive choices. Use its notation and the same shortcut clock. Define

    ell(n)=min { max(t,s) : T^t(n)=T^s(m), m>0, R(m)<R(n) },

with infinity for the empty set. The least rank and a minimum physical clock are independent objectives. An acceleration can consume many shortcut steps in one module.

## Prime-to-six denominators retain the minimizing index

The denominator of alpha_a in lowest terms is |d_a| and is coprime to six. Indeed gcd(c_a,d_a)=1 since their difference is 2^a and c_a is odd for a>=1. Applying any word preserves the entire prime-to-six part of that denominator, including multiplicities: directly the numerator of (d_a C_v−3^{q_v} c_a)/(2^t d_a) is a unit at every prime dividing d_a. An exact alignment F_v(alpha_a)=F_w(alpha_b) therefore requires |d_a|=|d_b|. Equality with F_w(−1/2) requires |d_a|=1.

Since d_0=d_1=−1, d_2=1, and d_a is strictly increasing from d_3=11, **every** short cheaper merger in the precision regime with a>=3 must align b=a. The moving-index resonance at −1/2 is possible only from the three fixed modes, even though its companion may have arbitrarily large index. In the surviving aligned case eta=alpha_a implies d_a divides L−B, using the notation Bm=Ln+E and gcd(c_a,d_a)=1.

## Exact clock a+1, with no competing witness

Take any a>=5 and n for which a minimizes and H=v3(z_a(n)) satisfies

    3^H > 1000 |d_a|³ 27^a.                                  (1)

Then ell(n)>a, regardless of its first dyadic bits. If its prefix is 1^a0, then **ell(n)=a+1**. In particular an entire physical aligned block is necessary even when arbitrary unequal clock diagrams are permitted.

To prove the lower bound assume t,s<=a. The precision dichotomy and the denominator argument force b=a and d_a dividing L−B. The normalized multipliers L,B are at most 3^a. Since 2d_a>3^a, a nonzero difference could only be plus or minus d_a, which is odd. Equal clocks give two odd multipliers and cannot do this. Suppose s>t. The even multiplier L=2^{s-t}3^{q_v} is at most 2*3^{s-1}<=2*3^{a-1}<d_a. The last inequality holds at a=5 and subsequently because 3^{a-1}>2^{a+1}. The other multiplier B=3^{q_w} must then be 3^a, as every smaller power is below d_a. This forces s=a and L=3^a-d_a=2^{a+1}, implying 3^{q_v}=2^{t+1}, an impossibility. Interchange the arms for t>s. We conclude L=B, hence t=s and q_v=q_w. The exact aligned rank ratio is one. This contradicts a cheaper witness. For the upper bound the physical block 1^a0 itself strictly lowers its a-component after a+1 steps, with the endpoint serving as the lower witness.

These hypotheses hold at ordinary positive sources for every a. For example take H=6a+7 and impose z_a(n)=3^H modulo 3^{H+1}. Then h(n)=a because 2 alpha_a+1=−3^a/d_a. The fixed components have respective values n², (n−1)²/3, (n+5)²/9, since n is −1/2 modulo 3^a. For sufficiently large n in this stratum the a-component is strictly smaller than all three by 3^H>9d_a². Its precision satisfies (1). Independently prescribe n=2^a−1 modulo 2^{a+1} to force the aligned word. There are arbitrarily large CRT lifts and the minimum clock is exact on all sufficiently large lifts. For a source known to reach 1, use the [halving-tail completion](TERMINATING_TOWERS.md) on the same word with the specified ternary source class. The exact optimality holds on those explicitly terminating examples as well.

## Logarithmic lower clocks on the actual unsafe support

There is also a fixed-index family where every possible lower diagram has a logarithmic clock, with an explicit successful witness. For M>=2 take H=3M+7, k=H+M+2, force n=1+3^H modulo 3^{H+1}, and force the binary word 1^M 0^k. Such n exist by CRT; choose the least positive lift. Then a=1 uniquely minimizes at n, R(n)=(n−1)²/3^H and 3^H>1000*27^M. The relevant fixed valuations follow from n=1 modulo 9. The smallest lift is at least 1+3^H, since its residue modulo 3^{H+1} is exactly 1+3^H.

Suppose both clocks t,s<=M. The forward word is 1^t, including the empty word when t=0. Exact root alignment and a lower rank would require

    |d_b|² 4^{s-t} 3^{t-q_w}<1.

If s>=t the left side is at least (4/3)^{s-t} since q_w<=s. If s<t, every root alpha_b<=1 satisfies F_w(alpha_b)<=2(3/2)^s−1<F_{1^t}(1). This follows by monotonicity of both affine branches and the all-odd upper trajectory starting at 1. So there is no exact alignment. The same upper bound excludes the half companion at s<t. For s>=t, F_w(−1/2) has exact dyadic denominator 2^{s+1}, while F_{1^t}(1)=2(3/2)^t−1 is integral at t=0,1 and has exact denominator 2^{t-1} thereafter. Equality is again impossible. The dichotomy rules out every cheaper merger with both clocks <=M.

The first A module has length M+1: after 1^M0 the next bit is even. It increases rank by the [forward classification](SHORT_MERGERS.md) at t=M+1, whose precision 3^H>200*8^{M+1} holds for M>=2. The source is an odd ternary unit and hence lies in the [actual re-entry support](REENTRY_SUPPORT.md). Its endpoint after the longer prescribed path is

    y=((3/2)^M(n+1)−1)/2^k < (n−1)/3^{H/2}.

Indeed (n+1)/(n−1)<=2 and k=H+M+2. Thus R(y)<=y²<R(n), giving ell(n)<=M+k. The CRT representative satisfies

    1+3^{3M+7} <= n < 2^{5M+9}3^{3M+8},     M < ell(n) <= 5M+9.

Consequently these explicit sources have ell(n) of order log n. No selector giving a universally successful moving-rank merger in o(log n) physical steps on each arm can cover the re-entry support. This lower bound leaves higher-clock selectors open and makes no assertion about an arbitrary source's eventual repayment.

Additional arbitrarily large lifts in the same class can be certified terminating: complete the word to a power of two using the given ternary precision as in [the terminating construction](TERMINATING_TOWERS.md). The preceding lower and upper inequalities in terms of M still apply. Only the least CRT lift was used for the displayed upper bound on n.

The [replay](check_optimal.py) validates the rank strata and the constructive upper clocks, and exhaustively inspects all alternative physical diagrams up to their lower clock caps on small examples. The global lower bound at arbitrary a and M is the argument above.
