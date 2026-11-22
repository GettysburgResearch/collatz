# Independent power blocks: an effective cycle-classification argument

**Full Collatz: OPEN.** This is a literature-inspired attempt at the cycle
alternative, using the exact ordinary arithmetic already present in PR 183.
It removes the one-parameter restriction from PR 185's fixed-block cycle
schemas: the repetition counts below are independent nonnegative integers.
The result concerns any fixed finite list of blocks, and does not assert that
all Collatz cycles admit one common bounded-complexity description.

**Evidence:** `BlockCompression.lean` checks the finite ordinary compression
dichotomy and its primitive-cycle consumer. The effective cutoff and the
classification of all exponent tuples are complete written arguments using
Matveev's published Corollary 2.3. Matveev's theorem is not installed as a
Lean axiom. Compiler evidence is reported separately from the written result.

The map throughout is the ordinary shortcut map

\[
 T(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\
 (3x+1)/2,&x\equiv1\pmod2.\end{cases}
\]

## 1. The new target and its relation to the literature

Fix nonempty binary words \(V_1,\ldots,V_r\), and consider

\[
 W(\mathbf k)=V_1^{k_1}\cdots V_r^{k_r},
 \qquad \mathbf k\in\mathbb N^r,
 \qquad |W(\mathbf k)|>0. \tag{BC-1}
\]

The word specifies the complete parity itinerary of a proposed positive
cycle. In PR 185's frozen packet the exponents were affine functions of one
parameter. Here they can vary independently, with no ratio, ordering, or
common-growth hypothesis. The whole cycle equation is retained.

The mechanism combines two kinds of information:

1. A long exact repetition at an ordinary integer requires a large ordinary
   source, unless that source is already periodic with the atom's period.
2. A positive cycle with a long total period has a minimum bounded by a fixed
   power of that period, by a lower bound for the nonzero form
   \(N\log2-s\log3\).

The first statement can be chained across independently repeated mixed
blocks. This yields an exponential lower bound for the cycle minimum in
terms of its total period, with a constant depending on the number and length
of atoms. The second statement supplies a polynomial upper bound. Their
comparison gives an effective finite cutoff.

This is the same broad chaining-and-transcendence architecture used by
Simons–de Weger [SdW05, Lemmas 6–7 and Theorem 3], building on the earlier
cycle work of Steiner and Brox. We do **not** claim fixed-\(m\)-cycle
finiteness as new. Their \(m\) counts local minima. The parameter here counts
powers of arbitrary finite mixed parity words: one atom containing both zero
and one can have arbitrarily many local minima when its exponent grows,
while it remains one power block. Thus the specific arbitrary-word interface
is different from merely putting a bound on the number of monotone runs.
No claim of historical priority is made for the generalization.

## 2. Exact finite ordinary compression

Suppose a segment beginning at a positive ordinary integer \(x\) follows
\(V^k\), where \(\ell=|V|\ge1\) and \(k\ge1\). Write
\(y=T^\ell x\). The first \((k-1)\ell\) parity digits at \(x\) and
\(y\) agree. The ordinary parity-cylinder identity therefore gives

\[
 x\ne y\quad\Longrightarrow\quad
 2^{(k-1)\ell}\le |x-y|. \tag{BC-2}
\]

This is a divisibility statement about the two actual ordinary integers,
not an identification of an ordinary integer with an arbitrary two-adic
limit. It is the existing PR 183 `repeated_parity_requires_displacement`
lemma applied to the actual repeated word.

The universal elementary bound \(T^j x\le2^j x\) then gives

\[
 |x-T^\ell x|\le2^\ell x,
 \qquad
 \boxed{2^{k\ell}\le 2^{2\ell}x.} \tag{BC-3}
\]

The full endpoint also satisfies

\[
 \boxed{T^{k\ell}x\le2^{2\ell}x^2.} \tag{BC-4}
\]

If \(x=y\), the excluded branch is a genuine finite cycle certificate of
period \(\ell\). It is kept as an alternative, not discarded as a division
by zero. A purely even atom is allowed; a positive fixed point for such an
atom cannot occur, but the uniform argument does not need a special exception.

Now divide an actual finite prefix, from the **same original source** \(n\),
into \(r\) power blocks \(V_i^{k_i}\) with \(1\le |V_i|\le B\).
Let \(x_i\) be their successive actual starting values, with \(x_0=n\),
and let \(N=\sum_i k_i|V_i|\). Zero exponents can be omitted. Put
\(C=2^{2B}\). If no atom closes a short cycle, (BC-3)–(BC-4) give

\[
 2^{k_i|V_i|}\le Cx_i,
 \qquad x_{i+1}\le Cx_i^2.
\]

Induction over the blocks yields the exact integer inequality

\[
 \boxed{2^N\le(Cn)^{2^r-1}.} \tag{BC-5}
\]

For the induction step, if the tail exponent is \(e=2^{r-1}-1\), then
\(Cx_1\le(Cn)^2\). Multiplying the head bound by the tail bound gives
\((Cn)^{1+2e}=(Cn)^{2^r-1}\). Every block retains its original ordinary
starting point; no averaging or choice of a fresh source occurs.

Taking logarithms gives

\[
 N\le(2^r-1)(2B+\log_2 n), \tag{BC-6}
\]

and the fully integer version is

\[
 \boxed{N\le(2^r-1)(2B+\lfloor\log_2 n\rfloor+1).} \tag{BC-7}
\]

**BC-T1, formal finite dichotomy.** For every actual finite parity prefix
with the displayed power-block description, either its source reaches a
cycle of period at most \(B\), or (BC-5) and (BC-7) hold. In particular,
a compressed prefix longer than the right side of (BC-7) supplies a genuine
short-cycle certificate. This is unconditional for finite ordinary inputs.
It does not assume that arbitrary infinite itineraries have such prefixes.

### A sharper written chaining constant

The factor two in the logarithmic chaining is convenient for an elementary
integer formalization, but is not essential. Put
\(\alpha=\log_2 3\) and \(\beta=\alpha-1=\log_2(3/2)\). Since

\[
 T^j x+1\le(3/2)^j(x+1),
\]

(BC-2) gives \(2^{k\ell}\le3^\ell(x+1)\). Thus, with
\(h_i=\log_2(x_i+1)\),

\[
 k_i|V_i|\le h_i+\alpha B,
 \qquad h_{i+1}+\alpha B\le\alpha(h_i+\alpha B).
\]

The resulting stronger written bound is

\[
 N\le\frac{\alpha^r-1}{\alpha-1}
       (\log_2(n+1)+\alpha B). \tag{BC-8}
\]

The explicit cutoff below uses the weaker integer bound (BC-6), so its
effectivity does not rely on optimizing (BC-8).

## 3. Primitive cycles and the minimum at block boundaries

Consider a positive cycle whose **least ordinary period** is \(N\), and
suppose one complete period is a product of \(r\) powers of atoms of length
at most \(B\). If \(N\le B\), its period is already bounded. Assume
\(N>B\). Then the short-cycle alternative in BC-T1 is impossible: every
state of a primitive \(N\)-cycle has that same least period. This fact is
also checked in `later_period_pullback` and
`no_short_cycle_of_primitive`.

Let \(m\) be the minimum over every state of the cycle, and let \(m_b\)
be the minimum over its power-block boundaries. A cyclic permutation of the
block list makes \(m_b\) its starting point. We need to relate these minima;
one cannot simply assume that the least ordinary state is already a boundary.

For a fixed atom \(V\), its ordinary affine formula is

\[
 F_V(x)=a_Vx+b_V,
 \qquad a_V=3^{s(V)}/2^{|V|}>0,
 \qquad b_V=C_V/2^{|V|}\ge0.
\]

Across successive copies of that same atom,

\[
 F_V^{j+1}(x)-F_V^j(x)=a_V^j(F_V(x)-x).
\]

These copy-boundary values are monotone, so each is at least the smaller
endpoint of the whole power block, and hence at least \(m_b\). Inside a
single copy, \(T^t z\ge z/2^t\), with \(t<B\). Consequently

\[
 \boxed{m_b\le2^B m.} \tag{BC-9}
\]

This covers expanding, contracting, and fixed affine blocks, with no
assumption that a block is monotone at each individual shortcut step. The
fixed case cannot occur when \(N>B\), but no estimate is obtained by
dividing by \(1-a_V\).

Applying (BC-6) after the cyclic permutation gives

\[
 \boxed{N\le(2^r-1)(2B+\log_2 m_b).} \tag{BC-10}
\]

## 4. The full-cycle logarithmic form

Let \(s\) be the number of odd states in the complete primitive period.
There is at least one: a positive orbit cannot consist solely of successive
halvings and return to its source. Multiplying all actual one-step ratios
around the cycle gives

\[
 2^N=3^s\prod_{x\text{ odd in the cycle}}
          \left(1+\frac1{3x}\right).
\]

Thus the nonzero logarithmic form satisfies

\[
 0<\Lambda:=N\log2-s\log3
 =\sum_{x\text{ odd}}\log\left(1+\frac1{3x}\right)
 <\frac{s}{3m}\le\frac N{3m}. \tag{BC-11}
\]

All \(N\) steps and all \(s\) odd factors belong to the same complete
cycle. No factor of \(2^N-3^s\) is substituted for that denominator.

For a deliberately conservative, completely specified separation constant,
set

\[
 K=2^{33}.
\]

Matveev [Mat00, Corollary 2.3, p. 1219] applies to
\(\alpha_1=2\), \(\alpha_2=3\), \(b_1=N\), \(b_2=-s\), with
number field \(\mathbb Q\), \(D=1\), real parameter \(\varkappa=1\),
\(A_1=\log2\), \(A_2=\log3\), and \(B^*=N\). Its displayed
constant satisfies \(C_1(2)\le2^{6\cdot2+20}=2^{32}\). Since
\((\log2)(\log3)<2\), the theorem gives

\[
 \log\Lambda>-K(1+\log N),
 \qquad
 \boxed{\Lambda>e^{-K}N^{-K}.} \tag{BC-12}
\]

The theorem's algebraicity, degree, height, coefficient-size and nonzero-form
hypotheses are explicit here. This use does not require an unproved
irrationality measure, a conjecture on continued fractions, or a recent
Collatz preprint. The very large numerical constant is chosen for a simple
primary-source derivation, not for numerical competitiveness.

Combining (BC-11) and (BC-12),

\[
 m<\frac{e^K}{3}N^{K+1},
 \qquad
 m_b<\frac{2^B e^K}{3}N^{K+1}. \tag{BC-13}
\]

Now substitute the **upper** bound (BC-13) in the **lower-minimum**
constraint (BC-10). Using \(\log2>1/2\) and discarding a negative term,

\[
 \boxed{N<(2^r-1)\bigl((K+1)\log_2N+3B+2K\bigr).} \tag{BC-14}
\]

This is the decisive comparison. A polynomial bound on \(m\) alone would
not prove cycle finiteness. It is the exact repeated-word budget (BC-10)
that converts it into a finite period bound.

## 5. A literal computable cutoff

Put

\[
 D_{r}=(2^r-1)(K+1),\qquad
 E_{r,B}=(2^r-1)(3B+2K),
\]

and define the positive integer

\[
 J(r,B)=\max\{B,16,4D_r^2,2E_{r,B}\}. \tag{BC-15}
\]

**BC-T2, written effective primitive-cycle bound.** Every primitive positive
cycle admitting an \(r\)-power-block description with atom lengths at
most \(B\) has least period at most \(J(r,B)\).

**Proof.** The case \(N\le B\) is included. Otherwise (BC-14) holds. If
\(N>J(r,B)\), then \(\log_2N\le\sqrt N\), because \(N\ge16\).
Also \(D_r\sqrt N<N/2\) and \(E_{r,B}<N/2\), so
\(D_r\log_2N+E_{r,B}<N\), contradicting (BC-14). The elementary
inequality \(\log_2t\le\sqrt t\) for \(t\ge16\) follows by
differentiating \(\sqrt t-\log_2t\); it vanishes at 16 and has positive
derivative thereafter. ∎

The implicit sharper estimate (BC-14), or its version using (BC-8), is more
informative than the deliberately rough cutoff. For fixed \(B\), the
number of required power blocks grows at least logarithmically with the
primitive period, up to the logarithm of the period's logarithm and constants
depending on the displayed logarithmic-form estimate. This is a necessary
compression condition, not a claim that large cycles exist.

## 6. From primitive periods to all independent exponent tuples

The length \(|W(\mathbf k)|\) in (BC-1) need not be the least period.
For example, \((10)^k\) describes the known cycle repeatedly for every
\(k\ge1\). An argument that asserted a finite cutoff on every supplied
word length would be false.

Suppose an actual cycle with least period \(p\) realizes
\(W(\mathbf k)\). Its primitive parity word \(P\) is the length-\(p\)
prefix of \(W\). Truncate the product at that position. It consists of
some complete earlier power blocks, followed by zero or more copies of one
atom, followed possibly by a proper prefix of that atom. Treat the last
nonempty prefix as one atom with exponent one. Therefore \(P\) has a
description with at most \(r+1\) power blocks, each of length at most
\(B=\max_i|V_i|\). BC-T2 gives

\[
 \boxed{p\le J(r+1,B).} \tag{BC-16}
\]

**BC-T3, written classification theorem.** For every fixed finite list of
nonempty parity atoms, only finitely many primitive positive cycles can be
represented by (BC-1). They can be classified by a terminating exact
algorithm. The complete set of exponent tuples representing those cycles is
effectively semilinear, after excluding the all-zero tuple.

Here is a direct algorithm and the proof of its completeness.

1. Set \(J=J(r+1,B)\). Enumerate binary words \(P\) of lengths at most
   \(J\). For each word compute the full affine numerator \(C_P\) and
   denominator \(2^{|P|}-3^{s(P)}\). Keep only positive integral candidates
   and replay every ordinary shortcut branch and its return to the start.
   Remove duplicates and reduce to primitive cycles. This finite procedure
   finds every cycle allowed by (BC-16). It can of course find cycles that
   do not occur in the original language; the next stage removes those.
2. For each retained cycle and each of its possible starting states, build
   the finite automaton that reads its periodic parity word. Its states are
   the phases \(0,\ldots,p-1\) and one dead state. Reading the required
   next parity digit advances the phase; the other digit enters the dead
   state. Phase zero is accepting. A nonempty accepted word is exactly a
   complete traversal repeated a positive number of times from this start.
3. Regard the fixed word \(V_i\) as a single transition on this finite
   automaton. Iterating it \(k_i\) times gives an ultimately periodic
   sequence of automaton states, computed by following a finite directed
   map. For each pair of phases, the set of allowed exponents is therefore
   effectively ultimately periodic. Choose the finitely many intermediate
   phases between the \(r\) blocks and take the corresponding Cartesian
   products of exponent sets. Their finite union is an effective semilinear
   description of precisely the allowed tuples.

The first stage has astronomical worst-case size; no such enumeration is
reported as executed here. Its role is to prove finite **effectivity**, not
to suggest that the numeric bound is usable in a brute-force experiment.
The algorithm preserves the whole cycle denominator and replays the actual
positive ordinary orbit. The semilinear description includes repeated
traversals of all discovered cycles, rather than mistaking them for infinitely
many distinct primitive cycles.

## 7. The attempted full closing step

The classification theorem settles every one fixed bounded power-block
architecture, even with independently and adversarially chosen exponents.
It does not reduce all arbitrary parity words to one such architecture.
Both parameters matter: a word can always be called one atom by setting
\(B=N\), in which case the short-atom premise needed for (BC-14) disappears.
Alternatively every bit can be its own atom, but then \(r=N\) and the
compression estimate is too weak to exclude it.

For a nonperiodic ordinary orbit, BC-T1 instead says that the actual prefix
compression must satisfy (BC-7) for **every** valid selected description.
A global repetition principle producing violations of that budget would
force eventual periodicity. A further classification of the resulting
positive cycles would still be required for full convergence to one.

The forced dyadic band supplies exact actual marked visits. It does not yet
supply this temporal compression theorem. In particular, the earlier AR-4
construction permits arbitrary orderings of a long prescribed valuation
block at close genuine marked visits. That finite construction does not
refute every fixed-source repetition principle, but it prevents treating
closeness of leading phases as the missing exact word identity.

Thus the new all-parameter cycle result and formal finite dichotomy are
unconditional within their stated domains. The first unsupported global
inference remains the production of a strong enough repeated-word
description on every unresolved ordinary trajectory, or a separate way to
exclude the unbounded-complexity cycle and escape alternatives.

## Formal boundaries

`BlockCompression.lean` formalizes the actual parity predicate `Repeats`, the
transported source predicate `Trace`, the exact short-cycle alternative, the
dyadic power and clock bounds, and the primitive-cycle consumer. A trace
contains genuine ordinary iterates at every block; it is not a list of
arbitrary congruence residues.

The monotone-copy boundary argument (BC-9), the sharper real bound (BC-8),
Matveev's estimate, the scalar effective cutoff, and the semilinear
classification are written proofs in this note. They are not counted as
additional Lean theorems. No universal compression or Collatz premise is
installed in the formal module.

Exact source versions and primary citations are in [SOURCES.md](SOURCES.md).
