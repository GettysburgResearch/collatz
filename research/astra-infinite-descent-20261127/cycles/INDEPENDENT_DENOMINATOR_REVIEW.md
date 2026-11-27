# Independent review of the denominator bound through six mismatches

**Verified as a written implication using Evertse's theorem and the cited rational-minimum estimate.** For a primitive positive rational cycle with \(p\) odd departures, a supplied proper rotation with at most six valuation mismatches forces its complete reduced denominator to exceed \(2^{p/4096}\) for every sufficiently large \(p\). The onset is ineffective. The conclusion for ordinary cycles covers the specified rotations. [Denominator argument](ROTATION_DENOMINATORS.md) · [Native chain argument](MISMATCH_CHAINS.md).

## Reconstruction

Write \(2^{e}y'=3y+q\) for the actual successive positive odd numerators. Charging a chosen excess at its departure gives
\[
 y'+q\le(1+q)(3/2)(y+q)2^{-(e-1)}.
\]
Other departures satisfy \(y'+q\le(3/2)(y+q)\). Each chronological prefix uses each of its own selected departures once. An interval between selected states also pays once for replacing its initial \(y\) by \(y+q\). After division by \(p\), the prefix at zero-based rank \(j\) has error budget \((j+2)/4096+o(1)\) and the interval has budget \(2/4096+o(1)\). The post-minimum convention placing an exact return at time one preserves both bounds.

Under the contrary bound on \(q\), the lap identity first gives \(h=O(p^2)\). The minimum estimate then gives \(\log_2(m+1)=O(\log p)\). On a common arc with total common divisions \(A\), the two starting numerators differ by a nonzero multiple of \(2^A\). Their higher member \(Y\) is at least \(2^A\). In the common affine carry \(C\), the cumulative divisions before each individual term are less than \(A\). Consequently \(2C<3^L Y\) for an arc of odd length \(L\). The unnormalized higher-side logarithmic correction is at most \(\log_2(1+q/2)\), independently of the lower side. The shifted height bound puts the normalized heights and excesses in the unit cube. The spacing bound also puts \(A/p\) in the cube. The fixed number of arcs now gives \(h=O(p)\), as needed for the normalized Diophantine errors.

In the compact chain identity, each right-hand summand has a different dyadic valuation. In a split final payload, consider a hypothetical nonempty proper vanishing subsum after adjoining the negative left side. If the two final pieces stay together, the side omitting the left side is ruled out by the compact argument. If they separate, the side omitting the terminal quotient has precisely one ternary-unit summand. All earlier payloads and the left side have a factor of three. This reasoning includes a full cyclic chain in which the first and last quotients are the same integer. The application of Evertse's inequality (14) uses \(S=\{\infty,2,3\}\), \(T=\{3\}\), and nonvanishing of every nonempty right-hand subsum. For any fixed number of cuts the ordinary term heights are \(\exp(O(h))\); taking an arbitrary fixed Diophantine exponent yields the required \(o(h)\) error. [Evertse, Theorem 2, printed page 228](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf).

## Independent finite checks

The [point evaluator](check_denominator_independent.py) rebuilds the physical inequalities numerically at each supplied point without importing the production row-matrix builder. For each slope endpoint, evaluation at the cube origin and each coordinate unit vector determines the entire affine form and its exact cube maximum. The checker explicitly enumerates all \(2^s\) higher-side assignments for every order type and compares each distinct charged maximum with the original rational receipt. All 25 order types and 29 leaves agreed. The largest charged maximum was \(-15713923/1024000409600\).

The [ordinary arithmetic replay](check_denominator_native.py) reuses the packet's rational-cycle enumerator for primitive positive cycles of shortcut clocks 4 through 12. It recomputes higher-start carries and consecutive chain identities directly. It checks the smaller endpoint at each cut, the split final payload, all starting cuts, all chain lengths up through the complete mismatch lap, and every nonempty right-hand subsum. It checked 4,754 higher starts and 19,682 cyclic chains, including 4,754 complete laps. These finite samples check the ordinary formulas. The all-period conclusion uses the written argument.

Both scripts produced byte-identical output under Python with flags `-B` and `-OB`. Run them directly from the packet.

| Reviewed object | SHA-256 |
|---|---|
| Denominator argument | `03a0b1593a5de409d8bf90a0a5d9a8ee0a8d606268df1aeb16a0f671ad5cd084` |
| Consecutive mismatch argument | `adf3fe4367a307363147ec53015384bbcf814fb198b5ef16a25ebb3d4d5b70fc` |
| Production verifier | `73bd735a0633895ccb82ca51da16d9f9380cd50286e7404c386609a4bd2b86ba` |
| Dual tree data | `d950810f9ae909f18a1facb0ac228e7d8e9b613f475cf97d5d139dc4bee06eb7` |
| Archived exact maxima | `97fad86160963cc0bab3cb773acf7e344fe2e4603150b55b42dd13d0ea3f9d91` |
| Independent point evaluator, output | `72a56a707786ffd5015de5dd2a4e211a5194e113e9ce8a6cded772ed58e1e663`, `c46588849ca12d48669851d45bbca82009a07d7cb96b95f3d135c8c9f0ac82ce` |
| Independent native replay, output | `d1a9daeb3902c2fa15fa7e00a35fdea27595c1601dca1816401b102f93717ad6`, `c9fd92cd89e4b1f4fb114a905b659c48e74b5fb24f6fdb5c45ff90f9313ad4d1` |
| Existing rational-cycle enumerator | `d3fb32077798ec6749444663523c130bb5e2dbbd75a979791a9c6de34a97f277` |
