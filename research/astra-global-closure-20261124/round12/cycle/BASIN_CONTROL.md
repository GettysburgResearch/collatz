# A rational cycle with complete lower-numerator basin separation

**Verified finite control.** Fix an odd denominator $d$ prime to six. On the positive odd numerator lattice use $U_d(y)=(3y+d)/2^{v_2(3y+d)}$, the ordinary odd rational map on $y/d$. Every entry of a trajectory retains the originally chosen denominator representation. A component here is the set $B$ of odd numerators whose forward trajectories reach a designated odd cycle. Calling its complement good defines a component coloring. Reaching one fixed reference numerator is a different predicate.

Take $d=1631$. An exact cycle, in chronological numerator order, is

$$
 10865, 17113, 26485, 40543, 30815, 23519, 18047, 13943 .
$$

It has odd period $p=8$, total physical exponent $h=13$, successive exponents $1,1,1,2,2,2,2,2$ and minimum $S=10865$. Its odd width is $40543/10865$, between 3 and 4. Sorted dyadic mantissas form one rotation by $h$ modulo $p$. After restoring the intervening even states, sorted ternary mantissas form one rotation by $-p$ modulo $h$. The ranks have binary bands $0,1,1,0,1,0,0,1$, with cyclic Hamming distances $6,4,2,8,2,4,6$ at the seven nonzero shifts. The rank determinant itself is 1631 and the reduced cycle denominator equals it.

Every smaller positive odd numerator $y<S$ belongs to the complement of $B$. Every positive odd multiple of three $y<2S+d$ also belongs to the complement. The numerator $2S+d=23361$ lies in $B$, whereas $Q=(2S+d)/3=7787$ reaches the distinct cycle of minimum 6625. Consequently $S$ is the least odd member of $B$ and $Q$ is the least odd disagreement of the complement coloring with its triple. For every odd $y<Q$, both $y<S$ and $3y<2S+d$ fall under the two exhaustive checks.

The computation covers all 5,432 smaller odd numerators and all 3,893 smaller odd multiples of three. Each forward path reaches an explicitly repeated state or meets a previously classified path. The resulting 17,076-state finite graph is closed under the actual map. The checker verifies its exact outgoing edges, the constancy of every label along those edges, and the closure of each listed terminal cycle. Determinism then excludes entry into the distinguished cycle after any additional number of steps. Allowing non-reduced starting numerators enlarges the census domain. The finite calculation checks every required start in this example and has no preset orbit-depth limit. [Checker](check.py) · [Counts and terminal cycles](../../../../reports/astra-global-closure-20261124/round12/cycle/control.json)

The numerator 1 reaches the distinct cycle of minimum 4913, so the $Q$ orbit in this example does not supply a hit to that reference. A smaller companion with $d=13$ has cycle $(283,431,653,493,373)$, $p=5,h=8$, least bad numerator $S=283$ and least bad multiple $579=3\cdot193$. It has the same complete basin separation, and $Q=193$ does reach the numerator 1. Numerator 7 also reaches 1 whereas 21 reaches the cycle of minimum 131. Thus the least disagreement for hitting the single reference 1 is already 7 in the companion; the component coloring remains essential. The distinguished cycles in both examples consist of genuine positive reduced rationals. Neither yields an ordinary counterexample or a family of late continued-fraction candidates.
