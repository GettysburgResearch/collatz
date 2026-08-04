# L-9310 — Completion-height rigidity for integral phase carries

**Claim ID:** L-9310  
**Title:** In every coprime expanding phase chain, long zero-carry runs force a height contradiction and total phase energy grows logarithmically  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** elementary modular lifting; the phase-chain convention of `L-9309` for the `64 -> 81` specialization  
**Scope:** general coprime `M -> N` phase chains and the all-depth Fourier cusp  
**Related counterexample candidates:** none

## 1. General expanding phase chain

Fix coprime integers

\[
2\le M<N,
\]

an integer `c != 0` satisfying

\[
\gcd(c,M)=1,
\]

an integer depth `K>=1`, and a nonzero integer numerator `h` satisfying the primitive condition

\[
M\nmid h.
\tag{1}
\]

For

\[
0\le \ell<K,
\]

let `s_ell` be the signed representative in

\[
\left(-\frac{N^{\ell+1}}2,
       \frac{N^{\ell+1}}2\right]
\]

of

\[
\boxed{
 s_\ell
 \equiv
 -c h M^{\ell-K}
 \pmod{N^{\ell+1}}.
}
\tag{2}
\]

Here `M^(ell-K)` means the inverse of `M^(K-ell)` modulo the displayed power of `N`.

Put

\[
x_\ell=\frac{s_\ell}{N^{\ell+1}}
\in\left[-\frac12,\frac12\right].
\tag{3}
\]

For

\[
0\le\ell<K-1,
\]

define the integral carry

\[
\boxed{
 a_\ell
 =
 \frac{M s_\ell-s_{\ell+1}}{N^{\ell+1}}
 =M x_\ell-Nx_{\ell+1}.
}
\tag{4}
\]

The first equality is integral because reduction of `(2)` at level `ell+1` gives

\[
s_{\ell+1}\equiv Ms_\ell\pmod{N^{\ell+1}}.
\]

Define

\[
\mathcal E_K(h)
=
\sum_{\ell=0}^{K-1}x_\ell^2,
\tag{5}
\]

and let

\[
W_K(h)
=
\#\{0\le\ell<K-1:a_\ell\ne0\}.
\tag{6}
\]

## 2. Carry energy inequality

One has

\[
\boxed{
W_K(h)
\le
\sum_{\ell=0}^{K-2}a_\ell^2
\le
2(M^2+N^2)\mathcal E_K(h).
}
\tag{7}
\]

In particular,

\[
\boxed{
\mathcal E_K(h)
\ge
\frac{W_K(h)}{2(M^2+N^2)}.
}
\tag{8}
\]

The first inequality uses only that every nonzero carry is a nonzero integer.

## 3. Zero-carry run rigidity

Suppose

\[
a_\ell=a_{\ell+1}=\cdots=a_{\ell+r-1}=0
\tag{9}
\]

for some `r>=1`, with `ell+r<K`. Put

\[
t=K-\ell-r\ge1.
\tag{10}
\]

Then

\[
s_{\ell+r}=M^r s_\ell.
\tag{11}
\]

At level `ell+r`, equation `(2)` therefore implies that the ordinary integer

\[
Z=M^{K-\ell}s_\ell+ch
\tag{12}
\]

is divisible by

\[
N^{\ell+r+1}.
\]

The primitive condition `(1)` makes `Z` nonzero: equality `Z=0` would imply

\[
M^{K-\ell}\mid ch,
\]

hence `M|h`, because `c` is a unit modulo `M`.

Consequently,

\[
N^{\ell+r+1}
\le |Z|
\le
\frac12 M^{r+t}N^{\ell+1}+|ch|,
\]

and division by `N^(ell+1)` gives the exact height squeeze

\[
\boxed{
N^r
\le
\frac12 M^{r+t}+|ch|.
}
\tag{13}
\]

Define the chart criticality constant

\[
\boxed{
\kappa_{M,N}
=
\frac{\log M}{\log(N/M)}
=
\frac1{\log_MN-1}>0,
}
\tag{14}
\]

and

\[
C_h=\log_N(2|ch|).
\tag{15}
\]

Then every zero-carry run satisfies

\[
\boxed{
r\le \kappa_{M,N}t+C_h.
}
\tag{16}
\]

Indeed, if `N^r<=2|ch|`, then `r<=C_h`. Otherwise `(13)` gives

\[
N^r<M^{r+t},
\]

which rearranges to `r<kappa_(M,N)t`.

## 4. Chaining all zero runs

Put

\[
A_{M,N}=1+\kappa_{M,N},
\qquad
B_h=1+\frac{C_h+1}{\kappa_{M,N}}.
\tag{17}
\]

The `K-1` carries split into `W=W_K(h)` nonzero carries and `W+1` zero runs, including the two terminal runs.

Read these zero runs from the right. If `t_i` is the terminal phase length following one run and `r_{i+1}` is the next run to its right, then

\[
t_i=t_{i+1}+r_{i+1}+1,
\tag{18}
\]

with the final value `t_W=1`. Equation `(16)` gives

\[
t_i
\le
A_{M,N}t_{i+1}+C_h+1.
\tag{19}
\]

Applying the same bound once more to the initial zero run yields

\[
\boxed{
K
\le
B_h A_{M,N}^{W+1}.
}
\tag{20}
\]

Therefore

\[
\boxed{
W_K(h)
\ge
\left(
\frac{\log(K/B_h)}{\log A_{M,N}}-1
\right)_+,
}
\tag{21}
\]

where `(u)_+=max(u,0)`.

Combining `(8)` and `(21)` proves the general logarithmic energy bound

\[
\boxed{
\mathcal E_K(h)
\ge
\frac1{2(M^2+N^2)}
\left(
\frac{\log(K/B_h)}{\log(1+\kappa_{M,N})}-1
\right)_+.
}
\tag{22}
\]

This is pointwise in both `K` and the primitive numerator `h`. No averaging, random model, finite-state truncation, or external Diophantine theorem is used.

## 5. The `64 -> 81` specialization

For the adelic-cusp chain,

\[
M=64,
\qquad
N=81,
\qquad
c=17.
\]

Thus

\[
\boxed{
\kappa
=
\frac{\log64}{\log(81/64)}
=
\frac1{\log_{64}81-1}
\approx17.6548475770851,
}
\tag{23}
\]

\[
A=1+\kappa
\approx18.6548475770851,
\tag{24}
\]

and

\[
C_*=2(64^2+81^2)=21314.
\tag{25}
\]

For every `h` with `64` not dividing `h`, put

\[
C_h=\log_{81}(34|h|),
\qquad
B_h=1+\frac{C_h+1}{\kappa}.
\tag{26}
\]

Then

\[
\boxed{
\mathcal E_K(h)
\ge
\frac1{21314}
\left(
\frac{\log(K/B_h)}{\log(1+\kappa)}-1
\right)_+.
}
\tag{27}
\]

The same criticality constant `kappa` appears independently in PR #20's ordinary-code repetition rigidity. Both arguments are manifestations of the same completion-height principle: a long repeated or zero-carry pattern gives extremely strong `2`-adic agreement, while its rational/archimedean height grows only like a power of `N`.

That cross-branch comparison is explanatory only; no PR #20 claim is a dependency of this proof.

## Dependency audit

- The general proof uses only coprimality, signed residue representatives, integer divisibility, and elementary real inequalities.
- `L-9309` supplies the exact reciprocal phase-chain convention for the specialization.
- `LIT-KTHM-0016` and the Mahler/FLP literature note supplied useful conceptual guidance about completion-versus-height decoupling, but no imported theorem is invoked.
- The finite-state tilted-transfer theorem `LIT-KTHM-0026` is not needed: integral carry quantization replaces a truncation-dependent spectral estimate.
- No issue-#4 average theorem or room-position theorem is used.

## Gap audit

- The primitive condition `M∤h` is essential to rule out `Z=0`. General numerators must first be divided by their exact `M`-power, as done in `T-9311`.
- The exponent in `(22)` is deliberately tiny. Positivity, not optimization, is the structural result.
- The lemma controls phase energy. A Fourier consequence additionally needs a mask inequality such as `L-9303`.
- The theorem does not construct or exclude an ordinary integer in the survivor attractor.
- All proof-looking claims remain `PROPOSED` pending independent reconstruction.

## Adversarial tests

1. If all carries vanished, `(20)` would bound `K` by a constant depending only logarithmically on `|h|`; a primitive fixed numerator cannot support an arbitrarily long exact zero-carry chain.
2. If a zero run reaches the terminal phase, then `t=1`, and `(16)` gives a uniform bound `r<=kappa+C_h`.
3. Multiplying `h` by a power of `M` violates primitiveness but merely shifts to a shallower copy; this is handled exactly in `T-9311`.
4. The zero-numerator possibility is excluded by `(1)`, rather than hidden inside an absolute-value inequality.
5. Direct exact modular checks over bounded `K,h` found no failure of carry integrality, `(13)`, `(20)`, or `(22)`; these checks are validation only and are not proof dependencies.

## Remaining uncertainty

The proof is complete-looking. The highest-value review targets are:

1. the modulus `N^(ell+r+1)` in `(12)`;
2. the nonzero argument using `M∤h`;
3. the right-to-left recurrence `(18)` and its endpoint convention;
4. the passage from integer carry count to phase energy in `(7)`.

## Suggested next attack

Combine `(27)` with the cosine-energy inequality and exact `64`-power self-similarity. This yields pointwise decay on every subexponential numerator window in `T-9311`, replacing the former harmonic-location conjecture by a deterministic carry theorem.