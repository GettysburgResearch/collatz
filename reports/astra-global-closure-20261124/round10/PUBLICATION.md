# Verified round-ten scientific publication

25 November 2026. **Partial research; Collatz remains OPEN.**

The scientific commit is
[`d22a248361dca84a554da188da84aba425e5613e`](https://github.com/GettysburgResearch/collatz/commit/d22a248361dca84a554da188da84aba425e5613e).
Its tree is `6f543f30bb1a0fce28488bc2d93cc55e7bc9b435` and its parent is
`51e2c43a60950e446eabe782c5b1cb1d0ae11bab`. The tree exactly matched the
locally committed and validated candidate tree. Publication appended to
the existing `research/astra-global-closure-20261124` branch using a
non-forced update with the exact expected prior head. A fresh PR195 query
confirmed this new head and the existing open draft status.

The coordinator fetched that exact published commit and created a new
complete, clean checkout with 832 tracked files. The command

```sh
python -X utf8 -B tools/validate.py --receipt /absolute/path/outside/checkout.json
```

passed all five required commands. The unmodified execution receipt is
[published-science-validation.json](published-science-validation.json).
The 46 frozen source/evidence hashes in [SOURCE_HASHES.json](SOURCE_HASHES.json)
were separately checked against that exact remote checkout and all matched.
The copied validation receipt and this publication note are outside the
scientific manifest; neither changes a scientific source or Lean module.

The final branch head containing these two receipts is checked separately
and reported in the PR description. The final readback is not claimed as
an event already contained inside its own commit.

Mathematical evidence is separate: the [Lean receipt](lean/receipt.json)
records seven rebuilt project modules and 65 selected axiom inventories;
the [finite controls](controls/control-replay.json) record six executions
with matching normal/optimized output. The universal Lean consumer still
takes the explicitly open `FrontierMerger` premise. Repository integrity,
compiled finite lemmas and source-qualified analytic estimates do not
constitute a complete proof of Collatz.
