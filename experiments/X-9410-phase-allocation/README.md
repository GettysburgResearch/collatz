# X-9410 — Phase-allocation optimization census

Experiment ID: `X-9410`  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: `L-9411`, `T-9416`, `R-9404`  
Classification: exact finite verification of the asymptotic functional interface

## Research question

Can unequal allocation of Gaussian-binomial cancellation roots among periodic
stack phases improve the universal valuation-to-height shape beyond equal
allocation?

## Replay

```bash
python3 -B -m py_compile experiments/X-9410-phase-allocation/run.py
python3 -B experiments/X-9410-phase-allocation/run.py \
  --check-results experiments/X-9410-phase-allocation/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9410-phase-allocation/run.py \
  --write-results experiments/X-9410-phase-allocation/results/canonical.json
```

Canonical SHA-256:

```text
aab92d29cf446b13c39c9e7eb9cc681c09f4199bf52d6ae0ee6a9ffa923d2259
```

## Frozen scope

The script exhausts every weak composition

```text
n_0+...+n_(r-1)=D
```

for

```text
2<=r<=7,
1<=D<=18.
```

That is `657,774` exact allocation vectors. For each vector it computes the
exact rational shape

```text
[D^2+2mD+(1-r)m^2]
 /[D^2+sum_j n_j^2],

m=min_j n_j,
```

which is the first-phase valuation shape divided by the raw denominator-height
shape in `T-9416`.

The verifier checks:

1. every shape lies below
   ```text
   (r^2+r+1)/(r(r+1));
   ```
2. every finite maximizing allocation is balanced, with coordinates differing
   by at most one;
3. whenever `r|D`, exact equal allocation attains the continuous bound;
4. zero allocations and all period-length boundary cases are included.

## Interpretation boundary

The finite census validates the algebraic optimization interface. `T-9416`, not
the enumeration, proves the universal continuous inequality.

The experiment does not rule out:

- numerator/denominator gcd savings;
- cross-phase error cancellation;
- adjacent-order determinants;
- period-four irrationality;
- the balanced nonperiodic stack directive;
- an ordinary M1 witness or the Collatz conjecture.