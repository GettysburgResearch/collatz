# Fixed-head intake on PR192 and PR193

The comparison is between PR192 `26f070c38ad9edd21ed7dac6efaab6554550c2a3` and `a0d7c6e36c378bbb6c826002039aef486bbe0383`, and between PR193 `fbe870ec44239e6b6c753bab9d1c7537acfff701` and `24cdd0e5471d4421716cfce6bd88916f858f994c`. The diffs add 81 and 33 files respectively. These two new heads add separate ordinary convergence criteria. Each retains an open merger or coverage premise. [PR192 packet](https://github.com/GettysburgResearch/collatz/tree/a0d7c6e36c378bbb6c826002039aef486bbe0383/research/astra-universal-closure-20261124) · [PR193 packet](https://github.com/GettysburgResearch/collatz/tree/24cdd0e5471d4421716cfce6bd88916f858f994c/research/astra-universal-proof-20261124)

## Consequences for the round-nine proposal

- **Priority between two minima matters.** PR192 selects the least positive base $w$ admitting a bad $3^r w$, then the least bad $r$ there. It proves $w$ is an odd ternary unit, $w$ is good, $r>0$, every $2^i3^j b$ with $0<b<w$ is good and every $3^j w$ with $j<r$ is good. The comparison heights can therefore be unbounded. The least tripling disagreement $q$ in the round-nine proposal minimizes a different quantity. The smooth reservoir is available under the `FirstTower` hypothesis. Applying it at round nine's selected $q$ requires an additional identification or an actual merger.
- If $3^r w+1=2^M a$ with $a$ odd, the lower power makes $a$ good. In the strict regime $2^M>3^r$ one has $a<w$ and $3^M a\equiv1,11\pmod{16}$ at a first tower. For $r\ge2$ its source also avoids 85 modulo 512. A reference with $T^h(3^r v)=1$ produces an actual merger between the lifts at $v+4\cdot2^h t$ and $v+3\cdot2^h t$. Its existence for the required lower prefix at a fixed surviving tower is open. The four converging controls in `SMOOTH_RAY.md` rule out unrestricted affine-identity coverage on the one chosen smaller tower. They allow ordinary pointwise meetings. Neither these controls nor the smooth-reservoir theorem supplies a small outside-prime carry for the fixed round-nine source.
- **Independently obtained cycle arithmetic.** PR192's cycle paper already derives the quarter-grid order, rank rotation, $\gcd(h,p)=1$ and the mixed-band congruence under the restricted cycle hypotheses. It supplies a 41-odd rational cycle with $\gcd(C,D)=19$ and reduced denominator greater than one. The earlier PR193 arithmetic paper proves the one-octave conclusion by the complete denominator and credits Knight's balanced-cycle obstruction and earlier ordered-state work. Round nine independently reconstructs the overlapping conclusions.
- PR193 proves in writing that more than $p/21$ odd phases of every sufficiently long primitive ordinary cycle exceed twice its minimum. The local profile-capacity and code results are formal. The authors use Wu–Wang's Theorem 1 with constant coefficient zero to bound the complete-lap logarithmic form. I checked this substitution against the published theorem. PR193 synchronizes high phases and strict companion records on the same orbit. Its reduced companion denominator remains distinct from the physical denominator, and the rotated physical congruences enforce the same divisibility test. This improves the occupancy restriction without ruling out large ordinary cycles. [Wu and Wang, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)
- PR193's exact-clock floor uses F to yield at least a constant times $(4/3)^b/\sqrt b$ integer unit ancestors at each unit $q>1$. The exhibited carries satisfy $\beta\le1$ and are below the fixed relative cutoff for $q>1/\epsilon$. Its occupation theorem and its floor therefore do not supply the missing fixed-cutoff row upper bound at the failure terminals. Its own certificate checker requires a smaller $v$ with $T^i(3q)=T^j(3v)$ for **every** $q>1$. The selector theorem leaves this coverage explicit. Long blocks with convergent lower arms in its minimum construction concern varying starts and finite horizons.
- The final round-nine arithmetic prose now explicitly simulates a joint clock $j\le40(k+1)$ with $T^jm=T^j(3m)$ when choosing the finite-search program's first lift. The same selection also checks both hitting times. This matches the paired construction in round eight. Arithmetic README SHA-256 after this refinement is `42bd1e6a28db80dcb9324f3294d1f0626afae2189b35f9723d9b0319f7a9d317`.

## Independent replay and source binding

I rebuilt the ten newly added Lean modules and the three needed PR192 dependencies directly from the listed blobs in a temporary object directory, with Lean 4.34.1, the local Mathlib dependency objects, warnings as errors and automatic implicit variables disabled. A fresh importing module queried every public theorem from the ten new modules, 34 from PR192 and 31 from PR193. All 65 succeeded. Their combined transitive axioms were `propext`, `Quot.sound` and `Classical.choice`. Each of the three named Python controls produced identical output in normal and optimized modes. This was a targeted replay. The two PRs' complete repository-validation scripts, other Python controls, analytic proof of F and proof of the external logarithmic-form estimate were outside it.

The paths in the following tables are relative to the directory and revision printed immediately before each table. Hashes are SHA-256 of the exact source bytes. “Read” records the written sources used for the comparison. “Lean” records a clean source build, with counts for the ten new modules. “Python” records both execution modes.

**`research/astra-universal-closure-20261124` at `a0d7c6e36c378bbb6c826002039aef486bbe0383`**

| Source | Action | SHA-256 |
| --- | --- | --- |
| `README.md` | Read | `d8c557dcfb99d6aede39f319389e27bbb0118372e09acfb6b6df327807a673ff` |
| `global/README.md` | Read | `d67bd69118e60cb8c76b6809082a1f774def46e79b5cc17e531e80599821facd` |
| `global/SmoothCore.lean` | Lean, 14 | `488bd1d4081e92cfe836d85dd1b27201b4787c46ee395b9196508294684613db` |
| `descent/CORE_PREFIX.md` | Read | `3e4668c30e09c9ad75b1eb89e0c0483601bf4d502fdbf6355471f15db46b744a` |
| `descent/CorePrefix.lean` | Lean, 2 | `fe1699e1431a933a9ed0abb548afa7e029a2620cb8b2a9c2075cc27dc9e7a30d` |
| `descent/SMOOTH_RAY.md` | Read | `98cd45e84b7c57f99fabc5c962c6f18e24e04b24229be62c4fa95be15c8095b6` |
| `descent/check_prefix.py` | Python | `2f09c4439e24e12cb99ea438b1a9fc8019bc74a1fe78a6ce43287fa30453ad9c` |
| `descent/check_smooth_ray.py` | Python | `00f2d5fbf15ffa96b0d2d7158df040681a463bdb2d2ee03a6d1351627848ca0c` |
| `descent/CrossingRank.lean` | Lean, 3 | `2a887a4177e5741a6f927b70a5637d22344c1d61ab1003b2eb9b2f61e396c7bf` |
| `cycle/README.md` | Read | `24629507ac85f3ad5c1f10d526bbb346f695bd03271c38d77f46293fed91b128` |
| `cycle/DecorationControl.lean` | Lean, 4 | `937d521ebadcb9a61f6cc7862e90f1dc11b174c645f8ab42776401636bc19f38` |
| `cycle/RationalBasin.lean` | Lean, 11 | `fdc41d4f3892a379ceb0322361cf8567df2b49b19dada21b279f9f31c4231fd6` |

**`research/astra-universal-proof-20261124` at `24cdd0e5471d4421716cfce6bd88916f858f994c`**

| Source | Action | SHA-256 |
| --- | --- | --- |
| `README.md` | Read | `5e4f6a03671b08e767c1d50fd016297d78141165e851947502aca57599f39dda` |
| `LITERATURE.md` | Read | `92b797e6096d404189ebd5441da74f3fbf314a5164c69a2748f1c4ace2815063` |
| `UniversalProposal.lean` | Lean, 10 | `2f5377e2231af4cfc048f0948c7885fe6244bfe1818072cb91f8ccf6507c132a` |
| `critical/CYCLE_OCCUPATION.md` | Read | `a32c8af6e9c23c3747e2499825876a367c2824709700485766a3e5cf7411ce26` |
| `critical/COMPANION_SYNCHRONIZATION.md` | Read | `0144b105ef63e3a274325df3a1d81c69b3773d99e58fb423967b3da09c6ea200` |
| `critical/CLOCK_MASS.md` | Read | `ab339d1389ab3981dd392a5c1f0ad554d7246c6079e65c6b454a512364b807dd` |
| `minimum/README.md` | Read | `293e7c787a790003dfbb93a7a9de526a84c6fb40c83018e8c9b25023ddc1ae18` |
| `minimum/MovingOctaveOrder.lean` | Lean, 4 | `7541675b4f597dbf94c49232a85c56fddfb84dd84b1fcaa6b325ee7234fd97ac` |
| `critical/OctaveOccupation.lean` | Lean, 6 | `67dc83cf4dea5e2cd003e1c64d6e868d2d72e57301770402791f49137d4599de` |
| `minimum/RunClock.lean` | Lean, 5 | `4ecf880e923700c4f41a0db32e1c2e73f6f63d875e92150316b64d446acdb1d2` |
| `interior/OrdinaryStationary.lean` | Lean, 6 | `df3a5a4384151d2ec42d7c4b8d2a5df77c9e99a53875e8578533d0b24e79cfeb` |
| `minimum/check.py` | Python | `b458fd659b6b714f34ae96559250e8d16f571b6ce20e69b3f63a6caee7bd5d31` |

**`research/astra-minimum-source-20261124` at `a0d7c6e36c378bbb6c826002039aef486bbe0383`**

| Source | Action | SHA-256 |
| --- | --- | --- |
| `arithmetic/SourceDeletion.lean` | Lean, dependency | `21227f38df7f95b29613ec322a1e48f3fc0e423155fb12867c9dfcf546699af0` |
| `minimal/MinimumFailure.lean` | Lean, dependency | `988435d6a6e986d20293593037765775e951a73f1f74e712690ba6ddfc4334c4` |
| `renewal/UpperRepresentative.lean` | Lean, dependency | `4f370f593f549210fe2ef3888d24700702427236f945617e353bfd2ce75227ee` |

The first two dependency files above are byte-identical at both PR192 revisions and in the round-nine vendor directory. The one-octave proof in `research/astra-global-synthesis-20261124/arithmetic/proof.md` has SHA-256 `716dd2fc0d26e09c8bcf499403976a76ccaea6d2df0d094dc3b2a70f62996305` at both frozen PR193 revisions. Section 2 supplies the ordinary one-octave exclusion.
