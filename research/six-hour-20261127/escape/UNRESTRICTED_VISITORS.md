# Every finite word without adjacent twos has positive-density protection against all smaller ordinary visitors

**Proposed written theorem, with a source-qualified natural-density transfer.** Let
\(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers. Fix a nonempty chronological word \(w\) on \(\{1,2\}\) starting with 1 and having no consecutive twos. Write \(n=|w|\), \(A=\sum w_i\) and \(g_*=3^n/2^A\). Among positive odd integers \(x\) whose first \(n\) exponents are \(w\) and for which \(3^{128}\mid x\), the lower relative natural density of the following event exceeds \(0.99\):
\[
 \forall\,0\le i\le n,\ \forall\,0<u<x\text{ odd},\ \forall\,h\ge0,
 \qquad U^h(u)\ne U^i(x).                                           \tag{1}
\]
The visitor horizon in (1) is unrestricted. The result also protects every intermediate shortcut state up to the terminal odd state, since a meeting persists until that terminal. The fixed forward-word cylinder has absolute density \(2^{-A-1}3^{-128}\) among all positive integers. The relative lower bound is independent of the word and its length. In particular, varying finite positive integers can pass the complete smaller-visitor test on arbitrarily long prescribed words with positive drift.

The same Borel set of ternary *source* coordinates, of relative Haar measure greater than \(0.99\) in \(3^{128}\mathbb Z_3\), protects every word in this language against every strict inverse-gain improvement. This stronger simultaneous Haar assertion concerns a source coordinate paired separately with each prescribed dyadic word. The natural-density conclusion fixes one finite word before counting ordinary sources. No single positive ordinary source with an infinite prescribed script follows from it.

Weaver's Paper 1 already gives the inverse affine cone and excludes every smaller visitor up to the observed depth plus \(v_3(x)\). Weaver's Paper 178, §7, already obtains protection against unrestricted visitors on the all-ones and negative-five cycle cylinders, with much stronger proportions there. Its §8 conditions on a ternary ball at one ordinary anchor and sums continuation gains squared. Here the cone covers the entire positive-entropy language, and conditioning all its affine offsets near ordinary positive integers gives a common protected set for every word and every depth. [Paper 1/v3, Lemma 1 and Theorems 2, 6](https://rstation.ai/problems/collatz/papers/1) · [Paper 178/v1, §§2, 7–8](https://rstation.ai/problems/collatz/papers/178)

## One ternary event for every word

For a positive exponent \(e\), the inverse \(I_e(z)=(2^ez-1)/3\) is legal when it lies in \(\mathbb Z_3\). A path with \(h\) inverses of total exponent \(F\) has gain \(g=3^h/2^F\). Its domain is one residue class modulo \(3^h\), and on that class its endpoint is Haar-uniform when the input is Haar-uniform. Write \(G(z)\) for the supremum of the gains of every finite legal inverse word at \(z\), including the empty gain 1. For Haar probability \(\pi\) and \(a\ge1\),
\[
                         \pi\{G>a\}\le a^{-2}.                       \tag{2}
\]
Indeed the words first crossing \(a\) in inverse order form a prefix-free set. The mass of each legality cylinder times its gain squared equals \(3^h4^{-F}\), its word mass under the independent probability \(\Pr(e=j)=3/4^j\). Sum the cylinder measures by the union bound. This is the stopped squared-gain comparison of Paper 178, §2, in odd-clock notation.

For \(k\ge1\), choose \(m\) with relative Haar law on \(3^k\mathbb Z_3\). Define \(\mathcal P\) by requiring \(G(m)\le1\) and
\[
 G(2^d m+c)\le 2^d
 \quad\text{for every }d\ge1\text{ and every odd }0<c\le5(2^d-1).    \tag{3}
\]
These are countably many Borel conditions. Since \(3\mid m\), the first condition always holds. We deliberately include every odd integer in the cone, whether or not it ever occurs as an offset for a word.

Consider the ternary terminal \(z=U_w(m)\), using the stated affine word and division by the unit \(2^A\) in \(\mathbb Z_3\). Each competing inverse path truncated after exactly \(n\) odd inverses has endpoint \(2^d m+c\), where \(d\) is its excess exponent. Its gain relative to \(g_*\) is \(2^{-d}\). By Weaver's cone, either \((d,c)=(0,0)\) with the identical word, or \(d\ge1\) and \(c\) is one of the offsets in (3). To apply the cone to a ternary source, choose an ordinary dyadic lift of the reference word. The terminal residue modulo \(3^n\) and the list of legal length-\(n\) inverse words are independent of that lift. The resulting affine identity and its integer constant are independent of it as well. Thus (3) rules out a larger gain for every longer competitor. A shorter competitor of \(h<n\) odd steps is bounded by the gain of the corresponding true suffix, by division-minimality of that suffix. The true prefix of length \(n-h>0\) has gain strictly above one, since the word starts with 1 and each of its prefixes has at most half twos. The shorter competitor has strictly smaller gain. Equality for a different number of odd steps would violate unique factorization of 2 and 3. At the same odd depth Weaver's cone gives the identical word at zero excess. The principal gain is the unique maximum.

## Conditioning all positive offsets at once

Fix \(d,c\) in (3). The first \(k\) inverses from \(2^d m+c\) see exactly the same legality decisions as from the ordinary odd integer \(c\), because their initial states are congruent modulo \(3^k\). Before or at that depth a gain \(g>2^d\) would give a positive odd ordinary source \(u<c/g<5\). The only possible starts are 1 and 3, and on their complete trajectories every gain is at most \(3/2\), less than \(2^d\). This is the positive-anchor argument in Weaver's Theorem 6.

After exactly \(k\) inverse steps from \(c\), write \(u\) for the positive odd endpoint and \(g_k(u)=3^k2^{-A_k(u)}\) for its forward gain to \(c=U^k(u)\). Each such word gives exactly one \(u\), which determines the word. Its endpoint when starting from \(2^d m+c\) is Haar-uniform in \(\mathbb Z_3\) under the conditional law: its affine dependence on \(m/3^k\) has multiplier \(2^{d+A_k(u)}\), a ternary unit. The gain already accumulated does not depend on \(m\). By (2) the probability this particular word can continue to a violation is at most \(4^{-d}g_k(u)^2\). No independence between words is needed.

For a fixed \(u\), only one \(c=U^k(u)\) can occur, even when all words and offsets are tested. Put \(D(c)=\min\{d\ge1:c\le5(2^d-1)\}\). After summing all eligible \(d\), the contribution is at most
\[
 g_k(u)^2\sum_{d\ge D(c)}4^{-d}
 \le \frac{100}{3}\left(\frac{g_k(u)}{c}\right)^2
 \le \frac{100}{3u^2}.                                                \tag{4}
\]
The last inequality follows from the ordinary positive affine relation \(c\ge g_k(u)u\), and the first from \(2^{D(c)}>c/5\). This gives uniform summability in the actual positive source \(u\) after superposing infinitely many candidate offsets.

Take \(k=128\). Each positive odd \(u\le4095\) reaches 1 within 87 odd steps, as checked by [the finite control](check_visitor_anchor.py) and by kernel evaluation in [VisitorAnchor.lean](VisitorAnchor.lean). Thus \(U^{128}(u)=1\) and \(g_{128}(u)\le (3/4)^{41}/u\). For these starts the geometric tail in (4) is at most \(1/3\) before its bound in terms of \(c\) is used. For \(u>4095\) use (4) and the decreasing integral bound on the sum over all such integers. The total probability of violating even one test (3) is bounded by
\[
 \frac{2}{3}(3/4)^{82}+\frac{100}{3\cdot4095}<\frac1{100}.             \tag{5}
\]
This proves the claimed common set estimate. More generally, finite verified initial ranges and longer ternary conditioning give the corresponding bound (4). Under absence of escape this same argument gives relative density tending to one as \(k\to\infty\), by dominated convergence even if other positive cycles exist: each lap has gain strictly below one.

## Transfer to actual ordinary sources

Use the shortcut \(T(x)=x/2\) on evens, \((3x+1)/2\) on odds. A reverse shortcut word from an odd terminal groups into complete Syracuse inverses, with possible extra doublings at the end. Removing those final doublings increases its gain. Hence the maximum just proved is also the unique maximum over shortcut inverse words, with the principal word of length \(A\). The target ball is the image of \(3^{128}\mathbb Z_3\) under \(U_w\), of Haar mass \(3^{-n-128}\). On more than 99 percent of that ball the prescribed word is the unique gain winner.

For completeness, restrict first to visitor shortcut clock at most \(J\ge A\). On each of finitely many terminal ternary residue classes the legal competitors are fixed. Whenever the principal word uniquely wins in gain, its positive inverse source is eventually strictly smaller than the competitor sources as the ordinary terminal grows, by the strict inequality of the affine slopes. Actual sources with the specified exact word form one residue class of odd integers modulo \(2^{A+1}\). The additional modulus \(3^{128}\) and any finite ternary tests on the target have the relative Haar proportions just computed, by the Chinese remainder theorem applied to the source. Thus the bounded-visitor minimum event has relative lower density at least the bound from (5).

Passing \(J\to\infty\) uses the all-time transfer in Weaver's Paper 178, §2, specifically the estimate imported there from Paper 177, §8, (3). For a fixed source cutoff \(X\) the observed terminal is at most \(C_w X\), and distinct sources in the word cylinder have distinct terminals. If a truncated protected source has a smaller visitor at a later clock, the least positive ancestor of its terminal first arrives after \(J\), and the entire first-arrival path stays at or above that ancestor. The cited estimate bounds the upper density of these terminals by \(O_w(\rho^J)\), with \(\rho<1\). Dividing by the positive fixed cylinder density and sending \(J\to\infty\) proves (1). This argument imposes no cap on the smaller visitor's time and asserts no quantitative uniform onset as \(w\) varies.

## Protected starts in the basin of 1, under two further inputs

Let \(P_w\) denote the ordinary set in the stated dyadic and ternary class satisfying (1). It can be approximated arbitrarily well in upper natural density of the symmetric difference by periodic sets. Indeed, for fixed visitor deadline \(J\), all competing shortcut words give finitely many ordinary affine source expressions at the actual terminal, each on one congruence class. Comparison with the principal source has eventual constant truth on each class, even for equal slopes. This bounded-deadline set is periodic up to finitely many starts. The unrestricted set differs from it only on the late least arrivals just estimated. In particular \(p_w=\operatorname{dens}(P_w)\) exists and exceeds \(0.99\cdot2^{-A-1}3^{-128}\).

For any forward-invariant basin \(C\) whose membership is unchanged along each shortcut edge, the fixed-shift counted-fusion estimate gives
\[
  \#\{x\le X:\mathbf 1_C(x)\ne\mathbf 1_C(x+1)\}=o(X).
\]
Here one fixes a finite shortcut clock, uses periodicity of counted fusion by that clock, then sends the clock to infinity using Haar probability one of adjacent fusion. Consequently the counts of \(C\) in any two residue classes of a fixed modulus differ by \(o(X)\). Multiply first by a periodic indicator and then use the upper-density approximation above. This proves
\[
   \frac{\#(C\cap P_w\cap[1,X])}{X}
       =p_w\frac{\#(C\cap[1,X])}{X}+o(1).                             \tag{6}
\]
The identity does not require existence of a density for \(C\).

Apply (6) to the basin of 1. **Conditional on the cited fixed-target theorem M** that this basin has positive lower natural density, every one of these prescribed finite words has a positive-lower-density set of genuine convergent ordinary realizations with no smaller visitor, at any visitor time, to any state through the word. For the fixed-shift input see Weaver, Paper 124/v1, (18), or the explicit passage to Haar probability one in PR193. For M we use the exact public target-one instance of Mazur's September 2026 theorem on positive lower natural density of predecessors. PR197 records its formalization commit and advertised 388-file checking boundary; that external development was not rebuilt in this pass. The classical power-law predecessor lower bound alone does not give this corollary. [Paper 124](https://rstation.ai/problems/collatz/papers/124) · [PR193, fixed shift](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/boundary/PAIRED_BOUNDARY.md) · [Mazur, proof record](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/) · [PR197, source qualifications](https://github.com/GettysburgResearch/collatz/blob/b0538639df0ab7edd239281bd897e705160f732c/research/ayh-resource-reset-20261124/literature-step/MACROSCOPIC_PAIR_CLOSURE.md)

## A fixed positive integer as the ternary coordinate

There is also an explicit pointwise all-depth example. Take the ternary coordinate \(m=15\). Use Weaver's sharper cone fact that a realized excess-one offset is exactly \(c=1\) for forward words starting with 1 (Paper 1, Lemma 3). For a strict deeper win through \(b=2^d15+c\) an actual positive odd source would satisfy \(u<b/2^d<20\). At \(d=0\) the branch is \(b=15\), a multiple of three unavailable for a further inverse. At \(d=1\) the branch is \(b=31\); at \(d\ge2\) it satisfies \(b\ge61\). The complete odd trajectories of the ten positive odd starts below 20 visit only
\[
 \{1,3,5,7,9,11,13,15,17,19,23,29,35,53\}.
\]
This finite set is forward invariant and disjoint from the candidate branches. Thus for **every** eligible symbolic script, simultaneously at all prefixes, the fixed ternary coordinate 15 satisfies all-horizon calibration. With \(y_i=U_{w_{<i}}(15)\in\mathbb Z[1/2]\cap\mathbb Z_3\),
\[
 m_h(y_i)\ \ge\ \left\lceil A_i+(h-i)\log_2 3\right\rceil
 \quad(h,i\ge0),\qquad m_i(y_i)=A_i.
\]
Here \(m_h\) is the minimum legal inverse clock, as in PR192's corrected-height calibration. The formula includes \(i=0\) since 15 is divisible by three.

These rational terminals are positive and grow exponentially. For a script starting with 1 its prefixes satisfy \(A_i\le3i/2\). Its real affine correction \(G_i^{(0)}=\sum_{j<i}2^{A_j}/3^{j+1}\) is at most 5: at even indices \(j=2t\) use \(A_{2t}\le3t\) and at odd indices \(j=2t+1\) use \(A_{2t+1}\le3t+1\); summing pairs gives \((1/3+2/9)/(1-8/9)=5\). Therefore \(y_i=3^i2^{-A_i}(15+G_i^{(0)})\) has multiplicative raw correction at most \(4/3\), and the genuine ternary density \(\rho_i=3^i p_i\) satisfies
\[
                  \rho_i(y_i)/y_i\ \ge\ 1/20 .
\]
The first \(i\) letters are one competing word of weight \(2^{-A_i}\); the bounded full posterior in [GEODESIC_POSTERIOR.md](GEODESIC_POSTERIOR.md) also gives a uniform upper bound. At the genuine positive source 15 the first four valuations are \((1,1,1,5)\), so every infinite script in this language loses dyadic legality within four steps. Subsequent positive rational values need not be the least positive odd representatives of their ternary cells. The example isolates the missing integrality even with a fixed positive integer in the source ternary coordinate, positive targets of the macroscopic size, and all comparison horizons present.

**Ordinary obstruction still open.** A rule guaranteed to produce a smaller source during every fixed-length prefix in this language fails even on an arbitrarily large genuine positive source. To exclude a positive infinite itinerary one must use the same integer as the forward word length tends to infinity, or prove a bound depending on that source. Protection of an entire infinite symbolic itinerary at a ternary coordinate does not enforce its infinitely many binary congruences at that same ordinary integer.
