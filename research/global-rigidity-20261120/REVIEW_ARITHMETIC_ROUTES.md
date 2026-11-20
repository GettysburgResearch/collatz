# Independent review: four arithmetic closure-route notes

**Reviewer:** pressure/operator route, independently reconstructing the
alternative-route proofs. **Verdict:** the stated density and algebraic
claims below are VERIFIED at the frozen bytes, with the shifted-product
scope correction incorporated. The proposed global closure hypotheses
remain OPEN. No integer counterexample or full Collatz proof is accepted.

## Frozen review boundary

All four complete proof notes were read and reconstructed. The final
shifted note was reread after the requested scope correction.

| File | Bytes | SHA256 |
|---|---:|---|
| `ADIC_REAL_DENSITY.md` | 11250 | `1bad5ff1f3e1e88dcc68fa44b8dd83b41883f556aac52f2e9e0f45e1ec73888e` |
| `FIXED_SOURCE_CLOSURE.md` | 10320 | `7924fbc896aaf8beceb69c66f7995e7c6cf4104a9a7929cad7cc501d775f3deb` |
| `FINITE_PLACES.md` | 5770 | `484f7e0f9b5a22e85bceec3b537336a705fc0365594303719ca8123c0d3c8c5b` |
| `SHIFTED_LINEARIZATION.md` | 6726 | `fb7fd7ad0643a49d06b290b3747a1f608a59a1fda941789c8ee8eca99c656cb0` |

The source-qualified reciprocal input is PR150,
`ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`,
`research/pointwise-closure-20261120/LOCAL_DISTORTION.md`, LD1--LD2.
I independently reconstructed that lemma in the preceding project pass;
its precise simple-path scope is retained here. No predecessor-basin
reciprocal bound is substituted for it.

## 1. AR1--AR2: verified joint tuning and nonintegrality

I independently composed a length-K prefix `w`, then `b` odd letters
and `a` even letters. With `F_w(x)=Ax+B`, the resulting map is

\[
 x\mapsto RA x+R(B+1)-2^{-a},\qquad R=3^b/2^{a+b}.
\]

This gives exactly the displayed numerator and denominator. The
positive real target requires `R -> x_*/(Ax_*+B+1)`, which is strictly
below `1/A`. Thus positivity is compatible with arbitrarily accurate
real approximation. Modulo `3^M`, taking `b>=M` removes the prefix and
gives `r=-2^{-a}`. The order of 2 is `2*3^{M-1}`, so every ternary unit
can be chosen by one congruence for `a`. Restricting `a` to that
progression leaves an irrational rotation in `b`; its cofinal dense
orbit gives simultaneous real tuning, with both exponents tending to
infinity. No effective uniform search bound is needed for existence.

The parity-legality argument is sound. The fixed points of all cyclic
rotations have an odd unreduced denominator, so all phases are 2-adic
integers. The edge identities then force exactly the advertised parity
at each branch. This addresses a real issue: an arbitrary real affine
fixed point would not by itself certify the parity itinerary. Positivity
and ternary units survive all phases of this actual rational cycle.

The score tends to `b*(8-5 log_2 3)` up to lower-order terms, and that
coefficient is positive by `3^5<2^8`. Compressing at odd phases has total
accelerated valuation equal to the shortcut word length, so a positive
lap score can be repeated legally. This proves infinite inverse score
at every odd phase, without requiring a primitive word.

The nonintegrality argument does not assume that positive integer cycles
are absent. The reduced denominator is preserved along every branch,
because it is coprime to six. At the phase `v/d` followed by `b`
consecutive odd letters, `2^b` divides the positive integer `v+d`.
For bounded root height, `v/d` is uniformly bounded, giving
`d>=2^b/(v/d+1)` and hence unbounded denominators. This excludes a
hidden denominator-one subsequence at sufficiently large `b`.

AR2 is the exact divisibility statement for `u-nd`: if the reduced
denominator is a unit at 2 and 3 and the difference is nonzero, its
numerator is divisible by `2^K3^M`. The resulting lower bound is correct.

**Scope:** this proves infinitely many changing noninteger rational
cycles in the joint real/binary/ternary neighborhood. It gives no
consistent all-time ordinary trajectory and no integer cycle.

## 2. FS1--FS4: verified exact threshold, with the global step still open

The identity

\[
 C-n(2^K-3^q)=2^K(n_K-n)
\]

and the odd denominator immediately give
`gcd(C,|D|)=gcd(n_K-n,|D|)`. Both local valuations and the reduced
denominator formula follow. After removing the 2- and 3-parts of the
nonzero endpoint difference, the normalized approximation cost is the
positive integer `|h_0|/g`. Thus beating one would indeed force an
actual return. The note correctly does not treat that exact threshold
as an estimate which has already been beaten.

For a hypothetical nonperiodic odd-unit orbit, I reconstructed

\[
 L_{j+1}-L_j=\lambda_j/3,\qquad
 \lambda_j(n_j+1)\longrightarrow L,
\]

using the pinned reciprocal budget only on the single simple ordinary
orbit. At an ordinary odd state with `s=v2(n+1)`, precisely `s-1`
accelerated gaps equal one before the first gap at least two. That
first defect is at least `lambda_j*(2/3)^s`. Therefore

\[
 (L-L_j)/\lambda_j\ge1+(2/3)^s>1
\]

is correct, including its strictness. It also supplies the stated
negative limit of the natural rational pins. This does not imply that
their real limit is a positive ordinary source or an integer.

For FS3, the primitive pair `(3^j,2^{A_j}n_j)` has local maximum norm
one at both 2 and 3. The unnormalized product of the specified forms
is exactly `(L-L_j)/lambda_j`; normalizing at infinity divides it by
`H_j^2`. I checked the primary Evertse source, *The p-adic Subspace
Theorem*, Theorem 1.1, page 1, including the displayed PDF:
[primary lecture notes](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf).
Its `r=n=2` specialization requires an unnormalized power saving
`O(H^{-eta})`, equivalently a normalized saving beyond `H^{-2}`.
The arithmetic floor therefore defeats this particular pair of fixed
forms. Algebraicity of `L` is separately unproved, as the note says.

The one-burst completion equation is also correct. Its 2-adic valuation
forces `b=v2(n_K+1)` when the number of final even letters is positive.
This is the number of consecutive **shortcut odd inputs**, whereas
the `s-1` above counts **accelerated valuation-one gaps**. The two
clocks are used consistently. If the endpoint is even, the equation
forces `b=0` and cannot realize a requested positive odd burst.

**Scope:** the pin and product identities are exact; an unrestricted
actual endpoint return, algebraicity of the limiting real constant,
and all positive cycle exclusion remain unproved.

## 3. FP1: verified additional finite-place control

Over a modulus `Q` coprime to six, both affine branches are permutations.
Their finite semigroup is a group, so inverses can be expressed by
positive words. With

\[
 A=E^{-1}O=3x+1,\qquad B=OE^{-1}=3x+1/2,
\]

the product `AB^{-1}` is translation by `1/2`. Its powers give every
translation, and `E^{-1}` supplies scaling by two. This proves exactly
the control action used in the note; it does not require generation of
the entire affine permutation group.

I checked the composition order. Appending `v` to `w` gives
`F_u=F_v F_w=E^{-a0}S`. Imposing the displayed exponent progressions
makes the final return map `E^{a0}F_u=S(x)=2x-z_Q`. The fixed-point
denominator is then `-2^N modQ`, a unit, and the numerator is
`-z_Q2^N modQ`. Reduction cannot introduce a denominator factor at a
controlled prime. Restricting `b` to a multiple of its finite order
still leaves an irrational rotation, so the real coordinate is tunable.

All observations are finite. A nontrivial denominator has its primes
outside the controlled set; this is not a rational integer at every
prime. The additional cost `d|r-n|>=2^K3^M Q` follows from the same
nonzero-integer argument as AR2.

## 4. Shifted linearization: verified after one scope correction

The exact increment

\[
 \lambda_{j+1}(n_{j+1}+1)-\lambda_j(n_j+1)
 =\lambda_j(2^{a_j}-2)/3
\]

does remove every valuation-one contribution. It is a real change in
the local cancellation, not an unexplained change of notation.

I checked the primitive normalization both when `t_j<=j` and when
`t_j>j`. With `k=min(j,t_j)`, the common divisor is exactly `3^k`;
the latter case has `q'_j=1` and still has a 3-part in `p'_j`. The
local product cancels this common 3-power correctly and equals

\[
 \mathcal P'_j=\frac{\mathcal P_j-1}{2^{s_j}3^{t_j}}.
\]

The first-defect lower bound is `3^{-s_j-t_j}`. The lower height bound
`q'_j>=2^j/(n_0+1)` is valid because `3^{min(j,t_j)}<=n_j+1` and
`n_j+1<=(3/2)^j(n_0+1)`. Thus primitive heights really diverge; common
ternary cancellation cannot invalidate the conditional Subspace
argument. If `L` were algebraic and the stated power saving occurred
infinitely often, the primitive pairs would lie in finitely many rational
lines, each with at most two primitive integral points. That is a valid
conditional contradiction. Both inputs remain open.

The bound for any fixed target `c!=L` is correct as well:
`2^{s_j}3^{t_j}<=n_j+1` gives a positive limiting lower bound for its
product. Changing the algebraic target with `j` would change the forms
and require a further coefficient-height argument.

**Correction requested and incorporated:** the earlier phrase that the
shifted pair had “no universal positive product floor” went beyond what
was proved for actual hypothetical escaping orbits. The final reviewed
note says that this identity no longer supplies the prior unit floor,
and explicitly refrains from refuting another actual-orbit lower bound.
The distinction is substantive. As a local algebraic control, a source
`2^s-1` for odd `s` has `s-1` gaps one and then gap two; appending a
**formal** all-one tail gives the shifted product exactly `3^{-s}`.
That demonstrates the algebraic scale, without constructing an actual
infinite ordinary continuation.

## 5. Independent finite arithmetic evidence

`review_arithmetic_routes.py` imports none of the author's Python code.
The two cycle reports supply only explicit prefix/exponent parameters.
The review script independently composes every entire word, reduces its
fixed point, and replays rational numerators through every branch with
constant denominator. It checks target neighborhoods, all local residue
conditions, score, denominator growth, and full modular slope/offset.
The ordinary-prefix and shifted-product checks are freshly generated
from smaller source ranges, with formal tails explicitly labeled.

Actual independent coverage:

- 12 rational cycles and 10,582 shortcut edges; the four extra moduli
  were 5, 91, 35 and 25.
- 7 diagonal ordinary-integer approximation costs, including the two
  compatible finite-place cases.
- 4,684 nonreturn natural pins and 40 actual-return controls, from
  sources 1 through 121 and 40 shortcut clocks.
- 1,971 primitive shifted products, 1,249 ternary cancellations and
  98 cases with `t_j>j`, from odd unit sources through 301.
- 1,859 first-defect floors whose required defect was present in the
  actual finite prefix; six separate formal-tail sharpness controls.

Normal and optimized executions produced identical output. The exact
commands were

```text
python -X utf8 -B review_arithmetic_routes.py --source-root /workspace/scratch/46eba7b29f50/agent-alternative-next
python -OO -X utf8 -B review_arithmetic_routes.py --source-root /workspace/scratch/46eba7b29f50/agent-alternative-next
```

Review script SHA256:
`b1b43094fcb745a2492995236a40c32757c46b36a90d741847c3d238858ac008`.
Report `arithmetic-routes-review-report.json` SHA256:
`ba81c3d5828e11d40d10d4861ebf4289e32705411113ccb6d91557fa0e1966dc`.

The author's broader finite reports are not silently relabeled as my
independent executions. Nor does this review claim a formal proof
assistant run, exhaustive software security review, or literature-priority
search. The all-precision statements depend on the reconstructed written
proofs, not the finite case counts.

## Final review boundary

The precise additions are the simultaneous rational density with growing
denominator, its finite-place extension, the exact ordinary-pin integer
threshold, and the two different adelic product formulas. The shifted
formula supplies a legitimate conditional closing route with two explicit
unproved global inputs. None of these results creates an ordinary
counterexample, forces a universal return, proves an escaping limit
algebraic, establishes the required product saving, or excludes
nontrivial positive cycles. Those limitations are present in the final
reviewed notes and are essential to this verdict.
