# Independent review of the endpoint-capacity relaxation

**Verdict: VERIFIED in the stated relaxed analytic cone.** I independently
reconstructed EC1–EC5, read their exact comparison sources, and replayed
the finite checker. No correction is required in the reviewed bytes.
This verdict does not assert a Collatz-invariant counterexample, a failure
of an inequality on actual invariant Boolean labels, or a solution of
Collatz.

## 1. Exact review boundary

The reviewed files are in
`/workspace/scratch/46eba7b29f50/agent-analytic-remains/`.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `ENDPOINT_CAPACITY.md` | 10,826 | `0e4479eefbb7f27f2cabca82c2414a7c9fab4d6c2c2788235ad6e997a0d1e65d` |
| `check_endpoint_capacity.py` | 7,319 | `9869f152674d8043b5c221ce9c2f8f6dde19989b58ecf0845e6a002ae76d54bb` |
| `endpoint-capacity-report.json` | 2,629 | `647b27bc7b4da12b5d1a87bf2af0ed7ebdf8e09472955cbc1616ac371dd6049d` |

The source comparisons were read directly by `git show` at:

- PR155 `92f499b9d340d1ff8cc643c3eef3477d61b477c1`,
  `research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`,
  especially OD1, its norm normalization, and OD3's profile comparison;
  `ENDPOINT_BOUNDARY.md`, especially equations E1–E5.
- PR146 `6863d298187af8b2619efbf78cc4b0aa8e627393`,
  `research/upper-bit-mergers/TRIPLING_VARIATION.md`, its homogeneous
  variation statement; `THREE_RAY_VARIATION.md`, its logarithmic-circle
  comparison; and `THREE_RAY_UPPER.md`, its interval and odd-progression
  upper bound.

These inspections establish the comparison targets. They are not a new
blanket review of every theorem in those source files. EC1–EC5 themselves
are proved from explicit integer functions, counting, and elementary
summation; they do not depend on assuming an unknown Collatz component.

## 2. EC1: the Boolean family and uniform shell variation

The odd-part decomposition gives exact doubling invariance and

\[
 b_M(3n)-b_M(n)=-1_{\{M/3<o(n)\le M\}}.
\]

In the half-open shell `[2^k,2^(k+1))`, a fixed odd part has at most
one lift. Thus the dyadic mean is at most `A_M/2^k` and tends to zero
for every fixed cutoff. No conclusion uniform in `M` is needed for
this limit; the later norm obstruction deliberately lets `M` vary.

I checked the real-endpoint details of the variation proof. If
`R<M/2`, then `floor(2R)+1<=M`, so even the last endpoint `n+1` of
an included edge has label one. If `R>=M/2`, the odd defect count up
to `2R` is exactly `B_M`. Every changing edge has an endpoint labeled
one, and each such endpoint is charged at most twice. The interval
`[R,2R+1]` has endpoint ratio at most three for `R>=1`; three lifts
of one odd part would require a ratio at least four. Hence its
variation is at most `4A_M`.

For `M>=7`, the displayed estimates imply
`A_M <= (M+1)/2 <= M-3 <= 3B_M`. The six smaller positive cutoffs
satisfy the same inequality directly. This proves the claimed
`12 D_b(2R)` bound with constants independent of both variables.
The inclusive upper endpoint and the `R=M/2` boundary cause no gap.

## 3. EC2: exact norms and the critical order

Both the function and its absolute tripling defect are doubling
invariant, so the full norm is the odd norm multiplied by
`(1-2^(-s))^(-1)`. This factor occurs on both sides and cancels in
the ratio. For `0<s<1`, subtracting the odd partial sums at `M` and
`M/3` gives the denominator factor `1-3^(s-1)`. The stated limiting
ratio and the lower pole constant `1/log 3` follow.

At `s=1`, the odd harmonic sum is
`(log M)/2 + constant + O(1/M)`. Its annular difference is
`(log 3)/2 + O(1/M)`. Multiplying by the dyadic factor two gives
the two full-norm formulas in (9). Integrating `log x/x` over the
odd annulus gives `(log 3)(log M)/2+O(1)`, as stated.

The replacement-weight claim explicitly concerns the **odd-defect
sum** of PR155 E5. On that sum the support is bounded by `M`, so
monotonicity permits its weight to be replaced by `w(M)`. It would
not be legitimate to use that pointwise bound on unrestricted dyadic
lifts with a weight evaluated at the full integer. The final reviewed
text makes the odd-defect interpretation explicit. An added constant
in a weight does not affect the `o(log M)` comparison.

This proves sharp order for the retained cone. No lower bound for the
best constant on genuinely `T`-invariant functions is inferred.

## 4. EC3: a fixed real counterexample to harmonic-mass coercivity

For each positive odd part `m`, the summands in the mixture begin at
`J(m)`. The telescoping identity
`sum_(j>=J) 1/(j(j+1))=1/J` proves the closed form. After truncation
at an arbitrary index `R`, the tail is uniformly at most `1/(R+1)`,
so the series converges uniformly.

Every summand's tripling defect is nonpositive. Thus the absolute
defect of the mixture is exactly the mixture of absolute defects;
there is no cancellation loss in (12). Adjacent variation requires
only the triangle inequality, and both its finite sums and the
nonnegative defect sums can be interchanged. Splitting off a finite
mixture and its uniformly small tail proves vanishing dyadic means.

The full harmonic defect of every `b_(4^j)` is less than three.
Its full harmonic mass is `j log 4 + O(1)`. Tonelli therefore gives
a finite defect norm but infinite mass for the **one fixed** real
function `f`. This is not a varying-source compactness argument.

The centering issue is harmless. Vanishing nonnegative dyadic means
give a zero profile limit. More directly, for any nonzero constant
`c`, the shell average of `|f-c|` is at least `|c|` minus the shell
average of `f`, and hence eventually at least `|c|/2`. Its harmonic
norm is infinite as well. Thus no choice of constant repairs the
harmonic-mass failure. The function is bounded and real, and is
explicitly neither Boolean nor Collatz invariant.

## 5. EC4: uniformity in interval location and odd common difference

For an odd part `m`, multiplication by three increases `J(m)` by at
most one because `3<4`. At an increasing jump, the defect is exactly
`1/(J(m)(J(m)+1))`, bounded by `J(m)^(-2)`. This verifies (15).

For a positive progression `a+bi`, `0<=i<N`, with odd `b`, let
`L=ceil(log_2 N)`. For each `v<L`, at most `H` terms can have the
form `2^v m` with odd `m<=H`; each candidate integer can occur at
most once. Among indices in a block of length `N<=2^L`, at most
one term is zero modulo `2^L`, since `b` is invertible modulo that
modulus. This single term covers all valuations at least `L`.
Hence `HL+1` is uniform in both `a` and `b`; no small-stride or
bounded-location premise is missing.

With `H=floor(sqrt N)`, the low-odd-part contribution is
`O(sqrt N log N)`, which is `o(N/log^2 N)`. The remaining contribution
is `O(N/log^2 N)` by the pointwise bound. Small lengths can be covered
by increasing one absolute constant because each defect is at most
one, regardless of the progression. This proves the stated uniform
estimate, not merely a fixed-location limit.

If the relaxed cone imposes a particular positive numerical constant
in the weaker PR146 real-valued upper estimate, replace `f` by a
sufficiently small positive scalar multiple. Its harmonic mass remains
infinite, its harmonic defect stays finite, and the homogeneous
variation inequality is unchanged. This rescaling observation is
available for real functions; it does not preserve Booleanity.

The distinction in the note is therefore essential: the Boolean
family has a positive defect proportion in its own annuli and does
not meet an `M`-uniform sublinear interval bound. The fixed real
mixture does meet such a bound. EC4 does not refute compactness or
coercivity for Boolean functions satisfying all exact Collatz
conditions.

## 6. EC5 and the unresolved ordinary condition

For `n=(4^j-1)/3`, literal application of the odd shortcut branch
gives `T(n)=2^(2j-1)`. The remaining ordinary steps are halvings
to one. Choosing `n>M` gives the claimed Boolean change from zero
to one. Taking `n>4` also gives `f(n)<f(T(n))=1`.

Thus the failure of odd-branch invariance is explicit, occurs on a
known convergent ordinary path, and is not hidden in an unproved
component or a completion. These examples preserve exact doubling
and the stated analytic relaxations while losing one exact branch
of the Collatz equations.

The final scope discussion is sound. The bound
`D(X)=O(X/sqrt(log X))` supplies only a nonsummable upper bound on
successive profile differences. Small rotation errors make each
fixed nonzero Fourier coefficient tend to zero; they do not imply
strong convergence or preserve Boolean values under weak limits.
If the means themselves are not known to converge, the constant-mode
limit also remains a separate issue. The note does not claim that
its counterexample disproves strong convergence for every genuine
invariant labeling. Even a strong zero profile would not itself
make a sparse ordinary component empty.

## 7. Execution evidence and limitations

I ran the author's checker in normal and `-OO` modes. Both outputs
matched the frozen report byte for byte, including its proof hash.
The report records 16,640 definition/doubling checks, 33,344 bounded
real-shell checks, 64 literal odd-edge failures, 16,384 fixed-function
integer controls, and 20 odd-progression controls.

I also implemented selected checks independently in a separate inline
Python program, without importing the author's module. It used a
different definition of `J` by repeated powers of four, exact rational
values, real shell endpoints on a sixth-grid plus seventh-offset
boundary probes, and odd progressions with non-power-of-two lengths
and large starts/strides. All passed:

- 6,486 independent real-shell inequalities, including the zero-shell
  and full-annulus boundary cases;
- 512 fixed-function mixture, doubling, and sign-coherence checks;
- 45 odd-progression low-odd-part and exact two-piece defect bounds;
- 23 explicitly checked odd edges followed by their known halving
  paths to one.

These executions test finite algebra and endpoint handling. The
infinite norm conclusions, uniform quantifiers, and asymptotic orders
were established by the reconstructed written arguments above, not
by extrapolating the bounded replay. No author file was modified.
