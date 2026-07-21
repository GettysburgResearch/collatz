# KTHM-0004 — LTE, exact orders of `81` and `64`, and the `1+9Z_3` subgroup

**Source status:** standard lifting-the-exponent arithmetic; all needed cases are proved below.  
**Proof status:** complete  
**Maps to:** `CLAUDE/T-0005`, `CLAUDE/L-0013`, `CLAUDE/T-0019`; useful to `PR3/L-0006` and later precision calculations

## Lemma

Let `p` be an odd prime, `p|(a-b)`, and `p∤ab`. Then

\[
v_p(a^n-b^n)=v_p(a-b)+v_p(n).
\]

For odd `a≡1 (mod 4)`,

\[
v_2(a^n-1)=v_2(a-1)+v_2(n).
\]

These are the standard LTE identities. In the present applications they can also be proved directly by repeatedly factoring `X^p-1` or `X^2-1`; the cofactor has exactly one additional factor of `p` at each lifting step.

## Theorem

For every nonzero integer `d`,

\[
v_2(81^{4d}-1)=6+v_2(d).
\]

For every `j≥4`,

\[
\operatorname{ord}_{2^j}(81)=2^{j-4}.
\]

For every positive integer `n`,

\[
v_3(64^n-1)=2+v_3(n).
\]

For every `k≥1`,

\[
\operatorname{ord}_{81^k}(64)=3^{4k-2}=9\,81^{k-1}.
\]

Finally, for every `j≥1`,

\[
\langle64\rangle\pmod {81^j}=1+9\mathbb Z/81^j\mathbb Z.
\]

Thus `64` topologically generates `1+9Z_3`.

## Proof

Because `81≡1 (mod 16)`, the `2`-adic LTE identity gives

\[
v_2(81^m-1)=v_2(80)+v_2(m)=4+v_2(m).
\]

Taking `m=4d` proves the first formula. The least positive `m` for which this valuation is at least `j` is `2^{j-4}`, proving the order formula.

For `p=3`, note that `v_3(64-1)=v_3(63)=2`. Odd-prime LTE gives

\[
v_3(64^n-1)=2+v_3(n).
\]

The modulus `81^k` is `3^{4k}`. Therefore the least positive `n` with `64^n≡1 (mod 3^{4k})` has `v_3(n)=4k-2`, namely `n=3^{4k-2}`.

Since `64≡1 (mod 9)`, its generated subgroup is contained in `1+9Z/81^jZ`. The latter group has

\[
\frac{81^j}{9}=3^{4j-2}
\]

elements, exactly the order just computed. The two finite groups are equal. Passing through the compatible inverse system gives topological generation. ∎

## Consequences

- `M↦(81^{4M}-1)/64` preserves `2`-adic distances, because the valuation of a difference is `v_2(M'-M)`.
- The level-`k` carry gadget length predicted from the order of `64 mod 81^k` is exactly `9·81^{k-1}`.
