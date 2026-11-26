# A fixed conductor Dirichlet completion of the ordinary escape test

**Written finite-law identities.** The source-qualified result in
[Exponential dust](../escape/EXPONENTIAL_DUST.md) reduces absence of positive
ordinary escape to a signed harmonic trace of the *original* finite Syracuse
law. The elementary completion below turns its moving finite interval into
three Dirichlet twists with fixed conductor eight. No bound for the remaining
normalized Dirichlet value is asserted.

Put `q = 3^k` and let `rho_k` be the density on `Z/qZ`, extended periodically
to all integers. On the odd representatives `1 <= y < 2q` its total is `q`.
For positive odd `y` put

\[
 W(y)=\begin{cases}-1/4&y\equiv1\pmod8,\\
 3/4&y\equiv3\pmod8,\\-5/4&y\equiv5\pmod8,\\
 3/4&y\equiv7\pmod8.\end{cases}
 \qquad
 Z_k=\sum_{\substack{1\le y<2q\\y\text{ odd}}}
                 \frac{W(y)\rho_k(y)}y.
\]

## Uniform completion

The ordinary ordered series

\[
 S_k=\sum_{y\ge1,\ y\text{ odd}}\frac{W(y)\rho_k(y)}y
\]

converges, and at every `k >= 0`

\[
                         |S_k-Z_k|\le\frac58.                 \tag{1}
\]

Indeed its coefficient sequence has period `8q` and zero sum: over the four
odd translates of any residue modulo `q`, `W` visits its four values once.
For one principal odd representative `r`, the omitted sequence is
`W(r+2lq)`, `l >= 1`. Its period is four because `q` is odd. Every partial
sum of this sequence has absolute value at most `5/4`, by the four displayed
values (either orientation of the cycle gives the same bound). Summation by
parts gives

\[
 \left|\sum_{l\ge1}\frac{W(r+2lq)}{r+2lq}\right|
       \le\frac{5}{4(r+2q)}\le\frac{5}{8q}.
\]

Multiply by the nonnegative `rho_k(r)` and sum; normalization gives (1).
There are only `q` residue classes in this grouping, so it also agrees with
the ordinary ordered limit. This does not replace the law by Haar measure.

## Three fixed real characters

Extend the following real Dirichlet characters to be zero on even integers:

| odd residue | 1 | 3 | 5 | 7 |
|---|---:|---:|---:|---:|
| `chi_-4` | 1 | -1 | 1 | -1 |
| `chi_8` | 1 | -1 | -1 | 1 |
| `chi_-8` | 1 | 1 | -1 | -1 |

The literal identity is

\[
                  W=(-3\chi_{-4}+\chi_8+\chi_{-8})/4.          \tag{2}
\]

For any of these characters define, first for `Re(s)>1`,

\[
 L_k(s,\chi)=\sum_{n\ge1}\frac{\rho_k(n)\chi(n)}{n^s}.
\]

Each coefficient sequence is periodic of period `8q` and has mean zero.
Its bounded partial sums give holomorphy for `Re(s)>0` by summation by parts,
with the ordinary convergent series at `s=1`. Consequently

\[
 S_k=\tfrac14[-3L_k(1,\chi_{-4})+L_k(1,\chi_8)
                                      +L_k(1,\chi_{-8})].       \tag{3}
\]

This is a Dirichlet series with a periodic density coefficient, not the
Euler product of a new multiplicative character. In particular classical
bounds for primitive character L-functions do not by themselves bound it.

For comparison, at depth zero `rho_0=1`; the usual three elementary
Dirichlet values give

\[
 S_0=-\frac{3\pi}{16}
       +\frac{\log(1+\sqrt2)}{4\sqrt2}
       +\frac{\pi}{8\sqrt2}.
\]

## Exact transfer at a general Mellin parameter

Let `e(x)=v_2(3x+1)` and `U(x)=(3x+1)/2^{e(x)}` on positive odd integers.
For any bounded function `V` on the positive odd integers, and `Re(s)>1`,
the original geometric-gap recursion and a change of variables give

\[
 \sum_{y\text{ odd}>0}\frac{\rho_{k+1}(y)V(y)}{y^s}
 =\sum_{x\text{ odd}>0}\rho_k(x)
       \left(\frac3{2^{e(x)}}\right)^{1-s}
       \frac{V(Ux)}{(x+1/3)^s}.                                \tag{4}
\]

For fixed `k` both sides are absolutely convergent in this half-plane.
The change of variables retains precisely the legal positive parents:
`x=(2^e y-1)/3` is a positive odd integer exactly when the ternary
congruence holds; oddness of `y` forces the exponent to be the full
valuation of `3x+1`. No independent inverse policy is introduced.

At `s=1`, for the test `W`, both ordinary ordered series still converge and
(4) yields

\[
 S_{k+1}=\sum_{x\text{ odd}>0}
                     \frac{\rho_k(x)W(Ux)}{x+1/3}.             \tag{5}
\]

Here is the needed rearrangement justification. Group first by `e`. After
the substitution to `y`, its coefficient in the harmonic sum is `3/2^e`
times a bounded sequence periodic in `y` with period dividing `24q` and
zero mean, including the ternary gate. It has sup norm at most
`max rho_k`. Every partial harmonic sum of such a sequence is
`O((max rho_k) log(2q))`, uniformly in `e` and the upper cutoff. The
geometric `2^{-e}` factor therefore gives uniform convergence over the
groups. The cutoff `x <= X` merely changes the terminal `y` cutoff in
each group. One may first keep finitely many groups and then pass to
their uniformly small tail. This verifies (5) in the ordinary `x` order,
as well as by the limit `s -> 1+` in (4).

An exact finite-root transport, including the fact that every supplied
trace is an actual accelerated odd orbit, is proved in
[FormalTransport.lean](FormalTransport.lean). Its `exact_mark_transport`
also retains the affine offset in the joint real/ternary analysis; it is
not a proof of an infinite analytic limit.

## The full escape obligation in this form

Under the explicitly retained ordinary density, passage, and atom-floor
inputs of the companion theorem, let `H_C>0` be the charge of each positive
escaping component. Equations (1) and (3) and that theorem imply

\[
 \liminf_{k\to\infty}\frac{S_k}{k}
 \ \ge\ \left(\frac74-\log_2 3\right)\sum_{C\text{ escaping}}H_C.
                                                               \tag{6}
\]

If there is no positive escape, the same theorem gives `S_k/k -> 0`.
Thus the following concrete fixed-conductor assertion would be enough
to settle the escape half, and is equivalent to it under those inputs:

\[
 \liminf_{k\to\infty}\frac{
 -3L_k(1,\chi_{-4})+L_k(1,\chi_8)+L_k(1,\chi_{-8})}{k}\le0.
                                                               \tag{7}
\]

Assertion (7) is unproved. The identity reduces its test to a fixed
finite character combination; the coefficient `rho_k` still carries
the complete exact affine law. Merely retaining low quotient marginals,
an `L^p` bound, or very small total variation error does not suffice, as
the earlier ordinary-head perturbations show. Even an escape exclusion
must still be paired with exclusion of nontrivial positive cycles for a
complete Collatz proof.
