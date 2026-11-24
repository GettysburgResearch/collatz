# Minimum-source arithmetic replay

The local Lean 4.34.1 compiler accepted `SourceDeletion.lean` with warnings treated as errors. It reported `propext` and `Quot.sound` for `lift`, `swapped_paths`, `swapped_row`, `delete_digit`, `lower_representative`, `all_below` and `all_below_cutoff`. The `seven_mod_eight` declaration additionally reports `Classical.choice`. These declarations concern explicit trajectories or an arbitrary invariant natural-valued label. The passage to the actual basin and the smallest bad multiple of three is given in the [arithmetic proof](../../../research/astra-minimum-source-20261124/arithmetic/README.md).

The Python replay in ordinary mode and in `-O` mode gave identical output. It inspected 100,000 inputs from 2 through 100,001. The six case counts were respectively 50,000 even, 16,667 odd multiples of three, 16,667 odd numbers equal to two modulo three, 5,555 in the four-mod-nine case, 5,556 in the seven-mod-nine case and 5,555 in the one-mod-nine case. The replay also tested the swapped row, deletion paths and seven-mod-eight path at 4,097 distinct parameters, including $10^{50}$. The all-parameter assertions rest on proofs. The bound on the successive stripping exponents is a written proof.

| File | SHA256 |
|---|---|
| `README.md` | `17ceb3e8bfda7fa70214da2431c4ac5c4df3a9a1ff7b14ddc9cb9716396af4a8` |
| `SourceDeletion.lean` | `21227f38df7f95b29613ec322a1e48f3fc0e423155fb12867c9dfcf546699af0` |
| `check.py` | `043e95effb2b0a8d59ebaf3dfcce3fefb0ef3d6040e99a2018d2782da675530d` |

The remaining task is to discharge every original upper trajectory $3q$ at a hypothetical least discordant odd source. The smaller-source table certifies the whole initial interval and the stated paths exclude specified sources. Neither the table nor the all-clock upper bound on stripping exponents rules out the remaining positive ordinary trajectories.
