# Almost every source in an unsafe rank sublevel has a cheaper physical merger

**Status: PROPOSED.** This uses the proposed critical finite-coalescence estimate for odd-stride progressions. The result gives actual lower witnesses for all but a power-saving exceptional count. The strong obstruction to uniform short clocks in [the arithmetic results](OPTIMAL_CLOCKS.md) concerns individual inputs and is compatible with this count.

Fix a finite floor F>=1. Let D_F be the [exact re-entry support](REENTRY_SUPPORT.md) of the enlarged-unsafe return J_F. Let S be *any* subset of D_F, and let S_Y contain the members of S of moving rank R at most Y. Write p=log_3 2 and h=−p log_2 p−(1−p)log_2(1−p). There is a common shortcut clock r_Y=O(log Y log log Y) at which all but

    O(Y^{h/2} /(log Y)^{3/2})                                (1)

members of S_Y have a strictly cheaper partner in S_Y at that same clock. The constant is independent of S. The raw shortcut clock continues through the core for this first assertion. Alternatively each source either visits the floor by r_Y or, subject to the same exception count, has a cheaper partner whose path also stays above F through r_Y. After the physical meeting, the two original J_F itineraries either reach the floor or reach a *common unsafe return state*. Their numbers of induced returns can differ. If S consists of eternal fixed-floor survivors, the common return always occurs.

For S=D_F the population is of order sqrt(Y) for fixed F. Thus (1) is also a relative power saving on the entire actual re-entry support. Counting the possible permanent minima gives finite total critical weight sum R^{-h/2}, with tail O(1/sqrt(log Y)). The estimate does not bound the number of states in a single predecessor basin.

## The progression input and the slicing argument

We use the odd-stride estimate (2) in the companion manuscript `research/critical-orbit-mellin/RANK_SUBLEVELS.md` at commit `4ff383359446c77450956ca184fe08c0a61cb850`, Git blob `eda361eb9290c70930daeed283315c5dbe2b83d9`. That manuscript treats the injective section rank P. Its progression estimate itself has no rank hypothesis. It bounds the number of distinct common-clock endpoints of the positive inputs in an interval of A consecutive indices on an odd-stride d progression, uniformly in translation, by

    C(1+log d)d^sigma A^h/(log A)^{3/2},       sigma<h/2,    (2)

for A>=16, at a clock O(log(2dA)log log(4dA)). Larger clocks preserve the bound since deterministic iteration cannot increase cardinality.

At each n>1 choose one minimizing candidate a with the four-entry rule (use the least minimizing index for ties), and write z_a(n)=sign*3^e u, with u positive and prime to 3. On a fixed (a,e,sign) slice,

    R(n)=3^e u²,         n=(sign*3^e u−c_a)/d_a.

The rank is injective *within this slice*, even though it is not globally injective. If a>=3 is a minimizer from the four-entry rule, a=h(n) and e>=a because both terms 3^a(n+1) and 2^a(2n+1) are divisible by 3^a. For given e there are O(1+e) slices. Possible positive u are at most sqrt(Y/3^e) and occupy one residue modulo |d_a|. Passing from one u in that residue to the next changes n by plus or minus 3^e. The slice is therefore contained in an odd-stride progression with index count at most ceil(sqrt(Y/3^e))+1. Deleting nonminimizing points and imposing S causes no increase in image cardinality.

For d=3^e<=sqrt(Y), take A=ceil(sqrt(Y/d))+1, so log A is bounded below by a fixed multiple of log Y for large Y. Estimate (2) bounds the total images of all the slices here by

    C Y^{h/2}/(log Y)^{3/2} * sum_{e>=0}(1+e)^2 3^{e(sigma−h/2)}.

The series converges. For sqrt(Y)<d<=Y trivial counting costs at most O((1+log Y)Y^{1/4}+(1+log Y)^2), absorbed by (1). No larger d contributes. All required clocks are bounded by the claimed common r_Y since dA<=3Y at every relevant slice. At this clock, choose the least-rank S_Y input of each *slice's* nonempty image fiber. Only those representatives can lack a strict lower-rank partner. Choosing within each slice is what removes a possible multiplicity loss from global rank ties. The same proof applied to the subset surviving through r_Y gives both floor-clear paths in the alternative assertion.

The upper bound O(sqrt(Y)) for the full sublevel follows from the resident moving-rank spectrum. For a lower bound on D_F, prescribe n=1 modulo 3^7 and n=−17 modulo 2^11. The first primitive block is 11110, and its endpoint starts with three odd steps, so this is a maximal first A module. The first output Y_0 has ternary representative 73/16, with R(Y_0)/Y_0² tending to 1/9 in this class. Meanwhile R(n)<n²/3^7 and Y_0/n tends to 81/32. Thus all sufficiently large members of this positive-density progression are odd unsafe units in D_F. All those with n<=sqrt(Y) have R(n)<=Y, giving the lower estimate.

For states in S having no cheaper common-clock partner in S at *any* time, the counting bound at every scale Y gives (1) for their sublevel counts. Dyadic summation after multiplication by Y^{-h/2} gives the asserted tail. The same applies to states which never visit the floor and have no cheaper partner with a common surviving induced return, by using the surviving subset at each scale as above. If the shared future after an initial floor-clear meeting eventually visits F, the original state itself visits F, as required.

## Synchronizing the two accelerations after a physical meeting

Consider two J_F paths whose underlying raw shortcut trajectories have met at y. If a floor visit occurs, keep that outcome. Otherwise advance through the first zero bit in the common tail and call the state just after it z. Such a bit occurs for every positive y>1: its leading odd run has length at most log_2(y+1). The raw path is divided into primitive words 1^a0; every zero ends one primitive word. A partitions the primitive words into maximal runs of equal labels a. At z both primitive decompositions have a boundary, although one or both paths may still be inside a maximal run. Follow all consecutive complete copies of the next primitive label as seen from z. At A(z) that label changes. Both original paths must therefore have a maximal-module boundary there. From this state their A trajectories agree at all subsequent module boundaries. The [enlarged safe-exit theorem](../astra-three-routes/pass5-spectrum-switch/PLATEAUS_AND_SOURCES.md) gives a finite exit into U or 1, hence a shared genuine J_F return or a floor visit. This argument accommodates a meeting in the middle of either initial module.

One honest coarse extra physical-clock bound is O((y+5)^9 log(y+5)). The first primitive endpoint z has z+5<=(y+5)^3: a contracting mode decreases the state, and for an expanding mode its first block endpoint is at most A(y). The synchronized A endpoint has A(z)+5<=(z+5)^3. Each following safe module stays at boundary rank at most R(A(z))<=(y+5)^{18}. Safe boundaries are distinct until exit, and the resident bound on the size of a rank ball is 9 sqrt(R(A(z))). Each individual module from that ball takes O(log(y+5)) raw steps by its own height/clock bound. The synchronization is finite with no assumption about eventual Collatz convergence.

The [finite replay](check_sublevels.py) checks strict lower witnesses within slices, actual module re-synchronization after mid-module meetings, and the positive-density unsafe progression. It does not verify the asymptotic progression estimate.
