# Linear selected blocks, a uniform Syracuse atom floor, and harmonic predecessor mass

## Status and scope

This is a complete written derivation **using Tao's published fine-scale mixing theorem** as an external theorem. It is being submitted for independent mathematical review. The analytic argument is not yet formalized in Lean, and the file is not a proof of Collatz. In particular it does not prove the missing finite-energy estimate in PR167.

The selected-density strategy and the weighted residue-counting device are attributed to Naoufal El Jaouhari, *Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts* (October 2026), DOI `10.5281/zenodo.23377671`. The strategy and elementary lemmas were located in the author's attributed exposition in [Fourier Wren, rStation paper 10, v2](https://rstation.ai/problems/collatz/papers/10/v2), Appendix A. The Zenodo archive itself was inaccessible in this session. No priority claim is made for the atom floor or the strategy. The simplification developed here is a **linearly growing independent block schedule**, which makes the uniform convergence estimate elementary once the counting device and Tao's theorem are available. None of the additional joint-mixing claims in the rStation paper is used.

The only imported analytic estimate is from Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12, Proposition 1.14, equations (1.26)--(1.27), together with consistency (1.23):

https://doi.org/10.1017/fmp.2022.8

The published Cambridge text was inspected directly. It states the estimate for every pair `1 <= m <= n`, with a constant depending only on the chosen power `A`. No ordinary-orbit mixing or statement about individual valuation slices is imported.

## 1. Exact normalization and the imported estimate

Let `G_s = Z/(3^s Z)`, with normalized counting average

\[
\langle f\rangle_s=3^{-s}\sum_{x\in G_s}f(x).
\]

For independent positive integers `a_i` with `Pr(a_i=a)=2^{-a}`, put

\[
A_i=a_1+\cdots+a_i,\qquad
X_s=\sum_{i=1}^s3^{i-1}2^{-A_i}\pmod {3^s},
\qquad D_s(x)=3^s\Pr(X_s=x).
\]

Thus `D_s` has full-Haar mean one, and is zero on multiples of three for `s >= 1`. This is the reverse-word orientation of Tao's Syracuse random variable, equation (1.29). Its projection to `G_m` is exactly the law of `X_m`: all terms after `m` vanish modulo `3^m`, and the first `m` exponents have the same independent distribution.

Write `lift` for pullback along reduction between these finite groups. Tao's estimate is therefore exactly

\[
\boxed{\|D_n-\operatorname{lift}D_m\|_{L^1(G_n)}
       \le C_A m^{-A}\quad(1\le m\le n).} \tag{FM}
\]

The `L^1` norm here uses normalized counting measure. The factors `3^n` in `D_n` cancel `3^{-n}` in the norm. In the rest of the argument only `A=4` is used.

## 2. Affine words and an elementary weighted counting estimate

For a finite word `w=(a_1,...,a_d)`, define the real positive quantities

\[
A(w)=\sum_i a_i,\quad
\omega_w=3^d2^{-A(w)},\quad
\beta_w=\sum_{i=1}^d3^{i-1}2^{-(a_1+\cdots+a_i)},
\quad \Phi_w(z)=\omega_wz+\beta_w.
\]

The rational coefficients also define maps on ternary residue groups, because their denominators are powers of two. The map `Phi_w : G_q -> G_(d+q)` is injective, with image the residue cylinder `r = beta_w (mod 3^d)`. Define a positive transport operator by

\[
(T_{w,q}h)(\Phi_w(z))=\omega_wh(z),
\]

and set it to zero outside this image. Direct summation gives

\[
\langle T_{w,q}h\rangle_{d+q}=2^{-A(w)}\langle h\rangle_q.
\tag{2.1}
\]

These operators commute with lifting. Word concatenation gives `Phi_(uv)=Phi_u o Phi_v` and `T_(uv)=T_u T_v` at the matching resolutions. In particular,

\[
D_{d+q}=\sum_{|w|=d}T_{w,q}D_q. \tag{2.2}
\]

The countable sum is a sum of nonnegative terms and has the stated probabilistic meaning.

### Fixed-total injectivity

For fixed word length `d` and total `A`, different words have different real offsets `beta_w`. To prove this, set

\[
B(w)=2^A\beta_w=\sum_{i=1}^d3^{i-1}2^{A-A_i}.
\]

When `d >= 2`, the identity

\[
B(w)-3^{d-1}=2^{a_d}B(a_1,\ldots,a_{d-1})
\]

recovers `a_d` from the exact two-adic valuation: the second factor is odd. Repetition recovers all letters except the first, which is fixed by the total. Length one is immediate.

### Weighted counting lemma

Let `Gamma` be a finite set of words of a common length `d`, satisfying

\[
0\le\beta_w\le B_*,\qquad \omega_w\le\Omega.
\]

Let `L` be the number of different totals `A(w)` occurring. Then, for every real function on `G_q`,

\[
\boxed{\left\|\sum_{w\in\Gamma}T_{w,q}h\right\|_\infty
 \le L(B_*+3^q\Omega)\|h\|_{L^1(G_q)}.} \tag{WC}
\]

Proof: fix an output residue and choose an integer representative `M`. A contributing word has the integral inverse value

\[
R_w=(M-\beta_w)/\omega_w=(2^{A(w)}M-B(w))/3^d.
\]

Its input residue is `R_w mod 3^q`. In a group with fixed total, `omega` is constant, and these integers are distinct by fixed-total injectivity. They lie in a real interval of length `B_*/omega`. Each residue modulo `3^q` occurs at most `B_*/(omega 3^q)+1` times. Multiplication by `omega` bounds its total coefficient by `B_*/3^q+omega`. Sum the absolute values of `h` and then the `L` groups. This proves (WC), including `d=0` with the singleton empty word.

## 3. A linear block schedule

Fix a positive integer `B` divisible by ten; `B=10` suffices. For `j >= 0`, set

\[
b_j=B(j+1),\quad k_j=b_j,\quad
d_N=\sum_{j<N}b_j=BN(N+1)/2,\quad
Q_N=d_N+k_N=B(N+1)(N+2)/2.
\]

Retain the finite set `W_j` of words of length `b_j` whose total satisfies

\[
|A(w)-2b_j|\le b_j/10.
\]

Let `Gamma_N` consist of concatenations of one retained word from each of `W_0,...,W_(N-1)`. Define `p_j=Pr(W_j)` and `P_N=prod_(j<N) p_j`.

For a geometric letter, the logarithmic moment generating function of `a-2` is

\[
\psi(t)=-t-\log(2-e^t).
\]

On `|t| <= 1/4`, `psi''(t)=2e^t/(2-e^t)^2 <= 6`. Thus `psi(t) <= 3t^2`. Chernoff with `t=+/-1/60` gives

\[
1-p_j\le 2\exp(-b_j/1200). \tag{3.1}
\]

Every `p_j` is positive, because the all-two word is retained. The rejected probabilities are summable. Consequently

\[
P_\infty:=\lim_NP_N>0. \tag{3.2}
\]

There is no requirement that the first few `p_j` be close to one.

### Uniform bounds for retained prefixes

Put `rho=7/8`. For a retained block,

\[
\omega_w\le(3/4)^{b_j}2^{b_j/10}\le\rho^{b_j},
\qquad 0\le\beta_w\le 2^{b_j}.
\]

The first bound uses the elementary numerical inequality `2^(1/10) <= 7/6`. The second follows from the termwise bound `a_1+...+a_i >= i`. Therefore every word in `Gamma_N` satisfies

\[
\omega_w\le\Omega_N:=\rho^{d_N},\qquad
\beta_w\le\sum_{j<N}2^{B(j+1)}\rho^{Bj(j+1)/2}\le B_*:=16\cdot2^{6B}. \tag{3.3}
\]

For the last estimate, the first six summands are at most `2^(6B)` each. From the sixth summand onward the ratio of consecutive terms is at most `(2 rho^6)^B < (9/10)^B <= 9/10`, so the remaining tail contributes at most nine more copies of `2^(6B)`.

All prefix totals lie in `[1.9 d_N, 2.1 d_N]`. In particular the number `L_N` of different totals is at most `d_N+1`.

The next comparison is at the tail resolution

\[
q_N=b_N+k_{N+1}=B(2N+3),\qquad d_N+q_N=Q_{N+1}.
\]

There is a uniform bound

\[
3^{q_N}\Omega_N\le 3^{37B}. \tag{3.4}
\]

Indeed the ratio of the left side at `N+1` and at `N` is `(9 rho^(N+1))^B`. Since `9 rho^17 < 1`, the sequence decreases for `N >= 16`; for `N <= 17`, dropping `rho^(d_N)` bounds it by `3^(37B)`. Set `K_B=B_*+3^(37B)`.

## 4. Uniform convergence of selected densities

Define a function at level `Q_N` by

\[
g_N=\sum_{w\in\Gamma_N}T_{w,k_N}D_{k_N}.
\]

It has the exact properties

\[
0\le g_N\le D_{Q_N},\quad
\langle g_N\rangle_{Q_N}=P_N,
\quad g_N=0\text{ on multiples of }3. \tag{4.1}
\]

To compare consecutive levels, put

\[
R_N=\sum_{v\in W_N}T_{v,k_{N+1}}D_{k_{N+1}}
       \quad\text{on }G_{q_N}.
\]

Then `0 <= R_N <= D_(q_N)` and

\[
\|D_{q_N}-R_N\|_1=1-p_N. \tag{4.2}
\]

Concatenation and lifting give, exactly at level `Q_(N+1)`,

\[
g_{N+1}-\operatorname{lift}g_N
=\sum_{w\in\Gamma_N}T_{w,q_N}
   (R_N-\operatorname{lift}D_{k_N}). \tag{4.3}
\]

Here the lift inside the parentheses is from `k_N` to `q_N`, and the lift on the left is from `Q_N` to `Q_(N+1)`. Since `q_N >= k_N >= 1`, (FM), (4.2), and (WC) yield

\[
\boxed{\|g_{N+1}-\operatorname{lift}g_N\|_\infty
\le K_B(d_N+1)
 \left(2e^{-b_N/1200}+C_4b_N^{-4}\right).} \tag{4.4}
\]

The sum over `N` is finite: `d_N=O_B((N+1)^2)` and `b_N=B(N+1)`. Denote the right side of (4.4) by `epsilon_N`. Choose a fixed `N_0` so large that

\[
\sum_{N\ge N_0}\varepsilon_N<P_\infty/2.
\]

Set `q=Q_(N_0)`. Since `g_(N_0)` has mean `P_(N_0) >= P_infty`, some unit residue `y mod 3^q` satisfies `g_(N_0)(y) >= P_infty`. Telescoping (4.4) shows that every lift of this residue to level `Q_N`, for every `N >= N_0`, has

\[
g_N\ge P_\infty-\sum_{j=N_0}^{N-1}\varepsilon_j
>P_\infty/2=: \kappa.
\]

Fix any `h >= q` and any residue `z mod 3^h` lying above `y`. Choose `N >= N_0` large enough that `Q_N >= h`. Every lift of `z` to level `Q_N` has `D_(Q_N) >= g_N >= kappa`. Averaging these lifts, exact consistency of the Syracuse laws gives

\[
\boxed{D_h(z)\ge\kappa\qquad(h\ge q,\ z\equiv y\pmod {3^q}).} \tag{4.5}
\]

The entire step uses finite groups and a summable numerical error sequence. No topology on `Z_3`, no almost-everywhere limit, and no ordinary-orbit mixing assertion is needed.

## 5. Spreading the cylinder to every unit

The infinite geometric version of the exact recursion is

\[
D_{h+1}(r)=
\sum_{a\ge1:\ 2^ar\equiv1\ (3)}
3\,2^{-a}
D_h\left((2^ar-1)/3\pmod {3^h}\right). \tag{5.1}
\]

For any unit `r mod 3^(h+1)` with `h >= q`, choose

\[
1\le a\le H:=2\cdot3^q,
\qquad 2^ar\equiv 3y+1\pmod {3^{q+1}}.
\]

Such an exponent exists because two generates the multiplicative unit group modulo every power of three. One elementary proof is `v_3(4^t-1)=1+v_3(t)`, which gives exact order `2*3^q` modulo `3^(q+1)`.

This chosen term in (5.1) has its input in the positive cylinder. Thus

\[
D_{h+1}(r)\ge3\,2^{-H}\kappa=:c>0. \tag{5.2}
\]

For smaller levels, projection from level `q+1` preserves the same bound at every unit residue. We obtain the global conclusion

\[
\boxed{D_s(r)=3^s\Pr(X_s=r)\ge c
\quad\text{for every }s\ge1\text{ and every }3\nmid r.} \tag{FLOOR}
\]

The constant exists independently of the level and residue. No numerical value is claimed. The proof used a fixed `C_4` from Tao's theorem, so the uniform convergence cutoff, cylinder, and hence `c` can depend on that constant.

## 6. Ordinary harmonic predecessor divergence

Let `U(n)=(3n+1)/2^(v_2(3n+1))` on positive odd integers.

### Nonperiodic odd target

Fix a positive odd unit `a` which is not periodic under `U`. An exponent word of length `s`, read outward from `a`, gives recursively

\[
x_0=a,\qquad x_i=(2^{a_i}x_{i-1}-1)/3.
\]

The congruence `beta_w = a (mod 3^s)` is equivalent to integrality of the final `x_s`. It also implies integrality of every earlier `x_i`: alternatively use each prefix congruence directly. Since the starting target is positive, the integral inverse recurrence gives `x_i >= 1` at every step. Each `x_i` is odd, and `3 x_i+1=2^(a_i) x_(i-1)` then shows that the prescribed valuation is exact. Thus `U^s(x_s)=a`.

At fixed `s`, different words give different sources: the deterministic forward `U` orbit and its exact valuations recover the word in reverse order. Also

\[
a=\omega_w x_s+\beta_w>\omega_w x_s,
\qquad \frac1{x_s}>\frac{\omega_w}{a}.
\]

Consequently the harmonic sum over sources at depth `s` satisfies

\[
\sum_{U^s n=a}\frac1n
\ge\frac1a\sum_{\beta_w\equiv a\ (3^s)}3^s2^{-A(w)}
=\frac{D_s(a)}a\ge\frac ca. \tag{6.1}
\]

A source cannot occur at two different depths: that would make `a` periodic. Thus all these depth sets are disjoint, and

\[
\boxed{\sum_{n:\exists s\ge0,\ U^s n=a}\frac1n=+\infty.} \tag{6.2}
\]

There is no assumption about the trajectory from `a` escaping to infinity, and no estimate for a trajectory's multiplicative correction factor is needed.

### Periodic odd target

Suppose instead that `a` is periodic and is a positive odd unit. Choose the least positive `e` with `2^e a = 1 (mod 3)` and consider its three odd inverse parents

\[
x_e=(2^e a-1)/3,\quad x_{e+2},\quad x_{e+4}.
\]

These are positive distinct odd integers. The relation `x_(e+2)=4x_e+1` shows that exactly one is divisible by three, so two are units. At most one is periodic: any periodic point mapping directly to a point on a deterministic cycle is its unique cycle predecessor. Therefore at least one unit parent `b` is nonperiodic. Every predecessor of `b` is a predecessor of `a`. Applying (6.2) to `b` proves the same divergent harmonic sum for `a`.

For a positive even unit target `a=2^i a_0` with `a_0` odd, use three admissible exponents `e,e+2,e+4` starting at the least admissible `e >= i+1`. Again two parents are units and at most one is periodic, and their shortcut orbits pass through `a`. This proves divergence for every positive target not divisible by three under the ordinary shortcut map.

If one wants the predecessor sum restricted to ternary-unit sources, it follows as well. Every odd nonunit source `n` has unit successor `m=U(n)` and `1/n=3/(2^e m-1) <= 6/(2^e m)` for its exponent `e >= 1`. Summing possible nonunit parents of one `m` bounds their reciprocal mass by `6/m`; each source has a unique successor. Hence finiteness of the unit-source predecessor mass would imply finiteness of the entire odd-source predecessor mass, contradicting (6.2).

### Positive lower logarithmic density, with an explicit valuation cutoff

There is a stronger conclusion needed at the repository's harmonic endpoint. Mere divergence in (6.2) would not contradict a zero limiting average. The floor supplies a uniform quantitative logarithmic bound as follows.

For the total `A_s` of `s` independent geometric letters,

\[
\mathbb E(3/2)^{A_s}=3^s.
\]

Markov's inequality therefore gives, uniformly in the target residue,

\[
3^s\Pr(A_s>6s)\le 9^s(2/3)^{6s}=(64/81)^s. \tag{6.3}
\]

Choose an integer `s_0 >= 1` such that `(64/81)^s <= c/2` for every `s >= s_0`. By (FLOOR) and (6.3), the normalized atom mass of words that reach any fixed unit residue and satisfy `A_s <= 6s` is at least `c/2`.

For a nonperiodic positive odd unit target `a`, each associated ordinary source satisfies

\[
n<a2^{A_s}/3^s\le aR^s,\qquad R=64/3.
\]

Their harmonic mass is at least `c/(2a)` at each depth, and those depth sets are disjoint. Thus, writing `H_a(X)` for the reciprocal sum of ordinary shortcut predecessors of `a` up to `X`,

\[
H_a(X)\ge\frac c{2a}
\left(\left\lfloor\log_R(X/a)\right\rfloor-s_0+1\right)_+.
\tag{6.4}
\]

In particular

\[
\liminf_{X\to\infty}\frac{H_a(X)}{\log X}
\ge\frac c{2a\log R}>0. \tag{6.5}
\]

For every positive shortcut target `a` with `3` not dividing `a`, the parent selection above yields a nonperiodic odd unit `b<22a` whose shortcut orbit meets `a`. In the even case the least admissible exponent is at most `i+2` and the chosen exponent at most `i+6`, so `b<64a/3<22a`; the odd case is included. Apply (6.5) to `b` to obtain the uniform conclusion

\[
\boxed{\liminf_{X\to\infty}\frac1{\log X}
\sum_{\substack{n\le X\\\exists t\ge0:\ T^t n=a}}\frac1n
\ge \frac c{44a\log(64/3)}>0\quad(3\nmid a).} \tag{LOG}
\]

This is positive lower **logarithmic** density; no positive natural-density conclusion is asserted. It is enough for the endpoint profile contradiction described in the companion `REPOSITORY_RIGIDITY_COROLLARY.md`.

## 7. What remains open in the repository's full proof attempt

The atom-floor proof establishes both divergent harmonic predecessor mass and the stronger positive lower logarithmic density (LOG). The companion corollary identifies how (LOG) replaces the positive-natural-density hypothesis in the existing harmonic finite-energy rigidity argument, and how the predecessor moments discharge the subcritical input for every exponent below one. This still requires the repository's finite-energy assumption: the present proof does not supply an all-source charge bound for PR167, convert the PR146 terminal count into summable full charge, or establish finite five energy for a hypothetical separating label.

The written analytic derivation must also be kept distinct from Lean verification. At present Tao's theorem and the analysis above are mathematical inputs, not imported kernel-checked Lean declarations in the no-Mathlib checkpoint.
