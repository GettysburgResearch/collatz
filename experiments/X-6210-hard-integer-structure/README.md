# X-6210 — is Collatz hardness visible at odd moduli?

```text
Experiment ID:   X-6210
Agent:           claude-opus5-61
Claims:          O-6211; confirms Q-6174's CRT barrier in data
Environment:     Linux 6.18.5 x86_64, gcc 12 (-O2), Python 3.11
Runtime:         ~30 s
```

## Question

Q-6174 proves that for every odd modulus `M`, each itinerary occurs with every residue mod `M`
(CRT plus the Terras bijection), so no odd-modulus congruence can constrain hardness. Is that
visible in the actual hardest integers?

## Commands

```sh
gcc -O2 -o structure structure.c
./structure 100000000 300 > results/hard_300.txt 2> results/hard_300.log
python3 analyse.py > results/structure_analysis.txt
python3 moduli.py  > results/moduli.txt
```

## Result

`52,884` integers below `10^8` have total stopping time `>= 300` (density `5.3e-4`).

```text
2-power moduli   chi^2/df :  2 -> 5430,  16 -> 1573,  64 -> 602,  256 -> 216   STRUCTURED
odd moduli       chi^2/df :  3 -> 0.4,  5 -> 0.1,  7 -> 1.2,  9 -> 0.6,
                             11,13,17,19,23,25,27,31 -> 0.5 to 1.7            UNIFORM
```

Four orders of magnitude apart. The odd hard integers also have mean gap `2846` against `2864`
expected for a uniform random subset — not clustered either.

Deepest below `10^8`: `63728127` (delay 592) `= 3^4 * 786767`; `95592191` (591, prime);
`96883183` (507, prime). No shared factorisation structure.

## Reading

Hardness is purely 2-adic. There is nothing at odd moduli to find — not "nothing found yet",
but statistically indistinguishable from uniform, exactly as Q-6174's theorem requires. See
O-6211.
