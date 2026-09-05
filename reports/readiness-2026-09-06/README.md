# Final repository-readiness pass

User-authorized cleanup and infrastructure preparation, not a new research wave or public-launch clearance. Publication: [PR100](https://github.com/GettysburgResearch/collatz/pull/100).

## Frozen inputs and disposition

Baseline main: `12eb510fb311588c2a3d6c0131b67aa642e79f91`, tree `22037ee8e96dab9caf106435e9beaffb04cf4a67`. Onboarding/security source: PR97 at `b85c227d9d1ccd2989e6f657ca80dbcc9e487640`. The research map, all proof/reference bodies, claim registries and A/B/D records remain unchanged. No new mathematical status, hypothesis or theorem is introduced.

The subject-based reading path is retained. The root now gives a contributor entrance and one reproducible validation command; AGENTS and integration guidance consistently require path-qualified source identities and keep exploration lightweight. The empty root `.gitkeep` is removed. Cache/virtual-environment files are ignored without ignoring scientific reports. No source branch or evidence archive is deleted.

## PR97 accounting

| Source component | Durable destination and treatment |
|---|---|
| CODEOWNERS | `.github/CODEOWNERS`, exact source blob `f4937a55cbe58b7d98c90f853fa798a5bc2560fc`; advisory until owners configure enforceable rules. |
| Contributor access template | `.github/ISSUE_TEMPLATE/contributor-access.md`, exact blob `65d553df49ec2a4344d2b77e66e2b0b25f7ea55a`; no private contact details requested. |
| Bounded security receipt | `docs/SECURITY_REVIEW_2026-09-05.md`, exact blob `51185f1581076a685d74c8dbcad887a9943a515e`; historical scan scope and exclusions unchanged. |
| README and contributor entrance | Adapted into root README and CONTRIBUTING, preserving research-first orientation and route-specific open obligations. |
| Phone walkthrough | `docs/PHONE.md`, with current official connection references; removes an unverified permanent all-repository installation assertion. Fresh-user end-to-end status remains untested. |
| Shared review | `docs/REVIEWING.md`, retaining contributor/integrator/owner responsibilities without treating a dated permission or plan snapshot as permanent. |
| Release gates | `docs/PUBLIC_RELEASE_GATES.md`, with actual outstanding operational, privacy, licensing and walkthrough decisions. |

The source PR preserves all original wording at its frozen head. After landing and rechecking that head, PR97 can be closed as absorbed with these destinations. No mathematical source PR is closed merely to reduce the queue.

## Integrity and portability

The original `tools/check_review_integration.py` was materialized and authenticated against its 11,510-byte Git blob `55a083e775af693bcbfc176c6079f08d8f78bd16` before modification. The change leaves the exact A/B assignments, source/review byte pins, namespace separation, pending flags, artifact distinctions and optimized legacy guards intact.

Windows can now use Git-index executable/symlink modes while still hashing actual working-file bytes. POSIX keeps filesystem-mode verification. No content is substituted from Git's index, and no line endings are silently normalized by the checker. `.gitattributes` uses LF for active text and raw-byte rules for frozen/source-pinned packets. This is not a rewrite of any historical artifact.

`tools/validate.py` wraps the existing structural and D follow-up checks, records the actual commit/tree, refuses dirty/incomplete/sparse inputs, retains child failures and can write a JSON receipt outside the checkout. Optional bounded regressions do not include large historical experiments. `tools/test_validation_driver.py` tests its fail-closed behavior using an explicitly synthetic repository, never represented as a Collatz checkout.

## Actual local evidence

See [validation.json](validation.json) for exact software/configuration blobs, commands, exit codes and stdout. Executed on the local materialization:

- Existing eight rejection fixtures: PASS, normally and under `-O`.
- Eleven real-Git mode/content/coverage controls: PASS in both modes; Windows mode selection simulated on Linux, not a native Windows full run.
- Seven driver/receipt/refusal fixtures: PASS in both modes.
- Fourteen LF/CRLF frozen files survived an actual local clone with `core.autocrlf=true` byte-for-byte.
- Four Python tool bodies parsed; workflow YAML and least-privilege configuration passed static checks.

These are software/configuration tests, not new theorem verification or a complete repository execution. Source and final-tree publication readback are recorded in PR100 separately from these local runs.

## Infrastructure decision and remaining execution gate

The user's authorization for this final pass includes configuration and restructuring. This pass adds a deliberately bounded, read-only GitHub-hosted integrity workflow rather than another research workflow: `contents: read`, ephemeral Ubuntu runner, ten-minute job cap, no supplied secrets, no persisted credentials, no caches, no deployment and no privileged PR-target event. The checkout action is pinned to `3d3c42e5aac5ba805825da76410c181273ba90b1` (official v7.0.1 release inspected during this pass). The same validation command is used locally and in the workflow; the JSON receipt is printed into the run log.

Primary configuration references: [GitHub secure-use guidance](https://docs.github.com/en/actions/reference/security/secure-use), [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1), and [official ChatGPT/GitHub connection instructions](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt). They support tooling choices, not mathematical claims.

**No full remote run is claimed.** The local environment still cannot resolve GitHub for Git/network checkout. The source administrative receipt reports Actions disabled; querying the new PR's workflow runs returned none. Available connector actions do not expose the repository's Actions-enable setting. GitHub's code-owner error endpoint is also not exposed by this connector, so team resolution is an explicit owner check, not a claimed validated setting.

Issue96 remains open for a real complete-checkout receipt, owner-approved terms/provenance, privacy/security/visibility and branch-rule decisions, and the fresh-user walkthrough. The workflow is prepared, not a green status badge. No membership, license, visibility, branch protection, history or organization setting is changed by this pass.
