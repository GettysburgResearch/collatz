# How much odd work can every smaller merger require?

**PROPOSED.** Fix an upper shortcut horizon $I$ and an extra allowance $D$. There is $H(I,D)$ such that, for every positive ordinary source $x=3^h a$ with $h\ge H(I,D)$ and $a\ge2\cdot3^D$, the following holds simultaneously at each $0\le i\le I$ for which $2^i\mid x+1$. If a smaller positive integer $y<x$ reaches $T^i x$ at **any** shortcut clock $j$, then
$$
                      Q_j(y)>i+h+D .
$$
Here $T(2n)=n, T(2n+1)=3n+2$, and $Q_j$ counts odd departures through the specified clock. The native word has exactly $i$ odd departures. There is no cap on the even work of the rival. The threshold is an existence theorem without a numerical rate in the two free parameters. [Kernel theorem `unbounded_extra`](SurplusProperness.lean)

The result also applies to explicit increasing Mersenne triples whose lower arms converge. On the same triple, advancing to a later endpoint gives a positive smaller **multiple of three** with just four extra odd steps, independently of $h$. Another certificate has a source whose ratio to the original tends to zero. Thus the early obstruction coexists with an ordinary descent certificate. Collatz and the all-source least-failure condition remain open.

## Proof on the actual two paths

Write $X_i=T^i x$. The all-odd prefix gives $2^i(X_i+1)=3^i(x+1)$. Every positive shortcut path satisfies
$$
  3^{Q_j(y)}(y+1)\le 2^j(T^j y+1)\le3^j(y+1).
$$
The two inequalities follow by multiplying the one-step bounds. In particular no smaller $y$ reaches $X_i$ at $j\le i$. For a merger at $j=t+i$, put $z=T^t y$ and let $v$ count odd departures in the last $i$ clocks. Its affine carry $c$ satisfies $2^i X_i=3^v z+c$, $0\le c\le3^i-2^i$, by the resident ordinary affine bound. Therefore $z\ge3^{i-v}x$. [Resident carry lemma](../../astra-universal-descent-20261124/EscapeCore.lean)

One elementary bound transports a ternary-aligned threshold. For every positive $A$,
$$
          n<2^s A \quad\Longrightarrow\quad T^s n<3^{Q_s(n)}A.
$$
Induct on $s$, using the threshold $2A$ one clock earlier. Apply this in reverse to $z\ge3^{i-v}x$. If the full rival grade $u=Q_j(y)$ were at most $i+h$, then $3^{u-v}\mid 3^{i-v}x$, so
$$
                  y\ge \lambda x,\qquad
                  \lambda=2^t3^{i-u}.
$$
But $y+1\le\lambda(x+1)$ by the shifted lower bound. These force $\lambda\ge1$ and $y\ge x$. This proves the initial strict inequality $u>i+h$. [Physical proof of `excess_grade`](MersenneAncestors.lean)

Suppose now $u=i+h+d$, with $1\le d\le D$. Cut the rival's first $t$ steps immediately after its $d$-th odd departure, at clock $k$. Such a departure exists since $u-v\ge h+d$. Set $L=t-k$, $Y=T^k y$, and $g=Q_L(Y)=h+i-v\ge h$. The suffix threshold now reads $z\ge3^g a$, hence $Y\ge2^L a$. Set $b=Y-2^L a$. The length-$L$ binary lift gives ordinary integer identities
$$
          Q_L(b)=g,\qquad T^L b=z-3^g a=:E.
$$
These are two counts of the very same residual word, so the native grade $h$ is retained at the small ordinary seed.

Here are all size estimates used on this path. Write $S=2^t$, $P=3^{h+d}$. The shifted path inequality gives $P(y+1)\le S(x+1)$, and $y<x$ then implies $3^d y<S a$. Indeed the opposite would imply $Sx\le Py$, hence $P\le S$ and $x\le y$. The elementary affine carry bound charged by odd count is
$$
              2^k Y\le 3^d y+2^k3^d .
$$
Induction on the actual shortcuts gives this bound. Inserting $Y=2^L a+b$ proves $b<3^d$. Since $S a\le 2^kY\le 3^d x+S3^d$ and $a\ge2\cdot3^d$, we also get $S\le2P$. Finally the exact last-$i$ identity gives $3^v E+c+2^i=3^i$, so $0\le E<3^i$. Together,
$$
  b<3^D,\qquad E=T^L b<3^I,\qquad h\le g=Q_L(b),
       \qquad 2^L\le(2\cdot3^D)3^g .
$$
No convergence test on $b$ is used in the general theorem. [Kernel extraction `bounded_shadow`](MersenneAncestors.lean)

For fixed $B,F,C$, there is a bound on $g$ among **all** ordinary paths with $b\le B, T^L b\le F, 2^L\le C3^g$. For a positive odd fixed endpoint $e$, every departure from $e$ contributes a factor $1+1/(3e)$ to the physical product $2^L T^L b/(3^g b)$. The latter is bounded by $Ce/b$. Hence the number of earlier visits from fixed $b>0$ is bounded, and distinct visitation clocks have distinct prior visit counts. A positive even endpoint can be advanced through its halvings to an odd endpoint, increasing $C$ by a finite factor. Zero has no positive predecessor. The finitely many seed/endpoint pairs now give a common grade bound. This also proves that the optimal normalized inverse cost at a **fixed** positive ordinary gate tends to infinity along all realized grades, since a ratio at most $C$ forces the source to be at most $Ce$. Taking $h$ above the finite bound contradicts the shadow. [Fixed-gate product and visit-rank injection](../../astra-closure-20261125/escape/GateVisits.lean) · [Fixed-target and finite-window proofs](SurplusProperness.lean)

## An actual later smaller triple

For each positive even $h$, put
$$
 m=2\cdot3^{h-1},\quad x=2^m-1=3q=3^h a,\quad w=2^h a-1.
$$
The expansion of $4^{3^{h-1}}$ by successive cubing shows $a=1\bmod3$ and $a\ge3^{h-1}$. Thus $h$ is the exact ternary valuation of $x$, $q$ is odd, and $0<w<x$ is divisible by three. The lower arm $q$ reaches $2^{m-1}$ after one odd step, then one at clock $m$. The proposed smaller triple first reaches $x-1$ in $h$ all-odd steps, then $s=(x-1)/2=2^{m-1}-1$. The $s$ and $x$ arms reach $3^{m-1}-1$ and $3^m-1$ after their respective all-odd blocks. Since $3^{m-1}=3\bmod4$, two more shortcuts from each land at $(3^m-1)/4$. Consequently
$$
 T^{h+m+2}w=T^{m+2}x,\qquad Q_{h+m+2}(w)=h+m,
                  \qquad Q_{m+2}(x)=m .
$$
Here $w/x=(2/3)^h-1/x$ tends to zero. For every $I,D$ one can take $h$ cofinally large with the early obstruction, the convergent $q$, and this same later merger. [Ordinary family and clocks](MersenneCertificates.lean)

There is also a bounded-work partner independent of $h$. For every positive odd $x$ divisible by 243, put $u=x/243$ and $w_4=192u-3$. This is a smaller positive multiple of three. Its first seven shortcut images are
$$
288u-4,\quad144u-2,\quad72u-1,\quad108u-1,\quad162u-1,
       \quad243u-1,\quad (x-1)/2 .
$$
Exactly four departures are odd. Whenever $x=3q$ meets $(x-1)/2$, the theorem `four_odd_checker` turns those two physical meeting clocks into a passing resident certificate for $q$, for either normalized ternary unit. For the Mersenne sources above with $h\ge5$, the shared endpoint at clock $m+2$ on the upper arm is reached from $w_4$ at clock $m+8$ with exactly $m+4$ odd departures. More generally, $x=3q=2s+1=3^h a$ with $2^h a-1=3v>0$ and $x$ meeting $s$ gives a true certificate for the resident checker by following $3v$ to $s$ in $h+1$ steps. That last statement includes $h=1,2$. At an actual least failure the smaller triple would already be good. [Seven-step path, four-odd exit, and actual checker consumer](MersenneCertificates.lean)

## A numerical bound uniform over the entire upper staircase

For $D=8$ the small-seed argument gives the obstruction at **every** $i$ with $2^i\mid x+1$ whenever $h\ge101$ and $a\ge13122$, independently of the length of the upper staircase. The finite computation follows the actual orbits of the positive seeds below $3^8=6561$ and exhausts every clock with $2^L\le13122\cdot3^{Q_L(b)}$. Once a seed reaches 1 with ratio greater than $3\cdot13122/2$, all future ratios exceed 13122. The intervening odd departure multiplies it by $2/3$, and each complete lap multiplies it by $4/3$. Seed zero has grade zero. The largest qualifying grade is 100, attained from 6171 at clock 172 and endpoint 2. The regular and optimized Python runs both checked 454,255 positive seed/clock pairs. This numerical refinement uses the proved shadow implication and an exact finite replay; the preceding arbitrary-$I,D$ theorem uses no enumeration. [Checker](check_shadows.py) · [Replay](../../../reports/astra-multiple-attacks-20261125/descent/shadows.json)

In particular every even $h\ge102$ in the displayed family has the early exclusion through its changing native deadline $m$. It persists at clock $m+1$, measured relative to the same native odd grade $m$. The even state $(3^m-1)/2$ is at least $x$ and is $1\bmod3$, so its only shortcut predecessor is $3^m-1$ via a halving. Every smaller rival reaching it must already have crossed the preceding site at the same grade. **One more physical shortcut**, from clock $m+1$ to $m+2$, changes the bound from more than $m+h+8$ odd departures for every smaller ordinary rival to at most $m+4$ for a genuine smaller triple. The source-saving partner $w$ above also remains available there. [Forced last edge and four-odd exit](MersenneCertificates.lean)

## Relation to earlier results and the unresolved inference

Weaver’s Proposition 6 already gives the $i+h$ odd-depth barrier at odd endpoints for a larger language of native gaps using ones and isolated twos. The paper also gives an example where advancing a single odd iterate escapes an unbounded inverse-depth obstruction. The first bound above gives a separate shortcut proof for the all-odd case and includes an even last shortcut endpoint. The arbitrary additional margin, small-seed extraction, and comparison on an unbounded staircase with a computed surplus-eight obstruction are the contributions here. PR192 already used the descent from $2^h a-1$ to $x-1$ and the adjacent Mersenne coalescence. The present certificate uses the exact ternary unit to make the smaller start itself a multiple of three and compares its work to all early rivals. [Weaver, v2, Proposition 6 and Corollary 7](https://rstation.ai/problems/collatz/papers/1/v2) · [PR192’s native merger](https://github.com/GettysburgResearch/collatz/blob/1f1d3d690d7517e1b2a44b5f2f4930bd45b63302/research/astra-minimum-source-20261124/descent/README.md)

The fresh PR192 cycle optimality theorem is about all competitors at a supplied bounded ordinary cycle phase. An additive constant above the critical inverse cost cannot be attained at infinitely many grades at any fixed ordinary target, by `source_free_gate`. An excess growing more slowly than grade is still possible. The known all-depth cone gives no construction of those incoming paths and no upper bound on their word complexity sufficient to invoke PR210’s rational critical-record classification. On the explicit Mersenne family the later smaller triple is known. At an arbitrary actual first bad $3q$, a source-dependent proof must still produce a smaller triple in that same component, including cases where the adjacent arm has another component. No such universal coverage is established. [PR192 inverse clocks](https://github.com/GettysburgResearch/collatz/blob/1f1d3d690d7517e1b2a44b5f2f4930bd45b63302/research/astra-diagonal-closure-20261125/cycle/README.md) · [Resident least-failure interface](../../astra-closure-20261125/FinalProposal.lean)
