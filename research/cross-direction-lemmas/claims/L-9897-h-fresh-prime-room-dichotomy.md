# L-9897 -- H bridges obey a fresh-prime or room dichotomy

Claim ID: `L-9897`
Title: Fixed prime support occurs only finitely often on a nonperiodic exact H chain
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-a`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `L-9889`, `L-9894`; standard nondegenerate S-unit finiteness theorem for Statement 5
Scope: successive positive H renewal bridges; Statement 5 assumes a positive nonperiodic infinite exact H chain
Related counterexample candidates: none

## Setup

At renewal index `k`, use the notation of `L-9894`:

\[
a=L_{k-1},
\qquad b=L_k,
\qquad R=R_k,
\qquad U=U_k,
\tag{1}
\]

\[
X=W_{k-1},
\qquad Y=W_k.
\tag{2}
\]

Thus `X` arrives at the central nonzero state and `Y` departs from it.  All
of `U,X,Y` are positive and coprime to `6`.  Define

\[
G_k=\gcd(X,Y),
\qquad
E_k={X\over G_k},
\qquad
F_k={Y\over G_k}.
\tag{3}
\]

The factor `F_k` is the forward exponent-increment factor after removing the
shared core.  Its prime factors need not be globally new.

## Statement 1 -- primitive compatibility and telescoping balance

The primitive parts satisfy

\[
\gcd(E_k,F_k)=1
\tag{4}
\]

and the exact factored compatibility law

\[
\boxed{
G_k\left(8^R4^bF_k-9^R3^aE_k\right)
=9^R-8^R.
}
\tag{5}
\]

In particular,

\[
\boxed{G_k\mid9^R-8^R.}
\tag{6}
\]

For the logarithmic form `Lambda_k` of `L-9894/(19)`, there is an exact
positive toll

\[
\boxed{
\log F_k-\log E_k
=\Lambda_k+\epsilon_k,
\qquad
0<\epsilon_k<{1\over3^aX}.
}
\tag{7}
\]

Consequently, on every finite interval of renewal transitions,

\[
\boxed{
\sum_{k=m}^{n}(\log F_k-\log E_k)
=\log W_n-\log W_{m-1}.
}
\tag{8}
\]

Thus even divergent forward increment mass can be cancelled by later
primitive divisor loss; `sum log F_k` alone is not a growth theorem for
`W_k`.

### Proof

Equation (4) is immediate from (3).  Substitute `X=G_kE_k` and `Y=G_kF_k`
in `L-9894/(6)` to obtain (5)--(6).  Since

\[
{F_k\over E_k}={Y\over X},
\tag{9}
\]

equation `L-9894/(20)` and its toll bound `L-9894/(25)` give (7).  Summing
`log(Y/X)=log(W_k/W_(k-1))` proves (8). **QED**

## Statement 2 -- exact prime-exponent persistence tax

Fix a prime `ell>=5` and put

\[
x=v_\ell(X),
\qquad y=v_\ell(Y),
\qquad g=\min(x,y),
\qquad d=v_\ell(9^R-8^R).
\tag{10}
\]

Then

\[
\boxed{d\ge g,}
\tag{11}
\]

and whenever the adjacent exponents differ,

\[
\boxed{x\ne y\quad\Longrightarrow\quad d=g.}
\tag{12}
\]

Let

\[
h_\ell=\operatorname {ord}_{\ell}(9/8),
\qquad
\lambda_\ell=v_\ell(9^{h_\ell}-8^{h_\ell}).
\tag{13}
\]

If `h_ell` divides `R`, odd-prime LTE and order lifting give

\[
\boxed{
d=\lambda_\ell+v_\ell(R/h_\ell),
}
\tag{14}
\]

\[
\boxed{
\operatorname {ord}_{\ell^e}(9/8)
=h_\ell\ell^{(e-\lambda_\ell)^+}.
}
\tag{15}
\]

Therefore the whole shared core pays the exact simultaneous order condition

\[
\boxed{
\operatorname {ord}_{G_k}(9/8)
=\operatorname {lcm}_{\ell^e\parallel G_k}
 h_\ell\ell^{(e-\lambda_\ell)^+}
\mid R_k.
}
\tag{16}
\]

More sharply, if `x!=y` and `g>0`, then

\[
\boxed{
g\ge\lambda_\ell,
\qquad
v_\ell(R/h_\ell)=g-\lambda_\ell.
}
\tag{17}
\]

An exponent change therefore saturates exactly the valuation cost of the
reused prime power.

### Proof

In `L-9894/(6)`, the two left-hand terms have `ell`-adic valuations `y` and
`x`, because `ell>=5`.  Their difference is divisible by `ell^g`, proving
(11).  If `x!=y`, the lesser valuation is unique and the ultrametric
inequality gives equality, proving (12).

When `h_ell|R`, odd-prime LTE proves (14); the standard order-lifting formula
then gives (15).  Apply it prime-power by prime-power to (6) and take the lcm
to prove (16).  If `g>0` and `x!=y`, equation (6) implies `h_ell|R`, while
(12) and (14) give (17). **QED**

## Statement 3 -- every transition pays in room or forward increment

Every central transition satisfies the strict local bound

\[
\boxed{
U_k<4^{L_k}F_k.
}
\tag{18}
\]

For each fixed `0<=theta<=1`, at least one of the following holds:

\[
\boxed{L_k\log4\ge\theta\log U_k,}
\tag{19}
\]

\[
\boxed{\log F_k>(1-\theta)\log U_k.}
\tag{20}
\]

In particular, either the next zero room has logarithmic length at least half
the central-core size, or

\[
F_k>\sqrt {U_k}.
\tag{21}
\]

The universally valid positive-part form is

\[
\boxed{
(\log U_k-L_k\log4)^+\le\log F_k.
}
\tag{22}
\]

The inequality in (22) cannot be made strict when `F_k=1`, because both
sides can then be zero.

### Proof

From (6), `G_k<=9^R-8^R`.  The second central equation of `L-9894/(4)` gives

\[
\begin{aligned}
9^RU_k
&=1+4^bY\\
&=1+4^bG_kF_k\\
&\le1+4^b(9^R-8^R)F_k\\
&<9^R4^bF_k.
\end{aligned}
\tag{23}
\]

Division proves (18).  If (19) fails, take logarithms in (18) to get (20).
The choice `theta=1/2` gives (21).  Taking the positive part gives (22), with
the stated equality caveat. **QED**

## Statement 4 -- fresh-free run rigidity

If

\[
F_k=1,
\tag{24}
\]

then

\[
W_k\mid W_{k-1}.
\tag{25}
\]

On an interval where every `F_k=1`, each strict drop has quotient

\[
E_k\ge5.
\tag{26}
\]

Hence a run starting from the core `W` contains at most

\[
\boxed{
\Omega(W)\le\log_5W
}
\tag{27}
\]

strict drops, where `Omega` counts prime factors with multiplicity; every
other transition is a plateau.  At a plateau
`W_(k-1)=W_k=W`,

\[
\boxed{
W\mid9^{R_k}-8^{R_k},
\qquad
\operatorname {ord}_{W}(9/8)\mid R_k,
}
\tag{28}
\]

and

\[
\boxed{
W\left(
8^{R_k}4^{L_k}
-9^{R_k}3^{L_{k-1}}
\right)
=9^{R_k}-8^{R_k}.
}
\tag{29}
\]

### Proof

If `F_k=1`, then `Y=G_k` and `X=G_kE_k`, proving (25).  A strict quotient
`E_k>1` is coprime to `6`, hence at least `5`; every strict drop consumes at
least one prime factor with multiplicity, proving (26)--(27).  Equations
(28)--(29) are (6), (16), and (5) specialized to `E_k=F_k=1`. **QED**

## Statement 5 -- global finite-support exclusion for bridge cores

Assume a positive nonperiodic infinite exact H chain and its infinite renewal
sequence.  For every fixed finite set of primes `mathcal S`, there are only
finitely many central transitions with

\[
\boxed{
\operatorname {supp}(W_{k-1}W_k)\subseteq\mathcal S.
}
\tag{30}
\]

Consequently the bridge cores `W_k` have infinite prime support.

Define the genuinely globally new factor

\[
P_k^{\rm new}
=\prod_{\substack{
\ell\mid W_k\\
\ell\nmid W_0W_1\cdots W_{k-1}}}
\ell^{v_\ell(W_k)}.
\tag{31}
\]

for `k>=1`.

Then

\[
\boxed{P_k^{\rm new}\mid F_k,}
\tag{32}
\]

infinitely many of the factors in (31) exceed one, and

\[
\boxed{
\sum_k\log P_k^{\rm new}=\infty,
\qquad
\sum_k\log F_k=\infty,
\qquad
\log P_k^{\rm new}\le\log F_k
}
\tag{33}
\]

### Proof

Normalize the successive-core compatibility equation as

\[
\boxed{
-4^bY
 +3^a(9/8)^RX
 +(9/8)^R
=1.
}
\tag{34}
\]

If (30) holds, all three left-hand terms lie in the finitely generated
multiplicative group

\[
\Gamma=\langle-1,2,3,\mathcal S\rangle.
\tag{35}
\]

Equation (34) is nondegenerate.  The two positive terms cannot have zero
sum.  A zero subsum of the negative term with the second term would require

\[
4^bY=3^a(9/8)^RX,
\tag{36}
\]

while a zero subsum with the third would require

\[
4^bY=(9/8)^R.
\tag{37}
\]

In both cases the left side has `2`-adic valuation `2b>0`, while the right
side has valuation `-3R<0`.  Both are impossible.

The standard nondegenerate three-variable S-unit finiteness theorem now gives
only finitely many triples

\[
\left(
-4^bY,
\ 3^a(9/8)^RX,
\ (9/8)^R
\right).
\tag{38}
\]

Each triple uniquely recovers the full central state data:

- the third coordinate determines `R`;
- the `2`-adic valuation of the first determines `b`, then its value
  determines `Y`;
- after `R` is known, the `3`-adic valuation of the second determines `a`,
  then its value determines `X`;
- the equation `3^aX+1=8^RU` determines `U`.

Therefore only finitely many exact central states

\[
p_{t_k}=2^{3R_k+2}U_k
\tag{39}
\]

occur among transitions satisfying (30).  Infinitely many such indices would
repeat a state of the deterministic orbit and make it eventually periodic,
contrary to hypothesis.  This proves the finite-support assertion.

If a prime appears for the first time in `W_k`, it does not divide
`W_(k-1)` and its full power in `W_k` survives division by `G_k`.  This proves
(32).  Infinite prime support gives infinitely many nontrivial factors
`P_k^(new)`; each is at least five, so their logarithms have divergent sum.
The termwise divisibility (32) forces the second divergence in (33). **QED**

## What this advances

- `L-9894` restricted every reused prime power separately.  Equations
  (14)--(17) now give the exact valuation price when a reused exponent
  changes.
- The room-or-increment law forces every central core to be paid for locally,
  while (8) records why forward mass can still disappear later.
- Statement 5 proves the first global prime-support theorem for the `W`
  bridge cores: no finite alphabet of primes can recur infinitely often on a
  nonperiodic exact chain.
- The result isolates sparsity as the remaining escape.  Globally new primes
  must occur infinitely often, but they may occur too sparsely for the
  inherited exponentially discounted budgets to notice.

## Dependency audit

- `L-9894` supplies the central equations, compatibility law, logarithmic
  toll, and shared-prime firewall.
- `L-9889` supplies the infinite renewal sequence if Statement 5 is applied
  to a hypothetical nontrivial positive survivor rather than assumed
  directly.
- Equations (14)--(17) use elementary odd-prime LTE and the standard lifting
  formula for multiplicative orders.
- Statement 5 imports the standard nondegenerate S-unit finiteness theorem,
  the same external ingredient used in `PR19/L-9507`.  It remains a named
  external dependency pending citation-level review.
- No conclusion from conditional `PR19/T-9509` is used.

## Gap audit

- The theorem does not exclude a nonperiodic exact H chain.  New primes may
  arrive at arbitrarily sparse renewal indices.
- The divergent sum in (33) is unweighted.  It is compatible with the
  exponentially discounted core budget of `PR19/T-9505`.
- A large `F_k` can later be cancelled by `E_j`; equation (8) explicitly
  prevents treating fresh mass as monotone core growth.
- Finite central CRT universality in `L-9894` is unaffected.  It builds one
  algebraic central star, not completed outer bridges or an infinite
  fixed-support chain.
- Statement 5 is conditional on an infinite exact chain and the external
  S-unit theorem.  It is not an existence theorem for such a chain.

## Adversarial checks

- `F_k` removes only the prime powers shared with `W_(k-1)`; it is not itself
  the globally new factor `P_k^(new)`.
- Equality `d=g` in (12) requires unequal adjacent exponents.  Equal
  exponents may acquire extra cancellation in the compatibility equation.
- The lcm in (16), rather than the product, is the exact composite order.
- The positive-part inequality in (22) is weak at `F_k=1`; writing it as a
  universal strict inequality would be false.
- The S-unit equation has three variables on the left.  Nondegeneracy is
  checked explicitly before invoking its finiteness theorem.
- A repeated central integer state, not merely a repeated `W` plateau, is
  what forces deterministic periodicity.

## Remaining uncertainty

Can globally new prime arrivals be shown to have positive discounted mass, or
can long `F_k=1` runs be converted from resonant plateaux into repeated full
states?  Either strengthening would confront the remaining sparse-support
escape.

## Suggested next attack

Combine (17) with lower bounds for
`ord_(ell^e)(9/8)` across successive plateaux, and compare the resulting
divisibility of `R_k` with the renewal capital law.  Alternatively, seek a
quantitative S-unit height bound that turns Statement 5's qualitative
finiteness into an explicit recurrence horizon.
