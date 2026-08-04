# Positive cycle synthesis and classical cycle bounds

## Exact algebra

For an accelerated valuation word, `LIT-KTHM-0015` gives the affine monoid and `LIT-KTHM-0023` gives

```text
(2^A - 3^k) n0 = C.
```

This equation is the correct arithmetic gateway. Divisibility and positivity reconstruct a candidate; exact valuation replay is still mandatory.

## Located cycle literature

- Eliahou: lower bounds on nontrivial cycle lengths.
- Simons–de Weger: theoretical and computational bounds for `m`-cycles.
- Hercher: no Collatz `m`-cycles with `m <= 91`, where `m` is a local-minimum parameter.
- Sterin–Woods: a neighboring reverse cellular-automaton representation.

## Parameter discipline

The literature uses several inequivalent counts: odd accelerated steps, total unaccelerated steps, local minima, and blocks between minima. A solver may use a published exclusion only after proving that its expanded object has the source theorem's parameter.

## Proof-producing solver output

A useful certificate contains:

1. the compressed grammar derivation;
2. expanded valuation word or independently checkable straight-line program;
3. `k`, `A`, local-minimum count, and affine constant `C`;
4. factor/residue evidence for `2^A-3^k`;
5. the reconstructed positive odd integer;
6. exact intermediate valuations and return;
7. a tiny dependency-free replay verifier;
8. the exact bounded grammar/parameter frontier when no solution is found.

## Coordination

Issue #9 and PR #11 should share one affine summary implementation, one certificate format, and one verifier. Distinct search grammars can remain separate experiments.