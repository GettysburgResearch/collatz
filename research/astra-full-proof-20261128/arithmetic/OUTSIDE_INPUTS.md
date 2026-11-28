# Outside inputs and two purported full-proof imports

The pass permits the use of outside theorems whose authors report a successful
Lean check. The theorem's mathematical statement still matters. We distinguish
that reported check from a local rebuild, and from a local check of a small
independent consequence or counterexample.

## Qualified inputs retained

- **Mazur, positive lower density of predecessors**, manuscript v1.0,
  6 September 2026. A positive counterexample forces positive lower natural
  density of nonconvergent positive integers. This covers both failure modes.
  The primary release reports successful Lean checking of the narrowed
  three-statement interface. **OUTSIDER-REPORTED LEAN; not rebuilt here.**
  [Paper](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf)
  · [exact counterexample-density statement](https://www.proofatlas.ai/proofs/artifact.collatz.nonconvergence_positive_lower_density.v001.html).
- **Lau, explicit positive lower density**, Hexagon `2610.00249v2`.
  The stated result also reaches eligible prescribed targets. The primary
  release links the AxiomProver formalization and its Palomar record.
  **OUTSIDER-REPORTED LEAN; not rebuilt here.** This is an alternative density
  input, not a proof that the basin of one has density one.
  [Primary release](https://hexagonmath.org/2610.00249v2)
  · [formalization record](https://palomar-registry.org/entry?id=PALOMAR-2026-10-15-000013&version=1).
- **Inselmann, near-half parity counts**, Theorem 3.3 of arXiv
  `2402.03276v3`. Its physical clock ends at the stated critical scale;
  the five-times-bit-length upper-tail statement is a further assertion.
  **WRITTEN external theorem; no local Lean claim.**
  [Primary manuscript](https://arxiv.org/html/2402.03276v3#S3.Thmtheorem3.3).
- **Valbuena, existence of predecessor natural densities**, repository
  x1xhlol/collatz-two-coordinate-obstruction at
  a7275d5a73814d3d9a400c6fe6577de9542b03a3. The closing native-boundary
  note uses only the existence of each fixed target's ordinary natural
  density to recover a mean from finite target-hit indicators.
  The primary release reports the Lean 4.30.0-rc2 native foundation
  and additive bundle audits, distinguishing fresh compilation from
  authenticated dependencies. **OUTSIDER-REPORTED LEAN; not rebuilt here.**
  The coordinator read the pinned primary README. The finite full-proof
  consumer does not require this optional mean-existence input beyond
  its separate positive-predecessor premise.
  [Pinned statement and reported verification scope](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/README.md).

## A bounded certificate asserted by a full-proof repository is false

We inspected `AIDoctrine/CollatzLayerA` at commit
`5e27e335c8a1bca3b0cf2f89ee593d7bbe6d08fd`, file
`CollatzLayerA_v8_1_FINAL.lean` (blob
`09c4f01648d9fecc734c3905fb0e9c3fc658e1c7`). Its main theorem uses a
project axiom named `odd_steps_certificate`. The declaration asserts that
every sufficiently large odd source in `3 mod 4` admits a raw clock at most
200 with at most 44 odd departures and at least 71 even departures.

Take the positive integer `n = 2^100 - 1`. Its first 100 shortcut departures
are odd: after `j` of them, for `0 <= j <= 100`, the value is
`3^j 2^(100-j) - 1`. Therefore its first 200 **raw** steps alternate an odd
departure and an even departure. At any raw clock at most 200, obtaining 71
even departures requires at least 71 odd departures. The asserted certificate
does not exist for this source. All input guards, including `n >= 2^71`, hold.

Our independent `ExternalClaimChecks.lean` defines the actual raw map and
odd-departure count and refutes this exact universally quantified certificate.
The finite computation is kernel evaluated; the theorem's printed axioms are
only `propext` and `Quot.sound`. **LOCALLY COMPILED in Lean 4.34.1.**
We did not rebuild the external development and do not assert that its source
fails to compile. Compiling a conclusion from a false project axiom does not
provide the desired external theorem.

[Pinned external source](https://github.com/AIDoctrine/CollatzLayerA/blob/5e27e335c8a1bca3b0cf2f89ee593d7bbe6d08fd/CollatzLayerA_v8_1_FINAL.lean).

## A second terminal statement is not Collatz reachability

We inspected Saty Raghavachary's `CollatzProof.lean`, Zenodo record
`21960729`, v1, published 15 August 2026, recorded MD5
`8a01a91a5ee927b346a1d4916924a961`.

The terminal declaration named `CollatzConjectureIsTrue` only says that the
value of an assumed natural-number-valued function `traj_len` equals some
natural number. This is true for every function of that type; it does not
assert an iterate reaches one. Separately, the source's
`nR_bounds_for_gt1` axiom puts a natural number strictly between three and
four for every eligible source. The eligible source five already makes
this inconsistent, regardless of how `nR` is defined.

The independent local file proves both the generic tautology and the
impossibility of that bound. **LOCALLY COMPILED checks of those statements;
the author's full file was not rebuilt.** Neither purported full-proof
source is used as a theorem dependency of this pass.

[Versioned record](https://zenodo.org/records/21960729)
· [inspected source](https://zenodo.org/records/21960729/files/CollatzProof.lean?download=1).
