# Third all-route pass: signed boundaries, finite records, and joint arithmetic memory

Agent: `astra-three-routes-03` (GPT-6 Pro). Date: 2026-09-05.
Frozen parent: PR #92 at `48e043c2822dbeea4f91c801ac2d3fc531af1466`.

**All three routes remain active. All new theorem-level claims are PROPOSED
pending independent mathematical review. No complete Collatz proof is claimed.**
Earlier proof and experiment bodies are preserved. This pass adds exact
arithmetic results and tests rather than extending the earlier finite pilots
and presenting their trend as a theorem.

| Route | Main new argument | Still missing |
|---|---|---|
| [1. Signed boundary charge](BOUNDARY_CHARGE.md) | Only one color of first surviving parity-cylinder representatives contributes positive residue bias; an exact signed-curvature expansion has a rigorous infinite-tail bound | An all-depth signed charge estimate at one fixed convergent floor |
| [2. Finite coefficient records](FINITE_RECORDS.md) | Uniform reciprocal budgets extend to finite simple paths; finite coefficient stopping on a near-source window gives an explicit descent-or-repetition clock | The local coefficient-stopping certificates in every required window, and nontrivial cycle exclusion |
| [3. Joint arithmetic ranks](JOINT_ARITHMETIC_RANKS.md) | Even arbitrary joint nonlinear functions of finitely many polynomial valuations and residues fail, including bounded adaptive groups of whole-run macros | A constructive total mechanism with genuinely different information or unbounded repayment |

## Strongest exact statements

For route 1 let a_w be the first ordinary survivor of parity word w, modulo
m=2^k. With f_l=(a_w+ml)^(-s), the residue defect's sign depends on the first
eligible index j in {0,1,2}. Only j=0 is positive. Its exact leading term is
f_0/3 plus a signed discrete-curvature series; the other colors are nonpositive.
A first-representative mass condition is thus an explicit necessary condition
for excess bias, not an assumed mixing law. For s=3/2, every H>=32*2^k gives
Q_k/M_k<11/32<69/200. The floor grows with k; this is not fixed-floor closure.
At H=64 the required cofinal signed charge is written explicitly and remains
OPEN. The all-source finite-time checker keeps the negative terms: dropping
them loses useful certificates already in the small pilot.

For route 2 any finite simple path staying above n has

    product_odd(1+1/(3x)) <= exp((200/3)n^(-1/40)).

Put B(n)=floor(n exp((200/3)n^(-1/40))) and R(n)=B(n)-n+1. If every integer
in [n,B(n)] has coefficient stopping time <=N, then within R(n)N steps the
source n descends below itself or repeats a state. This is a finite conditional
clock, not an unconditional time to the SC-infinite source from pass 2. A
non-explicit refinement replaces the window width by O(n^(19/20)).

For route 3 take an arbitrary finite vector of polynomial-valuation and residue
observations V(n). No scalar rank

    s log n + Phi(V(n)) + o(log n), s>0,

can be nonincreasing at every large source under any fixed shortcut block,
or under any total selector of between 1 and B maximal-run macros for fixed B.
Phi can be fully coupled and arbitrary. The proof chooses a rational cycle
center outside the finite dictionary and constructs exponentially large
ORDINARY sources shadowing it for arbitrarily many packets. The complete
feature vector is identical at all packet boundaries; the logarithmic size
increases by a positive constant times the number of packets. The sources
change with that number, so no infinite ordinary counterexample is extracted.

## Checks, scope, and read order

Read the three proofs, then [SOURCES_AND_REVIEW.md](SOURCES_AND_REVIEW.md), then
the separate checker in `experiments/X-ASTRA3-003-boundary-records-shadow/`.
The finite report covers:

- 16,382 complete parity cylinders and 65,528 ordinary surviving lifts;
- 26 all-source finite-time mass rows (H=64,4096 and k=0,...,12), with explicit
  AP and curvature tails; all certify the original bias ceiling in this range;
- 6,146 no-descent subsegments, 24,101 exact correction-product positions,
  and the full convergent core 1..64;
- 18 long ordinary shadow certificates, 189 exact maximal-run packets, and
  adaptive bounded-group checks for three nonlinear polynomial dictionaries;
- eight resealed corrupt reports rejected by independent reconstruction.

The generator and verifier share no source imports. Both were authored in
this session: implementation independence is NOT independent mathematical
review. The universal claims are the written proofs, not extrapolations of
the finite tests. No large external certificate or prior inverse-cone replay
was run, and no workflow or canonical status was changed.

Semantic SHA-256:

    dd5c52ff9a06ae728f7f10d84db655ae3324ca2318531b130ff66eced5b7feb6

This pass deliberately does not narrow the portfolio. Its constructive next
connection is to use record-set or unbounded repayment information to control
the signed boundary process, rather than another finite observation table.
That connection is a research proposal, not a proved global inequality.
