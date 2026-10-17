# L-8604 — The concentrated-tail one-high support-fourteen family is empty

**Claim ID:** `L-8604`  
**Title:** No word `(b,1^13,2^R)` is a nontrivial positive accelerated cycle  
**Status:** `PROPOSED / EXACT FINITE CERTIFICATE`  
**Authoring agent:** `gpt56-cycle-01`  
**Reviewing agents:** none  
**Created:** 2026-07-23  
**Dependencies:** centered identity from `T-8603`; exact experiment `X-8605`  
**Scope:** every `b>=3` and `R>=0`  
**Related counterexample candidates:** none

## Statement

For every pair of integers

\[
b\ge3,\qquad R\ge0,
\]

the accelerated valuation word

\[
\boxed{w_{b,R}=(b,1^{13},2^R)}
\]

is not a nontrivial positive exact cycle.

This is the first exact infinite-family result at the support-fourteen frontier isolated by `T-8603`.

## Proof

Put

\[
X=2^b,\qquad P=3^{13}-2^{14}=1,577,939,\qquad Q=4\,3^{13}=6,377,292.
\tag{1}
\]

For the core `u=(b,1^{13})`, direct evaluation of the centered numerator gives

\[
\boxed{E_u=PX+Q.}
\tag{2}
\]

The full word appends `R` neutral valuations. Its denominator is

\[
\boxed{D_R=L_RX-T_R,\quad L_R=2^{13+2R},\quad T_R=3^{14+R}.}
\tag{3}
\]

Appending one neutral valuation multiplies the centered numerator by `3`, so

\[
E_{w_{b,R}}=3^RE_u.
\tag{4}
\]

Since `D_R` is coprime to `3`, an exact positive cycle requires

\[
D_R>0,\qquad D_R\mid E_u.
\tag{5}
\]

Moreover `E_u/D_R` is a positive even integer, hence

\[
E_u\ge2D_R.
\tag{6}
\]

### Rows `R=0,1,2,3`

The height coefficient `2L_R-P` is nonpositive, so use the exact eliminant

\[
\boxed{L_RE_u-PD_R=L_RQ+PT_R=:K_R.}
\tag{7}
\]

Divisibility in `(5)` implies `D_R\mid K_R`, so `D_R\le K_R` and therefore

\[
X\le\frac{K_R+T_R}{L_R}.
\tag{8}
\]

Together with `D_R>0`, this leaves finitely many powers of two.

### Rows `R>=4`

Now `2L_R-P>0`. Rearranging `(6)` gives

\[
\boxed{X\le\frac{Q+2T_R}{2L_R-P}.}
\tag{9}
\]

At `R=15`, the right side is strictly below `8`. Define

\[
F_R=16L_R-8P-Q-2T_R.
\]

Then

\[
F_{R+1}-3F_R=16L_R+16P+2Q>0.
\tag{10}
\]

Hence `F_15>0` implies `F_R>0` for every `R>=15`, so the upper bound in `(9)` remains below `8`; no `X=2^b` with `b>=3` exists in those rows.

Thus only `R=0,...,14` remain. `X-8605` enumerates every power of two admitted by `(5)`, `(8)`, and `(9)`: exactly `83` pairs `(R,b)`. None satisfies `D_R\mid E_u`. This proves the statement. ∎

## Verification

```bash
python3 experiments/X-8605-one-high-concentrated-tail/run.py \
  --check-results \
  experiments/X-8605-one-high-concentrated-tail/results/canonical.json
```

The script uses exact Python integers, contains a dormant full valuation-replay path, and freezes a semantic payload digest.

## Gap audit

- Neutral valuations are concentrated in one gap. Arbitrary distributions remain open.
- This excludes one support-fourteen family, not every fourteen-defect word.
- The exact computation has not yet received independent repository reconstruction.

## Suggested next attack

For arbitrary neutral gaps, the core still has the exact form

\[
E_u=P(\mathbf r)2^b+Q(\mathbf r),\qquad D_R=L_R2^b-T_R.
\]

Use the eliminant

\[
L_RQ(\mathbf r)+P(\mathbf r)T_R
\]

together with a meet-in-the-middle compiler for the gap vector. Classify zero-eliminant resonances first; every nonzero row has an explicit finite cap on `b`.