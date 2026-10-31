# Contact transport: infinite obstructions and an exact occupation lift

**Status: PROPOSED, with explicit proofs and bounded exact replay. Collatz remains open.**
This note continues PR142 at `d0f48c472d45a336e9083b37b45e1a8d39a2cf16`.
It uses that packet's definitions and ORD-001--005. The inherited power-of-three
spike is from PR106 at `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`.
No external priority claim or proof-assistant certification is made.

## 1. Objects and the result of this pass

Let T be the shortcut map, S its version absorbed at one, and

\[
g(d)=d^2/3^{v_3(|d|)},\qquad
\Gamma(n)=\min\bigl(g(n),\{4^j g(T^j n-n):j\ge1,
T^j n\ne n\}\bigr),\quad n\ge2,
\]

with Gamma(1)=0. Let

\[
\Phi(n)=\max_{j\ge0}\lceil\Gamma(S^j n)/3^j\rceil,
\qquad C=\{n\ge2:\Phi(n)=\Gamma(n)\}.
\]

The known facts used here are

\[
n\le\Gamma(n)\le\Phi(n)\le(n+1)^2,\quad
\Phi(n)=\max(\Gamma(n),\lceil\Phi(Sn)/3\rceil),
\]

and, at a noncontact n,

\[
\Phi(Sn)-1\ge3(\Phi(n)-1).                 \tag{1}
\]

Every source reaches C or one in a proved finite time. Write R(x) for the
first positive-time contact return from x in C, killed on hitting one, and
r(x) for its literal shortcut clock. K is shortcut mass pushforward on
{2,3,...}, killed at one, and K_C is contact-return mass pushforward on C.

The main conclusions are:

* Positive Phi moments, although preserved by one shortcut step, can become
  infinite after **one contact return**. This persists after killing any
  fixed finite set.
* An explicit infinite family of **odd, nonmultiples of three** gives an
  expanding contact-to-contact edge. It rules out every positive summable
  weight eventually of the form `n^a Phi(n)^(-s) h(v2(n),v3(n))`, s>0,
  even after arbitrary finite corrections and finite terminal-core changes.
* There is nevertheless an exact finite, computable **occupation lift** of
  contact data. It is invariant at every noncontact state; its entire
  transport residual lies on C. Its exact summability domain is a clock
  moment, and explicit endpoint-moment bounds account for actual transport.

These statements do not rule out residue-dependent weights, other arithmetic
features, or a successful physical merger. They identify a real failure of
the previous rank-moment domain and give a constructive replacement interface.

## 2. CT-001: unbounded moment amplification on contact return

For every p>0 and every finite terminal set F containing one, the contact
return killed on first entering F is unbounded on the weighted mass space

\[
\|f\|_{p,\Phi}=\sum_{x\in C\setminus F}\Phi(x)^p|f(x)|.
\]

There is a nonnegative full-support f in this space whose image has infinite
Phi^p moment. Likewise, for every s>0, the row ratios
`K_C(Phi^(-s))(y)/Phi(y)^(-s)` are unbounded even after any finite changes
to the weight or terminal set.

### Proof

Use m=3^h for h sufficiently large. The inherited spike gives

\[
\Gamma(m)=m,\qquad \Phi(m)>m^\kappa/3,
\quad \kappa=2\log4/\log12>1.              \tag{2}
\]

Thus m is noncontact. Let r be the least positive integer such that
x=2^r m is contact. This r always exists. Otherwise inverse Bellman identities
would give `Phi(2^j m)=ceil(Phi(m)/3^j)` for every j, eventually equal to one,
contrary to properness. The same argument gives a finite effective search.

Since x is contact,

\[
\Phi(m)\le3^r\Phi(x)=3^r\Gamma(x)
\le3^r g(x)=12^r m.
\]

Consequently

\[
r>\frac{(\kappa-1)\log m-\log3}{\log12}\longrightarrow\infty. \tag{3}
\]

All the r states x/2,...,m are noncontact. Let y=R(x); its clock k=r(x)
is at least r+1. This return cannot be killed at one: its preceding state
would be the contact state two, so an earlier contact return would already
have occurred. Iterating (1) from u=x/2 until y gives

\[
\Phi(y)-1\ge3^{k-1}(\Phi(u)-1)
\ge3^r(2^{r-1}m-1).
\]

Since `Phi(x)<=4^r m` and u>=3,

\[
\boxed{\frac{\Phi(y)}{\Phi(x)}>
\frac13(3/2)^r\longrightarrow\infty.}      \tag{4}
\]

Every state z after the initial x on this whole return has
`Phi(z)>=Phi(u)>=m`. Hence `z>=sqrt(m)-1`. The initial x is at least m.
The entire return therefore avoids any prescribed finite terminal set once
h is large enough; this is not merely an endpoint avoidance argument.

Choose distinct sources x_j with the ratio in (4) at least `2^(2j/p)` and
set `f(x_j)=2^(-j)Phi(x_j)^(-p)`. The input Phi^p moment is finite, while
the output moment is at least `sum_j 2^j`. Positivity handles coincident
endpoints without cancellation. Adding `2^(-n)Phi(n)^(-p)` at every live
contact makes the mass full support without changing either conclusion.

For the inverse weight, the single predecessor x contributes the ratio
`(Phi(y)/Phi(x))^s`; (4) proves unboundedness. All relevant states escape
every finite patch. QED.

**Scope.** The sources in this particular proof are even, so this argument
alone would not exclude an odd contact section. The next theorem supplies
an independent obstruction entirely on odd sources coprime to three.

## 3. CT-002: an explicit expanding odd contact family

For every integer k>=12, put

\[
n_k=243\,4^k+115,\qquad
y_k=T(n_k)=\frac{3n_k+1}{2}
          =\frac{729}{2}4^k+173.
\]

Both numbers are odd and coprime to three. They satisfy the exact formulas

\[
\boxed{\Gamma(n_k)=\Phi(n_k)=\frac{(n_k+5)^2}{3},\qquad
\Gamma(y_k)=\Phi(y_k)=\frac{(y_k+1)^2}{3}.} \tag{5}
\]

Thus their contact return is a single shortcut step. Moreover

\[
\frac{y_k}{n_k}\to\frac32,\qquad
\frac{\Phi(y_k)}{\Phi(n_k)}
=\frac94\left(\frac{n_k+1}{n_k+5}\right)^2\to\frac94.
                                                        \tag{6}
\]

### 3.1 All prefix candidates, including the unbounded cutoff

The two finite ordinary templates are b=115 and b=173. Their trajectories
reach one in respectively 23 and 22 shortcut steps, with respectively 10
and 9 odd steps. Continue the templates through the 1,2 cycle. For each
prefix write

\[
T^j u=c_j u+\delta_j,\quad c_j=3^{q_j}/2^j,
\quad\delta_j=T^j b-c_j b
\]

whenever u has that template's first j parity bits. Set
`D_b=max_{j>=1}v3(|T^j b-b|)`. No displacement is zero: these b are not
on their terminal cycle. Direct finite arithmetic gives the following
certificate; the eventual 1,2 tail introduces no larger valuation.

| Template b | First hit of 1 | Odd count | D_b | Winning prefix | Minimum other leading coefficient, j=1,...,23 | Minimum other abs(c_j-1) | Maximum delta_j, j=1,...,23 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 115 | 23 | 10 | 3 | 3 | 1 | 5/32 | 97453/32768 < 3 |
| 173 | 22 | 9 | 4 | 1 | 25/27 | 1/4 | 47633/16384 < 3 |

Here the leading coefficient means

\[
a_j=\frac{(3^{q_j}-2^j)^2}{3^{v_3(T^j b-b)}}.
\]

For u=n_k its parity template is valid through L=2k steps and its difference
from 115 has v3=5. For u=y_k the corresponding length is L=2k-1 and its
difference from 173 has v3=6. Thus all displacement valuations through
these lengths equal those of their templates, since D_b is smaller.

At the winning prefixes the exact candidates are `(u+5)^2/3` for b=115
and `(u+1)^2/3` for b=173. All other j<=23 satisfy, since u>=240,

\[
4^j g(T^j u-u)
\ge(1-24/u)^2 a_j u^2
\ge\frac{81}{100}\frac{25}{27}u^2
=\frac34u^2>\frac{(u+5)^2}{3}.             \tag{7}
\]

The baseline g(u)=u^2 is also larger. For `24<=j<=L`, the templates are
already on the 1,2 cycle, `c_j<=1/2` and `0<=delta_j<=2`. Hence

\[
|T^j u-u|\ge u/4,\qquad
4^j g(T^j u-u)\ge\frac{4^j u^2}{16\cdot81}>u^2.\tag{8}
\]

It remains to exclude prefixes after the known parity word. Both sources,
at their respective L, reach the exact state

\[
T^L u=3^{k+4}+2.
\]

Only j<=floor(log_2 u) can improve the baseline. Such j beyond L satisfy
j-L<=7 for n_k and j-L<=9 for y_k: the exact logarithm floors are
2k+7 and 2k+8. We use the harmless larger gap 8 for n_k below; the
y_k denominator absorbs one additional factor 3/2. The elementary bound
`T(z)+1<=(3/2)(z+1)` therefore gives, in both cases,

\[
\frac{T^j u}{u}
\le B_k:=(3/2)^8\left[\frac13(3/4)^k+
                       \frac1{81}4^{-k}\right]<\frac12,
\quad k\ge12.                              \tag{9}
\]

The last inequality holds at k=12 by exact rational arithmetic, and both
terms decrease with k. Also `4^L>=2u` for k>=12. Since g(d)>=|d|,
every such long candidate is at least
`4^(L+1)u/2>u^2`. This covers the entire growing prefix cutoff and proves
the two Gamma identities. A finite sample of k is not being extrapolated.

### 3.2 The envelope does not replace these ranks

Write n=n_k. Along its first six states, the following are valid Gamma
upper bounds, supplied by the indicated actual-prefix candidates:

| Position j | Template state | Prefix used for the bound | Upper bound B_j(n) |
|---:|---:|---:|---|
| 0 | 115 | 3, exact above | (n+5)^2/3 |
| 1 | 173 | 1, exact above | 3(n+1)^2/4 |
| 2 | 260 | 3 | (5n+1)^2/16 |
| 3 | 130 | 3 | (5n+1)^2/64 |
| 4 | 65 | 3 | 9(n+13)^2/256 |
| 5 | 98 | 2 | 3(9n-11)^2/1024 |

All needed parities and valuations follow from `n=115 mod 2^24` and
`n=115 mod 243`. Direct quadratic comparisons, valid for n>=115, give

\[
B_j(n)/3^j\le B_0(n)\quad(1\le j\le4),\qquad
B_{j+1}(n)/3^j\le B_1(n)\quad(1\le j\le4).
\]

For positions j>=5 relative to each source u=n_k or u=y_k, the general envelope bound is at most
`(3/4)^5(u+1)^2 < (u+1)^2/3`. This is below the respective exact Gamma
value. Because those Gamma values are integers, ceiling does not spoil any
of the inequalities. The j=0 terms attain them. This proves (5). QED.

## 4. CT-003: no polynomial height/rank/valuation weight closes the rows

Fix s>0, a real a, and any strictly positive function
`h:N_0^2->R_{>0}`. A weight which, outside a finite set, equals

\[
w(n)=n^a\Phi(n)^{-s}h(v_2(n),v_3(n)),\qquad n\in C,             \tag{10}
\]

cannot be both summable and an inverse supersolution `K_C w<=w`.
This remains true after killing any fixed finite terminal set, and after
inducing further on odd contact states coprime to three.

**Proof.** Use (5). Both valuation pairs are (0,0), and n_k,y_k escape every
finite set. If a<2s, then

\[
\frac{w(n_k)}{w(y_k)}\longrightarrow(3/2)^{2s-a}>1.
\]

The one inverse predecessor n_k already violates the row inequality at y_k.
There are no interior states which could be removed by a finite terminal set
or by the indicated odd section. If a>=2s, (5) gives
`w(n_k)~3^s h(0,0)n_k^(a-2s)`, so the summands do not even tend to zero.
This contradicts summability. QED.

This theorem does **not** exclude dependence on full residues, winning-prefix
data, or other nonregular arithmetic features. A fixed valuation correction
is insufficient; it is not a proof that every computable positive weight fails.

## 5. CT-004: exact finite occupation lift

Let w be any finite-valued nonnegative weight on C. Its occupation lift is

\[
(Lw)(n)=\sum_{x\in C}w(x)
  \sum_{0\le j<r(x)}\mathbf1_{S^j x=n},\qquad n\ge2.          \tag{11}
\]

The endpoint is excluded, including when it is one. Then:

1. Every value in (11) is a **finite sum**, with complete finite enumeration.
2. `(Lw)|C=w`. If w is positive everywhere on C, then Lw is positive
   everywhere on {2,3,...}.
3. The exact residual identity is

\[
\boxed{(I-K)Lw=\iota_C(w-K_Cw),}                              \tag{12}
\]

   where iota_C extends contact data by zero. In particular `K Lw=Lw`
   at every noncontact state.
4. Its exact total mass is

\[
\boxed{\sum_{n\ge2}(Lw)(n)=\sum_{x\in C}r(x)w(x).}           \tag{13}
\]

Thus finite clock moment is necessary and sufficient for summability.

### Complete finite enumeration

If n is contact, only the arc starting at n contributes. Otherwise explore
its shortcut predecessors backward, stopping whenever a contact is reached.
At a noncontact predecessor z, Bellman gives

\[
\Phi(z)=\lceil\Phi(Sz)/3\rceil<\Phi(Sz).
\]

Consequently every branch stops within `ceil(log_3 Phi(n))` levels. The same
height and Fibonacci width bounds as ORD-005 apply to this noncontact target:
at depth d, every tested source is at most
`2 ceil(Phi(n)/3^(d-1))`, and the width is at most `F_(d+2)`.
The total tested-node bound remains `O(Phi(n)^0.3046...)`.

Each leaf x is exactly a contact source whose arc visits n before its next
contact. A noncontact state cannot repeat within such an arc: (1) would
strictly increase Phi around that cycle. Determinism excludes two different
paths from the same x to n. Thus there is no multiplicity or hidden inverse
tail. If w has an exact rational evaluator, Lw has one too.

For positivity, follow the pure doubling ancestors n,2n,4n,... until the
first contact. Failure to find one would force
`Phi(2^j n)=ceil(Phi(n)/3^j)` forever, contradicting properness. This
contact's arc contains n before its next contact.

Each finite arc has a telescoping flow residual: its initial unit mass minus
its surviving endpoint unit mass. Summing gives (12); all pointwise sums
are finite. Nonnegative Tonelli summation gives (13), including infinite
values. QED.

### Minimality and uniqueness

If v>=0 agrees with w on C and satisfies `v(n)>=Kv(n)` at every noncontact,
then v>=Lw. Induct through the finite backward tree at each noncontact.
If equality holds at every noncontact, this induction gives v=Lw. Thus Lw
is the unique extension with exact interior flow balance and the least
nonnegative superbalanced extension for the prescribed contact trace.

This is a constructive flow compiler, not a new proof of the missing contact
inequality. In particular the positive computable lift of `Phi^(-s)` retains
the explicit contact-row failures established above.

## 6. CT-005: actual endpoint budgets and an unconditional moment domain

The known contact proof supplies the following explicit clock bound:

\[
r(x)\le2+\frac{\log((9/2)(x+1))}{\log(4/3)}.                 \tag{14}
\]

Indeed start at u=Sx. For a noncontact u, the old exit condition is
`(4/3)^j>(u+1)^2/(Phi(u)-1)`. Since u>=2,
`(u+1)^2/(Phi(u)-1)<=(u+1)^2/(u-1)<=3(u+1)`.
Taking the next integer beyond the logarithm, and using
`u+1<=(3/2)(x+1)`, gives (14). Immediate absorption or immediate contact
also obeys this bound.

Set

\[
\theta=\frac{\log2}{\log(4/3)}\approx2.4094,
\qquad A=\frac94\left(\frac92\right)^{\theta-1}.
\]

Every state z on the actual arc, including its endpoint, satisfies

\[
z+1\le A(x+1)^\theta.                                      \tag{15}
\]

This follows from `(S^j x)+1<=(3/2)^j(x+1)` and (14). Therefore, for p>=0,

\[
\sum_n n^p(Lw)(n)
=\sum_{x\in C}w(x)\sum_{j<r(x)}(S^j x)^p
\le A^p\sum_{x\in C}r(x)(x+1)^{p\theta}w(x).               \tag{16}
\]

For `w_s(x)=Phi(x)^(-s)`, the inherited sublevel estimate
`#{Phi<=M}=O(sqrt(M)log M)` implies:

* Lw_s is positive, finite-valued, and summable for every s>1/2; it is
  computable when s is computable.
* It has finite p-th ordinary-height moment whenever `s>p theta+1/2`.
* It has finite Phi^p moment whenever `s>2p theta+1/2`.

The proof uses (14)--(16), x<=Phi(x), and dyadic summation with the extra
logarithmic factors. For integer s the evaluator is rational. For a fixed
computable real s>1/2 it is a finite computable-real sum.

Contact transport itself has the explicit domain-loss bound

\[
\sum_y\Phi(y)^p(K_C f)(y)
\le A^{2p}(3/2)^{2p\theta}
       \sum_x\Phi(x)^{2p\theta}f(x),\qquad f\ge0.            \tag{17}
\]

Thus extra source integrability can pay for one whole contact return; CT-001
shows why the same p-moment domain cannot be reused unchanged. Repeating
(17) repeatedly increases the required exponent. It is not an all-return
bound for one fixed source space.

There is also a weak domain that *is* preserved: (15) implies
`1+log(Phi(Rx)+1)<=B[1+log(Phi(x)+1)]` for an absolute finite B.
Every finite logarithmic Phi moment therefore stays finite on one return.
These estimates do not supply a summable inverse power of the logarithmic
rank, so this observation supplies no contracting summable weight.

## 7. A precise connection with positive-source inverse density

Restrict Lw_s to odd states, without changing its shortcut-clock definition.
If `s>theta+1/2`, let
`M_0=sum_{t odd}(Lw_s)(t)` and `M_1=sum_{t odd}t(Lw_s)(t)`, both finite.
The previous packet's **odd inverse-reference law**, independently of this
shortcut map, then obeys by nonnegative summation

\[
\sum_{t\text{ odd}}(Lw_s)(t)\rho_q(t)
\le6qM_1+(64/81)^qM_0.                                    \tag{18}
\]

For 0<=z<1, summing in depth gives the corresponding finite resolvent bound

\[
\sum_{q\ge1}z^q\sum_{t\text{ odd}}(Lw_s)(t)\rho_q(t)
\le\frac{6M_1z}{(1-z)^2}
 +\frac{M_0(64/81)z}{1-(64/81)z}.                          \tag{19}
\]

This is a justified way to pay for **actual changing endpoints** with an
explicit contact-source moment. It does not identify shortcut return clocks
with odd inverse depth, prove finiteness at z=1, or preserve a single source
moment under arbitrarily many contact returns.

### Stronger cross-track consequence: a bounded depth-average pairing

The companion `INVERSE_GREEN.md`, IFT-003, independently proves the cumulative
bound

\[
\sum_{q=0}^Q\rho_q(t)\le\kappa_t
 \left[t(1+Q\log96)+\frac98(64/81)^Q\right],
\qquad\kappa_t\le3t+1.                                    \tag{20}
\]

Here kappa_t includes exact periodic renewal when needed; the universal
upper bound does not assume that t is nonperiodic. Suppose now that
`s>2 theta+1/2`, and define `M_2=sum_{t odd}t^2(Lw_s)(t)`, which is finite
by (16). Nonnegative summation of (20) gives, for Q>=1,

\[
\boxed{\sum_{q=0}^Q\sum_{t\text{ odd}}(Lw_s)(t)\rho_q(t)
\le(3M_2+M_1)(1+Q\log96)
 +\frac98(3M_1+M_0)(64/81)^Q.}                            \tag{21}
\]

Thus the actual occupation population has bounded Cesaro averages in inverse
depth. Its Abel transform has a simple-pole **upper order**, explicitly

\[
\limsup_{z\uparrow1}(1-z)
 \sum_{q\ge0}z^q\sum_{t\text{ odd}}(Lw_s)(t)\rho_q(t)
\le(3M_2+M_1)\log96.                                     \tag{22}
\]

For example s=6 gives an exact rational pointwise occupation evaluator and
finite M_2: `theta<11/4` follows from `3^11<2^18`, so
`2 theta+1/2<6`. Formula (22) follows by summation by parts from (21), not
from a claimed meromorphic continuation or a claimed limit of the profile.
No bound for a single prescribed depth, or unweighted orbit termination,
is inferred. This upgrade pays an explicit second-height-moment cost and
keeps the two operators and clocks distinct.

## 8. Evidence and what is still missing

The companion `check_contact_transport.py` reconstructs the finite templates,
the exact rational inequalities supporting the all-k proof, bounded instances
of the two infinite families, and the occupation lift in two directions.
It uses an independently implemented fixed-cutoff prefix evaluator and a
source-only envelope horizon, rather than importing PR142's evaluator.
Explicit exceptions preserve checks under Python optimization.

The flow comparisons use a **proved complete contact-source cutoff** for
the selected targets, not an arbitrary truncated inverse search. A separate
finite source population checks the full Poisson residual and exact clock
mass identity by literal forward arcs.

The remaining contact task is an arithmetic trace w whose complete rows
satisfy a useful inverse inequality, or a physical descent mechanism that
retains a fixed original source. Finite core changes, polynomial height/rank
weights, and valuation-only corrections do not solve this task. The occupation
lift makes the required global extension exact and computable, but does not
manufacture the missing inequality on C.
