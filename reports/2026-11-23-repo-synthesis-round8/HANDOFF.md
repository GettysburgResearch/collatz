# Next-pass calculation: a sharp threshold inside one block family

23 November 2026. Reported by the ordinary-selector lane after its
science files were frozen. **This is a proposed follow-up calculation,
outside the current reviewed and Lean-compiled claim scope.** No
additional controls or universal selection theorem are claimed here.

For the literal blocks L=(2,1) and P=(1,4), the lane reports that the
whole ordinary word family `L^m P` has a sharp descent/expansion split:

\[
m\le10\Longrightarrow r<q,\qquad
m\ge11\Longrightarrow r>q.
\]

The proposed complete source class is

\[
q=2^{3m+1}(u_m+32z)-7,\qquad z\ge0,
\]

where `u_m=13*9^(-m-1) mod 32` is the representative in
`{5,13,21,29}`. Its endpoint is

\[
r=\frac{9^{m+1}(u_m+32z)-29}{16}.
\]

The reported proof uses the complete affine identity already verified
in R8-O3, together with q>=73 for m>=1. The slope is
`A_m=(9/32)(9/8)^m`. Its adjacent threshold values are

\[
A_{10}=\frac{31381059609}{34359738368}<1,
\qquad
A_{11}=\frac{282429536481}{274877906944}>1.
\]

For the descending range the proposed estimate is
`r-q<=(80*A_10)-1197/16<0`; m=0 is P directly. In the expanding
range the positive affine remainder gives r>q. A next pass should
reconstruct the completeness of the source class, prove the inequalities,
and decide whether this resource threshold helps a larger actual carry
return system. Merely checking longer blocks in the same two-block
subsystem would not settle arbitrary denominator-eight carries.

The principal open target remains a successful triadic construction
for the actual scalar of one arbitrary fixed positive ordinary source.
This finite-family threshold does not provide it.
