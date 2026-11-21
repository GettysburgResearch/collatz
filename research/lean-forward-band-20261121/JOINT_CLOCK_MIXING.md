# Keeping the complete clock in Syracuse mixing

## Status and target

This continuation attacks the missing distributional step directly. It derives
a joint fine-scale estimate for the Syracuse offset and the **whole sum of
the exponents**, then uses it to prove a fixed-total version of the selected
atom floor. These are written analytic results, with an independent review
in `GLOBAL_RENEWAL_ATTACK.md`. They have not been formalized in Lean.
They do not prove universal Collatz convergence.

The non-elementary input is the nonnegative renewal estimate in Terence Tao,
*Almost all orbits of the Collatz map attain almost bounded values*,
[DOI 10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8),
**Proposition 7.3, equation (7.10)**. The proof below also uses the precise
prefix separation argument in that paper's Section 6, especially Corollary
6.3. This is a new derivation from the stronger intermediate estimate, not
an assertion that the marginal statement of Proposition 1.14 alone controls
conditional totals. No neighboring joint-mixing claim in an external
unreviewed manuscript is imported. No priority claim is made.

The selected-prefix construction, its attribution, and its real-offset
and operator bounds are those in PR180 at
`f87cb69b3dd86257731ddfbab58c87bf3b5f63d6`,
`research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md`.
Only the new clock-sensitive argument is developed here.

## 1. Exact objects and the two conclusions

Let the independent positive integers `a_i` have probabilities `2^(-a_i)`.
Write

\[
 A_n=\sum_{i=1}^n a_i,\qquad
 X_n=\sum_{i=1}^n3^{i-1}2^{-A_i}\pmod {3^n},
 \qquad J_n(u,r)=3^n\Pr(A_n=u,X_n=r).
\]

Clock functions are extended by zero to all integers. Let `p_t` be the
probability mass function of the sum of `t` independent geometric letters,
with `p_0` the mass at zero. Convolution `*` below acts **only on the clock**.
The spatial norm is full Haar average on `G_n=Z/(3^n Z)`; thus

\[
 \|H\|_{1,1}=3^{-n}\sum_{r\in G_n}\sum_{u\in\mathbb Z}|H(u,r)|.
\]

The first result is, for every fixed `K>0`,

\[
 \boxed{\|J_n-\operatorname{lift}(J_m*p_{n-m})\|_{1,1}
       \le C_Km^{-K}\quad(1\le m\le n).}                 \tag{JF}
\]

The coarse law retains the entire final clock. In particular it is **not**
`J_m` with the final clock silently replaced by `A_m`, and is not the product
of the two marginals.

The second result is a controlled fixed-total floor. There are constants
`B,c>0` and `s_0` such that, for every `s>=s_0`, every unit residue `r mod 3^s`,
and every integer `u` with `|u-2s|<=sqrt(s)`, a finite family of length-`s`
words satisfies

\[
 A(w)=u,\quad 0\le\beta_w\le B,\quad
 \beta_w\equiv r\pmod {3^s},\qquad
 \boxed{\sum_w3^s2^{-u}\ge c/\sqrt{s}.}                  \tag{CFJ}
\]

Here `beta_w=sum_i 3^(i-1)2^(-A_i)`, as in the parent packet. Finiteness
follows already from positive letters and the fixed total. The constants
are independent of the level, total in this window, and unit residue.
The accompanying review derives **positive lower natural predecessor
density** from (CFJ), an improvement over the preceding logarithmic result.

## 2. The Fourier estimate survives every bounded clock test

For a primitive character `chi` modulo `3^h`, set

\[
 z_h(u)=\mathbb E[1_{A_h=u}\chi(X_h)].
\]

We claim

\[
 \boxed{\sum_u|z_h(u)|\le C_Kh^{-K}.}                   \tag{TF}
\]

To verify the claimed strengthening, let `phi` be any complex function
with modulus at most one. Condition on the pair sums
`b_j=a_(2j-1)+a_(2j)`; if `h` is odd, condition on the last unpaired letter
as well. The total `A_h` is then fixed. The conditional expectation of
`chi(X_h)` factors into exactly the pair factors used in Tao's equations
(7.4)--(7.5), and, when appropriate, a final factor of modulus one.
Multiplication by `phi(A_h)` cannot increase its modulus.

The bound for the expectation of the product of the moduli is supplied by
Tao's Lemma 7.2 and Proposition 7.3. Their nonnegative envelope is unchanged
by the clock test. Consequently

\[
 |\mathbb E[\phi(A_h)\chi(X_h)]|\le C_Kh^{-K}.
\]

Taking `phi(u)=conj(z_h(u))/|z_h(u)|` when `z_h(u)!=0`, and zero otherwise,
proves (TF). This choice is legitimate for the absolutely summable
sequence: `sum_u|z_h(u)|<=sum_u Pr(A_h=u)=1` before the sharper estimate.

If the word has length `t>=h` but the character has conductor `3^h`, only
its first `h` letters affect the offset. The additional `t-h` letters add
an independent clock. The sliced Fourier sequence is therefore convolved
with `p_(t-h)`, which contracts its `ell^1` norm. Thus (TF) holds with
`h` on the right for this case as well.

This step preserves correlations with the total; it does not replace a
conditioned word by an independent geometric word.

## 3. Joint fine-scale mixing

First suppose `0.9n<=m<=n`; finitely many small `n` can be absorbed into
the constant. Use the prefix splitting from Tao's Section 6. For any desired
error exponent, exclude an event of probability smaller than a prescribed
negative power of `n`, on which a subinterval sum deviates too far from
twice its length. Stop the prefix at length `k+1`, with

\[
 k=\frac{\log3}{2\log2}n+O(\sqrt{n\log n}),\qquad
 \ell=A_{k+1}=\frac{\log3}{\log2}n-O(\log n).
\]

As in the source proof, enlarge the prefix-good event so that it only
depends on the prefix, at a further negligible probability cost. Partition
by `k` and `ell`. There are at most polynomially many pieces; constants in
the displayed `O` terms may depend on the requested error power.

For one such piece let `nu` be its prefix-offset subprobability on `G_n`.
The source's separation lemma says that at most one allowed prefix with
this fixed total has any prescribed residue. Each such prefix has
probability `2^(-ell)`. In unnormalized Fourier convention this gives

\[
 \sum_{\xi\in G_n}|\widehat\nu(\xi)|^2
 =3^n\sum_y\nu(y)^2\le3^n2^{-\ell}=n^{O(1)}.       \tag{3.1}
\]

Let `t=n-k-1`. The suffix, independent of the entire conditioned prefix,
has joint slices `mu_v(z)=Pr(A_t=v,X_t=z)`. The complete offset is prefix
offset plus `3^(k+1)2^(-ell)` times suffix offset, and the complete clock is
`ell+v`. Thus the Fourier transform of clock slice `ell+v` is

\[
 \widehat\nu(\xi)\widehat\mu_v(3^{k+1}2^{-\ell}\xi).
\]

Subtract spatial averaging on cosets modulo `3^m`. Only frequencies of
valuation less than `n-m` remain. On the suffix these have conductor
`3^h` with

\[
 h\ge m-k-1\ge c_1n
\]

for some absolute positive `c_1`, once `n` is sufficiently large. Formula
(TF), including its longer-word extension, now gives

\[
 \sum_v|\widehat\mu_v(3^{k+1}2^{-\ell}\xi)|^2
 \le\left(\sum_v|\widehat\mu_v(3^{k+1}2^{-\ell}\xi)|\right)^2
 \le C_Ln^{-2L}.                                      \tag{3.2}
\]

Truncate the complete clock at `6n`. The discarded probability is
exponentially small by the geometric moment generating function. Clock
truncation commutes with spatial averaging. Cauchy--Schwarz on at most
`6n` clock values and `3^n` spatial values, then Plancherel, bounds the
square of the joint `ell^1` error of this piece by

\[
 6n\sum_\xi |\widehat\nu(\xi)|^2
               \sum_v|\widehat\mu_v(3^{k+1}2^{-\ell}\xi)|^2
 \le C_L n^{1+O(1)-2L}.                              \tag{3.3}
\]

Choosing `L` sufficiently large absorbs this polynomial loss, the prefix
partition, and all excluded events. This proves the asserted joint error
between the full law and its spatial projection in the local regime.

The projected law is exactly `J_m*p_(n-m)`: later letters vanish from the
offset modulo `3^m` and add an independent clock to `A_m`. This proves
(JF) when `m>=0.9n`.

For arbitrary `m<=n`, insert a geometrically spaced chain of intermediate
resolutions, with adjacent ratios at least `0.9`. Lift each local error
to `G_n` and convolve it with the clock law for the as-yet missing letters.
Lifting preserves the normalized norm and convolution contracts it. The
errors sum to `O_K(m^(-K))`. This proves (JF) in the stated normalization.

## 4. A clock version of the weighted counting operator

For a fixed prefix word `w` of length `d`, total `A(w)`, multiplier
`omega_w=3^d2^(-A(w))`, and affine map
`Phi_w(z)=omega_w*z+beta_w`, define

\[
 (\mathcal T_wH)(u,\Phi_w(z))
       =\omega_w H(u-A(w),z),
\]

and set it to zero off the word's spatial cylinder. Suppose a finite
prefix family has `beta_w<=B_*`, `omega_w<=Omega`, and `L` different totals.
The same fixed-total injectivity argument as the parent weighted-counting
lemma gives

\[
 \boxed{\sup_r\sum_u|\sum_w\mathcal T_wH(u,r)|
 \le L(B_*+3^q\Omega)\|H\|_{1,1}.}                    \tag{CW}
\]

Indeed, group prefixes by their total. For one group, the legal integer
inverse values at a fixed output residue are distinct and lie in an
interval of length `B_*/omega`. Each input residue occurs at most
`B_*/(omega*3^q)+1` times. The sum over the clock is unaffected by the
common shift. Sum the absolute values of `H` and then the `L` groups.
The order of the mixed norm is `sup_r sum_u`, not the stronger
`sum_u sup_r`.

## 5. Selected densities with a conserved clock

Use the parent construction with `b_j=10(j+1)`,
`d_N=sum_(j<N)b_j`, `Q_N=d_N+b_N=d_(N+1)`. Its finite retained prefix
family `Gamma_N` satisfies

\[
 \beta_w\le B_*,\quad\omega_w\le\rho^{d_N},\quad
 \rho=7/8,\quad L_N\le d_N+1,
\]

and has probability `P_N>=P_infinity>0`. The rejected probability for its
next block is at most `2 exp(-b_N/1200)`. Also
`3^(b_N+b_(N+1))*rho^d_N` is bounded by an absolute constant.

Define the nonnegative joint subdensity at depth `Q_N` by

\[
 G_N=\sum_{w\in\Gamma_N}\mathcal T_wJ_{b_N}.
\]

Its full spatial-clock mass is `P_N`, and it vanishes on multiples of three.
Equations (JF) and (CW), followed by subtraction of the rejected next-block
mass, prove

\[
 E_N=G_{N+1}-\operatorname{lift}(G_N*p_{b_{N+1}}),\qquad
 \sup_r\sum_u|E_N(u,r)|\le\epsilon_N,                 \tag{5.1}
\]

where, for any chosen fixed `K`,

\[
 \epsilon_N=C(d_N+1)
       \big(2e^{-b_N/1200}+C_K b_N^{-K}\big)
       =O_K(N^{2-K})+O(N^2e^{-cN}).                    \tag{5.2}
\]

All clocks in (5.1) have depth `Q_(N+1)`: the added independent clock has
length `Q_(N+1)-Q_N=b_(N+1)`. This bookkeeping is essential.

## 6. The local clock floor

The elementary negative-binomial law is

\[
 p_t(u)=\binom{u-1}{t-1}2^{-u}\quad(u\ge t\ge1).
\]

Stirling's formula gives an absolute upper bound
`sup_u p_t(u)<=C/sqrt(t)` for `t>=1`. For every fixed `M`, it also gives
`p_t(u)>=c_M/sqrt(t)` when `|u-2t|<=M sqrt(t)` and `t` is sufficiently
large. Both bounds are uniform in the integer `u` in the indicated range.

Choose `K>5` in (5.2). Fix a large `N_0` and a unit residue `y mod 3^Q_N0`
such that `sum_u G_N0(u,y)>=P_infinity`; such a residue exists by the mean.
Choose a finite set of clocks carrying at least half this mass. For a lift
`r` of `y`, telescope (5.1) to obtain the exact identity

\[
 G_N(u,r)=(G_{N_0}*p_{Q_N-Q_{N_0}})(u,y)
       +\sum_{j=N_0}^{N-1}
         (E_j*p_{Q_N-Q_{j+1}})(u,r\bmod3^{Q_{j+1}}).
                                                               \tag{6.1}
\]

The finite retained set of initial clocks contributes at least
`c_(M+1) P_infinity/(2 sqrt(Q_N))` to the first term for
`|u-2Q_N|<=M sqrt(Q_N)`, once `N` is large. The fixed initial clock shifts
only change the onset; the lower constant for the slightly wider window
`M+1` covers them and the fixed difference in the variance scale.

For `j<=N/2`, the remaining convolution has length comparable to `Q_N`.
Its contribution in absolute value is at most
`C epsilon_j/sqrt(Q_N)`. Choose `N_0` so that the sum of these error
coefficients is smaller than one quarter of the positive main coefficient.
This choice is possible because (5.2) is summable.

For `j>N/2`, use the elementary bound `sup p_t<=1`, including `t=0`.
After multiplying by `sqrt(Q_N)=O(N)`, the total late error is

\[
 O\left(N\sum_{j>N/2}j^{2-K}\right)=O(N^{4-K})=o(1).
\]

Thus there is a constant `c_M'>0` such that every lift of `y` satisfies

\[
 G_N(u,r)\ge c_M'/\sqrt{Q_N}
 \quad\text{when }|u-2Q_N|\le M\sqrt{Q_N},              \tag{6.2}
\]

for all sufficiently large `N`.

To obtain every large word depth `s`, choose `Q_N<=s<Q_(N+1)` and keep
the prefix `Gamma_N`, followed by `k=s-d_N` unrestricted letters. Then
`b_N<=k<b_N+b_(N+1)`. Applying (JF) and (CW) compares its joint density
with `G_N*p_(s-Q_N)`, with mixed-norm error `O(N^(2-K))` plus an
exponentially small term. This is `o(s^(-1/2))`.
For the floor, telescope (6.1) directly with the final clock `s`, then add
this intermediate-depth error. The same early/late split applies because
`Q_N<=s<Q_(N+1)` and these depths are asymptotic. The first term uses the
negative-binomial lower bound at `s-Q_N0`. This gives (6.2) at every
sufficiently large `s` in the fixed positive cylinder, without assuming
that convolution preserves a lower bound on an unchanged finite window.

Every full word just used also has bounded **real** offset. An arbitrary
positive-letter suffix of length `k` has offset less than `2^k`, irrespective
of its total. Hence

\[
 \beta_{wv}\le B_*+\rho^{d_N}2^k\le B_*+1
\]

for all large `N`. Restricting to one final total makes this family finite.
No unbounded real offset was introduced by the clock convolution argument.

## 7. All unit residues

Let the positive cylinder above be `y mod 3^q`. For any unit target residue
at a sufficiently high level, choose a positive exponent `e<=2*3^q`
such that its exact inverse parent is congruent to `y mod 3^q`; two
generates the unit group modulo `3^(q+1)`. Prepend this one letter to a word
from Section 6. The weighted contribution is multiplied by `3*2^(-e)`,
which is bounded below by a fixed positive constant.

The clock shifts from `u` to `u-e`, and the word depth from `s` to `s-1`.
Use the cylinder floor with `M=2`; the fixed bound on `e` ensures it
contains every required window `|u-2s|<=sqrt(s)` at large `s`. The real
offset after prepending is at most
`1/2+(3/2)(B_*+1)`, so it too has an absolute bound. This proves (CFJ).

## 8. What this changes, and the remaining global target

The prior packet deliberately avoided any fixed-total mixing assumption.
This continuation supplies a specific additional derivation from Tao's
nonnegative pair-sum estimate, retaining total slices through every Fourier,
projection, convolution, and selected-density step. The resulting local
floor supports linear-size ordinary predecessor populations in intervals,
as proved in `GLOBAL_RENEWAL_ATTACK.md`.

That lower population bound does not prove an upper bound on survivors or
finite five energy. Those are still global tasks. In particular, no density
of ordinary integers is turned into a statement about one fixed forward
orbit, and no hypothesis in the Lean files is silently discharged by this
unformalized analytic proof.
