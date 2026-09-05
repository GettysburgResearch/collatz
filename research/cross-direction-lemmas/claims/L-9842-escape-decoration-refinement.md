# L-9842 -- Ternary refinement of horizontal escape decorations

Claim ID: `L-9842`  
Title: Horizontal escape decorations form a finite ternary-closed alphabet with an exact width-refinement recurrence  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9825`, `L-9838`; the standard Eilenberg kernel criterion and Cobham theorem  
Scope: decoration words on positive-valuation horizontal cycles of a 2-automatic shortcut-component coloring  
Related counterexample candidates: none

## Definitions

Let `s=(s_n)_(n>=0)` be finite-valued, 2-automatic, and satisfy

\[
s_{2m}=s_m\quad(m\ge1),
\qquad
s_{2m+1}=s_{3m+2}\quad(m\ge0).
\tag{1}
\]

Write

\[
c_{N,x}(n)=s_{3^Nn+x},
\qquad
0\le x<3^N,
\tag{2}
\]

and put

\[
\mathcal K=\mathcal K_2(s).
\tag{3}
\]

For a sequence `f`, define its three ternary sections by

\[
P_af(n)=f(3n+a),
\qquad
a\in\{0,1,2\}.
\tag{4}
\]

The escape-decoration alphabet is the set of sequences

\[
\boxed{
\mathcal D
=\{c_{N,x}:N\ge1,\ 0<x<3^N,\ x\equiv2\pmod3\}.
}
\tag{5}
\]

Repeated offset labels which define the same sequence contribute one member
to `D`.

Fix `h>=1` and width `k>=1`. Set

\[
E=h+k,
\qquad
L_k=2\cdot3^{k-1}.
\tag{6}

\]

For `0<=j<L_k`, let

\[
r_{k,j}=[2^{-j}]_{3^k},
\qquad
w_{k,j}=r_{k,j}\bmod2.
\tag{7}

\]

These are the normalized horizontal offset and staying bit from `L-9838`.
Define

\[
M_{h,k}=3^{h+k+1}
\tag{8}
\]

and the canonical escape offset

\[
\boxed{
v_{h,k,j}
=\left[
2^{-1}(1+3^{h+1}r_{k,j})
\right]_{M_{h,k}}.
}
\tag{9}

\]

The corresponding decoration state is

\[
\boxed{
d_{h,k,j}=c_{h+k+1,v_{h,k,j}}\in\mathcal D.
}
\tag{10}

\]

## Statement

### 1. The escape alphabet is finite and ternary-section closed

Every member of `D` is an absolute primitive ternary state. The uniform
primitive collapse `L-9838/(16b)` therefore gives

\[
\boxed{
\mathcal D\subseteq\mathcal K,
\qquad
|\mathcal D|\le|\mathcal K|<\infty.
}
\tag{11}
\]

Moreover, for every `d=c_(N,x) in D` and `a in {0,1,2}`,

\[
\boxed{
P_ad
=c_{N+1,x+a3^N}
\in\mathcal D.
}
\tag{12}

\]

Thus `D` is simultaneously a finite ternary kernel container and a subset of
the finite binary kernel of `s`. Every decoration state is both 2-automatic
and 3-automatic, hence eventually periodic by Cobham.

This does not make a decoration constant: it need not satisfy the component
identities (1) as a sequence in its own argument.

### 2. Exact decorated-cycle normal form

Let

\[
f_{h,k,j}=c_{h+k,3^hr_{k,j}}.
\tag{13}

\]

Indices in `j` are cyclic modulo `L_k`. The two binary children of every
positive-valuation horizontal state are exactly

\[
\boxed{
E_{w_{k,j}}f_{h,k,j}=f_{h,k,j+1},
\qquad
E_{1-w_{k,j}}f_{h,k,j}=d_{h,k,j}.
}
\tag{14}

\]

Consequently a coheight-`k` stratum is one directed binary cycle carrying the
full-period staying word `w_(k,0)...w_(k,L_k-1)` from `L-9838`, with every
off-cycle edge decorated by one of the finitely many eventually periodic
states in `D`.

### 3. Exact width-`k` to width-`k+1` lift

For `0<=j<L_k` and `m in {0,1,2}`, define the unique lift digit

\[
\tau_{k,j,m}\in\{0,1,2\}
\tag{15}
\]

by

\[
\boxed{
r_{k+1,j+mL_k}
=r_{k,j}+\tau_{k,j,m}3^k.
}
\tag{16}

\]

For each fixed `k,j`, the three digits `tau_(k,j,m)` form a permutation of
`0,1,2`.

Put

\[
\zeta_{h,k,j}
=\frac{
2v_{h,k,j}-(1+3^{h+1}r_{k,j})
}{M_{h,k}}
\in\mathbb Z.
\tag{17}

\]

Define

\[
\boxed{
a_{h,k,j,m}
=\left[2(\tau_{k,j,m}-\zeta_{h,k,j})\right]_3
\in\{0,1,2\}.
}
\tag{18}

\]

Then the lifted escape offsets and decoration states satisfy

\[
\boxed{
\begin{aligned}
v_{h,k+1,j+mL_k}
&=v_{h,k,j}+a_{h,k,j,m}M_{h,k},\\
d_{h,k+1,j+mL_k}
&=P_{a_{h,k,j,m}}d_{h,k,j}.
\end{aligned}
}
\tag{19}

\]

For each fixed old position `j`, the three digits `a_(h,k,j,m)` also form a
permutation of `0,1,2`. Hence the three columns above `d_(h,k,j)` are exactly

\[
\boxed{
\{d_{h,k+1,j+mL_k}:m=0,1,2\}
=\{P_0d_{h,k,j},P_1d_{h,k,j},P_2d_{h,k,j}\}
}
\tag{20}

\]

as a multiset. Equation (19) supplies the exact arithmetic permutation, not
only the unordered triple.

### 4. Finite incidence-matrix recurrence

Index rows and columns by the finite set `D`, and define

\[
\boxed{
\mathbf A_{g,f}
=\#\{a\in\{0,1,2\}:P_af=g\}.
}
\tag{21}

\]

Every column sum of `A` is three. Let the decoration-count vector be

\[
\mathbf N_{h,k}(f)
=\#\{0\le j<L_k:d_{h,k,j}=f\}.
\tag{22}

\]

Then the width refinement has the exact finite linear recurrence

\[
\boxed{
\mathbf N_{h,k+1}=\mathbf A\mathbf N_{h,k}
\qquad(h\ge1,k\ge1).
}
\tag{23}

\]

In particular, all additive statistics of the decoration word are controlled
by one fixed finite substitution matrix, independent of `h` and `k`.

### 5. The remaining ordered-cocycle obstruction

The ordered word at width `k+1` is not obtained from (20) by one proved
stationary substitution. Its three copies are placed at the column positions

\[
j,
\qquad
j+L_k,
\qquad
j+2L_k,
\tag{24}

\]

and their order is the permutation

\[
\pi_{h,k,j}:m\longmapsto a_{h,k,j,m}
\quad\text{in }S_3.
\tag{25}

\]

The exact formula (18) computes this permutation. `L-9844` subsequently shows
that its schedule is generated by a three-state transducer driven by the
staying word and a fixed alternating clock; it still need not be a function
of the finite decoration label `d_(h,k,j)` alone.

Therefore (23) alone controls the full multiset of exits but not their cyclic
order relative to the least-period staying word. `L-9844` restores that order,
and `L-9849` proves that different unabsorbed widths remain distinct as
infinite root sequences. Cumulative finiteness is now exactly an eventual
finite-core absorption question.

## Proof

### Escape alphabet

An offset `x congruent 2 modulo 3` is primitive, so (11) is `L-9838/(16b)`.
Direct calculation gives

\[
P_ac_{N,x}(n)
=s_{3^N(3n+a)+x}
=c_{N+1,x+a3^N}(n).
\tag{26}

\]

The new offset remains two modulo three and is in the canonical range, which
proves (12). Finiteness plus closure under all `P_a` proves 3-automaticity by
the ternary-kernel criterion. Membership in `K_2(s)` proves 2-automaticity,
so Cobham gives eventual periodicity.

Conversely, every offset `x congruent 2 modulo 3` is an escape offset from the
preceding depth. Indeed, solve

\[
R\equiv\frac{2x-1}{3}\pmod {3^{N-1}}.
\tag{27}

\]

Then `2x congruent 3R+1 modulo 3^N`, which is exactly the escape congruence in
`L-9838/(10)`. Thus (5) is precisely the global escape-decoration alphabet.

### Decorated horizontal cycle

The normalized residues `r_(k,j)` run through all units modulo `3^k` under
multiplication by the inverse of two. Multiplication by `3^h` gives the
stratum of valuation `h` at depth `h+k`. The staying bit is its parity because
`3^h` is odd. The other child has canonical offset determined by

\[
2v\equiv1+3^{h+1}r_{k,j}pmod {M_{h,k}},
\tag{28}

\]

which is (9). Substitution in the child normal form `L-9838/(9)` proves (14).

### Width refinement

The width-`k+1` unit orbit reduces modulo `3^k` to the width-`k` orbit. Since
its length is `3L_k`, the positions `j,j+L_k,j+2L_k` are the three distinct
lifts of `r_(k,j)`. This proves (16) and the permutation assertion for `tau`.

The new escape congruence, with modulus `3M_(h,k)`, reduces to (28) modulo
`M_(h,k)`. Hence there is a unique digit `a in {0,1,2}` such that

\[
v_{h,k+1,j+mL_k}
=v_{h,k,j}+aM_{h,k}.
\tag{29}

\]

Insert (16), (17), and (29) into the new congruence. After division by
`M_(h,k)`, one obtains

\[
\zeta_{h,k,j}+2a-\tau_{k,j,m}\equiv0\pmod3.
\tag{30}

\]

Since the inverse of two modulo three is two, this is exactly (18). The map
from `tau` to `a` is affine with nonzero slope, so it preserves the
permutation property.

Finally,

\[
\begin{aligned}
d_{h,k+1,j+mL_k}(n)
&=s_{3M_{h,k}n+v_{h,k,j}+aM_{h,k}}\\
&=d_{h,k,j}(3n+a),
\end{aligned}
\tag{31}

\]

which proves (19)--(20). Summing the three children over every old position
gives exactly the incidence recurrence (23). This completes the proof. QED

## Motivation

`L-9838` reduces every positive-valuation binary kernel to a horizontal cycle
whose off-cycle children lie in `K_2(s)`. This claim computes those children
and their width refinement exactly. The exit labels themselves are no longer
an uncontrolled source of states: they live in one finite alphabet, are
ternary-section closed, and even have eventually periodic integer sequences.

This claim stops at order: a finite incidence matrix sees how many times each
decoration occurs but forgets which decoration is attached to which position
of the exponentially long, full-period horizontal word. `L-9844` recovers
that order, and `L-9849` turns cross-width equality into finite-core
absorption versus width rigidity.

## Dependency audit

- `L-9838` supplies primitive collapse, the horizontal cycle, and its exact
  child normal form.
- `L-9825` supplies the component identities underlying those child formulas.
- The ternary closure, canonical lift recurrence, permutation law, and
  incidence matrix are proved directly here.
- Cobham is used only to conclude eventual periodicity of individual escape
  decorations; no component rigidity is applied to them.
- No Collatz connectivity or convergence premise is assumed.

## Gap audit

- Eventual periodicity of every off-cycle decoration does not imply eventual
  periodicity of the cycle root; automatic Toeplitz-type constructions can
  retain information in an indefinitely followed staying path.
- The incidence recurrence (23) is abelianized and loses cyclic order.
- This claim's incidence recurrence forgets the permutation schedule;
  `L-9844` supplies its finite-state generator and `L-9849` shows why that
  alone does not identify unabsorbed roots of different widths.
- Even a stationary substitution for the decoration word would still need to
  be combined with the full-period staying word before root-state finiteness
  followed.
- No nonconstant automatic component coloring is constructed or excluded.

## Adversarial tests

- Decorations are offsets congruent to two modulo three, not all primitive
  offsets. Offsets congruent to one occur on their binary horizontal cycles.
- In (16), the three lifts occupy columns separated by `L_k`; treating them as
  three adjacent letters changes the ordered recurrence.
- The correction `zeta_(h,k,j)` in (18) is essential. The naive rule
  `a congruent 2*tau modulo 3` can select the wrong canonical lift.
- Equality in (20) is a multiset equality because ternary children can define
  equal sequences.
- Cobham makes a decoration eventually periodic, not constant: a decoration
  is not known to satisfy (1) in its own argument.

## Remaining uncertainty

`L-9844` resolves the `S_3`-valued cocycle, and `L-9849` resolves equality
outside the finite binary core. The remaining datum is which widths are
absorbed into that core. Finitely many exceptional widths force constancy;
any nonconstant coloring must have infinitely many unabsorbed widths.

## Suggested next attack

Use the padded-digit equality test in `L-9849` to construct a finite separating
family for membership in the core. A uniform separator would turn absorption
at width `k` into an explicit condition on the ordered decoration word.
