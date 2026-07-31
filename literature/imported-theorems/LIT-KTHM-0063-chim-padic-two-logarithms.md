# LIT-KTHM-0063 — Chim's logarithmic-height bound for two `p`-adic powers

**Status:** `KNOWN — EXACT SOURCE + FINITE-PRIME COROLLARY`  
**Primary source:** Kwok Chi Chim, *Lower Bounds for Linear Forms in Two p-adic Logarithms*, Journal of Number Theory 266 (2025), 295–349, Theorem 2.1  
**Source inspection:** complete 55-page PDF, including the theorem, main proposition, and variants table  
**Native interfaces:** pulse/cycle denominator growth, mixed-place height gates, fresh-prime arguments  
**Counterexample status:** no positive cycle or divergent orbit is claimed

## Source theorem

Let `p` be prime and let `alpha_1,alpha_2` be multiplicatively independent algebraic `p`-adic units. For positive integers `b_1,b_2`, put

\[
\Lambda=\alpha_1^{b_1}-\alpha_2^{b_2}.
\]

Chim's Theorem 2.1 gives an explicit upper bound for `v_p(Lambda)` whose dependence on the exponent parameter is linear in

\[
H\asymp\log B,
\]

rather than quadratic in `log B`. The theorem records all field, ramification, residue-degree, principal-unit, height, and root-of-unity parameters explicitly.

## Rational `2`/`3` specialization away from `6`

Fix a prime `ell>=5`. In `Q_ell`, both `2` and `3` are units, the field parameters are

\[
D=e=f=1,
\]

and the principal-unit exponent `g` divides `ell-1`. Since `2` and `3` are multiplicatively independent, the theorem applies to

\[
\Lambda=2^a-3^b.
\]

With

\[
\log A_1\ge\max\{\log2,\log\ell\},
\qquad
\log A_2\ge\max\{\log3,\log\ell\},
\]

it yields a completely explicit bound of the form

\[
\boxed{
v_\ell(2^a-3^b)
\le C_\ell\bigl(1+\log(a+b)\bigr),}
\tag{1}
\]

where `C_ell` is read directly from Theorem 2.1 or one of its variants.

## Finite-prime escape corollary

Let `S` be any fixed finite set of primes disjoint from `{2,3}`. Summing `(1)` gives

\[
\log\left((2^a-3^b)_S\right)
=O_S(\log(a+b)),
\]

where the subscript denotes the `S`-part. Thus

\[
\boxed{
(2^a-3^b)_S\le(a+b)^{C(S)}}
\tag{2}
\]

for an explicit constant `C(S)`.

On any family for which a real logarithmic-form estimate makes `|2^a-3^b|` exponential up to a polynomial factor, `(2)` forces prime divisors outside every fixed `S`. In particular, an unbounded cycle-denominator family cannot remain supported on a fixed finite prime library.

This is an effective finite-place version of the qualitative fresh-prime principle already used elsewhere in the repository.

## Correct scope

- The theorem does not apply at `ell=2` or `ell=3` to the pair `(2,3)` because one base is not a unit.
- The constant depends on the fixed prime and on the principal-unit exponent `g`.
- It controls the two-term denominator `2^a-3^b`, not an arbitrary multi-term numerator.
- Fresh denominator primes do not by themselves contradict full-denominator divisibility; the pulse correction may acquire the same primes.

## Comparison with Bugeaud 2002

Bugeaud treats several non-Archimedean places simultaneously but has a quadratic logarithmic dependence. Chim treats one prime at a time and obtains the optimal logarithmic dependence on exponent height, with larger but explicit constants. They are complementary:

```text
fixed finite composite modulus:
  Bugeaud;

one load-bearing prime with large exponent range:
  Chim.
```

## Gap audit

The current repository still needs an exact bridge showing that a fresh denominator prime cannot divide the corresponding pulse correction. Without that bridge, `(2)` is a structural restriction, not a cycle exclusion.
