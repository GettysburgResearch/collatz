# Verification of the actual-certificate and ordered-gap packet

The scientific files have local and independent Lean checks. A clean complete checkout replay will be recorded here at its exact science commit before the branch is published. This initial text does not claim that replay has occurred.

The schedule rebuilds three exact project dependencies and all six new modules, then audits every public theorem, runs both finite-control scripts in ordinary and optimized Python, and invokes the repository validator with its bounded regressions. The output directory must be outside the checkout and must not already exist. The reused external dependencies are Lean 4.34.1 and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`; all nine project objects are freshly generated.

[Replay driver](replay.py) · [Root mathematical review](ROOT_REVIEW.md) · [Independent core/cycle/intake review](core-review.md) · [Independent core review](bridge-review.md) · [Independent bridge review](cycle/BRIDGE_REVIEW.md)
