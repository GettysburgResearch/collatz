# Exact closing interfaces for localized five energy

**PROPOSED elementary identities and a closing-attempt ledger.** The
latest ordinary localization theorem aligns exactly with the renewable
domain, but composing its inverse weights with renewal gives an identity,
not strict energy loss. No absolute finite-energy bound is obtained.

Use the notation `f,e,E_s,H,R_12,J` of
[EXPANDED_FIVE_RENEWAL.md](EXPANDED_FIVE_RENEWAL.md), SHA-256
`3589ca1bcf2533bc7cbd427feb0d8f830cc077c3a6e90d2a7abd6eeef3ffd70b`.
All labels are actual ordinary invariant labels. All source sums run over
positive odd ternary units; cutoffs always refer to the original source.

The new comparison source is PR146 at
`fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`,
"Transport both orbits into one residue class." No shifted-core theorem
is used as an input to the elementary identities below.

## CI1. An exact localization-renewal round trip

Let

\[
H_1=\{x>0:x\equiv49\pmod{64},\ 3\nmid x\}.
\]

This is exactly the `r=1` part of the old ladder, hence a subset of `H`.
For each positive odd ternary unit `q`, choose the unique `L_0` in
`[6,11]` with `2^L_0 q=7 mod9`. Among

\[
\frac{2^{L_0}q-7}{9},\qquad
\frac{2^{L_0+6}q-7}{9},
\]

choose the first ternary unit and call it `sigma(q)`. Their difference
is `7*2^L_0 q`, a ternary unit, so at least one is eligible. Both are
positive odd integers in `49 mod64`. The actual source word is
`(2,L-2)`, and its paired target word is `(5,L-5)`. Thus

\[
T^L\sigma(q)=q,\qquad T^L(5\sigma(q))=5q,
\qquad e(\sigma(q))=e(q),
\tag{1}
\]

\[
7q\le\sigma(q)<Kq,\qquad K=2^{17}/9.
\tag{2}
\]

The map `sigma` is injective because `U^2(sigma(q))=q`. These are
the physical lift and constant in the pinned PR146 result.

For `s>0` put

\[
r_q=(q/\sigma(q))^s>0.
\]

The selected inverse-fiber contribution is exactly

\[
\sigma(q)^{-s}e(\sigma(q))
=r_q q^{-s}e(q).
\tag{3}
\]

Localization back to the endpoint uses the inverse factor `r_q^(-1)`:

\[
\boxed{
q^{-s}e(q)
=r_q^{-1}\sigma(q)^{-s}e(\sigma(q))
=r_q^{-1}r_q q^{-s}e(q).}
\tag{4}
\]

This identity holds term by term and hence on every finite set of
endpoints. At a potentially contributing endpoint `q>=5`, if `k_s(q)`
is the full positive inverse-fiber kernel for `H_1`, it contains this
selected source, so

\[
k_s(q)\ge r_q,
\qquad r_q^{-1}k_s(q)\ge1.
\tag{5}
\]

Other eligible inverse sources add nonnegative mass. Thus this particular
localization followed by its full inverse-fiber estimate cannot produce
a strict coefficient below one, even when the weights and endpoint
residues are retained exactly. It is a statement about this composition;
it does not exclude an estimate exploiting which defects arise from an
actual invariant label.

The coarse cutoff version makes the same limitation visible. If a
label-blind kernel bound gives
`E_(H1,s)(Y)<=C_s E_s(Y/7)`, then localization gives

\[
E_s(X)\le K^s E_{H_1,s}(KX)
\le K^s C_s E_s(KX/7).
\tag{6}
\]

Here `K/7=2^17/63>1`. For `q>=5`, moreover `C_s>=r_q` and `K^s r_q>=1`,
so `K^s C_s>=1`. The exact identities (3)--(5) explain this without
relying on the coarseness of the displayed constant. The known zero
endpoint `q=1` may be omitted throughout the renewal bound.

### The other sufficient progression lies in the uncovered remainder

The same pinned PR146 theorem gives bounded-distortion, injective
localization into

\[
S=\{x>0:x\equiv6375551795\pmod{2^{71}},\ 3\nmid x\}.
\]

Its first seven exact exponents are `(1,3,3,3,3,3,3)`. In particular
`S` is outside both the ladder (first exponent two) and the three new
four-input families (first two exponents one). Hence

\[
S\subseteq\{x\notin H:a(x)\le2\},\qquad E_{S,1}(X)\le R_{12}(X).
\tag{7}
\]

For each fixed `s>0`, that localization and ordinary inclusion prove

\[
E_s(\infty)<\infty
\quad\Longleftrightarrow\quad E_{S,s}(\infty)<\infty.
\tag{8}
\]

No absolute bound on the right side is provided. This identifies an
explicit portion of the remaining energy that already retains the
full finite-energy obligation. It is not an obstruction to proving
that obligation by some additional argument.

## CI2. The adjacent remainder has an exact converse comparison

For a high-valuation source, write `q=U(x)`, `a=v2(3x+1)>=3`.
The proof of ER4 identifies three labels:

\[
e(x)=d(f(5x),f(q)),\quad
e(q)=d(f(5q),f(q)),\quad
j_a(q)=d(f(5x),f(5q)).
\]

Besides ER4's inequality `e(x)<=e(q)+j_a(q)`, the triangle inequality
therefore gives

\[
j_a(q)\le e(x)+e(q).
\tag{9}
\]

At a contributing endpoint `q>=5`, all inverse exponents `a>=3`
form one progression of difference two, before deleting nonunit sources.
Their normalized harmonic sum is at most

\[
\frac{3}{2^{a_0}-1/q}\frac1{1-1/4}
\le\frac4{8-1/5}=\frac{20}{39}.
\tag{10}
\]

The omitted endpoint `q=1` has `e(1)=0`. Every such source has
`q<=x/2`, so positive summation of (9) gives

\[
J(X)\le E_{a\ge3,1}(X)+\frac{20}{39}E_1(X/2).
\tag{11}
\]

The source sets in `R_12` and `E_(a>=3,1)` are disjoint. Combining
(11) with ER4, and subtracting only at finite cutoffs, proves

\[
\boxed{
R_{12}(X)+J(X)\le\frac{59}{39}E_1(X),\qquad
E_1(X)\le8\,[R_{12}(X)+J(X)].}
\tag{12}
\]

Thus `R_12(infinity)+J(infinity)` is finite exactly when full harmonic
five energy is finite. This is a quantitative equivalence, with no
summability assumption used in deriving the finite-cutoff bounds.

## CI3. Why the shifted-core estimates do not supply the missing moment

Define the nonnegative charge on ordinary odd unit sources by

\[
\rho_f(x)=\begin{cases}
e(x),&x\notin H,\ a(x)\le2,\\
j_{a(x)}(U(x)),&a(x)\ge3,\\
0,&x\in H.
\end{cases}
\]

The cases are disjoint because every member of `H` begins with valuation
one or two. The missing estimate is exactly

\[
\sum_x\frac{\rho_f(x)}x<\infty.
\tag{13}
\]

Equivalently, setting `D_k(f)=sum_(2^k<=x<2^(k+1)) rho_f(x)`, it is

\[
\boxed{\sum_{k\ge0}2^{-k}D_k(f)<\infty.}
\tag{14}
\]

The two nonnegative sums differ by at most a factor two. For a Boolean
invariant label, `D_k(f)` is an actual count of nonzero residual charges
in a height interval.

The parallel `EXCURSION_FREQUENCY.md`, EF1--EF4, controls a different
quantity: outside-core visits indexed by time along one fixed ordinary
future. Its new superlogarithmic and iterated-logarithmic estimates are
lower bounds for that visit count on a nonperiodic orbit. They contain
neither a source-height distribution for (14) nor a bound on these label
differences. A pathwise frequency estimate does not become (14) by
changing its index from times to starting integers; the multiplicities
and the weights would require their own positive summation proof.

The parallel `FIXED_DEFECT_CORE_RETURNS.md`, FD1--FD3, does count
distinct canonical segments across all ordinary sources, with fixed
endpoint cores and a fixed defect count. To use that finite count here,
one must first assign the charges in (13) to such segments and then sum
over their endpoint cores and defect counts. Neither that assignment
with controlled congestion nor a summable bound for the unrestricted
core/defect sum has been proved. The S-unit theorem's solution count
does not supply a height distribution for its solutions.

Consequently the exact localization, recurrence, and renewal interfaces
leave the first missing estimate as (13), or equivalently (14). The
finite-energy rigidity implications retain the separate source-qualified
inputs stated in PR163; none of these comparisons establishes the
required finite energy or full Collatz convergence.

## CI4. The sparse sieve gives a positive row reduction, with a column gap

This is a **PROPOSED source-qualified consequence** of the explicit
all-discarded-index reduction and retained-set count in PR146 at the same
pin, `research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md`, and its
`check_least_failure_sieve.py::descent_dependencies`. The 71 directed
certificates and their height bounds are credited there to PR163,
`051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
`research/deep-reverse-closure-20261120/LEAST_FAILURE_HEIGHT.md`, H1--H2.
The source-qualified sparsity theorem is used as stated, not reproved here.

Write `X(k)=128k+1`, `Y(k)=64k+1`, and let `mathcal R` be the
retained eligible indices of that sieve; eligibility means `k>0` and
`4 not dividing k`. For an actual invariant label
`g:positive integers -> [0,1]` with `g(1)=1`, define

\[
\delta(k)=(g(X(k))-g(Y(k)))_+,
\qquad \mathcal D_s(X)=\sum_{\substack{0<k\le X\\4\nmid k}}
k^{-s}\delta(k).
\tag{15}
\]

The basin indicator `g=1_C` is one such label; then `delta` indicates
a failed directed comparison. For every discarded index, fix the actual
finite dependency list constructed in the pinned source. Let `N(k,j)`
be the number of occurrences of index `j` in that list, including all
repetitions. The construction gives

\[
N(k,j)>0\Longrightarrow j<5k/8,
\qquad \sum_j N(k,j)=O(\log(2k)).
\tag{16}
\]

**Row-reduction lemma.** Every discarded eligible index satisfies

\[
\boxed{\delta(k)\le\sum_j N(k,j)\delta(j).}
\tag{17}
\]

To prove this, follow the source's directed path from `Y(k)` through
its first violating ordinary iterate and the unit descent, ending at 1.
Ordinary edges in either direction preserve `g`. Each added adjacent
arrow is exactly `Y(j)->X(j)`, with positive label increment at most
`delta(j)`. Telescoping gives
`1-g(Y(k))<=sum_j N(k,j)delta(j)`. Since `g(X(k))<=1`, the left
side is at least `delta(k)`. This proves (17) for the actual invariant
label on every discarded source. It uses the explicit all-source
reduction, not an assumption that every smaller implication is already
true. Also `128j+1<5(128k+1)/8` implies `j<5k/8`, proving the
height assertion in (16) in the index coordinate.

### The retained charge is summable at its critical exponent

The pinned count has exponent

\[
p=\log_3 2,\qquad
\rho=-p\log_2p-(1-p)\log_2(1-p)=0.949955527\ldots<1.
\]

The number of retained indices in a dyadic height interval is
`O(2^(h rho) h^(-3/2))`. Since `0<=delta<=1`, their weighted
charge is bounded by a constant times

\[
\sum_{h\ge1}2^{h(\rho-s)}h^{-3/2}.
\tag{18}
\]

It follows that `mathcal D_(ret,s)(infinity)<infinity` for every
`s>=rho`, including `s=rho` itself. In particular harmonic retained
energy is finite. The count alone gives no such conclusion at `s=21/25`,
because `21/25<rho`. The matching lower cardinality estimate includes
an already solved comparison class, so it must not be relabeled as
divergence of the actual defect energy at a smaller exponent.

### The next missing lemma is a weighted column estimate

A sufficient operator bound would be

\[
\boxed{
\sup_{\substack{j>0\\4\nmid j}}
j^s\sum_{\substack{k\notin\mathcal R\\k>0,\;4\nmid k}}
k^{-s}N(k,j)\le C<1.}
\tag{19}
\]

If (19) were proved, positive summation of (17), retaining the actual
source cutoff and multiplicities, would give

\[
\mathcal D_s(X)\le\mathcal D_{\mathrm{ret},s}(X)
                      +C\mathcal D_s(5X/8),
\tag{20}
\]

and hence finite full directed adjacent energy for `s>=rho`. No bound
of the form (19) is established here. The number of queries in one
row and their smaller heights do not bound the sum of all incoming
weighted occurrences at a fixed column `j`. Termination of each finite
dependency tree does not bound the aggregate multiplicities of the trees
from all original sources. A support-sensitive substitute for (19) would
have to use actual invariant-label constraints explicitly.

There is a further propagation obligation: finite directed adjacent
energy must imply finite full five energy, or a direct rigidity theorem
must be proved for this one-sided adjacent quantity. The zero-defect
equivalence of criteria is not such an energy comparison. PR163 FE1
compares five energy to tripling energy with five energy on the right
and cannot be reversed to supply it.

Finally, using any successfully obtained harmonic five-energy bound for
global rigidity retains PR163 Section 4's named fixed-target
positive-lower-density input PD. The `21/25` rigidity route instead
retains its predecessor-moment input, but (18) does not provide the needed
retained moment at that exponent. Neither source-qualified implication
is promoted to an unconditional closing theorem. Equations (17) and
(19) isolate a concrete next analytic problem, beyond merely asking
again for an unspecified finite remainder.
