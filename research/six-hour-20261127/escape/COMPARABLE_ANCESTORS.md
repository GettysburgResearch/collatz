# The all-time predecessor count at a fixed multiple of the target

Use the shortcut \(T(x)=x/2\) on even inputs and \(T(x)=(3x+1)/2\) on odd inputs. For a positive integer \(y\) let
\[
 \pi_y(Cy)=\#\{1\le x\le Cy:T^t x=y\text{ for some }t\ge0\}.
\]
The bound \(C\ge1\) is fixed. All starts and targets in this count are ordinary positive integers. There is no time or intermediate height restriction.

**Written theorem.** When \(y\) is uniform on the integers of \([X,2X)\), the law of \(\pi_y(Cy)\) converges in total variation as \(X\to\infty\). Its limit is the law, on normalized ternary Haar measure, of
\[
 N_C(v)=\#\{w:w\text{ is a finite legal reverse shortcut word at }v,\
               g(w)=3^{r(w)}/2^{|w|}\ge1/C\},                         \tag{1}
\]
including the empty word. Any fixed dyadic restriction on the target gives the same limit. A fixed ternary residue restriction gives the corresponding conditional Haar limit. In particular, for every \(1<s<2\),
\[
 {\bf E}N_C\le C^s/[1-(1+3^{s-1})/2^s].
                                                                         \tag{2}
\]
For \(K\ge1\), uniformly in \(K\) and large \(X\), the number of targets with at least \(K\) distinct starts in this window is
\[
                O_C(X/K+X^{\eta}(1+\log X)),\qquad
                \eta=H_2(3/5)<0.971 .                                 \tag{3}
\]
These are distribution and counting bounds. A vanishing fraction of targets can have a growing predecessor count, so (2) by itself supplies no convergence of untruncated ordinary first moments.

## Removing all late arrival clocks

Fix \(0<a<b\) and \(D>0\). Count terminal integers \(aX\le y\le bX\) hit by some \(1\le x\le DX\) at any shortcut time \(t>J\). With \(k=\lfloor\log_2 X\rfloor\), for large \(X\) this count is
\[
          O_{a,b,D}\bigl(X\rho^J+X^\eta(1+\log X)\bigr),\qquad
          \rho=2^{H_2(\log_3 2)-1}<1.                                 \tag{4}
\]
For \(J\le t<k\), use \(T^t(x)=3^{r_t}x/2^t+B_t\) with \(0\le B_t\le(3/2)^t-1=o(X)\), uniformly at this horizon. An endpoint at least \(aX\) forces \(r_t\ge(\log_3 2)t-O_{a,D}(1)\). Each length-\(t\) parity word takes one residue modulo \(2^t\); at most \(O_D(X/2^t)\) allowed inputs have that word. The binomial upper tail with a fixed shift is \(O_{a,D}(2^{tH_2(\log_3 2)})\), by exponential tilting at the fixed threshold. Thus **all pairs** \((x,t)\) at these clocks number \(O_{a,D}(X\rho^J)\).

For \(t\ge k\), the entire future of all source starts lies in the union of the complete positive orbits from \(T^k([1,DX])\). For every fixed \(L\) this initial image \(T^k([1,LX])\) has \(O_L(X^\eta)\) elements. Inputs with at least \(3k/5\) odd departures occupy \(O_L(2^{kH_2(3/5)})\) classes with bounded multiplicity. All other images are positive and are at most \(LX3^{3k/5}2^{-k}+(3/2)^k=O_L(X^\eta)\), since \((3/5)\log_2 3\) and \(\log_2(3/2)\) are strictly below \(\eta\).

For any finite union of \(M\) full orbits and any finite source interval \(I\), its intersection with \(I\) contains at most \(|T^k(I)|+kM\) distinct sites. To see this, add orbits one at a time, retaining their previously unseen parts. A piece ending at an old orbit is a simple finite path. A disjoint eventually periodic piece consists of a simple path followed by a cycle and a disjoint infinite orbit is simple. Remove the last at most \(k\) transient sites of every piece that has a finite transient path. The \(k\)-step map on everything retained is injective: remaining transient images stay in that same piece outside its cycle, while cycle images permute their cycle. Different pieces have disjoint images. Apply the interval image estimate also to \(I=[aX,bX]\). The set of possible late targets has \(O_{a,b,D}(X^\eta(1+\log X))\) elements. This proves (4); with \(J=0\), Markov's counting inequality for the early pairs gives (3). The orbit-union compression and the analogous transfer for the least ancestor before descent are Weaver's. Here every arrival from the source window is counted, including paths going below their source. [Paper 177/v1, §§7–8](https://rstation.ai/problems/collatz/papers/177/v1) · [Paper 180/v1, logarithmic least-arrival cutoff](https://rstation.ai/problems/collatz/papers/180/v1)

For a fixed reverse deadline \(J\) each word is legal on a single class modulo \(3^{r(w)}\), and its inverse endpoint is \(y/g(w)-c_w\) with \(c_w\ge0\). On a legal class positive ordinary inverses stay positive. Thus the test at the inclusive upper height \(Cy\) eventually selects exactly \(g(w)\ge1/C\), including equality. Different gains give coincident sources only at finitely many targets. Equal gains force equal length and odd count by unique factorization. Two different inverse words of the same length reaching the same source would contradict deterministic forward parity. The number of distinct sources at this deadline is therefore eventually a function of \(y\bmod3^J\) equal to (1) truncated at \(J\). Ternary classes equidistribute in the target octave, also inside each fixed dyadic class. Their conditional distributions give the version with a ternary restriction.

A length-\(t\) word with \(r\) odd inverse letters has legal Haar mass \(3^{-r}\). Summing \(g^s\) times that mass over words gives \([(1+3^{s-1})/2^s]^t\). This ratio is less than one for \(1<s<2\), by strict convexity of \(\log(1+3^{s-1})-s\log2\) and equality at the two endpoints. The probability of any omitted word is bounded by summing this geometric sequence beyond \(J\) times \(C^s\). Formula (4) bounds the probability of any omitted ordinary arrival, first letting \(X\to\infty\) at fixed \(J\). Letting \(J\to\infty\) proves the claimed total-variation limit and (2).

## Uniformly few local entrants on protected growing prefixes

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers. Fix \(C\ge1\). There is an absolute-in-the-word integer \(K(C)\) with the following property. For **every fixed** finite exponent word \(w\) in \(\{1,2\}\) starting with 1 and having no consecutive twos, write \(n=|w|\), \(A=\sum w_i\). Among positive integers \(x\) with this exact odd word and \(x\equiv1\bmod3^{128}\), a relative natural density at least \(0.98\) has both properties
\[
 \begin{split}
 &\text{the least positive ancestor of }U^n(x)\text{ is }x,\\
 &\#\{1\le u\le Cx:T^j u=U^n(x)\text{ for some }j\ge0\}\le K(C).
 \end{split}                                                         \tag{5}
\]
Every meeting with any earlier shortcut or odd prefix site continues to the same final target. Both visitor clocks in (5) are unrestricted. The forward word is finite before the natural density is taken. The modulus makes both the starts and the terminal odd state units modulo three. Under the fixed-target basin and fixed-shift fusion results used in the [earlier unrestricted-visitor theorem](UNRESTRICTED_VISITORS.md), a positive lower natural density of these ordinary sources also reaches 1.

We give the source conditioning details. An exact \(h\)-step odd inverse word with total exponent \(F\) has gain \(3^h/2^F\) and legal Haar mass \(3^{-h}\). The stopped gain bound \(\Pr(\sup_R g_R>a)\le a^{-2}\) for \(a\ge1\) follows by paying each first strict crossing with its prefix-free word mass \(3^h4^{-F}\). Take the source ternary coordinate \(v\) uniform in \(1+3^{128}\mathbb Z_3\). For \(d=0\) use the sole offset \(c=0\); for \(d\ge1\) include all positive odd \(c\le5(2^d-1)\). We impose
\[
                    G(2^dv+c)\le2^d\quad\text{for every }(d,c).       \tag{6}
\]
At the ordinary anchor \(b=2^d+c\) a strict violation before or at \(k=128\) is impossible. For \(d=0\), the target is 1 and every positive odd ancestor \(u\) has \(g u\le1\). For \(d\ge1\), a strict violation would imply \(u<b/2^d<6\). The complete odd trajectories of \(1,3,5\) have gain at most \(3/2<2^d\). Legality through these \(k\) inverses is identical throughout the source ball.

At depth \(k\) each legal word from \(b\) corresponds to one positive \(u\) with \(U^k u=b\). Its terminal when started at \(2^dv+c\) is Haar-uniform because its multiplier on \((v-1)/3^k\) is a ternary unit. The stopped bound pays \(4^{-d}g_k(u)^2\) for any subsequent violation. For each \(u\) only \(b=U^k u\) occurs. At \(d\ge1\) its possible weights sum to at most \(48/b^2\), by the geometric series starting at \(2^d\ge b/6\). Include the possible \(d=0,b=1\) and use \(g_k(u)u\le b\) to bound the total by \(49/u^2\). All odd \(u\le4095\) reach 1 within 87 odd steps by the [existing kernel audit](VisitorAnchor.lean); for those starts only \(b=1,d=0\) contributes and \(g_k(u)\le (3/4)^{41}/u\). A decreasing integral over the step-two grid gives \(\sum_{u>4095,\ u\ \mathrm{odd}}u^{-2}\le1/(2\cdot4095)\). The relative probability of any failure of (6) is at most
\[
                  2(3/4)^{82}+49/8190<1/100.                         \tag{7}
\]

On (6) the prescribed word is the unique maximum-gain prehistory of its terminal. Indeed the no-consecutive-twos division theorem and inverse affine cone give the intermediate source \(2^d v+c\) after the final \(n\) inverse odd steps, with \(d,c\) as above and relative gain \(2^{-d}\). The case \(d=0\) uses the prescribed word itself. Every shorter competitor is bounded by the gain of a suffix of the same length; the omitted prefix has gain strictly above one. Unique factorization excludes ties at different odd lengths, and at equal length the cone excludes all ties with \(d>0\). This is the same finite-word comparison as in the [earlier source-zero ball](UNRESTRICTED_VISITORS.md), now on a ball of units. [Weaver, Paper 1/v3, Lemma 1 and Theorem 2](https://rstation.ai/problems/collatz/papers/1/v3)

We need a count in addition to a maximum. On the whole ternary source space define \(Z_C(v)\) to count every pair consisting of one of the displayed \((d,c)\) and an arbitrary finite legal odd inverse word \(R\) at \(2^d v+c\) with \(g_R\ge 2^d/C\). The empty word is included. Under unconditional law the coordinate \(2^dv+c\) is Haar-uniform. Put \(s=3/2,\ \sigma=3^{s-1}/(2^s-1)<1\). At a given odd depth \(h\) the legal Haar integral of the sum of \(g_R^s\) is \(\sigma^h\), by summing each \(e\ge1\) independently. Therefore
\[
 {\bf E} Z_C\le
   {C^{3/2}\over1-\sigma}\left(1+5\sum_{d\ge1}2^{-d/2}\right)=:M_C .
\]
Conditional on the fixed source ball the expectation is at most \(3^{128}M_C\). With \(K_0(C)=\lceil200\cdot3^{128}M_C\rceil\), the joint probability of (6) and \(Z_C(v)\le K_0(C)\) exceeds \(0.98\), uniformly over all scripts and lengths.

To compare with actual sources, first truncate the total visitor shortcut length at a fixed \(J\). A candidate positive odd visitor with at least \(n\) odd steps before hitting the terminal first runs some \(R\) forward to \(2^d x+c\); its source is \((2^d x+c)/g_R-c_R\). For each fixed candidate through clock \(J\), the condition that it is at most \(Cx\) for arbitrarily large \(x\) forces \(g_R\ge2^d/C\). Thus across these finitely many possibilities every such visitor for large \(x\) is counted in \(Z_C(v)\); distinct sources require different triples \((d,c,R)\). For a visitor of \(h<n\) odd steps, put \(i=n-h\). The same division-minimality theorem on the suffix gives its source as \(2^dU^i(x)+c\) with \(d\ge0,\ 0\le c\le7\cdot2^d\). The upper bound follows from the exact affine carry sum and \(A_j\le(3j+1)/2\) even when the suffix starts with 2; the nonnegative correction follows from minimality on every suffix. The original prefix, which starts with 1, gives \(U^i(x)\ge(3/\sqrt8)^i x\). Affordability forces \(i\le I=\lfloor\log C/\log(3/\sqrt8)\rfloor\) and \(d\le D=\lfloor\log_2 C\rfloor\). There are at most \((I+1)\sum_{d=0}^D(7\cdot2^d+1)\) possible triples \((i,d,c)\). All gains and affordability comparisons at deadline \(J\) are eventually fixed on finitely many ternary classes once the actual dyadic word is fixed. On the uniquely maximizing classes the prescribed positive source is the least for sufficiently large targets. Conditional Haar proportions therefore bound the lower relative natural density of this joint finite-clock event by \(0.98\).

Take \(J\) at least the prescribed total shortcut cost. Every even visitor has an odd part that also hits the odd target. At the finite cutoff this odd part cannot be smaller than \(x\) under the no-smaller-visitor condition, so there are at most \(1+D\) possible doublings per odd visitor. The product of \(1+D\) with the sum of the preceding two odd bounds gives \(K(C)\), independent of \(w\). Finally, when \(X\le x<2X\), the target \(U^n(x)\) lies between two fixed positive multiples of \(X\), and different \(x\) in the word cylinder give different targets. Any new visitor beyond \(J\) with start at most \(Cx\) is covered by (4), with constants depending on the fixed \(w,C\). Dividing by the positive cylinder density \(2^{-A-1}3^{-128}\), first send \(X\to\infty\), then \(J\to\infty\). The same truncation makes the full event approximable in upper natural density of symmetric differences by periodic sets, establishing existence of the stated density and the fixed-shift basin intersection.

## What local amplification would need

Wren's fixed-target lower bound is \(\pi_y(X)\ge cX/y\) for every unit target \(y\) and \(X\ge y\), with the averaged joint-mixing hypothesis supplied by its cited sources. At \(X=Cy\) this is constant order. Formulae (1)–(5) give ordinary positive controls at exactly that scale, even on arbitrarily long growing, no-smaller-visitor prefixes. On a genuine least bad source a lower bound on **all** bad vertices in its octave could use mergers occurring arbitrarily far along that single source's actual future. Taking a different physical source for each prescribed word cannot supply or contradict such a component-specific lower bound. [Wren, Paper 10/v3, Theorem 1](https://rstation.ai/problems/collatz/papers/10/v3)

If a fixed unit \(a\) actually escapes, every sufficiently late orbit point \(y=T^t a\) has \(\pi_y(y)\ge\pi_a(y)\ge cy/a\) by forward continuation. Thus all sufficiently high points on its ray belong to the exceptional targets in (3) with linear local multiplicity. This is compatible with their zero density; it specifies what the generic count misses. The [rational source sector](RATIONAL_SOURCE_SECTOR.md) needs bulk occupation of a bad component near its **least** height to defeat its scalar tail. Summing fixed-target counts along one ordered ray counts nested sets. Formula (5) gives no uniform abundance there.

Paper 227 supplies many directed crossings for each fixed admissible affine comparison, then derives arbitrarily low-price routes without a height bound on its subpower catalogue. Paper 232, building on 228, gives height at most \(6m+2\) with all cofactors \(9q\le8m+1\) when arbitrary selected cofactors are available. At a fixed linear height its catalogue must have positive lower density, and its charged implications remain open. The known branch comparison by itself gives no source of \(m^{0.95}\) distinct **ordinary orbit vertices** at the least bad component's scale. [Paper 227/v1, §§2–3](https://rstation.ai/problems/collatz/papers/227/v1) · [Paper 232/v1, Theorems 1–2](https://rstation.ai/problems/collatz/papers/232/v1)


The [kernel interfaces](ComparableAncestors.lean) check the finite discard-and-image inequality, the native shortcut terminal stride, the source-to-terminal mass cancellation, the finite crowded-target count, a translation-disagreement inequality and the unit-anchor budget. They do not formalize the distributional or all-time propositions. The [finite replay](check_comparable_ancestors.py) traces all ordinary starts through 24573 to 1, giving complete predecessor counts through \(3y\) for \(4096\le y<8192\); it separately checks every depth-seven ternary class and explicit positive unit-ball lifts of every eligible word through length seven at the displayed visitor deadlines. [Retained exact control](COMPARABLE_CONTROLS.json) · [Protected windows inside one supplied component](PROTECTED_COMPONENT_WINDOWS.md)
