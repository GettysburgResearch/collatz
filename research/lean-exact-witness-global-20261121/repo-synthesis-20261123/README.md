# Ordinary basin packing, infinite-word descent, and complete joint edits

23 November 2026. **Full Collatz and the original residue-512 implication
remain OPEN.** This checkpoint began with a repository-wide orientation
and three parallel attacks on the remaining construction, escape, and cycle
steps. Its main new connection is an unconditional power saving for the
number of disjoint sibling basins with a small ordinary source. That
supplies a strictly stronger pressure theorem on the same original
component. The other two attacks prove all-time descent for an infinite
word language and complete finite search for arbitrary bounded joint edits.

[Repository synthesis](REPOSITORY_SYNTHESIS.md) ·
[Source inventory and execution](../../../reports/lean-exact-witness-global-20261121/repo-synthesis-20261123/README.md) ·
[Previous checkpoint](../universal-step-20261123/README.md)

## 1. A new connection between short descent and sparse orbit roots

Let \(q_j=U^j(q_0)\) be one injective positive odd unit orbit and put
\(S(q)=64q+21\). For **every** \(j\ge0,b\ge1\), take the minimum
\(m_{j,b}\) of the full positive shortcut predecessor basin of
\(S^bq_j\). These basins are pairwise disjoint. The new theorem is

\[
\boxed{\#\{(j,b):m_{j,b}\le X\}\le12X^{799/800}.}
\]

The proof has a finite ordinary source split. If a basin minimum descends
within \(H\) shortcut clocks, it must have visited its designated root
first. Its root is therefore at height at most \((3/2)^H(X+1)\), where
the existing sparse-orbit count applies. Otherwise its actual parity word
belongs to the short-horizon no-descent count. Choosing
\(H=\lfloor\log_2X/25\rfloor\) gives the displayed strict power saving.
No basin is replaced by an injective orbit, and no predecessor-population
or random-parity premise is used.

A separately scoped sharper version uses the existing critical whole-orbit
estimate. With \(\theta=H_2(\log_3 2)\), it gives

\[
\#\{(j,b):m_{j,b}\le X\}
=O\!\left(\frac{X^\eta}{\sqrt{1+\log X}}\right),\qquad
\eta=1-\frac{(1-\theta)^2}{1-\theta+\theta\log_2(3/2)}
\approx0.99586542.
\]

[Complete source-preserving proof](escape/SPARSE_BASIN_MINIMA.md).
The elementary \(799/800\) version suffices for the following result.

### Critical roots of the actual Green ratios are summable

On a hypothetical escaping unit component, retain the actual positive
pressure weight

\[
r(n)=\frac1n\prod_{k\ge0}\frac{3U^kn}{3U^kn+1}
\]

and the unchanged inverse operator
\(P_sf(q)=\sum_e(3/2^e)^s f((2^eq-1)/3)\), over actual positive odd
unit parents. Write \(Z_s=\sum_{k\ge0}P_s^k1\). For every \(s>1\),

\[
\boxed{\sum_{j\ge0}\sum_{b\ge1}64^{-b}
\left(\frac{Z_s(S^bq_j)}{Z_s(q_j)}\right)^{1/s}<\infty.}
\]

In particular,

\[
\boxed{\sum_{j\ge0}\sqrt{\frac{Z_2(64q_j+21)}{Z_2(q_j)}}<\infty.}
\]

The earlier packet proved summability of the ratios. The roots are a
strictly stronger conclusion. The new ingredient is the number of basins
that meet a low source range. If \(b_i\) are their actual \(s\)-masses,
their decreasing rearrangement now obeys

\[
b_N^*=O_s\!\left(N^{-\kappa_s}\right),\qquad
\kappa_s=1+\frac{s-1}{799/800}>s.
\]

An explicit dyadic-shell argument proves every power sum above
\(1/\kappa_s\), including the previously missing critical power \(1/s\).
The same minimum count gives \(\sum_{j,b}1/m_{j,b}\le9600\), and hence
the same bound for any choice of one ordinary ancestor from each basin.

[Complete packing and pressure proof](escape/BASIN_PRESSURE_PACKING.md).
It also states the weaker Green lower comparison that would now exclude
escape, and the exact integer-height cost of the existing inverse-tree
compiler. That comparison and the required low-cost ordinary repair remain
open. This is an unconditional necessary theorem about any hypothetical
escape, not an assertion that escape exists.

### The complete inverse kernel is retained too

The [all-branch extension](escape/ALL_BRANCH_CAPACITY.md) proves the exact
partition of the component into the initial predecessor basin, later ray
atoms, and every off-ray parent basin. The same argument gives at most
`64 X^(799/800)` such basins meeting the low source range. If
\(A_s(q)=\sum_{U^k n=q}r(n)^s\), with each actual ancestor counted once,
then the complete ordinary capacity increments satisfy

\[
\boxed{\sum_{j\ge0}
\bigl(A_s(q_{j+1})-A_s(q_j)\bigr)^{1/s}<\infty.}
\]

This includes the new root atom, lower-exponent parents, both legal
ternary colours, and every larger inverse exponent. It is a written
all-branch theorem; the finite formal core is reused at its displayed
scope. No chronological decay rate or lower Green comparison is inferred.

## 2. All-time descent with independently unbounded repetition counts

Fix a contracting actual parity word
\(F_u(x)=(Px+C)/Q\), \(d=Q-P>0\). Allow any indexed family of defect
words \(F_{t_i}(x)=(R_ix+B_i)/S_i\), and put
\(E_i=dB_i-(S_i-R_i)C\). Suppose one \(K\ge1\) satisfies

\[
\boxed{R_iP^K+|E_i|<S_iQ^K\quad\text{for every allowed defect}.}
\]

For any actual positive ordinary infinite path with complete tail

\[
u^{k_0}t_{i_0}\,u^{k_1}t_{i_1}\cdots,\qquad k_j\ge K,
\]

the boundary displacement \(h_j=(d x_j-C)/Q^K\) is an integer and
satisfies

\[
|h_j|\le\max(|h_0|-j,0).
\]

Thus every boundary eventually equals \(C/d\). If that number is not a
positive integer, the whole infinite language has no ordinary realization.
Otherwise the orbit reaches its actual \(u\)-cycle. The run lengths,
defect labels, and number of defects can change without bound; even an
infinite defect dictionary is permitted under the uniform certificate.

For example, **no positive integer** has a complete tail
\((100)^{k_0}1(100)^{k_1}1\cdots\) with all \(k_j\ge1\).
The exact cutoff is \(15<16\), and its center is \(1/5\).
For \(u=10\), every defect word of length at most \(B\ge1\) is covered
by \(K=2B\); such an actual complete tail reaches 1.

[Proof and full scope](cycles/INFINITE_DICTIONARY_DESCENT.md).
The Lean theorem `ordinary_word_language_hit` consumes literal positive
parity traces and proves the all-time explicit boundary clock. Universal
coverage by this language is not asserted.

## 3. A complete bounded-edit merger compiler

For positive starts \(x,y<2^N\), allow matching shortcut branches at zero
cost and a step on either trajectory alone at cost one. For **every**
first-merger alignment with at most \(t\) such edits, all alignment
columns and both ordinary clocks are at most

\[
\boxed{N(2^t-1).}
\]

A common run of length \(k\) forces \(2^k\mid x-y\). One edit can
replenish the binary precision but at most doubles the current bit budget.
Induction pays for every common run, insertion, deletion, and change of
difference sign. The executable compiler is sound and complete for the
entire prescribed edit budget, without a guessed time bound. Rejection
excludes all larger-clock attempts at that budget too.

Given the complete input tuple for \(y\), acceptance emits a complete
tuple for odd \(x\), with output shortcut clock at most
\(2N(2^t-1)+L\), where \(L\) is the supplied input's terminal exponent.
Arbitrary terminal padding is supported.

The original-class pair \(y=385,x=193\) shows that the input's own
clock need not fund the number of edits: its supplied clock is 23,
whereas the exact minimum edit count is 39, even allowing unlimited
terminal-cycle padding. Independent algorithms reconstructed that optimum
on the complete 1,848-state ordinary orbit product.

[Proof, executable command, and complete tuple consumer](candidate/JOINT_EDIT_COMPILER.md).
Universal selection of a successful edit budget remains open; an outer
unbounded search is not presented as a terminating proof.

## 4. Evidence and remaining full-theorem step

The new source files, exact inventories, internal reconstruction reviews,
and actual execution receipts are linked from the
[report](../../../reports/lean-exact-witness-global-20261121/repo-synthesis-20261123/README.md).
The first two Lean modules use core/Std; the finite pressure module uses
the explicitly pinned Mathlib build. The infinite real-analysis portions
are distinguished from those formal declarations. Existing frozen proof
files remain unchanged.

The repository review covered all 145 PR metadata records, the complete
main tree, the integrated catalog and errata, and selected live proof
files. It was an orientation and synthesis, not a claim of rechecking
every historical proof.

The original implication still needs a construction from the unrestricted
input tuple to a universally successful target certificate. The new merger
compiler fully decides each prescribed edit budget. The escape route still
needs an ordinary lower comparison or a sufficiently small integer repair;
the all-time lattice theorem still needs coverage of other itineraries.
None of these remaining assertions is hidden as a Lean axiom.
