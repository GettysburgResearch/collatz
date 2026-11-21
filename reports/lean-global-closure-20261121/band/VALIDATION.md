# Forced-section continuation: actual execution record

## Scientific commit and source

- PR: <https://github.com/GettysburgResearch/collatz/pull/175>
- Scientific commit: `d27ae7c160757a3c77e515136b1cd479a23de9b2`
- Scientific tree: `e57c97f919076cf6634e735f37a807bc6b82d480`
- Complete checkout: 374 tracked files, clean before and after execution.
- Upstream section source: PR173 at `fa0c9e2a2851e6324391e39c17afcb5913185aec`.

The checkout was created by a fresh direct GitHub clone of the published
branch, without a shallow, filtered, or partial checkout. Its actual head
and tree were checked before the commands below. The source manifest
confirmed that the four vendored upstream files are unmodified.

## Fresh Lean build

[full-build.json](full-build.json) records an actual invocation of
`research/lean-global-closure-20261121/build_band.py --full`, from that
published checkout, with the exact command for each module.

All **17 compilation units, including the package entrypoint, passed**.
This includes the four earlier proof modules, four frozen upstream modules,
eight new section modules, and the entrypoint. Every project output was
written into a fresh directory; no previously compiled project module was
on the search path. Only the pinned mathlib/dependency cache was reused.

- Lean: `4.34.1`, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Every compiler command used `-j1`, `-DwarningAsError=true`, and
  `-DautoImplicit=false`.
- Total recorded compiler time: 119.901 seconds.
- 96 printed axiom reports; the union is exactly `propext`,
  `Classical.choice`, and `Quot.sound`.
- The independent finite reset witness has no axiom dependencies.
- Receipt SHA256:
  `7af5237541f9bce6fcf5cffb53abfe15d7f74033f7a2af88207f9fae84d38502`.

The package's Lake configuration also loaded successfully with the new
vendored-source library: `lake env lean --version` returned the pinned
Lean version. This was a configuration/runtime check, not a second claim
of a complete Lake build.

## Complete-checkout repository gate

[repository.json](repository.json) records the successful command

```sh
python -X utf8 -B tools/validate.py --receipt /workspace/scratch/957bb0caa6f2/band-published-repository.json
```

All five required commands passed at the scientific head and tree above.
Receipt SHA256:
`cd71ca2c77193e8c9eb3eb9243b96cca0f6cb47a3ca58ae92c68b3d1d1c6885c`.
These repository checks concern integrity and scoped replay fixtures;
they are distinct from mathematical proof checking. The optional broad
regression bundle was not run in this continuation.

## Receipt follow-up boundary

This report and the complete build/gate receipts are added in a follow-up
commit together with the final segment-minimum attempt note and documentation
links. They do not change any Lean source, the build driver, the toolchain,
the dependency manifest, or the Lake configuration. Every one of the 17
current Lean source hashes was compared with the fresh-build receipt before
publication of the follow-up. The repository gate is run again at the actual
follow-up head; that final receipt is embedded in the PR body to avoid a
self-referential receipt commit.

These executions establish the declarations actually present in the proof
files. **They do not establish universal Collatz convergence.** The universal
eventual descent assertion for marked returns remains open.

## Preserved earlier evidence

[development-builds.json](development-builds.json) contains successful
individual-module commands before the scientific checkpoint. It explicitly
distinguishes those development executions from the fresh complete build.
[pre-band-final-repository.json](pre-band-final-repository.json) preserves
the earlier PR175 final-head receipt that was previously embedded in the PR
body. It applies to `8ba80e8cf3d243850611b477cf149dfb3dab2c01`, not to the
new continuation.
