# Positive Rényi moments of the actual first-landing rows

**Source-qualified written theorem.** The inputs are Weaver's ordinary certified-source count and PR213's relative first-landing estimate. Their combination controls the unsmoothed discrete probabilities at every floor and every true source octave. The stationary profile used for the limiting constant is the one constructed in the earlier packet.

For an integer floor $B\ge2$ let $p$ be either the odd-relative limiting first-landing law $\mu_B$ or the first-landing law from the uniform odd integers in any $[X,2X)$ with $X\ge B$. The positive odd labels are the first states at or below $B$ and $\dagger$ denotes a failed passage. Define
\[
 g=1-H_2(\log_3 2)+1/351,\qquad g=0.05289\ldots .
\]
For every $0<\eta<1$, uniformly in the floor, source, and arbitrary set of finite labels $A$,
\[
 p(A)\le C_\eta (|A|/B+B^{-g})^\eta,\qquad
 p(\dagger)\le C_\eta B^{-g\eta}.                                   \tag{1}
\]
For every $0<q<g/(1-g)$, including the cemetery in the sum, one has
\[
              \sup_{B,p} B^q\sum_y p(y)^{1+q}<\infty .                \tag{2}
\]
Moreover for $p=\mu_B$ as $B\to\infty$ or for any sequence of actual octaves with $B\to\infty$ and $X/B\to\infty$,
\[
          (B/2)^q\sum_y p(y)^{1+q}
           \longrightarrow \int_{[0,1]\times\mathbb Z_3} G^{1+q}
                                  \,du\,d\lambda_3 .                   \tag{3}
\]
Here $G$ is the normalized physical and ternary first-landing density, with $du$ on $[0,1]$ and normalized ternary Haar measure. Thus the Rényi entropy at order $1+q$ has constant correction $-q^{-1}\log\int G^{1+q}$ to $\log(B/2)$. The result concerns the original labelled laws before any binning or deletion of exceptional mass. No fate of any ordinary integer is required.

## Two complementary ordinary counts

Weaver's Paper 102, Lemma 4, counts the full shell $[2^K,2^{K+1})$ with a fixed shortcut landing label in $(B/2,B]$. The odd part gives a bijection between this band and the odd labels through $B$. Equation (16), or the smooth comparison in (19) with its domination of ordinary octaves, gives
\[
 p_{B,X}(A)\le C(1+\log X)(1+\log B)^2(|A|/B+B^{-g}).                \tag{4}
\]
The cemetery satisfies this with $|A|=0$. For a direct octave deduction split the octave into at most two binary shells, retaining only starting values above $B$; immediate landings contribute $O(|A|/B)$. The same proof supplies a second input used for the real fibres below: on odd $y\in(2^{n-1},2^n]$, except for $O((1+n)^3 2^{(1-g)n})$ labels, the first crossing of $2^{n-1}$ uses at most $Cn$ native shortcut steps. Indeed Lemma 3 bounds the certified clock by $H_n=O(n)$, while the proof of Lemma 4, equation (18) and its initially bad sources, counts every uncertified path whether it eventually lands or fails. Passing to the odd part after the crossing adds only even steps, so the same upper bound holds for the odd grade to the first odd landing. Endpoints can be included at a cost of one source. [Weaver, Paper 102, Lemmas 3–4 and equations (16)–(19)](https://rstation.ai/problems/collatz/papers/102).

The earlier packet supplies uniform bounds $p(A)\ll_{\eta,K}(|A|/B)^\eta+(1+\log B)^{-K}$ and $p(\dagger)\ll_K(1+\log B)^{-K}$. The imported relative comparison, at a log separation $u=\log(X/B)$ with sufficiently large absolute onset, gives $|p_{B,X}(A)-\mu_B(A)|\le C\mu_B(A)u^{-1/9}+C_Du^{-D}$ for every $D>0$, uniformly in $B,X,A$ and likewise for the cemetery. [Earlier direct clock-cell count and its transfer](FIRST_LANDING_ENTROPY.md) · [PR213, relative landing estimate, pinned equation (1)](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/renewal_landing.md).

Put $x=|A|/B+B^{-g}$, with $x=B^{-g}$ for the cemetery. Values $x$ bounded below need only a constant. Fix $\delta=(1-\eta)/4$. If $x\ge(1+\log B)^{-1/\delta}$, the previous packet's estimate with $K\ge\eta/\delta$ yields (1). Otherwise let $v=x^{-\delta}>1+\log B$. For every $B\le X\le Be^v$, (4) is at most $Cv^3x=Cx^{1-3\delta}$. Comparing the matching octave $Be^v$ with $\mu_B$, the relative error is absorbed once $Cv^{-1/9}\le1/2$, and the additive error is at most $C_Dx^\eta$ for $D\ge\eta/\delta$. The bounded remaining $v$ cost a constant. This proves (1) for the limiting law. At every larger source separation the upper relative error and additive remainder cost at most constants times this same bound. This proves (1) at every source height.

## Uncropped moment and limiting constant

For $t\ge1$ put $A_t=\{y\ne\dagger:Bp(y)>t\}$ and $m=p(A_t)$. Then $|A_t|/B\le m/t$. From (1),
\[
             m\le C_\eta(m/t)^\eta+C_\eta B^{-g\eta}.
\]
If $m$ exceeds twice the second term, rearrange the first one. Including the cemetery and separately testing on singletons gives
\[
 \Pr_p(Bp(Y)>t)\le C_\eta t^{-\eta/(1-\eta)}+C_\eta B^{-g\eta},
 \qquad \max_y Bp(y)\le C_\eta B^{1-g\eta}.                          \tag{5}
\]
Choose $\eta$ close enough to one that $q<\eta/(1-\eta)$ and $q(1-g\eta)<g\eta$. Integrate (5) against $qt^{q-1}$ up to the displayed maximum, and (2) follows. In particular the cemetery term $B^q p(\dagger)^{1+q}$ tends to zero for this choice.

On the finite grid put $f_B(y)=(B/2)p(y)$, using grid measure $2/B$ per odd integer. For a larger $q'$ still in the open range of (2), the $1+q'$ grid moments are bounded uniformly. This makes $f_B^{1+q}$ uniformly integrable. The local profile theorem gives, to each requested $L^1$ accuracy, a bounded fixed interval-and-ternary-cylinder template for $G$ whose samples approximate $f_B$ in discrete $L^1$ at that accuracy along every sequence in (3). Approximate $z^{1+q}$ by a bounded Lipschitz truncation on $[0,\infty)$ vanishing at zero, first use the grid $L^1$ comparison and the fixed-template Riemann limit, and next take the limiting template in $L^1$. Finally remove the truncation using the discrete bound with $q'$ and the earlier $G\in L^{1+q'}$. This yields (3) with the displayed factor of two. [Original-label profile, equation (1)](LOCAL_LANDING_PROFILE.md).
