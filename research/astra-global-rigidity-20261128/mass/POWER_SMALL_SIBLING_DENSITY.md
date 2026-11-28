# Polynomially small basin gains on logarithmically long ordinary climbs

Write \(c=3/2\), \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers, and \(d(x)\) for the natural density of all positive starts whose shortcut orbit visits \(x\). For an odd target it equals its relative density among odd sources under \(U\), by stripping the initial powers of two.

**Theorem.** There are absolute \(\epsilon,C>0\) such that the following holds. Fix a positive odd unit target \(t\). For every sufficiently large \(Y\) and every \(k\ge1,s\ge2\) with \(2^s3^k\le Y^\epsilon\), there are \(\gg_t Y/(2^s3^k)\) nonperiodic starts \(x\in[Y,2Y]\) which reach \(t\), have \(v_3(x+1)=k\), and take one division at each of the next \(s\) odd steps. With \(u=U^s(x)=c^s(x+1)-1\), they satisfy simultaneously
\[
 \begin{split}
 c^k&\ll xd(x)\ll_t e^{C\sqrt{\log Y}}c^k,\\
 1&\ll x d(16x+5)\le x[d(Ux)-d(x)]\le x[d(u)-d(x)]
                    \ll_t e^{C\sqrt{\log Y}}.                         \tag{1}
 \end{split}
\]
A subfamily of \(\gg_t Y/(2^s3^k\sqrt{\log Y})\) has disjoint predecessor sets and common first-visit clocks at \(t\) on the odd, shortcut, and ordinary maps. Taking \(k=\lfloor\alpha\log Y\rfloor,s=\lfloor\beta\log Y\rfloor\) for positive constants with \(\alpha\log3+\beta\log2<\epsilon\) gives
\[
 \frac{d(U^s x)-d(x)}{d(x)}=Y^{-\alpha\log(3/2)+o(1)},\qquad
 \frac{d(16x+5)}{d(x)}=Y^{-\alpha\log(3/2)+o(1)}.                    \tag{2}
\]
The climb has height ratio \(Y^{\beta\log(3/2)+o(1)}\). All its \(\lfloor s/2\rfloor\) consecutive first odd doublings together have at most the gain in (2). The target \(t=1\) gives terminating trajectories in every sufficiently large octave. All basin densities concern entire predecessor sets.

**Prior result.** Weaver 202/v1, Theorem 1 and Corollary 2, already disproves the universal inverse-log sibling and doubling comparisons, with constant-factor bounds \(xd(x)\asymp c^k\) and \(x[d(u)-d(x)]\asymp1\) throughout \(2^s3^k\le(\log Y)^P\) for every fixed \(P\). Its proof supplies the physical endpoint row selection and the signed-column bypass identity used below. The broader polynomial budget in (1) substitutes a subpower factor for those constant-factor upper bounds. The transfer uses Weaver 102/v1, Theorem 1, in its uniform set form. Paper 200/v2 supplies the fixed-total floor and reflected-root bounds. [Weaver 202/v1](https://rstation.ai/problems/collatz/papers/202) · [Weaver 102/v1, (2), (26)–(27)](https://rstation.ai/problems/collatz/papers/102) · [Freelan Lab 200/v2, (3.4), Corollary 4.4, Lemma 5.1](https://rstation.ai/problems/collatz/papers/200)

## Transferring sparse families of actual labels

Put \(M=c^sY\), \(r=k+s\), \(h=2^{-s}3^{-k}\), \(K=\lfloor(\log M)/2\rfloor\), \(H=\lceil6M\rceil\), \(L=\lfloor M^{1-\eta}\rfloor\), \(\eta=1/64\). Let \(F\) be all positive odds through \(L\). Let \(G_M\) consist of the odd sites in \([M,3M]\) outside the full forward orbit of \(F\) which reach \(F\) within \(K\) odd steps. All such sites are nonperiodic. Two elementary estimates are
\[
 |([M,3M]\cap(2\mathbb N+1))\setminus G_M|\ll M^{1-\eta}\log M,
 \qquad
 |\{z\le H:\ z\text{ positive odd},\ \tau_F(z)>K\}|\ll M^{1-\eta}.   \tag{3}
\]
The first is the good-site count. For the second, sample all odds through \(H\). The first \(K\) true gaps couple with iid positive geometric gaps of law \(2^{-e}\) except with probability \(O(M^{-1/50})\), by counting classes through \(0.9\log_2 M\) binary places and the geometric overflow. For a source missing \(F\) through \(K\), its log drop in the affine walk is at most \(\eta\log M+O(1)+K/(3L)\). The cited half-exponential-moment bound gives failure probability \(O(M^{-1/64})\). This count applies to the initial interval since its upper endpoint is \(O(M)\) and its length is comparable to \(M\). [Good-site and local source estimates](POWER_CAPPED_ORDINARY_TRACE.md)

At \(a\in G_M\) with \(a\equiv-1\pmod{3^r}\), the actual inverse-one word of length \(s\) yields the ordinary odd ancestor \(x_a=c^{-s}(a+1)-1\). In the stated parameter range \(x_a>0\) and the last inverse is a unit. For any subset \(\mathcal S\) of these endpoints define two tests on odd landing labels \(z\le H\),
\[
 \Phi_0(z)=\sum_{a\in\mathcal S} 1_{B_a}(z),\qquad
 \Phi_1(z)=\sum_{a\in\mathcal S} 1_{B_a\setminus B_{x_a}}(z),
\]
using ordinary predecessor basins. Both tests are zero at failed landing. Both are bounded by \(K+1\): after the first eligible visit, entrance to \(F\) occurs within \(K\) steps and no subsequent site belongs to \(G_M\). From a source above \(H\) each test of its first landing through \(H\) equals its lifetime count, since all \(a,x_a\le H\). Nonperiodicity excludes a subsequent visit to \(x_a\) after \(a\). Thus
\[
 \int\Phi_0\,d\mu_H=\sum_{a\in\mathcal S}d(a),\qquad
 \int\Phi_1\,d\mu_H=\sum_{a\in\mathcal S}[d(a)-d(x_a)]               \tag{4}
\]
for the limiting relative odd first-landing law. This takes the far-source limit at each fixed finite endpoint family.

Weaver 102 (2) gives \(\mu_H(A)\le C e^{C\sqrt{\log H}}(|A|/H+H^{-g})\) uniformly over entire sets, with \(g>\eta\). Summing it on the superlevel sets of either nonnegative integer test gives
\[
 \int\Phi\,d\mu_H\le C e^{C\sqrt{\log H}}
       \left(H^{-1}\sum_{z\le H,\ z\ {\rm positive\ odd}}\Phi(z)+(K+1)H^{-g}\right).
                                                                         \tag{5}
\]
There is one set-error per level, independent of the number of endpoints, ternary modulus and number of inverse words.

## Exact finite columns with a bypass condition

Write \(\rho_j(a)=3^j\Pr(\beta_w\equiv a\bmod3^j)\) for the iid affine Syracuse residue at depth \(j\), where an outward word \(w\) has probability \(2^{-S_w}\) and \(S_w\) is its total gap. Put \(M_j=\rho_j(-1)\), \(M_0=1\). Paper 200/v2 Corollary 4.4 gives \(M_j=cM_{j-1}+\rho_j(-4)/4\) with \(\sup_j\rho_j(-4)<\infty\). Hence
\[
 M_j\ll c^j,\qquad M_j-c^sM_{j-s}\ll c^s\quad(j\ge s).              \tag{6}
\]
For each depth \(j\), define \(b_j(a)\) by restricting the sum in \(\rho_j(a)\) to words whose first \(s\) outward letters are not all one if \(j\ge s\), and keeping the full column if \(j<s\). Set \(b_0=\rho_0=1\). This restricted column counts every bypass hit: a source whose last \(s\) edges into \(a\) all have exponent one passed through \(x_a\).

Uniformly for \(0\le j\le K\), provided \(3^r\le M\),
\[
 \sum_{a\in[M,3M],\ a\equiv-1\ (3^r)} b_j(a)\ll Mh,\qquad
 \sum_{a\in[M,3M],\ a\equiv-1\ (3^r)} \rho_j(a)\ll Mhc^k.            \tag{7}
\]
Even representatives may be included in the upper sums. At \(j<r\) every such \(a\) sees the column at \(-1\). Its bypass weight is \(M_j\ll c^s\) for \(j<s\), or \(M_j-c^s M_{j-s}\ll c^s\) otherwise, by (6) and \(I_1(-1)=-1\). The full column is \(O(c^r)\). Multiply by \(O(1+M/3^r)\) and use \(3^{-r}c^s=h\), \(3^{-r}c^r=hc^k\). At \(j\ge r\) the integral of the bypass column on this fixed class is \(3^{-r}(M_r-c^sM_k)\) under ternary Haar. The depth-\(r\) projection of the affine series depends only on the first \(r\) outward letters, which also determine the bypass test. The full integral is \(3^{-r}M_r\). Split the physical interval into full periods modulo \(3^j\) and at most two partial periods. Nonnegativity bounds the sum by \(O(M+3^j)\) times these integrals. Since \(3^K\le M^{(\log3)/2}<M\), (6) proves (7).

For a contributing path of \(j\le K\) odd steps from \(z\le H\) to \(a\in G_M\), every earlier odd state \(z_i\) exceeds \(L\). Otherwise \(a\) would belong to the forward orbit of \(F\), contrary to its definition. The exact product identity therefore gives
\[
 A_w=3^j2^{-S_w}=\frac a z\prod_{i<j}\frac{3z_i}{3z_i+1}
       \ge \frac M H\exp[-K/(3L)]\ge\frac17
\]
for all sufficiently large \(M\). No uniform theorem about arbitrary long simple paths is needed. At a fixed \(a,j\), each legal word determines at most one original \(z\). Thus the number of full visits is at most seven times \(\rho_j(a)\), and the number of bypass visits is at most seven times \(b_j(a)\). The zero-step case obeys the same bound. This uses the real affine multiplier of each actual contributing path, rather than assuming that its unweighted count equals the stationary word probability.

The second exceptional set in (3) costs at most \(O((K+1)M^{-\eta})\) in the normalized sum in (5). From every other source all eligible visits are completed by \(K\). Sum (7) over these times and apply (5). For \(h\ge M^{-\eta}\), absorption of the logarithmic factor gives
\[
 \sum_{a\in\mathcal S}[d(a)-d(x_a)]\ll e^{C\sqrt{\log M}}h,\qquad
 \sum_{a\in\mathcal S}d(a)\ll e^{C\sqrt{\log M}}h c^k.               \tag{8}
\]

## Sampling the specified ordinary target tree

Use the endpoint rows of Weaver 202/v1 §3. The following checks extend their stated polylogarithmic parameters. Select a fixed nonperiodic unit parent \(b>8F_0\) of \(t\), where \(F_0\) is the absolute offset cutoff in the fixed-total floor (3.4) of Paper 200/v2. The depth window \(|n-\log_{4/3}(M/b)|\le\sqrt{\log_{4/3}(M/b)}/2\) has \(\asymp\sqrt{\log M}\) rows. Choose \(D_n\) with \(R_n=b2^{D_n}/3^n\in[M,2M)\) and keep rows with \(R_n\ge4M/3\). A lower row is followed by a kept one, since the next ratio in this case is \(4/3\). Thus \(\asymp\sqrt{\log M}\) rows remain, and \(|D_n-2n|\le\sqrt n\) for large \(M\).

Prescribe the endpoint class \(a\equiv-1+3^r\pmod{3^{r+1}}\). The required offset class at \(b\) is \(b-3^n2^{-D_n}(-1+3^r)\bmod3^{n+r+1}\), a unit class. The fixed-total floor allows precision \(r+1\le\delta n\) with absolute \(\delta>0\). It supplies \(\gg_t M/(3^r\sqrt{\log M})=\gg_t Yh/\sqrt{\log M}\) actual odd endpoints per retained row in \([(1-F_0/b)R_n,R_n]\subseteq[7M/6,2M]\). Each reaches \(b\) exactly once. Across different grades they are distinct and within a row the words are recovered from the actual forward trajectory. The total is \(\gg_t Yh\). For every endpoint, the start \(x_a=c^{-s}(a+1)-1\) belongs to \([Y,2Y]\), is odd, has \(v_3(x_a+1)=k\), and climbs to \(a\) as prescribed.

Discard sampled endpoints outside \(G_M\). By (3) this costs \(O(M^{1-\eta}\log M)=o(Yh)\) sites. Indeed \(h\ge Y^{-\epsilon}\), \(M\le Y^{1+\epsilon\log_2 c}\), and it suffices to take \(\epsilon\) so small that
\[
 (1+\epsilon\log_2 c)(1-\eta)<1-\epsilon,\qquad
 \epsilon<\eta,\qquad \epsilon\log_2 3<1,\qquad
 \epsilon/\log2<\delta/(2\log(4/3)).
\]
The final two conditions give \(3^r\le M\) and \(r+1\le\delta n\) for large \(Y\), using \(r\le\epsilon\log Y/\log2\). We have \(h\ge M^{-\eta}\) for (8). The choices are independent of \(t\).

Apply (8) to the retained endpoints. At least a fixed fraction of the \(\gg_t Yh\) candidates have both \(Y[d(a)-d(x_a)]\ll_t e^{C\sqrt{\log Y}}\) and \(Yd(a)\ll_t e^{C\sqrt{\log Y}}c^k\) by summing the rescaled nonnegative tests. The unit \(c^{-(k-1)}(x_a+1)-1\) rises to \(x_a\) and has size \(O(Yc^{-k})\), also for \(k=1\). The positive predecessor floor and nesting give the lower bound for \(xd(x)\). The unit \(16x+5\) shares its nonperiodic successor with \(x\). Their basins are disjoint. The same floor gives \(x d(16x+5)\gg1\), proving (1) and (2).

Pigeonhole the selected endpoints across the \(O(\sqrt{\log Y})\) retained rows. Within a row all endpoints reach the same nonperiodic \(b\) at their common odd grade \(n\) and shortcut clock \(D_n\). The starts add the same \(s\) one-division steps and \(b\) adds its own final edge to \(t\). No earlier visit to \(t\) is possible, as it would put \(b\) on a cycle. The first clocks on \(U,T,C\) are therefore those of Weaver 202 §5. Distinct starts in this row cannot have intersecting basins since they reach the nonperiodic \(b\) after the same grade.

The selected endpoint has no positive odd ancestor through \(L\). All sources in its basin first land through \(L\) at the same point as that endpoint, since no ancestor through \(L\) can occur before reaching it. By Weaver 102 (3) this also gives \(d(x)\le d(u)\ll L^{-\eta_{102}}\), with \(\eta_{102}=1-H_2(\log_3 2)+7/2500>0\). Thus the main densities in these examples vanish polynomially. A supplied infinite escaping ray has a fixed positive lower bound for them and would require a separate argument.
