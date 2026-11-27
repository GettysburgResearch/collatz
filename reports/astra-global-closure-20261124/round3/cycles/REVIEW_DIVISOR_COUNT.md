# Fixed-word source counting

**VERIFIED finite injection and finite cover.** I checked source research/astra-global-closure-20261124/round3/controller/DivisorCount.lean at SHA-256 af766e9243cc79185bf893409ed3acf494725a36bfa86a428030a78b482a4f20 and independently compiled it strictly with Lean 4.34.1 and Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612. Both public declarations report propext, Classical.choice and Quot.sound. The process exited zero.

For fixed $D,B,C,P$ the source relation is $Dq(x)=Bx+C$ with $B>0$, $P\ne0$ and $q(x)\mid P$. Since $P\ne0$, all the endpoints are positive divisors of $P$. Two sources giving the same endpoint have equal $Bx+C$ and therefore coincide. Thus the number of sources is at most $\tau(P)$. For source-dependent row choices, filtering the fixed original source set by each supplied row, taking their union and summing the individual cardinalities gives the second declaration. Overlaps only increase this upper bound.

Application requires a covering family with each selected nonzero $P$ and a common per-row affine relation. The size of that family and an estimate of its divisor counts are independent obligations. Neither declaration bounds a class defined by $P=0$.
