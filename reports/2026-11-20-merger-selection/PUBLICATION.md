# Published scientific content and exact validation

The scientific content commit is
`46e8f08c9109b7c74cb01fb5527858e0b885f80f`.
Its complete tree is `aee5b799e2f86a604e513fdbbf4f330c019b96ff`.

The GitHub tree was compared with the locally checked scientific tree
and was identical. The actual published commit was then fetched into a
separate complete detached checkout with 339 tracked files. On that
clean checkout, all **11** repository validation and regression commands
passed. The checkout identity was unchanged after execution.

[Exact execution receipt](content-validation.json).

The four new arithmetic programs had also passed on this exact content
tree. Their detailed finite reports are linked in [the execution
overview](README.md). Independent reviewers reconstructed the written
arguments and recorded exact file hashes. These are separate forms of
evidence: neither repository integrity nor a bounded replay is a formal
proof of the unbounded mathematical statements.

This record and the receipt are added in a subsequent documentation-only
commit. That commit does not alter any scientific note, proof program,
source pin, review, or previously recorded finite result. The
prepublication hash manifest remains a manifest of the scientific
content commit, not a self-referential hash of this later record.

The work is on branch `research/ordinary-merger-selection-20261120`.
The base remains main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The change is submitted for review; it does not assert a resolution of
Collatz or a complete successful ordinary selector.
