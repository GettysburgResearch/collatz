# R-9405 — Rochev's single-expanding-place theorem does not directly apply

Claim ID: `R-9405`  
Title: The nearest broad p-adic q-series linear-independence theorem misses the stack phase vector at one load-bearing place hypothesis  
Status: `PROPOSED` applicability audit / method boundary  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-9408`, `L-9410`  
Scope: direct black-box application of I. P. Rochev's 2011 q-series theorem  
Related counterexample candidates: none

## Source inspected

I. P. Rochev, *On linear independence of values of certain q-series*,
Izvestiya: Mathematics 75 (2011), 177--221,
DOI `10.1070/IM2011v075n01ABEH002531`.

The paper treats a broad q-series class in both archimedean and p-adic cases and
is the closest located general theorem to the finite Tschakaloff phase vector of
a periodic stack word.

## Exact stack normalization

For a periodic word `W` of length `r`, sum `S`, and transfer data from `L-9408`,
`L-9410` writes the tail as a rational linear combination of phases

```text
G_j
 =sum_(N>=0)
   R^[N(N-1)/2](Z lambda^j)^N,
0<=j<r,
```

where

```text
lambda=(64/81)^(9S),
R=lambda^r.
```

In the usual Tschakaloff orientation, put

```text
q=R^(-1)=(81/64)^(9Sr).
```

Then

```text
G_j=sum_(N>=0)(Z lambda^j)^N q^[-N(N-1)/2].
```

## Failed hypothesis

Rochev's p-adic theorem fixes one place `w` with

```text
|q|_w>1
```

and requires

```text
|q|_v<=1
```

at every other place in the chosen set-up. This one-expanding-place condition is
used in the proof to keep the complementary global height of the linear forms
subquadratic relative to the smallness at `w`.

For the stack value in `Q_2`, the natural distinguished place is `w=2`. But

```text
|q|_2>1
```

because the denominator of `81/64` is a power of two, while simultaneously

```text
|q|_infinity>1
```

because `81/64>1` in the real embedding. The archimedean place therefore
violates the required nonexpansion condition.

Reversing the parameter does not repair the application. With `q=R`, the real
absolute value is below one, but the resulting Tschakaloff orientation no longer
produces the convergent `Q_2` series whose value is the stack context.

## Consequence

The following inference is not justified:

> The periodic stack tail is a finite vector of Tschakaloff values, so Rochev's
> p-adic linear-independence theorem proves every periodic tail irrational.

The phase-vector identification is exact, but the global-place hypothesis fails.
No conclusion about the values follows from this failed application.

## Why the native Padé construction still matters

`L-9409` and `L-9410` explicitly carry both competing heights:

- the `2`-adic gain from powers of `64`;
- the archimedean/odd-denominator cost from powers of `81`.

Their threshold constants are precisely the balance hidden by the failed
single-place shortcut. The period-four deficit is therefore a genuine global
height issue, not something a black-box p-adic theorem automatically removes.

## Nearby sources and limits

- Matala-aho's Padé-type q-series work and the Tschakaloff literature are close
  in construction, but the located statements use parameter/place hypotheses
  that must be checked individually.
- Results stated for integral `q` do not directly cover
  `(81/64)^(9Sr)`.
- A future theorem allowing simultaneous expansion at the archimedean and
  `2`-adic places could be relevant, but no such directly applicable statement
  has been verified in the current audit.

## Gap audit

- This is an applicability result, not a novelty claim for the repository Padé
  formulas.
- Failure of one theorem's hypotheses does not imply the stack values are
  rational or algebraic.
- The source comparison must remain separate from independent reconstruction of
  `L-9410` and `T-9414`.
- A more general adelic Subspace-Theorem formulation remains an open route.

## Suggested next attack

Any external-theorem route should explicitly budget both expanding places. A
useful target would be an adelic determinant theorem whose product-formula gain
is compared directly with the native exponent `mu_r`, or a phase-coupled
construction that lowers the archimedean height rather than ignoring it.