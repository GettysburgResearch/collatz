# LIT-KTHM-0062 — Bugeaud's simultaneous `m`-adic two-logarithm bounds

**Status:** `KNOWN — EXACT SOURCE; NATIVE APPLICATION REQUIRES HYPOTHESIS MATCHING`  
**Primary source:** Yann Bugeaud, *Linear Forms in Two m-adic Logarithms and Applications to Diophantine Problems*, Compositio Mathematica 132 (2002), 137–158, Theorems 1–3  
**Source inspection:** complete PDF  
**Native interfaces:** PR #53/PR #70 pulse residuals; PR #50 mixed-place height gates  
**Counterexample status:** no cycle or divergent orbit is claimed

## Source setting

Let

\[
m=p_1^{u_1}\cdots p_w^{u_w}
\]

and

\[
L=(x_1/y_1)^{b_1}-(x_2/y_2)^{b_2}.
\]

The source assumes that both rational bases are units at every prime dividing `m`. It also requires one integer `g`, coprime to those primes, for which the `g`th powers enter the relevant principal-unit disks; the prime `2` has a strengthened convergence condition.

Under explicit interpolation-determinant hypotheses, Theorem 1 bounds `v_m(L)`. Theorems 2 and 3 give explicit simplified estimates. For `m` in

\[
\{4,6,8,10,15\},
\]

Theorem 2 gives constants

\[
66.8,46.1,36.9,32,26.1
\]

without multiplicative independence, and

\[
53.6,35.5,27.4,22.9,18
\]

with multiplicative independence. The dependence on the exponent height is quadratic in a logarithm. Theorem 3 handles prime-power `m` without the coprimality condition on the two exponents.

## Correct native use

The theorem is directly relevant only after a native identity has produced a genuine two-term residual

\[
\alpha_1^{b_1}-\alpha_2^{b_2}.
\]

For any fixed modulus `m` coprime to `6`, the bases `2` and `3` are `m`-adic units. A suitable fixed `g` can be chosen from their orders modulo the prime-power factors of `m`. The source then gives an effective polylogarithmic upper bound on

\[
v_m(2^a-3^b).
\]

This can control several fixed finite places simultaneously and is a natural finite-place half of a mixed real/adic height argument.

## Nonapplications

- At the prime `2`, the base `2` is not a unit; at the prime `3`, the base `3` is not a unit. The theorem cannot be applied to `2^a-3^b` at those places in its stated form.
- A multi-term pulse correction is not automatically a two-logarithm form.
- The parameter `g` may grow badly if the modulus itself varies. The source does not provide a uniform theorem over all moving denominator primes.
- High `m`-adic valuation of one residual does not by itself force a full denominator to divide it.

## Strategic use

The source is best used after exact elimination:

```text
multi-pulse identity
 -> two-term resultant at a fixed finite set of primes
 -> Bugeaud simultaneous m-adic bound
 -> Archimedean height comparison
 -> finite replay.
```

It should not be cited merely because an equation contains powers of `2` and `3`.

## Gap audit

No current pulse packet has yet supplied a source-matched two-term residual at a growing set of finite places. The paper supplies a tool and a strict applicability checklist, not a closure of the remaining cycle classes.
