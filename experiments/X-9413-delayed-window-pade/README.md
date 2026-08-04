# X-9413 — Delayed-window block Padé audit

Experiment ID: `X-9413`  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: `L-9418`, `T-9422`, `R-9410`  
Classification: exact Laurent-polynomial, monomial-height, and threshold replay

## Research question

Can one keep the degree of the periodic Gaussian-binomial denominator fixed but
move its exact simultaneous cancellation window to a later block depth? If so,
does the resulting valuation-to-height gain prove a native period-nine theorem,
and where does the family stop?

## Replay

```bash
python3 -B -m py_compile experiments/X-9413-delayed-window-pade/run.py
python3 -B experiments/X-9413-delayed-window-pade/run.py \
  --check-results \
  experiments/X-9413-delayed-window-pade/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9413-delayed-window-pade/run.py \
  --write-results \
  experiments/X-9413-delayed-window-pade/results/canonical.json
```

Canonical SHA-256:

```text
ddce893eef7edf6b15c5b83dc2598bf7a832479507cf2c92309dba2172c8ec4c
```

## Frozen exact scope

The verifier checks:

```text
Laurent product identities       630
exact zero-window placements     180
first-error phase comparisons     36
denominator monomials           1,986
numerator monomials             47,694
```

The finite ranges are:

```text
1<=period<=4,
1<=order<=3,
1<=delay-degree<=3.
```

For every frozen tuple it independently constructs both sides of

```text
sum_k (-1)^k [D choose k]_lambda
 lambda^[beta-rNk+r k(k+1)/2-jk]

 =prod_(h=0)^(D-1)
   (1-lambda^[h+rM-rN-j])
```

as exact Laurent polynomials over `Z`. It then checks all allocated zeros, the
first surviving phase, and every monomial appearing in the displayed common
height bound.

## Exact asymptotic certificates

The optimized delayed exponent is

```text
mu_r^delay(alpha)
 =log_81(64)*[((alpha+1)^2-r)/(alpha^2+r)],
```

with optimizer

```text
alpha_r^*
 =(2r-1+sqrt(4r^2+1))/2.
```

The frozen table records that the optimized exponent is above one precisely for
periods `1,...,9` among the tested periods through fifteen.

### Native period-nine certificate

A single rational delay ratio works uniformly:

```text
alpha=37/2.
```

At period nine the shape is `297/281`. The script verifies

```text
64^93>81^88,
88*297-93*281=3,
```

which proves

```text
log_81(64)*(297/281)>1.
```

### Period-ten family ceiling

The script verifies

```text
263/250-f_10(alpha)
 =[13alpha^2-500alpha+4880]
  /[250(alpha^2+10)],
```

with discriminant `-3760`, and also verifies `64^20<81^19`. Hence

```text
mu_10^delay(alpha)<4997/5000<1
```

for every real delay ratio.

## Interpretation boundary

The finite replay validates the exact algebra and displayed threshold
certificates. The universal product identity and height theorem are proved in
`L-9418`; the irrationality theorem is `T-9422`; the family closure is
`R-9410`.

The experiment does not prove:

- period-ten irrationality;
- a reduced-height common-factor theorem;
- applicability of a general `q`-difference source theorem;
- irrationality of the balanced nonperiodic `17/18` directive;
- an ordinary M1 witness;
- or the Collatz conjecture.