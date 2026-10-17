# Session report — height forcing and `N_*` target correction

```text
Agent: gpt56-cycle-02
Issue: #9
Branch: agent/gpt56-cycle-02/9-factor-guided-cycle
Date: 2026-07-23
```

## Starting hypothesis

Continue the reported critical paired-chart Hensel ladder until divisibility by a sufficiently large power of the known factor product, together with the tiny real gap, forces

```text
C=N_*D.
```

## First adversarial check

Before extending the expensive lift, I checked the physical chart domain of the proposed ordinary quotient

```text
N_*=110,340,992,901,879.
```

The exact paired chart of `T-8302` has first-state residue classes

```text
0 mod16,
5 mod16,
13 mod16.
```

But `N_*=7 mod16`. It cannot execute either chart branch. This refutes the target independently of all later packet choices and all odd-prime congruences.

The physical seed `2*N_*+1` also reaches `1` after 208 shortcut steps, with trajectory digest recorded in `X-8307`.

## Exact height result

For the critical parameters,

```text
A=4,992,586,555,009,
K=3,149,971,404,836,
M=1,465,129,870,107,858,983,
```

exact rational logarithm enclosures give

```text
0<A log2-K log3<2^-41.
```

Hence

```text
D=2^A-3^K<2^(A-41).
```

The reported real gap is below `2^-41`, so

```text
|C-ND|<2^(A-82).
```

Therefore a mixed divisibility certificate

```text
2^B M^J | C-ND
```

forces equality when

```text
B+60J>=A-82.
```

Pure odd-prime lifting would require at most

```text
83,209,775,916
```

levels by the elementary power-of-two bound. Exact range-reduced logarithms sharpen the sufficient exponent to

```text
82,733,048,428.
```

The previously reported order-seven lift supplies only 420 coarse bits. It was not close to the global height threshold.

## Main conceptual correction

The full physical dyadic cylinder is a vastly stronger height certificate than repeated lifting at a handful of odd factors.

If one ordinary integer follows the complete advertised word, then

```text
2^A | C-ND.
```

If the same finite rational fixed point lies within one of that integer, then

```text
|C-ND|<D<2^A,
```

and equality follows immediately.

The correct constructive product state is therefore

```text
physical dyadic prefix
+ odd-prime quotient cylinder
+ directed real interval.
```

The dyadic state must be checked first.

## New files

```text
research/critical-chart-mechanical/claims/L-8310-mixed-place-height-forcing.md
research/critical-chart-mechanical/claims/R-8301-nstar-dyadic-domain-refutation.md
research/critical-chart-mechanical/Q-8301-mixed-place-height-closure.md
experiments/X-8307-height-gate/
reports/gpt56-cycle-02/2026-07-23-9-height-gate-and-nstar-refutation.md
```

## Candidate counterexamples

None. `N_*` is withdrawn as a possible chart-cycle quotient.

## Failed approach preserved

Odd-prime Prouhet/Hensel packets can match many proper-place quotient digits while the proposed integer fails the first physical branch. Such a ladder cannot be interpreted as converging toward a counterexample without a dyadic cylinder certificate.

## Recommended next actions

1. Add a dyadic chart-prefix track to every replacement node in `X-8302`.
2. Reject candidate integers at the first physical mismatch.
3. Extend a legal physical prefix before spending odd-prime Hensel levels.
4. Close only when the exact mixed height budget of `L-8310` is met.
5. Prefer complete compressed physical replay: with a unit real interval it already forces the full cycle identity.

## Organizational improvement

Every future near-candidate table should display, side by side:

```text
real integer candidate,
first physical branch residue,
dyadic replay depth B,
odd-prime lift depth J,
height-budget total B+floor(log2(M))*J.
```

This would have exposed the `N_*` failure before the recursive odd-prime packet work began.
