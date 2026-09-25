# Arithmetic component rigidity — active proposed research

**PROPOSED; no complete Collatz proof and no independent mathematical acceptance.**
Map: unabsorbed shortcut T(n)=n/2 for even n, (3n+1)/2 for odd n.

The programme studies invariant functions on the ordinary merger components, rather than only constructing successful residue cylinders. Start with [the first-pass manuscript](pass1/PROOF.md): exact boundary laws; boundary births; uniform relative-gap geometry of every original component; a macroscopic-block closing criterion; and a lower bound for the dyadic variation of any nonconstant invariant function.

The universal upper-variation estimate remains OPEN. Topological density does not imply equality of components; the manuscript retains a 5x+1 control.

## First-pass publication and replay

`pass1` preserves the original manuscript, all three Python sources, README, original validation receipt and hash ledger. Statements there saying no GitHub publication was performed describe the original authoring pass; this parent page records its subsequent publication. The two large deterministic JSON outputs are regenerated rather than committed. Their exact original SHA-256 hashes are in the preserved ledger. This is a source-and-hash publication, not a claim that the original ZIP itself is stored in Git.

From `research/component-rigidity/pass1`:

```sh
python -S -B experiment.py --output results.json
python -O -S -B experiment.py --output results.optimized.json
python -S -B build_certificates.py
python -S -B verify_certificates.py
python -O -S -B verify_certificates.py
sha256sum -c SHA256SUMS.txt
```

The experiment and certificate checker were rerun in normal and optimized modes on 25 September 2026. The regenerated experiment matched the original 62,403-byte output exactly. Original experiment semantic digest: `d43c7b75ccc8e6144e40d65d3805f29776750aaf1053c455183505d965605258`. All four uploaded scientific/source blobs were remotely read back and matched the originals' Git blob hashes before this publication receipt.

Original conversation ZIP SHA-256: `ee9a08575464ac4f1f0416fa0be4fbe618de247bb491de82ee7b20872ee95f4e`.

No complete-checkout repository validation, remote CI, formal proof build or independent mathematical review was performed by this publisher. Container Git networking failed with DNS resolution; publication used the authorized GitHub connector. No main, workflow, setting, canonical scientific status or other contributor's branch was changed.
