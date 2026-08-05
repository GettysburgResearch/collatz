# Independent adversarial review of PR #45's critical-cycle compiler

**Agent:** `gpt56-refund-01`  
**Reviewer identity/model:** OpenAI `GPT-5.6 Pro`  
**Role:** independent reconstruction, not extension  
**Source PR:** #45  
**Frozen target:** `5d17926b48e29f94a935f1d433559b0c417cef55`  
**Date:** 2026-07-22

## Executive verdict

The packet

```text
L-8401 -> L-8402 -> L-8403 -> O-8401 / X-8401
```

is **PASSED** in its stated scope. The three universal algebraic claims reconstruct, and the trillion-step finite straight-line computation is independently reproduced. The frozen word is rigorously nonintegral; no cycle or counterexample is claimed.

## 1. `L-8401` — exact product gate

For a positive accelerated cycle,

```text
2^a_i n_(i+1)=3n_i+1
```

becomes

```text
2^a_i n_(i+1)=3n_i(1+1/(3n_i)).
```

Multiplication around the cycle cancels the states and gives

```text
2^A/3^k=product_i(1+1/(3n_i)).
```

If all states are at least `X`, logarithms give exactly the submitted upper slope window. At `A=2k`, every factor is at most `4/3`; equality of products forces every state to be one. Endpoints, signs, and strictness all pass.

**Verdict: PASSED.**

## 2. `L-8402` — local numerator repair

For chronological concatenation, direct affine substitution gives

```text
C(uv)=3^k_v C(u)+2^A_u C(v).
```

A same-length, same-total block replacement leaves all prefixes before the block and after its end unchanged. Only its internal prefix powers move, yielding the submitted sum. The adjacent swap formulas specialize correctly:

```text
01 -> 10: +3^(k-u-2) 2^A_(u+1)
10 -> 01: -3^(k-u-2) 2^(A_(u+1)-1).
```

Disjoint same-total swaps are additive because each preserves every later total prefix. For a rotation `uv -> vu`, subtraction of the two concatenation formulas gives

```text
2^A_u C(vu)-3^k_u C(uv)=D C(u),
D=2^A-3^k.
```

Since `D` is odd, rotation preserves divisibility.

**Verdict: PASSED.**

## 3. `L-8403` — noncommutative Euclidean compiler

For `q=ap+s`, the gaps before successive ones in the lower mechanical word have lengths

```text
a-1 + U(s,p)_t.
```

Thus lower letters expand to `0^(a-1)1` or `0^a1`. The upper word has the dual after-one gaps and expands to `10^(a-1)` or `10^a`. These substitutions preserve order, so the result is valid in an arbitrary associative, noncommutative monoid.

The independent checker evaluated all lower and upper words for `1<=q<80`, comparing the recursion with literal strings. All 6,478 products agree.

**Verdict: PASSED.**

## 4. Frozen trillion-step target

The independent implementation reconstructed

```text
k=3,149,971,404,836
A=4,992,586,555,009
gcd(A-k,k)=1.
```

The five displayed integers are prime and each satisfies

```text
2^A == 3^k mod p.
```

Their product is

```text
M=1,465,129,870,107,858,983.
```

The independently compiled lower mechanical word has

```text
C_base mod M=655,756,015,106,852,524.
```

The first 80 disjoint mixed adjacent sites and both masks regenerate the submitted 43 positions exactly. Summing the independent swap deltas gives

```text
C_modified mod M=0.
```

The cyclic local-minimum count is

```text
1,307,356,254,653.
```

## 5. Completion-safe real rejection

A 170-digit directed interval implementation and a separate 240-digit scalar implementation give the same fixed point. The directed interval is

```text
1791361447298439130709020.9975283539098510107859711562546399767831669907701910897463476475120008538767324760660413065677992404534204762886255980560072685470190724787376332
< C/D <
1791361447298439130709020.9975283539098510107859711562546399767831669907701910897463476475120008538767324760660413065677992404534204762886255980560189960682315744265811368.
```

This overlaps the committed 120-digit interval and leaves distance at least

```text
0.002471646090148989214028843745
```

from the next integer. Therefore the frozen word is not an integral cycle.

During review, an initial independent interval implementation used unary `Decimal` negation outside its directed context, causing a false mismatch. Replacing it with exact sign-copying restored enclosure and agreement. This reviewer error is recorded because it is a useful regression: cancellation near `1-r` makes silent context rounding visibly dangerous.

**Verdict for `O-8401` and `X-8401`: PASSED.**

## 6. Source/frontier context

The target has over `3.1e12` odd terms and over `1.3e12` cyclic local minima. Its reconstructed fixed point is above the currently cited `2^71` verified range. Those facts make it a serious finite grammar probe, but none is used to infer a cycle. The load-bearing conclusion is only the exact modular component plus real nonintegrality.

## 7. Remaining constructive frontier at the frozen comparison head

At the PR #34 comparison head initially frozen for `X-8201`, Smith form and universal gcd formulations merely restated `D|C`, selected primitive prime powers could be silent, and words with at most four non-2 valuations were excluded. The finite-certificate target there was

```text
complete D|C identity
for a primitive, genuinely varying word,
with at least five non-neutral valuations
or an unbounded compressed grammar.
```

PR #45's `Q-8401` states the full-denominator boundary honestly. No `K-84xx` object exists.

## 8. Live frontier addendum

After this review froze, PR #34 advanced to `b7eec65ffb13c5a89415a888c0153f36a52f23e3`. Its proposed `L-9912` and `L-9913` exclude exactly five and exactly six non-2 valuations. Subject to their own independent review, the live sparse-cycle floor is therefore now **at least seven** non-2 valuations. This does not alter any PR #45 verdict; it sharpens the successor search target.

## Replay

```bash
python3 -B experiments/X-8201-wave-review/run.py > /tmp/X-8201.json
diff -u experiments/X-8201-wave-review/results/canonical.json /tmp/X-8201.json
python3 -B experiments/X-8201-wave-review/verify.py experiments/X-8201-wave-review/results/canonical.json
```
