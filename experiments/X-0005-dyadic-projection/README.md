# X-0005 — Complete dyadic projection construction

Experiment ID: `X-0005`  
Agent: `gpt56-pro-01`  
Issue: `#2`  
Status: `EMPIRICAL` verification of `L-0009`, `L-0010`, and `T-0007`

## Purpose

Verify the finite construction of supercritical collision fibers whose offset alphabets meet every residue class modulo an arbitrarily prescribed power of two.

## Command

```bash
python3 -m py_compile experiments/X-0005-dyadic-projection/run.py
python3 experiments/X-0005-dyadic-projection/run.py
```

## Checks

For `1 <= b <= 5`, the script:

- constructs all `2^b` fixed-weight prefixes;
- verifies the triangular bijection modulo `2^b`;
- corrects every prefix to one common inverse signature with a one-hot suffix;
- directly traces every corrected branch to one common output;
- chooses a CRT root with the shortest forced odd tail making the chart supercritical;
- directly verifies the complete parity block and complete projection modulo `2^b`.

## Expected output

```text
b=1 branches=2 core_length=8 tail=9 projection=complete
b=2 branches=4 core_length=22 tail=30 projection=complete
b=3 branches=8 core_length=60 tail=92 projection=complete
b=4 branches=16 core_length=170 tail=278 projection=complete
b=5 branches=32 core_length=496 tail=832 projection=complete
all dyadic-projection checks passed
```

## Limitation

This verifies finite instances only. `T-0007` supplies the general symbolic proof. Complete modular projection is a construction resource, not finite-boundary closure.
