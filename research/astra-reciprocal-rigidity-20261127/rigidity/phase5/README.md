# First-hit clocks for moving ordinary targets

[FAST_CLOCK_EDGE.md](FAST_CLOCK_EDGE.md) bounds the number of ordinary shell sources hitting a prescribed odd ternary unit near the fastest possible time. As the relative excess clock \(\delta\) tends to zero, the upper and lower exponents agree in the terms of orders \(\delta\log(1/\delta)\) and \(\delta\). The first-hit times concern positive shortcut trajectories. The only inputs are inverse integer arithmetic and binomial counting.

[SOURCE_CLOCK_BANK.md](SOURCE_CLOCK_BANK.md) constructs a selected polynomial-size family of first visits for any moving odd ternary unit and any odd-landing threshold. Its largest individual true clock fiber occupies \(O(1/\sqrt{\log(X/M)})\) of the selected family. A finite eight-odd-step certificate gives a population exponent strictly greater than one half. The same method-by-types argument supplies individual highly populated, unusually fast clocks. The note compares the central-speed results of Wren and Weaver and the fixed-component consequence of Mazur's positive-density theorem.

The two exact checkers use the Python standard library. From this directory run

```sh
python source_clock_controls.py --check
python -O source_clock_controls.py --check
python fast_clock_controls.py --check
python -O fast_clock_controls.py --check
```

The frozen reports are [SOURCE_CLOCK_CONTROLS.json](SOURCE_CLOCK_CONTROLS.json) and [FAST_CLOCK_CONTROLS.json](FAST_CLOCK_CONTROLS.json). They test the advertised finite residue recursions, direct ordinary first hits, dyadic equalization and exhaustive short inverse layers. The asymptotic arguments remain written proofs. The fate of each target after the visit remains an open part of the Collatz problem.
