# Integral recurrences and skeleton rigidity

## The correct imported tool

`LIT-KTHM-0007` proves that characteristic bases of an integer-valued linear recurrence are algebraic integers. The proof uses:

- finite rational Hankel rank;
- a rational generating function;
- `p`-adic analyticity of an integer-coefficient power series;
- integrality of reciprocal poles.

This is the exact dependency needed in `CLAUDE/T-0020`.

## Why it is stronger than a smoothness assumption

The theorem does not require characteristic bases to be rational, algebraic in advance, Pisot, or composed only of primes dividing `MN`. Integrality of the sequence forces algebraic integrality of every surviving base.

Thus a rational noninteger dominant ratio such as `(N/M)^U` cannot occur in a minimal integer recurrence.

## Native proof checklist

Before applying the theorem, the branch should:

1. combine equal positive bases in each exponential polynomial;
2. delete identically zero polynomial coefficients;
3. prove the cofactor subsequence is integer-valued eventually;
4. prove its consecutive ratio has a finite limit;
5. identify that limit with the largest surviving base;
6. show the skeleton recurrence forces the same limit to be `(N/M)^U`.

This makes the load-bearing contradiction auditable without the ambiguous phrase “Kronecker criterion.”
