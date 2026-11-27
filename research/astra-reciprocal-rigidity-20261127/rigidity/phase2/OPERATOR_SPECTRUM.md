# The ordinary squared-slope operator has a computable maximal fiber

**Proposed mathematical theorem.** Let `T` be the ordinary shortcut on the positive integers. Write `w(x)=1/4` for an even input and `w(x)=9/4` for an odd input. Consider the complex weighted composition operator `C f(x)=w(x)f(Tx)`, either on all positive integers or restricted to the actual basin of 1. For every `1≤p<∞` the two operators on the corresponding `ℓᵖ` spaces have **the same norm at every iterate** and the same spectrum, the closed disk of radius `9/4`. The same equality of spectra holds for `c₀` and `ℓ∞`.

On the known basin, the closed annulus `1≤|λ|≤9/4` lies in the continuous spectrum on `ℓᵖ` for `p<∞` and on `c₀`. At the physical eigenvalue 1 the full ordinary operator has a nonzero eigenvector precisely if an ordinary positive trajectory escapes. Its spectrum, spectral radius, and finite power norms have the same values regardless of that question. An extra positive cycle is not an eigenvector at 1, since the true product of its slopes is less than one.

## A chronological fiber fits in a short interval

Fix the shortcut time `k`, an endpoint `y`, and an even-input count `j`. Along a candidate path from `n` to `y`, write `e_i,o_i` for the prior counts at site `i`. Odd steps multiply `x+1` by `3/2`; even steps send it to `(x+1)/2+1/2`. Dividing each update by the cumulative slope and telescoping gives

\[
  n+1+E=Q,\qquad Q=2^k3^{-(k-j)}(y+1),\qquad
  E=\sum_{i\ {\rm even\ input}} 2^{e_i}(2/3)^{o_i}.
\]

Thus `0≤E≤2^j−1`. Every such integer preimage is in the same closed interval `[Q−2^j,Q−1]`, of length `2^j−1`. It has at most `2^j` integer occupants. This covers `j=0` and does not require a simple path. On any such path the product of the squared slopes is `(9/4)^k 9^{-j}`.

## The extremizing residue is exactly minus one

For `p<∞`, disjoint source fibers give

\[
 \|C^k\|_p^p= (9/4)^{kp}\sup_y\sum_{n:T^kn=y}9^{-p e_k(n)}.
\]

Here `e_k` is the number of even inputs through the stated `k` steps. In general the normalized sum is at most `Σ_{j≥0}(2/9^p)^j`. If there is no all-odd preimage it is at most `(2/9^p)/(1−2/9^p)<1`. An all-odd preimage exists exactly when `y≡−1 mod 3^k` (for `k≥1`): its start is `2^k((y+1)/3^k)−1`. Its single contribution already equals 1.

Within this residue every admissible length-`k` inverse word agrees with the admissible bank at the signed integer endpoint `−1`. An inverse even branch doubles the current integer and preserves congruence modulo the current power of 3. An odd inverse branch `(2y−1)/3` is allowed precisely at residue 2 modulo 3 and costs one digit of precision. Initial agreement modulo `3^k` therefore couples all the choices until step `k`. Each integral inverse branch is positive when started from a positive endpoint, and parity makes different words lead to different integers at a fixed depth. The same holds on the signed graph when starting from `−1`. Consequently every ordinary positive `y≡−1 mod 3^k` realizes the same, strictly maximal normalized fiber mass. At least one such `y` in the basin of 1 exists for every `k`, as shown below. All its positive preimages are also in that basin.

Reflecting the signed negative orbit gives `R(x)=x/2` at even inputs and `R(x)=(3x−1)/2` at odd inputs, with `R(1)=1`. Let `E(n)` count even inputs until the first hit of 1 under `R`. The exact result, for all `k≥0`, is

\[
 \boxed{\quad \|C^k\|_p=(9/4)^k
    \left(\sum_{R^k n=1} 9^{-p E(n)}\right)^{1/p}.\quad}
\]

If `m_j` counts all reflected positive starts with exactly `j` even inputs before first hitting 1, then `m_j≤2^j`. In reverse from 1 an even branch doubles and a nontrivial odd branch strictly decreases. Therefore a first-hit path with `j` even steps stays within `[1,2^j]` and has length at most `2^j−1`. This proves both the bound and an exact finite enumeration for each `m_j`. Monotone convergence gives the limit of the parenthesized factor before its `1/p` power as `Σ_{j≥0}m_j 9^{-pj}`, with tail after `J` at most `(2/9^p)^{J+1}/(1−2/9^p)`. For `p=1` it is about `1.139084267651561`. For `c₀` and `ℓ∞`, an all-odd path gives the exact norm `(9/4)^k` directly. All these spaces thus have spectral radius `9/4`.

## A known terminating source for arbitrarily large amplification

For `k≥1` put

\[
 e_k=1+3^k,\qquad q_k=(2^{e_k}-1)/3,\qquad
 t_k=(q_k+1)/3^k,\qquad x_k=2^k t_k-1 .
\]

The exponent `e_k` is even. The elementary identity `v₃(2^(3^k)+1)=k+1` follows by cubing, with the factor `a²−a+1` having exactly one factor of 3 when `a≡−1 mod3`. Hence `q_k` is an odd ternary unit and `q_k≡−1 mod3^k`. It goes directly to `2^(e_k−1)` and reaches 1 by halvings. Between `x_k` and `q_k` the first `k` steps are all odd. The exact profile is `3^i 2^(k−i)t_k−1` at step `i`. The path strictly increases through those steps, so its first hit of `q_k` is exactly at `k`. The different odd roots `q_k≥5` have disjoint predecessor trees. Each has only powers of two after its first step and therefore never reaches any other such root.

Suppose `0<|λ|<9/4` and `λ²≠9/16`. If `λI−C` had a bounded inverse, solve for forcing `δ_{q_k}` of norm one. On the unforced cycle `1,2` the recurrence gives zero, hence zero on the forward powers of two after `q_k`. The coefficient at `q_k` must equal `1/λ`. Pulling back along the all-odd path forces the coefficient at `x_k` to equal `(9/4)^k/λ^{k+1}`. This violates bounded inversion on every indicated space. The argument uses only known convergent starts, including for the operator on the full graph. Closedness of the spectrum supplies `0, ±3/4` and the boundary circle. The radius bound above excludes all exterior points.

## Continuous spectrum at the physical value

For a fixed positive target `y`, let `h_y(n)` be its first-hit time wherever finite. For `|λ|≥1` put

\[
  g_y(n)=\lambda^{-1-h_y(n)}\prod_{i<h_y(n)}w(T^i n)
\]

on that predecessor tree and zero elsewhere. The endpoint identity for a positive path gives `Π slope≤y/n` directly, so `|g_y(n)|≤y²/n²`. In particular every column belongs to `ℓ¹` and `c₀`. At each `n≠y` the exact residual of `λI−C` is zero. At `y` it is 1 if `y` does not return to itself, or `1−λ^{-d}Π_{i<d}w(T^i y)` on a cycle of minimal length `d`. The latter factor is nonzero since multiplying the exact positive endpoint laws around a cycle gives `Π slope<1` (there must be an odd site and its additive correction is positive). Rescaling supplies every coordinate impulse in the range, on both the full graph and the known basin. Thus the range is dense for `1≤p<∞` and for `c₀`. Density of finite support is not asserted on `ℓ∞`.

For `|λ|≥1` on the basin of 1, the homogeneous solution is identically zero by the unforced 1-cycle condition followed by propagation back along each finite path to 1. Within the disk the dense range is proper by the spectral result. In particular 1 is in the continuous spectrum on the known basin and has approximate eigenvectors there: normalize the exact, disjoint known columns `g_{q_k}` by their diverging norms when `1≤|λ|<9/4`. Their residual tends to zero. At the boundary use closedness of the approximate point spectrum. On the full graph a positive acyclic component carries a nonzero exact vector for `λ=1` by the ordinary calibration and finite-simple-path packing in [the preceding checkpoint](../ORDINARY_SPECTRUM.md); conversely, every true positive cycle forces an exact vector at 1 to vanish throughout its component. This isolates ordinary escape from extra cycles.

The same column estimate yields a useful difference in the order of limits. For each fixed positive `y`, the sum `Σ_{k≥0}||C^k δ_y||₁` is finite. In a nonperiodic target's tree each start contributes once and at most `y²/n²`. On a periodic target each repeated contribution is multiplied by its fixed cycle product less than 1. Thus every fixed impulse has summable iterates while the global operator norm grows exactly at the rate above.

## Comparison with earlier operators

Leventides and Poulios, *Koopman operators and the 3x+1-dynamical system*, Theorem 5.4, relate the unweighted `ℓ²` power norm to preimage multiplicities. The rStation paper 47, Theorem 5, analyzes the unweighted shortcut norm using ternary inverse-word fibers. Béhani studies a Collatz operator on weighted Bergman spaces. The norm reduction to fibers is standard. The squared weights in this note yield the unique maximizing ternary residue, the reflected normalized constant and an exact match of the full and known-basin spectra. [Leventides–Poulios](https://arxiv.org/pdf/2010.12987) · [rStation 47](https://rstation.ai/problems/collatz/papers/47) · [Béhani](https://doi.org/10.1090/proc/16627)
