# Fifth pass: end-to-end attempts on all three routes

Agent: `astra-three-routes-05` (GPT-6 Pro). Date: 2026-09-05.
Target: existing PR #92, frozen at
`6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc`.

**PARTIAL RESEARCH. All new theorem-level claims are PROPOSED pending independent
mathematical review. No complete Collatz proof was obtained.** All three routes
are retained. No earlier proof or experiment is rewritten or promoted.

## The constructive advance

A mode change can destroy a large ternary valuation and increase the common
integer rank enormously. This pass proves that a SPECIFIED following block
repays that loss. For every t>=3 there are infinitely many ordinary sources
with exact word `1110(110)^t`, starting with v3(n+5)=t, such that

    n < A(n) < A^2(n),
    R(A(n)) > 2*3^(t-2) R(n),
    R(A^2(n))/R(n) < (81/256)*(27/64)^t < 1/4.

The same R is used at all three endpoints. This crosses the initially
misaligned case left by pass 4. It does not claim that every orbit chooses
this word. An explicit wrong-next-mode counterexample is retained.

## Three complete logical endpoints, and where each attack stops

| Route | New proved partial statements | Missing end-to-end assertion |
|---|---|---|
| Mass transport | Rank spectrum has sharp exponent 1/2; reciprocal-rank weights are summable exactly for p>1/2; every nonincreasing-rank excursion has a certified all-source tail | A positive summable supersolution or actual aggregate control for the induced unsafe process. Pure R^(-p) weights fail there on an explicit infinite family |
| Ordinary-source separation | Every smaller refined-rank witness belongs to one exact O(sqrt(R(n))) list; equal-rank steps cannot cycle; complete bounded-clock merging tests are implemented | A proved total temporal merging cover, not just a finite source list or a sequence of increasing search caps |
| Termination/rank repayment | One strict integer refinement orients all nonincreasing steps; a general all-parameter two-mode repayment theorem and a sharper unbounded-spike family cross some increases | A complete physically valid cover of the remaining mode changes. Ternary precision alone does not force the repayment word |

## Read the proofs

1. [SWITCH_REPAYMENT.md](SWITCH_REPAYMENT.md): the positive unbounded-spike result.
2. [RANK_SPECTRUM.md](RANK_SPECTRUM.md): sharp square-root counting and explicit tails.
3. [PLATEAUS_AND_SOURCES.md](PLATEAUS_AND_SOURCES.md): flat-rank orientation and complete spatial search.
4. [INDUCED_MASS.md](INDUCED_MASS.md): exact safe elimination and the failed global weight.
5. [ATTEMPT_AND_SOURCES.md](ATTEMPT_AND_SOURCES.md): frozen dependencies, claim boundaries, and publication status.

## Quantitative results at a glance

For all M>=1,

    #{n>=2:R(n)<=M} < 9 sqrt(M),
    sum_(R(n)>=M) R(n)^(-p) <= [9p/(p-1/2)] M^(1/2-p), p>1/2.

An equal-rank A step necessarily increases n. Thus

    Phi(n)=R(n)^2+R(n)+1-n

strictly decreases on every R-nonincreasing A step. An entire such run has
at most 9 sqrt(R(n)) modules before reaching 1 OR an unsafe state.

For mass bounded by C/R(n)^2, the enlarged safe region has

    ||K_G^r f||_1 <= 8748 C/r^3, r>=9,
    sum_(r>=L)||K_G^r f||_1 <= 4374 C/(L-1)^2, L>=10.

These are all-time bounds only for the explicitly killed SAFE process.
The induced unsafe operator still has arbitrarily large pointwise ratios for
R^(-p), even above every fixed floor. Its ordinary witness family is
x=3^e, e=4 mod16, J(x)=(9x+7)/16.

## Exact finite verification

The generator and separately written verifier agree on the complete report.
The verifier imports no generator or repository code, evaluates the full
component dictionary, scans complete rank sublevels independently, uses literal
shortcut dynamics, and reverses full finite trees for the merging tests.
It also passes with Python -O; checks use explicit exceptions.

Coverage includes nine complete rank sublevels through M=65536, 16383 ordinary
module sources, six all-source safe-mass intervals with analytic omitted tails,
thirteen induced-operator spike witnesses, 44 special repayment lifts, 28
general parameter cases, and ten complete bounded-clock merging tests. Eight
resealed corrupt reports are rejected. Same-author implementation independence
is not independent mathematical review.

    python -B experiments/X-ASTRA3-005-spectrum-switch/run.py \
      --check experiments/X-ASTRA3-005-spectrum-switch/results/canonical.json
    python -O -B experiments/X-ASTRA3-005-spectrum-switch/verify.py \
      experiments/X-ASTRA3-005-spectrum-switch/results/canonical.json --self-test

Semantic report SHA-256:

    45888e331821905d73141de70258b9cbfc03df94ec58208a94b5d66f9d687aee

## Publication boundary

This authoring session read the existing PR and completed the local research
and checks, but did NOT push a commit. The available connector exposes only
read operations, plugin discovery returned the already-installed GitHub
connection, and direct git failed DNS resolution. This addition-only packet
is packaged as a continuation patch against the frozen existing PR head.
The publication helper is supplied but was not executed. No remote branch,
PR, settings, workflow, or canonical mathematical status was changed.
