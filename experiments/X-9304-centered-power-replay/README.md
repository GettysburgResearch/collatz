# X-9304 — Exact centered-power and paired `8 -> 9` replay audit

**Experiment ID:** X-9304  
**Status:** EMPIRICAL interface audit  
**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Associated claims:** `T-9315`, corrected `L-9312`; refutation `R-9304`  
**Date:** 2026-07-22

## Correction notice

The former version of this experiment checked a purported four-phase `3/2`
schedule derived from the false identity

\[
81/64=(3/2)^4.
\]

That check is retracted. The correct factorization is

\[
\boxed{81/64=(9/8)^2,}
\]

and the current replay checks the exact paired `8 -> 9` lift proved in the
corrected `L-9312`.

## Purpose

This experiment adversarially checks the finite-prefix algebra behind:

1. the centered-power equivalence `T-9315`;
2. the exact factorization of each `64 -> 81` transition into two `8 -> 9`
   transitions carrying the same digit;
3. the centered square-root parameter `zeta=8 xi` for the ratio `9/8`.

It is not evidence that an infinite centered orbit exists or does not exist.
The script freezes indexing and reconstruction interfaces only.

## Exact construction

For every binary word through depth `8`, the script:

1. reconstructs its standard finite survivor residue modulo `64^j`;
2. replays the exact ordinary recurrence;
3. chooses the non-endpoint real tail `x_j=1/3` and propagates the real
   companion backwards;
4. forms

   \[
   \xi=(A_0-x_0)/64;
   \]

5. checks at every available position that

   \[
   \xi(81/64)^n=B_n+u_n,
   \qquad |u_n|<1/81;
   \]

6. reconstructs the digit from `sgn(u_n)`;
7. reconstructs the ordinary state from

   \[
   A_n=\lceil64\xi(81/64)^n\rceil;
   \]

8. checks the integral centered carry

   \[
   81u_n-64u_{n+1}=e_n-e_{n+1};
   \]

9. checks the forced residues

   \[
   B_n\bmod64\in\{0,15,49\};
   \]

10. sets `zeta=8 xi` and verifies

    \[
    \zeta(9/8)^{2n}=8B_n+8u_n,
    \qquad
    \zeta(9/8)^{2n+1}=9B_n+9u_n;
    \]

11. checks the two ordinary half-steps

    \[
    X_{2n}=A_n,
    \qquad
    X_{2n+1}=(9A_n-e_n)/8,
    \]

    \[
    8X_{m+1}=9X_m-f_m,
    \qquad
    f_{2n}=f_{2n+1}=e_n.
    \]

All arithmetic uses Python integers and `fractions.Fraction`. There is no
floating-point comparison.

## Replay

```bash
python3 -B -m py_compile experiments/X-9304-centered-power-replay/run.py
python3 -B experiments/X-9304-centered-power-replay/run.py \
  --check-results \
  experiments/X-9304-centered-power-replay/results/canonical.json
```

## Frozen scope

- depths: `1,...,8`;
- nontrivial finite survivor words checked: `494`;
- centered trace checks: `3,514`;
- paired `8 -> 9` half-steps checked: `7,028`;
- centered carry checks: `3,020`;
- chosen terminal real coordinate: `1/3`;
- random seeds: none.

Canonical SHA-256:

```text
75b258853a7b623d04e291b4172eec405316671d200cbb27510893fdea740fe1
```

## Boundary

- The real terminal value `1/3` is a deterministic interior probe, not an
  ordinary future tail.
- The script checks finite-prefix identities. Compatible finite prefixes do not
  by themselves produce one ordinary integer.
- The theorem converses are algebraic proofs and are not inferred from this
  enumeration.
- The invalid four-phase `3/2` artifact is preserved only through `R-9304` as a
  refuted formulation.
- No centered parameter, ordinary infinite survivor, divergent Collatz seed, or
  counterexample is constructed.
