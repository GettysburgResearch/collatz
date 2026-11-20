# Actual validation and exact evidence boundaries

## Clean scientific checkout

The root executed the required driver in the clean complete review worktree
at scientific commit `cdb9a9197dcf7578e03d551219b3299f9f295ecb`, tree
`a365c185ef72da4ec10923e97ed056fed4b49699`, with 334 tracked files.

```text
python -X utf8 -B tools/validate.py --regressions --receipt /workspace/scratch/6c37546fb87e/structural-science-checkout-validation.json
```

**PASS: all 11 child commands, exit code 0.** The driver began at
2026-11-20 19:21:31 UTC and finished at 19:21:36 UTC. Its before/after
checkout records match. A separate status read after all new checks was
also clean. Python was 3.12.14 on Linux.

The original receipt was written outside the checkout as required. Its
unmodified copy is [checkout_validation.json](checkout_validation.json).
It records actual commands, outputs, exit codes and both checkout
identities. This is repository integrity and bounded-regression evidence,
not verification of a universal mathematical claim.

## New research checks at that same commit

[research_validation.json](research_validation.json) preserves the actual
root command results. These runs used the same clean review checkout.

| Actual command | Result and scope |
|---|---|
| `python -X utf8 -B research/structural-reset-20261120/check_prime_height.py` | PASS, exit 0. Exact finite arithmetic on 20 selected seeds, 32 transitions each: 4,560 affine-pair checks, 5,700 local budgets, 1,440 finite-history budgets, and nine predecessor controls. Largest actual division exponent 2048. |
| `python -O -X utf8 -B research/structural-reset-20261120/check_prime_height.py` | PASS, exit 0. Output exactly identical to the normal run; checks use explicit exceptions. |
| `python -X utf8 -B research/structural-reset-20261120/component/check_component_rigidity.py` | PASS, exit 0. All 480 symbolic affine cells, including every positive lift, satisfy the conditional domains, identities, positivity, strict descent and uniform bound. At most nine primitive conditional-law applications per reduction. |
| `python -O -X utf8 -B research/structural-reset-20261120/component/check_component_rigidity.py` | Correctly rejected, exit 1, with `Run without -O: certificate checks require assertions.` This is an expected guard result, not a successful optimized proof replay. |

The prime-height check uses a declared candidate pool when choosing its
heaviest sample primes. The written argument, not that pool, proves
uniformity over all prime sets of bounded cardinality. It does not test
an escaping orbit or exclude a nontrivial positive cycle.

The component check represents n=480k+r by exact affine coefficients and
checks inequalities at the coefficient level and the smallest permitted k.
It is not a census of 480 input values. Its scope remains the selector
under the printed functional identities. It does not prove the merger
hypothesis E or supply its physical clocks.

The earlier author check and nonauthor checker replay remain separate
events in their adjacent receipts and reviews. They are not substituted
for these executions at the published scientific commit.

## Written review and file identity

The proof and review address table in [README.md](README.md) gives the
complete PR, scientific commit, path and claim scope. The independent
adelic review reconstructed the elementary argument without analytic
input or computation. The component review checked the exact F=f domains,
every descent branch, the smaller sufficient law system, and the
conditional final implication. The root separately reconstructed the
physical pair maps, proper cost, reset counterexample, drift criterion,
clock obstruction and fixed-source tail guard.

The only correction to the reviewed component proof was the explicit
phrase "For each fixed a" in its auxiliary two-word slope obstruction.
Both original and corrected hashes are preserved in its review. The
conditional equivalence and selector were unchanged by that correction.
No narrow verdict covers the still-open hypotheses.

## Publication follow-up and evidence ceiling

The scientific commit was pushed to
`research/structural-reset-20261120`, read back through the GitHub ref API,
fetched, and matched locally before the executions above. Draft PR154
was then opened. This follow-up adds the actual receipts and exact source
mapping; it does not change any research proof or checker. The final
publication head receives its own clean-checkout driver run, recorded
outside the checkout and reported in the PR description after execution.
The receipt above remains explicitly for the scientific commit.

No repository validator is presented as a proof of Collatz. No external
formal build, large new convergence search, full cycle enumeration, or
automatic human approval is claimed. The research result remains the
scoped structural theorems and their explicit unresolved closing steps.
