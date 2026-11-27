# Minimum source height at every compensated grade of one ordinary reference

**PROPOSED.** Fix one supplied positive reference $y$ and its initial integer grade $j\ge0$. For a requested initial grade $N\ge j$, allow every positive ordinary start $u$ for which some common clock $h$ satisfies
$$
    T^h u=T^h y,\qquad N+P_h(u)=j+P_h(y).                       \tag{1}
$$
Write $m_y(N)$ for the least such $u$. It exists at every grade. Choose a clock $h$ with $P_h(y)=N-j$ and take $u=2^h T^h y$. Its first $h$ steps are halvings. Every positive orbit has arbitrarily many odd departures, since a positive integer cannot halve indefinitely.

The graded minimum has the following mutually exclusive forms.

* If $y$ reaches one at clock $H_0$ after $p_0$ odds, put $I=2(j+p_0)-H_0$. For **every** $N$ with $e=2N-I\ge0$, the exact answer is $m_y(N)=2^e$.
* More generally, when $y$ reaches a positive cycle of least period $L$ and odd count $q$, then $m_y(N+q)=2^L m_y(N)$ for every sufficiently large $N$. The threshold may depend on the supplied finite reference and cycle. This includes any hypothetical nontrivial positive cycle.
* If $y$ is not eventually periodic, put
$$
       A_y=3^{-j}\lim_{h\to\infty}2^h T^h y/3^{P_h(y)} .
$$
This limit is positive and finite. As $N\to\infty$, **every** permitted start satisfies $u/3^N\longrightarrow A_y$, uniformly over all its eligible values at that grade. In particular $m_y(N)\sim A_y3^N$.

Thus a fixed nonperiodic Mersenne peak $y=3^j-1$ has an actual open relative gap around the nominal high-grade height $3^N$. Indeed $A_y>1$: in the shifted height $v+1$, each even step contributes the factor $1+1/(v+1)$ to the product, odd steps contribute one, and $y$ is even. The shifted and unshifted limits coincide since the nonperiodic orbit tends to infinity. Consequently all sufficiently high grades miss a whole interval $[(1-\epsilon)3^N,(1+\epsilon)3^N]$ for some $\epsilon_y>0$. The radius permits perturbations of unbounded integer size. For a periodic reference every fixed constant multiple of $3^N$ is eventually below the minimum.

## Proof for a supplied upper hit

Continue any merger (1) until both trajectories hit one together, after time $H_0$. If the visitor at any individual hit has clock $H$ and $p$ odds, the cycle through one gives
$$
                        2(N+p)-H=I .
$$
Conversely this equality between two actual hits allows extension to the same clock with the same augmented grade: extend the visitor by $2(j+p_0)$ and the reference by $2(N+p)$ clocks. At a positive integer $x$, $2T(x)\le4^{x\bmod2}x$. Multiplying on the visitor path gives $2^H\le4^p u$. Hence $2^{2N-I}\le u$ whenever $2N\ge I$. The pure power $u=2^{2N-I}$ has a hit with $p=0$ at clock $2N-I$. This proves the formula, without estimating any unknown visitor's stopping time. The charge test and the height lower bound generalize the corresponding tower identities in [round twelve, §2](../../astra-global-closure-20261124/round12/arithmetic/README.md). Optimizing over all positive sources also supplies the attaining source at each eligible grade.

## A nonperiodic reference

For each nonperiodic positive $v$ define
$$
      U(v)=v\prod_{i:\ T^iv\ {\rm odd}}\left(1+\frac1{3T^iv}\right).
$$
The uniform reciprocal bound on simple paths proves convergence and $U(v)\ge v$. More precisely $U(v)/v\to1$ uniformly on paths whose least visited positive integer tends to infinity. Multiplication along a single edge gives $U(Tv)=3^{v\bmod2}U(v)/2$. Linkage (1) therefore gives the exact identity $U(u)/3^N=U(y)/3^j$.

Fix any small integer gate $b$. Among all sources satisfying (1), it can be visited at only one elapsed clock. Two such sources coincide with the reference at some common time, by extending both of their witnesses. If their visits to $b$ were at different times $v_1,v_2$, advancing their common endpoint by $v_1+v_2$ would make two different iterates of $b$ coincide. Its future is nonperiodic. At a fixed time $v_1$ there are only finitely many positive ancestors of $b$, since $u\le2^{v_1}b$. Each $u$ has at most one permitted grade $N$: advance two witnesses to their common later clock. Thus for any finite set of small gates, all sufficiently high-grade permitted sources avoid all of them for their entire future. The product estimate implies $u/3^N\to U(y)/3^j$. For a peak $3^j-1$ the positive shifted product used in round thirteen yields the strict relative gap stated above. [Simple-path estimate and synchronous visit-time rigidity](../../astra-global-closure-20261124/round12/arithmetic/README.md) · [shifted-height product](../../astra-global-closure-20261124/round13/trace/FINITE_FAMILY.md)

## Exact eventual scaling on every positive cycle

Fix a phase $b$ with least period $L$ and $q$ odd steps. Let the reference first reach $b$ at $H_0$ with $p_0$ odds. Here $q>0$ and $\lambda=L/q>\log_2 3$, by the positive odd correction around one lap. For a linked visitor first reaching $b$ at $H$ with $p$ odds we have $H\equiv H_0\bmod L$ and
$$
           L(N+p)-qH=I_0,\qquad I_0=L(j+p_0)-qH_0.
$$
Both assertions follow by extending a common meeting to a later shared visit to $b$. Conversely these two equations at any actual visits imply linkage, since adding complete laps aligns the clocks and grades. The departed path to a *first* phase visit is simple, so its positive product $D=\prod_{\rm odd}(1+1/(3x))$ is bounded above by an absolute constant. From $2^H b=3^p uD$ we obtain
$$
         \log_2 u=\lambda N+(\lambda-\log_2 3)p+O_y(1).          \tag{2}
$$
The all-even candidate at grade $N$ costs $\log_2u\le\lambda N+O_y(1)$ since the reference on its eventual cycle accumulates $q$ odds per $L$ clocks. Thus any minimizer has $p\le P_y$ for a fixed finite integer $P_y$.

Run the minimizing first-hit word backwards from $b$. Its $p$ odd inverse letters $O(v)=(2v-1)/3$ split the even letters $E(v)=2v$ into $p+1$ blocks, the last nearest the source. If $p=0$ the word already consists only of halvings in forward time. Otherwise take $D=2\cdot3^{p-1}$, so $2^D=1\bmod 3^p$. Any nonterminal block of at least $D$ even inverse letters can have $D$ of them moved to the terminal block. Removing these doublings preserves the current residue modulo $3^p$, and at most $p$ subsequent odd inverses each cost one ternary digit. Every subsequent inverse remains legal on a positive integer. The restored terminal doublings preserve the total clock and grade and still give a word visiting $b$. The new source is strictly smaller: pushing $E^D$ past any odd inverse toward the source changes $O(E^D v)=(2^{D+1}v-1)/3$ to $E^D(Ov)=(2^{D+1}v-2^D)/3$, with strict decrease. This algebraic comparison may pass through positive rational intermediate values while commuting the formal maps; legality of the final reordered word was proved separately by residue preservation. The reordered word still links by the clock congruence and the charge, even if the recorded visit to $b$ is now not first.

All nonterminal even blocks of a minimizer are therefore shorter than $2\cdot3^{P_y}$. Since $H=\lambda(N+p)-I_0/q$ and $p\le P_y$, the terminal even block eventually has at least $L$ steps. Remove $L$ of them. The source is divided by $2^L$, the phase clock drops by $L$ with equal phase, and the number of odds is unchanged. At grade $N-q$ this is an eligible source. Conversely, prepending $L$ forward halvings to any grade-$N-q$ optimizer gives an eligible source at grade $N$. This proves the asserted exact equality. It also proves that every high-grade optimizing path begins with at least $L$ ordinary halvings.

## Consequence for simultaneous resets of a genuine disagreement

Suppose $3y$ has a given hit at $(H_0,p_0)$ and $y$ has no hit at one. Take initial reference grades zero on both arms. If both $(u,g)$ links to $(y,0)$ and $(3u,g)$ links to $(3y,0)$, the charge bound gives
$$
               4^g\,2^{H_0}\le4^{p_0}\,3u.                     \tag{3}
$$
For a nonperiodic lower reference $u\le3^gU(y)$ by the exact product identity. Thus
$$
              (4/3)^g\le 3U(y)4^{p_0}/2^{H_0}.
$$
This holds for every positive simultaneous reset, with unbounded independent clocks on the two arms (within each arm the visitor and reference clocks coincide). Allowing a bounded difference between the two requested grades only changes the constant. No escaping lower can realize arbitrarily high such balanced increases with its supplied good upper arm.

Without any assumption on the lower orbit type, let $m=\min_i T^i y$. At a lower meeting let $p$ count the visitor's odd steps, so the reference has $p+g$ odds. Its finite product is at most $(1+1/(3m))^{p+g}$ and the visitor's product is at least one. The clock cancellation gives $u\le3^g y(1+1/(3m))^{p+g}$. Substitution in (3) now lower-bounds the actual visitor work,
$$
   (1+1/(3m))^{p+g}\ge
        (4/3)^g\,2^{H_0}/(3y4^{p_0}).
$$
At a globally least reverse defect $y$, the previous quantitative return yields $m\ge y/2^{40}$. This can substantially increase the lower cost of using the supplied finite upper hit. Regenerating a pair with equal component labels does not imply (1) for either arm, nor does constructing a long return at changing inputs ensure a positive increment at this fixed pair. Establishing an appropriate deterministic all-source reset, or a usable return with different clock and grade changes, remains open.

## The upper minimum when the visitor must itself be a canonical triple

Fix one supplied good triple $y=3z$, $z=17\bmod48$, and give it grade zero. For each grade $g$ let $m(g)$ now be the minimum **parent** $w=17\bmod48$ among visitors $(3w,g)$ linked to $(y,0)$. This more constrained problem still has an exact eventual recurrence. For every sufficiently large integer $g$ the minimum exists, and
$$
       27m(g+27)+5=2^{54}\bigl(27m(g)+5\bigr).                 \tag{4}
$$
Every high-grade minimizer has at least 56 consecutive halving clocks immediately after its first two odd inputs. Its halving block can be shortened by 54 to recover a lower-grade minimizer.

For $w=17\bmod48$, the upper $x=3w$ is $51\bmod144$. The first two inputs are odd and $v=T^2x=(9x+5)/4=(27w+5)/4$ is divisible by four. To insert 54 halving clocks after these two odds, replace $v$ by $2^{54}v$. This gives $w'$ with $27w'+5=2^{54}(27w+5)$. The replacement is canonical: $2^{54}=1\bmod81$, so $x'=(4\cdot2^{54}v-5)/9$ is integral and agrees with $x\bmod9$; divisibility of $2^{54}v$ by four gives $x'=3\bmod16$. Together these specify $x'=51\bmod144$. The actual hit gains 54 clocks and retains its odd count, hence the grade grows by 27. In particular repeated insertions give $m(g)=O_y(4^g)$ along every occupied class modulo 27.

There are no missing classes at high grades. Canonical triples $3w$ with $w\le514673$ have explicit hits realizing all 54 ordinary charges $2p-H=-18,-17,\ldots,35$. The finite witness list and every listed hit are kernel-checked. For $I=2p_y-H_y$ choose a witness with $2p-H\equiv I-2g\bmod54$. For large $g$, repeated insertions lower its charge by 54 each time to reach $I-2g$ exactly. The charge test gives the requisite link. [All 54 direct hits and the arbitrary-word insertion](CanonicalGrade.lean)

For a minimizing $x=3w$, take its first visit to one. Formula (2) with $L=2,q=1$ and the uniform simple-path product bound now gives $\log_2 x=2g+(2-\log_2 3)p+O_y(1)$. Thus the number $p$ of odd letters is uniformly bounded. A minimizing inverse word ends in the two consecutive odd inverses reconstructing the first two ordinary steps. The even block immediately before them has at least two letters because $4\mid v$. If any other even block has length at least $D=2\cdot3^{p+1}$, move $D$ doublings from it to that distinguished block. Before the final two odd inverses, this moves the doublings past at least one odd inverse, strictly reducing the final source as in the unrestricted proof. Since $2^D=1\bmod3^{p+2}$, deleting and reinserting the doublings preserves every positive inverse choice and the final residue modulo nine: each remaining odd inversion loses at most one ternary digit, and there are at most $p$. The enlarged distinguished even block retains $4\mid v$, so the final binary residue is still 3 modulo 16. The reordered source is canonical and retains its visit clock and charge, contradicting minimality.

All the other even blocks are therefore bounded uniformly. The first-hit clock $H=2g+2p-I$ tends to infinity, so the distinguished block eventually has at least 56 letters. Divide $v$ by $2^{54}$. At least two halvings remain, and $2^{54}=1\bmod81$ preserves the final $x$ modulo nine. This deletion gives a valid canonical parent at grade $g-27$. Its inverse insertion is the increasing affine operation just proved. Minimality in each direction proves (4).

For a concrete lower-arm test of this upper operation, suppose in addition that $27z+5=32b$ (equivalently $z=1\bmod32$). For $g=0\bmod27$ inflate to $27w_g+5=4^g(27z+5)$. The upper retains its supplied odd count and inserts $2g$ actual clocks. Five ordinary lower steps from $w_g$ reach $4^gb+1$; the next $g$ pairs reach $3^gb+1$, while the original lower reaches $b+1$ at clock five. For every fixed $b>0$ these post-contraction sites $3^gb+1$ eventually fail linkage at grade $g$ to $b+1$ at grade zero. For a periodic reference (2) prices every eligible source above any fixed multiple of $3^g$. For an escaping reference the uniform limit is $U(b+1)\ge b+1>b$. Even an exactly adjustable canonical upper insertion and an ordinary lower contraction cannot supply these synchronized lower grades indefinitely.
