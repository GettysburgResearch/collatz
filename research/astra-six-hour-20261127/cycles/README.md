# The bounded least-disagreement cycle

**The bounded branch remains open.** Its hypothetical positive cycle has physical odd values $s\le x\le(16s+7)/3$, native odd gaps in $\{1,2\}$, and lower and upper neighbors in the actual basin of one. This packet isolates what those genuine good labels force.

| Result | Scope |
| --- | --- |
| [Four fifteen-odd exclusions](FIFTEEN_ODDS.md) | No $x-1,x+1,2x-1$ or $3x$ at a bad phase can hit one with at most fifteen odd departures. Exhaustion of 128,545,757 nodes and every candidate hit was independently replayed. |
| [Finite upper languages](UPPER_LANGUAGES.md) | For any fixed odd budget, or any fixed zero-entropy finite-state upper language, all eligible phases lie in a computable bounded range. The theorem extends to all cycles of any prescribed finite eccentricity. |
| [Explicit clock growth](UPPER_CLOCK_GROWTH.md) | At each applicable phase, a hitting upper mark needs at least $\log_2^*s-O(1)$ odd departures, with no condition on the lengths of its halving runs. |
| [Phase population](PHASE_POPULATION.md) | All but $o(p)$ genuine phases have at least $(\log_2s)/20-O(1)$ upper odds at all four marks before the first $\log_2s$ clocks, using the stated logarithm theorem. A positive fraction of the phases are on-cycle canonical starts with good tripled mark. |
| [Simultaneous ordinary controls](WINDOW_CONTROLS.md) | Every prescribed finite two-sided native cylinder has unbounded ordinary all-good controls. Explicit windows realize the strict central minimum and each exact $r=2,3,4,5$ while all named marks converge. A simpler unbounded family has four grades $3,3,3,2$. |

[CriticalStrip.lean](CriticalStrip.lean) verifies the signed rational critical-strip obstruction with its actual odd-edge and coefficient hypotheses. [FourMarks.lean](FourMarks.lean) verifies the explicit unbounded four-mark control. The arbitrary-gap extension, tree compactness, asymptotic bounds, general steering consequence and population argument have written proofs. The fifteen-odd computation has two independent arithmetic implementations. [Rational-strip kernel output](../../../reports/astra-six-hour-20261127/cycles/CriticalStrip.lean.log) · [Four-mark kernel output](../../../reports/astra-six-hour-20261127/cycles/FourMarks.lean.log)

No published input used here supplies an upper bound on the good marks' odd counts. The finite-language bounds depend on the language, the population statement allows exceptional specified phases, and the convergent controls do not repeat their marked window as a bad cycle. Full ordinary exclusion at unbounded upper complexity and the independent first-crossing alternative remain open.
