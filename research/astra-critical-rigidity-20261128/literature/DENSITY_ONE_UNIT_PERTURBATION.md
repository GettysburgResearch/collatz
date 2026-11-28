# Adding one on a sparse set makes almost every ordinary start diverge

**Proposed elementary written theorem.** For any prescribed \(B\ge2\) there is one computable map \(U\) of the positive integers with all of the following properties.

* At every even input \(U(n)=n/2\). At every odd input \(U(n)\) is either \(T(n)=(3n+1)/2\) or \(T(n)+1\). It agrees with the genuine shortcut at every input at most \(B\), including the full known cycle \(1,2\).
* Its complete set of changed inputs \(\mathcal D=\{n:U(n)\ne T(n)\}\) satisfies
\[
       |\mathcal D\cap[1,X]|\ll
           X\,\frac{(\log\log X)^{12}}{(\log X)^2}                     \tag{1}
\]
for large \(X\), with an absolute constant. Each of the square-root octave costs of \(\mathcal D\) therefore belongs to \(\ell^q\) across octaves for every \(q>1\).
* The set of starts whose \(U\)-trajectory eventually consists entirely of strictly increasing odd values has natural density **one**. Each of these trajectories has \(\lim_{t\to\infty}(2/3)^tU^t(n)\in(0,\infty)\). For a density-one set of starts the increasing tail begins by \(O(\log n/(\log\log n)^2)\) native steps. At such starts \(\tau_U(n)<\tau_T(n)\), where each date is the first global minimum for its own map. The joint laws of the starting integer and its complete path stopped at that minimum, for \(U\) and for \(T\), have total variation distance tending to **one** under uniform sampling through \(X\).

In particular the known cycle still exists and its \(U\)-basin has natural density zero. A finite list of previously computed finite true trajectories is retained by taking \(B\) at least their largest observed value. The construction produces escaping ordinary integers for the modified map. Its conclusions about \(T\) are the true finite visits and later smaller witnesses used to prove capture. No external stationary or first-passage theorem is required for these three properties.

## The change set

Use the computable set \(F=F_1\) of [Sharp multiscale targets](SHARP_MULTISCALE_TARGETS.md), whose construction and density-one early visit proof use the native parity bijection and finite word counts. For odd \(y\), let \(g(y)\) be the least odd integer at least \((3y+1)/2\). It is either the true next value or one larger, with
\[
    \tfrac32 y+\tfrac12\le g(y)\le\tfrac32 y+\tfrac32 .
\]
It is strictly increasing on the odd inputs: consecutive odd inputs have true outputs differing by three, and rounding changes each by at most one. Write
\[
 S=\bigcup_{t\ge0}g^t\big(F\cap(B,\infty)\big),\qquad
 U(n)=
 \begin{cases}g(n),&n\in S,\\ T(n),&n\notin S.\end{cases}              \tag{2}
\]
This is an odd set entirely above \(B\). To decide membership of an odd \(y\), check its original seed condition, then check its unique possible prior odd \(x\) under \(g\). It suffices to test the at most two integers \((2y-1)/3,(2y-3)/3\) when these are integral, positive and odd. A genuine prior value is strictly smaller, so this test terminates. This also specifies \(U\) at inputs whose genuine forward behavior is unknown.

Here is the full counting cost of closing \(F\) under these indefinitely many forward steps. Put \(b=3/2\). Iteration gives
\[
     b^t y\le g^t(y)\le b^t(y+3) .
\]
Consequently a seed feeding \([X,2X)\) at depth \(t\) is in \([Xb^{-t}-3,\,2Xb^{-t})\). The possible depths satisfy \(t=O(\log X)\). For \(W=Xb^{-t}\ge\sqrt X\), the seed interval meets a bounded number of dyadic octaves of size comparable to \(W\). The seed-density bound is \(O(W(\log\log X)^{12}/(\log X)^2)\), uniformly in this range. Its sum is \(O(X(\log\log X)^{12}/(\log X)^2)\) by geometric decay. When \(W<\sqrt X\), the trivial counts \(O(1+W)\) sum to \(O(\sqrt X+\log X)\). Thus the entire \(S\) satisfies the claimed octave bound. Summing the resulting octave estimates above \(\sqrt X\), and counting at most \(\sqrt X\) smaller positive integers, proves (1) for \(S\) and hence its subset \(\mathcal D\).

## Capture and the two actual minimum dates

Outside \(S\), both maps take identical edges. On entering \(S\), the modified trajectory follows \(g\) forever by (2), and is strictly increasing. For every start, its membership in the set of trajectories entering \(S\) is exactly the event \(O_T(n)\cap S\ne\varnothing\). Moreover its first entrance under either map is the same. Along an increasing tail from \(y\),
\[
     b^{-t} g^t(y)=y+\sum_{i=0}^{t-1}
                   b^{-i-1}\big(g(g^i y)-b g^i y\big)
\]
is increasing and bounded by \(y+3\), which gives the claimed positive scaled limit after restoring the fixed entrance-date factor.

On the source octave \([2^j,2^{j+1})\) use the joint good event in the elementary proof of [Sharp multiscale targets](SHARP_MULTISCALE_TARGETS.md). By \(K=\lfloor j/(\log(j+2))^2\rfloor\) the **true** trajectory hits \(F\) at a state at least \(n2^{-K}>B\) eventually, and \(T^{16K}n<n2^{-K}\). Thus the modified trajectory entered \(S\) at some date at most \(K\); it never decreases after that date. Its minimum is attained by \(K\), whereas every genuine state through \(K\) exceeds the genuine value at \(16K\). This yields the strict inequality of minimum dates. The same conclusions hold uniformly for source intervals in this octave containing at least \(2^{20K}\) consecutive integers. The preceding note's octave decomposition gives the density-one statement through every ordinary cutoff. For a fixed start the two stopped paths are deterministic. When the start is included in the output, distinct starts have disjoint supports, so total variation equals the fraction of starts on which the two stopped paths differ. Their unequal lengths on the joint good event prove the last assertion.

## The stronger summability condition

For comparison, [All high targets](ALL_HIGH_TARGETS.md) proves a source-qualified bound for a genuine preminimum visit to any high mask \(E\) by a constant times the sum of its square-root octave costs, plus \(o(1)\). For any modified map fixing \(1,2\) whose changed inputs are all at least \(R>2\), a start in the genuine basin of one can leave that basin's true future only if it reaches a changed input before its first true visit to one. Consequently its **absolute** capture probability is at most \(Cw_R(\mathcal D)+o(1)\) under uniform sampling as \(X,R\to\infty\). The previous paragraphs give complete capture, in density, of the genuine basin despite the weaker summability in (1); its genuine positive density is a separate predecessor-theorem input. This comparison concerns asymptotic probabilities and does not decide the genuine Collatz conjecture. [Mazur, predecessor density](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf)
