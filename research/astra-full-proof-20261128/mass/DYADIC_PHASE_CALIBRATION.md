# A summable basin-boundary test and a genuine terminal-phase obstruction

The summable-boundary consumer and its exact dyadic interpolation were already published in the earlier checkpoint of [concurrent PR 217](https://github.com/GettysburgResearch/collatz/blob/85b48ef9de755fe016166592cb048167c83fb7e8/research/astra-collision-factor-bridge-20261128/collision/DYADIC_BOUNDARY_ZERO_ONE.md). That note removes the need to assume a density limit using the exact odd equation and separates counted synchronous fusion from component membership. Its [sharp halving example](https://github.com/GettysburgResearch/collatz/blob/85b48ef9de755fe016166592cb048167c83fb7e8/research/astra-collision-factor-bridge-20261128/collision/SHARP_HALVING_BOUNDARY.md) is a constructed binary label. The contribution here is the divergent-boundary theorem for the **actual** two-phase terminal mark on positive integers, even when one demands a complete certificate and permanent synchronous nonfusion.

Let \(T(n)=n/2\) for even \(n\) and \(T(n)=(3n+1)/2\) for odd \(n\). Its terminal shortcut cycle is \(1,2\). For a function \(w\) on positive integers define its dyadic middle-edge fraction
\[
 D_j(w)=2^{-j}\#\{\,2^j\le n<2^{j+1}:w(2n+1)\ne w(2n)\,\}.
\]

**Sufficient condition for full convergence.** Write \(f(n)=1\) if \(n\) reaches 1, \(f(n)=0\) otherwise. If \(\sum_jD_j(f)<\infty\), every positive integer reaches 1, using natural density of the convergence basin and positive predecessor lower density at every unit as external inputs. Indeed \(f(2n)=f(n)\). The step functions \(F_j(u)=f(\lfloor 2^j u\rfloor)\), \(1\le u<2\), satisfy
\[
 \|F_{j+1}-F_j\|_1=\tfrac12D_j(f).
\]
Summability gives a strong \(L^1\) limit that is 0 or 1 almost everywhere. Natural density \(d\) gives the weak limit equal to the constant \(d\) by differencing ordinary counts on intervals. Hence \(d\in\{0,1\}\). The known positive density at root 1 rules out zero. A bad component contains a positive unit target (take one odd forward image), whose positive-density predecessors would exclude density one. Summability for the actual basin labels is open.

**A first-hit and permanent nonfusion calibration.** Define an ordinary terminal mark \(p(n)=(-1)^{\tau_1(n)}\) when the first shortcut hitting time \(\tau_1(n)\) is finite, and zero otherwise. Then the following is an unconditional mathematical deduction from positive predecessor density of 1:
\[
                            \sum_{j\ge0}D_j(p)=\infty .
\]
Every edge in \(D_j(p)\) has at least one arm with a literal finite first-hit certificate to 1, and the two arms never meet at the same shortcut time. This includes all times after the terminal visit. Thus providing a first-hit certificate on one arm, together with genuine permanent *synchronous* nonfusion, does not justify a summable estimate. A proof of the preceding sufficient condition has to distinguish changes in convergence basin from differences in the phase of the known cycle.

To prove divergence, \(p(Tn)=-p(n)\) holds at every positive integer, including at \(1\) because \(T(1)=2\) and \(T(2)=1\). In particular
\[
 p(2n)=-p(n),\qquad p(2n+1)=-p(3n+2).
\]
If \(p\) differs on two starting values, its values differ on all pairs of simultaneous iterates. At least one of the two marks is nonzero.

Assume \(\sum_jD_j(p)<\infty\). Put \(P_j(u)=(-1)^jp(\lfloor2^j u\rfloor)\). On the left half of each dyadic cell \(P_{j+1}=P_j\), and on the right half they differ only on the indicated middle edges, by at most two. Hence \(\|P_{j+1}-P_j\|_{L^1[1,2]}\le D_j(p)\). Write \(P\) for the strong limit. The exact compatibility \(P_j(2u)=-P_{j+1}(u)\) extends convergence to \(L^1\) on every compact interval inside \((0,\infty)\) and gives \(P(2u)=-P(u)\) almost everywhere.

For \(n=\lfloor2^ju\rfloor\), the relations above and \(D_j(p)\to0\) give
\[
 (-1)^jp(3n+2)-P_j(u)\longrightarrow0
 \quad\hbox{in }L^1([1,2]).
\]
The quantity \(P_j(3u)\) evaluates the same mesh array at \(3n\), \(3n+1\), or \(3n+2\). The \(L^1\) error from changing to \(3n+2\) tends to zero: on each of the three subcells translate the argument \(3u\) by at most \(2\cdot2^{-j}\), use strong local convergence of \(P_j\), and translation continuity of the limit \(P\) in \(L^1\). Consequently \(P(3u)=P(u)\) almost everywhere, first on \([1,2]\) and then on all its dyadic dilates. The function \(v\mapsto P(e^v)\) is periodic with period \(\log4\) and invariant under rotation by \(\log3\). The ratio \(\log3/\log4\) is irrational, since positive powers of 3 and 4 differ. The Fourier coefficients of a periodic \(L^1\) function fixed by this rotation vanish away from frequency zero, so \(P\) is constant almost everywhere. The relation at scale 2 forces this constant to be zero.

But \(\|P_j\|_1\) is the fraction of the octave reaching 1. Its convergence to zero would make the upper natural density of the entire convergence basin zero by summing dyadic octaves (one partial octave costs at most its full count). This contradicts positive lower predecessor density at 1.

The distinction between synchronous merger and eventual membership in the same component is essential. The sharp raw counted-merger tail of order \(t^{-1/2}\) is consistent with this proof; no quantitative coalescence theorem or conjecture about the distribution of the first-hit-time parity enters the divergence argument. It does not decide the sequence \(D_j(f)\).

The natural-density and predecessor-positivity inputs are documented separately in [Weaver 12, Inputs C and D](https://rstation.ai/problems/collatz/papers/12/v1) and [the external Lean audit of the positive lower-density theorem](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html). The [quantitative synchronization paper](https://rstation.ai/problems/collatz/papers/13/v1) describes the different counted-merger observable and credits the earlier Duran–Leen results. The deductions above are written proofs; the cited formal developments were not rebuilt in this packet.
