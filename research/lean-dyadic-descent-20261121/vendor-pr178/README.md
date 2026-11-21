# Frozen PR178 dependencies

These three Lean files are copied byte for byte from PR178,
`0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`, at
`research/band-return-20261121/lean/`:

- `ReturnFourier.lean`: exact finite rotation error estimates.
- `MarkPhase.lean`: marked-value phase bounds and the finite kernel.
- `MarkFrequency.lean`: kernel estimates and qualitative temporal density.

They are credited dependencies, not new theorems of this continuation.
Their original definitions and proof bodies are unchanged. They import the
same pinned PR173 `ForwardSection.lean` used by this packet. Exact Git blob
identifiers and SHA256 values are in the parent `SOURCES.json`.

The new work is in `AnalyticCoupling.lean` and `TemporalDensity.lean`: a
uniform harmonic error budget on finite distinct prefixes, explicit Fourier
bounds, and a uniform logarithmic temporal-count bound. The replay script
checks the vendor hashes before rebuilding them and the new modules.

Original repository licensing and notices remain applicable.
