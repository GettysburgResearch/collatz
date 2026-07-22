# L-9834 -- Ternary full shift of survivor-cylinder differences

Claim ID: `L-9834`  
Title: The survivor-cylinder difference set is an exact ternary full shift with additive energy `6^n`  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `R-9804`; `L-9815` only for the cyclic-successor interpretation  
Scope: exact finite additive geometry and 2-adic difference coding of survivor cylinders  
Related counterexample candidates: none

## Definitions

Let

\[
G_n=\mathbb Z/64^n\mathbb Z.
\tag{1}
\]

For a directive word

\[
\varepsilon=(\varepsilon_0,\ldots,\varepsilon_{n-1})
\in\{0,1\}^n,
\tag{2}
\]

write its depth-`n` survivor-cylinder representative as

\[
\alpha_n(\varepsilon)
=
\left[
17\sum_{j=0}^{n-1}
\varepsilon_j64^j81^{-(j+1)}
\right]_{64^n}.
\tag{3}
\]

The exact inverse-cylinder bijection in `R-9804` says that

\[
S_n={\alpha_n(\varepsilon):\varepsilon\in\{0,1\}^n\}
\subseteq G_n
\tag{4}
\]

has `2^n` elements and is exactly the set of depth-`n` survivor classes.

Put

\[
\mathcal A={-1,0,1\}.
\tag{5}
\]

For a signed word `eta in A^n`, define its signed cylinder

\[
\boxed{
\kappa_n(\eta)
=
17\sum_{j=0}^{n-1}
\eta_j64^j81^{-(j+1)}
\quad\text{in }G_n.
}
\tag{6}
\]

Let

\[
z(\eta)=\#\{0\le j<n:\eta_j=0\}.
\tag{7}
\]

For `x in G_n`, define the ordered difference-representation function

\[
r_n(x)=\#\{(a,b)\in S_n^2:b-a=x\},
\tag{8}
\]

and the truncated base-64 valuation

\[
\overline\nu_{64,n}(x)
=\max\{0\le r\le n:x\equiv0\pmod {64^r}\}.
\tag{9}
\]

Thus the zero class has truncated valuation `n`.

## Statement

### 1. Exact signed-cylinder coding

For every two directive words `epsilon,nu in {0,1}^n`, put

\[
\eta_j=\nu_j-\varepsilon_j.
\tag{10}
\]

Then

\[
\boxed{
\alpha_n(\nu)-\alpha_n(\varepsilon)
=\kappa_n(\eta)
\quad\text{in }G_n.
}
\tag{11}
\]

Conversely, every signed word `eta in A^n` occurs in this way. At a coordinate
with `eta_j=1` the binary pair is forced to `(epsilon_j,nu_j)=(0,1)`; at a
coordinate with `eta_j=-1` it is forced to `(1,0)`; and at a zero coordinate
it can be either `(0,0)` or `(1,1)`.

The coding

\[
\boxed{
\kappa_n:\mathcal A^n\longrightarrow G_n
}
\tag{12}
\]

is injective. Hence

\[
\boxed{
S_n-S_n
=\{b-a:a,b\in S_n\}
=\kappa_n(\mathcal A^n),
\qquad
|S_n-S_n|=3^n.
}
\tag{13}
\]

This is an exact difference-set count, not only an upper bound obtained from
the `4^n` ordered pairs.

### 2. The signed chart is the left shift

For `eta in A^n`, its signed cylinder has first residue

\[
\boxed{
\kappa_n(\eta)\equiv\eta_0\pmod {64},
}
\tag{14}
\]

where `-1` is represented by residue `63`. On the three legal residues define

\[
\mathfrak D(x)=\frac{81x-17\eta(x)}{64},
\qquad
\eta(x)\in\{-1,0,1\},
\qquad
x\equiv\eta(x)\pmod {64}.
\tag{15}
\]

Then the exact shift identity is

\[
\boxed{
\mathfrak D(\kappa_n(\eta_0,\ldots,\eta_{n-1}))
\equiv
\kappa_{n-1}(\eta_1,\ldots,\eta_{n-1})
\pmod {64^{n-1}}.
}
\tag{16}
\]

More concretely, choose binary words realizing `eta`, choose ordinary lifts
`A<B` of their cylinder classes, and let `d=B-A` be the positive cyclic gap.
The two starts survive `n` steps, and their positive orbit difference obeys

\[
\boxed{
\Delta_j=\mathfrak D^j(d),
\qquad
\nu_j-\varepsilon_j=\eta_j
\quad(0\le j<n).
}
\tag{17}
\]

For the all-zero signed word, the zero class is realized by taking two copies
of the same cylinder one period apart, so `d=64^n`; its first `n` signed
digits are indeed zero.

### 3. Exact representation multiplicity and additive energy

Every difference class has a unique signed word, and its representation
multiplicity is

\[
\boxed{
r_n(\kappa_n(\eta))=2^{z(\eta)}.
}
\tag{18}

\]

Consequently the additive energy is exactly

\[
\boxed{
\begin{aligned}
E(S_n)
&:=\#\{(a,b,c,d)\in S_n^4:b-a=d-c\}\\
&=\sum_{x\in G_n}r_n(x)^2
=\sum_{\eta\in\mathcal A^n}4^{z(\eta)}
=6^n.
\end{aligned}
}
\tag{19}
\]

The identity

\[
\sum_{x\in G_n}r_n(x)=4^n
\tag{20}
\]

is recovered coordinatewise from `2+1+1=4`, while the energy uses
`4+1+1=6`.

### 4. Exact valuation distribution

For a nonzero difference class, its truncated base-64 valuation is the first
nonzero signed position:

\[
\boxed{
\overline\nu_{64,n}(\kappa_n(\eta))
=\min\{j:\eta_j\ne0\}.
}
\tag{21}
\]

Hence, for every `0<=k<n`,

\[
\boxed{
\#\{x\in S_n-S_n:
\overline\nu_{64,n}(x)=k\}
=2\,3^{n-k-1}.
}
\tag{22}

\]

The sole class of valuation `n` is zero. Representation-weighting gives the
companion ordered-pair laws, valid for `0<=r<=n`,

\[
\boxed{
\#\{(a,b)\in S_n^2:
b-a\equiv0\pmod {64^r}\}
=2^{2n-r},
}
\tag{23}

\]

and, for `0<=r<n`,

\[
\boxed{
\#\{(a,b)\in S_n^2:
\overline\nu_{64,n}(b-a)=r\}
=2^{2n-r-1}.
}
\tag{24}

\]

Thus a uniformly chosen ordered survivor-cylinder pair has aligned directive
prefix of length at least `r` with exact probability `2^{-r}`. This is an
exact global pair count; it is not a statement about the specially selected
successor pair.

### 5. Infinite ternary difference Cantor set

Let the infinite survivor completion set be

\[
\mathscr S_\infty
=\left\{
17\sum_{j\ge0}\varepsilon_j64^j81^{-(j+1)}:
\varepsilon_j\in\{0,1\}
\right\}
\subset\mathbb Z_2.
\tag{25}
\]

Then

\[
\boxed{
\mathscr S_\infty-\mathscr S_\infty
=\left\{
\kappa(\eta)
:=17\sum_{j\ge0}\eta_j64^j81^{-(j+1)}:
\eta_j\in\mathcal A
\right\}.
}
\tag{26}
\]

The map `kappa` is a homeomorphism from the one-sided ternary full shift onto
this difference set, and the signed chart is conjugate to the left shift:

\[
\boxed{
\mathfrak D(\kappa(\eta_0,\eta_1,\ldots))
=\kappa(\eta_1,\eta_2,\ldots).
}
\tag{27}

\]

If two signed sequences first differ at position `k`, then

\[
\boxed{
\nu_2(\kappa(\eta)-\kappa(\theta))
=6k+\nu_2(\eta_k-\theta_k)
\in\{6k,6k+1\}.
}
\tag{28}

\]

Therefore the difference set has

\[
\boxed{
\dim_H(\mathscr S_\infty-\mathscr S_\infty)
=\frac{\log 3}{\log64}
=\log_{64}3,
}
\tag{29}

\]

and Haar measure zero in `Z_2`.

### 6. Cyclic successor consequences

Order the canonical representatives as

\[
0\le s_0<s_1<\cdots<s_{2^n-1}<64^n,
\qquad
s_{2^n}=s_0+64^n,
\tag{30}
\]

and put `g_i=s_(i+1)-s_i`. These are precisely the cyclic successor gaps from
`L-9815` when the starting class already survives depth `n`. They satisfy

\[
\boxed{
\sum_{i=0}^{2^n-1}g_i=64^n,
\qquad
\frac1{2^n}\sum_i g_i=32^n,
\qquad
\max_i g_i\ge32^n.
}
\tag{31}

\]

Every `g_i` is the positive representative of `kappa_n(eta)` for a unique
nonzero signed word. If a signed word has `z` zero positions, then at most
`2^z` cyclic successor edges can have that gap, because (18) counts every
ordered survivor pair with that difference, adjacent or not.

For a particular successor pair whose ordinary addition carry settles at
`u<=n`, `L-9830` identifies its settled inverse-cylinder carry as

\[
\boxed{
C_u(B)-C_u(A)=\mathfrak D^u(g_i).
}
\tag{32}

\]

The finite shift conjugacy also gives the explicit carry cylinder

\[
\boxed{
C_u(B)-C_u(A)
\equiv
\kappa_{n-u}(\eta_u,\ldots,\eta_{n-1})
\pmod {64^{n-u}}.
}
\]

Its common directive block after settlement is therefore exactly the initial
zero run of the shifted signed word `(eta_u,eta_(u+1),...)`. Thus the
pair-specific valuation statistic in `L-9830` is the ordinary cylinder
valuation (21) applied after `u` signed shifts.

## Proof

### Signed cylinders and injectivity

Subtracting (3) for `epsilon` and `nu` proves (11). The coordinatewise binary
choices stated after (11) realize every signed word.

Suppose `eta!=theta`, and let `k` be their first differing position. Factoring
their signed-cylinder difference gives

\[
\kappa_n(\eta)-\kappa_n(\theta)
=17\,64^k81^{-(k+1)}
\left((\eta_k-\theta_k)+64Z\right)
\tag{33}
\]

for some integer class `Z`. The leading difference belongs to
`{-2,-1,1,2}` and is not divisible by `64`. Hence (33) is nonzero modulo
`64^n`, proving injectivity and (13). It also proves the sharper valuation
formula (28) on passage to infinite 2-adic series.

Because (81\equiv17\pmod {64}), the coefficient
(17\cdot81^{-1}) is one modulo (64); this proves (14). Direct calculation gives

\[
\frac{81\kappa_n(\eta)-17\eta_0}{64}
=17\sum_{j=1}^{n-1}
\eta_j64^{j-1}81^{-j},
\tag{34}
\]

which is (16). For ordinary lifts of two legal survivor cylinders, the chart
is strictly increasing and subtraction of their recurrences gives exactly
(17). Taking one representative one full period higher realizes the zero
signed word as a positive pair.

### Multiplicity, energy, and valuations

Injectivity says that a fixed difference class has one signed word. At each
nonzero signed coordinate its binary pair is forced, while every zero signed
coordinate has two choices. This proves (18). Squaring and summing factors
independently over the coordinates:

\[
\sum_{\eta\in\mathcal A^n}4^{z(\eta)}
=(4+1+1)^n=6^n,
\tag{35}
\]

which proves (19). The same calculation without squaring gives (20).

If the first nonzero signed coordinate is `k`, formula (6) factors as a unit
times `64^k`; all later terms contain an additional factor `64`. This proves
(21). There are two choices at the first nonzero coordinate and three at each
later coordinate, proving (22).

For a pair difference to vanish modulo `64^r`, its first `r` signed digits
must be zero. Each such coordinate has two common binary choices, while every
later coordinate has four arbitrary binary-pair choices. Therefore the count
is

\[
2^r4^{n-r}=2^{2n-r},
\tag{36}
\]

proving (23). Subtracting the count at `r+1` proves (24).

### Infinite geometry and successors

The series in (25)--(26) converge in `Z_2`. Coordinatewise subtraction proves
one inclusion in (26), and the same binary choices used after (11) prove the
reverse inclusion. Formula (28) makes `kappa` injective and bi-Lipschitz, up
to a factor of two, from the symbolic metric in which first difference at
`k` has distance `64^(-k)`. Compactness then makes it a homeomorphism.
Passing (34) to the limit proves (27).

The ternary symbolic metric has Hausdorff dimension `log(3)/log(64)`, and a
bi-Lipschitz map preserves dimension. Alternatively, at depth `n` there are
exactly `3^n` occupied balls of radius `64^(-n)`. Their total Haar measure is

\[
3^n64^{-n}=(3/64)^n\longrightarrow0,
\tag{37}
\]

which also proves Haar nullity.

Finally, the cyclic gaps telescope around `G_n`, proving (31). Every edge is
an ordered survivor pair, so (13), (18), and the signed-chart shift apply.
Equation (32) is the settled-carry identity of `L-9830`. This completes the
proof. QED

## Motivation

`L-9830` turns one successor carry difference into a signed-chart orbit. The
present lemma identifies the entire state space of that signed chart: no
unspecified language remains. Pairwise survivor differences are a ternary
full shift, with an exact finite representation function and exact additive
energy.

This is useful separation of roles. The ambient pair geometry is now closed
form; the genuinely difficult successor problem is the order selection that
chooses only adjacent pairs from this ternary difference set.

## Dependency audit

- `R-9804` supplies the binary cylinder formula and its bijection with depth-
  `n` survivor classes.
- The signed coding, injectivity, shift conjugacy, multiplicities, energy, and
  dimension are proved directly here.
- `L-9815` is used only to call the ordered cyclic edges successor gaps.
- `L-9830` is used only in part 6 to identify the post-settlement carry; the
  ternary full-shift theorem does not depend on its borrow analysis.
- No probabilistic independence, asymptotic equidistribution, or ordinary
  infinite survivor is assumed.

## Gap audit

- The exact global pair distribution does not describe the highly selected
  subset of cyclically adjacent pairs.
- Difference-set sparsity alone does not lower-bound the smallest positive
  difference; a sparse modular set can still contain tightly clustered
  elements.
- The probability `2^(-r)` in part 4 is for a uniformly chosen ordered pair,
  not for the minimum survivor and its successor.
- Additive energy counts all ordered quadruples. It is not a successor-edge
  count and does not prove pseudorandomness.
- The infinite ternary difference set lies in `Z_2`; its nonzero points need
  not be ordinary nonnegative integers.
- The average and maximum gap in (31) give no lower bound for every gap or for
  the minimum survivor sequence.

## Adversarial tests

- There are `4^n` ordered binary-word pairs but only `3^n` differences. The
  missing multiplicity is exactly the choice between `(0,0)` and `(1,1)` at
  zero signed digits.
- The signed digit `-1` is residue `63 modulo 64`; replacing it by an illegal
  binary directive would destroy the shift identity.
- The all-zero signed word represents the zero class in `G_n`. As a positive
  ordinary pair it is one cylinder period `64^n`, not two distinct classes.
- Formula (28) has a one-bit distinction: changing `-1` directly to `1`
  contributes valuation `6k+1`, whereas the other first-symbol changes give
  `6k`.
- Equality modulo `64^r` counts common low directive prefixes. It is unrelated
  to the high-to-low lexicographic comparison which selects a successor.
- Haar-null difference geometry does not exclude a countable ordinary
  intersection.

## Remaining uncertainty

The exact ternary language contains all pair differences, but cyclic adjacency
is a global order constraint. No theorem here identifies which signed words
occur on the `2^n` successor edges, controls their initial or shifted zero
runs, or bounds the smallest cyclic gap.

## Suggested next attack

Express cyclic adjacency as the absence of a third binary cylinder in the
ordinary interval between the two endpoints. In signed coordinates this is a
forbidden decomposition of the successor gap into two positive signed
cylinders. An additive-order theorem showing that a long zero run permits such
a positive decomposition would turn the exact `3^n` difference geometry into
the missing lexicographic exchange argument.
