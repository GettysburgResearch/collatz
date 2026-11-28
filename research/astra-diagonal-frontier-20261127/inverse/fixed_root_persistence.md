# Sharp persistence exponents at each supplied positive root

For a positive odd ternary unit $a$ use the strict physical word weights $W_\epsilon(a,n)$ of the [Brownian reserve theorem](brownian_reserve.md). Under its averaged joint Syracuse mixing input (J) and the stated ordinary trace inputs, at **every fixed such integer**,
\[
       W_0(a,n)=n^{-1/2+o(1)} .                                      \tag{1}
\]
Let $q_\epsilon^h(a)$ be the canonical probability that $S_j>(2-\epsilon)j$ at every positive odd inverse time, on the actual tree of that root. Then
\[
       q_\epsilon^h(a)=\epsilon^{1+o(1)}\qquad(\epsilon\downarrow0).
                                                                         \tag{2}
\]
The same exponent holds for the natural probability $q_\epsilon(a)$ at every fixed nonperiodic $a$. The exponents in (1) and (2) resolve the order at an individually supplied root, beyond the moving-root upper bounds from Haar averaging. Equation (1) concerns the unnormalized finite-word sum. Equation (2) concerns infinite-time survival with a strictly subcritical slope.

## An upper comparison without a discarded path class

Fix $0<\gamma<1/4$ and put $m=\lceil n^\gamma\rceil$. Consider the test
\[
              D_p+\epsilon p\ge0,\qquad m\le p\le\lfloor n/2\rfloor ,
                    \qquad 0\le\epsilon\le n^{-1/2}.                 \tag{3}
\]
Relaxing strictness here gives an upper bound. Work first at any padded precision $j\ge n$, starting at $Q=\lfloor n^{\gamma/10}\rfloor$. In the proof of (3) of the [upper functional law](functional_upper.md), take $\ell=\lfloor n^{\gamma/8}\rfloor$ and the numerical switch tolerance $b=n^{\gamma/3}$. Thus $Q^2=o(b)$, $b=o(\sqrt m)$, and $\ell=o(m)$. At each precision $x\ge Q$ retain only the lower-prefix constraint $S_d\ge1.9d$ at $d=\lfloor0.9x\rfloor$, in addition to the previously exposed lower constraints. At the final precision include the full test (3). A genuine path surviving the slope $2-\epsilon$ all the way to $j$ satisfies every lower constraint as soon as $\epsilon\le1/10$.

In the physical counting inequality (2) of the upper functional law, split each exposed prefix into $1.9d\le S_d\le20d$ and $S_d>20d$. For the former the number of totals is $O(d)$ and $\omega3^{x+1-d}\le1$, giving the same bound $a+1$ per group. For the latter, the entire subdensity at either of the two precisions is bounded by $3^{x+1}\Pr_0(S_d>20d)$, even after arbitrary other checks, since later conditional probabilities are bounded by one. With fair geometric letters the moment at $\log(3/2)$ is three, and this bound is at most $e^{-cd}$ for an absolute $c>0$. The sum over all lifts or switches of these errors is $O_B(n^{-B})$ for every $B$.

At each date $p$, start with its centered sum at $p+2\ell$, using the original constant $\epsilon p$ and a slack $b$. Switch to its true date at precision $p+\ell$ and remove its own slack. Any newly admitted word must then have $|D_{p+2\ell}-D_p|>b$. At each lift every check inside the exposed prefix is a Boolean requirement comparing the integer value at its actual date and its specified constant. Discard all prefixes failing one such test. For the others the residual conjunction depends only on $S_d$ and the deterministic remaining tests. In particular there is no grouping by nonintegral barrier heights or by the number of past tests.

For $x\in[m/2,2n]$, the residual past/future gap in Paper 211 (A.6) is at least $\ell$ at each lift. There are $O(n)$ lifts, each with $O(n)$ relevant prefix totals. Thus the total signed lift error is $O((a+1)n^2J_{b'}\ell^{-b'})$ for any chosen mixing order $b'>0$, where $J_{b'}$ denotes its mixing constant. Outside this range there are only future marks, or the entire test has been resolved inside the exposed prefix; the error is at most $O((a+1)J_{b'}10^{b'}\sum_{x\ge Q}(x+1)^{1-b'})$. Switch failures have fair mean at most $2\exp[-\min(b^2/(24\ell),b/8)]$ and cost $O((a+1)n^2)$ times that mean in total. Each exposure deletes nonnegative mass, as required for an upper estimate. These bounds give $O_{\gamma,B}((a+1)n^{-B})$ uniformly in all $j\ge n$, after choosing $b'$ sufficiently large.

The starting projected density at $a$ is at most $\rho_Q(a)\le C h(a)$, with the absolute comparison in Paper 12 (26). Its part with $S_Q>Q^2$ is $O_B(n^{-B})$. On the remainder resampling the first $Q$ fair letters and undoing their initial date shifts costs at most another $O(b)$ in each test, outside a fair probability $O_{\gamma,B}(n^{-B})$. All following letters at this starting precision really are independent. We conclude that the resulting terminal density at $a$ is at most
\[
 C h(a)\Pr_0\{D_p+\epsilon p\ge-Cb,\quad m\le p\le\lfloor n/2\rfloor\}
                  +O_{\gamma,B}((1+a+h(a))n^{-B}).                 \tag{4}
\]
The projection and weight here are $3^j$ times the raw residue probability, as in the upper functional law.

## A short fair-walk estimate at small drift

Let $L=\lfloor n/2\rfloor-m$, and allow a deterministic starting reserve $s\ge0$. For the centered fair geometric walk $D'_k$ from zero, there is an absolute $C$ such that, uniformly in $0\le\epsilon\le n^{-1/2}$ and large $n$,
\[
 \Pr_0\{s+D'_k+\epsilon k\ge0,\ 1\le k\le L\}
 \le C(s+1)\log n/\sqrt n+\exp[-c(\log n)^2].                     \tag{5}
\]
For an upper bound increase the drift to $\eta=n^{-1/2}$. There is a positive $r\asymp\eta$ such that $\mathbb E e^{-r(e-2+\eta)}=1$, using strict convexity, the negative possible increment and $\log\mathbb E e^{-r(e-2)}=r^2+O(r^3)$. Choose $H=\sqrt n/\log n$. From any start $s\in[0,H)$ stop at the first visit below zero or to $[H,\infty)$. The lower overshoot is at most one. The stopped exponential martingale is bounded by $e^r$, and the stopping time is almost surely finite because independent blocks of length $\lceil H^2\rceil$ each have a fixed positive probability of net upward movement greater than $H$. The latter follows already at zero drift from the ordinary central limit theorem.

If $P_\uparrow$ is the probability of exiting above, the stopped expectation therefore obeys $e^{-rs}\le(1-P_\uparrow)e^r+P_\uparrow e^{-rH}$. Since $rH\le1$ for large $n$, it gives $P_\uparrow\le C(s+1)/H$. The probability of no exit by $L$ is at most $(1-c_0)^{\lfloor L/\lceil H^2\rceil\rfloor}$ by the same independent block estimate. For $s\ge H$ the right side of (5) can be taken at least one. This proves (5).

At the first monitored time $m$, the reserve in (4) is $D_m+\epsilon m+Cb$; discard the paths where it is negative and bound its positive-part expectation by $\sqrt{2m}+\epsilon m+Cb$. The independent future letters then allow (5). Thus (4) is at most
\[
 C h(a)(1+\sqrt m+\epsilon m+b)\log n/\sqrt n
                        +O_{\gamma,B}((1+a+h(a))n^{-B}).            \tag{6}
\]

## Returning to the physical words

For (1), take $\epsilon=0$ and $j=n$. Every genuinely critical word passes all lower constraints and (3); including terminal nonunits in the upper density only enlarges it. Equation (6) gives $W_0(a,n)\ll_{a,\delta}n^{-1/2+\delta}$ for every $\delta>0$ by choosing $\gamma$ small. The uniform raw-word lower bound in the Brownian reserve theorem gives the other exponent.

For (2), set $n=\lfloor\epsilon^{-2}\rfloor$, so $\epsilon\le n^{-1/2}$. Genuine infinite survival guarantees the lower constraints at arbitrarily large padded precisions. As in Paper 12 (29), on this full event multiply by $\rho_1(X_j)/h(X_j)$, bounded in expectation by $2/h(a)$ times the terminal density (6), and Cesàro average over $j$. This proves, for every $\delta,B>0$ with absolute-in-$a$ constants depending on those parameters and the stated inputs,
\[
 q_\epsilon^h(a)\le C_\delta\epsilon^{1-\delta}
                +C_{\delta,B}\big(1+(1+a)/h(a)\big)\epsilon^B.       \tag{7}
\]
In particular the upper exponent holds on every supplied unit. The matching canonical lower follows from the strict finite-word lower estimate $\liminf_{j\to\infty}\inf_a W_\epsilon(a,j)\ge c_\delta\epsilon^{1+\delta}$ and $h\ge\alpha$ at every endpoint. Indeed the canonical probability of each finite survival event is at least $\alpha W_\epsilon(a,j)/h(a)$; these events decrease to infinite survival. At fixed nonperiodic $a$ the bounded equivalence of the entire path laws gives the same exponent for $Q_a$, also using the natural lower bound proved in the Brownian reserve theorem.

For the canonical **finite-time** critical probability the original event permits unrestricted future prefixes after $n$. That event does not by itself supply the padded lower constraints in the proof of (7). The raw finite-word limit and the infinite-time probability limit above are the two conclusions.
