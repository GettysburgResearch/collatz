# Independent review of the finite fixed-tower comparisons

**Verdict.** VERIFIED for the claims and source versions below. The delayed theorem at the reviewed hash gives no asynchronous meeting through $H$ and a common-clock meeting at $H+5$. Its witnesses are selected edges of the single tower based at 17. It gives no basin theorem for an arbitrary supplied rank.

| Source | Reviewed SHA-256 | Claims |
|---|---|---|
| `FixedTowerReflection.lean` | `fcaa17f9adc99a21787ff08e42e6801f6107502e5976ead225f6fb879ccb5ada` | `reflect_iff`, `returning_multiplier`, `defect_delay`, `convergent_control` |
| `TowerLowerCone.lean` | `eff19ef6b4da91557ae687b5cad090868c6ca1a41d287faabd7c0056e2e016af` | `high_tower_merger`, `orientation`, `clock_bound`, `defect_clock_bound`, `block_endpoint_exclusion` with asynchronous threshold 1593 |
| `DelayedTowerMerger.lean` | `cc1a0d0ff68a76a5b4d48cc2f976427157d049806d54f47c4366d37cacbb9a7d` | `delayed_merger` with the five-clock interval |

For reflection I expanded each source at the same returning multiplier. The unlifted endpoints are both strictly smaller than the common coefficient modulus $kz$ from the assumed inequality $k>3\cdot2^H$. Reducing an equality modulo $kz$ therefore forces equality of the two actual base endpoints. Cancellation then forces equality of the slope monomials. Their binary valuations fix the clocks, and their ternary valuations fix the compensated odd counts. At a reverse defect the base endpoints cannot meet. At the convergent control, 17 and 51 meet at clock 17 with equal odd counts. An earlier or later compensated common-clock meeting would preserve the compensation when extended and conflict with that common tail.

For lower-cone orientation I reconstructed the aligned affine expansion with remainders below $3^H$. If both total grades are at least $H$, ternary divisibility forces equality of the leading terms. For $w<z$ coprimality of $z$ with 6 would then force $z\mid w$, which is impossible for positive $w$. If only the source grade is high, the source slope coefficient is at least $3^H$ and must be strictly smaller than the comparison coefficient. This forces a shorter comparison clock and the stated strict power inequality. The threshold $3^{2252}<6^{1381}\le3^{2253}$ checks the reviewed 1593 endpoint bound.

For the delayed construction I checked the normalized high digit, its odd invertibility modulo 32, and the five-step suffix on the positive rank return. The source paper's checker ran here and reported 18,240 reflection clock pairs with 31 meetings, 309,385 lower-cone comparisons with 251 high-grade cases, and the horizon-17 and horizon-19 deadlines 22 and 24.

I independently wrote and ran `review_tower_deadlines.py` in normal and optimized Python. It checks all pairs of clocks through $H+5$ for each of the twelve odd $H$ from 17 through 39. It uses the actual starting power modulo $2^{H+5}$ for the bits, and uses the exact affine slope and offset for every comparison. Each difference has form $A3^r+B$ with $|B|<2^r\le3^r$, so a zero test is an exact ordinary equality. All twelve first asynchronous deadlines were $H+5$. The script SHA-256 is `6a40b771ba6a69a15c7fb3e33047886baf8fd415c66d944c8a7af11f1b8650e4`.

**Subsequent strengthening.** The selected residue gives suffix starts $32b+6$ and $96b+16$. At each of the first four subsequent equal clocks their affine expressions differ. They meet at clock five at $9b+2$. High-grade same-tower orientation forces every independent-clock meeting through $H+4$ to be synchronous. I kernel-checked these implications for arbitrary supplied suffix data in `TowerSuffixSharp.lean` (SHA-256 `b60889359035625dd56de4b70207d6b70aa438916fbbb323bcde3fe34a8e871d`). Applying the new lemma to the universal rank constructor yields exact first deadline $H+5$ once that application is compiled. The historical hash in the table states the interval result. The later construction head should carry its own strict compilation receipt.

**Final source recheck.** I reviewed the constructed rank estimate and invocation of the suffix lemma, then independently compiled the four modules in dependency order into a separate empty object directory. Lean 4.34.1 used `-DautoImplicit=false -DwarningAsError=true` and the fresh baseline dependency path. All four invocations exited zero. The source SHA-256s before and after each invocation agreed. The printed dependencies were contained in `propext`, `Classical.choice`, and `Quot.sound`.

| Final source | SHA-256 | Verified change from the initial review |
|---|---|---|
| `FixedTowerReflection.lean` | `fcaa17f9adc99a21787ff08e42e6801f6107502e5976ead225f6fb879ccb5ada` | Same reflection and control |
| `TowerLowerCone.lean` | `a081cc5ecf18d1da62f6f5ccd2c8447a67f482ead90ce68b9cff97ff750a5a06` | At high grade, $q<H$ gives $3^{p+1}<6^H$, improving the asynchronous endpoint exclusion to $m\ge1592$ |
| `TowerSuffixSharp.lean` | `b60889359035625dd56de4b70207d6b70aa438916fbbb323bcde3fe34a8e871d` | Exact five-clock suffix and high-rank synchronization |
| `DelayedTowerMerger.lean` | `ed5cbf240ecfae83335c5870c9b4d93862aebe9869972d57e8ce26d551b60d4c` | For every odd $H\ge17$ and every rank lower bound, the constructed positive edge has **exact first asynchronous deadline** $H+5$ |
