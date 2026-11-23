# Independent review of the carry and real/2-adic transfer packet

Reviewer: `triadic_construction`, 23 November 2026. This is an independent
agent review inside this project, not external peer review.

**Verdict:** the local carry identities, the forced real control, its
aperiodicity and density estimates, and the two unequal-limit controls
are correct at the source hashes below. A fresh strict Lean build and
the explicit eight-theorem axiom audit pass. The assessment of the
López–Stoll argument is appropriately limited: an explicit assertion in
Section 2 is refuted, and the corresponding transfer cannot be imported.
Neither Collatz nor the falsity of that preprint's final Theorem 1 is
established.

## Frozen review targets

All three files have exactly one final newline and no extra EOF blank
line. The reviewed source files were not edited by this reviewer.

| File, relative to `research/profound-step-20261123/transfer/` | SHA-256 |
| --- | --- |
| `REAL_ADIC_TRANSFER_ATTEMPT.md` | `a45d38f6be88a76209ce72860acffe585a2be3f27c868ab9a75148444de6e2ae` |
| `lean/RealAdicControl.lean` | `47b155e7a049363fe6c8ddf06162726b60fa159fe0be60397d3111db3dbfcfd6` |
| `lean/RealAdicAudit.lean` | `4cb865773037bb680576ac1d8221304a2ad410ae2266fc1ff8d032a85d7271ed` |

## 1. The q-adic construction and ordinary carry

I reconstructed the identities independently. For the actual parity
sequence, multiplying its generating series by `1 + q^2` yields the
claimed conjugacy to `T_(1,1+q^2)`. Its coefficients after the first two
are exactly the two-clock parity differences. Thus the note correctly
retains eventual period-two parity as the missing polynomiality
condition.

For an odd integer, write its binary digits as `b_j`, with `b_(-1)=0`.
The ordinary digit sum at position `j` is

\[
b_j+b_{j-1}+\mathbf1_{j=0}+c_j
=s_j+2c_{j+1}.
\]

The initial total is two; all later totals are at most three, so the
carry digits really belong to `{0,1}`. Summing over `j` gives the note's
integer-polynomial identity (2), including the sign `q-2`. Reduction
modulo two followed by division by `q` gives (3), with the residual
carry polynomial still present.

For `E(n)=h_q(n)+P_n`, the exact backwards equations are

\[
E(n)=qE(Tn)\quad(e_0=0),\qquad
E(n)=\frac q{1+q}E(Tn)+\frac q{1+q}R_n
\quad(e_0=1).
\]

After `K` substitutions the terminal term is
`q^K (1+q)^(-p_K) E(T^K n)`. Its valuation is at least `K`: `1+q` is a
unit and `E(T^K n)` is a formal power series for every finite ordinary
state. Each carry term indexed by `j` has valuation at least `j+1`.
This proves convergence and the precise exponent `p_(j+1)` in (4)
without assuming Collatz convergence. It provides no finiteness theorem
for the coefficient-section orbit.

I directly read [Monks' primary article](https://cs.uwaterloo.ca/journals/JIS/VOL28/Monks/monks6.pdf),
Theorems 2 and 5 and Conjecture 6. The note correctly distinguishes the
formal conjugacy and polynomial dynamics from the conjectural claim
about the conjugacy images of positive integers.

I also read [Christol–Kamae–Mendès France–Rauzy](https://www.numdam.org/article/BSMF_1980__108__401_0.pdf),
Theorem 1 and Sections 6–7, printed pp. 406–409. The theorem relates
algebraicity, finite automata, and substitutions over finite fields;
the proof uses a finite orbit under coefficient-section operators.
The note does not replace this finite-state hypothesis with mere
computability. These external theorems remain source-qualified
mathematics, not extra Lean imports or a universal Collatz argument.

## 2. The real control, with all denominators retained

The interval checks in Proposition 1 are correct. A zero branch sends
`[2,5/2]` into `[1,5/4]`, and a one branch sends `[1,2)` into `[1,5/2)`.
For `d_k=2^(k+1)`, the two numerator updates are `a_k` and `3a_k-d_k`.
Both are odd because `a_k` is odd and `d_k` is even. Therefore the
denominator is exactly `2^(k+1)` in lowest terms. No hidden denominator
reduction or ordinary-rational parity hypothesis is being used.

The zero image is below two, so zeros cannot be adjacent and
`p_K >= floor(K/2)`. Both equations in (8) follow from their actual
integer updates. In the one branch, `a_k < 2d_k` implies
`2(3a_k-d_k) <= 5a_k`, proving the residual inequality by induction.
Dividing the finite identity by `2*3^p_K`, and then using the bound
`(3/2)(5/6)^p_K`, proves the real Bernstein value `-3/2`.

The aperiodicity proof is valid for the word, rather than relying just
on nonrepetition of states. An eventual period of length `A>=1` must
contain `p>=1` ones. Positive terms of the convergent real Bernstein
series force its block ratio `2^A/3^p` to be less than one. The geometric
tail then has a denominator dividing a power of three times
`3^p-2^A`. This is odd, as is the finite prefix denominator, and cannot
produce the reduced denominator two of `-3/2`. This explicitly supplies
the needed contradiction.

For the density estimate, a zero multiplies `z` by `1/2`, while a one
multiplies it by `(3-1/z)/2 < 5/4`. Therefore

\[
1\le z_K\le\frac32\frac{(5/2)^{p_K}}{2^K}
\]

gives the stated lower limit at least `log(2)/log(5/2)`, strictly above
`log(2)/log(3)`. This is a bound on the lower limit; existence of an
ordinary density limit is not asserted or needed.

## 3. Unequal limits and the precise literature conclusion

Every term of the 2-adic Bernstein sum has valuation equal to its digit
position. The 2-adic limit `alpha` exists in `Z_2`, so it cannot equal
the real value `-3/2`. Prepending one produces the real value `-4/3`
and the 2-adic value `beta=-1/3+(2/3)alpha`. The latter is odd while
`-4/3` is even in `Z_2`. Thus the second control still disproves
identification when the real value itself has odd denominator. Its
first forced odd branch is not the genuine rational-parity branch.

I directly inspected [López–Stoll, arXiv:2101.12747v1](https://arxiv.org/pdf/2101.12747):
Section 2, equations (15)–(16) and the surrounding text on printed
pp. 7–8; Section 6, Lemmas 23–26 and the final Theorem 1 proof on
pp. 28–30. The Section 2 pages were also inspected as rendered images.
The assertion excluding an even reduced denominator for an existing
real limit is explicit. The final proof invokes (15)–(16) to transfer
the real conclusion to the 2-adic expansion. Residues of the rational
approximants do not identify the two limiting values. The constructed
controls therefore validate the note's limited objection. They do not
determine whether `alpha` is rational, do not refute the preprint's
final theorem, and do not produce a positive-integer Collatz
counterexample.

## 4. Fresh Lean execution and scope

The two modules were compiled independently into the fresh directory
`/workspace/scratch/56e7a5765d0c/nov23-arithmetic-transfer-review`.
Both invocations used `-DautoImplicit=false -DwarningAsError=true` and
returned exit code zero. Source hashes were unchanged during this
execution. The compiler was Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and the reused Mathlib dependency
objects were from commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
No previous project proof corpus was rebuilt.

The explicit audit covers exactly these eight public theorems:

- `denominator_pos`, `denominator_succ`, `denominator_even`;
- `bounded_odd`, `digit_zero_one`, `no_two_zeroes`;
- `finite_bernstein`, `residual_bound`.

Only `propext`, `Classical.choice`, and `Quot.sound` occur in the audit
output. There is no `sorryAx` or project-specific axiom. The q-series,
the infinite real and 2-adic limits, the geometric aperiodicity proof,
the logarithmic density bound, and the external-source assessment are
written mathematics reviewed above; they are not counted as additional
formalized theorems.

| Execution artifact in this report directory | SHA-256 |
| --- | --- |
| [transfer-review-execution.json](transfer-review-execution.json) | `d2a4924447de36b032f529d74421d04df95305f491d9e6ee2ada8326b1951cda` |
| [transfer-review-compile.log](transfer-review-compile.log) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| [transfer-review-axioms.log](transfer-review-axioms.log) | `c823563da4d09b739d4bb0389b9bdcfe320dd2e43185f0eeca60df1fb5d007f1` |

The remaining mathematical obligation is unchanged: prove a finite
coefficient-section structure or stronger actual-carry cancellation
and ultimately the required polynomiality, or construct the preceding
checkpoint's height-controlled triadic witness for every fixed positive
ordinary source. This packet verifies neither universal construction.
