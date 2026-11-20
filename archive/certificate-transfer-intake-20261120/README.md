# Supplied certificate-transfer material, preserved unchanged

These files were supplied by the user for analysis and publication to
the Collatz repository. No author-stage mathematical label in a source
file is silently promoted to an accepted repository theorem.

| Preserved source | Contents |
| --- | --- |
| [code-v1.zip](code-v1.zip) | Original 12-file `collatz-16k1-32k1-code.zip` reviewed in the preceding discussion. |
| [code-v2.zip](code-v2.zip) | Updated 15-file `collatz-16k1-32k1-code(1).zip`. |
| [code-v2/](code-v2/) | All 15 members of the updated ZIP, byte-for-byte. |
| [certificate-density-draft.pdf](certificate-density-draft.pdf) | Separate unfinished 18-page user-supplied manuscript, "Collatz certificates under x -> (x+1)/2: a density-one theorem and the open remainder". The original PDF bytes and embedded title are retained. |

The second ZIP changes only its README among the original twelve files
and adds `problem2.py`, `conv.c`, and `conv_dfs.c`. In particular the
original `research3.py` checker still has the two first-hit/fixed-clock
false negatives discussed in the review. Its programs print some failure
counts without returning a failing process exit status.

The PDF refers to its own numbered results and an embedded appendix.
It is a separate thread, not the missing forward-pair write-up cited by
the ZIP. The PDF's code is printed text with line wrapping; extracted
indentation is not treated as an original executable. The active checker
is a separately identified reconstruction.
No executable companion to that PDF was supplied separately.

The [source manifest](../../reports/2026-11-20-certificate-transfer-intake/source-manifest.json)
records original names, SHA-256 hashes, sizes, archive members, and the
previously prepared problem statements. The
[review](../../reports/2026-11-20-certificate-transfer-intake/README.md)
states corrections and replay coverage. The
[research packet](../../research/certificate-transfer-intake-20261120/README.md)
contains the proposed mathematical reconstruction.

Preservation is not endorsement of every source assertion or experiment.
The user supplied these generated research materials for inclusion;
existing source notices and attribution are retained.
