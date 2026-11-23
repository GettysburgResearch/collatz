# Uniform clock bounds and complete affine merger rays

## Result and status

**Status: Lean kernel checked, unconditional ordinary-integer theorem.**
The map is the shortcut Collatz map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

For every actual merger

\[
T^h(An+B)=T^t(Cn+D),\qquad h,t\le H,
\tag{1}
\]

with natural parameters, put \(M=\max(B,D)\). If

\[
n+2^H>3^H(M+1),
\tag{2}
\]

then the two actual normalized affine slopes agree:

\[
2^{H-h}3^{a_h(An+B)}A
=2^{H-t}3^{a_t(Cn+D)}C.
\tag{3}
\]

Here \(a_j(x)\) counts the odd inputs in the first \(j\) actual steps from
\(x\). Neither word is prescribed, and both words may vary with the source.

More positively, that **one large observed merger certifies the complete
ordinary parameter class**:

\[
\forall z\ge0,\quad
T^h\!\left(A\bigl((n\bmod2^H)+2^Hz\bigr)+B\right)
=T^t\!\left(C\bigl((n\bmod2^H)+2^Hz\bigr)+D\right).
\tag{4}
\]

This includes members below the observed parameter. The independent clocks
remain exactly \(h,t\). Every trajectory in (4) is an actual ordinary
trajectory; the proof does not replace legality by a modular affine equation.

For the special pair \(n,mn\), if \(m\) has a divisor \(d>1\) coprime to
both two and three, every merger satisfies the pointwise bound

\[
\boxed{n+2^H\le3^H.}
\tag{5}
\]

In particular (5) holds for multiplication by five. Thus the maximum of the
two merger clocks is strictly greater than \(\log_3 n\) for positive sources.
This bounds each source separately, rather than only the number or density
of sources served by a bounded menu. It does not assert a merger exists.

`MergerClockRigidity.lean` proves the general affine result, the complete-ray
extension, the nonresonance test, and the concrete five case using Lean core
and `Init.Data.Nat.Coprime`. It imports only this packet's existing
`EndpointSteering` project module. No analytic premise, convergence axiom,
`sorry`, or native evaluation is used.

## Proof

### 1. A common correction bound for every actual word

For each actual prefix define its nonnegative correction \(c_h(x)\) by

\[
2^hT^h(x)=3^{a_h(x)}x+c_h(x).
\tag{6}
\]

The module constructs the correction recursively and proves the equality.
For the first input bit \(b=x\bmod2\), its recursion is

\[
c_{h+1}(x)
=3^{a_h(Tx)}b+2c_h(Tx).
\]

Since \(a_h(Tx)\le h\) and \(b\le1\), induction gives

\[
0\le c_h(x),\qquad c_h(x)+2^h\le3^h.
\tag{7}
\]

This is the familiar all-odd correction bound, here proved for the actual
recursive orbit and used uniformly over both varying parity words.

Multiply (6) by \(2^{H-h}\). The padded correction satisfies

\[
2^{H-h}c_h(x)+2^H\le3^H,
\quad
2^{H-h}3^{a_h(x)}\le3^H.
\tag{8}
\]

The operation pads an equality to a common denominator. It does not insert
orbit steps or assert that either original history stays inside a binary
source horizon.

### 2. Integer slopes cannot cross with small offsets

Apply (8) to the left source \(An+B\). Its padded affine expression is

\[
L n+E,\quad
L=2^{H-h}3^{a_h(An+B)}A,
\]

\[
E=2^{H-h}3^{a_h(An+B)}B+2^{H-h}c_h(An+B).
\]

The nonnegative offset has the bound

\[
E+2^H\le3^H(M+1).
\tag{9}
\]

The right source has the same form \(Rn+F\), with the same upper bound for
\(F\). A merger gives \(Ln+E=Rn+F\).

If \(L<R\), integrality gives \(L+1\le R\), so \(n+F\le E\).
Consequently \(n+2^H\le3^H(M+1)\). The case \(R<L\) is symmetric.
Under (2), neither case is possible, proving (3). Once the slopes agree,
the offsets agree as well.

### 3. The parameter lift retains actual legality

The existing ordinary binary lifting theorem gives, for every \(z\ge0\),

\[
T^h(A(n+2^Hz)+B)
=Lz+T^h(An+B).
\tag{10}
\]

The analogous identity holds on the other arm with slope \(R\). Equation
(3) and the supplied merger prove equal endpoints for every lifted
parameter. This already gives an infinite ordinary ray.

To include the lower members of the same class, write
\(n=r+2^Hq\), \(0\le r<2^H\). The mergers at \(n\) and \(n+2^H\),
expressed by (10) based at \(r\), force equal slopes and equal base endpoints
at \(r\). Equation (10) now proves (4) for all \(z\ge0\).

The file also proves the exact converse interface: a full parameter ray
merges if and only if its base point merges and its two actual padded slopes
agree. A sample is not extrapolated without a theorem certifying that step.

### 4. Multipliers with a factor outside two and three

Take \(A=1,B=0,C=m,D=0\). Equality (3) would give

\[
2^u3^a=m2^v3^b.
\]

If \(d>1\) divides \(m\) and is coprime to two and three, then \(d\)
divides the left side while being coprime to it. This forces \(d=1\), a
contradiction. Therefore (2) is impossible, proving (5).

More generally, the same test applies to an affine pair when \(d\mid C\)
and \(d\) is coprime to \(2,3,A\). No primality predicate is needed in the
formal theorem. For fixed positive leading coefficients, failure of every
two-three ratio is the intrinsic condition; the coprime-divisor test is a
convenient sufficient certificate for it.

## How this changes the global merger attack

The new conclusion separates two mechanisms without limiting either
ordinary clock in advance.

1. **An isolated nonresonant crossing pays a source-dependent clock cost.**
   In particular a universal repair of the semigroup's multiplication-by-five
   step cannot use clocks bounded independently of the source, and cannot
   use \(H\le\log_3 n\). The previous packet proved only finiteness for
   fixed clocks by counting word pairs; (5) supplies an explicit threshold
   and applies to every proposed source-dependent word selector.

2. **A sufficiently large resonant crossing is already an entire physical
   ray.** The threshold turns one observed actual merger into a complete
   all-parameter certificate. The slopes, intercepts, positivity of any
   requested starts, and rank or size reduction still need to fit the
   intended application. The theorem does not assert all residue classes
   contain such a crossing.

For the PR183 blocked-erasure pair
\(3^k(6q+1)+r\) and \(3^k(2q)+r\), the leading coefficient ratio is three.
It is resonant and is not prohibited by this result. A successful global
construction still has to find the corresponding legal words and exact
correction equality for every needed suffix. Likewise PR185's variable-clock
AL27 partner has ratio \(9/16\), so this theorem is consistent with that
positive selector and does not extend its complementary-phase coverage.

## Current-source reconciliation and attempted completion

The following sources were read at the exact heads shown. These were
targeted source inspections, not fresh upstream compiler replays or blanket
independent reviews.

| Source | Pin | Relevant conclusion and retained boundary |
|---|---|---|
| PR176, `research/lean-global-resolvent-20261121/overview/parallel/SOURCE_ENVELOPE.md` | `8aeb843bba254f065743b6fa277a70906b51d520` | The paid literal-cut source envelope is exact and attained; an independent-clock merger into it is still a supplied universal selector. |
| PR176, `research/lean-global-resolvent-20261121/overview/parallel/COFINAL_ENVELOPE_LIMITATION.md` | same | Cofinal cap-four certificates attain the halving envelope; this is not proved cofinal after all retained-even residual-cell exclusions. |
| PR178, `research/literature-reframe-20261122/README.md` | `be5696cc45a95ad1903802b08ba1dc3ebba66930` | Actual unequal-clock tail barriers and ordinary critical-moment criteria leave an unbounded successful selector or a global moment bound open. |
| PR182, `research/lean-dyadic-descent-20261121/LITERATURE_CERTIFICATE_BRIDGE.md` | `45354128f890fb479f6c23b547368bcddd9cebe6` | Arbitrarily long inserted prefixes preserving a supplied literal tail can still lose a fixed proportion of source height; bounded target lookahead does not repair that interface universally. |
| PR185, `research/literature-orbit-closure-20261121/AL27_HALF_ROUTE.md` | `276be8154f4e867acc0230466b34d9cb224aacf5` | An actual variable-clock smaller partner covers half of its stated branch, including examples before first descent; its complementary phase remains outside that theorem. |

I tried to extend the half-source diamond behind the last result. For
\(n=2^rw-1\), erasing the first rising bit proposes
\(x=2^{r-1}w-1<n\). At the ends of their odd runs the comparison is
\(3B-1\) versus \(B-1\), where \(B=3^{r-1}w\).

When \(B\equiv3\pmod4\), two halvings on the first arm and a halving then
an odd step on the second give the same endpoint \((3B-1)/4\). This is the
known positive diamond. When \(B\equiv1\pmod4\), write \(B=4c+1\).
The two components reduce instead to the pair

\[
6c+1\quad\hbox{and}\quad c.
\]

Asserting that this pair always merges would fill the missing reverse-even
branch of \(x\mapsto3x+1\); it is not supplied by the first phase or by
the source envelope. On the nontrivial rising starts \(r\ge2\), one has
\(3\mid B\), so the residual input always satisfies \(c\equiv2\pmod3\).
An unconditional merger theorem just on this last class would already
suffice: starts congruent to one modulo four directly descend; the other
odd starts would merge with their strictly smaller half-source. Strong
induction would then close the entire positive theorem. This explains the
exact force of the missing complement without treating it as a small
unchecked case.

Erasing more rising bits changes the affine ratio and
the carry, but no decreasing common rank was obtained for the unrestricted
residual pair. The new ray theorem certifies an actual merger when one is
found; it does not manufacture the missing one.

**First unsupported global inference:** every residual target/source state
admits a legal two-arm ordinary merger with a smaller paid source or smaller
common rank. This remains OPEN. No theorem in this note proves full Collatz.

## Evidence

`MergerClockRigidity.lean` has 22 public theorem axiom reports. The actual
Lean 4.34.1 compiler run used `-j1 -DwarningAsError=true -DautoImplicit=false`.
The only project import, `EndpointSteering.lean`, was compiled from its
published bytes into a fresh local output directory. All new reported
dependency closures are subsets of `propext`, `Classical.choice`, and
`Quot.sound`. The local execution receipt records exact commands, compiler
identity, source hashes and outputs; root integration should retain its own
complete-checkout repository gate separately.
