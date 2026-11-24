# Testing complete-graph descent and fixed-source renewal

**Full Collatz and the unrestricted smaller-source merger remain OPEN.** This pass attempted a total positive ranking function and a fixed-source mass contradiction. Neither target was proved. The finite certificates below do not supply an all-source selector. The strongest positive analytic result obtained here is a bound on the duration and cost of one visit to a threefold size interval; the number of visits remains uncontrolled.

Use the shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

The central ordinary target is unchanged: for every possible least nonconverging source \(m>1\), construct positive \(b<m\) and finite clocks \(i,j\) with \(T^i(m)=T^j(b)\). All literal edges in both directions were allowed in the graph attack. A smaller value than an intermediate inflated state does not meet this target.

## The positive candidate and the missing global estimate

Let \(b(n)\) be bit length. Give every undirected shortcut edge the symmetric cost

\[
c(x,y)=\frac1{\max(b(x),b(y))}.
\]

Along a path starting at \(x\), bit length can increase by at most one per edge. Its first \(r\) edges therefore cost at least \(\sum_{j=1}^r1/(b(x)+j)\). This diverges with \(r\). Consequently finite-radius cost balls are finite, and

\[
V_K(x)=\min_{y\text{ in the component of }x}
\left(K\lfloor\log_2y\rfloor+d_c(x,y)\right)
\]

is a computable proper function, whether or not Collatz holds. It obeys an exact Bellman recurrence. If \(V_K(x)<K\lfloor\log_2x\rfloor\) for every \(x>1\), some actual adjacent vertex has strictly smaller rank and repeated selection must reach 1.

For \(K=3\), the exact finite check covers every \(1\le x\le10^6\), including competitors outside that interval. On these sources \(V_3(x)\) equals the cumulative cost of the actual forward orbit to 1. The largest observed ratio to \(\lfloor\log_2x\rfloor\) is \(237739/102960\), attained at 27. This is finite evidence. It is not a universal bound on runtime, height, or weighted duration.

The proof attempt obtained one usable charge. Fix an integer \(X\ge1\), and set \(h=\lceil\log_2(2X)\rceil\). An injective trajectory segment making \(L\) successive edges while remaining inside \([X,3X)\) satisfies

\[
L\le3h-1.
\]

Inside this interval, staying in the interval forces each state below \(2X\) to be odd and each state above it to be even. The allowed map preserves cyclic order. Extend this finite partial map to a circle homeomorphism. Its two partition boundaries have at most \(2h\) preimages through clock \(h-1\), so at most \(2h\) different length-\(h\) parity words occur. Exact parity coding makes those words injective on the ordinary integers of the interval, since its width is at most \(2^h\). Applying the count to overlapping windows proves the bound. Each such visit has bounded harmonic cost.

**The failed gluing step is explicit.** Projecting different intervals onto one circle does not preserve cyclic order; [rewriting.md](rewriting.md) gives an ordinary trajectory witnessing the reversal. The proof does not bound the number of visits, the number of bands reached, or their accumulated cost in terms of the original source. In particular it does not prove the global prefix estimate

\[
\sum_{i<r}c(T^i x,T^{i+1}x)<3\lfloor\log_2x\rfloor
\]

up to the first visit to 1. A proof of that estimate would exclude an infinite trajectory because its harmonic cost diverges. No such proof resulted.

The same ordered-gap calculation excludes positive cycles contained in \([m,3m)\), except \(1,2\). The resulting parity word is mechanical; Knight's published exclusion of high cycles is relevant prior art. We make no priority claim for this restricted cycle exclusion. Arbitrary cycles need not fit one such interval.

## Why the first global candidates failed

The full-graph finite-residue attempt used ranks \(n^s w(n\bmod M)\), with arbitrary positive weights and arbitrary fixed finite collections of legal path words. [integer.md](integer.md) proves that no such rank covers all sufficiently large positive inputs with a strict improvement. The obstruction tracks the binary input \(-1\) and ternary input 0 simultaneously. Every finite legal component path from this paired input is \(n\mapsto cn+d\) with \(c\ge1,d\ge0\). Arbitrarily large ordinary integers shadow each fixed finite amount of this arithmetic. A lexicographic argument also handles exact additive improvements when homogeneous weights tie.

The paired input is not an ordinary integer. Different precision requests require different positive approximants. This theorem refutes that finite policy architecture, not Collatz. The harmonic edge cost above deliberately depends on actual bit length and avoids the finite-ratio argument.

A separate exact certificate shows that every unrestricted path from

\[
n=9663+7342984060644141028475928576\,t,\qquad t\ge0,
\]

to a smaller positive integer reaches at least \(1024n\). The complete graph is used, with no bound on path length. This excludes a fixed peak ceiling for that family and leaves larger excursions possible. The certificate and the finite-residue theorem serve as failed-attempt records; neither is presented as an exclusion of a fixed ordinary exceptional orbit.

The finite-binary-word ranking search, including positional digit features and small matrix products, is recorded separately in [digit_rank.md](digit_rank.md). Its exact positive cancellation witnesses reject the stated templates. They do not rule out more general functions of the finite input.

## The fixed-source renewal attempt

[basin.md](basin.md) tests the exact ratio-five return dictionary from PR200. Its affine maps on \(\mathbb R\times\mathbb Q_3\) have product Haar Jacobian equal to their sampling probabilities. That identity suggested a finite-volume invariant tile, which would have produced a joint stationary density.

The tile route fails. Conditional on the cited unmarked seed-image volume estimate, the endpoints of **every** binary code with limiting odd frequency in \((0,\log_3 2)\) lie in one Haar-null set. The proof uses a deterministic logarithmic telescope to show positive-frequency returns of the real suffix to a bounded interval. PR200's polynomial reverse-prefix likelihood bound supplies frequency \(1/2\) for its marked law, so that law is also jointly singular. This does not decide absolute continuity of the ternary marginal.

The alternative fixed-source diagonal argument also fails: transporting a real inverse fibre along an escaping ordinary source preserves a positive relative gap from its integer coordinate. The electrical-network and multiscale antichain attempts in the same note retain their exact conductances and the unresolved side-mass estimate. No typical-point statement has been substituted for pressure at the fixed ordinary source.

## Proof and verification boundaries

| Artifact | Mathematical role | Evidence boundary |
|---|---|---|
| [rewriting.md](rewriting.md) | Proper cost rank; one-band residence; ordered gaps; exact peak family | Written proofs, exact finite control; global charge OPEN |
| [rewriting.lean](rewriting.lean) | Finite peak tree, neighbor coverage and arithmetic lift | Kernel-checked declarations listed in the replay receipt; full path induction remains written |
| [integer.md](integer.md) | Mixed arithmetic input; finite-residue impossibility; finite digit transport | Written universal arguments; no fixed ordinary counterexample |
| [integer.lean](integer.lean) | Exact transport, division budget and rational inverse inequalities | Named kernel declarations; CRT and the full Bellman theorem remain written |
| [digit_rank.md](digit_rank.md) | Direct finite-word ranking attempts | Exact integer/polynomial cancellation certificates for the stated templates |
| [basin.md](basin.md) | Return-law singularity and fixed-cohort transport | Written, source-qualified analytic arguments; finite controls check identities only |

The [root review](../../reports/astra-two-centre-20261124/ROOT_REVIEW.md), [source pins](../../reports/astra-two-centre-20261124/SOURCES.json), and [verification record](../../reports/astra-two-centre-20261124/VERIFICATION.md) distinguish fresh execution from imported mathematical inputs. Repository integrity checks are not mathematical proof checks.

## Next unresolved obligation

For the positive rank candidate, the concrete remaining issue is to charge repeated band visits and upward moves to finite information in the original input. For the renewal route, it remains an adequate ordinary-source lower estimate on the disjoint side branches of a fixed positive-density escaping spine. Neither obligation was discharged. The general cycle denominator and every possible escaping source remain in the problem.
