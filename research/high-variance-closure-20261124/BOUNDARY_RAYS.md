# Actual ordered boundaries under dyadic subdivision and ternary transport

**Status.** Written positive ordinary theorems and an unresolved global rigidity attempt. These statements apply to the indicator f of *any* union of ordinary shortcut components, and hence to the indicator of reaching one. They do not assume convergence. A boundary is an integer n≥1 with f(n)≠f(n+1). Its orientation is the ordered pair (L,R)=(f(n),f(n+1)).

## 1. One persistent address per ordinary boundary

The exact identity f(2n)=f(n) implies exactly one of 2n,2n+1 has the same oriented boundary: use the color of 2n+1 between the endpoints 2n and 2n+2. Iteration gives n_(j+1)=2n_j+d_(j+1) and f(n_j)=L, f(n_j+1)=R at all clocks. The nested closed intervals [n_j,n_j+1]/2^j select a real α, with the indicated binary expansion even at an ambiguous dyadic endpoint. If a least nonconverger q exists it is odd, q+1 reaches one since (q+1)/2<q, and q is one such initial boundary.

The binary path has no substring 10(11)^s0, s≥0, that ends at a monitored boundary. Indeed the corresponding n equals 2^k u−2 for k=2s+1 and u≡3 mod4. The path from n halves once and then makes k−1 successive odd steps, reaching w=3^(k−1)u−1. From n+1 the k successive odd steps reach 3^k u−1=3w+2. Here w=2a with a odd, so w and 3w+2=2(3a+1) have the common future (3a+1)/2. This includes k=1 with an empty odd run on the first arm. All values and paths used are ordinary.

After a newly observed 1, successive zeroes must be separated by an odd number of ones: if a pair of consecutive zeroes had an even gap of ones, the first such pair following a 1 produces the forbidden substring (the gap zero case is included). Consequently all zero positions in the resulting tail have the same parity. There is no restriction needed for a tail consisting entirely of ones; a path with no new 1 is eventually zero. In base four, the nondyadic tails have one compulsory 1 bit in every digit, at the same parity throughout. All possible addresses consequently lie in a countable union of affine copies of base-four two-digit sets, of Hausdorff dimension at most 1/2, together with dyadic points. This concerns future addresses of the actual boundaries. It does not assert a 1/2 counting exponent for the full set of present-day boundaries.

## 2. Tripling transfers at every zero

Consider a nondyadic address, with infinitely many zeroes and ones. At a sufficiently late zero position k, n=n_k ends in 10. Both n/2 and n+1 are odd. Since f(3u+1)=f(u) for odd u,
    f(3n+2)=L,           f(3n+4)=R.
Thus M=(3n+2)/2 is an ordinary boundary of the *same orientation*. Let t=2^k α−n. Its future digits include a 1 in every odd position, so 2/3≤t<1. Consequently
    M=floor(2^(k−1)·3α).
No continuity, frequency or averaging hypothesis enters this pointwise transfer.

If successive zeroes are 2s positions apart, the intervening digits are 2s−1 ones and a zero, giving
    n'=4^s(n+1)−2,       M'=4^s M+2^(2s−1)−2.
Thus the digits appended to the transferred index are 0, then 2s−2 ones, then 0. In particular there is an unmonitored intermediate level even when s=1. After choosing its parity, the binary digits of 3α are eventual equal pairs: write the original fractional tail as 1−C or 1−2C with C in the base-four 0,1 Cantor set. Multiplication of C by 3 produces base-four digits 0,3 without carries. Complementation and a one-bit shift preserve eventual equal pairing. Were 3α *itself a persistent boundary address at every sufficiently fine level*, the no-00 property in section 1 would then force a dyadic endpoint. The displayed exact transfers occur on selected levels; the missing intermediate persistence cannot be inferred from nested oriented endpoints alone.

## 3. Inverse ternary transport recurs at every third zero

Whenever n≡1 mod3, A=(4n−1)/3 and A+1 form a boundary of the same orientation as n,n+1. Indeed A is odd with shortcut 2n, while A+1=2(2n+1)/3 halves to the odd integer (2n+1)/3 whose shortcut is n+1. The identity is reversible: for every l≥0 the oriented jump at 4l+1 is exactly the jump at 3l+1.

For two successive zero indices n,n' above, n'≡n−1 mod3. The residues thus cycle through 0,1,2 independent of all run lengths. At every third zero n≡2 mod3; let m=n/2=n_(k−1)≡1 mod3. Its next binary digit is zero. Inverting the two arms gives A=(4m−1)/3=(2n−1)/3, and
    A=floor(2^(k+1)·α/3).
Indeed the remainder at level k−1 is in [0,1/2), so (4m+4t)/3=A+(1+4t)/3 with 0≤t<1/2. This provides same-oriented boundaries at α/3 on infinitely many actual levels, independent of the frequency of zeroes. Such a boundary need not descend persistently from the two ordinary integers surrounding α/3 at level zero. For α originating at a hypothetical least q, those two integers are smaller than q and have the same color when q>2.

## 4. Actual births on the tripled address

At any consecutive zero pair separated by 2s with s≥2, the transferred M' ends in 10. Its unique same-oriented child is 2M'+1, since 2M' ends in 100 and hence has no boundary. If there is a subsequent zero, however, the next transferred binary segment starts with a zero. Therefore the later transferred boundary lies in the monochromatic *left* half of M', and does not descend from M'. A new pair of opposite jumps is born there after that split. This explicitly disproves the proposed automatic propagation even on the actual path, conditional on those successive gap events. A transfer argument must account for those births, or obtain a contradiction from their recurrence. Distinct lost transfers can create further persistent boundaries; the current argument gives no scale-uniform lower bound on the intervals between such creations or on the mass supported by the new paths.

A separate terminal possibility also survives the address analysis. An all-ones continuation from a boundary n compares 2^h(n+1)−1 to 2^h(n+1) for all h. Equivalently f(3^h(n+1)−1) stays opposite f(n+1) throughout that tail. No argument here forces equality at some h. A finite window can be arbitrarily long without forming that infinite ordinary scenario.

## 5. Exact action on a terminal right-sided boundary

Suppose b is a positive odd integer prime to three, f(b)=L, and f(2^k b+1)=R≠L for every sufficiently large k. Dyadic scaling gives the same statements at b/2^u, so write the center simply as b. The point b/3 then has an actual persistent, alternating boundary ray beginning at a finite level. Indeed choose all sufficiently large j with B=2^j b≡1 mod3, which occur every two clocks, and put n=(2B−2)/3. The integer n ends in 10, and section 2's exact integer identity gives g(n)=g(B) with the same orientation. These n are the zero-position floors at b/3. The next is n'=4n+2. At the intermediate index 2n+1 the left color is f(4n+2)=L and the right color is f(n+1)=R. This fills every intermediate level and proves persistence for this particular inverse dilation.

A second inverse dilation admits **an exact nonpersistent local pattern**. At b/9, for every sufficiently high k the two endpoints of the dyadic cell have ordered colors
    (L,R) if 2^k b mod 9 is 5 or 7;     (R,R) otherwise.
This is two consecutive clocks out of six. In particular there can be actual transfers at b/9 arbitrarily late even though its full cell is monochromatic at four clocks in every period.

To prove it, first note T²(4a+1)=3a+1. The prescribed right germ at b, on even and odd k separately, gives f(3^h b+1)=f(2·3^h b+1)=R for all large h. Since 3^h b+2=T(2·3^(h−1)b+1) for h≥1, it too has color R. Write r=2^k b mod9, ranging over 1,2,4,5,7,8. The two floor-cell endpoints are (2^k b−r)/9 and (2^k b+9−r)/9. Their first k parities are those of the small signed rational seeds −r/9 and (9−r)/9 (ordinary parities of rationals of odd denominator are taken from their numerators). At clock k the endpoint is 3^(p−2)b + T^k(seed), with p the seed's number of odd inputs. The negative seeds −5/9 and −7/9 have precisely two odd inputs and reach zero. The remaining four negative seeds and all six positive seeds reach positive integers in the 1,2 cycle, consequently p increases without bound and their ordinary lifted colors are R. In the listed order of r, the first (clock, odd count, entry) triples for the negative seeds are (2,2,1), (3,2,1), (4,2,1), (2,2,0), (3,2,0), (5,2,1). For the positive right seeds they are (6,2,1), (6,4,2), (4,2,1), (5,2,1), (4,2,1), (3,2,1); the proof requires only the trajectories of these twelve small seeds, not any unspecified positive convergence.

More generally the only unit residues 0<r<3^d whose signed seed −r/3^d hits zero, for d≥2, are 3^d−2^d and 3^d−2^(d−1). To see this, the inverse signed odd path back from zero first reaches −1/3. Write t for the absolute value in (0,1). A further reverse odd transform, including intervening even inverses, sends t to (1+2^e t)/3 for some e≥1. From t=1/3 the only choices are 5/9 and 7/9. Both exceed 1/2, after which only e=1 keeps t<1 and no final doubling is possible. The two closed forms follow. The inverse run never goes beyond t=1 since it could not return across that absorbing barrier. Statements about the colors attached to the other seeds for general d would require their entry to the positive cycle or an independent alternative; the d=2 conclusion above uses the finite exact table only.

## 6. A signed transport test with a fixed ordinary source

For each original integer interval [a,b] and every h, the telescoping sum of oriented jumps at the 2^h(b−a) descendant edges equals f(b)−f(a) exactly. Thus the signed sum retains an original ordinary boundary at unit strength. An opposing pair born inside a parent of equal color has total signed charge zero forever. At a trit head write Δ(x)=f(x)−f(floor(x/81)). Testing Δ against the constant function only gives
    sum_(x in H_j) Δ(x) = G_j−81G_(j−1),
where G_j counts convergent-color points in H_j. The *absolute* cut count instead has the exact dual test
    sum_(x in H_j) |Δ(x)| = sum_(x in H_j) Δ(x)(1−2f(floor(x/81))).
Thus a useful signed bound must permit the actual, scale-dependent parent color as a test function. Smooth weak tests or the exact dyadic identity above do not supply it. Indeed the elementary doubling-invariant coloring f₀(n)=1_{3 divides n} has uniformly bounded signed head discrepancy over the levels (zero at all high levels) and a positive proportion of disagreeing head edges at every high level. Its whole dyadic descendant identity holds identically. This diagnostic coloring violates the odd shortcut identity and is not a Collatz counterexample. It pinpoints what the additional true arithmetic transport must accomplish.

There is an unconditional one-sided detection property for the real Collatz coloring: inside the ternary descendants of *every* fixed bad head parent there is a genuinely good child of a bad parent. Powers of two reach one, and irrationality of log_81(2) puts their normalized values in the interior of any fixed rescaled head cylinder infinitely often. Compare a good vertex there with its bad starting ancestor and take the first change along the finite chain. If a bad source b exists, its dyadic multiples similarly force a good-to-bad transition below every fixed good head parent. This is pointwise and retains the original head cell, but the hitting level is not uniformly bounded as the cell shrinks. Opposing births cannot cancel either transition on its own path. No quantitative bound on the scale-dependent signed dual test follows, and color agreement would not itself establish a common future for two inputs from different nonconvergent components. The closing bound for the actual PR197 failed edges is open.

**Finite formal scope.** `lean/OrientedBoundary.lean` verifies the unique-child color dichotomy, both oriented adjacent transfer identities and the full unbounded forbidden even-gap family from the two elementary ordinary color identities. The Cantor geometry, transfer timing and terminal calculations are written proofs.
