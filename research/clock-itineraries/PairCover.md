# The first common clock for a pair of arithmetic progressions

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. The **least** clock at which the pairs $(23+32t,3(23+32t))$, $t\ge0$, have every positive odd target coprime to three as a common image is **23**. In symbols, for every such $b$ there is a $t$ with
$$T^{23}(23+32t)=T^{23}(3(23+32t))=b.$$
At each earlier clock some target is missed even by the first member of every pair. At clock 22 one such target is 8161. [Lean statements and proofs](PairCover.lean)

Both members reach $20+27t$ after five steps. For each of the 4374 odd units modulo $2\cdot3^8$, the certificate gives a parameter whose next 18 steps reach the least positive representative, with at most five odd steps. If the number of odd steps is $j$, adding $2^{18}\cdot 2\cdot 3^{5-j}v$ to the parameter adds precisely $2\cdot3^8v$ to the endpoint. This proves the claim for arbitrarily large target integers. For the lower bound, Lean checks exact inverse alternatives separately at every clock from five through 22. The common five-step formula treats the earlier clocks as well. [Finite certificate](PairCoverData.lean) · [Affine lift](FiberTransport.lean)

The independent replay regenerates every table entry from parity words, checks both starting trajectories at three lifts of every representative, and searches backwards for the missed targets. Run `python pair_fiber_replay.py` from this directory. [Replay](pair_fiber_replay.py)

A smaller predecessor would make an induction on the target possible. For every $h,t\ge0$, every ordinary predecessor of $b=1+3^h t$ at any clock through $h$ has size at least $b$. Thus even a uniform inverse construction faces explicit size obstructions at arbitrarily large finite clocks. [Inverse height theorem](InverseHeight.lean)

## A finite-count form of the remaining conjecture

Write $X_k=1+\lfloor 2^{4k+2\lfloor k/2\rfloor}(k+1)/3^k\rfloor$. Inspect the parameters $0\le t\le9710X_k$. A parameter misses a chosen gate $g$ if neither member of its pair visits $g$ by time $O$. Lean proves that every positive start reaches 1 if and only if, for arbitrarily large $k$, some $O,g$ give strictly fewer than $\sum_{i=0}^{\lfloor k/2\rfloor}\binom{k}{i}$ misses. The gate and deadline may depend on the stage. The 23-step construction bounds the chosen parameter by $9710b$ for each target $b$. Distinct targets give distinct parameters, so the earlier inverse-tree counting theorem applies. [Full equivalence](PairCapture.lean) · [Inverse witnesses and quota](WindowCapture.lean)

At gate 1, direct iteration of all 19,421 parameters at stage zero gives zero misses at deadline 237. All 106,811 parameters at stage one pass by deadline 329. In each case a parameter attains the stated deadline. The unbounded-stage estimate remains open. [Replay](pair_fiber_replay.py)
