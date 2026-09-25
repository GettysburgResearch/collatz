# Exact dyadic completion and actual odd-edge repair

**PROPOSED, not independently reviewed. No full Collatz proof.**
Read [PROOF.md](PROOF.md), then [VALIDATION.json](VALIDATION.json).

This additive continuation of PR #138 retains every halving equality and any
finite set of actual odd edges. It solves that ordinary separation problem
exactly, at a finite or infinite height, through a finite compressed interval
graph. Infinite costs are certified as A*zeta(2)+B with rational B.

The main results are lossless elimination (DC-001), an exact infinite completion
and finite tail phase diagram (DC-002), a sharp fresh-ray repair bound (DC-003),
an actual two-edge example requiring an old label to change at cutoff 2^30
(DC-004), and finite complete-edge constraint generation (DC-005). An upper
repair budget uniform over arbitrary insertion orders is refuted; the original
complete-height upper target remains open (DC-006).

The example with source 7 at 2^30 concerns a deliberately incomplete retained
odd-edge set, NOT an actual Collatz trajectory delay. Likewise solving a problem
at symbolic height 2^1025 does not mean all odd edges below it were checked.
The full finite-edge oracle explicitly scans its finite cutoff.

## Replay

From this directory, with standard-library Python:

```sh
python -S -B run.py --output /tmp/dc-corpus.json
python -S -B verify.py /tmp/dc-corpus.json --self-test
python -S -B check_models.py
```

Repeat with `-O` or `-OO`. Checks use exceptions, not removable assertions.
`check_models.py` also reads the preserved
`../anchored-cuts/experiment.py` as a bounded full-graph comparison reference.
The standalone verifier does not import it or any producer code.

The deterministic corpus contains 46 completion certificates and six
finite-height refinement traces, with all 50 round certificates retained.
It includes exact infinite completions, a symbolic finite cutoff 2^1025,
the sharp 27->41 repair, both sides of the source-7 phase transition,
27's actual 70-step convergence, p=5 controls, and a genuine round-cap outcome.
Large reproducible output is not committed; VALIDATION.json pins its hash.

## Boundaries

All-halving + finitely many odd edges is not the full infinite Collatz graph.
Infinite completion provides a real function on every positive ordinary integer,
but it satisfies ONLY the specified odd equalities. Unlisted equalities are not
asserted. The literal convergence result is returned only when the retained
physical edges connect the original pins, with a replayable actual path.

The finite graph structural bound is O(mD), not a uniform running-time bound for
full Collatz coverage. Symbolic arithmetic has a precision cap; finite refinement
has a round cap. Resource exhaustion is explicit. The code is research tooling,
not a claim of hardened untrusted-input processing or a remote execution service.

Full independent review and the source-dependent, height-uniform COMPLETE-graph
repair bound remain outstanding.
