# Ordinary component clocks

[CLOCK_DISPERSION.md](CLOCK_DISPERSION.md) proves, from the quantitative adjacent coalescence estimate, that the sum over all ordinary components of their largest individual clock fibers below \(X\) is \(O(X/\sqrt{\log X})\). It handles all cycle cuts in one elementary binomial estimate and shows \(H(\text{clock}\mid\text{component})\ge\frac12\log\log X-O(1)\). Consecutive long blocks reaching 85 at the same clock show why the conclusion concerns initial prefixes.

[CLOCK_PHASES.md](CLOCK_PHASES.md) gives joint clock equidistribution modulo every fixed modulus for the signed shortcut time and odd-input count. It identifies the possible real-frequency resonances and the bounded ordinary Green height they retain. Both documents distinguish density-free, componentwise statements from conclusions that require positive density of a specified component. The named 2026 timed-passage and terminal-law results serve for literature comparison.

[clock_controls.py](clock_controls.py) checks eight finite fixtures with exact rational integration over sixth-cells, including every coordinate of every balanced transport step, the terminal-support disappearance, translated atoms, and summed row maxima. Four fixtures use the true first-hit time to one. Four impose two additional known integer cuts at 5 and 85 to exercise multiple rows and unequal origins. Those three-row fixtures are algebra controls, not three ordinary connected components. Run

```sh
python clock_controls.py --check
python -O clock_controls.py --check
```

The [recorded report](CLOCK_CONTROLS.json) is identical in both modes. It tests the finite transport identities only. The quantitative synchronization input is a written imported theorem, and the full universal Collatz assertion remains open.
