# LIT-KTHM-0033 — Entropy-surplus routing through symbolic embeddings

**Type:** external theorem and native applicability criterion.  
**Sources:** Krieger's embedding theorem; MacDonald's zero-error sliding-block extension.  
**Maps to:** `PR3/T-0024` and the missing 256-transition stage router.

## Krieger embedding theorem

Let `X` be an expansive homeomorphism of a Cantor space, and let `Y` be a mixing shift of finite type. Suppose

```text
h_top(X) < h_top(Y)
```

and, for every `n>=1`, the number of points of least period `n` in `X` does not exceed the corresponding number in `Y`.

Then `X` is topologically conjugate to a subsystem of `Y`.

For subshifts, the conjugacy is given by a finite sliding-block code and supplies a stationary causal embedding of every admissible source sequence into the target shift.

This theorem is imported as a black box from Krieger (1982).

## Zero-error refinement

MacDonald considers a mixing SFT `Y`, a mixing sofic shift `Z`, and a surjective sliding-block observation

```text
pi:Y->Z.
```

Under explicit entropy and periodic-point conditions, a lower-entropy source subshift can be embedded into `Y` so that the observed code `pi` remains injective. This is the relevant form when a router must preserve both hidden arithmetic state and one visible residue/output stream.

The exact necessary-and-sufficient conditions should be copied from the source before native use.

## Native router criterion

PR #3 proves an aggregate bit-length surplus for one 256-transition stage. That scalar inequality becomes a symbolic existence theorem only after constructing:

1. a stationary source subshift `X` encoding the next-stage demand/bulk stream;
2. a stationary mixing target SFT `Y` whose paths are **exactly** legal 256-transition connector blocks;
3. an entropy inequality
   ```text
   h_top(X)<h_top(Y);
   ```
4. the periodic-point count inequalities of Krieger;
5. a sliding-block decoding map from a `Y` path to the required low connector bits;
6. an arithmetic realization theorem showing that the embedded path initializes from one ordinary marked state.

If items 1--5 hold, Krieger supplies the finite-memory symbolic router. If the visible output must remain injective through a prescribed projection, the MacDonald framework is the sharper target.

## Why this shortens the proof search

The native theorem `PR3/T-0024` already shows that raw information capacity is not the scarcity. The embedding theorem says the remaining symbolic problem need not be solved by hand with one enormous substitution table: it can be reduced to

```text
mixing + entropy + periodic point counts + exact arithmetic realization.
```

This cleanly separates:

- **symbolic routing**, potentially handled by embedding theory;
- **arithmetic legality and ordinary initialization**, still native.

## Nonapplication boundary

The current stage system is scale-dependent (`m` changes), carries exact congruence domains, and has an unbounded stack. It is not yet a stationary SFT. Entropy surplus alone does not imply an embedding, Hall expansion, or correct low bits.

A useful first result would be a finite-state normalized stage relation after factoring out the explicit odometer and logarithm digits. If that normalized relation is mixing, symbolic embedding theory becomes directly actionable.