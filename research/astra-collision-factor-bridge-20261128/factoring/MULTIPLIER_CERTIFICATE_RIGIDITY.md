# What a finite Collatz merger certificate can do to a multiplier

**PROPOSED written result; three algebraic/ordinary-replay roots checked in Lean.** Map: \(T(2n)=n\), \(T(2n+1)=3n+2\). A merger below may use different clocks on its two arms. This is a statement about bounded finite certificates, not about failure of eventual convergence.

## The exact two-source theorem

For a finite parity word \(w\), let \(\ell(w)\) be its shortcut length, \(g(w)\) its number of odd departures and \(A(w)\) its nonnegative affine numerator. On every positive ordinary source that actually realizes \(w\),

\[
  2^{\ell(w)}T^{\ell(w)}n=3^{g(w)}n+A(w).
\]

Let \(a,b\) be nonnegative integers. Suppose two **distinct** ordinary sources \(n,m\) realize one common word \(w\), their affine images \(an+b,am+b\) realize another common word \(v\), and the two actual pairs merge at those respective word lengths. Then

\[
  2^{\ell(v)}3^{g(w)}
     =a\,2^{\ell(w)}3^{g(v)}.                                  \tag{M1}
\]

Indeed clear the two powers of two in each merger equation. The resulting affine polynomial in the source vanishes at both \(n\) and \(m\). Subtracting makes its leading coefficient times \(n-m\) zero, proving (M1). The constants need not agree separately before this argument.

If a prime \(p\ne2,3\) divides \(a\), the right side of (M1) is divisible by \(p\), while the left side is not. Consequently a fixed pair of parity words can certify **at most one** positive source for such a multiplier, however large the permitted words are.

For odd \(a>0\), (M1) also forces \(\ell(w)=\ell(v)\), by comparing 2-adic valuations, and then \(a=3^r\) for some nonnegative integer \(r\). More generally, for a positive rational slope the only possible slopes on a two-source affine cell belong to \(2^{\mathbb Z}3^{\mathbb Z}\). The Lean endpoint used here is the cleared identity and the prime-divisor consequence; this final valuation classification is a written corollary.

### Formal connection to actual paths

[AffineMultiplierRigidity.lean](AffineMultiplierRigidity.lean) imports the previous packet's actual shortcut map and parity-word theorem. Its public roots are:

- \(\texttt{two_point_word_slope}\): the rational affine calculation.
- \(\texttt{actual_two_point_slope}\): consumes four genuine ordinary word realizations and two genuine endpoint equalities.
- \(\texttt{prime_multiplier_cell_unique}\): excludes two distinct sources when the multiplier has a prime divisor other than two and three.

The accompanying [audit module](AffineMultiplierRigidityAudit.lean) separately imports the compiled object and prints every public root's axioms. The fresh compilation receipt is in [reports](../../../reports/astra-collision-factor-bridge-20261128/factoring/lean-runner-receipt.json). The only reported axioms are \(\texttt{propext}\), \(\texttt{Classical.choice}\) and \(\texttt{Quot.sound}\). No infinite-density theorem or complexity lower bound is formalized.

## A uniform finite-clock census bound

Fix \(a,b\ge0\) with some prime \(p\ne2,3\) dividing \(a\), and a nonnegative integer \(h\). Put

\[
 E_h(a,b)=\{n>0:\exists\,s,t\le h,\ T^s n=T^t(an+b)\}.
\]

Then the **entire set**, without any source-height cutoff, satisfies

\[
                  |E_h(a,b)|\le (2h+1)2^h.                    \tag{M2}
\]

To see this, extend both arms of a merger by the same number of further steps until one clock equals \(h\). There are \(2h+1\) possible resulting clock pairs \((h,t)\) or \((s,h)\), counting \((h,h)\) once. The first \(h\) parity departures of \(n\) are determined by \(n\bmod2^h\), and those of \(an+b\) by the same residue. This is the ordinary finite-cylinder property, obtained inductively from the two branches of \(T\). For each clock pair and each residue, all candidate sources have fixed words \(w,v\). The two-source theorem allows at most one of them. Summing proves (M2).

In particular, for any fixed \(\epsilon>0\), two-arm mergers through

\[
 h(X)\le(1-\epsilon)\log_2X
\]

occur for only \(O((\log X)X^{1-\epsilon})=o(X)\) of the sources through \(X\). The estimate is uniform in \(a,b\), subject to the displayed prime-divisor condition, so these may also vary with \(X\). This does **not** conflict with universal Collatz: a successful path can have clocks of order \(4.819\log_2X\), well beyond the range in which (M2) saves a power. It also says nothing about a merger with one unbounded arm.

The result is a finite-cell obstruction. It does not prohibit a short program from describing many cells, a proof using unbounded clocks, or a global arithmetic argument.

## A sharper boundary: the corresponding Haar merger event is null

Extend the shortcut map to the two-adic integers by its ordinary even and odd formulas. Let \(a,b\in\mathbb Q\) have odd denominators, and assume \(a\notin2^{\mathbb Z}3^{\mathbb Z}\). Then

\[
 \{x\in\mathbb Z_2:\exists s,t\ge0,\ T^s x=T^t(ax+b)\}
\]

is **countable and Haar-null**. In fact every one of its elements is rational.

For a specified pair of finite words, the equality is one affine equation in \(x\), with rational coefficients. Its leading coefficient is nonzero by the excluded slope condition. It consequently has at most one solution, which is rational if it exists. There are countably many finite word pairs. A singleton of \(\mathbb Z_2\) has Haar measure zero because it lies in a cylinder of measure \(2^{-k}\) at every precision \(k\). Countable subadditivity gives the conclusion. Intersecting with the actual word cylinders only removes possible solutions.

For every prime multiplier \(a>3\), a proposed Haar-almost-sure merger of \(x\) and \(ax+b\) is therefore **false**, even if both clocks are allowed to be arbitrarily large. This is compatible with every positive ordinary integer converging: the ordinary integers are themselves countable and Haar-null. The successful ordinary paths would lie in precisely this exceptional population. A full ordinary argument must use the finite binary expansion or another arithmetic property of those points; a generic fresh-suffix Haar argument cannot supply the missing product/factor merger.

More generally, for a nonaffine polynomial \(f\in\mathbb Q[X]\) mapping the domain in question into \(\mathbb Z_2\), every pair of word charts gives a nonzero polynomial equation \(3^u x+c=2^r3^v f(x)+d\). It has finitely many roots. Thus the set of eventual mergers of \(x\) and \(f(x)\) is again countable and Haar-null. The affine smooth-slope case is the only case in which a whole word cylinder can survive this algebraic test. This extension is written, not among the three formal roots.

## Why this matters for the factoring import

Factoring PR #296 constructs useful permutations of \((\mathbb Z/2^w)^\times\), and then inverts positions at \(N=pq\bmod2^w\). One must choose how a modular output is supposed to become an ordinary Collatz source.

1. **Use an actual multiplication \(n\mapsto an+b\).** For a multiplier carrying a prime other than two or three, a fixed pair of native parity charts never supplies a two-source merger cell. The modular inverse identity is not such a diagram.
2. **Keep the high quotient and permute only the low \(w\) bits.** This gives a piecewise translation. Fixed-width translation coalescence can apply as the outer source height tends to infinity, but it changes only a bounded-size block and does not mix different component masses on the outer scale.
3. **Discard the high quotient and output a small recovered residue.** A theorem preserving the ordinary component under this operation would itself be a strong descent theorem. The factoring proof recovers a curve label, not a Collatz state in the same component.

These three possibilities isolate a real missing construction. They prevent a CRT identity, a factor-recovery program, or a residue permutation from silently becoming an ordinary-orbit certificate.

## An attempted escape: approximate the multiplier by powers of two and three

For \(a>3\), one can approximate \(a\) by \(3^r/2^s\). But replacing \(an\) by the nearby smooth multiple leaves displacement

\[
   \left|a-\frac{3^r}{2^s}\right|n .
\]

At the logarithmic native horizons supported by exact ordinary cylinder transport, the known pair/family bounds require a displacement whose logarithm is much smaller than the available source precision. A relative approximation by an inverse power of \(\log n\) still leaves displacement with logarithm \((1+o(1))\log n\). The published offset estimate therefore gives no vanishing error. Taking very large exponents changes the actual clock and height budget; binary modular exponentiation does not shorten an ordinary Collatz itinerary.

This attempt is **BLOCKED**, not disproved in every possible form. A useful repair must prove a real, source-dependent merger or return theorem beyond the presently controlled finite-certificate regime.
