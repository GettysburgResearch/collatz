# Skolem–Mahler–Lech, power sums, and `S`-unit terminology

## Imported theorem

Skolem–Mahler–Lech says that the zero set of a characteristic-zero linear recurrence sequence is a finite union of a finite set and arithmetic progressions. For a nondegenerate power sum `Σ c_i α_i^n`, the zero set is finite. See KTHM-0007. [@Bell2019]

## Audit of `CLAUDE/T-0006`

The repository states that an unsteered supply-demand equality is a nondegenerate three-term power sum. To invoke the corollary, the claim file must display:

- the exact sequence `u_m`;
- coefficients `c_i` and bases `α_i` in a characteristic-zero field;
- proof that every surviving `c_i` is nonzero;
- proof that `α_i/α_j` is not a root of unity for each distinct pair;
- proof that the desired coincidences are exactly zeros of `u_m`, with no varying auxiliary parameters.

Until these appear, the literature theorem is verified but the reduction is not.

## `S`-unit carry chains

`PR3/T-0004` calls equations such as

\[
d_k+N^{u_k}C_k=d_{k+1}+M^{u_{k+1}}C_{k+1}
\]

an `S`-unit carry chain. The powers of `M` and `N` create an `S`-unit flavor, but the coefficients `C_k` vary and may have unrestricted prime factors. Classical fixed-coefficient `S`-unit equations therefore do not apply merely from the terminology.

A future application must first freeze a finite schema for the cofactors or ratios, producing a genuine fixed `S`-unit equation or a linear recurrence.
