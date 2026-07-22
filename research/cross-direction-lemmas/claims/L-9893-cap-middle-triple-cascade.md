# L-9893 -- The cap middle is an 84-triple zero-seam cascade

Claim ID: `L-9893`
Title: Every late 252-cell cap bridge factors through 84 canonical triple seams, excluding generic Hensel reachability
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-c`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `L-9887`, `L-9888`; `PR33/L-9702`, `PR33/T-9703`; frozen `PR3/T-0027`
Scope: every sufficiently late cap-correction chain for the frozen corrected 256-transition stage
Related counterexample candidates: none

## Setup

At scale `m>=8`, put

\[
B=2^m,
\qquad
\delta={B\over256}=2^{m-8},
\tag{1}
\]

\[
t_j=B+j\delta\quad(0\le j\le256),
\qquad
t_{257}=2B+2\delta.
\tag{2}
\]

Let `f_(m,j)` be the frozen local residual transition

\[
f_{m,j}(z)
=
{3^{7(t_j+1)}z+C_{m,j}
 \over
 2^{11(t_{j+2}+1)}}.
\tag{3}
\]

Use the three pieces isolated in `L-9887`:

\[
F_m=T_m\circ I_m\circ H_m,
\tag{4}
\]

where

\[
H_m=f_{m,1}\circ f_{m,0},
\qquad
T_m=f_{m,255}\circ f_{m,254},
\tag{5}
\]

and `I_m` consists of transitions `2,...,253`.

Partition the middle into 84 chronological triples. For `0<=ell<=83`, set

\[
j_\ell=2+3\ell,
\qquad
G_{m,\ell}
=f_{m,j_\ell+2}
 \circ f_{m,j_\ell+1}
 \circ f_{m,j_\ell}.
\tag{6}
\]

Then

\[
I_m
=G_{m,83}\circ\cdots\circ G_{m,1}\circ G_{m,0}.
\tag{7}
\]

For any canonical composite `A`, retain the notation `R(A),S(A),N(A),Q(A)`
from `PR33/L-9702`.

## Statement 1 -- exact triple-seam collapse

For every sufficiently late hypothetical cap-chain stage,

\[
\boxed{S(H_m)=R(G_{m,0}),}
\tag{8}
\]

\[
\boxed{
S(G_{m,\ell})=R(G_{m,\ell+1})
\quad(0\le\ell<83),
}
\tag{9}
\]

and

\[
\boxed{S(G_{m,83})=R(T_m).}
\tag{10}
\]

Consequently the 252-cell bridge is the exact canonical cascade

\[
R(H_m)
\xrightarrow{H_m}
R(G_{m,0})
\xrightarrow{G_{m,0}}
\cdots
\xrightarrow{G_{m,83}}
R(T_m).
\tag{11}
\]

In particular,

\[
\boxed{
R(I_m)=R(G_{m,0}),
\qquad
S(I_m)=S(G_{m,83}).
}
\tag{12}
\]

Every ordinary quotient at a boundary between triples vanishes. No claim is
made about the two local seams inside one triple.

### First cap inequality

The head multiplier is

\[
\log_2N(H_m)
=7(t_0+t_1+2)\log_2 3,
\qquad
t_0+t_1+2=513\delta+2.
\tag{13}
\]

The first triple radix is

\[
\log_2Q(G_{m,0})
=11(t_4+t_5+t_6+3)
=11(783\delta+3).
\tag{14}
\]

Using `3^41<2^65`, hence `log_2 3<65/41`, gives

\[
\boxed{
\log_2Q(G_{m,0})-log_2N(H_m)
>{119718\delta+443\over41}>0.
}
\tag{15}
\]

Thus `N(H_m)<Q(G_(m,0))`.

### Uniform internal cap inequality

Fix `0<=ell<83`, put `j=j_ell`, and write

\[
U_j=t_j+t_{j+1}+t_{j+2}+3.
\tag{16}
\]

The next triple's three denominator heights are each `5delta` above the
corresponding current source height. Therefore

\[
\log_2Q(G_{m,\ell+1})
-\log_2N(G_{m,\ell})
>
165\delta-{4\over41}U_j.
\tag{17}
\]

The largest possible current sum occurs at `j=248`:

\[
U_j\le t_{248}+t_{249}+t_{250}+3
=1515\delta+3.
\tag{18}
\]

Hence, uniformly in `ell`,

\[
\boxed{
\log_2Q(G_{m,\ell+1})
-\log_2N(G_{m,\ell})
>{705\delta-12\over41}>0.
}
\tag{19}
\]

### Canonical-bound induction

`L-9887` supplies the exact middle path from `S(H_m)` to `R(T_m)`. Its first
input has the form

\[
S(H_m)=R(G_{m,0})+Q(G_{m,0})u_0,
\qquad u_0\ge0.
\tag{20}
\]

The canonical bound and (15) give

\[
S(H_m)<N(H_m)<Q(G_{m,0}),
\tag{21}
\]

so `u_0=0`, proving (8). If a triple begins at its canonical correction, its
output continues as

\[
S(G_{m,\ell})
=R(G_{m,\ell+1})+Q(G_{m,\ell+1})u_{\ell+1},
\qquad u_{\ell+1}\ge0.
\tag{22}
\]

But the local canonical tile fact of `PR33/T-9703` and (19) give

\[
S(G_{m,\ell})
<N(G_{m,\ell})
<Q(G_{m,\ell+1}).
\tag{23}
\]

Thus every `u_(ell+1)=0`. Induction proves (9), and the terminal collar
identity of `L-9887` proves (10). **QED**

## Statement 2 -- triples are the first uniform equal-width cascade

The analogous elementary single and pair caps both fail near the terminal
end. At the final internal single seam `252 -> 253`,

\[
\boxed{
\log_2N(f_{m,252})-
\log_2Q(f_{m,253})
>{791\delta+5\over53}>0.
}
\tag{23a}
\]

For the pair starting at `j=250`, put

\[
U=t_{250}+t_{251}+2=1013\delta+2.
\tag{24}
\]

The next pair starts at `252`, and its radix adds total height `8delta`.
Using `3^53>2^84`, hence `log_2 3>84/53`, gives

\[
\boxed{
\log_2N(P_{250})-log_2Q(P_{252})
>{401\delta+10\over53}>0.
}
\tag{25}
\]

Thus the current single or pair multiplier exceeds the following radix at a
late seam. Canonical cap bounds cannot force every width-one or width-two seam
to zero. Width three is the first uniform equal-width cascade justified by
these height margins and this forcing method; (23a) and (25) do not prove that
an actual narrower seam is nonzero.

## Statement 3 -- the generic Hensel sections are not bridge-reachable

Define the bridge-reachable terminal/head mismatch language

\[
\mathcal D_m^{\rm br}
=
\{R(H_{m+1})-S(T_m):
  \text{boundary type words satisfy the triple cascade}\}.
\tag{26}
\]

A two-transition terminal cap and a two-transition next-head correction each
depend on four tower symbols. Without physical cross-stage overlap,

\[
\boxed{|\mathcal D_m^{\rm br}|\le4^8=65536.}
\tag{27}
\]

For a physical directive, the last two tower instances at scale `m` are the
first two at scale `m+1`. Only six independent boundary symbols remain, so

\[
\boxed{|\mathcal D_m^{\rm br}|\le4^6=4096.}
\tag{28}
\]

The 84 seam equations can only reduce this language or identify more words.

By contrast, `L-9888` proves that unrestricted mismatch normalization has at
least

\[
2^{D-\lceil\log_2N(T_m)\rceil}
>
2^{(1779/10496)2^m-8/41-1}
\tag{29}
\]

distinct residual functions at its critical depth. Already at `m=8`, this is
larger than `2^42`. A physical bridge language with at most 4096 inputs can
visit at most 4096 of those sections. Therefore

\[
\boxed{
\text{the unrestricted state lower bound of `L-9888` is not witnessed by
the physical bridge language.}
}
\tag{30}
\]

This does not refute `L-9888`: that claim explicitly treats unrestricted
mismatches. It refutes only promotion of its exponential bound to the
bridge-reachable language. At a fixed scale, a prefix trie for at most `K`
admissible `D`-bit mismatches has at most `1+KD` states. Thus physical
restriction can reduce the nonuniform per-scale cost to `O(4096D)`, but no
scale-uniform bounded controller follows.

## Statement 4 -- endpoint and scale transport

For every canonical composite `A`, exact endpoints `x -> y` obey

\[
\boxed{
N(A)(x-R(A))=Q(A)(y-S(A)).
}
\tag{31}
\]

Because `N(A)` is odd,

\[
x
=R(A)+Q(A)N(A)^{-1}(y-S(A))
\quad\text{in }\mathbb Z_2.
\tag{32}
\]

If `Q(A)=2^{D(A)}`, then every `h<=D(A)` has

\[
x\equiv R(A)\pmod {2^h}.
\tag{33}
\]

The triple cascade strengthens this low-bit reset to exact equality at each
triple input.

For the final stitch, put

\[
\mathcal N_m=N(T_m)
=3^{(7147/256)2^m+14},
\qquad
\mathcal Q_m=Q(H_{m+1})
=2^{(5687/128)2^m+22}.
\tag{34}
\]

Then

\[
\boxed{
\mathcal N_{m+1}={\mathcal N_m^2\over3^{14}},
\qquad
\mathcal Q_{m+1}={\mathcal Q_m^2\over2^{22}}.
}
\tag{35}
\]

If `d_m=R(H_(m+1))-S(T_m)` and

\[
a_{m,h}=[d_m\mathcal N_m^{-1}]_{2^h},
\tag{36}
\]

then the exact coefficient transport is

\[
\boxed{
a_{m+1,h}
=[3^{14}\mathcal N_m^{-2}d_{m+1}]_{2^h}.
}
\tag{37}
\]

This is not autonomous in `a_m` or `d_m`: all middle inter-triple quotients
reset, and `d_(m+1)` is regenerated from the next six boundary symbols.

## What this advances

- `L-9887` reduced a cap stage to one 252-cell bridge and two collars.
  Equations (8)--(10) now resolve that whole bridge into 84 exact canonical
  triple seams.
- The remaining cap-chain existence problem is finite and local at each
  scale: an 84-layer overlap graph, not an unrestricted Montgomery mismatch.
- The result closes the tempting inference from `L-9888`'s generic
  exponential section count to the physical cap language.
- Equation (37) isolates why no scalar scale recurrence has appeared: the new
  boundary mismatch is regenerated rather than transported by the middle.

## Dependency audit

- `L-9887` supplies the exact head/middle/tail collar path.
- `PR33/L-9702` supplies the canonical composite endpoint law and quotient
  decomposition.
- `PR33/T-9703` supplies the local nonnegative canonical bound
  `0<=S(A)<N(A)` for every triple tile.
- Frozen `PR3/T-0027` supplies the corrected height schedule and the
  four-symbol dependence of each two-transition boundary cap.
- `L-9888` is used only for the comparison with unrestricted Hensel sections.
- The numerical margins use the elementary rational bounds
  `3^41<2^65` and `3^53>2^84`.

## Gap audit

- Everything is conditional on the hypothetical late cap chain and frozen
  corrected stage interface.
- Exact seam rigidity does not prove that a compatible 84-edge type path
  exists or fails to exist.
- No theorem here makes the terminal/head mismatch nonzero.
- Use the 65536 bound if physical cross-stage overlap is not imposed; the
  sharper 4096 bound assumes the shared boundary symbols.
- The trie observation is nonuniform in scale and is not a bounded-router
  construction.
- No marked initialization or Collatz conclusion is supplied.

## Adversarial checks

- The 84 triples cover exactly transitions `2,...,253`; the last begins at
  `j=251`.
- The internal inequality uses current starts only through `j=248`, because
  it compares with a following triple.
- At `m=8`, `(705delta-12)/41` is already positive.
- Pair failure is an obstruction to this cap argument, not a proof that a
  single or pair seam is nonzero.
- The 4096 count bounds inputs, hence reachable sections; it does not bound
  the total unrestricted section set.
- Equation (37) transports the odd normalization coefficient but still
  contains the newly generated mismatch `d_(m+1)`.

## Remaining uncertainty

Does the 84-layer triple-seam graph have any path for a sufficiently late
scale? The middle is now a finite overlap constraint, while only six boundary
symbols survive into the final stitch.

## Suggested next attack

Build the 84-layer graph at a scale-stable small modulus. Each triple depends
on five consecutive tower symbols and adjacent triples share two. Either prove
that one required seam has no admissible edge uniformly in scale, or construct
an exact compatible path through all 84 seams before returning to the final
terminal/head mismatch.
