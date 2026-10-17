# Iteration 07: rounded-deficit pressure and fresh-prime renewal

All theorem-level claims remain `PROPOSED` pending independent reconstruction.
The standard nondegenerate S-unit finiteness theorem is imported only in
`T-9513`, with the proper-subsum audit written out below.  No claim in this
file proves termination of the H subsystem.

This iteration combines the exact future-demand identity of `T-9511` with the
successive-renewal arithmetic suggested by the wave-5 literature audit.  The
result is a sharper description of the sole remaining subcritical ray:

```text
large valuation
 -> a later large rounded deficit
 -> an exponentially large odd-core reset;

large renewal core
 -> a long zero room or a large primitive bridge factor;

fixed bridge-prime support
 -> only finitely many transitions.
```

The missing theorem is now quantitative: prove that the globally fresh bridge
mass forced by these resets cannot fit inside the discounted completion-height
budget.

---

## L-9519: Exact rounded-deficit pressure

**Claim ID:** `L-9519`  
**Title:** Exact H transitions pay a uniform rounded-deficit toll  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `D-9501`  
**Scope:** every genuine positive exact H chain

### Definitions

Let

\[
2^{3r_{n+1}+2}u_{n+1}-3^{2r_n+1}u_n=1
\tag{1}
\]

be an exact positive chain.  Put

\[
c={\log 9\over\log 8},
\qquad
h_n=\log_8 u_n,
\tag{2}
\]

\[
\theta_n=\lceil cr_n\rceil-cr_n\in[0,1),
\qquad
s_n=\lceil cr_n\rceil-r_{n+1},
\tag{3}
\]

and split

\[
s_n=d_n-o_n,
\qquad
d_n=(s_n)^+,
\qquad o_n=(-s_n)^+.
\tag{4}
\]

Finally set

\[
X_n=3^{2r_n+1}u_n=p_{n+1}-1
\tag{5}
\]

and

\[
\delta_n=
\log_8{4X_n\over3(X_n+1)}.
\tag{6}
\]

Because every genuine positive exact endpoint satisfies `p_(n+1)>=16`,

\[
X_n\ge15.
\tag{7}
\]

Hence, with

\[
\delta_*:=\log_8(5/4)>0,
\qquad
\delta^*:=\log_8(4/3),
\tag{8}
\]

one has

\[
\boxed{
\delta_*\le\delta_n<\delta^*.
}
\tag{9}
\]

### Statement 1: exact pressure identity

For every transition,

\[
\boxed{
h_{n+1}-h_n=s_n-\theta_n-\delta_n.}
\tag{10}
\]

Consequently, on every interval `a<=n<b`, with `L=b-a`,

\[
\boxed{
\log_8{u_b\over u_a}
=D-O-\Theta-\Delta,
}
\tag{11}
\]

where

\[
D=\sum_{a\le n<b}d_n,
\quad
O=\sum_{a\le n<b}o_n,
\quad
\Theta=\sum_{a\le n<b}\theta_n,
\quad
\Delta=\sum_{a\le n<b}\delta_n.
\tag{12}
\]

Since `u_b>=1`,

\[
\boxed{
D\ge O+\Theta+\delta_*L-\log_8u_a.
}
\tag{13}
\]

In particular, on every infinite positive exact chain,

\[
\boxed{
\liminf_{N\to\infty}{1\over N}\sum_{n<N}d_n
\ge\delta_*.
}
\tag{14}
\]

### Statement 2: rounded-critical runs contract the integer core

If

\[
r_{n+1}\ge\lceil cr_n\rceil,
\tag{15}
\]

then `s_n<=0`, and

\[
\boxed{
{u_{n+1}\over u_n}\le8^{-\delta_*}={4\over5}.
}
\tag{16}
\]

Thus a consecutive rounded-critical run beginning at core `u` has length at
most

\[
1+\left\lceil\log_{5/4}u\right\rceil.
\tag{17}
\]

No infinite genuine positive chain can eventually remain rounded-critical.

### Statement 3: a positive deficit is an exponential reset

If `d_n>0`, then

\[
\boxed{
{u_{n+1}\over u_n}
>
{3\over4}\,8^{d_n-1}.
}
\tag{18}
\]

Under the subcritical hypothesis of `T-9511`,

\[
{r_n\over c^n}\longrightarrow0,
\tag{19}
\]

variation of constants gives

\[
\boxed{
\sup_{m\ge n}d_m\ge(c-1)r_n.
}
\tag{20}
\]

Combining (18) and (20),

\[
\boxed{
\sup_{m\ge n}
\log_8{u_{m+1}\over u_m}
>
(c-1)r_n-1-\delta^*.
}
\tag{21}
\]

So an unbounded subcritical valuation sequence necessarily produces
arbitrarily large multiplicative core resets.

### Proof

From (1),

\[
{u_{n+1}\over u_n}
=
{3\over4}
8^{cr_n-r_{n+1}}
\left(1+{1\over X_n}\right).
\tag{22}
\]

Since `cr_n-r_(n+1)=s_n-theta_n`, definition (6) turns (22) into

\[
{u_{n+1}\over u_n}=8^{s_n-\theta_n-\delta_n},
\tag{23}
\]

which proves (10).  Summation proves (11), and (9) gives (13)--(14).
If `s_n<=0`, (23) and (9) give (16); iteration gives (17).
If `s_n=d_n>0`, use `theta_n<1` and `delta_n<delta^*` in (23) to obtain
(18).  Equation (20) is `T-9511/(24)--(25)`, and (21) follows. QED.

### Interpretation

The subcritical ray is not a low-variation exceptional path.  It must alternate
between contracting rounded-critical stretches and increasingly violent
integer core resets.  Any finite-trap proof must account for those resets
rather than treating them as bounded noise.

---

## L-9520: Successive-renewal compatibility and the prime firewall

**Claim ID:** `L-9520`  
**Title:** Adjacent renewal cores satisfy one exact two-place equation  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `L-9518`  
**Scope:** three consecutive nonzero renewal times

### Setup

At an interior nonzero renewal, abbreviate

\[
a=L_{k-1},
\qquad b=L_k,
\qquad R=R_k,
\qquad U=U_k,
\tag{24}
\]

\[
X=W_{k-1},
\qquad Y=W_k.
\tag{25}
\]

All of `U,X,Y` are positive and coprime to `6`.

### Statement 1: central two-place star

The adjacent renewal bridges share

\[
\boxed{
3^aX+1=8^RU,
\qquad
4^bY+1=9^RU.
}
\tag{26}
\]

Eliminating `U` gives

\[
\boxed{
8^R4^bY-9^R3^aX=9^R-8^R.
}
\tag{27}
\]

### Statement 2: prime firewall

One has

\[
\boxed{
\gcd(U,XY)=1,
\qquad
\gcd(X,Y)\mid 9^R-8^R.
}
\tag{28}
\]

If `ell^e` divides `gcd(X,Y)`, then `ell>=5` and

\[
\boxed{
\operatorname{ord}_{\ell^e}(9\cdot8^{-1})\mid R.
}
\tag{29}
\]

Thus every prime power reused across the central renewal pays an exact
multiplicative-order condition in the current letter `R`.

### Statement 3: primitive forward factor or long room

Put

\[
G=\gcd(X,Y),
\qquad E=X/G,
\qquad F=Y/G.
\tag{30}
\]

Then

\[
\boxed{U<4^bF.}
\tag{31}
\]

Consequently at least one of

\[
\boxed{b\ge{1\over4}\log_2U}
\tag{32}
\]

or

\[
\boxed{F>\sqrt U}
\tag{33}
\]

holds at every central renewal.

### Statement 4: second integral sign law

Define

\[
\Lambda_k
=R\log(9/8)+a\log3-b\log4.
\tag{34}
\]

Then

\[
\boxed{
Y=e^{\Lambda_k}X
\left(
1+{1-(8/9)^R\over3^aX}
\right).
}
\tag{35}
\]

The coefficient `e^(Lambda_k)` is never one, and integrality gives

\[
\boxed{
\Lambda_k>0\Longrightarrow Y>X,
\qquad
\Lambda_k<0\Longrightarrow Y\le X.
}
\tag{36}
\]

A plateau `X=Y=W` is necessarily resonant:

\[
\boxed{
W\mid9^R-8^R.
}
\tag{37}
\]

### Proof

Equations (26) are the two instances of `L-9518/(6)` adjacent to the central
renewal; elimination gives (27).  A common divisor of `U` and `X` or of `U`
and `Y` would divide `1` in (26), proving the first part of (28).  A common
divisor of `X,Y` divides the left side of (27), hence its right side.  Division
by `8^R` modulo `ell^e` proves (29).

Write `X=GE`, `Y=GF`.  From (28), `G<=9^R-8^R`; hence

\[
9^RU=1+4^bGF
\le1+4^b(9^R-8^R)F
<9^R4^bF,
\tag{38}
\]

which proves (31).  If (32) fails, then `4^b<sqrt(U)`, and (31) gives
(33).  Factoring (27) proves (35).  If `Lambda_k<0`, the right side is
strictly smaller than `X+1`; integer-valuedness gives `Y<=X`.  The positive
case is immediate, and (37) follows from (28). QED.

---

## T-9513: Fixed bridge-prime support is finite

**Claim ID:** `T-9513`  
**Title:** A nonperiodic exact H survivor cannot recycle one finite bridge-prime alphabet  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `L-9520`; nondegenerate S-unit finiteness (`LIT-KTHM-0043`)  
**Scope:** a hypothetical positive nonperiodic infinite exact orbit

### Statement

For every fixed finite set of primes `S`, only finitely many central renewals
satisfy

\[
\operatorname{supp}(XY)\subseteq S.
\tag{39}
\]

Consequently the bridge cores `W_k` have infinite global prime support.

Let

\[
P_k^{\rm new}
=
\prod_{\substack{
\ell\mid W_k\\
\ell\nmid W_0W_1\cdots W_{k-1}}}
\ell^{v_\ell(W_k)}.
\tag{40}
\]

Then

\[
\boxed{P_k^{\rm new}\mid F_k}
\tag{41}
\]

for the primitive forward factor in (30), infinitely many `P_k^(new)` exceed
one, and

\[
\boxed{
\sum_k\log P_k^{\rm new}=\infty,
\qquad
\sum_k\log F_k=\infty.
}
\tag{42}
\]

### Proof

Normalize (27) as

\[
\boxed{
-4^bY+3^a(9/8)^RX+(9/8)^R=1.
}
\tag{43}
\]

Under (39), all three terms lie in the finitely generated multiplicative group

\[
\Gamma=\langle-1,2,3,S\rangle.
\tag{44}
\]

The equation is nondegenerate.  The two positive terms cannot have zero sum.
If the negative term cancelled the second term, then

\[
4^bY=3^a(9/8)^RX;
\tag{45}
\]

if it cancelled the third, then

\[
4^bY=(9/8)^R.
\tag{46}
\]

In each case the left side has positive `2`-adic valuation `2b`, whereas the
right side has valuation `-3R`; both are impossible.  Thus the standard
nondegenerate S-unit theorem gives only finitely many triples in (43).

The third coordinate recovers `R`; the first then recovers `b,Y`; after `R`
is known, the `3`-adic valuation and value of the second recover `a,X`; and
(26) recovers `U`.  Infinitely many occurrences would therefore repeat one
exact central state, forcing eventual periodicity.  This proves (39).

A prime appearing globally for the first time in `W_k=Y` does not divide
`X=W_(k-1)`, so its full prime power survives division by `G` and divides
`F`.  Infinite prime support proves (41)--(42). QED.

### Scope boundary

The theorem gives divergent **unweighted** fresh logarithmic mass.  It does not
yet prove that fresh mass appears early enough to contradict the exponentially
discounted core budget of `T-9505`.

---

## T-9514: Exact final survivor dichotomy

**Claim ID:** `T-9514`  
**Title:** Every remaining nonperiodic survivor is either finite-alphabet or reset--renewal wild  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `T-9509`, `T-9511`, `L-9519`, `L-9520`, `T-9513`  
**Scope:** conditional on existence of a nonperiodic infinite exact orbit and on the audited Yu specialization in `T-9509`

### Statement

Every such orbit is subcritical,

\[
r_n=o(c^n),
\tag{47}
\]

and falls into one of the following mutually exhaustive alternatives.

### A. Bounded-letter alternative

The letters `r_n` remain bounded.  Then the orbit has a finite letter alphabet,
but it must still:

1. be non-eventually-periodic;
2. introduce infinitely many bridge primes;
3. have superlinear factor complexity along a subsequence by `L-9515` whenever
   its maximum capital is sublinear in orbit time.

### B. Reset--renewal alternative

The letters are unbounded.  Then:

1. the rounded deficits `d_n` are unbounded;
2. there are arbitrarily large multiplicative resets satisfying (21);
3. every large renewal core `U_k` is paid for either by a zero room satisfying
   (32) or by a primitive forward factor satisfying (33);
4. no fixed finite prime alphabet can support those primitive factors
   indefinitely.

Thus a counterexample cannot be a bounded-carry perturbation of the critical
trajectory, cannot live in a fixed S-unit group, and cannot avoid both long
zero rooms and large primitive bridge factors.

### Proof

Subcriticality is `T-9509`.  If the letters are bounded, Alternative A is only
the stated specialization of nonperiodicity, `T-9513`, and `L-9515`.  If they
are unbounded, (20)--(21) prove items 1--2; (31)--(33) prove item 3; and
`T-9513` proves item 4. QED.

### Interpretation

This is not a termination theorem.  It is the complete structural split left
by the current proof package.  The bounded-letter branch requires a
finite-alphabet nonstabilization theorem.  The unbounded branch requires a
quantitative comparison between fresh prime mass, zero-room length, and the
discounted core budget.

---

## R-9504: Why the present pressure bounds do not yet close H

**Claim ID:** `R-9504`  
**Title:** Rounded pressure and unweighted fresh mass remain scale-compatible  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22

The following implications are invalid without an additional quantitative
input:

```text
unbounded deficits  => contradiction;
infinite prime support => contradiction;
plastic dimension < 1 => no ordinary point;
finite ordinary minima growing through a fixed precision => divergence.
```

A subcritical schematic profile can have polynomially growing letters,
quadratically growing `log u_n`, increasingly late fresh primes, and still fit
inside

\[
\sum_n c^{-n}\log u_n<\infty.
\tag{48}
\]

The profile need not be an exact orbit; it demonstrates that the current
one-dimensional inequalities are not mutually contradictory.  A closing
argument must couple the arithmetic **time of appearance** of fresh factors or
zero carries to their completion-height cost.

---

## Q-9508: Discounted fresh-mass or finite-alphabet nonstabilization

**Claim ID:** `Q-9508`  
**Title:** Close the two surviving branches of `T-9514`  
**Status:** `IDEA`  
**Authoring agent:** `gpt56-h-01`  
**Created:** 2026-07-22  
**Dependencies:** `T-9505`, `T-9513`, `T-9514`

A proof of either pair of statements below would finish the infinite survivor
obstruction.

### Unbounded-letter target

Show that the globally fresh factors forced by `T-9513` obey a lower bound
incompatible with the discounted core budget; for example, prove on every
unbounded reset--renewal ray that

\[
\sum_k c^{-t_k}\log P_k^{\rm new}=\infty
\tag{49}
\]

while deriving from the exact bridges and `T-9505` the corresponding finite
upper bound.

The exact statement (49) is only a model target; another completion-height
quantity with the same contradiction is acceptable.

### Bounded-letter target

For every finite alphabet `A subset Z_(>=0)`, prove that an infinite exact
itinerary with all `r_n in A` and an ordinary positive ghost is eventually
periodic.  Periodic positive-capital tails are already excluded by their
negative real affine fixed point, while contracting tails descend.

Equivalently, prove eventual nonzero carry for every nonperiodic finite-alphabet
ghost code.

### Direct all-orbit alternative

The stronger scalar theorem remains

\[
\boxed{\nu_K\longrightarrow\infty.}
\tag{50}
\]

A proof of (50) bypasses both branches and the still-open signed-displacement
claim.
