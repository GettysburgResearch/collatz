# Tilted renewal trace: a finite arithmetic budget and the retained immigration

**Status: written proof, with explicitly identified source-qualified inputs.
No escape exclusion is claimed.** The useful positive conclusion is a
uniform \(O(R^{-1})\) budget for the tilted trace over *every* block of
inverse depths. The actual real-tail density admits a rigorous comparison
with that budget plus a finite ordinary first-entry term. The latter term
still contains the original escaping source.

## 1. Inputs and conventions

Use the same stationary pair \((R_0,Z)\), actual odd map \(U\), finite density
\(D_j=P^j1\), and canonical ordinary trace \(h\) as in
[MOVING_CESARO_FIBRES.md](MOVING_CESARO_FIBRES.md). That file fixes the
ordinary mean absolute trace source at Valbuena commit
`a7275d5a73814d3d9a400c6fe6577de9542b03a3` and the actual \(h\)-path law.

The source-qualified real-tail input is the scalar Kesten--Goldie estimate
\(\Pr(R_0>t)\sim C/t\). The hypotheses and exact coefficient are discussed
in [*Ternary Syracuse laws: real localization, clock stability, and
critical regularity*, v2, Section 3](https://rstation.ai/problems/collatz/papers/9).
This note has not independently replayed that paper's entire proof. We
need only the consequence

\[
 C_T:=\sup_{t>0}t\Pr(R_0>t)<\infty.
 \tag{1}
\]

The arithmetic input is already in this repository at
`f63204765438c83def68154e7f253ee9b660979c`:

- `research/astra-three-routes/pass3/FINITE_RECORDS.md`, Section 1,
  with the terminal-boundary correction in the finite simple-path count;
- `research/lean-global-closure-20261121/LITERATURE_TRANSPORT_ATTEMPT.md`,
  Section 2, which uses the resulting count on actual nonperiodic paths.

For every finite simple ordinary odd path and every \(X\ge1\), the number
of its odd states up to \(X\) is at most \(5X^{39/40}\). Hence, including
only states at least \(M\ge1\),

\[
 \sum_{x\text{ on the path},\ x\ge M}\frac1x
 \le200M^{-1/40}.
 \tag{2}
\]

Indeed, apply nonnegative Mellin integration to that subset:
\(\sum x^{-1}=\int_M^\infty N_{\ge M}(t)t^{-2}\,dt\), and use
\(N_{\ge M}(t)\le5t^{39/40}\). The subset need not be a contiguous portion
of the path. Every finite inverse prefix from a nonperiodic root is a
finite simple path in the reverse order, so (2) applies with the same
constant. Passage to an infinite inverse path uses increasing finite
prefixes, not an assertion that the infinite inverse path is a single
forward orbit set.

## 2. The tilted ternary trace is an actual square-weighted row

Let \(\mathbb P_*\) give independent gaps \(e\ge1\) probabilities
\(3/4^e\), and let \(\sigma\) be its stationary ternary series law.
The series converges in \(\mathbb Z_3\); a real stationary limit under
this tilted law is neither needed nor presumed. Define

\[
 T_j(q)=3^j\sigma(q+3^j\mathbb Z_3),\qquad T_0(q)=1.
 \tag{3}
\]

For an ordinary positive odd \(q\), a prefix of length \(j\) with total
division exponent \(S\) has coefficient \(A=3^j/2^S\). Its ternary residue
equals \(q\bmod3^j\) exactly when reversing the prefix from \(q\) gives
positive ordinary integer states. Positivity follows inductively from
\(x\mapsto(2^e x-1)/3\), whenever the result is integral. The gap valuations
are exact because each reversed state is odd.

For every fixed source \(x\) with \(U^jx=q\), its actual forward itinerary
determines this reversed word uniquely. The tilted probability of the
word is \(3^j4^{-S}\), and multiplying by \(3^j\) gives \(A^2\). Thus

\[
 \boxed{T_j(q)=\sum_{U^jx=q}A_j(x)^2.}
 \tag{4}
\]

**Endpoint convention:** the sources \(x\) in (4) are all positive odd
integers, including those divisible by three at the *last inverse state*.
The finite residue condition has no remaining ternary digit to exclude
them. There is no \(K_h\)-path interpretation of those nonunit endpoints;
equation (4) is a finite tilted marginal identity.

The real affine identity \(q=A_j(x)x+B_j(x)\), with \(B_j(x)\ge0\), gives

\[
 \frac{A_j(x)^2}{q^2}\le\frac1{x^2}.
\]

If \(q\) is nonperiodic, a fixed positive source \(x\) reaches \(q\) at
at most one odd depth. Otherwise the two visits would give a positive
return of \(q\). Summing nonnegative terms therefore proves

\[
 \boxed{\sum_{j\ge0}\frac{T_j(q)}{q^2}
       \le\sum_{x\ge1}\frac1{x^2}=\zeta(2).}
 \tag{5}
\]

Keeping only odd sources improves the constant to \(\pi^2/8\); no such
improvement is needed. For every \(J\ge0,R\ge1\),

\[
 \boxed{\frac1R\sum_{j=J}^{J+R-1}\frac{T_j(q)}{q^2}
       \le\frac{\zeta(2)}R.}
 \tag{6}
\]

This bound is uniform over all nonperiodic ordinary roots and all depth
blocks. It involves no source resampling and no probabilistic
typicality of an ordinary forward orbit.

## 3. Large relative real prefixes force a finite ordinary visit

Throughout Sections 3--5, \(q\) is a nonperiodic positive odd ternary
unit. The finite marginal identity (4) itself permits every positive odd
root.

For an actual inverse prefix from \(q\), write its successive states as
\(X_0=q,X_1,\ldots,X_j\) and its affine coefficients as \(A_j,B_j\).
Direct multiplication gives

\[
 \frac{q-B_j}{q}
   =\prod_{i=1}^j\frac{3X_i}{3X_i+1}.
 \tag{7}
\]

If every \(X_i>M\), (2) and \(1-e^{-u}\le u\) give

\[
 \frac{B_j}{q}
 \le\sum_{i=1}^j\log\left(1+\frac1{3X_i}\right)
 \le\varepsilon_M:=\frac{200}{3}M^{-1/40}.
 \tag{8}
\]

The same conclusion holds for \(B_\infty/q\) on an infinite path avoiding
the finite set \(K_M=\{x>0:x\text{ odd},x\le M\}\).
Given \(0<\theta<1\), choose \(M\ge1\) so large that
\(\varepsilon_M<\theta/2\). Then

\[
 B_j\ge\theta q/2\quad\Longrightarrow\quad
 \text{the inverse prefix hits }K_M.
 \tag{9}
\]

This is a pathwise implication on genuine ordinary integers. In
particular no fibre regularity or almost-everywhere qualification is
needed to force this finite visit.

## 4. The exact real-tail comparison retains a finite immigration term

From here \(q\) is a nonperiodic positive odd ternary unit, so the
canonical \(h\)-path law and the ratios involving \(h(q)\) are defined.

Let

\[
 H_j(q;\theta)=3^j\Pr(R_0>\theta q,\ Z\equiv q\pmod{3^j}).
 \tag{10}
\]

After a valid prefix \(w\) of length \(j\), the stationary real suffix is
independent and the residual ordinary integer is \(x_w\). Thus

\[
 H_j(q;\theta)=\sum_w A_w
   \Pr\!\left(R'_0>\frac{\theta q-B_w}{A_w}\right).
 \tag{11}
\]

Here all finite endpoints, including the possible nonunit last endpoint,
are retained. If \(B_w<\theta q/2\), (1) bounds its contribution divided
by \(q\) by \((2C_T/\theta)A_w^2/q^2\). The other words hit \(K_M\) by (9).

Let \(\Gamma_M(q)\) be the finite set of possible *first* ordinary hits
of \(K_M\), including the time-zero hit when \(q\in K_M\). Each
\(x\in\Gamma_M(q)\) has a unique hitting depth \(\ell_q(x)\) and a unique
affine prefix coefficient \(A_{q,x}\). Summing all continuations of
length \(j-\ell_q(x)\) gives exactly \(D_{j-\ell_q(x)}(x)\). The bad-prefix
event is only a subset of these first-hit cylinders, so

\[
 \boxed{\frac{H_j(q;\theta)}q
 \le\frac{2C_T}{\theta}\frac{T_j(q)}{q^2}
 +\sum_{\substack{x\in\Gamma_M(q)\\\ell_q(x)\le j}}
       \frac{A_{q,x}}qD_{j-\ell_q(x)}(x).}
 \tag{12}
\]

The first term has mean at most \(2C_T\zeta(2)/(\theta R)\) over every
depth block. The second term is a genuine finite ordinary immigration,
with the prefix source and depth still present.

For a nonunit first-hit point, \(D_0(x)=1\) and \(D_m(x)=0\) for \(m\ge1\).
Such a point can occur only as the terminal inverse state. Its contribution
to the depth average is at most \(1/(Rx)\), because
\(A_{q,x}/q\le1/x\). This explicitly pays the nonunit terminal boundary;
it is not discarded by calling it an \(h\)-path.

For a fixed original nonperiodic positive odd ternary unit \(p\), put
\(q_k=U^kp\) as long as retained. In the sums over all first-hit endpoints,
extend \(h\) by zero to positive odd multiples of three, exactly as in the
all-positive ordinary trace theorem. The \(h\)-path law itself uses only
unit states.
At a common ordinary first-hit point \(x\),
\(\ell_{q_k}(x)-k=d_p(x)\) is a fixed, possibly negative integer.
The finite set \(K_M\), the coefficient bound \(A_{q_k,x}/q_k\le1/x\),
and the pinned mean absolute trace imply

\[
 \begin{split}
 \sup_{k:\,q_k\text{ retained}}
 \left|\frac1R\sum_{r=0}^{R-1}
 \sum_{\substack{x\in\Gamma_M(q_k)\\\ell_{q_k}(x)\le k+r+1}}
 \frac{A_{q_k,x}}{q_k}D_{k+r+1-\ell_{q_k}(x)}(x)
 -I_M(q_k)\right|\longrightarrow0,\\
 I_M(q):=\sum_{x\in\Gamma_M(q)}\frac{A_{q,x}}q h(x)
   =\frac{h(q)}q\Pr_q^h(\tau_M<\infty).
 \end{split}
 \tag{13}
\]

In the supremum, the expression \(I_M(q_k)\) is inside the absolute value
at the same \(k\). Equation (13) uses a finite sum of endpoint-dependent
Cesàro shifts. Missing times before contact have at most
\((d_p(x)-1)_+\) slots, fixed for that \(x\); negative shifts only change
the fixed starting index. No estimate uniform over all ordinary roots
is asserted for this convergence.

Thus (12) pays the tilted part in the exact moving-Cesàro regime and
identifies precisely the surviving part as \(I_M\). The limiting
ordinary-fibre implication also follows directly from (8):

\[
 \frac{h(q)}q\widehat\mu_q^h([\theta,1])\le I_M(q)
 \quad\text{when }\varepsilon_M<\theta.
 \tag{14}
\]

## 5. Why the finite term has not vanished

Suppose the original \(p\le M\) escapes. Let \(x_*\in K_M\) be the last
state of its forward orbit in \(K_M\); it exists because escaping
nonperiodic states are distinct. For every sufficiently late \(q_k\),
the reverse of that actual forward segment first hits \(K_M\) at \(x_*\).
Consequently

\[
 I_M(q_k)\ge\frac{A_{q_k,x_*}}{q_k}h(x_*)
 =\lambda(x_*\rightsquigarrow q_k)\frac{h(x_*)}{x_*}
 \ge\delta\frac{h(x_*)}{x_*}>0.
 \tag{15}
\]

This is the same retained original mass as the submeasure in
`MOVING_CESARO_FIBRES.md`, equation (32), now exposed as a specific finite
first-entry term in a rigorous real-tail/tilted-trace inequality.

The scalar tail bound cannot remove it: once \(B_w\ge\theta q\), the
conditional threshold in (11) is nonpositive and its tail probability
is one. Replacing this factor by a multiple of \(A_w/q\) without retaining
that event would delete the term in (15).

The literature's finite-quotient tail limit does not supply this deletion.
The cited ternary-tail paper's Theorem 1 gives a Gaussian change of
regime with precision, while its Corollary 7 gives full-space mutual
singularity at every finite real threshold. Neither statement is a
relative upper bound on this specified moving ordinary residue. Even an
unconditional quotient error tending to zero would be multiplied here by
\(3^{k+r}/q_k^2\), which can grow exponentially.

Finally, first-entry localization does not transport the PR177 run
weight from a source to its terminal point. The relevant pin is
`e4ca639326bac73da8c2a698dec8a749e5efbe68`,
`research/lean-exact-witness-global-20261121/LITERATURE_CANONICAL_ENERGY.md`,
Section 8, especially equation (47). Multiplying (13) by the
terminal weight retains \(A_{q,x}h(x)w(q)/q\), not
(h(x)w(x)/x). A bounded truncation costs its full sup norm. Therefore
the present argument provides no uniform bound on PR177's canonical
commutator (47), and no conclusion about the vanishing of escape charge.
