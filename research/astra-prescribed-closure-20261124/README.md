# Prescribed pairs and repeated descent of actual components

**PROPOSED / SOURCE-QUALIFIED research checkpoint, 24 November 2026.** This packet continues the full convergence attempt from [the previous checkpoint](../astra-deep-closure-20261124/README.md), incorporating the newer heads of PRs 192, 195 and 197. The final intake also read the new PR201 finite-row criterion; its connection to the tilted moment is recorded in [the late-source note](orbit/LATE_PR201.md). It supplies actual paired ordinary ancestors, a growing chain of smaller component representatives, and an exact count for short prescribed returns. Universal positive Collatz convergence remains open in this packet.

The shortcut is $T(2n)=n$, $T(2n+1)=3n+2$. Write $a\sim b$ when their positive ordinary paths meet, allowing different clocks. All labels below refer to these actual components. A supplied target stays fixed in the statements that quantify over its ancestors.

## The new results

### Repeated descent while retaining both ordered components

Fix $s,r\ge0$. On the row $2^d\le n<2^{d+1}$, even after prescribing any $L\le d^{3/5}$ low binary digits, all but a relative fraction $e^{-d^{1/100}}$ have a positive odd ternary unit $u$ satisfying

$$
 n\sim u,\qquad 3^s n+r\sim3u,\qquad u\le2^{d^{99/100}}.
$$

The certificate has a growing number of genuine physical transfers, of order $\log d$. Each shrinks the current dyadic height exponent by a factor between .80 and .85. The construction handles both possible orders of the two physical odd counts. Its next comparison reads fresh bits of the original source, and its iteration counts the children in the exact residue forced by the previous transfer. This applies to the actual $n,81n+r$ heads, including the remaining suffix 57. The same source can support every prescribed word of ternary residues of a growing modulus, using a different physical chain for each word. [Full proof](head/README.md) · [Prescribed residues](head/PRESCRIBED_RESIDUES.md)

This probability theorem uses the frozen PR146 complete-grid symbolic absorption estimate. With the separate fixed-target predecessor-density premise M, it also reduces universal convergence to a directed pointwise implication on two explicit sparse dyadic progressions near any chosen ternary unit. The pointwise implication has not been proved. The exceptional count is an ambient source count, and it can contain all representatives of a particular exceptional pair.

### Both endpoints prescribed, with one pattern valid for every target

For every sufficiently large $N$, there is a pattern $P_N\subset[0,N-1]\cap\mathbb Z$ with $|P_N|\ge cN/\log N$ such that, for **every supplied positive odd unit $q$**, arbitrarily large translates of that same pattern consist of actual paired ancestors of $(q,5q)$. Every source in a translate has the same physical landing clock on both arms and equal odd counts. The pattern is chosen before $q$.

The proof controls the real affine offset at the actual heavy-tailed renewal epochs, extracts a central clock/grade row, and attaches one ordinary suffix to the whole selected pattern. It assumes PR146's stated iid ratio-five renewal law. Kelley–Meka's theorem then gives many disjoint three-term arithmetic progressions in the common pattern, with differences divisible by a supplied $m\le N^{1-\epsilon}$. The suffix fixes both targets, but its length and the interval's absolute position can be very large. [Proof and exact example](paired/README.md)

### A count for adaptive returns to two prescribed pair relations

Consider $(x,9x+2)$ and $(x,3x)$. Allow arbitrary switching between these relations and independently chosen forward clocks of length at most $H$ on each arm. At a sufficiently large ordinary source, any such short exact return forces the two clocks to agree and is an affine identity on the current cylinder. Each observed return exposes a fixed positive chance of a literal merger in the next six source bits.

Consequently chains reaching a discordant pair below $2^{(1-\delta)d}$, from the row of exponent $d$, occupy $o(e^{-d^{.01}})$ of the original sources if every link has $H=o(d^{.99})$. The statement includes a frozen prefix of $d^{3/5}$ bits and a union over terminal targets. Thus an inverse construction confined to short returns on these two relations cannot supply enough discordant ancestors to overcome the preceding descent theorem's exceptional count. Long excursions and more general common-future comparisons remain outside this bound. [Exact statement and proof](orbit/README.md)

## The direct closing attempts

The pointwise sparse reduction permits a chosen ternary unit, so we tested whether a contracting inverse at the neighborhood of $-1$ could remove the binary information retained between descent stages. It gives a genuine size decrease, but an exact paired identity shows that the two new paths replay the old states after a delay. In the other dyadic progression the new pair does merge, but it retains only one of the two supplied labels. These are ordinary identities, not a random-path objection. [Ternary transfer calculation](head/TERNARY_TRANSFER.md) · [Self-returns in the original cylinders](head/FROZEN_CYLINDERS.md)

There are two further distinctions needed to join the main results. The ratio-five pattern measures interval length, whereas the ordered descent bounds absolute height. Also, separate physical affine words change a slope ratio only by powers of two and three; they do not turn the factor five into a power of three. A general bounded-offset row bound in the paired note quantifies why the current first-target fibers are too small to beat an ambient exceptional count at a growing prescribed target.

The useful unresolved statements are therefore specific: control the descent exceptions **inside an actual prescribed component fiber**, supply a common-future comparison covering its long excursions, or prove the directed implication on the stated sparse inputs. None is supplied by a finite-prefix identity or by the written counts above.

## Evidence and dependencies

The three Std-only Lean modules prove the physical lifts, the full common pattern translation and router, the exact inverse fibers, the merger cylinders, and the finite affine rigidity statements. The new infinite probability and counting proofs are written mathematics, with their source hypotheses stated beside them. No Lean theorem in this packet asserts universal convergence or formalizes the imported analytic estimates.

[Frozen source ledger](SOURCES.json) · [Independent review and scope](../../reports/astra-prescribed-closure-20261124/ROOT_REVIEW.md) · [Complete new-module axiom audit](../../reports/astra-prescribed-closure-20261124/kernel/CHECKS.json) · [Paired agent's independent reconstruction of the descent proof](paired/REVIEW_HEAD.md)
