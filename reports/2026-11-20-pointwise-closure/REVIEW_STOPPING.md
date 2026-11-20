# Independent reconstruction of the stopping-burden packet

Reviewer: the separate `alternative_global` agent, 20 November 2026.

Reviewed files: `agent-pressure/STOPPING_BURDEN.md`, `agent-pressure/check_stopping_burden.py`, and the final self-contained appendix `agent-pressure/LOCAL_DISTORTION.md`. The two suggested clarifications below were sent to the author, applied, and subsequently read back by this reviewer. The final local appendix and revised SB5 were then independently reconstructed. This is a mathematical reconstruction and a bounded independent invocation, not formal proof checking or an external referee verdict.

## Final reviewed bytes

The following table identifies the final reviewed files exactly. Paths are relative to the shared task staging directory `/workspace/scratch/46eba7b29f50`; the integration report maps these files to their repository destinations. The verdict below applies to these bytes and does not automatically cover later changes.

| Staging path | Byte length | SHA-256 |
|---|---:|---|
| `agent-pressure/STOPPING_BURDEN.md` | 9,280 | `07fb725bec1f9d31e2f64abab8731ecded2a4e7be04a0f5e6b3696dfe1dd6174` |
| `agent-pressure/LOCAL_DISTORTION.md` | 4,511 | `824c2587fcdc723bd07a0aff1635dcc968ebbacd8009d6ec630f163d00a8a5ec` |
| `agent-pressure/check_stopping_burden.py` | 6,004 | `537a3d105ccae6c6a027989eae175443820c83448c83377bd30a7e228aee6c84` |

## Verdict

**VERIFIED WITH CLARIFICATIONS at the narrow written-claim level; the clarifications have been applied.** SB1–SB5 follow by elementary arguments on their specified positive odd ternary-unit domain. SB5 now uses a self-contained local reciprocal-packing proof, separately reconstructed below, instead of relying on an imported qualified input. None of these claims proves that `W(1)` is finite or proves convergence of an unverified source.

The examined potential definition is PR #149 at `92c0129e794dde3ec55ceec470a12d51ba3f7e2f`, `research/forward-inverse-defect/CLOSURE_BOUNDARY.md`. The initial uniform distortion reference was PR #145 at `dd245a712f985909f541590e3f6c179b7ba011e4`, `research/native-pressure-20261118/ORDINARY-DENSITIES.md`, section “Uniform distortion of simple paths.” I inspected both exact source files. The final stopping packet instead supplies the independent local proof below. I did not re-prove the stronger translated packing argument in the historical source; it is not needed for the final constants.

## Reconstruction

### SB1: the supremum really is over first-hit basin paths

For a positive odd unit target, every integral `I_g(t)=(2^g t-1)/3`, with `g>=1`, is a positive odd integer. The potential retains only unit intermediates and endpoints. Every resulting inverse word from 1 reverses to a deterministic positive ordinary odd orbit ending at 1. Once its forward trajectory first reaches 1, all remaining accelerated steps are repetitions of `U(1)=1`, each with valuation 2. Therefore `k=a+r`, `A=d+2r`, and its score is precisely `8a-5d-2r`. Conversely, every first-hit path from an odd unit stays in the units and reverses to an admissible word. Both inequalities in the supremum identity hold. The empty word supplies zero, so `W(1)>=0`.

No assertion about all starting integers is needed: the equality ranges over starts already known, as a mathematical condition, to reach 1.

### SB2: the ninth-power distortion bound

The odd inputs before a first hit are distinct and exclude 1. A repetition would trap the deterministic orbit in a cycle before its first hit. Starting from an odd unit, every later odd value remains a unit because `3u+1` is coprime to 3 and division by 2 preserves this property.

The sorted admissible values are bounded below by `5,7,11,13,...`, whose `i`-th value is at least `3i+1`. Thus

\[
 \log D\le\frac13\sum_i\frac1{u_i}
 \le\sum_{i=1}^{a}\frac1{9i+3}
 \le\int_0^a\frac{dx}{9x+3}
 =\frac19\log(3a+1).
\]

The integral comparison has the correct direction since the integrand decreases. Exponentiation proves `D^9<=3a+1`; every factor is at least 1. The empty path at 1 gives equality. Multiplication of the exact odd step equations proves `2^d=3^a nD`, so the score identity follows with `delta=8-5 log_2 3>0`.

### SB3: uniform logarithmic burden, only on the actual basin

The inequality is `delta a<=5 log_2 n+B+(5/9) log_2(3a+1)`. An elementary linear domination of the final logarithm first yields `a=O_B(1+log n)`. Substitution back gives the stated leading coefficient and logarithmic correction. For `d`, the correction coefficient is indeed

\[
 \frac{\ell C_a+1}{9}=\frac{C_d}{9},
\]

and the leading coefficient is `ell C_a+1=C_d`. The converse with a bounded additive error, rather than a logarithmic correction, follows from `D>=1`; the note correctly retains the gap between the two directions.

The all-positive-integer extension of the *leading constants* is also sound. If `n=2^v q` with q odd, the even prefix costs v steps while `log_2 q=log_2 n-v`; since `C_d>1`, this is absorbed. For an initial odd nonunit q, after its first odd event with valuation g the unit target is `t=(3q+1)/2^g`. Then `a(q)=1+a(t)` and

\[
 g+C_d\log_2t
 =C_d\log_2(3q+1)-(C_d-1)g
 \le C_d\log_2q+O(1).
\]

This does not extend the exact unit-domain formulas unchanged to an arbitrary initial source.

### SB4: deadline and membership decision

Multiplying the clock inequality by nine and exponentiating gives exactly the weak reverse of (8). The left/right ratio in (8) has successive quotient

\[
 \frac{2^{72}}{3^{45}}\left(\frac{3a+1}{3a+4}\right)^5.
\]

The second factor increases with a, and the exact check at a=10 is strict. The exponential base exceeds 1, so a crossing exists and every later integer remains beyond it. Hence a convergent unit input must have `a<L_B(n)`. Running for that many odd events is a finite procedure. Failure to hit is a valid rejection **conditional on a known valid global bound B**. It is not an unconditional rejection, and the observed sample maximum is not such a bound.

At n=1 the actual first-hit clock is zero; the positive deadline is merely conservative. For `B<0`, the premise `W(1)<=B` is impossible because of the empty word. Such B should be rejected at the procedure's input, rather than silently interpreted in the integer-shift implementation.

**Clarifications applied and read back:** B is explicitly a nonnegative integer; the direct deadline algorithm is on `n in S`; arbitrary positive n is first normalized to a unit and that unit's deadline is used. The public `deadline`/`exceeds` functions now validate their integer domains. I independently exercised negative B and zero n: both are explicitly rejected with the intended domain errors. The deadline at `(n,B)=(1,0)` is 55; the first hit is still zero. These changes concern domains and usability, not a missing inequality.

### LD1–LD2: the final self-contained reciprocal budget

For a finite simple shortcut path and a shell `[Y,2Y)`, let `h=floor(log_2 Y)` and discard the final h positions. For every remaining position, the h-step image stays inside the simple segment, so images at different indices are distinct. This truncation is essential and is supplied correctly.

A parity word with q odd inputs has affine remainder at most `(3/2)^q-1`, by moving all zeros before all ones. There is one source residue per parity word modulo `2^h`. For `q>3h/5`, exponential Markov weighting with `r=3/2` bounds the number of words by `(3125/108)^(h/5) <= 2^(49h/50)`. Each residue has at most two representatives in the shell, giving the high-lane contribution `2Y^(49/50)`.

For the remaining lane, every image is a positive integer at most `5*3^(3h/5)<=5Y^(49/50)`. This is one common interval for all low weights q; no extra summation over q is needed. Injectivity gives that same source-count bound. Adding at most `h<=Y^(49/50)` discarded states proves the shell count `8Y^(49/50)`. The h=0 case is also valid.

Summing the resulting reciprocal estimates over dyadic shells yields `8/(1-2^(-1/50))<600`. I separately evaluated the equivalent exact integer comparisons

```text
5^50 < 3^30 * 2^69
3^30 < 2^49
75^50 < 2 * 74^50
```

All three returned true. The first is algebraically identical to the appendix's `3125^10<108^10*2^49`. The scalar checks certify the numerical comparisons, while the argument supplies the assertion for every finite simple path. Consequently `log_2 D <= 200/ln 2` follows from `ln(1+t)<=t` without a harmonic-trace, stationary-law, or convergence input for arbitrary sources.

### SB5: the resulting elementary equivalence

Given a uniform `log_2 D<=D_*`, rearrangement of the exact score yields

\[
 \delta\left(a-C_a\log_2n\right)
 =(8a-5d)+5\log_2D.
\]

The two bounded suprema are therefore equivalent. The final local appendix gives `D_*=200/ln 2`. If `W(1)<=B`, it follows that

\[
 a\le C_a\log_2 n+(B+5D_*)/\delta.
\]

Substitution into `d=ell a+log_2 n+log_2 D` gives the stated remainder `(ell B+8D_*)/delta`, because `5ell+delta=8`. The improved bounded-error equivalence is thus unconditional as a reduction; its boundedness premise remains open. The stronger historical constant is properly identified only as a comparison.

## Actual execution

I separately ran:

```text
python -X utf8 -B check_stopping_burden.py --limit 10001
```

It exited zero and reported 3,334 unit-source first-hit comparisons and exact distortion checks, 257 direct rational products, 7,392 inverse words with depth at most 7 and gap at most 10, and 201 conditional deadline checks. The maximum observed score was zero. This is bounded evidence; it gives no global score bound.

The verifier uses explicit `require` checks rather than Python assertions. Its two forward clocks are implemented separately. The inverse-word checks only call unbounded odd replay for constructed ancestors whose finite path is already provided by the inverse construction. The ordinary sampled inputs are first required to terminate under the bounded shortcut implementation.

## A safe connection to sparse-return bounds

The sparse-return result in `SPARSE_RETURN_SPECTRUM.md`, SR-4, can be applied to the `a(n)+1` distinct odd states of a first-hit path, including 1. If `W(1)<=B`, SB3 then implies that, for each fixed S,

\[
 \#\{\text{first-hit odd states with popcount}\le S\}
 =O_{S,B}\bigl((1+\log n)^{1-1/S}\bigr),\qquad S\ge2.
\]

This is a conditional bound in terms of the source, not a new proof of B. Conversely, a path with positive score `Q=8a-5d` has `Q<=delta a`, hence `a>=Q/delta`. The fraction of its odd states with popcount at most fixed S is `O_S(a^(-1/S))`, and therefore `O_S(Q^(-1/S))` as Q grows. Hypothetically unbounded inverse scores would thus be witnessed by already convergent paths spending almost all odd events above every fixed popcount cap. High digit complexity alone cannot contradict the burden; the missing global control is still present.

No density implication from these finite-path counts to ordinary component membership is asserted.
