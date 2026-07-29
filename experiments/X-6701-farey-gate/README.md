# X-6701 — exact Farey-gate certificate

**Experiment ID:** `X-6701`  
**Agent:** `gpt56-positive-01`  
**Issue:** #75  
**Claim packet:** `research/positive-coefficient-gate/`  
**Classification:** exact finite arithmetic certificate  
**Status:** `EXACT` within the stated scope

## Research question

For the least-counterexample reduction in `T-6703`--`T-6707`, certify without floating-point assumptions that:

1. the quoted rational intervals enclose `log(2)` and `log(3)`;
2. the continued-fraction prefix of
   ```text
   alpha = log(2)/log(3)
   ```
   is uniquely determined through the required next convergent;
3. the microscopic first-crossing window lies between the declared Farey neighbors;
4. the first admissible denominator is `114,208,327,604` and has the unique mediant numerator `72,057,431,991`;
5. the mechanical-word/Denjoy--Koksma remainder upper bound is strictly smaller than the minimum remainder required by no descent above
   ```text
   N_* = 4*3^44+2;
   ```
6. after excluding the first mediant, the next possible denominator is at least `217,976,794,617`.

## Method

`run.py` uses only the Python standard library.

- Every proof comparison is performed with `fractions.Fraction`.
- `log(x)` is enclosed through the positive atanh series
  ```text
  log(x) = 2 sum_{k>=0} z^(2k+1)/(2k+1),
  z = (x-1)/(x+1),
  ```
  together with an explicit rational tail bound.
- The continued fraction is recovered by interval arithmetic: each floor must be identical at both rational endpoints before the reciprocal step is taken.
- Decimal arithmetic is used only after all assertions have passed, to render a readable transcript.
- No random seed, external package, network access, or generated input is used.

## Command

```bash
python3 experiments/X-6701-farey-gate/run.py
```

## Independently replayed session values

The exact arithmetic was replayed during the authoring session. The committed checker asserts the exact fractions before printing these decimal enclosures:

```text
X-6701 EXACT CERTIFICATE: PASS
N_*                          : 3939083608734444931526
epsilon upper                : 4.859819084768091e-23
M                            : 72057431991/114208327604
lambda lower                 : 5.510890095769573e-12
remainder upper              : 17326149966.76824...
N_* coefficient-drop lower  : 21707856845.72310...
exclusion margin lower       : 4381706878.95486...
first denominator gate       : 114208327604
left-cell next denominator   : 238856515799
same-rational next multiple  : 228416655208
right-cell next denominator  : 217976794617
SHARPENED GATE               : 217976794617
```

The full run prints substantially more digits and the certified continued-fraction prefix.

## Exact objects frozen by the checker

```text
L =   6586818670 /  10439860591
U =  65470613321 / 103768467013
M =  72057431991 / 114208327604
F =  78644250661 / 124648188195
R = 137528045312 / 217976794617
```

The checker also verifies

```text
det(L,U) = det(F,M) = det(M,U) = 1,
F < alpha-epsilon_* < M < alpha < U,
ceil((den(M)-1) alpha) = num(M).
```

## Interpretation

A passing transcript is a proof-grade certificate for the finite arithmetic used in the packet. In particular, it certifies that the first candidate has a positive contradiction margin of more than `4.381e9` and that the post-exclusion denominator gate is exactly `217,976,794,617`.

## Limitations

This program does **not** prove:

- Barina's exhaustive verification theorem;
- Ansari's recursive-sufficiency theorem;
- the least-counterexample no-descent lemma;
- the mechanical-word extremizer;
- the Denjoy--Koksma inequality;
- the existence or nonexistence of a Collatz counterexample;
- anything about coefficient crossings after the declared gate.

Those mathematical dependencies are stated and audited separately in `research/positive-coefficient-gate/PROOF.md`. The checker must not be cited as a substitute for independent proof reconstruction.

## Environment

Tested logic: CPython with standard-library `fractions` and `decimal`. The script is dependency-free and should run on any maintained Python 3 release supporting postponed annotations and built-in generic type syntax.