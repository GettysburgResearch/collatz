# A full integral polynomial evaluation lattice at one fixed terminal and two exact clocks

**PROPOSED written theorem.** Let \(y\) be any fixed positive odd integer with \(3\nmid y\), and let \(d\ge1\). There are absolute constants \(C_1,C_2\) such that for **every** \(k\ge C_1(d+1)\) and **every** \(H\ge C_2(d+1)^2 k\), the following finite set of positive odd sources has the full integral evaluation lattice in degree \(d\):
\[
 S_{y,k,H}=\{x>0\text{ odd}:U^k(x)=y,\
      \textstyle\sum_{i<k}v_2(3U^i(x)+1)=H\}.
\]
Write \(t_x=(x-1)/2\) and \(v_d(t)=(\binom t0,\ldots,\binom td)\). Then
\[
 \boxed{\operatorname{span}_{\mathbb Z}\{v_d(t_x):x\in S_{y,k,H}\}
                         =\mathbb Z^{d+1}.}                         \tag{1}
\]
In particular one can take \(k=O(d+1)\), \(H=O((d+1)^3)\). All witnesses satisfy \(x\le y2^H/3^k\), directly from the positive complete path carry. The theorem controls the maximum ordinary height required for (1) uniformly in the supplied terminal. It neither assumes nor implies any known forward fate of \(y\).

For every finite vector of rational polynomials of degree at most \(d\) in \(t\) taking integer values on integers, its integer evaluation lattice on this **same fiber** equals its integer evaluation lattice on all integers. The number of output coordinates and coefficient heights are arbitrary. In particular the polynomials may use \(k,H,2^H,3^k,y\) as coefficients and may include the **complete integer carry**
\[
                       C=2^Hy-3^k(2t+1).                            \tag{2}
\]
More generally, for rational-polynomial vectors without the integrality condition the two generated fractional lattices are equal, by multiplying by a common denominator. Every prime and every determinantal divisor have thus been retained. Equation (1) does not assert that a *single* maximal minor is a unit; different primes can use different witnesses. The torus grade and representation degree are both allowed to grow.

## Fixed-clock routing input

The proof uses the elementary interval and compression argument from the [companion routing proof](../cycle/README.md). The precise consequence needed here is as follows. Put \(b\ge1\) coprime to six, \(r\ge1\), and
\[
 L=\operatorname{lcm}(6,\operatorname{ord}_b(2),2\cdot3^r);
 \qquad \operatorname{ord}_1(2)=1 .
\]
There is an absolute \(c\) such that every \(k\ge c(1+\log b+r)\) and every \(H\ge(3L+1)k\) give, at the one positive unit terminal \(y\), **all** odd sources classes modulo \(b3^r\), meaning that every class modulo this odd modulus has a positive odd representative in the exact fiber. All routing exponents may be at least two.

To recall the arbitrary-clock point, fix \(J=H\bmod L\). The virtual carry construction chooses a free carry \(C\equiv 2^J y-3^k a\bmod b3^{k+r}\); its residue is a ternary unit and the interval width exceeds \(b3^{k+r}\). Lift the free powers in order by their common period; prescribe the virtual total congruent to \(J\) modulo that period, enlarged by \(L\) if necessary. This gives an ordinary path with the required terminal, residue and total congruent to \(J\bmod L\). Write \(s=v_3(2^L-1)\ge r+1\) (the binomial expansion of \(4^{3^r}\) gives the stated inequality). At each inverse step replace the virtual exponent by the least \(e\ge2\) in its class modulo \(L\), or by \(e+L,e+2L\). Preserving the current site modulo \(b3^s\), exactly one choice matches the virtual next site modulo \(3^s\) after division: the current site is a ternary unit and \(2^L\equiv1+c3^s\bmod3^{s+1}\), \(3\nmid c\). All choices preserve the residue modulo \(b\). The compressed total is at most \((3L+1)k\) and equals \(J\bmod L\). Increase the *last inverse exponent* by the remaining nonnegative multiple of \(L\). This preserves the final source modulo \(b3^r\) since \(v_3(2^L-1)\ge r+1\). All divisions and exact exponents follow from the edge equations with positive odd endpoints.

## Integer-valued interpolation

For \(p\) prime, \(p^r>d\), and \(t\equiv u\bmod p^r\), the vectors \(v_d(t),v_d(u)\) agree modulo \(p\). For nonnegative inputs this follows by comparing through degree \(d\) in \((1+X)^t\) and \((1+X)^u\) over \(\mathbb F_p\): \((1+X)^{p^r}=1+X^{p^r}\). The \(d+1\) rows with \(t=0,\ldots,d\) form a lower triangular integral matrix with diagonal one. Thus it suffices, at a given \(p\), to reach each \(t\bmod p^r\). At \(p>d\), it suffices instead to have any \(d+1\) distinct residues modulo \(p\), since the determinant is
\[
     \det\bigl(\tbinom{t_i}{j}\bigr)_{0\le i,j\le d}
            =\frac{\prod_{i<j}(t_j-t_i)}{\prod_{j=0}^d j!}.
                                                                    \tag{3}
\]
This identity follows by triangular change of basis from monomials.

## One geometric family covers infinitely many primes

Make \(k-2\) reverse steps from \(y\), always ending at a ternary unit and using an exponent in \(\{2,\ldots,7\}\). Such an exponent exists because \(2^e\bmod9\) traverses all six units, and a preimage \((2^e z-1)/3\) is a unit when \(2^e z\) is \(4\) or \(7\bmod9\). Call the resulting shared unit \(w\), and its cost \(H_0\le7(k-2)\). Reserve \(T=H-H_0\) for the last two inverse edges. Choose \(2\le t\le7\) so \(2^t\equiv2^T w-3\bmod9\); the right side is a unit. Use the pair of inverse exponents \(T-t-6j,\ t+6j\), for every \(0\le j\le d\). Both are positive (indeed at least two) for the displayed size threshold on \(H\). The positive odd sources are
\[
                 x_j=(2^T w-3-2^{t+6j})/9.                        \tag{4}
\]
The congruence ensures integrality of both edges: first reduce the affine identity modulo three, then divide the remaining equation by three. Exponents at least two ensure positivity on the reverse path. Hence (4) is a single set of \(d+1\) ordinary witnesses at exactly the required two clocks.

At every \(p>d\) with \(p\ge5\) and \(\operatorname{ord}_p(64)>d\), the numbers in (4) are distinct modulo \(p\), since each difference is a \(p\)-unit multiple of \(64^{j-i}-1\). The same is true of their half-odd coordinates, and (3) applies simultaneously at all these primes.

## The finitely many exceptions fit the same clocks

If \(p>d,\ p\ge5,\ \operatorname{ord}_p(64)\le d\), then \(p\le64^d\) and \(\operatorname{ord}_p(2)\le6d\), since \(p\mid 2^{6j}-1\) for some \(1\le j\le d\). In the routing result take \(b=p,r=1\). The required odd depth is \(O(d+1)\), \(L=O(d+1)\), and \(H=O((d+1)k)\) suffices as a threshold. At every higher \(H\) this realizes all \(t\bmod p\), because two is invertible modulo \(p\).

For \(5\le p\le d\), let \(p^u\) be the smallest power \(>d\). Use \(b=p^u\le pd\le d^2,\ r=1\). Now the threshold on \(k\) is \(O(1+\log d)\) and \(L=O((d+1)^2)\). This realizes the required \(t\)-residues. For \(p=3\) use \(b=1\) and the smallest \(3^r>d\), thus \(L=O(d+1)\) and \(k\gg1+\log d\) suffice.

For \(p=2\), take the smallest \(2^u>d\) and set \(s=u+1\). We need all positive odd classes modulo \(2^s\). Choose an odd representative \(1\le n_a<2^s\) for each, follow it forward for \(s\) odd edges to an odd unit \(z_a\), and let \(B_a\) be their total cost. We have \(s\le B_a\le3s\), since \(2^{B_a}z_a\le4^s n_a\) by \(3n+1\le4n\). Route from \(y\) backwards at grades \((k-s,H-B_a)\) to a positive odd \(w_a\equiv z_a\bmod3^s\). This takes \(b=1,r=s\), so \(L=O(3^s)=O((d+1)^{\log_2 3})\). The displayed absolute common thresholds are sufficient for every \(a\). Append the \(s\) reverse edges of the chosen prefix. Their integrality follows by successively subtracting the congruent old edges, dividing one factor of three at a time. Each new integer \((2^e z-1)/3\) from a positive odd \(z\) is positive and odd. The final source differs from \(n_a\) by \(2^{B_a}(w_a-z_a)/3^s\), a multiple of \(2^s\). This proves dyadic coverage at the same \(k,H\).

## From local ranks to integral equality

Let \(\Gamma\subseteq\mathbb Z^{d+1}\) be the left side of (1). The rows generate all of \(\mathbb F_p^{d+1}\) after reduction at each prime, by the preceding arguments. Reduction at even one prime gives full rational rank, hence \(\Gamma\) has finite index. If a prime divided that index, the Smith normal form would give rank less than \(d+1\) modulo this prime. Thus the index is one. Newton expansion by successive integer forward differences gives integer coefficients in the binomial basis for every rational polynomial integer-valued on \(\mathbb Z\). Applying its coefficient matrix to (1) proves the vector and fractional-lattice forms.

There is also a joint statement when the two clocks appear as polynomial variables. Let \(F(t,k,H)\) be any finite vector of rational polynomials, integer-valued on integer triples. The lattice generated by \(F(t_x,k,H)\) over the entire fixed-\(y\) basin equals the one over all \(\mathbb Z^3\). In fact for every finite modulus \(m\) the companion Theorem 3 realizes every desired triple residue for \((t,k,H)\), using modulus \(2m\) on the odd source. Clear a fixed common denominator \(D\) from the coefficients of \(F\); matching triples modulo \(Dm\) matches their integral evaluation vectors modulo \(m\). If \(\Gamma\) denotes the basin-generated subgroup and \(\Lambda\) the generic subgroup in \(\mathbb Z^\ell\), then every \(v\in\Lambda\) belongs to \(\Gamma+m\mathbb Z^\ell\) for every \(m\). Smith normal form gives \(\bigcap_{m\ge1}(\Gamma+m\mathbb Z^\ell)=\Gamma\), including when \(\Gamma\) has smaller ambient rank. Thus \(\Lambda=\Gamma\). The fractional version again follows by clearing denominators. This joint assertion concerns unbounded clocks across the fiber choices; (1) gives the stronger single-fiber assertion in the source variable.

## Consequence for a proposed height argument

A high-rank lattice estimate can be stronger than the product formula on one integer if there is *extra* local divisibility in a large image and an opposing bound on its real norm. Here the entire integral source-moment image has been computed. Equation (2) retains the complete weighted offset of each path. At this late range of clocks it supplies no further determinantal divisor beyond what polynomial evaluation at all odd integers would give. The result applies even after dividing a polynomial by its generic fixed divisor or using different integer output coordinates. It leaves room for observables of the internal path, or a combination of archimedean confinement and selected shorter clocks. The exhibited heights can be exponentially larger than the terminal \(y\); full integral span alone gives no smaller ordinary witness. [Rubinstein's working guide, pp. 3–5, for the general lattice mechanism and its separate hypotheses](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf)

## An additive clock budget above the minimum for this terminal

Let \(C_k(y)\) be the minimum total cost of a length-\(k\) inverse word at \(y\) whose source is an odd ternary unit. Set \(C_0=0\). Every unit admits a unit inverse child at cost at most four. Indeed the good residues for \(2^e y\bmod9\) are 4 and 7, and every four consecutive exponents contain a good one, by the six-element power cycle modulo nine. All earlier reverse vertices are necessarily ternary units if an inverse step follows. Hence every nonempty \(S_{y,k,H}\), even with a terminal-side reverse path ending at a multiple of three, satisfies \(H\ge C_{k-1}(y)+1\ge C_k(y)-3\).

There are absolute \(a,b\) such that, for every \(d\ge1\),
\[
              k\ge a(d+1),\qquad H\ge C_k(y)+b(d+1)^3             \tag{5}
\]
imply the same integral equality (1). To see this, fix \(r=\lceil a(d+1)\rceil\) with \(a\) large enough for the first theorem and take \(k\ge r\). In a minimizing reverse path of length \(k\), retain its first \(k-r\) edges at total cost \(s\). Its current positive unit \(w\) is fixed and \(s\le C_k(y)-r\). All remaining \(r\)-edge paths at \(w\) of cost \(H-s\) belong, after concatenation, to \(S_{y,k,H}\). Their cost satisfies the main theorem at \(r\), by choosing \(b\) large enough. Thus even a growing total depth \(k\) costs only the displayed additive overhead above its own least attainable unit-ended clock.

One can express the asymptotically sharp worst-terminal clock coefficient without evaluating it. Put \(W_k=\max_y C_k(y)\) over positive odd ternary units. A length-\(k\) word is admissible with unit source solely by a congruence on \(y\bmod3^{k+1}\), and integer inverse quotients from positive input are positive odd. Thus the maximum is attained on finitely many residue classes. Concatenating a minimizing path of length \(i\) with one of length \(j\) from its current unit gives \(W_{i+j}\le W_i+W_j\). Therefore \(\tau=\inf W_k/k=\lim W_k/k\), with \(k\ge1\). Given \(\epsilon>0\), all sufficiently large \(k\), all terminals, and all \(H\ge(\tau+\epsilon)k\) have (1) through every \(1\le d\le c_\epsilon k^{1/3}\), by (5). For each sufficiently large \(k\), take a terminal with \(C_k(y)=W_k\). Its fiber at every \(H\le(\tau-\epsilon)k\) is empty, since \(H\ge W_k-3\) would be necessary.

The critical forward coefficient \(\alpha=\log_2 3\) is strictly less than \(\tau\). Each word of \(k\) positive exponents of total at most \(h\) can be admissible at only one terminal residue modulo \(3^k\), by its complete affine equation. There are \(\binom hk\) such words when \(h\ge k\), and \(2\cdot3^{k-1}\) unit residues. With \(h=\lfloor sk\rfloor\), the exponential rate of the former is at most \(s\mathcal H(1/s)\), where \(\mathcal H(u)=-u\log u-(1-u)\log(1-u)\). At \(s=\alpha\) this is strictly less than \(\alpha\log2=\log3\), since \(1/\alpha\ne1/2\). The same strict inequality holds on a right neighborhood. For all large \(k\) some ordinary terminal thus has \(C_k(y)>sk\) at a fixed \(s>\alpha\). The optimal inverse speed itself is studied in [the minimax inverse-speed paper, §2](https://rstation.ai/problems/collatz/papers/229/v1). The new implication here transfers its minimum-cost clock to full integer polynomial evaluation.

## Persistence along a supplied forward ray and its exact carry index

Fix any positive odd ternary unit \(a\), let \(q_i=U^i(a)\), and let \(A_i\) be its ordinary total cost up to \(q_i\). Choose once and for all any \((r,E)\) satisfying (5) at \(a\). Every original source in \(S_{a,r,E}\) belongs to \(S_{q_i,r+i,E+A_i}\) for every \(i\), by appending the same genuine path from \(a\). Consequently the same fixed finite witnesses give full source-moment span at every one of these moving terminals and exact clocks. They work equally well if a point of the ray repeats.

The complete carry of this extended path at coordinate \(t\) is
\[
 C_i(t)=2^{E+A_i}q_i-3^{r+i}(2t+1)=b_i+s_i t,\qquad
 s_i=-2\cdot3^{r+i}.
\]
For \(0\le j\le d\), the polynomial \(\binom{b_i+s_i t}{j}\) is integer-valued on all integers (using polynomial binomials at negative arguments). Its Newton coefficients give an integral triangular substitution matrix with diagonal \(s_i^j\), by comparison of leading terms. It takes generic source-moment vectors to carry-moment vectors. Therefore the exact index of the carry-moment lattice at each of the displayed fibers, including using only the original fixed witnesses, is
\[
                         (2\cdot3^{r+i})^{d(d+1)/2}.                 \tag{6}
\]
This is a determinantal calculation on a single supplied ordinary orbit with no resampling of witnesses. Affine carry growth contributes exactly its generic substitution determinant.

Real positivity is a separate restriction on the same vectors. For \(d\ge2\), a convex combination of sampled \(v_d(t_j)\) can equal \(v_d(t_*)\) only if some sampled coordinate actually equals \(t_*\). Evaluate the linear functional corresponding to \((t-t_*)^2\). Its values are nonnegative, and every sample with positive weight must make the square zero. The signed integral combinations in (1) therefore supply no lower positive ancestor by themselves.
