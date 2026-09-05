# L-9830 -- Settled successor carries and the signed difference chart

Claim ID: `L-9830`  
Title: After the base-64 borrow settles, a successor carry difference is an exact signed-chart iterate  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `R-9804`; `L-9815` only for the exact-successor specialization  
Scope: pair-specific base-64 carry valuation for two finite survivor prefixes  
Related counterexample candidates: none

## Definitions

Let

\[
A<B=A+d
\tag{1}
\]

be nonnegative integers which both survive at least `n>=1` chart steps. Write
their chart states and directive digits as

\[
A_j=T^j(A),\quad \varepsilon_j,
\qquad
B_j=T^j(B),\quad \nu_j,
\tag{2}
\]

and put

\[
\Delta_j=B_j-A_j,
\qquad
\eta_j=\nu_j-\varepsilon_j\in\{-1,0,1\}.
\tag{3}
\]

Use ordinary infinite base-64 expansions, padded by high zeros,

\[
A=\sum_{j\ge0}a_j64^j,
\quad
B=\sum_{j\ge0}b_j64^j,
\quad
d=\sum_{j\ge0}q_j64^j.
\tag{4}
\]

The subtraction borrows for `B-A=d` are defined by

\[
\beta_0=0,
\qquad
q_j=b_j-a_j-\beta_j+64\beta_{j+1},
\qquad
\beta_j\in\{0,1\}.
\tag{5}
\]

Equivalently, the same `beta_j` are the carries in the addition `A+d=B`.
Let

\[
t=\min\{k\ge1:d<64^k\},
\qquad
u=\min\{j\ge t:\beta_j=0\}.
\tag{6}
\]

The integer `u` exists because the padded expansions are eventually zero. It
is the first high digit position after the addition carry has settled. Put
`ell=u-t`; this is the high carry-avalanche length.

For a survivor `X`, let `C_j(X)` be the exact inverse-cylinder carry from
`R-9804`, characterized by

\[
T^j(X)
=81^j\left\lfloor\frac{X}{64^j}\right\rfloor+C_j(X).
\tag{7}
\]

Write

\[
H_j=C_j(B)-C_j(A).
\tag{8}
\]

Finally, define the partial signed difference chart

\[
\mathfrak D(z)=\frac{81z-17\eta(z)}{64},
\tag{9}
\]

on positive integers with residue `0`, `1`, or `63` modulo `64`, where

\[
\eta(z)=
\begin{cases}
0,&z\equiv0\pmod {64},\\
1,&z\equiv1\pmod {64},\\
-1,&z\equiv63\pmod {64}.
\end{cases}
\tag{10}
\]

For a positive integer `m`, use the base-64 valuation

\[
\nu_{64}(m)=\max\{r\ge0:64^r\mid m\}.
\tag{11}
\]

## Statement

### 1. Borrow settlement exactly identifies the common high quotient

For every `j>=0`,

\[
\boxed{
(B\bmod64^j)-(A\bmod64^j)
=(d\bmod64^j)-\beta_j64^j
}
\tag{12}
\]

and therefore

\[
\boxed{
\left\lfloor\frac B{64^j}\right\rfloor
-\left\lfloor\frac A{64^j}\right\rfloor
=\left\lfloor\frac d{64^j}\right\rfloor+\beta_j.
}
\tag{13}
\]

At the settlement position,

\[
\boxed{
\left\lfloor\frac B{64^u}\right\rfloor
=\left\lfloor\frac A{64^u}\right\rfloor,
\qquad
a_j=b_j\quad(j\ge u).
}
\tag{14}
\]

If `ell>0`, the intervening high digits have the rigid avalanche form

\[
a_j=63,\quad b_j=0
\qquad(t\le j<u-1),
\tag{15}
\]

and the clearing digit satisfies `b_(u-1)=a_(u-1)+1`.

### 2. The orbit difference is autonomous

At every survived step,

\[
\boxed{
64\Delta_{j+1}=81\Delta_j-17\eta_j,
\qquad
\Delta_j\equiv\eta_j\pmod {64}.
}
\tag{16}
\]

Consequently the residue of `Delta_j` determines `eta_j`, and

\[
\boxed{
\Delta_j=\mathfrak D^j(d),
\qquad
\eta_j=\eta(\mathfrak D^j(d))
}
\tag{17}
\]

through every depth at which the pair survives.  Thus the signed directive
difference word is a function of the initial gap `d` alone; the lower member
`A` determines whether that signed word is jointly realizable, but not what it
must be once realized.

### 3. Exact settled-carry identity

For every `j<=n`,

\[
\boxed{
H_j
=\Delta_j-81^j
\left(
\left\lfloor\frac d{64^j}\right\rfloor+\beta_j
\right).
}
\tag{18}
\]

In particular, if `u<=n`, then the common high quotient in (14) cancels and

\[
\boxed{
H_u=\Delta_u=\mathfrak D^u(d)>0.
}
\tag{19}
\]

The settled carry difference therefore loses all dependence on `A` except
through the settlement time `u` and the realizability of the pair.

There are two exact finite compilers for this integer.  First,

\[
\boxed{
64^uH_u
=81^ud
-17\sum_{j=0}^{u-1}
\eta_j81^{u-1-j}64^j.
}
\tag{20}
\]

Substituting the subtraction stream gives the explicitly coupled form

\[
\boxed{
\begin{aligned}
64^uH_u
={}&81^u\sum_{j=0}^{u-1}
(b_j-a_j-\beta_j+64\beta_{j+1})64^j\\
&-17\sum_{j=0}^{u-1}
\eta_j81^{u-1-j}64^j.
\end{aligned}
}
\tag{21}
\]

Second, if

\[
G_j=H_j+81^j\beta_j,
\tag{22}
\]

then `G_0=0`, `G_u=H_u`, and the digitwise recurrence is

\[
\boxed{
G_{j+1}
=\frac{
81(G_j+81^jq_j)-17\eta_j
}{64}.
}
\tag{23}
\]

Equations (20)--(23) express the endpoint carry difference entirely through
the finite gap-digit/borrow stream and the signed directive stream.

### 4. Exact valuation and future-agreement statistic

Assume `u<=n`. Since the ordinary input digits of `A` and `B` agree at every
position at or above `u`, for every `0<=r<=n-u`,

\[
\boxed{
\varepsilon_{u+k}=\nu_{u+k}
\quad(0\le k<r)
\iff
64^r\mid H_u.
}
\tag{24}
\]

Equivalently,

\[
\boxed{
\min\{\nu_{64}(H_u),n-u\}
=\max\{r\le n-u:
\varepsilon_{u:u+r}=\nu_{u:u+r}\}.
}
\tag{25}
\]

Combining (20) and (24) yields a sharp finite congruence test:

\[
\boxed{
\nu_{64}(H_u)\ge r
\iff
81^ud
-17\sum_{j=0}^{u-1}
\eta_j81^{u-1-j}64^j
\equiv0\pmod {64^{u+r}}.
}
\tag{26}
\]

Thus no hidden infinite-state quotient is needed to measure the common
directive suffix of this particular pair: it is exactly the extra base-64
divisibility of the finite numerator in (20).

### 5. A general upper bound for the settled valuation

Put

\[
\delta=\log_{64}(81/64).
\tag{27}
\]

If `u<=n` and `v=nu_64(H_u)`, then

\[
\boxed{
v<\delta u+\log_{64}(d+1)
\le\delta u+t.
}
\tag{28}
\]

Writing `u=t+ell` gives the carry-avalanche form

\[
\boxed{
v<(1+\delta)t+\delta\ell.
}
\tag{29}
\]

In particular, because `t<=u`,

\[
\boxed{v<(1+\delta)u.}
\tag{30}
\]

This controls the full arithmetic valuation, not merely its truncation at the
observed survivor depth.

### 6. Exact-successor specialization

Take

\[
B=A+D_n(A)
\tag{31}
\]

from `L-9815`. Then the `q_j` in (4)--(5) are precisely the lexicographically
least positive cyclic subtraction digits among all depth-`n` survivor
cylinders. Whenever their ordinary carry settles by `u<=n`, equations
(19)--(30) give an exact pair-specific replacement for the globally impossible
zero-reset proposed before `R-9804`:

\[
\boxed{
C_u(B)-C_u(A)
=\mathfrak D^u(D_n(A)),
}
\tag{32}
\]

and the length of the following common directive block is exactly its
base-64 valuation, truncated by `n-u`.

The lexicographic minimality in `L-9815` does not, by itself, bound either the
avalanche `ell` or the cancellation in (20).  Any strengthening specific to
successors must exploit that optimization, rather than assuming a reset.

## Proof

### Borrow and quotient identities

Multiply (5) by `64^j` and sum over `0<=j<k`. The intermediate borrow terms
cancel, leaving

\[
\sum_{j<k}q_j64^j
=\sum_{j<k}(b_j-a_j)64^j+\beta_k64^k.
\tag{33}
\]

The left side is `d mod 64^k`, while the first sum on the right is
`(B mod 64^k)-(A mod 64^k)`. This proves (12). Splitting `B-A` into its low
remainder difference and its high quotient difference proves (13).

For `j>=t`, one has `q_j=0`. If `beta_j=0`, equation (5) forces
`b_j=a_j` and `beta_(j+1)=0`; hence the borrow stays cleared forever. This
proves (14). If the borrow remains one, (5) forces `a_j=63,b_j=0`; at the
last digit before it clears, it forces `b_j=a_j+1`. This proves (15).

### Signed chart and carry compiler

On the legal domain, `64q+e -> 81q+e` is strictly increasing, so
`Delta_j>0` at every common survived depth. Subtracting the two chart
recurrences gives the first equation in (16).
Reducing it modulo `64` and using `81 congruent 17 modulo 64` gives

\[
17(\Delta_j-\eta_j)\equiv0\pmod {64}.
\tag{34}
\]

Because `17` is invertible modulo `64`, this is the second equation in (16).
The only possible signed digits are `-1,0,1`, so the residue chooses exactly
the branch in (10). Induction from `Delta_0=d` proves (17).

Subtract (7) for `A` and `B`, and insert the high-quotient difference (13).
This proves (18). At `j=u`, both terms in parentheses vanish by `d<64^u`
and `beta_u=0`, proving (19).

Iterating the first recurrence in (16) to time `u` proves (20). Equation (21)
is (20) with `d=sum_(j<u) q_j64^j` and (5) substituted. To prove (23),
subtract the carry recurrences (9) of `R-9804` for the two input digits:

\[
H_{j+1}
=\frac{81(81^j(b_j-a_j)+H_j)-17\eta_j}{64}.
\tag{35}
\]

Insert (5), collect `H_j+81^j beta_j=G_j`, and add
`81^(j+1) beta_(j+1)` to both sides. This gives (23), and (19) gives
`G_u=H_u`.

### Valuation and upper bound

At position `u+k`, the two inverse-cylinder transductions read the same
ordinary digit by (14). Their legality residues therefore differ by the
current carry difference. Their directives agree exactly when that difference
is divisible by `64`; on an agreeing branch, their next carry difference is
`81/64` times the old one. Induction proves (24), hence (25). Multiplying the
divisibility `64^r divides H_u` by `64^u` in (20) proves (26).

For completeness, iteration of (16) and the bound `abs(eta_j)<=1` give

\[
(81/64)^u(d-1)+1
\le\Delta_u
\le(81/64)^u(d+1)-1.
\tag{36}
\]

Since `H_u=Delta_u>0` and `64^v<=H_u`, its upper half implies

\[
v<\log_{64}((81/64)^u(d+1))
=\delta u+\log_{64}(d+1).
\tag{37}
\]

The definition of `t` gives `d+1<=64^t`, proving (28). Substitution
`u=t+ell` proves (29), and `t<=u` proves (30). The specialization in part 6
uses only the exact successor and subtraction characterization in `L-9815`.
This completes the proof. QED

## Motivation

`R-9804` showed that a common high zero input cannot globally reset exact
carries. The surviving pair still has much more structure than an arbitrary
pair of exact states: adding its small successor gap changes only a finite low
base-64 block, followed by one possible carry avalanche. This lemma starts at
the first position after that avalanche and eliminates the common high
quotient exactly.

The result converts the missing pairwise synchronization question into one
finite integer. Long agreement after settlement is neither heuristic nor an
automata assumption; it is precisely high `64`-adic divisibility of (20).

## Dependency audit

- `R-9804` supplies the exact inverse-cylinder invariant (7) and its carry
  recurrence. No finite-state quotient or reset property is imported.
- The signed difference recurrence, borrow identities, valuation criterion,
  and real upper bound are rederived here.
- `L-9815` is used only in part 6 to identify `d=D_n(A)` and its
  lexicographically minimizing subtraction word.
- The comparison estimate (36) is included explicitly, so no result from
  `L-9819` is logically required.
- No global Collatz orbit, density assertion, or empirical minimum pattern is
  assumed.

## Gap audit

- The settlement position can exceed the common survived depth `n`; then the
  exact arithmetic identities still hold once both orbits exist that far, but
  no depth-`n` common-suffix conclusion follows.
- Bound (28) is linear in the settlement scale. It is not the sublinear
  valuation estimate that would force a macroscopic directive disagreement
  suffix.
- Lexicographic minimality of the successor digits does not automatically
  bound the high carry avalanche or prevent cancellation in (20).
- The signed chart determines the only possible difference itinerary for a
  gap. It does not guarantee that two individual legal chart orbits realize
  that signed itinerary.
- No bounded reset, finite automaton, or exponential successor-gap theorem is
  proved.

## Adversarial tests

- The borrow signs in (5) matter. With this convention, a continuing high
  carry changes `a_j=63` to `b_j=0`; reversing `A` and `B` reverses the
  formula.
- The high quotients need not agree before `u`. Thus `H_j=Delta_j` is valid at
  settlement, not throughout the low block.
- The signed residue `-1` is represented by `63 modulo 64`, not by an illegal
  directive digit.
- `nu_64` counts complete factors of `64`; it is not `nu_2`, and
  `nu_64(m)=floor(nu_2(m)/6)` only for nonzero integers.
- The gap digits vanish from position `t` onward, but the carry can persist;
  replacing `u` by `t` silently discards the avalanche.
- The successor order is lexicographic from the high subtraction digit down.
  That order alone does not constrain the low-to-high borrow stream.

## Remaining uncertainty

The next useful estimate is a successor-specific improvement of (28), for
example a bound on `ell` together with an upper bound on the extra
divisibility in (20), or a direct theorem that

\[
\nu_{64}(\mathfrak D^u(D_n(A)))=o(n-u)
\]

in a regime where `u<n`. Nothing here establishes such an asymptotic claim.

## Suggested next attack

Assume the numerator in (20) vanishes modulo a very high power of `64`.
Translate the resulting long zero block in the signed difference itinerary
back through the triangular cylinder formula. Then test whether changing the
first high signed digit after that block produces a positive legal cyclic
difference whose high-to-low subtraction word is smaller than the successor
word. Such an exchange argument is the natural place where the lexicographic
minimality from `L-9815` can add information beyond the general pair bound.
