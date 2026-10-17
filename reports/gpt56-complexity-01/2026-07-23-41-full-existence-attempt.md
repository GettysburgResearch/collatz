# Session report — full six-branch existence attempt

**Date:** 2026-07-23  
**Agent:** `gpt56-complexity-01`  
**Issue:** #41  
**Branch:** `agent/gpt56-complexity-01/41-smooth-cycle-synthesis`

## Requested endpoint

The target was one finite tuple `(r_0,i_0,g,c_0)` whose intrinsic `L-8407` decoder is defined for every future step. Such a tuple would initialize an explicit positive unbounded shortcut orbit. No finite state passed an all-time induction in this session.

## Results committed

### `T-8404` — ordinary-code complexity

For `M=2^19` and `N=3^12`, equal length-`ell` branch factors whose second occurrence starts at `t` obey

\[
 \ell<(\log_MN-1)t+\log_M(h_0+1240029/7153).
\]

Hence every nontrivial ordinary survivor code satisfies

\[
 \liminf_{\ell\to\infty}{p(\ell)\over\ell}
 \ge {1\over\log_{2^{19}}(3^{12})-1}
 =971.866577472579\ldots .
\]

Its ordinary top-growth rate is

\[
 {\log_Mh_n\over n}\to0.0010289478238881146\ldots .
\]

### `T-8405` — no C-finite top boundary

An eventually C-finite quotient is eventually periodic modulo `2^19`. Deterministic type decoding then makes the branch code eventually periodic, whose rational completion has nonpositive real value. Polynomial, exponential-polynomial, rational-generating-function, and fixed linear-register top formulas are therefore excluded.

### `X-8405` — finite top audit

```text
intrinsic cells                         504
exact cell/target transitions        3,024
zero input top residues                  0
zero output constants                   11
coarse ordered pairs                     36
minimum strict coarse growth            149
maximum strict coarse growth          6,803
```

Every transition has one exact next cell and one law

```text
2^19 q' = 3^A q + kappa.
```

The scaled quotient is increasing above `4,271,324` in section `g=1` and above `3,212,050` in section `g=7`. One ordinary 13-cell quotient refunds two complete cells, survives 15 transitions, and then exits.

Canonical semantic digest:

```text
5af2cc52001aeff14d070ffeb37edf7399a92ac06ba23752bf34b8c480c3a29b
```

## Closed proof templates

- zero-top induction: all 3,024 transitions have `rho!=0`;
- periodic phase or cell cycles;
- fixed integer-linear top recurrences;
- a fixed finite-prime library;
- residue-only lassos without a canonical top boundary;
- extrapolation from a finite refund prefix.

## Remaining theorem

The surviving target is a genuinely nonlinear, non-C-finite ordinary invariant for

\[
 2^{19}q'=3^Aq+\kappa
\]

across the 504 intrinsic cells. It must retain one finite top quotient, select each nineteen-bit cell causally, manufacture fresh arithmetic information indefinitely, and prove all-time definedness. No such invariant was obtained here; the full existence statement remains open.
