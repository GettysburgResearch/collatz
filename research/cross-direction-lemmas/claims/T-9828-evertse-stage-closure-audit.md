# T-9828 -- The corrected-stage Evertse closure survives source audit

Claim ID: `T-9828`
Title: The frozen corrected 256-stage interface excludes every signed ordinary completion by Evertse admissibility
Status: `PROPOSED / SOURCE-QUALIFIED CONDITIONAL RECONSTRUCTION`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave14-period-ten`; `gpt56-synthesis-01-wave16-completion-cold-review`; `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: frozen PR #33 head `c9d62bce3e93f5785f72e4520bc576863d9379eb`; frozen PR #3 `L-0028`, `T-0027` at head `f274dfeee3c9c391c48e58d8b57cb9f1759236f8`; Evertse 1984, Corollary 1
Scope: the physically overlapping corrected 256-transition directives represented by the frozen source interfaces
Related counterexample candidates: issue #31; PR #33; no `K-####` candidate

## Purpose and frozen boundary

PR #33 proposes a universal exclusion theorem for the corrected 256-stage
class.  Its last step invokes Corollary 1 of J.-H. Evertse,
[*On sums of S-units and linear recurrences*](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf),
Compositio Mathematica 53 (1984), 225--244.  This claim independently
reconstructs that last proof chain and audits the primary source.

The conclusion below is conditional on the exact corrected-stage and physical
overlap identities frozen at the two heads in the metadata.  In particular,
it does not silently upgrade the native `PROPOSED` status of PR #3's tower
algebra.  Subject to those frozen identities, every remaining arithmetic and
external-theorem interface is proved here.

There is one scope point worth making explicit.  PR #3 `T-0027` phrases its
canonical quotient decomposition for nonnegative inputs and `Y_m>=0`.
The signed extension in (1) instead uses `L-0028/(7)--(10)`: its composite
congruence and exact finite-domain equivalence hold for every ordinary integer,
after which the unique representation `z_m=R_m+Q_mY_m` has `Y_m in Z`.
Thus the negative branch below is justified algebraically, but is not itself a
positive physical Collatz tail.

## Frozen stage data

At scale `m`, a chosen stage word gives the canonical signed tile

\[
 z_m=R_m+Q_mY_m,
 \qquad
 z_{m+1}=S_m+P_mY_m,
\tag{1}
\]

where

\[
 Q_m=2^{D_m},\qquad P_m=3^{A_m},
 \qquad 0\le R_m<Q_m,\qquad0\le S_m<P_m,
\tag{2}
\]

and continuation is

\[
 S_m+P_mY_m=R_{m+1}+Q_{m+1}Y_{m+1}.
\tag{3}
\]

The next-scale precision gap is

\[
 \kappa_m={P_m\over Q_{m+1}}<{1\over4}.
\tag{4}
\]

Writing the normalized stage map as

\[
 z_{m+1}=\Lambda_mz_m+\beta_m,
 \qquad \Lambda_m={3^{A_m}\over2^{D_m}},
\tag{5}
\]

the frozen bounds are

\[
 |\beta_m|<256\Lambda_m,
 \qquad \Lambda_m>257,
\tag{6}
\]

\[
 \log_2\Lambda_m
 <{161341\over10496}2^m+{1024\over41}.
\tag{7}
\]

At stabilized scales, the connector-free endpoint coordinate satisfies one
of the two positive relations

\[
 2^{E_m}U_{m+1}
 =3^{A_m}U_m+
 \sum_{j=0}^{255}b_{m,j}2^{u_{m,j}}3^{v_{m,j}},
\tag{8a}
\]

or

\[
 3^{A_m}U_m
 =2^{E_m}U_{m+1}+
 \sum_{j=0}^{255}b_{m,j}2^{u_{m,j}}3^{v_{m,j}},
\tag{8b}
\]

with

\[
 E_m={8459\over2}2^m+2816,
 \qquad b_{m,j}\in\{9,54,36,24\},
\tag{9}
\]

\[
 u_{m,0}=0,
 \qquad v_{m,255}=0.
\tag{10}
\]

The boundary residues are

\[
 U_m\equiv\pm p_{m}\pmod {64},
 \qquad p_m\in\{5,30,20,56\}.
\tag{11}
\]

Equation (8a) is the cap orientation and (8b) is the co-cap orientation.

## Theorem

For every infinite directive in the frozen corrected-stage class:

1. any signed ordinary stage trajectory eventually has either the permanent
   cap quotient `Y_m=0` or the permanent co-cap quotient `Y_m=-1`;
2. either tail produces infinitely many primitive, nondegenerate integer
   zero sums in 258 coordinates satisfying Evertse's fixed
   `(c,d,S_0)=(1,1/50,{2,3})` inequality;
3. those primitive tuples are pairwise projectively distinct; and
4. consequently the directive's unique 2-adic completion is not in
   `Z`.  Its canonical residue blocks are nonzero infinitely often.

Thus PR #33's `T-9705` conclusion is source-qualified at the frozen head.  No
claim about directives outside that exact interface, and no claim resolving
the Collatz conjecture, is made.

## Proof 1 -- signed quotient extinction

Suppose first that `Y_m>=0`.  Equation (3) has nonnegative left side, so its
canonical next quotient is also nonnegative.  Since `S_m<P_m`,

\[
 0\le Y_{m+1}
 <\kappa_m(Y_m+1)<{Y_m+1\over4}.
\tag{12}
\]

For an integer `Y_m>=1`, the last expression is at most `Y_m/2`; if `Y_m=0`,
it forces `Y_(m+1)=0`.  Hence a nonnegative quotient reaches and stays at
zero.

If `Y_m<=-1`, then `S_m+P_mY_m<0`, so `Y_(m+1)<=-1`.  Put

\[
 K_m=-Y_m-1\ge0.
\tag{13}
\]

Substitution in (3) gives

\[
 Q_{m+1}K_{m+1}
 =P_mK_m+(P_m-S_m)-(Q_{m+1}-R_{m+1}).
\tag{14}
\]

The last parenthesis is at least one, and therefore

\[
 0\le K_{m+1}<\kappa_m(K_m+1)<{K_m+1\over4}.
\tag{15}
\]

Thus `K_m` reaches and stays at zero, equivalently `Y_m=-1`.  The two signs
cannot alternate.  On the two permanent tails, respectively,

\[
 S_m=R_{m+1},
\tag{16a}
\]

\[
 P_m-S_m=Q_{m+1}-R_{m+1}.
\tag{16b}
\]

This proves the signed cap/co-cap dichotomy without imposing positivity on the
initial completion.

## Proof 2 -- endpoint-height constants

Let

\[
 W_m=R_m
\tag{17a}
\]

on a cap tail and

\[
 W_m=Q_m-R_m
\tag{17b}
\]

on a co-cap tail.  Equations (5)--(6) and (16) give, with the sign of
`beta_m` reversed in the co-cap case,

\[
 W_{m+1}+257<\Lambda_m(W_m+257).
\tag{18}
\]

Iterating (18), applying (7), and dividing by `2^m` yields

\[
 \limsup_{m\to\infty}
 {\log_2(W_m+257)\over2^m}
 \le {161341\over10496}.
\tag{19}
\]

The first connector height is

\[
 t_{m,1}={257\over256}2^m,
 \qquad
 H_{m,1}=2^{11(t_{m,1}+1)}.
\tag{20}
\]

For a connector representative `X_m`, the frozen canonical construction has

\[
 0<X_m<64H_{m,1}.
\tag{21}
\]

On a cap tail,

\[
 U_m=X_m+64H_{m,1}W_m
 <64H_{m,1}(W_m+1).
\tag{22a}
\]

On a co-cap tail, `W_m>=1` and

\[
 U_m=64H_{m,1}W_m-X_m
 <64H_{m,1}W_m.
\tag{22b}
\]

The two estimates and (19) give the common bound

\[
 \begin{aligned}
 \limsup {\log_2U_m\over2^m}
 &\le {2827\over256}+{161341\over10496}\\
 &= {1083\over41}.
 \end{aligned}
\tag{23}
\]

Since the leading coefficient of `E_m` is `8459/2`,

\[
 \boxed{
 \limsup {\log_2U_m\over E_m}
 \le {2166\over346819}}
\tag{24}
\]

and shifting the endpoint index doubles the numerator relative to the current
stage height:

\[
 \boxed{
 \limsup {\log_2U_{m+1}\over E_m}
 \le {4332\over346819}.}
\tag{25}
\]

This reconstructs rather than merely copies the two constants used by PR
#33.

## Proof 3 -- primitive nondegenerate tuples

In orientation (8a), form the 258 coordinates

\[
 2^{E_m}U_{m+1},
 \quad -3^{A_m}U_m,
 \quad -b_{m,j}2^{u_{m,j}}3^{v_{m,j}} (0\le j\le255).
\tag{26a}
\]

For (8b), use

\[
 3^{A_m}U_m,
 \quad -2^{E_m}U_{m+1},
 \quad -b_{m,j}2^{u_{m,j}}3^{v_{m,j}} (0\le j\le255).
\tag{26b}
\]

In either case exactly one coordinate is positive and the other 257 are
strictly negative.  A nonempty subset omitting the positive coordinate has
negative sum.  A proper subset containing it has sum equal to the total
magnitude of the omitted negative coordinates and is positive.  Hence no
nonempty proper subsum vanishes.

Let `g_m` be the gcd of the 258 absolute coordinates and divide every
coordinate by `g_m`.  Each internal coordinate is supported only on primes
two and three, so no prime at least five divides `g_m`.  The `j=0` term and
(10) give

\[
 v_2(g_m)\le\max_{b\in\{9,54,36,24\}}v_2(b)=3.
\tag{27}
\]

The `j=255` term gives similarly

\[
 v_3(g_m)\le3.
\tag{28}
\]

Therefore

\[
 \boxed{g_m\mid2^3 3^3=216.}
\tag{29}
\]

The normalized tuple is primitive and remains nondegenerate.

## Proof 4 -- exact Evertse admissibility

For a nonzero integer `x`, define its outside-`{2,3}` content by

\[
 \operatorname{out}_{2,3}(x)
 =|x|\,|x|_2|x|_3.
\tag{30}
\]

Division by `g_m` removes only powers of two and three.  Thus all 256 internal
primitive coordinates have outside content one, while the two endpoint
coordinates have outside contents at most `U_m` and `U_(m+1)`.  If `x_m`
denotes the primitive tuple, then

\[
 \prod_{k=0}^{257}\operatorname{out}_{2,3}(x_{m,k})
 \le U_mU_{m+1}.
\tag{31}
\]

Equations (24)--(25) imply

\[
 \limsup {\log_2(U_mU_{m+1})\over E_m}
 \le {6498\over346819}<{1\over50},
\tag{32}
\]

because

\[
 50\cdot6498=324900<346819.
\tag{33}
\]

One primitive coordinate contains `2^(E_m)U_(m+1)/g_m`; hence

\[
 \|x_m\|=\max_k|x_{m,k}|\ge {2^{E_m}\over216}.
\tag{34}
\]

The strict exponent gap is

\[
 \delta={1\over50}-{6498\over346819}
 ={21919\over17340950}>0.
\tag{35}
\]

Choose the limsup margin `delta/2`.  For all sufficiently large `m`, (32)
gives

\[
 \log_2(U_mU_{m+1})
 \le\left({1\over50}-{\delta\over2}\right)E_m.
\tag{36}
\]

Once `delta E_m/2 >= log_2(216)/50`, equations (34)--(36) yield

\[
 \boxed{
 \prod_{k=0}^{257}\operatorname{out}_{2,3}(x_{m,k})
 \le\|x_m\|^{1/50}.}
\tag{37}
\]

This checks the fixed constant `c=1`, not merely an unspecified asymptotic
constant.

Evertse's Corollary 1 on page 227 states that, for fixed `n>=1`, `c>0`,
`0<=d<1`, and a finite prime set `S_0`, only finitely many primitive integer
tuples `(x_0,...,x_n)` satisfy

- total sum zero;
- no nonempty proper vanishing subsum; and
-
  \[
  \prod_{k=0}^{n}
  \left(|x_k|\prod_{p\in S_0}|x_k|_p\right)
  \le c\|x\|^d.
  \tag{38}
  \]

For `K=Q`, the source norm is exactly `max_k|x_k|` on primitive integer
coordinates.  Equations (26)--(37) match the theorem with the fixed data

\[
 n=257,
 \qquad S_0=\{2,3\},
 \qquad c=1,
 \qquad d={1\over50}.
\tag{39}
\]

The source imposes no pairwise-coprimality hypothesis.  Page 228 also notes
that each rational projective point has exactly two primitive integer
representatives, differing by global sign.

## Proof 5 -- infinitely many distinct tuples

Compare, in a fixed coordinate ordering, the endpoint coordinate containing
`2^(E_m)U_(m+1)` with the `j=0` internal coordinate.  By (10)--(11), the
2-adic valuation of their projective ratio is

\[
 E_m+v_2(U_{m+1})-v_2(b_{m,0})
 \in[E_m-3,E_m+3].
\tag{40}
\]

Primitive normalization cancels from this ratio.  Moreover

\[
 E_{m+1}-E_m={8459\over2}2^m>6.
\tag{41}
\]

The intervals in (40) are therefore pairwise disjoint as `m` increases.
The projective points, and hence their primitive representatives up to the
irrelevant global sign, are pairwise distinct.

An infinite cap or co-cap tail would now give infinitely many tuples allowed
by (38), whereas Evertse permits only finitely many.  This contradiction
excludes both signed tails.

Finally, the frozen nested-cylinder interface gives one unique 2-adic
completion for every directive.  If it were a signed ordinary integer, exact
finite-stage equivalence would propagate it into the signed trajectory just
excluded.  If its canonical new residue blocks were eventually zero, its
least representatives would stabilize at a nonnegative ordinary integer,
also excluded.  This proves all four conclusions. **QED**

## Primary-source map

The following loci were read directly in the source PDF:

- page 226, equation (2): the norm `||x||`;
- page 226, equation (5): primitive rational coordinates satisfy
  `H(X)=||x||`;
- pages 226--227, equation (6): `(c,d,S)` admissibility;
- page 227, Corollary 1, equations (9)--(12): the integer zero-sum,
  nondegeneracy, gcd, and outside-prime product conditions; and
- page 228: the two primitive representatives `+/-x` of one rational
  projective point.

The source requires only `c>0`; it is `d`, not `c`, that must satisfy
`0<=d<1`.

## Dependency and status audit

- The signed quotient argument uses only canonical cap bounds and the strict
  next-radix gap (1)--(4).  Its all-integer domain is PR #3 `L-0028`, not the
  nonnegative-only wording of `T-0027/(9)`.
- The constants (24)--(25) were independently derived from the correction
  height and first connector scale.  They are not experimental inputs.
- The gcd bound uses both endpoint internal monomials: `u_(m,0)=0` controls
  two, and `v_(m,255)=0` controls three.
- Nondegeneracy follows from signs; no sampled subset test is substituted.
- Projective distinctness uses a coordinate ratio and therefore survives gcd
  normalization.
- Evertse's theorem is the only external black box.  Its exact source
  statement, dimension convention, and rational specialization were checked.
- The corrected tower identities, the 256-stage composition, and physical
  overlap remain frozen `PROPOSED` source interfaces.  This theorem is a
  conditional reconstruction, not an independent rebuild of every tower
  cell from first principles.

## Adversarial boundary

- There are 258 coordinates, so Evertse's source parameter is `n=257`, not
  258.
- The co-cap fixed quotient is `-1`, not zero, and its positive correction is
  `Q_m-R_m`.
- The two endpoint height exponents must be added.  Neither bound alone proves
  (37).
- A limsup strictly below `1/50` is converted to `c=1` using both the explicit
  gap (35) and the fixed primitive loss 216.
- Finiteness would not contradict repeated copies of one tuple.  The disjoint
  valuation intervals (40)--(41) provide the necessary distinctness.
- The result excludes an architecture.  It neither constructs a Collatz
  counterexample nor proves that every Collatz orbit belongs to this frozen
  corrected-stage class.

## Suggested next attack

The source-qualified closure makes the exact scope question decisive.  Either
independently reconstruct the frozen PR #3 physical-overlap interface from the
base tower definitions, or identify a broader corrected-stage class for which
the same two-endpoint outside-prime budget remains below Evertse's `d<1`
threshold.  Replacing the conditional source algebra by a branch-independent
derivation would promote this exclusion from a checked closure theorem to a
fully local one.
