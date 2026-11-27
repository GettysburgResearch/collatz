# Squareclasses that force ordinary descent

**A6, kernel-checked local descent and actual hit.** Use the odd map `U(x)=(3x+1)/2^{a(x)}` with `a(x)=v₂(3x+1)` for odd positive `x`. A triple `x,y,z` of odd states is *dependent* if some nonempty subset has square product. This is equivalent to linear dependence of their rational multiplicative squareclasses: a rational square which is an integer is an integer square. The subset can contain one, two or three of the states.

**Theorem.** If every triple `x,U(x),U²(x)` starting at a growth step `a(x)=1` along a fixed ordinary trajectory is dependent, that trajectory hits 1. In particular, every trajectory whose odd-state squareclasses belong to a subspace of dimension at most two hits 1. The first statement permits a different relation and a different two-dimensional subspace at each growth.

Let `2y=3x+1`, `2^b z=3y+1`. Since `y` is odd, `x≡3 (mod 4)`, hence `x` has a prime `3 (mod 4)` to odd valuation. Since `y≡2 (mod 3)`, `y` is a nonsquare. Consecutive odd states are coprime, directly from each affine equation. The squareclasses `[x],[y]` are nonzero with disjoint prime support, hence are independent. Moreover

$$2^{b+1}z=9x+5,\qquad\gcd(x,z)\mid5.$$

If the three classes are dependent, `[z]` is one of `0,[x],[y],[xy]`. Coprimality with `y` excludes the two classes containing `[y]`. The prime `3 (mod 4)` found in `[x]` cannot be 5, and cannot divide `z`, excluding `[x]`. Thus `z` is an **ordinary square**. The converse is immediate. This is an exact local equivalence at every growth.

The transition `y→z` has `b≥2`, because exponent one would give `z≡2 (mod 3)`. An odd square is `1 (mod 8)`, so `a(z)=2`. For `x≥5` this yields

$$32\,U^3(x)\le27x+23<32x.$$

Every step with `a(x)≥2` decreases for `x>1`. A path satisfying the local hypothesis therefore descends in one or three odd transitions at every `x≥5`; the remaining odd values are `1` and `3`, with `3→5→1`. Strong induction applies to the actual shift of the same path. The Lean file defines `U` by ordinary factorization and proves the local statement and the eventual hit without parameters for an unspecified dynamical system. [SquareclassDescent.lean](SquareclassDescent.lean).

## A7. A ternary obstruction in an archimedean square grid

**PROPOSED written proof.** A first descent below a high ordinary odd source is forced if the first thirteen odd rows span a squareclass space of dimension at most seven. The argument gives an entirely elementary high-source result. The final, separate all-source corollary uses the published computational result that all positive integers below `2^71` converge.

Let `n_i=U^i(n)`, with `A_0=0`, `A_{i+1}=A_i+a(n_i)` and `A_i` the total binary clock. Suppose `n≥2^71` and `n_i≥n` for `0≤i≤12`. Telescoping gives

$$2^{A_i}\le(3+1/n)^i<3^i+1\quad(1\le i\le12).$$

The last strict inequality follows by the mean-value bound `i·4^{i-1}/n<1`. Hence `2^{A_i}≤3^i`. The normalized rows are

$$z_i=2^{A_i}n_i/3^i=n+t_i,\qquad t_i=\sum_{j<i}2^{A_j}/3^{j+1},\qquad 0\le t_i\le i/3\le4.$$

For `i≥1`, `v₃(t_i)=-i` because the last summand has unit numerator at that precision. The same holds for `z_i`; `n_i` is prime to 3 after one accelerated step. At index zero `v₃(z₀)≥0`.

Choose `2k` distinct rows with `k=1,2,3`. Put `h=max i`. Suppose their normalized product is a rational square with positive square root `Y`. Let `Q(X)` be the polynomial part of `√∏(X+t_i)` at positive infinity, defined by the binomial expansion. Its value at `X=n` has the equivalent homogeneous expression

$$Q(n)=[u^k]\prod_i(1+z_i u)^{1/2}.$$

Indeed translating the variable by `n` translates the polynomial part and leaves every negative Laurent power in the negative powers. With `w_i=3^h z_i`, the `w_i` are integers, precisely the last one a ternary unit. For the elementary symmetric sums `E_j` in `w_i`, the following table gives the integral grid numerator `D_k 3^{hk} Q(n)`. Its reduction modulo 3 is a nonzero multiple of `w_h^k`.

| `k` | `D_k` | Grid numerator |
|---:|---:|---|
| 1 | 2 | `E₁` |
| 2 | 8 | `4E₂−E₁²` |
| 3 | 16 | `8E₃−4E₁E₂+E₁³` |

On the other hand `3^{hk}Y=√∏w_i` is an integer divisible by 3. Thus `Y` and `Q(n)` differ by **at least** `1/(D_k 3^{hk})`. This local arithmetic supplies the strict grid separation that a real approximation alone would lack.

For the opposite bound shift expansion center to `X'=n+2`, so every `|t_i−2|≤2`. The coefficient of degree `j` of the centered binomial product has modulus at most `b_{k,j}2^j`, where `b_{k,j}=[u^j](∑_{m≥0}|binom(1/2,m)|u^m)^{2k}`. The absolute one-factor series sums to `2` at `u=1`, so `∑_j b_{k,j}=4^k`. Direct rational convolution gives `b_{1,2}=1/2`, `b_{2,3}=3/2`, `b_{3,4}=135/32`. The tail after degree `k` therefore obeys

$$|Y-Q(n)|\le\frac{2^{k+1}}{n+2}\left(b_{k,k+1}+\frac{2\,4^k}{n+2}\right)<\frac{80}{n}.$$

At `n≥2^71` this is smaller than `1/(16·3^{36})`, since `80·16·3^{36}<2^71`. This contradiction proves that no such set of `2,4,6` rows has square normalized product. The bound needs just the local no-descent assumption for these thirteen rows.

Apply this to the thirteen lifted vectors `([n_i], A_i mod 2, i mod 2, 1)`. If their physical component has rank at most seven, the kernel of their joint map from `F₂^{13}` has dimension at least three. Choose a three-dimensional subspace of the kernel. Over its seven nonzero vectors any nontrivial coordinate is one exactly four times. Total weight is at most `4·13=52`, so some nonzero word has weight at most seven. The final lifted coordinate makes the weight even, so it is `2,4` or `6`. Vanishing of the remaining lifted coordinates makes its normalized product a square. This contradicts the mixed-place bound.

Consequently `min_{1≤i≤12} n_i<n` when the thirteen-state physical rank is at most seven and `n≥2^71`. If **every** thirteen-state window on the trajectory satisfies that physical rank bound, one can iterate these actual strict decreases until a state below `2^71` occurs. With Barina's verified base this trajectory reaches 1. In particular, the same holds for any orbit of global squareclass rank at most seven. The high-source argument is mathematical; this packet has not rerun Barina's range computation. [D. Barina, improved verification limit](https://doi.org/10.1007/s11227-025-07337-0) · [Project verification milestones](https://pcbarina.fit.vutbr.cz/).

This coding argument scales with the number of checked rows, the protected relation weights, and the ternary and real bounds. In general the coefficient `binom(1/2,k)` must be a ternary unit for the one-unit separation argument as stated. No assertion at all ranks follows from the finite numerical threshold.
