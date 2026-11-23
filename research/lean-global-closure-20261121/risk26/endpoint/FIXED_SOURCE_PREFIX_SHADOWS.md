# Fixed-source prefix shadows: exact cancellation and local products

23 November 2026. **Finite core Lean verified; asymptotic deductions written
and source-qualified. Collatz remains OPEN.** This note keeps one original
positive ordinary source through every prefix. No stationary reference law,
changing finite CRT source, or compact carry quotient occurs.

## 1. Source, complete carries, and dependencies

Let `p=q_0` be a positive odd integer, and let

\[
 q_{n+1}=U(q_n)=\frac{3q_n+1}{2^{a_n}},\qquad
 a_n=v_2(3q_n+1)\ge1,
 \qquad A_N=\sum_{j<N}a_j.
\]

Take a ternary-unit source if needed, by moving to the first successor.
Every successor is a ternary unit. Define the **complete integer carry**

\[
 C_0=0,\qquad C_{N+1}=3C_N+2^{A_N},\qquad
 D_N=2^{A_N}-3^N.
\]

Multiplying the actual edge identities gives

\[
 2^{A_N}q_N=3^Np+C_N.                              \tag{F1}
\]

For `N>=1`, both `C_N` and `D_N` are odd and prime to `3`; in particular
`D_N` is nonzero. Put

\[
 g_N=\gcd(C_N,D_N)>0,\qquad
 z_N=\frac{C_N/g_N}{D_N/g_N}=\frac{C_N}{D_N}.
\]

The rational height convention is
`H(z_N)=max(|C_N|,|D_N|)/g_N`, with reduced denominator
`b_N=|D_N|/g_N`. All logarithms below are natural.

The finite assertions (F1)–(F3) use only the displayed integer equations.
The escaping-source consequences use the finite reciprocal correction

\[
 \sum_{n\ge0}q_n^{-1}<\infty.                       \tag{FC}
\]

Within the current source family, (FC) follows from the uniform injective
orbit count in PR182, frozen at
`a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
`research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, §§1–6.
The application to one escaping ray and the resulting identities are
reconstructed in the companion root note
`../root/UNCONDITIONAL_CYCLE_BOUNDARY.md`, (UB8)–(UB11).
For the proof below, (FC) is an explicit sufficient hypothesis; it is not
silently supplied by iid genericity.

The critical conclusions additionally use

\[
 A_N\log2=N\log3+o(N).                              \tag{CR}
\]

If (CR) has only been proved along selected horizons, every assertion
below involving `o(N)` is restricted to those same horizons. An empirical
weak limit alone does not imply an all-horizon rate or a maximum-height
estimate.

## 2. Exact cancellation is bounded by the actual displacement

For every prefix, including nonescaping ones,

\[
 \boxed{g_N=\gcd(q_N-p,D_N).}                        \tag{F2}
\]

Indeed (F1) gives

\[
 C_N=D_Np+2^{A_N}(q_N-p),
\]

and `gcd(2^{A_N},D_N)=1`. Adding a multiple of `D_N`, then removing the
coprime factor, proves (F2). Consequently

\[
 g_N\mid(q_N-p),\qquad
 q_N\ne p\ \Longrightarrow\ 1\le g_N\le|q_N-p|.   \tag{F3}
\]

This is a positive fixed-source restriction: cancellation of the full
periodic denominator is charged to the displacement of the actual
endpoint from the same original integer `p`. If `q_N=p`, (F3)'s size
bound is unavailable; the distinctness premise is necessary.

The file `FixedSourcePrefixGcd.lean` proves (F2), divisibility, and (F3)
for arbitrary integer affine data with coprime multipliers. It then
specializes to `2^A` and `3^N`, and derives (F1) from **all original edge
identities** by induction. The final theorem therefore does not assume
an independent prefix-carry equation. Its scope is finite arithmetic;
it neither assumes nor proves an escaping orbit.

## 3. Escaping rays have a finite positive normalization

Suppose the fixed orbit escapes and (FC) holds. Set

\[
 E_N=\frac{2^{A_N}q_N}{3^N}=p+\frac{C_N}{3^N}.
\]

The edge identities give, at every horizon,

\[
 E_{N+1}-E_N=\frac{2^{A_N}}{3^{N+1}},\qquad
 E_N=p\prod_{j<N}\left(1+\frac1{3q_j}\right).
                                                               \tag{F4}
\]

Thus `E_N` increases to a finite number `E_infinity>p`. Since an escaping
orbit has `q_N -> infinity`,

\[
 \frac{2^{A_N}}{3^N}=\frac{E_N}{q_N}\longrightarrow0,
 \qquad
 \frac{D_N}{3^N}\longrightarrow-1,
 \qquad
 \frac{C_N}{3^N}\longrightarrow E_\infty-p>0.       \tag{F5}
\]

In particular the actual periodic shadows have the real limit

\[
 \boxed{z_N\longrightarrow p-E_\infty<0
        \quad\text{in }\mathbb R.}                \tag{F6}
\]

Their binary behavior retains the original positive integer:

\[
 z_N-p=\frac{2^{A_N}(q_N-p)}{D_N},\qquad
 |z_N-p|_2=2^{-A_N}|q_N-p|_2\longrightarrow0.       \tag{F7}
\]

Here `D_N` is odd and `A_N>=N`. The negative real limit and the positive
binary limit live in different completions and do not imply a
contradiction.

## 4. The critical branch fixes the height and binary exponents

Assume in addition (CR). The exact normalization gives

\[
 \log q_N=N\log3-A_N\log2+\log E_N=o(N).           \tag{F8}
\]

Since the ray is nonperiodic, (F3) yields `log g_N=o(N)`. Combining this
with (F5) proves

\[
 \boxed{\log b_N=N\log3+o(N),\qquad
        \log H(z_N)=N\log3+o(N).}                 \tag{F9}
\]

No lower bound for a linear form in `log2` and `log3` is needed. The
finite correction and actual escape already force
`|2^{A_N}-3^N|/3^N -> 1`, while the exact gcd identity bounds the only
remaining cancellation.

There is also an exact approximation exponent. Because `q_N-p` is a
nonzero integer,

\[
 0\le v_2(q_N-p)\log2\le\log|q_N-p|=o(N).
\]

Using (F7) and (CR),

\[
 \boxed{\frac{-\log|z_N-p|_2}{\log H(z_N)}
        \longrightarrow1.}                       \tag{F10}
\]

Thus these actual consecutive-prefix shadows do not furnish a binary
approximation exponent strictly above one. This is an exact conclusion
about the specified approximants, not a theorem excluding different
Diophantine constructions.

The rate `log q_N=o(N)` is insufficient to conflict with the sharp
polynomial repetition demand established in
`REPETITION_ENTROPY_BOUNDARY.md`. That demand grows with exponent
`1/log_2(log_2 3)=1.5050070664...` for almost every critical iid sample.
An unspecified subexponential height envelope can exceed every
polynomial. Moreover, iid genericity of an actual selected ray does
not itself make it typical for the growing-window almost-sure theorem.

## 5. Exact all-prefix products for the same positive source

This section examines two particular collections of local linear
forms; it does not assert a no-go for other choices or higher-dimensional
encodings. For `N>=1`, take the primitive integer vector

\[
 x_N=(X_N,Y_N)=(3^N,C_N),
\]

which is primitive because `C_N` is prime to `3`. Normalize
`|r|_ell=ell^{-v_ell(r)}` for `ell=2,3`.

### 5.1 Rational source forms

Use the two forms `X,pX+Y` at the real and binary places, and `X,Y`
at the ternary place. The determinants are `1` in absolute value,
and the same positive integer `p` is used at every horizon. Since
`p3^N+C_N=2^{A_N}q_N`, with `q_N` odd,

\[
 \begin{aligned}
 &|X_N(pX_N+Y_N)|_\infty
  |X_N(pX_N+Y_N)|_2 |X_NY_N|_3\\
 &\hspace{30mm}=\bigl(3^N2^{A_N}q_N\bigr)
                  2^{-A_N}3^{-N}
  =\boxed{q_N\ge1}.                               \tag{F11}
 \end{aligned}
\]

All consecutive prefix equations have been retained. Their local
smallness exactly cancels the natural real size, leaving the actual
positive endpoint, not a negative power of the vector height.

### 5.2 Even the real boundary coefficient leaves a positive tail

Suppose escape and (FC), and put `alpha=E_infinity-p>0`.
At the real place replace the second form by `alpha X-Y`; leave the
binary forms `X,pX+Y` and ternary forms `X,Y` unchanged. If `alpha`
is not algebraic, the usual algebraic-coefficient Subspace Theorem is
already inapplicable. Even if its algebraicity were supplied, the exact
product is

\[
 \begin{aligned}
 \mathcal P_N
 &= |X_N(\alpha X_N-Y_N)|_\infty
    |X_N(pX_N+Y_N)|_2 |X_NY_N|_3\\
 &=\frac{3^N}{2^{A_N}}(E_\infty-E_N)\\
 &=\sum_{j\ge0}\frac{2^{A_{N+j}-A_N}}{3^{j+1}}
  =q_N\left(\frac{E_\infty}{E_N}-1\right)
  \ge\boxed{\frac13}.                            \tag{F12}
 \end{aligned}
\]

The inequality comes from the **first future correction**, so it is
independent of how slowly the ray escapes. It rules out the required
fixed negative power saving for these forms even when the real limit
is admitted as a coefficient.

One can subtract the first `K` future corrections before evaluating the
real expression. The resulting unrenormalized scalar tail is exactly

\[
 \mathcal T_{N,K}
  :=\frac{3^N}{2^{A_N}}(E_\infty-E_{N+K})
   =\sum_{j\ge K}\frac{2^{A_{N+j}-A_N}}{3^{j+1}}
   \ge\frac{2^K}{3^{K+1}},                        \tag{F13}
\]

because all actual gaps are at least one. If `K_N=o(N)`, then
`-log mathcal T_{N,K_N} <= log3+K_N log(3/2)=o(N)`.
Under (F9), this cannot be `H(z_N)^{-epsilon}` for any fixed
`epsilon>0` at all sufficiently large selected horizons. When performing
such subtraction through changed forms, their moving coefficients,
denominator clearing, and height cost must also be accounted for.
(F13) is an exact scalar tail bound, not a claim that those costs or
arbitrary alternative forms have been controlled.

## 6. Scope and first missing step

The useful positive-source gain is (F2)–(F10): the complete carry gcd is
exactly an endpoint-displacement gcd, and under the critical clock the
actual reduced shadows retain height exponent `log3` and binary
approximation exponent one. The forms (F11)–(F13) then identify a
specific obstruction to improving the source-anchored Subspace argument
by using all consecutive prefixes and their real limit.

Neither result bounds the actual repeated-word collision energy, supplies
an entropy-to-Renyi transfer for the same endpoint law, or excludes an
ordinary escaping ray. A further source-dependent mechanism would have
to extract strict arithmetic saving beyond these positive correction
tails, or prove a quantitative orbit-height constraint strong enough to
conflict with forced recurrence while retaining the same source.

## Verification boundary

`FixedSourcePrefixGcd.lean` was checked with Lean `4.34.1`, `import Std`
only, and `-DwarningAsError=true`. The command exited `0`; all printed
axiom dependencies are subsets of `{propext, Quot.sound}`. There is no
`sorry`, `axiom`, private mathematical placeholder, or imported closure
claim. The finite recurrence, exact gcd and displacement statements are
formalized. The limiting arguments, normalized absolute-value products,
and literature applicability discussion are written proofs, not claimed
Lean theorems.
