# Source-aware triadic construction: coefficient frontier and tail resets

**Date:** 2026-11-23. **Status:** new construction attempts and exact finite
arithmetic consequences; universal successful witness existence remains **OPEN**.
No claim below is a proof of Collatz. This note works with one unchanged
positive ordinary source and does not replace it by independent parity words.

The target is to construct, for each `n>0`, a signed triadic value equal to the
parity-complement autoconjugacy `Omega(n)`. The pre-existing triadic rank then
forces ordinary convergence. The target is existence, not a new certificate
conditional on an already supplied witness.

## 1. Normalization and source pins

Use `T(n)=n/2` when `n` is even and `(3n+1)/2` when `n` is odd. Write

\[
x_K=T^K(n),\quad e_K=x_K\bmod2,\quad p_K=\sum_{i<K}e_i,
\quad b_K=K-p_K.
\]

The complete ordered carries are

\[
C_0=D_0=0,\quad
C_{K+1}=3^{e_K}C_K+e_K2^K,\quad
D_{K+1}=3^{1-e_K}D_K+(1-e_K)2^K.
\]

They obey the exact source identity

\[
                       2^Kx_K=3^{p_K}n+C_K.                 \tag{1}
\]

For any terminal triadic value `z`, its inverse complementary image is

\[
                    I_K(z)=\frac{2^Kz-D_K}{3^{b_K}}.       \tag{2}
\]

This passes the first `K` complementary parity tests. If `z` also has parity
opposite to `x_K`, it passes the terminal test as well. Neither statement
provides the tests after `K`.

The source framework is Monks--Yazinski, *The Autoconjugacy of the 3x+1
Function*, Section 1 and Theorem 2.1,
<https://monks.scranton.edu/files/pubs/AutoConjV13.pdf>.
The current repository inputs read for this attempt were:

* PR175, `53ba1e1ffc46bf022433c2124a62682ad8dd4739`,
  `research/lean-global-closure-20261121/risk24/TRIADIC_AUTOCONJUGACY_ATTACK.md`
  and `TriadicDual.lean`;
* PR178, `e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`,
  `research/profound-step-20261123/arithmetic/TRIADIC_CONSTRUCTION_ATTEMPT.md`
  and `FAILURE_POSITION_RESETS.md`;
* PR176, `fb402404deb810bd8e32e596993739bb5a6967d1`,
  `research/lean-global-resolvent-20261121/overview/triadic-height/TRIADIC_AMORTIZED_BUDGET.md`;
* PR182, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
  `research/whole-repo-round3-20261123/TRIADIC_CLOSURE.md`.

The earlier notes already test constant cycle-tail completion, the original
carry determinant, centered residues, and denominator pigeonholing. The two
attempts here instead use the finite ordinary-input binomial expansion and
terminal data depending on the actual current integer `x_K`.

## 2. A genuine triangular half of the Mahler construction

Let `f(n)=Omega(n)` for nonnegative integers and define its finite Newton
coefficients

\[
a_j=\sum_{i=0}^j(-1)^{j-i}\binom ji f(i).
\]

For every ordinary `n`, binomial inversion gives the **finite** identity

\[
                        f(n)=\sum_{j=0}^n a_j\binom nj.     \tag{3}
\]

This makes a tempting existence attack precise: prove all `a_j` triadic by
an ordinary-index recursion. Then (3) constructs a triadic witness without
running the original trajectory. It is unnecessary to assume an infinite
analytic expansion to obtain (3).

The exact functional equations are

\[
3f(2n)=2f(n)-1,\qquad f(2n+1)=2f(3n+2).                  \tag{4}
\]

The first equation **does** give a useful triangular recursion. From

\[
(1+z)^{2n}=\sum_k\binom nk(2z+z^2)^k
\]

one obtains, for every `k>=1`,

\[
\boxed{
a_{2k}=\frac23a_k-
 \sum_{j=k}^{2k-1}\binom{k}{j-k}2^{2k-j}a_j.
}                                                        \tag{5}
\]

Consequently every even coefficient is constructed from earlier
coefficients using only addition, integer multiplication, and division by
three. This is an actual partial construction, not a parity-prefix
completion. The unresolved coefficients are at odd indices.

For the odd equation in (4), the exact coefficient equation is

\[
\begin{split}
\sum_{j=k}^{2k+1}a_j[z^j](1+z)(2z+z^2)^k
={}&2\sum_{j=k}^{3k+2}a_j[z^j](1+z)^2
                    (3z+3z^2+z^3)^k.                    \tag{6}
\end{split}
\]

Its raw highest coefficient is `-2 a_(3k+2)` when the right side is moved
to the left. Unlike (5), this equation reaches beyond the current index.
Eliminating even coefficients creates real cancellations; discarding them
would exaggerate the obstruction.

For example, with `a_0=-1`, the first three reduced odd equations are

\[
\begin{split}
0&=1-a_1/3,\\
0&=-256a_1/9+21a_3-2a_5,\\
0&=1904a_1/27-52a_3+5a_5.
\end{split}                                               \tag{7}
\]

Five times the second plus twice the third gives
`a_3=32a_1/27`. Hence `a_1=3`, `a_3=32/9`, and the two equations also
construct `a_5`. This is a successful finite elimination for actual small
coefficients; it does not establish a triangular rule for every odd
coefficient.

### Exact finite-equation boundary

Let `M` be any finite cutoff containing every index appearing in a chosen
finite family of equations (4). On the vector `(f(0),...,f(M))`, the change
of coordinates (3) is the lower triangular integer matrix

\[
                       P_{ij}=\binom ij,\qquad \det P=1.
\]

Its inverse has entries `(-1)^(i-j) binom(i,j)`. Replacing each chosen
equation by a finite binomial combination of its first rows is also a
triangular integer row operation. Thus the corresponding finite Mahler
system is exactly an invertible change of coordinates and equations of
the original finite functional system; no additional equation is created.

The original system has a concrete directed graph. For every selected
source `m>0`, it has the edge `m -> T(m)` and equation

\[
f(m)=\begin{cases}(2f(Tm)-1)/3,&m\text{ even},\\
                         2f(Tm),&m\text{ odd}.
       \end{cases}                                       \tag{8}
\]

In a finite acyclic component whose forward endpoint is unprescribed,
assigning that endpoint an arbitrary parameter `t` solves all equations
in the component, with every preceding value a nonconstant affine
function of `t`. This follows by backward substitution, since each edge
has nonzero slope. A component containing an already prescribed value or
a complete cycle can instead be closed by its relevant constraint.
The statement uses the selected complete graph, not just a truncated
table whose outgoing edges have silently been deleted.

A finite closed component may determine a rational value without
determining a triadic value. For a complete cycle the affine slope is
`2^L/3^b`, and solving its scalar equation generally introduces a divisor
of `2^L-3^b`. Rational solvability of that finite subsystem is therefore
not a successful triadic construction.

Therefore a finite Mahler elimination cannot remove an unprescribed
forward endpoint merely by changing basis. The attempted universal step
would require a new theorem that its growing finite equation systems
close each requested coefficient, or a genuinely infinite arithmetic
argument proving that the limiting coefficients remain in `Z[1/3]`.
Neither follows from the triangular half (5). This is the first
unsupported inference in the coefficient construction.

## 3. An actual-source terminal anchor with no denominator cancellation

The next attempt uses the actual current integer rather than a constant
terminal state. Set

\[
z_K=-x_K-1,\qquad
\theta_K=I_K(z_K)=\frac{N_K}{3^{b_K}}.
\]

The value `z_K` always has parity opposite to `x_K`. Thus this constructs a
legal candidate through clock `K`, using only ordinary integer data. By
(1), its numerator has the two exact forms

\[
\boxed{
N_K=-2^K(x_K+1)-D_K
   =-3^{p_K}n-C_K-D_K-2^K.
}                                                        \tag{9}
\]

**No-cancellation theorem.** If the actual prefix has seen at least one
odd and at least one even source, then

\[
                         N_K\not\equiv0\pmod3.           \tag{10}
\]

Consequently the reduced denominator of `theta_K` is **exactly**
`3^b_K`. Actual source integrality has produced no cancellation at all.

**Proof.** Once a carry has received its first active update it is a unit
modulo three, because an active update replaces it by three times its old
value plus a power of two; an inactive update leaves it unchanged.
The term `3^p_K n` vanishes modulo three. If the last source was odd,

\[
C_K=C_{K-1}\,3+2^{K-1},\quad D_K=D_{K-1},\quad
C_K+D_K+2^K\equiv D_K\not\equiv0\pmod3.
\]

If the last source was even, the same sum is congruent to the untouched
unit `C_K`. Equation (9) proves (10).

This is not confined to a single affine formula. For any fixed integers
`u,v` with `u=v=-1 mod 3`, the source-aware affine anchor `z_K=u x_K+v`
has numerator

\[
u3^{p_K}n+uC_K+v2^K-D_K,
\]

which is congruent to the numerator in (9). Every anchor in this entire
congruence class retains the full denominator after both parities have
occurred. Requiring `u,v` odd additionally gives the correct terminal
parity for every ordinary `x_K`.

## 4. Calibrating the source-aware anchor to the actual cycle

The previous anchor does not match the target cycle. The unique affine
rule with `h(1)=2` and `h(2)=1` is

\[
                              h(x)=3-x.
\]

It also has opposite parity to `x` for every integer. Its candidate
stream is

\[
\eta_K^{h}=
 \frac{2^K(3-x_K)-D_K}{3^{b_K}}.
\]

The exact updates are

\[
\eta_{K+1}^{h}-\eta_K^{h}=
\begin{cases}
-2^{K+1}(x_K-1)/3^{b_K},&e_K=1,\\
\phantom{-}2^{K+1}(x_K-2)/3^{b_K+1},&e_K=0.
\end{cases}                                               \tag{11}
\]

Each update vanishes precisely at the appropriate standard-cycle state.
Two consecutive alternating updates cancel even away from that cycle.
Thus matching the terminal cycle repairs the particular failure of (9),
but does not make each individual correction decrease a height.

There is a stronger obstruction shared by a broad class of calibrated
anchors, not just this affine choice.

## 5. Full-denominator resets for every calibrated local rule modulo three

Let `h` be any integer-valued terminal rule satisfying

\[
x\equiv1\pmod3\Rightarrow h(x)\equiv2\pmod3,
\qquad
x\equiv2\pmod3\Rightarrow h(x)\equiv1\pmod3.              \tag{12}
\]

Every polynomial `h in Z[X]` with `h(1)=2`, `h(2)=1` satisfies (12).
More generally, so does any rule preserving congruences modulo three and
calibrated to those two values. For those integer polynomials the correct
terminal parity is automatic as well: even inputs are congruent to two
modulo two and hence have odd outputs, while odd inputs are congruent to
one and hence have even outputs. For a general rule (12), retain the
additional opposite-parity condition when a legal candidate through the
terminal clock is needed; the denominator calculation itself uses only
(12).

After the first original odd step, `x_K` is a unit modulo three.
For

\[
                         A_K^h=2^Kh(x_K)-D_K,
\]

equations (1) and (12) give the exact congruence

\[
\boxed{ A_K^h\equiv-(C_K+D_K)\pmod3. }                   \tag{13}
\]

Let `j_o,j_e` be the last odd and even indices of the prefix. Then

\[
C_K\equiv2^{j_o},\quad D_K\equiv2^{j_e}\pmod3.
\]

Once both symbols have occurred, let `ell` be the length of the final
constant-parity run. The two last active positions differ by `ell`.
Since two is minus one modulo three, (13) proves

\[
\boxed{
3\mid A_K^h\quad\Longleftrightarrow\quad \ell\text{ is odd}.
}                                                        \tag{14}
\]

In particular **every even-length final run resets the reduced
denominator to the full `3^b_K`, for every rule (12)**. An anchor chosen
from any fixed family of such rules cannot avoid the reset by switching
which rule it uses at that clock.

A useful finite core avoids defining the entire last run. If the final
three prefix symbols are `011` or `100`, the final run has length two.
If `U=2^(K-3)` and the earlier carries are `C,D`, the new carry sum is
respectively

\[
9C+3D+11U\quad\text{or}\quad3C+9D+11U.
\]

Both are congruent to `2U`, a unit modulo three. Thus these two explicit
blocks force full denominator for all calibrated rules (12), regardless
of the earlier prefix or the original positive integer.

### All-time consequence, with its quantifier limit

A positive ordinary orbit has infinitely many odd and even sources. If
it were eventually all even, repeated halving would violate positive
integrality; if eventually all odd, `v_2(x+1)` would strictly decrease.
If only finitely many blocks `011` and `100` occurred while both symbols
occurred infinitely often, all sufficiently late constant runs would
have length one. The orbit would therefore eventually alternate. Such a
positive ordinary orbit reaches the standard cycle, since at its odd
clocks `u_next-1=(3/4)(u-1)`.

Hence an actual positive source that fails to reach one would have
infinitely many simultaneous full-denominator resets for **every** rule
in (12), with the reset exponents tending to infinity. Conversely, on a
source reaching one, every exactly calibrated rule becomes the true
constant triadic dual after the first visit to the standard cycle.

This excludes boundedness of the entire denominator sequence as a free
consequence of source-aware polynomial calibration. It does **not**
exclude a favorable intervening subsequence. It does not provide a lower
bound on the frequency of even source steps, and it does not turn these
resets into a universal nonexistence result for other constructions.

## 6. What remains to be constructed

The coefficient attack has a genuine finite triangular half, (5), and
successful small eliminations (7). Its missing step is a proof that all
odd coefficients enter a finite triadic elimination, or an arithmetic
argument controlling the infinite endpoint parameters.

The source-aware tail attack has two new exact restrictions: the broad
affine class of Section 3 has no cancellation at all, and all calibrated
rules local modulo three share the resets in Section 5. The latter class
includes every integer polynomial calibrated to the standard cycle.
To obtain a successful candidate by this route one still has to prove
enough cancellation and numerator control at a specified intervening
clock. Adaptive rules outside (12), or integer-valued binomial
polynomials whose residue can depend on higher base-three digits, are
not excluded by the theorem.

## 7. Formal execution and its boundary

`SourceAwareTails.lean` compiles with Lean 4.34.1, importing only `Std`.
Its 26 theorem declarations include the complete carry invariants, the
source-anchor identities, the full affine no-cancellation class, the
calibrated-tail reset implication, the two universal reset blocks, and
the exact alternating-pair invariance of the reflection candidate.
It also defines the actual integer shortcut iteration and proves its
finite source identity. Thus `actual_negative_anchor_unit` assumes only
that the actual finite prefix has seen both parities; it does not take
the source identity or any convergence conclusion as an additional
premise.

All twelve printed key axiom inventories contain only `propext` and
`Quot.sound`; none contains `sorryAx`. The command `lean
SourceAwareTails.lean` exits zero without warnings. Exact source hashes,
version, command, declaration list and output are in
`source-aware-lean-receipt.json`.

The Mahler identities and finite-graph interpretation, polynomial
specialization of (12), the all-run formula (14), the all-time frequency
argument, and the interpretation of a numerator unit as an exact reduced
denominator remain written mathematics. The Lean module proves the
finite arithmetic core, not universal successful witness existence.
