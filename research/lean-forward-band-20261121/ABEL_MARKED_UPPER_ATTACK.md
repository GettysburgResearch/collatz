# A global sublinear bound before the critical Abel limit

**Status: written upper estimate, derived below from exact ordinary word
arithmetic and the geometric exponent law. Not Lean-formalized. Full Collatz
and the critical marked-band upper bound remain OPEN.**

This is a focused continuation of the ordinary inverse-envelope attack. It
does not assume that a generic harmonic function has the desired growth.
In particular, the atomic examples in `HARMONIC_RAY_OBSTRUCTION.md` make that
inference invalid. The target here is the specific Abel family used in
`GLOBAL_RENEWAL_ATTACK.md`, before taking its critical limit.

## 1. An actual upper theorem for the Abel family

For a positive odd ordinary target `q`, use the exact density

\[
D_s(q)=3^s\Pr(X_s\equiv q\pmod{3^s}),\qquad D_0(q)=1,
\]

with independent positive geometric letters `Pr(a=e)=2^(-e)`. Let
`A_s=a1+...+as`, and define

\[
F_\rho(q)=(1-\rho)\sum_{s\ge0}\rho^sD_s(q),\qquad0<\rho<1.
\]

Put

\[
R=64/3,\qquad r=64/81.
\]

For every `1/3<rho<1`, set

\[
\theta_\rho=1+\frac{\log\rho}{\log3}\in(0,1),\qquad
A=1+\frac{\log R}{\log3},
\]

\[
B_\rho=2+\log R+
 \frac{3\rho(1-\rho)}{3\rho-1}+
 \frac{\rho(1+\log R)}{1-\rho}.
\]

Then, uniformly over positive odd integers `q`,

\[
\boxed{F_\rho(q)\le
q^{\theta_\rho}\bigl(B_\rho+A\log q\bigr).}
\tag{AU}
\]

In particular, **every fixed subcritical Abel approximant is globally
sublinear**:

\[
\frac{F_\rho(q)}q\longrightarrow0
\qquad(q\to\infty,\ \rho<1\text{ fixed}).
\tag{AS}
\]

The estimate includes periodic targets. It does not require knowing which
positive cycles exist, and no cycle-dependent constant appears.

For completeness, the elementary bound `D_s<=3^s` directly gives
`F_rho<=(1-rho)/(1-3rho)` for `rho<1/3`. At `rho=1/3`, the proof below
gives `F_rho(q)=O(1+log q)`, again sublinear.

## 2. The ordinary-source tail estimate

Fix an integer `L>=0`. At depth `s`, retain only words with `A_s<=6s`.
Every retained word ending at `q` has one positive odd ordinary source `n`,
with

\[
q=\omega_w n+\beta_w,\qquad
\omega_w=3^s2^{-A_s}\le q/n,
\qquad n\le qR^s.
\tag{2.1}
\]

For a fixed source `n` and a fixed odd depth `s`, there is at most one such
word: the actual odd trajectory determines its complete valuation word.
A periodic target can allow that source at several depths. We deliberately
overcount it at **every eligible depth**, so no disjoint-depth assertion is
needed.

Let `J_L(n)` be the least integer `s>=L` such that `n<=qR^s`. Nonnegative
summation and `(2.1)` give

\[
\begin{aligned}
&(1-\rho)\sum_{s\ge L}\rho^s D_s^{\,A\le6s}(q)\\
&\quad\le(1-\rho)\sum_{n\ge1}\frac qn
 \sum_{\substack{s\ge L\\n\le qR^s}}\rho^s
 =q\sum_{n\ge1}\frac{\rho^{J_L(n)}}n.
\end{aligned}
\tag{2.2}
\]

This is where discounting removes the potentially large cycle factor.
The geometric repetition bound is `1/(1-rho)` even if a cycle multiplier
is very close to one, and the prefactor `1-rho` cancels it.

The sources `n<=qR^L` contribute at most

\[
q\rho^L\bigl(1+\log q+L\log R\bigr).
\]

For each `j>=1`, the sources in
`qR^(L+j-1)<n<=qR^(L+j)` have `J_L(n)=L+j`. Their reciprocal sum is at
most `log R+1`; this follows from the integral bound for harmonic sums,
and the lower interval endpoint is at least one. Summing these intervals
proves

\[
\boxed{
(1-\rho)\sum_{s\ge L}\rho^s D_s^{\,A\le6s}(q)
\le q\rho^L\left(
1+\log q+L\log R+
\frac{\rho(1+\log R)}{1-\rho}\right).}
\tag{2.3}
\]

For the omitted clocks, the same elementary geometric moment estimate as
the companion Cesaro proof gives

\[
D_s^{\,A>6s}(q)\le3^s\Pr(A_s>6s)\le r^s.
\]

Indeed `E[(3/2)^a]=3`, so Markov's inequality yields
`3^s * 3^s * (3/2)^(-6s)=(64/81)^s`. Therefore the discarded part of
the Abel tail is at most

\[
\frac{(1-\rho)(\rho r)^L}{1-\rho r}.
\tag{2.4}
\]

Equations `(2.3)`--`(2.4)` already prove that the Abel series is finite
for every positive odd ordinary argument, uniformly without a cycle
classification.

## 3. Optimizing the depth split

The early depths satisfy

\[
(1-\rho)\sum_{0\le s<L}\rho^sD_s(q)
\le(1-\rho)\sum_{0\le s<L}(3\rho)^s.
\tag{3.1}
\]

Take `L=ceil(log(q)/log(3))`. For `rho>1/3`,

\[
q\rho^L\le q^{\theta_\rho},\qquad
(3\rho)^L\le3\rho\,q^{\theta_\rho},\qquad
L\le\frac{\log q}{\log3}+1.
\]

Insert these inequalities into `(2.3)` and `(3.1)`. The geometric sum in
`(3.1)` is at most
`3rho(1-rho)q^theta/(3rho-1)`. The term `(2.4)` is at most one, which is
at most `q^theta`. Collecting constants yields exactly `(AU)`.
The case `q=1` has `L=0`; the same upper bound remains valid.

For `rho=1/3`, the early-depth bound is `(2/3)L`, while `q rho^L<=1`.
Equations `(2.3)`--`(2.4)` give the logarithmic bound stated above.

## 4. What happens as the discount approaches one

The rate is explicit. On `1/2<=rho<1`, for an absolute constant `C`,

\[
\frac{F_\rho(q)}q
\le C\left(\frac1{1-\rho}+\log q\right)
 \exp\!\left(-\frac{(1-\rho)\log q}{\log3}\right).
\tag{4.1}
\]

This uses `-log rho>=1-rho` and the displayed formula for `B_rho`.
Consequently there are near-critical diagonals with a genuine sublinear
bound. For example, for any fixed `K>log3`, take

\[
\rho(q)=1-K\frac{\log\log q}{\log q}
\]

at sufficiently large `q`. Then `(4.1)` gives

\[
F_{\rho(q)}(q)/q
=O\bigl((\log q)^{1-K/\log3}\bigr)\longrightarrow0.
\tag{4.2}
\]

This does **not** prove sublinearity of the critical Abel limit. The
construction of that limit first takes `rho->1` at each fixed ordinary
argument. The coefficient `B_rho` diverges and `theta_rho` tends to one.
Neither `(AU)` nor `(4.2)` is uniform in the order of limits required by
that construction.

## 5. Why this upper bound does not yet close the marked potential route

The exact resolvent equation is

\[
F_\rho(q)=(1-\rho)+\rho(PF_\rho)(q).
\tag{5.1}
\]

Thus `F_rho` need not be excessive for `P`. In fact,
`PF_rho=(F_rho-(1-rho))/rho`; whenever `F_rho(q)>1`, its value under `P`
is larger than itself.

The uniform atom floor gives `F_rho(b)>=c0 rho^s0` at unit parents.
Use the distinct short unit parent from `InverseDensityPotential.lean`.
For an actual odd unit edge `n->q` with `2^e q=3n+1`, `(5.1)` yields

\[
F_\rho(q)\ge\rho\frac3{2^e}F_\rho(n)+c_\rho,
\qquad
c_\rho=(1-\rho)+\rho\frac{3c_0\rho^{s_0}}{64}>0.
\tag{5.2}
\]

Writing `H_rho(n)=F_rho(n)/n`, the resulting drift is

\[
H_\rho(q)-H_\rho(n)
\ge-(1-\rho)H_\rho(n)
 +\frac{c_\rho-\rho H_\rho(n)/2^e}{q}.
\tag{5.3}
\]

The first term is the precise loss absent from the critical harmonic
argument. For fixed `rho<1`, the sublinear bound `(AU)` does not make that
loss smaller than `c_rho/q`. The fixed positive threshold barrier used in
`MarkedDensityPotential.lean` therefore does not follow.

Likewise, defining a function by the diagonal choice in `(4.2)` changes
the discount between neighboring ordinary states. It is no longer the
fixed-parameter resolvent in `(5.1)`. No transfer estimate comparing these
different parameters has been proved.

The least excessive majorant and its atomless harmonic part, constructed
in `MINIMAL_ENVELOPE_ATOM_REMOVAL.md`, remove the generic atomic examples.
They do not automatically inherit `(AU)`: a subcritical resolvent is not
an excessive majorant for the undiscounted operator. Their proved decay
on the whole ancestor set of each fixed target still has target-dependent
cutoffs. A hypothetical escaping orbit changes that target as it moves
forward, and marked cofinality does not produce one common ordinary root
for all those future marked states.

## Outcome of this focused attack

The specific Abel family has a global, quantitative sublinear upper bound
at every subcritical parameter, with no unknown-cycle factor. The exact
remaining issue is passage to an appropriate critical excessive or
harmonic envelope while retaining a marked-band upper bound. Neither
pointwise finite atom values, fixed-target atomlessness, nor the
near-critical diagonal above supplies that uniform passage. The full
marked sublinearity assertion remains unproved.
