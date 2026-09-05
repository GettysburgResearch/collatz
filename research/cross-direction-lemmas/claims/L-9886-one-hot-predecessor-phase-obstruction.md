# L-9886 -- Legal-predecessor phase obstruction to one-hot exposure

Claim ID: `L-9886`
Title: Every predecessor depth has an exact residue phase, forcing unbounded lower renewal lifetimes along exposing depths
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-b`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `L-9826`, `L-9834`, `L-9883`, `L-9885`
Scope: the one-hot exposure family and all finite legal predecessor chains in the `64 -> 81` survivor chart
Related counterexample candidates: none

## Setup

The ordinary survivor transition with directive `a in {0,1}` is

\[
T_a(B)={81B-17a\over64},
\qquad B\equiv a\pmod {64}.
\tag{1}
\]

At a nontrivial exposing depth `n>=5` from `L-9883`, put

\[
A_*=64^{n-1}.
\tag{2}
\]

Fix `k>=1` and a binary history

\[
a=(a_0,\ldots,a_{k-1}).
\tag{3}
\]

Define

\[
P_k(a)
=\sum_{i=0}^{k-1}a_i81^{k-1-i}64^i
\tag{4}
\]

and

\[
A_k(a)=-17\,64^{-k}P_k(a)\pmod {81^k}.
\tag{5}
\]

## Statement 1 -- complete predecessor classification

There is a legal chain

\[
B_0\xrightarrow{a_0}B_1\xrightarrow{a_1}\cdots
\xrightarrow{a_{k-1}}B_k=A_*
\tag{6}
\]

if and only if

\[
\boxed{
a_{k-1}=1,
\qquad
64^{n-1}\equiv A_k(a)\pmod {81^k}.
}
\tag{7}
\]

When it exists, the predecessor is

\[
\boxed{
B_0={64^kA_*+17P_k(a)\over81^k}.
}
\tag{8}
\]

For every one of the `2^(k-1)` histories ending in `1`,

\[
A_k(a)\equiv1\pmod9.
\tag{9}
\]

Moreover,

\[
\boxed{
\operatorname{ord}_{81^k}(64)=3^{4k-2},
\qquad
\langle64\rangle
=\{u\in(\mathbb Z/81^k\mathbb Z)^\times:u\equiv1\pmod9\}.
}
\tag{10}
\]

Hence every history in (7) gives a unique exponent class

\[
n-1\equiv s_k(a)\pmod {3^{4k-2}},
\tag{11}
\]

and distinct histories give distinct classes. After imposing the exposing
phase `n=1 mod 4`, the legal `k`-predecessor depths are exactly `2^(k-1)`
classes modulo

\[
\boxed{4\cdot3^{4k-2}.}
\tag{12}
\]

The all-one history has `s_k=0`, so it gives the explicit subfamily

\[
\boxed{
n\equiv1\pmod {4\cdot3^{4k-2}},
\qquad
B_0=1+{64^k(A_*-1)\over81^k}.
}
\tag{13}
\]

For `k=1`, this is

\[
n\equiv1\pmod {36},
\qquad
B_0=1+{64(A_*-1)\over81},
\tag{14}
\]

the first automatic obstruction phase.

## Proof of Statement 1

Iterating (1) through (6) gives

\[
64^kA_*=81^kB_0-17P_k(a),
\tag{15}
\]

which proves (8) and the congruence in (7). Reduction of the last backward
step modulo `81` requires

\[
A_*\equiv a_{k-1}\pmod {81}.
\tag{16}
\]

Since every power of `64` is `1 mod 9`, a binary last digit must be `1`.
Conversely, let the combined numerator in (15) be divisible by `81^k`.
For each suffix beginning at `a_i`, multiply its backward numerator by
`64^i`. Its difference from the full numerator is a sum whose every term is
divisible by `81^(k-i)`. Since `64` is a unit modulo `81`, that suffix
numerator is divisible by `81^(k-i)`. Thus every backward quotient is
integral. The backward identity

\[
81B_i=64B_{i+1}+17a_i
\tag{17}
\]

also gives `B_i=a_i mod64`, so the whole chain is legal.

Modulo `9`, only the last term of (4) survives. With `a_(k-1)=1` and
`64=1 mod9`, equation (5) gives (9).

The lifting-the-exponent identity is

\[
v_3(64^t-1)=v_3(64-1)+v_3(t)=2+v_3(t).
\tag{18}
\]

Therefore the order modulo `81^k=3^(4k)` is `3^(4k-2)`. The units congruent
to `1 mod9` form a group of that same order, proving (10). Equations
(9)--(10) give the unique exponent class (11).

If two histories gave the same class `A_k`, their `P_k` values would be
congruent modulo `81^k`. But

\[
0\le P_k(a)\le\sum_{i=0}^{k-1}81^{k-1-i}64^i
={81^k-64^k\over17}<81^k,
\tag{19}
\]

so congruence forces equality. At the first index `i` where two distinct
histories differ, the corresponding difference term has exact `2`-adic
valuation `6i`, whereas every later term is divisible by `2^(6i+6)`, a
contradiction. This proves the class count. The odd order in (11) combines
uniquely with `n=1 mod4`, giving (12).

For the all-one history, the geometric sum in (19) is exact, so

\[
A_k(a)\equiv1\pmod {81^k}.
\tag{20}
\]

Equations (8) and (20) give (13). **QED**

## Statement 2 -- every such predecessor defeats global exposure

Every nontrivial predecessor in Statement 1 satisfies

\[
\boxed{2\le B_0<A_*.}
\tag{21}
\]

Suppose the one-hot candidate `A_*` has the `m`-step zero-block extension
selected in `L-9883`. Then `B_0` survives `k+n+m` transitions. At depth `n`
it is already a canonical lower prefix, and

\[
\boxed{
R_{n-1}(B_0)={B_0-a_0\over64}<64^{n-2},
\qquad
\ell_n(B_0)\ge m+k.
}
\tag{22}
\]

Thus `B_0` is a block-zero competitor at horizon `m`, so the candidate
`A_*` is not the global minimum. In the lifetime notation of `L-9885`,

\[
\boxed{H_n^-\ge m+k.}
\tag{23}
\]

### Proof

The inverse branches in (17) are increasing and map the fixed points `0,1`
to themselves. A legal chain ending at `A_*>1` therefore has `B_0>1`.
Also (19) gives

\[
B_0
\le1+\left({64\over81}\right)^k(A_*-1)<A_*,
\tag{24}
\]

which proves (21).

Starting from `B_0`, first follow the `k` legal predecessor transitions to
`A_*`, then the `n+m` transitions of the exposed one-hot word and its suffix.
Since `B_0<A_*<64^n`, its first `n` directives have canonical representative
`B_0`. It remains unchanged for the next `m+k` directives. Equation (7) of
`L-9885` proves the lifetime bound, and equation (5) there gives the centered
residue in (22). The strict centered inequality follows from `B_0<A_*`.
Finally, `L-9885/(21)` proves failure of global exposure. **QED**

## Statement 3 -- no suffix-uniform promotion bound

Fix a suffix `v` of length `m`. The exposing congruence of `L-9883` selects
one depth class modulo

\[
2^{6m+2}.
\tag{25}
\]

For every `k`, the Chinese remainder theorem intersects this power-of-two
class with every odd predecessor class (11). Hence there are infinitely many
depths exposing the same suffix `v` for which (23) holds. As `k` is arbitrary,

\[
\boxed{
\sup_{\substack{n\text{ exposes }v}}H_n^-=\infty.
}
\tag{26}
\]

There is therefore no bound depending only on the suffix and its horizon that
promotes all centered one-hot exposures to global minima.

This does not show that `H_n^-=infinity` at one fixed depth: the CRT depth
changes with `k`.

## Statement 4 -- arbitrarily late first differences still fail

Choose the predecessor history

\[
a=0^{k-1}1
\tag{27}
\]

and an exposing CRT depth `n>k` in its class. The competitor and the one-hot word
agree in their first `k-1` directives and first differ at position `k-1`.
The signed-difference law of `L-9834` gives

\[
\boxed{
v_2(A_*-B_0)=6(k-1),
\qquad
{A_*-B_0\over64^{k-1}}
\equiv-81^{-(k-1)}\pmod {64}.
}
\tag{28}
\]

The least positive unit in (28) cycles as

\[
63,15,31,47
\tag{29}
\]

with `k-1 mod4`. Thus lower block-zero competitors can agree with the
candidate for arbitrarily many initial digits while their renewal lifetime is
at least `m+k`. A bounded first-difference window cannot bound `H_n^-`.

### Proof

For (27), the candidate-minus-competitor signed word first has the digit `-1`
at index `k-1`. `L-9834/(21)` gives the exact base-64 valuation. Dividing its
cylinder formula by `64^(k-1)` gives

\[
17(-1)81^{-k}\equiv-81^{-(k-1)}\pmod {64},
\tag{30}
\]

because `81=17 mod64`. Direct inversion modulo `64` gives the four-cycle in
(29). **QED**

## What this advances

- The remaining promotion criterion in `L-9883` now has an infinite explicit
  family of lower block-zero competitors.
- Every finite predecessor depth is classified by exact residue phases, not
  by search.
- Even fixing the exposed suffix does not bound the lower renewal lifetime
  uniformly across exposing depths.
- The signed-difference law cannot help through a bounded first-difference
  argument: the obstruction can postpone its first difference arbitrarily.

## Dependency audit

- `L-9826` supplies the exact survivor transition (1).
- `L-9883` supplies the one-hot candidate and exposing depth class.
- `L-9885` supplies the equivalence between block zero, centered renewal
  lifetime, and global promotion.
- `L-9834` is used only for the exact signed-difference corollary (28).
- LTE and the Chinese remainder theorem are elementary here.

## Gap audit

- All predecessor families lie inside the already bad one-step phase
  `n=1 mod36`; they stratify its failure but do not decide the other exposing
  phases.
- The depth `n` changes with `k`, so (26) does not construct one infinite
  ordinary survivor.
- A particular exposing suffix outside all predecessor phases may still be a
  global minimum.
- No successor-promotion criterion is proved.
- The result obstructs this one-hot exposure strategy, not arbitrary global
  survivor selectors.

## Adversarial checks

- The last predecessor directive must be `1`; omitting it admits impossible
  residue classes.
- Divisibility by `81^k` is read through every backward quotient, not only at
  the combined endpoint.
- The history count is `2^(k-1)`, not `2^k`.
- The exposing power-of-two class already imposes `n=1 mod4`; after matching
  that shared condition, its modulus and the odd predecessor modulus in (11)
  are coprime, so CRT creates no further compatibility assumption.
- Equation (28) retains the unit `-81^(-(k-1))`; the valuation alone loses
  the four residue phases.

## Remaining uncertainty

Which exposing phases outside `n=1 mod36` admit lower block-zero competitors?
The exact predecessor classifier suggests searching by the first future time
at which a lower ordinary survivor meets, rather than precedes, the one-hot
orbit.

## Suggested next attack

Classify orbit mergers into later points of the one-hot trajectory, not only
predecessors of its initial value `A_*`. Their congruence classes may cover
additional exposing phases and could decide whether any one-hot cylinder is
ever globally promoted.
