# Escaping rays force local excess in the spatial integer trace

**SOURCE-QUALIFIED written deduction.** Let `T` be the shortcut map, let
`U` be its first return to odd positive integers, and put
\(\delta=\tfrac12\log(4/3)\). Use Valbuena's nonnegative stationary
envelope \(E\) for full additive Haar probability on \(\mathbb Z_3\).
Its integral is one. At each positive integer \(n\), its value is
\(g(n)=\delta G_n nD_n\), with \(D_n\) the natural mean of the
reciprocal first-hit correction and \(G_n=1\) for nonperiodic targets.
These are cited theorems, with outsider-reported Lean checks. We inspected
the primary TeX at the pin below and did not rebuild its Lean bundles.

Choose any finite collection of odd ternary units \(u_i\) on pairwise
disjoint escaping components. Write
\[
 m_i=D_{u_i}/P_\infty(u_i)>0,
 \qquad P_\infty(u)=\prod_{j\ge0}\left(1+\frac1{3U^j u}\right).
\]
First-hit positivity and uniform reciprocal packing on a simple orbit give
these assertions. For any fixed \(c>3/2\) and integers \(Y\to\infty\),
\[
 \liminf_{Y\to\infty}\frac{1}{\#I_Y}\sum_{n\in I_Y}g(n)
 \ \ge\ 1+\frac{2\delta}{c-1}\sum_i m_i,
 \qquad I_Y=\{n\text{ odd}:Y\le n<cY\}.                 \tag{1}
\]
In particular one sequence of increasing shells on which this **ordinary
unweighted spatial mean** approaches at most one would exclude escape.
This condition does not exclude an additional finite cycle.

For an odd iterate \(y=U^j u_i\), concatenate first-hit paths from sources
reaching \(u_i\) with the segment from \(u_i\) to \(y\). An earlier hit of
\(y\) before \(u_i\) would put both on a cycle. Thus
\(D_y\ge D_{u_i}/P_\infty(u_i)=m_i\), and \(g(y)\ge\delta m_i y\).
An injective integer orbit leaves every fixed finite set. Its first odd
iterate \(y_i\ge Y\) satisfies \(y_i\le(3(Y-1)+1)/2<cY\) for all
large \(Y\), since the preceding odd value is below \(Y\). Points from
the finitely many selected components are distinct. In fact the same limit
in (1) is valid for \(c=3/2\), with integer \(Y\) as stated.

For fixed conductor \(k\), let \(e_k\) be the infimum of \(g\) over
ordinary positive roots in each ternary residue class. The envelope theorem
gives \(e_k\uparrow E\), and \(e_k\) is finite and bounded at any fixed
\(k\). Its mean over the odd interval \(I_Y\) tends to its Haar integral
because the odd grid cycles through all residues. At each of the distinct
\(y_i\), replacing \(e_k(y_i)\) by \(g(y_i)\) gains at least
\(\delta m_iY-\|e_k\|_\infty\). First take the lower limit in \(Y\),
using \(\#I_Y\sim(c-1)Y/2\), and then take \(k\to\infty\). Monotone
convergence gives (1), without an upper estimate on any moving conductor.

**Priority and difference in observables.** Valbuena's earlier divergent
raw-occupation theorem obtains the same underlying first-hit factorization
and a strictly positive excess in \(\sum_{n\le R,\ n\text{ odd}}D_n/\log R\).
Its baseline is provided by the pre-barrier clock. Equation (1) uses his
lower semicontinuous envelope to place the excess in *every* sufficiently
large fixed-ratio odd shell of the cycle-corrected integer trace, with an
unweighted spatial average. A global integrated lower coefficient by itself
need not imply this short multiplicative-shell conclusion. Neither result
proves its matching upper estimate.

[Envelope, definitions and proof](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex)
· [Raw occupation and its divergent excess, Section 12](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex)
