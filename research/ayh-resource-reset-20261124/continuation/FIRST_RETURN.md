# Physical first returns and a ternary stopping test

**PROPOSED written theorem.** There exist arbitrarily large n in the exact eight-excess section B whose *first positive physical return* v to B satisfies v > n^(27/25). This tests a possible stopping proof at its actual return, including every intermediate shortcut clock. It leaves eventual returns to smaller members and mergers with other starting values open.

Let α=log₂3. Take arbitrarily large convergent denominators Q with numerator a, so |Qα−a|≤1/Q. Set k=Q−1, d=2k and e=ceil((d+1)/5). Define D=d−e−k+a and f=ceil((D+1)/5). We will build

$$
u=2^k c-1,\qquad n=(2^e u-1)/3,\qquad v=3^k c-1 .
$$

Require c to solve

$$
2^k c\equiv1+2^e\pmod3,\qquad
3^{k+1}c\equiv 2+2^f\pmod{2^{f+1}} .
$$

The Chinese remainder theorem gives exactly one class modulo 3·2^(f+1). Choose its least member at or above 3·2^(d−e−k)(1+3/Q). The overshoot is less than 3·2^(f+1). Here (d−e−k)/d tends to 0.3, while f/d tends to (0.8+(α−1)/2)/5<0.22, so the relative rounding error is o(1/Q). Consequently

$$
n/2^d=1+3/Q+o(1/Q),\qquad
v/2^D=2^{Q\alpha-a}(1+3/Q+o(1/Q)).
$$

Uniformly in the sign of the phase error, both ratios lie in [1+1/Q,1+5/Q] for all large Q. Thus d,D are the respective binary exponents. Both marks hold since (d+1)/Q tends to 2 and (D+1)/Q tends to 1.6+α−1<2.2. The first congruence ensures n is integral, and n is odd since e≥1. Its cofactor u is odd, giving exact exponent e. The second congruence gives 3v+1 congruent to 2^f modulo 2^(f+1); v is odd and its exact exponent is f. The ceilings put both surpluses between zero and four, inclusive.

The path from n consists of its odd step followed by halvings to u at clock e. Every state at intermediate clocks 1,…,e−1 is even. Its next k states are Tʲu=3ʲ2^(k−j)c−1 for 0≤j≤k. The last is v. Each input with j<k is odd and its next output is also odd (c is even by the second congruence), so the exact exponent of 3Tʲu+1 is one. These inputs are all ≥u>32 and fail the lower critical inequality. Hence v is the first positive B return. Finally D/d tends to 4/5+(α−1)/2>27/25 because 3²⁵>2³⁹, and log v/log n has that same limit.

The exact routine `verify_rising.py` constructs and replays the entire trajectory for denominators 53, 306 and 665, at source binary exponents 104, 610 and 1328. Both ordinary section memberships, absence of any intervening critical state, and v²⁵>n²⁷ are checked by integer arithmetic. The written proof establishes infinitude.

## Which ternary mesh hit would actually pay the original target?

The inverse four-clock row traverses s odd inputs in 4s clocks. Compressing its three even inputs per block suggests a substantially smaller candidate *relative to the original target*. The following identity holds independently of any row. For s≥1 and k≥1, let w=3ˢk−1 and v=2ˢk−1. The first s clocks from v are odd, yielding Tˢv=w. Thus if a specified q merges with some w=3ˢk−1 satisfying 2ˢk<q+1, there is a physically certified smaller partner v<q in the same component as q. For k the closest positive integer to (q+1)/3ˢ the mesh error is O(3ˢ), and v+1=(2/3)ˢ(q+1)+O(2ˢ). This is a candidate below the original q when 3ˢ is small relative to q. The unresolved condition is the merger between that *particular* q and an admissible w.

One can state the open obligation intrinsically. Put s(z)=v₃(z+1) and P(z)=2^s(z)(z+1)/3^s(z)−1, a positive integer for positive z (for s=0 it is z). Then P(z) reaches z in s(z) odd clocks. For odd z, P(Tz)=P(z), since Tz+1=3(z+1)/2. Universal convergence is equivalent to the assertion that every q>1 has some forward state z for which P(z)<q. Sufficiency follows by strong induction, since P(z) and q both reach z and 1 is on a closed cycle. Necessity follows by taking z=1 in a convergent orbit. In particular a minimal counterexample q would obey, along its very same forward orbit,

$$
(3/2)^{v_3(z+1)}\le (z+1)/(q+1).
$$

The formulation permits ternary savings after an actual excursion above q. It does not assign an independently random ternary residue to z. A constructive obstacle to an inverse-only version is q=7. None of the starts 1,…,6 ever reaches 7 (their paths are verified directly), so a reduced v<7 can merge with 7 only at a later common state, never by making v reach 7 itself. More generally doubling q to fit the mesh demands a discrete logarithm modulo 3ˢ. For q congruent to 1 modulo 3ˢ, the least j≥0 with 2ʲq congruent to −1 modulo 3ˢ is 3^(s−1), using the order 2·3^(s−1) of 2. This is far beyond the linear-in-s cost that preserves the gain for large s. These obstructions identify the missing pointwise step without turning a typical high-register estimate into a statement about one q.

`TernaryStopping.lean` checks the odd-block identity and the equivalent universal mesh test formulated with existential s,k and a physical hit of 3ˢk−1. For any admissible smaller witness one may use maximal s=v₃(z+1), since each further admissible all-odd compression decreases the preceding integer. The scalar maximal-valuation formulation above is written. Both Lean declarations compile using the same frozen PR 197 imports as the counting module.
