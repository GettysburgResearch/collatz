# Replay the spectral and energy checks

Python standard library only. From the repository root:

```sh
python -X utf8 -B experiments/spectral-energy-20261031/check_exact.py --output /tmp/exact.json
python -O -X utf8 -B experiments/spectral-energy-20261031/check_exact.py --output /tmp/exact_O.json
python -X utf8 -B experiments/spectral-energy-20261031/certify_energy.py --max-level 14 --precision 50 --output /tmp/energy.json
python -O -X utf8 -B experiments/spectral-energy-20261031/certify_energy.py --max-level 14 --precision 50 --output /tmp/energy_O.json
```

Each normal/optimized pair was actually run and byte-identical. Saved output
files are `exact_checks.json` and `energy_enclosures.json`. The energy file
contains exact rational outward bounds, 14 rows, and hashes of both complete
integer endpoint arrays at each depth. It does not contain all large arrays.
Those are regenerated deterministically by the producer.

SHA-256 of the complete saved output bytes:

* exact: `0fc9bd337e794b39e1be91ba5c65edfc60761d7be4e151e9adc004c609b90fdc`
* energy: `369249ddf1fa8eba6f7cb3cafff69f95f197a6995e79cb07408120212302a78b`

Semantic SHA-256 of each canonical payload:

* exact: `5d3397eac1b08a15703c36d9e7eaf015001171f3a568ad0618b190c5bacabfe9`
* energy: `96d53c98b3b590ee9e6823a0f0ed4bbbb14ec80217ddb9639fd8bdc9b559bc4f`

The exact checker has a separate full-period Fraction implementation of the
law; it cross-checks the interval enclosure through depth 5. Its signed Gram
checks are rational; the written complex-function proof is not replaced by
sampling complex values. Its explicit huge source is checked by literal
integer odd-map updates, not just residues.

The 14-level enclosure is NOT an independent second implementation at every
large level. Normal and optimized execution test reproducibility, not
independent mathematical review. No theorem prover, full checkout validator,
Windows replay or remote CI run is claimed.
