# Finite transverse critical record current with a first real moment

For a positive odd starting integer \(a\) at a permanent corrected minimum of an escaping component, there is a finite positive measure \(\mathcal M\) on
\[
         (1+2\mathbb Z_2)\times\mathbb Z_3\times(0,\infty)
\]
fixed by the positive-real, quadratic, first-record inverse transfer defined below. It has finite first real moment. Its joint real and ternary projection is absolutely continuous. On the specified binary fibre \(a\) it dominates ternary Haar times Lebesgue measure restricted to \([a,a+1]\). Conversely, a positive fixed measure for this transfer charging a positive ordinary binary fibre forces that integer to escape. No equality of its ternary or real coordinate to the binary integer is needed in this converse.

Use the [critical record words](FINITE_RECORD_CURRENT.md) with \(a_*=\log_2 3\). For each completed outward word \(w\), write \(\omega_w>1\) for its ordinary multiplier and \(y=\omega_w(x+c_w)\) for its chronological forward affine map. The true first \(+1\) gives \(c_w\ge1/3\). When the ternary divisions are admissible, apply the inverse affine map in all coordinates and retain the output exactly when its real coordinate \(r'=r/\omega_w-c_w\) is positive. Weight the edge by \(\omega_w^2\). Write \(\mathcal K_2\) for this transfer on tests. Every positive inverse chain of record length \(k\) has \(k<3r\) at initial real height \(r\). This last assertion applies to noninteger real marks as well. The underlying rational affine and chain inequalities are formally proved in [RecordAffine.lean](RecordAffine.lean).

## The quadratic Haar estimate below the physical cut

Given a fixed real \(r>0\) and a full Haar ternary coordinate, a prescribed word of raw length \(l\) has eligibility probability \(3^{-l}\); conditional on success, its output again has full Haar law. The squared expected raw letter weights are the iid probability \(p(e)=3\,4^{-e}\). Its exponent mean is \(4/3<a_*\), so it completes a first record almost surely, also from any finite unfinished outward excess. For complete record words the expected mass sums to one and
\[
           \sum_w3^{-|w|}\omega_w^2\omega_w^{-1}=p_1<1.
\]
Here \(p_1\) is the genuine record probability under iid fair gaps \(2^{-e}\), as proved in the critical record note. For the Green sum over all record generations, including the initial point, the expected mass is at most \(1+3r\). Its expected first real moment is at most \(r/(1-p_1)\): a surviving endpoint has \(r'\le r/\omega_w\), so each further generation contracts the expected positive height by at least the indicated geometric factor. These Haar conclusions may be used with any fixed binary coordinate. [Weaver, quadratic gap law and normalized integer ball masses, Paper 9 v2](https://rstation.ai/problems/collatz/papers/9).

## Cut at raw grade zero, including a partially completed record word

Give \(a\) raw odd grade zero, so \(g(Ux)=g(x)+1\). Use \(P(Ux)=(3/2^{e(x)})P(x)\) and \(x\le P(x)\le Kx\). At the successive permanent sites \(y_i\) of the forward orbit, couple the triple
\[
   \big(y_i,\ y_i+G_i\eta,\ y_i+G_i\xi\big),\qquad
   G_i=P(y_i)/P(a),\quad \eta\sim m_3,\quad \xi\sim\mathrm{Unif}[0,1]
\]
with independent perturbations. The same true affine record word connects every consecutive pair in all three coordinates. Its positive real endpoints ensure that the inverse branch is retained. Take the Green measure from this triple, average and normalize by \(G_i^{-2}\). The sequence increases as measures, since the next Green contains the whole previous Green through that known branch with exactly compensating weight.

For a raw inverse prefix stopping at grade \(v\ge0\), the perturbation is integral through each required division. Eligibility of such a prefix agrees with the true ordinary target, since the initial perturbation vanishes modulo \(3^{g(y_i)}\). Its raw endpoint \(x\) is a genuine positive odd integer, its normalized squared weight is \((P(a)/P(x))^2\), and its real coordinate is \(x+(P(x)/P(a))\xi\). If it ends on a completed record, it is a permanent site. In a fixed Green expansion each such integer occurs once because its forward path to \(y_i\) has a unique raw word and outward first records have a unique successive parsing. The combined mass and first real moment of these outputs is at most a constant depending on \(a\) times
\[
                       \sum_{x\in S_{a_*}}\big(P(x)^{-2}+P(x)^{-1}\big)<\infty,
\]
by the actual dyadic source entropy bound of the record note.

For each branch running below raw grade zero, cut at its unique ordinary grade-zero prefix endpoint \(b\). Its ternary coordinate is full Haar, as \(P(b)/P(a)\) is a dyadic unit at 3. Let \(c\) be the last completed record at or above the cut, using \(c=b\) when a record ends there. Otherwise the unfinished outward prefix has multiplier less than one, so \(P(c)\le P(b)\). At its first completed record *below* the cut the positive real coordinate is bounded above by the real coordinate at \(c\), hence by \(C_aP(b)\). The total expected squared suffix weight up to this first completion is at most one: with full Haar at the cut it is the iid \(3\,4^{-e}\) first-crossing law from the known unfinished excess, with any nonpositive terminal real discarded. Conditional on each completed suffix the terminal ternary coordinate is again full Haar, independently of the real perturbation subject to the retained real condition. Apply the preceding Green estimates there. The entire below-cut contribution to mass plus first moment is bounded by
\[
              C_a\sum_{g(b)=0} P(b)^{-2}(1+P(b))<\infty .                \tag{1}
\]
The last step is the finite *physical* reciprocal mass of grade zero, not an estimate on all grades combined. In a fixed expansion each cut prefix \(b\) is unique; completing all its possible suffixes includes all endpoints below the cut. [Original grade reciprocal bound](../../astra-unconventional-20261126/boundary/TRACE_PROFILE.md).

The bounds are uniform in \(i\). Monotone convergence now yields the asserted finite limit and finite first real moment. The Green resolvent defect is the starting-point law times \(G_i^{-2}\to0\); hence \(\mathcal K_2^*\mathcal M=\mathcal M\). Every finite word sends the independent absolutely continuous real and ternary perturbations to an affine image restricted by a ternary cylinder and an open real half-line, so absolute continuity survives the countable Green sum and increasing limit. The initial term at \(a\) supplies the stated fibre lower bound. This is an archimedean-positive record variant of the [earlier, subquadratic full-step transverse construction](../../astra-unconventional-20261126/global/TRANSVERSE.md).

For the converse let a positive binary integer \(x\) have nonzero marginal mass. The fixed equation on that fibre gives at least one inverse word whose source fibre has positive mass and whose terminal binary result is \(x\). Reading this word forward from \(x\), oddness at every binary phase forces its exponents to be precisely the actual valuations. Its forward endpoint \(y\) is therefore an ordinary integer and \(y=\omega_w(x+c_w)>x\), irrespective of the separately carried real coordinate. Iterating gives an unbounded subsequence on the true trajectory of \(x\). A repeated positive state would make that orbit ultimately periodic and bounded, so the trajectory escapes.

## The first-moment projection and the precise loss on returning to all odd steps

Let \(\nu\) be the projection of \(r\mathcal M\) to the binary and ternary coordinates. For every nonnegative bounded local test \(f\),
\[
 \int f\,d\nu=\int \sum_{w\,\mathrm{eligible}}\omega_w^2
                       (r/\omega_w-c_w)_+f(I_w)\,d\mathcal M .           \tag{2}
\]
The first-power **record** transfer \(K_1^*\nu\) therefore dominates \(\nu\) plus the positive defect obtained by replacing the real prefactor on the right with \(\min(\omega_w r,\omega_w^2 c_w)\). The defect is genuinely positive, for example on the retained edge from the next physical record back to \(a\). The potentially unbounded transfer is understood as a positive measure by monotone summation. For the **full raw** quadratic Haar law, in contrast, \(\sum_e (3\,4^{-e})2^e/3=1\), so this argument gives no contracting geometric first-moment bound on its tower.

In fact the critical harmonic cost of this particular finite record projection is infinite. Let \(h\) be the specified first-power stationary ternary density, whose averaged value on the \(v\)-digit ball at \(y\) is \(\rho_v(y)\). The smoothed fibre on each forward physical record \(y_i\) has mass at least \(G_i^{-2}\), real coordinate at least \(y_i\), and ternary law uniform on its raw \(v=g(y_i)\) ball. Since the genuine word from \(a\) is among those in that ball, \(\rho_v(y_i)\ge G_i\). These distinct fibres contribute at least \(y_i/G_i=P(a)F(y_i)\ge P(a)/K\) apiece to \(\int h\,d\nu\). Thus \(\int h\,d\nu=\infty\), despite the finite first real moment. The all-step Haar uniqueness theorem and the record-subinvariance inequality (2) have different operators and integrability domains. The [upper real endpoint theorem](REAL_ENDPOINT_SUPPORT.md) further shows that the past canonical law reaches every neighborhood of 1.
