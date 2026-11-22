# Independent review: affine merger rigidity and its residual global target

Date: 2026-11-22. Reviewer: `global_certificate22`.

## Frozen scope and verdict

Reviewed exact local source bytes:

- `MergerClockRigidity.lean`, SHA256
  `4f7bff5ea23a750a3c784e12012c1ace0b862daac1f1301a4c1af1065355b497`.
- `AFFINE_MERGER_RIGIDITY.md`, SHA256
  `9369df6adef51506620cc39e1206290f4620db057a142273589c1816d90e87f2`.

**Verdict: VERIFIED at the displayed claim level by independent mathematical
and source review.** I reconstructed the correction bound, common-clock
offset argument, full residue-class continuation, arithmetic nonresonance
test, and the written sufficiency of the residual class `c=2 mod 3`.
No correction is required for those statements. This review is not a new
compiler execution; root's fresh compilation remains a separate event.

The verdict does not assert existence of the proposed universal merger,
review any later version, or extend to an unproved global stopping policy.

## 1. Padded correction and intercept bounds

For the actual shortcut orbit, the recursively defined correction satisfies

`2^h T^h(x) = 3^a x + c_h(x)` and `c_h(x)+2^h <= 3^h`.

The induction uses the actual first input bit and the actual suffix odd
count. Its recursion is correct: multiplying the suffix numerator by two
gives the old correction doubled and adds `3^(suffix odd count)` precisely
when the initial input is odd.

For `h<=H`, multiplication by `2^(H-h)` yields

`2^(H-h)c_h(x)+2^H <= 2^(H-h)3^h <= 3^H`.

The final inequality uses `2^(H-h)<=3^(H-h)`, not an unsupported relationship
between actual orbits. The denominator padding does not insert trajectory
steps.

Likewise the padded slope factor is at most `3^H`, since `a<=h`. Hence the
offset of the affine source `A*n+B` is nonnegative and is at most
`3^H B + (3^H-2^H)`. With `M=max(B,D)`, adding `2^H` gives the claimed
bound `3^H(M+1)` for both offsets. This does not require a bound on `A` or
`C`, and it remains valid when a leading coefficient is zero.

The integer-line argument is exact: if `L<R`, then `L+1<=R`, so an equality
`L*n+E=R*n+F` implies `n+F<=E`. Nonnegative `F` then contradicts
`n+2^H>3^H(M+1)`. The symmetric case is identical. Therefore the slope
equality is forced under the strict threshold. Equality at the threshold
is correctly left outside that implication.

## 2. The complete residue class really includes lower parameters

The ordinary lift starts at an actual natural source and adds
`2^h*(2^(H-h)*A*z)`. The existing `orbit_shift` theorem therefore supplies
all legal trajectories along the parameter progression; no parity word is
assumed solely from an endpoint congruence.

After the large merger proves an upward ray from `n`, write
`n=r+2^H*q`, with `r=n mod 2^H`. Express the observed mergers at `n` and
`n+2^H` using the same base `r`. Subtraction of their two affine equalities
forces equality of the slopes based at `r`, and either equality then forces
equality of the base endpoints at `r`. All values used are natural numbers;
there is no negative parameter extrapolation. The ordinary lift from `r`
now proves the whole nonnegative class, including parameters below `n`.

The interface `affine_merger_ray_iff` is also correctly bidirectional:
the forward direction uses the class members with parameters zero and one;
the reverse direction uses the exact actual-word shift formula.

## 3. Multiplier and coprime-divisor condition

If a divisor `d>1` of `m` is coprime to two and three, it is coprime to
`2^u*3^a` for all nonnegative exponents. The asserted resonance equation
would also make it divide that same positive integer, forcing `d=1`.
Thus the criterion is sufficient without requiring `d` to be prime.

For the affine pair the additional hypothesis `Coprime(d,A)` is essential
and is present. With it, `d` is coprime to the entire left slope, while
`d|C` makes it divide the right slope. The proof does not overstate the
convenient divisor criterion as a necessary criterion.

The concrete multiplier-five bound follows by taking `d=m=5`. Setting
`H=max(h,t)` in `n+2^H<=3^H` gives `3^H>n` for positive `n`, and therefore
the written strict logarithmic lower bound on the larger merger clock.
No merger existence is inferred.

## 4. The residual `6c+1` versus `c` class is sufficient for full Collatz

The written claim is correct with the explicitly stated universal merger
premise. Here is the reconstructed proof.

Proceed by strong induction on a positive input `n`. Even inputs halve.
For an odd input `n=4k+1>1`, two shortcut steps reach `3k+1<n`; one is a
base case. Every remaining odd input has

`n=2^r*w-1`, where `r>=2` and `w` is positive odd.

Its proposed partner `x=2^(r-1)*w-1` is positive and strictly smaller.
Put `B=3^(r-1)*w`. After their initial odd runs the two arms are `3B-1`
and `B-1`. Both are positive, and `B` is odd and divisible by three.

If `B=3 mod 4`, the known two-clock diamond joins the arms. If `B=1 mod 4`,
write `B=4c+1`. Then `B>=9`, so `c>0`, and `3|B` gives `c=2 mod 3`.
One shortcut step takes `3B-1` to `6c+1`; two take `B-1` to `c`.
The proposed merger on this restricted class therefore joins the original
input to its strictly smaller partner. Induction proves convergence.

There is a useful weaker sufficient premise: it is enough to establish
`Basin(c) -> Basin(6c+1)` for positive `c=2 mod 3`; an unconditional merger
is stronger. The smaller partner's known convergence gives `Basin(c)` by
the actual path. This observation does not discharge the premise.

For odd `c`, one target shortcut step is exactly `6c+1 -> 9c+2`. Thus the
new signed carry compiler applies directly to this genuine global target
when a complete certificate of `c` is supplied. It computes every finite
transport and preserves the source tail, but it does not prove the
remaining successful interval guard. In particular, this review does not
conflate a complete finite simulation with a total stopping proof.

## Limitations retained

The affine rigidity theorem controls what a sufficiently large observed
merger must look like and certifies its entire class once observed. It
does not produce an observed merger in every residual class, prove that
the remaining carry fits a lower-rank interval, or supply a common global
rank for the unbounded merger selector. Those are precisely the open
conclusions stated in the reviewed note.
