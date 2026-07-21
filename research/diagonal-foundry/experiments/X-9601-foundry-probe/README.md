# X-9601 — Foundry probe

```text
Experiment ID:   X-9601
Agent:           fable-01
Issue:           #21
Claims:          validates the T-9601 construction; supplies the empirical
                 discoveries behind O-9601, L-9602, O-9602 (all statuses in
                 research/diagonal-foundry/FOUNDRY.md)
```

## Research question

Does the digit-by-digit foundry recursion (T-9601) reproduce the classically
known open-loop answers exactly, and what do the first closed-loop
(feedback) solutions look like?

## Exact code / command

- Code: `run.py` (this directory; dependency-free, standard library only).
- Command: `python3 run.py` (equivalently `python3 run.py 1024`).
- Parameters: `K = 1024` digits built per operator; working precision
  `K + 8` bits; uniqueness spot-check stages
  `[1, 2, 3, 5, 13, 64, 100, 512, 1022]`.
- Environment: Python 3.x, no third-party packages, no floats on critical
  paths, no randomness (the "random" operators are SHA-256-keyed
  deterministic functions of the digit prefix; seeds `x9601a`, `x9601b`).

## Output

`results/foundry-probe.log` (committed; regenerated verbatim by the command
above — the run is fully deterministic).

## Interpretation

- All four constant-operator gates match their closed forms **exactly**
  mod `2^1024`: `(100)^ω → 5^{-1}`, `(1)^ω → −1`, `(10)^ω → 1`,
  `(110)^ω → −5`. This ties the foundry's open-loop corner to the
  repository's known territory (rational itineraries, sign-criticality).
- Every built solution passes an independent replay verifier that shares no
  orbit code with the builder, and uniqueness spot-checks confirm the
  rejected digit fails at each tested stage.
- Discoveries (first run, then pinned as exact gates): shifted quines
  collapse to `−1` and `0`; prefix-parity to `0`; both thermostat operators
  lock onto `−5/3`. Proofs promoted into FOUNDRY.md (O-9601, L-9602).
- Unstructured feedback (anti-correlation, window XOR, keyed hash) yields
  digit density ≈ 0.5 with no anomalous zero runs (O-9602).

## Limitations

- 1024 digits is a finite window: digit statistics are observations, never
  statements about the infinite tail (README §17.10).
- The identity `α_thermo = −5/3` is *proved* (L-9602) — the log alone would
  only certify a 1024-digit congruence.
- No probe here is a counterexample candidate; no `K-####` is issued.
