# Pass 2: residue-locked component geometry

**PROPOSED, not independently reviewed. No complete Collatz proof.**
Start with [PROOF.md](PROOF.md), especially CR2-003 (joint residue-window
coverage), CR2-004 (explicit compactification), CR2-005 (finite patterns in
every high relative window), and CR2-006/007 (two obstructions to closure).

The finite-pattern synchronizer is credited to #134/#132, with the exact
source and construction in the proof. The added result couples its endpoint
congruence to logarithmic size while retaining the same original component.

## Reproduce

Python 3.10 or later, standard library only, from this directory:

```sh
python -S -B experiment.py --output certificates.json
python -O -S -B experiment.py --output certificates.optimized.json
python -S -B verify_certificates.py certificates.json
python -O -S -B verify_certificates.py certificates.json
```

The two generated JSON files must agree byte-for-byte. Expected SHA-256:
`f9d0851705fd05958bfb6e3730b701d9514d6fc97aeaf881d55468e02667fa32`.
The 100,870-byte deterministic JSON is generated rather than committed.
It contains compact recipes for all original-source ladders and windows;
large integers are regenerated without floating arithmetic. The download
packet also includes this generated evidence.

`verify_certificates.py` imports neither the generator nor project modules.
It uses direct rational powers for the ideal net, instead of the generator's
incremental normalization, and reconstructs all displayed physical paths.
This is same-author implementation diversity, not peer review.

## Evidence distinctions

The generator's small grids literally replay 1,008,890 shortcut steps over
42,240 inverse edges. Its large source nets contain 6,272 additional edges
checked by exact compressed word identities. The checker verifies those
6,272 compressed edges, 64 complete composed window arms, and 32 four-block
roots with 352 literal shortcut steps. It does not rerun the small-grid census.
Normal and optimized output comparisons passed; ten checker mutations were
rejected. See [VALIDATION.json](VALIDATION.json) for exact receipts.

The giant example has 1,312,421 bits. This is not a convergence census or a
claim about exhaustive coverage up to that number. The all-window theorem
uses the written net proof, not just the 64 retained window samples.

## Open boundary

No global sublinear-variation bound, continuity theorem for arbitrary
component separators, or macroscopic convergent-block construction is
proved. The explicit finite colorings with large boundary variation are not
claimed to extend globally. The 5x+1 control receives the residue/logarithmic
construction, not the 3x+1 finite-pattern compiler.

No main/status/workflow/settings edits, full-checkout validator, remote CI,
formal proof build, independent review or exhaustive priority audit occurred.
