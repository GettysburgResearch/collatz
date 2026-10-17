# LIT-KTHM-0044 — Cross-completion limits must not be identified

**Type:** elementary standalone theorem plus a literature-guided proof discipline.  
**Maps to:** `PADIC/L-9416`, `PADIC/L-9417`, withdrawn `PADIC/T-9418`–`T-9421`, `ADEL/T-9315`, and every Padé argument using both an Archimedean and a finite-place estimate.

## Theorem

A sequence of rational numbers may converge to different rational limits in two completions of `Q`.

More explicitly, put

```text
x_N = 2^N/(1+2^N).
```

Then

```text
x_N -> 1 in R,
x_N -> 0 in Q_2.
```

### Proof

In the real absolute value,

```text
1-x_N = 1/(1+2^N) -> 0.
```

In the `2`-adic absolute value, the denominator `1+2^N` is odd and therefore a `2`-adic unit, while

```text
v_2(x_N)=N.
```

Hence `|x_N|_2=2^(-N)->0`. QED.

## Completion firewall

Let `(r_N)` be rational partial sums which converge to `L_infinity` in `R` and to `L_p` in `Q_p`. The following inference is invalid without an additional rational identity:

```text
an Archimedean bound for L_infinity
 -> the same bound for L_p.
```

The two limits may be compared as the same rational number only after one has proved a completion-independent representation, for example:

1. a finite rational expression;
2. an eventually periodic geometric formula;
3. a rational-function identity in `Q`;
4. or a cross-multiplied nonzero ordinary integer relation whose sizes are estimated at all relevant places.

## Correct Padé pattern

The safe two-place architecture is:

```text
one rational Padé numerator/denominator pair
 + a p-adic estimate for its error at the target value
 + an Archimedean estimate for those same rational coefficients
 + the product formula or ordinary numerator divisibility
 -> a contradiction.
```

It is not necessary—and is generally false—to identify the `p`-adic target with the Archimedean companion approached by the same Padé polynomials.

A useful published model is Ernvall-Hytönen, Matala-aho, and Seppälä, *Euler's factorial series, Hardy integral, and continued fractions* (2022). Their Padé polynomials approach Euler's factorial series at a finite place and a Hardy integral at the Archimedean place. The Archimedean companion is used to bound the rational Padé polynomial; it is not declared equal to the `p`-adic value.

## Application to PR #20

For a binary `64/81` tail, the rational partial sums have:

- a positive bounded real limit;
- a generally different `2`-adic limit used by the survivor coding.

`PADIC/L-9416` and `L-9417` validly prove that rational `2`-adic tail denominators form a descending divisor chain. They do not bound the ordinary numerators of those rational `2`-adic values. Therefore denominator descent alone does not imply:

- a finite rational state set;
- eventual periodicity;
- irrationality of every unbounded-gap series;
- or triviality of the ordinary section.

The withdrawals `PADIC/T-9418`–`T-9421` correctly preserve this boundary.

## Reusable audit rule

Every repository proof involving one formal series at more than one place should name the completion-specific values separately until a rational identity has been established. Every application should identify:

```text
p-adic target,
Archimedean companion,
rational Padé coefficients,
nonzero ordinary integer or product-formula object.
```

No cross-completion equality may be inferred from common partial sums alone.
