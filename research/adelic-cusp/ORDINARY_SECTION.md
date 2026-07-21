# Ordinary-section frontier after all-depth EQ

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Status:** theorem-level claims `PROPOSED`; exact computation bounded; no counterexample claimed

## 1. What the attempted decisive contradiction revealed

The proposed complexity--carry contradiction does not close by comparing its two critical constants.

`L-9311` proves that a repeated factor in an ordinary survivor itinerary is already an exact zero-carry chain for the difference of two ordinary tail orbits:

\[
64D_{i+1}=81D_i.
\]

Its repetition-height inequality is therefore the same completion-versus-height mechanism as `L-9310`'s reciprocal phase-carry theorem. The common constant

\[
\kappa
=
\frac1{\log_{64}81-1}
=
\frac{\log64}{\log(81/64)}
\]

is not an incompatibility. `R-9302` records this method closure explicitly.

The missing theorem must couple the two cocycles through the same ordinary point.

## 2. Fixed-room coherence

Let

\[
A=\Phi(\varepsilon)\in\mathbb Z_{\ge0}
\]

and let

\[
A_j=\Phi(\sigma^j\varepsilon)
\]

be its ordinary tail states. Define

\[
P_j
=
17\sum_{t=0}^{j-1}
\varepsilon_t81^{j-1-t}64^t.
\]

`T-9313` proves the exact invariant

\[
\boxed{
81^jA=64^jA_j+P_j.
}
\]

The quotient is the same room `A` at every depth.

If the past word is reversed, its triadic coordinate belongs to `C_j`, and

\[
A_j\pmod{81^j}
\]

is exactly that coordinate. Simultaneously, the future tail code puts `A_j` back in the infinite survivor attractor.

The real companion gives

\[
\boxed{
(81/64)^j(A-1)+1
\le A_j
\le(81/64)^jA.
}
\]

Thus a nontrivial ordinary survivor is exactly one coherent sequence of nontrivial `C_j` classes whose standard representatives remain in a critical moving window and whose room quotient never changes.

## 3. Finite exclusion certificates

Let

\[
m_j=\min(C_j\setminus\{0,1\}),
\]

and

\[
B_j
=
\min\left\{
64^j,
\left\lceil m_j(64/81)^j\right\rceil
\right\}.
\]

`T-9313` proves that every nontrivial ordinary room satisfies

\[
A\ge B_j
\]

for every `j`.

`X-9303` computes `m_j` exactly by meet-in-the-middle modular subset sums. At depth `44`,

\[
B_{44}
=
227578060273510610973552811001603322347312502177488333909527505984
>2^{217}.
\]

`T-9314` therefore excludes every nontrivial ordinary survivor room through `2^217`, subject to independent replay of the exact finite certificate.

## 4. The exact remaining theorem

The infinite problem is now:

\[
\boxed{
B_j\longrightarrow\infty.
}
\]

This is enough to exclude every fixed room `A>=2`.

Equivalent formulations include:

1. no fixed `A>=2` supports coherent integral tails satisfying the fixed-room equation at every depth;
2. the least nontrivial standard representative of `C_j` cannot stay below `O((81/64)^j)` along an infinite coherent path;
3. the nested active-cylinder blocks associated with the same ordinary point cannot eventually terminate;
4. every bounded room eventually leaves the past/future intersection window.

The expected random scale is much larger—roughly `32^j` after rescaling—but the theorem needs only divergence.

## 5. Highest-value next attacks

### A. Coherent minimum, not unconditional minimum

`m_j` minimizes over all `2^j` past words. A genuine ordinary path also requires future survivorship and compatibility with every earlier depth. Prove a lower bound for the **coherent** minimum, which may be much easier than controlling all of `C_j`.

### B. Active-cylinder block nonstabilization

PR #20's `T-9409` says an infinite directive selects one nested `2`-adic cylinder and is ordinary exactly when its newly appended blocks eventually vanish. Identify those blocks with the fixed-room representatives here and prove infinitely many are nonzero.

### C. First-return height gain

Use `L-9311` to turn any recurrence of a coherent past/future state into a zero-carry orbit difference. Show that coherence forces a recurrence before the local height budget permits it.

### D. Sign or product-formula certificate

The fixed-room numerator is an explicit ordinary integer at every depth. Seek a sign, valuation, or factorization invariant that cannot remain compatible with the critical moving window.

## 6. Status boundary

- All-depth weighted EQ is proposed in `T-9312`.
- The fixed-room characterization is proposed in `T-9313`.
- The bounded exclusion is proposed in `T-9314` and depends on exact finite computation.
- No all-room nonintersection theorem is claimed.
- No ordinary Collatz counterexample, divergent seed, nontrivial cycle, or resolution is claimed.
