# Literature map — draft PR #3

**Namespace:** `PR3/...`  
**Live ledger inspected:** 2026-07-21

| Qualified claim | Verdict | Located connection and scope |
|---|---|---|
| `PR3/D-0001` shortcut/parity conventions | `FOLKLORE / STANDARD` | Matches the shortcut map used by Everett, Terras, Bernstein–Lagarias, Tao, and much of the modern literature. [@Everett1976; @Terras1976; @BernsteinLagarias1996; @Tao2022] |
| `PR3/L-0001` parity-affine formula | `KNOWN — EXACT` | KTHM-0001 gives the same cylinder formula with complete proof. |
| `PR3/T-0001` consecutive collision bundles induce radix maps | `PARTIAL OVERLAP` | Classical affine cylinders imply the starting identities, but no exact named antecedent for the conjugacy package was located. |
| `PR3/O-0001` two-branch `64→81` chart | `POSSIBLY NOVEL FORMULATION` | Exact finite identity internal to repo; overlaps `CLAUDE/T-0015`. No external occurrence located. |
| `PR3/O-0002` three-branch `512→729` chart | `POSSIBLY NOVEL FORMULATION` | Exact finite chart; no located antecedent. |
| `PR3/O-0003` six-branch depth-17 chart | `POSSIBLY NOVEL FORMULATION` | Exact finite chart; no located antecedent. |
| `PR3/L-0002` nine-column carry amplifier | `POSSIBLY NOVEL FORMULATION` | Strong internal overlap with `CLAUDE/L-0010` and `CLAUDE/L-0014`; distinct from AYH rewriting. |
| `PR3/X-0001` consecutive-fiber census | `INTERNAL COMPUTATION` | Applegate–Lagarias/Krasikov–Lagarias count backward preimages, not same-depth equal-output affine fibers. [@ApplegateLagarias1995a; @ApplegateLagarias1995b; @KrasikovLagarias2003] |
| `PR3/T-0002` arbitrary sparse collision-fiber conjugacy | `POSSIBLY NOVEL FORMULATION` | Uses classical parity cylinders, but exact `H_D` lift not found in literature. |
| `PR3/L-0003` exact binary recursion for fibers | `POSSIBLY NOVEL FORMULATION` | Parity recursion is standard; complete level-set recursion and `O(2^L)` packaging not located. |
| `PR3/L-0004` universal carry pumping | `POSSIBLY NOVEL FORMULATION` | No exact mixed-radix pumping antecedent located. |
| `PR3/T-0003` dual adic/real coding and aperiodicity | `PARTIAL OVERLAP` | Bernstein–Lagarias supplies classical `2`-adic Collatz conjugacy; the repository's simultaneous real-tail law and integer aperiodicity argument appear internal. [@BernsteinLagarias1996] |
| `PR3/T-0004` run-length skeleton / `S`-unit carry chain | `POSSIBLY NOVEL FORMULATION` | The displayed equations have `S`-unit flavor, but no classical `S`-unit theorem applies merely from the name. |
| `PR3/O-0004` eighteen-branch depth-22 chart | `POSSIBLY NOVEL FORMULATION` | Exact finite identity, internally reproduced; no external occurrence located. |
| `PR3/X-0002` complete-fiber census through depth 22 | `INTERNAL COMPUTATION` | Literature tree bounds are related only at a broad counting level. |
| `PR3/L-0005` parity signatures and inverse reconstruction | `KNOWN COMPONENTS / POSSIBLY NOVEL PACKAGING` | Exact parity-word inversion is classical (KTHM-0002); the signature chosen to characterize equal affine outputs is repo-specific. |
| `PR3/L-0006` 3-adic collision-code composition | `POSSIBLY NOVEL FORMULATION` | LTE/order tools are standard; the precision-surplus composition theorem was not located externally. |
| `PR3/T-0005` exponentially large mildly supercritical fibers | `POSSIBLY NOVEL FORMULATION` | Pigeonhole, parity inversion, and CRT are classical; no exact theorem combining them into exponential equal-output fibers was located. It is not implied by tree-density bounds. |
| `PR3/O-0005` 339-branch depth-44 chart | `INTERNAL EXACT OBSERVATION` | Independently reproduced on the CLAUDE branch; no external source located. |
| `PR3/X-0003` signature-tail experiments | `INTERNAL COMPUTATION` | No external theorem status. |
| `PR3/L-0007` inverse-root offset tensor law | `POSSIBLY NOVEL FORMULATION` | Algebraic composition identity; no exact antecedent located. |
| `PR3/L-0008` arbitrary-precision two-word atomic codes | `POSSIBLY NOVEL FORMULATION` | Classical modular arithmetic ingredients; exact code theorem not located. |
| `PR3/T-0006` geometry-preserving code amplification | `POSSIBLY NOVEL FORMULATION` | Appears repository-specific; requires internal adversarial verification. |
| `PR3/X-0004` tensor/geometry checks | `INTERNAL COMPUTATION` | No external theorem status. |
| `PR3/Q-0001` finite-boundary regeneration | `OPEN — NO LOCATED THEOREM` | AYH gives an equivalent termination frontier in another representation, not a regeneration theorem for these maps. [@YolcuAaronsonHeule2023] |
| `PR3/Q-0002` analytic fiber growth | `PROPOSED INTERNAL RESOLUTION` | `PR3/T-0005` addresses unbounded/exponential cardinality; literature tree density does not independently verify it. |
| `PR3/Q-0003` width-three carry grammar | `OPEN — NO LOCATED THEOREM` | No external closure grammar located. |
| `PR3/Q-0004` multi-chart transition groupoid | `OPEN — NO LOCATED THEOREM` | Measure rigidity and generalized rewriting are only analogies. |
| `PR3/Q-0005` finite versus adic closure | `OPEN — CLASSICAL WARNING` | Bernstein–Lagarias confirms the naturality of `2`-adic encodings; it does not turn an adic point into an ordinary integer. [@BernsteinLagarias1996] |
| `PR3/Q-0006` independent verification | `PROCESS CLAIM` | Requires repository review, not literature matching. |
| `PR3/Q-0007` vertical macro-tile closure | `OPEN — NO LOCATED THEOREM` | AYH termination technology may provide proof methods, not an existing solution. |
| `PR3/Q-0008` parameterized `S`-unit schemas | `OPEN — LITERATURE INTERFACE` | Future pass should compare exact equations to Evertse–Schlickewei–Schmidt style `S`-unit results; no application is asserted here. |
| `PR3/Q-0009` structured code geometry | `OPEN — NO LOCATED THEOREM` | Preimage trees count different objects. |
| `PR3/Q-0010` growing geometry under tensor amplification | `OPEN — NO LOCATED THEOREM` | Internal algebraic/combinatorial target. |

## Most useful imported dependencies

- `KTHM-0001`–`KTHM-0003`: parity cylinders, parity/residue bijection, and exact tracking.
- `KTHM-0004`: order formulas for `2`- and `3`-adic precision calculations.
- `KTHM-0013`: tree-density theorems, primarily as a warning not to identify preimage growth with collision-fiber growth.
