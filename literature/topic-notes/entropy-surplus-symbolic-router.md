# Entropy surplus and symbolic routing

## The native state

`PR3/T-0024` proves that a full 256-transition stage generates asymptotically more residual bit length than the next connector depth requires:

```text
generated slope  ~ 14.29 * 2^m,
connector demand ~ 11.04 * 2^m,
surplus          ~  3.25 * 2^m.
```

The theorem correctly warns that bit length does not determine low bits or produce an invariant arithmetic cylinder.

## Symbolic-dynamics connection

Krieger's embedding theorem is the rigorous form of the slogan

```text
entropy surplus + periodic compatibility => finite-memory embedding
```

when the target is a mixing shift of finite type. MacDonald's zero-error refinement treats embedding through a prescribed sliding-block observation.

This suggests replacing a hand-designed 256-column substitution by a proof that the **normalized legal connector relation** is a mixing SFT with entropy above the demand process.

## Required normalization

The raw stage is not stationary because:

- stage scale `m` grows;
- odometer depth changes;
- the logarithmic bulk reveals a new digit;
- connector moduli grow;
- the marked ordinary residual changes size.

A stationary symbolic relation may emerge after separating explicit coordinates:

```text
known odometer phase,
known next digit of -(7/4)log_2(3),
finite tower type,
finite connector residue class,
normalized surplus block.
```

The goal is a finite alphabet whose legal transitions are independent of `m` after this normalization.

## Proof program

1. **Finite alphabet:** identify the minimal residue/carry data needed to certify one normalized transition.
2. **Exact adjacency:** compute the finite directed graph of legal normalized transitions, with an independent verifier.
3. **Mixing:** prove the graph is primitive or identify its cyclic decomposition.
4. **Source shift:** encode required future bulk/odometer digits as a subshift `X`.
5. **Entropy:** compare `h_top(X)` with the Perron entropy of the connector graph.
6. **Periodic points:** check the exact period-count condition, not only entropy.
7. **Embedding:** invoke Krieger, or MacDonald if a visible output projection must stay injective.
8. **Arithmetic lift:** prove the symbolic path corresponds to one ordinary initial residual and not only a completion point.

## Why information surplus alone is insufficient

A large set of possible outputs can all share the wrong low bit. Entropy is an asymptotic orbit count and does not imply local Hall expansion or arithmetic initialization. The symbolic theorem becomes applicable only after exact legal transitions and periodic obstructions are encoded.

## Alternative finite combinatorial route

If the stage router is naturally finite but time-inhomogeneous, prove Hall-type expansion for the bipartite graph from current stack prefixes to next-stage demands. An infinite compatible matching then follows from compactness/König arguments. This is more elementary but may require stronger local expansion than entropy embedding.

## Success criterion

The useful outcome is not merely a symbolic embedding. It is a machine-checkable finite router plus a proof that one ordinary marked state enters and follows it forever.