# Published scientific checkpoint

The scientific checkpoint was pushed to PR193 on 2026-11-24 at commit
`3ee92a03e3e304eb7831334d8ccc01d299107d85`, with tree
`512e233c3bb95ad37a9ca39cb6d2c79c43a8ef13`.

The GitHub API returned exactly the locally tested tree. The branch was advanced
from `4dcc03aa236fd64b7dc1c04d2574d0f56cc24f79` with an expected-head lease and
without force. A subsequent PR read returned the new scientific commit, and
a fresh Git fetch returned the same commit and tree. The fetched tree had no
differences from the locally tested scientific checkpoint.

The complete clean checkout was then switched to that actual published commit.
`python -X utf8 -B tools/validate.py` passed there, writing its receipt outside
the checkout. `PUBLISHED_CHECKOUT.json` preserves that receipt; both its before
and after records identify the published commit and tree, with 413 tracked
files. The validator checks repository integrity and its listed bounded
regressions; it does not prove Collatz or validate the analytic literature.

The separate mathematical audit remains `LEAN_AND_CONTROLS.json`: eleven new
public declarations in three Lean modules and four control programs in normal
and optimized Python. Its source hashes cover the frozen scientific content.
The receipt follow-up changes only this report and `PUBLISHED_CHECKOUT.json`.

PR193 remains a draft research PR. Universal convergence and the required
nontrivial-cycle exclusion have not been established.
