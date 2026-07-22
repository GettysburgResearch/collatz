# L-9858 -- Residual-to-address correction isometry

Claim ID: `L-9858`  
Title: Every finite physical padding correction is an isometric permutation of the residual quotient  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`  
Reviewing agents: `gpt56-synthesis-01`, `gpt56-synthesis-01-h`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9820`, `L-9852`; `PR3/T-0026` and `PR3/T-0028`  
Scope: finite residual-to-address coupling inside one bijective connector-isometry chart  
Related counterexample candidates: none

## Definitions

Let

\[
\Omega:\mathbb Z_2\longrightarrow\mathbb Z_2
\tag{1}
\]

be the bijective connector isometry supplied by `PR3/T-0028`.  Thus

\[
\nu_2\!\left(\Omega(x)-\Omega(y)\right)
=\nu_2(x-y)
\qquad(x,y\in\mathbb Z_2),
\tag{2}
\]

with the convention `nu_2(0)=infinity`.  Define the target-address map

\[
\mathcal A(w)=\Omega^{-1}(-w),
\qquad
a_V=\mathcal A(V),
\qquad
a_h=\mathcal A(h).
\tag{3}
\]

The minus sign in (3) is part of the physical connector convention.  The map
`mathcal A` is again a bijective isometry.

For `x in Z_2`, let `[x]_(2^M)` denote its canonical representative in
`{0,...,2^M-1}`.  If `H>=0`, `V in Z_2`, and

\[
h=V+2^Hd,
\qquad d\in\mathbb Z_2,
\tag{4}
\]

define the normalized address correction

\[
\boxed{
\Psi_{H,V}(d)
=\frac{\mathcal A(V+2^Hd)-\mathcal A(V)}{2^H}.
}
\tag{5}
\]

The quotient in (5) will be proved integral below.

## Statement

### 1. Exact residual-to-address valuation law

For every `h,V in Z_2`,

\[
\boxed{
\nu_2(a_h-a_V)=\nu_2(h-V).
}
\tag{6}
\]

Consequently the physical and bulk addresses have the same first `H` bits
if and only if the physical tail and bulk word have the same first `H` bits:

\[
\boxed{
a_h\equiv a_V\pmod {2^H}
\iff
h\equiv V\pmod {2^H}.
}
\tag{7}
\]

### 2. Every normalized correction is a pointed bijective isometry

For every `H>=0` and `V in Z_2`, formula (5) defines a bijective isometry

\[
\boxed{
\Psi_{H,V}:\mathbb Z_2\longrightarrow\mathbb Z_2,
\qquad
\Psi_{H,V}(0)=0,
}
\tag{8}
\]

and

\[
\boxed{
\nu_2\!\left(\Psi_{H,V}(d_1)-\Psi_{H,V}(d_2)\right)
=\nu_2(d_1-d_2).
}
\tag{9}
\]

In particular its first bit is universal:

\[
\boxed{
\Psi_{H,V}(d)\equiv d\pmod2.
}
\tag{10}
\]

For every `Q>=1`, the finite truncation

\[
\boxed{
\psi_{H,V}^{(Q)}:
\mathbb Z/2^Q\mathbb Z\longrightarrow\mathbb Z/2^Q\mathbb Z,
\qquad
[d]_{2^Q}\longmapsto[\Psi_{H,V}(d)]_{2^Q},
}
\tag{11}
\]

is a well-defined permutation fixing zero.  It is an isometry for the
truncated dyadic valuation.

### 3. Exact canonical finite-prefix formula

Put

\[
A_V^{(H+Q)}=[a_V]_{2^{H+Q}},
\qquad
A_h^{(H+Q)}=[a_h]_{2^{H+Q}},
\tag{12}
\]

and let

\[
C_{H,V}^{(Q)}(d)=[\Psi_{H,V}(d)]_{2^Q}.
\tag{13}
\]

Under (4), the exact correction of canonical address prefixes is

\[
\boxed{
\left[A_h^{(H+Q)}-A_V^{(H+Q)}\right]_{2^{H+Q}}
=2^H C_{H,V}^{(Q)}(d).
}
\tag{14}
\]

Equivalently,

\[
\boxed{
A_h^{(H+Q)}
\equiv A_V^{(H+Q)}
+2^HC_{H,V}^{(Q)}(d)
\pmod {2^{H+Q}}.
}
\tag{15}
\]

The modular brackets in (14) are essential: the naked difference of two
canonical representatives may cross the endpoint `2^(H+Q)`.

The construction is finite.  If `Omega_(H+Q)` is the permutation induced by
`Omega` modulo `2^(H+Q)`, then both prefixes in (12), and hence (13), are
obtained entirely from `Omega_(H+Q)^(-1)`.  No completed address need be
evaluated to construct the `Q`-bit correction table. In a physical connector
application, this statement is used only when `H+Q` lies within the available
connector-prefix precision.

At `Q=1`, if `beta_V` and `beta_h` are the address bits at position `H`, then

\[
\boxed{
\beta_h=\beta_V\mathbin\oplus(d\bmod2).
}
\tag{16}
\]

Thus (16) is exactly the residual-defect XOR law of `L-9852`, now identified
as the first bit of a full correction isometry.

### 4. Odd-affine zipper cylinders realize every correction word

Specialize in this section to an ordinary bulk word `V in Z`. Assume the
physical zipper output of `PR3/T-0026` has the form

\[
h(y)=\psi+Ny,
\qquad
\psi\in\mathbb Z,
\qquad
N>0\text{ odd}.
\tag{17}
\]

For fixed `H` and bulk word `V`, let

\[
\boxed{
y_H^*=[(V-\psi)N^{-1}]_{2^H}
\in\{0,\ldots,2^H-1\}.
}
\tag{18}
\]

Then `h(y) congruent V modulo 2^H` exactly on the cylinder

\[
y=y_H^*+2^Ht,
\qquad t\in\mathbb Z_2.
\tag{19}
\]

Define the integral cylinder offset

\[
d_H^*=\frac{\psi+Ny_H^*-V}{2^H}\in\mathbb Z
\tag{20}
\]

If `psi,V` are instead allowed to be arbitrary elements of `Z_2`, the same
definition gives `d_H^* in Z_2` and all isometry and finite-permutation
conclusions below remain valid. The ordinary-integrality and eventual-
nonnegativity assertions use the physical specialization just stated.

Define the normalized zipper correction

\[
\boxed{
\Theta_{H,V,\psi,N}(t)
=\frac{a_{h(y_H^*+2^Ht)}-a_V}{2^H}
=\Psi_{H,V}(d_H^*+Nt).
}
\tag{21}
\]

Then

\[
\boxed{
\Theta_{H,V,\psi,N}:\mathbb Z_2\longrightarrow\mathbb Z_2
\text{ is a bijective isometry}.
}
\tag{22}
\]

Consequently, for every `Q>=1`,

\[
\boxed{
[t]_{2^Q}
\longmapsto
[\Theta_{H,V,\psi,N}(t)]_{2^Q}
}
\tag{23}
\]

is a permutation of `Z/2^Q Z`.  Every `Q`-bit address-correction word occurs
for exactly one quotient class `t modulo 2^Q`.  Because every such class has
arbitrarily large nonnegative representatives, all finite correction words
also occur on ordinary nonnegative zipper inputs, with nonnegative zipper
output `h(y)` once the representative is sufficiently large. This last
assertion concerns the odd-affine formula itself; it does not assert that
those representatives obey a separate finite stage cap or the full physical
grammar.

### 5. Exact information lower bound and sufficiency

Fix the chart data `H,V,psi,N,Omega` and a precision `Q`.  Suppose a proposed
deterministic finite rule receives residual-dependent information only
through a state

\[
\sigma:\mathbb Z/2^Q\mathbb Z\longrightarrow\mathcal S
\tag{24}
\]

Precisely, assume there is an output map
`g:S -> Z/2^Q Z`, allowed to depend on all the fixed chart data, such that
`g(sigma([t]_(2^Q)))=[Theta_(H,V,psi,N)(t)]_(2^Q)` for every quotient class.
The rule has no other input channel depending on `t`.

Then

\[
\boxed{|\mathcal S|\ge2^Q.}
\tag{25}
\]

Indeed, two quotient classes with the same state would receive the same
output, while (23) assigns them different outputs.  Thus at least `Q` bits of
residual-dependent state are necessary in the worst case.

Conversely, the raw residue `[t]_(2^Q)`, or equivalently
`[d_H^*+Nt]_(2^Q)`, is sufficient: apply the finite permutation (23) and then
(15).  Hence exactly `Q` residual bits are information-theoretically
necessary and sufficient for `Q` physical address-correction bits.

### 6. Interpretation boundary

The sufficiency in Section 5 is a finite lookup/permutation statement.  Its
state space has size `2^Q`, may depend on the chart and on `H,V,psi,N`, and
need not admit a bounded local update as `Q` or the scale changes.  The
theorem does not:

1. force the zipper into the compatibility cylinder (19);
2. derive a scale-to-scale recurrence for its correction state;
3. route the remaining physical connector block or certify intermediate
   Collatz crossings; or
4. prove that either completed 2-adic address is an ordinary integer.

It is an exact finite-prefix coupling theorem, not a completed ordinary
realization.

## Proof

### Valuation law and ball restriction

Negation, `Omega^(-1)`, and their composition `mathcal A` are bijective
isometries.  Therefore

\[
\nu_2(a_h-a_V)
=\nu_2\!\left((-h)-(-V)\right)
=\nu_2(h-V),
\tag{26}
\]

proving (6)--(7).

Every bijective isometry maps each dyadic ball onto the ball of the same
radius around the image of its center.  In the present notation,

\[
\boxed{
\mathcal A(V+2^H\mathbb Z_2)
=a_V+2^H\mathbb Z_2.
}
\tag{27}
\]

For completeness, isometry gives the forward inclusion.  Conversely, if
`z in a_V+2^H Z_2`, put `w=-Omega(z)`.  Then `mathcal A(w)=z`, while
`Omega(z) congruent Omega(a_V)=-V modulo 2^H`; hence
`w congruent V modulo 2^H`.  This proves the reverse inclusion without a
compactness or counting argument.

Equation (27) proves that (5) is integral and surjective after division by
`2^H`; injectivity follows from injectivity of `mathcal A`.  For two inputs,

\[
\begin{aligned}
\nu_2\!\left(
\Psi_{H,V}(d_1)-\Psi_{H,V}(d_2)
\right)
&=\nu_2\!\left(
\mathcal A(V+2^Hd_1)-\mathcal A(V+2^Hd_2)
\right)-H\\
&=\nu_2\!\left(2^H(d_1-d_2)\right)-H\\
&=\nu_2(d_1-d_2).
\end{aligned}
\tag{28}
\]

This proves (8)--(9).  A pointed isometry of `Z_2` preserves the even ball
`2Z_2` and its complement.  Since `Psi(0)=0`, it induces the identity on the
two-element quotient, proving (10).  Notice that the negative physical target
in (3) disappears only modulo two; no higher-bit formula `Psi(d)=d` is
asserted.

### Finite permutations and canonical representatives

Equation (9) implies

\[
d_1\equiv d_2\pmod {2^Q}
\iff
\Psi_{H,V}(d_1)\equiv\Psi_{H,V}(d_2)\pmod {2^Q}.
\tag{29}
\]

Thus (11) is well-defined and injective; finiteness makes it bijective.  It
fixes zero by (8), and (29) also preserves every truncated valuation stratum.

The identity in `Z_2`

\[
a_h-a_V=2^H\Psi_{H,V}(d)
\tag{30}
\]

reduced modulo `2^(H+Q)` proves (14)--(15).  Reduction of (30) modulo
`2^(H+1)`, followed by division by `2^H`, proves (16).  The construction from
the induced finite permutation `Omega_(H+Q)` follows because a bijective
isometry preserves congruence in both directions and therefore induces a
bijection at every finite precision.

### Zipper cylinder and information count

Since `N` is odd, it is invertible modulo every power of two.  This proves the
unique cylinder (18)--(19).  Substitution gives

\[
\frac{h(y_H^*+2^Ht)-V}{2^H}
=d_H^*+Nt,
\tag{31}
\]

which proves (21).  The affine map `t mapsto d_H^*+Nt` is a bijective
isometry of `Z_2`, so its composition with the bijective isometry `Psi` proves
(22)--(23).

If a decoder factors the permutation (23) through `sigma`, injectivity of
(23) forces `sigma` to be injective.  This proves (25).  Taking `sigma` to be
the identity residue and the decoder to be the finite permutation proves
sufficiency.  Equations (14)--(15) then recover the physical address prefix.
This completes the proof. QED

## Motivation

`L-9852` identified one indispensable residual-defect bit at the first
bulk-to-physical padding lift.  The present result shows that this was not an
isolated XOR accident.  At every precision, the residual quotient and the
physical address correction are related by an exact isometric permutation.

This gives the sharp finite information content of the interface.  A
`Q`-bit correction cannot be reconstructed from fewer than `Q` bits of
residual-dependent state, while those `Q` bits always suffice through a
finite chart permutation.  What remains is dynamical rather than
information-theoretic: update that state locally as the scale and zipper
change.

## Dependency audit

- `PR3/T-0028` supplies the bijective connector isometry `Omega`.
- `PR3/T-0026` supplies the positive odd-affine zipper output.
- `L-9820` supplies the finite inverse-isometry and canonical-prefix
  interpretation.
- `L-9852` supplies the physical bulk/residual interface and its one-bit XOR
  law; equation (16) recovers and extends it.
- The ball-surjectivity, normalized isometry, finite permutation, zipper
  conjugacy, and information lower bound are proved directly.
- No completed inverse-bulk limit, numerical search, or ordinary seed is used.

## Gap audit

- Compatibility `h congruent V modulo 2^H` is characterized, not forced.
- The theorem gives a family of finite permutations, not a uniform bounded
  transducer or a scale-to-scale recurrence.
- Its exact `Q`-bit information lower bound allows other implementations with
  `2^Q` states; it does not require storing the raw quotient bits literally.
- The chart permutation can vary with `H` and `V`, and a table of size `2^Q`
  is not a constant-state grammar.
- Finite 2-adic prefixes do not imply that the completed address or tail is an
  ordinary integer.

## Adversarial tests

- The target changes from `-V` to `-h`; the normalized input displacement is
  `-d`, not `d`.  Parity erases that sign in (10), but higher correction bits
  are governed by the full isometry `Psi` and need not equal the raw bits of
  either `d` or `-d`.
- Canonical representative subtraction must be reduced modulo `2^(H+Q)` as
  in (14).  A naked ordinary subtraction can be negative or include a wrap.
- Global bijectivity of `Omega` is used to make the restricted ball map onto,
  not merely into, the address ball.
- Oddness of `N` is essential.  If `N` were even, the zipper quotient would
  reach only a proper correction subcylinder and the `2^Q` information count
  would change.
- The information lower bound counts only residual-dependent state.  It does
  not charge fixed chart data or forbid recomputation from another channel
  that already contains the same `Q` residual bits.
- The `2^Q` lower bound ranges over the full odd-affine quotient cylinder. A
  stage-specific cap that admits fewer quotient residues gives only the
  corresponding restricted cardinality bound.
- The assertion `d_H^* in Z` uses the ordinary physical specialization
  `psi,V in Z`. For abstract 2-adic chart data the correct conclusion is only
  `d_H^* in Z_2`, and eventual ordinary nonnegativity is not asserted.
- Choosing `Q=K-H` does not by itself prove a legal physical rewrite through
  the remaining connector: local exposure, nonnegativity, and intermediate
  orbit constraints are separate.

## Remaining uncertainty

Can the scale-level Montgomery zipper update the finite correction word under
its quadratic bulk recurrence using bounded local state per emitted bit?  The
present theorem proves that no compression below one residual bit per address
bit is possible in the worst case, but it does not decide whether a streaming
one-bit-per-step realization exists.

## Suggested next attack

Write the finite reductions of consecutive chart isometries as permutations
`psi_(H,V)^(Q)` and conjugate the exact stage affine zipper map through them.
Determine whether the resulting correction update is triangular in the
least-significant bit.  A uniform triangular recurrence would turn the
information-theoretic sufficiency above into a bounded streaming rewrite;
failure would quantify the extra cross-scale memory beyond the unavoidable
`Q` residual bits.
