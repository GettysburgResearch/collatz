# Internal claim crosswalk

This file records overlap without merging IDs or deciding priority.

| PR #3 namespace | Issue-#4 namespace | Relationship | Literature substrate |
|---|---|---|---|
| `PR3/L-0001` | `CLAUDE/D-0001`, `CLAUDE/L-0001`, `CLAUDE/L-0004` | Same finite parity-affine coordinate system; issue-#4 adds bounds and valuation language. | Terras 1.1–1.2; Everett Theorem 1. |
| `PR3/T-0001` | `CLAUDE/T-0015` | Both derive the `64→81` induced map; PR3 states a general consecutive-bundle theorem. | Classical affine cylinders only; induced-map packaging is internal. |
| `PR3/T-0002` | `CLAUDE/D-0002`, `CLAUDE/T-0015` | PR3 gives the arbitrary sparse-fiber conjugacy under which issue-#4 charts are instances. | No exact external antecedent located. |
| `PR3/L-0002` | `CLAUDE/L-0010`, `CLAUDE/L-0014` | Same nine-cycle/stack-amplifier territory, independently derived. | No exact external antecedent located. |
| `PR3/L-0003`, `PR3/X-0002` | `CLAUDE/O-0010`, `CLAUDE/C-0003` | Exact coalescence recursion and independently reproduced width table. | Tree literature is related but counts a different object. |
| `PR3/L-0004` | `CLAUDE/L-0010`, later ladder work | PR3 proves general carry pumping; issue-#4 uses chart-specific cycles and stacks. | No exact external antecedent located. |
| `PR3/T-0003` | `CLAUDE/T-0002`, `CLAUDE/T-0018` | Dual 2-adic/real coding constrains the issue-#4 survivor set and periodic codes. | Bernstein–Lagarias gives standard-map 2-adic conjugacy; exact induced theorem is internal. |
| `PR3/T-0004` | `CLAUDE/L-0015`, `CLAUDE/T-0020` | PR3 supplies the run-length normal form; issue-#4 studies periodic and exp-polynomial schema obstructions. | SML/Fatou theory is a dependency only after local reductions. |
| `PR3/O-0001` | `CLAUDE/T-0015`, `CLAUDE/T-0016` | Same explicit chart; independent calculations may support verification after review. | No external exact chart located. |
| `PR3/O-0002`, `PR3/O-0003`, `PR3/O-0004` | ladder charts in issue #4 | PR3 supplied new wider alphabets later adopted and independently checked by issue #4. | No external exact charts located. |
| `PR3/T-0005` | `CLAUDE/C-0003`, `CLAUDE/T-0014` | PR3 now proves exponential unboundedness of finite supercritical fibers; issue-#4's empirical single-fiber width exponent concerns the *maximal direct fibers at a fixed depth* and can coexist with the signature-tail family at different geometry/length. Integrator should align definitions before treating one as resolving the other. | Pigeonhole/CRT over classical parity coordinates; backward-tree literature is not the same theorem. |

## Termination-frontier packet

Draft PR #6 occupies a separate namespace. Its external root, the Yolcu–Aaronson–Heule rewrite equivalence, is verified. The packet's `L-9001`, `R-9001`, `Q-9001`, and `Q-9002` remain native results/open interfaces; they should be cross-linked to the literature suite but not renumbered into either active ledger until integration.

## Integration warning

The claim text on both branches is changing rapidly. Before assigning canonical IDs, an integrator should compare statement hashes or exact file contents, not only titles. “Independently re-derived” is evidence for verification after adversarial reconstruction; it is not evidence of external novelty.
