# A sparse dyadic section for ordinary Collatz components

Every positive target coprime to three has arbitrarily large marked predecessors with a prefix of at least one fifth of their binary bit length in shortcut clocks. The prefix consists of one odd step followed by halvings and ends at $u\le4x^{4/5}$ for starting value $x$. Convergence on this sparse set is equivalent to universal convergence. The endpoint used in the construction remains above the original target. The proof and the first unsupported step of the global descent argument are in [MarkedPredecessors.md](MarkedPredecessors.md).

The second checkpoint proves the sharper closed equivalence with marked odd sources whose exact excess $5v_2(3n+1)-(\lfloor\log_2n\rfloor+1)$ belongs to $\{0,\ldots,7\}$. An explicit smaller marked quarter partner removes each excess of eight until this boundary or the base one is reached. [Critical-section proof](CRITICAL_SECTION.md) · [Lean](CriticalSection.lean).

| Lean declaration in `CollatzShell.MarkedCylinders` | Formal statement |
|---|---|
| `cofinal_marked_power_predecessors` | For every fixed ternary-unit target and every lower bound, an ordinary marked predecessor exceeds that bound and has an explicit prefix ending at $u$ with $u^5\le4^5x^4$. That endpoint hits the supplied target. |
| `universal_iff_marked_power` | Universal convergence is equivalent to convergence of all marked $x$ admitting $3x+1=2^e u$ with $5e\ge\lfloor\log_2x\rfloor+1$. |
| `critical_quarter_descent` | A marked source above the exact eight-value boundary has an ordinary smaller marked partner, the same odd cofactor, exact excess reduction eight, and a physical common endpoint. |
| `universal_iff_critical_mark` | Universal convergence is equivalent to convergence of marked $n$ with odd cofactor in $3n+1=2^e u$ and both inequalities $\lfloor\log_2n\rfloor+1\le5e\le\lfloor\log_2n\rfloor+8$. |
| `section_of_inverse_row` | A finite row of ordinary integers satisfying the phase and size bounds hits the marked band. |
| `odd_predecessor`, `cylinder_predecessor` | Exact ordinary attachments for the long halving prefix and for a fixed guarded binary residue. |
| `inverse_power_cost`, `inv4_not_dvd_sixteen` | Power-cost obstruction for inverse constructions that keep their endpoint above the original target, and an upper bound on extra halvings. |

The octave count, the general fixed-suffix construction and the asymptotic sharpness example are written proofs. The exact finite replay runs independently of Lean and uses integer arithmetic. Its 24 rows cover eight targets at denominators 53, 306 and 665, amounting to 8,216 row entries. It checks all 728 marked entries through their original target.

## Replay

Use Lean `v4.34.1` and mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. From the built mathlib checkout, run `lake env bash /path/to/positive-section/check_lean.sh`. The script compiles three pinned inputs followed by the three research modules into a fresh temporary module directory, with one worker, warnings as errors and `autoImplicit=false`. The global statements print exactly `propext`, `Classical.choice` and `Quot.sound`. To replay the finite rows, run `python -B /path/to/positive-section/replay_marked.py`. The critical-section census is `python -B /path/to/positive-section/check_critical_section.py`; it also supports `-O`.

| Vendored source | Exact upstream identity | SHA-256 |
|---|---|---|
| `ShellCover.lean` | [PR 173, source](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/ShellCover.lean) | `76477e195c733e8b8c9fdf523d954d85375b3ac244ee0590127192743bffc88c` |
| `ForwardSection.lean` | [PR 173, source](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/ForwardSection.lean) | `f134020b95f79c3b90cfe104c7d4234ee8d162c97acaa02c6aefc6ec86d19ae4` |
| `OffsetDescent.lean` | [PR 182, source](https://github.com/GettysburgResearch/collatz/blob/cbec52dde5bed390a693310dd04e911033ba0cc9/research/lean-dyadic-descent-20261121/OffsetDescent.lean) | `e0af0b1cbe4c4d90b34272bbbc45f25f6a084072dd17c2eb24be9e31641fde8b` |
