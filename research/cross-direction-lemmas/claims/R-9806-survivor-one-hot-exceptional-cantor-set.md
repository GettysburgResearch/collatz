# R-9806 -- Delayed one-hot avoidance leaves a positive-dimensional exceptional Cantor set

Claim ID: `R-9806`
Title: Delayed one-hot obstructions are quantitatively generic but leave a positive-dimensional formal exceptional set
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave12-centered-section`
Reviewing agents: `gpt56-synthesis-01-wave12-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `L-9826`, `L-9883`, `L-9885`, `L-9896`
Scope: the delayed one-hot obstruction events inside one fixed suffix-exposure progression for the `64 -> 81` survivor chart
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

Retain the notation of `L-9896`.  Thus the one-hot cylinder `w_n v`, with
`w_n=0^(n-1)1`, is exposed precisely on one progression

\[
n=n_0+O_0t,
\qquad
O_0=\operatorname {ord}_{64^{m+1}}(81)=2^{6m+2},
\qquad t\in\mathbb Z.
\tag{2}
\]

Put

\[
M=64^{m+1}.
\tag{3}
\]

For `h>=1`, define

\[
N_h=64^{h-1},
\qquad
D_h(t)=\left[17\,81^{-(n-h+1)}\right]_{MN_h}.
\tag{4}
\]

For an ordinary integer `t`, this is literal exponentiation with
`n=n_0+O_0t`.  On the formal completion `t in Z_2`, it means the unique
continuous finite-level extension

\[
D_h(t)
=\left[17\,81^{h-1-n_0}
       \left(81^{-O_0}\right)^t\right]_{MN_h};
\tag{4a}
\]

the last power depends only on `t mod N_h`.

The reduction of `D_h(t)` modulo `M` is independent of `t`; call it `c_h`.
There is therefore a coordinate

\[
D_h(t)=c_h+M Q_h(t),
\qquad
0\le Q_h(t)<N_h.
\tag{5}
\]

`L-9896` proves that `Q_h` is a permutation of `Z/N_h Z`.  For
`h>=m+2`, put

\[
K_h=64^{h-m-2},
\qquad
E_h=\{t:Q_h(t)<K_h\}.
\tag{6}
\]

When `t` is ordinary and `h<n(t)`, membership in `E_h` gives the distinct
lower delayed one-hot zero-block competitor

\[
0^{n-h}1\,0^{m+h-1}
\tag{7}
\]

to the exposed representative `64^(n-1)`.  Every `E_h` has relative density

\[
\frac{K_h}{N_h}=64^{-(m+1)}.
\tag{8}
\]

Define the **formal all-delay avoiding set** in the completed exposure phase by

\[
\mathcal C_{m,v}
=\bigcap_{h\ge m+2}E_h^{\mathrm c}
\subset\mathbb Z_2.
\tag{9}
\]

The word *formal* is load-bearing: an ordinary depth `n(t)` only realizes the
delayed word (7) for `h<n(t)`, whereas (9) imposes every algebraic event,
including delays beyond that finite depth.

Finally set

\[
R=64^{m+1},
\qquad
B=R-\frac{R-1}{63}=\frac{62R+1}{63}.
\tag{10}
\]

Both numbers are integers because `R=1 mod 63`.

## Statement 1 -- exact phase-retention law

For every `1<=a<=h`, reduction of the high coordinate retains precisely the
lower `t`-phase:

\[
\boxed{
Q_h(t_1)\equiv Q_h(t_2)\pmod {N_a}
\quad\Longleftrightarrow\quad
t_1\equiv t_2\pmod {N_a}.
}
\tag{11}
\]

Consequently, fix one parent class `t=rho mod N_a`.  As its
`N_h/N_a` children modulo `N_h` vary, their `Q_h` coordinates are exactly

\[
q_\rho+N_a j,
\qquad
0\le j<N_h/N_a,
\tag{12}
\]

in some order, for one `0<=q_rho<N_a`.

### Proof

Odd-base LTE gives

\[
v_2(81^{O_0}-1)=6m+6.
\tag{13}
\]

Hence `g=81^(-O_0)` has exact order `N_h` modulo `MN_h`, and exact
order `N_a` modulo `MN_a`.  Incrementing `t` multiplies `D_h(t)` by `g`.
Thus, modulo `MN_a`, the orbit is the complete reduction fiber over `c_h`
and is indexed bijectively by `t mod N_a`.  Dividing that fiber by `M`
proves (11).  Globally `Q_h` is a permutation modulo `N_h`; restricting it
to one parent fiber and using (11) gives (12). **QED**

## Statement 2 -- exact block child bounds

For `j>=0`, put

\[
a_j=(j+1)(m+1).
\tag{14}
\]

The `j`th delay block is

\[
a_j+1\le h\le a_{j+1}.
\tag{15}
\]

It contains exactly `m+1` events, and refinement from modulus `N_(a_j)` to
modulus `N_(a_(j+1))` gives exactly `R` children per parent.

Inside **every** parent class modulo `N_(a_j)`, the number of children which
avoid every event in (15) lies between

\[
\boxed{B\le \#\{\text{surviving children}\}\le R-1.}
\tag{16}
\]

In particular, every class modulo

\[
N_{m+1}=64^m
\tag{17}
\]

has an infinite descendant in `C_(m,v)`.

### Proof

Write `h=a_j+d`, where `1<=d<=m+1`.  Then

\[
K_h
=64^{a_j+d-m-2}
=N_{a_j}\,64^{d-m-1}
\le N_{a_j}.
\tag{18}
\]

Fix one parent `rho mod N_(a_j)`.  By (12), all children have the same
`Q_h` residue `q_rho mod N_(a_j)`.  Because the event interval
`0<=Q_h<K_h` lies inside one complete residue interval modulo `N_(a_j)`,
the event `E_h` meets this parent in either

- no class modulo `N_h`, when `q_rho>=K_h`; or
- exactly one class modulo `N_h`, when `q_rho<K_h`.

One class modulo `N_h` contains exactly

\[
\frac{N_{a_{j+1}}}{N_h}
=64^{m+1-d}
\tag{19}
\]

children at the end of the block.  The union bound over the `m+1` delays
therefore removes at most

\[
\sum_{d=1}^{m+1}64^{m+1-d}
=1+64+\cdots+64^m
=\frac{R-1}{63}
\tag{20}
\]

of the `R` final children.  This proves the lower bound `B`.

For the last delay `d=m+1`, (18) is equality: `K_h=N_(a_j)`.  Every
`q_rho` lies below this threshold, so this last event removes exactly one
final child from every parent.  At most `R-1` children survive, proving the
upper bound.

Starting from any class modulo (17), repeatedly choose a surviving child.
The finite-branching tree has at least `B>=2` children at every node, so
compactness (equivalently, Koenig's lemma) supplies an infinite descendant in
the intersection (9). **QED**

## Statement 3 -- the formal exceptional set is a thick null Cantor set

Use the standard metric

\[
d_2(x,y)=2^{-v_2(x-y)}.
\tag{21}
\]

Then `C_(m,v)` is compact, perfect, uncountable, nowhere dense, and has
normalized Haar measure zero.  Its Hausdorff dimension satisfies the explicit
sandwich

\[
\boxed{
\frac{\log B}{\log R}
\le
\dim_H\mathcal C_{m,v}
\le
\overline{\dim}_{B}\mathcal C_{m,v}
\le
\frac{\log(R-1)}{\log R}
<1.
}
\tag{22}
\]

Thus delayed one-hot events cover Haar-almost every formal phase, but they do
**not** cover every formal phase.  In fact their full avoiding set has positive
Hausdorff dimension in every root class modulo `64^m`.

### Proof

A class modulo `N_(a_j)=64^(a_j-1)` is a `2`-adic ball of diameter
`N_(a_j)^(-1)`.  Passing from `a_j` to `a_(j+1)` contracts diameter by
exactly

\[
\frac{N_{a_j}}{N_{a_{j+1}}}=R^{-1}.
\tag{23}
\]

By Statement 2, the block tree has between `B` and `R-1` children at every
node.  Retain arbitrarily exactly `B` children at each node.  The resulting
regular ultrametric subtree carries the uniform measure for which every
level-`j` ball has mass `B^(-j)` and diameter equal to a fixed initial factor
times `R^(-j)`.  The mass-distribution argument gives dimension
`log B/log R` for this subtree and hence the lower bound in (22).

Conversely, at level `j` the whole avoiding set is covered by at most a fixed
initial factor times `(R-1)^j` balls of diameter a fixed factor times
`R^(-j)`.  The same estimate at the boundedly many intermediate binary scales
gives the upper box bound in (22).

The fraction of all children surviving through `j` blocks is at most

\[
\left(\frac{R-1}{R}\right)^j\longrightarrow0,
\tag{24}
\]

so Haar measure is zero.  The set is closed as an intersection of clopen
sets.  Every surviving node has at least `B>=2` infinite descendants, so no
point is isolated; compactness and perfection imply uncountability.  A closed
Haar-null subset of `Z_2` has empty interior, proving nowhere density.
**QED**

## Statement 4 -- exact binomial residue counts on spaced delays

Take the spaced delays

\[
h_j=m+2+(j-1)(m+1),
\qquad j\ge1.
\tag{25}
\]

Then

\[
N_{h_j}=R^j,
\qquad
K_{h_j}=R^{j-1}.
\tag{26}
\]

Inside every parent class modulo `R^(j-1)`, the event `E_(h_j)` is exactly
one of its `R` children modulo `R^j`.  Therefore, for `0<=k<=J`, the exact
number of residues `t mod R^J` belonging to exactly `k` of the first `J`
events is

\[
\boxed{
\binom{J}{k}(R-1)^{J-k}.
}
\tag{27}
\]

In particular, the number belonging to fewer than `s` of them is

\[
\boxed{
A_{J,s}
=\sum_{k=0}^{\min(s-1,J)}
\binom{J}{k}(R-1)^{J-k}.
}
\tag{28}
\]

### Proof

For `j=1`, (26) and the permutation law say that one of the `R` residues is
the event.  For `j>1`, apply (12) with `a=h_(j-1)` and `h=h_j`.  Since
`K_(h_j)=N_(h_(j-1))`, exactly one of the `R` children of each parent is in
the event.  A path of length `J` with a prescribed set of `k` event levels
has one choice at those levels and `R-1` choices at the other levels.  Sum
over the `binomial(J,k)` choices of event levels to obtain (27)--(28).
**QED**

## Statement 5 -- a power-saving bound for ordinary exceptional depths

For an ordinary nonnegative parameter `t`, let `L(t)` be the number of
distinct lower delayed one-hot competitors certified by events

\[
m+2\le h<n(t).
\tag{29}
\]

For every fixed `s>=1`, define

\[
\mathcal A_s(T)
=\{0\le t<T:n(t)>0,\ L(t)<s\}.
\tag{30}
\]

Put

\[
d_m=\frac{\log(R-1)}{\log R}
=1+\frac{\log(1-R^{-1})}{\log R}
<1.
\tag{31}
\]

Then, with constants depending only on the fixed suffix exposure data,

\[
\boxed{
#\mathcal A_s(T)
=O_{m,v,s}\!\left(T^{d_m}(\log T)^{s-1}\right).
}
\tag{32}
\]

For `s=1`, no logarithmic loss occurs:

\[
\boxed{
#\mathcal A_1(T)=O_{m,v}(T^{d_m}).
}
\tag{33}
\]

Consequently, among exposed depths `n<=X`, the number at which the one-hot
representative `64^(n-1)` can possibly be the global nontrivial minimum is

\[
\boxed{O_{m,v}(X^{d_m}).}
\tag{34}
\]

This is a necessary-condition count only.  Avoiding delayed one-hot
competitors does not prove global promotion, because arbitrary multi-hot and
other block-zero competitors remain.

### Proof

Let

\[
J=\lfloor\log_R T\rfloor
\tag{35}
\]

and assume `T` is large enough that `J>=s`.  Since `h_J=O_m(J)` whereas
`n(t)=n_0+O_0t`, only `O_(m,v)(J)` parameters satisfy `n(t)<=h_J`.
For every other parameter, all first `J` spaced events are actual delayed
words.  Thus `L(t)<s` forces the residue of `t mod R^J` to be one of the
`A_(J,s)` classes in (28).

Because

\[
R^J\le T<R^{J+1},
\tag{36}
\]

each residue modulo `R^J` occurs at most `R+1` times in `[0,T)`.  Also,

\[
A_{J,s}
\le sJ^{s-1}(R-1)^J
\le sJ^{s-1}T^{d_m}.
\tag{37}
\]

Equations (35)--(37), together with the `O(J)` finite-depth cutoff, prove
(32)--(33).  Distinct event delays give distinct binary words and hence
distinct representatives by finite-cylinder injectivity in `L-9826`.

Finally, `L-9883` and `L-9896` show that any one valid event supplies a lower
block-zero representative.  Global promotion therefore implies `L(t)=0`.
There is one exposing depth per parameter `t`, and `t=O(X/O_0)` for `n<=X`,
so (33) gives (34). **QED**

## Exact replay used during the audit

The proof is not computational.  The following bounded integer replay checked
the first child block at `m=1`, `v=0`:

```python
m = 1
M = 64 ** (m + 1)
O0 = 2 ** (6 * m + 2)
target = pow(17, -1, M)
n0 = next(n for n in range(O0) if pow(81, -n, M) == target)

events = {}
for h in (3, 4):
    modulus = 64 ** (m + h)
    Nh, Kh = 64 ** (h - 1), 64 ** (h - m - 2)
    c = (17 * pow(81, h - 1, M) * target) % M
    g = pow(81, -O0, modulus)
    D = (17 * pow(81, h - 1 - n0, modulus)) % modulus
    events[h] = []
    for t in range(Nh):
        assert D % M == c
        events[h].append((D - c) // M < Kh)
        D = D * g % modulus
    assert sum(events[h]) == Kh

from collections import Counter
Nparent, Nfinal = 64 ** m, 64 ** (2 * m + 1)
counts = Counter()
for t in range(Nfinal):
    if not events[3][t % 64**2] and not events[4][t % 64**3]:
        counts[t % Nparent] += 1
print(n0, min(counts.values()), max(counts.values()))
assert min(counts.values()) >= 64**2 - (64**2 - 1) // 63
```

It gives

```text
n0 = 109 mod 256
E_3: 1 residue mod 4096
E_4: 64 residues mod 262144
surviving children per class mod 64: minimum 4032, maximum 4095
theorem lower bound B: 4031
```

Thus the exact event sizes and the worst-case union bound pass the first
nontrivial boundary case.  The replay does not enter any proof.

## What this advances and refutes

- `L-9896` proved relative natural density one for delayed one-hot
  obstruction and left open whether the avoiding set was empty, finite, or a
  zero-dimensional Cantor set.  Statements 2--3 prove that the **formal**
  avoiding set is a positive-dimensional Cantor set.  The empty, finite, and
  zero-dimensional formal alternatives are refuted.
- Statement 5 upgrades qualitative density-one rank divergence to an explicit
  power-saving exceptional count, with the exact exponent dictated by the
  one-forbidden-child tree.
- Delayed one-hot words alone cannot give an all-phase formal covering proof.
  Any uniform promotion obstruction must use additional multi-hot words or an
  arithmetic theorem separating ordinary parameters from the formal Cantor
  set.

## Source-direction and dependency audit

- `L-9896/(4)--(15)` supplies the exposure parameter, lift coordinate,
  permutation law, and exact event threshold.  Statement 1 reconstructs the
  reduction compatibility needed here directly from LTE and the cyclic
  kernel, rather than assuming independence at short range.
- `L-9826` supplies finite-cylinder injectivity, used only to count event
  witnesses as distinct lower competitors.
- `L-9883` supplies the exposed one-hot representative and the fact that one
  lower block-zero point prevents global promotion.
- `L-9885` identifies the terminal zero block with an exact centered renewal
  plateau.  This is interpretation, not an additional counting assumption.
- The current PR-16 head
  `f800597d0facc26d99ac98f783e0765e7583b0c0` was audited through
  `CENTERED_POWER.md`, `ORDINARY_SECTION.md`, and `T-9315`.  It supplies the
  ordinary-section/centered-rational-power context, but no theorem from that
  branch is needed in the proof above.
- The current PR-19 head
  `e8e2d0a4892c451144d5135cc79bc5aa42515e45` was audited through
  `SURVIVOR_THEORY.md`, `STRUCTURAL_RESULTS.md`, and `ITERATION_05.md`.  Its
  ghost-minimum stabilization problem is analogous but arithmetically
  different; no H-frontier identity is imported here.
- No external theorem, asymptotic equidistribution result, experiment, or
  infinite ordinary-survivor hypothesis is used.

## Gap audit

- Positive Hausdorff dimension in `Z_2` does not imply that
  `C_(m,v)` contains even one ordinary nonnegative integer.  The intersection
  `C_(m,v) intersection Z_(>=0)` may be empty, finite, or infinite.
- Conversely, an ordinary finite depth need avoid events only for `h<n(t)`.
  It need not belong to the formal all-delay set (9).  Statement 5 handles
  this cutoff explicitly; it does not identify the individual exceptions.
- The lower and upper dimension bounds need not coincide.  Determining the
  exact dimension requires the short-range correlations among the `m+1`
  events within a block.
- A lower delayed one-hot point defeats one-hot global promotion, but absence
  of all such points does not prove promotion.  Multi-hot and arbitrary
  block-zero competitors are outside this claim.
- Neither a nontrivial ordinary survivor nor a Collatz counterexample is
  constructed or excluded.

## Adversarial checks

- The block starts at `a_0=m+1`, so its first event is exactly `h=m+2`; no
  small-delay event is silently omitted.
- The threshold comparison in (18) is valid only for the next `m+1` delays.
  This is why the block length is exactly `m+1`.
- The lower child count uses a union bound.  Overlap can improve it (as in the
  replay), but no disjointness is assumed.
- The final event of each block removes exactly one child, which supplies the
  strict upper dimension bound and Haar nullity without extrapolating from a
  finite computation.
- The binomial formula counts algebraic phase events.  The cutoff
  `n(t)>h_J` is imposed before interpreting them as actual delayed words.
- Dimensions in (22) use the ordinary `2`-adic metric.  A modulus increase by
  `R=2^(6m+6)` contracts diameter by `R^(-1)`, so no missing factor of six
  occurs in the logarithmic ratio.

## Suggested next attack

Compute the exact finite transition matrices for the `m+1` short-range event
types symbolically (not by enumerating the full modulus).  Their joint spectral
radius should determine the exact Hausdorff dimension of `C_(m,v)`.  Then add
two-hot block-zero events to ask whether the combined exceptional tree retains
positive branching or becomes arithmetically empty on ordinary parameters.
