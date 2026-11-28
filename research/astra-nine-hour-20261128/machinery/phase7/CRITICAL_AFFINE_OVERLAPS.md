# Exact rational affine overlaps of the critical ternary Syracuse law

Let \(\theta=\theta_*\), \(q=1-\theta\), and let \(\mu\) be the ternary Syracuse law of iid gaps \(p(e)=\theta q^{e-1}\) with \(H(p)=\log3\). Regard \(\mu\) as a probability on \(\mathbb Q_3\), supported on \(\mathbb Z_3^\times\). Write \(A_e(z)=2^{-e}(1+3z)\), \(A_w=A_{e_1}\circ\cdots\circ A_{e_n}\), \(S_w=\sum e_i\) and \(p(w)=\theta^nq^{S_w-n}\). The empty word denotes the identity. For every
\[
    g(z)=2^a3^b z+c,\qquad a,b\in\mathbb Z,\qquad c\in\mathbb Z[1/6],
\]
we have
\[
 \boxed{\quad \mu\not\perp g_*\mu\quad\Longleftrightarrow\quad
                   g=A_u A_v^{-1}\text{ for two finite positive-gap words}.\quad}       \tag{1}
\]
Membership on the right is decidable by a finite exact calculation described below. On the part shared with \(\mu\), the Radon–Nikodym derivative of \(g_*\mu\) is the constant \(q^a(q/\theta)^b\). In particular \(\mu\perp\mu(\cdot-d)\) for **every nonzero ordinary integer** \(d\). Some nonintegral shifts do overlap: the words \((1,2),(2,1)\) have equal slope and offsets \(7/8,5/8\), giving overlap at displacement \(1/4\).

The analytic input is full ternary entropy dimension at criticality. An elementary deterministic steering argument supplies the actual positive counted fusions. The published scalar probability theorem gives an independent stronger input for that step. Weaver 135 proves critical singularity relative to Haar from information fluctuations and a stopping cover. That result compares one probability to Haar. Formula (1) compares it with its own rational affine images and determines the shared component. [Leen, full entropy dimension, Theorem C](https://doi.org/10.5281/zenodo.23268832) · [Weaver 135, §§3–4](https://rstation.ai/problems/collatz/papers/135) · [Leen, scalar absorption, §2](https://doi.org/10.5281/zenodo.23268751)

## Critical decoding and an actual positive fusion

Let \(Z=A_E(Y)\), with \(Y\sim\mu\) and \(E\sim p\) independent. Since \(A_E\) contracts exactly one trit, conditional on \(E\) the residue \(Z\bmod3^j\) and \(Y\bmod3^{j-1}\) determine one another. Thus
\[
 d_j:=H(E\mid Z\bmod3^j)=\log3+H(\mu_{j-1})-H(\mu_j),\qquad j\ge2.
\]
The decreasing sequence \(d_j\) tends to zero by full entropy dimension. Conditional entropy converges for this countable finite-entropy letter, by truncation and martingale convergence, so \(E\) is determined by \(Z\) almost surely. After recovering \(E\), recover \(Y\) and repeat. In particular the countably many measures \((A_w)_*\mu\) at each fixed depth are supported on pairwise disjoint Borel sets up to their respective null sets. This is the coding fact used below. [Finite entropy identity](../phase5/CRITICAL_BELLMAN_LIFTS.md)

Suppose now that \(G(x)=2^m x+B\) with \(m\ge0\) and \(B\in\mathbb Z\), and that \(G\) maps odd integers to odd integers. If \(G\ne\operatorname{id}\), then \(\mu\perp G_*\mu\). To prove this, use the physical shortcut \(T(x)=x/2\) for even \(x\) and \((3x+1)/2\) for odd \(x\). The first \(m\) parity bits of \(2^m x+B\) depend only on \(B\bmod2^m\). Its position after those steps is \(3^k x+C\) with a fixed integer \(C\) and the fixed number \(k\) of odd departures already credited. The [deterministic steering and cylinder lifting lemma](DETERMINISTIC_COUNTED_FUSION.md) forces the original first bit odd, reaches counted fusion in finitely many steps, and prescribes the parity of the common endpoint odd by one unused bit. A sufficiently large positive lift gives both actual starts positive. For an independent probabilistic route, Leen’s remaining-absorption lemma quantifies over every \(k\ge0,C\in\mathbb Z\), and Weaver 124, Lemma 2 records a failure probability tending to zero at large \(t\). The event that both \(x\) and \(T^t x\) are odd has binary Haar probability \(1/4\), so those results also supply a positive cylinder with the same properties. [Leen, primary TeX, `pair:remaining-tail` and `pair:uniform-tail`, SHA-256 `d2f961635d339a4b215c82b1f2f8b9ca53143043f4c58b9aa67290f46056996e`](https://zenodo.org/api/records/23268751/files/collatz-synchronization-rates.tex/content) · [Weaver 124, equations (3)–(6)](https://rstation.ai/problems/collatz/papers/124)

Let its two gap words in inverse order be \(u,v\), leading from the shared odd endpoint back to \(x,G(x)\) respectively. Both have the same positive depth \(n\), counting the initial \(k\) on the second path, while their shortcut totals are respectively \(t,t+m\). Thus \(A_u\) and \(A_vG\) have identical slopes, and agree at \(x\). They agree everywhere. The words are distinct because \(G\ne\operatorname{id}\). Apply an invertible affine change of coordinates to the singularity of \((A_u)_*\mu\) and \((A_v)_*\mu\). This proves the assertion for \(G\). For example, with \(G(x)=2x+1\), the ordinary inputs \(1,3\) reach the common odd endpoint \(1\) at clocks \(4,5\) and odd count two. With \(G(x)=8x-7\), the inputs \(39,305\) reach \(11\) at clocks \(13,16\) and odd count seven.

## Reduction of the full affine group and the exact decomposition

Write \(A_w(z)=(D_w+3^{|w|}z)/2^{S_w}\); for a nonempty word \(D_w\) is an odd positive integer. Take positive depths \(n_u=n_v+b\), both as large as needed below. Expand \(\mu=\sum_{|u|=n_u}p(u)(A_u)_*\mu\), and apply \(g\) to the depth-\(n_v\) expansion. For a pair \(u,v\), the normalized comparison is with \(G=A_u^{-1}gA_v\), whose slope is \(2^m\), \(m=S_u+a-S_v\), and whose offset is
\[
       B=\frac{2^m3^bD_v+2^{S_u}c-D_u}{3^{n_u}}.                      \tag{2}
\]
If \(m<0\), interchange the pair and use \(g^{-1}\), so the slope exponent becomes nonnegative. Choose the depths in advance so that \(2^{S_u}c\) and its counterpart \(2^{S_v}g^{-1}(0)\) have positive 2-adic valuation whenever nonzero; \(S_u\ge n_u\), \(S_v\ge n_v\) suffice. Formula (2) then has denominator a power of three in either chosen orientation. Unless \(B\) is 3-adically integral the two unit supports are disjoint. Once integral it is an ordinary integer. Its parity is even for \(m=0\) and odd for \(m>0\), using oddness of both numerators and of \(3^b\) as a 2-adic unit. Thus the normalized comparison either has disjoint supports, falls under the preceding singularity lemma for a nonidentity physical \(G\), or has \(G=\operatorname{id}\). The last case says precisely \(gA_v=A_u\). Conversely a matching pair supplies a positive common component through these same cylinder expansions (or directly through the expansions at the lengths of the given words).

At the fixed depths, take mutually singular Borel coding carriers \(C_u\) for the \(u\)-components. A matching \(u\) has at most one corresponding \(v\), since identical maps at a fixed depth have identical inputs under the almost sure decoder. Let \(E_g\) be the union of the matched \(C_u\), after deleting null sets if needed. Unmatched comparison components are singular to all unmatched or differently matched carriers, by the countable pairwise comparisons just proved. For each match, \(S_v=S_u+a\) and \(n_u=n_v+b\), giving the complete Lebesgue decomposition
\[
       g_*\mu=q^a(q/\theta)^b\,\mu|_{E_g}+\sigma_g,
                       \qquad \sigma_g\perp\mu.                         \tag{3}
\]
Here a carrier at one fixed depth can be replaced by any other choice modulo \(\mu\)-null sets.

## A finite membership decision

For a pure word or inverse word, the slope determines length and total, so all such candidates can be enumerated finitely, including the identity. For a pair with both words nonempty, cancel identical final letters on the right until one word is empty or their final letters differ. In the latter case write \(u=u'e\) and \(v=v'f\) with \(e\ne f\). Put \(\beta_w=A_w(0)\). The constant terms contributed by these last letters cancel at the matching slope, leaving exactly
\[
 c=\beta_{u'}-2^a3^b\beta_{v'},\qquad
        f-e=a+S_{u'}-S_{v'},\qquad |u'|-|v'|=b.                       \tag{4}
\]
For nonempty \(w\), \(v_2(\beta_w)=-S_w\) by the odd numerator formula. If both prefixes are nonempty, their two summands in (4) have different 2-adic valuations because \(e\ne f\). With \(r=-v_2(c)\) for \(c\ne0\), this forces
\[
 S_{u'}\le\max(0,r),\qquad S_{v'}\le\max(0,r+a).
\]
The same bounds hold with one empty prefix, since the other summand then has exactly the valuation of \(c\). Enumerate both bounded lists, allowing empties. Check the offset and length equalities in (4); any stipulated difference \(f-e\) has positive representatives. Combined with the pure-word test, this decides membership. When \(c=0\), different final letters with two nonempty prefixes would give a nonzero difference in (4), and one empty prefix with one nonempty does so as well. Two empty prefixes give \(b=0\), and every pure dyadic dilation has a matching pair of single gaps. A nonempty pure word or its inverse has nonzero offset. Thus \(c=0\) gives overlap exactly when \(b=0\).

For a nonzero integer translation take \(a=b=0\), \(r\le0\). The only bounded prefixes are empty and hence give offset zero, and a pure word at slope one must be empty. This proves the asserted integer-translation singularity. Countability permits one Borel conull set \(B\) whose translates \(B+d\), \(d\in\mathbb Z\), are pairwise disjoint: first choose a conull carrier charged by no nonzero translated measure, then remove all its nonzero integer translates from it. The support of \(\mu\) is nevertheless all ternary units. No part of (1) provides a reverse entropy estimate relative to Haar.

## Exact mass of the common part

The same finite search computes total variation without enumerating arbitrarily long tails. Call a matching pair reduced if it has no identical final letter to cancel. The target words \(u\) of distinct reduced matches form a prefix-free family. Indeed if \(u_2=u_1w\), then \(gA_{v_2}=A_{u_2}=gA_{v_1}A_w\). Word freeness gives \(v_2=v_1w\), so \(w\) must be empty by reducedness. For freeness, equality of slopes gives equality of depths and totals, and equality of maps at that depth forces equality of words by the almost sure decoder. The source words are prefix-free by the same reasoning with \(g^{-1}\).

Every match reduces into this family. Conversely a reduced match extends on the right by every common suffix and so its whole cylinder belongs to the shared carrier up to null sets. This also follows directly from \(gA_v=A_u\). In particular the matched pairs at the fixed large depths used in (3) and the full collection of reduced paired cylinders have the same shared carrier modulo null sets. Let \(M_g=\mu(E_g)\), the mass of the shared **target** carrier, measured using \(\mu\). A reduced pure match \(u,v\) with an empty member contributes \(p(u)\), including \(p(\varnothing)=1\). Each bounded pair \(u',v'\) in (4) with \(D=a+S_{u'}-S_{v'}\ne0\) contributes
\[
             \sum_{e\ge\max(1,1-D)}p(u'e)
                         =p(u') q^{\max(0,-D)}.                          \tag{5}
\]
Add these finitely many numbers, using prefix-freeness. The term with \(D=0\) is omitted because it would have a common final letter. For \(c=0,b=0\), the target mass is \(q^{\max(0,-a)}\), including the identity. The mass measured with \(g_*\mu\) on the common absolutely continuous carrier is \(\kappa_g M_g\), with \(\kappa_g=q^a(q/\theta)^b\). Consequently, taking total variation distance in \([0,1]\),
\[
               d_{\rm TV}(g_*\mu,\mu)=1-\min(1,\kappa_g)M_g.             \tag{6}
\]

| Transformation | \(M_g\) | \(\kappa_g\) | Mass of the overlap \(1-d_{\rm TV}\) |
|---|---:|---:|---:|
| \(z\mapsto2z\) | \(1\) | \(q\) | \(q\) |
| \(z\mapsto z/2\) | \(q\) | \(1/q\) | \(q\) |
| \(z\mapsto z\pm1/4\) | \(\theta q\) | \(1\) | \(\theta q\) |
| \(z\mapsto z+1/2\) | \(0\) | \(1\) | \(0\) |
| \(A_e\) | \(p(e)\) | \(1/p(e)\) | \(p(e)\) |
| \(A_e^{-1}\) | \(1\) | \(p(e)\) | \(p(e)\) |

The [exact rational control](check_affine_overlap.py) compares the finite search with independently composed word pairs, checks inversion symmetry and negative controls, and replays actual integer branch words at unequal clocks. Its rational parameter \(2/3\) is above the threshold and makes the masses fully rational. It checks the finite arithmetic. The principal analytic input is the cited written entropy-dimension theorem. The normalized physical fusion uses the elementary steering already present in Paper 212.

## The exact parameter range

For an arbitrary nondegenerate geometric tilt \(0<\theta<1\), Leen's entropy dimension theorem gives \(\lim_{n\to\infty}H(\mu_{\theta,n})/n=\min(H(p_\theta),\log3)\). The conditional letter identity at this parameter replaces \(\log3\) in the definition of \(d_j\) by \(H(p_\theta)\), and therefore gives
\[
              H(E\mid Z)=\max(0,H(p_\theta)-\log3).
\]
Every argument in (1)–(4) remains valid at every \(\theta_*\le\theta<1\), with that parameter's \(q=1-\theta\). For \(0<\theta<\theta_*\), positive conditional entropy implies that at least two first-letter measures \((A_e)_*\mu_\theta,(A_f)_*\mu_\theta\) lack mutual singularity. Their first trits force the letters to have the same parity. Applying the inverse of one of the maps shows that \(\mu_\theta\) overlaps a translate-dilate \((H^k)_*\mu_\theta\) for some \(k\ge1\), where \(H(x)=4x+1\). Every \(H^k(x)=4^kx+(4^k-1)/3\) maps odd integers to odd integers and differs from the identity. The physical fusion lemma at criticality and (1) exclude it from the word-transporter list, a list independent of \(\theta\). Thus validity of the classification (1) for all \(g\) characterizes exactly the half-interval \([\theta_*,1)\). This argument identifies the existence of some \(k\) below the threshold, without fixing which power overlaps there.
