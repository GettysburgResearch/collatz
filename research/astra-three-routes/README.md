# Astra: three routes toward a complete Collatz resolution

**Agent:** `astra-three-routes-01` (GPT-6 Pro). **Date:** 2026-09-05.
**Overall status: PARTIAL RESEARCH; COLLATZ UNSOLVED.**
All new theorem-level claims are **PROPOSED pending independent review**.
No canonical registry, accepted theorem status, or other contributor's files are changed.

This is one coherent research packet pursuing the three routes requested by the
project owner, not three plans without mathematical work. It supplies an
aggregate all-source mass identity and finite certificate, an exact return-echo
displacement sieve, and a complete obstruction to a broad arithmetic rank class.
The remaining proof-level gaps are stated alongside the results.

## Read the three routes

| Route | New work supplied | Precise remaining gap |
|---|---|---|
| [1. Aggregate Mellin transport](ROUTE1_MELLIN.md) | Killed source/endpoint identity; a ternary-bias ceiling implying global contraction; source-cutoff-free finite-time inverse-cone certificates; exact failure of a simpler mixing claim; forced critical-mass ternary bias | Control survivor-conditioned residue mass for all times, or prove a weaker nonsummable dissipation estimate |
| [2. Return-echo displacement sieve](ROUTE2_RETURN_ECHO.md) | First-disagreement descent after a near-return; exact common-d lower thresholds by v_2(d); a least-counterexample reduction that permits descent after the first crossing | Exclude every echo-safe ordinary tuple, including cycles, and close the supercritical lane |
| [3. Arithmetic rank obstruction](ROUTE3_RANKS.md) | Every finite affine-valuation correction to positive logarithmic size fails fixed-block nonincrease and, by a separate proof, the adaptive whole-run macro; explicit ordinary witnesses | A nonlinear, different adaptive, vector/tree-valued, or controlled infinite-feature rank |

The [carry-normalization packet](CARRY_NORMALIZATION.md) supplies the positive
algorithmic interface for route 3: unique mixed-radix carry normal forms and an
exact odd-run macro retaining unbounded ordinary data.

## Main formulas

For route 1, put chi_k(n)=1 when the first k+1 states from n remain above 64,
and use weight n^(-3/2). Write M_k for its total survivor mass and Q_k for the
mass of eligible endpoints y>=98, y=2 modulo 3. The concrete open target is

\[
Q_k\le(69/200)M_k\quad\text{for every sufficiently large }k.
\]

It implies M_(k+1)<(993/1000)M_k and hence Collatz. It is certified only for
0<=k<=36. The stronger assertion Q_k<=M_k/3 is refuted at k=19.

For route 2, an ordinary return n -> n+d, d>0, has a forced parity disagreement
after t=v_2(d) further steps. If T^t(n) is odd, then

\[
(2-C_t)n>C_t d+E_t
\]

certifies descent below n after t+1 further steps. Substitution of the complete
first-crossing equation A=Dn+2^j d gives an exact displacement-stratum sieve.

For route 3, no rank

\[
R(n)=s\log n+\sum_{p,\alpha}c_{p,\alpha}v_p(n-\alpha)\log p+o(\log n),
\qquad s>0,
\]

with finitely many rational affine roots can be nonincreasing under T^ell on
all sufficiently large positive integers, for any fixed ell. A separate theorem
excludes the same template for the adaptive whole-run macro. Neither theorem
excludes all unbounded-memory termination methods.

## Exact finite evidence

* All-source mass at H=1 through time 40, using 267,024 inverse-cone vertices;
  at H=64 through time 36, using 2,510,783 vertices. Analytic tail intervals include
  every positive source, without asserting eventual convergence.
* 32,768 ordinary first-disagreement tests. The rational first-crossing compiler
  covers 12,449 words through length 21 and removes 6,431 of 9,779 formal positive-
  displacement pairs. None of these 9,779 formal sources is an integer.
* All 19,531 mixed-radix words through length 6, 16,384 odd macro inputs, and 18
  ordinary fixed-block rank-increasing witnesses for six sample ranks and three
  block sizes, plus six adaptive-macro rank witnesses.

The generator and verifier are separate standard-library implementations. They
were written in the same session, so implementation independence is not external
mathematical review. Finite tests do not verify the proposed all-length proofs.

From the repository root:

```bash
python experiments/X-ASTRA3-001-three-routes/run.py \
  --check experiments/X-ASTRA3-001-three-routes/results/canonical.json
python experiments/X-ASTRA3-001-three-routes/verify.py \
  experiments/X-ASTRA3-001-three-routes/results/canonical.json
python experiments/X-ASTRA3-001-three-routes/test_verifier.py
```

## Provenance and review

Intended base: canonical main at `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
No dependency is silently imported from an unmerged branch. See
[SOURCES.md](SOURCES.md), [CLAIM_MATRIX.md](CLAIM_MATRIX.md), and
[ATTEMPT.md](ATTEMPT.md) for frozen sources, theorem scope, failed shortcuts, and
what to try next. The native theorems are elementary; only the final critical-
exponent comparison invokes the source-qualified external predecessor theorem.

Recommended mathematical review order: the rank coefficient-transport lemma,
the killed odd-inverse boundary and analytic tails, and the source-versus-endpoint
normalization in the echo sieve. Review the all-time hypotheses separately from
the successful finite certificates.

## Continuation: all three routes remain active

The [second pass](pass2/README.md) extends this packet at the separately frozen
parent `879343c33a7dca29128891cf6e10d9c7be1ba482`. It supplies explicit orbitwise
Mellin budgets and a cofinal-time bias criterion; actual SC-infinite tail
extraction and a complete continuation compiler; and separate fixed-block and
adaptive-macro obstructions for arbitrary nonlinear valuation profiles. All
new claims remain PROPOSED pending independent review. Earlier proof and
experiment bodies above are preserved; no route is dropped.
