# Frozen comparison of the exact-row estimates

**Status.** PR206 independently obtains the finite-survivor test and the convergent climb. Given an escaping ordinary orbit, PR207's proposed renewal floor forces a large population at many moving endpoints below the range of the reflection bound. Neither packet supplies a cofinal upper bound on that population. This review covers two frozen heads.

| Source | Commit | Directory |
| --- | --- | --- |
| PR206 originally imported | 37d2b5d644664a746891042c199e58cfb06f1176 | research/clock-itineraries/ |
| PR206 reviewed update | 611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2 | research/clock-itineraries/ |
| PR207 reviewed head | b56c4dc2c28a184cf55638bb80c49a9d4662fc81 | research/diffusive-central-row-closure-20261124/ |

## PR206

The local file at `research/astra-global-closure-20261124/round9/vendor/TernaryItinerary.lean` is byte-identical to PR206's original `TernaryItinerary.lean`. Both are 19,637 bytes with SHA-256 `b79cfc44200087ac0ca9bed9daab9c83a64487bbdb29a4e1e410ba7d6d3f8112`. The reviewed update has 19,657 bytes and SHA-256 `b6a2bce0e51455a8c5177a473b751219da82021086e158698564cb4c920b6b56`. Removing the new `@[expose]` attributes on `digit` and `FullRow` reproduces the original bytes exactly.

- On an actual odd suffix of \(n=b-m\) gaps, physical clock \(v\) and endpoint \(q\), PR206 proves that \(\mathrm{FullRow}(a,b,m)\) is equivalent to \(q>2\) when \(m\ge2\) and \(v+6m+7\le2b\). Its sharp bound \(2^{5v}q^5/(2^{8n}a^5)\le100000/59049\) allows \(22m+5H+35\le2b+5Q\) when \(a\le2^H,\ 2^Q\le q,\ 2\le m\le b\). Taking \(Q=0\) gives the same finite-survivor statement reconstructed here. The sharp constant is attained on the ordinary path \(9,7,11,17,13,5\). [FixedGate.md](https://github.com/GettysburgResearch/collatz/blob/611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2/research/clock-itineraries/FixedGate.md)
- The convergent climb \(a=6\cdot2^Bu-1\) is also shared. PR206 chooses \(u\) so that one gate passes every admissible test in a given finite list and then reaches one. Its general path translation preserves every prescribed gap and the integer carry, while multiplying every relative carry by \(q/q'\) at the new endpoint \(q'>q\). The present lane additionally counts sources in PR201's internally filtered maximum at a specified decreasing threshold. [SynchronousShadow.md](https://github.com/GettysburgResearch/collatz/blob/611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2/research/clock-itineraries/SynchronousShadow.md)
- For exact row distortion \(D=4^bq/(3^b x)\), an ordinary witness \(q>2,\ D^6>b+1\) forces a nontrivial cycle. A nontrivial cycle supplies such a witness at one fixed \(q\) at every sufficiently large \(b\), without F. The depth-\(b\) test is finite because a witness has \(x<10\cdot2^b\). The clock-and-row equivalence still requires both a crossing on each ordinary gate and absence of all witnesses. A weakly smaller inverse ancestor at \(q>2\) requires \(5s\le8b\), which excludes the central clock window for \(b\ge7\). [CycleAmplification.md](https://github.com/GettysburgResearch/collatz/blob/611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2/research/clock-itineraries/CycleAmplification.md) · [ClosureProposal.lean](https://github.com/GettysburgResearch/collatz/blob/611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2/research/clock-itineraries/ClosureProposal.lean) · [DescentClocks.md](https://github.com/GettysburgResearch/collatz/blob/611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2/research/clock-itineraries/DescentClocks.md)
- PR206 also obtains an unconditional cohort count \(\gg b\,2^{\lfloor b/16\rfloor-1}\) for an escaping gate at every observation clock \(H\ge2b\), and a conditional positive fraction on the scale \(G_b=(4/3)^b\) using F and simple-path sparsity S. The observation is a high physical state after a visit to the gate. The final odd step count at \(H\) varies. Separately, its proposed cycle theorem puts the largest odd state above \(52/25\) times the minimum odd state, using the indicated published height, period and logarithm inputs. Wide cycles remain possible under this estimate. [OrbitTrace.md](https://github.com/GettysburgResearch/collatz/blob/611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2/research/clock-itineraries/OrbitTrace.md) · [OrbitAttack.md](https://github.com/GettysburgResearch/collatz/blob/611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2/research/clock-itineraries/OrbitAttack.md)

## PR207

Write \(N_b^s(q,\epsilon)\) for actual high-carry sources in row \((b,2b)\) with all \(b+1\) odd states distinct, and \(L_b=\lceil\sqrt b\rceil\). Under the source-qualified central exact-count floor F, one escaping ray \(q_i=U^i(a)\) gives \(N_b^s(q_i,\epsilon)\ge c_a q_i G_b/\sqrt b\) at \(\gg\sqrt b\) distinct terminals on every large \(b\), with the same \(\epsilon=1/(3a+1)\). The prefix has \(n=b-i\) odd steps and clock \(2b-A_i\), where \(A_i\) is the actual clock from \(a\) to \(q_i\). For \(i\) from \(\lfloor L_b/4\rfloor\) through \(\lfloor L_b/2\rfloor\), the discrepancy \(2i-A_i\) is in the central window. S removes only \(o(\sqrt b)\) terminals below \(L_b\). Summing \(N_b^s/(q_iG_b)\) over the remaining terminals gives a positive lower bound for \(E_b(\epsilon)\) on \([L_b,2^{L_b}]\).

Every one of these endpoints obeys \(q_i+1\le(a+1)(3/2)^i\), by \(U(y)+1\le(3/2)(y+1)\). Thus all forced endpoints eventually satisfy \(q_i<(3/2)^{351b/352}\). In fact the entire window \(q\le2^{L_b}\) eventually does. The reflection bound in this packet makes no contradictory count estimate on this window. PR207's written upper uses a finite small gate and the first passage to a growing polylogarithmic barrier. For gate suffix length \(j\), the weighted contribution of \(j\le\eta\sqrt b\) is \(O_\epsilon(\eta+b^{-1/2})\) using the source-qualified grade-spreading input P. The weighted contribution for \(j\ge C_{A,\epsilon}\sqrt{b\log b}\), or for \(q\ge\exp(C_{A,\epsilon}\sqrt{b\log b})\), is \(O_{A,\epsilon}(b^{-A})\). These bounds leave the intermediate range and do not imply the PR201 absolute-count cutoff \(2^{\lceil b/32\rceil}\). [Main proofs and input statements](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/README.md)

For cycles, PR207's conditional \(C_b\) uses all rows, including repeated states, at fixed threshold \(1-2^{-100}\). A fixed periodic \(q>1\) eventually lies below \(L_b\). The near-diagonal analysis at \(k=\lceil b^{2/3}\rceil\) gives \(J_b(q,k)\ll_{q,A}qG_b2^{-k}b^{-A}\) for every fixed \(q>1\). Its bounded-offset F lower reaches that scale at \(q=1\). At a hypothetical nontrivial cycle it reaches only \(k\le c_q\sqrt b\). Indeed at \(r\) laps the central discrepancy contains \(r(2p-A_q)\), strictly positive per lap for odd period \(p\) and physical period \(A_q<2p\). The lower and upper estimates at a nontrivial cycle concern different scales. [Near-diagonal proof](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/NEAR_DIAGONAL.md)

## Source and execution scope

The table records SHA-256 of the compared artifacts. Paths are relative to their immutable PR directories above.

| PR | File | SHA-256 | Scope |
| --- | --- | --- | --- |
| 206 | FixedGate.md | 26b66fc2ac55abbca77dfb417fab6d4ff7f4637f1e06754bab087e58dfb04bca | Written bound and overlap |
| 206 | SynchronousShadow.md | a6f20e0e9ab5afa2d1cbb34f51b59ac6f3a7ad60f6d4ba5f240d7b9d4085f22d | Written climb and path translation |
| 206 | CycleAmplification.md | 7d6de3d34318b4e83e8c6d723951b53d865332e6c076ee4fbc03f6dbe4914972 | Written finite-test proof |
| 206 | DescentClocks.md | c8a811d86b2941b609cc8f43e2f38e45d2f0f9bd23956d4e9aab79e307d669cc | Clock cap and root-cylinder obstruction |
| 206 | ClosureProposal.lean | eb91552efac88b983f174b491b0dca06fdc786348d0753994381f60054d8ee21 | Read theorem interface and proof |
| 206 | CycleDetection.lean | 36fe77bda861ff82a6d1f7ec6846df0542d8d7b0bdc617e314703843987004d0 | Inspected distinct-input estimate and cycle interface |
| 206 | OrbitTrace.md | 44254de77843d41fa4810dc960c463bf9242872d31678a8a1d3b13ad839ecfee | Both observation-clock estimates |
| 206 | OrbitAttack.md | 431f78e46ef0d872eb2733fa5d01babb813b6fc29a04c379c95e5869b65ce612 | Proposed width and stated input boundary |
| 206 | MinimumDescent.md | 2f8ff67dfe804f375f6d39221524564e43a50310587de62b5814c64d8d9d1035 | Inspected restricted source family |
| 206 | proposal_replay.py | 61d01501bac68d7a724b8c87d97c7c030a6d3133cce79ad5133a1b9a6f9eb34e | Read and executed with and without optimization |
| 207 | README.md | 6ee24648dea08ec941b989aa602cfd5646938575760c1107c2afcf243651a6da | Written estimates and hypotheses |
| 207 | NEAR_DIAGONAL.md | c147b6df2710e5fd3747f2895b7f88ad2600622447d839a7f8ca06926059c283 | Written residual-shell proof |
| 207 | DiffusiveRows.lean | e2d70f40cf7be9caefa2c6ab3010da166a880744b4088da60800f51e1f2fc122 | Inspected finite algebra interfaces |
| 207 | controls.js | 35b9425d4a3be85b4df177c412beca423983cf1da6271c82721f873c04c7148d | Read and executed |
| 207 | CONTROLS.json | ee6f99fc238db27fb1be4f7bc1b26e149d19474b94920bb0a0ec7b01142b4a00 | Compared every published count |

On Python 3.12.14, `python proposal_replay.py` and `python -O proposal_replay.py` each exited zero with byte-identical output, SHA-256 `4d5ffb1d2556cfcf745b1ce484e3f68c027f40080e80d4663206a094374eae12`. The replay found 2,731 clock crossings, 2,724 above one, 79,378 simple segments, 32,072 balanced candidates across exhaustive witness depths 0 through 16, zero cycle witnesses, 48 shadow families, 114 translated paths, and first hitting time 553 at the published finite gate.

On Node v24.22.3, `node controls.js` exited zero. Its output, SHA-256 `eef85d203b54acf082ecdaf5a3796a87194222799adfe0df3ace24dd8e91b284`, exactly matches the parsed counts in `CONTROLS.json`. Both computations of the balanced rows at \(1\le b\le10,\ q\le99\) found 222 rows, comprising 212 simple paths and 10 repeated paths. The replay checked 1,541 suffix carry inequalities, 112 moving-window instances, 36 cycle residuals, and five superdiffusive shell calculations.

This intake independently reran the two bounded programs. The new upstream Lean modules were inspected at the indicated interfaces, with no fresh upstream compilation in this intake. The analytic inputs F and P and the published cycle-period and logarithm estimates retain their stated source status. The separate [row kernel and bounded replay record](EXECUTION.md) covers this packet's own Lean files and original pinned import.
