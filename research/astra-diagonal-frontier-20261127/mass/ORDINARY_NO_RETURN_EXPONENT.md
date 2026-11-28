# The ordinary fixed-root no-return mass has exponent minus one

At each nonperiodic positive odd unit \(z\), let \(d_z\) be its relative odd natural predecessor density and \(q_z=Q_z(S_i>7i/4\text{ for all }i\ge1)\) under the ordinary natural entrance law. For every \(\epsilon>0\) there are absolute \(c>0\) and \(C_\epsilon<\infty\) such that
\[
                  {c\over z}\le d_zq_z\le C_\epsilon z^{-1+\epsilon}.
                                                                          \tag{1}
\]
There is no permanent-orbit assumption in this statement. For a permanent odd unit, periodic or nonperiodic, the analogous bounds hold for its first-entry atom \(\mu_z\). Thus each constrained natural mass has logarithm \((-1+o(1))\log z\) along any sequence of the respective specified roots tending to infinity. The proof combines the [retained physical lower floor](NO_RETURN_LANDING_FLOOR.md) with [relative sparse passage](RELATIVE_SPARSE_PASSAGE.md); both depend on the external inputs specified in those notes.

## Counting the finite source octave

Write \(\omega=2^{7/4}/3>1\) and \(C_*=[3(\omega-1)]^{-1}\). Along any finite actual inverse word with \(S_i>7i/4\) at each positive prefix, its multipliers and offsets obey
\[
 A_i=3^i2^{-S_i}<\omega^{-i},\qquad
 B_j=\tfrac13\sum_{i=1}^jA_i<C_*,
 \qquad v=(z-B_j)2^{S_j}/3^j.                                       \tag{2}
\]
This uses the order of the prefixes from the specified target. For \(z\ge 2C_*\) every such positive-length ancestor \(v\in[Y,2Y)\) satisfies \(v>(z/2)\omega^j\). Take \(Y\ge z\). There are \(O(1+\log(2Y/z))\) possible lengths \(j\), with an absolute constant since the slope is fixed. At a fixed \(j\), the possible totals \(s=S_j\) satisfy
\[
           Y/z\le2^s/3^j<4Y/z .
\]
There are at most three integers \(s\) in this range of width two in the logarithm. At each pair \((j,s)\), (2) places **the distinct ordinary integers** in an interval of length \(C_*2^s/3^j\le4C_*Y/z\); hence there are at most \(1+4C_*Y/z\) of them. The source \(v=z\), corresponding to the empty word, contributes at most one additional integer. Dividing by the number of odd sources in the octave therefore gives
\[
 \Pr\bigl(W_Y\text{ reaches }z\text{ along a word satisfying (2)'s strict gate}\bigr)
   \ll {1\over Y}+(1+\log(2Y/z))\left({1\over z}+{1\over Y}\right).
                                                                         \tag{3}
\]
Overcounting a source or including impossible pairs only increases this upper bound. No distribution of its hitting clock was used.

When \(z\) is permanent the event \(F(W_Y)=z\) entails this exact strict gate on its word to the *first* \(z\), including ties in the reverse record criterion. At a periodic permanent target the same implication holds by considering its first occurrence. Apply the uniform relative estimate (2) of the sparse-passage note to the test selecting \(z\). Choose \(Y=\exp(z^\eta)\) for fixed \(0<\eta<\min(\epsilon,1)\). For all sufficiently large \(z\) one has \(Y\ge z\). The multiplicative error can be absorbed on the left, and choose \(A>1/\eta\) to make the additive \((\log Y)^{-A}=z^{-\eta A}\le z^{-1}\). Equations (2)–(3) yield \(\mu_z\ll_\epsilon z^{-1+\epsilon}\). Absorb the finitely many smaller \(z\) in the constant. The lower estimate for \(\mu_z\) is (2) of the physical lower-floor note.

## An auxiliary label to treat a nonpermanent root

Fix a nonperiodic positive odd unit \(z\). Every input in its basin first reaches \(z\) at a unique depth. Declare a site on this finite path *passing to \(z\)* when each of its forward prefixes through its arrival at \(z\) passes the \(7/4\) gate. The target itself passes using the empty path. Define \(L_z(v)\) as the first passing-to-\(z\) site on that finite physical path, or cemetery if \(v\) does not reach \(z\). Outside the set of passing-to-\(z\) sites the label is invariant over one actual edge. This includes sites outside the basin; \(z\) itself may be an exception.

All such exceptional sites lie in the common PR201 sparse principal set \(D\), apart from a finite region below \(z^2+1\). Indeed, a passing word of length \(j\) from \(y\) to \(z\) has division count \(s\le7j/4\) and \(y\le z2^s/3^j\). If \(3^j\ge z\), then \(y\le2^s<2^{s+1}\), so it is the least positive odd representative for this passing word. If \(3^j<z\), then \(y\le z\omega^j\le z^2\), since \(1<\omega<3\). The empty path is included in this second bound or as a singleton. Thus the sparse-passage theorem first supplies a countable limiting law \(\nu_z\) for fixed \(z\). More precisely its octave estimate for \(L_z\) holds **with constants independent of \(z\) whenever \(Y^{1/\alpha}>z^2+1\)**, where \(\alpha=1.001\). In equations (7)–(8) of the sparse-passage proof every marked departed state exceeds the bottom cutoff \(r\), so the finite exceptions are absent on every rung as soon as \(r>z^2+1\). All remaining constants use the common \(D\). To compare with the limiting law, let the second octave source tend to infinity for that fixed \(r,z\).

The event \(L_z(v)=z\) is precisely the strict inverse-prefix condition of (3) for the finite path to this target. To see this, the seed at reverse depth \(i\) passes all the way to \(z\) exactly when its reverse debt \(7i-4S_i\) is a weak running maximum up to \(i\). Each forward length-\(h\) debt is the difference of the reverse debts at \(i\) and \(i-h\). The absence of any such positive-time weak record is strict negativity at every positive time. This finite argument does not need the future of \(z\) to pass.

In addition \(\nu_z(\{z\})=d_zq_z\). At fixed reverse depth \(k\), the actual conditioned predecessors converge on their cylinder partition to \(Q_z\); sources having fewer than \(k\) inverse letters have natural density zero. For the latter assertion the possible division totals through a source cutoff \(X\) are \(O_{k,z}(1+\log X)\) by the physical product with \(3+1/u\le4\), so only polynomially many words in \(\log X\) need be counted. If a physical predecessor has no record among its first \(k\) reverse letters but has a later one, its label \(L_z(v)\) cannot be \(z\): it is a labeled predecessor of depth \(>k\). The countable total-variation limit puts all but any prescribed \(\epsilon'\) of its finite mass on a finite list of labels. The members of that list reaching this nonperiodic \(z\) each have a unique finite depth. Choose \(k\) beyond all these depths and divide the remaining error by \(d_z>0\). Taking the limits in this order proves the equality. Taking \(Y=\exp(z^\eta)\) as above satisfies \(Y^{1/\alpha}>z^2+1\) for large \(z\), hence (3) proves the upper side of (1). The lower side is the physical positive floor at this same \(z\).

## Consequences for pressure and escape

For a fixed nonperiodic \(z\), let \(K_z\) be the supremum over finite prefix-free families of actual **unit-ended** strict inverse words from \(z\) of the sum of reciprocals of their ordinary terminal ancestors. Allow the empty word. The lower-floor amplification gives \(cK_z\le d_zq_z\). Hence
\[
          {1\over z}\le K_z\ll_\epsilon z^{-1+\epsilon}
\]
without assuming that \(z\) passes. Collecting central clocks or adaptive finite antichains in this strict tree can improve logarithmic factors, but cannot supply a fixed positive power gain over its reciprocal-root exponent.

The actual unrenormalized non-cemetery law has polynomial height tail. The only nonunits with positive-length odd predecessors would contradict \(U(v)\not\equiv0\bmod3\). Thus a finite label at a nonunit \(z\) can occur only at its single input and has zero limiting mass. Let \(P^\times\) denote the permanent odd units. Since \(\#(D\cap[1,X])\ll X^d\) for \(d=H_2(4/7)<1\), a dyadic sum of the pointwise upper bound proves, for \(0<\epsilon<1-d\),
\[
 \mu\{z\in P:z\ge M\}
   \ll_\epsilon M^{-(1-d)+\epsilon}.
\]
This gives every finite moment of order \(s<1-d\) of the finite label height when \(s\ge0\). More generally, comparison of (1)'s bounds on unit atoms shows that for infinite \(P^\times\) the supremum of finite nonnegative power moments is \(1-\limsup_{X\to\infty}\log\#(P^\times\cap[1,X])/\log X\), independent of the behavior at the endpoint exponent. The identity follows by comparing the corresponding Dirichlet series \(\sum_{z\in P^\times} z^{s-1}\) from below and the same series at \(s+\epsilon\) from above.

If a positive unit \(a\) escapes and \(z\) ranges over its later permanent phases, \(d_z\ge d_a>0\). Therefore its actual conditional no-return probability satisfies \(q_z=z^{-1+o(1)}\) on these phases; the same statement holds for every later unit on the ray for the auxiliary target-stopped test. To exclude the escaping ray via an inverse-power-of-logarithm lower bound one would have to contradict this unconditional upper estimate for a root whose full predecessor density stays bounded below. The estimate reconciles first-entry decay and reciprocal multiplicity. It neither proves absence of escape nor rules out additional cycles.
