# Frozen sources, scope, and mathematical review

Date: 2026-11-22. Repository: `GettysburgResearch/collatz`.

## Repository-wide inventory

The [metadata snapshot](../../../../reports/2026-11-22-whole-repository/pr-snapshot.json)
contains all 145 pull requests returned by the repository-wide query, including
122 open and 23 closed records. Each record retains its full head SHA, base,
title, state, and URL. Main was
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; our starting published head was
`8aeb843bba254f065743b6fa277a70906b51d520` on PR176.

The inventory establishes which work was visible. It does not independently
verify the mathematical contents of every PR. This pass refreshed the current
repository maps and scoped errata, then read the following source families
for the specific assertions used in the new arguments.

Before publication, a second remote read found that PR183 had advanced to
`68345f60a4f757acb42a69a4ac95910f8ce26163`. That continuation was fetched
and read across all three lanes. Its exact comparison is in
[the late-head integration](LATEST_HEAD_INTEGRATION.md). The earlier
145-record snapshot is preserved as the earlier inventory; it is not
silently relabeled as a later query.

## Selected current sources

| Source | Full frozen commit | Exact path / local claim boundary | Use and evidence boundary |
| --- | --- | --- | --- |
| PR175 | `2bc2ad37b490a5aea63658eaf657bc048da4532e` | `research/lean-global-closure-20261121/CANONICAL_POTENTIAL_SUPERLEVELS.md` | Read the global nonperiodic potential moments, superlevel structure, and antichain budget. Its source-qualified predecessor input remains visible. |
| PR177 | `a0a0d76f91b4e3846c1b1f0706cad56cb6098317` | `research/lean-exact-witness-global-20261121/lean/Collatz/`, exact 14-module list in `DEPENDENCIES.json` | Byte-identical formal imports for complete supplied certificates, their multiset grade, and the low-interval induction hypothesis. These imports were freshly compiled for this checkpoint. |
| PR178 | `be5696cc45a95ad1903802b08ba1dc3ebba66930` | `research/literature-reframe-20261122/ORDINARY_RENEWAL.md`, Section 3; `ABEL_ANTICHAIN.md`; `PHYSICAL_MERGERS.md` | Read the critical first-moment escape criterion and exact physical source/clock boundaries. No upper bound for the critical first moment is inferred. |
| PR179 | `27a2c7414fdb92eeca57ad552a9ab5c36d8430d8` | Current exact interval/certificate source family | Context for prior finite budgets and inverse ladders; no new formal dependency imported from this head. |
| PR180 | `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` | `research/lean-forward-band-20261121/` and `research/lean-wide-pass-20261122/{ENERGY_SYNTHESIS,RETURN_SYNTHESIS,WITNESS_SYNTHESIS}.md` | Canonical finite potential/harmonicization and the critical-law comparisons used through PR185. Their written/source-qualified status is retained. |
| PR182 | `45354128f890fb479f6c23b547368bcddd9cebe6` | `research/lean-dyadic-descent-20261121/LITERATURE_RIGIDITY_BRIDGE.md` | Read ordinary invariant-label Fourier rigidity and the explicit missing approximation condition. No multiplicativity, compact-to-ordinary trace, or Besicovitch approximation is supplied. |
| PR183 | `907a540943090968bc683b1b9246208e9053c1f8` | `research/literature-closing-20261121/`, especially `mergers/CONSTRUCTIVE_NORMAL_FORM.md`, `lean/EntranceRenewal.lean`, `lean/RetainedTransport.lean`, `arithmetic/BandArithmetic.lean`, `mergers/MixedBaseNormalForm.lean` | Read the actual-source transport and mixed-base erasure cover. Current upstream receipt reports 69 checked theorems across four modules; this checkpoint does not rerun those four modules or treat erasure coverage as proved. |
| PR183, later continuation | `68345f60a4f757acb42a69a4ac95910f8ce26163` | `research/profound-step-20261122/`, especially `arithmetic/{FREE_EXPONENT_CYCLES,CARRY_COMPRESSION_BRIDGE}.md`, `mergers/ARBITRARY_DEBT.md`, `operator/WOLD_CHANNELS.md`, `transport/ASYNCHRONOUS_RESIDUE.md`, and `RECONSTRUCTION_REVIEW.md` | Read the 52-theorem continuation's written arguments, theorem types relevant to the overlap, and execution report. Credit its concurrent free-exponent classification and arbitrary-debt transport. Combine its sharper chain and asynchronous residue with this packet's rotation and last-contact source measure. The 52 upstream modules' declarations are not included in our own audit count. |
| PR184 | `366dab89ee9548084ab9b5e4e90ff82abf287a20` | Source-relative marked-band and merger-coupling packet | Retain the original source, not an unrelated mark or a fresh convergent certificate, when comparing possible handoffs. No additional imported Lean dependency. |
| PR185 | `276be8154f4e867acc0230466b34d9cb224aacf5` | `research/whole-repo-closure-20261122/{EFFECTIVE_FIXED_BLOCK_CYCLES,ORDINARY_HARMONIC_FLOW_AND_COLLISIONS,CARRY_LANGUAGE}.md` | Read the full ordinary harmonic-flow note and selected arithmetic/carry arguments. The new classifier generalizes the exponent parameterization; the new last-contact measure composes this harmonic flow with our first-contact theorem. |
| PR186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | `literature/deep-machinery-20261122/{README,06_agent_tasks}.md` and the rigidity/long-shot guide | Read the guide and 14 task interfaces as research direction, not as new proved closure. Its older PR183 replay status and band-clock task are reconciled below. |

The two older formal imports from PR176 are pinned to
`03e40fa4d7506ad92682a49c850103b028a11dbe`:

- `research/lean-global-resolvent-20261121/lean/Collatz/TerminalCarry.lean`:
  the original signed high-bit transfer, reused without alteration.
- `research/lean-global-resolvent-20261121/overview/parallel/lean/Collatz/SourceEnvelope.lean`:
  the exact maximal paid source exponent, reused without alteration.

The current analytic first-contact input is
`(PR176, 8aeb843bba254f065743b6fa277a70906b51d520,
research/lean-global-resolvent-20261121/overview/parallel/OBSTACLE_ENTRANCE_RENEWAL.md)`.
Its finite formal lemmas and its written infinite argument keep their separate
evidence levels. The new analytic conclusions are written deductions, not
extra claims about what the Lean audit covers.

## New narrow review boundaries

| New result | Review performed | Status |
| --- | --- | --- |
| `BlockRepetitionBudget.lean`, all 12 public declarations | Root inspected the actual definitions and theorem types; a separate mathematical reader checked the nonfixed reserve and full clock interface; fresh integrated compilation and all audits passed | VERIFIED for those finite formal statements |
| Independent-exponent classifier, Sections 2–6 | Root and a separate reader checked tuple-dependent rotation, complete denominator, template exception, explicit cutoff, and original Matveev constant. The finite automaton now explicitly covers every initial cycle phase and rejects the empty tuple | VERIFIED WITH CLARIFICATIONS as a written argument using the stated published logarithm theorem; not a Lean classifier |
| `Collatz/AffineDispatcher.lean`, all 13 public declarations | Root inspected source retention, current degree/offset, physical clock, negative invariant, common grade, and partner merger hypotheses; fresh integrated compilation and audits passed | VERIFIED for the stated compositional rules; successful universal coverage remains OPEN |
| `Collatz/SourceTargetInduction.lean`, all 12 public declarations | Root inspected the nested induction, downward interval, original-target comparison, independent clocks, and exact exponent-three-to-two capture; fresh integrated compilation and audits passed | VERIFIED for mixed-induction soundness and the stated capture class; `MixedCover` remains OPEN |
| One-pass automatic capture | Exact integer replay at `e=1,q=17,[2,3,4],t=63`; all source-cut paid ceilings are missed | REFUTED for one-pass capture. The example does not refute independent-clock merger coverage |
| Reused affine repair | Exact symbolic replay of `T^8(256w+63)=T^7(128w+31)=729w+182` for every nonnegative parameter via constant-parity affine steps | VERIFIED as a reused family; credit belongs to PR185's `prefix_language_rules.json`, row `[1,8,63,31,1]` |
| Last-contact measure, capacity, Green, and source-tail identities | Root inspected the actual ordinary inverse paths, the global antichain, nonnegative sums, and escaping-domain restrictions; independent mathematical cross-read recorded in the execution report | SOURCE-QUALIFIED written deductions, retaining the analytic assumptions of PR185 and checkpoint 8 |
| Sharper full-word cutoff in `SHARPER_BLOCK_CUTOFF.md` | Root reconstructed the real height chain, rational upper coefficient, and explicit logarithmic cutoff; concurrent PR183 contribution credited | VERIFIED as a written refinement under the same published logarithm input; not a new Lean cutoff theorem |
| `L²(eta)` channel extension | Root and a separate reader reconstructed the weighted Cauchy–Schwarz bound, actual endpoint counts, phase signs, and uniform finite-source tail control | SOURCE-QUALIFIED written deduction, restricted to sources supported on the canonical last-contact antichain |

No verdict in this table extends to a whole source PR or a later head.

## Literature and priority

The independent-exponent note cites Matveev's original 2000 paper,
Corollary 2.3, from the publisher PDF. Both the coefficient convention and
the explicit specialization were checked. The external logarithm theorem
is not installed as a Lean axiom. The original article is:

<https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng>

The classical local-minimum cycle framework and effective logarithmic
separation appear in the Simons–de Weger author revision:

<https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf>

The recent primary manuscript *Height and periodic-dictionary complexity for
rational Collatz trajectories*, rStation paper 15, v2 (2026-10-27), already
states a stronger dictionary-complexity lower bound and gives the elementary
repeated-block divisibility mechanism. It was consulted for priority and
scope; its full theorem is not imported into the present classifier:

<https://rstation.ai/problems/collatz/papers/15>

Accordingly the new result is described as an explicit classifier and a Lean
arithmetic kernel, not a new general complexity mechanism or an improved
numerical cycle exclusion.

## Reconciled descriptions

1. PR186's guide snapshot calls PR183's four recent formal scripts pending
   replay. The later frozen PR183 head above reports their completed 69-theorem
   replay. The current mathematical gap is coverage, not missing execution.
2. PR186's band-clock upgrade task overlaps checkpoint 6's already checked
   finite entrance bound and its written polylogarithmic consequence. It is
   not counted here as a fresh unresolved finite theorem.
3. The new dispatcher credits checkpoint 6's arbitrary signed lift and PR185's
   smaller carry language. Its addition is arbitrary-edge composition with
   a literal suffix and rank-paid handoff, not rediscovery of the signed lift.
4. The short-contact limit alone is qualitative. The earlier finite-front
   estimate remains a stronger quantitative upper bound under the joint
   inputs. Neither statement supplies a lower contact rate or a contradiction
   without a new lower estimate.
5. The late PR183 continuation reaches the same qualitative independent-block
   classification and an equivalent nonpositive signed-carry transition.
   These are credited as concurrent derivations, not counted as additional
   distinct mechanisms. The new combined results are the sharper complete-word
   cutoff, the joint source-grade/target induction, and the uniform
   `L²(eta)` extension for sources on the canonical last-contact antichain.
