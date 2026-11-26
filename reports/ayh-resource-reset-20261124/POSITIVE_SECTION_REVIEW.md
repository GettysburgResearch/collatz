# Independent review of the marked power-predecessor theorem

**Verdict.** Verified at statement and mathematical proof level for the
ordinary shortcut map. The existence theorem preserves an arbitrary fixed
positive ternary-unit target and proves a power-sized drop relative to
the newly constructed predecessor. The unconditional equivalence reduces
universal convergence to convergence on the marked power section. Its
right-hand side remains open.

| Reviewed path, relative to the positive-section packet | SHA-256 |
|---|---|
| `MarkedPredecessors.md` | `e9e0454120f3474d5b14bb04f092b0192270c785fedd8bb06a87abe02ce648e5` |
| `InversePowerRows.lean` | `61b8e48f32538ed4f498ecebd6e6054b70b70c33e10c41d58a604ac13227cc87` |
| `MarkedCylinders.lean` | `3da95faaaa6ea34cac8d2b2a1d9f0bdab9a5ca7586f407ab263b7131fd8fafb8` |
| `vendor/ForwardSection.lean` | `f134020b95f79c3b90cfe104c7d4234ee8d162c97acaa02c6aefc6ec86d19ae4` |
| `vendor/OffsetDescent.lean` | `e0af0b1cbe4c4d90b34272bbbc45f25f6a084072dd17c2eb24be9e31641fde8b` |
| `vendor/ShellCover.lean` | `76477e195c733e8b8c9fdf523d954d85375b3ac244ee0590127192743bffc88c` |

The review inspected the two main declarations, the fixed-suffix argument,
and the imported definitions and interfaces they use. It does not extend
to other proposals in the source PRs. The review did not rerun the
separately reported compilation.

**Quantifiers and physical clocks.** For every ordinary natural number
q with nonzero residue modulo 3 and every lower cutoff L, the conclusion
gives one positive odd x>L, an exponent e, and an ordinary u. Nonzero
residue excludes q=0. The construction chooses
\(u=L^s(2^Qq)\) and \(3x+1=2^eu\). Hence the first shortcut is odd and
the next \(e-1\) are halvings. They end at u, after which precisely
\(4s\) clocks reach \(2^Qq\), and Q more reach q. Thus the source and
the hit are linked by one finite trajectory. The output u can be even,
so its correct description is *endpoint of the forced prefix*.
An unqualified “first odd endpoint” or “first return” would add a claim
that the main declaration does not prove.

**Mark and exponent.** Write \(d=\lfloor\log_2 x\rfloor\).
The actual predicate is oddness and
\((d+1)(x-2^d)\le70\,2^d\). The one-sided grid has an error of at
most \(1/Q\) when replacing the rational rotation by the irrational one.
The shift by \(2/Q\) places the model phase between \(2/Q\) and \(5/Q\)
above a single integer, with the variation of \(e_s\) absorbed into an
integer. The row contributes at most \(1/Q\) more error. Therefore the
true log lies between 0 and \(6/Q\) above that same integer. Since
\(d+1\le5Q\), the phase test sees at most 30, within its allowance of
35. The inequalities \(e\ge Q\) and \(x<2^{5e}\) give
\(x\,u^5\le(2^e u)^5=(3x+1)^5\le4^5x^5\). Cancellation is valid
because x is positive. The resulting bound \(u\le4x^{4/5}\) is
consistent with \(u\ge 2^Qq\) on the constructed rows. In particular
it supplies no smaller representative relative to the fixed target q.

**Closed equivalence.** Since \(3x+1\) is positive,
\(\exists e,u:\ d+1\le5e,\ 3x+1=2^eu\) is precisely
\(d+1\le5v_2(3x+1)\). For each positive ternary unit q,
`cofinal_marked_power_predecessors` supplies x in the stated set.
Convergence at that x implies convergence at the physically hit q,
by `basin_at_hit`. Every positive multiple of three can be halved to an
odd multiple of three and its next shortcut is a ternary unit. The other
direction is the restriction of universal positive convergence. There is
no extra hypothesis asserting convergence of any unit or selected row
inside the equivalence theorem.

**Written extensions.** The octave count follows by counting one
residue class modulo \(2^{\lceil(d+1)/5\rceil}\) in the marked
interval. For a fixed odd residue r and fixed width k, the affine formula
for the first k clocks and the order of 2 modulo \(3^a\) in the prose
give the required bounded extra clock \(j_s\). All added phase errors tend
to zero uniformly with Q for this fixed cylinder. The full cofinal
marked-cylinders conclusion is a written argument. The Lean
`cylinder_predecessor` only glues the cylinder under its explicit
congruence and size assumptions. The manuscript correctly separates
arbitrary prescribed odd residues from the growing power condition.
In fact, for fixed k and sufficiently large x in the power section,
\(2^k\mid3x+1\), so only the one residue \(x\equiv-3^{-1}\pmod{2^k}\)
is compatible with both requirements cofinally.
