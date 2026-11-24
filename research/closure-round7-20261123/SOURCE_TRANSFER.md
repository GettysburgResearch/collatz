# The actual forward law separates from the ordinary inverse entrance law

23 November 2026. Parent checkpoint:
`e4367dd2c4406c1041e66d82dfba822908747fa3`.

**Status: PROPOSED written actual-source comparison theorem, using the
exact source-qualified entrance-law construction and the earlier proved
whole-orbit count. No closing collision upper, sibling-pressure lower
bound, escaping ordinary orbit, or full Collatz proof is constructed.**

The newly advanced PR177 constructs an inverse sampler whose terminal
ordinary source law converges in total variation. The collision programme
instead uses empirical laws of the actual forward orbit. These are two
different laws on the same component. This note quantifies their
separation without substituting an abstract probability model for either:
their ordinary total variation tends to its maximum at a power rate,
their relative entropy diverges at an explicit rate, and their finite
residue projections remain maximally separated on the very scales where
ordinary-height packing makes the forward collision small.

This result blocks a direct use of the new entrance-law convergence as
the missing forward-law convergence estimate. It does not refute the
entrance-law theorem or the possibility of an additional arithmetic
transport with its full cost paid.

## 1. Exact objects and frozen sources

Use the odd accelerated map

\[
U(q)=\frac{3q+1}{2^{v_2(3q+1)}}.
\]

Work conditionally on one hypothetical escaping component `E` of positive
odd ternary units. Fix its injective actual ray `q_i=U^i(q_0)`. The two
laws below retain this same component and this same original source.

The inspected PR177 head is
`3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`. Its path
`research/lean-exact-witness-global-20261121/profound-step-20261123/pressure/ORDINARY_ENTRANCE_LAW.md`,
blob `5779df91e1b5daa5a47e56a668424d106823340c`, supplies EL1--EL5:

\[
r(n)=\frac1n\prod_{k\ge0}\frac{3U^kn}{3U^kn+1},\qquad
0<c_*/n\le r(n)\le1/n,
\]
\[
D_j=\{n\in E:U^kn=q_j\text{ for some }k\ge0\},\qquad
A_j=\sum_{n\in D_j}r(n)^s,\qquad s>1,
\]
\[
\boxed{\nu_j(n)=\frac{r(n)^s1_{D_j}(n)}{A_j}.}
\tag{1}
\]

This is the exact terminal-source law of the full inverse Green transform,
including its killing probability. Write `a=A_0>0`. The predecessor sets
increase and retain the original source, so

\[
0<r(q_0)^s\le a\le A_j\le M_s\le\sum_{n\ge1}n^{-s}<\infty.
\]

Their union is `E`, and the source proves

\[
\nu_j\longrightarrow\mu_s,
\qquad \mu_s(n)=r(n)^s/M_s,
\qquad M_s=\sum_{n\in E}r(n)^s<\infty,
\]

in ordinary total variation. The sampler's terminal source is an ordinary
integer; it is not the forward empirical root or its stationary residue
limit. The formulas and killing normalization were read in full. The
source's potential-transform literature input is credited there, and no
additional Markov-boundary theorem is imported in this note.

The forward empirical law is

\[
\boxed{\pi_N=\frac1N\sum_{i=0}^{N-1}\delta_{q_i},}
\qquad H_N=\max_{0\le i<N}q_i,
\qquad N\ge1.
\tag{2}
\]

Every state is retained and the states are distinct. In particular
`H_N>=N`. Total variation is half the `ell^1` distance, equivalently the
supremum of event-probability differences.

The local source
`research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, blob
`6881dc864f3b586958bd46d5c38b1c2524008565` at the parent checkpoint,
proves for the same entire injective odd orbit

\[
F(X):=\#\{i\ge0:q_i\le X\}
\le C\frac{X^\theta}{\sqrt{1+\log X}},\qquad X\ge1,
\tag{3}
\]
\[
\theta=H_2(\log_3 2)=0.949955527188\ldots<1,
\]

with an absolute `C>=1`. Its complete proof, including arbitrarily
separated visits, was read. The exact entropy expression defines theta;
no rounded exponent enters the claims. Natural logarithms are used below.
The bound applies to the injective forward orbit, not to `D_j` or `E`.

## 2. Maximal ordinary separation, uniformly over the inverse root

**R7-ST-1.** For every integer `X>=1`, every `N>=1`, and every `j>=0`,

\[
\boxed{
\operatorname{TV}(\pi_N,\nu_j)
\ge1-\frac{X^{1-s}}{(s-1)a}
       -\frac{C X^\theta}{N\sqrt{1+\log X}}.
}
\tag{4}
\]

**Proof.** The exact inverse law and the full ordinary tail give

\[
\nu_j\{n>X\}
\le\frac1a\sum_{n>X}n^{-s}
\le\frac{X^{1-s}}{(s-1)a}
\tag{5}
\]

by the integral bound for the decreasing tail beyond the integer X.
The forward mass on the same ordinary initial interval is at most
`F(X)/N`. Test total variation on `[1,X]` and use (3). This proves (4)
for every inverse root `j`, without a convergence rate for `nu_j` and
without requiring `N<=j+1`. All possible inverse sources above X remain
in the explicit tail cost. \(\square\)

One obtains a sharper rate by retaining the exact forward support in
the overlap. For `N>=max(1,a)`, put `R=(N/a)^(1/s)>=1`. Then, uniformly
for all `j>=0`,

\[
\boxed{
1-\operatorname{TV}(\pi_N,\nu_j)
\le \frac{Cs}{s-\theta}\,
\frac{a^{-\theta/s}N^{\theta/s-1}}{\sqrt{1+\log R}}
=O_{s,q_0}\!\left(
\frac{N^{-(1-\theta/s)}}{\sqrt{1+\log N}}\right).
}
\tag{6}
\]

**Proof of (6).** The states in the forward prefix are distinct, hence

\[
1-\operatorname{TV}(\pi_N,\nu_j)
=\sum_{i<N}\min\{1/N,\nu_j(q_i)\}
\le\sum_{i\ge0}\min\{1/N,1/(a q_i^s)\}.
\]

For each positive q, the minimum in this sum is exactly

\[
\frac{s}{a}\int_R^\infty 1_{q\le t}\,t^{-s-1}\,dt.
\]

Summing these nonnegative integrals and then applying (3) gives

\[
\begin{aligned}
\sum_{i\ge0}\min\{1/N,1/(a q_i^s)\}
&=\frac{s}{a}\int_R^\infty F(t)t^{-s-1}\,dt\\
&\le\frac{Cs}{a\sqrt{1+\log R}}
       \int_R^\infty t^{\theta-s-1}\,dt\\
&=\frac{Cs}{a(s-\theta)}
       \frac{R^{\theta-s}}{\sqrt{1+\log R}}.
\end{aligned}
\]

Here `s>1>theta` makes the integral finite. Substituting R proves
(6). The tail in this calculation runs over the same actual forward
orbit, not over the inverse component. \(\square\)

For example, with `s=2`, the power is exactly `1-theta/2`.
The same bound holds with `mu_s` in place of `nu_j`, because its
normalizer is at least a and it has the same pointwise weight upper.
The new estimate concerns separation between these actual ensembles;
it is not a rate for the convergence of the forward law to its own
stationary residue limit.

## 3. The separation survives growing residue resolution

Ordinary total variation can decrease after projection. The previous
section alone therefore gives no lower bound at a fixed modulus. The
full ordinary quotient supplies the required separate estimate.

Let `Q>=1` be an integer modulus and let `1<=X<Q` be an integer. Put

\[
L_{N,Q}=\frac{N}{\lfloor H_N/Q\rfloor+1}.
\]

**R7-ST-2.** For all `j>=0`,

\[
\boxed{
\operatorname{TV}(\pi_N\bmod Q,\nu_j\bmod Q)
\ge1-\frac{X^{1-s}}{(s-1)a}-\frac{X}{L_{N,Q}}.
}
\tag{7}
\]

**Proof.** Take the residue set `R={1,...,X}` modulo Q. It consists of
X distinct classes. It contains the projection of every ordinary inverse
source at most X, so `nu_j(R)>=1-X^(1-s)/((s-1)a)` by (5). Each class
contains at most `floor(H_N/Q)+1` of the distinct actual forward states.
Counting all classes, with every quotient and every forward occurrence,
gives `pi_N(R)<=X/L_(N,Q)`. Their event-probability difference proves (7).
No distributional premise on the residues is used. \(\square\)

Since `H_N>=N`, one has `L_(N,Q)<Q`. For `L_(N,Q)>=2^s`, choose
`X=floor(L_(N,Q)^(1/s))`. This is a positive integer smaller than Q and
is at least half the displayed real power. Equation (7) gives the
explicit uniform bound

\[
\boxed{
1-\operatorname{TV}(\pi_N\bmod Q,\nu_j\bmod Q)
\le\left(1+\frac{2^{s-1}}{(s-1)a}\right)
L_{N,Q}^{-(s-1)/s}.
}
\tag{8}
\]

In particular, along any growing prefixes and any sequence of moduli
for which `H_N/Q_N=o(N)`, one has `L_(N,Q_N)->infinity`, and

\[
\operatorname{TV}(\pi_N\bmod Q_N,\nu_{j_N}\bmod Q_N)\longrightarrow1
\]

for **every** choice of inverse roots `j_N`. This includes ternary
moduli `Q_N=3^(m_N)`. It again holds for `mu_s` as well.

The same `L_(N,Q)` is the reciprocal of the finite collision-packing
upper in the preceding checkpoint. Thus, on the scales where that
packing upper tends to zero, these inverse endpoint laws and forward
laws approach maximal separation. Their identification cannot supply
the missing small-error collision transfer. A separate transport has
to change the law and account for that change.

This statement does not rule out a coincidence of fixed-modulus limits
in some different argument: fixed Q has `L_(N,Q)<Q`, and the hypothesis
of (8)'s vanishing error then fails. No fixed-modulus limit is exchanged
with a growing one.

There is also a direct collision distinction. The retained atom at the
original source gives `nu_j(q_0)>=r(q_0)^s/M_s=:b>0`, uniformly in j.
For every modulus Q, therefore,

\[
\sum_{u\bmod Q}(\nu_j\bmod Q)(u)^2\ge b^2.
\]

The same is true of `mu_s`. Consequently the ternary collision dimension
of each of these inverse laws is zero: the quotient of minus the log
collision by `m log 3` tends to zero as `Q=3^m` grows. This is a statement
about the inverse endpoint laws; it gives no collision dimension for the
forward stationary law. The atom's fixed ordinary identity and the full
normalizer are essential to this distinction.

## 4. A quantitative actual-source relative-entropy cost

Now require `j>=N-1`, so every `q_i` in the forward prefix is in `D_j`.
There are no zero reference probabilities on that prefix. The exact
relative entropy is

\[
\operatorname{KL}(\pi_N\Vert\nu_j)
=\log A_j-\log N-\frac{s}{N}\sum_{i<N}\log r(q_i).
\tag{9}
\]

**R7-ST-3.** There is a constant K depending only on `s,q_0` and the
absolute count constant C such that, for all `N>=1` and `j>=N-1`,

\[
\boxed{
\operatorname{KL}(\pi_N\Vert\nu_j)
\ge\left(\frac{s}{\theta}-1\right)\log N
 +\frac{s}{2\theta}\log(1+\log N)-K.
}
\tag{10}
\]

One may take

\[
K=\frac{s}{\theta}\left(\log C+\frac32\right)-\log a.
\]

**Proof.** Sort the N distinct actual forward states increasingly as
`n_1<...<n_N`. This changes no source or probability. Since they are
positive integers, `n_k>=k`. Equation (3) gives

\[
k\le C n_k^\theta/\sqrt{1+\log n_k},
\]

and therefore

\[
\log n_k\ge\frac1\theta
\left[\log k-\log C+\frac12\log(1+\log k)\right].
\tag{11}
\]

The elementary integral bound for `log(N!)` yields

\[
\frac1N\sum_{k=1}^N\log k\ge\log N-1.
\]

Also, for `1<=k<=N`,

\[
\log(1+\log k)
\ge\log(1+\log N)-\log(N/k).
\]

For example this follows by integrating the derivative
`1/(x(1+log x))<=1/x` from k to N. Averaging and using the preceding
factorial bound gives

\[
\frac1N\sum_{k=1}^N\log(1+\log k)
\ge\log(1+\log N)-1.
\]

Average (11), use `r(q_i)<=1/q_i` and `A_j>=a` in (9), and collect
the constants. This proves (10). \(\square\)

Replacing `A_j` by `M_s` gives the same lower bound for
`KL(pi_N||mu_s)`. The inequality concerns the actual forward trial
law, so choosing it in the new inverse free-energy variational formula
does not have a bounded entropy penalty. Its signed arithmetic transport
cost must still be paid; (10) alone does not bound that signed term or
the optimal variational value over other finite trials.

## 5. Actual address repetition does not stabilize the balanced anchor

The complete balanced compiler in PR177 compares roots `q` and
`S(q)=64q+21` using the same parent colour and canonical exponent-lift
index. Its source is
`research/lean-exact-witness-global-20261121/universal-step-20261123/escape/BALANCED_INVERSE_TRANSPORT.md`,
blob `8eb631c4c7718c0013027b8cbab72a5bc76f1dda`, read at the same
head `3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`.

Here is an all-depth control on actual positive ordinary paths. Start
with roots 1 and 85 and repeat the address `(colour 1, lift index 0)`.
The original root stays at 1: its exponent is two and `(4*1-1)/3=1`.
The transported root evolves by

\[
y_0=85,\qquad
y_{k+1}=\frac{2^{e_1(y_k)}y_k-1}{3},
\]

where, for `y==1 mod3`, the actual canonical exponents are

\[
e_1(y)=
\begin{cases}
2,&y\equiv1\pmod9,\\
6,&y\equiv4\pmod9,\\
4,&y\equiv7\pmod9.
\end{cases}
\]

The table gives an odd positive integer `y_(k+1)==1 mod3`, and its
exact forward valuation is `e_1(y_k)`. Thus every step is a literal
ordinary inverse step, not a completion. Since every exponent is at
least two,

\[
3(y_{k+1}-1)=2^{e_1(y_k)}y_k-4\ge4(y_k-1).
\]

Induction proves

\[
\boxed{y_k\ge1+84(4/3)^k\qquad(k\ge0).}
\tag{12}
\]

The unprimed branch address has one repeated symbol and one repeated
ordinary source; its transported ordinary state grows exponentially.
Consequently finite address memory does not by itself give a bounded
transported anchor. A proposed finite-state argument must retain enough
of the changing ordinary root to control the exponent table.

This is a **periodic ordinary control**, not an escaping counterexample.
The repeated unprimed source occurs at different path depths. It cannot
be inserted into the injective-ray law (1) as distinct ordinary atoms,
and it does not refute a pressure comparison specifically conditioned
on an escaping component. The exact same-source arithmetic needed to
bound `Phi_j(n)` moderately along an injective ray remains unproved.

## 6. Evidence and the remaining closing step

The proof of (4)--(10) uses only the explicit actual entrance weights,
normalizer lower bound, ordinary tail sum, retained full quotient, and
the proved count for the same injective orbit. The infinite entrance
construction remains source-qualified at its exact PR177 path; no
additional uniformity or invariance is inferred from it.

The companion `transfer_controls.py` checks finite ordinary identities
and the periodic compiler control with exact rational arithmetic. Its
finite inverse laws are explicitly truncated laws on actually enumerated
ordinary ancestors. They are not advertised as the infinite law of an
escaping component, and no finite check verifies the asymptotic rates.
No new Lean wrapper is claimed for the analytic total-variation or
relative-entropy statements. The earlier collision module already
formalizes the source/quotient recovery used in (7).

Executed controls: both `python -X utf8 -B` and `python -O -X utf8 -B`
on the companion file passed with identical deterministic output:
7,621 exact checks, 237 distinct ordinary sources, 35 finite inverse laws,
733 projected cutoff cases, and the compiler control through depth 128.
The finite layer-cake representation was checked in 12 cases. The
transported compiler value at depth 128 has 336 bits and accumulated
signed exponent displacement 276. These are finite control receipts;
the all-depth assertion (12) is justified by the displayed induction.

The main pressure target is still an absolute transported ordinary mass
lower bound, or equivalently a paid free-energy trial for the unchanged
sibling. The collision target still needs a rate for the actual forward
law relative to its own limit. The new inverse entrance law supplies
neither through direct identification: the exact comparisons above show
the scale and entropy costs of that attempted identification.
