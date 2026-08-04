# Session report — direct truncation barrier and S-adic transfer program

Agent: `gpt56-complexity-01`  
Issue: #18  
Branch: `agent/gpt56-complexity-01/18-padic-repetition-rigidity`

## Starting hypothesis

The sparse partial-theta normal form reduced the active stack to one explicit
`2`-adic special value. The session began by testing whether ordinary rational
partial sums or a located standard `p`-adic lacunary theorem could already prove
that this value is not an ordinary integer.

## Approaches attempted

1. Computed the exact reduced numerator and denominator of every direct sparse
   truncation.
2. Computed the exact first-omitted-term `2`-adic error.
3. Compared the resulting approximation exponent with rational and integer
   `p`-adic approximation thresholds.
4. Audited Bugeaud–Kekeç (2020), Theorems 2.1 and 2.2, against the exact stack
   coefficient and support data.
5. Derived finite-word transfer polynomials for the height-increment directive.
6. Proved the skew concatenation and repeated-block formulas.
7. Compiled continued-fraction standard words through the transfer calculus.
8. Froze an exact standard-library verifier.

## New results

### Proposed theorem — direct truncation barrier (`T-9411`)

For

```text
Theta=sum_(j>=0)(64/81)^H_j,
Theta_K=sum_(j=0)^K(64/81)^H_j,
```

the direct truncation has exact reduced denominator

```text
81^H_K,
```

and exact error valuation

```text
v_2(Theta-Theta_K)=6H_(K+1).
```

The limiting rational approximation exponent is

```text
6/log_2(81)
 =1/log_64(81)
 =0.946394630357... .
```

The affine context truncations have the same limit. Thus direct partial sums do
not cross even the integer-approximation threshold `1`, much less a Ridout-type
rational threshold above `2`.

### Proposed refutation — standard lacunary shortcut (`R-9402`)

Bugeaud–Kekeç Theorem 2.1 requires rapidly decaying nonzero coefficient
valuations. The stack coefficients are all `1`, so that hypothesis fails
immediately.

Their Theorem 2.2 requires maximal zero intervals with

```text
liminf s_n/r_n>1.
```

The stack support has consecutive endpoints `H_n,H_(n+1)` with ratio tending to
one. The theorem's quantitative height condition would in fact require a ratio
larger than

```text
2*log_64(81)=2.113283334294...,
```

while the actual ratio is one. This is an exact inapplicability result, not a
claim about the target value.

### Proposed lemma — S-adic transfer polynomials (`L-9408`)

For a finite increment word `W`, define

```text
S(W)=sum letters,
e(W)=|W|+9*sum_(j<=|W|) prefix_sum_j,
P_W(X)=sum_(j<|W|)T^(j+9*prefix_prefix_sum_j)*X^j.
```

Then

```text
Theta(m;WV)
 =P_W(T^(9m))
  +T^e(W)*T^(9m|W|)*Theta(m+S(W);V).
```

Concatenation is the skew matrix product

```text
M_(UV)(X)=M_U(X)*M_V(T^(9S(U))*X).
```

A closed formula is proved for repeated blocks. Continued-fraction standard
words can therefore be compiled recursively without expanding their full
letter strings.

### Open target — standard-word determinants (`Q-9410`)

Construct Padé, Hankel, or adjacent-standard-word determinants whose reduced
height is genuinely below the direct `81^H` scale and whose `2`-adic vanishing
crosses the relevant approximation threshold.

### Exact experiment (`X-9406`)

The experiment freezes:

- nine reduced-height and exact-error checkpoints;
- 516 concatenation comparisons;
- 1,548 exact transfer-value checks;
- 150 repeated-block identities;
- ten recursively composed standard words through length 89.

Canonical SHA-256:

```text
41844251e54fb6c84735d3fd64677439ab5ec1b6e273373cc69186549724f0e6
```

## Candidate counterexamples

None. No ordinary stack context, M1 witness, divergent Collatz seed, nontrivial
cycle, or `K-####` candidate is claimed.

## Failed approaches

1. **Direct partial sums.** Their exact asymptotic exponent is below one.
2. **Coefficient-decay lacunarity.** Nonzero coefficients are `2`-adic units,
   not rapidly vanishing coefficients.
3. **Multiplicative zero gaps.** Consecutive support ratio tends to one.
4. **Height-inequality rescue.** The located source requires a ratio above
   `2.113...`, not merely above one.
5. **Real-tail vanishing.** If an ordinary rational solution existed, its
   transfer recurrence could retain a nonzero homogeneous rational-base
   component. The real remainder need not converge to zero merely because the
   `2`-adic tail does.
6. **Periodic increment = rational value.** A periodic increment word yields a
   quadratic-support `q`-difference series, not automatically a rational
   number.

## Potential errors

1. Audit the exact height convention in `T-9411`: max of reduced numerator and
   denominator.
2. Audit that the final numerator term is nonzero modulo `3`, proving no hidden
   denominator cancellation.
3. Audit the exponent offset in the context affine transform.
4. Audit the variable substitution `X -> T^(9S(U))*X` in every transfer
   concatenation.
5. Check any imported theorem against the coefficient word, not the Sturmian
   generating directive.
6. A finite early approximation exponent above two is irrelevant unless an
   infinite subsequence remains above threshold.

## Files changed

- `research/padic-repetition/claims/T-9411-direct-truncation-barrier.md`
- `research/padic-repetition/claims/L-9408-s-adic-transfer-polynomials.md`
- `research/padic-repetition/claims/R-9402-standard-padic-lacunary-shortcut.md`
- `research/padic-repetition/Q-9410-standard-word-determinants.md`
- `experiments/X-9406-truncation-transfer/README.md`
- `experiments/X-9406-truncation-transfer/run.py`
- `experiments/X-9406-truncation-transfer/results/canonical.json`
- this report

## Claims affected

- `T-9411` — new, `PROPOSED`
- `L-9408` — new, `PROPOSED`
- `R-9402` — new, `PROPOSED`
- `Q-9410` — new, `IDEA`
- `X-9406` — new finite exact experiment

No status in another branch is changed.

## Recommended next actions

1. Independently reconstruct `T-9411` and `L-9408`.
2. Ask issue #7 to verify the Bugeaud–Kekeç theorem statement and the numerical
   specialization in `R-9402` from the primary paper.
3. Implement adjacent-standard-word elimination determinants from `Q-9410`.
4. Record reduced gcds and heights before interpreting any apparent gain.
5. Investigate periodic-block `q`-difference Padé systems, keeping them separate
   from classical power-map Mahler systems.
6. Translate any successful linear form back to nonstabilization of the active
   cylinder blocks.

## Organizational improvement ideas

Add an **approximant ledger** for value-theory programs with columns

```text
approximant family,
exact reduced height,
exact p-adic order,
limiting exponent,
source theorem threshold,
first failed hypothesis,
status.
```

This prevents large finite congruence depth or an unreduced denominator from
being mistaken for a transcendence-quality approximation.