# Cycle denominator execution record

**2026-11-24.** The two standalone Lean modules both completed with exit status 0 and warnings treated as errors. All ten public declarations emitted transitive axiom reports. DenominatorBudget’s eight use only propext and Quot.sound. ValuationDominance’s two additionally use Classical.choice. The raw diagnostics are [DenominatorBudget.log](DenominatorBudget.log) and [ValuationDominance.log](ValuationDominance.log).

| Component | Checked version |
|---|---|
| Lean | 4.34.1, x86_64-unknown-linux-gnu, release commit 5045d0056413266e57c625dcd7c365b10e377c52 |
| Mathlib | d13f23b723b8a846827a245b89c10fc7d3f11612 |
| Python | 3.12.14 |

From the repository root, with the pinned Mathlib and package object directories on LEAN_PATH, the invocation for each module was equivalent to

    lean -DwarningAsError=true -j1 research/astra-global-closure-20261124/closing/cycles/DenominatorBudget.lean
    lean -DwarningAsError=true -j1 research/astra-global-closure-20261124/closing/cycles/ValuationDominance.lean

DenominatorBudget proves exact product comparison after closing a finite path, divisibility equivalence at a signed cut with Bézout data, divisibility for nested gaps, and the two cross-carry identities. ValuationDominance proves the per-prime cover implied by a maximal coefficient and the truncation of that cover. The entire rational-word realization, logarithmic height estimates, multiplicative independence theorem, and counting asymptotics are written mathematical deductions. The Lean kernel did not verify those complete deductions.

Both commands below returned status 0 and produced byte-identical JSON. The checker uses explicit exceptions for failed conditions. The output is saved in [controls.json](controls.json).

    python -B research/astra-global-closure-20261124/closing/cycles/check.py
    python -O -B research/astra-global-closure-20261124/closing/cycles/check.py

The checker enumerated all 16,382 marked words of lengths 1–13, including 13,509 positive contracting words. It tested 1,131 distinct positive primitive necklaces, 12,282 proper centers, and 61,997 unordered cut pairs, including both signs of the clock gap. For 1,099 nonzero near-return center families it computed exact rank using rational row operations on signed prime valuations. Of these, 1,090 were multiplicatively independent and the sufficient gcd-overlap criterion certified 1,057. The bounded sample compares finite algebra and does not test a putative large ordinary cycle. It also checks the per-denominator count, reciprocal moment and the disjoint-cycle product inequality.

| File | SHA-256 |
|---|---|
| DenominatorBudget.lean | defafaf8f5fb735e4ad12f7119be0361fb43b787d9061253cf102ee34f0638bb |
| NEAR_MINIMUM.md | 2d1c75cb221917c038e3929e6c73004a442445537de843f78db2f1ffea26fad5 |
| README.md | 1c5723869e3145d4e2236ef1c7fdfd7f47cec8cbc6a81e410dd83a4744f48840 |
| ValuationDominance.lean | c9bc26ec2b1e91d1ac8cbabc8fc510c39bf33475e6f211be34be84e9fead4c39 |
| check.py | e2052a83511768e1eaf4d7ac714e7f23995f077694689cdc13c83a3a4969f7a9 |
| DenominatorBudget.log | c66dbcbe62d5c3d2446230ffbb174c5099a94c87bd1582c2a041a1f579a5618d |
| ValuationDominance.log | b9631e227b592199704cdfe5d13ef39186a2f740bd682b6edec55bcc5e4204df |
| controls.json | f2a4dc16f840471e5610f8159cc65f5d6bb303dde507692617041a29df38ab0f |
