# Polynomial-height occupation forces positive parity entropy

**PROPOSED.** Write x_j=T^j(n) for a simple infinite ordinary shortcut orbit and w_j=x_j mod 2. Let μ be any subsequential weak limit of the empirical distributions of the shifted infinite words σ^j w, for 0≤j<N. It is shift invariant. Fix A>0 and pass to a further subsequence on which the fraction of j<N with x_j≤N^A tends to δ. If δ>0, there exists a shift-invariant probability ν with

    δν ≤ μ,                 h₂(ν) ≥ 1/A.                            (1)

Here h₂ denotes the stationary binary entropy rate in bits. In particular:

* If μ is ergodic then δ>0 forces h₂(μ)≥1/A. For a parity-generic orbit with ergodic law of entropy h, the states ≤N^A thus have time density zero for every A<1/h.
* For arbitrary μ, δ≤A h₂(μ). Any zero-entropy subsequential limit forces density-zero occupation below every fixed polynomial along that subsequence. This concerns a single forward orbit; its shifts need not form a process initially sampled from μ.

## Extracting the high-entropy distribution

Let J be the selected low starts and K=ceil(A log₂N)+1, so 2^K>N^A. Equal K-symbol forward parity words force their initial states to be equal modulo 2^K. The states at starts in J are distinct and belong to [1,N^A], so all their K-symbol words are different. The uniformly selected word has entropy log₂|J|.

Form ν_N by choosing j uniformly in J and independently choosing a uniform offset in 0,…,K−1, then taking the entire shifted word starting there. Since K→∞ the shift changes ν_N by total variation at most 1/K. For any nonnegative bounded continuous test f, each actual timestamp occurs from at most K pairs, whence

    (|J|/N) ν_N(f) ≤ (1/N) Σ_(i=0)^(N−1) f(σ^i w) + (K/N)||f||∞.

By compactness take a subsequential limit ν. This gives invariance and domination in (1).

For each fixed m, split the uniformly chosen long word into disjoint m-symbol blocks for each of the m possible alignment residues. At most 2m symbols remain at the ends for each residue. By subadditivity of entropy, summing these m decompositions and then using concavity on the offset distributions gives

    m log₂|J| ≤ 2m² + K H_m(ν_N),

where H_m is the entropy of the first m binary symbols. Indeed the wholly contained blocks use each offset from 0 to K−m exactly once across the alignments. The remaining offsets contribute nonnegative entropy. For fixed m, continuity of H_m and log₂|J|/K→1/A yield H_m(ν)/m≥1/A. Take the infimum over m for a stationary process. This proves (1).

If μ is ergodic then domination and invariance give ν=μ by extremality, including the case δ=1. More generally split μ into δν and its invariant positive remainder. Concavity of every finite-block entropy gives h₂(μ)≥δh₂(ν) by taking normalized limits. No independence or rate of empirical convergence is required.

The critical parity-frequency packing estimates already give a height lower exponent for every simple orbit; (1) addresses the entropy of each particular orbit's limiting law and can be stronger for low-entropy limits. The prior factor-complexity cone concerns a different induced recurrence. [Critical packing and prior strict power saving](../critical-orbit-mellin/HEIGHT_CAP.md) · [Induced factor-complexity cone](../integrated/factor-complexity/README.md)
