# X-0017 — Three-symbol room filter and real defect digits

Experiment ID: `X-0017`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of the exact finite algebra in `L-0033`, `T-0037`, and `L-0034`

## Questions

1. Does one three-symbol prefix select one canonical scaled-tail input?
2. Does a six-bit Hensel lift give the canonical output residue modulo 64?
3. Is there at most one admissible fourth tower type?
4. Do the exact stabilized filters reproduce the independent PR #34 head counts?
5. Does the normalized real defect obey the positive digit recurrence and lie immediately above its current toll digit?

## Method

`run.py` uses exact Python integers and `fractions.Fraction` only.  For scales
12, 13, and 14 it:

- constructs the three-symbol modulus `M_m`;
- computes the common odd inverse modulo `64*M_m`;
- constructs all 64 lifted addresses;
- extracts the high six-bit Hensel block;
- reconstructs the output residue directly;
- retains the unique fourth type when the output lies in `{5,30,20,56}`;
- records the minimum ordinary address bit length;
- verifies the exact completion-height coefficient `35913/5248`;
- checks a finite exact instance of the defect-digit expansion;
- verifies `(2048/2187)^128 < 2^(-10)` and the resulting `1/16` leading-digit interval.

## Command

```bash
python3 -m py_compile experiments/X-0017-room-filter/run.py
python3 experiments/X-0017-room-filter/run.py
```

## Expected output

```text
m=12 precision=136257 survivors=5 heads=0311,1330,2013,2111,2303 minimum_address_bits=136252
m=13 precision=272481 survivors=3 heads=0203,2202,2300 minimum_address_bits=272472
m=14 precision=544929 survivors=4 heads=2111,2231,3010,3222 minimum_address_bits=544923
verified exact defect-digit recurrence and leading interval
all three-symbol room-filter checks passed
```

The checked-in output is `results/summary.txt`.

## Extended local audit

During the authoring session an independent GMP implementation evaluated the
same six-bit filter through scale 19.  The exact survivor counts were

```text
m : 12 13 14 15 16 17 18 19
n :  5  3  4  6  3  4  5  2
```

and independently reproduced the displayed heads through scale 14.  This
extended result is recorded only as an authoring audit because the portable
repository checker deliberately remains standard-library Python.

## Limitations

- Finite nonzero counts do not prove a room exists.
- One scale with a small survivor count does not improve the global room bound;
  `T-0037` requires a lower-limit statement.
- The experiment does not control the growing inverse-lift carry from one scale
  to the next.
- No marked Collatz initialization or counterexample is proposed.