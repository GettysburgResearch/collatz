# Full denominators of spliced laps and proper factors

The shortcut map on rationals of odd denominator sends an even numerator to half the value and an odd numerator to three halves the value plus one half. We use chronological binary words. The fixed value of a nonempty word is called its anchor.

## Splicing same-side laps

Choose a finite cyclic list of nonempty words. Word $i$ has length $L_i$, weight $u_i$, multiplier $\gamma_i=3^{u_i}/2^{L_i}$ and reduced anchor $a_i=p_i/b_i$ with $b_i>0$. Suppose all multipliers lie below one, or all lie above one. Suppose the list uses at least two distinct anchors. Write $R=\max_i a_i-\min_i a_i>0$, and let $d'$ denote the reduced denominator of the anchor of the full concatenation.

At **every cut at a maximal or minimal selected anchor**, one has

$$
                        d' b_i R>2^{L_i}.                              \tag{1}
$$

If several successive words at this extremum have the same anchor, the exponent can be replaced by their combined length, measured from the start of that run. Both assertions allow any number of pieces, including a run crossing the presentation boundary.

For a primitive positive ordinary cycle of least period $n$, splice any cyclic list of full rotations that includes two distinct phases. Its new cyclic anchor satisfies $d'R>2^n$. Repeating the same extremal rotation $r$ consecutive times gives $d'R>2^{rn}$ from the start of that run. The same statements hold for one negative ordinary cycle, or for a rational cycle with the corresponding factor $b_i$. One may also select laps from several cycles if their multipliers all lie on the same side of one.

**Proof.** A word of length $L$ and weight $u$ acts on its parity cylinder by the affine map

$$
 F(x)=(3^u x+C)/2^L,\qquad
 C=\sum_{j=1}^u 2^{i_j}3^{u-j},\qquad 0\le i_1<\cdots<i_u<L.
$$

Its anchor is $a=C/(2^L-3^u)$ and realizes the required parity word. Indeed the parity cylinder is the single class $3^u x+C=0\bmod 2^L$, since each bit restricts the preceding cylinder to one of its two lifts. The anchor satisfies this congruence. All cuts in a periodic trajectory have the same reduced denominator: each parity step can only divide the previous odd denominator, and it returns after a lap.

Write $F_i(x)=\gamma_i x+(1-\gamma_i)a_i$. The fixed point $z_i$ of the concatenation starting at cut $i$ is a weighted sum of the $a_j$. In chronological order the coefficient on $a_j$ is $(1-\gamma_j)\prod_{k\ {\rm after}\ j}\gamma_k/(1-\prod_k\gamma_k)$. The coefficients sum to one by telescoping and are strictly positive under either hypothesis. Thus every $z_i$ lies strictly between the extremes. It shares its first $L_i$ bits with $a_i$. If $z_i=P_i/d'$, the native dyadic congruence gives $2^{L_i}\mid b_iP_i-d'p_i$. This integer is nonzero at an extremal cut. Its absolute value is strictly less than $d'b_iR$, proving (1). A consecutive run with the same anchor has that anchor as its affine fixed point, so the proof applies to its combined word.

If every selected anchor agrees, the mixed anchor equals it. In particular a pure repetition preserves the original reduced denominator and least period. Distinct rotations at different phases of a primitive cycle have distinct anchors. Mixed contractions and expansions can fail (1). The positive word $10$ has anchor $1$, the negative word $1$ has anchor $-1$, and their concatenation $101$ has anchor $-7$.

## Size of any signed cyclic anchor

The following numerical exponents use Rhin's external estimate $|n\log2-u\log3|\ge n^{-13.3}$ for $n\ge2$, $0<u<n$. Let $p=\log_3 2$. There is an absolute constant $C_0$ such that every cyclic anchor of a length-$n$ word satisfies

$$
                   |a|\le C_0 n^{13.3} 2^{(1-p)n}.                    \tag{2}
$$

Rotations satisfy the same bound. An exact elementary bound before inserting the irrationality measure is $|a|\le 2^{n-u}(3^u-2^u)/|2^n-3^u|$. [Rozier–Terracol v5, Proposition 6.3, p. 19](https://arxiv.org/pdf/2502.00948v5#page=19)

Indeed $i_j\le n-u+j-1$ in the formula for $C$, giving the displayed numerator bound by summation. For $\Lambda=|n\log2-u\log3|$, the denominator equals $\max(2^n,3^u)(1-e^{-\Lambda})\ge(1-e^{-1})n^{-13.3}\max(2^n,3^u)$. Below the critical weight $u\le pn$ the resulting exponential factor is bounded by $(3/2)^u\le 2^{(1-p)n}$. Above it the factor is at most $2^{n-u}\le2^{(1-p)n}$. Words of weights $0$ and $n$ have anchors $0$ and $-1$.

Consequently mixed same-side equal-length laps with $b_i\le Q$ satisfy

$$
                          d'Q\gg n^{-13.3}2^{pn}.                     \tag{3}
$$

In particular every nonconstant splice of rotations of a hypothetical positive integer lap has an exponentially large reduced denominator as $n\to\infty$.

## Proper factors of a genuine periodic orbit

Let $y$ be any phase of a signed rational orbit with reduced denominator $d$ and least period $N$. Take the factor of length $1\le L<N$ starting at $y$, close it periodically and write its reduced anchor as $a/q$. Then

$$
                      d q\,|y-a/q|\ge 2^L.                            \tag{4}
$$

Both signs of the parent and both signs of the factor are permitted. The factor may be a power. Its anchor and denominator always refer to its reduced value.

The factor shares all $L$ initial bits with $y$. Equality of the two values would imply a return of the parent after $L<N$ steps. Their reduced cross difference is therefore a nonzero integer divisible by $2^L$. Together with (2), this gives simultaneously at every proper factor

$$
                   d q\gg N^{-13.3}2^{L-(1-p)N}.                      \tag{5}
$$

If the parent is nonzero, choose a phase of minimum absolute value $m$. For **every** proper prefix length $1\le L<N$ at this phase, a stronger bound is

$$
                       d q\gg N^{-14.3}2^{pL}.                        \tag{6}
$$

In fact $m\ll N^{14.3}$. On a positive lap, the logarithmic gap $|N\log2-u\log3|$ is the sum of $\log(1+1/(3|y_j|))$ over odd phases, bounded by $u/(3m)$. On a negative lap, odd steps in magnitude have the form $(3|y_j|-1)/2$ since every phase stays negative. The minimum must occur at an odd phase because an even step halves its nonzero magnitude. The following magnitude is at least $m$, hence $m\ge1$. The absolute gap is then the sum of $-\log(1-1/(3|y_j|))\le1/(2|y_j|)$. Rhin gives the claimed minimum bound when $0<u<N$. The remaining nonzero fixed point is $-1$, with no proper factor. Substituting $|y-a/q|\le m+C_0 L^{13.3}2^{(1-p)L}$ into (4) proves (6).

There is also an exact endpoint formula. Let $P_0=dy$, $P_L=dT^L(y)$, $\Delta=P_L-P_0$ and $D_L=2^L-3^{s_L}$. Then

$$
                 \frac q{\gcd(q,d)}
                    =\frac{|D_L|}{\gcd(|D_L|,\Delta)}.                \tag{7}
$$

Indeed the affine identity gives $d(a/q)=P_0+2^L\Delta/D_L$. The left side of (7) is the denominator of this rational and $D_L$ is odd. In particular at the two ends of complementary factors in a parent lap, both reduced-denominator tests use the same displacement up to sign.

At the minimum-magnitude cut, set $s=N-L$. Each inverse shortcut step satisfies $|x|+1\le2(|T(x)|+1)$, so $|T^L(y)|+1\le 2^s(m+1)$. The displacement $\Delta$ is nonzero for every proper prefix. Rhin and (7) give

$$
                   d q\gg N^{-27.6}2^{L-s}.                           \tag{8}
$$

Here $|D_L|\gg L^{-13.3}2^L$, also valid for the all-even and all-odd factors after adjusting the absolute constant. We used $|\Delta|\le 2d\,2^s(m+1)$ and $m\ll N^{14.3}$. In particular, for **any** sequence of nonzero ordinary cycles of least periods $N\to\infty$, the denominator of **every** proper prefix $L=N-o(N)$ at the minimum obeys $q=2^{N+o(N)}$. The upper bound for positive parents follows from $3^u<2^N$ and $q\le |D_L|$. For negative ordinary parents the $N$ magnitudes are distinct positive integers. The complete logarithmic gap is at most $\tfrac12\sum_{j=1}^N 1/j$, so $3^u\le2^N\exp((1+\log N)/2)$, giving the same exponential upper bound. The exact full factor has the original denominator one.

The same minimum bound sharpens (1) for any mixed splice of rotations chosen wholly within $r$ steps before or after the minimum of an ordinary lap. All those phases have absolute value at most $2^r(m+1)$ by the forward and inverse step bounds. Thus $d'\gg 2^{n-r}n^{-14.3}$ for any nonconstant splice from this window. The number of selected pieces can grow arbitrarily.

Endpoint information from the other side of the same factor carries exactly the original integer. If $y_j,x_j$ are the physical phases of the parent and repeated factor after $j\le L$ bits, and $s_j$ is the intervening weight, then

$$
      dq(y_j-x_j)=3^{s_j}2^{L-j}k,\qquad
      k=2^{-L}dq(y_0-x_0)\in\mathbb Z\setminus\{0\}.                 \tag{9}
$$

The cut $j=L$ exchanges the initial factor $2^L$ for $3^{s_L}$. Treating the two divisibilities as independent would count the same $k$ twice. At the exact full return $L=N$, $k=0$.

## Growth with the least period of the splice

Take a fixed dictionary of $a\ge2$ distinct same-side words of common length $n$. Let the chosen sequence of dictionary words have **least period $k\ge2$ in dictionary symbols**. Restrict the dictionary to the $a$ words actually used, and let $R$ be their anchor span. For equal lengths, distinct words have distinct anchors by their native parity cylinders. The common denominator of the concatenation satisfies the additional elementary inequality

$$
      d'R>2^{n(\lceil\log_a k\rceil-1)}
           \ \ge\ 2^{-n}k^{n/\log_2 a}.                              \tag{10}
$$

In fact the $k$ boundary phases of one least dictionary period are distinct. Equal phases have identical future binary words. Cutting those future words every $n$ bits gives identical dictionary-symbol sequences, inconsistent with two distinct boundary indices modulo $k$. This proof does not require the least physical period $P$ to equal $nk$; it gives $P\le nk$. All boundary phases are strictly between the extremal anchors by the same-side convexity proof. Among the $k$ boundary phases, two share their first $\ell=\lceil\log_a k\rceil-1$ symbols, since $a^\ell<k$. For $\ell=0$ the shared prefix is empty. These phases have a common reduced denominator $d'$. The nonzero difference of their integer numerators is divisible by $2^{n\ell}$ and has absolute value less than $d'R$. This proves (10) and is the elementary count of native parity cylinders in a bounded interval.

For rotations of an ordinary lap, $a\le n$ and (1) also yields $d'R>2^n$. Together with (2), these imply that for **every** fixed $A>0$, all sufficiently large parent periods $n$ give $d'>(nk)^A$ for every nonconstant cyclic list of rotations, when $k$ is its least dictionary period. Indeed if $k\le n^4$, then $d'\gg 2^{pn}n^{-13.3}$ suffices. If $k>n^4$, put $e_n=n/\log_2 n$. Now $e_n\log_2 k>4n$, while

$$
          \log_2 d'\ge e_n\log_2 k-(2-p)n-O(\log n)
                     \ge \tfrac12 e_n\log_2 k .
$$

Since $e_n\to\infty$ and $\log(nk)\le(5/4)\log k$, this proves the assertion. The uniform large-parent statement uses the external input in (2).

In particular there is an absolute $c>0$ such that **every** nonconstant rotation splice of a positive ordinary primitive lap satisfies $d'\ge c P^2$. For large $n$ take $A=2$ above. For each of the remaining finitely many $n$, (10) gives $d'\gg_n k^{e_n}$, since those finitely many length-$n$ words have a bounded range of anchors. We have $e_n\ge2$ for $n=2$ and $n\ge4$. At $n=3$ a positive primitive word must have exactly one odd symbol, with possible anchors $1/5,2/5,4/5$; none is ordinary. A period-one lap has no two distinct rotations. The proof uses the stated bound on the least physical period. For fixed ordinary parents that are negative, (10) still gives $d'\gg_n k^{e_n}$, including the possible length-three case with exponent $3/\log_2 3$.

## Provenance and implication

The cycle anchor formula and parity cylinders are classical. PR200 already uses the nonzero dyadic cross difference for compact periodic shadows of escaping integer paths and proves the sharp exponent $d=2^{n+o(n)}$ for a specialized family of traces and short extensions. Our phase3 rational-piece results use related endpoint constraints and, for some asymptotic conclusions, the Subspace Theorem. Here (1), (4), (7), (9) and (10) are elementary, with same-side convexity and least period identifying the cuts where the cross difference cannot vanish. The polynomial-exponent estimates (2), (3), (5), (6) and (8) invoke the logarithm-separation input. [Halbeisen–Hungerbühler](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf), [PR200 fixed snapshot](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/FULL_DENOMINATOR_SHORT_CLOSURES.md), [rational pieces](../phase3/RATIONAL_PIECES.md)

A density-one exclusion of small denominators does not propagate by taking powers, which preserve least period. Mixing rotations of a long ordinary cycle produces expensive denominators by (3). Thus these two constructions do not force a positive-density family of new ordinary least periods from one candidate. To eliminate the isolated candidate using (6), one would need an independent theorem producing a proper long prefix at its minimum with a sufficiently small cyclic denominator. The candidate's own exact full return provides no such proper prefix.
