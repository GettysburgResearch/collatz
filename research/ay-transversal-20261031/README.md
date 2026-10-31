# AYH continuation: transverse mergers, proof-language normalization, and inverse credit

**PROPOSED. Collatz remains unresolved.** This pass follows the recovered unpublished packet at `../ay-return-recovered-20261031/RECOVERY.md` and the original PR #141 source at `ccf1887cd07502c3772f8ccbd77c8dab22ea51c5`. It does not restore the interrupted workspace byte-for-byte. All proofs here are newly reconstructed; the current session did not have an independent-agent launcher or an external reviewer.

## What actually changed

1. A general proof-normalization theorem eliminates **every proper-ancestor edge**, not just the earlier `f^h` family, from the specified suffix-closed forward rank language. This reconstructs and strengthens the late unpublished no-gain claim rather than assuming its missing proof.
2. A genuinely transverse merger rule strictly enlarges that language. An explicit two-parameter family has no admissible old forward edge, but has a new budgeted smaller-rank diagram. The family extends to more than 10,000-bit sources in the supplied tests; the theorem is for arbitrary eligible parameters.
3. An exact finite-state potential supplies the explicit natural rank `7t+V(c mod 6561)−1` for inverse mixed-base conversion. It improves the universal inverse-cone budget from `4t−2` to `floor((7t+17)/3)`. A separate four-digit cover gives `3t`. Both are **conversion** bounds, not Collatz termination bounds.
4. A counting theorem explains the limitation: any universal inverse compiler needs asymptotic worst-case length at least `1.641794… t`, already above the `log_2(3)t` threshold for universal numeric contraction. The proportion of ternary tails that admit a contracting same-prefix binary preimage is at most exponentially small at large width. An increasingly large inverse dictionary is not, by itself, a route to full coverage.

Read [the proof-language and merger results](TRANSVERSAL.md) and [the finite-state order and counting bound](INVERSE_CREDIT.md). Programs, the finite certificate, and deterministic outputs are in `../../experiments/ay-transversal-20261031/`. Fresh execution scope and source hashes belong in the review receipt, not in the original pass's validation record.

## Strongest remaining obligation

The extended search is a total decision procedure for its **finite rank-decreasing proof language**, with outcomes PROVED or UNRESOLVED. It is not a total successful Collatz selector. For the census of 4,096 positive odd seeds, strict forward-only search proves 154 and adding the transverse menu proves 156; the budgeted figures are 139 and 142. The majority remain unresolved by this deliberately small language. The infinite family proves a strict *one-step certificate-language* enlargement; it does not prove convergence of all its endpoints.

The next decisive task is not another ancestor dictionary: it is a source-persistent family of genuinely transverse diagrams that covers the remaining low-rank barriers, or a different global rank with a proved coverage theorem. In particular, 7 and 9 remain unresolved by the current strict language. No averaging, periodic-density claim, or finite census fills that gap.

## Attribution

The mixed binary/ternary SRS and its Collatz equivalence are due to Emre Yolcu, Scott Aaronson and Marijn J. H. Heule, *An Automated Approach to the Collatz Conjecture*, arXiv:2105.14697, Journal of Automated Reasoning 67, article 15 (2023). The elementary equivalence `U(4m+1)=U(m)` is old; it appears, for example, in the discussion of equivalent odd integers in the 2010 paper *The 3x+1 Problem as a String Rewriting System* (Sinyor), DOI 10.1155/2010/458563. The contribution claimed here is the exact rank-language separation, normalization argument, and finite credit certificate—not discovery of that equivalence or external priority for all component identities.
