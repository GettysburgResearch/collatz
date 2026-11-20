# Independent review of the shifted-core return bounds

**Review result: the scoped arithmetic claims RU1–RU3 and FD1–FD3 pass,
subject to the explicitly cited Evertse S-unit theorem.** The reviewer
reconstructed the two nondegeneracy arguments, the unit encodings and
their injections, the end-run extension argument, and the excursion
quantifiers. No missing arithmetic step was identified. These results
remain proposed research additions; this review does not change the
repository's accepted theorem registry or establish Collatz convergence.

There is one terminology qualification for RU3's shorthand “nonperiodic
orbit”: it must mean an orbit **with no repeated state**, or equivalently
one that is **not eventually periodic**. FD3 states this precise hypothesis
explicitly. An orbit which is merely not periodic from its initial state
can have a periodic tail. The proofs and this review count excursion
occurrences as distinct paths only under the no-repeated-state hypothesis.
Both notes exclude repeated cycle laps from that counting argument.

## Exact review target

The reviewed artifacts have the following SHA256 values. No author code
was imported into the independent checker.

| Artifact | SHA256 |
|---|---|
| `MULTISTEP_CORE_RETURNS.md` | `a1f939725bb3ffc333255fb57cafa8e95ed8dace8155650b5a608ef34ba20d5b` |
| `check_multistep_core_returns.py` | `c36e3180590d4cfd6215a43417c9da712ae594700527421c283df961fd3a1593` |
| `multistep-core-returns-report.json` | `e1eab13cea6f2d5edde5d91f8cc44fbef3bb12cd1f3e11c5d3fef3086d0cd630` |
| `multistep-core-returns-report-oo.json` | `e1eab13cea6f2d5edde5d91f8cc44fbef3bb12cd1f3e11c5d3fef3086d0cd630` |
| `FIXED_DEFECT_CORE_RETURNS.md` | `2412c6bfdcb3eeb280079235c5f04656cff49feaf091ba5421147acd1e81ba64` |
| `check_fixed_defect_core_returns.py` | `016695a9eefe241a952fe25af1cfaa066518ee6c24d0e66ea9eb07fe205d9093` |
| `fixed-defect-core-returns-report.json` | `96e259b2c3ba9ab2885b2f3961bef81f75248d6b90bb5a2896870bfea97bef52` |
| `fixed-defect-core-returns-report-oo.json` | `96e259b2c3ba9ab2885b2f3961bef81f75248d6b90bb5a2896870bfea97bef52` |

The reviewer read both complete author checkers and reran each in ordinary
Python and with `python3 -OO`. All four reruns exited successfully and
reproduced their corresponding frozen report byte for byte. Neither
checker relies on Python `assert` statements.

## 1. RU1: the full-path degeneracy classification

Let an actual positive odd path have states \(n_0,\ldots,n_r\), division
exponents \(a_i\ge1\), cumulative exponents \(A_i\), and shifted values
\(m_i=n_i+1\). The equation reviewed is

\[
3^r m_0+\sum_{i=1}^{r-1}3^{r-1-i}2^{A_i}
+2^{A_r}-2^{A_r}m_r=2\,3^{r-1}.
\]

The unrolling and the shift were checked directly. The left side has one
negative term. Any vanishing nonempty subsum must contain that term; its
complement is therefore positive and sums to the displayed right side.
The initial positive term is too large to belong to the complement,
because \(m_0\ge2\). Thus the complement uses only the middle terms and
the final power of two.

Those terms have strictly increasing binary valuations. The target has
binary valuation one, which forces the first available term and
\(A_1=1\). After the first \(j-1\) terms have been removed, the exact
residual is \(2^j3^{r-j}\). Its valuation forces the next term and
\(A_j=j\). The final residual forces \(A_r=r\). This proves both that
all increments are one and that the complement contains all the available
terms. It also proves uniqueness of the vanishing subsum. The case
\(r=1\) is handled by the same valuation argument on its singleton
complement.

Conversely, every valuation-one transition multiplies the shift by
\(3/2\), so an all-ones path has the claimed endpoint cancellation.
The infinite all-ones family in the note is a valid necessary exception,
not an artifact of the proof. Positive integer paths, rather than formal
unit solutions, are essential to the size and exact-valuation arguments.

## 2. FD1: no proper vanishing subsum after compression

For a canonical segment, the first and last edges are defects and its
defect positions are \(1=i_1<\cdots<i_d=r\). The shifted affine
recurrence gives

\[
P_0+\sum_{j=1}^d(P_j-Q_j)-E=0.
\]

The additive correction is zero on every valuation-one edge. This
justifies retaining only the defect positions in the equation.

The proof must rule out every proper signed subsum, not merely cancellation
of one positive term against one negative term. It does so. The correction
valuations are strictly interlaced,

\[
v_2(Q_1)<v_2(P_1)<\cdots<v_2(Q_d)<v_2(P_d)<v_2(E).
\]

The first defect gives \(v_2(m_0)=1\), so only \(P_0\) and \(-Q_1\)
can jointly remove the smallest valuation. Every nonempty zero subsum
must contain both. Their sum has the exact valuation of \(P_1\), because
its remaining odd factor is the actual positive state \(n_1\). This
forces \(P_1\).

After all terms through \(P_j\) are forced, their partial sum is exactly
\(3^{r-i_j}2^{A_{i_j}}m_{i_j}\). If the next defect is separated by
\(\ell\) valuation-one steps, then
\(v_2(m_{i_j})=\ell+1\): each intervening step lowers this valuation by
one, and a defect occurs exactly when the next source shift has valuation
one. Consequently the partial sum has exactly the valuation of
\(Q_{j+1}\); all later terms have larger valuation. This forces the
next negative correction. Subtraction leaves an odd-state multiple that
forces the next positive correction. Induction includes every correction
and then the final endpoint term.

The argument is valid for unrestricted intervening run lengths. It does
not assume that the intermediate shifted cores belong to the fixed prime
pool. At \(d=1\), canonicality implies \(r=1\), consistently with the
one-edge case.

## 3. Unit theorem, fixed coefficients and injectivity

The reviewer inspected Evertse's Theorem 3, printed page 7, and the
definitions of the unit equation and places on printed page 4 in the
[author-hosted primary PDF](https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf).
The theorem permits arbitrary fixed nonzero coefficients in the ground
field and bounds nondegenerate solutions by
\((2^{35}N^2)^{N^3|S|}\). Over \(\mathbb Q\), a pool of \(s\) finite
primes gives \(|S|=s+1\), including the real place.

For RU2, the \(r+2\) variables are units over the stipulated pool. The
endpoint cores remain in fixed rational coefficients and add no places.
The vector recovers the source from its first coordinate and recovers all
the cumulative exponents. Every actual path with a defect is
nondegenerate by RU1. Counting all solutions of the unit equation therefore
bounds the smaller set of actual positive ordinary paths.

For FD2, dividing by \(Q_1=2\,3^{r-1}\) leaves exactly \(2d+1\) unit
variables with coefficients independent of the unbounded path length.
The coefficients contain the fixed endpoint cores. FD1 excludes every
nonempty zero subsum on the normalized left side, since such a subset
would omit \(-Q_1\) from the homogeneous equation.

The injection also survives unbounded time. Each labeled positive
correction coordinate is
\(2^{A_{i_j}-1}/3^{i_j-1}\). Unique factorization separately recovers
\(A_{i_j}\) and \(i_j\); there is no cancellation between its numerator
and denominator. Canonicality identifies the final recovered position
with \(r\). Together with the recovered initial state, that determines
the entire deterministic ordinary path. No different canonical segment
with the same fixed core pair can share this unit vector.

This establishes the displayed counts for fixed length and fixed defect
count, respectively. Neither application provides a height bound or a
method for enumerating every exceptional segment.

## 4. End runs, finite cores and occurrence counts

Deleting initial and terminal valuation-one runs preserves the two
shifted cores because the pool contains 2 and 3. A canonical segment with
first shift \(m\) has at most \(v_3(m)\) backward valuation-one steps:
the possible predecessor shift after \(k\) steps is
\(2^k m/3^k\). Its final shift \(m'\) permits precisely
\(v_2(m')-1\) successive forward valuation-one steps before the next
defect. Both extension sets are finite. The count for canonical segments
is not silently reused as a uniform count for all extensions.

An excursion out of a finite core set and back has defective first and
last edges, because a valuation-one edge cannot cross either core-set
boundary. Thus such an excursion is canonical. The ordered endpoint-core
pairs give the stated \(|Q|^2\) factor. Summing the fixed-defect bound over
\(1\le d\le D\) counts all distinct excursions with at most \(D\)
defects, over all actual positive sources.

On an orbit with no repeated state, distinct excursion occurrences have
distinct initial states. For every fixed \(D\), there are therefore only
finitely many occurrences with at most \(D\) defects. If there are
infinitely many completed excursions, their defect counts tend to
infinity. This is the exact conclusion justified by the finite counts.
It does not control the increasing-defect excursions or force an
unfinished excursion to return. A cycle cannot be excluded by recounting
its repeated laps.

## 5. Independent finite controls and reproducibility

The independent checker first prescribes exponent words, solves the
endpoint congruence for each inverse cylinder, verifies every inverse
division, and then replays the resulting source through literal shortcut
steps. This construction is separate from the author checkers' small-source
fixtures and their special two-defect family. It imports no author module.

The independent normal and `-OO` runs produce identical reports:

- 28 canonical inverse-cylinder controls from 14 different words and two
  different endpoint lifts per word;
- 14,176 compressed signed subsums, including all subsets for each of those
  controls;
- 2,632 full-path signed subsums, including all-ones exceptions and lone
  defects placed at different positions;
- 56 fixed-pool unit vectors decoded back to the full ordinary path;
- prescribed paths of up to 259 odd steps while the correction equation
  retains a fixed defect count;
- the outside excursion \(17\to13\to5\), all four permitted combinations
  of end extensions around \(29\to11\), two valid but noncanonical paths
  rejected from the canonical interface, and a repeated-cycle control.

These finite checks support the arithmetic review; they do not establish
the universal propositions by enumeration. The external S-unit theorem
is not executed or reproved by either checker.

| Independent artifact | SHA256 |
|---|---|
| `check_core_returns_independent.py` | `d5adbb3851fa042dd705cf1368ca1ec79cc68c0b21b0d7380018ef37ba1a3fb6` |
| `core-returns-independent-report.json` | `8644ed6c2e64b866eddf18e31346193d9e61f4be29c844181eff677ef89c6f48` |
| `core-returns-independent-report-oo.json` | `8644ed6c2e64b866eddf18e31346193d9e61f4be29c844181eff677ef89c6f48` |

When the eight author artifacts are in another directory, run:

```bash
python3 check_core_returns_independent.py --reviewed-dir /path/to/author/artifacts
python3 -OO check_core_returns_independent.py --reviewed-dir /path/to/author/artifacts
```

If they are next to the independent checker, the directory argument can
be omitted. The checker rejects any change to a pinned author artifact.
It does not contain a machine-specific workspace path.

## Remaining unsupported step toward convergence

The results prove finiteness for fixed excursion defect budget. Global
closure would additionally need a theorem controlling excursions whose
defect counts grow without bound, or another argument that precludes the
remaining orbit behavior. No such theorem is supplied by these notes or
by this review. The bounded-defect conclusion cannot be promoted to an
unbounded-defect conclusion by taking a countable union of finite sets.
