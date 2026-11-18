# Uniform arithmetic nonconcentration on time-height curves

**PROPOSED.** Fix an irreducible P(t,X) over the rationals with integer coefficients, depending on both t and X. For every positive ordinary shortcut trajectory x_j, every time interval I of N successive nonnegative integers, and every integer modulus Q≥2,

    #{j∈I : P(j,x_j) ≡ 0 mod Q}
          ≤ C_P (1 + N/(1+min(log Q,log(2N)))).                       (1)

The constant is independent of the starting integer, time origin and modulus, including the factors 2 and 3. No assumption of simplicity, escape, limiting measure or typicality is made. In particular arbitrary increasing precision along longer intervals forces the fraction of hits to zero. Exact algebraic hits cost O_P(N/log(2N)+1) even at very large time translations. For example, no ordinary orbit can follow j↦j² to unbounded modular precision on a positive upper Banach proportion of times.

## Eliminating the height variable at short returns

A word w of d≥1 shortcut branches sends X to (3^s X+C_w)/2^d, where s counts the ones and the integer offset satisfies log(1+C_w)=O(d). Put h=deg_X P. Form

    B_w(t,X)=2^(dh) P(t+d,(3^s X+C_w)/2^d),
    R_w(t)=Res_X(P(t,X),B_w(t,X)).

This is a fixed-size Sylvester determinant with integer polynomial entries of degree O_P(1) in t and logarithmic coefficient height O_P(d+1). Consequently deg R_w≤r for a fixed r≥1 and every coefficient has absolute value at most exp(C_P(d+1)). Furthermore R_w is nonzero. Indeed a zero resultant would imply proportionality of P and its affine pullback: P is primitive in X over Q[t] up to a scalar, irreducible over Q(t) by Gauss's lemma, and the affine substitution is a polynomial-ring automorphism over Q, preserving irreducibility. Center the state coordinate at the rational fixed point of the affine word. Its slope λ=3^s/2^d is neither 1 nor a root of unity. For an invariant polynomial Σ b_l(t)Y^l, the identity b_l(t+d)λ^l=c b_l(t) forces c=λ^l by the leading t coefficient, and then b_l constant by periodicity. Thus the only nonconstant irreducible invariant polynomial is horizontal, contradicting the hypothesis.

If j and j+d both give hits modulo any integer q, then q divides R_w(j) for the actual word w. This follows from the integral polynomial Bézout identity for the resultant and evaluation at (j,x_j). Clearing a power of two in B_w multiplies an already divisible integer. No modular division by two is needed at a dyadic factor.

## Uniform count for every modulus

For any nonconstant univariate integer R of degree v≤r and leading coefficient a≠0, the times with q|R(t) lie in at most r^ω(q) residue classes modulo a common integer at least (q/|a|)^(1/r) if q≥|a|. Here ω counts distinct prime divisors. Indeed for p^e exactly dividing q and e>v_p(a), factor R over an algebraic closure of Q_p. Every solution t has valuation v_p(t−α)≥(e−v_p(a))/v at one of its roots. Two integer solutions near that same root agree modulo p^ceil((e−v_p(a))/v). Multiply the moduli by the Chinese remainder theorem; discard primes with e≤v_p(a). This proves the count. The elementary bound r^ω(q)≤C_(r,ε)q^ε follows by separating the finitely many primes below r^(1/ε). For a nonzero constant resultant smaller than q in absolute value there are no hits.

If Q≤N take q=Q. If Q>N has a prime factor p>N, take q=p. In the remaining case multiply prime factors, with multiplicity, until reaching q≥N, so that N≤q≤N² and q divides Q. Let m=min(log Q,log N); in all cases log q≥m. For bounded m the trivial count suffices, so assume m is large. Set D=floor(c m) for a fixed sufficiently small c depending only on P. For d≤D all nonzero resultant coefficients then have absolute value ≤exp(m/4). Thus for each word the possible starting times in a length-N interval number at most

    r^ω(q) [1+N exp(−3 log(q)/(4r))].

There are fewer than 2^(D+1) words of lengths 1 through D. Taking, for example, ε=1/(8r) in the prime-factor bound, the aggregate of the second terms is O_P(N exp(−m/(4r))) by reducing c. For the first terms, when q≤N² choose instead ε≤1/16, obtaining O_P(N^(1/4)) after reducing c; when q is a single prime larger than N, r^ω(q)=r suffices. Absorb both errors in O_P(N/(1+m)).

List all hits in increasing order. There are at most 1+N/D hits starting the list or following a gap longer than D. Every other hit is accounted for by a preceding hit with one of the short words above. This proves (1).

## Constant algebraic phases and the precise exception

For irreducible P(X)∈Z[X], without a clock argument, the resultant is an integer independent of time of absolute value at most exp(C_P(d+1)). Two hits at separation d with log Q>C_P(d+1) therefore force it to vanish. The same invariant-polynomial argument says P is linear and its root ξ is exactly fixed by the intervening affine word. Every cyclic phase of that formal word has odd denominator, and each consecutive pair y,y' satisfies 2y'=3^b y+b, hence y≡b mod 2. The return word is therefore on the genuine periodic dyadic orbit of ξ; ξ can be negative or nonintegral in the real sense. If ξ is not such a periodic point or P has degree at least two, successive hits are separated by at least c_P log Q−1. The resulting count is O_P(1+N/(1+log Q)). This also identifies what prevents the same bound for an arbitrary constant target: an ordinary periodic source at its cycle vertex yields positive-frequency hits even at infinite precision.

The argument differs from holonomic rigidity for full linear identities in the successive states [Paper 106](https://rstation.ai/problems/collatz/papers/106/v1). It bounds hits of a specified non-invariant curve; it gives no reason for a hypothetical escaping orbit to require such hits.
