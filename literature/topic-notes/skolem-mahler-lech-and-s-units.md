# Skolem–Mahler–Lech, power sums, and “S-unit” language

## SML application template

To invoke `LIT-KTHM-0008`, a native claim should display

```text
u_n = sum_i c_i alpha_i^n
```

and record:

- the characteristic-zero field;
- every nonzero coefficient;
- every pairwise quotient `alpha_i/alpha_j`;
- why no quotient is a root of unity;
- why the sequence is not identically zero;
- whether the target is exact equality or only divisibility/congruence.

For the bases `81^18`, `81^9`, and `1`, nondegeneracy is immediate once all present coefficients are nonzero.

## Effectivity boundary

Skolem–Mahler–Lech gives qualitative finiteness. It generally does not give an effective upper bound for the last zero. A computational “all coincidences occur below X” statement needs additional arithmetic.

## S-unit terminology

`PR3/T-0004` calls

```text
d_k + N^u_k C_k = d_(k+1) + M^u_(k+1) C_(k+1)
```

an S-unit carry chain because powers of `M` and `N` occur. Classical S-unit equations usually require variables themselves to range over a finitely generated multiplicative group while coefficients are fixed. Here the cofactors `C_k` are new unbounded integer variables and the exponents/carries are coupled dynamically. No classical S-unit finiteness theorem applies merely from the name.

## Promising refinement

If a candidate grammar restricts every cofactor `C_k` to a fixed finite-rank multiplicative group, then genuine S-unit or Subspace-Theorem machinery may become applicable. That restriction would be a substantial native hypothesis and should be made explicit.
