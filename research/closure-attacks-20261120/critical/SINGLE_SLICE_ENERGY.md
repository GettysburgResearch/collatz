# One multiplicative-five slice: an exact energy bridge and the first gap

**Status: PROPOSED local analytic theorem; global propagation OPEN.** This
note does not turn a conditional descent into an unproved summability
estimate. It records the actual source maps and the harmonic weights.

Use the positive shortcut map and an invariant metric label
\(f:\mathbb N_{>0}\to(Y,d)\). Put

\[
 e_5(x)=d(f(5x),f(x)),\qquad
 E_5(s)=\sum_{\substack{x\ge1\\x\text{ odd},\ 3\nmid x}}
             \frac{e_5(x)}{x^s},\qquad s>0.
\]

Exact doubling gives \(e_5(2x)=e_5(x)\), hence

\[
 \sum_{\substack{x\ge1\\3\nmid x}}\frac{e_5(x)}{x^s}
 =\frac{E_5(s)}{1-2^{-s}}.                              \tag{1}
\]

At the old five-ray parameter \(t=4x\), ordinary trajectories give
\(f(4x)=f(x)\) and \(f(20x+1)=f(5x)\). Therefore its energy on the
single slice \(v_2(t)=2\), \(3\nmid t\), is exactly \(4^{-s}E_5(s)\).
No higher even valuation enters.

## SE-001. A bounded two-query comparison on two residue classes

For every positive \(n\equiv1\pmod4\), \(3\nmid n\), set

\[
 b=\frac{3n+1}{4},\qquad a=\frac{15n+1}{4}=5b-1.
\]

The ordinary paths \(T^2(n)=b\), \(T^2(5n)=a\) are legal, and
\(a+1=5b\). Consequently

\[
 \boxed{d(f(a+1),f(a))\le e_5(n)+e_5(b).}               \tag{2}
\]

Both query parameters are ternary units. The second can be even; (1)
handles its odd part exactly. Writing \(n=4m+1\) shows

\[
 a=15m+4,\quad b=3m+1,\quad m\ge0,\quad m\not\equiv2\pmod3.
\]

Thus (2) covers precisely the adjacent edges with
\(a\equiv4,19\pmod{45}\). The excluded class \(a\equiv34\pmod{45}\)
would require the forbidden query \(3\mid n\); it cannot be inserted.

Summing (2) gives, with extended nonnegative sums allowed,

\[
 \sum_{\substack{a\ge1\\a\equiv4,19\ (45)}}
       \frac{d(f(a+1),f(a))}{a^s}
 \le\left[\left(\frac4{15}\right)^s
              +\frac{4^{-s}}{1-2^{-s}}\right]E_5(s).    \tag{3}
\]

Indeed \(a\ge(15/4)n\), and the first query map is injective.
Also \(a=5b-1\ge4b\), the second query map is injective before
stripping powers of two, and its image is a subset of all positive ternary
units. Equation (1) therefore accounts for the entire infinite odd-part
multiplicity. In particular,

\[
 \sum_{a\equiv4,19\ (45)}\frac{d(f(a+1),f(a))}{a}
 \le\frac{23}{30}E_5(1).                               \tag{4}
\]

The value \(23/30\) is merely the exact result of these two elementary
bounds; no optimization or numerical significance is claimed.

## SE-002. What would make this a closing endpoint argument

The neighboring conditional theorem proves that \(E_5(s)=0\) forces
\(f\) to be constant, because every individual M5 query then vanishes.
It does **not** prove

\[
 E_5(1)<\infty\quad\Longrightarrow\quad f\text{ constant}. \tag{5}
\]

A sufficient new transport statement would be an ordinary estimate

\[
 \sum_{n\ge1}\frac{d(f(n+1),f(n))}{n}
 \le C E_5(1),                                         \tag{6}
\]

or a finite-energy comparison from the M5 defect to the full tripling
defect. To see that (6) suffices under PD, first apply any bounded
real 1-Lipschitz test to the metric label. Exact doubling means that
comparing its values at \(\lfloor2^{k+1+t}\rfloor\) and
\(2\lfloor2^{k+t}\rfloor\) charges only adjacent changes.
Their \(L^1\) costs summed over \(k\) are bounded by the left side
of (6), so these real logarithmic profiles have an \(L^1\) limit. The
unconditional ordinary tripling upper bound from PR146, together with
its ordinary variation comparison, makes that limit invariant under
rotation by \(\log_2 3\); it is therefore a constant. The positive
lower density argument with the separating test in CS-003 then gives
constancy of \(f\).
This paragraph is a conditional continuation, not a proof of (6).

The precise unresolved task is to propagate the two residue classes in
(3) to all required adjacent comparisons while keeping finite weighted
multiplicity. The algebraic selector in M5-003 uses at most three M5
queries per stage and \(O(\log n)\) stages, but a query at an affine
parameter can have a very small odd part. Repeating the descent can
revisit such small queries for many starting sources. Neither the number
of stages nor the one-stage height bound controls the sum in (6).

For the PR146 sparse target \(a=54j+1\), equation (2) directly covers
the full class \(j\equiv2\pmod5\): its queries are
\(n=(72j+1)/5\) and \(b=(54j+2)/5\), both positive ternary units,
and \(n\equiv1\pmod4\).

One further ordinary transport, supplied independently by the merger
agent, covers \(j\equiv4\pmod5\). If \(z\equiv1\pmod4\),
the two adjacent sources \(z,z+1\) have actual two-step images
\((3z+1)/4,(3z+1)/4+1\). Thus, writing
\(A_f(a)=d(f(a+1),f(a))\),

\[
 A_f(a)=A_f((4a-1)/3)\qquad(a\equiv1\pmod3).            \tag{7}
\]

At \(a=54j+1\), its right side is \(A_f(72j+1)\).
For \(j\equiv4\pmod5\), \(72j+1\equiv19\pmod{45}\),
and the M5 queries are now
\(n=(96j+1)/5\), \(b=(72j+2)/5\). They again lie in the correct
unit domains and \(n\equiv1\pmod4\). Both maps in (7) are
injective, and \((72j+1)/(54j+1)<4/3\). Therefore the two full
quinary classes together satisfy

\[
 \sum_{\substack{j\ge1\\j\equiv2,4\ (5)}}
   \frac{A_f(54j+1)}{(54j+1)^s}
 \le \left(1+(4/3)^s\right)
       \left[(4/15)^s+\frac{4^{-s}}{1-2^{-s}}\right]E_5(s).
                                                               \tag{8}
\]

At \(s=1\) the constant in this bound is \(161/90\). The two
image sets can overlap; bounding the two sums separately is why (8)
does not assume disjointness. The remaining three quinary classes have
not been covered by a universal finite weighted construction. No broader
residue census was used to assert such a cover.

## Sources and finite verification

The ordinary convention and old restricted-domain descent are from PR154,
`fe40bb6f88e8094290ef01207d9bf7c4798d35d0`,
[component/PROOF.md](https://github.com/GettysburgResearch/collatz/blob/fe40bb6f88e8094290ef01207d9bf7c4798d35d0/research/structural-reset-20261120/component/PROOF.md).
The new single-slice theorem is the separately authored
[SINGLE_MULTIPLIER.md](../merger/SINGLE_MULTIPLIER.md), reviewed in
[M5_REVIEW.md](M5_REVIEW.md). Equations (1)--(4) above are elementary and
use no external theorem. The conditional continuation uses the explicit
PD/UP/EP source boundaries in [CRITICAL_SINGULARITY.md](CRITICAL_SINGULARITY.md).

Concurrent PR157,
`64361ecca770092d6c8242dc6211e38818af2e50`,
[merger.md](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md),
contains a stronger one-sided forward-five basin criterion. This note
does not claim to advance that merger requirement. Its weighted local
comparisons are separate from either conditional global descent.

`check_single_slice_energy.py` verifies both allowed affine cells, both
actual two-step paths, the exact weight constants, and the excluded
ternary class. It also checks the two-step adjacent transport and both
sparse-target reparameterizations on their full affine cells. These finite
checks do not certify the limiting
arguments and do not fill the global propagation gap.
