# Iteration 11: exact renewal one-counter normal form and refund graph

All theorem-level claims remain `PROPOSED` pending independent review.
`X-9509` is an exact finite computation, not an infinite-orbit claim.

This iteration imports the constructive lesson of the repository's quotient-
refund work: a counterexample architecture should end with one finite ordinary
state and one deterministic unbounded counter update, rather than with an
abstract compatible inverse limit. For H, the successive-renewal equations
admit exactly such a normal form.

The exact block recurrence is

\[
p_{n+1}=\frac{3^{2r_n+1}}{2^{3r_n+2}}p_n+1,
\qquad
p_n=2^{3r_n+2}u_n,
\tag{1}
\]

with `u_n=1 mod 4` and `p_n=1 mod 3`.

At consecutive nonzero renewals the bridge notation of `L-9518` is

\[
3^aX+1=8^RU,
\qquad
4^bY+1=9^RU,
\tag{2}
\]

where

\[
a,R,b\ge1,
\qquad
X\equiv Y\equiv5\pmod6,
\qquad
U\equiv1\pmod4.
\tag{3}
\]

---

## L-9527: canonical renewal type cylinders

**Claim ID:** `L-9527`  
**Title:** Every renewal type is one exact ordinary counter progression, and every type-to-type transition is one affine quotient-refund branch  
**Status:** `PROPOSED`  
**Dependencies:** `L-9518`  
**Scope:** exact positive renewal bridges

### Type cylinder

Fix a renewal type

\[
\tau=(a,R,b),
\qquad a,R,b\ge1,
\tag{4}
\]

and put

\[
d_\tau=3R+2b,
\qquad
M_\tau=3\cdot2^{d_\tau+1}.
\tag{5}
\]

There is a unique integer

\[
0\le x_\tau<M_\tau
\tag{6}
\]

satisfying

\[
x_\tau\equiv5\pmod6
\tag{7}
\]

and

\[
9^R3^ax_\tau+9^R-8^R
\equiv2^{d_\tau}\pmod{2^{d_\tau+1}}.
\tag{8}
\]

Define

\[
U_\tau=\frac{3^ax_\tau+1}{8^R},
\qquad
Y_\tau=\frac{9^RU_\tau-1}{4^b}.
\tag{9}
\]

Then every positive solution of (2)--(3) of type `tau`, and no other one, is
parametrized by one ordinary counter `k>=0`:

\[
\boxed{
X=x_\tau+M_\tau k,
}
\tag{10}
\]

\[
\boxed{
U=U_\tau+2^{2b+1}3^{a+1}k,
}
\tag{11}
\]

\[
\boxed{
Y=Y_\tau+2\cdot3^{2R+a+1}k.
}
\tag{12}
\]

In particular,

\[
U_\tau\equiv1\pmod4,
\qquad
Y_\tau\equiv5\pmod6.
\tag{13}
\]

### Type transition

Let

\[
\tau=(a,R,b),
\qquad
\sigma=(b,S,c).
\tag{14}
\]

Put

\[
q_\sigma=3S+2c,
\qquad
g_\tau=2R+a.
\tag{15}
\]

There is a unique residue

\[
0\le\eta_{\tau\sigma}<2^{q_\sigma}
\tag{16}
\]

with

\[
\boxed{
\eta_{\tau\sigma}
\equiv
\frac{x_\sigma-Y_\tau}{6}
\,3^{-g_\tau}
\pmod{2^{q_\sigma}}.
}
\tag{17}
\]

Define

\[
\boxed{
\zeta_{\tau\sigma}
=
\frac{
Y_\tau+2\cdot3^{g_\tau+1}\eta_{\tau\sigma}-x_\sigma
}{M_\sigma}.
}
\tag{18}
\]

Then `zeta_(tau sigma)` is a nonnegative integer, and the exact deterministic
transition from type `tau` to type `sigma` is

\[
\boxed{k=\eta_{\tau\sigma}+2^{q_\sigma}t,}
\tag{19}
\]

\[
\boxed{k'=\zeta_{\tau\sigma}+3^{g_\tau}t,}
\tag{20}
\]

for one and only one `t>=0`.

### Proof

Eliminating `U` from (2) gives

\[
9^R3^aX+9^R-8^R=2^{3R+2b}Y.
\tag{21}
\]

Because `Y` is odd, the left side has exact `2`-adic valuation `d_tau`, which
is exactly congruence (8). The right-hand side of (8) is odd before the
multiplicative inverse is taken, so its solution modulo `2^(d_tau+1)` is odd.
Combining that residue with `X=2 mod 3` gives one class modulo `M_tau`, proving
existence and uniqueness of (6)--(8).

Modulo `8^R`, equation (8) makes `3^a x_tau+1` divisible by `8^R`, proving the
first integrality in (9). After division by `8^R`, (8) says

\[
9^RU_\tau-1
\equiv2^{2b}\pmod{2^{2b+1}},
\tag{22}
\]

so the second quotient in (9) is odd. Since `b>=1`, reducing (22) modulo four
gives `U_tau=1 mod 4`; reducing the second equation of (2) modulo three gives
`Y_tau=2 mod 3`, hence (13).

Increasing `X` by `M_tau` changes `U` by

\[
\frac{3^aM_\tau}{8^R}
=2^{2b+1}3^{a+1},
\tag{23}
\]

and changes `Y` by

\[
\frac{9^R}{4^b}2^{2b+1}3^{a+1}
=2\cdot3^{2R+a+1}.
\tag{24}
\]

This proves (10)--(12) and their converse.

For the transition, the outgoing bridge core `Y` of `tau` must equal the
incoming bridge core `X` of `sigma`. Using (10) and (12), this equality is

\[
Y_\tau+6\cdot3^{g_\tau}k
=x_\sigma+6\cdot2^{q_\sigma}k'.
\tag{25}
\]

Division by six and inversion of the odd factor `3^(g_tau)` give the unique
congruence (17). Substitution `k=eta+2^q t` into (25) gives (18)--(20).
The numerator in (18) is a multiple of `M_sigma`. It is greater than
`-M_sigma`, because `Y_tau>=0`, `eta>=0`, and `0<=x_sigma<M_sigma`; hence that
multiple is nonnegative. QED.

---

## T-9518: counterexample equivalence and renewal Kraft law

**Claim ID:** `T-9518`  
**Title:** H counterexamples are exactly forever-defined renewal counters, and one renewal consumes a `1/21` fraction of the dyadic counter space  
**Status:** `PROPOSED`  
**Dependencies:** `D-9501`, `L-9518`, `L-9527`  
**Scope:** positive ordinary exact H orbits

### Counterexample equivalence

A positive infinite H orbit exists if and only if there is one finite ordinary
tuple

\[
\boxed{(a_0,R_0,b_0,k_0),
\qquad a_0,R_0,b_0\ge1,
\quad k_0\ge0,}
\tag{26}
\]

whose deterministic transition (17)--(20) is defined at every future renewal.

Given such a tuple, reconstruct

\[
X_0=x_{\tau_0}+M_{\tau_0}k_0,
\tag{27}
\]

\[
U_0=U_{\tau_0}+2^{2b_0+1}3^{a_0+1}k_0,
\tag{28}
\]

\[
p_0=2^{3R_0+2}U_0,
\qquad
n_0=\frac{p_0-4}{3}.
\tag{29}
\]

Then `n_0` is a positive integer and its exact block itinerary is

\[
R_0,0^{b_0-1},R_1,0^{b_1-1},R_2,\ldots.
\tag{30}
\]

Conversely, every positive infinite H orbit supplies a tail and a tuple (26)
with a forever-defined renewal counter.

### Exact Kraft law

For one fixed source type `tau`, the domains (19), as `(S,c)` range over all
positive integers, are pairwise disjoint. Their relative Haar measures in
`Z_2` add to

\[
\boxed{
\sum_{S,c\ge1}2^{-(3S+2c)}
=
\left(\sum_{S\ge1}2^{-3S}\right)
\left(\sum_{c\ge1}2^{-2c}\right)
=rac1{21}.
}
\tag{31}
\]

Conditioned on one edge, the tail update

\[
t\longmapsto\zeta_{\tau\sigma}+3^{g_\tau}t
\tag{32}
\]

is a bijection of `Z_2`. Hence the set of counters surviving `h` complete
renewals from one fixed source type has exact Haar measure

\[
\boxed{21^{-h}.}
\tag{33}
\]

### Ordinary stabilization

For every fixed length-`h` type path, exact composition of (19)--(20) has the
form

\[
\boxed{k_0=R_h+2^{Q_h}t_h,}
\tag{34}
\]

\[
\boxed{k_h=C_h+3^{G_h}t_h,}
\tag{35}
\]

where `Q_h` is the sum of the consumed quantities `3S+2c`, so `Q_h>=5h`.
For a fixed ordinary integer `k_0`, once `2^(Q_h)>k_0`, equation (34) forces

\[
R_h=k_0,
\qquad
t_h=0.
\tag{36}
\]

Thus the ordinary-section problem remains an eventual-zero-appended-block
problem in this exact one-counter chart.

### Proof

The reconstruction follows directly from `L-9527`; equation (2) gives every
current nonzero letter and the following zero room, and equality of adjacent
bridge cores stitches the blocks. Modulo three, the first equation of (2) gives
`8^R U=1`, while `2^(3R+2)=(-1)^R` modulo three, so `p_0=1 mod 3` and (29) is
integral. Every infinite H orbit has infinitely many nonzero letters: if its
block letters were eventually zero, then

\[
p_{n+t}-4=(3/4)^t(p_n-4),
\tag{37}
\]

which is impossible for nonzero ordinary integers; the only fixed value `p=4`
corresponds to `n=0`.

Pairwise disjointness in (31) follows because the next `S` and `c` are
recovered uniquely from the exact valuations of the two next bridge equations.
The domain measure is `2^(-q_sigma)`. Equation (32) is a `Z_2` bijection because
its multiplier is odd, proving independence under iteration and (33).
Equations (34)--(35) follow by induction from (19)--(20). QED.

---

## L-9528: exact refund edges

**Claim ID:** `L-9528`  
**Title:** One renewal edge has an exact nondecreasing-counter criterion  
**Status:** `PROPOSED`  
**Dependencies:** `L-9527`

For one edge `tau -> sigma`, write

\[
q=q_\sigma,
\qquad
g=g_\tau,
\qquad
\eta=\eta_{\tau\sigma},
\qquad
\zeta=\zeta_{\tau\sigma}.
\tag{38}
\]

Every point of its domain obeys

\[
\boxed{k'-k=(\zeta-\eta)+(3^g-2^q)t.}
\tag{39}
\]

Call the edge a **refund edge** when

\[
\boxed{3^g\ge2^q,
\qquad
\zeta\ge\eta.}
\tag{40}
\]

Then every ordinary point in the edge cylinder satisfies

\[
\boxed{k'\ge k.}
\tag{41}
\]

Because `q>=5`, equality `3^g=2^q` is impossible. Hence (41) is strict whenever
`t>0`; at `t=0` equality occurs only when `zeta=eta`.

A finite tuple whose deterministic decoder is forever defined and eventually
uses only refund edges is therefore an explicit positive H counterexample. If
strict refund occurs infinitely often, its counter is unbounded, although
unboundedness is not needed merely to disprove H termination.

Equation (39) is immediate from (19)--(20). QED.

---

## R-9509: the finite refund graph is a genuine engine but not a witness

**Claim ID:** `R-9509`  
**Title:** A refund SCC is positive construction data, but an ordinary counter must still be exhibited  
**Status:** `PROPOSED`  
**Dependencies:** `T-9518`, `L-9528`

The type-level refund graph can contain self-loops and large strongly connected
components. This differs materially from the `10/30` compiler, whose physical
zero-carry macros descend. A refund SCC supplies genuine positive multiplier
cycles in the renewal-counter projection.

Nevertheless, it is not a counterexample by itself. An infinite graph path
defines one nested `2`-adic counter cylinder. The corresponding point need not
be a nonnegative ordinary integer. A periodic type path is especially
insufficient: its unique rational fixed ghost is governed by the usual affine
cycle equation and must pass the positive-cycle integrality test.

The exact proof object remains one finite tuple with a forever-defined decoder.
A modular lasso, SCC, positive density of finite paths, or an abstract `Z_2`
point does not meet that gate.

---

## X-9509: bounded one-counter and refund-graph audit

The exact standard-library experiment checks every type and target parameter in

\[
1\le a,R,b,S,c\le15.
\tag{42}
\]

It verifies (10)--(20) by direct valuation decoding at two tail values for each
transition cylinder. The frozen totals are

\[
\begin{array}{l|r}
\text{types}&3,375\\
\text{transition cylinders}&759,375\\
\text{refund edges}&353,835\\
\text{refund self-loops}&42\\
\text{zero-increment refund edges}&1\\
\text{refund SCCs}&34\\
\text{largest refund SCC}&594.
\end{array}
\tag{43}
\]

The longest canonical-root refund chain in this box has four transitions and
starts from

\[
\tau_0=(1,8,7),
\qquad
k_0=133,973.
\tag{44}
\]

Its reconstructed initial state is

\[
X_0=220,957,479,840,077,141,
\tag{45}
\]

\[
U_0=39,510,276,289,
\tag{46}
\]

\[
p_0=2,651,489,758,080,925,696,
\qquad
n_0=883,829,919,360,308,564.
\tag{47}
\]

The exact counter path is

\[
\begin{aligned}
(1,8,7),133973
&\to(7,4,3),65999254\\
&\to(3,2,1),3699285805175\\
&\to(1,2,1),31602883030933\\
&\to(1,1,2),59996098254038\\
&\to\text{undefined}.
\end{aligned}
\tag{48}
\]

It is an exact rejected construction candidate, not a counterexample.

Semantic digest:

```text
95d98ad1b0b915ec0905235e567779c99a9d971e4ac73f596ef089c25f80697d
```

---

## Q-9513: the explicit renewal-counter counterexample atom

**Claim ID:** `Q-9513`  
**Title:** Find one forever-defined ordinary renewal counter, or prove that every one exits  
**Status:** `IDEA`

The constructive target is now finite and exact:

\[
\boxed{
\text{Exhibit one }(a_0,R_0,b_0,k_0)
\text{ whose deterministic decoder (17)--(20) is defined forever.}
}
\tag{49}
\]

A stronger positive certificate keeps the path in the refund graph and proves
that strict refund occurs infinitely often.

The negative alternative is an all-time theorem that every nonnegative integer
counter eventually fails one of the two valuation tests defining its next
renewal.

This is the H analogue of the repository's deterministic complement-counter
frontier. Unlike a ghost-only formulation, (49) already includes the ordinary
root, exact physical initialization, unique next type, and every future bridge
replay. Solving (49) positively gives an unconditional H counterexample and,
through `L-9501`, an unconditional Collatz counterexample.
