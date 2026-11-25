# Independent review of the final cylinder dispatch

| Lean source | SHA-256 |
|---|---|
| MersenneRescueCylinder.lean | `9b7c05e91474e0e705574e8a5bd12df113cf56d5ccb3a219fdb1933b5654a00f` |
| MersenneProgressCases.lean | `a91b286866f347e88292e90ee96efd7ec4c33f502552bc78d64cf2c473131bb2` |
| FinalProgressProposal.lean | `f803ed28152845d620f0114ed870cfd621340871c6f8dcc869b3203fe8e0df57` |

**Verified at these sources.** The cylinder theorem ranges over every
ordinary $t\ge0$ in $m=m_0+2^{284}t$. Splitting $t$ by its residue
modulo 11 covers all eleven rows. Each subsequent step of eleven periods
increments $s$ by $1134\cdot2^{284}$. Independently recomputing the
constants with integer modular exponentiation confirmed
$0\le m_0<2^{284}$, $3^{67+108m_0}\equiv-53\pmod{2^{288}}$, and all
eleven starting residues and period congruences. In Lean the proved
modular exponentiation routine establishes the starting and period
congruences; induction supplies each actual exponent. The binary-cylinder
identification via the exact multiplicative order is a separate written
argument. The all-$t$ progression and its ordinary meetings are formal.

Here $j\ge97$, so $j-1$ has its ordinary integer value. Every starting
$s$ is at least 59, whereas the subtracted exponent is at most 15;
the target $a=s-\mathrm{drop}+\mathrm{rise}$ is positive and below
$j$. The coefficient equalities thus use ordinary powers. The reflected
offset subtractions in the affine mergers are protected by the checked
bounds on both starting affine constants in `MersenneRescueWords.lean`.
Both ordinary witness clocks are at most 285 **after the checkpoint**.

In `cylinder_closure`, the parent equation identifies the supplied $z$
with the prior rank-three witness by uniqueness. The previously proved
`bounded_return` and below-parent minimality discharge the quantitative
and leastness inputs of `exact_first_bad`. The resulting earlier good
Mersenne exponent and the kernel-checked ordinary meeting contradict the
bad checkpoint. The last corollary obtains below-parent minimality from
global minimality of the supplied reverse defect.

The final consumer picks the least reverse defect from an assumed failure,
takes an actual upper hit there, and excludes the two-odd layer, tail case,
one-sixteenth case, and explicit cylinder case. It invokes its **open**
`ResidualExclusion` argument on the remaining tuple. The reverse direction
of the stated equivalence uses universal convergence to contradict any
reverse defect. The declaration supplies an equivalence and leaves the
residual implication open.

I independently rebuilt the three frozen modules and their
`SourceProgressCases.lean` consumer dependency with Lean 4.34.1, pinned
Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, and warnings as
errors. The eight audit entries in the three modules passed with
`propext` and `Quot.sound`, and `Classical.choice` where used.
