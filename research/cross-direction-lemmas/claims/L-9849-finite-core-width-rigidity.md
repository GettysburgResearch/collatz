# L-9849 -- Finite-core absorption or width-rigid horizontal roots

Claim ID: `L-9849`  
Title: Every horizontal root cycle is absorbed by one finite core or is intrinsically tagged by its width  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9823`, `L-9836`, `L-9838`, `L-9842`, `L-9844`; Eilenberg's kernel criterion and Cobham's theorem  
Scope: equality and cross-width proliferation of positive-valuation ternary root states for a 2-automatic shortcut-component coloring  
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
\mathcal K=\mathcal K_2(s),
\qquad
b_h(n)=s_{3^hn},
\qquad
\mathcal B=\{b_h:h\ge0\}.
\tag{2}
\]

By `L-9825`, `B` is finite. The finite central binary core is

\[
\boxed{
\mathcal F=\mathcal K\cup\mathcal B.
}
\tag{3}
\]

For a sequence `f`, put

\[
E_i f(n)=f(2n+i),
\qquad
P_a f(n)=f(3n+a).
\tag{4}
\]

For `k>=1`, define

\[
L_k=2\cdot3^{k-1},
\qquad
r_{k,j}=[2^{-j}]_{3^k},
\qquad
w_{k,j}=r_{k,j}\bmod2
\quad(0\le j<L_k).
\tag{5}
\]

Indices in `j` are cyclic modulo `L_k`. For `h>=1`, the pointed horizontal
root and its escape decoration are

\[
\boxed{
x_{h,k,j}(n)
=s_{3^{h+k}n+3^hr_{k,j}},
\qquad
d_{h,k,j}=c_{h+k+1,v_{h,k,j}}
\in\mathcal D.
}
\tag{6}
\]

Here `D` and the canonical escape offset `v_(h,k,j)` are those of `L-9842`.
The exact binary-section graph is

\[
\boxed{
E_{w_{k,j}}x_{h,k,j}=x_{h,k,j+1},
\qquad
E_{1-w_{k,j}}x_{h,k,j}=d_{h,k,j}.
}
\tag{7}
\]

Moreover,

\[
\boxed{
\mathcal D\subseteq\mathcal K\subseteq\mathcal F.
}
\tag{8}
\]

For later equality testing, define the pointed ordered decoration word

\[
\mathbf d_{h,k}^{(j)}
=\left(d_{h,k,j+t}\right)_{0\le t<L_k}.
\tag{9}
\]

## Statement

### 1. The augmented ordered compiler also lifts the roots

Use the finite lift data of `L-9844`:

\[
q_{k,j}=r_{k,j}\bmod3,
\qquad
\rho_{k,j}
=\frac{[2^{-j}]_{3^{k+1}}-r_{k,j}}{3^k},
\tag{10}
\]

and, for `m in {0,1,2}`,

\[
\begin{aligned}
\tau_{k,j,m}
&=[\rho_{k,j}-mq_{k,j}]_3,\\
a_{k,j,m}
&=[2(\rho_{k,j}+w_{k,j}-1)-2mq_{k,j}]_3.
\end{aligned}
\tag{11}
\]

Then the full ordered width lift is

\[
\boxed{
\begin{aligned}
x_{h,k+1,j+mL_k}
&=P_{\tau_{k,j,m}}x_{h,k,j},\\
w_{k+1,j+mL_k}
&=[w_{k,j}+\tau_{k,j,m}]_2,\\
d_{h,k+1,j+mL_k}
&=P_{a_{k,j,m}}d_{h,k,j}.
\end{aligned}
}
\tag{12}
\]

Starting from `rho_(k,0)=0`, the state `rho` evolves during the scan
`0<=j<L_k-1` by the three-state update

\[
\rho_{k,j+1}=[w_{k,j}-\rho_{k,j}]_3,
\tag{13}
\]

while `q_(k,j)` is the fixed alternating clock. Thus `(q,rho,d,w)` gives an
exact finite-state compiler for the ordered local data, and (12) adds the
previously implicit infinite root sequence to that compiler.

### 2. Finite-core absorption dichotomy

The core `F` is closed under both binary sections. Explicitly,

\[
\boxed{
E_0b_h=b_h,
\qquad
E_1b_h\in\mathcal K,
\qquad
E_i\mathcal K\subseteq\mathcal K.
}
\tag{14}
\]

Consequently, for every `h>=1` and `k>=1`, exactly one of the following holds:

\[
\boxed{
\begin{array}{ll}
\text{absorbed:}
&x_{h,k,j}\in\mathcal F
\quad\text{for every }j;\\[1mm]
\text{unabsorbed:}
&x_{h,k,j}\notin\mathcal F
\quad\text{for every }j.
\end{array}
}
\tag{15}
\]

On an unabsorbed cycle, the staying bit is intrinsic to the infinite root
sequence:

\[
\boxed{
w(x)=\text{the unique }i\in\{0,1\}
\text{ such that }E_i x\notin\mathcal F.
}
\tag{16}
\]

Indeed, the staying child is the next unabsorbed root, whereas the other child
is an escape decoration in `D subseteq F`. Thus the entire periodic staying
tail can be reconstructed from the root sequence and membership in the fixed
finite core.

### 3. Exact equality classification outside the core

Suppose `x_(h,k,j)` and `x_(h',k',j')` are both unabsorbed. Then

\[
\boxed{
x_{h,k,j}=x_{h',k',j'}
\iff
\left(
\begin{array}{l}
k=k',\\
j=j',\\
\mathbf d_{h,k}^{(j)}
=\mathbf d_{h',k}^{(j)}.
\end{array}
\right)
}
\tag{17}
\]

Here `j=j'` is interpreted in the common canonical range
`0<=j,j'<L_k`.

In particular:

1. every unabsorbed width-`k` cycle contains exactly `L_k` distinct root
   sequences;
2. unabsorbed cycles at different widths are disjoint as sets of sequences;
3. at a fixed width and pointed phase, the complete ordered decoration word
   is an exact equality invariant, not merely a finite presentation.

The first two conclusions are independent of whether two different central
bases happen to give the same decoration word.

### 4. Eventual absorption is equivalent to full ternary-kernel finiteness

Call a width `k` unabsorbed if at least one positive central depth produces an
unabsorbed cycle, and put

\[
\mathcal U
=\{k\ge1:\exists h\ge1, x_{h,k,0}\notin\mathcal F\}.
\tag{18}
\]

Then

\[
\boxed{
|\mathcal K_3(s)|<\infty
\iff
|\mathcal U|<\infty
\iff
\exists k_0\ \forall k\ge k_0\ \forall h\ge1,
\quad x_{h,k,0}\in\mathcal F.
}
\tag{19}
\]

The converse direction uses the finite central-base parameter explicitly:

\[
\boxed{
x_{h,k,j}(n)
=b_h(3^kn+r_{k,j}).
}
\tag{20}
\]

Thus, at any fixed width `k`, the entire family over all `h>=1` and all phases
has at most `|B|L_k` distinct sequences. If only finitely many widths are
unabsorbed, all roots outside `F` therefore lie in a finite union of finite
families.

Conversely, for every finite `U_0 subseteq U`, choosing one unabsorbed cycle
at each selected width gives the quantitative lower bound

\[
\boxed{
|\mathcal K_3(s)\setminus\mathcal F|
\ge
\sum_{k\in\mathcal U_0}L_k.
}
\tag{21}
\]

Hence infinitely many unabsorbed widths force infinitely many genuinely new
ternary root states.

### 5. Zero-or-infinite consequence for a component coloring

Under the hypotheses (1),

\[
\boxed{
s|_{\mathbb Z_{\ge1}}\text{ is constant}
\iff
\mathcal U=\varnothing
\iff
|\mathcal U|<\infty
\iff
|\mathcal K_3(s)|<\infty.
}
\tag{22}
\]

Therefore any hypothetical nonconstant 2-automatic component coloring must
have infinitely many unabsorbed widths. At arbitrarily large coheight it must
create a full horizontal cycle of `L_k=2*3^(k-1)` distinct states outside the
same fixed finite core `F`.

This is a necessary state-proliferation theorem, not a construction of such a
coloring and not a proof that the nonconstant case exists.

## Proof

### Augmented root lift

The formulas for `tau`, `a`, the new staying bit, and the new decoration are
`L-9844/(9),(12),(20),(21)`. Directly from (6),

\[
\begin{aligned}
P_{\tau_{k,j,m}}x_{h,k,j}(n)
&=s_{3^{h+k}(3n+\tau_{k,j,m})+3^hr_{k,j}}\\
&=s_{3^{h+k+1}n
+3^h(r_{k,j}+\tau_{k,j,m}3^k)}\\
&=x_{h,k+1,j+mL_k}(n),
\end{aligned}
\tag{23}
\]

where the final equality uses the exact lift definition of `tau`. This proves
the first line of (12), and the cited formulas prove the other two lines.

### Core closure and cycle dichotomy

The binary kernel `K` is section-closed by definition. The central-base
closure `L-9836/(11)` gives

\[
E_0b_h=b_h,
\qquad
E_1b_h(n)
=s_{2^{2h+3}n+2^{2h+2}+1}
\in\mathcal K.
\tag{24}
\]

Since `B` is finite, this proves both finiteness and binary-section closure of
`F`, establishing (14).

If one state `x_(h,k,j)` of a horizontal cycle belongs to `F`, repeated use of
the staying transition in (7) keeps every later state in `F`. The horizontal
orbit returns after `L_k` steps and visits every cycle position, so the whole
cycle lies in `F`. Otherwise no position lies in `F`. This proves (15).

On an unabsorbed cycle, (7)--(8) show that `E_(w_(k,j))x` is outside `F` and
`E_(1-w_(k,j))x` is inside `F`. This proves the intrinsic reconstruction rule
(16).

### Necessity in the equality classification

Assume

\[
x_{h,k,j}=x_{h',k',j'}
\tag{25}
\]

and both sides are outside `F`. Their binary sections are equal. Rule (16)
therefore forces

\[
w_{k,j}=w_{k',j'}
\]

and then (7) forces equality of the two next horizontal roots. Iterating gives

\[
w_{k,j+t}=w_{k',j'+t}
\qquad(t\ge0).
\tag{26}
\]

By `L-9838/(19a)`, the two periodic words have exact least periods `L_k` and
`L_(k')`. Equal infinite periodic tails have the same least period, so
`L_k=L_(k')`, hence `k=k'`. With the width fixed, (26) says that `j'-j` is a
cyclic period of the width-`k` word. Its least cyclic period is `L_k`, so
`j=j'` in the canonical range.

At every matched cycle position, applying the opposite binary section in (7)
to the equal roots gives

\[
d_{h,k,j+t}=d_{h',k,j+t}
\qquad(0\le t<L_k).
\tag{27}
\]

This is equality of the pointed ordered decoration words and proves the
forward implication in (17).

### Sufficiency in the equality classification

Now suppose `k,j` agree and the decoration words in (17) are equal. Take any
ordinary integer `n>=0`, write its binary digits least significant first, and
pad that digit string by infinitely many zeros. Starting from the two roots,
follow the same section path prescribed by those padded digits.

As long as the input digit equals the current staying bit, both paths advance
to the next aligned cycle position. If it differs, both paths enter the same
decoration sequence by the assumed equality of the ordered decoration words;
all subsequent evaluations are then identical.

Such a mismatch occurs after finitely many steps. Indeed, the input digits are
eventually all zero, while the periodic staying word contains both symbols
(in fact `L-9838/(19)` says it is balanced). Thus a staying bit equal to one
eventually meets a padded zero. It follows that the two roots take the same
value at every `n`, proving the reverse implication in (17).

Taking the two roots from the same cycle shows that equality at two phases
would force those phases to agree, so an unabsorbed cycle has exactly `L_k`
distinct states. Equation (26) also proves cross-width disjointness.

### Full-kernel criterion and Cobham dichotomy

Every ternary state has the form

\[
c_{E,R}(n)=s_{3^En+R},
\qquad0\le R<3^E.
\]

If `R=0`, it belongs to `B subseteq F`. If `R>0`, write

\[
h=\nu_3(R),
\qquad
k=E-h.
\]

When `h=0`, the state is absolute primitive and lies in `K subseteq F` by
`L-9838/(16b)`. When `h>=1`, the unit `R/3^h` is exactly one `r_(k,j)`, so the
state is `x_(h,k,j)`. This exhausts the ternary kernel.

If `U` is finite, (20) and finiteness of `B` show that the states at its
finitely many widths form a finite set; every other ternary state lies in the
finite core `F`. Hence `K_3(s)` is finite. If `U` is infinite, choose one
unabsorbed cycle at each of finitely many selected widths. Part 3 makes their
`L_k` states distinct within a width and disjoint across widths, proving (21)
and infinitude. This proves (19).

By Eilenberg's criterion, finiteness of `K_3(s)` is exactly 3-automaticity.
The sequence is already 2-automatic, so Cobham's theorem makes it eventually
periodic. The component-coloring rigidity `L-9823` then makes it constant on
the positive indices. Conversely, if the positive-index coloring is constant,
every noncentral ternary state is the corresponding constant sequence, which
already occurs as `E_1s in K`; hence `U` is empty. Combining this with (19)
proves (22). QED

## Motivation

`L-9844` shows that every local width refinement is generated by a finite
`(q,rho,d,w)` compiler. That fact alone cannot decide whether longer pointed
cycles denote new infinite sequences. The missing invariant is membership in
the finite section-closed core `F`.

Outside that core, the horizontal transition is the unique binary child that
remains outside. The staying word is therefore readable from the root itself,
and its exact least period makes width an equality invariant. Finite-state
generation can organize the new cycles, but it cannot identify two different
unabsorbed widths.

The automaticity frontier is consequently an absorption question: a finite
ternary kernel is possible only if every sufficiently large horizontal cycle
falls back into the fixed core. Any nonconstant coloring must fail absorption
at infinitely many widths.

## Dependency audit

- `L-9836` supplies finiteness and binary-section closure of the central core
  `F`; its exact formulas are restated in (14) and (24).
- `L-9838` supplies the horizontal cycle, exact least period, balance of the
  staying word, and primitive-state collapse into `K`.
- `L-9842` supplies the escape decorations in `D subseteq K` and the decorated
  cycle normal form.
- `L-9844` supplies the explicit `q,rho,tau,a,w,d` width compiler; the root
  lift in (12) is derived directly here.
- `L-9823`, Eilenberg, and Cobham are used only for the final constant versus
  infinitely-many-widths consequence.
- Equality classification, finite-central-parameter counting, and the
  absorption criterion are proved directly.

## Gap audit

- The theorem does not prove that any large width is absorbed or unabsorbed.
- The finite compiler does not decide membership of a lifted root in `F`.
- Infinitely many unabsorbed widths are necessary for a nonconstant coloring,
  not a construction or consistency proof for one.
- The exact decoration-word equality test applies outside the core; absorbed
  cycles may alias freely inside the finite core.
- No rate is proved for the set of unabsorbed widths. It may be arbitrarily
  sparse under the present results.
- No Collatz orbit, component classification, or counterexample follows.

## Adversarial tests

- The core must be `F=K union B`, not merely `K`: central-base states are a
  separate finite family, and including them makes the final exhaustion
  exact.
- Binary-section closure is used only forward. One core state on a finite
  horizontal cycle suffices because repeated staying sections traverse the
  whole cycle.
- Width is intrinsic only outside `F`, where exactly one child remains
  outside. An arbitrary loop word in a finite automaton would not have this
  rigidity.
- The root width lift uses `P_tau`; `P_a` acts on the escape decoration.
  Interchanging these digits gives the wrong augmented compiler.
- Sufficiency in (17) uses padded ordinary binary expansions and the presence
  of both symbols in the staying word. Transition-graph similarity without
  this exit argument would miss the state output at zero.
- Infinite central depth does not spoil the converse in (19), because (20)
  depends on `h` only through one of the finitely many sequences in `B`.
- An unabsorbed cycle has `L_k` distinct roots; no count of decoration words
  is needed for the quantitative lower bound.

## Remaining uncertainty

Which widths are absorbed? Equivalently, when does a nontrivial central-base
state `b_h(3^kn+1)` coincide with one of the finitely many sequences in `F`?
The ordered compiler determines all of its local sections, but no current
invariant decides this equality.

## Suggested next attack

Construct a finite separating family of ordinary test inputs for membership
in `F`. Feed those inputs through the padded-digit exit description in the
proof of (17), and express their values as functions of the ordered decoration
word. A uniform separator would turn absorption at width `k` into a finite
word condition; failure of every bounded separator would itself quantify how
new roots evade the core.
