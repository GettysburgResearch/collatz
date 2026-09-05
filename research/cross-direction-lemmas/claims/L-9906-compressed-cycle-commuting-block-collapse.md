# L-9906 -- Commuting compressed cycle blocks collapse to one primitive root

Claim ID: `L-9906`
Title: Affine Collatz blocks commute exactly at a common fixed point, and every commuting cycle partition is a repeated smaller certificate
Status: `PROPOSED / EXACT GRAMMAR REDUCTION`
Authoring agent: `gpt56-synthesis-01-wave24-commuting-cycle-blocks`
Reviewing agents: `gpt56-synthesis-01` (independent reconstruction and boundary audit)
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9904` at repository head `b77a84c7e4ff15f36b59b29627671f1cb6544072`; issue #9 affine supplement at `b40e5c44959b20842e6c064084c668f5243b6ebd` and live PR #42 head `94fcd99fe7fb71e0f5a15915ba40e9d74b167a13`; PR #11 head `7950713cbb6ba0af0a424806cc36ce01ad24cf9e`, especially `D-0101`, `D-CYCLE-*`, and `O-0109`
Scope: affine summaries in characteristic zero, specialized to nonempty accelerated `3n+1` valuation words
Related counterexample candidates: none; the theorem removes commuting grammar duplicates and supplies an exact cut sieve

## Source freeze and purpose

`L-9904` proves that a nonempty accelerated valuation word is losslessly
encoded by `(k,A,C)`, that fixed-point divisibility forces exact positive
replay, and that powers and rotations must be reduced to primitive necklaces.
Issue #9 asks for compositional block invariants, while frozen PR #11 includes
an empirical search over powers and other short block grammars.

The next natural question is whether two *different* compressed blocks can
commute and thereby create a new cycle family. They cannot. For valid
accelerated words, affine commutation, equality of rational fixed points,
word commutation, and being powers of one primitive word are all equivalent.
On a positive cycle, the commutator is exactly the cycle denominator times
the displacement to the rotated starting state. Thus zero commutator is an
early return, while a primitive cycle forces every proper-cut commutator to
be a nonzero multiple of the full cycle denominator.

## 1. General affine commutator, including every degenerate case

Let

\[
 \sigma=(p,q,c),
 \qquad
 \tau=(r,s,d),
 \qquad
 q,s\ne0,
\tag{1}
\]

be affine summaries over a characteristic-zero field, with maps

\[
 F_\sigma(x)={px+c\over q},
 \qquad
 F_\tau(x)={rx+d\over s}.
\tag{2}
\]

Chronological composition means that `sigma` acts first and `tau` second:

\[
 F_{\sigma\tau}=F_\tau\circ F_\sigma.
\tag{3}
\]

The two composition constants over the common denominator `qs` are

\[
 c_{\sigma\tau}=rc+qd,
 \qquad
 c_{\tau\sigma}=pd+sc.
\tag{4}
\]

Define the oriented commutator defect

\[
 \boxed{
 \Omega(\sigma,\tau)
 =(q-p)d-(s-r)c
 =c_{\sigma\tau}-c_{\tau\sigma}.}
\tag{5}
\]

Then

\[
 \boxed{
 F_\tau\circ F_\sigma-F_\sigma\circ F_\tau
 ={\Omega(\sigma,\tau)\over qs}.}
\tag{6}
\]

### Theorem 1 -- complete affine classification

The maps commute if and only if `Omega(sigma,tau)=0`. More explicitly:

1. If `q != p` and `s != r`, both maps have unique finite fixed points

   \[
    \xi_\sigma={c\over q-p},
    \qquad
    \xi_\tau={d\over s-r},
   \tag{7}
   \]

   and

   \[
    \boxed{F_\sigma F_\tau=F_\tau F_\sigma
    \quad\Longleftrightarrow\quad
    \xi_\sigma=\xi_\tau.}
   \tag{8}
   \]

2. If `q=p` and `s=r`, both maps are translations, including possible
   identities, and they always commute.
3. If `q=p,c=0`, then `F_sigma` is the identity and commutes with every
   affine map. The symmetric statement holds for `tau`.
4. If `q=p,c != 0` is a nonzero translation and `s != r`, the maps do not
   commute. The symmetric statement again holds.
5. Zero translations cause no exception to (8): if `c=0,q != p`, then
   `F_sigma` is a homothety about zero and commutes with a nontranslation
   `F_tau` exactly when `d=0`, so that both have fixed point zero.

#### Proof

The linear coefficients of the two compositions are both `pr/(qs)`, and
(4) shows that their constants agree exactly when (5) vanishes. If both
slopes differ from one, (5) can be rewritten as

\[
 (q-p)(s-r)(\xi_\tau-\xi_\sigma)=0,
\tag{9}
\]

which proves (8), including the zero-translation case. If both slopes are
one, (5) vanishes identically. If exactly one slope is one, (5) vanishes
only when that map's translation is zero, making it the identity. This is
the complete list. **QED**

### Collatz degeneracies

For a valid accelerated word below, every nonempty block has

\[
 p=3^k,
 \qquad q=2^A,
 \qquad k,A\ge1,
 \qquad c=C>0.
\tag{10}
\]

Thus `p != q` by unique factorization, and none of cases 2--5 occurs. The
empty word has summary `(1,1,0)` in `(p,q,c)` notation and is the identity.
It must be deleted before declaring a grammar partition to be a commuting
decomposition.

For the broader shortcut-parity monoid of PR #11, a nonempty all-even block
has `c=0` and fixes zero. Such blocks commute with each other, but not with a
positive-translation nonidentity block. Their common fixed point zero cannot
produce a positive cycle. A critical nonzero translation cannot arise from
a valid Collatz word: `2^L=3^a` forces `L=a=0`, whose valid word is empty and
has translation zero.

## 2. Valid accelerated words

Let

\[
 u=(a_0,\ldots,a_{h-1}),
 \qquad
 v=(b_0,\ldots,b_{\ell-1})
\tag{11}
\]

be nonempty words over `Z_(>=1)`. Retain the notation of `L-9904`:

\[
 p_u=3^{k_u},
 \quad q_u=2^{A_u},
 \quad C_u=\sum_{i=0}^{k_u-1}3^{k_u-1-i}2^{A_{u,i}},
\tag{12}
\]

and similarly for `v`. Their formal branches are

\[
 F_u(x)={p_ux+C_u\over q_u},
 \qquad
 F_v(x)={p_vx+C_v\over q_v}.
\tag{13}
\]

Chronological concatenation has

\[
 C_{uv}=p_vC_u+q_uC_v,
 \qquad
 C_{vu}=p_uC_v+q_vC_u.
\tag{14}
\]

Put

\[
 \boxed{
 \Omega(u,v)
 =(q_u-p_u)C_v-(q_v-p_v)C_u
 =C_{uv}-C_{vu}.}
\tag{15}
\]

### Theorem 2 -- affine commutation is word commutation

The following five conditions are equivalent:

1. `F_u` and `F_v` commute;
2. `Omega(u,v)=0`;
3. the two rational fixed points agree,

   \[
    {C_u\over q_u-p_u}={C_v\over q_v-p_v};
   \tag{16}
   \]

4. the chronological words commute, `uv=vu`;
5. there is a unique primitive word `z` and positive integers `alpha,beta`
   such that

   \[
    \boxed{u=z^\alpha,\qquad v=z^\beta.}
   \tag{17}
   \]

Consequently, two nonempty valid blocks of opposite drift sign cannot
commute: `q-p>0` gives a positive rational fixed point, whereas `q-p<0`
gives a negative one because every `C` is positive.

#### Proof

Theorem 1 gives the equivalence of 1--3. If the maps commute, (14)--(15)
show that `uv` and `vu` have the same triple

\[
 (k_u+k_v,A_u+A_v,C).
\tag{18}
\]

The lossless decoder `L-9904/(8)--(9)` then gives `uv=vu`.

For completeness, word commutation gives (17) by induction on
`|u|+|v|`. Assume `|u|<=|v|`. If the lengths are equal, comparison in
`uv=vu` gives `u=v`. Otherwise `v` begins with `u`, so write `v=uv'`.
Cancelling the common initial `u` reduces `uv=vu` to `uv'=v'u`, and induction
gives powers of one word. Replacing that word by its unique primitive root
gives (17). Conversely, powers of one word commute chronologically, hence
their affine maps commute. **QED**

### Exact 2-adic noncommutation witness

Suppose `Omega(u,v) != 0`. Let

\[
 x=uv,
 \qquad y=vu,
\tag{19}
\]

and let `j` be their first differing letter. Their prefixes before `j` are
equal; write

\[
 P_j=\sum_{i=0}^{j-1}x_i.
\tag{20}
\]

Then

\[
 \boxed{
 v_2(\Omega(u,v))
 =P_j+\min(x_j,y_j).}
\tag{21}
\]

Indeed, split the common prefix using the concatenation law. It contributes
the factor `2^(P_j)` to `C_x-C_y`. In the two remaining equal-length suffixes,
the common first term `3^(K-j-1)` cancels. If, say, `x_j<y_j`, the residual
difference is

\[
 2^{x_j}\left(C_{x_{>j}}-2^{y_j-x_j}C_{y_{>j}}\right),
\tag{22}
\]

and the parenthesis is odd because valid nonempty-word constants are odd.
The first disagreement cannot be the final letter: `x,y` have equal total
valuation and an equal prefix. Thus the displayed tail constants exist, and
(21) follows. This gives a small boundary certificate for noncommutation
without comparing the full integers in (15).

## 3. A commutator is exactly a cycle-state displacement

Let `w=uv`, with both blocks nonempty, and put

\[
 k=k_u+k_v,
 \qquad A=A_u+A_v,
 \qquad D_w=2^A-3^k.
\tag{23}
\]

Assume `w` is a positive exact cycle certificate. By `L-9904`,

\[
 D_w>0,
 \qquad D_w\mid C_{uv},
 \qquad n_0={C_{uv}\over D_w}\in\mathbf Z_{>0}.
\tag{24}
\]

Let `n_u` be the state reached after the prefix `u`. The rotation identity
of `L-9904` gives

\[
 n_u={C_{vu}\over D_w}.
\tag{25}
\]

Subtracting (25) from (24) yields the exact displacement identity

\[
 \boxed{
 \Omega(u,v)=D_w(n_0-n_u).}
\tag{26}
\]

### Theorem 3 -- early-return decomposition

Under (24), the following are equivalent:

1. `F_u` and `F_v` commute;
2. `n_u=n_0`, so the cycle returns after the proper prefix `u`;
3. both `u` and `v` are positive exact cycle certificates with the same
   starting integer `n_0`;
4. there is a primitive positive cycle certificate `z` and positive
   `alpha,beta` such that `u=z^alpha` and `v=z^beta`.

In this case

\[
 w=z^{\alpha+\beta},
\tag{27}
\]

so the proposed certificate is only repeated traversal of the smaller cycle.

#### Proof

Equivalence of 1 and 2 is (26). If the prefix returns to `n_0`, exact replay
of `w` shows that `u` is a closed exact itinerary and that the following block
`v` starts and ends at `n_0`; hence 3. Conversely, two maps fixing the same
`n_0` commute by Theorem 1. Theorem 2 now gives a common primitive root `z`.
Since `w=z^(alpha+beta)` is a positive certificate, power collapse in
`L-9904/(23)--(29)` makes `z`, and therefore each positive power `u,v`, the
same positive certificate. **QED**

### Primitive cut dichotomy

If `w` is primitive, every proper nonempty cut `w=uv` satisfies

\[
 \boxed{
 0\ne\Omega(u,v),
 \qquad
 D_w\mid\Omega(u,v),
 \qquad
 |\Omega(u,v)|\ge D_w.}
\tag{28}
\]

The first assertion is Theorem 3, and the other two follow from (26). Since
`D_w` is odd,

\[
 \boxed{
 v_2(n_0-n_u)=v_2(\Omega(u,v))
 =P_j+\min(x_j,y_j),}
\tag{29}
\]

with the notation of (19)--(21).

Thus every proposed positive word and every proper cut has an exact
three-way outcome:

1. `Omega=0`: reduce to the smaller common primitive root;
2. `0<|Omega|<D_w`: reject the word, because it cannot satisfy cycle
   divisibility;
3. `|Omega|>=D_w`: the cut survives this necessary test, with `D_w|Omega`
   still required.

The rejection in case 2 does not assume the candidate is already known to be
integral. If `D_w` divided `C_w`, rotation invariance from `L-9904/(33)--(34)`
would make it divide both `C_(uv)` and `C_(vu)`, hence their difference
`Omega`, contradicting `0<|Omega|<D_w`.

## 4. Connected commuting partitions

Let

\[
 w=u_1u_2\cdots u_m,
 \qquad m\ge2,
\tag{30}
\]

be a partition into nonempty accelerated words. Form a graph on
`{1,...,m}` by joining `i,j` when `F_(u_i)` and `F_(u_j)` commute.

### Theorem 4 -- partition collapse

The following are equivalent:

1. the commutation graph is connected;
2. all block fixed points are equal;
3. all block maps commute pairwise;
4. there is one primitive word `z` and positive integers `e_i` such that

   \[
    \boxed{u_i=z^{e_i}\quad(1\le i\le m).}
   \tag{31}
   \]

Consequently,

\[
 w=z^{e_1+\cdots+e_m}.
\tag{32}
\]

If `w` is a positive exact cycle certificate, then `z` and every `u_i` are
smaller positive exact cycle certificates for the same starting integer. In
particular, pairwise commuting top-level grammar children, or merely a chain
of adjacent commuting children connecting the partition, never produce a new
cycle.

#### Proof

Along every graph edge, Theorem 2 gives equality of fixed points. Connectivity
makes that equality global, which gives pairwise commutation by Theorem 1.
Each pair with `u_1` has a common primitive root; uniqueness of the primitive
root of `u_1` makes it the same word `z` for every block. This proves (31),
whose converse is immediate. Equation (32) and `L-9904` power collapse prove
the certificate statement. **QED**

If the commutation graph is disconnected, the theorem applies within each
connected component only. It does not permit reordering interleaved blocks or
collapsing the entire grammar production.

## 5. Grammar and sieve consequences

### 5.1 Canonical commuting productions

Every connected commuting production should be replaced by the primitive
root `z` and one traversal count. Retaining all child summaries creates only
geometric numerator/denominator factors already removed by `L-9904`. The
root may lie outside the literal grammar language, so a negative grammar
result must route to and test the canonical root closure rather than silently
discard the production.

### 5.2 Exact fixed-point test

For nonempty accelerated blocks, shared fixed point is tested without rational
arithmetic by

\[
 \boxed{
 (q_u-p_u)C_v=(q_v-p_v)C_u.}
\tag{33}
\]

Opposite signs of `q-p` reject commutation immediately. A modular inequality
can certify noncommutation, but equality modulo a finite modulus is not a
proof of exact commutation.

### 5.3 Cut sieve

At a grammar node `w=uv`, compute `Omega` compositionally from the two child
summaries. If `D_w>0` and

\[
 0<|\Omega(u,v)|<D_w,
\tag{34}
\]

the node cannot be a positive cycle certificate. If `Omega=0`, it is a proper
power and should be canonicalized, not reported as a new hit. For a primitive
survivor, every cut must pass the divisibility and size conditions (28).

Equation (21) also supplies the exact 2-adic order of a nonzero defect from
the first boundary mismatch of `uv` and `vu`; a compressed implementation can
emit that mismatch as a short proof certificate.

### 5.4 Rotation warning

Every cyclic rotation of a cycle word is another certificate, but its block
map does not generally commute with the original cut. By (26), commutation
occurs exactly when the rotation starts at the same integer, hence exactly at
an early return. Ordinary rotation quotienting and commuting-block collapse
are related but not interchangeable operations.

### 5.5 Positivity and integrality warning

Commutation alone proves only a common rational fixed point and a common word
root. That fixed point may be negative or nonintegral. It becomes a positive
exact Collatz cycle only after the root satisfies

\[
 2^{A_z}>3^{k_z},
 \qquad
 2^{A_z}-3^{k_z}\mid C_z.
\tag{35}
\]

Theorem 3 transfers positivity and integrality because the *whole word* is
assumed to be a positive certificate; they must not be inferred from
commutation in isolation.

## 6. Adversarial and boundary audit

1. **Orientation.** Chronological `uv` means `F_v \circ F_u`, giving
   `C_(uv)=p_vC_u+q_uC_v`. Expanding both sides of (15) reproduces this sign,
   and (26) is `D_w(n_0-n_u)`, not its negative.
2. **Empty identity.** An empty child commutes with every block but supplies
   no common-root information. Every theorem after Section 1 requires
   nonempty children.
3. **Nonzero translations.** General affine translations commute with one
   another without a unique finite fixed point. They do not occur as valid
   Collatz words and are isolated explicitly in Theorem 1.
4. **Zero translations.** Homotheties about zero commute at fixed point zero.
   In the shortcut-parity monoid these are all-even blocks and cannot make a
   positive cycle.
5. **Critical slope.** No nonempty Collatz summary has slope one, because
   powers of two and three cannot agree.
6. **Common root without a cycle.** Supercritical powers of one word commute
   at a negative fixed point; subcritical powers may share a positive but
   nonintegral fixed point. Neither is a certificate without (35).
7. **Unaligned cuts.** A powered word can have noncommuting cuts through the
   middle of its primitive root. The zero-defect conclusion applies exactly
   to cuts aligned as powers in (17), not to every cut of an imprimitive word.
8. **Partial commutation.** One commuting pair inside a disconnected larger
   partition does not collapse unrelated blocks. The connectedness condition
   in Theorem 4 is essential.
9. **Primitive obstruction.** A primitive certificate has no early return at
   an odd-state boundary, so every proper-cut defect is nonzero. This is a
   least-period statement, not an assertion that rotated starting values are
   ordered monotonically.
10. **Exact finite audit.** An independent enumeration of all `24,025`
    ordered pairs of words of lengths at most three with letters in
    `{1,...,5}` checked (15)--(17) and the exact valuation formula (21).
    A second enumeration of all `335,922` words of lengths at most seven with
    letters in `{1,...,6}` checked (26)--(28) on every positive integral hit;
    the seven hits were the expected trivial words `(2)^k`. These computations
    are regression tests, not proof inputs.

## 7. Dependency and gap audit

- The abstract commutator calculation is self-contained and includes every
  slope-one, identity, translation, and zero-translation case.
- Specialization to valid accelerated words uses only `p=3^k`, `q=2^A`,
  positivity and oddness of `C`, and the lossless decoder of `L-9904`.
- The common-word theorem is proved by cancellation induction; no external
  combinatorics theorem is imported silently.
- The displacement formula uses the exact cyclic-rotation candidate from
  `L-9904`, so it preserves chronology and the starting-state orientation.
- Integrality and exact valuation replay enter only through the complete
  certificate theorem of `L-9904`.
- The cut bound `|Omega|>=D_w` is necessary, not sufficient. Passing it does
  not prove `D_w|C_w` or construct a cycle.
- The partition theorem requires nonempty valid accelerated blocks and a
  connected commutation graph. Synthetic affine summaries and disconnected
  families remain outside its collapse conclusion.
- No claim is made that every noncommuting grammar family is primitive, that
  the cut sieve is complete, or that any nontrivial Collatz cycle exists.

## Strongest conclusion

> A connected commuting family of nonempty accelerated Collatz blocks is not
> a new grammar mechanism: every block is a positive power of one primitive
> valuation word. If their concatenation is an exact positive cycle, that
> primitive word and every child are already smaller exact certificates for
> the same cycle. At any proper cut of a genuinely primitive certificate, the
> commutator cannot vanish; it is the full odd cycle denominator times the
> displacement to the rotated state, and therefore has absolute value at
> least that denominator.

## Suggested next attack

Augment the issue #9 grammar compiler with `Omega` at each binary production.
Canonicalize zero defects, reject defects satisfying (34), and retain the
exact first-mismatch certificate (21). The remaining genuinely primitive
nodes are the right input for modular factor sieves; commuting blocks no
longer need a separate search family.
