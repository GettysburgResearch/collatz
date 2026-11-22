# Independent mathematical review of the finite original-source entropy bound

Reviewer role: the arithmetic/source agent, independently reconstructing the
finite-distribution argument while the author develops the Lean source.
This is a semantic proof review, not a claim of compiler execution.

## Sources and scope

- `collatz_work/deep_root/OriginalSourceEntropy.lean`, the finite entropy,
  product code, affine path and endpoint-congruence declarations.
- `collatz_work/deep_escape/ACTUAL_ORBIT_ENTROPY.md`, equations E1--E12.

The final reviewed Lean source SHA256 is
`4b40c2c433751eeb72c3ceceb1c32df149d70dc7e99cf60ca7a066642be492ea`.
The reviewed written source SHA256 is
`958344f44fdd06acb771e8abd8af3b70f6c47c7069f035f8eb13f0209ca28d98`.
The physical decoder, actual weighted-family bridge, optimized mean bound,
sliding-window estimate and exact logarithmic budget are included in the
final review. All 21 public theorem statements were inspected. The
statements below distinguish semantic proof review from compiler evidence.

## Verdict on the finite inequality: VERIFIED at the stated scope

Let V be the finite word space `(Fin m -> Fin M)`. Let p be **any**
nonnegative probability on V, and f any deterministic finite projection.
For `0<rho<1`, set

`Q(v)=product_i (1-rho)*rho^(v_i)`.

This is a positive subprobability reference, not an independence assumption
on p. Indeed its total mass is `(1-rho^M)^m<=1`. The log-sum comparison gives

`H(p)<=-sum_v p(v)log Q(v)`.

The proof in the file uses `log x<=x-1` separately where p is positive;
zero masses are handled with the convention `0 log0=0`. The correction
term sums to `sum Q-sum p<=0`, so a subprobability reference is sufficient.

The logarithm of Q is exactly

`m log(1-rho)+(sum_i v_i)log rho`.

Deterministic pushforward decreases Shannon entropy: each individual p(v)
is bounded by the total mass in its f-fiber, and monotonicity of logarithm,
multiplied by the nonpositive coefficient -p(v), gives the inequality.
This argument needs no normalization for the intermediate pushforward
lemma; the final bound uses `sum p=1`.

Thus the declared finite bound

`H(f_*p)<=-m log(1-rho)-E_p[sum_i v_i]log rho`

is correct for the actual joint law as well as any other finite law. In
particular, it does not substitute independent geometric gaps for the
original orbit. Independence appears only in the chosen comparison code.

Degenerate finite types cause no missing case: m=0 gives the unique empty
word and entropy zero; M=0,m>0 admits no probability with total mass one.

## Physical decoder and actual weighted family: VERIFIED

The exact gap path identity is

`3^len(w)*n+offset(w)=2^sum(w)*r`,

where `offset(a::w)=3^len(w)+2^a*offset(w)`. The recursive proof multiplies
the first actual gap equation by `3^len(w)` and the suffix identity by
`2^a`, so the exponents and ordering are correct.

Since powers of two are units modulo `3^len(w)`, the endpoint residue is a
function of the gap word alone, regardless of the starting integer.
Consequently `same_word_same_ternary_endpoint` has the correct meaning and
is valid even for the more general affine path type used in the file.

The raw `GapPath` definition stores only `3n+1=2^a*u`; it deliberately
covers a larger algebraic class than positive odd accelerated Collatz paths.
The final header and theorem documentation state this scope correctly.
Every actual positive odd trajectory supplies these equations, so the
stronger algebraic theorem applies to it without an unproved dynamical
premise. The `gapWord` definition retains the necessary +1: a symbol v_i
is an **excess**, and its gap is `v_i+1`.

The final `ternaryCode` chooses an endpoint only when a word has an affine
path. Endpoint congruence makes this choice irrelevant for every observed
actual sample. A default value on infeasible words is harmless, since such
words have zero mass in the pushed sample law. The push-composition and
weighted-sum identities show that `finite_original_source_entropy` preserves
the original sample weights, actual endpoints and mean excess cost. It
introduces no independently selected ordinary source.

The optimized theorem takes a>1 and expected excess at most m(a-1), then
sets rho=(a-1)/a. Since -log rho is nonnegative, replacing the actual cost
by that upper bound has the correct inequality direction. Its conclusion
is exactly m[a log a-(a-1)log(a-1)]. The a=1 endpoint is not silently
included in the Lean statement; the written argument handles it directly.

The sliding-window theorem is also correct: for each offset j<m, the
injection k->k+j maps its N-m+1 samples into {0,...,N-1}. Nonnegative
cost then bounds that shifted sum by the complete N-term sum; summing
over m offsets gives the stated factor m.

Finally `single_gap_log_identity` takes logarithms of the exact positive
real equation 2^a*y=3*x+1 and uses
3*x+1=3*x[1+1/(3*x)]. `finite_gap_log_budget` telescopes these identities.
Both positivity hypotheses and all finite endpoint terms are present.
The later asymptotic use of integer positivity and nonperiodicity remains
in the written theorem, not an unstated premise of these finite equalities.

## Written actual-orbit theorem E1--E12: VERIFIED

I reconstructed the argument independently:

1. For a uniform K in `{m,...,N}`, the random word is the last m actual
   valuations, not a selected inverse word. Modulo `3^m`, the source term
   in the affine identity vanishes and the remaining correction determines
   the actual endpoint.
2. The sum of the expected m gap coordinates is at most
   `m*A_N/(N-m+1)`, because each physical gap appears at most m times in
   all the windows. Positivity ensures the mean argument is at least one.
3. The maximal entropy at a positive integer mean a is the geometric
   value `Phi(a)=a log a-(a-1)log(a-1)`. Finite support, concavity and
   monotonicity yield E1, including a=1 by continuity/direct determinism.
4. A nonperiodic deterministic positive integer orbit has no repeated
   state, and therefore eventually leaves every finite set: `q_N->infinity`.
   This is enough for the logarithmic error terms to have Cesaro mean zero.
   Telescoping gives `limsup A_N/N<=log_2 3`.
5. Fixing m before the weak limit is essential and is done correctly.
   Removing finitely many initial samples has vanishing total variation.
   Ternary residue cells are clopen; finite-simplex entropy is continuous,
   so every weak empirical limit obeys the same bound at every fixed m.
6. The identity with binary entropy and the strict inequality below one
   are correct. A dimension ceiling is not a proof that the whole measure
   is singular; the text preserves this distinction.
7. Jensen gives `sum p_r^2>=exp(-H(p))`. The unit group has
   `2*3^(m-1)` residue cells, hence the factor `(2/3)` in E11 is correct.
8. The speed refinement uses the exact upper comparison
   `q_N+1<=(3/2)^N(q_0+1)` and the same vanishing correction. Its interval
   for v and the expression `a_v=(log3-v)/log2` are correct.

No potential estimate, inverse-predecessor density theorem, GRH, or
independent-gap stochastic model is used in these deductions.

## What this does not establish

The entropy **upper** bound is a restriction on a hypothetical escape,
not a contradiction. A general place-dependent ternary affine stationary
law can have low entropy dimension. A theorem forcing a larger dimension
or a smaller collision energy for an actual ordinary escaping orbit is
still required. In particular, finite entropy code comparison is not a
proof of that missing lower bound.

The review does not promote the new prose to a machine-checked theorem.
The finite Lean inequality, the physical input bridge, and the written
weak-limit argument must be described at their respective evidence levels.
