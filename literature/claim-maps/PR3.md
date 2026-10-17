# Draft PR #3 claim-to-literature map

**Snapshot:** head `d162cd9dd54fe74f86d572612e3f80c2dd8fb59a`
**Namespace:** `PR3/...`

| Claim | Verdict | Located support | Audit note |
|---|---|---|---|
| `PR3/L-0001` parity-affine formula | **KNOWN — EXACT** | Terras 1976, Thm. 1.1; Everett 1976, Thm. 1 | Cite `LIT-KTHM-0001`; the full induction is included locally. |
| `PR3/T-0001` consecutive collision bundles induce radix maps | **PARTIAL OVERLAP** | Terras/Everett affine cylinders | Classical sources give the affine branches. The collision-to-digit-preserving conjugacy is a native algebraic packaging. |
| `PR3/T-0002` arbitrary sparse collision-fiber conjugacy | **POSSIBLY NOVEL FORMULATION** | Terras/Everett substrate; Bernstein–Lagarias 2-adic context | No exact antecedent located. The lifting congruence and positive-integer criterion are internal. |
| `PR3/L-0003` exact fiber recursion and level sets | **POSSIBLY NOVEL FORMULATION** | finite parity-coordinate theory | No exact source located for this binary dynamic-programming formulation or its `O(2^L)` accounting. |
| `PR3/L-0004` universal carry pumping | **POSSIBLY NOVEL FORMULATION** | no exact source | Mixed-radix carry identities are elementary once stated, but this universal theorem was not located. |
| `PR3/T-0003` dual 2-adic/real coding and aperiodicity | **PARTIAL OVERLAP** | Terras/Everett; Bernstein–Lagarias 1996 | 2-adic itinerary coding is classical. The exact real-tail formula, growth slope, and contradiction for eventually periodic induced digits appear native. |
| `PR3/T-0004` run-length skeleton | **POSSIBLY NOVEL FORMULATION** | SML and S-unit theory only thematically nearby | The identity is elementary and self-contained. Calling it an “S-unit carry chain” does not import the classical S-unit theorem. |
| `PR3/L-0005` inverse signatures | **PARTIAL OVERLAP** | Terras affine constants and parity-residue bijection | Inverting one affine parity cylinder is classical. The signature quotient modulo `3^a` and its use as a collision invariant were not located verbatim. |
| `PR3/L-0006` collision-code composition | **KNOWN — COROLLARY / POSSIBLY NOVEL FORMULATION** | affine-word composition is standard | `B(uv)=3^{|v|_1}B(u)+2^{|u|}B(v)` is an immediate composition identity. The finite precision-surplus calculus is native unless matched later. |
| `PR3/T-0005` exponentially unbounded supercritical fibers | **POSSIBLY NOVEL FORMULATION** | Terras/Everett; contrast Applegate–Lagarias and Krasikov–Lagarias | The proof is finite pigeonhole + CRT on parity signatures. Backward-tree density results do not imply it. No exact source located. |
| `PR3/O-0001`–`O-0005` explicit charts | **INTERNAL EXACT COMPUTATION** | none exact | Literature audit cannot certify scripts; no external chart antecedent located. Preserve certificates and exact arithmetic. |
| `PR3/X-0001`–`X-0003` enumerations | **INTERNAL EXACT COMPUTATION** | tree literature is contextual | Applegate–Lagarias count backward trees, not these complete forward collision fibers. |

## Strongest reusable literature connections

### Parity cylinders

Every proof that starts by fixing a finite parity word should cite Terras/Everett once and then use `LIT-KTHM-0001`. The native novelty question begins only after the affine cylinder is converted into a common-output fiber, induced alphabet, or structured code.

### Preimage trees are not collision fibers

The Applegate–Lagarias and Krasikov–Lagarias papers may inspire second-moment or branching estimates, but their vertices are backward preimages. A forward collision fiber groups distinct residues by equal `(odd count, endpoint)` after a fixed number of steps. A mapping between the two objects would itself require a theorem.

### `T-0005` and the issue-#4 width program

`PR3/T-0005` proves exponential growth for a constructed family after adding an odd tail and allowing the depth to change with the code. The issue-#4 direct-width data study maximal complete fibers at individual depths. The two claims may measure different geometries. Before declaring the empirical width conjecture resolved or contradicted, align:

- whether translated offsets or absolute residues are counted;
- whether appended common tails are included in the depth;
- fixed odd weight versus all supercritical weights;
- complete level sets versus selected subfibers;
- diameter and residue-projection constraints.

## Literature-safe novelty language

Recommended sentence for the PR:

> Terras and Everett supply the classical parity-cylinder coordinates used in the proof. We did not locate an external theorem giving the sparse collision-fiber conjugacy, inverse-signature code, or exponential odd-tail amplification in this form. These are therefore treated as repository-specific formulations pending a broader provenance audit, not asserted to be novel.
