# Exact worst-target quadratic curvature of genuine fixed-total Collatz rows

Let Δ=s−2n, t=|Δ|/sqrt(n), A(n,s)=2^s/3^n, and let R_F(y;n,s) count positive odd **unit** x with U^n x=y, S_n(x)=s, and 0≤y−x/A(n,s)≤F. There is an absolute finite F such that along **every** integer sequence with
\[
                 n\to\infty,\qquad t\to\infty,\qquad |\Delta|/n\to0,
\]
one has the exact minimax limit
\[
 \boxed{\quad\frac1{t^2}\log\left[\frac{\sqrt n}{A(n,s)}
              \inf_{y\ge1,\; y\ {\rm odd},\;3\nmid y}R_F(y;n,s)\right]
                 \longrightarrow-\frac14.\quad}                    \tag{1}
\]
The lower bound holds at every supplied ordinary target, even one moving with n. The upper bound uses a worst target at each pair (n,s) and makes no claim of a matching upper bound at a specified target. The range permits t to increase more slowly than sqrt(log n); keeping the precise sqrt(n) prefactor outside the logarithmic rate matters here.

## A single positive cylinder survives arbitrarily wide fixed central windows

Let π_n(s)=2^{−s} choose(s−1,n−1). There are **absolute** c₀,F₀>0 such that for each fixed B>0, some n₀(B) gives
\[
  R_{F_0}(y;n,s)\ge c_0 A(n,s)\pi_n(s)
  \quad (n\ge n_0(B),\ |s-2n|\le B\sqrt n)                         \tag{2}
\]
at every positive odd ternary unit. The published joint floor is stated with a possibly B-dependent constant. The following order of limits puts the dependence solely in the onset. No quantitative rate in B is asserted.

Use the **uncapped** selected families Γ_i of (70) and functions G_i from (74) of Weaver–Wren 48. The generation parameters, selected words and limiting nonnegative g_i do not depend on B. Wren 10, Proposition 4.5 and Lemma 4.6, supply for each fixed B a summable ε_i(B) bounding successive normalized increments in supremum norm, and fixed-i uniform convergence of G_i/π_n(s) to g_i in that window. The fixed initial block can be chosen once: its probability-loss product p_*>0, real bounds B_* and multiplier bounds are unconditional. In Proposition 4.5 the only change for a larger window is the constant coming from π_n(s)≥c_B/sqrt(n); its explicit bound at (4.2) and the following display retains the same sequence b_i and selected words. [Wren 10 v3, §4.2, Proposition 4.5 and Lemma 4.6](https://rstation.ai/problems/collatz/papers/10) · [Weaver–Wren 48 v2, equations (70)–(75)](https://rstation.ai/problems/collatz/papers/48)

At s=2n, pass to the fixed-i limit in the consecutive increment estimate. This gives ||g_{i+1}−lift(g_i)||∞≤ε_i(1). Choose **one** i₀ with tail sum at most p_*/8. The mean of g_{i₀} on unit residues is at least p_*, so choose one cylinder C above a residue with g_{i₀}≥p_*. At every later index j and every residue above this **same cylinder**, telescoping gives g_j≥7p_*/8. For each fixed B, now select J≥i₀ with sum_{i≥J} ε_i(B)≤p_*/8. The fixed-J base convergence costs ≤p_*/8 for n sufficiently large depending on B,J; telescoping to the final generation leaves ≥5p_*/8 throughout C. Thus taking a later starting generation to handle B never changes the cylinder's input precision.

The final free-tail estimate (78)–(79) in Weaver–Wren 48 works uncapped at one extra ternary digit K=1, with absolute unnormalized error O(b_j^{−2}). Since b_j is comparable to n and π_n(s)≥c_B/sqrt(n), after normalization this costs at most p_*/8 for n large depending on B. Its positive selected paths have real offsets ≤B_*+16^{b₀} by the deterministic bound after (79), **independent of B,J or the omitted letter cap**. Formula (72) applies directly to the uncapped family. No proof here needs a maximal single-letter cap. Finally spread to any unit beta residue by a single exponent e≤2·3^{Q_{i₀}}, fixed independently of B. A bounded first exponent carries β to 2^{−e}(1+3β), so one absolute F₀ works. Its probability factor 2^{−e} is bounded below absolutely, and π_{n−1}(s−e)/π_n(s)→1 uniformly over each fixed window and that finite range of e. Run the inner estimate on B+1 before mapping. Prescribe one more trit to ensure the actual terminal integer is a unit and peel the word through positive odd integers. Multiplying the atom probability by 2^s gives (2). [Weaver–Wren 48 v2, equations (78)–(83) and real cutoff](https://rstation.ai/problems/collatz/papers/48) · [Positive source and chronology dictionary](../ARITHMETIC_PROGRESSION_FLOOR.md)

## Composition and the uniform lower limit

Fix B≥2. Split n into b integers k_i equal up to one, where b is the nearest positive integer to t²/B². Along the sequences of (1), b→∞, k=min k_i→∞, and |Δ|sqrt(k_i)/n→B. Round s k_i/n to integer centers m_i summing to s. Then uniformly i, |m_i−2k_i|/sqrt(k_i)→B. Add d_i∈[−h,h] with h=floor(sqrt(k)/2) and sum d_i=0. These totals lie inside the fixed window (B+2)sqrt(k_i). The local limit theorem for the negative binomial with n successes and success probability 1/2 gives, for sufficiently large n depending on B,
\[
   \pi_{k_i}(m_i+d_i)\ge c_1 k_i^{-1/2}
                           \exp[-(B+2)^2/4],                         \tag{3}
\]
with c₁ absolute. Indeed sqrt(k)π_k(2k+v sqrt(k)) tends uniformly on every fixed compact interval to exp(−v²/4)/sqrt(4π); for each fixed B apply that convergence with an absolute error smaller than half the positive minimum on the relevant interval. Uniformity in B of this onset is unnecessary.

Compose the genuine unit rows from (2), using (3) and the count of zero-sum vectors in (2) of the linear-deviation note. Every block slope exceeds 2 for sufficiently large n, so the final real cutoff is F=2F₀. The sum of the block depths and totals is exactly n,s. At fixed B this proves
\[
 \inf_yR_F(y;n,s)\ \ge\ c_2\frac{A(n,s)}{\sqrt n}
          \left(c_3\exp[-(B+2)^2/4]\right)^b.                        \tag{4}
\]
Here c₂,c₃>0 are absolute, including the uniform cylinder constant c₀ in (2). Therefore the lower limit of the left side in (1) is at least (log c₃−(B+2)²/4)/B² for each fixed B. Let B→∞ to obtain −1/4.

For the upper bound, take one positive odd representative of each unit residue modulo 3^n. Each positive composition of s into n parts has one integral-target residue mod 3^n. At most one of the representatives therefore realizes this word. Discarding the unit-terminal and real restrictions for this upper count, the average number is at most (3/2)A(n,s)π_n(s). Along the stated moderate deviations, Stirling's formula at k=n and s=2n+Δ gives
\[
 \log(\sqrt n\,\pi_n(s))=-\Delta^2/(4n)
           +O(1+|\Delta|/n+|\Delta|^3/n^2).
\]
The error is o(t²), which proves the upper bound and (1). [Central-slice composition and zero-sum count](LINEAR_DEVIATION_ROWS.md)

## Consequence for actual slow terminating families

The same proof yields the sequential small-fixed-tilt pressure bound
\[
 \liminf_{d\to0,\ d\ne0}\ \frac1{d^2}
 \liminf_{n\to\infty}\frac1n\log\frac{\inf_y R_F(y;n,\lfloor(2+d)n\rfloor)}
                                          {A(n,\lfloor(2+d)n\rfloor)}
              \ \ge -1/4.                                           \tag{5}
\]
For clarity about the order of limits, fix B first and set b nearest to d²n/B². Then the smallest block size tends, as d→0 after n→∞, to infinity like (B/d)². For each fixed B the onset in (2) and the local limit bound (3) both hold for *all* sufficiently large block sizes. Rounding error in the standardized centers tends to zero in the outer limit. Taking n→∞, then d→0, then B→∞ in (4) gives (5). The same residue average also bounds the corresponding upper pressure by −d²/4+O(|d|³).

For an octave statement, fix any large terminating odd unit root y>4F, let d>0 be a sufficiently small fixed slope loss, and take s=floor((2−d)n). For a given large X we need n and s to put all bounded-real row sources in [X,2X). Varying n alone may leave a constant-factor gap because s is rounded. Instead choose n=floor(log(X/y)/(D−d log2)) and then choose s to be the least integer with A(n,s)y≥X. This gives X≤A(n,s)y<2X and s=(2−d)n+O(1). All sources are in [(1−F/y)X,2X); each x<X can be doubled once to reach [X,2X). The odd parts distinguish all starts, and the first-hit clocks only increase. The physical delay to log-height ratio tends to (2−d)/(D−d log2). Formula (5) is unchanged by the bounded rounding of s (its block estimates were uniform). Consequently, for h as defined in the spectrum note,
\[
  \boxed{\quad\limsup_{\delta\downarrow0}
       \frac{1-h(\mu+\delta)}{\delta^2}
       \le \frac{D}{4(\mu\log2-1)^2}.\quad}                         \tag{6}
\]
Indeed at each small δ choose the root-slope loss d that gives a strictly higher delay coefficient than μ+δ with d=δD/(μ log2−1)+o(δ). This imposes no sharp upper exponent on the slow population. Equation (1) is the two-sided minimax assertion for the inverse row; (6) is the one-sided original stopping-time conclusion. [Stopping-time spectrum](SLOW_TERMINATING_SPECTRUM.md)
