# L-9812 — Root renewal for the minimum survivor

Claim ID: `L-9812`  
Title: The minimum survivor renews exactly at one legal endpoint residue  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `PR16/T-9313`; `L-9806` for the simultaneous-cylinder specialization  
Scope: finite `64 -> 81` survivor minima and the ordinary-section frontier  
Related counterexample candidates: none

## Definitions

Write the induced chart map as

\[
T(64q+e)=81q+e,
\qquad e\in\{0,1\}.
\tag{1}
\]

Let `L(A)` be the number of legal forward steps from the ordinary integer
`A`, possibly infinity. Let `R_K subset [0,64^K)` be the standard depth-`K`
survivor set and `C_K subset [0,81^K)` its endpoint-class dual. Define

\[
M_K=\min(R_K\setminus\{0,1\}),
\qquad
m_K=\min(C_K\setminus\{0,1\}).
\tag{2}
\]

The exact minimum duality in `PR16/T-9313` identifies

\[
m_K=T^K(M_K).
\tag{3}
\]

## Statement

For every `K>=2` the following hold.

### 1. Backward-root characterization

The minimum cannot itself have a legal predecessor:

\[
\boxed{
M_K
=\min\{A\ge2:A\bmod81\notin\{0,1\},\ L(A)\ge K\}.
}
\tag{4}
\]

In particular,

\[
\boxed{M_K\bmod81\notin\{0,1\}.}
\tag{5}
\]

### 2. Exact renewal law

The monotone minimum stays in the same ordinary room for one more depth
exactly when its endpoint has a legal next digit:

\[
\boxed{
M_{K+1}=M_K
\iff
m_K\bmod64\in\{0,1\}.
}
\tag{6}
\]

On equality, with `e_K=m_K mod 64`,

\[
\boxed{
m_{K+1}=\frac{81m_K-17e_K}{64}.
}
\tag{7}
\]

Consequently,

\[
\boxed{
M_K\longrightarrow\infty
\iff
m_K\bmod64\notin\{0,1\}
\text{ for infinitely many }K.
}
\tag{8}
\]

Thus eventual confinement of the endpoint minima to the two legal residues is
not a weaker exceptional case: it is exactly stabilization of the ordinary
minimum, hence the unresolved existence of a nontrivial ordinary survivor.

### 3. Simultaneous-cylinder renewal digit

Fix the reciprocal numerator in `L-9806` to be `h=M_K`, and ask whether the
same room can extend with a proposed next itinerary digit `e in {0,1}`. The
resulting base-`5184` extension digit is

\[
\boxed{
c_K(e)
=81\left[(e-m_K)81^{-(2K+1)}\right]_{64}.
}
\tag{9}
\]

Therefore

\[
\boxed{c_K(e)=0\iff e\equiv m_K\pmod{64}.}
\tag{10}
\]

The reciprocal component cancels identically; the nonzero combined digit is
exactly a certificate that the current minimum room cannot renew.

### 4. Conditional depth-46 certificate

Condition on the internal exact computation `PR16/X-9303` and its proposed
wrapper `PR16/T-9314`. Their values satisfy

\[
M_{46}\equiv0\pmod{64},
\qquad M_{46}\equiv52\pmod{81},
\tag{11}
\]

and

\[
m_{46}\equiv26\pmod{64},
\qquad m_{46}\equiv1\pmod{81}.
\tag{12}
\]

Hence

\[
\boxed{M_{47}>M_{46},}
\tag{13}
\]

with simultaneous nonextension digits

\[
\boxed{c_{46}(0)=486,\qquad c_{46}(1)=4455.}
\tag{14}
\]

The certified depth-46 word begins `01`. This gives the sharper finite gap

\[
\boxed{M_{47}\ge M_{46}+960.}
\tag{15}
\]

All conclusions in this subsection retain the source certificate's
`INTERNAL EXACT`/`PROPOSED` status.

## Proof

If `A=81q+e>1` with `e in {0,1}`, then `q>=1` and

\[
B=64q+e<A,
\qquad T(B)=A.
\tag{16}
\]

If `A` survives `K` steps, `B` survives `K+1` steps and is a smaller
nontrivial depth-`K` survivor. This contradicts the minimality of `M_K`,
proving (4)--(5).

The survivor sets are nested in the standard-representative sense, so
`M_(K+1)>=M_K`. By (3), the deterministic state after the `K` certified steps
from `M_K` is `m_K`. If `m_K mod64` is `0` or `1`, the same start survives one
more step, forcing equality of the minima. Conversely, equality says that the
same ordinary start `M_K` belongs to `R_(K+1)`, so its deterministic endpoint
must have a legal residue. Equation (1) then gives (7).

Every forbidden residue produces a strict integer increase in `(M_K)`. Hence
infinitely many such residues force divergence. If there are only finitely
many, (6) makes `M_K` eventually constant. This proves (8).

For (9), use the simultaneous cylinder of `L-9806` at depth `K`. Since
`M_K<64^K<81^K`, taking `h=M_K` makes its canonical simultaneous
representative, itinerary representative, and fixed reciprocal integer all
equal to `M_K`. Thus `X_K=0`, while the itinerary endpoint is `tau_K=m_K`.
The proposed next digit gives

\[
p_K=[81^{-K}(e-m_K)]_{64}.
\tag{17}
\]

The fixed reciprocal integer extends without change, so the reciprocal
congruence for `c_K` is `c_K=0 mod81`. Write `c_K=81a`. The itinerary
congruence in `L-9806/(11)` becomes

\[
a\equiv(e-m_K)81^{-(2K+1)}\pmod{64},
\]

which proves (9)--(10).

For the conditional calculation, (12) and (6) prove (13). Since
`81 mod64=17` has inverse `49` and order four, substituting `K=46` in (9)
gives residues `6` and `55` for the bracket, proving (14).

Finally put `A=M_46`. Any `B>A` that survives even two steps has the form

\[
B-A=64j+e,
\qquad e\in\{0,1\}.
\tag{18}
\]

Because the first two certified digits of `A` are `01`, the second state of
`B` has residue

\[
1+17j+e\pmod{64}.
\tag{19}
\]

The least positive `64j+e` for which (19) is again `0` or `1` is obtained at
`j=15,e=0`, namely `960`. The old room `A` fails at step 47 by (12), and every
intermediate room fails already within two steps. This proves (15). ∎

## Motivation

The adelic program had reduced the ordinary section to divergence of a
monotone sequence of finite minima. This lemma identifies its exact renewal
bit and joins it to the simultaneous-cylinder digit from `L-9806`. The
universal problem is now visibly a repeated failure-of-renewal theorem, not a
generic equidistribution statement.

## Dependency audit

- `PR16/T-9313` supplies the exact endpoint/minimum duality (3) and the
  standard-representative monotonicity of `M_K`.
- Root descent, the renewal equivalence, and the `+960` local gap are elementary
  and rederived above.
- `L-9806` is used only for the simultaneous digit formula (9).
- The numerical depth-46 residues are explicitly conditional on
  `PR16/X-9303` and `PR16/T-9314`.

## Gap audit

- Equation (8) is an exact reformulation, not a proof that forbidden residues
  occur infinitely often.
- Periodic reciprocal digits do not determine the forward endpoint residue.
- The `+960` gap is finite and does not imply any asymptotic growth rate.
- No ordinary nontrivial survivor is constructed or excluded universally.

## Adversarial tests

- A legal endpoint residue gives equality in (6), not strict growth of the
  minimum; the tail state itself still grows whenever it exceeds `1`.
- The root condition is modulo `81`, whereas renewal is modulo `64`; swapping
  the two destroys the predecessor argument.
- In (9), the extra factor `81` is forced by the reciprocal congruence. Omitting
  it gives the itinerary component rather than the combined base-`5184` digit.
- The values in (11)--(15) are not promoted beyond their computational source.

## Remaining uncertainty

Whether the residues in (8) are forbidden infinitely often is exactly the
ordinary-section theorem. A useful intermediate target is a renewal-gap lower
bound that grows whenever the current root fails to extend.

## Suggested next attack

Given the certified word of `M_K`, compute symbolically the least positive
perturbation that survives its first `ell` steps. A lower bound tending to
infinity with `ell`, uniformly at every failed renewal, would turn the exact
local criterion into quantitative growth of `M_K`.
