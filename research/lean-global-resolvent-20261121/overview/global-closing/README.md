# Checkpoint 18: ordinary-source constraints on the closing routes

23 November 2026. **Full Collatz remains OPEN.** This checkpoint refreshes
the repository-wide picture, then attacks candidate construction, actual
orbit collisions, stationary recurrence, and complete cycle denominators
in parallel. Its new results are written proofs with exact finite controls
and internal mathematical review. No new Lean theorem is claimed here.

The main positive results are a finite bound for every successful
same-endpoint gap-one insertion repair, and an entropy bound on the
occupation of polynomial height ranges by one fixed injective ordinary
orbit. An infinite generic-ray construction tests what additional source
arithmetic is needed to turn the stationary-law work into an individual
orbit theorem. A paired-cycle calculation determines exactly what the
new tensor denominator adds to the scalar closing equations.

## 1. What changed in the surrounding work

The refresh inspected the current research map, open-obligation and source
catalogue context, 50 recent PR metadata entries, the central live branch
heads, the designated new mathematical files, and all 14 task cards in the
deep-machinery guide. It is not a claim to have re-audited every historical
proof. Four central peer heads advanced since checkpoint 17:

| Frozen branch | Relevant new input | Closing step still absent |
|---|---|---|
| PR177, `f47a5ec51aa5853f104013a6d5046d6220ff7423` | Independent finite exact-candidate recognition; source-tail transport and literal multiplier bounds | A successful candidate or merger for every fixed ordinary source |
| PR178, `c91b80a3156e640ad471cf30c47721145ae21eb1` | Finite certificates for arbitrary odd denominators; one equivalent harmonic flow with `O(1/N)` comparison to actual time laws; complementary denominator capacity | Candidate existence, an actual collision upper bound, or a competing denominator upper bound |
| PR180, `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161` | Stationary real-series classification, fixed-resolution entropy/phase rigidity, stronger complementary denominator restriction, and actual-series holonomicity consumer | Transfer at the actual growing resolution, ordinary source rigidity, or a constructed functional equation |
| PR182, `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c` | Linear-clock triadic recognition, finite ordinary local-randomness/collision controls, exact cycle-root normalization | A universal selector, fixed-source collision estimate, or complete-denominator exclusion |

The full heads, paths, content hashes, and read scopes are in
[`SOURCES.json`](SOURCES.json). The guide at PR186
`1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` supplies literature and task
leads, not imported proofs of its open applications. The preceding own
checkpoint is `4171e1fe40e41842af9f800bd821084b724cf8f9`.

Several branches independently reached exact finite recognition. These
are overlapping advances toward a trustworthy certificate interface;
counting them separately would overstate progress toward existence.
The new effort here is directed at source construction and the missing
global estimates.

## 2. A complete finite bound for one ordinary repair class

[`FINITE_GAP_ONE_INSERTIONS.md`](FINITE_GAP_ONE_INSERTIONS.md) treats the
following precise operation. Start with the actual odd-gap word of a
positive odd integer `n`, keep all its gaps in order, insert `t>=1`
additional gaps equal to one, and require the enlarged word to end at
the same ordinary endpoint.

If its starting value `m` is a positive integer, then `m<n`. Writing
`N=bitlength(n)` and `A` for the original shortcut clock at the last
insertion, the new theorem proves

\[
 3^t<2^t n,\qquad 2^t<n^2,\qquad
 A\le(N-2)(2^t-1),\qquad
 \boxed{A+t<N(n^2+2).}
\]

The trajectories already agree in this alignment after the last insertion.
Thus choosing an arbitrarily distant common endpoint cannot hide an
arbitrarily late edit. The entire successful insertion-only class has a
finite search domain for each source.

The proof keeps the positive even aligned difference `D=q-z`. Across a
common block with total valuation `B`, `2^(B+1)` divides its starting
difference. An inserted one decreases the difference. The same endpoint
prevents a sign change before the final edit; these facts give the clock
budget without any assumed growth estimate for the original orbit.

Multiple edits can repair each other's ternary denominators. The example

\[
45\xrightarrow{3}17,\qquad
19\xrightarrow{1}29\xrightarrow{3}11\xrightarrow{1}17
\]

comes from inserting ones at cuts 0 and 1. The first edit alone has
inverse source `89/3`, so imposing integrality on each partial edit
would miss the final ordinary merger.

This class does not give a universal selector: source 3 has no such smaller
repair, although it converges. Existence specifically at a least escaping
ordinary source remains open. Deletions, replacements, and general merger
words are outside the bound.

## 3. A bound on actual orbit occupation, not just its maximum

[`ACTUAL_ALL_GAP_COLLISIONS.md`](ACTUAL_ALL_GAP_COLLISIONS.md) retains one
fixed positive ordinary source with an injective odd orbit `q_j`.
Let `P_(N,k)` be its actual empirical distribution of `k` consecutive gaps,
with natural-log Shannon entropy. If along the same subsequence

\[
 H(P_{N_i,k})\to H_k,\qquad \alpha=\frac{H_k}{k\log3},
\]

then for every fixed `B>0`,

\[
 \boxed{\limsup_i\frac1{N_i}
 \#\{j<N_i:q_j\le N_i^B\}\le\min(1,\alpha B).}
\]

The exact finite inequality is

\[
 K\log K\le(N-m)H(P_{N,m})
 \le\left\lceil\frac mk\right\rceil(N-k)H(P_{N,k}),
\]

where `K` counts actual endpoints below `X<3^m`, omitting only the first
`m` clocks. Such endpoints have distinct `m`-gap words because each word
determines its endpoint residue modulo `3^m`.

In the strict finite-Shannon-deficit branch, `alpha<theta`, where

\[
 \ell=\log_2 3,\quad
 \Phi=\ell\log\ell-(\ell-1)\log(\ell-1),\quad
 \theta=\Phi/\log3.
\]

For every `1/theta<B<1/alpha`, a fixed positive proportion of the **same
orbit** must exceed `N_i^B`. The result strengthens a maximum-height
consequence to occupation. It remains compatible with escape.

The same note proves that the collisions forced by a strict entropy
deficit cannot all occur at short gaps. At
`m_i=floor(log(N_i)/Phi)`, there are at least `c N_i^(1+beta)` colliding
ordered pairs for some `beta>0`. All gaps at most `L_i` contribute at
most `N_i(2L_i+1)`. Thus almost all of that forced mass survives beyond
every `L_i=o(N_i^beta)`.

For every actual collision gap, reduce its complete fixed-point anchor
`C/(2^A-3^d)=c/b`. The exact joint divisibility is

\[
 2^{A+1}3^m\mid bq_i-c,
 \qquad
 H(c/b)\ge\frac{2^{A+1}3^m}{q_i+1}.
\]

This retains both arithmetic valuations at every lag. The missing upper
bound must control the changing anchors and the actual starting heights
over the full gap sum. The new fast harmonic-flow comparison does not
remove that ordinary endpoint variable.

## 4. One infinite ray can have all critical iid statistics and a transient pressure

[`GENERIC_RAY_CONSTRUCTION.md`](GENERIC_RAY_CONSTRUCTION.md) starts from
critical geometric iid gaps of mean `ell=log_2 3`. A running regulator
inserts only `o(n)` extra gap-one symbols. The resulting single infinite
word keeps every finite iid block frequency and the exact critical mean,
yet satisfies

\[
 \chi_j=3^j/2^{B_j}>1\quad(j>0),\qquad
 \chi_j\ge(j/2)^3\text{ eventually},\qquad
 \sum_j\chi_j^{-1}<\infty.
\]

Its centered pressure bridge also has oscillation `o(N)`. This is a
consistent infinite ray, extending the scope of earlier changing-source
finite controls. A nonatomicity argument and injectivity of the exact
2-adic gap code prove that its source is irrational almost surely.

The separate gap-two regulator gives the opposite pressure sign. It has
the same iid empirical statistics and mean, but
`sum chi_j<infinity`. That branch has a strict pressure **maximum** at
the origin. It does not satisfy the minimum condition of the first branch.

These statements keep the two real series separate:

| Output | Strict origin condition | Forward inverse series `sum chi_j^-1` | Reversed-gap real series `sum chi_j` |
|---|---|---|---|
| Insert ones | Minimum | Finite | Infinite |
| Insert twos | Maximum | Infinite | Finite |

Atkinson recurrence and PR180's critical stationary real-series theorem
are almost-everywhere statements for their specified stationary laws.
They cannot be applied to a selected generic point using finite block
frequencies alone. The positive construction does not contradict the
stationary reversed-series conclusion; its convergent series is the
reciprocal one. Neither construction supplies an ordinary integer orbit
or the actual canonical harmonic path law.

The finite ordinary repair theorem in Section 2 is therefore an essential
companion: the symbolic freedom used by the regulator does not become
unlimited source-preserving arithmetic freedom.

## 5. Paired cycle moments do not add a third closing equation

[`PAIRED_TENSOR_CLOSURE_ATTEMPT.md`](PAIRED_TENSOR_CLOSURE_ATTEMPT.md) pairs
a shortcut word and its parity complement. Their product has the
parity-independent multiplier `3/4`, suggesting the new full denominator
`4^A-3^A` might force extra cancellation.

For the two scalar residuals

\[
 f=(2^A-3^p)X-C,\qquad g=(2^A-3^{A-p})Y-C^*,
\]

the complete product closure is exactly

\[
 (4^A-3^A)XY-3^p C^*X-3^{A-p}CY-CC^*
 =2^AYf+2^AXg-fg.
\]

Every finite polynomial full-word moment closure likewise belongs to the
ideal generated by `f,g`. Those equations alone therefore supply no
independent third condition. This does not rule out additional inequalities,
valuation estimates, or constraints from ordinary integrality.

The note also computes the **full reduced complementary denominator**
for the earlier one-rise rational controls. Arbitrarily high, long,
primitive nonintegral rational cycles satisfy both refreshed companion
lower bounds and all the tensor identities. The omitted condition stays
explicit: the original complete denominator does not divide its carry.

## 6. Where to put the next attack

The live routes have different missing statements. Their combination does
not yet close either the escape branch or the positive-cycle branch.

| Route | Concrete next target | What it would resolve |
|---|---|---|
| Exact certificates and mergers | Construct a successful unchanged candidate, or a complete smaller ordinary merger, for every source required by the least-counterexample reduction | A direct route to full convergence |
| Actual collision law | A critical collision upper bound for the same actual endpoint law, with its precise order of limits retained | Escape, through the existing stationary strict-exponent contradiction |
| Fixed-floor occupation / analytic transport | Quantitative control that keeps the original ordinary source and survives all transport steps | Escape when it meets the resident closure consumer |
| Complete cycle denominators | A forced upper bound or shared cancellation incompatible with the full complementary denominator lower bounds | Nontrivial positive cycles |
| Analytic or arithmetic rigidity | A finite functional relation, recurrence, or height saving actually constructed from the ordinary source | The relevant recurrence or periodicity reduction; its remaining cycle obligation must still be discharged |

My priority is the universal source construction and the full actual
collision sum. The former already has exact finite recognizers; the latter
now has a strong same-law comparison and an explicit long-gap target.
The paired-cycle calculation makes plain why extra algebraic moments,
without new integral information, do not finish the denominator route.
The machinery guide remains useful when its independence, height, rank,
or source hypotheses can actually be established.

[`HANDOFF_QUESTIONS.md`](HANDOFF_QUESTIONS.md) gives self-contained tasks
at these boundaries, including an elementary positive-integer recurrence
formulation of the actual collision problem. These are open questions,
not assumptions silently supplied to a closing theorem.

## 7. Evidence and reproduction

The full proof packet is here; execution and internal review are in
[`reports/2026-11-23-global-closing`](../../../../reports/2026-11-23-global-closing/README.md).
The four new exact checkers are run normally and with `python -O`; their
outputs are compared to frozen records. The uniform theorems have written
proofs and are not inferred from the finite diagnostics. Upstream source
claims retain their stated review scope.

From a complete checkout:

```sh
python -X utf8 -B research/lean-global-resolvent-20261121/overview/global-closing/verify_checkpoint18.py \
  --receipt /tmp/checkpoint18-scoped.json
python -X utf8 -B tools/validate.py --receipt /tmp/checkpoint18-integrity.json
```

The first command checks this packet's frozen files, new controls and
available source pins. The second is the separate clean complete-checkout
integrity gate. Neither claims to prove Collatz. The prior Lean checkpoint
is retained without re-running the historical formal corpus.
