# Actual-prefix ranks: automatic selection across arbitrary expanding periods

**Full Collatz proof: NOT obtained. All APR claims are PROPOSED pending
independent mathematical review.** This continuation attacks the universal
rank-switching step left by PR106. Its positive result uses one computable
proper integer rank, not an assumed ability to alternate unrelated ranks.
The remaining fixed-source switching/merging cover is still OPEN.

## Main result

For n>=2, let g(d)=d^2/3^{v3(|d|)} for d!=0, and define

    Gamma(n)=min( g(n), 4^k g(T^k(n)-n): k>=1, T^k(n)!=n ),
    Gamma(1)=0.

T is the ordinary shortcut map. Zero displacements are omitted. Only actual
prefixes from n qualify. The apparently infinite minimum is computable using
at most floor(log_2 n) shortcut steps, with n<=Gamma(n)<=n^2.

For EVERY primitive expanding parity period w, the [all-period theorem](PERIODIC_SWITCHING.md)
gives explicit ordinary sources on which the unique minimizing length is |w|
at every position of an arbitrarily long prescribed finite repetition. At each
step the SAME rank drops by exactly 1/4 or 3/4, while the ordinary values grow
at period boundaries. Its proof excludes ALL competing actual prefixes,
including the unprescribed future, rather than assuming that the future is
periodic or truncating a search empirically.

The family 111010 is particularly informative. Its old moving rank R_* grows
through arbitrarily many quarter-unsafe mode switches. Gamma instead decreases
at every shortcut step, and starts below 4/27 of the old rank. No terminal
halving/repayment block is required for this finite phase. The parameters select
new ordinary sources; they do not force this behavior on every given source.

## Read the proofs

| ID | Result | Exact scope / remaining limit |
|---|---|---|
| APR-001 | Proper actual-prefix rank and a finite evaluator | No unknown stopping-time oracle; zero returns omitted |
| APR-002 | Physical rotation descent for even minimizing displacement | A sufficient guard, not exhaustive source coverage |
| APR-003 | Complete rank sublevels and convergence threshold s>1/2 | O(sqrt(M) log M) upper count; not survivor or basin counts |
| APR-004 | All-source safe tails and finite undiscounted safe occupation | Killed on unsafe entry as well as 1; no refreshed input envelope |
| APR-005 | Complete lower-Gamma merging criterion | Implication proved; universal cover/selector NOT supplied |
| APR-006 | Any primitive expanding period, every phase, one selected rank | Explicit finite ordinary families; sources vary with horizon |
| APR-007 | Old 111010 unsafe switches become Gamma-decreasing | All parameters in its guard, not every old unsafe source |
| APR-008 | Unbounded uniquely selected prefix lengths | The evaluator is input-dependent, not a fixed word dictionary |
| APR-009 | Powers of three force superlinear rank peaks and moment explosion | No convergence claim or induced-unsafe operator obstruction inferred |

[PROOF.md](PROOF.md) contains APR-001--005. [PERIODIC_SWITCHING.md](PERIODIC_SWITCHING.md)
contains APR-006--008 and all effective source conditions. [SPIKES.md](SPIKES.md)
proves APR-009 and rejects the attempted global pure-rank weight.
[Sources and review boundary](SOURCES_AND_STATUS.md) distinguishes credited
inputs from the new derivations.

## Where the complete proof attempt stops

The positive source-selection theorem closes the competing-prefix problem
on its explicit families. It does not close the dynamically generated
complement. For a hypothetical exceptional component minimum of Gamma,
every nonzero minimizing displacement must be odd, and a minimizing baseline
must be at an odd source. This necessary residual condition is not impossible
by the present argument.

In fact Gamma(3^H)=3^H and Gamma(T(3^H))>(3^H)^(11/10) for every H>=1.
Every lower-rank physical merger of 3^H must first traverse that rank spike.
The finite example 1932103 also shows a six-step contracting phase followed
by a rank-increasing change of minimizing prefix. Neither is a Collatz
counterexample. They prevent global monotonicity or perpetual renewal of a
finite phase guard from being silently asserted.

**OPEN APR-Q1:** prove a total selection of finite physical lower-Gamma
merging diagrams for the remaining sources, or a valid actual retained-mass
estimate. A smaller rank witness without a common endpoint is not sufficient.
A full proof is not supplied merely by the finite evaluator, safe tails,
positive families, or this conditional closing criterion.

## Evidence and submission

[X-ALF-002](../../../experiments/X-ALF-002-prefix-rank/README.md) independently
reconstructs the fixed finite corpus in two implementations. Both were written
in this session: implementation independence is NOT independent mathematical
review. The universal statements rest on the written proofs, not the corpus.

This is an addition-only continuation of PR106 at
`ca55b248722fd9bdeb713c6f05fdda5cbdc91f38`. Earlier mathematical files, historical
reviews, registry statuses and workflows remain untouched. The parent linear
frontier theorem is motivation, not an unreviewed premise of APR-001--009.
