# Verification of this checkpoint

The three specialist modules and bounded controls were executed during
development and independent review. The coordinator's clean scientific
commit replay is pending at the time this file is first committed. The
final publication receipt will replace this paragraph with the exact
commit, tree, source hashes and observed executions before the branch
reference is advanced.

The reproducible entry point is [replay.py](replay.py). It requires a
clean complete checkout and a new output directory outside that checkout.
It builds the three new Lean modules with warnings as errors and
auto-implicit variables disabled, checks every requested transitive
axiom inventory, runs every new Python control with and without
optimization, and runs the repository's default integrity driver.
The pinned prebuilt Mathlib/package runtime is reused; no whole-Mathlib
rebuild is claimed.

These checks do not formalize Evertse's theorem, the infinite weighted
duration estimate, or the imported probability estimates. Their written
proof and review scopes are in [ROOT_REVIEW.md](ROOT_REVIEW.md).
