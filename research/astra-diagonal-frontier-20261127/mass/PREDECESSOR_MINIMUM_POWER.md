# A power bound for predecessor density in terms of the smallest ancestor

Let \(h=H_2(\log_3 2)=0.9499555271\ldots\). On the cited relative passage, finite-quotient moment and beyond-dyadic-horizon canonical source inputs, there is an absolute \(\xi>0\) such that the following estimates hold with exponent
\[
                         \sigma=1-h+\xi>0.05004447.                    \tag{1}
\]
No numerical value for \(\xi\) is claimed. Constants may inherit ineffective onsets from the analytic inputs.

1. For every specified positive odd unit \(a\), put \(m_*(a)=\min\{v\ge1\text{ odd}: U^jv=a\text{ for some }j\ge0\}\). The proportion of odd inputs in **any** octave \([Y,2Y)\) reaching \(a\) is \(O(m_*(a)^{-\sigma})\), as is the relative natural predecessor density \(d_a\). The target may be periodic.
2. Let \(\mathcal B\) be any collection of distinct nonperiodic unit immediate parents \(x\) of a specified \(a\), with disjoint predecessor basins and \(m_*(x)>M\) for each. The entire union of their basins has proportion \(O(M^{-\sigma})\) in every such octave. The constants are independent of the target and collection. In particular for nonperiodic \(a\), \(Q_a(m_*(X_1)>M)\ll d_a^{-1}M^{-\sigma}\).
3. The global proportion of positive integers through any \(X\) whose whole forward orbit remains above \(M\) is \(O(M^{-\sigma})\), uniformly in \(X\). The same bound holds for the critical first-entry height tail and for \(d_zq_z^\lambda\) at every nonperiodic unit \(z\). Here \(\lambda=\log_2 3\); see [the critical classifications](CRITICAL_FIRST_ENTRY.md).

The predecessor-minimum conclusion concerns *ancestors* of a fixed target. A target without any small ancestor may later reach a smaller value, so the forward-minimum statement alone does not imply the first conclusion. The predecessor-density result in [Weaver, Paper 12, Theorem 11 and (36)](https://rstation.ai/problems/collatz/papers/12) had errors \(O_A((\log M)^{-A})\) in these two ancestor applications. For global forward minima, [Nashida, revision r8, theorem \(\texttt{Collatz.nd_collatz_uniform_explicit}\)](https://github.com/harappa/collatz-fixed-barrier-power-saving/blob/976fffb160744c56f1f26912f7bd23d195fe02d2/CollatzND/Core/Explicit.lean) already reports a fully formal uniform polynomial bound with explicit exponent approximately \(3.506\cdot10^{-6}\). The present numerical base \(1-h\), the extra unspecified positive gain and the stopped-ancestor bounds use different inputs. None of the analytic inputs below has been rebuilt in this packet.

## A uniformly sparse set at every target

Choose a fixed slope \(\beta>\lambda\), sufficiently close to \(\lambda\) as specified below. An input \(y\) *passes to* \(a\) if its finite word through first hitting \(a\) has \(S_i\le\beta i\) at all forward odd prefixes. Write \(E_a\) for these sites, including \(a\). Write \(P_\beta\) for those passing forever. We show that some absolute \(g>0\) gives
\[
 \#(E_a\cap[Y,2Y))\ll Y^{h-g},\qquad
 \#(P_\beta\cap[Y,2Y))\ll Y^{h-g},                                  \tag{2}
\]
uniformly in \(a\). For \(\bigcup_{x\in\mathcal B}E_x\) one can put a factor \(1+\log Y\) on the right; it can be absorbed in a smaller \(g\).

The external finite-source input is [Weaver, Paper 176 v1, §5.3, equations (28)–(29)](https://rstation.ai/problems/collatz/papers/176/v1). If \(C\) is the shortcut map and \(k=\lfloor\log_2 M'\rfloor\), it gives some fixed \(\delta,\eta>0\) with
\[
 \sum_{\substack{v\ge1\ {\rm odd}\\ C^t v>M'\ (0\le t\le k+\lfloor\delta k\rfloor)}}
               v^{-2}\ll (M')^{-(2-h+\eta)} .                          \tag{3}
\]
It cites [Paper 28 v3, Theorem E, (R4) at ternary precision zero](https://rstation.ai/problems/collatz/papers/28/v3). The first paper's proof takes \(h<d<1\) and \(\delta/[(\log_3 2)(1+\delta)]<c_d\); its subsequent tail summation gives some \(\eta>0\). We need only the displayed fixed pair and can decrease \(\eta\) so it is less than \(h/4\). Equation (28) at exactly \(k\) has exponent \(2-h\) with a logarithmic factor. Neither equation is itself a bound on natural predecessor density.

Take a small \(\tau>0\) such that \(\tau(2-h+\eta)<\eta/4\), set \(M'=\lfloor Y^{1-\tau}\rfloor\) and \(T=k+\lfloor\delta k\rfloor\). Then choose \(0<\beta-\lambda<7/4-\lambda\) small enough that
\[
    (1-\lambda/\beta)(1+\delta)<\tau/2,\quad
     (\beta-\lambda)(1+\delta)<h/2.                                   \tag{4}
\]
The choices do not depend on \(a,Y,M\) or on a physical word. For a passing word of odd length \(j\) and shortcut duration \(s=S_j\le T\),
\[
     y={2^s a\over3^j}-K,\qquad
 K=\tfrac13\sum_{i=0}^{j-1}{2^{S_i}\over3^i}
       \le C_\beta (2^{\beta-\lambda})^j,\qquad S_0=0.               \tag{5}
\]
The equality is the exact forward affine recurrence with its offset expressed at the original source scale. At each \((s,j)\) the number of distinct integers in this interval is at most \(1+C_\beta 2^{(\beta-\lambda)T}\), independent of the endpoint. Summing the \(O((1+T)^2)\) pairs, including the empty path, gives a short-word bound \(O((1+\log Y)^2Y^{h/2})\). In the parent-union case, a short word ending at any such \(x\) forces \(x\le2^j y\le 2^{T+1}Y\), since \(Uu\le2u\). The direct parent formula \(x=(2^e a-1)/3\) allows \(O(1+\log Y)\) endpoints in this range, uniformly in \(a\).

For \(s>T\), any initial \(t\) shortcut decisions, \(1\le t\le T\), have at least \(t/\beta\) odd departures: the first complete gap ending at or after \(t\) already began strictly before \(t\), and its total through that gap is at most \(\beta\) times its index. Positive affine offset gives
\[
 C^t y\ \ge y\,3^{t/\beta}/2^t
       \ge Y\,2^{-(1-\lambda/\beta)T}>M'
\]
for all sufficiently large \(Y\), by (4). This includes every intermediate halving, not only odd states. Hence those very same sources from the octave occur on the left of (3). Each has \(y^{-2}\ge(2Y)^{-2}\), so their number is at most
\[
  C Y^2(M')^{-(2-h+\eta)}\ll
      Y^{h-\eta+\tau(2-h+\eta)}\le Y^{h-3\eta/4}.
\]
This proves (2), for example with \(g=\eta/2\) after increasing constants. The long-word event is independent of which eventual parent is chosen, so it is counted only once for the entire parent union. Permanently passing sources are in this same long-word event. Bounded \(Y\) can be absorbed. The present use of (3) retains the original source; applying it afresh to a conditional later orbit state would need another theorem.

## From a finite complete word to its natural cell

For \(v\) reaching \(a\), let \(L_a(v)\) be the first site passing to \(a\) on its finite path to the **first** \(a\); let it be cemetery otherwise. The site \(a\) itself qualifies. Every changed departure belongs to \(E_a\). For the disjoint parent union, label a source by the first site passing to its own designated parent \(x\), or cemetery outside the union. The exceptional set is then contained in \(\bigcup E_x\). In particular the common target \(a\) after the designated parent is not substituted as a stopping label. For the global result use \(L=F_\beta\), with exceptional set \(P_\beta\).

For each of these labels, the countable limiting law \(\nu\) satisfies the [relative sparse-passage estimate](RELATIVE_SPARSE_PASSAGE.md) with common constants, even when the chosen target varies with the test. By (2) all local exceptional-set cardinalities and relative estimates are uniform. No common union over *all* possible targets is required. If \(L(v)=y\) is finite, its bounded physical prefix from \(v\) to this \(y\) has strictly \(S_i>\beta i\) in backwards order. Indeed the finite continuation from \(y\) to the designated target passes. Any earlier site that passed to \(y\) would therefore pass to the same target. Absence of any earlier passing-to-\(y\) site is equivalent to absence of nonnegative reverse records, including ties, hence to the claimed strict inequality. In the global case use the same argument with the passing infinite continuation. The root \(y\) is itself allowed as a source.

Writing \(W_Y\) for a uniform odd input in \([Y,2Y)\), the [strict-offset physical counting argument](ORDINARY_NO_RETURN_EXPONENT.md) with \(\omega=2^{\beta-\lambda}>1\) now gives, at any sufficiently large \(y\),
\[
 \Pr(L(W_Y)=y)\ll_\beta {1+\log(2+Y)\over y}
       \quad \text{if a strict word from the octave can occur}.          \tag{6}
\]
For this event necessarily \(y\le 4Y\) for \(y>2C_\beta\): the bounded reverse offset at \(y\) and initial \(v<2Y\) give \(v>y/2\) on any positive-length strict word. This justifies replacing the individual \(1/Y\) additive terms by \(4/y\) when \(Y<y\); if the event is empty it already satisfies the bound. The aperture per \((j,S_j)\) retains its integer \(+1\) term. The atom at the empty word is also \(O(1/Y)\).

Taking \(Y=\exp(y^\epsilon)\) in the relative estimate and choosing additive order \(A>1/\epsilon\) shows, with constants uniform across all these target choices,
\[
                         \nu(\{y\})\ll_\epsilon y^{-1+\epsilon}.        \tag{7}
\]
This also applies on a path ending at a periodic target. It only counts strict finite words, without assigning a canonical \(Q\) cylinder through that cycle. Nonunit labels have zero limiting mass.

By dyadic summation of (7) with (2), retaining any \(0<\epsilon<g/4\), the total limiting mass of finite labels \(y\ge M\) is \(O(M^{-(1-h+g-\epsilon)})\). For a uniform bound on every source octave, first take \(Y\le\exp(M^\epsilon)\) and sum (6) over the same sparse possible labels \(y\ge M\). The extra logarithm costs at most \(O(M^\epsilon)\). If \(Y>\exp(M^\epsilon)\), apply the relative estimate directly to the single indicator of finite labels \(y\ge M\), with \(A\epsilon>2\); its limiting mass already has the stated power decay. Shrinking the gain leaves, for example, \(\xi=g/4\) in (1), including the harmless logarithm in the stated parent-union count.

For the single predecessor basin every source reaching \(a\) has a finite label, necessarily at least \(m_*(a)\). For the union the first label belongs to the predecessor basin of its designated parent, and so exceeds \(M\). At a nonperiodic \(a\) the natural inverse transition assigns the parent \(x\) mass \(d_x/d_a\). The disjoint union and the uniform label law justify the summed bound, including infinitely many parents; equivalently one can first take finite families with the same constants and use natural countable additivity for that inverse transition.

For the global minimum, if the complete orbit of \(v\) stays above \(M\), then, for large enough \(M\) depending only on the fixed \(\beta\), its odd prefixes satisfy
\[
         S_j\log2\le j\log(3+1/M)+\log(v/M).
\]
Because \(\log_2(3+1/M)<\beta\), the forward debt \(\beta j-S_j\) tends to \(+\infty\). Its first future minimum supplies a permanently passing site, so \(F_\beta(v)>M\). Uniform octave bounds yield the uniform law through \(X\) by dyadic summation. Stripping initial powers of two proves the forward-minimum statement for all positive starts, since their minimum is precisely the minimum of the resulting odd orbit. For the critical height and \(q^\lambda_z\), use the deterministic \(y\ge c_0z\) inclusion from [the critical note](CRITICAL_FIRST_ENTRY.md) and the strengthened sparse count (2). This completes the cited implications without any assertion of global convergence.
