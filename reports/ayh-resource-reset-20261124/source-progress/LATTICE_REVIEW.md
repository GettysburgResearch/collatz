# Independent finite-lattice and source-census review

The reviewed Lean file is `LiftedLattice.lean` (SHA-256
`dfa342146d8afe933e72081d66cff55bae2806da4f6aea6c29cd7d66929cc2c5`).
Its finite graph dependency is `LocalResampling.lean` from PR 197,
`b27a6fe31a487adf5615e173329ad009b975a3cd`, at
`research/ayh-resource-reset-20261124/closing-proposal/LocalResampling.lean`.
The source-specific review began from `GRID_TRANSFER.md` (SHA-256
`39316a367d0a658298e75f68fd3f38444af0f719fe7a97a6771a519a19b08c4b`).
The original-data dependencies are the same head's
`directed-return/SELECTED_TRIT_CELLS.md` and
`closing-proposal/LOCAL_RESAMPLING.md` under that research packet.
The external word-probability comparison is PR 146,
`f431078244e868dc699fad011044f0d5e7f76437`,
`research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md`.

**Finite mathematics verified.** For a common integer lift $2^H K$, the
$i$th native state is $A_iK+B_i$, where
$A_i=2^{H-i}3^{p_i}$ and $B_i=T^i b$. Equal labels $(B_H,p_H)$ give a
direct physical meeting at $H$ on every lift. Consequently each label
class lies within a physical component. On the same index set, physical
deficiency is at most label deficiency. If a clipped window is enlarged
only for the label partition, its deficiency cannot decrease: adding
one index increases its largest class size by at most one. Enlarging
a *physical graph* can create bridging paths, so that alternative
monotonicity cannot be substituted.

At large $K>2^H\max b$, all native intercepts at clocks $i\le H$ are
strictly below $K$, so a meeting has equal slopes and intercepts.
Comparing the powers of two forces equal clocks; the powers of three
give equal odd counts. They keep identical appended trajectories and
grades up to $H$. Generally two unequal integer slopes yield at most
one potential $K$ per index/clock pair. Thus at most $M^2(H+1)^2$
lift values can be exceptional. It is legitimate to overlist zero,
impossible and truncated quotients. Small lifts need not have equality.
The independently implemented finite graph check covered 2,112 configurations,
including duplicate sites, zeros and positive dyadic multiples. Exact
partitions agreed in 1,948 nonlisted cases; in 111 configurations the
label partition was strictly finer than the physical partition.

**Original-source reduction verified under its stated source inputs.**
Fixing the suffix, $7R\le81n+r<8R$ gives $N=R/81$ parents. Every
$m=\lfloor c_0n\rfloor$ lies in an interval of length at most
$c_0N+2$. At fixed $v=n\bmod2^{a_0}$ and $m$, the native cap is
$A_*=O(c_0^{-1}2^{-a_0})$. One residue $b=m\bmod 2^D$ with
$D=\max_t\Delta_t+h$ supplies the low bits for every clock. The same
pair of physical seed parameters generates the slab. The joint event
takes the union of allowable seed choices inside its grid, while allowing
all formal replies, so a selected actual parent is included by its
own seeds and queries. The grid neither assigns its seeds a probability
nor multiplies single-clock probabilities.

Over an interval of length $V$, each grid residue occurs at most
$\lfloor V/2^D\rfloor+1$ times, with the tested residue set rotated if
one counts offsets from the interval's lower endpoint. Multiplying by
$A_*$, summing the $2^{a_0}$ native residues, and dividing by $N$ produces
$O(P_d+2^D/(c_0N))$. For $h=\lfloor d/3\rfloor$ the exponent margin is
$1-3.1(1-\tfrac12\log_2 3)-\tfrac13>0.023$. Polynomial losses are
harmless for the exceptional exact-partition count in this range.
The preceding calculation applies to the disclosed envelope and does
not prove its disagreement, regeneration, or population inputs. Neither
the marginal comparison nor this census proves the needed joint
$P_d=o(d^{-3})$.

The final manuscript was also reviewed at SHA-256
`83225da3c9e92121a7b82099fb3cf958eee32c8ccc070b93a236e75b5381c62b`.
Its new lower marginal holds for each fixed odd stride when averaging
whole aligned windows over all block translations on the complete
native grid. Two independently sampled site offsets give independent
uniform binary parity words for their first $r$ clocks. Their
odd-count difference has second moment $r/2$ and fourth moment
$(3r^2-r)/4$, so its magnitude is at least $\sqrt r/2$ for at least
$1/12$ of ordered offset pairs. Conditional on those offsets, the shared
block index supplies the remaining uniform bits at the lower-grade
endpoint, whose multiplier is odd. PR146's positive-level reflection
bound gives $\gg\sqrt{r/h}$ probability of different labels at the
horizon. Since $1-\sum p_i^2\le2(1-\max p_i)$, the same order is a
lower bound on mean *fractional* deficiency. This uses independent choices
of the two finite offsets. The actual adaptive queries of a parent remain
dependent across clocks.

A fresh isolated build against Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612` checked all eight printed
axiom lists, including `grid_census`, with only standard dependencies.
The compiled dependency's source hash was
`15cc801d0092092b86eaaff4ecdff79d98958c803932eda7023e475028ab2562`.
