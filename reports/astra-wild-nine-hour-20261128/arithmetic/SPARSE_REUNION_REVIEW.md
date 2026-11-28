# Review of the sparse-edit reunion bounds

The [proof packet](../../research/astra-wild-nine-hour-20261128/arithmetic/SPARSE_EDIT_INVERSE_REUNION.md) proves a necessary condition for two legal finite paths to join the same terminal ternary cylinder. A join after a prescribed displacement is a genuine congruence in the original source. Different clocks leave a nonzero linear coefficient. Equal clocks remove the source and leave signed trit blocks that must fit under an Archimedean bound.

## Verification

The [control program](../../research/astra-wild-nine-hour-20261128/arithmetic/check_sparse_inverse_reunion.py) uses integer arithmetic throughout. Run it with Python 3 from the repository root.

```sh
python -B research/astra-wild-nine-hour-20261128/arithmetic/check_sparse_inverse_reunion.py
python -OB research/astra-wild-nine-hour-20261128/arithmetic/check_sparse_inverse_reunion.py
```

Both invocations printed the same [JSON receipt](sparse_inverse_reunion.json).

- Binary decoding and strict numerator growth held for the empty word and every positive composition of total at most eight (256 words, with the strict growth assertion only for nonempty words).
- The exact linear-congruence solution count and the direct path check agreed on 1,296 choices of unequal word clocks, precision and signed ordinary displacement, across 432,432 concrete root representatives. The direct search found 683 legal reunions.
- For every pair of distinct words at equal clocks through total eight, at precisions one through eleven, a dynamic program computed the minimum Hamming weight of any signed ternary digit difference for the required displacement. All 24,485 cases with visible displacement satisfied the deterministic gap inequality. Forward coding from the terminal unit one supplied an independently evaluated legal reunion in every case.

These finite tests do not prove the exponents. The complete counting and height arguments for arbitrary precision are given in the proof packet. This checkpoint makes no new Lean verification claim. It uses the earlier biased entropy theorem only to change the initial root law in the exponential exceptional-set estimate. A comparison of independently optimal futures, where a common tail is unnecessary, remains open.
