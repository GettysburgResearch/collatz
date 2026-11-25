# A p-adic Subspace Theorem for critical backwards scripts

**Status: PROPOSED written deduction using the classical Schlickewei Subspace Theorem.** This is not a formalization of that theorem or a proof of Collatz. It gives arithmetic rigidity for a new class of actual critical-record limits. The rationality-to-periodicity consumer is proved in README §4, not assumed.

Let e=(e_1,e_2,...) be any infinite sequence of positive gap lengths satisfying S_j=sum_(i<=j)e_i, 2^S_j<3^j for every j>=1. Its ternary coordinate is

    z = sum_(j>=1) 3^(j-1) / 2^S_j in Z_3^times.

Use the backwards word convention of README throughout. For a finite word W of length n, total clock s(W), and partial sums S_j(W), define
    B_W = sum_(j=1)^n 3^(j-1)2^-S_j(W),
    C_W = 2^s(W) B_W = sum_(j=1)^n 3^(j-1)2^(s(W)-S_j(W)).
For the empty word B=C=0, s=0. Every nonempty C_W is a positive integer. Concatenation gives
    B_UV = B_U + 3^|U| 2^-s(U) B_V.
Every word of length n determines the z coordinate modulo 3^n, because all later terms are divisible by 3^n in Z_3. In particular this is the actual residue coordinate of any ordinary record limit with the retained word, not the dyadic companion series from PR182.

## 1. The theorem

Write kappa=log_3(9/2)=2-log_3 2=1.369070... . Suppose there exist finite words U_i,V_i, with r_i=|U_i|, p_i=|V_i|->infinity, r_i<=L p_i for a fixed L>=0, and the actual infinite script begins with U_i followed by at least w p_i consecutive letters of the infinite repetition V_i^infty. Rounding down or up the last partial copy changes the count by at most one.

**Theorem S1.** If
    w > kappa+(kappa-1)L,
then z is rational or transcendental (never algebraic irrational). If the script is not eventually periodic, z is transcendental.

**Theorem S2 (balanced clock).** Suppose in addition to criticality that
    (j log 3-S_j log 2)/j -> 0.
Then the same conclusion holds for EVERY fixed w>1, with r_i/p_i bounded as above.

The hypothesis is only on the cumulative gap deficit of this particular script. We do not infer it from the ordinary height growth of a hypothetical escaping ray: passing to a backwards record limit and taking the clock average need not commute.

**Corollary S3.** For a non-eventually-periodic critical script with balanced clock as in S2, if its factor-complexity function p_e(n) has finite liminf p_e(n)/n, its ternary coordinate is transcendental. In particular an algebraic irrational critical coordinate with balanced script forces p_e(n)/n->infinity (allow infinity for an infinite alphabet). This follows by an elementary repetition extraction given below. No automaticity assumption is needed. Compare the stammering method of Adamczewski and Bugeaud, *On the complexity of algebraic numbers I: expansions in integer bases*, Annals of Math. 165 (2007), Theorem 6, for ordinary p-adic base digits. The present arithmetic is weighted by variable gap costs; the digits are not ternary base digits.

## 2. Rational approximants retaining the two clock monomials

For each i suppress indices, set r=|U|, p=|V|, s=s(U), A=s(V), and periodize the actual prefix into U V^infty. Its coordinate is exactly
    z_i = B_U + (3^r/2^s) C_V/(2^A-3^p)
        = N/(X-Y),
    X=2^(s+A), Y=2^s 3^p,
    N=C_U(2^A-3^p)+3^r C_V.

The denominator is nonzero by unique factorization and is a unit at 3. The geometric sum is valid in Q_3 because the period multiplier 3^p/2^A has ternary norm 3^-p, regardless of its real size. The preperiod and the period are allowed to have different clock slopes; the period alone need not be critical. Only the combined prefix is used in the height bounds.

If m is the number of matching initial gaps, then
    |z-z_i|_3 <= 3^-m,
    m >= r+w p-O(1).
This also proves |z(X-Y)-N|_3<=3^-m. For all large i, N is nonzero because z is a unit and the approximation has agreement at least one ternary digit.

The following height bound uses the actual critical inequality at r and r+p, and the fact all gaps are at least one. For every finite word W of length n, B_W<= (3/2)^n-1 (sum the geometric majorant with S_j>=j). Hence
    2^s <=3^r, 2^(s+A)<=3^(r+p), 2^s>=2^r,
    |C_U(2^A-3^p)| <= B_U (2^(s+A)+2^s3^p)
                         <=2 (9/2)^r 3^p,
    3^r C_V =3^r 2^A B_V
             <= (9/2)^(r+p).
In particular
    max(X,Y,|N|) <= 3 (9/2)^(r+p).                         (H)
The second line follows using the two critical prefix bounds; in the third line use 2^A<=3^(r+p)/2^s<=3^(r+p)/2^r. This deliberately avoids a false separate upper bound on A from criticality of the entire script.

Under the balanced clock hypothesis define d_j=j log3-S_j log2. Then d_j=o(j), and max_(j<=r+p)|d_j|=o(r+p) as p->infinity. The discrepancy of a prefix of V is d_(r+j)-d_r, also uniformly o(r+p). Thus the bounds
    B_U <= (r/3) exp(max_(j<=r)|d_j|),
    B_V <= (p/3) exp(max_(j<=p)|d_(r+j)-d_r|)
show both B_U and B_V are <= exp(o(r+p)). The formula 2^A=3^p exp(d_r-d_(r+p)) gives
    max(X,Y,|N|) <= 3^(r+p) exp(o(r+p)).                  (H_bal)
The empty U case is covered by C_U=0. These estimates concern the *unreduced* complete numerator, no hidden denominator cancellation.

## 3. The genuine three-place theorem

Use the following classical result: Schlickewei's p-adic Subspace Theorem, in J.-H. Evertse, *The p-adic Subspace Theorem*, May 2011, Theorem 1.1, with r=n=3 and S={infinity,2,3}; [source](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf). For linearly independent triples of algebraic-coefficient forms at each place and any fixed delta>0, the primitive integer vectors for which the product of the three absolute form values at all three places is <=C ||x||^-delta lie in finitely many proper rational linear subspaces. Algebraic coefficients at 3 may lie in the algebraic closure of Q_3. No effectivity is asserted. We apply it under the hypothesis that z is algebraic over Q. The source theorem is read at its stated fixed dimension, fixed places and fixed forms; no growing family of fields or forms.

At infinity and at 2 take the three coordinate forms. At 3 take
    L1=X, L2=Y, L3=z(X-Y)-N,
as linear forms in the three coordinates (X,Y,N). They are independent because the coefficient of the last coordinate in L3 is -1. At 3, X is a unit and |Y|_3=3^-p. At 2, |X|_2=2^-(s+A) and |Y|_2=2^-s; |N|_2<=1. Multiply all three places:
    product <= (X Y |N|) 2^-(2s+A) 3^-p 3^-m
             = |N| 3^-m.                                  (P)
This is the load-bearing cancellation: both clock monomials are S-units and their archimedean cost is cancelled exactly at the finite places. Ordinary Roth applied merely to the reduced denominator would lose this gain.

The common gcd of X,Y,N is a power of two, dividing 2^s. Divide by it to obtain primitive integer coordinates. The product of absolute forms is unchanged, by the product formula at infinity and 2 for powers of two (their 3-adic norm is one). Their primitive height is at least 3^p (the second coordinate after division is still divisible by 3^p), and no greater than the bound (H) or (H_bal).

Under the S1 condition m-kappa(r+p)>=c p for a fixed c>0 and all large i. Combining (P) and (H) therefore gives <=||x_primitive||^-delta for some fixed delta>0, after absorbing constants. Under S2, m-(r+p)>=(w-1)p-O(1), whereas (H_bal) loses only o(p) because r<=L p. Again a fixed delta works. The primitive heights tend to infinity, so a proper rational subspace contains infinitely many of these primitive vectors. There exist rational constants u,v,t, not all zero, with
    u X + v Y + t N = 0
on an infinite subsequence, since the same homogeneous relation holds on unreduced coordinates.

Now divide by X and take the limit in Q_3:
    Y/X=3^p/2^A ->0,
    N/X=z_i(1-Y/X) -> z.
Thus u+t z=0. If t=0 then u=0, and the original relation forces v=0 because Y is nonzero. Hence t!=0 and z is rational. By README theorem R1, an infinite critical script with rational coordinate is eventually periodic after the finite normalization of its dyadic denominator. This proves S1 and S2, including the transcendence claim for every nonperiodic such script.

Observe that for r=0, S1 already needs a repeat fraction strictly above log_3(9/2), not twice that threshold. For balanced scripts the strict threshold is one. All approximation signs and the primitive denominator have been retained.

## 4. Extracting repetitions from linear factor complexity

Suppose p_e(n)<=C n along infinitely many n, with C>=1 fixed; p_e(n) counts all distinct length-n consecutive factors of the one infinite gap script. If it is infinite the condition does not hold. In the first floor(Cn)+1 length-n factors two coincide, at starting positions i<j, zero-indexed, with d=j-i<=Cn and i<=Cn. The segment of length n+d beginning at i is periodic with period d: equality of the two length-n factors gives the required equality for every overlap index, even when d>n.

If d>=n/2, take V to be its first d letters, p=d. The segment length is p+n>=p(1+1/C), and p>=n/2. If d<n/2, take p=d max(1,floor(n/(2d))) (which lies between n/4 and n/2 in the d<n/2 case). The segment is also periodic with this p (all needed index comparisons follow by repeatedly shifting d), and its length is at least n>=2p. In either case p>=n/4, r=i<=Cn<=4Cp, and the segment repeats its length-p prefix to at least (1+1/(2C))p letters. Taking U as the initial i letters of the actual infinite script yields precisely the S2 hypotheses with a fixed w>1 and r/p bounded. This proof does not require disjoint occurrences of the repeated factors. S3 follows.

## 5. What this does and does not settle

The complete arithmetic split on the critical record tree is now:
* rational points: exactly the finite-prefix negative-periodic structure of R1;
* repetitive nonperiodic scripts of controlled clock height: transcendental, by S1/S2;
* in particular balanced algebraic irrational scripts must have superlinear factor complexity.

These statements apply to every coherent backwards word limit of one actual nonrepeating ordinary trajectory. However the compactness argument selecting such a limit does **not** force rationality, algebraicity, a stammering condition, balanced average clock, or uniformly bounded record gaps. Indeed the critical tree itself has dense negative rational periodic points and nonperiodic words; ordinary finite realizations of arbitrary critical words are available. The theorem is a structural restriction on the actual limiting coordinate, not a claim that a transcendental limit is impossible on an integer orbit.

The next truly load-bearing step would be an ordinary-source arithmetic theorem forcing a compact finite rational confinement of its critical limits, together with bounded gaps of records (R2), or an incompatible arithmetic/complexity constraint. The known phase equidistribution, sparse occupation, and finite-prefix integer trace estimates do not supply this. Nontrivial positive cycles remain a separate obligation. This is not a rephrasing of a conditional statement as a complete solution.
