# A pointwise bound through every gap of the same upper certificate

Let $s$ be the least positive bad integer in the bounded alternative, let $z$ be the original least canonical reverse disagreement, and use its actual first upper hit. By the [absolute orientation theorem](ORIGINAL_CANONICAL_FLOOR.md), write
$$z=1+2\cdot4^\ell u,\qquad L=T^{2\ell}z=1+2a,\qquad a=3^\ell u,\quad u>0\ {\rm odd},\quad\ell\ge2.$$
The lower $L$ is bad and the positive $a$ is good. The upper $3z$ reaches $T(a)$ after $2\ell+2$ shortcuts with exactly $\ell$ odd departures. All intervening states exceed one. Indeed the first five steps are the positive lift of $3,5,8,4,2,1$ with a nonzero transfer, the subsequent pairs start at $1+4b>1$ and visit $2+6b>1$, and the last state before the meeting is $1+3a$. The first step of $a\ge9$ is odd. Thus the actual first-hit costs satisfy
$$
 H(3z)=H(a)+2\ell+1,\qquad P(3z)=P(a)+\ell-1,\qquad J(3z)=J(a)+3.
$$
At a captured source $L=s$, so the unbounded portion of the original certificate is precisely the first-hit suffix of $(s-1)/2$. The physical meeting, lower value and prefix grade are [strict Lean theorems](CanonicalTripleFloor.lean).

## The first full even block

During consecutive odd departures $T(2v+1)=2T(v)+1$ for odd $v$. When that true good arm first reaches an even $v=2^e b$, $b$ odd, the continuing actual good suffix begins at $b$. The bad child $2v+1$ reaches $1+3\cdot2^{e-1}b$ in two steps.

* If $e=2k+1$, another $2k+1$ steps physically meet $T(3^k b)$. Thus $3^k b$ is bad. In particular $e=1$ is impossible.
* If $e=2k\ge2$, another $2k-2$ steps give the bad child $1+2\cdot3^k b$. The coefficient on the same actual continuing suffix $b$ is now $c=3^k$. After $j$ subsequent simultaneously odd departures the exact affine relation is $Y_j=2c\,b_j+2c-1-2(c-1)(3/2)^j$. Its additive offset changes from $1$ to $2-c<0$ on the first such departure.

Both exit identities use $T^2(1+4w)=1+3w$. Keeping the coefficient $c$ fixed after the first even exit only describes subsequent shared odd steps, and replacing $b$ by $3^k b$ would change the supplied certificate. The argument below follows $b$'s actual word through all later gaps.

**The first loss of binary alignment forces a real upper peak.** Let $u_q$ be the clock just after the $q$-th lower odd departure. Let $j_q$ be the clock just before the next upper odd departure after $q$ prior odds, setting $j_r=H(a)$ at the true terminal. Use $u_0=j_0=0$. Write $d_q=j_q+1-u_q$ and $c_q=T^{u_q}L-2^{d_q}T^{j_q}a$ as a rational number. A rank is paid when $d_q\ge0$, which makes $c_q$ integral. If $l$ evens precede the next lower odd, the physical affine updates give
$$c_{q+1}=\frac{3c_q+2^l-2^{d_q}}{2^{l+1}}.$$
The formula remains valid across unpaid ranks with dyadic rational centers. Starting from $d_0=1,c_0=1$, every initial uninterrupted sequence of paid ranks has $c_q\le1$: the right side is at most $3/2$ when $d_q\ge0$ and $c_q\le1$, and an integral output is at most one. At the first unpaid rank the same bound $c_q\le3/2$ holds. Thus its actual upper value $T^{j_q}a=2^{-d_q}(T^{u_q}L-c_q)$ is at least $2s-3$. For $s\ge25$ it is not the terminal one. This uses only the global lower floor.

There is a positive averaging recurrence even when the center is not integral. Put $Y_q=T^{u_q}L$ and $R_q=1-c_q/Y_q=2^{d_q}T^{j_q}a/Y_q$. Write $y=Y_q/2^l$ for the next departing lower odd. Direct division by $Y_{q+1}=(3Y_q+2^l)/2^{l+1}$ gives
$$
 R_{q+1}=\frac{3yR_q+2^{d_q-l}}{3y+1}.
$$
At an unpaid rank the value being averaged with $R_q$ is at most $1/2$. As long as $c_q\le0$ there, $R_q$ drops by at least $1/(2(3y+1))$. Large paid reserves can inject a positive term of size $2^{d_q-l}/(3y+1)$ on the same actual certificate. A change from $c_q\le0$ to $c_{q+1}>0$ must have $0<c_{q+1}<1/2$ by the unnormalized recurrence. Its dyadic denominator is at least four. At this very rank the actual good upper is $2^kY-u$ with $k\ge2$ and $1\le u<2^{k-1}$, hence at least $4s-1$. This quantitative recovery condition uses the original lower floor. The averaging identity gives monotonicity on the stated portions and supplies no monotonicity through arbitrary alternations.

On the distinguished restricted bad cycle this first loss has a more specific form. The lower has $l\le1$, and the upper advances at least one clock to its next odd, so $d_q$ can drop by at most one. A first loss has previous $d=0$, new $d=-1$, $l=1$, and consecutive upper odds. Its previous integral center is $-1-4k$ for some $k\ge0$: the new center $(3c+1)/4$ must be a nonintegral half integer, and $c\le1$. Thus, with $Y=T^{u_q}L$, the actual upper is $2Y+1+6k$. In fact $k\ge1$. At an odd cycle phase $Y$ the lower neighbor $(Y-1)/2$ is good, and the ordinary odd-run comparison forces the bad $Y$ to merge with $2Y+1$. At an even phase $Y=2x$ with $x$ an odd bad phase, $2Y+1=4x+1$ also merges with $x$. Hence $2Y+1$ is bad at either phase and cannot be the actual good upper. This rules out the zero error $k=0$ at a first loss; positive errors can occur in ordinary finite controls. [Pinned neighboring labels and physical comparison](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md)

The threshold on the center fails after a lost rank is recovered. For the ordinary canonical $z=558349308735329$, the reduction with $\ell=2$ gives $L=314071486163623$ and $a=157035743081811$. For the first 45 clocks the lower stays above or at $L$, has no consecutive evens, and its odd sites satisfy the distinguished numerical ceiling with $s$ replaced by $L$. The first unpaid rank is $q=10$, with $(u_q,j_q,d_q,c_q)=(14,12,-1,-13/2)$ and $T^{12}a=2263868064755369$. After this actual upper excursion the rank data $(41,41,1,3)$ and $(42,42,1,4)$ occur at $q=27,28$. Both numerical inputs converge, in 199 and 198 clocks respectively. This is a control for the local assertion, not an original bad source. [Exact first-hit and prefix replay](check_records.py) · [Numbers](../../../reports/astra-sixhour-20261127/descent/distortion-records.json)

## An explicit bound from a single upper rank

Let $r=P(a)$ be the actual number of odd departures before its first hit of one, and put $H=H(a)$. Assume $s\ge25$. Suppose every odd lower state on the first $H+1$ clocks from $L$, including the endpoint if odd, is at most $8s$. All lower states are at least $s$ by global leastness. They are all below $13s$, since $L$ is odd and an even state follows an odd shortcut or further halvings. The odd ceiling is automatic on the distinguished cycle, including every captured original. The six off-cycle types have no such established ceiling. For each of them the alternative to the bound below is an actual odd state above $8s$ by clock $H+1$ on its lower, even with arbitrary native halving gaps.

Define $U_1=0$ and
$$U_{q+1}=1000(1+q+2^{U_q}).$$
Then
$$
   \boxed{\qquad s\le 5r+13\quad\hbox{or}\quad H\le U_{r+1},
                 \qquad s\le 1+2^{H+1}.\qquad}                         \tag{1}
$$
In particular the protected floor is bounded explicitly at every fixed rank of this **one actual original upper**. The resulting pointwise rank lower bound grows at least as an iterated logarithm of $s$, up to an additive constant. PR195's completed-grade theorem constrains long upper marks or repeated classes over a population of phases, and its language exclusions treat cycle hypotheses on families. The present estimate applies at the specified original source with a binary gap bound conditional on its preceding physical prefix. Growth in (1) is rapid and supplies no upper bound on the possible actual rank. [Compared PR195 completed-grade result](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/cycles/COMPLETED_GRADES.md)

**Proof.** Write $t_1=0<t_2<\cdots<t_r$ for the clocks of its odd departures and set $t_{r+1}=H$. For $1\le q\le r$, put $d=t_{q+1}+1$. The exact upper prefix through its $q$-th odd and all subsequent even departures gives
$$
 B=\sum_{i=1}^{q}3^{q-i}2^{t_i},\qquad
 3^q L=2^d b+3^q-2B
$$
where $b=T^{t_{q+1}}a$ is the next actual odd suffix, possibly one. Thus $w=1-2B/3^q$ depends on the preceding odd positions and is independent of the new even gap. Every portion of the protected segment containing $n$ odd departures has clock length $h<2n+4$: every factor in the exact step product is at most $(3+1/s)/2$ at an odd site and $1/2$ otherwise, and the starting-to-ending height ratio is below $13$. Thus $2^h<13(3+1/s)^n$. If $d<2q+4$ there is already the needed clock bound. Otherwise the signed rational $w$ shadows $L$ until the $q$-th lower odd departure at a time $t\le2q+4$. This follows by the binary translation on the displayed identity, since after $i$ common departures and $k$ odds the displacement is $2^{d-i}b/3^{q-k}$. The numerator of $w$ is a ternary unit because $B\equiv2^{t_q}\pmod3$. Hence that last departure clears the denominator and yields an integer $c$. It shadows $T^t L$ for the next $d-t$ clocks.

On any matching segment from a positive bad state $V_0\ge s$ to $V_j$, the slope is at most $V_j/V_0$. Its nonnegative affine remainder is at most $V_j m/(3s)$ through $m$ odd departures. Indeed each odd departure at $V_i$ contributes half the later slope, at most $V_j/(3V_i+1)$ by positivity of the later affine correction. In particular $w\le1$ gives $c\le13+5q$. On the other side $2B/3^q<2^{t_q}$ by the geometric sum of $3^{-i}$, so $c\ge-13\cdot2^{t_q}$. A positive $c\ge s$ already proves $s\le5r+13$. The underlying positive affine remainder inequality, with denominators cleared and no record assumption, is [kernel-checked as floor_affine_remainder](CanonicalTripleFloor.lean).

Here are explicit bounds for the remaining alignment length.

* For $c=-m<0$ the ratio of negative magnitude to the positive physical state drops by $(1+R)/(3V_i+1)$ at each shared odd departure. The argument of [CarryAlignment.lean](CarryAlignment.lean) bounds their number by $(3\max V_i+1)m/s<25m$ since odd $V_i\le8s$. The step-product bound above gives clock length below $50m+4$.
* For $0<c<s$, the control is good. Before its first one its odd sites are distinct and all except possibly the first are ternary units. If it matches $n$ odd departures before this first hit, each of those control sites is at most $8c+(8/3)n$ by the same affine remainder bound at the corresponding odd physical site $V_i\le8s$. Up to $K$ there are at most $K/3+2$ positive odd ternary units. Thus $n\le1+(8c+(8/3)n)/3+2$, giving $n\le24c+27$. This part takes at most $48c+58$ clocks. If the control reaches one, eight copies of its two-clock lap cannot still match: the corresponding lower $v\le8s$ would then reach $1+(3/4)^8(v-1)<s$. Hence the total match has at most $48c+73$ clocks.
* Zero can match at most three all-even clocks by the step-product bound.

Combining with $t\le2q+4$ gives $t_{q+1}\le1000(1+q+2^{t_q})$ unless the claimed linear rank bound already holds. Induction gives (1). Finally $a\le2^H$ since every physical step divides by at most two and the endpoint is one, while $s\le L=2a+1$. The case $q=1$ in fact has $w=1/3$ and $c=1$ at clock one, so its first gap already has an absolute bound.

**Arbitrary fixed peak ratio.** For any fixed $K\ge 2$, the same fixed-rank boundedness holds when all lower states are at most $Ks$. The clock bound becomes $2n+1+\log_2 K$. Only the positive-control packing argument needs replacement. A simple ordinary path has $O_\eta(N^\eta)$ visits to any interval of length $N$, for every $\eta>H_2(\log_3 2)$ below one. This follows, for example, from the scalar specialization of the [translated-strip proof](PAIRED_INTERVALS.md) with pairs $(x,x)$: remove the last $O_\eta(\log N)$ clocks of the simple segment and observe that fixed-deadline images of all remaining visits are distinct. The positive control before its first hit is simple; every matching site is at most $K(c+n/3)$. Consequently $n\le A_\eta(1+K(c+n))^\eta$. If $n>c+1$, this gives $n^{1-\eta}\le A_\eta(3K)^\eta$. Its matching tail after hitting one costs $O(1+\log K)$ as before. The negative and initial-control bounds have constants depending only on $K$, so the same induction bounds $s$ in terms of $K,r$. Thus bounded ranks with arbitrarily large protected floors would force the odd lower peak divided by $s$ to exceed every fixed constant by the endpoint deadline. This is a pointwise tradeoff, not a proof of the physical return below $s$.

The multiple-gap induction and packing arguments are written results. The Lean file checks the exact prefix, the two first-exit alternatives, and the floor-relative affine correction used by the induction.

There is a complementary exact cost identity over this same certificate. Write $D_V(j)=\prod_{i<j,\,V_i\ {\rm odd}}(1+1/(3V_i))$, and let $d_j=P_j(L)-P_j(a)$. Comparing the two exact positive products at the actual hit $H$ yields
$$
 d_H\log3+\frac{P_H(L)}{3s}\ \ge\ \log\frac{sa}{2a+1}\ \ge\ \log(s/3).
$$
Consequently $H\ge(3/2)s\log(s/3)$ or the lower has gained at least $\tfrac12\log_3(s/3)$ odd departures over the good certificate. Unlike (1) this last inequality only requires the lower floor through $H$. A large grade difference, a large gap budget and a very long good certificate all remain consistent with absence of a smaller bad ordinary point. This is the unresolved step for the coupled word argument.
