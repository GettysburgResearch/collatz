# Full-denominator capacity of arbitrary block mixtures

23 November 2026. **Status: proved written class exclusion, with an
all-length smooth-gap specialization checked in Lean. Full integer-cycle
exclusion and Collatz remain OPEN.**

This continuation starts from PR177 at
`f47a5ec51aa5853f104013a6d5046d6220ff7423`. The preceding positive-carry
energy attempt could not separate the rational words
`11101010(11011010)^(k-1)`. The present argument excludes **every arbitrary
concatenation** over those two blocks as an integer cycle, and then proves
an unbounded family theorem for arbitrary block lengths and dictionaries.
It uses the original full numerical closing denominator, all block cuts,
and the minimum ordinary boundary state. No finite period cutoff, assumed
Collatz verification range, or logarithmic-form conjecture is used.

## 1. The equal-shape block interface

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

For a binary word B of length A and weight p, let C(B) be its complete
affine carry, so that its branch composition is

\[
f_B(x)=\frac{Px+C(B)}Q,\qquad P=3^p,\quad Q=2^A.
\tag{BC1}
\]

The chronological concatenation convention is

\[
C(FG)=3^{p(G)}C(F)+2^{|F|}C(G).
\tag{BC2}
\]

Fix any finite dictionary of distinct words with these same A,p, where
A,p are positive. Let its carries lie in an interval of width
\(\Delta=C_{\max}-C_{\min}>0\), and let G>0 be any common divisor of
their differences. Taking their exact gcd gives the strongest form below.

Consider an arbitrary nonempty cyclic concatenation of N dictionary
blocks. A positive integer realization has positive ordinary boundary
states \(x_i\) and the literal equations

\[
Qx_{i+1}=Px_i+C_i\qquad(i\bmod N).
\tag{BC3}
\]

Throughout (BC5)--(BC13), "integer cycle" and "integer boundary cycle"
mean positive integer states in this interface. No signed-cycle
exclusion is claimed by the written note.

If Q<P, every block strictly increases its positive source, so such a
positive cycle is impossible. Hence only Q>P needs consideration. Put

\[
D_N=Q^N-P^N>0,\qquad
S_N=\sum_{j=0}^{N-1}Q^jP^{N-1-j},\qquad
D_N=(Q-P)S_N.
\tag{BC4}
\]

These are the **complete** denominator and geometric sum. The main
argument does not replace D_N by one cyclotomic factor.

## 2. Complete-denominator capacity theorem

**Theorem BC5.** If the boundary cycle (BC3) is nonconstant, then

\[
\boxed{
\Delta\ge(P+Q)\frac{G}{\gcd(G,D_N)}.
}
\tag{BC5}
\]

The statement permits repeated boundary states, repeated block types,
arbitrary N, and an arbitrarily large dictionary. A constant boundary
cycle has all used carries equal to \((Q-P)x\); for actual parity blocks
it simply repeats the one block emitted by that state.

**Proof.** Unroll (BC3) at each cyclic cut i:

\[
D_Nx_i=\sum_{j=0}^{N-1}Q^jP^{N-1-j}C_{i+j}.
\tag{BC6}
\]

Since every C_j is congruent to one fixed C_0 modulo G, the right side
is congruent to \(C_0S_N\), independently of i. Subtraction at two cuts
therefore gives

\[
G\mid D_N(x_i-x_j).
\]

Let \(g=\gcd(G,D_N)\) and \(d=G/g\). Cancelling the gcd in this integer
divisibility shows

\[
\boxed{d\mid x_i-x_j\quad\text{for every }i,j.}
\tag{BC7}
\]

Choose the minimum boundary value m. Since the cyclic boundary sequence
is nonconstant, some edge enters a run of values m from a value greater
than m, and some edge leaves a run of values m for a value greater than m.
These need not be adjacent edges or the same visit to m. By (BC7), write
their other endpoints as \(m+da\) and \(m+db\), with a,b>=1. Their
incoming and outgoing carries are

\[
C_-=(Q-P)m-Pda,\qquad C_+=(Q-P)m+Qdb.
\]

Consequently

\[
\Delta\ge C_+-C_-=d(Pa+Qb)\ge d(P+Q),
\]

which is (BC5). This avoids silently assuming a primitive boundary
period. \(\square\)

### Uniform all-period consequence

Write the 6-smooth part and the part coprime to six of a positive G as

\[
G_{\{2,3\}}=2^{v_2(G)}3^{v_3(G)},\qquad
G^{(6)}=G/G_{\{2,3\}}.
\]

Because D_N is coprime to six,
\(\gcd(G,D_N)\le G^{(6)}\). Theorem BC5 therefore implies

\[
\boxed{
\frac{\Delta}{G_{\{2,3\}}}<P+Q
\quad\Longrightarrow\quad
\text{every integer boundary cycle is constant.}
}
\tag{BC8}
\]

This excludes all nonconstant boundary cycles simultaneously, for every
N and every ordering and frequency of the dictionary blocks. It does
not exclude a constant boundary cycle of one dictionary block unless
that block's fixed point is separately shown nonintegral or trivial.

## 3. Two arbitrary blocks: no mixed cycle below the carry threshold

For two distinct equal-shape blocks B_0,B_1, set
\(\delta=|C(B_1)-C(B_0)|\). Here \(G=\Delta=\delta\). A cyclic
concatenation using both blocks has a nonconstant boundary cycle, since
a constant boundary value would force both carries equal. Thus

\[
\boxed{
\text{mixed integer cycle}\quad\Longrightarrow\quad
\gcd(\delta,Q^N-P^N)\ge P+Q.
}
\tag{BC9}
\]

In particular,

\[
\boxed{
\delta^{(6)}<2^A+3^p
\quad\Longrightarrow\quad
\text{no mixed integer cycle at any block period}.
}
\tag{BC10}
\]

This is stronger than just excluding smooth carry differences. The
full period-dependent condition (BC9) can still apply when (BC10) does
not: every admissible block period must make a divisor of delta of size
at least P+Q divide the original full D_N.

For example `11111000` and `11110001` have A=8,p=5 and carries 211,323.
Their difference is \(112=2^4\cdot7\), so the surviving part is 7,
below \(256+243=499\). Every mixed concatenation is excluded without
enumerating the number of switches or the block period.

### Smooth-gap proof with no minimum-state argument

When \(\delta=2^u3^v\), a shorter proof also works directly on the full
cycle equation. Let epsilon_j indicate the larger carry and let

\[
E_N=\sum_{j<N}Q^jP^{N-1-j}\epsilon_j.
\]

Then

\[
C(W)=C(B_0)S_N+\delta E_N,
\qquad 0<E_N<S_N
\tag{BC11}
\]

for a mixed word. The integer cycle equation gives
\(S_N\mid\delta E_N\). But
\(S_N\equiv P^{N-1}\pmod2\) and
\(S_N\equiv Q^{N-1}\pmod3\), so S_N is coprime to delta. Hence
\(S_N\mid E_N\), contradicting the strict inequalities.

This entire all-length argument is the specialization checked by
[BlockMixture.lean](BlockMixture.lean). Its closed-path theorem retains
literal integer block equations, rather than assuming a merely formal
parity word is an ordinary orbit.

## 4. Unbounded contexts and run transpositions

If equal-shape blocks B_0,B_1 are put in the same prefix F and suffix H,
their carry difference becomes

\[
\delta'=2^{|F|}3^{p(H)}\delta.
\tag{BC12}
\]

Its part coprime to six is unchanged, whereas the new threshold
\(2^{A+|F|+|H|}+3^{p+p(F)+p(H)}\) is at least the old threshold.
Therefore every exclusion (BC10) survives arbitrary common contexts.
This covers unbounded block length, not only arbitrarily long repetition
of two fixed short blocks.

For the whole dictionary, both Delta and G acquire the same smooth
factor in (BC12), so \(\Delta/G_{\{2,3\}}\) is unchanged. Thus (BC8)
also survives arbitrary common contexts. For each fixed equal-shape
dictionary, sufficiently long common contexts make (BC8) hold. This is
a rigidity statement about possible mixed boundary cycles; it does not
decide the individual contextual block's own fixed point.

Three explicit unbounded families follow.

1. **Adjacent transposition.**
   \(B_0=F10H\), \(B_1=F01H\) have
   \(\delta=2^{|F|}3^{p(H)}\). No mixed integer cycle is possible.
2. **One odd symbol across any zero run.** For k>=1, the cores
   \(10^k\), \(0^k1\) have carry difference \(2^k-1\). Its
   6-free part is smaller than \(2^{k+1}+3\), so arbitrary common
   contexts and arbitrary mixed concatenations are excluded.
3. **One zero symbol across any odd run.** For k>=1, the cores
   \(1^k0\), \(01^k\) have carry difference \(3^k-2^k\), smaller
   than \(3^k+2^{k+1}\). The same conclusion follows.

No balanced or Christoffel hypothesis appears in these mixed-language
theorems. In particular, no assertion that an arbitrary cycle is balanced
is used to transfer an existing high-cycle exclusion.

## 5. The previous positive-carry obstruction language is entirely nonintegral

Take

\[
U=11101010,\quad V=11011010,\quad
(A,p,P,Q,C(U),C(V))=(8,5,243,256,283,319).
\]

Their carry difference is \(36=2^2 3^2\), so all mixed concatenations
are excluded by (BC10) or the Lean-checked smooth-gap argument. Pure
concatenations repeat the fixed points \(283/13\) or \(319/13\), both
nonintegral. Therefore

\[
\boxed{
\text{every nonempty cyclic word over }\{U,V\}
\text{ is nonintegral.}
}
\tag{BC13}
\]

This removes the entire arbitrary-switch language that contained the
old local-energy obstruction, not just the previously analyzed words
\(UV^{k-1}\). The rational cycles still exist and can stay above 21;
their existence is exactly why the preceding local energy separation
could fail even though the full integer arithmetic excludes them.

There is also direct ordinary descent for finite realized U/V paths.
The legal source residues modulo 256 are 199 for U and 123 for V.
Thus every positive ordinary block source is at least 123, and

\[
256(x-x')=13x-C_B\ge13\cdot123-319=1280.
\]

Every complete block lowers its actual source by at least five. This
does not by itself claim that the point reached after leaving this
language converges under the unrestricted map.

## 6. Sharp controls and exact remaining scope

The P+Q threshold is sharp for general affine integer block systems.
For P=3,Q=4, the carries 1 and 8 give the positive two-state cycle

\[
4\xrightarrow{C=8}5\xrightarrow{C=1}4.
\]

Here delta=7, D_2=7, and gcd(delta,D_2)=P+Q. These carries are not those
of two actual length-two weight-one Collatz words, whose carries are
1 and 2. This is a control on the algebraic theorem, not a Collatz
counterexample. It shows that discarding the gcd or replacing a strict
exclusion threshold by a weak one would be false.

The single-symbol run results must not be extended to moving a symbol
across an arbitrary mixed word without another argument. For
\(B=000011110\), the two words 1B and B1 have length 10, weight 5,
carry difference 1471, and threshold \(1024+243=1267\). The 6-free
carry criterion does not apply. This is a failure of that attempted
coverage inference, not an integer cycle.

The full theorem still needs an argument covering an arbitrary putative
cycle's word. Such a word need not decompose into a dictionary with a
common length and weight satisfying (BC8). The arbitrary-shape two-block
extension being developed in the coordinating lane has its own boundary.
No universal decomposition or all-cycle exclusion is asserted here.

## 7. Formal and computational evidence

The standalone Std-only [Lean source](BlockMixture.lean) proves eight
public declarations, including:

- exact affine composition of arbitrary closed integer block paths;
- arbitrary-length decomposition (BC11);
- the no-mixed-cycle theorem under coprimality of S_N and delta;
- coprimality for every 6-smooth delta and every positive A,p,N;
- the resulting unbounded closed-path exclusion.

The general G/gcd(G,D_N) minimum-state theorem, the nonsmooth criterion,
and the contextual/run-family interpretations are written mathematics.
They are not counted as additional Lean theorems.

The small [exact checker](block_carry_capacity_check.py) checks the
literal carry identities, all mixed U/V schedules through a stated
finite depth, selected nonsmooth and contextual cases, nonvacuous
general affine cycles, and the sharp threshold countercontrol. Its
finite executions are checks of the formulas and implementation; the
all-parameter statements above follow from the proofs and the scoped
Lean theorem, not extrapolation from a census.

## 8. Source and overlap boundary

- The classical affine carry and chronological concatenation identities
  are explicitly given in Halbeisen--Hungerbuehler, *Optimal bounds for
  the length of rational Collatz cycles*, Section 2, equations (3)--(4)
  and Lemma 2. The [primary author PDF](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf)
  was read. The present minimum-residue argument is derived above.
- The existing balanced/high-cycle exclusion is not claimed as new.
  Our frozen parent already discusses it in `HIGH_VARIANCE_ARITHMETIC.md`.
- For overlap, the primary manuscript
  [*Collatz cycles whose parity word has two periodic stretches*](https://rstation.ai/problems/collatz/papers/57)
  (29 October 2026, v1), especially Sections 2 and 5, was inspected.
  It treats two stretches and bounded/general stretch constraints with
  possibly different block slopes. The present equal-shape condition
  permits arbitrarily many switches and uses a different common-carry
  residue argument. No claim of complete literature priority is made,
  and none of that manuscript's numerical exclusions is imported.
- PR182 at `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`,
  `research/literature-round4-20261123/CYCLE_RIGIDITY.md`, was flagged
  by the coordinating agent for the full-denominator cut-determinant
  interface. This note supplies its own algebra and does not inherit a
  review verdict for that packet.
