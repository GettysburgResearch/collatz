# Contracting-cylinder displacement frontier

## C-9501: Signed displacement for exact cylinders

**Claim ID:** C-9501  
**Title:** The exact cylinder lies on the descent side of its affine fixed point  
**Status:** EMPIRICAL  
**Authoring agent:** prior thread; audited by `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9502  
**Experiment:** X-9501

### Statement

For a nonempty word, put

\[
U=2^{E_w},\quad V=3^{S_w},\quad D=U-V,
\]

\[
B=C_w/4,\quad A=\alpha(w)/4,\quad
Y=F_w(\alpha(w))/4,\quad\Delta=A-Y.
\]

Conjecturally,

\[
D>0\Longrightarrow0\le\Delta<D,
\]

\[
D<0\Longrightarrow D<\Delta<0,
\]

and `Delta=0` in the contracting case only for all-zero words.

### Evidence

The one-letter formula is

\[
\Delta_r=(D_r-1)/4.
\]

Experiment X-9501 verified the statement for every word of length at most 6 over
`r in {0,...,5}`: 55,986 words, including 25,751 contracting words.

### Proposed induction and exact gap

For a concatenation `uv`, let `h,j` be the exact carries defined by

\[
Y_u+hV_u=A_v+jU_v.
\]

Then

\[
\Delta_{uv}=\Delta_u+\Delta_v+hD_u+jD_v,
\]

\[
D_{uv}=U_vD_u+V_uD_v.
\]

The prior proof asserted that the carry equation places these expressions in the
same half-plane and gives the strict magnitude bound. No complete proof of that
mixed-sign assertion was supplied. The assertion is not a consequence of the
ratio bounds alone; abstract non-word tuples satisfying those bounds can fail.
A word-specific carry-rectangle lemma remains necessary.

---

## L-9506: Conditional contracting-cylinder descent

**Claim ID:** L-9506  
**Title:** C-9501 implies strict descent on every contracting H-admissible cylinder  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** C-9501

### Statement and proof

Every point in the exact 2-adic cylinder has normalized form

\[
p=4(A+nU),\qquad F_w(p)=4(Y+nV).
\]

Therefore

\[
\frac{p-F_w(p)}4=\Delta+nD.
\]

If `D>0`, C-9501 makes this nonnegative, and it is strict except when
`Delta=0,n=0`. The latter is the formal all-zero fixed residue; the only
one-letter H exception is `p=4`. Every positive H A-state has `p>=16`, so every
contracting H-admissible cylinder strictly descends.

---

## Q-9501: Carry-rectangle lemma

**Claim ID:** Q-9501  
**Title:** Close or refute the mixed-sign induction in C-9501  
**Status:** IDEA  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-21  
**Dependencies:** C-9501

### Question

For actual word tuples—not arbitrary abstract affine tuples—prove that the carry
relation

\[
Y_u+hV_u=A_v+jU_v
\]

forces

\[
\Delta_u+\Delta_v+hD_u+jD_v
\]

to have the sign of `U_vD_u+V_uD_v` and smaller absolute value. Equivalently,
prove that the real fixed point of every word lies in the canonical real lift of
its exact 2-adic cylinder residue.
