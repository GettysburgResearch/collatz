# Full denominator bounds for binary clock corridors and arbitrary mechanical switches

**PROPOSED written results.** Let a primitive positive rational cycle have odd period `p`, positive odd phases `x_i`, binary gaps `e_i ∈ {1,2}`, and common reduced denominator `d`. Put `A=Σ e_i`, `θ=A/p`, `λ=log₂3`, `X=max x_i`, and let `W` be the range of `E_i−iθ`, where `E_i=Σ_{j<i} e_j`. The same reduced denominator occurs at every rotation: `D=2^A−3^p` is prime to six, and the odd rotated carries realize precisely the specified gaps. Two clocks which describe the same slope will be kept separate: `p` is the least odd period of the actual word and `q=p/gcd(A,p)` is the reduced denominator of its mean.

### 1. A terminal census for actual reduced numerators

Let `P_b` denote the number of different cyclic factors of length `b` in the gap word, counting each different factor once. For all `b≥1`, if `2·3^b≥dX`, then `p≤P_b`. Indeed the two terminal integer numerators of an identical factor differ by a multiple of `2·3^b`, since the two initial and terminal differences satisfy `2^E ΔN_end=3^b ΔN_start` and terminal numerators are odd. Distinct phases of a primitive orbit are distinct positive numbers, so their difference is strictly less than `dX`. This argument allows words longer than the period. It also works on an injective finite trajectory when only sites with a supplied preceding word are counted. This is the ternary terminal-packing mechanism from Paper 205 and the pinned PR206; all estimates below count the eligible factors under additional specified restrictions. [Paper 205](https://rstation.ai/problems/collatz/papers/205/v1) · [PR206](https://github.com/GettysburgResearch/collatz/blob/640bf7e511831a0ffc4f00462f12df81f8a8a619/research/clock-itineraries/ReturnOrbit.md)

An elementary second inequality is

\[
 X\le {2^W\over 2^\theta-3} \le {2^W\over 3(\log 2)(\theta-\lambda)}. \tag{1}
\]

In fact every rotated prefix sum differs from `jθ` by at most `W`. Bound every term of the numerator `Σ_{j<p}3^{p-1-j}2^{E_j}` by `2^W` times its value at the straight profile. The latter geometric sum divided by `D` is exactly `1/(2^θ−3)`. In particular `θ>λ`. All logs without a base in the estimates below are natural.

### 2. Binary gaps of width below two

Let `φ=(1+√5)/2`, `R=(1+√2)/φ²<1`, and

\[
 B_0={\log3\over\log\phi}=2.2830118\ldots,\qquad
 B_1={\log3\over\log\phi+(2\lambda-3)\log R}=2.3502775\ldots .
\]

Every primitive positive rational binary cycle with `W<2` satisfies

\[
 dX\gg [p/\log(2p)]^{B_0}. \tag{2}
\]

Whenever additionally `λ<θ<5/3`, this holds with the larger exponent `B_1`, with an absolute implicit constant. For `d=1`, (1) thus implies `0<θ−λ ≪ [log(2p)/p]^{B_1}` for growing periods. The general canonical-height-one inequality of Weaver's Paper 145 has limiting exponent `2.307351...` for integer phases and arbitrary positive gaps within that class. The sharper exponent here imposes the binary gap restriction and the estimate includes every reduced denominator. [Paper 145, (2), (6)](https://rstation.ai/problems/collatz/papers/145/v1)

For the count, put `s=max_i(E_i−iθ)`. There are bits `z_i∈{0,1}` with

\[
 E_i=\lfloor i\theta+s\rfloor-z_i,
\]

because `s−(E_i−iθ)∈[0,2)`. For any factor beginning at `j`, normalize its intercept to `t={jθ+s}∈[0,1)`. There are at most `b+1` mechanical increment words of length `b` as `t` varies. The floor values change only at `{−kθ}` for `1≤k≤b`; the right-continuous convention includes all breakpoint values even if several breakpoints coincide. Given the mechanical increments `m_i`, the gap is `e_i=m_i+z_i−z_{i+1}`. The allowed transition matrices in row–column convention, ordered by `z=0,1`, are

\[
 L=\begin{pmatrix}1&0\\1&1\end{pmatrix}\quad(m_i=1),\qquad
 U=\begin{pmatrix}1&1\\0&1\end{pmatrix}\quad(m_i=2).
\]

Both initial states and both final states may be counted, which only enlarges the language. The sum of all entries of their product is bounded by twice its Euclidean operator norm. The individual norms equal `φ`; this follows from the larger eigenvalue of `LᵀL` or `UᵀU`. Thus `P_b≤2(b+1)φ^b`.

For `3/2<θ<5/3`, the mechanical baseline has no consecutive ones and no three consecutive twos: every two-letter sum is at least three, and every three-letter sum is at most five. Write `n_1,n_2` for the two counts in a length-`b` factor. The number of disjoint `22` pairs is at least `n_2−n_1−1≥(2θ−3)b−3`, by bounding the number of two-runs by `n_1+1` and telescoping the floor. Each such pair has norm `‖U²‖=1+√2`, strictly below `φ²`. Group disjoint pairs and take norms. Consequently

\[
 P_b\le 2 R^{-3}(b+1)[\phi R^{2\lambda-3}]^b. \tag{3}
\]

Use the least `b≥1` with `2·3^b≥dX`. If `b` exceeds a sufficiently large fixed multiple of `log(2p)`, the desired lower bound for `dX` is immediate by minimality; otherwise `b+1=O(log(2p))`. The terminal census gives (2) and its sharpening. If (2) is applied with `d=1` along growing `p`, (1) makes `θ→λ`, so the stronger regime is automatic. This argument never treats arbitrary binary gap words as if every occurrence had the same intercept.

### 3. Arbitrarily many same-direction switches

Let a cyclic mechanical baseline of mean `θ` have entries in `{1,2}`. Independently at any subset of the baseline's occurrences of `12` replace `12` by `21`, or independently at occurrences of `21` replace `21` by `12`, using one direction for the entire word. All centers of either chosen orientation are disjoint. The density and arrangement of chosen switches are unrestricted. Both upper and lower mechanical baseline conventions are covered: at rational slope the upper rotation is a lower rotation with intercept shifted by a sufficiently small quantity at the finite set of distinct phases. For this whole class set

\[
 B_{\rm sw}={\lambda\over 2-\lambda}=3.8188416793\ldots .
\]

Every resulting primitive positive rational cycle obeys

\[
 dX\gg[p/\log(2p)]^{B_{\rm sw}}. \tag{4}
\]

To specify a length-`b` factor, select the length-`b+2` baseline factor including one gap at both boundaries. There are at most `b+3` choices. Every switch affecting the target touches a distinct unit gap in this enlarged factor. Its number of unit gaps is at most `(2−θ)(b+2)+1`. Hence `P_b≤8(b+3)2^{(2−λ)b}`, using `θ>λ`. This pays for switches crossing either boundary, and does not assume independence or periodicity of their selections. Terminal packing proves (4). A switch changes just one cumulative date by one; all changes have the same sign. The baseline has range strictly below one, so `W<2` follows even when the number of switches is proportional to `p` (an additive constant at the cyclic seam is immaterial).

Let `M` be any known upper bound for the irrationality exponent of `λ`. For every `η>0` there is a constant `c_η>0` such that `θ−λ≥c_η q^{−M−η}`; finitely many exceptional reduced fractions are absorbed into the constant. From (1) and (4),

\[
 d\gg_\eta (p/\log(2p))^{B_{\rm sw}} q^{-M-\eta}. \tag{5}
\]

In particular, **if `M<B_sw` then the class contains only finitely many primitive cycles of any fixed reduced denominator**, including `d=1`. This is finiteness, with no effective onset or assertion identifying the finite exceptions. For a prescribed growth law `X≤Cp²`, (4) already excludes `d=1` for all sufficiently large `p` without any irrationality input. For the dense two-prime construction in the companion paper, the stronger explicit `X≍a²` can be inserted directly, and (4) holds for every primitive choice of its masks, before any probabilistic argument.

**Source-qualified consequence.** Chudnovsky's October 2026 preprint states `μ(log a/log b)≤3` for multiplicatively independent positive rationals. The inputs `a=3,b=2` satisfy elementary unique factorization. On this quoted theorem, (5) gives `liminf log d/log p≥B_sw−3=0.8188416793...` without a clock-gcd restriction. The proof of the external theorem and its stated Lean chain have not been independently rebuilt here. [Chudnovsky, arXiv:2610.28079v1, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11)

Paper 22 v4 already treats arbitrary dispersed one-direction changes and bounds the Farey residual in terms of its mismatch count; a fixed number of swaps is excluded for large periods. PR200's MC1–MC2 already provide independent switched weights. Paper 223 v1 allows every subset of a particular list of native parity switches at one critical clock pair and proves an exact first descent there. The present counting argument allows arbitrary positive-density choices along growing accelerated clock pairs and estimates the whole denominator. In the growing-clock-gcd subfamily there is also a prior exact integer obstruction: Paper 114 Theorem 1 gives `gcd(A,p)=1` at canonical height at most two. A maximizing cut of any word with our real range `W<2` has canonical integer height at most one. At that height one can see the mechanism by multiplying the ordinary phase `x_i` by `2^(1−z_i)`: the map `F(k)=3k+lowbit(k)` is strictly increasing on integers with binary valuation at most one. At a common mechanical phase the block transfer preserves order, so cannot permute several distinct phases cyclically. This prior fact alone already distinguishes the two-prime control family's `gcd(A,p)=qr` at `d=1`. [Paper 22](https://rstation.ai/problems/collatz/papers/22/v4) · [Paper 114](https://rstation.ai/problems/collatz/papers/114/v1) · [PR200 MC1–MC2](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/arithmetic/COMPLETE_MODULAR_CARRY.md) · [Paper 223](https://rstation.ai/problems/collatz/papers/223/v1)

### 4. Stability under further arbitrary substitutions

Suppose a primitive binary word differs at at most `εp` positions from a word formed by these arbitrary one-direction switches in a binary mechanical baseline of slope `θ'`, with the same presentation length `p`. An upper bound `ε<1/2` on the altered fraction is fixed. The two means can differ by at most `ε`. If `θ'` is specified to be `θ`, the `+ε` in the next denominator can be omitted. With binary entropy `H₂`, any growing sequence of these cycles satisfies

\[
 \liminf {\log(dX)\over\log p}
 \ \ge B_\varepsilon:={\lambda\over 2-\lambda+\varepsilon+H_2(\varepsilon)} . \tag{6}
\]

For any fixed `ε<τ<1/2` at least `(1−ε/τ)p` cyclic starts have at most `τb` substitutions in their length-`b` windows, counting multiplicities even if `b>p`. This follows by summing substitution instances over all starts. Each such word belongs to a binary Hamming ball about an eligible reference factor, costing at most `2^{b H₂(τ)}`. Its reference factor count uses `2−θ'≤2−λ+ε` in the preceding proof. The terminal census injects this positive proportion whenever `2·3^b≥dX`. The logarithmic factors disappear on taking the lower limit and then `τ↓ε`. For `ε=0`, (4) gives the stronger finite statement.

For ordinary cycles with these substitutions, (1) and an irrationality bound `M` force

\[
 \liminf {W\over\log_2 p}\ \ge B_\varepsilon-M . \tag{7}
\]

For instance `ε=1/100` gives `B_ε>3.12`; `H₂(.01)<.081`, `1.5849<λ<1.5850` suffice. With the source-qualified `M=3` there are only finitely many primitive ordinary cycles within one percent of the broad switched language and with `W=o(log p)`. More precisely no growing sequence of such cycles can have that width law. If the distance to that language is `t=o(p)` along a sequence, (6) gives `B_sw` by letting the fixed `ε` decrease to zero. Centering a cyclic word after `t` substitutions changes any centered interval sum by at most `t`: each altered position has absolute coefficient at most one after subtracting the interval fraction of the full change. Therefore `W≤2+t`, and ordinary cycles require `liminf t/log₂p≥B_sw−M` whenever `t=o(p)`. The unbounded-width and high-error sectors remain open.
