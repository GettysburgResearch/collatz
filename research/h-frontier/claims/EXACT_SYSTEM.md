# Exact H block, cylinder, ghost, and toll claims

All claims in this file are `PROPOSED` until independently reviewed.

## D-9501: Exact block system

**Claim ID:** D-9501  
**Title:** Exact `p`-coordinate block system for H  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** none  
**Scope:** the partial H subsystem  
**Related counterexample candidates:** none

### Statement

At an H-state `n=4x`, define

\[
p=3n+4=12x+4.
\]

Let a block consist of one `n -> 3n/4` step followed by exactly `r>=0`
applications of `n -> (9n+1)/8`, ending at another multiple of 4. Put

\[
e_r=3r+2,\qquad s_r=2r+1.
\]

The block is exact legal precisely when

\[
p=2^{e_r}u,\qquad u\equiv1\pmod4,\qquad p\equiv1\pmod3,
\]

and the next `p`-state is

\[
\boxed{p^+=\frac{3^{s_r}}{2^{e_r}}p+1=3^{s_r}u+1.}
\]

Every infinite H-orbit has infinitely many such block states.

### Proof

After the first branch, `y=3n/4` and

\[
y+1=(3n+4)/4=p/4.
\]

After `r` second-branch steps,

\[
B^r(y)+1=9^r p/2^{3r+2}.
\]

The endpoint is a multiple of 4 exactly when the last displayed quotient is
`1 mod 4`. Since `9^r=1 mod 4`, this is equivalent to
`p=2^(3r+2)u` with `u=1 mod 4`. If the endpoint is `n^+`, then

\[
p^+=3n^++4=3(n^++1)+1=3^{2r+1}u+1.
\]

Finally, an eventual infinite run of only the second branch would require
`8^j | n+1` for every `j`, which is impossible for a fixed positive integer.

### Gap audit

The formal exact state `p=4` corresponds to `x=0`, not a positive H A-state.
Positive H A-states have `p>=16`.

---

## L-9501: H-to-Collatz lift

**Claim ID:** L-9501  
**Title:** An infinite positive H-orbit lifts to an infinite shortcut-Collatz orbit  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** D-9501  
**Scope:** relation to the repository counterexample objective

### Statement

Let

\[
C(N)=\begin{cases}N/2,&N\text{ even},\\(3N+1)/2,&N\text{ odd}.
\end{cases}
\]

If `n_0,n_1,...` is an infinite positive H-orbit, then `N_i=8n_i+1`
occurs as a subsequence of one infinite shortcut-Collatz orbit. Therefore a
counterexample to H is a counterexample to Collatz.

### Proof

If `n=0 mod 4`, then

\[
8n+1\xmapsto{C}12n+2\xmapsto{C}6n+1
=8(3n/4)+1.
\]

If `n=7 mod 8`, then

\[
8n+1\xmapsto{C}12n+2\xmapsto{C}6n+1
\xmapsto{C}9n+2
=8((9n+1)/8)+1.
\]

Concatenating these exact finite segments lifts the whole H-orbit.

### Gap audit

The converse statement is not claimed here.

---

## L-9502: Exact finite cylinders

**Claim ID:** L-9502  
**Title:** Every finite block word has one exact arithmetic-progression cylinder  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** D-9501

### Statement

For a word `w=(r_0,...,r_{L-1})`, define

\[
E_i=\sum_{j<i}(3r_j+2),\qquad
S_i=\sum_{j<i}(2r_j+1).
\]

The endpoint map is

\[
F_w(P)=\frac{3^{S_L}P+C_w}{2^{E_L}},
\qquad
C_w=\sum_{k=1}^L2^{E_k}3^{S_L-S_k}.
\]

Define

\[
g_w\equiv-\sum_{k=1}^L2^{E_k}3^{-S_k}
\pmod{2^{E_L+2}}.
\]

There is a unique residue class modulo `3*2^(E_L+2)` satisfying

\[
P\equiv g_w\pmod{2^{E_L+2}},\qquad P\equiv1\pmod3.
\]

If `Pi(w)` is its least positive representative, then the exact positive
cylinder is

\[
\boxed{C(w)=\Pi(w)+3\,2^{E_L+2}\mathbb Z_{\ge0}.}
\]

In particular, every finite word is exactly realizable.

### Proof

Unrolling the recurrence gives, for each prefix,

\[
p_i=\frac{3^{S_i}}{2^{E_i}}
\left(P+\sum_{k=1}^i2^{E_k}3^{-S_k}\right).
\]

Assume the final ghost congruence. Reducing it modulo
`2^(E_(i+1)+2)` makes all terms with `k>i+1` vanish, hence `p_(i+1)` is
divisible by 4. The recurrence

\[
p_{i+1}-1=3^{2r_i+1}p_i/2^{3r_i+2}
\]

then implies `2^(3r_i+2)|p_i`; reducing modulo 4 and using
`3^(2r_i+1)=3 mod 4` gives an odd core `1 mod 4`. The mod-3 condition
propagates because every endpoint is `1 mod 3`.

Conversely, exact realization makes the final endpoint divisible by 4, so the
unrolled formula gives the stated ghost congruence. CRT supplies one residue
class modulo `3*2^(E_L+2)`.

### Equivalent recursive form

For a one-letter word,

\[
\alpha(r)=2^{3r+2}\pmod{2^{3r+4}}.
\]

For a first letter `r` and suffix `v`,

\[
\boxed{
\alpha((r)v)\equiv
2^{3r+2}3^{-(2r+1)}(\alpha(v)-1)
\pmod{2^{3r+2+E_v+2}}.
}
\]

This follows by solving the requirement that the first endpoint lie in the
suffix cylinder. Thus the direct ghost and recursive constructions agree.

### Gap audit

An earlier thread asserted that the final ghost congruence could miss
intermediate exactness. The prefix reduction above corrects that assertion.

---

## L-9503: Carry recursion and ghost stabilization

**Claim ID:** L-9503  
**Title:** Exact carries, monotone representatives, and positive-integer ghosts  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9502

### Statement

Let `F_w(Pi(w))=4Y_w`. Appending `r` selects a unique carry

\[
c(w,r)\in\{0,\ldots,2^{3r+2}-1\}
\]

satisfying

\[
\boxed{
c(w,r)\equiv
(2^{3r}-Y_w)(3^{S_w+1})^{-1}
\pmod{2^{3r+2}}.
}
\]

Then

\[
\boxed{
\Pi(wr)=\Pi(w)+3\,2^{E_w+2}c(w,r).
}
\]

For an infinite itinerary `r`, define

\[
\mathcal G(\mathbf r)=
-\sum_{L\ge1}2^{E_L}3^{-S_L}\in\mathbb Z_2.
\]

The following are equivalent:

1. a positive ordinary integer follows the itinerary forever;
2. `Pi(w_L)` is bounded;
3. `Pi(w_L)` eventually stabilizes;
4. all sufficiently late carries are zero;
5. `G(r)` is a positive ordinary integer congruent to 1 modulo 3.

### Proof

Every parent-cylinder point is

\[
p=\Pi(w)+3\,2^{E_w+2}t.
\]

The endpoint satisfies

\[
F_w(p)/4=Y_w+3^{S_w+1}t.
\]

The next exact class is `2^(3r) mod 2^(3r+2)`, giving the displayed unique
carry and representative update. Hence representatives are nondecreasing.

A fixed positive integer follows every prefix iff it lies in every cylinder,
which is equivalent to `Pi(w_L)` being bounded by that integer. A bounded
nondecreasing integer sequence stabilizes. The ghost is the compatible limit
of the cylinder residues modulo powers of 2, giving the last equivalence.

---

## L-9504: Toll-Euler identity

**Claim ID:** L-9504  
**Title:** Exact additive and multiplicative toll formulas  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** D-9501

### Statement

For an exact orbit and prefix multipliers

\[
M_L=\prod_{i<L}\frac{3^{2r_i+1}}{2^{3r_i+2}},
\]

one has

\[
\boxed{
\frac{p_L}{M_L}=p_0+\sum_{k=1}^L\frac1{M_k}
}
\]

and

\[
\boxed{
p_0+\sum_{k=1}^L\frac1{M_k}
=p_0\prod_{j=1}^L\left(1-\frac1{p_j}\right)^{-1}.
}
\]

### Proof

The additive identity follows by iterating `p_(i+1)=a_i p_i+1`.
Also `a_i=(p_(i+1)-1)/p_i`; multiplying these identities and solving for
`p_L/M_L` gives the Euler product.
