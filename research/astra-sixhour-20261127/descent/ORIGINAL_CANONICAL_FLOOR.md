# The least bounded reverse source is the least bad canonical integer

Call a positive integer good when its shortcut orbit visits one. Let \(M\) be any positive number such that **all positive multiples of three below \(M\) are good**. For the least odd tripling disagreement \(q\), one can take \(M=3q\) without the bounded alternative. In that alternative \(M=2s+1\), where \(s\) is the global least bad positive integer. [Least bad multiple theorem](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124/README.md) · [Bounded global minimum](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md)

**Orientation on an interval.** If \(y\equiv1\bmod16\) and \(9(y-1)<32M\), then \(y\) or \(3y\) is good. The alternatives have explicit physical mergers and need no restriction on either hitting clock. For \(y>1\) write \(y=1+2^d u\) with \(u\) odd and \(d\ge4\).

* If \(d=2l\), then \(T^{2l}y=1+3^l u\) and \(T^{2l+1}y=T(3^{l-1}u)\). The positive multiple \(3^{l-1}u\le3(y-1)/16\) is below \(M\). Thus \(y\) itself is good.
* If \(d=2l+1\), then \(T^{2l+1}(3y)=1+3^{l+1}u\) and \(T^{2l+2}(3y)=T(3^l u)\). The positive multiple \(3^l u\le9(y-1)/32\) is below \(M\), so \(3y\) is good.

Here \(l\ge2\). For the lower calculation use \(T^2(1+4b)=1+3b\). For the upper one, \(3y=3+32(3\cdot4^{l-2}u)\) follows the five parities of \(3,5,8,4,2,1\), reaching \(1+27\cdot4^{l-2}u\). Apply the same two-clock identity another \(l-2\) times. The bounds use \((3/4)^l\le9/16\). [Strict Lean verification of both actual mergers and the interval implication](CanonicalTripleFloor.lean)

The five-clock identity and the odd-\(d\) upper route on **on-cycle** consecutive two-edges appear in the prior canonical-floor proof. The new statement above applies the least-multiple cut to both parity cases throughout an absolute interval, including all ordinary off-cycle sources. [PR195 on-cycle route and original comparison](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/CANONICAL_FLOOR.md)

Let \(z\) be the least \(17\bmod48\) source with bad lower and good triple. In the bounded alternative the pinned \(243(z-1)\le1024(s-1)\) puts every \(y\le z\) inside the displayed orientation interval. Therefore
\[
 \boxed{\quad z=\min\{y>0:y\equiv17\bmod48,\ y\ {\rm bad}\}.\quad}         \tag{1}
\]
Indeed any earlier bad canonical \(y\) has a good triple by the interval theorem and contradicts the original leastness. In particular any positive smaller canonical ancestor of the fixed lower immediately closes the bounded case. Its triple and the original triple both physically visit 8 on their actual good paths. The existence of a smaller ancestor is still open. Also \(v_2(z-1)\) must be odd, so the first matched balance at clock five with carry one in [the first-balance note](FIRST_BALANCE.md) applies to every original bounded \(z\).

There is an equivalent one-row minimum. Since \(T^4(17+48a)=10+27a\) bijectively in the nonnegative row parameter,
\[
          g=(9z+7)/16
             =\min\{n>0:n\equiv10\bmod27,\ n\ {\rm bad}\}.               \tag{2}
\]
In particular every restricted cycle phase following a native exponent word \(1,2,2\) has height at least \(g\). Its first two-edge source is \(17\bmod48\), as it follows a one-edge and starts two consecutive two-edges. The last two shortcuts pairs produce the stated row. At \(v_3(s-1)=2\) the older capture theorem gives \(g=s\) exactly, so the additional row floor can have zero relative improvement. [Kernel statements all_earlier_canonical_good and canonical_fourth_value](CanonicalTripleFloor.lean)

## The first inverse detour must cross the original ceiling

On the distinguished bounded bad cycle use the native odd edges \(3v+1=2^a x\), \(a\in\{1,2\}\). At the terminal \(x\), the other odd ordinary predecessors are exactly
\[
                    4^b v+(4^b-1)/3,\qquad b\ge1 .
\]
This holds since the parity of a permissible positive inverse exponent is fixed modulo two. Consider every odd inverse path starting at a cycle phase and keeping **all** its vertices strictly below the original \(z\). The only possible first off-cycle odd predecessor is \(w=4v+1\). If \(z\le4s+1\) even this one is unavailable. Otherwise the original pinned bound gives \(v<(256/243)s\). Such a phase cannot have an outgoing two-edge since its successor would be below \(s\). Hence \(v\equiv3\bmod4\). Its incoming edge must be a two: the predecessor from an incoming one would be smaller than \(s\) since \(v<3s/2\). Its native predecessor \(p=(4v-1)/3\) likewise has \(p< (1024/729)s<3s/2\), so its own incoming edge must be a two. Thus \(p\equiv v\equiv1\bmod3\).

Now \(w\equiv2\bmod3\) has first odd predecessor
\[
                          (2w-1)/3=2p+1 .
\]
Its next possible alternative \(4(2p+1)+1\) exceeds \(z\). The first predecessor \(2p+1\) is a multiple of three and has no odd predecessors. Neither \(w\equiv13\bmod16\) nor \(2p+1\equiv3\bmod4\) is canonical. This exhausts the possible branch after its **first** detour regardless of the preceding number of native laps. Thus a smaller off-cycle canonical member of this particular component must be reached by an inverse path which somewhere goes at least as high as \(z\). Globally \(z\) can itself lie in a different bad component; this search started at the distinguished cycle, so it does not assume that the original \(z\) already lies there.

Write \(r=v_3(s-1)\in\{2,3,4,5\}\). At a least source outside the distinguished cycle the prior capture gives \(v_2(z-1)<2r\). Combined with oddness from the new interval orientation, the remaining pairs \((r,v_2(z-1))\) are
\[
                 (3,5),(4,5),(4,7),(5,5),(5,7),(5,9).
\]
This is a restriction on the original source with its actual upper word. It gives no bound on that word's odd rank. The missing implication in (1) is existence of the original-floor return, potentially after a taller inverse excursion.
