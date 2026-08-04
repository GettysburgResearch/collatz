# X-0002 — Exact collision fibers, carry pumping, and phase skeletons

Experiment ID: `X-0002`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` for the finite enumeration; exact identities are separately stated in proposed claim files.

## Research questions

1. What changes when complete collision fibers are enumerated rather than only consecutive runs?
2. Can the affine tables be generated recursively without retracing every residue for every depth?
3. Does the nine-column `64 -> 81` stack gadget generalize to every induced collision chart?
4. Does the run-length skeleton reconstruct exact finite trajectories?

## Method

`run.py` uses exact Python integers and the standard library only.

It implements the recursion of `L-0003`:

- even residue `2*k` inherits the depth-`L` affine data of `k`;
- odd residue `2*k+1` first maps to `3*k+2`, which is split into quotient and residue modulo `2**L` before the existing affine table is applied.

At each depth it groups residues by the exact pair

```text
(number of odd steps, common output)
```

and retains nontrivial supercritical fibers. It also independently checks the proposed conjugacy, carry-pumping, coding, and run-length results.

## Command

```bash
python3 experiments/X-0002-collision-fibers/run.py
```

Optional syntax check:

```bash
python3 -m py_compile experiments/X-0002-collision-fibers/run.py
```

## Environment

- Python 3.11 or newer recommended
- standard library only
- deterministic; no random seed
- peak work occurs at depth 22 (`2**22` residues)

## Parameter range

- recursive tables and complete supercritical fibers: every `1 <= L <= 22`;
- direct-trace cross-check of the recursion: every residue through `L=12`;
- explicit lifted checks of the depth-22 fiber: `q in {0,1,2,7,101}`;
- finite carry-pump and phase-skeleton tests on several exact contexts.

## Main output

The maximum cardinality of a nontrivial supercritical collision fiber is:

```text
L=6..8:   2
L=9..10:  3
L=11..13: 4
L=14..16: 5
L=17..18: 8
L=19..21: 12
L=22:     18
```

The first maximum-cardinality depth-22 fiber is

```text
[621248, 621264, 621268, 621269, 621280, 621282,
 621283, 621288, 621290, 621297, 621316, 621317,
 621318, 621326, 621327, 621340, 621341, 621342]
```

with fourteen odd steps and common output `708587`.

The script verifies the exact lifted identity

```text
T**22(4194304*q + residue) = 4782969*q + 708587
```

for every listed residue.

It also recovers the universal zero-output carry block in the `64 -> 81` chart and verifies the short admissible-output tile

```text
R_1 L_361 L_0 -> L_2 L_2 R_1
```

in the `512 -> 729` chart.

## Checked-in output

```text
results/summary.txt
```

SHA-256 digests at the time of this contribution:

```text
e7aa9f820fc20fd23eeef40224e47a32aa248d0aa2b5a182066e710acfe42629  run.py
321fd0eb8df6b3e333a0b20210a01881dc949e131e2864711302b574ae7d9087  results/summary.txt
```

## Interpretation

The decisive generalization is from consecutive intervals to arbitrary finite collision fibers. A sparse fiber is just as valid an induced digit alphabet, and its cardinality can substantially exceed the best consecutive width at the same search depth.

The carry experiment also shows that finite-horizon pumping is universal. Therefore local amplifiers should be treated as reusable macro-tiles rather than as rare candidate counterexamples. The unresolved problem is vertical closure of a finite high-order boundary.

## Limitations

- Enumeration stops at depth 22.
- No asymptotic growth law for maximum fiber cardinality is proved.
- A large alphabet does not imply an infinite admissible orbit.
- The carry-pump tests are finite-horizon identities.
- The run-length skeleton is an exact reformulation, not an existence theorem.
- Compatible infinite digit data may still define only a nonordinary `2`-adic integer.
