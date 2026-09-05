# Shared review, a small trusted core

Anyone can explore. Contributors review one another. Integrators maintain the accepted research record; owners manage access and project-level decisions. The founder need not review every PR.

## Responsibilities

| Role | Intended access | Normal work |
|---|---|---|
| Public participant, once public | Reading and fork PRs | Explore, report gaps, submit work, review |
| `polymath-contributors` | Write | Own branches and PRs; review others' work |
| `polymath-integrators` | Maintain | Triage, coordinate reviews and integrate scoped results |
| `owners` | Admin | Access, settings, infrastructure and release oversight |

The [dated security receipt](SECURITY_REVIEW_2026-09-05.md) records the observed setup, not a permanent guarantee of current permissions. Owners administer actual membership and branch rules. [CODEOWNERS](../.github/CODEOWNERS) nominates core reviewers and owners for infrastructure changes; it does not itself enforce approval. Before launch, owners must decide and verify PR requirements, stale-review dismissal, and force-push/deletion protections. See the official [code-owner documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).

## Two review depths

**Exploration:** check that the question, evidence, dependencies and uncertainty are legible. Conjectures and failed approaches may be accepted as research notes. Merging a note does not make its theorem verified. Avoid requiring a proof before someone is allowed to investigate.

**Accepted mathematics:** someone other than the author reconstructs the load-bearing argument at an exact commit, checks assumptions and scope, and records a verdict. An integrator checks that this supports the proposed status and placement. A reviewer can also integrate a contribution when independent of its authorship; an extra approval round is not automatically necessary.

Different chats using the same model can repeat the same mistake. Seek fresh derivations, adversarial examples, different tools and human scrutiny where available. Agreement among agents is not a substitute for a proof.

## A useful review report

Record the exact `(PR, SHA, path, claim ID)`; what you reconstructed; verdict and scope; first gap or necessary correction; checks actually run; and explicit omissions. Use VERIFIED, VERIFIED WITH FIXES, GAP/BLOCKED or REJECTED at the appropriate claim level. A conditional implication does not establish its hypothesis.

When the author changes the proof, review the new commit and affected dependencies. Preserve the old report. A byte-identical import needs identity and placement checks; newly synthesized mathematical wording has its own review boundary. A typographical correction must not conceal a new hypothesis or conclusion. Follow [integration practice](INTEGRATION_PRACTICE.md).

## Software and execution

Checker, automation, dependency and access-related changes need review appropriate to the code. The repository integrity workflow uses GitHub-hosted runners with a read-only token and no persisted checkout credentials; it does not use repository secrets or privileged PR events. Actions may still be disabled by repository policy. A passing run establishes only its explicit structural and bounded-regression scope.

Never run unfamiliar code with repository or personal credentials. Do not expand the integrity workflow into arbitrary branch-provided experiments, privileged jobs, caches shared with untrusted code, or deployment without a separate infrastructure decision. Review workflow edits themselves before enabling or approving a run.

## Keep the project moving

Preserve useful failed attempts and exact refutations. Track the first missing theorem and dependency consequences so corrections reach downstream claims. New work should branch from current main rather than repeatedly merge old integrated research snapshots. Source-PR closure requires an explicit disposition and durable destinations; reducing the PR count is not a research result.
