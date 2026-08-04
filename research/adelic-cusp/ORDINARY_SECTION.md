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

Its repetition-height inequality is the same completion-versus-height mechanism as `L-9310`'s reciprocal phase-carry theorem. The common constant

\[
\kappa
=
\frac1{\log_{64}81-1}
=
\frac{\log64}{\log(81/64)}
\]

is not an incompatibility. `R-9302` records this method closure.

The missing theorem must couple both cocycles through the same ordinary point.

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

`T-9313` proves

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

Conversely, coherent integral fixed-room equations reconstruct the ordinary survivor series exactly.

## 3. Exact finite duality

Let

\[
m_j=\min(C_j\setminus\{0,1\}),
\]

and let

\[
M_j=\min(R_j\setminus\{0,1\})
\]

be the exact first nontrivial depth-`j` survivor.

`T-9313` proves the constructive identity

\[
\boxed{
M_j
=
\left\lceil m_j(64/81)^j\right\rceil.
}
\]

The minimizing triadic word is reversed into chronological survivor order; the fixed-room identity reconstructs the starting room; direct recurrence replay ends at the minimizing triadic class.

The sequence is monotone:

\[
\boxed{M_{j+1}\ge M_j,}
\]

because every survivor valid for `j+1` steps is valid for `j` steps.

The ordinary-section problem is equivalent to

\[
\boxed{M_j\longrightarrow\infty.}
\]

## 4. Exact depth-46 certificate

`X-9303` computes `m_j` by meet-in-the-middle modular subset sums and replays the corresponding survivor exactly.

At depth `46`,

\[
\boxed{
M_{46}
=
275396778563393867136351926990265018601508986973296055235244496661568
>2^{227}.
}
\]

The chronological minimizing word is

```text
0110110111101001010000011100110000101010111011
```

and the replay ends at

\[
13995580641937679806861747515838198945935546006963182029787326398035667034.
\]

`T-9314` therefore excludes every nontrivial infinite ordinary survivor room through `2^227`, subject to independent replay.

Frozen digest:

```text
f2c4dd9b0c436c9450c03424b27d80366865f54bb8c286944a35047d0662c9bc
```

## 5. Exact remaining theorem

The infinite problem is now simply

\[
\boxed{M_j\longrightarrow\infty.}
\]

Equivalent formulations are:

1. no fixed `A>=2` supports coherent integral tails at every depth;
2. no bounded starting room belongs to every finite survivor set;
3. the nested active-cylinder blocks associated with one ordinary point cannot eventually terminate;
4. every bounded room eventually leaves the fixed-room past/future intersection.

The expected random scale is much larger than what the theorem needs. Any divergence, however slow, closes the ordinary section.

## 6. Highest-value next attacks

### A. Extendible minimum

`M_j` minimizes over every finite survivor prefix. A genuine infinite path must also admit extensions forever. Define the least **extendible** depth-`j` survivor and prove that it diverges. This may expose stronger pruning than the unconditional minimum.

### B. Active-cylinder block nonstabilization

PR #20's active-cylinder theorem says an infinite directive is ordinary exactly when its appended cylinder blocks eventually vanish. Identify those blocks with the fixed-room path and prove infinitely many are nonzero.

### C. First-return height gain

Use `L-9311` to turn any recurrence of a bounded coherent state into a zero-carry orbit difference. Prove that bounded-room coherence forces recurrence before the local height budget permits it.

### D. Monotone minimum recursion

Find an exact recursion or lower-envelope operator for `M_j`, retaining enough residue information to prove it cannot stabilize. This would turn the finite MITM data into a universal theorem.

## 7. Status boundary

- All-depth weighted EQ is proposed in `T-9312`.
- Fixed-room coherence and exact minimum duality are proposed in `T-9313`.
- The exact depth-46 minimum and bounded exclusion are proposed in `T-9314` and depend on bounded exact computation.
- No all-room nonintersection theorem is claimed.
- No ordinary Collatz counterexample, divergent seed, nontrivial cycle, or resolution is claimed.
