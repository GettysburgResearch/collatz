# Paired cell lower pressure checks

From the repository root the following exact commands completed successfully on 2026-11-24.

```sh
python -B research/astra-global-budget-20261124/renewal/check.py
python -OB research/astra-global-budget-20261124/renewal/check.py
LEAN_PATH="$(cat ../lean_env/leanpath)" ../lean_env/lean-4.34.1-linux/bin/lean research/astra-global-budget-20261124/renewal/CellPressure.lean
```

[Finite output](controls.json) records 658 bounded-offset complete words through clock 16, 1,316 exact whole-unit-cell incidences, and 160 actual ordinary sources pulled back across both arms in 144 fixed-pair tests. Sixteen tests had more than one source in one localized window. Checks on 1,872 positive odd lifts verified the prefix correction on both arms at precisions one through three. The checker raises an explicit exception on failure. Standard and optimized Python produced byte-identical JSON. The ordinary source segment and the first six steps of the terminal transfer were replayed literally. The remaining common halvings were checked by the exact power-of-two equation with odd terminal target.

[Lean output](CellPressure.log) records the axioms of the two compiled finite lemmas. They verify the heavy-cell counting inequality and affine composition of the two segments. The iid renewal argument, moment bound, and all-depth ordinary applications are written mathematics. The external or upstream analytic proofs were not rebuilt as part of this check.

For the amplification in §3, PR200’s finite branch pressure and stopped-set theorem are source-qualified inputs. The disjoint-window transport is written here. All original intermediates use the single row selected from (1) for this value of Y, so the width BG is common, and the odd part of 9Q+7 recovers the original stop a. Within one window all retained sources share the full path from that stop to the prescribed q. Different windows can and generally do have different total clocks.
