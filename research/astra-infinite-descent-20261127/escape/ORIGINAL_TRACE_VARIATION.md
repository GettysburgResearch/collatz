# A dyadic mean bound for the original stopped-trace rate statistic

**Unconditional written upper bound.** For the actual finite-law statistic \(Q_j^*\) in PR193, there is an absolute \(C<\infty\) such that for every integer \(D\ge1\),
\[
                         \sum_{D\le j<2D} Q_j^*\le C\sqrt D.             \tag{1}
\]
In particular there is an unbounded sequence \(j\) with \(Q_j^*\ll j^{-1/2}\). The earlier full-convergence criterion asks for \(O(j^A(2/3)^j)\) along such a subsequence. The polynomial upper bound (1) leaves that criterion open. The proof uses a first-moment identity on all ordinary forward visits, elementary geometric-word cutoff bounds and the [independent scalar return estimate](SCALAR_RETURN_PROOF.md). The [finite octave comparison](CLOCK_ANTICONCENTRATION.md) has a companion Lean proof for individual first-hit atoms. The full all-visits variation argument below is written mathematics.

## Exact original law

Use the odd map \(U(x)=(3x+1)/2^{v_2(3x+1)}\). An inverse word of \(d\) positive odd-gap exponents ending at a unit source \(x\), begun at a positive odd unit target \(y\), has multiplier \(A=3^d2^{-m}\), where \(m\) is the sum of its exponents. Let \(\rho_1(x)=1\) for \(x\equiv1\bmod3\), \(2\) for \(x\equiv2\bmod3\), and zero for \(3\mid x\); these are the summed single-letter positive multipliers, allowing nonunit leaves after that letter. The original total/constrained rows are
\[
    \rho_{d+1}(y)=\sum_w A_w\rho_1(x_w),\qquad
    L_{d,y}(t)=\sum_w A_w\rho_1(x_w)\mathbf1_{A_wx_w/y\le t}.
\]
The empty word is included at \(d=0\); nonunit target rows vanish. The \(d\)-letter words are all visits, including repeats. With \((u)_+=\max(0,u)\), the exact statistic studied here is
\[
 Q_j^*=\sum_{y>1\ {\rm odd}}\frac{1}{y(3y+1)}\max\!\left\{
 (\rho_{j+2}(y)-\rho_{j+1}(y))_+,\
 \sup_{0\le t\le1/(j+1)}(L_{j+1,y}(t)-L_{j,y}(t))_+\right\}.          \tag{2}
\]
The positive part is taken separately at every target. [PR193, full pinned head aa6868996f6f30b12d91c367f7c6edcfd93784b2, ENDPOINT_RATE_TEST.md, rational-band statistic](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/ENDPOINT_RATE_TEST.md).

## A vector of all visits with total mass at most one per source after scaling

For *every* positive integer \(x\) let \(y_d=U^d(\operatorname{oddpart}x)\), and let \(m_d\) be its true shortcut clock to this odd landing, including the initial halvings. Each landing is kept, including every lap of a recurrent trajectory. At the \(d\)-th landing put
\[
 h_d(x)=\frac{3^d2^{-m_d}}{y_d},\qquad b_d(x)=x h_d(x),\qquad
 v_x(d,y)=\mathbf1_{y_d=y}\frac{h_d(x)}{3y+1}.
\]
Then \(b_0=1\) and \(b_{d+1}=b_d\,3y_d/(3y_d+1)\). Consequently
\[
          x\sum_y v_x(d,y)=b_d-b_{d+1},\qquad
          \sum_{d,y}v_x(d,y)\le 1/x .                                 \tag{3}
\]
Here and below \(y\) ranges over all positive odds, temporarily including 1. These nonnegative sums require no finite-orbit assumption. The source selector \(\psi(x)=\mathbf1_{x\ {\rm odd}}\rho_1(x)\) has fixed period six and mean \(1/2\). At grade \(d\), a positive odd unit source determines its forward path to the indicated \(y_d\), while every retained inverse word gives this same physical path. It follows exactly that
\[
             \sum_{x\ge1}\psi(x)v_x(d,y)=\frac{\rho_{d+1}(y)}{y(3y+1)}.
                                                                         \tag{4}
\]
For \(3\mid y\) both sides vanish, since a positive-grade forward landing is a ternary unit and a nonunit source has zero selector. Adding the missing-odd-parity sources only occurs in the intermediate unweighted calculation.

## The derivative on one octave, including the source selector

Take a dyadic octave \(I_N=[N,2N)\cap\mathbb Z\) with \(N\ge2\), and let \(f\) be the [measure-preserving real octave map](CLOCK_ANTICONCENTRATION.md) for \(dt/t\). Write \(x=\lfloor t\rfloor\), \(x'=\lfloor f(t)\rfloor\), \(f(t)=3t/2^s\) with \(s=1\) or 2. Set \(L=\max(1,\lfloor\tfrac12\log_2 N\rfloor)\). Except on a set of logarithmic octave measure \(O((1+L)^{-1/2}+2^L/N)\), the two paths reach the same state at clocks \(L+s,L\), and the first path has one extra odd departure. This uses just the two fusion equalities, with no target removal.

Introduce the finite-mass vector \(t v_x\) on integer grades and positive odd targets, extending it by zero at negative grades. Let \(E\) denote the unit grade shift, \((Ea)(d,y)=a(d-1,y)\). On a successful comparison, all odd landings in the common future agree between \(t v_x\) and \(E(f(t)v_{x'})\). Indeed the physical clocks differ by \(s\), the grades by one, and \(3^d2^{-m}t=3^{d-1}2^{-(m-s)}f(t)\). If the merger state is even, finish the same even coast on both paths; it contributes no odd landing before its end. Every unmatched landing preceded the merger at a clock at most \(L+2\), and has \(y\ge N/2^{L+2}\) because a shortcut step decreases height by at most a factor of two. There are at most \(L+3\) unmatched landings on each path. Since \(t h_d(x)\le t/x\le1+1/N\), their combined mass is \(O((L+1)2^L/N)\). On a failed comparison (3) bounds the combined total mass by \(2(1+1/N)\) irrespective of the futures. Integrating in \(dt/t\), using invariance and \(tv_x\,dt/t=v_x\,dt\) on each unit source cell, gives
\[
      \left\|\sum_{x\in I_N}v_x-E\sum_{x\in I_N}v_x\right\|_1
          \ll (\log(2N))^{-1/2}.                                       \tag{5}
\]
All vector integrals may first be taken on any finite set of grade-target coordinates. The triangle inequality bounds every such restriction by the same integrated full mass in (3). Increasing those finite sets and applying monotone convergence to the sum of absolute differences proves (5) on the full countable index set. This \(\ell^1\) norm sums over *all* grades and targets at once.

For the source selector, on every counted-fused adjacent pair \(x,x+1\) through the same clock \(L\), all post-merger entries of \(v_x,v_{x+1}\) agree exactly, with no grade shift. Their unmatched mass is \(O((L+1)2^L/N^2)\). Otherwise its bound is \(2/N\). The number of failed adjacent comparisons among \(x\in I_N\) is \(O(N/\sqrt{L+1}+2^L)\) by the same fixed binary-period count. Therefore \(\sum_{x\in I_N}\|v_{x+1}-v_x\|_1\ll(\log(2N))^{-1/2}\). The totals of \(v_x\) on each pair of neighboring residue classes modulo six differ by at most this bound plus \(O(1/N)\) for the two ends. Comparing all six classes shows
\[
       \left\|\sum_{x\in I_N}\psi(x)v_x-\tfrac12\sum_{x\in I_N}v_x\right\|_1
            \ll (\log(2N))^{-1/2}.
\]
The grade shift is an isometry on the extended index set. Combining with (5) proves the same octave variation for the exact selected physical source measure. The first finite octave costs an absolute constant by (3).

## Completing every source and target in the original law

Let \(X=2^{20D}\), \(Y=2^{4D}\); use sources \(x<X\) so the selected interval is a union of entire dyadic octaves. Summing (5) and the selector error over their \(20D\) octaves costs \(O(\sqrt D)\), since \(\sum_{j\le20D}(j+1)^{-1/2}\ll\sqrt D\). Take only grades \(D\le j<2D\) and \(y>1\) after this simultaneous bound.

Here are explicit unmarked upper bounds for restoring the tails, valid also for the marked rows by domination. The full one-letter row sum is at most two, so \(\rho_{d+1}(y)\le2^{d+1}\). For \(0\le d\le2D\) the discarded weighted mass of targets \(y>Y\) is at most \(2^{d+1}/(3Y)\). For \(y\le Y\) and \(x\ge X\), positive inverse affine transport gives \(x\le 2^m y/3^d\le2^m y\), hence \(m\ge16D\). Drop all integrality conditions and take independent positive gaps with \(\Pr(G=e)=2^{-e}\). Their joint clock \(m\) has \(\mathbb E(4/3)^m=2^d\). Since \(\psi\le2\), the omitted undivided mass at each such \(y\) is at most
\[
       2\,3^d\Pr(G_1+\cdots+G_d\ge16D)\le 2\,6^d(3/4)^{16D}.
\]
This holds also at \(d=0\), where the omitted rows in fact vanish. The kernel summed over \(y>1\) is bounded by an absolute constant. With \(d\le2D\), \(36(3/4)^{16}<1\); the target-tail base is at most \(1/4\). Thus summing all the omitted terms over the needed grades costs \(O(D\theta^D)\) for a fixed \(0<\theta<1\). Absolute differences cost at most the two omitted masses. In particular the **two-sided** unmarked summed variation is \(O(\sqrt D)\).

Finally the marked positive difference in (2) is at most \(L_{j+1,y}(1/(j+1))\). For \(j\ge D\), a retained source can contribute only at grades \(d=j+1\) with \(b_d\le1/D\). By monotonicity of \(b_d\) and (3),
\[
     \sum_{d:\,b_d\le1/D}\sum_y v_x(d,y)\le\frac{1}{Dx} .             \tag{6}
\]
The selected sources \(x<X\) consequently cost at most \(2(1+\log X)/D=O(1)\) over the whole grade block. The preceding exponential tail bounds control all other sources and targets. Thus even the sum over grades and targets of the **endpoint band alone** is \(O(1)\) per dyadic grade range. Combining the two estimates yields (1).

The full unmarked terminal law has a source-qualified qualitative convergence theorem in Weaver 176. Its conclusion and the stopped-rate criterion in PR193 have different hypotheses and quantitative content. Estimate (1) is a rate for dyadic *means of consecutive original rows*, without replacing columns by an average before taking the absolute value or positive part. It gives neither a bound at all individual grades nor exponential decay along a subsequence. [Weaver 176/v1](https://rstation.ai/problems/collatz/papers/176/v1) · [PR193, stopped-rate criterion](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/STOPPED_RATE_TEST.md).

## Why the discarded merger probability cannot furnish an exponential upper bound

The first branch of the octave exchange has a residue cell \(k=6v\). There \(x=2v\), \(x'=3v\), and after the one left step the canonical pair is \((v,3v)\), with count gap one. Before its first zero the mixed-time count gap is an unbiased nearest-neighbor walk from one, and each mixed step needs at least one physical step. Thus a walk that survives its first \(L\) mixed steps cannot have counted-fused at physical clock \(L\). The reflection count gives
\[
          p_{1,L}\ge\tfrac16 2^{-L}{L\choose\lfloor L/2\rfloor}\gg(L+1)^{-1/2}.
\]
The factor six retains just the displayed cell residue in the finite comparator. Complete binary periods transfer this lower bound, up to an absolute constant, to the actual failed-cell logarithmic mass when \(L\le\tfrac12\log_2 N\) and \(N\) is large. More generally the optimized *error expression* \(p_L+2^L/N\) cannot be smaller than a constant times \((\log N)^{-1/2}\): when \(L\le 2\log_2 N\) use the lower bound; beyond it the remainder alone exceeds one. The full-trajectory bad-cell allowance used in (5), when summed over the first \(20D\) source octaves, therefore has square-root order before any restriction to a grade block. Reducing this error needs to retain the loss actually deposited at the tested grades, or cancellations between sources or octaves. The argument is a lower bound on a specific proof allowance, not a lower bound on the original signed variation or on \(Q_j^*\).

## Bounded verification

[check_trace_transport.py](check_trace_transport.py) independently enumerates all ordinary odd-unit inverse words with positive source below 257, target below 129 and grade through eight, using the intermediate height bound from the real forward map. It checks every path and original normalization against forward trajectories, including repeated cycle landings. It also checks the loss identity and band charge to grade 140 on eleven actual sources, and a two-sided truncated all-target variation bound in three complete octaves. These tests are finite. [Exact receipt](../../../reports/astra-infinite-descent-20261127/escape/TRACE_TRANSPORT_CHECKS.json).

The signed derivative also has an exact [ordinary gap-three representation](GAP_THREE_TRACE.md) that retains the unpaid loss at the tested grades. The finite telescoping identities (3), (6) and the shifted common-future scalar loss are kernel-checked in [OriginalLoss.lean](OriginalLoss.lean).
