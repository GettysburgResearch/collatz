# T-9809 -- Three toll symbols leave at most sixty-four rooms

Claim ID: `T-9809`
Title: The shortest dyadic toll prefix which outruns the fixed-room scale has length three, so at most 64 eventual rooms survive
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave15-period-ten`
Reviewing agents: `gpt56-synthesis-01-wave14-quant-fresh-primes`; `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: branch-qualified `PR3/L-0025`, `L-0031`, and `T-0033` at `c37e96efd0dcc9dd610d59041234dc57e74090fd`; local `T-9808`
Scope: eventual positive ordinary tails in the stabilized corrected 256-transition phase-34 stage architecture
Related counterexample candidates: none

## Setup

Fix `m>=12`, put

\[
 B=2^m,
 \qquad
 D_m={B\over256}=2^{m-8},
\tag{1}
\]

and use the corrected heights

\[
 t_{m,j}=D_m(256+j)
 \qquad(0\le j\le256).
\tag{2}
\]

For `0<=q<=256`, the binary prefix exponent of `PR3/L-0031` is

\[
 U_{m,q}
 =11\sum_{r=1}^q(t_{m,r}+1).
\tag{3}
\]

The positive stage toll and stage equation are

\[
 \mathcal T_m(w)
 =\sum_{k=0}^{255}
 2^{U_{m,k}+\alpha_{i_k}}
 3^{V_{m,k}+\beta_{i_k}},
\tag{4}
\]

\[
 2^{\mathcal E_m}W_{m+1}
 =3^{\mathcal A_m}W_m+\mathcal T_m(w_m),
\tag{5}
\]

where

\[
 (\alpha_0,\alpha_1,\alpha_2,\alpha_3)=(0,1,2,3),
 \qquad
 (\beta_0,\beta_1,\beta_2,\beta_3)=(2,3,2,1).
\tag{6}
\]

For an assumed eventual ordinary path, `PR3/T-0033` supplies one real room
`C>0` with

\[
 W_m=\lfloor C H_m\rfloor,
 \qquad
 H_m={3^{a_m}\over2^{e_m}},
\tag{7}
\]

\[
 a_m={5369\over2}2^m+1792m,
 \qquad
 e_m={8459\over2}2^m+2816m.
\tag{8}
\]

Let `mathscr C` denote the set of rooms which support such an eventual path,
with the starting scale allowed to depend on the room.

## Theorem 1 -- exact prefix growth and the minimal length

For every `q`, equation (3) has the closed form

\[
 \boxed{
 U_{m,q}
 =11\left\{
 \left(256q+{q(q+1)\over2}\right)D_m+q
 \right\}.
 }
\tag{9}
\]

In particular,

\[
 \boxed{
 U_{m,2}={5665\over256}2^m+22,
 \qquad
 U_{m,3}={4257\over128}2^m+33.
 }
\tag{10}
\]

Their positions relative to the room scale are opposite:

\[
 \boxed{
 U_{m,3}-\log_2H_m\longrightarrow+\infty,
 \qquad
 U_{m,2}-\log_2H_m\longrightarrow-\infty.
 }
\tag{11}
\]

More precisely,

\[
 U_{m,3}-\log_2H_m
 >{35913\over5248}2^m+33-{1024\over41}m,
\tag{12}
\]

and

\[
 \log_2H_m-U_{m,2}
 >{41387\over13568}2^m+{1280\over53}m-22.
\tag{13}
\]

Consequently, for every fixed `K>0`, eventually

\[
 \boxed{K H_m<2^{U_{m,3}},}
\tag{14}
\]

whereas

\[
 \boxed{{2^{U_{m,2}}\over K H_m}\longrightarrow0.}
\tag{15}
\]

Since `U_(m,1)<U_(m,2)`, the prefix length `q=3` is the unique shortest
positive length whose dyadic modulus eventually dominates `K H_m` for every
fixed `K`.  This minimality concerns the single-scale prefix-modulus
pigeonhole used below; it does not exclude a different argument combining
several scales or additional congruences.

### Proof

Summing (2) for `1<=r<=q` gives

\[
 \sum_{r=1}^q(t_{m,r}+1)
 =\left(256q+{q(q+1)\over2}\right)D_m+q,
\tag{16}
\]

which proves (9)--(10).

The exact integer comparisons in `PR3/L-0025` are

\[
 3^{53}>2^{84},
 \qquad
 3^{41}<2^{65}.
\tag{17}
\]

They are directly checkable from

\[
 3^{53}=19383245667680019896796723
 >19342813113834066795298816=2^{84},
\]

\[
 3^{41}=36472996377170786403
 <36893488147419103232=2^{65}.
\]

Thus

\[
 \boxed{{84\over53}<\log_2 3<{65\over41}.}
\tag{18}
\]

From (7)--(8),

\[
 \log_2H_m
 ={5369\log_2 3-8459\over2}2^m
 +(1792\log_2 3-2816)m.
\tag{19}
\]

The upper bound in (18) gives

\[
 \log_2H_m
 <{1083\over41}2^m+{1024\over41}m.
\tag{20}
\]

Subtracting (20) from the `q=3` identity in (10) and using

\[
 {4257\over128}-{1083\over41}
 ={35913\over5248}>0
\tag{21}
\]

proves (12) and the first limit in (11).

The lower bound in (18) similarly gives

\[
 \log_2H_m
 >{2669\over106}2^m+{1280\over53}m.
\tag{22}
\]

Now

\[
 {2669\over106}-{5665\over256}
 ={41387\over13568}>0,
\tag{23}
\]

so subtracting the `q=2` identity in (10) proves (13) and the second limit in
(11).  Adding or subtracting the fixed number `log_2 K` does not change either
limit.  This proves (14)--(15), and monotonicity of `U_(m,q)` in `q` proves the
minimality assertion. **QED**

## Theorem 2 -- three-symbol incoming addresses

For a three-symbol prefix

\[
 \mathbf i=(i_0,i_1,i_2)\in\{0,1,2,3\}^3,
\tag{24}
\]

define its truncated toll

\[
 \mathcal T_m^{[3]}(\mathbf i)
 =\sum_{k=0}^{2}
 2^{U_{m,k}+\alpha_{i_k}}
 3^{V_{m,k}+\beta_{i_k}},
\tag{25}
\]

and its incoming address

\[
 \boxed{
 \rho_m^{[3]}(\mathbf i)
 =\left[-3^{-\mathcal A_m}
 \mathcal T_m^{[3]}(\mathbf i)
 \right]_{2^{U_{m,3}}}.
 }
\tag{26}
\]

Here brackets mean the least nonnegative residue, and
`3^(-mathcal A_m)` is the inverse of the odd unit `3^(mathcal A_m)` modulo
`2^(U_(m,3))`.

The 64 addresses in (26) are pairwise distinct.  Every valid stage satisfies

\[
 \boxed{
 W_m\equiv
 \rho_m^{[3]}(i_{m,0},i_{m,1},i_{m,2})
 \pmod {2^{U_{m,3}}}.
 }
\tag{27}
\]

Thus the incoming boundary residue modulo `2^(U_(m,3))` determines exactly
the first three stage symbols.

### Proof

Every toll term with `k>=3` is divisible by `2^(U_(m,3))`, so the full toll
and (25) have the same residue.  If two prefixes first differ at `k<3`, their
first unequal toll-term difference has valuation

\[
 U_{m,k}+\min\{\alpha_{i_k},\alpha_{i'_k}\}
 <U_{m,k+1}\le U_{m,3}.
\tag{28}
\]

Here distinctness of the four `alpha` values makes the first valuation unique,
and all powers of three are odd.  Every later difference is divisible by
`2^(U_(m,k+1))`, so it cannot cancel (28).  The truncated toll residues are
therefore distinct.  Multiplication by the odd unit
`-3^(-mathcal A_m)` preserves distinctness.

Finally, reduce (5) modulo `2^(U_(m,3))`.  Since
`U_(m,3)<mathcal E_m`, its left side vanishes, and the resulting congruence is
exactly (27). **QED**

## Theorem 3 -- the sharp prefix-method room bound

The eventual room set satisfies

\[
 \boxed{\#\mathscr C\le4^3=64.}
\tag{29}
\]

One room determines at most one eventual boundary-tail and full stage-word
tail.  Hence eventual tails, modulo deletion of a finite initial segment, also
have cardinality at most 64.

### Proof

Suppose for contradiction that `mathscr C` contains 65 distinct rooms

\[
 C_1,\ldots,C_{65}.
\tag{30}
\]

Put

\[
 K=1+\max_j C_j,
 \qquad
 d=\min_{r\ne s}|C_r-C_s|>0.
\tag{31}
\]

Choose one scale `m` beyond all 65 starting scales and so large that

\[
 K H_m<2^{U_{m,3}},
 \qquad
 H_m^{-1}<d.
\tag{32}
\]

The first inequality is Theorem 1.  The second is possible because the lower
bound (22) makes `H_m` tend to infinity.  For each selected room, the floor
law gives

\[
 0\le W_m=\lfloor C_jH_m\rfloor<2^{U_{m,3}}.
\tag{33}
\]

Equation (27) therefore forces `W_m` to equal one of the 64 least residues
`rho_m^[3](i)`.  Consequently every `C_j` lies in one of the 64 half-open
intervals

\[
 \boxed{
 I_m(\mathbf i)
 =\left[
 {\rho_m^{[3]}(\mathbf i)\over H_m},
 {\rho_m^{[3]}(\mathbf i)+1\over H_m}
 \right).
 }
\tag{34}
\]

Each interval has diameter `H_m^(-1)<d`, so it contains at most one of the
65 selected rooms.  This contradicts the existence of only 64 prefixes and
proves (29).

For a fixed room, (7) determines every sufficiently late integer `W_m`.
The full-word decoder of `T-9808/Theorems 1--2`, which is the same valuation
argument as Theorem 2 with `q=256`, determines the entire word `w_m` from
`W_m mod 2^(mathcal E_m)`.  Thus one room supports at most one eventual tail
in both coordinate systems. **QED**

## What this advances

- `T-9808` used the full 256-symbol modulus `2^(mathcal E_m)` and obtained
  `4^256` rooms.  Only the first three toll symbols are needed for the room
  pigeonhole, improving the bound exactly to 64.
- The improvement is not a looser asymptotic estimate: Theorem 1 proves that
  three is the shortest prefix whose modulus dominates every fixed finite
  collection's boundary scale.  The two-symbol modulus is exponentially
  smaller than `H_m`.
- The other 253 symbols remain relevant to connector and seam validity, but
  they no longer contribute to the cardinality of the eventual room set.

## Dependency and novelty audit

- `PR3/L-0031` supplies the exact positive toll, the prefix exponents, and the
  stage equation.  The prefix-growth comparison and the 64-room conclusion
  are new here.
- `PR3/T-0033` supplies only the conditional fixed-room floor law and the
  exact scale `H_m`.  Its shrinking fractional-defect estimate is not used.
- `PR3/L-0025` supplies the exact integer comparisons in (17).  They are
  restated explicitly so every strict asymptotic sign can be checked locally.
- Local `T-9808` supplies the general lossless toll decoder and full-word
  uniqueness.  The three-symbol specialization and its exact minimality are
  proved again here.
- No S-unit theorem, PR #34 seam theorem, or computation is a proof
  dependency.  Those constraints can only remove rooms from the set counted
  here.

## Gap and scope audit

- Minimality of `q=3` is specific to domination of `K H_m` by one dyadic
  prefix modulus.  It is not a lower bound on every conceivable room-counting
  argument; several scales or odd-prime information might improve 64.
- The theorem is conditional on the proposed PR #3 stage equation and
  fixed-room law.  It does not promote either source claim.
- A set of at most 64 rooms can be nonempty.  No room, ordinary
  initialization, cap stitch, or Collatz counterexample is constructed or
  excluded.
- The first three decoded types do not certify the remaining 253 types,
  collars, connectors, or triple seams.  Full validity still requires all
  native checks.
- The bound is cardinal, not effective: it does not list the rooms or decide
  whether any supports an infinite tail.

## Adversarial and bounded exact checks

- Exact substitution in (9) gives
  `U_(m,2)=5665*2^(m-8)+22` and
  `U_(m,3)=8514*2^(m-8)+33` for every tested `12<=m<=40`.
- Direct integer replay verified both inequalities in (17), all rational
  simplifications in (20)--(23), and the signs in (12)--(13).
- Exhaustive exact modular replay of all 64 prefixes at `m=12` found 64
  distinct truncated toll residues and decoded every prefix by successive
  `2`-adic valuations.
- The ratio `2^(U_(m,2))/H_m` decreases across every tested
  `12<=m<=40`, while `2^(U_(m,3))/H_m` increases.  This finite check supports
  the exact asymptotic proof but is not a dependency.
- The room contradiction uses a room-dependent finite `K` only after 65
  rooms are selected; it does not assume a uniform bound over all possible
  rooms.

## Suggested next attack

At one late scale there are now only 64 possible room intervals, indexed by
the first three source types.  Intersect each interval with the two-level head
cell hierarchy of `T-9806`, then decode the remaining word and test the 84
triple seams.  Any argument eliminating all four choices of the fourth symbol
uniformly over one surviving three-symbol interval removes that room class.
