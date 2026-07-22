# L-9836 -- Fixed-width closure of translated ternary sections

Claim ID: `L-9836`  
Title: Every fixed-width translated cone above the central ternary spine has a uniformly finite binary kernel  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9825` for central-spine finiteness and its exact odd-section formula  
Scope: finite-valued 2-automatic sequences satisfying the shortcut-component identities  
Related counterexample candidates: none

## Definitions

Let `s=(s_n)_(n>=0)` take values in a finite alphabet and, on positive
indices, satisfy

\[
\boxed{
s_{2m}=s_m\quad(m\ge1),
\qquad
s_{2m+1}=s_{3m+2}\quad(m\ge0).
}
\tag{1}
\]

Use one fixed arbitrary value at index zero, as in `L-9825`. For a sequence
`f`, define its binary sections

\[
E_if(n)=f(2n+i),
\qquad i\in\{0,1\},
\tag{2}
\]

and let

\[
\mathcal K=\mathcal K_2(s),
\qquad
K=|\mathcal K|<\infty.
\tag{3}
\]

The central ternary states are

\[
b_e(n)=s_{3^en},
\qquad
\mathcal B=\{b_e:e\ge0\},
\qquad
M=|\mathcal B|.
\tag{4}
\]

By `L-9825`,

\[
\boxed{M\le K.}
\tag{5}
\]

For the full ternary kernel, write

\[
c_{E,R}(n)=s_{3^En+R},
\qquad
0\le R<3^E.
\tag{6}
\]

For a fixed width `k>=0`, define the central-cone states

\[
\boxed{
h_{e;k,r}(n)
=b_e(3^kn+r)
=c_{e+k,3^er}(n),
\qquad
e\ge0,\qquad 0\le r<3^k,
}
\tag{7}
\]

and put

\[
\mathcal C_k
=\{h_{e;k,r}:e\ge0, 0\le r<3^k\}.
\tag{8}

\]

The coheight of a noncentral ternary state `c_(E,R)` is

\[
\operatorname{coht}(E,R)=E-\nu_3(R)
\qquad(R>0).
\tag{9}

\]

It measures the state's distance from the central spine after removing all
common powers of three from its level and offset.

## Statement

### 1. One common finite binary closure for the central spine

The family

\[
\boxed{
\mathcal F=\mathcal K\cup\mathcal B
}
\tag{10}

\]

is closed under both binary section operators. More precisely,

\[
\boxed{
E_0b_e=b_e,
\qquad
E_1b_e(n)
=s_{2^{2e+3}n+2^{2e+2}+1}
\in\mathcal K,
}
\tag{11}

\]

while `K_2(s)` is section-closed by definition. Consequently

\[
\boxed{
|\mathcal F|\le K+M\le2K,
\qquad
\mathcal K_2(b_e)\subseteq\mathcal F
\quad(e\ge0).
}
\tag{12}

\]

Thus all central states are recognized inside one common finite binary state
space; the automaton is uniform in `e`.

### 2. Fixed-multiplier affine closure

Let `a>=1` be fixed and define

\[
\mathcal H_a(\mathcal F)
=\{H_{f,r}:f\in\mathcal F, 0\le r<a\},
\qquad
H_{f,r}(n)=f(an+r).
\tag{13}

\]

This family is closed under `E_0,E_1`. Indeed, for `i in {0,1}`, write

\[
ai+r=2q+j,
\qquad
j\in\{0,1\},\qquad 0\le q<a.
\tag{14}

\]

Then

\[
\boxed{
E_iH_{f,r}=H_{E_jf,q}.
}
\tag{15}

\]

It follows that every member of `H_a(F)` is 2-automatic and

\[
\boxed{
\bigcup_{H\in\mathcal H_a(\mathcal F)}
\mathcal K_2(H)
\subseteq\mathcal H_a(\mathcal F),
\qquad
|\mathcal H_a(\mathcal F)|
\le a(K+M)\le2aK.
}
\tag{16}

\]

This supplies an explicit common automaton bound for every fixed affine
multiplier, rather than invoking closure of automatic sequences abstractly.

### 3. Uniform fixed-width central-cone theorem

For every fixed `k>=0`,

\[
\boxed{
\mathcal C_k
\subseteq\mathcal H_{3^k}(\mathcal F).
}
\tag{17}

\]

Therefore

\[
\boxed{
|\mathcal C_k|
\le3^kM
\le3^kK,
}
\tag{18}

\]

and, more strongly,

\[
\boxed{
\left|
\bigcup_{h\in\mathcal C_k}\mathcal K_2(h)
\right|
\le3^k(K+M)
\le2\,3^kK.
}
\tag{19}

\]

Thus every bounded-coheight region of the translated ternary state table has
a uniform finite binary realization.

### 4. Exact profile count and eventual scale periodicity

The complete depth-`k` profile of a central state is

\[
\Phi_k(f)
=\bigl(f(3^kn+r)\bigr)_{0\le r<3^k}.
\tag{20}

\]

The map `Phi_k` is injective. Hence

\[
\boxed{
\left|
\{\Phi_k(b_e):e\ge0\}
\right|=M.
}
\tag{21}

\]

Moreover,

\[
b_{e+1}(n)=b_e(3n).
\tag{22}

\]

The sequence of central states is therefore an orbit of one deterministic
map on `B`. There exist integers `mu>=0,p>=1` with

\[
\boxed{
\mu+p\le M,
\qquad
b_{e+p}=b_e\quad(e\ge\mu).
}
\tag{23}

\]

For every fixed `k,r`, the same preperiod and period give

\[
\boxed{
h_{e+p;k,r}=h_{e;k,r}
\quad(e\ge\mu).
}
\tag{24}

\]

At the first translated level, put

\[
p_e(n)=b_e(3n+1),
\qquad
q_e(n)=b_e(3n+2).
\tag{25}

\]

Then

\[
\boxed{
\left|
\{(b_{e+1},p_e,q_e):e\ge0\}
\right|=M\le K,
}
\tag{26}

\]

each of the two translated families has at most `K` members, both are
eventually periodic in `e`, and their combined binary kernels lie in a set of
at most

\[
\boxed{3(K+M)\le6K}
\tag{27}

\]

states. This completely controls the two families requested at the frontier
of `L-9825`.

### 5. Exact localization of the remaining full-kernel problem

The fixed-width cones exhaust the full ternary kernel:

\[
\boxed{
\mathcal K_3(s)=\bigcup_{k\ge0}\mathcal C_k.
}
\tag{28}

\]

Indeed, if `R>0`, set

\[
e=\nu_3(R),
\qquad
k=E-e,
\qquad
r=R/3^e.
\tag{29}

\]

Then

\[
\boxed{c_{E,R}=h_{e;k,r}.}
\tag{30}

\]

The central case `R=0` belongs to `C_0`. Consequently, if the full ternary
kernel is infinite, every infinite subfamily must have unbounded coheight.
No fixed translated layer, and no bounded collection of layers, can contain
the obstruction.

### 6. Sharpness of the fixed-width argument without the full odd identity

Let

\[
u_n=
\begin{cases}
1,&n\text{ is a positive power of }2,\\
0,&\text{otherwise},
\end{cases}
\qquad n\ge0.
\tag{31}

\]

This sequence is 2-automatic and obeys `u_(2m)=u_m` for every `m>=1`. Its
central ternary spine is maximally simple:

\[
\boxed{
u_{3^en}=0
\quad(e\ge1, n\ge0).
}
\tag{32}

\]

Nevertheless the translated states

\[
v_e(n)=u_{3^en+1}
\qquad(e\ge1)
\tag{33}

\]

are all distinct. Their first `1` after `n=0` occurs exactly at

\[
\boxed{
N_e=\frac{2^{2\cdot3^{e-1}}-1}{3^e}.
}
\tag{34}

\]

Thus every fixed-width cone can be finite while the union over unbounded
width is infinite.

This example satisfies even the odd component identity away from one sparse
set. Precisely,

\[
u_{2m+1}\ne u_{3m+2}
\iff
m=\frac{2^{2j+1}-2}{3}
\quad\text{for some }j\ge1.
\tag{35}

\]

The exceptional set has density zero. Hence automaticity, exact doubling
invariance, central-spine finiteness, and a density-one odd identity still do
not make the bounds (18)--(19) uniform in `k`.

The sequence `u` is not a component coloring and does not refute a possible
full-kernel theorem under all of (1).

## Proof

### Common binary closure

The central-state even section is

\[
E_0b_e(n)=s_{2\cdot3^en}=s_{3^en}=b_e(n).
\tag{36}

\]

The odd-section formula in `L-9825` is exactly (11), so `E_1b_e` belongs to
`K_2(s)`. Since a binary kernel is closed under `E_0,E_1`, this proves that
`F` is section-closed and proves (12).

For the affine state `H_(f,r)`, direct calculation gives

\[
\begin{aligned}
E_iH_{f,r}(n)
&=f(2an+ai+r)\\
&=f(2(an+q)+j)\\
&=(E_jf)(an+q),
\end{aligned}
\tag{37}

\]

which proves (15). The inequality `0<=q<a` follows from
`0<=ai+r<2a`. Closure and the cardinality bound prove (16).

### Central cones and profiles

Equation (7) puts every member of `C_k` in `H_(3^k)(F)`. For each fixed
residue `r`, applying the same affine section operator to the `M` members of
`B` gives at most `M` sequences. Summing over the `3^k` residues proves (18),
while (16) proves (19).

The profile `Phi_k(f)` recovers every value of `f`: write an index uniquely as
`3^kn+r`. Therefore `Phi_k` is injective and (21) follows. Equation (22) is
immediate from the definition of `b_e`. A deterministic orbit through `M`
states has preperiod plus period at most `M`, proving (23)--(24). At `k=1`,
the profile is exactly `(b_(e+1),p_e,q_e)`, which proves (26)--(27).

For a nonzero canonical residue `R`, substitution of (29) into (7) gives

\[
h_{e;k,r}(n)
=s_{3^e(3^{E-e}n+R/3^e)}
=s_{3^En+R},
\tag{38}

\]

proving (28)--(30). The final localization assertion follows because a finite
union of the finite sets `C_0,...,C_L` is finite.

### Explicit obstruction outside the full component class

The canonical binary language of positive powers of two is `10^*`, proving
2-automaticity of `u`; doubling invariance and (32) are immediate.

For `v_e(n)=1` one needs

\[
2^a\equiv1\pmod {3^e},
\qquad
n=\frac{2^a-1}{3^e}.
\tag{39}

\]

For `a=2m`, the elementary LTE identity gives

\[
\nu_3(2^{2m}-1)=\nu_3(4^m-1)=1+\nu_3(m),
\tag{40}

\]

while odd `a` cannot give residue one modulo three. Thus the least positive
exponent in (39) is `a=2*3^(e-1)`, proving (34). The numbers `N_e` tend
strictly to infinity, so the position of the second `1` distinguishes all
the sequences `v_e`.

For `m>=1`, the odd integer `2m+1>1` is not a power of two, so the left side
of the odd identity is zero. The right side is one precisely when
`3m+2=2^a`; reduction modulo three forces `a` odd. The case `a=1` is `m=0`
and satisfies the identity, while `a=2j+1>=3` gives exactly (35). The
exception count below `X` is `O(log X)`, proving density zero. This completes
the proof. QED

## Motivation

`L-9825` proves that the central ternary spine is finite but leaves its first
translated descendants open. Those descendants actually close immediately,
and the same argument controls every fixed number of ternary levels at once.
The affine family (13) also supplies one explicit common binary automaton for
the whole bounded-coheight region.

The result moves the frontier rather than closing it: the full ternary kernel
is an increasing union of these finite cones, and the bound grows as `3^k`.
Part 5 identifies unbounded coheight as the only possible location of an
infinite family.

## Dependency audit

- `L-9825` supplies `|B|<=K` and the exact formula placing `E_1b_e` in the
  binary kernel of `s`.
- The affine transition (15), uniform kernel bounds, profile periodicity,
  cone exhaustion, and obstruction are proved directly here.
- LTE in (40) is used only for the explicit location of the second `1` in the
  abstract obstruction; it is the standard elementary `3`-adic LTE case.
- No Cobham theorem, Collatz convergence statement, or connectivity premise
  is used.

## Gap audit

- The bound in (19) grows exponentially with the coheight `k`; it is not a
  uniform bound on the full ternary kernel.
- Eventual periodicity in the scale variable `e` at each fixed address does
  not imply eventual periodicity in the integer variable `n`.
- Finiteness of every `C_k` separately does not imply finiteness of their
  countable union.
- The power-of-two obstruction fails the full odd identity on the explicit
  sparse set (35). It is not a component coloring or a Collatz counterexample.
- Density-one satisfaction of a functional identity cannot replace exact
  satisfaction at every index.
- Nothing here proves that a nonconstant 2-automatic component coloring
  exists.

## Adversarial tests

- The first translated states are `c_(e+1,3^e)` and `c_(e+1,2*3^e)`, not
  `c_(e+1,1)` and `c_(e+1,2)` when `e>0`.
- A fixed-width cone keeps `k` fixed while `e` varies. Allowing `k` to grow is
  exactly the unresolved full-kernel problem.
- In (14), the remainder `q` is always below `a`; omitting the division of
  `ai+r` by two would not give a closed affine family.
- The profile count in (21) is exactly `M`, but the union of its coordinate
  sequences can have as many as `3^kM` members.
- The special case `R=0` must not use `nu_3(0)`; it lies in the central cone
  `C_0` by definition.
- The obstruction's all-zero central spine begins at `e=1`; `b_0=u` is not
  zero.

## Remaining uncertainty

It remains open whether the exact odd identity in (1) forces a bound on the
coheight needed to represent every distinct state, or forces repetitions
between states lying in cones of different widths. Either conclusion would
make the full ternary kernel finite and finish the automatic-coloring problem
through Cobham and `L-9823`.

## Suggested next attack

Restrict to primitive translated states `c_(E,R)` with `3` not dividing `R`,
since part 5 reduces every noncentral state to one of these at its full
coheight. Iterate the exact binary-section table in `L-9825/(14)` and ask
whether the full odd identity forces a primitive state into a bounded-width
cone after a uniformly bounded binary word. The power-of-two obstruction
shows that any such proof must use the identity on its sparse exceptional
indices, not merely on a density-one set.
