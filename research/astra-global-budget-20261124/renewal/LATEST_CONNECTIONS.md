# A fixed first endpoint and the moving return state of its companion

**PROPOSED written deduction, conditional on PR201's explicit extra-depth atom floor F and the scalar source-count estimates pinned below.** Every fixed positive odd unit \(y\), including \(1\), has nearly optimal inverse multiplicity at exact central clocks after imposing one common physical companion endpoint and one common companion grade **chosen anew at each clock**. The first endpoint stays fixed. The result quantifies the cost of selecting a moving companion state. The fixed finite menu required by PR200's new common-suffix theorem remains open.

## Central ordinary slices at one prescribed endpoint

Let \(p\) be any sufficiently large integer, \(e=2p\), \(G=(4/3)^p\), and use the positive shortcut map. PR201 §1, (2)–(3), with extra precision one and a fixed unit source residue modulo three, gives \(\gg G/\sqrt p\) distinct positive odd units \(x\) such that
\[
       T^e(x)=y,\qquad P_e(x)=p,\qquad 0\le\beta_x\le F_0,\qquad x<yG,
\]
where \(P_t\) counts odd inputs and \(\beta_x=y-x/G\). Remove the \(O(G/p)\) integers below \(G/p\). This leaves the same order of magnitude even for \(y\le F_0\). We do not assume a conditional fair law on the retained sources.

Group \(5x\) in dyadic bands \([R,2R)\), so throughout \(d=\log_2 R=\log_2G+O_y(\log p)\). Set \(a=1-\tfrac12\log_2 3\), so \(\log_2G=ae\). The scalar first-passage estimates give, except for \(O(Rd^{-2})\) original integers in a band, an entrance \(\sigma\) below \(M=d^D\) such that
\[
 a\sigma=d-\log_2 M+O(\sqrt{d\log d}),\qquad
 P_\sigma(5x)=\sigma/2+O(\sqrt{d\log d}).
\]
The scalar stage proof applies on any macroscopic source band: construct the geometric threshold schedule of PR197 FIRST_PASSAGE_MARKS, use a prefix maximum deviation \(C\sqrt{k_i\log d}\) on each length-\(k_i\) fair grid as in LANDING_WEIGHT_TRANSFER (4), and pay the polynomial fiber factor before summing the geometric square roots. The multiplier correction through the floor is \(O(d/M)\) since the duration is \(O(d)\) and all prior heights are at least \(M\). This is solely a scalar result, with no restriction on the source's companion or color. Since \(x\mapsto5x\) is injective, and the sum of the band heights is \(O_y(G)\), removing these exceptions costs \(O_y(Gp^{-2})\) of the initially selected starts. The earlier initial deletion allows this estimate without a lower bound on \(y-F_0\).

Write \(L=\sqrt{p\log p}\). Every remaining source has \(|\sigma-e|+|P_\sigma(5x)-p|\ll_y L\) and \(W=T^\sigma(5x)\le C_y p^D\). Either direction from the observed time to the entrance gives
\[
              T^e(5x)\le 2^{|\sigma-e|}W,\qquad
              |P_e(5x)-p|\ll_y L.
\]
For \(e\le\sigma\), use the lower one-step bound \(T(n)\ge n/2\) forward from \(e\); for \(e\ge\sigma\), use the upper bound \(T(n)\le2n\) forward from \(\sigma\). There are at most \(\exp(O_y(L))\) possibilities for the integral endpoint and grade together. Hence at the **original clock \(e\)** a single ordinary endpoint \(Y_p\) and a single integer \(k_p\) satisfy
\[
 \#\{x:T^e(x)=y,\ P_e(x)=p,\ T^e(5x)=Y_p,\ P_e(5x)=p+k_p,\ \beta_x\le F_0\}
       \ \ge\ G\exp(-O_y(L))=G^{1-o(1)}.                             \tag{1}
\]
These are distinct positive odd units. Here \(Y_p\le\exp(O_y(L))\) and \(|k_p|\ll_y L\). In PR200's notation the actual offset is the same on this cohort, \(D_p=3^{(k_p)_-}Y_p-5\,3^{(k_p)_+}y\), hence \(|D_p|\le\exp(O_y(L))\). Equation (1) proves the numerical lower count in FS for a *moving singleton* at the given \(y\).

A polynomial-loss version retains two observed clocks. There are only \(p^{O(1)}\) possibilities for the triple \((\sigma,W,P_\sigma(5x))\) over all the dyadic bands, even though their entrance thresholds may differ. Some one such triple serves \(\gg_y G/p^{C}\) distinct starts for an exponent \(C\) that can be fixed after choosing the scalar tail parameters; all multiplicative constants and the onset may depend on the fixed \(y\). No uniform claim for moving first terminals is made. Within this cohort the first arm is at \(y\) at clock \(e\) and the second at \(W\le C_y p^D\) at clock \(\sigma=e+O_y(L)\). Advancing the earlier arm to \(\max(e,\sigma)\) produces one common physical clock, one common endpoint on each arm, and one common odd count for each arm across all starts, with the same polynomial-loss count. The first endpoint at this new clock is \(T^{(\sigma-e)_+}y\), so (1) is the version that always keeps the stipulated first endpoint at the original clock. The counts on the two arms need not equal one another.

## What remains at the new fixed-target reduction

At PR200's frozen head the menu and ternary class are specified first; the theorem then constructs an ordinary \(y(q)\) implementing their common suffix to a prescribed \((q,5q)\). Equation (1) applies literally to that \(y(q)\), but selects its own state \((k_p,D_p)\). A sequence contained in sets of cardinality \(\exp(O(\sqrt{p\log p}))\) need never visit a fixed finite set. Applying the suffix theorem to the newly observed singleton constructs a potentially different first endpoint, where the prefix count was not established. Keeping the same \(y(q)\) and extending its specific ordinary companion cannot force that companion to arrive at \(5q\). The polynomial-loss two-clock version has a moving second endpoint and the same issue.

The completed-cell estimate in this branch already has the desired exact companion state \((0,0)\) at every good unit residue modulo \(3^{p+1}\), with lower proportion \(\gg1/p\) for a selected near-central row per scale. The prefix-corrected version prescribes \(O(\log p)\) low ternary digits at polynomial loss. No small ordinary lift of the *specified* good cell is supplied on a prescribed pair's inverse tree; a fixed small lift of a coarse prefix need not belong to any favorable fine cell. PR201's positive-relative-density theorem C controls initial binary prefixes \(h\le(\log X)^\eta\), \(\eta<1\), of the one-arm ancestor set. With \(X\asymp G\), this is \(o(e)\) clocks. Indeed \(T^h(x)\ge x/2^h\) keeps a retained source \(x\ge G/p\) far above the fixed \(y\) on this range. At those early clocks a paired-return condition can be imposed, but its persistence until \(e\) does not follow. Theorem B's ternary source precision \(K\le(\log X)^\eta\) is also too small to specify \(p+1\) trits at a desired routing height \(X=\exp(o(p))\); its routes are one-arm routes even at their stated precision. Thus neither the good-cell result nor (1) pays the fixed companion-state filter of FS.

**Pins.** PR200 `abf36c63b4d0181541d7e029d390d6f636940750`, `research/regularity-rigidity-20261124/pointwise-fibers/COMMON_SUFFIX.md` (common suffix and FS), and `PAIRED_FIBERS.md` (PT and exceptional-target quantifier). PR201 `b68cf8f0fd565c4bb2151afc3ce7668f8801770d`, `research/killed-green-head-closure-20261124/prefix-density/README.md`, §1 (2)–(3), §§3–4. Its atom floor from rStation paper 37 v4 is an assumed input here. PR197 `6eb986b0ce0b1836a356474d25d709ed4e948b67`, `research/ayh-resource-reset-20261124/literature-step/FIRST_PASSAGE_MARKS.md`, (1)–(5), and `joint-renewal/LANDING_WEIGHT_TRANSFER.md`, scalar stage argument for (4) in the same research directory. These new deductions are written mathematics. The compiled finite lemmas and bounded controls from the preceding packet do not formalize or test the analytic inputs or the asymptotic extension.
