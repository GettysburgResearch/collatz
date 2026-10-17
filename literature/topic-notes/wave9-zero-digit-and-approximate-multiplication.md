# Wave 9 topic note — zero-digit hitting and approximate multiplication

## Exact native system

\[
P=3^{12}=531441,
\qquad
Q=2^{19}=524288,
\qquad
F(x)=\left\lceil {Px\over Q}\right\rceil.
\]

The six physical digits are

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

The six source residues are

\[
\mathcal S=
\{294912,331776,438784,297024,6472,466033\}.
\]

The identities

\[
\delta(x)=QF(x)-Px,
\qquad
\delta(x)\in\mathcal A
\iff
x\bmod Q\in\mathcal S
\]

identify the chart exactly with the Dubickas–Mossinghoff approximate-multiplication map restricted to `S`.

## One-letter reduction

Since

\[
P=Q+7153,
\]

we have

\[
F(x)=x+\left\lceil {7153x\over Q}\right\rceil
\]

and

\[
\delta(x)=Q\left\lceil {7153x\over Q}\right\rceil-7153x.
\]

Because `gcd(7153,Q)=1`,

\[
\delta(x)=0\iff Q\mid x.
\]

Thus the universal hitting statement

\[
\forall x>0\ \exists n:\ Q\mid F^n(x)
\]

eliminates the complete six-branch chart.

## Logical hierarchy

```text
full rational-base normality
    => every finite word appears with correct frequency

full residue equidistribution
    => every residue modulo Q^k appears

all-letter richness
    => every canonical digit appears at least once

zero-letter richness
    => digit 0 appears at least once
    => the six-branch chart exits

six-digit termination
    => some digit outside A appears
```

The zero-letter statement is substantially weaker than the first three. It is stronger than necessary for chart termination because the orbit may exit through any of `Q-6` forbidden digits.

## Positive-side hierarchy

```text
Z_(P/Q)-number exists
    => some orbit survives every residue set S with |S|=6
       when P<6Q
    => in particular one six-branch survivor exists
    => branch-qualified Collatz counterexample.
```

The first implication is the contrapositive of Dubickas–Mossinghoff Proposition 3.1. The reverse implications are not known.

## Search discipline

A useful computation should target a theorem-shaped invariant, not merely deeper prefixes. Suitable outputs include:

1. a monotone quantity forcing a first hit of `QZ`;
2. a finite exact decomposition reducing every zero-avoiding orbit to a known impossible class;
3. an induced return map on one smaller modulus with a strict rank;
4. an explicit ordinary zero-avoiding orbit, followed by the stronger check that every digit lies in `A`.

A modular lasso without the actual ordinary root is not a witness.

## Literature firewall

- Dubickas 2009 proves high factor complexity, not digit occurrence.
- Dubickas–Mossinghoff 2009 prove singleton termination, not six-set termination.
- Andrieu–Eliahou–Vivion 2026 conjecture normality; the load-bearing zero-digit statement remains open.
- Väänänen–Wallisser 1991 concerns finite vectors of p-adic special values, not rational-base digit hitting.

## Immediate theorem target

> **Zero-digit theorem for one base.** Every positive orbit of
> \[
> x\mapsto x+\left\lceil {7153x\over524288}\right\rceil
> \]
> reaches a multiple of `524288`.

A proof is a genuine exhaustive-class result and is strictly narrower than the full Collatz conjecture.