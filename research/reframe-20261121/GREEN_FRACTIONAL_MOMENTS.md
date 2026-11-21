# Fractional Haar moments of the exact square-pressure Green function

**Status: PROPOSED, complete paper proof; not Lean-formalized.** The compact
Green function has every positive moment below one, and no moment at or
above one. This supplies genuine integrability for the compressed Green
profile in [GLOBAL_MASS.md](GLOBAL_MASS.md). It also rules out its
superharmonicity almost everywhere on the ternary space. The eventual
inequality on positive ordinary integers remains unresolved.

## 1. The compact operator and its exact word domains

Let `X=Z_3^times`, and let `mu` be additive Haar measure restricted to
`X`, normalized so `mu(X)=1`. For `a>=1`, write

\[
R_a(u)=\frac{3u+1}{2^a},\qquad
E_a=R_a(X),\qquad
I_a(\zeta)=\frac{2^a\zeta-1}{3}\quad(\zeta\in E_a).
\]

The map `R_a` takes `X` into `X`. The domain condition is exactly
`2^a zeta mod9 in {4,7}`. The square-pressure operator is

\[
(P_2f)(\zeta)=
\sum_{a\ge1}\frac9{4^a}\mathbf1_{E_a}(\zeta)f(I_a\zeta).
\tag{F1}
\]

Define `F_q=P_2^q 1`, including `F_0=1`, and the extended nonnegative
Green function

\[
G(\zeta)=\sum_{q\ge0}F_q(\zeta).
\tag{F2}
\]

For a word `w=(a_1,...,a_q)` of positive exponents, put
`A_w=a_1+...+a_q`, `R_w=R_(a_1) o ... o R_(a_q)`, and `E_w=R_w(X)`.
The exact coefficient of this affine map is `3^q/2^(A_w)`. Consequently
the additive Haar scaling factor is `3^(-q)`. Since both the original
domain and its image lie in `X`, normalization of the restricted measure
cancels, giving

\[
\boxed{\mu(E_w)=3^{-q}.}
\tag{F3}
\]

More explicitly, `R_w(u)=b_w+3^q 2^(-A_w)u`, so `E_w` consists of the
two unit lifts in that affine residue cylinder at modulus `3^(q+1)`.
Every intermediate image is a unit, because each `R_a` preserves `X`.
Thus `E_w` is exactly the domain of the whole inverse word, with no omitted
intermediate legality condition.

Expanding `(F1)` gives

\[
F_q(\zeta)=
\sum_{w\in\mathbb N_{>0}^q}
\left(\frac{3^q}{2^{A_w}}\right)^2\mathbf1_{E_w}(\zeta).
\tag{F4}
\]

The word domains can overlap. No disjointness is asserted or used.
All terms are nonnegative; the coefficient sum at fixed `q` is finite,
so the expansion and subsequent integrations follow by monotone
convergence. Each `F_q` is a bounded continuous function.

## 2. The fractional-moment bound and its exact endpoint

**GF1.** For every `1/2<eta<1`, define

\[
\Lambda_{2\eta}=\frac{3^{2\eta-1}}{2^{2\eta}-1}.
\]

Then

\[
\boxed{
\int_X F_q^\eta\,d\mu\le\Lambda_{2\eta}^q,
\qquad
\int_X G^\eta\,d\mu\le\frac1{1-\Lambda_{2\eta}}<\infty.
}
\tag{F5}
\]

For `0<eta<1`, subadditivity `(sum b_i)^eta<=sum b_i^eta` and `(F3)`
give

\[
\begin{aligned}
\int F_q^\eta\,d\mu
&\le\sum_w
 \left(\frac{3^q}{2^{A_w}}\right)^{2\eta}\mu(E_w)\\
&=3^{(2\eta-1)q}
 \left(\sum_{a\ge1}2^{-2\eta a}\right)^q
=\left(\frac{3^{2\eta-1}}{2^{2\eta}-1}\right)^q.
\end{aligned}
\]

For `beta=2eta` in `(1,2)`, strict concavity of `x^(beta-1)` at
`2=(1+3)/2` gives `2^beta>1+3^(beta-1)`. Therefore `Lambda_(2eta)<1`.
Apply subadditivity again to `(F2)`, and sum the geometric bound to prove
the second assertion of `(F5)`.

Since `G>=1`, every smaller positive power is bounded by any chosen
power `eta` in `(1/2,1)`. Thus

\[
\int G^\theta\,d\mu<\infty\qquad(0<\theta<1).
\tag{F6}
\]

The endpoint is exact. Without applying subadditivity, `(F3)`--`(F4)` give

\[
\int F_q\,d\mu
=\left(\frac3{4-1}\right)^q=1.
\]

Tonelli then gives `integral(G)=infinity`. Since `G>=1`, all its powers
with exponent at least one also have infinite integral. In particular,

\[
\boxed{\int G^\theta\,d\mu<\infty
\quad\Longleftrightarrow\quad0<\theta<1
\qquad(\theta>0).}
\tag{F7}
\]

The function `G` is finite almost everywhere, despite its infinite first
moment. The moment estimate also gives the explicit tail bound
`mu{G>R} <= R^(-eta)/(1-Lambda_(2eta))` for every exponent in `(F5)`.

## 3. The compressed function cannot be superharmonic almost everywhere

**GF2.** If `f>=0` lies in `L^1(mu)` and `P_2 f<=f` almost everywhere,
then `f=0` almost everywhere. In particular, for every `0<theta<1`,

\[
\mu\{\zeta:P_2(G^\theta)(\zeta)>G(\zeta)^\theta\}>0.
\tag{F8}
\]

Here all statements are made up to null sets; `(F6)` makes the compressed
function an ordinary finite `L^1` class.

First, the single-branch change of variables has factor `1/3`, giving

\[
\int P_2 f\,d\mu=
\sum_{a\ge1}\frac9{4^a}\frac13\int f\,d\mu
=\int f\,d\mu
\tag{F9}
\]

for every nonnegative measurable `f`. Thus `P_2` preserves nonnegative
`L^1` mass. Second, `(F5)` implies `F_q -> 0` in measure.

For any nonnegative `f` in `L^1`, truncate it as
`f=min(f,M)+(f-M)_+`. Positivity gives

\[
P_2^q\min(f,M)\le M F_q,
\qquad
\|P_2^q(f-M)_+\|_1=\|(f-M)_+\|_1.
\]

For every `epsilon>0`, Markov's inequality therefore implies

\[
\limsup_{q\to\infty}\mu\{P_2^q f>\varepsilon\}
\le\frac2\varepsilon\|(f-M)_+\|_1.
\]

Letting `M` tend to infinity proves `P_2^q f -> 0` in measure. If
`P_2f<=f` almost everywhere, `(F9)` forces equality almost everywhere;
iteration and convergence in measure then force `f=0`. Applying this to
the nonzero integrable function `G^theta>=1` proves `(F8)`.

This is compatible with `P_2G=G-1`: the uncompressed `G` has infinite
first moment, so it lies outside the hypothesis of GF2. It is also
compatible with preservation of `L^1` mass: convergence in measure here
is not convergence in `L^1`.

## 4. Exact relation to positive ordinary sources

For a positive odd integer `t` with `3` not dividing `t`, each legal
inverse step `I_a(t)` is a positive odd integer. The unit guard is
precisely the domain condition in `(F1)`. Inductively, the compact finite
columns agree exactly with the ordinary columns:

\[
F_q(t)=\sum_{\substack{n>0\text{ odd},\ 3\nmid n\\U^q(n)=t}}
J_q(n)^2,
\qquad G(t)=G_2(t).
\tag{F10}
\]

These are equality statements at the specified ordinary integers, not
distributional approximations. The independent first-hit/cycle estimate
in `GLOBAL_MASS.md` `(G10)` proves `G_2(t)<infinity` for **every** such
ordinary `t`, including periodic targets. Its source is PR169,
`6cb9bfdc828f91576066b0e4a099d47d8144e915`,
`research/certificate-renewal-20261121/FIXED_ENDPOINT_SUMMABILITY.md`,
ES1, with the same elementary argument at exponent two.

The two finiteness statements have different quantifiers and measures.
The ordinary bound sums actual histories entering one fixed integer.
The fractional estimate integrates a compact profile against Haar
measure. Neither assertion treats Haar measure as the distribution of
the original positive sources after transport.

## 5. What this settles about the remaining column inequality

For every compressed exponent below one, GF2 rules out the compact
almost-everywhere inequality `P_2(G^theta)<=G^theta`. Thus such a global
compact inequality cannot supply the remaining ordinary contraction.

It does **not** settle whether the same inequality could hold at all
sufficiently large positive ordinary targets for an exponent in

\[
\frac{2\log(3/2)}{3\log3}\le\theta<\frac13.
\]

Those targets form a countable Haar-null subset. The function `G` is
unbounded (already `F_q(-1)>=(9/4)^q`), and its compressed powers are not
the bounded continuous profiles covered by GM1. The positive-measure
violation in `(F8)` cannot be transferred to this countable subset merely
by density or by the equality `(F10)`.

One precise sufficient transfer would be the ordinary sampling limit

\[
\frac1{|\mathcal O^*\cap[1,X]|}
\sum_{\substack{t\le X\\t\in\mathcal O^*}}
\bigl(P_2(G^\theta)(t)-G(t)^\theta\bigr)_+
\longrightarrow
\int\bigl(P_2(G^\theta)-G^\theta\bigr)_+\,d\mu.
\tag{F11}
\]

The right side is finite and strictly positive by `(F6)`, `(F8)`, and
`(F9)`. An eventual ordinary contraction would make the left side tend
to zero, so `(F11)` would refute it. Fixed finite word sums have the
necessary residue averaging; passing to this unbounded all-depth
function needs new control of the Green tails under ordinary sampling.
The Haar fractional moments proved here do not supply that control.

The positive conclusion of this note is the exact compact moment
threshold, its quantitative bound, and the resulting exclusion of all
nonzero `L^1` superharmonic compact densities. The ordinary eventual
column inequality and full Collatz closure remain open.
