# Exact source interfaces and attribution

**This is a dependency and comparison record, not an endorsement of every
claim at each cited head.** New proofs and their scoped reviews live in
this packet. Earlier source results retain their stated qualifications.
The [metadata snapshot](source-snapshot.json) records the inspected heads.

## New local arguments and their dependencies

| Local claim | Exact input | What is newly argued here |
| --- | --- | --- |
| RU1–RU3 | Positive odd recurrence; Evertse Theorem 3 | Complete degeneracy classification for a fixed-length shifted equation, injective unit encoding, and excursion count. |
| FD1–FD3 | Same recurrence and external unit theorem | Nondegeneracy after compression to defects, with the unbounded length recovered from the normalized vector. |
| EF1–EF3 | Local RU2 only | Exact block/gap incidence and run clock, then superlogarithmic and explicit iterated-logarithm outside frequency. |
| EF4 | EF3 and PR161 SS1–SS2 | Convergence under the specified sparse-excursion upper bound, including `O(log N)`. |
| HT1–HT5 | Actual affine odd words and deterministic first-hit paths | Complete homogeneous decoder, its architecture scope, complete minimal initial-one classification, three cylinders, and explicit limitations. |
| ER1–ER4 | PR166 FL1–FL3 and local HT3–HT4 | Joint endpoint-residue constants, expanded-domain renewal, and exact adjacent remainder for all first valuations at least three. |
| DC1–DC3 | Exact source and endpoint residue fractions | Harmonic mean identity and its qualified consequence for positive inverse-fiber bounds. |
| Homogeneous localization | Local HT1–HT2 and PR146 proportional lifts | Cancellation equivalence for complete decoder admissibility, with an infinite solved family outside the recognizer. |
| Latest reduction boundary | PR146's latest Mersenne/least-failure interface, PR164 domain statements, local RU2 | Exact adjacent unresolved pair and escape of the lifted sources from every finite shifted-core family. |
| Closing energy interfaces | Local renewal and PR146 localization/sieve | Exact round-trip weight accounting and the remaining all-source column/propagation obligations. |

### External unit theorem

[Evertse, Theorem 3, printed page 7](https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf)
bounds the nondegenerate solutions of a fixed-coefficient unit equation
with `n` variables by `(2^35 n^2)^(n^3 |S|)`. The theorem allows arbitrary
fixed nonzero rational coefficients; the endpoint cores belong in these
coefficients rather than in a changing prime pool. Over the rationals,
`s` finite primes give `|S|=s+1`, including the real place. The primary
author-hosted theorem and its place convention were inspected by the
arithmetic author, the independent arithmetic reviewer, and the primary
agent. The external theorem itself was not reproved or formalized.

The unit theorem counts solutions. It supplies neither a bound on their
heights in this application nor an effective final time after which all
returns cease. No such consequence is inferred in this packet.

## Latest work incorporated

### PR146: sieve, lifting, and smaller five comparisons

The pass started with head `dd2d5dbd56f9b75ee4dc0bf14f6ab02eefc9b953`
and fetched the later head
`fd991063721e9c157d318e40bb20131762f7d750` before freezing the synthesis.

- [LEAST_FAILURE_SIEVE.md at the final inspected head](https://github.com/GettysburgResearch/collatz/blob/fd991063721e9c157d318e40bb20131762f7d750/research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md)
  gives the logarithmic parity test, the sparse sufficient set, explicit
  smaller-comparison reduction, and the retained rank-five Mersenne
  family. The exponent is about `0.949955527`; the matching counting order
  applies to this particular test, not to every conceivable refinement.
- [FIVE_STEP_SEEDS_AND_MULTIPLIERS.md](https://github.com/GettysburgResearch/collatz/blob/fd991063721e9c157d318e40bb20131762f7d750/research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md)
  is the material update read during this pass. It transports every
  prescribed pair `(q,5q)` into a single progression, gives the smaller
  bounded-height lift into `49 mod64`, and reduces the Mersenne survivor
  to a smaller five comparison beginning with valuation one. The present
  closing notes inspect these interfaces rather than treating the
  localization equivalence as a proof on the sufficient progression.
- [DEEP_REVERSE_BASIN.md](https://github.com/GettysburgResearch/collatz/blob/fd991063721e9c157d318e40bb20131762f7d750/research/upper-bit-mergers/DEEP_REVERSE_BASIN.md)
  supplies the one-sided adjacent criterion and source-qualified
  least-failure machinery used by the later notes. No external Lean
  execution from this PR is claimed as an execution of the present pass.

### PR163: already completed propagation and smooth transitions

Head `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`:

- [FIVE_SLICE_ENERGY.md, FE1 and Section 4](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md)
  already proves the full positive five-to-tripling energy comparison.
  This packet does not claim that propagation result as new. The harmonic
  rigidity consequence explicitly retains PD, the named fixed-target
  positive-lower-density input; the subcritical consequence retains its
  predecessor-moment input. An inequality from five to tripling cannot
  be inverted to bound five energy.
- [REVERSE_CERTIFICATE_KERNEL.md](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/REVERSE_CERTIFICATE_KERNEL.md)
  supplies the ranked reverse kernels inspected by the arithmetic agent.
- The same PR's complete shifted-smooth transition analysis strengthens
  the earlier possible boundary-path description in PR161. This pass
  does not reclaim that classification. Its finite-core results allow
  arbitrary fixed prime pools and endpoint cores, and EF4 uses only the
  earlier elementary cycle exclusion identified below.

### PR166: physical ladder and its old renewal

Head `5996b9f525ca50978bc34f423192c36a87765bf3`:

- [FIVE_CERTIFICATE_LADDER.md, FL1–FL3](https://github.com/GettysburgResearch/collatz/blob/5996b9f525ca50978bc34f423192c36a87765bf3/research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md)
  proves the unbounded initial-two ladder and its complete language of
  successful block concatenations. Its domain has relative density
  `1/24` among odd ternary units.
- [LADDER_RENEWAL.md, R1–R6](https://github.com/GettysburgResearch/collatz/blob/5996b9f525ca50978bc34f423192c36a87765bf3/research/grh-certificate-closure-20261120/LADDER_RENEWAL.md)
  gives the earlier coefficients `16/21` and `81744/82925`, with endpoint
  at most `x/7`. The new proof adds the three disjoint initial-one
  cylinders and correlates their endpoint residues with the full ladder.
  Its smaller constants are not a bound on the uncovered remainder.

No GRH assumption is used by the new arithmetic, transport, or renewal
claims. The GRH interfaces in the source PR are distinct proposed
mechanisms with their own arithmetic-versus-basin limitations.

### PR164: strengthened witness domains

The first inspected head was `85aad425a3bc714e27b1b8cb7e299f85c7025a05`;
the later inspected head is `6fa6b429870a9cd53cde0fc77ad64a3c3956199f`.
The arithmetic agent read the relevant delta, including
[continuation-negative.md](https://github.com/GettysburgResearch/collatz/blob/6fa6b429870a9cd53cde0fc77ad64a3c3956199f/research/witness-closure-512-2026-11-20/continuation-negative.md)
and [continuation-j.md](https://github.com/GettysburgResearch/collatz/blob/6fa6b429870a9cd53cde0fc77ad64a3c3956199f/research/witness-closure-512-2026-11-20/continuation-j.md).
The local boundary note checks the advertised W512-070/072/080–082 domains
against the specific surviving parameter. It does not rule out all
possible compositions of those rules.

## Earlier inputs retained at exact heads

| Source | Used boundary |
| --- | --- |
| [PR161 SS1–SS2](https://github.com/GettysburgResearch/collatz/blob/4a0536b587fc91ee0c7bb1b160c06dda16ddbf23/research/source-rigidity-20261120/SHIFTED_SMOOTH_CYCLES.md) | Elementary exclusion of a nontrivial cycle wholly inside `n+1=2^a3^b`; needed only for EF4's eventually periodic case. |
| [PR157 GCM-002](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md) | Full Collatz is equivalent to forward multiplication-by-five closure on odd ternary units. A fixed label's zero defect and universal basin closure must not be confused. |
| [PR157 GCL-001/002](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/closing-attempts.md) | The rank-one five-companion family remains an exact boundary for declaring the adjacent remainder identically zero. |
| [PR162](https://github.com/GettysburgResearch/collatz/pull/162), `2279da37ac612dbe049777354cdedb3c0aa03282` | Earlier physical two-input block, Hardy-flow and carry/occupation boundaries; source comparison only. |
| [PR165](https://github.com/GettysburgResearch/collatz/pull/165), `78bdb31ccba608de3d089b751a0ab59a52007408` | Certificate-transfer intake and rank-four exceptional family; distinct from universal five closure. |

All latest-source execution claims remain their authors' claims. This
packet's own executed commands and byte comparisons are recorded in its
separate report directory. Review pins do not extend to later source
heads or to neighboring statements that were not reconstructed.
