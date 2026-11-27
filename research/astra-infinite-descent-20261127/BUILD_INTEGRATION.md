# Flat Lean modules and private imports

The first fresh fourth-checkpoint rebuild of source commit `3104ffab7beaed8789548d84188d260cb81ffb36` stopped at the pinned PR206 `BasinTransport.lean`: Lean could not resolve its imported private theorem `halve`. The failed receipt is preserved in `CHECKPOINT_04_FAILED_BUILD.json`. That attempted build is not a successful validation.

All packet imports and output files use flat module names. The replay script had allowed Lean to infer a different logical module name for nested source paths. This inconsistency becomes visible when a source uses Lean's `module` header and `import all` to access a private declaration. The compiler help specifies that `-R` controls the package root from which the input module name is calculated.

The replay script now passes `-R source.parent` for every compilation, including the generated audit. This makes the logical module name agree with the flat import and output names. It preserves every pinned proof byte. A targeted recompilation of `TernaryItinerary` and `BasinTransport` passed with only `propext`, `Classical.choice`, and `Quot.sound` in their printed axiom reports. The subsequent full fresh build and all-declaration audit, rather than that targeted check, determine the checkpoint's final validation status.

## Mixed module styles in the aggregate audit

The second fresh run compiled all 74 mathematical modules, then the generated audit failed because explicit `import all` is only valid in the new module style. Adding `module` was not an appropriate repair: that style cannot import the packet's legacy modules. Both actual errors are retained in `CHECKPOINT_04_FAILED_AUDIT.json`.

The correct audit remains a legacy root with ordinary imports. Pinned Lean source `Lean/Elab/Import.lean`, `processHeaderCore`, chooses the private import level for such a root; `Lean/Environment.lean` documents and implements transitive private loading. A targeted aggregate check of the freshly compiled objects then passed 3,117 declarations, including 1,486 private declarations. In particular the imported PR206 private helpers and kernel-computed finite certificates were present. The script also checks that every packet module appears in the declaration audit. The final successful receipt comes from another complete end-to-end run of the corrected script, not from counting either failed invocation as a success.
