# Iteration 14B: every divergent Collatz spine is logarithmically sparse

All theorem-level claims remain `PROPOSED` pending independent reconstruction.
This note isolates the architecture-free theorem underlying Iteration 14.

## T-9523: divergent-orbit spine sparsity

**Claim ID:** `T-9523`  
**Title:** The state set of every positive divergent Collatz orbit has logarithmic density zero  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Dependency:** Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), Theorem 1.3  
**Scope:** every positive ordinary orbit tending to infinity

Let `T` be the shortcut Collatz map and suppose

\[
x_k=T^k(x_0)\longrightarrow+\infty.
\tag{1}
\]

Put

\[
m_k=\min_{j\ge k}x_j.
\tag{2}
\]

Then `m_k -> infinity`.  Define

\[
f(N)={1\over2}\min\{m_k:x_k\ge N\}.
\tag{3}
\]

As in Iteration 14, `f(N)->infinity`.  The minimum of the unshortened Collatz
orbit beginning at `x_k` is exactly `m_k`, because the extra odd intermediate
value `3x+1` is larger than the following shortcut value.  Hence

\[
\operatorname{Col}_{\min}(x_k)=m_k>f(x_k).
\tag{4}
\]

Thus the orbit-state set

\[
\mathcal O=\{x_k:k\ge0\}
\tag{5}
\]

is contained in Tao's exceptional set

\[
\mathcal E_f=
\{N:\operatorname{Col}_{\min}(N)>f(N)\}.
\tag{6}
\]

Tao's theorem gives logarithmic density zero for `E_f`, and therefore

\[
\boxed{
\lim_{X\to\infty}
{1\over\log X}
\sum_{\substack{n\le X\\n\in\mathcal O}}{1\over n}=0.
}
\tag{7}
\]

No prescribed itinerary, parity-density assumption, or finite-state hypothesis
is used.

## Corollary: no divergent orbit has a linear upper envelope

The orbit states in (1) are distinct.  If for some constant `C` one had

\[
x_k\le C(k+1)
\qquad(k\ge0),
\tag{8}
\]

then, at `X_N=C(N+1)`,

\[
\sum_{\substack{n\le X_N\\n\in\mathcal O}}{1\over n}
\ge {1\over C}\sum_{k=0}^N{1\over k+1}
={1\over C}\log N+O(1),
\tag{9}
\]

contradicting (7).  Hence

\[
\boxed{
\sup_k{x_k\over k+1}=+\infty.
}
\tag{10}
\]

More precisely, for each fixed `C>0`, define

\[
J_C(N)=\{0\le k\le N:x_k\le C(k+1)\}.
\tag{11}
\]

Then (7) and the same harmonic comparison give

\[
\boxed{
\sum_{k\in J_C(N)}{1\over k+1}=o(\log N).
}
\tag{12}
\]

Thus `x_k/(k+1) -> infinity` in logarithmic time density.

## Relation to the coefficient surplus

For an all-time coefficient-supercritical orbit, with

\[
D_k=q_k-k\log_3 2\ge0,
\tag{13}
\]

the exact affine identity gives

\[
x_k\le3^{D_k}\left(x_0+{k\over2}\right).
\tag{14}
\]

If `D_k<=B`, then the right side is at most `C_B(k+1)`.  Equation (12)
therefore implies

\[
\sum_{\substack{k\le N\\D_k\le B}}{1\over k+1}=o(\log N),
\tag{15}
\]

which is `T-9522` from Iteration 14.

The conceptual bridge is:

\[
\boxed{
\text{Tao almost-boundedness}
\Longrightarrow
\text{logarithmic sparsity of one divergent spine}
\Longrightarrow
\text{surplus escape in logarithmic time density}.
}
\tag{16}
\]

## Scope boundary

Equation (7) is a genuine theorem about every hypothetical divergent orbit, but
it does not exclude a sufficiently sparse orbit.  A complete proof still needs
a mechanism forcing the orbit-state set, an inverse basin, or a bounded-surplus
subsequence to carry positive logarithmic density, or a different global
ordinary-extraction/descent theorem.