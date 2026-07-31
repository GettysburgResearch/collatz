# LIT-KTHM-0059 — Small-interval exclusion, Sturmian boundary, and exact nonapplication to the centered union

**Status:** `KNOWN — EXACT + APPLICABILITY/NONAPPLICATION AUDIT`  
**Primary sources:**  
1. Artūras Dubickas, *Powers of a Rational Number Modulo 1 Cannot Lie in a Small Interval*, Acta Arithmetica 137 (2009), 233–239, Theorems 1 and 3  
2. Artūras Dubickas, *On the Powers of 3/2 and Other Rational Numbers*, Mathematische Nachrichten 281 (2008), 951–958  
**Source inspection:** both complete PDFs  
**Native interfaces:** PR #16 and PR #67 centered `64 -> 81` work  
**Counterexample status:** no ordinary centered survivor is excluded or constructed

## Exact 2009 theorem

Let `1<q<p<q^2` be coprime. Dubickas proves that for every nonzero real `xi` and every closed interval `I` of length `1/p` on `R/Z`,

\[
\{\xi(p/q)^n\}\notin I
\]

for infinitely many positive integers `n`.

The source first proves a boundary theorem: if all fractional parts lie in one interval of length `1/p`, then the associated integer carry word is a Sturmian word over two consecutive integers. Repeated factors in a Sturmian word then force an impossible divisibility-versus-growth inequality when `p<q^2`.

## Exact centered consequence

For `(p,q)=(81,64)`, the hypothesis `81<64^2` holds. Suppose

\[
\xi(81/64)^n=B_n+u_n,
\qquad |u_n|\le1/81.
\]

If `u_n>=0` eventually, then the fractional parts eventually lie in the interval `[0,1/81]`. If `u_n<=0` eventually, they eventually lie in the torus interval `[-1/81,0]`. Either alternative contradicts the theorem after shifting the initial index.

Therefore every nonzero hypothetical centered orbit satisfies

\[
\boxed{
u_n>0\text{ infinitely often and }u_n<0\text{ infinitely often}.}
\tag{1}
\]

Equivalently, the native sign/control word changes sign infinitely often.

## Why the theorem does not solve the centered problem

The centered admissible set is

\[
[-1/81,1/81]\pmod1,
\]

which is the union of two intervals and has total length `2/81`. The 2009 theorem excludes confinement to one interval of length `1/81`; it does not exclude this two-sided union.

The Sturmian conclusion likewise applies only after confinement to one such interval. It does not classify a word that alternates between both halves.

## Exact audit of the 2008 paper

The 2008 paper proves a special two-interval exclusion for powers of `3/2`, including

\[
\eta\le\|\xi(3/2)^n\|\le9\eta/4
\]

for `1/5<=eta<=8/39`. This annular hypothesis is not satisfied by the native centered problem, which imposes only an upper bound and permits arbitrarily small errors.

Its general constructive theorems also do not apply to `81/64`:

- Theorem 2.2 assumes `p>2q`, whereas `81<128`.
- Theorem 2.3(i) assumes `p>2q`.
- Theorem 2.3(iii) has a different parameter range and an upper bound far larger than the native radius.
- The measure-zero construction of Theorem 2.4 assumes `p>=q^2+1`, whereas `81<<64^2`.

Thus the full 2008 source supplies useful neighboring geometry but no missing direct implication for PR #16/PR #67.

## Strategic conclusion

The full-paper audit closes a false hope:

```text
Dubickas 2006:
  exact scalar limit points, subcritical;

Dubickas 2009:
  excludes either one-sided half forever;

Dubickas 2008:
  two-interval results do not match the native centered set.
```

The surviving target is arithmetic:

\[
q_K=0\text{ eventually}
\]

must be excluded by a transported-height, recurrence, determinant, or canonical-boundary argument. Real interval geometry alone still sees the complete binary shift.

## Gap audit

- Infinite sign changes are much weaker than ordinary nonexistence.
- The source does not quantify return times between the two halves.
- It supplies no bound on the native renewal quotient.
- It supplies no equality-language classification at radius `1/81`.
