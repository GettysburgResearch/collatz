# Independent review: integer-cycle residual degree

Date: 2026-11-23. Reviewer: `/root/risk25_endpoint`.

## Frozen object and verdict

Reviewed file:
`/workspace/scratch/957bb0caa6f2/risk25/cycles/INTEGER_RESIDUAL_DEGREE.md`.

SHA-256:
`d92b1dd9c6da48459dad86a918b1a639f98c43aac8b6610157efd956b7a84b2a`.

**Verdict: VERIFIED as a written necessary-condition theorem for every
primitive positive integer odd cycle, with the stated external-input
qualifications.** I found no gap in the actual-polynomial root argument,
the reduced-clock use of Matveev, or the combination with the pinned
ordinary count. This review does not certify the entire preceding PR185
factor-gap proof, and it does not verify a positive-cycle exclusion.
The exponential denominator consequence retains that separately supplied
factor-gap theorem as its premise.

The main reviewed conclusions are:

\[
 e(m)\le d\Lambda/p,\qquad
 m<C_m d^{K_0+1},\qquad
 d\ge c p^{1/(1+(K_0+1)\theta)}.
\]

These concern unrestricted primitive positive integer cycles, not a fixed
word schema or a bounded list of periods. The constants are absolute and
effective, but extremely weak.

## Reconstruction of the actual polynomial step

1. From the supplied integer cycle, put `v_j=2^(s_j)*x_j`.
   The edge equation gives `v_(j+1)=3*v_j+2^(s_j)`. Direct coefficient
   comparison yields `(X-3)H=Q+x_0F`, including the constant term:
   `2^(s_(p-1))-2^A*x_0=-3*v_(p-1)`.
   Thus the sign in (IR3) is correct.

2. `F(3)!=0` because `2^A!=3^p`. Consequently the common polynomial
   factor `G` is coprime to `X-3`, so (IR3) gives `G|H`. Since `G` is
   monic integral, the quotient `J=H/G` is integral. Its degree is
   `d-1` and leading coefficient is the actual starting state `x_0`.
   For `p>=2`, the two leading coefficients `x_0,3*x_0+1` indeed make
   `H` primitive, and Gauss's lemma then makes `J` primitive.

3. The positive-coefficient root lemma is correctly oriented. If
   `t=min(c_(j+1)/c_j)`, the ascending coefficients of `P(tz)` are
   nonincreasing. In the displayed identity for `(1-z)f(z)`, the sum
   of the absolute values of all subtracted terms is strictly less than
   `a_0` when `|z|<1`; the last coefficient is positive. This excludes
   roots there. Applying the same lower bound to the reciprocal
   polynomial gives the upper bound. The proof does not need a
   separate, unverified root-location theorem.

4. Applying this to `H` gives the annulus
   `[3+1/M,3+1/m]`. Omitting the last cycle edge from the adjacent
   coefficient list causes no problem: the full-cycle minimum and
   maximum are valid outer bounds for the ratios that are present.
   Every root of `J` is a root of `H`, with multiplicity, since `H=GJ`.

5. Every root of `G` has the common modulus
   `r=2^(A/p)`. Its constant-term modulus is therefore `r^(p-d)`.
   The final actual cycle edge gives, exactly,

   `abs(J(0))/x_0 = r^d/(3+1/x_(p-1))`.

   The product of the `d-1` root moduli of `J` lies between the
   corresponding powers of the two annulus radii. Taking logarithms
   gives precisely (IR8), with `d*tau-e(x_(p-1))` in the middle.

6. Odd rotation preserves the monic gcd degree. The stated identity
   `2^(a_0)*Q_next=XQ-F` is correct, and multiplication by `X` is a
   unit modulo `F`. Rotation can therefore place the minimum at the
   predecessor position without changing `d`. The lower half of
   (IR8) then implies (IR9). When `d=1`, the empty root product is
   handled correctly: it forces every predecessor state equal, so a
   primitive positive integer odd cycle is the one-state cycle at 1.

This is an actual-cycle argument. It would be invalid to use arbitrary
positive-coefficient `Q` without the orbit polynomial `H` and the exact
identity (IR3). The file does not make that substitution.

## Reduced clock and the external logarithm estimate

I opened Matveev's original English PDF through the stable MathNet
endpoint and inspected printed page 1219, including a screenshot of
Corollary 2.3 and its hypotheses:

<https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng>.

The statement bounds the logarithmic linear form itself, so the note
does not confuse it with a bound for a multiplicative expression minus
one. With the real field `Q`, `n=2`, `D=1`, heights `log 2,log 3`, and
`B*=max(a,b)<=2b`, its coarse branch permits `C_1(2)<=2^32`.
Both height parameters exceed the required `0.16`. This gives
`log L > -K_0 log(2 e b)` and hence (IR15) exactly. No parameter
dimension or algebraic height grows with the unreduced period.

Independently, the proof that `b|d` is valid: the monic integer
polynomial `F_0` has nonzero constant term of modulus `2^(ad/b)`.
Raising to the `b`th power and taking the 2-adic valuation gives
`b|a*d`; coprimality of `a,b` gives `b|d`. The cycle product also
gives `a<=2b`, because every state is at least one.

Finally `tau=Lambda/p=L/b<=1/(3m)`. Combining this with (IR15)
gives `m<(3c_0)^(-1)*b^(K_0+1)<=C_m*d^(K_0+1)` in the stated
direction. This reduced denominator is what makes the argument say
something about `d`; replacing it by the unreduced period would not
give the same theorem.

## Distinct-state and global-count consumers

The elementary first consumer uses only `p` distinct positive integer
states. After sorting them, their reciprocals sum to at most `H_p`.
Thus `Lambda<=H_p/3`, while `e(m)>=1/(4m)`. These inequalities and
(IR9) give (IR11), and substitution of the minimum upper bound gives
(IR17). This stand-alone result is valid without the newer global
count.

For the sharper version I read, at its full pinned head,

`PR182 a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
`research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`.

I reconstructed its compression and counting argument. Its domain is
an injective forward-invariant set of ordinary positive odd integers.
A finite primitive cycle is exactly such a set: `U` is a permutation
of its distinct states. There is no summation over repeated cycle
traversals. The equal *odd* clock in the compression step is essential
and is retained. The binomial upper-tail estimate has a fixed slope
strictly between `1/2` and `1`, so its constants can be made absolute
and effective.

For the finite cycle, Tonelli's identity

`sum_i 1/x_i = integral_m^infinity F_S(t) t^(-2) dt`

is exact. Bounding the logarithmic denominator below by its value at
`m`, and integrating `t^(theta-2)`, gives (IR19), including the
factor `1/(1-theta)`. Combining with `1/(4m)<=d*Lambda/p` yields
(IR20). Inserting `m<C_m*d^K` and discarding only the denominator
`sqrt(1+log m)>=1` gives (IR21). No hidden upper bound on `p`, `m`,
or the word alphabet enters this argument.

## Boundaries that remain material

- The root-product inequality itself also applies to positive rational
  cycles. Its integer-specific consequences use distinct *integer*
  states and the ordinary count. The file separates these inputs.
- The all-word factor-gap inequality `abs(F_0(3))>(3/2)^(d-1)` is
  retained as a source-qualified PR185 result. I checked the algebraic
  use of it, not its entire original Matveev/cyclotomic certificate.
- A primitive odd cycle gives a primitive shortcut parity cycle; a
  proper repeated shortcut block fixing the state would already have
  its positive affine iterate fix that state after one repetition.
  Thus the primitive-word scope of the inherited factor-gap theorem is
  compatible with the consumer here.
- `Q_0(3)=-mF_0(3)` remains the required distinguished ordinary
  divisibility. The new lower bound for the size of `F_0(3)` does not
  bound its numerical gcd with `Q_0(3)` from above.
- Even a future effective lower bound such as `log m>=c d` would
  first reduce the problem to finite residual degree/period ranges.
  The present note does not claim to have excluded all those ranges.

No change is required for the reviewed theorem. I did not run the lane's
finite control script or a Lean compiler as part of this independent
review. The evidence here is a direct reconstruction of the unbounded
written argument, the independently inspected pinned count, and the
primary Matveev statement. The review does not extend to later edits.
