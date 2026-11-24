# Pinned finite directed-return certificate

`SingleReturn.lean` is copied byte for byte from PR 193, commit
`67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e`, at
`research/astra-global-resolution-20261124/rewriting/SingleReturn.lean`.
Its Git blob is `797e2629e931551cc5913acbe7ef314aea489cd2` and its SHA-256 is
`12890afd898231aa543a9818f61164c03afd903b4c7835fdaf9fb02c8e7f91f7`.

[Original file](https://github.com/GettysburgResearch/collatz/blob/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/rewriting/SingleReturn.lean)
and [written certificate](https://github.com/GettysburgResearch/collatz/blob/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/rewriting/SEVEN_RETURN.md).

The certificate's finite cover and global directed implication are prior PR 193 work.
The new `FourSuffixClosure.lean` consumer uses `singleReturnCover` after deriving
tripling invariance from the four multiplier comparisons. The replay script
compiles this source anew, including its kernel-evaluated finite cover, and
queries all three of its public theorem declarations. No probability or
positive-density theorem is imported into that Lean implication.
