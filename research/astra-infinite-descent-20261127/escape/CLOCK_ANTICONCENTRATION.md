# A uniform atom bound for first-hit clocks and grades

Let \(T\) be the positive shortcut map, \(q_j(z)\) its number of odd departures through clock \(j\), and \(\tau_S(z)=\inf\{j\ge0:T^jz\in S\}\). Write \(g_S(z)=q_{\tau_S(z)}(z)\) on the finite-hit event. The target \(S\) may be any nonempty finite set of positive integers, chosen separately on every octave. There is no restriction on its location. Write \(B=|S|\).

**Unconditional written upper bound.** At every integer octave \([N,2N)\), uniformly over finite hit clocks \(m\), grades \(d\), and sets \(S\),
\[
 \frac1N\#\{N\le z<2N:\tau_S(z)=m\},\quad
 \frac1N\#\{N\le z<2N:\tau_S(z)<\infty,\ g_S(z)=d\}
 \ \ll\frac1{\sqrt{\log(2+N/B)}} .                                      \tag{1}
\]
Each statistic erases the other coordinate. The proof uses the square-root binary-cylinder survival upper bound for the single counted adjacent pair. A [self-contained derivation](SCALAR_RETURN_PROOF.md) rederives this prior estimate from elementary finite-walk and moment arguments and the kernel-checked existence of counted integer merger cylinders. No fixed-target predecessor-density, stopping-time limit, trace floor or singular-support input enters (1). The finite bound below needs no infinite-time synchronization theorem. The qualitative vanishing for \(N/B\to\infty\) needs only qualitative absorption of the adjacent counted pair. Said Duran's paper and accompanying formalization and Leen's quantitative paper are external works. This packet does not rebuild those developments. [Said Duran, qualitative counted fusion](https://doi.org/10.5281/zenodo.23003524) · [Leen, fixed-state quantitative fusion](https://doi.org/10.5281/zenodo.23268751) · [Weaver 124/v1, equations (3)–(7), finite-cylinder realization](https://rstation.ai/problems/collatz/papers/124/v1).

## A finite comparator and an exact flux bound

Take \(N\) even; odd \(N\ge3\) can be covered by neighboring even octaves, or the cell at their middle boundary can be split into two. Give the real octave \([N,2N)\) the measure \(dt/t\), of mass \(\log2\). The bijection
\[
  f(t)=\begin{cases}3t/2,&t<4N/3,\\3t/4,&t\ge4N/3\end{cases}
\]
preserves this measure: its two image intervals are \([3N/2,2N)\) and \([N,3N/2)\). On each of the \(3N\) cells \([k/3,(k+1)/3)\), \(3N\le k<6N\), the two integer sources are
\[
             x=\lfloor k/3\rfloor,\qquad x'=\lfloor k/2^s\rfloor,
             \qquad s=1\ (k<4N),\quad s=2\ (k\ge4N).
\]
Its weight is \(\log((k+1)/k)\). Invariance for functions of the integer sources is a finite identity: the three outgoing cells at each \(x\) sum to \(\log((x+1)/x)\), as do its two or four incoming cells.

At an arbitrary supplied horizon \(L\ge1\), call the cell good if both of the following finite tests hold:

* \(T^{L+s}x=T^Lx'\) and \(q_{L+s}(x)=q_L(x')+1\);
* neither source visits \(S\) through its respective comparison clock, including the endpoints.

On a good cell a finite first hit by either source is equivalent to a finite first hit by the other. Their first clocks differ by exactly \(s\), and their first grades differ by exactly one, with the larger of each attached to \(x\). This follows by appending the common deterministic suffix to both protected prefixes. It includes periodic targets and the possibility that both sources miss \(S\).

For a supplied \(m\), write \(F=\{\tau_S<m\}\), \(A=\{\tau_S=m\}\). On good cells \(x\in F\cup A\) implies \(x'\in F\). Invariance gives \(\mu(A)+\mu(F)\le\mu(F)+\mu(\mathrm{bad})\). Exactly the same proof uses finite first grades, excluding misses from both sets. Each integer in \([N,2N)\) has weight at least \(1/(2N)\) and each cell has weight at most \(1/(3N)\), by integrating \(dt/t\) or by the elementary logarithm bounds. Thus either of the two atom counts satisfies the **unconditional finite inequality**
\[
                          3\# A\le 2\#\{\text{bad cells}\}.               \tag{2}
\]

To isolate startup costs, for \(s=1,2\), \(j<3\cdot2^s\) and \(0\le v<2^L\), put \(k=3\cdot2^s v+j\). Test the two physical equalities above at its two integer sources, omitting \(S\). Using zero as a residue representative causes no positivity issue: the lift formula preserves the boolean counted test. Let \(p_{s,L}\) be the fraction of failed equalities among all such \((v,j)\), and \(p_L=\max_s p_{s,L}\). For fixed \(j\) the test depends only on \(v\bmod2^L\). Indeed \(x=2^sv+\lfloor j/3\rfloor\), \(x'=3v+\lfloor j/2^s\rfloor\); after the first \(s\) steps, \(T^s x=3^a v+b\), \(a=q_s(\lfloor j/3\rfloor)\), \(b=T^s(\lfloor j/3\rfloor)\). At any lift by \(2^L u\), the two \(L\)-step parity words stay fixed. Their final affine slopes agree exactly when the tested grade equality holds, and then endpoint equality is also lift-invariant. The total number of cells failing the two fusion equalities is at most \(3Np_L+18\cdot2^L\), counting complete periods on each side and at most one further period each.

At most \((2^{L+3}-1)B\) positive integers visit \(S\) by time \(L+2\), since each state has at most two positive shortcut parents. Each such integer is incident to three outgoing and at most four incoming cells. Consequently (2) yields
\[
                  \frac{\# A}{N}\le 2p_L+50(1+B)2^L/N.                 \tag{3}
\]
Every item on the right is explicit and finite. No stationarity conjecture on the integer trajectories or the starting integers is involved.

## Reduction to one scalar pair

The finite menu comprises pairs \(3^av+b,3v+c\), with \(a\in\{0,1,2\}\), bounded integer offsets, and the known grade adjustment \(a\). Directly apply the fixed-state counted pair estimate after taking the lower-slope affine variable as Haar anchor. Alternatively let \(u_L\) be the fraction of adjacent pairs \((t,t+1)\bmod2^L\) that have unequal state or unequal grades at the specified physical clock \(L\). There is an absolute finite \(C\) with \(p_L\le C u_L\) for every \(L\ge1\):

* Two inputs of equal slope differ by a bounded integer. Join them by that many adjacent comparisons and use the union bound. Every anchor runs through the entire binary residue system, since its slope is odd.
* For slopes differing by three, call the lower one \(w\) and the higher one \(3w+e\), \(e\) bounded. Pick the odd number \(w'\in\{w,w+1\}\). At clock one, \(w'\) and \(3w'+1\) reach exactly the same state, with the lower input having precisely one extra odd departure. This identity persists to clock \(L\). Join \(w\) to \(w'\) and \(3w+e\) to \(3w'+1\) by bounded translations. One may union over both possible choices of \(w'\) before applying the binary residue estimate. Restoring the initial grade \(a\) gives the required left-minus-right grade difference of one in each orientation.

Thus qualitative \(u_L\to0\) suffices for uniform vanishing in (1) without a rate. With the [fixed-state upper bound](SCALAR_RETURN_PROOF.md) \(u_L\ll(L+1)^{-1/2}\), choose \(L=\max(1,\lfloor\tfrac12\log_2(N/B)\rfloor)\) when \(N/B\) is large, and use the trivial bound otherwise. This proves (1). The proof does not transfer the first \(L\) binary bits to an unbounded event: it uses those bits only for an exact finite comparison before the two source paths share a common future.

For fixed nonnegative integers \(a,b\) with \(a+b>0\), the same cut at a finite threshold gives (1) for each atom of \(a\tau_S+b g_S\); either of the two individual clocks can be absent. In particular this includes the ordinary clock \(\tau_S+g_S\) to a positive odd target. An interval of \(w\) consecutive integer values costs at most \(w\) times this bound.

## Kernel proof and bounded replay

[MantissaFlow.lean](MantissaFlow.lean) proves both exact logarithmic weight identities and the integer flux inequality (2) for an arbitrary disjoint atom and strict lower set on the actual finite comparison graph. [FirstHitFlux.lean](FirstHitFlux.lean) proves both first-visit lags on every protected physical merger and instantiates (2) for every finite target set, any supplied finite first-hit deadline, and every positive integer combination of clock and grade. The bound is independent of the deadline. Since an octave is finite, taking a deadline beyond all its finite visits gives the stated unrestricted finite atom. The Lean statements have no absorption or density hypothesis. The survival and integration estimates yielding (1) and (4) are written proofs.

[check_mantissa.py](check_mantissa.py) independently computes finite comparator survival by the canonical two-branch kernel and by direct ordinary positive-residue lifts, then checks actual first-entrance transfer and the atom counts in three complete octaves for four target sets. [Exact finite receipt](../../../reports/astra-infinite-descent-20261127/escape/MANTISSA_CHECKS.json).

## The fair source cutoff and its sharpness

For one odd target \(y\), use the first-arrival row \(A_{d,m}(y)\) and \(h=3^d2^{-m}/y\). Each start obeys \(hz\le1\). Apply (1) on dyadic source shells which meet \((R,1/h]\), summing their geometric lengths. For \(R\ge3\),
\[
  \sup_{y,d,m}h\,\#\{z\in A_{d,m}(y):z>R\}\ll(\log R)^{-1/2}.           \tag{4}
\]
A partial bottom shell has lower end at least \(R/2\); the sum of all shell lengths is at most \(2/h\). No positive correction floor is needed in the upper bound. In particular the limiting maxima and finite attainment proof in [EXTREMAL_ROWS.md](EXTREMAL_ROWS.md) can use adjacent qualitative synchronization and elementary reciprocal packing alone. This argument for (4) does not prove nullity of the full compact correction set; the [closed-support argument](FAIR_CLOCK_DIFFUSION.md) has its separately listed inputs.

A separate fixed-target **lower** input makes (4) sharp. At target 1, the positive-basin timed Gaussian law gives constants \(A,c>0\) such that every large octave \([R,2R)\) contains at least \(cR\) starts first hitting 1 in the window \(\mu\log R+[-A,A]\sqrt{\log R}\). This follows by subtracting the fixed-target cumulative counts at \(R,2R\) with fixed Gaussian thresholds, allowing the bounded change in the centering on the octave. Their first marks satisfy \(c_0\le hz\le1\) by the unconditional simple-segment correction floor. At each of the \(O(\sqrt{\log R})\) clocks, \(c_0/(2R)\le3^d2^{-m}\le1/R\) allows at most \(1+\lceil\log_3(2/c_0)\rceil\) grades. Some joint row consequently has normalized mass from sources in \([R,2R)\) at least \(c'/\sqrt{\log R}\). Using the next octave if necessary gives the same strict tail \(z>R\) in (4). This lower estimate uses no local Gaussian theorem. [Leen fixed-target timed law as stated in Weaver 179/v1, Appendix A.5, equation (A.8)](https://rstation.ai/problems/collatz/papers/179/v1) · [Elementary correction floor](HIGH_TARGET_ROWS.md).

Equations (1) and (4) estimate families of high starting integers. One fixed integer on a hypothetical escaping trajectory would remain present in a sequence of rows below each sufficiently large source cutoff. Its small-source contribution still has to be controlled to deduce boundedness.

## Joint grade translation with a retained terminal coordinate

There is also a distributional form of the comparison. On the finite-hit event for the log-uniform real octave parameter \(t\), record the first-hit label \(y\in S\), its clock \(m\), its grade \(g\), and
\[
                   J=m-g\log_2 3-\log_2(t/N).
\]
The finite-hit law of \((g,J,y)\) is a subprobability \(\nu\) on \(\mathbb Z\times\mathbb R\times S\), omitting misses. On a protected good edge, the transformed starting integer has \((g',m')=(g-1,m-s)\), the same label, and **exactly the same** \(J\) by \(f(t)=3t/2^s\). Both sources miss together when the common tail misses. If \(E\) translates grade up by one, this coupling and octave invariance give
\[
          \|\nu-E\nu\|_{\rm variation}\ll (\log(2+N/B))^{-1/2}.
\]
The norm is total absolute variation, at most twice the bad probability under normalized \(dt/(t\log 2)\). Reducing grade modulo a positive \(Q\) and averaging its first \(Q\) translates thus puts its joint law within \(O(Q/\sqrt{\log(2+N/B)})\) of uniform on \(\mathbb Z/Q\mathbb Z\) times its own \((J,y)\) marginal. This is an absolute subprobability estimate; conditioning on a rare subevent costs its mass in the denominator. Replacing \(t\) by the integer \(\lfloor t\rfloor\) in \(J\) changes its value by \(O(1/N)\) and therefore allows bounded Lipschitz tests with that additional error. Exact total variation for arbitrary measurable selections uses the original continuous parameter.

The bounded weight \(t3^g2^{-m}/y\le1+1/N\) is a function of \((J,y)\) and is invariant on good edges. Integrating against \(dt/t\) gives the *exact* integer fair first-moment coefficient \(3^g2^{-m}/y\) on each unit source cell. Thus the measure-valued grade difference also controls the fully physical first-moment histogram with the other clock summed out. For all visits and all positive odd target labels simultaneously, a further loss factor makes the complete occupation sum finite; the [original stopped-trace bound](ORIGINAL_TRACE_VARIATION.md) gives the exact rate for its dyadic mean.
