# Smaller ordinary heads after the opposite-phase test

**PROPOSED composition of two written estimates. Universal convergence remains OPEN.** Source snapshot: PR197 `6eb986b0ce0b1836a356474d25d709ed4e948b67`, directory `research/ayh-resource-reset-20261124/two-class-descent/`. Reviewed the central counting inequality in `HEAD_INCIDENCE.md` (1), (2), (3) and its distinctness refinement; the endpoint certificates in `ROUNDED_HEAD_DESCENT.md`; the retained-fiber assertion in `ADAPTIVE_PAIRED_PROJECTION.md`; and the scope of `FINITE_FLOOR_FRONTIER.md`. The imported scalar concentration, large-grade occupancy, source transfer, and two-logarithm estimates retain their source qualifications. This is a verification of the interface and an additional restriction on the targets that can carry its mass. No independent full build of PR197 is claimed.

## A positive fraction of the returned edges survive the window test

Write \(R=81^j\), \(d=\log_2R\), and test the actual basin-of-one color on each original pair \((x,\lfloor x/81\rfloor)\) for \(7R\le x<8R\). Within a smaller head row \(\ell\), call a discordant edge *detected* if somewhere within distance \(\lfloor e^{\ell^\beta}\rfloor\) of either endpoint there is a terminating integer whose shortcut time to one has the parity opposite to that of the edge's terminating endpoint. Fix \(0<\beta<1/12\). The four choices of phase and orientation partition unphased discordance. Apply the full-row estimate (W2) to each, then sum. The normalized count \(g_\ell\) of detected edges satisfies

\[
 g_\ell\ll_{p,\beta}(1+\ell)^{-s},\qquad s=p-\beta(3+2p)>1
\]

for a fixed \(1<p<3/2\). The proof of (W2) bounds the whole head before restricting to a smaller mantissa patch. Its power margin matters when passing through the incidence coefficient. [Growing-window proof](../../../../research/astra-global-closure-20261124/round5/head/README.md)

Use (1) of `HEAD_INCIDENCE.md` with \(B=d/4\), or with \(B=d^b\) for any fixed \(1/s<b<1\); in the second case take \(b>1/2\) as well. On its good original sample a discordant child supplies at least \(cB\) distinct **clocks** with certified truncation chains. Each chain contains some discordant head \(z\). At a prescribed clock \(t\) and head \(z\), the bounded upper-arm intercept confines the original source to an interval of length \(O(R/z)\). Testing original pair nonfusion on that interval leaves \(O(R/(z\sqrt d))\) sources; the upper-arm choice and the 81 initial remainders incur a fixed factor. At most \(O(\sqrt{d\log d})\) clocks can charge a fixed \(z\). The location of \(z\) in its chain may be chosen after seeing all colors.

Fix \(0<\eta<c\). At each certified clock that admits **any** detected discordant head, choose one such head and count the incidence. For the number \(N_{j,\eta}\) of original discordant children having at least \(\eta B\) such clocks, the source proof gives

\[
 \frac{N_{j,\eta}}R
 \ll_A d^{-A}+\frac{C_{A,J}\sqrt{\log d}}{\eta B}
 \sum_{\substack{z\text{ detected in the target band}}}\frac1z
 \ll_{p,\eta,A,J} d^{-A}+\sqrt{\log d}\, B^{-s}.                 \tag{L1}
\]

Indeed the target logarithms are in \([B-O(1),2B+O_A(\sqrt{d\log d})]\); hence their row indices are comparable to \(B\) and meet \(O_A(B)\) rows. On a single row the reciprocal weight is comparable to \(81^{-\ell}\). This proves (L1) by the bound on \(g_\ell\). The unconditioned exceptional set is paid once. Any nonempty open mantissa interval \(J\subset(7,8)\) can be specified for the returned heads by using PR197's interior patch. Its constants may change.

In particular (L1) is summable in the original rows, since \(A>1\) and \(s>1\) at \(B=d/4\), or \(bs>1\) for the power choice. Outside a set of finite total original weight, **every discordant source supplies at least \((c-\eta)B\) clocks on which every available discordant head in the certified chain is undetected**. One may choose a discordant head at each such clock. PR197's nonzero-logarithm bound makes all the resulting child integers distinct. The clocks retain the bounded-intercept and scale premises in the incidence proof. The same calculation applies if the detection rule also allows the polynomial-width time windows in (W3) for any fixed subcritical parameters, because their row estimate has an inverse-power margin beyond summability.

## Why the undetected mass remains

At a certified clock, the upper truncation uses an equal-clock symbolic merger and the bottom certificate has equal physical clock 13. The two ends of the chain can therefore have labels \(B\) and \(\iota^t q\), where \(q\) is the original terminating phase. The entire finite chain may use just these two labels. Its discordant crossing need not contain or adjoin a vertex of the opposite terminating phase. The recurrence locates an unphased original-color difference on its smaller heads; it cannot impose the originally selected directed orientation on each returned crossing.

Different clocks also supply no automatic nearby third label. For any of their chosen child centers, the source's distinctness calculation gives \(|\log(z/z')|\gg_A d^{-\nu}\) for some fixed \(\nu\). The same estimate holds when either center is replaced by its parent: subtract \(4\log3\) and allow a rounding error \(O(1/z)\). The nonzero coefficient of \(\log2\) is still the difference of the two clocks. At these heights the centers from distinct clocks are separated by at least \(c_A 2^B d^{-\nu}\), much greater than \(\exp(O(B^\beta))\). Thus even if two clocks transport different terminating phases, juxtaposing their child/parent centers does not put one into the other's tested neighborhood.

The fixed or growing deep-floor menus remove simultaneous low-grade alternatives under their stated bounds. They make no assertion about the opposite phase at the resulting high-grade edge. The paired projection retains actual future endpoints and counts at one common clock on each fiber, so all its parent origins have the same phase label and all its child origins have the same phase label in their respective arms. Its conditional estimate for a *prescribed sparse set of source residues* does not identify a sparse residue condition implied by undetected discordance. At a returned location, a different short-window law conditional on being undetected would be needed to make such an inference.

For a quantitative check, as abstract nonnegative profiles take \(a_\ell=(1+\ell)^{-1/2}\) and \(g_\ell=0\). On a target band with \(B\ge\sqrt{d\log d}\) the right side of the source recurrence has scale at least a positive constant times \(\sqrt{\log d}/\sqrt B\), which dominates \(d^{-1/2}\) for \(B\le d/4\). This is a model of the scalar inequalities only. It shows why removing the detected summand does not close them. To use the new incidence bound for universal convergence one still needs an upper estimate for the undetected original-color mass in the target bands, or a new mechanism forcing enough returns to detected edges; neither follows from (L1).

| PR197 source at the specified commit | Git blob |
|---|---|
| `README.md` | `8a45890d2d458b3663555975c07158ce03ccfd2a` |
| `HEAD_INCIDENCE.md` | `1257ebfb05083de6b48d345e9870d10339d30340` |
| `ROUNDED_HEAD_DESCENT.md` | `6725e04f712190f2f8f757bea8d3b022894b161b` |
| `ADAPTIVE_PAIRED_PROJECTION.md` | `63ae011a109e507ae2fcb886b527836a679ca0b1` |
| `FINITE_FLOOR_FRONTIER.md` | `69b758dbf21c3a60347bd0d69d88d60fb18e0cb9` |
