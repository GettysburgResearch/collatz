# Independent review of the ordinary source cases

Scope: source reconstruction on the files below of GettysburgResearch/collatz, against PR197 at b27a6fe31a487adf5615e173329ad009b975a3cd. Root separately executes the clean Lean replay. This review was limited to the listed scientific sources, the inherited definitions in FinalProofProposal and their stated inputs.

| File in research/ayh-resource-reset-20261124/source-progress/ | SHA-256 |
| --- | --- |
| SourceProgressCases.lean | 3f4302bbe12eb79445c04a855a0f01878e1f573501243d3ef101f9e04d569f93 |
| TernaryPowerLift.lean | 5ff83d37cdb629a2b036dcaf69c518ecdd8e84f15f940edf645cedba9bbe063f |
| WordRank.lean | 873802f2b394de8de1be50a24f94847dcbdc35c5881272271432adbdbdbc30fe |
| OrdinaryWordRealization.lean | d160b8a77442e71f55f4ad9f68b22af05760930468839aa92296facd15ad3229 |
| PositiveWordDescent.lean | f6499c78faad234b376b5e306e8c7e64949912656623ca7291b46e14f14d0f19 |

**Verdict: VERIFIED as a reconstruction of these conditional and pointwise statements.** The existence result fixes $q\ge2$, a finite lower word $W$, an upper rank $r\ge q+44+2|W|$, and any source floor $L$. It constructs $z\ge L$. A different tuple may use a different source.

The dyadic power lift reaches cofinally every prescribed unit class modulo a power of three. Each lift exposes one further trit, using $2^{2\cdot3^j}=1+3^{j+1}(3u+1)$, which cycles its new ternary digit through all three possibilities. The first $W$ bits at the lower arm select an odd-slope binary subprogression. On the associated upper ternary unit row, the construction appends $R$ consecutive odd departures and then reaches a power $2^e\ge4$. The subsequent $e$ halvings give a first hit, since a previous visit to 1 would restrict the remaining orbit to $\{1,2\}$. For a prescribed word followed by $q+40+|W|$ zero bits, its forced count $s$ is at most $q+41+2|W|$. Thus choosing $R=r-3-s$ is legal and yields exactly the stated first-hit upper rank.

The ordinary deduction starts at the same $z$: $2T^{q+8}z+1=3^q t$ and the all-even suffix exactly divides the delayed lower endpoint by $2^{q+40+a}$. Combined with $T^a x\le2^a x$ and the actual affine source equation, this gives a positive ordinary iterate $n$ with $2^{40}n<z$. Its basin is the original basin. The least-defect exclusion gets a strictly smaller genuine reverse defect from the already proved quantitative return applied to this same $n$ if $z$ is bad. Its contradiction uses no population or probabilistic premise.

RemainingProgress is explicitly an argument of collatz_from_remaining. That consumer uses the pointwise case whenever TailCase holds and the stated open premise otherwise. The reverse implication proving equivalence assumes UniversalConvergence; it does not supply the open premise. The exported dense_closing_cases conclusion contains SourceProgress at the constructed source. It does not explicitly return TailCase as a conjunct, although its construction imposes the requisite odd cofactor and zero word. No proof for an arbitrary supplied higher-rank witness follows.
