# Independent repetition counts: an effective bounded-language classifier

Research checkpoint, 2026-11-22. **The full Collatz conjecture is not proved.**

**Late-head comparison:** PR183 subsequently published the same qualitative
free-exponent classification at `68345f60a4f757acb42a69a4ac95910f8ce26163`.
[The sharper combined cutoff](SHARPER_BLOCK_CUTOFF.md) credits that overlap
and combines its improved real chaining factor with this note's exact
coefficient reserve and suffix rotation. The original conservative cutoff
below remains valid; its 12 formal arithmetic statements are unchanged.

This note extends PR185's supplied linear one-parameter schema to arbitrary
independent repetition counts. It gives an explicit finite cutoff outside
cycles already represented by one of the supplied blocks. The arithmetic
kernel, including its full ordinary-path interface, is checked in
[BlockRepetitionBudget.lean](lean/BlockRepetitionBudget.lean). Rotation and the imported logarithm separation
are written arguments, not Lean declarations.

This is a simpler classification proof and a formalized reusable interface,
not a claim to have discovered periodic-dictionary complexity. A fresh
literature check found a substantially stronger recent dictionary theorem;
the comparison and its exact relevance are recorded below.

## 1. Scope and output

Use the shortcut map

\[
T(x)=\begin{cases}x/2&x\equiv0\pmod2,\\(3x+1)/2&x\equiv1\pmod2.\end{cases}
\]

Supply nonempty binary blocks \(V_1,\ldots,V_r\). Consider every word

\[
W(e)=V_1^{e_1}\cdots V_r^{e_r},\qquad e_i\in\mathbb N_0,
\tag{1}
\]

with independent exponents. No common parameter, ordering of exponent sizes,
or bounded exponent ratio is assumed.

The result is an effective algorithm producing a finite list of all primitive
positive ordinary cycles realized by (1). Their full exponent sets can then
be recognized by finite automata on those explicitly replayed cycles.
More specifically, every realization either has total shortcut clock below
the explicit cutoff in Section 5, or lies on a cycle represented by one of
the original blocks itself. Those template cycles are computed first and
are never assumed to be trivial.

Zero exponents are deleted for a given input. The entirely empty word is a
zero-clock identity, not a positive-cycle certificate. A nonempty all-zero
binary word cannot be a positive cycle. Empty supplied blocks can be removed
without changing the nonempty words under consideration.

## 2. Exact legality and the repeated-block reserve

For a block \(V\) of length \(L>0\), with \(s\) odd branches, its formal
affine map is

\[
F_V(x)=\frac{a x+C}{b},\qquad
a=3^s,\quad b=2^L,\quad C\in\mathbb N_0.
\]

Put

\[
D=b-a\ne0,\qquad \xi=C/D,\qquad \Delta_V(x)=Dx-C.
\]

The two branch maps have positive slopes and nonnegative translations.
Final integrality of a prescribed binary word at an integer input forces
every intermediate prescribed parity to be correct: after the first wrong
parity, its numerator is odd over two, and each later branch leaves an odd
numerator over a strictly larger power of two. It can never become integral.
Thus a positive integral fixed point of a block is an actual positive cycle.

For \(e\) legal repetitions from \(x\) to \(y\), the exact identity is

\[
b^e\Delta_V(y)=a^e\Delta_V(x).
\tag{2}
\]

Since \(a,b\) are coprime,

\[
\boxed{2^{Le}\mid\Delta_V(x).}
\tag{3}
\]

If \(\Delta_V(x)\ne0\), this gives the full repetition budget

\[
2^{Le}\le|\Delta_V(x)|
\le (|D|+C)(x+1).
\tag{4}
\]

There is no restriction on \(e\), the valuation pattern inside \(V\), or
the sign of \(D\). Equation (3) includes the entire dyadic clock.

If instead \(\Delta_V(x)=0\), the block itself fixes the incoming positive
integer. It is an actual cycle with minimal shortcut period dividing \(L\).
Once the supplied path reaches that state, determinism keeps it on this
cycle. In a closed ordinary path, the initial source belongs to the same
cycle. This case is a finite, explicitly identifiable output of the
classifier, not an exception discarded from the proof.

## 3. A full-clock budget for any finite concatenation

Let

\[
K=\max\left(1,\max_i(|2^{L_i}-3^{s_i}|+C_i)\right).
\]

Suppose none of the active repeated blocks fixes its incoming state. Write
\(x_i\) for the successive boundaries and \(t_i=L_i e_i\) for their
shortcut clocks. By (4),

\[
2^{t_i}\le K(x_i+1).
\tag{5}
\]

Every exact shortcut branch on a nonnegative integer satisfies
\(T(x)+1\le2(x+1)\). Iterating gives

\[
x_{i+1}+1\le2^{t_i}(x_i+1).
\]

Hence, with \(Y_i=K(x_i+1)\),

\[
Y_{i+1}\le Y_i^2,
\qquad Y_i\le Y_0^{2^i}.
\]

Multiplication of (5), with \(A=\sum_i t_i\), proves

\[
\boxed{2^A\le[K(x_0+1)]^{2^r-1}.}
\tag{6}
\]

Here \(r\) may be replaced by the number of active pieces. Keeping the
original \(r\) only enlarges the right side. This statement holds for
ordinary open paths as well as cycles. The formal theorem `full_clock_budget`
checks it for arbitrary lists of supplied words and arbitrary repetition
counts; no finite word census is used.

## 4. Rotating an arbitrary exponent vector

Assume the supplied nonempty word is a positive cycle. Its complete
multiplier is

\[
M=\prod_i\mu_i^{e_i}=3^S/2^A<1,
\qquad \mu_i=3^{s_i}/2^{L_i},
\]

where \(S\) is the total odd count. Positivity of the complete translation
forces the displayed strict inequality.

For this particular exponent vector, choose a minimum among the prefix
products of the active multipliers, including the empty prefix but excluding
the full product, and rotate the block list to begin there. Every suffix
product in the rotated list is at most one. To see this, write the unrotated
prefix products \(P_j\), with the selected \(P_j\le1\). Before wrapping,
a rotated prefix has ratio \(P_i/P_j\ge1\), except that the full original
prefix gives \(M/P_j\ge M\); after wrapping it has value
\(MP_i/P_j\ge M\). Divide \(M\) by these rotated prefixes.

The rotation may depend on \(e\), unlike PR185's fixed linear-parameter
rotation. There are only finitely many rotations, and the constants below
are invariant under rotation.

Let \(R_i\) be the suffix product beginning at block \(i\), with
\(R_{r+1}=1\). Exact affine composition gives complete translation

\[
N=\sum_{i=1}^r\xi_i(R_{i+1}-R_i).
\]

Consequently

\[
0<N\le B:=2\sum_{i=1}^r|\xi_i|,
\qquad
\boxed{x_0=\frac{N}{1-M}\le\frac{B}{1-M}.}
\tag{7}
\]

No individual factor of the cycle denominator has been substituted for the
complete denominator \(2^A-3^S\). Intermediate boundaries can be much larger
than \(x_0\); the quadratic propagation in Section 3 explicitly pays for
that possibility.

## 5. An explicit cutoff using a two-logarithm estimate

Use constants \(c\in(0,1]\) and an integer \(\kappa\ge1\) satisfying

\[
1-3^S/2^A\ge c A^{-\kappa}
\quad(1\le S\le A,\ 3^S<2^A).
\tag{8}
\]

Such effective constants follow from Matveev's published Corollary 2.3.
This is the only external theorem needed for the classifier. It is not
installed as a Lean axiom.

For a concrete deliberately loose instantiation, one may take
\(\kappa=2\cdot10^9\) and \(c=2^{-(2\kappa+2)}\). Indeed apply that
corollary over \(\mathbb Q\) to \(A\log2-S\log3\), with algebraic
height bounds 1 and 2. Its constant is below \(\kappa\), since
\(e\,30^5\,2^{7/2}\cdot2<1.8\cdot10^9\). Its coefficient parameter
may be taken as \(A\). The result is
\(A\log2-S\log3>e^{-\kappa}A^{-\kappa}\). The inequality
\(1-e^{-u}\ge\min(1/2,u/2)\), followed by \(e<4\), gives (8) with
the stated smaller rational \(c\). The numeric constants are not intended
for practical enumeration.

Choose an integer \(b\ge0\) such that

\[
K(1+B/c)\le2^b,
\qquad E=2^r-1,\quad P=\kappa E,\quad Q=bE.
\]

Equations (6)--(8) give

\[
2^A\le2^Q A^P,
\qquad A\le Q+P\log_2 A.
\tag{9}
\]

For \(A\ge16\), \(\log_2 A\le\sqrt A\). Thus if
\(A\ge4Q\) and \(A\ge16P^2\), the right side of (9) is at most
\(A/2\), a contradiction. Therefore every realization not already lying
on a template cycle has

\[
\boxed{
A<N:=\max(16,4b(2^r-1),16\kappa^2(2^r-1)^2).
}
\tag{10}
\]

All constants are computable from the supplied blocks. Enumerate the
finitely many tuples with \(\sum_i L_i e_i<N\), discard the empty word,
and test its entire quotient

\[
\frac{C_{W(e)}}{2^{|W(e)|}-3^{\#1(W(e))}}
\]

for positive integrality. Replay every positive integer result and record
its minimal cycle. Add every positive integer template fixed point
\(\xi_i\) and its replay. The resulting finite cycle list is complete.

To recognize all exponent tuples for a listed cycle, take the union over
every possible initial phase of that cycle, retaining the selected phase
in the finite state. Add a failure state and a flag that rejects the
all-zero exponent tuple. Each block acts by the actual prescribed parity
path, or reaches failure at the first mismatched parity. Its \(e_i\)-fold
action is a power of this finite transition map. Acceptance requires a
nonempty input and return to the selected initial cycle state. This gives
an exact finite-state description, and hence
an effective eventually periodic description in each exponent coordinate.
It handles unbounded trivial-cycle repetitions and any supplied nontrivial
template cycle honestly.

## 6. Uniformity in block contents and the actual missing bound

The argument is also uniform over all blocks of length at most \(\ell\).
Their translations satisfy \(C_V\le3^{|V|}-2^{|V|}\), by induction using
the all-odd word as the maximum. Thus one may use

\[
K=2\cdot3^\ell,
\qquad B=2r3^\ell.
\]

With the explicit constants from Section 5, it suffices to choose

\[
b=2\kappa+5+4\ell+\lceil\log_2 r\rceil.
\tag{11}
\]

Indeed \(K(1+B/c)\le6r9^\ell/c\le2^b\). Therefore (10) applies even
when the blocks vary from one candidate to the next, provided their number
and maximum lengths have the stated bounds. A primitive cycle longer than
\(\ell\) cannot encounter the fixed-block degeneracy.

The remaining global assertion would have to control the description of
*every* possible cycle or a fixed-source escaping trajectory. For example,
with bounded block length, a cycle decomposition with
\(r\le(1/2-\varepsilon)\log_2 A\) for a fixed \(\varepsilon>0\)
would eventually contradict (10). No such
upper bound has been proved. Allowing a separate arbitrary block for each
step gives \(r=A\), which is fully compatible with (10).

The forced marked band supplies no finite-prefix complexity restriction by
itself. For every binary word of length \(A\) beginning with an odd branch,
there is a unique source residue modulo \(2^A\) carrying that exact shortcut
prefix. This is the classical finite parity-cylinder bijection. For any
fixed desired nonzero ternary residue, combine it by CRT with that residue.
Whenever

\[
d\ge70,\qquad 3\cdot2^A(d+1)\le70\cdot2^d,
\tag{12}
\]

the interval beginning at \(2^d\) of length \(3\cdot2^A\) contains such
a representative. It is positive, odd, in the desired ternary unit class,
lies below \(2^{d+1}\), and satisfies
\((d+1)(n-2^d)\le70\cdot2^d\). Thus the marked band admits every
finite odd-starting parity pattern, through clocks almost equal to the
source bit length. This statement concerns arbitrary marked inputs; it does
not assert that every such pattern closes to a positive cycle.

Consequently a closing argument must use additional information linking
successive returns of the *same* ordinary source. Merely combining markedness
with the finite block classifier does not provide that missing upper
description bound.

## 7. Prior work and evidence

- **PR185**, commit `276be8154f4e867acc0230466b34d9cb224aacf5`,
  `research/whole-repo-closure-20261122/EFFECTIVE_FIXED_BLOCK_CYCLES.md`:
  provides the fixed linear-parameter classification, the rotation idea,
  and the repeated-block divisibility identity. Here the exponent tuple is
  independent, the rotation depends on that tuple, and logarithm separation
  replaces the one-parameter power-sum cutoff.
- **Matveev (2000), Corollary 2.3**, journal page 1219:
  [primary publisher PDF](https://www.mathnet.ru/links/95cd0c82966e868aa656d4b19b4003ea/im314_eng.pdf).
  The statement and coefficient convention were inspected directly. The
  explicit instantiation in Section 5 is this note's elementary consequence;
  the external theorem is not formalized here.
- **Simons--de Weger**, author revision 1.43 (2007), Sections 5--6:
  [primary author PDF](https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf).
  Effective fixed-local-minimum cycle finiteness and the logarithm-separation
  mechanism are established prior work. A repeated block with several
  internal alternations can create arbitrarily many local minima, so the
  present description parameter is different. No claim of a new general
  transcendence mechanism or a stronger numerical cycle bound is made.
- **Weaver, “Height and periodic-dictionary complexity for rational Collatz
  trajectories,” rStation paper 15, v2, 2026-10-27**:
  [primary author text](https://rstation.ai/problems/collatz/papers/15).
  This recent, source-qualified preprint states stronger arbitrary-dictionary
  lower bounds and charges an adaptive dictionary's total division budget.
  Its elementary Section 3 already gives periodic divisibility and repeated
  height propagation. Its full proof has not been independently replayed in
  this checkpoint; it is not an input to the classifier above. The present
  result should be described as an explicit elementary classifier and Lean
  arithmetic kernel, not as novel dictionary-complexity finiteness.

[BlockRepetitionBudget.lean](lean/BlockRepetitionBudget.lean) proves 12 public lemmas/theorems: exact affine
defect transport, coprime reserve division, the actual branch-word affine
identity and growth bound, their repetition bridges, the nonfixed reserve
height bound, and (6). Its definitions keep the nonfixed-block hypothesis
visible. The complete classifier (10), its finite automaton output, and the
CRT observation (12) are written proofs. Neither full cycle exclusion nor
exclusion of escape follows, and neither is asserted.
