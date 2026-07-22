# L-9900 -- Fixed-rank two-endpoint Evertse budget lemma

Claim ID: `L-9900`
Title: A subunit outside-prime budget on two moving endpoints forbids an infinite fixed-rank family of nondegenerate zero sums
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: J.-H. Evertse, *On sums of S-units and linear recurrences*, Compositio Mathematica 53 (1984), Corollary 1
Scope: fixed-dimensional rational-integer zero sums with fixed internal prime support
Related claims: local `T-9828`; live PR #33

## Definitions

For a finite set `S_0` of rational primes and a nonzero integer `a`, put

\[
 \operatorname{out}_{S_0}(a)
 =|a|\prod_{p\in S_0}|a|_p.
\tag{1}
\]

This is the positive integer part of `|a|` supported outside `S_0`.  In
particular,

\[
 \operatorname{out}_{S_0}(a)=1
\tag{2}
\]

exactly when `a` is an integer `S_0`-unit.

## Statement

Fix:

- an integer `r>=1`;
- a finite prime set `S_0`;
- a constant `G>=1`; and
- an exponent `0<d<1`.

Suppose infinitely many indices `m` produce a raw integer tuple

\[
 a_m=(e_{m,0},e_{m,1},s_{m,1},\ldots,s_{m,r})
 \in(\mathbf Z\setminus\{0\})^{r+2}
\tag{3}
\]

with the following properties.

### 1. Minimal zero sum by signs

\[
 \sum_{k=0}^{r+1}a_{m,k}=0,
\tag{4}
\]

and exactly one coordinate is positive while every other coordinate is
strictly negative.

### 2. Fixed internal prime support

For every `1<=j<=r`,

\[
 \operatorname{out}_{S_0}(s_{m,j})=1.
\tag{5}
\]

The internal `S_0`-unit exponents may vary with `m`; only their number and
prime support are fixed.

### 3. Bounded normalization loss

Writing

\[
 g_m=\gcd(|a_{m,0}|,\ldots,|a_{m,r+1}|),
\tag{6}
\]

assume

\[
 g_m\le G.
\tag{7}
\]

### 4. A raw projective-height scale

There are real numbers `H_m>1`, with `H_m->infinity`, such that

\[
 \max_k|a_{m,k}|\ge H_m.
\tag{8}
\]

### 5. Two-endpoint outside-prime budget

There are `B_(m,0),B_(m,1)>=1` satisfying

\[
 \operatorname{out}_{S_0}(e_{m,i})\le B_{m,i}
 \qquad(i=0,1),
\tag{9}
\]

and

\[
 \Theta:=
 \limsup_{m\to\infty}
 {\log(B_{m,0}B_{m,1})\over\log H_m}
 <d.
\tag{10}
\]

A convenient stronger hypothesis is

\[
 \limsup{\log B_{m,0}\over\log H_m}\le\theta_0,
 \qquad
 \limsup{\log B_{m,1}\over\log H_m}\le\theta_1,
 \qquad
 \theta_0+\theta_1<d.
\tag{11}
\]

### 6. Optional explicit projective separator

For two fixed coordinate indices `q!=t`, the ratios

\[
 {a_{m,q}\over a_{m,t}}
\tag{12}
\]

may be used to certify pairwise distinctness.  It suffices that, for some
prime `ell`, their
valuations belong to pairwise disjoint intervals:

\[
 v_\ell\!\left({a_{m,q}\over a_{m,t}}\right)\in I_m,
 \qquad I_m\cap I_{m'}=\varnothing\quad(m\ne m').
\tag{13}
\]

This separator is not an additional hypothesis: (7)--(8) already force the
primitive heights to infinity.  It is recorded because many applications,
including `T-9828`, naturally supply the stronger coordinate-ratio
certificate.

Under conditions 1--5, no such infinite family exists.

## Proof

### Step 1 -- nondegeneracy

Let `P_m>0` be the unique positive coordinate, and write the others as
`-n_(m,j)` with every `n_(m,j)>0`.  Equation (4) gives

\[
 P_m=\sum_jn_{m,j}.
\tag{14}
\]

A nonempty subset omitting `P_m` has negative sum.  A proper subset containing
`P_m` omits at least one negative coordinate, so its sum is

\[
 P_m-\sum_{j\in J}n_{m,j}
 =\sum_{j\notin J}n_{m,j}>0.
\tag{15}
\]

Therefore no nonempty proper subsum vanishes.

### Step 2 -- primitive normalization

Put

\[
 x_{m,k}={a_{m,k}\over g_m}.
\tag{16}
\]

Then `x_m` is a primitive integer tuple with the same zero sum and sign
pattern.

Because `r>=1`, the gcd `g_m` divides at least one internal `S_0`-unit.
Consequently every prime divisor of `g_m` belongs to `S_0`, and

\[
 \operatorname{out}_{S_0}(g_m)=1.
\tag{17}
\]

Thus normalization does not change outside-`S_0` content:

\[
 \operatorname{out}_{S_0}(x_{m,k})
 =\operatorname{out}_{S_0}(a_{m,k}).
\tag{18}
\]

Every primitive internal coordinate still has outside content one, and

\[
 \prod_{k=0}^{r+1}\operatorname{out}_{S_0}(x_{m,k})
 \le B_{m,0}B_{m,1}.
\tag{19}
\]

The primitive projective height satisfies

\[
 \|x_m\|
 =\max_k|x_{m,k}|
 ={\max_k|a_{m,k}|\over g_m}
 \ge {H_m\over G}.
\tag{20}
\]

### Step 3 -- absorb the fixed gcd with `c=1`

Choose

\[
 \varepsilon={d-\Theta\over2}>0.
\tag{21}
\]

By (10), for all sufficiently large `m`,

\[
 B_{m,0}B_{m,1}\le H_m^{d-\varepsilon}.
\tag{22}
\]

Since `H_m->infinity`, eventually

\[
 H_m^\varepsilon\ge G^d.
\tag{23}
\]

Equations (19)--(23) give

\[
 \begin{aligned}
 \prod_{k=0}^{r+1}\operatorname{out}_{S_0}(x_{m,k})
 &\le H_m^{d-\varepsilon}\\
 &\le {H_m^d\over G^d}\\
 &\le\|x_m\|^d.
 \end{aligned}
\tag{24}
\]

Thus every sufficiently late primitive tuple is `(1,d,S_0)`-admissible in
Evertse's rational-integer formulation.

### Step 4 -- infinitely many primitive projective points

Equation (20) and `H_m->infinity` give `||x_m||->infinity`.  A rational
projective point has only the two primitive integer representatives `+/-x`,
both of the same fixed norm.  Therefore the primitive tuples already contain
infinitely many distinct projective points.

When the optional ratio certificate is available, division by `g_m` cancels
from every coordinate ratio:

Division by `g_m` cancels from every coordinate ratio:

\[
 {x_{m,q}\over x_{m,t}}
 ={a_{m,q}\over a_{m,t}}.
\tag{25}
\]

Condition (12), or the valuation certificate (13), can therefore make the
primitive tuples pairwise projectively distinct without first passing to a
subsequence.

### Step 5 -- Evertse contradiction

The tuples have fixed source dimension

\[
 n=r+1,
\tag{26}
\]

are primitive, satisfy a zero sum with no proper vanishing subsum, and obey
(24) for fixed

\[
 c=1,
 \qquad0<d<1,
 \qquad S_0.
\tag{27}
\]

Evertse's Corollary 1 permits only finitely many such primitive tuples.  Step
4 produces infinitely many.  This contradiction proves the lemma. **QED**

## Sharpness and weakenings

The one-positive hypothesis is not essential.  It may be replaced exactly by

\[
 \sum_{k\in J}a_{m,k}\ne0
\tag{28}
\]

for every nonempty proper coordinate set `J`.  One negative coordinate and
all others positive is also sufficient by global sign reversal.

Some nondegeneracy condition is essential.  Without it,

\[
 (2^m,-2^m,1,-1)
\tag{29}
\]

for `S_0={2}` is an infinite, primitive, projectively distinct family with
zero outside-`S_0` budget, but it contains proper vanishing subsums.

The sharp asymptotic budget for this method is

\[
 \Theta<1.
\tag{30}
\]

Indeed, one may then choose any fixed `d` with `Theta<d<1`.  For a preassigned
`d`, condition `Theta<d` automatically yields the eventual constant `c=1`.
If instead one has the uniform boundary estimate

\[
 B_{m,0}B_{m,1}\le C H_m^d,
\tag{31}
\]

equality of exponents is still allowed: Evertse applies with the fixed
constant

\[
 c=CG^d.
\tag{32}
\]

Thus strictness is needed to infer a fixed constant from exponent data alone,
not because Evertse requires `c=1`.

The ratio separator is sufficient rather than necessary.  Under the stated
bounded-gcd and growing-height hypotheses, primitive-height divergence already
proves that infinitely many projective points occur.

## Exact specialization to `T-9828`

For either the cap or co-cap orientation in `T-9828`, take

\[
 r=256,
 \qquad n=257,
 \qquad S_0=\{2,3\}.
\tag{33}
\]

The two raw endpoints are, up to orientation,

\[
 2^{E_m}U_{m+1},
 \qquad -3^{A_m}U_m,
\tag{34}
\]

and the internal coordinates are

\[
 -b_{m,j}2^{u_{m,j}}3^{v_{m,j}},
 \qquad0\le j\le255.
\tag{35}
\]

Hence every internal coordinate is a `{2,3}`-unit, and the stage relation has
exactly one positive coordinate.

The endpoint conditions `u_(m,0)=0` and `v_(m,255)=0` give

\[
 v_2(g_m)\le3,
 \qquad v_3(g_m)\le3,
 \qquad G=216.
\tag{36}
\]

Choose

\[
 H_m=2^{E_m}.
\tag{37}
\]

The tuple contains `2^(E_m)U_(m+1)`, and `U_(m+1)>=1`, so (8) holds.
Since multiplication by powers of two or three does not change
outside-`{2,3}` content, take

\[
 B_{m,0}=U_m,
 \qquad B_{m,1}=U_{m+1}.
\tag{38}
\]

The reconstructed endpoint bounds give

\[
 \theta_0={2166\over346819},
 \qquad
 \theta_1={4332\over346819},
\tag{39}
\]

and therefore

\[
 \Theta\le{6498\over346819}<{1\over50}=d.
\tag{40}
\]

The exact gap is

\[
 d-\Theta\ge{21919\over17340950}>0.
\tag{41}
\]

Finally, compare the coordinate containing `2^(E_m)U_(m+1)` with the `j=0`
internal coordinate.  Their ratio has 2-adic valuation in

\[
 [E_m-3,E_m+3].
\tag{42}
\]

Because

\[
 E_{m+1}-E_m={8459\over2}2^m>6,
\tag{43}
\]

these intervals are pairwise disjoint.  This supplies an explicit projective
separator, stronger than the primitive-height divergence already sufficient
for Evertse.

Thus `T-9828` is an exact specialization with

\[
 (r,S_0,G,H_m,d)
 =\left(256,\{2,3\},216,2^{E_m},{1\over50}\right).
\tag{44}
\]

Its signed quotient and endpoint-height arguments establish the inputs to this
lemma; the lemma then replaces its primitive normalization, admissibility,
nondegeneracy, and projective-finiteness steps verbatim.

## Dependency and gap audit

- Evertse's Corollary 1 is the only external input.
- The lemma permits arbitrary variation of the internal `S_0`-unit exponents
  and endpoint integers, but the number of coordinates and `S_0` are fixed.
- The bounded gcd hypothesis is used only to compare raw scale `H_m` with
  primitive height.  A subpower bound could be absorbed by reducing the
  available exponent gap.
- The two-endpoint formulation extends verbatim to any fixed number of moving
  endpoints by replacing their product in (10).
- The sign pattern is only a transparent sufficient certificate for
  nondegeneracy.  It is not a theorem requirement.
- The optional ratio separator is useful for local auditing but logically
  redundant once primitive height is known to tend to infinity.
- No conclusion follows at `Theta>=1` from this method because Evertse requires
  `d<1`.
