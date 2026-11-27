# How many odd steps must a smaller Collatz visitor spend?

**PROPOSED. Collatz remains open.** The results concern a fixed ordinary source during its actual initial sequence of odd shortcut steps. They bound the cost of every strictly smaller ordinary visitor and construct families with a successful visitor. The universal claim that every positive source other than 1 has some smaller merger remains open.

Use the shortcut map \(T(2v)=v,\ T(2v+1)=3v+2\). Write \(Q_e(m)\) for the number of odd inputs in the first \(e\) shortcuts from \(m\). In the proofs, \(\operatorname{Walk}(e,k,m,y)\) records \(T^e(m)=y\) and \(Q_e(m)=k\). The Lean relation uses signed integer edge equations. Its readout theorem identifies the actual deterministic iterator and odd count. The original sources and comparison witnesses below are positive integers.

## 1. A lower bound at every phase of the same source

**Theorem D1.** Suppose \(s\in\{0,1\}\), \(n>s\), \(3^K\mid n-s\), and \(2^j\mid n+1\). For every positive integer \(m<n\) and every native shortcut clock \(e\),
\[
       T^e(m)=T^j(n)\quad\Longrightarrow\quad Q_e(m)>K+j.
\]
The upper source stays fixed as \(j\) ranges from 0 to \(v_2(n+1)\), including the even peak. The lower arm has unrestricted time, height and number of even steps. The divisibility is ordinary, with no compatibility limit over changing sources. [Native theorem and sharpness](RampShadow.lean)

**Proof.** The upper path takes the maximum possible step at each time through \(j\), so a smaller start cannot reach its endpoint in fewer than \(j\) steps. Write \(e=d+j\) and \(k=Q_e(m)\). Suppose \(k\le K+j\). The integer \(a=3^{j-k}(n-s)\) and the positive rational \(D=2^d3^{j-k}\) give
\[
 m=m_0+D(n-s),\qquad m_0=m-2^d a\in\mathbb Z.
\]
The first \(d\) parities from \(m_0\) agree with those from \(m\). If they contain \(p\) odds, write \(z_0=T^d(m_0)\) and \(z=T^d(m)=z_0+3^p a\). Write \(u=k-p\). The actual remaining \(j\)-step word has an intercept \(0\le A\le3^j-2^j\). Subtract the translated linear terms in its endpoint equation and the formula \(2^j(T^j(n)+1)=3^j(n+1)\). This gives
\[
          3^u z_0+A=3^j(s+1)-2^j.
\]
Hence \(z_0\ge0\), strictly when \(s=1\). Nonpositive ordinary integers under the signed shortcut rule cannot reach a positive integer, and negative integers remain negative. Thus \(m_0\ge s\). The full lower path has nonnegative affine intercept, giving \(m_0<D(s+1)\). The strict inequality \(m<n\) forces \(D<1\), since \(n>s\).

When \(s=0\), the only possibility is \(m_0=0\), whose first \(d\) steps are all even. Then \(k\le j\), contradicting \(D<1\). When \(s=1\), the only possibility is \(m_0=1\), so \(z_0\in\{1,2\}\) and \(3^p\le2^dz_0\). If \(z_0=1\) then \(3^{p+u}\le2^d3^j\). If \(z_0=2\), the tail cannot be all odd. An all-odd tail would force \(z=n\) by its exact endpoint formula and then \(z_0=1\) by translation. Thus \(u<j\), and \(3^{p+u}\le2^{d+1}3^{j-1}<2^d3^j\). Each contradicts \(D<1\).

## 2. Extra odd cost from a finite ordinary prefix bound

**Theorem D2.** Fix nonnegative \(b,L\). Assume that every positive integer \(q\) with \(2^b q<4\cdot3^b\) satisfies
\[
       2Q_r(q)-r\le L\qquad\text{at every native clock }r.
\]
For \(K\ge b\) with
\[
       4^{K+1-b}2^b\ge 3^{K+1-b}2^{L+1}3^b,
\]
every visitor in D1 must spend **more than \(K+j+b\) odd steps**. The same finite set of ordinary sources works at every such precision and every upper phase. For example, the parent packet's kernel certificate covers every required positive source within its range through 648 for \(b=12,L=22\). The inequality holds for \(K\ge84\), so the protected lower cost is then strictly greater than \(K+j+12\).

A complete verification can stop at each tested source's first hit of 1 and account for the continuing 1,2 cycle. The largest excess can occur earlier. At a fixed positive source the all-prefix excess is bounded **if and only if** that source reaches 1. For the nontrivial direction, suppose it never reaches 1. Every odd input \(x\) satisfies \(3x+1\le(7/2)x\). Therefore a path of \(r\) steps with \(p\) odds satisfies \(2^{r+p}T^r(q)\le7^p q\). A bound \(2p-r\le L\) forces \((8/7)^p\le2^Lq\), which bounds \(p\); then \(2^r\le7^p q\) bounds \(r\), an impossibility. Conversely, only finitely many excess values occur before the cycle at 1, after which the excess alternates between two values. Consequently assuming these finite checks at unbounded \(b\) would already imply full Collatz. [Kernel-checked equivalences](PrefixMeaning.lean) [Finite-to-infinite transfer](PrepaidRamp.lean)

**Proof.** Suppose a visitor has \(K+j<k\le K+j+b\). Split its lower path before the last \(j\) clocks. This prefix has more than \(K\) odd inputs. Cut off its initial segment through \(b\) odds, reaching the ordinary positive integer \(z'\). At each odd step, shifted height \(x+1\) is multiplied by \(3/2\); an even step cannot increase it. Consequently \(z'<(3/2)^b n\). The remaining lower walk has \(k'=k-b\le K+j\) odds. Apply the integer translation in D1 to this walk. Its origin \(q\) is a nonnegative integer. With \(r\) its prefix clock before its last \(j\) steps,
\[
 z'=q+D'(n-s),\quad 0\le q<D'(s+1),\quad D'=2^r3^{j-k'}.
\]
Since \(n/(n-s)\le2\), we have \(D'<2(3/2)^b\) and \(q<4(3/2)^b\). The translated \(r\)-step path has \(p'\ge k'-j\ge K+1-b\) odds, so \(q\ne0\). Its actual prefix bound implies
\[
 (4/3)^{p'}\le 2^L 2^r/3^{p'}\le 2^L D'<2^{L+1}(3/2)^b,
\]
contradicting the threshold. A tempting shortcut would translate the original walk by a fraction of denominator \(3^b\) before removing those \(b\) odds. Positivity of the translated start would then be unjustified. For instance the signed odd branch sends \(-1/9\) to \(1/3\). Removing the actual prefix first keeps every translated state used in the sign argument integral.

## 3. The least extra cost for an inverse descent on a ternary fibre

Define \(e_K\) to be the least shortcut clock of a walk with exactly \(K\) odd inputs ending at **the ordinary integer 1**. Repeated laps at 1 are allowed. There is always the \(2K\)-clock row. Define
\[
  b_K=\min\{b\ge0:2^{e_K+b}<3^{K+b}\}.
\]

**Theorem D3.** Among all sufficiently high lifts \(n\equiv1\pmod{3^K}\), the smallest odd count attainable by a coefficient-contracting inverse row at \(n\) is exactly \(K+b_K\). Here contracting means the backward linear multiplier \(2^E/3^k\) is strictly less than 1. At any fixed odd-count cutoff, numerical descent at sufficiently large \(n\) requires this same strict contraction. In particular \(K+b_K\) is also the sharp threshold for ordinary smaller ancestors in arbitrarily high lifts, with the terminal fixed at the original \(n\) for each certificate. This optimization treats direct ancestry of \(n\); D1 and D2 also permit meetings later on the ramp.

For necessity at \(k\le K\), lift a putative row from \(n\) to 1 by subtracting its integral source displacement. The resulting signed path ends at 1, so its origin is at least 1. The nonnegative forward intercept gives \(2^E\ge3^k\). At \(k=K+b\), transfer the last \(K\) odd steps to the same ordinary anchor 1. That suffix costs at least \(e_K\), and the discarded prefix costs at least \(b\). Thus \(E\ge e_K+b\). The quantity \(2^{e_K+b}/3^{K+b}\) decreases with \(b\). [Kernel-checked price bound](RampShadow.lean)

For numerical descent at fixed depth \(k\), an odd inverse row has the form \(x=(2^E/3^k)(n-\beta)\), with \(0\le\beta\le(3/2)^k-1\) by induction over the odd gaps. An even beginning on the forward walk can be stripped from any smaller source. If \(k>0\) and \(2^E\ge3^k\), unique factorization gives \(2^E\ge3^k+1\), which forces \(x\ge n\) whenever \(n\ge 3^k(3^k+1)\). Zero odd steps cannot yield a smaller ancestor. Taking the maximum of these thresholds over a fixed range of \(k\) proves the claim.

**Attainment.** Choose a minimizing walk \((e_K,K,u,1)\). At \(n=1+3^K v\), its ordinary lift starts at \(y=u+2^{e_K}v\). Impose \(y+1\equiv0\pmod{3^{b_K}}\), and write \(y+1=3^{b_K}t\). Then \(m=2^{b_K}t-1\) takes \(b_K\) consecutive odd steps to \(y\), followed by the exact lifted walk to \(n\). Its leading coefficient in \(v\) is \(2^{e_K+b_K}/3^{b_K}<3^K\), so \(0<m<n\) on every sufficiently high lift in the prescribed class. The congruence on \(v\) is one solvable class since \(2^{e_K}\) is a ternary unit. A simultaneous arbitrary initial ramp length \(H\) is obtained by imposing \(3^K v+2\equiv0\pmod{2^H}\), independently by CRT. The two starts now meet every displayed phase \(j\le H\) with exactly \(K+b_K+j\) lower odd steps. [Physical decoder and arbitrarily high ordinary CRT attainment, including the exact contraction equivalence](FibreAttainment.lean)

The lifted paths can also be chosen with \(n=2^h-1\). Impose
\[
   2^h\equiv 2-3^K(u+1)2^{-e_K}\pmod{3^{K+b_K}}.
\]
For \(K\ge1\) the right side is a unit, and 2 generates the ternary unit group. Indeed \(v_3(4^{3^a}-1)=a+1\) by induction using the binomial formula. Thus the admissible \(h\) form an infinite arithmetic progression. For \(K\ge2\) it lies in \(h\equiv1\pmod6\). These are individual positive ordinary Mersenne sources. The construction certifies a merger to a smaller integer and gives no automatic proof of that integer's convergence.

A simple closed formula uses the \(K\) trivial two-step loops regardless of optimality. In the construction put \(u=1\), \(E=2K\), and choose \(b\) with \(2^b4^K<3^{K+b}\). The witness satisfies
\[
   m+1=(2/3)^b\bigl(2+4^K v\bigr),\qquad n=1+3^K v,
\]
and is strictly smaller for every positive compatible \(v\). At \(K=1\), \(n=9v+4\), the three-step witness \(m=8v+3\) spends exactly two odds to reach \(n\). It gives equality in D1's integer lower bound at **all** phases, including every Mersenne \(h\equiv5\pmod6\). The witness itself occurs in PR197. D1 proves its optimality against all smaller starts and all physical clocks.

## 4. Growth of the optimal cost

**Theorem D4.** We have \(1\le e_{K+1}-e_K\le2\), and \(2^{e_K}/3^K\to\infty\). Thus \(b_K\to\infty\). [Kernel-checked increment and divergence](InversePrice.lean)

Deleting one odd input costs at least one native clock; appending one lap at 1 costs two. If \(2^{e_K}/3^K\le B\), the nonnegative carry forces every minimizing origin \(u\le B\). The finite set of such origins which reach 1 has bounded first-hit clocks and odd counts. Write those as \(t(u),p(u)\). At depth \(K\ge p(u)\), the only later visits to 1 from that source have cost \(t(u)+2(K-p(u))\). Their normalized multipliers grow as \((4/3)^K\), excluding every bounded \(B\). This uses no assertion that every member of the initial finite set reaches 1.

The exact finite formula is
\[
   e_K=2K-\max_{\substack{u\text{ reaches }1\\p(u)\le K}}
        \bigl(2p(u)-t(u)\bigr).
\]
Odd sources suffice: stripping an even start strictly improves a candidate with the same odd count. Given a verified upper price \(E\), sources \(u>2^E/3^K\) cannot improve it. This lets a bounded search certify unrestricted minima at the requested depths.

| \(K\) | \(e_K\) | \(b_K\) | A minimizing source | Sufficient source ceiling |
|---:|---:|---:|---:|---:|
| 20 | 40 | 15 | 1 | 315 |
| 40 | 69 | 10 | 31 | 48 |
| 60 | 106 | 19 | 1215 | 1913 |
| 80 | 139 | 21 | 2919 | 4714 |
| 100 | 173 | 25 | 6171 | 23230 |
| 120 | 206 | 28 | 35655 | 57230 |

The finite program obtained all \(K\le120\) after scanning odd sources through 103131. It stops each trajectory after 120 odd inputs or its first hit; it needs no extrapolation about a remaining positive trajectory. It tested 4,706 inverse compositions independently through \(K=7\). It also examined all starts \(m<n\le512\) on the two admissible ternary residues through 72 lower shortcuts, finding 2,401 actual ramp contacts. Direct physical replays of the optimal Mersenne lifts used \((K,h)=(1,11),(2,13),(3,253),(4,919)\). [Reproduction program](replay.py)


## 5. Exact odd cost at the second halving after the peak

**Theorem D5.** Write \(n=2^H v-1\), \(H\ge5\), \(v>0\), with \(4\mid3^H v-1\). Put \(P=3^H v-1\) and \(Y=P/4\). Among **all** positive \(m<n\) and all native clocks \(e\) with \(T^e(m)=Y\), the minimum of \(Q_e(m)\) is **exactly \(H-1\)**. At the preceding point \(P/2\), every earlier bound D1 or D2 still applies. Indeed \(P/2\equiv1\pmod3\) has only the even incoming edge from \(P\), and \(P/2\ge n\). [Exact minimum and the preceding barrier](CoastCollapse.lean)

The attaining source is \(m=3\cdot2^{H-2}v-1=3(n+1)/4-1<n\). Its first \(H-2\) odd steps end at \(3^{H-1}v-1\); one even and one odd step reach \(Y\). These last two steps use \(3^{H-1}v\equiv3\pmod4\). The neighboring peak merger itself occurs in PR192. Advancing the smaller arm one step saves one odd departure while its source remains strictly below \(n\).

For optimality suppose a smaller visitor uses \(k\le H-2\) odds. If it has any even input, keep that even step and bound away every other even step in the upper estimate for shifted height. An odd applies \(z\mapsto3z/2\) to \(z=x+1\), and an even applies \(z\mapsto(z+1)/2\). This gives
\[
 Y+1\le (3/2)^k(m+2)/2
       \le (3/2)^{H-2}(n+1)/2
       < (3/2)^H(n+1)/4 <Y+1 .
\]
With no even input, \(v_3(Y+1)=1\) forces \(k\le1\); but \(H\ge5\) gives \(Y+1>(3/2)(n+1)\). The condition on \(H\) matters: \(n=15\) has \(H=4\), \(Y=20\), and \(13\) reaches 20 in one odd step.

The cost change across this physical step can be arbitrarily large on actual integers. Given any \(H\ge5\) and \(K\), impose \(v\equiv3^{-H}\pmod4\) and \(2^H v\equiv s+1\pmod{3^K}\) for \(s=0\) or 1. CRT supplies arbitrarily large positive odd \(v\). At \(P/2\) every smaller visitor needs more than \(H+K\) odds, or more than \(H+K+12\) for \(K\ge84\) using the finite certificate. At \(P/4\) the minimum is exactly \(H-1\). A proof that charges a single extra odd budget uniformly over successive postpeak points therefore fails even on these explicit positive families.

**One actual family on the other exit.** When \(H\ge5\) and \(3^H v\equiv43\pmod{256}\), the peak has exactly one factor of two. Write \(3^{H-2}v=256a+147\). The original peak and the earlier peak \(256a+146\) meet after eight shortcuts at \(81a+47\), with respective odd counts 2 and 4. This coincidence and a different smaller starting representative appear in PR192. Advancing the lower opening along three odd steps gives \(m=27(n+1)/32-1<n\), from which the same meeting costs \(H-1\) odd departures. The kernel replays the two base words and transports them at the original native clock. These residues do not exhaust the single-halving exit. [Ordinary certificate](CoastCollapse.lean)

The finite control also replays 96 second-halving witnesses, finds 858 ordinary contacts in its smaller-source/clock comparison, and replays 90 members of the eight-clock family. [Recorded output](CONTROLS.txt)

## Scope, exact precedents and the unresolved step

Main is frozen at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. This packet uses elementary physical path arithmetic and the positive trivial cycle. A logical exclusion of all positive cycles or escaping trajectories is not imported.

| Frozen source | Exact comparison |
|---|---|
| PR146, `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/MERSENNE_EXPONENT_DESCENT.md` | Two reverse gaps of 2 followed by arbitrarily many gaps of 1 give a positive Mersenne family. An inverse first-crossing count excludes some depth-bounded visitors. D3 optimizes over **all** histories at increasing precision. |
| PR197, `1f0f496fbea37792439feada6106eaaff596bcd1`, `research/ayh-resource-reset-20261124/unconventional/FIRST_ATTACHMENT_CLOCK.md` and `FRESH_ASCENT_BARRIER.md` | The first paper gives the same \((8n-5)/9\) witness and bounds clock surplus after a visitor's own ascent. The second bounds the odd surplus at a fresh attachment using the signed anchor \(-1\). D1 uses the positive ternary source anchors 0 and 1, and includes visitors attaching at the start. |
| PR201, `d21bac748e705a64b6b57a7996a8ad6282f0bcbf`, `research/six-hour-20261127/coupling/PEAK_RIGIDITY.md` and `research/six-hour-20261127/escape/COMPARABLE_ANCESTORS.md` | The first classifies smaller Mersenne visitors in a postpeak clock cone. The second gives all-clock protection on a large density subset for each fixed allowed word. D1 and D2 protect every ordinary lift under their explicit budget and apply throughout the actual prepeak ascent. |
| PR192, `ae48a04cca29abe5fc8273bcda45e7eee0874896`, `research/astra-sixhour-20261127/transport/ORIGINAL_FLOOR_SIEVE.md` | A different canonical comparison uses virtual controls, an all-depth ternary density-point limit and a finite absolute control at 353. Those canonical ranks and the Haar statement are not hypotheses of D1–D5. At this same frozen PR head, `research/astra-minimum-source-20261124/renewal/README.md` and `UpperRepresentative.lean` already give the neighboring peak merger and the eight-clock residue. D5 adds minimum-cost optimality and the comparison with the preceding point, including the compensated visitor budget. |
| PR206, `640bf7e511831a0ffc4f00462f12df81f8a8a619`, `research/clock-itineraries/README.md` | The fixed-clock itinerary theorem already constructs many physical routes at a prescribed target. The presence of those routes does not by itself lower the source. D3's price uses the target 1 and a strictly contracting coefficient instead. |

An ordinary \(n\) can have quite different behavior after its initial finite ramp. Nor does an arbitrary cofactor \(v=(n-1)/3^K\) obey the decoder's congruence for a winning path. For example at \(n=7\), every smaller positive start follows a directly checkable orbit to 1 that misses 7, so no pure inverse decoder can supply a smaller ancestor there. The missing global step is to find an actual later common endpoint for **each fixed residual source**, at whatever clocks its lower bound requires. The computations and transfer inequalities above do not supply such coverage.

Run `bash check.sh` with Lean 4.34.1 and its compatible Mathlib build on the Lean search path, then `python -B replay.py`. The Lean results and the finite program have distinct evidence boundaries. The full ordinary CRT attainment, inverse clock bounds, sharp second-halving minimum and divergence have corresponding kernel checks. The Mersenne discrete logarithm specialization and the conversion from strict coefficient price to sufficiently high numerical row minima are written proofs. All nineteen printed declarations in this packet use only `propext`, `Classical.choice` and `Quot.sound`.
