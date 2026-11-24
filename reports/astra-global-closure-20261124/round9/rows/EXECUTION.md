# Exact-row execution

The read-only upstream source was `research/clock-itineraries/TernaryItinerary.lean` from PR206 commit `37d2b5d644664a746891042c199e58cfb06f1176`. Its SHA-256 was `b79cfc44200087ac0ca9bed9daab9c83a64487bbdb29a4e1e410ba7d6d3f8112`. No upstream source edit was necessary. Lean's `import all` in the new module makes the definitions of the actual upstream maps available to kernel reduction.

The final run started in a fresh directory with the pinned source and [FiniteSurvival.lean](../../../../research/astra-global-closure-20261124/round9/rows/FiniteSurvival.lean). Lean 4.34.1 for x86-64 Linux, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, built the upstream module and then the new file. Both invocations returned zero with warnings treated as errors and auto-implicit declarations disabled. The new source SHA-256 was `104c52cc8a4bef5dc2e6d7d186653ca9a2339c60428231a51e155c2382f7a96d`. All seven new printed dependency lists use only `propext`, `Classical.choice` and `Quot.sound`. [Upstream output](TernaryItinerary.log) · [New theorem output](FiniteSurvival.log)

The separate [BarrierEnvelope.lean](../../../../research/astra-global-closure-20261124/round9/rows/BarrierEnvelope.lean) uses only Std. The same compiler and flags accepted its final source, SHA-256 `d5f647ba9ea7255b2eabd2340ff9fb15e18a7e4fb2c8794cfaaaac938c516bf9`. Its six printed declarations cover the one-step carry invariant, the running-maximum update, the balanced envelope, the physical affine equation, the literal power-of-two denominator, and the relative cutoff at the supplied source and endpoint. Every printed axiom is standard. The complete reflection bijection and the endpoint-uniform asymptotic consequence have written proofs in [UPPER.md](../../../../research/astra-global-closure-20261124/round9/rows/UPPER.md). [Barrier kernel output](BarrierEnvelope.log)

From a checkout with the pinned commit available, the following commands reproduce the build, using a Lean 4.34.1 executable on the search path.

```sh
rows_build=$(mktemp -d)
git show 37d2b5d644664a746891042c199e58cfb06f1176:research/clock-itineraries/TernaryItinerary.lean > "$rows_build/TernaryItinerary.lean"
cp research/astra-global-closure-20261124/round9/rows/FiniteSurvival.lean "$rows_build/"
cp research/astra-global-closure-20261124/round9/rows/BarrierEnvelope.lean "$rows_build/"
(
  cd "$rows_build" || exit 1
  lean -DwarningAsError=true -DautoImplicit=false -o TernaryItinerary.olean TernaryItinerary.lean &&
    LEAN_PATH=. lean -DwarningAsError=true -DautoImplicit=false -o FiniteSurvival.olean FiniteSurvival.lean &&
    lean -DwarningAsError=true -DautoImplicit=false -o BarrierEnvelope.olean BarrierEnvelope.lean
)
```

The [Python replay](../../../../research/astra-global-closure-20261124/round9/rows/check.py) has SHA-256 `b3c6d9538f84138f7d3d6741db5d486957ccaf6f0e268685386cf599eb7d07a5`. It ran under both `python -X utf8 -B` and `python -O -X utf8 -B`, reproducing identical [control output](controls.json) with SHA-256 `3dbe724ad6bf21d044a794bf5a31066bb3440921e12593729b42347b039ddb1a`. It checked the carry envelope at all 125,476 balanced words with first input odd and odd depth one through ten, and matched all 55 barrier histograms with the exact binomial reflection count. It also evaluated the 2,272 finite raw cases, including 351 surviving endpoints, and all 32 cutoff cases. The independent two-gap constructor and forward replay recovered 862 distinct source records across seven rows. Each record was checked at the prescribed marks, exact gaps, gate, whole clock, actual endpoint and relative carry. All seven endpoints reached one by further direct iteration. Eight separate small parameters also exercised the immediate-terminal identity. These executions concern the finite claims and examples. The asymptotic amplification under F and the fixed-threshold upper-bound obstruction are assessed in the [mathematical packet](../../../../research/astra-global-closure-20261124/round9/rows/README.md).
