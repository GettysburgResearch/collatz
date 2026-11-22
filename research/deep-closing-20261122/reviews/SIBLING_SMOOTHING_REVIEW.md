# Independent review: exact sibling entropy cost

Date: 2026-11-22. Author: `deep_escape`; reviewer: `deep_cycles`.
Reviewed `collatz_work/deep_escape/SIBLING_SMOOTHING_ATTEMPT.md`,
Initial SHA256 `a46fc9a93bdba2e0848c87724c645845a039791cbc6d015b5b5ef1c91dea594b`.
The wording correction below was then applied; final reviewed SHA256
`07cfd3c6adf8a8b680d40c6c3ff9f0dad8f9e3231ab477e61d9a21454631e5f1`.
The later S9 control was reviewed separately below; final source SHA256
`0ad191c13b008818558330bdcb93304f9c5c0b8874804baa85531d494e4cc1da`.

**Verdict: VERIFIED for the elementary statements S2--S9.** The external
stationary-policy and occupation results in Sections 4--5 are outside
this review. The companion entropy result is reviewed separately.

For B(n)=64n+21, induction gives B^j(n)=64^j n+(64^j-1)/3 and hence
3B^j(n)+1=64^j(3n+1). The quotient is an odd positive integer, and
B^j(n)=n modulo3. This proves source legality, exact gap e+6j and the
same actual odd endpoint, rather than just a rational affine identity.

For d>0, first consider d prime to3: the first term d*63 in the
binomial expansion of (1+63)^d-1 has valuation2, while all higher
terms have valuation at least4. Cubing a number1+3^t u with t>=2
and3 not dividingu raises the valuation of its difference from1 by
exactly1. Separating d=3^s d_0 proves v3(64^d-1)=2+v3(d).
In the sibling difference, 64^j and3n+1 are ternary units and division
by3 subtracts one. Thus S4 follows. It also proves both distinctness
and exact period3^(m-1) modulo3^m, so consecutive uniform blocks
equidistribute on the entire fixed mod3 class.

The mean gap identity follows by expectation of the exact gap formula.
For a general nonnegative J with finite mean, min(J,L) gives refining
finite partitions. Their entropies increase to H(J); the geometric
maximum-entropy bound is uniformly at most Phi(1+EJ). Therefore H(J)
is finite with the stated bound, even for a countably infinite law.
Data processing gives the source residue bound. Finally
(a-1)log(1+1/(a-1))<=1, so Phi(a)<=1+log a. Exponentiation gives
S8 with its exact constants and no asymptotic approximation.

The calculation concerns this particular same-future sibling operation.
It does not preclude every different arithmetic smoothing construction,
and does not identify ancestor sampling with the future time law. Those
limitations are correctly retained in the source.

The added control S9 is also exact: substituting n=1 gives
(4*64^j-1)/3=(2^(6j+2)-1)/3. Thus3B^j(1)+1 is exactly2^(6j+2),
and the odd endpoint is1. The source laws are uniform on complete
odometer periods at every ternary precision, while their image is
the point mass at1. This refutes blanket forward entropy transfer
for same-future source averages, without refuting a hypothetical
additional result specific to escaping components.

Applied wording correction only: in the S4 proof, identify 64^j and
3n+1 explicitly as units, then account for the division by3. Calling
all the 'outside factors' units could otherwise be read as including
1/3. The displayed valuation and subsequent conclusions are correct.
