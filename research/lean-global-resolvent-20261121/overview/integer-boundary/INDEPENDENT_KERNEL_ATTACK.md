# Independent attack on the positive analytic kernel

## Outcome

I did **not** prove that the kernel vanishes and did not construct an unconditional nonzero solution. The boundary-regularity route has a precise obstruction: every nonzero solution would force an exact nondecaying geometric subsequence of its renormalized coefficients. Consequently its second boundary derivative cannot belong to Hardy H^1. Upgrading the given coefficient envelope to `h_n = o(n^-2)` is therefore a genuine new uniqueness theorem, not a routine consequence of the regularity already available.

The problem also admits a complete elementary maximal-solution construction. In conjunction with the parent project's independently proved reciprocal summability of injective Collatz orbits, this identifies the uniqueness statement with the absence of divergent positive Collatz trajectories. It does not exclude other cycles, which the cocycle already kills.

## Repository reconciliation and evidence boundary

This agent initially received only the standalone mixed equation and its coefficient envelope. It recognized the dynamics from the coefficients. The coordinator then supplied PR177's already-established elementary reciprocal bound so that time could be spent on the proposed regularity bootstrap. The maximal-solution and component classification below are therefore independent reconstructions of known project input, not claimed new results. The operator-growth test is also weaker than the positive known-basin quasimode theorem in [PRESSURE_WIENER_ATTACK.md](PRESSURE_WIENER_ATTACK.md).

The exact renormalized coefficient repetition, differentiated equation, and regularity test are the useful outcome of this additional attempt. They are written deductions with coordinating reconstruction; they are not Lean claims. No endpoint regularity or uniqueness theorem was obtained. Exact upstream pins are retained in [SOURCES.json](SOURCES.json).

## 1. Exact coefficient recurrence

Let `S = {n >= 1 : gcd(n,6)=1}`, let

\[
a(n)=\nu_2(3n+1),\qquad T(n)=\frac{3n+1}{2^{a(n)}}.
\]

The given analytic equation is equivalent to

\[
h_n=\frac{9}{4^{a(n)}}h_{T(n)}\qquad(n\in S). \tag{1}
\]

To check this without losing the large-valuation case, take the coefficient of `z^(3n+1)`. If `a(n)=e<=6`, precisely the `e`th term on the right contributes, with coefficient `36864/4^e`. Its residue condition is exactly the requirement that the predecessor `(2^e T(n)-1)/3=n` is not divisible by 3. If `a(n)>=7`, the right side contributes nothing and the second left-side term gives

\[
h_n=64^{-2}h_{(n-21)/64}. \tag{2}
\]

The new index belongs to S, its valuation drops by 6, and it has the same accelerated successor T(n). Iterating (2) gives (1). Conversely (1) gives all coefficients of the functional equation, including the high-valuation coefficients; all other coefficients vanish. Absolute convergence on the unit disk justifies this converse analytically.

## 2. A complete maximal-solution formula

Set `f_n=n sqrt(h_n)` and `q(n)=3n/(3n+1)`. Equation (1) becomes

\[
f_n=q(n)f_{T(n)},\qquad 0\le f_n\le1. \tag{3}
\]

For every n in S the decreasing product

\[
P(n)=\prod_{j\ge0}q(T^j(n))\in[0,1]
\]

exists. It satisfies `P(n)=q(n)P(T(n))`. Thus

\[
h_n^*=\begin{cases}n^{-2}P(n)^2,&n\in S,\\0,&n\notin S\end{cases} \tag{4}
\]

is always an admissible solution of the analytic equation, possibly identically zero. It is pointwise maximal: iterating (3) and using `f<=1` gives

\[
f_n\le\prod_{j<k}q(T^j(n))\longrightarrow P(n).
\]

Moreover,

\[
P(n)>0\iff\sum_{j\ge0}\frac1{T^j(n)}<\infty, \tag{5}
\]

because `-log q(m)=log(1+1/(3m))` is bounded above and below by positive constant multiples of `1/m` for positive integers m.

Every eventually periodic orbit gives P=0, independently of which cycle it enters. On a summable escaping orbit P is positive, and (4) is an actual counterexample conditional only on existence of that orbit. This is not a formal-series construction: `sum h_n^* <= sum n^-2`, so H* is continuous on the closed disk and holomorphic inside it.

On every forward-merging equivalence class with P>0, all solutions have the form `f_n=c_C P(n)` with one constant `c_C in [0,1]`. Indeed `f/P` is T-invariant; the upper bound follows from maximality. On all other classes f vanishes.

The parent supplied the already-proved project fact that every injective orbit has a power-saving counting bound, hence a finite reciprocal sum. With that fact, the kernel is nontrivial **if and only if there is a divergent positive Collatz trajectory**. Any positive trajectory enters S after its first odd step unless it was already there.

## 3. Exact obstruction to the proposed boundary bootstrap

Equation (2), now read in the opposite direction, gives for every n in S

\[
h_{64n+21}=64^{-2}h_n. \tag{6}
\]

Define

\[
g_n=(n+1/3)^2h_n.
\]

Since `64n+21+1/3=64(n+1/3)`, (6) gives the **exact identity**

\[
g_{64n+21}=g_n. \tag{7}
\]

Iterating, the indices are

\[
n_k=64^k(n+1/3)-1/3=64^k n+(64^k-1)/3,
\]

and

\[
n_k^2h_{n_k}=g_n\left(\frac{n_k}{n_k+1/3}\right)^2
\longrightarrow g_n. \tag{8}
\]

Thus any single positive coefficient forces `limsup m^2 h_m > 0`. Conversely `m^2 h_m ->0` forces H=0 immediately, without a maximum-principle argument.

Let `D=z d/dz`. If `D^2 H` had an L^1 boundary function in the Hardy H^1 sense, the Riemann-Lebesgue lemma would imply `n^2 h_n ->0`. Therefore every nonzero solution must have

\[
D^2H\notin H^1. \tag{9}
\]

The envelope gives continuity on the closed disk and the angular modulus

\[
|H(e^{i(t+\delta)})-H(e^{it})|
\le \sum_n n^{-2}\min(2,n|\delta|)
=O\!\left(|\delta|\log\frac{e}{|\delta|}\right). \tag{9a}
\]

Thus H belongs to C^alpha for every alpha<1. It also supplies

\[
H\in H^s(\mathbb T)\quad\text{for every Sobolev }s<3/2,
\]

since `sum n^(2s) h_n^2 <= sum n^(2s-4)`. In particular it does give an L^2 first weak boundary derivative, but neither a continuous first derivative nor an L^1 second derivative follows from the envelope. The envelope alone does not even guarantee Lipschitz continuity. No such stronger consequence of the full equation was established here. Even the endpoint `H in H^(3/2)` would not by itself force `n^2 h_n ->0`.

For perspective, the isolated lacunary series

\[
K(z)=\sum_{k\ge0}(n_k+1/3)^{-2}z^{n_k}
\]

obeys the coefficient envelope, belongs to C^1 and to every Sobolev H^s with s<2, and has a first derivative in C^alpha for every alpha<1. Nevertheless `n_k^2 [z^(n_k)]K ->1`. This is only a regularity diagnostic, **not** a solution of the full mixed equation. It shows that even substantial subcritical boundary smoothing would not establish the needed little-o estimate. C^2, W^(2,1), or Hardy H^1 control of D^2H would suffice, but none has been derived.

Equation (8) also yields a quantitative singularity. Fix a positive coefficient. For r sufficiently close to 1 there are a positive constant times `log(1/(1-r))` indices n_k below `1/(1-r)`, and `r^n_k` stays bounded below there. Hence

\[
D^2H(r)\ge c\log\frac1{1-r}-C. \tag{10}
\]

This does not contradict the supplied envelope, which only gives an upper bound of order `(1-r)^(-1)` for D^2H.

## 4. Differentiating the mixed equation does not close the estimate

Put

\[
F=D^2H,\qquad G=(D+1/3)^2H.
\]

Applying D^2 to the original equation and dividing by 36864 gives exactly

\[
zG(z^3)-z^{64}G(z^{192})
=\sum_{e=1}^6 (R_eF)(z^{2^e}). \tag{11}
\]

Here `G-F=(2/3)DH+(1/9)H` is already in H^2. This is the strongest promising-looking bootstrap identity I found.

The six terms on the right have mutually disjoint 2-adic valuation supports. Every allowed residue modulo 9 occurs in exactly two R_e. Therefore, **if one were allowed to assume** F in H^2, Parseval would give

\[
\left\|\sum_e(R_eF)(z^{2^e})\right\|_2^2=2\|F\|_2^2.
\]

But the two terms on the left overlap on exactly the coefficients `g_n` and `g_(64n+21)`, which are equal by (7). Their cross term is therefore `sum_n g_n^2`, whenever finite. Under that extra H^2 assumption, Parseval makes the left side have squared norm `2||G||_2^2-2||G||_2^2=0`, and (11) then forces F=0. This is a valid **conditional** uniqueness argument. It provides no finite bound for those norms in the first place. More directly, (7) already says that a nonzero G cannot belong to H^2, since one nonzero coefficient repeats infinitely often. The two compositions cannot be treated as unrelated dilation equations providing independent regularity.

The attractive Parseval identity thus assumes the very summability that would settle uniqueness. No estimate derived here puts F in H^1 or H^2 from its a priori bounded coefficients. Treating (11) as separate 2-Mahler and 3-Mahler equations would be unjustified.

## 5. A different failed closing mechanism: weighted contraction

Let B act on coefficient sequences by `(Bh)_n=(9/4^a(n))h_T(n)`. One might seek a contraction on `ell^1(n^p)`; the envelope automatically puts h in this space for p<1.

This cannot work with a plain polynomial weight. For any k there are arbitrarily large admissible chains of k successive inverse exponent-one steps:

\[
n_j=(2/3)^j(m+1)-1,\qquad 0\le j\le k.
\]

For example, take `m+1=2*3^(k+1)*L`. Then all n_j are odd and congruent to -1 modulo 3, and `T(n_j)=n_(j-1)` with exponent one. The contribution of this single branch to `B^k delta_m` has coefficient `(9/4)^k`. Letting L grow gives

\[
\|B^k\|_{\ell^1(n^p)\to\ell^1(n^p)}
\ge (3/2)^{(2-p)k}.
\]

So the spectral radius lower bound exceeds one for every p<2, including every polynomially weighted ell^1 space supplied by the envelope. An averaging calculation over residues that predicts contraction misses these arbitrarily long exceptional branches.

In the normalized bounded-coefficient formulation `(Qf)(n)=q(n)f(T(n))`, the operator and every power have norm one: any fixed finite number of factors q can be made arbitrarily close to one by taking the starting integer sufficiently large. There is no uniform killing rate available from this normalization alone.

## 6. What remains genuinely open in this attack

A successful analytic proof would have to exclude the exact geometric coefficient repetitions (7), for example by deriving a genuinely new boundary regularity theorem strong enough to put D^2H in H^1. The hypotheses currently available allow those repetitions and do not supply that regularity. Positivity, absolute summability of H, the standard first-derivative Sobolev bound, and the mixed differentiated equation do not close the gap by any argument established here.

No separate dilation equation, finite singularity set, automaticity, meromorphic continuation, or endpoint boundary regularity was assumed.
