# Published round-four checkpoint

The scientific packet was published on PR195's authorized branch `research/astra-global-closure-20261124` using a compare-and-swap update from `8edc24b576e7c7da56f99d882ce6fd1e014ee730`. The remote tree exactly matched the locally tested tree before the update. No force update was used.

| Object | Identity |
| --- | --- |
| Local scientific commit | `733b04b8a91e49c0f8e4e39c1971a927029fd514` |
| Published scientific commit | `e937a315b5efa81d8f0cfb939aa5aea54af560b1` |
| Identical scientific tree | `90dc94a6737d58ab50bc3ec0bccc6ec7c7a9876a` |
| Complete scientific checkout | 540 tracked files, clean before and after validation |
| New Lean evidence | Five modules, 28 selected declarations, source hashes unchanged |
| Exact finite replay | Four scripts, normal and optimized execution, eight passing runs |

After publication, Git fetched the remote branch into a separate local verification branch. The actual remote scientific commit passed all five default commands in `tools/validate.py` in a clean complete checkout. [Local receipt](local-checkout-validation.json) · [Fetched remote receipt](published-science-validation.json)

This record and those two receipts are a subsequent documentation-only addition. The 27 scientific-source and review entries in [SOURCE_HASHES.json](SOURCE_HASHES.json) are unchanged. The final receipt commit is fetched again and checked before the PR's published head and final validation are reported. Its own identity is reported on [PR195](https://github.com/GettysburgResearch/collatz/pull/195), avoiding a self-referential committed receipt.

[Research overview](../../../research/astra-global-closure-20261124/round4/README.md) · [Root reconstruction](ROOT_REVIEW.md) · [Lean replay](lean/receipt.json) · [Control replay](controls-replay.json) · [Latest intake](LATEST_INTAKE.md)

The mathematical boundary is unchanged: finite declarations passed Lean; the asymptotic proofs remain written; T3, M, P, S and R retain their named source qualifications where used. Repository integrity does not establish the universal Collatz statement.
