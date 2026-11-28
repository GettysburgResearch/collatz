# Dynamics checkpoint 4

The written [two-modulus anchor theorem](../../../research/astra-wild-nine-hour-20261128/dynamics/MERSENNE_ANCHOR.md) isolates one dyadic lift among true shallow positive predecessors for all log-heights below \((1-\delta)k^2\). Its paired Mersenne moduli have product below \(2^{2k+1}\). The explicit three-odd-step family at fixed anchor 37 proves the leading quadratic log-height constant is sharp. This theorem supplies no positive witness for an arbitrary prescribed anchor.

The [finite kernels](../../../research/astra-wild-nine-hour-20261128/dynamics/MersenneCarry.lean) compiled from fresh source with Lean 4.34.1, importing only Std. The code checks the merge count, the cyclic displacement of every initial token through arbitrary actual merge histories, the coefficient inequality, and rigidity after two exact evaluations with physical coefficient signs. The token initialization, final singleton, size estimates, recovery of both exact evaluations and ordinary-orbit conclusions remain written mathematics.

Strict replay used the following command, with the output object in temporary storage.

```bash
lean -DwarningAsError=true -o /tmp/MersenneCarry.olean research/astra-wild-nine-hour-20261128/dynamics/MersenneCarry.lean
```

The local axiom audit of the first three theorem roots reports `propext` and `Quot.sound`. The fourth root, `anchored_cone`, also uses `Classical.choice`. All four passed warning-as-error elaboration.

The [integer and rational replay](../../../research/astra-wild-nine-hour-20261128/dynamics/check_mersenne_anchor.py) directly enumerated complete genuine trajectories and token histories. Its output was

```text
PASS 200 ordinary carry reconstructions, 8 single-modulus and 6 paired-modulus sharp witnesses
```

The coordinator also reported a clean independent, serialized strict replay of the earlier checkpoint 2 source envelope after the initial local job had stalled.
