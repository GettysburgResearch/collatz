# Four-suffix reduction, late witness geometry and synchronized alternatives

**Collatz remains OPEN.** This checkpoint develops three attacks on the actual two-color remainder: an exact reduction of the whole head-disagreement series to prescribed suffixes, a joint incidence estimate at late physical clocks, and additive structure around the actual source and its smaller target heads. Four new Lean modules check the arithmetic and finite interfaces, including a global basin implication through the freshly rebuilt PR 193 certificate. The analytic estimates remain written proofs with the specific external inputs below.

Use the positive shortcut map \(T(2n)=n\), \(T(2n+1)=3n+2\), and an invariant label \(f(Tn)=f(n)\). For \(j\ge1\), put \(R_j=81^j\), \(d=\log_2R_j\), and

\[
a_j=R_j^{-1}\#\{7R_j\le x<8R_j:f(x)\ne f(\lfloor x/81\rfloor)\}.
\]

Set \(a_0=0\). All counts below concern actual positive integers and use the original row normalization. For the basin of one, the source-qualified fixed-target positivity and the earlier rigidity argument make \(\sum_j a_j<\infty\) a sufficient closing estimate. No result here establishes that summability.

## 1. One prescribed suffix per row retains the full closing obligation

Fix an open arc \(J\subset(7,8)\). It suffices, at the level of summability, to test the following periodic schedule:

| Row index \(j\bmod4\) | Tested suffix \(x\bmod81\) | Exact routed multiplier |
| ---: | ---: | ---: |
| 0 | 0 | \(81u\) versus \(u\), all positive \(u\) |
| 1 | 27 | \(27u\) versus \(u\), \(3\nmid u\) |
| 2 | 45 | \(9u\) versus \(u\), \(3\nmid u\) |
| 3 | 57 | \(3u\) versus \(u\), \(3\nmid u\) |

Let \(A_j^*\) count actual discordant heads in \(J\) with the indicated suffix, divided by \(R_j\). Then

\[
\sum_j a_j<\infty\quad\Longleftrightarrow\quad\sum_j A_j^*<\infty.
\tag{1}
\]

More precisely, for fixed constants \(C,K\),

\[
a_j\le C(j+1)81^{-j}
 +C\sum_{q=0}^j(q+1)81^{-q}
       \sum_{|\ell-(j-q)|\le K}A_\ell^*.
\tag{2}
\]

This conclusion holds for every invariant label without a component-density input. It also transfers little-\(o(R_j^\alpha)\) discrepancy counts for any fixed \(0<\alpha<1\). With the published predecessor exponent \(\alpha=.84\), the existing rigidity argument supplies a separate sufficient condition for convergence, without the recent positive-density input.

The exact construction is small. Put \(p=0,1,2,3\), \(a=4-p\), and \(r=81-2^p3^a\). Choose \(k\) in a suitable residue class modulo 18 so that \(3^p\mid2^ku+1\), and set

\[
v=(2^ku+1)/3^p,\qquad m=2^pv-1,\qquad
x=81m+r=2^{p+k}3^a u.
\]

The two arms reach \(u\) and \(3^a u\) at the same clock \(p+k\). Irrational rotation of \(\log_{81}x\) puts the child into the required mantissa arc and row class using a finite menu of multipliers, uniformly in \(u\). That finite menu gives bounded scale distortion and bounded multiplicity. Removing factors of 81 from a tripling discrepancy has recursive coefficient exactly \(1/81\). Composing this with the PR 146 actual-label variation inequality gives (2).

One may use four distinct row classes modulo any fixed \(M\ge4\), separate arcs for the four suffixes, and require the selected children to have any fixed number \(Q\) of initial even steps. The constants depend on these fixed choices. The stronger scheduled count may also retain \(m\equiv-1\pmod{2^p}\). No uniform assertion for growing \(M\) or \(Q\) is made.

[Exact routes](FOUR_SUFFIX_ROUTING.md) · [Whole-series comparison](FOUR_SUFFIX_EQUIVALENCE.md) · [Periodic schedule](PERIODIC_FOUR_SUFFIX_SCHEDULE.md) · [Lean routing](HeadRayRouting.lean) · [Lean global consumer](FourSuffixClosure.lean).

## 2. Actual smaller witnesses must spread and keep varying

In the late slab \(3d\le t\le3.1d\), write a regenerated discordant head as

\[
z=\lfloor3^k2^{-t}n\rfloor+O(1),\qquad
|k-t/2|\ll_A\sqrt{d\log d},
\]

where \(n\) is the original parent. Outside \(O_A(R_jd^{-A})\) original children, every interval of \(D\ge(\log d)^6\) clocks on a discordant source has a positive proportion of marked clocks. Any choice of one witness at each of those clocks has at least

\[
c_A\sqrt{D/\log d}
\]

distinct centered exponents \(k-\lfloor t/2\rfloor\). The sum of absolute changes of these selected centered exponents is at least \(\delta D\), uniformly over the choices.

The probability estimate behind these conclusions tests specified tracks of at most \(W\) exponents per clock. Such a track has at most \(C_AW\sqrt{D\log d}\) true hits, except on an arbitrarily small inverse-power fraction of original sources. A factorial-moment estimate permits exponentially large track menus in the appropriate range. The linear variation bound follows by counting integer paths with small total variation.

The late tests use one explicit coarse coordinate
\(m=\lfloor3^{\lfloor2.9d/2\rfloor}2^{-\lfloor2.9d\rfloor}n\rfloor\).
Its interval has more than \(2^{.39d}\) cells; all tests together expose fewer than \(.31d\) bits. Once its lower bits are fixed, the next tested head has a fixed suffix and its parent is an odd-affine function of the next block. This supplies a genuine multitime finite-grid product bound beyond the original physical bit horizon. It also permits conditioning on the first \(\lfloor d/2\rfloor\) original source bits with an explicitly counted cost.

[Late witness theorem](LATE_WITNESS_TRACKS.md) · [Variation and information needed to follow a track](TRACK_VARIATION.md) · [Lean block identities](LateWitnessTracks.lean).

## 3. A graph of simultaneous smaller disagreements

Use two separated subintervals of the late slab. Every good discordant original source generates \(\gg d^2\) ordered pairs \((z_1,z_2)\) of smaller discordant heads. They obey

\[
\left|\log(z_2/z_1)+v\log2-w\log3\right|\ll_A1/z_2,
\qquad
c_A\sqrt{d/\log d}\le|w-v/2|\le C_A\sqrt{d\log d}.
\]

For a fixed target pair, the classical two-logarithm separation makes the integer relative clock \(v\) and exponent \(w\) unique. Only \(O_A(\sqrt{d\log d})\) absolute-clock translations remain. If \(\Gamma_j\) is the sum of \(1/z_1\) over the resulting graph edges, then

\[
a_j\ll_A d^{-A}+\frac{\sqrt{\log d}}{d^2}\Gamma_j.
\tag{3}
\]

This counts the two targets jointly. It contains no product assumption about their colors.

A further reprojection gives the graph actual arithmetic thickness. Use shorter separated slabs and a fixed interior arc for the original witnesses. Outside another arbitrary-power source exception, each returned pair has at least

\[
2^{.01d}\exp\bigl(-C_A(\log(d+2))^{12}\bigr)
\]

positive shifts \(L\le2^{.01d}\) for which both
\((z_1\pm81\,2^vL,z_2\pm81\,3^wL)\) are true discordant pairs in the same respective rows. All four ordered child/parent colors and the exact additive rounding correction are preserved. These translated pairs are actual colored edges; they need not be outputs of additional original trajectories.

[Two-target weighted recurrence](WEIGHTED_TWO_HEAD_GRAPH.md) · [Simultaneous target midpoints](JOINT_TARGET_MIDPOINTS.md).

## 4. A centered tree through the actual source

Retain the exact endpoints and odd counts of a fixed finite family of odd-affine arms at clock \(h\). The previous largest-slope projection gives each retained good source fiber \(S\) at least \(F/J\) members in diameter \(LF\), with \(L,J\) polynomial in \(h\).

Applying the published Kelley–Meka progression-counting theorem to the subset of poor centers shows that almost every actual member of \(S\) is itself the midpoint of many three-term progressions in \(S\). It does not merely find a progression somewhere in the fiber. Backwards pruning then gives a ternary tree through that prescribed source of depth
\(m\gg h/(\log h)^{12}\), with \(3^m\) distinct positive source leaves. The splits occur in disjoint prescribed binary windows and preserve every recorded future.

The same projection gives a quantitative conditional information bound: the cumulative squared biases of exposed source bits are \(O_A(\log h)\) except on relative probability \(O(h^{-A})\). A Hellinger martingale proves an exponential tail, also for predictable blocks. This concerns the past of the recorded endpoints.

Separately, ordinary window synchronization makes locally sparse true discordance summable at polynomial neighborhood radii. These neighbors can have different future records. A matching native-clock result explains the limit of exhaustive early cross-search: on mass \(\gg h^{-1/2}\), no child in the entire rich fiber meets any parent in it at any two clocks through \(h\). Later meetings remain possible.

[Centered progressions and trees](SYMMETRIC_FUTURE_FORKS.md) · [Conditional information](RETROSPECTIVE_INFORMATION.md) · [Finite-clock scope](NATIVE_FIBER_CROSSING.md) · [Lean midpoint and parity interfaces](SymmetricFutureForks.lean).

## 5. Formal scope, inputs and the next mathematical step

The new Lean global theorem `FourSuffixClosure.basin_iff_four` concerns the actual positive basin of one. It connects the four explicit multiplier comparisons to universal convergence through PR 193's finite directed-return cover. The hypotheses are displayed in the theorem. Irrational routing into arcs, weighted counting, progression estimates and probabilistic conclusions are written proofs.

The mixed binary/ternary approach comes from Emre Yolcu, Scott Aaronson and Marijn Heule. The new routing concentrates the existing four-trit head obligation into prescribed ordinary source classes; it does not produce a terminating interpretation of their complete eleven-rule system. PR 193 supplies the exact global certificate; PR 146 supplies the actual-label variation estimate and the source-qualified finite-grid merger bound. Bloom–Sisask's published Theorem 21 supplies the Kelley–Meka count. The scalar regeneration and original-source transfer are reused from the preceding PR 197 packet. Recent external pair-chain, growing-block and fixed-target density claims retain their named source qualifications.

The remaining quantitative target in (3) is explicit. For example, a bound

\[
\Gamma_j\ll \frac{d}{(\log d)^{3/2+\epsilon}}
\]

for some fixed \(\epsilon>0\) would make \(\sum_j a_j\) finite. The present graph has transverse spread and many parallel centered neighbors, but these properties do not supply that upper bound. Alternatively, a summable estimate directly on the scheduled suffixes in (1) would close the same obligation. The native-clock result places a successful fiber-crossing argument beyond the already recorded early trajectories.

[Exact source ledger and reading scope](SOURCES.json) · [Coordinator reconstruction and checks](../../../reports/ayh-resource-reset-20261124/crossing-step/README.md).

For a fresh local formal replay with the pinned Mathlib checkout:

```sh
lake env bash /path/to/crossing-step/check_lean.sh
```

The script rebuilds the vendored certificate and all new local modules, then queries every new public theorem and the imported public certificate roots. The published-head repository validator receipt is retained in PR 197; integrity validation and mathematical evidence have separate scope.
