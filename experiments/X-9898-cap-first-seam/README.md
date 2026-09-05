# X-9898 -- Exact cap first-seam verifier

This experiment replays the finite table in `L-9898/(33)` from the stabilized
four-type tower anchors and connector equations.  It does not search Collatz
orbits and it is not used to extrapolate beyond the requested scales.

Run from the repository root:

```text
python experiments/X-9898-cap-first-seam/verify.py
```

The script uses exact Python integers only.  It precomputes the three
five-window contributions to the first canonical output, reducing the costly
odd-modulus work from one inversion per state to one inversion per scale.
Typical runtime is about two minutes for both default scales.

Expected output is stored in `results/canonical.json`.
