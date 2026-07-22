# X-0016 — Scaled-tail, S-unit, fixed-room, and adelic-bridge audit

Experiment ID: `X-0016`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of the exact finite algebra in `L-0031`, the native applicability interfaces of `T-0032`, and finite analogues of `T-0033`--`T-0035`

## Research questions

1. Do the stabilized phase-34 tower anchors have the exact form
   \[
   64A_i(t)=2^{11(t+1)}p_i,
   \qquad
   64B_i(t)=3^{7(t+1)}p_i+b_i?
   \]
2. Does the scaled connector equation reduce to
   \[
   3^{7(t_j+1)}X_j+b_{i_j}
   =2^{11(t_{j+1}+1)}Y_j?
   \]
3. On actual canonical residual cylinders, does the ordinary scaled tail obey
   \[
   2^{11(t_{j+1}+1)}W_{j+1}
   =3^{7(t_j+1)}W_j+b_{i_j}?
   \]
4. Does finite-chain composition give the positive `{2,3}`-unit toll sum of `L-0031` exactly?
5. Are the corrected-stage exponent formulas and scale-separating toll-coordinate ratio exact?
6. Does homogeneous normalization produce the exact room increments and floor identities used in `T-0033`?
7. Does quotient extinction convert the room floor into the residual/connector bridge of `T-0034`?
8. Do the exact coefficient inequalities used in `T-0035` hold without floating point?

## Scripts

### `run.py`

Uses exact Python integers to:

- reconstruct all four phase-34 tower types;
- verify the stabilized table
  ```text
  p = (5,30,20,56)
  b = (9,54,36,24);
  ```
- construct four nontrivial ten-tower words;
- compute every canonical connector, residual tile, complete correction, and cap;
- replay each path with three independent high tails;
- verify 96 local scaled-tail recurrences;
- verify the exact positive toll formula;
- check the 256-stage exponent sums for `m=12,...,24`;
- verify that a toll-coordinate ratio distinguishes the tested scales.

This script does **not** re-prove the Evertse--Schlickewei--Schmidt theorem used by `T-0032`. It checks the native fixed equation, positivity, fixed term count, and injective-scale interface.

### `fixed_room.py`

Isolates the exact normalization in `T-0033`:

- verifies normalized room increments in a finite expanding affine chain;
- checks exact floor identities;
- verifies
  \[
  144\,2048^{128}<2187^{128};
  \]
- checks the homogeneous exponent recurrence and positive stage-scale margin.

The infinite shrinking-target theorem is proved by a geometric tail estimate, not inferred from this finite model.

### `bridge.py`

Checks the algebraic identity behind `T-0034`:

\[
W=X+64TR
\quad\Longrightarrow\quad
C{H\over64T}-R={X+\varepsilon\over64T}.
\]

It also verifies the exact residual homogeneous exponent

\[
f_m={1085579\over256}2^m+2816m+17
\]

and the strict connector-word gap below `64T`.

### `height.py`

Checks the exact affine height-gap certificate

\[
\Gamma-7\log_2 3
>{41273\over13568}>3
\]

from `log_2(3)>84/53`, together with representative dyadic nonresonance coefficients used by `T-0035`.

## Commands

```bash
python3 -m py_compile experiments/X-0016-scaled-tail-sunit/run.py
python3 experiments/X-0016-scaled-tail-sunit/run.py

python3 -m py_compile experiments/X-0016-scaled-tail-sunit/fixed_room.py
python3 experiments/X-0016-scaled-tail-sunit/fixed_room.py

python3 -m py_compile experiments/X-0016-scaled-tail-sunit/bridge.py
python3 experiments/X-0016-scaled-tail-sunit/bridge.py

python3 -m py_compile experiments/X-0016-scaled-tail-sunit/height.py
python3 experiments/X-0016-scaled-tail-sunit/height.py
```

## Expected output

`run.py`:

```text
verified stabilized two-prime tower anchors
verified 96 actual scaled-tail connector transitions
verified 256-stage exponents and scale-injective toll ratios
all scaled-tail S-unit checks passed
```

`fixed_room.py`:

```text
verified exact finite-room increments and floor identities
verified shrinking-target bound ingredients
all fixed-room checks passed
```

`bridge.py`:

```text
verified exact finite room-connector bridge identity
verified residual homogeneous scale and connector gap
all adelic bridge checks passed
```

`height.py`:

```text
verified exact affine quadratic-generator height gap
verified representative dyadic nonresonance coefficients
all quadratic-generator height checks passed
```

Checked-in outputs are under `results/`.

## Interpretation

After scaling

\[
W=p_i+64h,
\]

the connector seed/cap data telescope into one positive toll from

\[
9,54,36,24.
\]

A fixed 256-symbol source word therefore gives one positive 257-term multiplicative equation. Positivity resolves the proper-subsum problem completely.

The endpoint prime support is the exact escape from a direct S-unit proof. `T-0032` proves that every infinite ordinary path must use infinitely many fresh primes.

The same stage equation has a fixed real normalization. `T-0033` gives one room hitting doubly-exponentially shrinking targets, and `T-0034` identifies the target address with the exact normalized connector word. `T-0035` then excludes fixed-polynomial uses of the quadratic generator by height nonresonance.

## Limitations

- Finite checks do not prove the imported S-unit theorem.
- Infinite fresh prime support is necessary, not impossible.
- The all-scale room and bridge statements are proved analytically, not extrapolated from finite runs.
- No cap-stitch tail, finite marked initialization, or positive-integer counterexample is constructed.
