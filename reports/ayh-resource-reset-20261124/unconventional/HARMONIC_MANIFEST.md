# Ordinary wall packet

The 22 mathematical Lean modules contain 90 public named theorems. The following order is topological. Each module uses Lean 4.34.1, Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612` and project baseline `f74d2144275c3e1f9148b0b2997fecc7931ae7f5`.

| Module | Local imports | Public theorems |
|---|---|---:|
| `WallRefinement` | baseline or Mathlib | 8 |
| `WallGate` | WallRefinement | 9 |
| `WallShadow` | WallGate | 2 |
| `WallWheel` | WallGate | 3 |
| `WallPeriodic` | WallShadow, WallWheel | 4 |
| `WallRun` | WallPeriodic | 5 |
| `WallBank` | WallRun | 2 |
| `WallRuns81` | WallBank | 2 |
| `WallRational` | WallGate | 4 |
| `WallAffine` | WallRational | 6 |
| `WallOrbit` | WallAffine, WallPeriodic | 7 |
| `WallGeneral` | WallOrbit | 6 |
| `WallUniform` | WallGeneral | 4 |
| `WallWords` | WallUniform, WallRun | 3 |
| `WallExamples` | WallGeneral | 4 |
| `WallTernary` | WallWords | 4 |
| `WallDichotomy` | WallTernary, WallExamples | 2 |
| `WallDensity` | WallDichotomy | 5 |
| `WallEscape` | WallDensity | 2 |
| `WallShifted` | WallEscape | 2 |
| `WallLinear` | WallShifted | 1 |
| `WallDelay` | WallLinear | 5 |

`WallAudit.lean` follows these modules and explicitly checks the axiom lists of 39 headline results. An independent audit of all 90 source-declared public results was run on the same build. The build uses `-j1 -DautoImplicit=false -DwarningAsError=true`.

`WALL_RESULTS.md` contains the mathematical narrative, precise scope, formal theorem names, and limits of the approach. `DELEGATE_REVIEW.md` records independent checks of the critical arithmetic and adelic packets.

The two finite replays are independent of Lean. Their exact outputs are checked into the packet.

```sh
python -O check_wall_controls.py | cmp - wall-controls.json
python -O check_wall_periods.py --through 30 | cmp - wall-periods30.json
```

## File digests

- `2df74c249a738f96dedc299252f12ca6d3afff338045e0f122bab46c41218792`  `WALL_RESULTS.md`
- `5718b7b0dab835401049364efc37ca6a224048c74d6d313283cc2239b80ee50b`  `DELEGATE_REVIEW.md`
- `2a301cdd05d6455b516f8a4a5e07e4e5a4398339d97733b39f6194d62f1806e6`  `check_wall_controls.py`
- `1991053aa2d7e9b5008792eb85017f5716dc94f24899b6be704b6ee2b05fc3f7`  `wall-controls.json`
- `85b71251366d5b41b4f9782f5c8aaf0a5ad5e123f0af6e8da5b10ad6db9c1770`  `check_wall_periods.py`
- `dd9e107b4aee6e1b126326f2257573a20b2fc2207e3b3402979074c45f4283db`  `wall-periods30.json`
- `467ba3bfad48e3032d4f3a348f70db163db818a5231f147118991218ea34b7fe`  `WallAudit.lean`
- `8b43349120e485ca7973d709fc6e6114413735f5cb3318432e2162d32573efd3`  `WallRefinement.lean`
- `1262877d3faa67ac01192ac1a63a1ff1de87e55c25c6803c21cd86828c60646a`  `WallGate.lean`
- `c866ec3a0beac7eec7b9783ecccf503ce14902f0573c35b1751472df59a532fb`  `WallShadow.lean`
- `efa58cec5cfede3617e1da88bcf1851762e6d0cf44a5ed8b3dca4cbcfe40605e`  `WallWheel.lean`
- `cccda4c3cfeb0843bc3eb5957bc0835c3096100d8d3c1b65431421446d24d2a8`  `WallPeriodic.lean`
- `4218149598edc98a3a72f72a9429b1b999666f8302bb770e67fb34ca4d54ed74`  `WallRun.lean`
- `52798220d573f0e0b70ee9628630c89db3460338c56a6f078aa34d2c5d3c203a`  `WallBank.lean`
- `92329f3cf6ece9e4408b6fe33e8879024639c0775e7c5836434252051b7036b8`  `WallRuns81.lean`
- `637c55447ea73463e6819a162b7c7524982f4d780ff9edecc83e38567cb33a00`  `WallRational.lean`
- `7481ee6ef874239ea42f883159a0a33e442f07a6c0b7d80074fc10a04b436193`  `WallAffine.lean`
- `8ec60ea8b757f4cee07e8d7b7a13b4fc7e5356a32207b4ab55be725ffe10c867`  `WallOrbit.lean`
- `cdadb60455d6a192c3be4c9409671111592e3850299cb52ae3f115415603a7a0`  `WallGeneral.lean`
- `664fe0fe217c8c20180ee0210c162766d1cd5361064c449a80399f6b25306a8f`  `WallUniform.lean`
- `fdd679d10ba7ad357b94243330e8f70066733249a9536083fe031ea60eab8607`  `WallWords.lean`
- `59f8117544701d7c27340e72235aed3027f38cce143f8a6f476e69c428f855c7`  `WallExamples.lean`
- `9607867398a3a6a6006946f4fe1f8cd0dcbea9c650cd332eca6f3b0ed6136d9c`  `WallTernary.lean`
- `7325b9e89decf7825774f7e46e3638e6f2eb290beeac759f491d9d28bd7ddcb8`  `WallDichotomy.lean`
- `1cfc6a0d736766df3caab83240bd930f3443ce23bb5808758b79ae7150153701`  `WallDensity.lean`
- `7892e34052317164e6f56da20efca882b13d08c7a32a58bad080a5fb3b51d342`  `WallEscape.lean`
- `0f00312fc6494abefbecc735586d2a1555cc7321edbf17dd9fd7804a50be6494`  `WallShifted.lean`
- `3481b846bd6cdb8153929d83a43ba9d976492fde01879d9a40abd924e30c4ef7`  `WallLinear.lean`
- `b5920220b206f91e46847fa011b0c846468e7ea5c65eb26eef0a77f838947d02`  `WallDelay.lean`
