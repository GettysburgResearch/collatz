# Sources, attribution, and exact limits

## Frozen project inputs

Main observed: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The live parent PR #124 was re-read at
`1d4dfc103055648def3db73860778a383a91ea3c`, tree
`00b4625229af3d07da248a90fcdea889541a86cf`.
The mounted published archive supplied its complete AAC proof, generator,
verifier, compact artifact and full finite corpus. This continuation is not
a fresh audit of all repository branches or all older mathematics.

* [AAC proof](https://github.com/GettysburgResearch/collatz/blob/1d4dfc103055648def3db73860778a383a91ea3c/research/astra-exit-merging/adaptive-companions/PROOF.md): same-centre lifting, the three-companion seed rules, finite even-adjacent and 5-mod-8 adjacent exits, affine clock restrictions. Those clauses are credited and restated only where needed; their statuses are not promoted.
* [AHR proof](https://github.com/GettysburgResearch/collatz/blob/bf0696f888442c82a4c6cdc1df36becf8550295a/research/astra-exit-merging/hard-return/PROOF.md): H return with arm swapping, exact finite itinerary compiler, and the 3003/999 synchronous mismatch. The new CRT entry uses this finite language, not an unproved assertion that every H state eventually merges.
* [AEM proof](https://github.com/GettysburgResearch/collatz/blob/65c91ecea97d9ebf931eb1d9284b7950182a298e/research/astra-exit-merging/PROOF.md): original-root comparison convention and early two-exit certificates. Its stronger one-third factor is not attached to different companions by analogy.

The new proof bodies are AES-001--006. The negative-centre prefix identities
are elementary consequences of the parity-affine formula; the two-step
adjacent contraction is also elementary. The contribution claimed here is
the precise conditional certificate, the parity-of-valuation choice that
completes the missing seed's finite entry, and their original-root-compatible
composition, not a claim that each elementary ingredient was unknown.

## Bounded public literature check

A bounded search located the related primary-source paper by Patrick Wiltrout
and Eric Landquist, *The Collatz Conjecture and Integers of the Form
2^k b-m and 3^k b-1*, FUEJUM 17 (2016), 1--5:
<https://scholarexchange.furman.edu/fuejum/vol17/iss1/1/>.
Only its bibliographic landing-page description was consulted in this pass,
not the full paper. It is background, not a theorem dependency or a basis
for establishing priority. No exhaustive literature or novelty audit was done.
All mathematical arguments used by the new certificates are written here.

## Scope of the finite evidence

The generator concatenates proved words. The verifier instead steps the
actual two trajectories for independently determined clocks. Direct-family
sources are reconstructed in the odd quotient w, while the generator solves
in u. Hard-family sources use an odd-modulus C equation in the verifier and
a dyadic w equation in the generator. The finite itinerary compiler runs
forwards in the verifier and backwards in the generator. All 411 tested
whole-family cylinders are checked symbolically for every nonnegative
translate, separately from literal finite-path replays.

These are same-author implementation checks, not independent mathematical
peer review or Lean formalization. The new theorems remain PROPOSED.

The ambient grid is exactly the parent's k=1..6, positive odd u<8192 grid.
The old-class counts and source witnesses are compared, not a new larger
sample presented as improvement on an unrelated baseline. The generator
retains complete old and new grid rows in --full output. Known budget and
outside-return cases are retained, including examples that admit an ordinary
forward-descent certificate outside this particular selected comparison.

## Boundaries that must survive reuse

1. The odd-spine factor m<n/2^k requires k>=3. The exact formula applies
   before that cutoff; k=u=1 is handled separately, not by strict descent
   from 3 to itself.
2. The complete entry statement is only for n=8^k u-5 with odd positive u.
   It does not cover every positive integer, and entering H is not merging.
3. AES-005's all-states lower bound applies to its direct final merger.
   It is not automatically a lower bound through appended H returns.
4. q=1 is a real fixed point of the adjacent contraction, with unequal raw
   phases. The selection proof uses q>1 and a finite nonzero valuation.
5. The general negative-centre merger requires all displayed source-order,
   periodicity and dyadic-gap guards. Its no-descent strengthening also
   requires the prefix coefficient condition.
6. Finite-list CRT constructions choose a source for each prescribed list.
   They are not one all-time ordinary trajectory or an eventual-entry theorem.
7. Main, prior proofs, canonical statuses, workflows, settings and licenses
   are not changed. Direct Git failed DNS; API publication and blob readback
   do not constitute a complete checkout or a full-repository validation run.
