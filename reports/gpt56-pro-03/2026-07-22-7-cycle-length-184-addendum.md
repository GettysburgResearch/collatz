# Wave-7 addendum — universal accelerated length-184 cycle exclusion

**Agent:** `gpt56-pro-03`  
**Date:** 2026-07-22  
**Parent report:** `2026-07-22-7-literature-audit-wave7.md`

## Result

The original wave-7 cycle packet froze the favorable parameter `(k,A)=(184,292)`. A second reduction extends the same ordered-jump decoder to every possible total valuation at accelerated odd length `184`.

Hercher's theorem forces at least `92` local minima. Length `184` permits at most `92`, so every possible cycle must alternate valuation `1` with a valuation at least `2`:

```text
(1,b_0,1,b_1,...,1,b_91).
```

Write

```text
A=276+H,
H=sum_i(b_i-2)>=16.
```

For every `H`, the necessary cycle divisibility reduces to

```text
sum_(r=0)^(H-1) 2^r 9^(92-j_r)8^(j_r)=mD'_H,
1<=j_0<=...<=j_(H-1)<=92.
```

Successive binary valuations recover the only possible jump positions. Uniform multiplier bounds split the infinitely many heights into two finite gcd classes:

```text
gcd(D_H,5)=1 -> m<=73,778;
gcd(D_H,5)=5 -> m<=1,005,828.
```

Direct scans at `H=16,...,20` find no solution. For all larger heights, the decoder is stable against changing `H`: the denominator perturbation has valuation at least `300` or `303`, while the two reference scans inspect valuations only through `31` or `42`. Thus the same early valuation-modulo-3 failure applies at every height.

Consequently:

```text
There is no nontrivial positive accelerated Collatz cycle
with odd-state length 184.
```

## Replay

```bash
python3 literature/experiments/LIT-X-0052-frontier-cycle/run.py \
  --check-results \
  literature/experiments/LIT-X-0052-frontier-cycle/results/canonical.json
```

Reference transcript digests:

```text
gcd 1: e7b965827614c319335e925782b8533690e3ba3827ba6a47674e4de44edc9702
gcd 5: b7ddde20ce910d6597d64bb3f7238a67ecab3f279f5583eef1ec5e2c9c8c687e
```

## Scope

This is a complete exact exclusion of one accelerated length and a reusable proof-producing decoder. It is not a positive cycle, a divergent orbit, or a Collatz resolution. The direct cycle lane now starts at `k>=185` within this parameterization, subject to stronger external cycle bounds and their exact conventions.