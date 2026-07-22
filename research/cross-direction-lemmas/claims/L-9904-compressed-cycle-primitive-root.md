# L-9904 -- Primitive-root collapse for compressed accelerated cycles

Claim ID: `L-9904`
Title: Powered accelerated valuation words have the same reduced fixed point and the same positive cycle as their primitive root
Status: `PROPOSED / EXACT SEARCH REDUCTION`
Authoring agent: `gpt56-synthesis-01-wave23-cycle-root`
Reviewing agents: `gpt56-synthesis-01-wave22-fixed-width-sunit`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: issue #9 and its affine-monoid supplement, fetched claimed-branch head `b40e5c44959b20842e6c064084c668f5243b6ebd`; PR #11 head `7950713cbb6ba0af0a424806cc36ce01ad24cf9e`, especially `D-0101`, `D-CYCLE-*`, and `O-0109`; Hercher 2023, Definition 5
Scope: nonempty finite accelerated `3n+1` valuation words over the positive integers
Related counterexample candidates: none; this theorem removes duplicate cycle certificates but constructs no cycle

## Source freeze and purpose

Issue #9 proposes compressed valuation words with exact affine summaries
`(k,A,C)` and requires divisibility, positivity, valuation replay, and an exact
local-minimum count. Its claimed branch was still at
`b40e5c44959b20842e6c064084c668f5243b6ebd` when this claim was written.
PR #11, at frozen head
`7950713cbb6ba0af0a424806cc36ce01ad24cf9e`, contains the corresponding
shortcut-parity fixed-point search. Its `O-0109` treats pure powers as an
empirical search family.

The purpose here is to remove that family exactly. More strongly, the single
fixed-point divisibility condition for a valuation word already forces all
intermediate states to be odd integers and forces every advertised valuation.
After powers and cyclic starting points are removed, the genuine search space
is the set of primitive necklaces, not the set of all compressed words.

## 1. Accelerated words and the affine monoid

Let

\[
 S(n)={3n+1\over 2^{\nu _2(3n+1)}}
\tag{1}
\]

be the accelerated map on positive odd integers. Fix a nonempty word

\[
 w=(a_0,a_1,\ldots,a_{k-1}),
 \qquad a_i\in\mathbf Z_{\ge1},
 \qquad k\ge1.
\tag{2}
\]

Put

\[
 A_0=0,
 \qquad
 A_j=\sum_{i=0}^{j-1}a_i,
 \qquad
 A=A_k,
\tag{3}
\]

and

\[
 C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}.
\tag{4}
\]

The formal branch determined by `w` is

\[
 2^A S_w^k(x)=3^kx+C_w.
\tag{5}
\]

Here `S_w^k` denotes the affine branch with the prescribed valuations; it is
not asserted before replay that an arbitrary `x` actually follows `w`.

For words `u,v`, chronological concatenation satisfies

\[
 \boxed{
 (k,A,C)_{uv}
 =\left(k_u+k_v,
 A_u+A_v,
 3^{k_v}C_u+2^{A_u}C_v\right).}
\tag{6}
\]

This is exactly the monoid law in the issue #9 supplement.

The expanded shortcut-parity word is

\[
 \pi(w)=10^{a_0-1}10^{a_1-1}\cdots10^{a_{k-1}-1}.
\tag{7}
\]

It has length `A`, odd weight `k`, and the affine numerator `B(pi(w))` of
PR #11/`D-0101` is exactly `C_w`. Thus the accelerated and shortcut-parity
fixed-point equations agree without a change of orientation.

### Lossless decoding

The valid summary `(k,A,C_w)` determines `w` uniquely. If `k=1`, then
`w=(A)` and `C_w=1`. If `k>=2`, then

\[
 C_w=3^{k-1}+2^{a_0}C_{(a_1,\ldots,a_{k-1})},
\tag{8}
\]

and the tail constant is odd. Hence

\[
 a_0=\nu _2(C_w-3^{k-1}).
\tag{9}
\]

Dividing in (8) and iterating recovers every letter; the final letter is also
the remaining valuation total. Thus the affine summary is lossless on valid
words, although a large compressed implementation may prefer to retain its
derivation rather than expand this decoder.

## 2. Divisibility already gives positivity and exact replay

Define

\[
 D_w=2^A-3^k.
\tag{10}
\]

Both `D_w` and `C_w` are odd, `D_w ne 0`, and `C_w>0`. The nonvanishing of
`D_w` follows from unique factorization, since `k,A>=1`.

### Theorem 1 -- complete finite certificate

The word `w` is the exact accelerated itinerary of a positive closed orbit if
and only if

\[
 \boxed{D_w>0\quad\hbox{and}\quad D_w\mid C_w.}
\tag{11}
\]

When (11) holds, put

\[
 n_0={C_w\over D_w}
\tag{12}
\]

and, for `0<=j<=k`, let

\[
 C_j=\sum_{i=0}^{j-1}3^{j-1-i}2^{A_i},
 \qquad
 n_j={3^jn_0+C_j\over2^{A_j}}.
\tag{13}
\]

Then every `n_j` is a positive odd integer,

\[
 n_k=n_0,
\tag{14}
\]

and

\[
 \boxed{
 3n_j+1=2^{a_j}n_{j+1},
 \qquad
 \nu _2(3n_j+1)=a_j}
 \qquad(0\le j<k).
\tag{15}
\]

Thus exact valuation replay is a theorem once (11) is known, not an
additional Diophantine condition.

#### Proof

If a positive orbit follows `w` and closes, (5) gives

\[
 (2^A-3^k)n_0=C_w.
\tag{16}
\]

Since the right side and `n_0` are positive, (11) follows.

Conversely, assume (11). At the cut after `j` letters, (6) gives

\[
 C_w=3^{k-j}C_j+2^{A_j}C_{(a_j,\ldots,a_{k-1})}.
\tag{17}
\]

Reducing `D_wn_0=C_w` modulo `2^(A_j)` and using
`D_w congruent -3^k (mod 2^(A_j))` gives

\[
 3^jn_0+C_j\equiv0\pmod {2^{A_j}},
\tag{18}
\]

because `3` is invertible modulo every power of two. Hence all numbers in
(13) are integers. Direct subtraction of consecutive prefix formulas gives
the first identity in (15), while (16) gives (14).

The quotient in (12) is positive. The recurrence in (15) then makes every
`n_j` positive. Also `C_w` and `D_w` are odd, so `n_0` is odd. For every
`j<k`, rearranging (15) gives

\[
 3n_j=2^{a_j}n_{j+1}-1,
\tag{19}
\]

whose right side is odd. Thus all `n_j` are odd, including the terminal
`n_k=n_0`, and the valuation equality in (15) follows. **QED**

### Trivial endpoint

The certificate has `n_0=1` if and only if

\[
 w=(2,2,\ldots,2).
\tag{20}
\]

Indeed, exact replay from `1` has valuation `nu_2(3*1+1)=2` at every visit.
Conversely, a word of all twos replays the accelerated fixed point `1`.
Therefore a certificate is nontrivial exactly when `n_0>1`, equivalently
when its primitive root below is not the one-letter word `(2)`.

## 3. Exact power factorization

Write

\[
 p=3^k,
 \qquad q=2^A,
\tag{21}
\]

and let `r>=1`. Define the positive geometric factor

\[
 G_r(p,q)=\sum_{i=0}^{r-1}q^{r-1-i}p^i
          ={q^r-p^r\over q-p}.
\tag{22}
\]

The order of `p,q` in the displayed sum is immaterial after reversing the
index.

### Theorem 2 -- power collapse

For the repeated word `w^r`,

\[
 \boxed{
 (k,A,C)_{w^r}
 =\left(rk,rA,C_wG_r(p,q)\right),}
\tag{23}
\]

and

\[
 \boxed{
 D_{w^r}=q^r-p^r=(q-p)G_r(p,q)=D_wG_r(p,q).}
\tag{24}
\]

Consequently,

\[
 {C_{w^r}\over D_{w^r}}={C_w\over D_w},
\tag{25}
\]

and, with absolute values in the gcd,

\[
 \boxed{
 \gcd(C_{w^r},|D_{w^r}|)
 =G_r(p,q)\gcd(C_w,|D_w|).}
\tag{26}
\]

The following are equivalent:

1. `w^r` satisfies the positive cycle condition (11);
2. `w` satisfies the positive cycle condition (11);
3. the candidate for `w^r` exactly replays `w^r`;
4. the same candidate exactly replays `w` and returns after the first copy.

#### Proof

Equation (23) follows from (6) by induction. Equation (24) is the difference
of powers. Both numerator and denominator have the identical positive factor
`G_r`, proving (25)--(26). Since

\[
 q^r>p^r\quad\Longleftrightarrow\quad q>p,
\tag{27}
\]

and

\[
 D_wG_r\mid C_wG_r
 \quad\Longleftrightarrow\quad
 D_w\mid C_w,
\tag{28}
\]

the two divisibility conditions are equivalent. The replay equivalence is
then Theorem 1, or directly (25) followed by the return after the first copy.
**QED**

### Primitive-root corollary

Every nonempty finite word has a unique representation

\[
 w=v^s
\tag{29}
\]

with `v` primitive, meaning that `v` is not a proper power. The word `w` is a
positive cycle certificate if and only if `v` is. When they certify, they
have the same starting value and the same underlying cycle; `w` merely walks
around it `s` times.

In particular, a search hit from a proper power is never genuinely new. The
geometric factors in (23)--(24) are automatic common factors and must be
cancelled before interpreting any denominator factorization or modular
residue as arithmetic progress.

## 4. Cyclic rotations

Let `w=uv`, and abbreviate

\[
 p_u=3^{k_u},\quad q_u=2^{A_u},
 \qquad
 p_v=3^{k_v},\quad q_v=2^{A_v}.
\tag{30}
\]

Then

\[
 C_{uv}=p_vC_u+q_uC_v,
 \qquad
 C_{vu}=p_uC_v+q_vC_u,
\tag{31}
\]

and both words have denominator

\[
 D=q_uq_v-p_up_v.
\tag{32}
\]

The exact rotation identity is

\[
 \boxed{q_uC_{vu}=p_uC_{uv}+C_uD.}
\tag{33}
\]

Since `D` is odd, `gcd(q_u,D)=1`, and therefore

\[
 \boxed{D\mid C_{uv}\quad\Longleftrightarrow\quad D\mid C_{vu}.}
\tag{34}
\]

If `uv` certifies a cycle with initial state `n_0`, the candidate for the
rotation `vu` is exactly the state after the prefix `u`:

\[
 \boxed{
 {C_{vu}\over D}
 ={p_un_0+C_u\over q_u}.}
\tag{35}
\]

Hence positivity, integrality, and exact replay are invariant under every
cyclic rotation. The candidate integer changes because the starting odd
state changes, but the cycle does not.

### Primitive-necklace classification

Let `root(w)` be the primitive root in (29), and let

\[
 \operatorname{can}(w)
 =\text{the lexicographically least cyclic rotation of }\operatorname{root}(w).
\tag{36}
\]

Then nontrivial positive Collatz cycles, up to cyclic choice of starting
point, are in bijection with primitive necklaces `v` satisfying

\[
 2^{A_v}>3^{k_v},
 \qquad
 2^{A_v}-3^{k_v}\mid C_v,
 \qquad
 v\ne(2).
\tag{37}
\]

Indeed, Theorem 1 constructs a cycle from such a necklace. If its odd-state
period were smaller than `k_v`, determinism would make its valuation word a
proper power, contradicting primitivity. Conversely, one traversal of the
least odd-state period of any positive cycle gives a primitive valuation
word, unique up to rotation. Thus two arbitrary certificate words describe
the same cycle if and only if their canonical forms (36) agree.

## 5. Exact local-minimum and period counts

Use Hercher's shortcut operator

\[
 \operatorname{Col}(n)=
 \begin{cases}
 n/2,&n\text{ even},\\
 (3n+1)/2,&n\text{ odd}.
 \end{cases}
\tag{38}
\]

Let `w=v^s` be a positive certificate with primitive root

\[
 v=(b_0,\ldots,b_{h-1}),
 \qquad B=\sum_i b_i.
\tag{39}
\]

The underlying shortcut cycle has exactly

\[
 \boxed{
 K=h\text{ odd entries},
 \qquad
 L=B-h\text{ even entries},
 \qquad
 K+L=B\text{ total entries}.}
\tag{40}
\]

Its exact number of local minima, and also of local maxima, is

\[
 \boxed{
 m(v)=\#\{0\le i<h:b_i\ge2\}.}
\tag{41}
\]

To see this, one accelerated letter `b_i` expands to one odd shortcut step
and `b_i-1` even shortcut steps. For a nontrivial cycle every odd state `x`
is greater than one, so

\[
 {3x+1\over2}>x.
\tag{42}
\]

If the preceding letter is `1`, the preceding state is odd and the incoming
shortcut step is increasing, so the current odd state is not a local
minimum. If the preceding letter is at least `2`, the immediate predecessor
is twice the current odd state, while (42) makes the successor larger; the
current state is a strict local minimum. Equivalently, every letter at least
two produces one local maximum followed by one local minimum. Cyclically this
proves (41). The same formula gives one minimum for the trivial root `(2)`.

The written power has raw counts

\[
 k_w=sh,
 \qquad
 A_w=sB,
 \qquad
 \#\{i:a_i\ge2\}=s\,m(v),
\tag{43}
\]

but these count `s` traversals. The cycle parameters used in lower-bound
theorems are the primitive counts (40)--(41), not the inflated quantities in
(43). In particular, repeating a short word cannot evade a lower bound stated
in terms of the number of local minima.

There are two further exact edge constraints. A nontrivial positive
certificate contains at least one letter `1` and at least one letter at least
`2`. The first assertion follows because if all letters were at least two,
every accelerated step from an odd state greater than one would strictly
decrease, making a return impossible. The second follows already from
`2^A>3^k`, since an all-one word has `2^k<3^k`. Thus for a nontrivial
primitive certificate,

\[
 1\le m(v)\le h-1.
\tag{44}
\]

## 6. Search and grammar consequences

### 6.1 Canonical search space

A cycle search may restrict without loss to one representative of each
primitive necklace. Proper powers add no candidates, and cyclic rotations
add only different starting states on the same candidate cycle. This is an
exact reduction, unlike a bounded census.

The reduction does not apply to arbitrary non-power concatenations,
sandwiches, substitutions, or morphic fixed words. Those families may create
new primitive necklaces and remain legitimate search directions.

### 6.2 Grammar root closure

For a frozen grammar language `mathcal L`, define its effective cycle
frontier by

\[
 \mathcal R(\mathcal L)
 =\{\operatorname{can}(w):w\in\mathcal L\}.
\tag{45}
\]

The grammar finds a cycle exactly when some element of
`mathcal R(mathcal L)` certifies one. A generated power may have a primitive
root outside the literal grammar language. It is safe to route that word to
the root and cache the result; it is not safe to discard it without testing
or otherwise excluding that root. A rigorous negative grammar result must
declare and exhaust the canonical frontier (45), not merely the primitive
words which happen also to lie in `mathcal L`.

### 6.3 Sieve normalization

For a power, cancel `G_r` in both `C` and `D` before factor-guided recursion,
CRT bookkeeping, or gcd statistics. Primes arising only through `G_r` impose
no new divisibility condition. In reduced form, the fixed-point numerator and
denominator are identical to those of the root by (25)--(26).

### 6.4 Bound normalization

Odd-step length, shortcut period, and local-minimum count must all be computed
on the primitive root. A powered representation can falsely appear to cross
classical lower bounds if the raw counts (43) are used. The Hercher bound
quoted in issue #9 is therefore applied to `m(root(w))`, not to the number of
letters at least two in the unreduced generated word.

Rotation quotienting does not remove the need to reconstruct the orbit when
using verified-range or size bounds: (35) gives all odd states, and their
minimum need not occur at the chosen canonical rotation.

### 6.5 Compressed certificate fields

The triple `(k,A,C)` is enough for affine composition, fixed-point
divisibility, and the lossless decoder (8)--(9). A proof-producing grammar
should additionally retain, or compute in compressed form:

1. the primitive root and a canonical rotation;
2. the count `m` of letters at least two;
3. the root counts `(K,L)=(k,A-k)`; and
4. enough derivation data to reconstruct the rotated states for an
   independent replay.

The replay is mathematically automatic under Theorem 1, but independently
checking it remains a valuable defense against implementation, orientation,
and decompression errors.

## 7. Boundary and adversarial audit

1. **Empty word.** It has `k=A=C=D=0`; every number is formally fixed. It is
   not a cycle itinerary and is excluded by `k>=1`.
2. **Critical equality.** `2^A=3^k` is impossible for positive `A,k`, so no
   zero denominator case is hidden.
3. **Wrong sign.** If `2^A<3^k`, then `C_w/D_w<0`; no positive certificate
   exists even when signed divisibility holds.
4. **One letter.** For `w=(a)`, `C_w=1` and `D_w=2^a-3`. The only positive
   divisibility case is `a=2`, giving the trivial root `(2)` and `n=1`.
5. **Trivial powers.** For `w=(2)` and `r=2`, equations (23)--(24) give
   `C_(2,2)=3+4=7` and `D_(2,2)=16-9=7`; the common factor is
   `G_2(3,4)=7`, and the reduced candidate remains `1`.
6. **Power orientation.** At `r=2` and `r=3`, the multiplier in (23) is,
   respectively, `p+q` and `p^2+pq+q^2`, matching both chronological
   applications of (6) and the denominator factorization.
7. **Rotation orientation.** Expanding the two sides of (33) gives
   `p_uq_uC_v+q_uq_vC_u` on each side; no reversal of `u,v` is hidden.
8. **Replay boundary.** The automatic replay proof uses the closed equation
   `D_wn=C_w`. Divisibility of an unrelated finite prefix does not force its
   advertised valuations.
9. **Rotation boundary.** Only cuts between accelerated letters are used.
   Shortcut-parity rotations beginning at an even state are starting points
   on the same full cycle, not separate accelerated valuation words.
10. **Empirical audit.** An independent exact enumeration of all `55,986`
    words of lengths at most six with letters in `{1,...,6}` checked (6),
    (23)--(26), (33)--(35), and Theorem 1. The only six positive integral
    hits were `(2)^k`, `1<=k<=6`, as predicted. This computation is a
    regression check, not an input to any proof.

## 8. Dependency and gap audit

- Equations (4)--(6) are proved directly and match the issue #9 orientation.
- Equation (7) identifies the accelerated constant with PR #11's parity-word
  numerator, so the two source directions are not being conflated silently.
- The prefix congruence (18), positivity, oddness, and exact valuations are
  all proved; no heuristic replay assumption remains.
- The factor `G_r` is positive and identical in numerator and denominator;
  (26) audits reduction as well as rational equality.
- Divisibility under rotation uses `gcd(2^(A_u),D)=1`; this is why no
  unproved cancellation is hidden in (34).
- Primitive-root uniqueness is combinatorics on finite words. The affine
  decoder proves that the valid summary itself loses no word information.
- The local-minimum convention is Hercher's shortcut-cycle convention. Under
  that convention one accelerated valuation at least two gives exactly one
  descending passage and hence one local minimum.
- The published external lower bound is not used to prove the collapse; it
  is only a search-normalization consequence.
- No claim is made that a general compressed grammar has been exhausted, that
  a nontrivial cycle exists, or that Collatz convergence follows.

## Strongest conclusion

> Pure powers are an exactly redundant compressed-cycle family. Every
> positive certificate obtained from `w^r` is already a certificate from
> `w`, and recursively from the primitive root of `w`; every cyclic rotation
> is only another odd starting state on that same cycle. After quotienting by
> powers and rotations, nontrivial positive cycles are exactly admissible
> primitive necklaces. Their true odd length, shortcut period, and
> local-minimum count are the primitive-root counts, so no powered grammar
> production can manufacture progress past a cycle bound.

## Source links

- [Issue #9 -- compressed valuation-word synthesis](https://github.com/gfreund123/collatz/issues/9)
- [PR #11 -- algebraic cycle hunt](https://github.com/gfreund123/collatz/pull/11)
- [Hercher, *There are no Collatz m-Cycles with m <= 91*](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf)

## Suggested next attack

Replace every pure-power branch in the compressed solver by canonical
primitive-root routing. Use the saved budget on genuinely primitive
concatenations, and report negative grammar frontiers through the canonical
root closure (45). A useful next lemma would give compressed, proof-producing
primitive-root and least-rotation algorithms for the actual straight-line
grammar chosen by issue #9.
