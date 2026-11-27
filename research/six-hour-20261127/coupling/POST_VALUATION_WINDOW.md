# A growing extra clock delay at the original cofactor-one parent

**Proposed written theorem from the pinned finite-word absorption bound.** Use the ordinary shortcut map $T$, the Mersennes $M_m=2^m-1$ and their peaks $P_m=3^m-1$. For each positive integer $k$, take the actual $m=12\cdot2^{18k}-1$ and $H=18k+4$. Let $K\ge16$ and $0\le J\le\log_2 K$ be integers. The number of $1\le k\le K$ for which **some** positive $x<M_m$ and independently chosen clocks $i,h$ satisfy
\[
 i\le H+J,\qquad h\le v_2(x+1)+H+J,\qquad T^i P_m=T^h x
\]
is at most
\[
 C\left(\log(2K)+\frac{2^J K}{\sqrt{\log(2K)}}\right)
\]
with an absolute constant. Consequently for every $0<\epsilon<1/2$, on a natural-density-one set of these $k$, even a source-dependent choice of any smaller ordinary visitor fails in the window with the **additional** allowance $J=\lfloor(1/2-\epsilon)\log_2\log_2 k\rfloor$ (ignoring the finitely many small indices). Neither canonical leastness nor convergence enters this separation. The statement permits a paid canonical query taking another route. Its exceptional count is for initial parameter intervals $[1,K]$.

The fixed-parent obstruction **through $H$ for every $k$** is prior PR 192, which also gives the signed nonzero lemma used below. The all-smaller-visitor reduction in the present research packet permits these two clocks and supplies grade equality at an actual meeting. The new step counts marked *earlier* signed trajectories against the valuation time that varies with the original parameter. [Prior fixed-parent delay](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/descent/POSTPEAK_DELAY.md) · [All-visitor rigidity](PEAK_RIGIDITY.md) · [Ordinary delayed source](DELAYED_UNIT.md)

## Reduction to a finite collection of marked rational values

Discard $O(\log(2K))$ small $k$ so that $3(H+J)<m$, $18k\ge J$, and $H\ge\lfloor\log_2(18K+4+J)\rfloor$. The [rigidity theorem](PeakRigidity.lean) sends every proposed meeting to a synchronized meeting of $P_m$ with $P_t$ for $1\le t<m$ at clock $i$. It also gives exact equality of the augmented odd grades $m+Q_i(P_m)=t+Q_i(P_t)$. By the earlier delay the meeting must occur at $H+j$ with $1\le j\le J$. Set $q=m+1-t\ge2$ and $U=U_{18k}=(3^{m+1}-1)/2^H$.

Let $d_q=3^{-q}-1$, and on rationals with odd denominator use the same shortcut rule, reading numerator parity. Write $r_q(a)$ for the odd count in the first $a$ signed clocks. The exact signed state of the earlier trajectory at clock $a$ is
\[
 \big(e_q(a),\,v_q(a)\big)=\big(r_q(a)-q,\ T^a d_q\big).
\]
Both entries will be needed. Since $P_t=2^H3^{-q}U+d_q$, $P_t$ and $d_q$ have identical parity words through clock $H$. At $H$ the earlier ordinary site equals $3^{e_q(H)}U+v_q(H)$. The native site equals $U$, with one odd departure from $P_m$ before $H$. If $p$ and $\ell$ are the odd counts of the native and earlier post-$H$ suffixes up to the meeting, augmented-grade equality gives $e_q(H)=p-\ell$ and $q=r_q(H)+\ell-p\le H+J$.

A word $w$ of $j$ ordinary shortcuts has the affine endpoint $(3^{p(w)}x+B(w))/2^j$. After cancellation of the equal $U$ slopes, equality of endpoints forces
\[
 v_q(H)=\frac{B(w_{\rm native})-B(w_{\rm earlier})}{3^\ell}.
\]
The recursion $U_{a+1}=U_a+2^{a+3}U_a^2$ gives $U_{18k}\equiv U_J\bmod2^J$ on the retained indices. Thus at each $j\le J$ there is just **one** possible native word. At most $2^j$ earlier words remain, each specifying both entries $(e_q(H),v_q(H))$. Across all $j$, fewer than $2^{J+1}$ marked states can qualify. Different clock lengths or words may specify the same state.

A signed trajectory from any $d_q$, $q\ge2$, visits each marked state at most once. Indeed equality of the integer entries at two different clocks forces only even departures between them. Returning to the same rational value then forces that value to be zero. The signed nonzero lemma in PR 192 excludes zero throughout each of these rational paths.

## Counting the trajectories that remain distinct

Let $Q=18K+4+J$ and $g=\lfloor\log_2 Q\rfloor$. Couple neighboring indices through the exact relation $d_q=3d_{q+1}+2$. The finite-word absorption estimate for $(s,d)=(1,2)$ bounds by $C_0\,2^g/\sqrt g$ the number of source residues modulo $2^g$ failing to give an identical affine endpoint by clock $g$. It is the **word identity** that is used here. It follows from the oriented-process proof on binary residues and specializes equally to the odd-denominator rational representative of a successful residue. This use requires no convergence assertion for signed rational starts. [PR 146 affine bound](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) · [Parity-word absorption proof](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)

As $q$ ranges from 2 through $Q-1$, the residues $d_{q+1}=3^{-(q+1)}-1$ are distinct in each consecutive block of $2^{g-2}$ indices by the exact order of 3 modulo $2^g$. At most eight such blocks cover the index range. Hence all but $O(Q/\sqrt g)$ neighboring edges absorb by $g$. On each successful edge, the two rational positions agree, and the grade of the trajectory from $d_{q+1}$ exceeds the other by one because the initial slopes are 1 and 3. Their marked states therefore agree at the meeting and at clock $g$. Removing failed edges leaves $O(1+Q/\sqrt g)$ runs of indices. All trajectories in any one run have identical marked states at every clock $a\ge g$.

On each such run every qualifying marked state can be visited at only one clock. Distinct retained $k$ have distinct $H=18k+4\ge g$. The count is therefore at most $2^{J+1}O(1+Q/\sqrt g)$, in addition to the discarded indices. Since $Q=O(K)$ this proves the theorem. For the stated density consequence take the increasing allowance bounded on $[1,K]$ by $(1/2-\epsilon)\log_2\log_2 K$.

The estimate extends the window in the native branch for typical original parameters. PR 192 exhibited actual paid repairs for the first thirty prescribed parameters and an infinite signed canonical address. The [gap-four closure](OFFSET_FOUR.md) uses a canonical source whose lower reaches an earlier Mersenne. The [paid original-parent classes](PAID_CHECKPOINTS.md) avoid this native comparison. Whether every prescribed $k$ has some paid route or eventual desynchronised merger remains open.
