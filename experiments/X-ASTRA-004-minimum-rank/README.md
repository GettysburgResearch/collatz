# X-ASTRA-004 — two-sided minimum-rank certificates

**Finite exact support. All theorem claims remain PROPOSED. No Collatz closure.**
The proofs and exact residual are in
[MINIMUM_RANK.md](../../research/astra-critical-mass/MINIMUM_RANK.md).

The experiment uses the shortcut map, section n=1 mod 3, and integer rank
P(n)=(2n+1)^2/3^v3(2n+1). A certificate connects a source to a lower-rank
merging integer by two actual parity words. Numerical increase is allowed;
ordinary integrality, positive sources, common endpoints, and rank decrease
are mandatory.

## Coverage

Every section source 4<=n<=2^18 is classified, without assuming convergence:

| Result | Count |
|---|---:|
| h=1 forward reduction | 58,254 |
| even-source merge | 14,564 |
| additional immediate forward reduction | 2,479 |
| immediate inverse reduction | 1,479 |
| h=2 two-return forward reduction | 4,045 |
| h=2 two-sided merge | 1,011 |
| six-step backward rule | 7 |
| residual label | 5,542 |
| total | 87,381 |

There are 19,418 h=2 inputs; exactly 1,011 survive these local rules, in
139,427,571,859,1003 modulo 1296. The all-integer statement comes from the
written proof, not from enumerating this cutoff.

Further exact checks:

- 128 full inverse-return fans, 256 sources. The separate verifier enumerates
  every section source x<=4y for each endpoint y. The bound is proved by the
  complete fan formula; it is not a guessed finite truncation.
- 70 CRT cases: H in {6,7,12,24,64}, L in {1,2,3,8,16,32,64}, two positive
  lifts each. All 1,260 forward returns have rank above the starting rank;
  each case has a larger lower-rank ancestor two reverse returns away.
- Radius-four undirected searches at the first 1,024 residual inputs: 784
  forward successes, 37 extra two-sided successes, and 203 unresolved cases.
- All 37 extra diagrams lift to infinite progressions by T-ASTRA-024. Each is
  also replayed at t in {0,1,7,1000,10^30}. The infinite conclusion follows
  from the affine/rank proof, not from these five substitutions.
- Source 121 remains unresolved at radius eight. This is not a counterexample;
  its first forward rank drop occurs after 16 section returns.
- Six resealed altered reports are rejected: removed tile, false global scope,
  reduced core coverage, reduced parameter coverage, changed witness parity,
  and a changed progression increment.

## Replay and evidence boundary

From the repository root:

```bash
python experiments/X-ASTRA-004-minimum-rank/run.py \
  --check experiments/X-ASTRA-004-minimum-rank/results/canonical.json
python experiments/X-ASTRA-004-minimum-rank/verify.py \
  experiments/X-ASTRA-004-minimum-rank/results/canonical.json --self-test
```

Both pass. Do not use Python -O: assertions are part of these checkers.
Semantic SHA-256:

    eb192ad108608599021061970c9a1135c7746cd3b7d2a770e79ad35c1fd55f9d

The report includes the 37 full tiles and digests of the reconstructed core,
fan, family, and search rows. The verifier imports neither the generator nor
repository modules. It uses literal shortcut stepping in place of closed-form
returns, a separate inverse traversal, exhaustive forward fan enumeration,
extended Euclid for CRT, and rational rather than integer affine composition.
Both implementations have the same author: implementation independence is
not independent mathematical review or formal verification.

No target hits, counts, or finite search successes are interpreted as a
complete cover. No external computation, Lean build, repository-wide validator,
workflow, or assumed high-range convergence is a dependency of these checks.
