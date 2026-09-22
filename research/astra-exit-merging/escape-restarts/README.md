# Actual escape restarts

**PROPOSED pending independent mathematical review. Not a Collatz proof.**
Continuation of #132 at `7687eec1ac364009d644cb8d015f1fe3b28730cc`;
combines with the separately pinned #129 R/valuation language.

[Read the proof](PROOF.md) · [Sources and boundaries](SOURCES_AND_LIMITS.md) ·
[Replay instructions](../../../experiments/X-AEM-007-escape-restarts/README.md)

The starting comparison is R(D)=(3D-4,D), D>=2, reached from
H(C)=(9C+2,C) on C=7 mod8. The previously abandoned K(E)=(9E-10,E)
branch now returns to R whenever E=2 mod4. In original R coordinates,
this is the whole class D=13 mod16.

Three added returns, together with the credited old return, satisfy

```
0 <= D_next-2 <= (6/7)(D-2),  D_next < D.
```

The given integer chooses its guard. Any actual interleaving therefore
terminates after O(log D) stages in a merger or an explicit outside state.
No input digits are changed, no rank is reset, and no convergence premise
is used for this partial normalizer. One new 15-step return passes through
an expanding 11-step return before reducing the parameter; accepting only
the expanding part would be unsound.

Every finite word in the four returns has a complete residue-class merger
continuation. Families starting with one of the three new returns are
OUTSIDE at time zero for the exact #129 selector. This is **not** a claim
that they escape every later repository method. They lift to original
sources with m=(N-3)/4 and actual unequal prefix clocks. For sufficiently
long first odd runs, the entire original arm stays above N and CRT can
force 3|N, excluding any smaller pure ancestor.

Example:

```
N=499228671, m=124807167;
T^28(N)=T^26(m)=2161541018;
min_{1<=j<=28}T^j(N)=748843007>N;
0<4m<N, 3|N.
```

The new finite experiment has 135,584 rows. On the same C=1..65536 grid,
it preserves the 5,082 #129 certificates and supplies 173 more, leaving
60,281 OUTSIDE. These are comparison-procedure outcomes, not convergence
percentages and not a comparison against the union of #130/#131/#132.
The standalone verifier independently reconstructs OUTSIDE outcomes too.

## What remains

The other K rows and remaining R guards are not solved. This finite
normalizer is not a universally successful selector. C=17 and C=71
remain OUTSIDE here despite their isolated actual mergers; H(2)=(20,2)
never meets synchronously because of opposite eventual core phases.
The global task remains a root-compatible restart or other proof at every
actual finite escape, not another assertion that a constructed success
subprogression contains the given input.

No existing proof or scientific status is edited by this packet. Publication
and execution limits are recorded separately in the report directory.
