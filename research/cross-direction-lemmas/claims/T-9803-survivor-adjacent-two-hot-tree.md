# T-9803 -- Adjacent two-hot lifts leave a positive-dimensional formal exceptional set

Claim ID: `T-9803`
Title: Adjacent two-hot lifts have an exact correlation law, and libraries of at most 62 fixed templates cannot cover every formal exposure phase
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave13-survivor-twohot`
Reviewing agents: `gpt56-synthesis-01-wave13-adelic-bridge`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `L-9826`, `L-9883`, `L-9885`, `L-9896`, `R-9806`
Scope: fixed-shape multi-hot block-zero competitors inside one suffix-exposure progression for the `64 -> 81` survivor chart
Related counterexample candidates: none

## Setup

Fix

\[
m\ge1,
\qquad
v\in\{0,1\}^m,
\qquad
r=\alpha_m(v).
\tag{1}
\]

Retain the suffix-exposure progression of `L-9896` and `R-9806`:

\[
n=n_0+O_0t,
\qquad
O_0=\operatorname {ord}_{64^{m+1}}(81)=2^{6m+2}.
\tag{2}
\]

Here `n_0` solves

\[
81^{-n_0}\equiv(17+64r)^{-1}\pmod {64^{m+1}}.
\tag{3}
\]

Put

\[
M=64^{m+1},
\qquad
N_h=64^{h-1},
\qquad
K_h={N_h\over M}=64^{h-m-2}
\quad(h\ge m+2),
\tag{4}
\]

and let

\[
\mathfrak M_h=MN_h=64^{m+h}.
\tag{5}
\]

For an ordinary parameter `t` and a delay `h<n`, consider the two words of
common length `n+m`

\[
\begin{aligned}
\omega_h^{(1)}&=0^{n-h}1\,0^{m+h-1},\\
\omega_h^{(2)}&=0^{n-h}11\,0^{m+h-2}.
\end{aligned}
\tag{6}
\]

The first is the delayed one-hot word of `L-9896`; the second has one
additional adjacent hot digit.  Define their reduced coefficients

\[
\begin{aligned}
D_h^{(1)}(t)
&=\left[17\,81^{h-1-n}\right]_{\mathfrak M_h},\\
D_h^{(2)}(t)
&=\left[17\cdot145\,81^{h-2-n}\right]_{\mathfrak M_h}.
\end{aligned}
\tag{7}
\]

The number `145=81+64` is not an approximation: the second hot digit gives
the exact odd-unit multiplier

\[
U={81+64\over81}={145\over81},
\qquad
D_h^{(2)}=[UD_h^{(1)}]_{\mathfrak M_h}.
\tag{8}
\]

For formal `t in Z_2`, powers in (7) mean their unique compatible
finite-level extensions.  Equivalently, with

\[
g=81^{-O_0},
\tag{9}
\]

one replaces `n` by `n_0+O_0t` and evaluates `g^t` modulo each
`mathfrak M_h`.  The resulting functions depend only on `t mod N_h`.
Here and below `mu` denotes normalized counting measure at a finite phase
level, equivalently normalized Haar measure on its inverse-limit cylinder.

## Statement 1 -- both templates are exact lower block-zero events

The two canonical representatives are

\[
\boxed{
\alpha_{n+m}(\omega_h^{(i)})
=64^{n-h}D_h^{(i)}(t)
\qquad(i=1,2).
}
\tag{10}
\]

They lie below the exposed candidate

\[
A_*=64^{n-1}
\tag{11}
\]

if and only if, respectively,

\[
E_h^{(i)}:\qquad D_h^{(i)}(t)<N_h.
\tag{12}
\]

Whenever (12) holds at an ordinary valid delay `h<n`, the final `m` zero
digits leave the depth-`n` representative unchanged.  Thus each event gives
a genuine lower block-zero competitor, not merely a congruence collision.

For `i=1,2`, reduce `D_h^(i)` modulo `M` and write uniquely

\[
D_h^{(i)}(t)=c_h^{(i)}+M Q_h^{(i)}(t),
\qquad
0<c_h^{(i)}<M,
\qquad
0\le Q_h^{(i)}(t)<N_h.
\tag{13}
\]

Then each

\[
Q_h^{(i)}:\mathbb Z/N_h\mathbb Z
\longrightarrow\mathbb Z/N_h\mathbb Z
\tag{14}
\]

is a permutation, and

\[
\boxed{
E_h^{(i)}\iff Q_h^{(i)}(t)<K_h,
\qquad
\#E_h^{(i)}=K_h,
\qquad
\mu(E_h^{(i)})={1\over M}.
}
\tag{15}
\]

More precisely, for every `1<=a<=h`, both coordinates retain exactly the
lower exposure phase:

\[
\boxed{
Q_h^{(i)}(t_1)\equiv Q_h^{(i)}(t_2)\pmod {N_a}
\iff
t_1\equiv t_2\pmod {N_a}.
}
\tag{16}
\]

### Proof

The finite-cylinder formula of `L-9826` gives the first line of (10).
Factoring the two hot contributions in the second word gives

\[
17\,64^{n-h}81^{h-1-n}
\left(1+{64\over81}\right),
\tag{17}
\]

which proves its line of (10) and the exact factor (8).  Comparing (10) with
(11) proves (12).  Under that strict inequality the full representative is
below `64^n`; reduction from depth `n+m` to depth `n` therefore does not
change it.  The terminal-block identity of `L-9885` makes this an exact zero
renewal block.

Odd-base LTE gives

\[
v_2(81^{O_0}-1)=6m+6.
\tag{18}
\]

Hence `g` has exact order `N_h` modulo `mathfrak M_h` and exact order `N_a`
modulo `MN_a`.  Multiplication by either fixed coefficient in (7) changes
only the initial unit in this orbit.  Thus, as `t` runs modulo `N_h`, each
`D_h^(i)` visits every lift of `c_h^(i)` modulo `M` exactly once.  This proves
(14).  Because `c_h^(i)` is odd and positive,

\[
c_h^{(i)}+M Q_h^{(i)}<N_h=MK_h
\iff Q_h^{(i)}<K_h,
\tag{19}
\]

which proves (15).

Finally, equality of two `Q_h^(i)` coordinates modulo `N_a` is equivalent to
equality of the corresponding units modulo `MN_a`.  Their ratio is
`g^(t_1-t_2)`, whose order there is exactly `N_a`.  This proves (16).
**QED**

## Statement 2 -- exact one-hot/adjacent-two-hot correlation

For brevity put

\[
c_h=c_h^{(1)},
\qquad
\ell_h=\left[81^{-1}c_h\right]_M\in\{1,\ldots,M-1\},
\qquad
L_h=\left\lfloor{N_h-1\over145}\right\rfloor.
\tag{20}
\]

The simultaneous-event count modulo `N_h` is exactly

\[
\boxed{
I_h:=\#(E_h^{(1)}\cap E_h^{(2)})
=
\begin{cases}
0,&\ell_h>L_h,\\[3pt]
1+\left\lfloor{L_h-\ell_h\over M}\right\rfloor,
&\ell_h\le L_h.
\end{cases}
}
\tag{21}
\]

Equivalently,

\[
\boxed{
I_h
=\#\{\ell\in\mathbb Z:1\le\ell<N_h/145,
\ 81\ell\equiv c_h\pmod M\}.
}
\tag{22}
\]

In particular,

\[
\boxed{
0\le I_h\le\left\lceil{K_h\over145}\right\rceil,
\qquad
\#(E_h^{(1)}\cup E_h^{(2)})=2K_h-I_h.
}
\tag{23}
\]

The exact asymptotic correlation is

\[
\boxed{
{I_h\over K_h}\longrightarrow{1\over145},
\qquad
\mu(E_h^{(1)}\cap E_h^{(2)})
\sim{1\over145M}.
}
\tag{24}
\]

For every `h>=m+3`, the adjacent-two-hot event contains phases outside the
one-hot event and conversely.  At the boundary `h=m+2`, where `K_h=1`, the
two singleton events may coincide.

### Proof

Fix `t mod N_h` and let

\[
x=D_h^{(1)}(t),
\qquad
y=D_h^{(2)}(t).
\tag{25}
\]

Equation (8) gives

\[
81y\equiv145x\pmod {\mathfrak M_h}.
\tag{26}
\]

If both events occur, then `0<x,y<N_h`, so

\[
|81y-145x|<145N_h< MN_h=\mathfrak M_h,
\tag{27}
\]

where the strict middle inequality uses `M>=64^2=4096>145`.  The congruence
in (26) is therefore the ordinary equality

\[
81y=145x.
\tag{28}
\]

Since `gcd(81,145)=1`, there is a positive integer `ell` with

\[
x=81\ell,
\qquad
y=145\ell,
\qquad
145\ell<N_h.
\tag{29}
\]

Conversely, if (29) holds, then (26) and the canonical range force the stated
value of `y`, so both events occur.

As `t` runs modulo `N_h`, Statement 1 says that `x` visits each integer in
the fiber `c_h+M q`, `0<=q<N_h`, exactly once.  Thus (29) is possible exactly
for the integers in (22).  The unique admissible residue of `ell mod M` is
`ell_h`; counting it in `1,...,L_h` proves (21).  An interval of length less
than `N_h/145` contains at most `ceil(N_h/(145M))=ceil(K_h/145)` members of
one residue class modulo `M`, proving (23).  Formula (21) differs from
`K_h/145` by a bounded amount, which proves (24).

For `h>=m+3`, one has `K_h>=64`, and
`ceil(K_h/145)<K_h`.  The two events have equal size `K_h` but intersection
strictly smaller than either, proving the final assertion. **QED**

## Statement 3 -- the exact joint child tree

Put

\[
a_j=(j+1)(m+1),
\qquad
R=64^{m+1},
\qquad
S={R-1\over63},
\qquad
B_2=R-2S={61R+2\over63}.
\tag{30}
\]

The integer `B_2` is at least `3966`.  Define the formal set avoiding both
templates at every delay by

\[
\mathcal C_{m,v}^{\rm adj}
=\bigcap_{h\ge m+2}
\left((E_h^{(1)})^{\rm c}\cap(E_h^{(2)})^{\rm c}\right)
\subset\mathbb Z_2.
\tag{31}
\]

Every parent class modulo `N_(a_j)` has exactly `R` children modulo
`N_(a_(j+1))`.  The number of those children which survive all `2(m+1)`
events

\[
E_h^{(i)},
\qquad
a_j+1\le h\le a_{j+1},
\qquad
i=1,2,
\tag{32}
\]

satisfies the uniform exact bounds

\[
\boxed{
B_2\le
\#\{\text{jointly surviving children}\}
\le R-1.
}
\tag{33}
\]

Consequently, every class modulo

\[
N_{m+1}=64^m
\tag{34}
\]

contains an element of `C_(m,v)^adj`.  More quantitatively, if `Z_J(rho)` is
the number of descendants of a fixed root class `rho mod 64^m` which survive
the first `J` complete blocks, then

\[
\boxed{
B_2^J\le Z_J(\rho)\le(R-1)^J.
}
\tag{35}
\]

### Proof

Write `h=a_j+d`, `1<=d<=m+1`.  Then

\[
K_h=64^{a_j+d-m-2}\le64^{a_j-1}=N_{a_j}.
\tag{36}
\]

Fix a parent `t=rho mod N_(a_j)` and one of the two templates.  By (16), its
`Q_h^(i)` coordinates over that parent are

\[
q_{\rho,i}+N_{a_j}u,
\qquad
0\le u<{N_h\over N_{a_j}},
\tag{37}
\]

in some order.  Since the event interval `[0,K_h)` has length at most
`N_(a_j)`, it meets this parent in either no class modulo `N_h` or exactly
one such class.  One class modulo `N_h` contains

\[
{N_{a_{j+1}}\over N_h}=64^{m+1-d}
\tag{38}
\]

final children.  Therefore one template removes at most

\[
\sum_{d=1}^{m+1}64^{m+1-d}
=1+64+\cdots+64^m
=S
\tag{39}
\]

children during the block.  The union bound for the two templates removes at
most `2S`, proving the lower bound in (33).  No disjointness is assumed.

At the last delay `h=a_(j+1)`, equality holds in (36).  For each template the
event interval therefore removes exactly one child from every parent.
Their two forbidden children may coincide, but their union removes at least
one child.  This proves the upper bound in (33).  Iteration proves (35), and
finite branching with `B_2>=2` supplies an infinite jointly avoiding path in
every root class. **QED**

## Statement 4 -- a finite-template obstruction

The same argument is not special to Hamming weight two.  Let

\[
\mathscr F=\{F_1,\ldots,F_q\}
\tag{40}
\]

be a library of `q` distinct normalized binary templates satisfying

\[
F_j\subseteq\{0,1,\ldots,2m+1\},
\qquad
0\in F_j,
\qquad
1\le j\le q\le62.
\tag{41}
\]

At delay `h`, place the template beginning at position `n-h` and pad with
zeros to total length `n+m`.  Its reduced coefficient is the odd-unit
multiple

\[
U_F=\sum_{s\in F}\left({64\over81}\right)^s
\tag{42}
\]

of `D_h^(1)`.  The support restriction in (41) makes every template valid
from the first delay `h=m+2` onward.  Explicitly, put

\[
D_{h,F}(t)=[U_FD_h^{(1)}(t)]_{\mathfrak M_h},
\qquad
E_{h,F}:\quad D_{h,F}(t)<N_h.
\tag{43}
\]

Let `C_(m,v)(mathscr F)` be the formal phase set avoiding the lower
block-zero event `E_(h,F)` of every template in `mathscr F` at every delay.
Put

\[
B_q=R-qS=R-q{R-1\over63}.
\tag{44}
\]

Then every block parent has between `B_q` and `R-1` surviving children, and

\[
\boxed{
B_q\ge{R+62\over63}\ge66.
}
\tag{45}
\]

Thus no library of at most `62` fixed normalized hot-pattern templates can
cover every formal phase.  In particular, adding the adjacent two-hot
template to the one-hot template is the case `q=2` of this theorem.

### Proof

The coefficient (42) is odd because its `s=0` term is `1` and every other
term is divisible by `64` in `Z_2`.  The orbit, permutation, phase-retention,
and one-class-per-parent proofs of Statements 1 and 3 therefore apply to each
template without change.  Each template removes at most `S` children per
block, so `q` templates leave at least `B_q`.  Any one template removes one
child at the final delay, giving the upper bound.  The minimum of `B_q` over
`q<=62` is

\[
R-62{R-1\over63}={R+62\over63},
\tag{46}
\]

which is `66` at the smallest value `R=4096` and increases with `R`.
**QED**

## Statement 5 -- positive-dimensional joint avoidance

In the ordinary `2`-adic metric, `C_(m,v)^adj` is compact, perfect,
uncountable, nowhere dense, and Haar-null.  Its dimensions satisfy

\[
\boxed{
{\log B_2\over\log R}
\le
\dim_H\mathcal C_{m,v}^{\rm adj}
\le
\overline{\dim}_B\mathcal C_{m,v}^{\rm adj}
\le
{\log(R-1)\over\log R}
<1.
}
\tag{47}
\]

More generally, every library in Statement 4 has

\[
\boxed{
{\log B_q\over\log R}
\le
\dim_H\mathcal C_{m,v}(\mathscr F)
\le
\overline{\dim}_B\mathcal C_{m,v}(\mathscr F)
\le
{\log(R-1)\over\log R}.
}
\tag{48}
\]

Hence the adjacent two-hot family is a genuinely new obstruction at each
sufficiently large delay, but it still cannot uniformly cover the
positive-dimensional formal one-hot exceptional set of `R-9806`.

### Proof

Refinement through one block contracts a `2`-adic ball by `R^(-1)`.  Retain
arbitrarily exactly `B_q` surviving children at each node.  The uniform
measure on that regular ultrametric subtree assigns mass `B_q^(-J)` to a
level-`J` ball of diameter equal to a fixed factor times `R^(-J)`.  The
mass-distribution argument gives the lower bound in (48).

Conversely, the upper child bound covers the full avoiding set at level `J`
by at most a fixed initial factor times `(R-1)^J` balls of diameter a fixed
factor times `R^(-J)`.  The boundedly many intermediate binary scales give
the stated upper box bound.

Every node has at least `B_q>=2` descendants, so the set is perfect and
uncountable; it is closed and hence compact.  At least one child is removed
from every parent in every block, so its Haar measure is at most

\[
\lim_{J\to\infty}\left({R-1\over R}\right)^J=0.
\tag{49}
\]

A closed Haar-null subset of `Z_2` has empty interior and is nowhere dense.
Taking `q=2` proves (47). **QED**

## Ordinary finite-depth consequence

For an ordinary parameter, let `L_(1,2)(t)` count all valid lower competitors
from (6), with the necessary cutoff `m+2<=h<n(t)`.  Since this count includes
the one-hot count from `R-9806`, for every fixed `s>=1`,

\[
\boxed{
\#\{0\le t<T:n(t)>0,\ L_{1,2}(t)<s\}
=O_{m,v,s}\!\left(T^{d_m}(\log T)^{s-1}\right),
\qquad
d_m={\log(R-1)\over\log R}<1.
}
\tag{50}
\]

For `s=1`, this is `O_(m,v)(T^(d_m))`.  This ordinary upper bound is inherited
from the one-hot subfamily; (47) must not be read as a matching lower bound
for ordinary integers.

## Exact replay used during the audit

The proof is symbolic.  A bounded replay of the first block at `m=1` checked
both possible one-bit suffixes.  It enumerated only the `64^3` formal phase
residues at the end of that block.

| suffix `v` | `n_0 mod 256` | `I_3` | `I_4` | minimum surviving children | maximum surviving children |
|---|---:|---:|---:|---:|---:|
| `0` | 109 | 0 | 0 | 4030 | 4094 |
| `1` | 1 | 1 | 1 | 4032 | 4094 |

At these two delays, `K_3=1` and `K_4=64`.  Direct enumeration and formula
(21) agreed in all four cases.  The uniform theorem gives

\[
B_2={61\cdot4096+2\over63}=3966,
\tag{51}
\]

so both observed child ranges satisfy (33).  The replay is an audit only and
does not enter any proof.

## What this advances

- `R-9806` left open whether the first multi-hot family kills its formal
  one-hot exceptional set.  It does not: the adjacent two-hot family leaves
  a positive-dimensional subset in every root phase.
- The adjacent event is not a relabeled one-hot event.  Formula (21) gives
  its exact overlap, and from the second delay onward it contributes genuinely
  new forbidden phases.
- The finite-template theorem identifies a structural threshold.  A bounded
  attack using at most `62` fixed normalized patterns cannot prove an
  all-formal-phase promotion obstruction.  Any such covering argument must
  exploit a larger or delay-growing pattern library, or use arithmetic beyond
  template-by-template child exclusion.
- Equation (50) preserves the power-saving ordinary necessary-condition
  count while keeping it logically separate from the formal Cantor result.

## Source-direction and dependency audit

- `L-9826` supplies finite-cylinder injectivity and the exact representative
  sum used in (10).
- `L-9883` supplies the exposed candidate `A_*=64^(n-1)` and the fact that a
  lower block-zero point prevents global promotion.
- `L-9885` identifies an unchanged terminal block with an exact zero-renewal
  block.
- `L-9896` supplies the suffix-exposure progression and one-hot lift
  coordinate.  The odd-unit template permutation and the adjacent
  correlation calculation are new here.
- `R-9806` supplies the one-hot exceptional-set question and its ordinary
  power-saving estimate.  The joint child bound is reconstructed for the
  enlarged event family rather than inferred from a measure heuristic.
- The audited PR-16 head
  `1bb8c6b9fa7df170a59b6f6658d0150c16628f13` was compared path-by-path with
  the previously audited head
  `f800597d0facc26d99ac98f783e0765e7583b0c0`.  Its `D-9302`, `L-9313`,
  `L-9314`, `CENTERED_POWER.md`, and `ORDINARY_SECTION.md` source paths are
  unchanged.  The newer PR-16 commits concern the recurrence/Thue--Morse
  lane and are not imported into this proof.
- No independence assumption, numerical equidistribution, infinite ordinary
  survivor, or empirical minimum table is used.

## Gap audit

- The theorem treats the adjacent two-hot family and, more generally, at most
  `62` fixed templates of bounded support.  It does **not** prove that the
  union of all two-hot gaps leaves any formal phase.  The number of available
  gaps grows with `h`, and that unbounded family lies outside (41).
- Positive Hausdorff dimension in `Z_2` does not imply that the avoiding set
  contains an ordinary nonnegative integer.  It may have empty ordinary
  intersection.
- Conversely, an ordinary depth only realizes delays `h<n(t)`.  It need not
  satisfy the all-delay formal intersection (31).  Formula (50) respects this
  finite-depth cutoff.
- The child bounds are not claimed sharp.  Same-delay overlap is exact in
  (21), but cross-delay overlaps can increase the number of survivors beyond
  the union-bound floor.
- Absence of one-hot and adjacent-two-hot competitors does not prove global
  promotion.  Wider-gap two-hot, higher-weight, and arbitrary block-zero
  competitors remain.
- No nontrivial ordinary survivor or Collatz counterexample is constructed or
  excluded.

## Adversarial checks

- The adjacent coefficient is `17*145*81^(h-2-n)`.  Omitting the original
  factor `17`, or replacing the modular odd unit `145/81` by a real-size
  approximation, gives the wrong event.
- The strict inequality in (27) is justified uniformly by
  `M>=4096>145`; it is what promotes a modular relation to the ordinary
  equality (28).
- Each event has size `K_h`, not one residue globally.  It becomes at most one
  class only after conditioning on a parent whose modulus is at least the
  event interval length.
- The lower child bound uses a union bound over both templates and all
  `m+1` delays.  It never assumes that the forbidden child classes are
  disjoint.
- At the final delay each template removes one child from every parent, but
  those children may coincide.  This is why the uniform upper bound is
  `R-1`, not `R-2`.
- Supports in (41) stop at `2m+1` precisely so every normalized template fits
  at the first delay `h=m+2`.  Delay-growing supports are not silently folded
  into the finite-template theorem.
- Dimensions use the ordinary `2`-adic metric.  A block multiplies the modulus
  by `R=2^(6m+6)`, so it contracts diameter by exactly `R^(-1)`.

## Suggested next attack

For the full two-hot family, index the second-hot gap by

\[
1\le s\le m+h-1
\tag{52}
\]

and compute the forbidden-child map induced by

\[
U_s=1+\left({64\over81}\right)^s.
\tag{53}
\]

The present theorem shows that no bounded initial library can finish the
covering.  The next decisive question is whether the new child labels created
as `s` grows eventually exhaust every survivor of the joint tree, or whether
their high-valuation congruences force persistent collisions and leave a
nonempty inverse-limit subtree.
