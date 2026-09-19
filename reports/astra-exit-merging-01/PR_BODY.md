## Proposed two-exit source-merging theorem; refs #121

**No complete Collatz proof. All new statements are PROPOSED pending
independent mathematical review. No external novelty claim.**

Publisher: insert the actual commit SHA and publisher-run checks here. The
authoring packet itself was not remotely published; preserve that receipt.

Base: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
Only additions under `research/astra-exit-merging/`,
`experiments/X-AEM-001-exit-merging/`, and `reports/astra-exit-merging-01/`.

### Main mathematics

For `n=8^k u-5`, u positive odd, read
`h=v2(9^k u+1)-4` and `a=(9^k u+1)/2^(h+4)` from the input. If h>=1 and
`3^(h+1)a=1 mod4`, explicit physical words give

```text
T^(3k+h+6)(n) = T^(3k+h+5)((n-5)/2).
```

The words cross unbounded repeated expanding 110 blocks, their actual exit,
a second unbounded odd run, and its guarded exit. The smaller witness is
relative to the original source, not the last inflated state.

When 3|n, one more inverse step composes to

```text
T^(3k+h+6)(n) = T^(3k+h+6)(n/3-2), with 0<n/3-2<n/3.
```

For all guarded k>=23, the original source's entire displayed forward arm
remains above n. Because 3|n, no pure smaller ancestor exists at any backward
depth either. An explicit CRT family realizes both unbounded length parameters
inside the old normalizer's n=3 mod12 residual class.

The reduced source is x=7 mod32 for k>=2. Its hard exit and the complementary
input guards remain unresolved; no universal successful selector is claimed.

### Read

`research/astra-exit-merging/PROOF.md`, especially Sections 3–5.
`SOURCES_AND_LIMITS.md` credits Sodelin's prior good odd-exit merger and
separates the source-halving construction from related forward-repayment work.

### Authoring evidence

Generator/check and independent verifier passed normally and under -O;
verifier also passed a separately completed -OO run. Outputs agree across
modes. The bounded corpus contains 1,084 CRT family cases with two physical
certificates each, 380 no-forward-descent cases, 128 even-exponent Mersennes,
2,048 good odd-exit certificates, a complete small ambient grid with retained
failures, and all partial-normalizer chains on 2..4096.

The verifier reconstructs CRT inputs through a different modulus, checks raw
parities and independent affine endpoints, and verifies the whole seed residue
cylinder symbolically. Twenty re-sealed envelope corruptions and four direct
bad controls are rejected. Same-author implementation diversity is not
independent mathematical review.

The exact semantic payload hash is
`207bdb81b078c67fb18a304d0997b988e747f0dad165546e18cf6343c6783b8d`.
The author did not execute full-repository validation, external Lean, CI, or
Windows/browser tests. The receipt records an interrupted combined-command
-OO attempt separately from the later successful standalone -OO rerun.

No existing claim, canonical status, license, settings, workflow, or main
branch is changed. This is an exploratory packet, not an integration approval.
