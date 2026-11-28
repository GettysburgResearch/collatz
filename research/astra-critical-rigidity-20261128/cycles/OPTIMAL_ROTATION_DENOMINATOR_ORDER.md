# The reciprocal mismatch-budget order of the complete denominator exponent

**Proposed written theorem.** For an integer \(s\ge4\), let \(c_s\) be the lower limit of \(\log_3 q/p\) over positive primitive rational odd cycles with odd period \(p\to\infty\) admitting a proper rotation of the valuation word with at most \(s\) mismatches. Here \(q\) is the common full reduced denominator. Let \(L_s\) be the largest positive odd integer with \(4L_s\le s\), and let \(\gamma=\log_2 3\). Then
\[
       \frac1{4\gamma s}
                    \ \le\ c_s\ \le\ \frac1{2L_s}.
                                                                    \tag{1}
\]
In particular \(c_s=\Theta(1/s)\) as \(s\to\infty\). The upper bound still holds if one additionally requires the witnessing rotations to have orders tending to infinity, the widths to be \(2+O(p^{-1+o(1)})\), the minima to be at least \(p^{2-o(1)}\), and the positive clock defects to be at most \(p^{-1+o(1)}\). The lower estimate is the [postmismatch event-height theorem, equation (3)](MISMATCH_EVENT_HEIGHT.md), converted to base three. It sharpens the original [all-fixed-budget estimate, equation (11)](ALL_FIXED_ROTATION_DENOMINATORS.md). The upper estimate determines the order of dependence on the mismatch budget.

There is also an unconditional finite restriction at every genuine cycle. If \(r\) is its minimal chronological recurrence degree and a proper rotation has \(u\) mismatches, then
\[
                         u(r-1)\ \ge\ p.                             \tag{2}
\]
Thus even when the budget grows, at least \(p/u+1\) chronological dimensions remain. For any cycle sequence already satisfying \(\log_3q/r\to1\), this gives \(\liminf u\log_3 q/p\ge1\).

## The native comparison sequence

Write \(a_i\) for the actual valuations, \(E_{i+1}-E_i=a_i\) and \(U_i=2^{E_i}\) on the whole periodic lift, with \(E_{i+p}=E_i+A\). For any supplied proper shift \(\ell\), let \(D_i=E_{i+\ell}-E_i\). The integer \(D_i\) changes at exactly the \(u\) positions where \(a_{i+\ell}\ne a_i\). Its constant circular runs cover all \(p\) positions. Primitivity gives \(u>0\), since a valuation period would reproduce the positive fixed point of the corresponding proper repeated affine word.

For a constant value \(D\) on any one of these runs, the nonzero sequence
\[
                         W=(S^\ell-2^D)U
\]
vanishes identically on that run. It cannot vanish identically on the whole lap, since that would make \(D_i\) constant everywhere. The degree-\(r\) monic chronological annihilator \(f\) annihilates \(W\): the genuine physical update gives \(U=(S-3)V\) for \(V_i=2^{E_i}x_i\), and \(f(S)V=0\). A block of \(r\) zeros would force every later value to vanish by the monic recurrence, hence the entire sequence by \(W_{i+p}=2^A W_i\). Every run therefore has length at most \(r-1\), proving (2). This argument can be used separately at each proper shift. [Minimal recurrence and its complete denominator](MINIMAL_RECURRENCE_DENOMINATOR.md)

## Positive cycles with exactly \(4L\) native valuation mismatches

Fix any odd \(L\ge1\) and any integer \(a\ge2\). Use \(g=2^aL\) sheets and the two marked ranks of the [nearcritical sheet-mask construction](NEARCRITICAL_DENOMINATOR_SPECTRUM.md). The first mask \(v(k)=1_{\{k=0\bmod L\}}\) is invariant in the two-power coordinate. The second is \(h_a(k)=1_{\{[k]_{2^a}<2^{a-1}\}}\). For any sufficiently large upper convergent \(B/P\) used there, the genuine primitive cycle has \(p=gP,\ A=gB\). The proven Fourier support and complete resultant estimate give
\[
                     r/p=1/(2L)+2^{-a},\qquad
                     \log_3 q/r\longrightarrow1
\]
at fixed \(a,L\) as \(P\to\infty\). The physical width, minimum and clock bounds in the opening apply after the same finite-stage diagonal.

Choose \(t\) modulo \(g\) with \(t=0\bmod L,\ t=1\bmod 2^a\). The shift \(\ell=tP\) has order \(2^a\) on the actual odd-period circle. Each position has the same reduced rank after shifting; its sheet advances by \(t\). Thus the first mask is unchanged. The second mask and its translate differ exactly at the two endpoint residues of the half interval, each with \(L\) possible odd-factor coordinates. The calendar error \(\epsilon_{i+\ell}-\epsilon_i\) is nonzero at exactly \(2L\) native positions in one full lap, all at the same reduced rank. Any two such positions are separated around the cycle by at least \(P>1\). As \(\ell\) is a multiple of \(P\), the nominal cumulative difference \(\lfloor(i+\ell)B/P\rfloor-\lfloor iB/P\rfloor\) is constant. A nonzero isolated calendar change therefore contributes exactly two distinct true valuation mismatches, one on entry and one on exit. There are exactly \(4L\) in total, including the cyclic seam.

Now let \(a\to\infty\) for fixed \(L\), choosing the convergent after each \(a\) so the normalized full denominator differs from the normalized degree by \(o(1)\), and \(\log(g+2)/\log P\to0\). This proves the upper estimate at \(L=L_s\) with increasing rotation order. More generally, for **every** prescribed \(H(p)\to\infty\) there is a sequence of genuine cycles and proper rotations with \(u\to\infty,\ u\le H(p)\), the same nearcritical geometry, and
\[
                         \frac{u\log_3 q}{p}\to 2,\qquad
                         \frac{\log_3 q}{p}\to0.
\]
For this take odd \(L\to\infty\), choose \(2^a/L\to\infty\), and at each finite stage choose \(P\) also large enough for \(H(gP)\ge4L\) and \(|\log_3q/r-1|\to0\). No explicit onset in \(s\) or in the stagewise resultant estimate is being assumed. This establishes a sharp contrast of quantifiers for the rational exponent. The question whether ordinary cycles with increasing odd-valuation mismatch counts can exist remains open.
