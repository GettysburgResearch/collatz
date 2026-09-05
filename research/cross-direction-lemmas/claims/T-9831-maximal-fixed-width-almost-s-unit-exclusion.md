# T-9831 -- Maximal bounded-width almost-S-unit exclusion

Claim ID: `T-9831`
Title: Bounded essential stage width, finite internal prime alphabets, and subunit primitive endpoint mass exclude every signed ordinary infinite completion
Status: `PROPOSED / SOURCE-QUALIFIED ABSTRACT CLOSURE`
Authoring agent: `gpt56-synthesis-01-wave22-fixed-width-sunit`
Reviewing agents: `gpt56-synthesis-01-wave22-completion-master`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: PR #38 `ACL-N016` at `5ad965771869a647102e22115ed56749dbe2e254`; PR #33 at `c9d62bce3e93f5785f72e4520bc576863d9379eb`; local `T-9828`, `L-9900`, `L-9901`, `L-9902`; Evertse 1984 Corollary 1
Quantitative comparison only: Evertse--Schlickewei--Schmidt 2002 Theorem 1.1
Scope: abstract corrected affine-stage architectures after exact passage to integer homogeneous relations
Related counterexample candidates: none; this is an abstract exclusion theorem
Related atom: PR #38 `ACL-N016`

## Motivation

Several corrected-stage directions already produce exact signed integer
relations with only finitely many moving endpoints. This theorem identifies
the maximal reusable arithmetic closure: once essential width, internal prime
support, nondegeneracy, primitive distinctness, and subunit primitive endpoint
mass are all proved, no additional stage-specific S-unit argument is needed.
It also identifies the precise ways a new architecture can escape that
closure.

## 1. Outside-prime content

For a finite set `S` of rational primes and
`z in Z\{0}`, put

\[
 \operatorname{out}_S(z)
 =|z|\prod_{p\in S}|z|_p
 =\prod_{p\notin S}p^{v_p(z)}.
\tag{1}
\]

Thus `out_S(z)=1` exactly when `z` is an integer `S`-unit.

## 2. Finite type catalogue

Fix a finite catalogue `mathcal T`. A type `tau in mathcal T` records:

1. a coordinate count

   \[
    2\le N_\tau\le N_*;
   \tag{2}
   \]

2. endpoint slots `E_tau subseteq {1,...,N_tau}` and internal slots
   `I_tau=E_tau^c`;
3. an optional coefficient, orientation, and sign class; and
4. one of finitely many finite internal prime alphabets.

Finite integral coefficients may be absorbed into the coordinates. Include
all prime divisors of those coefficients in the corresponding alphabet. If
there are fixed rational coefficients, first clear their denominators
type-by-type and include the finitely many denominator primes.

Let `S_*` be the union of every alphabet and every coefficient or denominator
prime in the finite catalogue. Then `S_*` is finite.

At stage `m`, let `tau(m) in mathcal T` and let

\[
 a_m=(a_{m,1},\ldots,a_{m,N_{\tau(m)}})
 \in(\mathbf Z\setminus\{0\})^{N_{\tau(m)}}
\tag{3}
\]

be the exact ordered stage tuple. Put

\[
 g_m=\gcd_k|a_{m,k}|,
 \qquad
 x_m={a_m\over g_m},
 \qquad
 h_m=\|x_m\|_\infty.
\tag{4}
\]

The vector `x_m` is the primitive representative of the stage's rational
projective point.

## 3. Statement -- arithmetic finite-bin theorem

Assume, apart from finitely many stages, the following five hypotheses.

### A. Exact zero sum

\[
 \sum_{k=1}^{N_{\tau(m)}}a_{m,k}=0.
\tag{5}
\]

### B. Internal almost-S-unit structure

For every `j in I_(tau(m))`,

\[
 \operatorname{out}_{S_*}(a_{m,j})=1.
\tag{6}
\]

A sufficient architecture-level certificate is that an internal coordinate
has the form `cu`, where `c` comes from a finite coefficient menu and `u` is
supported on the alphabet assigned to that type. After the finite union is
taken, an arbitrary `S_*`-unit need not remember which smaller type alphabet
generated it.

### C. Nondegeneracy

For every nonempty proper subset
`J subset {1,...,N_(tau(m))}`,

\[
 \sum_{j\in J}a_{m,j}\ne0.
\tag{7}
\]

A sufficient certificate is that exactly one coordinate is positive and all
others are negative, or the global-sign reverse. Hence both cap and co-cap
orientations qualify and may vary with `m` through two finite types.

### D. Subunit primitive endpoint mass

For each type `tau`, fix constants

\[
 c_\tau>0,
 \qquad
 0\le d_\tau<1,
\tag{8}
\]

such that every stage of that type satisfies

\[
 P_m:=
 \prod_{i\in E_\tau}
 \operatorname{out}_{S_*}(x_{m,i})
 \le c_\tau h_m^{d_\tau}.
\tag{9}
\]

If `E_tau` is empty, its product in (9) is defined to be one.

### E. Infinitely many primitive points

The collection of ordered primitive projective points represented by the
`x_m` is infinite.

Then no such infinite stage family exists.

## 4. Proof

Because `g_m` divides every coordinate,

\[
 \operatorname{out}_{S_*}(x_{m,k})
 ={\operatorname{out}_{S_*}(a_{m,k})
   \over\operatorname{out}_{S_*}(g_m)}
 \le\operatorname{out}_{S_*}(a_{m,k}).
\tag{10}
\]

If at least one internal coordinate is present, (6) forces `g_m` itself to
be supported on `S_*`, so every normalized internal coordinate remains an
`S_*`-unit. If there is no internal coordinate, every coordinate is already
an endpoint. In either case,

\[
 \prod_{k=1}^{N_{\tau(m)}}
 \operatorname{out}_{S_*}(x_{m,k})
 =P_m
 \le c_{\tau(m)}h_m^{d_{\tau(m)}}.
\tag{11}
\]

Set

\[
 c_*=\max_{\tau\in\mathcal T}c_\tau,
 \qquad
 d_*=\max_{\tau\in\mathcal T}d_\tau<1.
\tag{12}
\]

Since `h_m>=1`, equation (11) implies

\[
 \prod_k\operatorname{out}_{S_*}(x_{m,k})
 \le c_*h_m^{d_*}.
\tag{13}
\]

For each fixed coordinate count `N`, Evertse's Corollary 1 applies with

\[
 n=N-1,
 \qquad c=c_*,
 \qquad d=d_*,
 \qquad S_0=S_*.
\tag{14}
\]

It gives only finitely many primitive integer `N`-tuples satisfying (5),
(7), and (13). There are only finitely many dimensions `2<=N<=N_*`; their
union is finite. This contradicts hypothesis E. **QED**

## 5. Why finite coefficient and sign classes cause no hidden gap

Once a stage is written as the actual integer zero sum (5), Evertse sees
neither a separate coefficient vector nor a sign class. Coefficients have
already been absorbed into coordinates, and signs are part of those
coordinates.

The only analytic binning required is by coordinate count. Finite coefficient
classes are useful for proving (6), because their prime divisors can be placed
in `S_*`. Finite cap/co-cap or other sign classes are useful for proving (7).
Neither enlarges the Evertse parameter space.

Coordinate permutations also do not create an escape: for bounded `N` there
are only finitely many permutations. A ratio separator whose slot labels
depend on type should be checked in each finite type bin.

## 6. Exact normalized-height criterion

The fundamental exponent is

\[
 \Xi=
 \limsup_{m\to\infty}{\log P_m\over\log h_m},
 \qquad h_m\longrightarrow\infty.
\tag{15}
\]

If

\[
 \boxed{\Xi<1,}
\tag{16}
\]

choose any fixed `d` with `Xi<d<1`. Then eventually

\[
 P_m\le h_m^d,
\tag{17}
\]

so the theorem applies with `c=1`.

More generally, for a prescribed `d<1`, the sufficient gate is `Xi<d`. At
exponent equality, Evertse still applies if one has an actual uniform estimate

\[
 P_m\le Ch_m^d
\tag{18}
\]

with fixed `C`. Strictness is needed when only limsup exponent data are known;
Evertse itself permits every fixed `c>0`.

## 7. Raw endpoint and gcd certificate

Applications often estimate raw rather than primitive coordinates. Define

\[
 H_m=\max_k|a_{m,k}|,
 \qquad
 B_m=\prod_{i\in E_{\tau(m)}}
       \operatorname{out}_{S_*}(a_{m,i}).
\tag{19}
\]

Then

\[
 P_m\le B_m,
 \qquad
 h_m={H_m\over g_m}.
\tag{20}
\]

Let `R_m->infinity` be any proved raw scale satisfying `H_m>=R_m`, and put

\[
 \gamma=limsup{\log g_m\over\log R_m}<1,
 \qquad
 \Theta=limsup{\log B_m\over\log R_m}.
\tag{21}
\]

For a prescribed `0<d<1`, the raw sufficient gate is

\[
 \boxed{\Theta<d(1-\gamma).}
\tag{22}
\]

Indeed, choose `eta>0` with

\[
 (1+d)\eta<d(1-\gamma)-\Theta,
 \qquad
 \eta<1-\gamma.
\tag{23}
\]

Eventually,

\[
 g_m\le R_m^{\gamma+\eta},
 \qquad
 B_m\le R_m^{\Theta+\eta},
\tag{24}
\]

and therefore

\[
 h_m\ge R_m^{1-\gamma-\eta}\longrightarrow\infty,
\tag{25}
\]

\[
 P_m\le B_m
 \le R_m^{\Theta+\eta}
 \le R_m^{d(1-\gamma-\eta)}
 \le h_m^d.
\tag{26}
\]

Thus the same calculation supplies both admissibility and infinitely many
primitive points.

Consequences:

- bounded gcd gives `gamma=0`;
- an unbounded subpower gcd,

  \[
   \log g_m=o(\log R_m),
  \tag{27}
  \]

  also gives `gamma=0`;
- in either case `Theta<d` suffices, and this marginal `(Theta,gamma)`
  certificate supplies some Evertse exponent exactly when `Theta<1`.

The qualification in the last clause matters: the primitive product `P_m`
may be smaller than the marginal raw bound `B_m` because of normalization,
anticorrelation, or a loose endpoint estimate. The primitive invariant `Xi`
in (15), not the pair `(Theta,gamma)`, is the exact criterion for this
endpoint method.

At exponent equality, uniform estimates

\[
 g_m\le C_gR_m^\gamma,
 \qquad
 B_m\le C_BR_m^{d(1-\gamma)}
\tag{28}
\]

give

\[
 P_m\le C_BC_g^dh_m^d.
\tag{29}
\]

The primitive criterion (15) is stronger than the marginal raw criterion.
Even `gamma=1` is not an escape if primitive-height divergence and (9) are
proved directly.

## 8. Minimal-block extraction

The full stage relation need not itself be nondegenerate. It is enough to
select, on an infinite stage subsequence, an inclusion-minimal nonempty
zero-sum subtuple `b_m`, remove any zero slots, and then pigeonhole the bounded
sizes and finite types to one fixed dimension/type such that:

1. its coordinate count remains bounded;
2. its inherited internal coordinates are `S_*`-units;
3. its primitive endpoint mass satisfies (9); and
4. the selected primitive blocks yield infinitely many projective points.

Minimality makes the selected nonzero block nondegenerate automatically. The
fixed prime support, inherited endpoint designation and product after
primitive normalization, and primitive projective distinctness must all be
reverified for the extracted blocks; none is inherited merely from
minimality.

This qualification is necessary. A formal proper vanishing subsum is not by
itself an escape if a bounded nondegenerate block retaining the height and
distinctness data can be extracted. Conversely, extraction is not automatic:
the only growing coordinates may cancel in a repeated two-term block.

## 9. Signed ordinary-completion corollary

Consider a corrected affine-stage architecture with a nested 2-adic
completion interface. Suppose every hypothetical signed ordinary infinite
completion, after discarding a finite prefix, produces exact physical integer
stage relations satisfying Sections 2--3, or minimal blocks satisfying
Section 8.

The tail-producing mechanism may be an eventual cap, an eventual co-cap, a
finite collection of signed tail modes, or any other argument proving the
required nondegeneracy. If the relations have infinitely many primitive
projective points, the arithmetic theorem gives a contradiction. Therefore
no signed ordinary infinite completion exists.

The physical bridge is an explicit hypothesis: formal real, rational, or
2-adic identities that are not exact integer relations along the proposed
ordinary orbit do not trigger the corollary.

## 10. Specialization to PR #33

For `T-9828` and frozen PR #33, take

\[
 N_*=258,
 \qquad |E|=2,
 \qquad |I|=256,
 \qquad S_*=\{2,3\}.
\tag{30}
\]

The two types are cap and co-cap. Their one-versus-rest sign patterns prove
nondegeneracy. The raw normalization data are

\[
 R_m=2^{E_m},
 \qquad g_m\le216,
 \qquad \gamma=0,
\tag{31}
\]

and

\[
 \Theta\le{6498\over346819}<{1\over50}.
\tag{32}
\]

Thus (22) holds with `d=1/50`. Primitive height divergence already proves
infinitely many points; the disjoint 2-adic ratio intervals in `T-9828`
supply the stronger pairwise separator. PR #33 is one fixed-width,
one-alphabet, two-type instance of this theorem.

## 11. Evertse versus ESS

Evertse's 1984 Corollary 1 is the correct tool under Sections 2--3:

- it requires fixed dimension, fixed finite `S`, nondegeneracy, primitive
  normalization, and `d<1`;
- it does not require all endpoints to lie in a common finite-rank
  multiplicative group;
- fresh endpoint primes are allowed if their total outside-`S` mass obeys
  (9).

The quantitative Evertse--Schlickewei--Schmidt theorem is a different route.
After choosing a pivot in an `N`-coordinate zero sum, write

\[
 y_1+\cdots+y_{N-1}=1,
 \qquad
 y_i=-{x_i\over x_N}.
\tag{33}
\]

For one bin, ESS requires a fixed `n=N-1`, fixed coefficients if they were
not absorbed into the `y_i`, one subgroup

\[
 \Gamma\le(K^\times)^n
\tag{34}
\]

common to every solution in the bin, finite rank `rho`, and nondegeneracy. It
then bounds the number of solutions by

\[
 A(n,\rho)=
 \exp\left((6n)^{3n}(\rho+1)\right).
\tag{35}
\]

For finitely many dimension/coefficient/common-group bins `lambda`,

\[
 \#\mathcal F
 \le\sum_\lambda
 \exp\left((6n_\lambda)^{3n_\lambda}
                (\rho_\lambda+1)\right).
\tag{36}
\]

The group may not be chosen separately for each solution: every individual
solution lies in the cyclic group it generates, so that interpretation would
make ESS vacuous. Finite coefficient and sign binning does not replace the
common-group requirement.

Use ESS when a common finite-rank factorization is available or a quantitative
capacity is needed. Use Evertse when fresh endpoint primes prevent a common
finite-rank group but their outside-prime mass is subunit. Pure `S`-unit
families may satisfy both.

## 12. Sharp boundaries and counterexamples

### 12.1 Unbounded essential width

For every `N>=3`, the `N`-coordinate tuple

\[
 \left(
 2^{N-2},-1,-2,-2^2,\ldots,-2^{N-3},-1
 \right)
\tag{37}
\]

has sum zero, exactly one positive coordinate, gcd one, fixed alphabet
`S={2}`, outside-`S` mass one, and unbounded primitive height. There is one
tuple in every growing dimension. Thus bounded essential coordinate count
cannot be dropped; this is the diagonal obstruction recorded in `L-9902`.

### 12.2 The normalized exponent-one boundary

For `S={2}`,

\[
 x_m=(2^m,-(2^m-1),-1)
\tag{38}
\]

is primitive, nondegenerate, fixed-dimensional, and projectively distinct,
but

\[
 \|x_m\|=2^m,
 \qquad P_m=2^m-1,
 \qquad \Xi=1.
\tag{39}
\]

For every fixed `c>0` and `d<1`,

\[
 2^m-1>c\,2^{md}
\tag{40}
\]

eventually. Hence the threshold `Xi<1` is sharp for this method.

More generally, multiplying (38) by

\[
 G_m=
 2^{\left\lfloor{\gamma_0\over1-\gamma_0}m\right\rfloor},
 \qquad0\le\gamma_0<1,
\tag{41}
\]

gives

\[
 \gamma=\gamma_0,
 \qquad \Theta=1-\gamma_0.
\tag{42}
\]

This proves that the raw marginal boundary `Theta<1-gamma` cannot be replaced
by a non-strict inequality without additional constants or structure.

### 12.3 Nondegeneracy

For `S={2}`,

\[
 (2^m,-2^m,1,-1)
\tag{43}
\]

is primitive, fixed-dimensional, projectively distinct, and has zero
outside-`S` exponent, but contains proper vanishing subsums. Some
nondegeneracy or successful minimal-block extraction is essential.

### 12.4 Primitive distinctness

The raw tuples

\[
 a_m=2^m(2,-1,-1)
\tag{44}
\]

are nondegenerate, fixed-width `S`-unit zero sums of growing raw height, but
all normalize to the single point

\[
 (2:-1:-1).
\tag{45}
\]

Infinitely many stages are not enough; infinitely many primitive points must
survive normalization. This is why a bounded or subpower gcd is useful.

### 12.5 A stage-dependent prime alphabet

Let `M_m` be the product of the first `m` primes and let `S_m` contain the
prime divisors of `M_m(M_m-1)`. Then

\[
 (M_m,-(M_m-1),-1)
\tag{46}
\]

is a primitive nondegenerate `S_m`-unit zero sum with stagewise
outside-`S_m` mass one, while the union of the `S_m` is infinite. Therefore
"finite alphabet at each stage" is insufficient: one fixed finite union, or
finitely many alphabets with finite union, is required.

## 13. Dependency and gap audit

- Evertse's Corollary 1 is the only external input to the qualitative
  finite-bin theorem.
- Its source dimension is `n=N-1` for an `N`-coordinate tuple.
- The finite catalogue may vary stage width, endpoint placement, coefficients,
  orientations, and signs; bounded dimension and a fixed finite prime union
  are the analytic invariants.
- The endpoint budget is the product over all non-internal coordinates.
  Separate endpoint estimates must be added.
- One-versus-rest signs prove nondegeneracy; a general sign pattern does not.
- Bounded or subpower gcd is sufficient, not necessary. Direct primitive
  height and endpoint estimates are stronger.
- A projective ratio separator survives primitive normalization, but primitive
  height divergence is already sufficient.
- Raw width must mean essential width after exact cancellation or regrouping.
  Adding many terms that compress to a bounded relation does not escape the
  theorem.
- A degenerate relation remains covered only if a bounded minimal block
  retains the endpoint budget and infinitely many primitive points.
- The theorem does not supply a stage compiler, physical overlap, quotient
  extinction, endpoint-height estimate, or ordinary initialization. Those
  remain architecture-specific interfaces.
- No Collatz counterexample and no proof of the Collatz conjecture are claimed.

## Source links

- [Evertse 1984, Corollary 1](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)
- [Evertse--Schlickewei--Schmidt 2002, official Annals page](https://annals.math.princeton.edu/2002/155-3/p04)

## Adversarial tests

Sections 12.1--12.5 are theorem-level adversarial families. They separately
break bounded width, the strict exponent threshold, nondegeneracy, primitive
distinctness, and the fixed finite prime union while preserving every other
nearby hypothesis. The PR #33 constants were also reconstructed independently
with `N=258`, source dimension `257`, `g|216`, and endpoint ratio
`6498/346819`.

## Remaining uncertainty

There is no uncertainty in the abstract implication once Evertse's cited
Corollary 1 is accepted. Every application remains conditional on producing
the exact integer relations and primitive endpoint estimate in its own
physical architecture. Minimal-block extraction is deliberately not asserted
to exist automatically.

## Suggested next attack

For each atom in PR #38 with bounded proposed width, write its exact integer
zero sum and compute `Xi` directly after primitive normalization. If the raw
gcd is easier to control, first verify the sufficient `(Theta,gamma)` gate;
if a proper subsum appears, attempt the fixed-bin minimal-block extraction of
Section 8 and recheck every endpoint slot.
