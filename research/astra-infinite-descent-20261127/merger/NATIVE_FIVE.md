# Simultaneous first arrivals at an ordinary pair of targets

Let $T(n)=n/2$ on even inputs and $T(n)=(3n+1)/2$ on odd inputs. The grade of a path counts its odd departures. A flight of clock $D$ and grade $g$ from $x$ to $y$ requires both $x$ and $5x$ to reach $y$ and $5y$ at clock $D$, with grade $g$ on each arm. At every earlier clock both states must strictly exceed their respective targets. The targets may be even, and may belong to cycles.

## An ordinary source in every sufficiently high relative window

**Lean-checked.** Fix a trit precision $s$, positive moduli $M,Q$, and a real $\delta>0$. There exist positive constants $C,K$ and an integer $G$ such that for every positive $y$ prime to three, every $X\ge Cy$, every trit query $c$, and every pair of marks $\tau,\rho$, there is an ordinary flight $x\to y$ with
$$
 X\le x\le(1+\delta)X,\qquad
 x\equiv c\pmod{3^s},\quad x\equiv49\pmod{64},\quad
 D\equiv\tau\pmod M,\quad g\equiv\rho\pmod Q,
 \qquad g\le G,\quad 2^D y\le KX .
$$
The lower bound $2^Dy\ge x$ follows from $2T(n)\ge n$. Thus both clocks are within a constant of $\log_2(X/y)$. To apply the generic placement theorem with other fixed source classes or simultaneous translates requires an ordinary prefix bank for the requested class or family. PR146 supplies a written construction for such banks. The unconditional Lean corollary uses the native class $49\bmod64$. [FivePlacement.lean](FivePlacement.lean) · [PR146 uniform native prefix](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md)

The two genuine first-return records used here are $A(x)=(9x+7)/64$ on $49\bmod64$, of grade two, and $B(x)=(27x+37)/256$ on $65\bmod256$, of grade three. Their companion endpoints equal five times the source-arm endpoints. These particular records and their cylinder interpretation are prior work. Two copies of $A$, with padded clocks $e,D-e\ge6$, give
$$
 81x+63+7\cdot 2^e=2^D y.
$$
For every $D\ge54\cdot3^s+11$, the powers $2^e$ for $6\le e\le54\cdot3^s+5$ traverse all units modulo $3^{s+4}$. This yields the required $x\bmod3^s$, $x>0$, and both actual grade-four paths. A longer sequence of inverse $A,B$ flights places their waypoint into a relative interval. One packet with $Q-1$ copies of $A$ and one $B$ has grade $2Q+1\equiv1\pmod Q$. The irrational rotation of the logarithmic height by this grade times $\log_2 3$ supplies all phases while the endpoint and both marks are fixed. The flight proof uses the weight $2^Lz-64$ to bound the total affine error uniformly in the number of packets. [FiveRouting.lean](FiveRouting.lean) · [FiveLadder.lean](FiveLadder.lean) · [FiveWindow.lean](FiveWindow.lean) · [PR166](https://github.com/GettysburgResearch/collatz/pull/166) · [PR200 native records](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/regularity-rigidity-20261124/RATIO_PRESSURE.md)

The exact integer control independently replays all states of both arms. For $y=7$, $X=19\cdot2^{8192}$, and $\delta=1/16$, its actual source is $4\bmod9$ and $49\bmod64$. Both first clocks equal 9043 and both grades equal 536, with $D\equiv3\bmod4$, $g\equiv2\bmod3$. Additional fixtures use the periodic target 1 and even target 26. [check_native_five.py](check_native_five.py)

## Exact large-clock count at each fixed grade

**Written proof.** Let $N_g(D;y)$ be the number of all positive integer sources giving the flight above, with no input residue or parity condition. For every fixed $g\ge2$, uniformly in all positive $y$ prime to three, set $k=\lfloor g/2\rfloor$. Then
$$
 N_g(D;y)=\frac{3c_g}{2\,3^g k!}D^k+O_g((D+1)^{k-1}),
 \qquad c_{2k}=1,\quad c_{2k+1}=k.
$$
Exactly the same main term and error hold if one asks only for simultaneous visits, or simultaneous first visits without the strict altitude guard. For $g=0$ the sole source is $2^D y$, and for $g=1$ there is no source. These counts are at *one exact clock*, and include both source parities. Requiring the initial source odd removes the initial dyadic padding and gives an upper bound $O_g((D+1)^{k-1})$.

### Finitely many primitive records at fixed grade

After removing initial common even steps, the first departure on both arms is odd. Stop the first time the grades again agree and the endpoints have ratio five. Separate the ensuing run of common even departures, then restart at the next common odd departure. For an actual path terminating at equal grades and ratio five this gives the unique expression
$$
 E^r W_1 E^{b_1}\cdots W_j E^{b_j}.
$$
Here $W_i$ is a primitive positive return starting at an odd input, and $b_i,r\ge0$. Initial or internal zero padding is allowed. Each record has positive grade. A grade-one record would require $5\cdot2^0=2^0$ in the equality of the two affine carries, so every record has grade at least two.

For a path of total common grade $p$, let the odd input times on its two arms be $u_1<\dots<u_p$ and $v_1<\dots<v_p$. Both start at zero. Exact endpoint ratio gives
$$
 5\sum_{i=1}^p3^{p-i}2^{u_i}
   =\sum_{i=1}^p3^{p-i}2^{v_i}.
$$
Just after an event in this union, with last event time $t$, subtract the corresponding partial sums with the displayed full-grade weights. If this difference vanishes, its two equal magnitudes have respective ternary valuations $p-a,p-b$ where $a,b$ are the respective prefix counts. Indeed the final existing odd term has nonzero residue mod three after its common factor is removed. Consequently $a=b$ and the prefix has already returned to ratio five. In a primitive record before its end the difference is a nonzero integer of magnitude at most $5\cdot 3^p2^t$, by the geometric sum of its nonnegative terms on each side. If $t'$ is the next event, the difference is divisible by $2^{t'}$ because all the omitted terms are. Hence $t'-t\le2p+3$. There are at most $2p$ union events. At a primitive first return the final step is an event because a final common halving preserves the ratio and both grades backwards. This bounds the record clock in terms of $p$, proving finiteness.

### The extremal record types

For $p=2$, the two lists are $(0,a),(0,b)$, so $12+5\cdot2^a=2^b$. The only possibility is $a=2,b=5$, by considering $a=1,2$, then the valuation for $a>2$. The binary cylinder with those first-arm input parities is unique modulo $2^6$, and $x=49$ realizes both lists. Thus the only grade-two primitive record is $A$.

For $p=3$, write the lists as $(0,a,b),(0,c,d)$ with positive strictly increasing later indices. They satisfy
$$
 36+15\cdot2^a+5\cdot2^b=3\cdot2^c+2^d.
$$
If just one of $a,c$ equals one, the equation fails mod four. If both equal one, $60+5\cdot2^b=2^d$ has no solution since $b=2$ gives 80 and $b>2$ forces $d=2$. If $a,c\ge3$, or if both equal two, the equation fails mod eight. When $c=2,a\ge3$, it becomes $24+15\cdot2^a+5\cdot2^b=2^d$. For $a>3$ the valuation forces $d=3$. For $a=3$, the left side is $144+5\cdot2^b$, giving 224 at $b=4$, and forcing $d=4$ at $b>4$. The sole remaining case has $a=2,c\ge3$. The valuation of $96+5\cdot2^b$ equals $c$, since $d>c$. For $b=3,4,5$ the left sides are 136, 176, 256, of which only $176=3\cdot2^4+2^7$ works. For $b>5$ we get $c=5$ and $5\cdot2^b=2^d$. Thus only $a=2,b=4,c=4,d=7$ survives. The unique source cylinder is $65\bmod256$, as direct iteration at 65 verifies. This is $B$. A fixed source parity list specifying every input parity up to the last event determines one binary cylinder because the next high bit reverses the next parity while preserving all previous ones.

### Counting padding lengths and first visits

At grade $g$ there are finitely many record orders. Each order with $j$ records permits at most $O_g((D+1)^j)$ choices of nonnegative padded record clocks $e_i=h_i+b_i$, where $h_i$ is the clock of $W_i$. The initial padding then equals $D-\sum e_i$. Each tuple produces at most one ordinary source from the target. An order with $j=k$ consists entirely of $A$ for even $g$, or of one $B$ in one of $k$ positions among $A$'s for odd $g$. All other orders contribute to the stated error.

For each maximal order read the records backwards, from $y$. Write $p_i=2,3$ and $C_i=7,37$ as applicable. Given a unit parent $v$, the child is $u=(2^{e_i}v-C_i)/3^{p_i}$. It is automatically odd when integral. The fraction of exponents producing an integer is $1/(2\cdot3^{p_i-1})$, by the exact order of two modulo $3^{p_i}$. Requiring the child to be a unit additionally removes one of the three lifts mod $3^{p_i+1}$, so the fraction becomes $3^{-p_i}$. Every internal child must be a unit because it is also the parent of a subsequent positive-grade inverse step whose carry is a unit. On the last inverse step the child can be divisible by three, whether or not it is then multiplied by the initial $2^r$. Thus the product fraction of allowed tuples is
$$
  \prod_{i<k}3^{-p_i}\cdot\frac{3}{2\,3^{p_k}}
       =\frac{3}{2\,3^g}.
$$
For precision, take the common period $P=2\cdot3^{g+1}$ in each coordinate. Exponents mod $P$ determine $2^{e_i}\bmod3^{g+2}$. In each backward affine step division by $3^{p_i}$ loses at most $p_i$ trits, so integrality and the required unit tests for the entire tuple depend only on the exponent residues and the target class mod $3^{g+2}$. Conditional on earlier exponent coordinates the current parent is a specific unit to the precision needed for the next test. Multiplying these conditional fractions proves the displayed residue count, including the unrestricted last-child factor.

In each allowed residue vector, the number of tuples with $e_i\ge20$, $\sum_i e_i\le D$ equals $D^k/(k!P^k)+O_g((D+1)^{k-1})$. Subtract the least representatives above 20 and count the remaining simplex of nonnegative multiples of $P$ by stars and bars. Tuples with some $e_i<20$ cost only $O_g((D+1)^{k-1})$. At $e_i\ge20$ every permitted inverse is positive, and every state before its parent strictly exceeds that parent on each arm by the two explicit $A,B$ altitude estimates. The initial $r$ common doublings also strictly increase height going backwards. All these tuples therefore have the required flight, including when $y$ or $5y$ is periodic. Unique first-return decoding makes sources from distinct feasible tuples distinct. This proves all three counting assertions. [FiveLadder.lean](FiveLadder.lean) · [PR200 first-return decoder and ternary residue law](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/regularity-rigidity-20261124/RATIO_PRESSURE.md)

## Transfer of the broad-shell power count

**Written deduction using PR204.** For each fixed positive unit $y$ and each $\delta>0$, every sufficiently high window $[X,(1+\delta)X]$ contains $\gg_{y,\delta,s,M,Q} X^{1/5}/\log X$ distinct starts on *one* pair of physical clock/grade values, with genuine first arrivals at $y,5y$, arbitrary prescribed time and grade marks, and arbitrary prescribed trits of the initial source. The sources are all $49\bmod64$. The first-arm real affine offset can be required to lie below any fixed $\epsilon>0$ and the companion offset then equals five times that value. The selected clock and grade may grow with $X$. PR204 supplies the power count for paired visits in a broad shell of multiplicative width $2^{400}$. The transfer below retains its exponent and its factor $1/\log X$. [PR204 weighted pointwise rows](https://github.com/GettysburgResearch/collatz/blob/5d4698b692ec102b44cf77a59930a2a80b4104fd/research/astra-joint-closure-20261124/pressure/WEIGHTED_POINTWISE_ROWS.md)

First select an odd-unit predecessor $b$ for which $b,5b$ reach $y,5y$ along an $A$ flight, while $b$ is outside the forward orbit of $y$ and $5b$ is outside that of $5y$. To see that one such predecessor exists, use the infinitely many unit children $b_e=(2^e y-7)/9$ with $e\ge20$. All have first clock $e$ and grade two. At most one can belong to the future of $y$. Indeed such a child and $y$ would lie on the same cycle. If $b_e,b_f$ were two with $e<f$, their first-hit clocks both lie within one period. Injectivity of $T^e$ on the cycle gives $T^{f-e}b_f=b_e$. The nonempty prefix from the odd $b_f$ contains at least one odd departure, contradicting the equal total grades. This argument applies independently to the $5b_e$ and $5y$. Removing the two possible exceptions leaves a qualifying child.

Apply the pinned PR204 theorem at the fixed odd unit $b$ with upper shell cutoff $Y=X/C$, where $C$ is a fixed constant at least the window-placement threshold and at least one. Obtain $\gg_b Y^{1/5}/\log Y$ distinct odd-unit $u\in[Y/2^{400},Y]$ on one clock/grade row to $b,5b$. Every prefix reaching $b$ cannot have visited $y$ earlier, since $b$ is outside the forward orbit of $y$. The same applies independently to $5b,5y$. Append the fixed flight $b\to y$ to every old row.

For each old $u$, apply the Lean window theorem at the supplied target $u$ and scale $X$. Prescribe the source trits and choose the added clock and grade marks to cancel the old row and the fixed tail, leaving the final requested marks. The added clock is at most $\log_2(KX/u)\le \log_2(KC)+400$ and the added grade is bounded independently of $X$. Every prefixed source reaches $b,5b$, so neither path can visit its final target before the tail. A new source determines the old $u$ given its added clock. Consequently the map has bounded multiplicity, even prior to pigeonholing in the bounded added clock and grade. Keep the largest resulting exact row. This proves the stated count of *first* arrivals. The transferred paths have genuine first arrivals and can dip below $y$ earlier. For the additional offset cutoff, take the fixed eligible tail clock $e$ so large that $(18+7)/2^e<\epsilon$. The newly prefixed path has grade at most $G$, hence its real affine offset is at most $3^G$ by summing its normalized odd-departure carries. At the old row $u\to b$ the offset is at most $1/2$ by PR204 and the slope is at most $b/u=o(1)$ uniformly in the old shell. At $b$ the combined offset is at most $1/2+o(1)\le2$. The final $A$ branch multiplies that error by $9/2^e$ and adds $7/2^e$. Equal grades and exact endpoint ratio make the second full offset five times the first. The $\gg$-count and the preceding elementary fixed-grade asymptotic concern different clock and grade regimes.

## The physical five-closure question

The checked directed descent certificate in PR157 reduces universal ordinary convergence to $q\in C\Rightarrow5q\in C$ for odd $q$ prime to three, where $C$ is the basin of one. If such a supplied $q$ fails five-closure, every genuine pair of predecessors transfers the failure. The first theorem supplies transfers in every high relative window, and the broad-shell deduction supplies many on one row. Deciding the basin of $5q$ for this supplied $q$ still requires a source-preserving step. No part of the fixed-grade asymptotic gives the near-linear row count at grade proportional to clock sought by PR200 and PR204. [PR157 reduction](https://github.com/GettysburgResearch/collatz/pull/157) · [PR200 fixed-target paired-fiber reduction](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/regularity-rigidity-20261124/pointwise-fibers/COMMON_SUFFIX.md) · [PR204](https://github.com/GettysburgResearch/collatz/pull/204)
