# Iteration 05: centered ghost rooms and the ordinary-section minimum

All theorem-level claims remain `PROPOSED` pending independent review. The
finite minimum computation `X-9504` is `EMPIRICAL / EXACT FINITE CHECK` only.
No claim here proves divergence of the minimum sequence.

This iteration adapts the fixed-room ordinary-section viewpoint used elsewhere
in the repository to the H ghost IFS. The resulting scalar extremal is stronger
than the prefix-expanding minimum `mu_L`: its divergence would exclude every
nontrivial infinite exact H orbit directly, without first invoking contracting
cylinder descent.

---

## L-9516: Centered decomposition around the fixed ghost `4`

**Claim ID:** `L-9516`  
**Title:** Nontrivial H ghosts occupy disjoint valuation rooms around `4`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** `L-9514`

### Statement

Let

\[
 \phi_r(x)=2^{3r+2}3^{-(2r+1)}(x-1)
\]

and let `G` be the H ghost closure from `L-9514`. Put

\[
 \mathcal H=\bigcup_{r\ge1}\phi_r(G).
\]

Then `4` is the unique all-zero fixed ghost,

\[
 \phi_0(4)=4,
\]

and

\[
 \boxed{
 G=\{0,4\}\ \sqcup\ 
 \bigsqcup_{q\ge0}\phi_0^q(\mathcal H).
 }
 \tag{1}
\]

For every

\[
 x\in\phi_0^q(\mathcal H)
\]

one has

\[
 \boxed{v_2(x-4)=2q+2.}
 \tag{2}
\]

Thus the number of initial zero letters before the first nonzero letter is
recovered exactly from the ordinary centered valuation.

### Proof

Every nonzero itinerary is either the all-zero itinerary, whose ghost is the
fixed point `4`, or has a unique first nonzero letter after `q>=0` zeros. This
gives the set decomposition apart from disjointness.

If `y in H`, then its first letter is at least one, so

\[
 v_2(y)\ge5.
\]

Hence

\[
 v_2(y-4)=2.
\]

Since

\[
 \phi_0(x)-4=\frac43(x-4),
\]

iteration gives

\[
 \phi_0^q(y)-4=(4/3)^q(y-4),
\]

whose valuation is `2q+2`. The room labels are therefore disjoint. The closure
point `0` is separate, proving (1)--(2).

### Ordinary-coordinate form

If a positive ordinary ghost `P!=4` lies in room `q`, then

\[
 P=4+4^{q+1}z
\]

for a positive odd integer `z`, and after the initial `q` zero letters the exact
state is

\[
 \boxed{T_0^q(P)=4(1+3^qz).}
 \tag{3}
\]

The next letter is nonzero, so the right side is divisible by at least `2^5`.
This is a natural integral coordinate for the transformed-height problem
`Q-9505`.

---

## T-9510: Monotone ordinary-section minimum

**Claim ID:** `T-9510`  
**Title:** H termination is equivalent to divergence of one monotone ghost minimum  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** `L-9503`, `L-9514`

### Definition

For `K>=1`, let

\[
 G_K=G\pmod{2^K}.
\]

Define

\[
 \boxed{
 \nu_K=\min\left\{
 P\ge16:
 P\equiv1\pmod3,
 \ P\bmod2^K\in G_K
 \right\}.
 }
 \tag{4}
\]

The formal fixed ghost `4` is automatically excluded by `P>=16`.

### Statement

The sequence `nu_K` is nondecreasing. The following are equivalent:

1. there is a positive infinite exact H orbit;
2. there is a positive ordinary ghost `P>=16` with `P=1 mod 3`;
3. `nu_K` is bounded;
4. `nu_K` eventually stabilizes;
5. `nu_K` does not tend to infinity.

Consequently

\[
 \boxed{
 H\text{ terminates on every positive integer}
 \quad\Longleftrightarrow\quad
 \nu_K\longrightarrow\infty.
 }
 \tag{5}
\]

### Proof

Projection sends `G_(K+1)` into `G_K`. Every integer admissible at precision
`K+1` is therefore admissible at precision `K`, proving monotonicity.

An infinite exact orbit gives one fixed ordinary integer in every finite ghost
residue set, so `nu_K` is bounded. Conversely, a bounded nondecreasing integer
sequence stabilizes, say at `P`. Then

\[
 P\bmod2^K\in G_K
\]

for every sufficiently large `K`, hence for every `K` by projection. Branch
separation determines the first exact letter from `v_2(P)` and sends the tail
state back into every lower-precision ghost set. Iterating gives an infinite
exact future. Equivalently, one may apply the stabilization equivalences in
`L-9503`. This proves all equivalences.

### Relationship to earlier extremals

The prefix-expanding minimum `mu_L` addresses the survivor tail remaining after
a descent theorem. The new `nu_K` addresses the entire ordinary section of the
ghost attractor. Its divergence is stronger: it proves termination without
using `C-9501`.

---

## Q-9506: Prove ordinary-section minimum divergence

**Claim ID:** `Q-9506`  
**Title:** Show that the centered ghost rooms contain no fixed positive ordinary integer  
**Status:** `IDEA`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `L-9516`, `T-9510`

### Target

Prove

\[
 \nu_K\to\infty.
\]

The centered decomposition suggests splitting by the fixed finite room

\[
 q=(v_2(P-4)-2)/2.
\]

For fixed `q`, write

\[
 P=4+4^{q+1}z,
 \qquad z\text{ positive odd},
\]

and use (3) to move to the first nonzero branch. A successful transformed-height
theorem should show that a fixed positive `z` cannot survive arbitrarily deep
refinements unless the itinerary is all zero.

The sequence `nu_K` is suitable for exact finite minimum certificates and
meet-in-the-middle searches, but finite growth alone is not an asymptotic proof.

---

## X-9504 finite checkpoint

The exact computation through precision `K=50` gives

\[
 \boxed{\nu_{50}=10,205,790,208.}
\]

One residue path attaining this checkpoint begins

```text
(6,1,0,1,0,0,1,0)
```

at the available precision. The monotone minimum is not strictly increasing at
every bit precision; finite plateaus occur. This mirrors the zero-carry
plateaus in prefix-cylinder minima and again shows that an asymptotic proof must
exclude infinite stabilization, not every finite plateau.
