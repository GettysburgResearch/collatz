# Targeted source freeze

The pass read the35 most recently updated open PR records, then fetched
the current research sources needed by the closing attacks. This is a
targeted source selection, not a new review of the full repository.
Main remained ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a.

| PR | Frozen full head | Use in this pass |
|---|---|---|
|146|f431078244e868dc699fad011044f0d5e7f76437|Current reverse closure and ordinary merger setting; exact older reverse criterion imported through PR174.|
|164|9582df78eb4d768eb748d3cf367ba97582308a52|Updated direct reverse-tripling context; no theorem from this head silently assumed.|
|171|2bd243b3e05eaa5543adeb2894637b053c9662ca|Critical negative moment and recurrent-section continuation.|
|172|b22d94240f3d44a04231508e5dfe9a4947a57125|Uniform arbitrary-tail descent, smaller five failures and explicit unresolved selector costs.|
|173|a09eb47197cd99f218b3fa013c681df65ea0f69a|Lean shrinking-interval criterion, used to identify its missing upper survivor estimate. Its Mathlib development is not imported here.|
|174|7034109ed60a26bc49824e1ed43c239ceca81194|Dependency-free Lean definitions, reverse closure reduction and shadow identities.|

## Imported Lean sources

The following files are byte-identical copies from PR174 under
research/psi-closure-20261121/lean/:

- Collatz.lean
- Collatz/ReverseBasin146.lean
- Collatz/Closure.lean
- Collatz/Shadow.lean

[upstream-files.json](upstream-files.json) records their source and local
paths and SHA-256 values. The reverse-basin file itself credits PR146
at e238c63a5d57f96bb063b7472498d1977df51951 and identifies its core-only
shim. That inherited source pin is preserved. Our own source freeze
does not retroactively attribute its bytes to the later PR146 head.

The imported powers-of-four identity and one-step component facts are
credited to PR174/PR146. The new paired profile, ordinary expanding
cylinder, and first-return claim are separate declarations in
Closure/PsiDescent.lean. The older conditional full-conjecture theorem
retains its unproved hypothesis.

## Runtime used for execution

Official release: https://github.com/leanprover/lean4/releases/tag/v4.34.1

The official Linux archive's SHA-256 was checked before extraction:

    47bf4bbd78f70c2e9670598ab7124d92b6efb7330ff33e5fbb4030f6fd72e4e4

The executable reports Lean4.34.1, release commit
5045d0056413266e57c625dcd7c365b10e377c52. No third-party package is
required by this checkpoint. Exact build execution and theorem-axiom
output are recorded separately; a source file alone is not a build.
