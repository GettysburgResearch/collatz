# Topic note — p-adic Tschakaloff closure of periodic stack tails

## Exact native form

A period word of length `r` gives a finite rational linear combination of

```text
f_R(z_j)=sum_(N>=0)R^(N(N-1)/2)z_j^N,
```

where the points `z_j` lie in distinct `R`-orbits. See `LIT-KTHM-0034`.

## Shortest possible closure

Obtain Väänänen--Wallisser (1991) and check whether it proves linear independence of

```text
1,f_R(z_0),...,f_R(z_(r-1))
```

for the exact rational parameters. If so, every fixed period and every finite prefix of it is irrational by one source theorem plus the native transfer identity.

## Fallback

Use the q-functional equation

```text
f_R(z)=1+z f_R(Rz)
```

and treat the whole phase vector by one determinant/Hermite--Padé system. For period four, search common symbolic maximal-minor factors and cyclotomic factors before evaluation. The required height saving is explicitly small.

## S-adic bridge

A fixed-period theorem must be strengthened to a measure uniform in the word. Apply it to adjacent continued-fraction standard words `W_n^infinity`, then compare their values to the balanced limit using the exact S-adic transfer matrices.

## Failure conditions

- A theorem for integer `q` in the archimedean place is not automatically p-adic.
- Qualitative irrationality with constants exploding in `r` does not pass to the S-adic limit.
- Formal denominator cancellation must be measured after reduction.