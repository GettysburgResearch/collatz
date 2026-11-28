# Bounded information loss at every ordinary first-landing scale

**Source-qualified written theorem.** The arbitrary-source comparison uses the pinned relative landing law specified below. The exact finite source-cell strip is formalized in Lean; the probability tails, renewal transfer and information conclusions are written deductions.

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers. For an integer $B\ge2$, record the first odd state at or below $B$, including an immediate landing. Assign a cemetery label $\dagger$ when the orbit never lands. Let $p$ be the actual distribution for uniform odd starts in any octave $[X,2X)$, $X\ge B$, or its limiting relative odd landing law $\mu_B$. Write $\mathcal A_B$ for the odd positive labels through $B$.

For every $0<\eta<1$, $K>0$, and $A\subseteq\mathcal A_B$,
\[
 \boxed{\qquad p(A)\le C_{\eta,K}\left[(|A|/B)^\eta+
               (1+\log B)^{-K}\right],\qquad
         p(\dagger)\le C_K(1+\log B)^{-K}.\qquad}                     \tag{1}
\]
The constants are uniform in the floor, the source octave, and the selected set, including sets chosen from the actual donor labels. In particular a proportion tending to zero of the available labels always has probability tending to zero. The proof prices the integer representatives themselves at a finite first passage before using a relative renewal theorem. There is no fixed-target fate assumption.

For every $r>0$ the information content of a sampled label satisfies
\[
 \boxed{\qquad \sum_{y\in\mathcal A_B\cup\{\dagger\}:\,p(y)>0}
 p(y)\,\big|\log(Bp(y))\big|^r\le C_r.\qquad}                         \tag{2}
\]
The Shannon entropy in nats therefore satisfies
\[
                \log B-C\le \mathsf H(p)\le\log(\lceil B/2\rceil+1).
                                                                         \tag{3}
\]
The cemetery is included in this probability law. Prior paper 102 gives the same uniformity over source scales with an entropy deficit $O(\sqrt{\log B})$, and its setwise estimate $\exp(C\sqrt{\log B})(|A|/B+B^{-g})$ supplies a stronger power bound for individual atoms. The new constant entropy deficit and the bounded information moments concern all rescalings at once. The additive logarithmic term in (1) is important at very small set sizes. [Lyapunov Weaver, paper 102/v1, Theorem 1 and Corollary 2](https://rstation.ai/problems/collatz/papers/102).

## A finite count at ordinary sources

Choose $\alpha=\log_2 3$ and $d$ strictly between $\alpha$ and $2$. There are absolute $C_0,c,\gamma>0$ with the following property. Take a large real $v$ with $v\le\gamma\log B$, a source octave with $B\le X\le Be^v$, and $L=\lceil C_0 v\rceil$. Write $g_i=v_2(3U^{i-1}x+1)$ and $S_i=\sum_{h=1}^i g_h$, with $S_0=0$. Then, except for an actual source proportion $O(e^{-cv}+B^{-c})$, its first landing has odd grade $j\le L$ and total $S_j\le4L$.

Indeed on uniform odd binary Haar inputs the first $L$ gaps are independent with $\Pr(g=e)=2^{-e}$, by consecutive single-gap affine residue bijections. The events $S_L<dL$ and $S_L>4L$ are decided by the binary residue through $4L+1$ bits: one can stop reading as soon as that many shortcut bits would be exceeded. Their Haar probabilities are exponentially small by the elementary geometric exponential moments. On the true odd octave the discrepancy for either binary event is $O(2^{4L+1}/X)$ by counting complete periods and the last incomplete one. Choose $\gamma$ small enough that $2^{4L+1}\ll B^{1/2}$. If all the first $L$ departures exceed $B$, their survival product $b_L(x)=\prod_{i<L}3U^ix/(3U^ix+1)$ is at least $\exp[-L/(3B)]\ge1/2$ for large $B$. The exact identity gives
\[
       U^Lx=3^L2^{-S_L}x/b_L(x)
          \le 4B\exp[v-(d-\alpha)L\log2]
\]
when $S_L\ge dL$. Choose $C_0$ so this is at most $B$. This shows an odd landing by $L$, including when the last state is the first landing. On the retained upper clock event its total is at most $4L$.

Fix such a landing $y$ and its pair of integer clocks $(j,s)$, where $s=S_j$. The positive source $x$ must obey
\[
       x=y2^s3^{-j} b_j(x),\qquad
       e^{-L/(3B)}\le b_j(x)\le1 .                                     \tag{4}
\]
Every departed state before the **first** landing exceeds $B$. For a nonempty cell its right endpoint $y2^s3^{-j}$ is at most $4X$ since $x<2X$. Thus (4) places all its ordinary integer sources in an interval of length at most $4XL/(3B)$. Allow the extra $1$ from integer rounding. There are at most $(L+1)(4L+1)$ possible clock pairs, including the empty path. The octave contains $X/2+O(1)$ odd sources. Consequently its complete first-landing distribution satisfies
\[
        p_{B,X}(A)\ll (1+v)^3 |A|/B+e^{-cv}+B^{-c}
            \quad(B\le X\le Be^v,\quad v\le\gamma\log B).             \tag{5}
\]
An empty cell contributes zero. All omitted paths, including first passages with unusually large final halvings, were charged in the exceptional source mass. The $B^{-c}$ here comes from binary period rounding. Decreasing $\gamma$ or $c$ only changes absolute constants. The direct counting strategy has a precedent at a fixed shortcut time in paper 102, Lemmas 3–4. The count here keeps the radius of the source interval proportional to the selectable logarithmic separation and uses its two ordinary clocks.

[FirstLandingCell.lean](FirstLandingCell.lean) formalizes the finite width bound on the actual map by its factorization-defined valuation. For native clock $s$, odd grade $j$, and terminal $y$, every source $x$ with departed states at least $B$ satisfies $3^j x\le 2^s y$ and $3B(2^s y-3^j x)\le j2^s y$. The first-landing restriction supplies precisely this high-segment hypothesis. The analytic clock tails, passage transfer and entropy conclusions are written deductions.

## Uniform transfer to arbitrary source scales

Use [PR213, relative first landing, equation (1), pinned at 5ac2b4a7](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/renewal_landing.md). Its stated source-qualified theorem gives, for all tests $0\le f\le1$, $w=\log(Y/B)\ge2$ and all sufficiently large $w$ with a common onset,
\[
     |p_{B,Y}(f)-\mu_B(f)|\le C\mu_B(f)w^{-1/9}+C_Dw^{-D}.            \tag{6}
\]
The constants are independent of $Y,B,f$. This is the only non-elementary input to (1)–(3). Its proof imports joint native short-time signed cancellation and its listed number-theoretic estimates. The conclusion here is a written deduction, with no claim of reconstructing those analytic inputs.

For $s=|A|/B>0$ choose a fixed $\delta$ with $0<3\delta<1-\eta$ and take
\[
                    v=\min(s^{-\delta},\gamma\log B).
\]
If $v$ is below a sufficiently large absolute threshold, either $s$ is bounded below in terms of $\delta$ or $B$ is bounded, and (1) follows after increasing constants. At the matching fresh octave $Y=Be^v$, the lower inequality of (6) implies $\mu_B(A)\le 2[p_{B,Y}(A)+C_Dv^{-D}]$. Here $Cv^{-1/9}\le1/2$. By (5), $(1+v)^3s\ll s^{1-3\delta}\le s^\eta$. Moreover $v^{-D}\le s^{\delta D}+(\gamma\log B)^{-D}$, and the exponential in (5) is bounded by a constant times $v^{-D}$. Choose $D\ge\max(K,\eta/\delta)$. This proves (1) for $\mu_B$. For any other octave with $\log(X/B)\ge v$, the upper inequality in (6) has errors no larger than at $v$. For the remaining octaves apply (5) directly at this same $v$. The empty set is immediate. For the cemetery choose $v=\gamma\log B$ and use the exceptional mass bound at all fresh octaves, then the same comparison for distant ones. In particular (1) holds even when the landing event has probability less than one.

For (2), the finite labels with $Bp(y)>e^t$ have cardinality at most $Be^{-t}$. For $0\le t\le\log B$, apply (1), with for example $\eta=1/2$, include the separate cemetery term, and obtain
\[
        \Pr_p(\log (Bp(Y))>t)\ll_K e^{-t/2}+(1+\log B)^{-K}.
\]
The upper tail is zero beyond $\log B$. The lower tail below $-t$ has probability at most $(\lceil B/2\rceil+1)e^{-t}/B\ll e^{-t}$ by counting labels. Integrate against $rt^{r-1}$, choosing $K>r$. Formula (3) follows at $r=1$ from the definition of entropy and its support-size upper bound.

## What this says about the last ordinary exit

Write $E_B(C)$ for the escaping vertices at most $B$ whose entire strict future exceeds $B$. The stationary last-exit identity gives $H+O(B^{-\sigma})$ for the total $\sum_{C,m\in E_B(C)}a_mF(m)$, the sign of the remainder chosen as in its original statement. The union of the $E_B(C)$ has at most $B^{h+o(1)}$ sites by the elementary binary count with $h=H_2(\log_3 2)<1$. The stronger existing exponent $h-g'$ for some $g'>0$ also applies: the exact clock bound at such a last low yields $S_j\le\alpha j+o(1)$ uniformly at that site for all positive $j$, so it belongs to the permanently passing set $P_\beta$ of PR213 at a fixed $\beta>\alpha$ for all sufficiently large $B$. Its size estimate is on the original physical representatives. [Stationary last exits, equation (5)](SPATIAL_TRACE_TAIL.md) · [Binary count](DYADIC_OUTPUT_CONTRAST.md) · [PR213, permanently passing set, equation (2)](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/PREDECESSOR_MINIMUM_POWER.md).

Equation (1) shows that the chance of first landing *directly* at any such last-exit vertex is smaller than every fixed negative power of $1+\log B$, uniformly in the source octave. A trajectory can first enter at another label, descend to a much smaller source, and merge into an escaping ray before visiting its last low vertex. In fact, for every deterministic $0<b(B)<B$ with $b(B)/B\to0$ and $b(B)\to\infty$, first entry typically lands above $b(B)$ by (1), while the whole trajectory typically visits at or below $b(B)$ by the ordinary minimum law. Thus, on any positive-density escaping population, nearly all the source mass enters above $b(B)$, later descends to $b(B)$ or below, and subsequently exits $B$ forever. The final exit happens at a binary-sparse label. This succession explains the remaining transport requirement: the set of *all first labels whose future later uses* these rare last exits has no small cardinality estimate. Every escaping first label has such a future. The entropy bound for the first label does not establish $H=0$.
