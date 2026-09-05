# L-9857 -- Finite ordinary separator for horizontal absorption

Claim ID: `L-9857`  
Title: Every fixed-width horizontal root has an explicit finite ordinary separator from the binary core  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`, `gpt56-synthesis-01-a`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9838`, `L-9842`, `L-9844`, `L-9849`  
Scope: finite ordinary-input testing of fixed-width absorption for binary-automatic shortcut-component colorings  
Related counterexample candidates: none

## Definitions

Use the setting and notation of `L-9849`. Thus `s=(s_n)_(n>=0)` is
finite-valued and 2-automatic, satisfies

\[
s_{2m}=s_m\quad(m\ge1),
\qquad
s_{2m+1}=s_{3m+2}\quad(m\ge0),
\tag{1}
\]

and has the finite, binary-section-closed core

\[
\boxed{
\mathcal F=\mathcal K_2(s)\cup\mathcal B,
\qquad
E_i\mathcal F\subseteq\mathcal F
\quad(i=0,1).
}
\tag{2}
\]

Put `F=|mathcal F|`. For `h,k>=1` and `0<=j<L_k`, where

\[
L_k=2\cdot3^{k-1},
\tag{3}
\]

write

\[
x_j=x_{h,k,j},
\qquad
w_j=w_{k,j},
\qquad
d_j=d_{h,k,j}\in\mathcal D\subseteq\mathcal F,
\tag{4}
\]

with all phase subscripts read modulo `L_k`. Their exact binary-section graph
is

\[
\boxed{
E_{w_j}x_j=x_{j+1},
\qquad
E_{1-w_j}x_j=d_j.
}
\tag{5}
\]

The cyclic word `w_0...w_(L_k-1)` contains both symbols and has least cyclic
period `L_k` by `L-9838`.

Words in this claim are read **least significant bit first**. For
`u=u_0...u_(ell-1) in {0,1}^*`, define

\[
[u]_2=\sum_{t=0}^{\ell-1}u_t2^t,
\qquad
E_\epsilon q=q,
\qquad
E_{ui}q=E_i(E_uq).
\tag{6}
\]

Then

\[
\boxed{
(E_uq)(m)=q\bigl(2^{|u|}m+[u]_2\bigr),
\qquad
(E_uq)(0)=q([u]_2).
}
\tag{7}
\]

The advertised width-dependent Moore bound is

\[
\boxed{
D_k
=F(F+L_k)
=|\mathcal F|\bigl(|\mathcal F|+2\cdot3^{k-1}\bigr).
}
\tag{8}
\]

## Statement

### 1. A decorated Moore presentation with at most `F+L_k` states

Let

\[
\widehat{\mathcal C}_{h,k}
=\{\widehat0,\ldots,\widehat{L_k-1}\}\sqcup\mathcal F
\tag{9}
\]

be a disjoint set of formal phase occurrences and actual core states. Define
the transitions from a phase occurrence by

\[
\boxed{
\delta(\widehat j,w_j)=\widehat{j+1},
\qquad
\delta(\widehat j,1-w_j)=d_j,
}
\tag{10}
\]

and, on the core, by

\[
\delta(f,i)=E_if
\qquad(f\in\mathcal F, i\in\{0,1\}).
\tag{11}
\]

Extend `delta` to LSF words from left to right:
`delta(q,epsilon)=q` and
`delta(q,ui)=delta(delta(q,u),i)`.

For each phase let

\[
z_j=\min\{0\le t<L_k:w_{j+t}=1\}.
\tag{12}
\]

Give the resulting Moore machine the output map

\[
\boxed{
\lambda(f)=f(0),
\qquad
\lambda(\widehat j)=d_{j+z_j}(0).
}
\tag{13}
\]

Then the formal state `widehat j` produces exactly the sequence `x_j`:

\[
\boxed{
\lambda(\delta(\widehat j,u))=x_j([u]_2)
\qquad(u\in\{0,1\}^*).
}
\tag{14}
\]

Consequently `K_2(x_j)` is contained in
`F union {x_0,...,x_(L_k-1)}` and has cardinality at most `F+L_k`.

This is a presentation, not necessarily a minimal automaton. In an absorbed
cycle, several formal phases may represent the same sequence, and a formal
phase may represent a state already in `F`. No quotient or distinctness
assumption is made. Such aliasing can only decrease the number of actual
kernel states; the presentation always has exactly `F+L_k` formal states.

### 2. Uniform fixed-width ordinary-prefix separator

For every `h>=1`, `0<=j<L_k`,

\[
\boxed{
x_{h,k,j}\in\mathcal F
\iff
\exists f\in\mathcal F\quad
x_{h,k,j}(n)=f(n)
\quad(0\le n<2^{D_k}).
}
\tag{15}
\]

Thus the finite signature

\[
\operatorname{Sig}_k(q)
=\bigl(q(n)\bigr)_{0\le n<2^{D_k}}
\tag{16}
\]

tests membership of every width-`k` root, uniformly in its central depth and
phase:

\[
\boxed{
x_{h,k,j}\in\mathcal F
\iff
\operatorname{Sig}_k(x_{h,k,j})
\in\{\operatorname{Sig}_k(f):f\in\mathcal F\}.
}
\tag{17}
\]

The proof actually shows that the shorter interval
`0<=n<2^(D_k-1)` suffices. The exponent `D_k` in (15)--(17) is retained as a
simple product bound with no off-by-one convention.

### 3. Shortest distinguishing words and sparse separators

Fix a root occurrence `widehat j` and `f in F`. If `x_j!=f`, there is a
shortest least-significant-first word

\[
u_f=u_0\cdots u_{\ell_f-1}
\tag{18}
\]

such that

\[
\lambda(\delta(\widehat j,u_f))
\ne
\lambda(\delta(f,u_f)).
\tag{19}
\]

Every such shortest word satisfies

\[
\boxed{
\ell_f\le D_k-1.
}
\tag{20}
\]

If `ell_f>0`, then its last, hence most significant, digit is one:

\[
\boxed{
u_{\ell_f-1}=1.
}
\tag{21}
\]

Consequently `u_f` is the canonical least-significant-first binary expansion
of the ordinary integer

\[
n_f=[u_f]_2<2^{D_k-1},
\tag{22}
\]

while the empty word corresponds to `n_f=0`.

If `x_j` is unabsorbed, choose one shortest word for every `f in F`. Then

\[
\boxed{
S_{h,k,j}=\{[u_f]_2:f\in\mathcal F\}
\subseteq[0,2^{D_k})
}
\tag{23}
\]

has at most `F` ordinary integers and separates the root from the entire
core:

\[
\forall f\in\mathcal F\ \exists n\in S_{h,k,j},
\qquad
x_{h,k,j}(n)\ne f(n).
\tag{24}
\]

The shortest words are obtained by breadth-first search in the Moore product
of (9)--(13) with the core automaton. A word labels an edge in the same order
as the low-to-high binary digits of its ordinary witness.

### 4. Exact finite evaluation from the escape decorations

Let `b_t(n)` be the `t`-th binary digit of an ordinary `n>=0`, padded by
zeros for all sufficiently large `t`, and set

\[
\tau_j(n)
=\min\{t\ge0:b_t(n)\ne w_{j+t}\}.
\tag{25}
\]

The minimum exists because the padded digits are eventually zero whereas
every period of `w` contains a one. The first mismatching bit leaves the
horizontal cycle through its decoration, giving the exact evaluation rule

\[
\boxed{
x_{h,k,j}(n)
=d_{h,k,j+\tau_j(n)}
\left(\left\lfloor\frac{n}{2^{\tau_j(n)+1}}\right\rfloor\right).
}
\tag{26}
\]

In particular, if `n<2^(D_k)`, then

\[
\tau_j(n)\le D_k+L_k-1.
\tag{27}
\]

All decoration states lie in the fixed finite core, whose binary transition
and output table is closed. Therefore the finite word `(w_j,d_j)_(j mod
L_k)` determines every entry of `Sig_k(x_j)` by a finite calculation. The
ordered compiler of `L-9844` supplies these labels at each fixed width.

Formula (26) remains valid in the absorbed case. Even if the mismatch edge
and the staying edge happen to lead to equal sequences after aliasing, (5)
still identifies the decorated occurrence and both evaluations agree. Thus
finite evaluation does not rely on the outside-core rigidity of `L-9849`.

### 5. What is and is not decided

For a fixed supplied width and decorated cycle, (15) is a finite absorption
decision. It need not be performed by enumerating the enormous interval in
(15): the product graph has at most `D_k` states, and backward reachability
from unequal-output pairs gives the same answer.

The ordinary-prefix horizon itself is nevertheless huge:

\[
2^{D_k}
=2^{F(F+2\cdot3^{k-1})}
=\exp(\Theta(3^k))
\quad(F\text{ fixed}).
\tag{28}
\]

No width-independent horizon is proved. More importantly, a finite test for
each individual `k` is not a decision of the quantified eventual-absorption
statement

\[
\exists k_0\ \forall k\ge k_0\ \forall h\ge1,
\qquad
x_{h,k,0}\in\mathcal F.
\tag{29}
\]

Running the fixed-width test successively supplies no termination certificate
for (29), and this claim proves no recurrence that bounds the last
unabsorbed width.

## Proof

### The decorated presentation

Because the staying word contains a one, `z_j` in (12) exists. Starting at
`x_j` and repeatedly reading the ordinary input zero follows the horizontal
cycle while `w_(j+t)=0`. At the first `t=z_j` with `w_(j+t)=1`, zero is the
escape bit, so (5) gives

\[
E_0^{z_j+1}x_j=d_{j+z_j}.
\tag{30}
\]

Evaluation at zero is unchanged by `E_0`, and hence

\[
x_j(0)=d_{j+z_j}(0).
\tag{31}
\]

This proves the phase-output formula (13). Define a map from formal
presentation states to actual sequences by

\[
\pi(\widehat j)=x_j,
\qquad
\pi(f)=f.
\tag{32}
\]

Equations (5), (10), and (11) show that `pi` intertwines both binary
transitions; (13) and (31) show that it preserves outputs. Induction on the
word length, followed by (7), proves (14).

The map `pi` need not be injective. Keeping its domain as a disjoint formal
presentation is precisely what handles absorbed-cycle aliases without first
solving the absorption problem.

### Moore-product bound

The core itself is a Moore automaton with state set `F`, transition `E_i`, and
output `f mapsto f(0)`. Form the product of this automaton with the decorated
presentation (9). It has at most

\[
(F+L_k)F=D_k
\tag{33}
\]

ordered pairs. Mark a pair when its two outputs differ.

Suppose `x_j!=f`. Some ordinary input distinguishes the two sequences, so a
marked pair is reachable from `(widehat j,f)`. Let `u` be a shortest word
reaching one. No ordered pair can repeat along its path: deleting the segment
between two equal pairs would reach the same marked terminal pair by a
shorter word. A path of length `ell` visits `ell+1` pairs, and therefore

\[
|u|\le D_k-1.
\tag{34}
\]

This proves (20).

For every actual sequence state `q`,

\[
(E_0q)(0)=q(0).
\tag{35}
\]

The presentation preserves this identity by (32). Hence appending a final
zero to an LSF word cannot change whether the terminal outputs differ. A
nonempty shortest distinguishing word cannot end in zero, which proves
(21). Equations (7), (20), and (21) then give the ordinary witness (22).

If `x_j in F`, choosing `f=x_j` proves the forward implication in (15). If
`x_j notin F`, apply the preceding argument to every `f in F`; each has a
distinguishing ordinary input below `2^(D_k-1)`, so no `f` can agree with
`x_j` throughout the larger interval in (15). This proves (15)--(17).
Choosing the shortest witness for every core state proves (23)--(24).

Equivalently, in the finite product graph, a starting pair represents equal
sequences exactly when no marked pair is reachable from it. This gives the
claimed breadth-first or backward-reachability construction.

### Decoration evaluation formula

Let `t=tau_j(n)`. For the first `t` low bits, (5) follows the successive
horizontal states. At the next bit it takes the escape edge and reaches
`d_(j+t)`. The unread high bits represent exactly

\[
\left\lfloor n/2^{t+1}\right\rfloor.
\tag{36}
\]

Applying (7) to the read prefix and then evaluating the remaining quotient
proves (26).

If `n<2^(D_k)`, all digits from position `D_k` onward are zero. Among the
`L_k` positions beginning there, at least one staying bit is one. Thus a
mismatch occurs no later than position `D_k+L_k-1`, proving (27). Once the
escape occurs, all further sections stay in `F` by (2). This proves the
finite-evaluation assertions and completes the proof. QED

## Motivation

`L-9849` reduces full ternary-kernel finiteness to eventual absorption of
horizontal roots into one fixed binary core, but leaves equality with that
core as an infinite-sequence question. The exact escape decorations make
each fixed-width root a finite Moore presentation: only the horizontal
phases can occur before the first escape, and every escape lands permanently
in the core.

The product argument turns that presentation into an ordinary-integer
separator with an explicit bound. It also isolates the remaining issue
sharply. Fixed-width equality is finite; controlling all unbounded widths is
still not.

## Dependency audit

- `L-9838` supplies `L_k`, the periodic staying word, and the fact that it
  contains both symbols.
- `L-9842` supplies the exact two-child graph (5) and
  `D subseteq K_2(s) subseteq F`.
- `L-9844` supplies an exact finite compiler for the ordered staying and
  decoration data used in (10), (13), and (26).
- `L-9849` supplies the fixed finite section-closed core and the absorption
  interpretation. Its outside-core equality classification is not needed
  for the Moore-product bound.
- The LSF word identity, nonminimal presentation, shortest-word bound, and
  ordinary separator are proved directly here.
- No Cobham theorem, convergence hypothesis, or Collatz connectivity claim
  is used.

## Gap audit

- The bound is width-dependent: `D_k=Theta(3^k)` and its literal ordinary
  prefix has `2^(Theta(3^k))` entries.
- Product-graph search avoids enumerating that prefix, but the decorated
  presentation itself still has `L_k` phase occurrences.
- No bound independent of `k` is obtained, and no last unabsorbed width is
  bounded.
- The theorem decides a supplied fixed-width occurrence. It does not decide
  the universal eventual-absorption quantifier (29).
- The ordered compiler generates the finite presentation; finite-state
  generation across widths does not force any phase to alias the core.
- No nonconstant component coloring is constructed or excluded.

## Adversarial tests

- Binary section words are read least significant bit first. Reversing the
  word changes both the represented integer and the Moore path.
- A path with `ell` edges visits `ell+1` pairs, so the product bound is
  `ell<=D_k-1`, not merely `ell<=D_k`.
- A shortest nonempty word cannot end in zero because `E_0q(0)=q(0)`.
  This is why the word is a canonical ordinary binary expansion rather than
  only a padded address.
- The phase states in (9) are formal occurrences. Assuming them distinct as
  sequences would silently assume the cycle is unabsorbed; quotienting them
  in advance would silently solve the problem being tested.
- The output of a formal phase is not extra unknown data. Its padded-zero
  path exits at the first staying one, giving (13).
- A shortest distinguishing word need not visibly leave the horizontal
  cycle before it ends. Its terminal phase output is still evaluated by the
  later padded-zero exit encoded in (13).
- Equality of the two labeled children after absorbed aliasing does not
  invalidate (26); the selected edge identities remain exact even when their
  target sequences coincide.
- Finiteness for each fixed width does not permit checking infinitely many
  widths and declaring eventual absorption after an arbitrary cutoff.

## Remaining uncertainty

Can the recursively compiled decorated presentations be quotiented against
`F` by a width-independent invariant? The present theorem bounds a finite
test after the width is supplied, but the bound grows with every new
horizontal phase and reveals no mechanism forcing eventual absorption.

## Suggested next attack

Run Moore partition refinement symbolically through the three-block width
lift of `L-9844`, rather than expanding all `L_k` phases. A finite quotient of
the pair relation

\[
(\text{horizontal phase},\text{core state})
\tag{37}
\]

that is preserved by the lift would replace the growing bound (8) by a
width-independent separator. Failure of such closure should identify an
explicit new pair-state invariant carried by every unabsorbed width.
