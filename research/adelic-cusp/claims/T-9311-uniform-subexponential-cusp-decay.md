# T-9311 — Uniform pointwise decay on subexponential cusp windows

**Claim ID:** T-9311  
**Title:** Every subexponential numerator window has uniform pointwise Fourier decay at every depth  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9310`, `L-9303`, `T-9305`, and the exact `64`-power self-similarity in `L-9301`  
**Scope:** deterministic all-depth cusp decay for the original survivor coefficients  
**Related counterexample candidates:** none

## 1. Statement

For depth `K` and integer `h`, write

\[
F^{(2)}_K(h)
=
\frac{|S_K(h)|}{2^K},
\qquad
F^{(3)}_K(h)
=
\left|
\widehat\nu\!\left(\frac h{81^K}\right)
\right|.
\tag{1}
\]

Use the constants

\[
\kappa
=
\frac{\log64}{\log(81/64)},
\qquad
A=1+\kappa,
\qquad
C_*=21314,
\tag{2}
\]

and put

\[
\boxed{
b_*
=
\frac{2}{C_*\log A}
\approx3.2068228850\times10^{-5}.
}
\tag{3}
\]

For a nonzero integer `u` with `64` not dividing `u`, define

\[
C(u)=\log_{81}(34|u|),
\qquad
B(u)=1+\frac{C(u)+1}{\kappa}.
\tag{4}
\]

### Primitive numerator bound

If `64` does not divide `h`, then

\[
\boxed{
F^{(3)}_K(h)
\le
\exp\!\left[
-\frac2{C_*}
\left(
\frac{\log(K/B(h))}{\log A}-1
\right)_+
\right].
}
\tag{5}
\]

Moreover,

\[
\boxed{
F^{(2)}_K(h)
\le
\exp\!\left[
-\frac2{C_*}
\left(
\frac{\log(K/B(h))}{\log A}-1
\right)_+
\right]
+
\frac{\pi|h|}{64^K}.
}
\tag{6}
\]

Whenever

\[
K\ge A B(h),
\]

the first term in `(5)` can be written as

\[
\boxed{
F^{(3)}_K(h)
\le
e^{2/C_*}
\left(
\frac{B(h)}K
\right)^{b_*}.
}
\tag{7}
\]

### Arbitrary numerator bound

Let

\[
v=v_{64}(h)
=
\max\{j\ge0:64^j\mid h\},
\qquad
h_0=h/64^v,
\qquad
K_0=K-v.
\tag{8}
\]

For every

\[
0<|h|<64^K,
\]

one has

\[
\boxed{
F^{(2)}_K(h)
=
F^{(2)}_{K_0}(h_0)
\le
\exp\!\left[
-\frac2{C_*}
\left(
\frac{\log(K_0/B(h_0))}{\log A}-1
\right)_+
\right]
+
\frac{\pi|h_0|}{64^{K_0}}.
}
\tag{9}
\]

### Uniform subexponential-window theorem

Let `H_K` be any positive sequence satisfying

\[
\boxed{
\log(2+H_K)=o(K).
}
\tag{10}
\]

Then

\[
\boxed{
\max_{1\le |h|\le H_K}
F^{(2)}_K(h)
\longrightarrow0
}
\tag{11}
\]

as `K -> infinity`.

In particular, for every fixed `R>0`, there are constants `C_R` and `K_R` such that

\[
\boxed{
\max_{1\le |h|\le K^R}
F^{(2)}_K(h)
\le
C_R
\left(
\frac{\log K}{K}
\right)^{b_*}
}
\tag{12}
\]

for every `K>=K_R`.

This is stronger than the polynomial-window maximal condition formerly requested in `C-9301`.

## 2. Proof of the primitive numerator bound

For the signed reciprocal phases from `L-9310`, let

\[
\mathcal E_K(h)
=
\sum_{\ell=0}^{K-1}
\left\|
\frac{q_\ell(h)}{81^{\ell+1}}
\right\|^2.
\tag{13}
\]

When `64` does not divide `h`, equation `L-9310(27)` gives

\[
\mathcal E_K(h)
\ge
\frac1{C_*}
\left(
\frac{\log(K/B(h))}{\log A}-1
\right)_+.
\tag{14}
\]

The triadic mirror coefficient is the complete reciprocal cosine product. The elementary mask inequality from `L-9303`,

\[
|\cos(\pi x)|
\le
\exp(-2\|x\|^2),
\tag{15}
\]

therefore gives

\[
F^{(3)}_K(h)
\le
\exp(-2\mathcal E_K(h)).
\tag{16}
\]

Substitution of `(14)` proves `(5)`.

The split-collapse comparison `T-9305` gives

\[
\left|
F^{(2)}_K(h)-F^{(3)}_K(h)
\right|
\le
\frac{\pi|h|}{64^K}
\left(1-(64/81)^K\right)
<
\frac{\pi|h|}{64^K}.
\tag{17}
\]

Combining `(5)` and `(17)` proves `(6)`.

If `K>=AB(h)`, the positive part in `(5)` is active and

\[
\begin{aligned}
F^{(3)}_K(h)
&\le
\exp\!\left(
\frac2{C_*}
-
\frac{2\log(K/B(h))}{C_*\log A}
\right)\\
&=
e^{2/C_*}
\left(
\frac{B(h)}K
\right)^{b_*},
\end{aligned}
\]

which is `(7)`.

## 3. Remove exact powers of 64

By the moving-character identity `L-9301`,

\[
F^{(2)}_K(64^v h_0)
=
F^{(2)}_{K-v}(h_0)
\tag{18}
\]

for every `0<=v<K`.

If `0<|h|<64^K`, the exponent `v=v_64(h)` satisfies `v<K`, and `h_0` is primitive. Apply `(6)` at depth `K_0=K-v` to obtain `(9)`.

This step is exact. Frequencies carrying large powers of `64` are not exceptional; they are shallower copies of the same primitive problem.

## 4. Uniformity on subexponential windows

Assume `(10)` and let `1<=|h|<=H_K`. From `(8)`,

\[
v
\le
\log_{64}H_K
=o(K),
\]

so

\[
K_0=K-v=(1-o(1))K.
\tag{19}
\]

Also

\[
B(h_0)
\le
1+
\frac{1+\log_{81}(34H_K)}{\kappa}
=
o(K).
\tag{20}
\]

Consequently,

\[
\frac{K_0}{B(h_0)}
\longrightarrow\infty
\]

uniformly over the whole window. The first term in `(9)` therefore tends to zero uniformly.

For the second term,

\[
\frac{|h_0|}{64^{K_0}}
\le
\frac{H_K}{64^{K-o(K)}}
\longrightarrow0
\tag{21}
\]

because `log H_K=o(K)`. This proves `(11)`.

For `H_K=K^R`, equations `(19)` and `(20)` give

\[
K_0\ge K-O_R(\log K),
\qquad
B(h_0)=O_R(\log K).
\]

Equation `(7)`, with the exponentially small comparison term absorbed into the constant, proves `(12)`.

## 5. Conceptual interpretation

The earlier approach treated low-energy frequencies as a sparse exceptional language and sought information about the real location of its residue classes. `L-9310` reveals a stronger deterministic obstruction.

A large coefficient requires small total phase energy. Small energy allows only few nonzero **integral** carries. Few nonzero carries create long zero-carry runs. Every such run is simultaneously:

1. an exact multiplicative relation in the completion;
2. a rational approximation of controlled archimedean height;
3. impossible beyond the completion-height threshold.

The contradiction iterates from the terminal end. This converts carry quantization directly into logarithmic energy, with no probabilistic interchange and no finite-level tower closure.

The literature review's rational-base and Mahler/FLP notes suggested the relevant completion-versus-height decoupling. The finite-state tilted-transfer theorem suggested a pressure formulation, but the integral carry gap is stronger here: it supplies a state-independent positive cost whenever the carry is nonzero.

## Dependency audit

- `L-9310` is the only new arithmetic input.
- `L-9303` supplies the deterministic cosine-energy inequality.
- `T-9305` transfers from the exact triadic phase chain to the original survivor coefficient.
- `L-9301` removes exact powers of `64` without loss.
- No frequency average, depth average, external Fourier-decay theorem, solver, or computation is used.
- No PR #20 theorem is a dependency, although the identical criticality constant provides an independent conceptual cross-check.

## Gap audit

- The exponent `b_*` is extremely small. This does not affect convergence.
- Equation `(11)` is pointwise only on subexponential windows; full exponential windows still require the harmonic tail theorem `T-9308`.
- The theorem concerns finite-depth Fourier coefficients and does not settle the ordinary-integer intersection `Q-9301`.
- Every proof-looking claim remains `PROPOSED` pending independent reconstruction.

## Adversarial tests

1. `h=0` is excluded; its Fourier coefficient is exactly `1`.
2. Frequencies divisible by `64^v` are reduced before the primitive height argument.
3. If `h` grows polynomially, the height penalty is only `O(log K)`, while the available phase length is `K`.
4. If `h` grows like `exp(o(K))`, the same separation remains asymptotically unbounded.
5. The bound is compatible with nonmonotone individual coefficients: it constrains their envelope, not each adjacent-depth ratio.

## Remaining uncertainty

The proof is complete-looking. Independent review should reconstruct, in order:

1. `L-9310`'s zero-run modulus and terminal chaining;
2. the exact mirror product used in `(16)`;
3. the survivor/mirror comparison in `(17)`;
4. the uniform handling of `v_64(h)` in `(19)`.

## Suggested next attack

Use the polynomial window `(12)` below a growing cutoff and `T-9308` above it. Their harmonic weights are complementary and close the complete weighted EQ criterion at every depth in `T-9312`.