# Concurrent PR183 comparison and a sharper full-word cutoff

Written supplement, 2026-11-22. **Collatz remains open.** No new Lean
declarations or replay claims are made in this supplement. The existing
12-theorem `BlockRepetitionBudget.lean` audit is unchanged.

The new remote source is PR183 at
`68345f60a4f757acb42a69a4ac95910f8ce26163`, inspected with `git show`:

- `research/profound-step-20261122/arithmetic/FREE_EXPONENT_CYCLES.md`;
- `research/profound-step-20261122/arithmetic/BlockCompression.lean`;
- `research/profound-step-20261122/arithmetic/CARRY_COMPRESSION_BRIDGE.md`;
- `research/profound-step-20261122/mergers/ARBITRARY_DEBT.md`;
- `research/profound-step-20261122/RECONSTRUCTION_REVIEW.md`.

## 1. Precise overlap and complementary interfaces

PR183's BC-T3 and this packet's independent-block classifier establish the
same qualitative result: arbitrary independent nonnegative repetition
counts in a fixed finite list of parity blocks admit an effective finite
list of primitive positive cycles and an effective semilinear description
of the accepted exponent tuples. That conclusion must be credited to both
concurrent derivations. It is not a separate new conclusion of the present
supplement.

The formal interfaces differ usefully.

| Interface | PR183 | This packet |
|---|---|---|
| Ordinary path representation | Actual `orbit`, repeated parity predicate `Repeats`, and transported-source `Trace` | Exact integer branch equations for arbitrary supplied binary words |
| Repetition arithmetic | Same-parity displacement gives a bound in terms of atom length | Exact divisibility by the entire repeated dyadic denominator, with the block's actual affine coefficients |
| Cycle alternative | Formal reached-short-cycle alternative and primitive-cycle consumer | Nonfixed-block hypothesis explicit in the formal budget; template fixed points handled in the written classifier |
| Cycle source bound | Whole-cycle minimum, related to a block-boundary minimum | A suffix-product rotation bounds one periodic boundary directly |
| Effective output | Bounds the primitive period; a truncation may cost one extra atom | Bounds the entire supplied word outside the finite template-cycle cases |

Both formal chaining arguments use exponent `2^r-1`. PR183 additionally
derives the stronger real chaining factor

\[
S_r=\sum_{i=0}^{r-1}\alpha^i
=\frac{\alpha^r-1}{\alpha-1},\qquad \alpha=\log_2 3,
\]

in its written BC-8. The combination below credits that sharpening and
retains this packet's full-word/template dichotomy and suffix rotation.

These are refinements within an elementary bounded-description argument.
The stronger recent periodic-dictionary complexity results identified in
`INDEPENDENT_BLOCK_CLASSIFICATION.md` remain credited; no general
dictionary-complexity priority claim is made.

## 2. Combine the exact affine reserve with the sharper chain

Supply nonempty binary atoms \(V_1,\ldots,V_r\), with independent
exponents, and delete inactive factors for the argument. For atom \(i\),
write

\[
F_i(x)=\frac{a_i x+C_i}{b_i},\quad
a_i=3^{s_i},\quad b_i=2^{L_i},\quad
D_i=b_i-a_i\ne0,\quad \xi_i=C_i/D_i.
\]

Use the coefficient-specific integer

\[
K=\max\{1,\max_i|D_i|,\max_i C_i\}.
\tag{S1}
\]

This is a written slight refinement of the formal module's sum-based
`wordCost`: the elementary inequality
\(|D_i x-C_i|\le K(x+1)\) uses a maximum instead of a sum.

Suppose the actual positive path traverses \(e_i\) copies of atom \(i\)
from boundary \(x_i\), and put \(t_i=L_i e_i\). If
\(D_i x_i-C_i=0\), the first actual copy returns to \(x_i\): the path
has reached the explicitly replayable template cycle. Otherwise the exact
reserve identity proved by `repeated_word_reserve` gives

\[
2^{t_i}\le |D_i x_i-C_i|\le K(x_i+1).
\tag{S2}
\]

The ordinary shortcut map also satisfies

\[
T^t(x)+1\le(3/2)^t(x+1).
\]

Write \(h_i=\log_2(x_i+1)\), \(k_0=\log_2K\), and
\(\beta=\alpha-1\). Then

\[
t_i\le h_i+k_0,
\qquad
h_{i+1}\le h_i+\beta t_i,
\qquad
h_{i+1}+k_0\le\alpha(h_i+k_0).
\]

Summing the resulting geometric bounds proves the all-clock estimate

\[
\boxed{A:=\sum_i t_i\le S_r\log_2\bigl(K(x_0+1)\bigr).}
\tag{S3}
\]

It applies to open ordinary paths too, until a fixed-block alternative is
encountered. The same initial source is retained throughout. There is no
uniform bound on \(r\) asserted for arbitrary trajectories.

Now suppose the complete supplied word is a positive cycle and no active
block fixes its boundary. Rotate its actual multiplier list as in the
original classifier so every suffix product is at most one. Set

\[
B=2\sum_i|\xi_i|,
\qquad M=3^S/2^A<1.
\]

The exact complete affine numerator after rotation gives

\[
x_0\le\frac{B}{1-M}.
\tag{S4}
\]

Retain any correctly instantiated effective logarithmic-form constants
\(c\in(0,1]\), integer \(\kappa\ge1\), satisfying

\[
1-3^S/2^A\ge c A^{-\kappa}.
\]

The original note gives a directly checked conservative Matveev
instantiation. Choose an integer \(b\ge0\) with
\(K(1+B/c)\le2^b\). Equations (S3)--(S4) imply

\[
\boxed{A\le S_r\bigl(b+\kappa\log_2 A\bigr).}
\tag{S5}
\]

Unlike the primitive-period approach, this concerns the complete supplied
word. No primitive-prefix truncation or extra partial atom is needed.
Unbounded lengths remain allowed exactly through the retained template-cycle
alternative.

## 3. A substantially smaller explicit cutoff

For a rational, exactly computable upper coefficient, use
\(\alpha<8/5\), which follows from \(3^5<2^8\). For \(r\ge1\), put

\[
E_r=\left\lceil\sum_{i=0}^{r-1}(8/5)^i\right\rceil
=\left\lceil\frac{8^r-5^r}{3\cdot5^{r-1}}\right\rceil,
\qquad P=\kappa E_r,\quad Q=bE_r.
\tag{S6}
\]

Thus \(P\ge1\) and (S5) implies \(A\le Q+P\log_2 A\).
Choose the least integer \(j\) with \(4P\le2^j\), and set

\[
\boxed{N_*:=\max\{16,4Q,4Pj\}.}
\tag{S7}
\]

**Claim.** A positive \(A\) satisfying the displayed logarithmic
inequality must obey \(A<N_*\).

**Proof.** Put \(T=4Pj\). Since \(P\ge1\), \(j\ge2\) and
\(T\ge8\). Also

\[
\log_2 T=\log_2(4P)+\log_2j\le2j,
\qquad P\log_2T\le T/2.
\]

The function \(\log_2 t/t\) decreases for \(t\ge8\). Therefore
\(A\ge T\) implies \(P\log_2A\le A/2\). If also
\(A\ge4Q\), then
\(Q+P\log_2A\le3A/4<A\), a contradiction. This proves (S7).
The harmless 16 preserves the convention of the previous displayed
cutoffs. All quantities in (S6)--(S7) are obtained by exact integer or
rational arithmetic. ∎

This replaces the original coarse dependence
\(O(\kappa^2 4^r+b2^r)\) by

\[
O\!\left((8/5)^r
\bigl[b+\kappa(r+\log(\kappa+1))\bigr]\right).
\tag{S8}
\]

For fixed maximum atom length, the dependence on the number of pieces is
therefore a linear factor times \((8/5)^r\), rather than \(4^r\).
The exact implicit bound (S5) retains the slightly better base
\(\log_2 3\). This improves the explicit bounded-language classifier;
it does not supply a compressor for arbitrary cycles.

The constants can be made uniform in the contents of all atoms of length
at most \(\ell\). Indeed \(C_i\le3^{L_i}-2^{L_i}\), so
\(K\le3^\ell\) and \(B\le2r3^\ell\). With the original note's
\(c=2^{-(2\kappa+2)}\), it suffices to take

\[
b=2\kappa+4+4\ell+\lceil\log_2r\rceil.
\tag{S9}
\]

The finite classification procedure is unchanged: compute template cycles,
enumerate independent tuples with complete word clock below \(N_*\), and
check the full cycle quotient and actual path. For each listed cycle take
the union over **every starting phase** in its finite automaton and retain
a nonempty-word flag, so the all-zero exponent tuple is rejected.

## 4. What the carry-compression bridge adds and what it does not

PR183's bridge constructs complete supplied source certificates
\([3,\ldots,3,h]\to1\), with \(5k\) initial gap-threes, on which the
intermediate target debt exponent grows as \(4k+2\). This is stronger
than a family of uncertified sources as a test of a proposed fixed debt
cutoff. Its final gap \(h\) is unbounded; it is not a counterexample to
an alphabet-four-only state bound.

The temporal source and target words still have one power block each.
Their common exact divisibility budget is

\[
2^{15k}\mid5r-1,
\qquad
5(9r+2)-19=9(5r-1).
\]

This is a direct instance of our exact affine reserve. Large initial height
pays for the long repetitions, so the compression theorem does not bound
their intermediate debt uniformly. Their targets also satisfy
\(n\equiv23\pmod{32}\) and \(T^5n<n\). They are successful ordinary
descent cases, not unresolved counterexample candidates.

There is a useful compositional interface: outer induction on the existing
complete-source grade can be refined by inner strong induction on the
queried target. An ordinary descendant strictly below that queried target
remains in the same active source interval, while a paid capture decreases
the outer grade. The supplied source certificate can therefore be retained
on the ordinary-descent branch.

The original-target guard is essential. If \(9r+2\) was reached as an
intermediate carry from an earlier interval query, descent below
\(9r+2\) alone need not descend below the earlier query's target. Nor may
one insert a larger padded source without paying its grade. This supplement
does not assert those guards for every occurrence of the debt family.

PR183 supplies total finite carry transport, stronger paid capture rules,
and an exact overflow test family. The combined arithmetic still lacks a
universal successful dispatcher or an upper temporal-complexity bound on
every exceptional ordinary trajectory. Neither the improved cutoff nor
the two-level rank interface removes that global coverage obligation.
