# Uniform Gaussian lower bounds for fixed-total inverse rows in a linear window

Let U(x) be the odd Collatz map, let S_n(x) be the sum of its first n true positive valuations, and put A(n,s)=2^s/3^n. There are absolute c,δ,K,F>0 and n₀ with the following property. For n≥n₀, |s−2n|≤δn, any positive odd ternary unit y, any odd modulus M≤exp(δn) and any residue u modulo M, at least
\[
   \boxed{\quad \frac{cA(n,s)}{M\sqrt n}
       \exp\!\left(-K\frac{(s-2n)^2}{n}\right)\quad}                \tag{1}
\]
distinct positive odd x simultaneously satisfy
\[
  U^n x=y,\quad S_n(x)=s,\quad x\equiv u\pmod M,\quad
           (y-F)A(n,s)\le x\le y A(n,s).
\]
For M=1 these x can all be ternary units. If 3 does not divide M one can similarly impose a unit trit by replacing M with 3M and slightly decreasing δ. When M already contains a factor three the prescribed residue determines the terminal trit. The constants in the M=1 theorem depend only on the published central bounded-real row. The all-odd-M extension imports the mixed-modulus central row from this pass. Neither statement imports a fine mixing theorem for a tilted geometric law. This gives genuine slow or fast physical words at a **prescribed** ordinary target and a specified total throughout a full linear window.

## Positive central blocks and their joint clocks

The input, for all large k and each integer |j−2k|≤sqrt(k), consists of ≥c₀A(k,j)/sqrt(k) distinct positive odd *unit* predecessors of every positive odd unit target z. Their real offsets β, defined by x=A(k,j)(z−β), lie in [0,F₀]. Root uniformity and the one extra trit for the terminal unit are part of the central bridge. The analogue prescribing an arbitrary residue mod M has the extra factor 1/M for log M≤c₁k, without the terminal-unit restriction. The pure ternary input is already enough up to and including (4) below. [Weaver–Wren 48 v2, Theorem 8 and bounded-real assembly](https://rstation.ai/problems/collatz/papers/48) · [Positive ordinary rows and mixed-modulus version, equations (4)–(5)](../ARITHMETIC_PROGRESSION_FLOOR.md)

First prove (1) for units with M=1. Write Δ=s−2n and choose b=ceil(128(1+Δ²/n)). Split n into b lengths k_i equal to floor(n/b) or ceil(n/b), of total n. By reducing δ and increasing n₀, k=min k_i is above any prescribed constant. Also |Δ| k_i/n≤sqrt(k)/4 since k_i≤2n/b and k≥n/(2b). For the real numbers s k_i/n choose integer centers m_i by rounding some up and the rest down so their sum is s; |m_i−s k_i/n|≤1. Set h=floor(sqrt(k)/4). Every j_i=m_i+d_i with −h≤d_i≤h is central for k_i, and every corresponding slope obeys A_i=A(k_i,j_i)≥exp(Dk_i/2)≥2, where D=log(4/3).

The number of b-tuples d_i∈[−h,h]∩ℤ with sum zero is at least
\[
                    c_2\frac{(2h+1)^b}{1+h\sqrt b}.                 \tag{2}
\]
Indeed convolution of symmetric unimodal integer sequences is symmetric unimodal: convolution with the interval indicator has discrete difference w(j+h+1)−w(j−h) at j≥0, which is nonpositive. Start at the point mass zero. Thus zero has maximal mass for the sum of b uniform variables on this interval. Their total variance is b h(h+1)/3. Chebyshev places at least three quarters of its mass within twice the standard deviation, an interval containing O(1+h sqrt(b)) integers. This proves (2), also for h=0.

For each zero-sum vector, apply the central unit row successively at actual ordinary targets. The number of concatenations is at least
\[
      A(n,s)\,c_0^b\prod_i k_i^{-1/2}.
\]
Distinct choices are disjoint, both within and between the zero-sum vectors: starting from the final ordinary x, the deterministic U path recovers every intermediate target, every individual valuation and each block total in reverse order. No nonperiodicity of y is needed because all comparisons use the same n and the same block boundaries. The total real offset is β₁+β₂/A₁+⋯+β_b/(A₁⋯A_{b−1})≤2F₀. Finally (2h+1)/sqrt(k_i)≥c₃, while 1+h sqrt(b)≤C sqrt(n). Consequently the number of true unit sources is at least
\[
          \frac{c_4 A(n,s)}{\sqrt n}\,c_5^{\,b}
       \ge \frac{c_6 A(n,s)}{\sqrt n}
                    \exp(-K_1\Delta^2/n).                           \tag{3}
\]
All constants are independent of n,s,y. The construction uses many actual compatible central slices; simply multiplying lower bounds for one slice at each checkpoint would incur a logarithmic loss in the exponent.

## Keeping a growing modulus in the same linear window

Split n=n₁+n₂ into nearly equal halves. For each of ≫sqrt(n) integers j₂ with |j₂−2n₂|≤sqrt(n₂)/2 choose j₁=s−j₂. With δ reduced again and n large, |j₁−2n₁| is in (3)'s linear window, and (j₁−2n₁)²/n₁≤C(1+Δ²/n). Apply (3) to the first n₁ inverse letters, ending at genuine units. From each such endpoint use the original mixed central row for the final n₂ inverse letters with prescribed residue u. The final ordinary x recovers its two block totals and their boundary target by following its path for n₂ odd steps. The families indexed by j₂ are therefore disjoint. Products of the two slopes equal A(n,s), and the √n available choices cancel one square-root denominator. The real offset stays ≤3F₀ since A(n₁,j₁)≥1 in this narrower window. Since log M≤c₁n₂ is allowed, this proves (1).

## Applications to the original source problems

For any fixed terminating odd unit y>3F, every row gives τ(x)=s+τ(y). Choose d>0 small and s near (2−d)n. All the row sources are comparable to exp((D−d log2)n) and their physical delay ratio tends to
\[
                     \frac{2-d}{D-d\log2}=\mu+c_* d+O(d^2),
        \qquad c_*=(\mu\log2-1)/D>0.                                 \tag{4}
\]
Equation (1) therefore gives a lower counting exponent 1−O(d²) among genuinely terminating slow starts, at exact odd depth and exact physical total. The separate spectrum note gives its every-octave form. At moderate deviations |s−2n|/sqrt(n)→∞, (1) records the explicit loss exp(−K(s−2n)²/n) and the unchanged real window and residue mask.

For the fixed ordinary grade Γ of a hypothetical escaping component, retain the notation γ and σ in the previous checkpoint. Apply (3) at y=H_v, depth n=v and s nearest (2+d)v for an arbitrary fixed |d|<δ. Along a subsequence attaining γ one obtains
\[
           \sigma\ge \frac{D+d\log2-Kd^2}{D+d\log2+\gamma}.          \tag{5}
\]
Taking d=0 recovers the established D/(D+γ). For every γ>0, sufficiently small positive d gives a strict improvement: the derivative at zero of the right side of (5) is γ log2/(D+γ)². With γ≤log(3/2) and d a sufficiently small constant times γ one has a uniform improvement of order γ². Neither (5) nor (1) reaches the potentially decisive original-source synchronous clock s≈(log₂3)n on a slowly growing escape. The proof requires the local center of each block to stay in a known central window and its size above the inherited onset. [Fractional grade classification](../phase3/FRACTIONAL_GRADE_CLASSIFICATION.md) · [Every-octave delay spectrum](SLOW_TERMINATING_SPECTRUM.md)
