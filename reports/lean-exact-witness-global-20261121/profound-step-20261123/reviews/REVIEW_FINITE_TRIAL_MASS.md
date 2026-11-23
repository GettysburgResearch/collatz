# Reconstruction of the finite ordinary trial-mass interface

23 November 2026. **VERIFIED at the stated written scope.**

Source:
`research/lean-exact-witness-global-20261121/profound-step-20261123/COMMON_DISPLACEMENT_AND_FREE_ENERGY.md`

SHA256:
`867cca98da500a7b1be5c24e9185ac877b56c508be2a7da12436e9f3b0046abb`.

Reviewed scope: CF5--CF9, including CF7-F and the two normalization
controls. CF1--CF4 and the rest of the literature synthesis are outside
this review's verdict.

This reviewer authored the pressure entrance-law note and contributed the
finite upper-certification observation in CF7-F. The coordinating author
then supplied the explicit trial sigma_F. This report reconstructs the
displayed deductions; it is not an independent discovery of the shared
pressure input or external referee acceptance.

## Algebra and retained sources

1. CF5 uses the complete ordinary balanced bijection, not a formal
   transformation of an unrealized word. The factor 64^(-s) comes from
   r(Sq)=r(q)/64, and the remaining factor 2^(-s Delta) is the exact
   path-weight change. The direction of both factors is correct.
2. Define V=s log(2) Delta and nu(n)=r(n)^s/A. Then
   exp(-V(n))nu(n)=64^s r(Phi(n))^s/A. Summing over all ancestors
   gives R=Z_s(Sq)/Z_s(q), so the variational normalizer in CF6 has
   the stated orientation. On finite supports there are no undefined
   differences of infinite cost and entropy terms.
3. For finite nonempty F, set B_F=sum_F r(Phi(n))^s and
   tau_F(n)=r(Phi(n))^s/B_F. Directly expanding the finite relative
   entropy gives the CF7 identity with constant
   log A-s log64-log B_F. The constant has the correct minus sign
   before s log64. Positivity of all actual r values makes every
   term finite. Equality is obtained at tau_F.
4. The injectivity of Phi ensures that the finite list consists of
   distinct actual sources at the same fixed sibling. No multiplicity
   or changed-target gain is inserted into B_F.

## A finite certificate that does not evaluate infinite weights

The initial wording suggesting exact finite evaluation of the trial
objective was corrected in the reviewed source. Exact r and A still
contain infinite quantities. CF7-F instead uses the established bounds

`A<=zeta(s)<=1+1/(s-1)=s/(s-1)` and `r(n')>=c_*/n'`.

They give the displayed upper certificate

`log(s/(s-1))-s log(64 c_*)-log sum_F Phi(n)^(-s)`.

The explicit trial is also finite-data:
`sigma_F(n)=Phi(n)^(-s)/W_F`, where `W_F=sum_F Phi(n)^(-s)`.
For this trial, the expanded objective is

`log A-s log64+sum_F sigma_F(n) log(sigma_F(n)/r(Phi(n))^s)`.

The lower bound on r changes each logarithm to an upper bound
`-log W_F-s log c_*`; these bounds do not depend on n. Summing
with total probability one gives CF7-F for this particular trial.
Thus no unknown exact tilted weights are required to specify it.
The trial achieves the displayed upper bound in the inequality sense;
it need not be the exact optimizer tau_F.

## Closing implication and normalization controls

CF8 is the singleton case of CF7. CF9 assumes one fixed s>1 and
positive g(j) on its index set. An objective upper bound C+s log g(j)
implies `R_j^(1/s)>=exp(-C/s)/g(j)`. Summing on that same index set
contradicts the inherited root-summability theorem when its reciprocal
series diverges. Existence of these trial laws at the required scale is
correctly left open.

Adding a common constant c to V changes the normalizer by exp(-c)
and leaves the normalized tilt exactly unchanged. The actual empty-word
anchor is separately retained by the displayed two-part model:
for t in (0,1), epsilon=t^2 and factors 1,t give
`R=epsilon+(1-epsilon)t=t+t^2-t^3`. The root density is 1/R and
the other density is t/R<=1. Total variation is at most t. When a
root density exceeds M>1, the tail integral is t^2/R<=t<1/M.
Thus the uniform-integrability claim is correct. Both examples are
explicitly abstract controls on probabilistic hypotheses, not realized
Collatz constructions or counterexamples to sibling Harnack itself.

No additional execution or Lean coverage is claimed by this written
review. The infinite analytic source theorem and the universal trial
construction remain at their displayed separate proof boundaries.
