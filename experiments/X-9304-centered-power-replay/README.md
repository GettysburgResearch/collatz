# X-9304 — Exact centered-power replay audit

**Experiment ID:** X-9304  
**Status:** EMPIRICAL interface audit  
**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Associated claims:** `T-9315`, `L-9312`  
**Date:** 2026-07-22

## Purpose

This experiment adversarially checks the finite-prefix algebra behind the centered-power equivalence.

It is not evidence that an infinite centered orbit exists or does not exist. The universal statements are proved algebraically in `T-9315` and `L-9312`; this script only freezes their indexing and reconstruction interfaces.

## Exact construction

For every binary word through depth `8`, the script:

1. reconstructs its standard finite survivor residue modulo `64^j`;
2. replays the exact ordinary recurrence;
3. chooses the non-endpoint real tail `x_j=1/3` and propagates the real companion backwards;
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
   81u_n-64u_{n+1}=\varepsilon_n-\varepsilon_{n+1};
   \]
9. checks the forced residues
   
   \[
   B_n\bmod64\in\{0,15,49\};
   \]
10. checks the four intermediate `3/2` phase neighborhoods from `L-9312`.

All arithmetic uses Python integers and `fractions.Fraction`. There is no floating-point comparison.

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
- carry and scheduled-phase checks: `3,020`;
- chosen terminal real coordinate: `1/3`;
- random seeds: none.

Canonical SHA-256:

```text
e287cbf70c55adbbdfe3ae4296fc8836f424b2ca48ddda03830235b46f952a2f
```

## Boundary

- The real terminal value `1/3` is a deterministic interior probe, not an ordinary future tail.
- The script checks finite-prefix identities. Compactness or compatibility of all finite prefixes would not by itself produce one ordinary integer.
- The theorem's converse is a universal algebraic proof and is not inferred from this enumeration.
- No centered parameter, ordinary infinite survivor, divergent Collatz seed, or counterexample is constructed.
