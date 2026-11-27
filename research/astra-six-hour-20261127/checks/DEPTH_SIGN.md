# The tempting finite signed inequality is false

**EXACT INTERVAL COMPUTATION.** This check concerns the original independent
geometric Syracuse law. It tests a possible strengthening of the
[unscaled depth detector](../collision/DEPTH_DIFFERENCE.md), not the
existence of an escaping orbit.

Put \(q=3^{k+1}\) and

\[
S_k=\sum_{\substack{0<y<2q\\y\text{ odd}}}
       {\rho_{k+1}(y)-\rho_k(y)\over y}.
\]

The signed detector theorem would exclude escape if one proved
\(\liminf_k S_k\le0\), using its stated two-sided trace input. The stronger
claim \(S_k\le0\) at every finite depth is false. The exact integer
enclosure gives

\[
0.00070650824182767 < S_{13} < 0.00070650824182769.
\]

The first five values are negative. The particularly simple exact values
are \(S_0=-2/15\) and \(S_1=-12834/119119\). The absolute norm is already
nonmonotone: \(D_0=8/15\), while \(D_1\) is approximately 0.667769.
Neither the finite positive sign nor the norm increase contradicts the
summable-error propagation theorem, and neither is an escape witness.

## Integer enclosure proof

[check_depth_difference.cpp](check_depth_difference.cpp) uses the exact
one-step identity, with arguments interpreted at their respective periods,

\[
\rho_k(r)={1\over2}\rho_k(2r)+{3\over2}
 {\bf1}_{r=2\bmod3}\rho_{k-1}((2r-1)/3).
\]

At depth \(k\), start with 112 terms of this identity at \(r=1\), then
propagate backwards around the entire unit cycle modulo \(3^k\). The code
checks that its cycle visits every unit exactly once. Nonunits have density
zero. All calculations use lower integers \(L_k(r)\) with scale \(2^{88}\).
No floating-point operation is used.

Inductively, maintain

\[
0\le2^{88}\rho_k(r)-L_k(r)\le\varepsilon_k,
\qquad \varepsilon_0=0,\quad
\varepsilon_k=3\varepsilon_{k-1}+114.
\]

The full positive operator has maximum row sum two, so
\(\rho_{k-1}\le2^{k-1}\). The omitted 112-term tail in the unrolled
half-contraction therefore costs less than one scale unit for
\(1\le k\le14\). The old-density errors cost at most
\(3\varepsilon_{k-1}\), and the individual downward roundings cost less
than 112 units. A backwards update costs at most one more rounding unit
and preserves the stated error bound. The 128-bit arithmetic has ample
range: individual intermediates are below \(2^{105}\), and even the crude
bound obtained by adding the absolute numerators over all representatives
is below \(2^{127}\).

For each odd \(y\), the exact density difference is enclosed between
\(L_{k+1}(y)-L_k(y)-\varepsilon_k\) and
\(L_{k+1}(y)-L_k(y)+\varepsilon_{k+1}\), divided by the common scale.
Directed **integer** floor and ceiling division by \(y\), followed by
addition, gives rational enclosures for both signed and absolute norms.
The lower numerator for \(S_{13}\) is strictly positive.

As an independent check, [check_depth_intervals.py](check_depth_intervals.py)
constructs the complete geometric exponent period using exact Python
fractions through depth five. It does not use the backward half-contraction
recurrence. All ten resulting signed and absolute quantities lie in the
integer intervals.

## Replay and evidence boundary

With a C++ compiler supporting `__int128`, compile and run the C++ source,
saving its JSON stdout. Then run the Python checker with that JSON path
and `--output` followed by a report path. The checked range is hard-coded;
no arithmetic-range assertion is made for larger depths.

[Exact interval report](../../../reports/astra-six-hour-20261127/checks/depth-difference-intervals.json)
and [independent exact-law check](../../../reports/astra-six-hour-20261127/checks/depth-difference-independent.json)
record the executed checks. These computations have not been turned into
a Lean kernel certificate. The asymptotic signed inequality remains open.
