# Which affine pairs admit a common Collatz certificate?

**PROPOSED, unconditional.** All iterates are of the positive shortcut map $T$, including when a starting value is written $5t+1$. Write $x\sim y$ if the two positive orbits have a common value at independent clocks. Two different questions arise for an affine family. One asks for a meeting for each ordinary parameter. The other asks for two fixed words that certify every parameter in a binary residue class. The distinction can be decided exactly for linear families.

## A single family equivalent to the full conjecture

Every positive integer reaches 1 if and only if
$$
                     t\sim 5t+1\qquad\text{for every integer }t\ge1. \tag{1}
$$
If all orbits reach 1, they meet there. Conversely suppose (1) and argue by strong induction on the starting value $n$. An even $n$ halves. For odd $n>1$, the following ordinary value $y$ belongs to the component of $n$ and equals $5t+1$ with $1\le t<n$.

| $n\bmod5$ | $y$ | $t$ |
|---|---:|---:|
| 0 | $3n+1$ | $3n/5$ |
| 1 | $n$ | $(n-1)/5$ |
| 2 | $(3n+1)/2$ | $(3n-1)/10$ |
| 3 | $2n$ | $(2n-1)/5$ |
| 4 | $4n$ | $(4n-1)/5$ |

Doubling a start preserves its component, and $3n+1$ halves to $T(n)$. Thus (1) and the induction hypothesis put $n$ in the component of 1. Every member of that component reaches 1, since 1 and 2 form a cycle. [Lean proof, `collatz_iff_five_ray`](HighBit.lean)

For (1) even a single fixed pair of parity words can work for **at most one** parameter. Its two endpoint functions have slopes $3^q/2^i$ and $5\cdot3^{q'}/2^j$, which are different by unique factorization. The universal statement in (1) remains open. An unknown finite exceptional set can be removed. A counterexample would force at least $\log_2 X-O(1)$ failed parameters by $X$. [Proof](EVENTUAL_FIVE_RAY.md)

## Classification and a constructive bound

Fix $a,c>0$ and integer offsets $b,d$. For an integer $v>0$ let $v_*$ be what remains after removing all its factors of 2 and 3. The following are equivalent.

1. $a_*=c_*$.
2. **Every** prescribed binary class of $t$ contains a subclass on which $at+b$ and $ct+d$ meet on two fixed words, for all sufficiently large ordinary parameters.
3. Some fixed pair of words gives a meeting for two distinct ordinary parameters.

Moreover if the original class fixes $h$ bits, the new subclass fixes at most $O(L)$ bits in total, and both clock lengths are $O(L)$, where $L=1+h+\log_2(2+a+c+|b|+|d|)$. The constants are absolute. The subclass works for every lift with positive starts. In the other direction, if $a_*\ne c_*$, any **actual** meeting at clocks at most $H$ requires
$$
              t\le (|b|+|d|+2)6^H. \tag{2}
$$

For necessity, the two words give affine functions. Equality at two distinct parameters forces equality of slopes, hence $a3^q2^j=c3^{q'}2^i$. For (2), multiply the two endpoint formulas by $2^{i+j}$. The coefficient of $t$ is a nonzero integer. The affine numerator offset for a length-$i$ word is nonnegative and strictly below $3^i$, by the affine offset bound (also at $i=0$). Taking absolute values of the remaining terms gives (2). This permits ordinary mergers with clocks growing with $t$.

For sufficiency, substitute $t=r+2^h u$, $0\le r<2^h$. On the first arm take $i=h+v_2(a)$ shortcut steps, on the second take $j=h+v_2(c)$. The parities on these prefixes are fixed. Composition, also valid on signed integer intercepts, leaves the first arm with odd coefficient $(a/2^{v_2(a)})3^q$ on $u$, and similarly for the second arm. If $a_*=c_*$, the ratio of these odd coefficients, putting the larger one on top, is $3^s$ for some $s\ge0$. The arms have the form $X,3^s X+D$ with $X$ an odd-coefficient affine function of the remaining parameter. The constructive pair argument chooses $O(s+\log_2(2+|D|))$ further binary digits so the two endpoints agree identically. Every step of the algorithm follows the shortcut map with the prescribed parity, and an odd coefficient makes each requested next bit realizable. The initial $i,j,s$ are $O(L)$ and the intercepts and $|D|$ are at most $2^{O(L)}$, since an integer step increases $1+|x|$ by at most a factor of two. This proves the bound and the equivalence. [Deterministic word construction](PREFIX_COMPRESSION.md) · [Exact affine-certificate checker](check_affine_rays.py)

The difference of the two physical clocks is forced to be $v_2(a)-v_2(c)$, and the difference of the two odd counts is $v_3(c)-v_3(a)$. The same classification holds for a finite list: all slopes must have the same $v_*$. Successively refine the parameter class for each pair consisting of the first arm and one other arm. Previously certified identities persist. Pad the first arm to its largest resulting clock and extend the matching arms by the same respective amounts. The common endpoint on a final subclass is itself affine with positive odd coefficient: each construction normalizes all fixed parameter bits by advancing the first arm that many steps plus $v_2(a)$. Padding to that clock removes all fixed bits on each other arm as well. For a fixed list size the total clock remains linear in $L$, with a list-size-dependent constant.

## Prescribing which component contains the pattern

For any compatible finite list above and any positive target $u$ coprime to three, in **every** prescribed binary parameter class there are infinitely many ordinary parameters for which **all** the arms reach $u$. We include the arithmetic argument for a common endpoint in a progression, since the progression may have factors other than 2 and 3. Strong sufficiency of general arithmetic progressions also appears in the work of Monks, Monks, Monks and Monks. [Prior result, Theorem 4.1](https://arxiv.org/abs/1204.3904)

Write the common endpoint as $z=y+Bv$ with $B>0$ odd, and put $B=3^s d$, $\gcd(d,6)=1$. Any finite word is realized on some binary class of $v$. Modulo $d$, its two forward branches are the permutations $E(x)=x/2$ and $O(x)=(3x+1)/2$. Their semigroup contains their inverses because the underlying set is finite. The permutations $OE$ and $EO$ have equal slope and offsets differing by $1/4$, a unit. Hence the semigroup contains translation by $1/4$ and acts transitively. The assertions modulo $d=1$ are vacuous.

Let $o$ be the order of 2 modulo $d$ (take $o=1$ for $d=1$), and $w=1+v_3(o)$. Prescribe a terminal word of $w$ odd steps followed by $e$ even steps, choosing $e$ so $-2^{-e}\equiv u\pmod{3^w}$. This choice is possible because 2 generates the units modulo every power of three. The terminal word sends any legal input to $u\bmod3^w$, since an odd step multiplies $x+1$ by $3/2$. Modulo $d$ the terminal word is a permutation. By transitivity first insert a word sending $y\bmod d$ to the preimage of $u\bmod d$ under this permutation. For the whole word, with $Q$ odd steps, the endpoints on its binary class form a progression $z'+d3^{s+Q}v'$, where $z'\equiv u\pmod d$ and $z'\equiv u\pmod{3^w}$.

Now choose $J$ a multiple of $2o$ with $2^J u\equiv z'\pmod{3^{s+Q}}$. Indeed $v_3(2^{2o}-1)=1+v_3(o)=w$, and repeated cubing increases this valuation by exactly one each time. Thus $2^{2o}$ generates the units congruent to 1 modulo $3^w$ in the required modulus. Arbitrarily large $J$ satisfy both congruences, so $2^J u$ is achieved by a positive lift. A further $J$ halvings reach $u$.

In particular **every component contains arbitrarily long intervals of consecutive ordinary starts**, with the first member in any prescribed binary class and above any prescribed threshold. Apply the finite-list theorem to $t,t+1,\ldots,t+M-1$. Their slopes agree, so their clocks and odd counts at the common endpoint agree as well. Every component has a positive ternary-unit target, by deleting initial halvings and taking an odd step if necessary. Therefore full Collatz is equivalent to the following covering statement: some constant $M$ suffices so that every sufficiently large interval of $M$ consecutive positive integers contains a start reaching 1. A second component would supply arbitrarily large intervals of exactly that length disjoint from the basin of 1.

Neither (1) nor the bounded-gap condition has been established for all ordinary inputs. The constructive classification supplies the wide blocks in each component, including any hypothetical second component.

## Compressing the parameters of the five-ray test

Although each fixed meeting in (1) singles out one parameter, two parameters can present the same question. At clock $h$ label $t$ by the endpoints **and odd counts of both** $t$ and $5t+1$. If $u,t$ share a label then $u\sim t$ and $5u+1\sim5t+1$. Hence (1) has the same truth value at these two parameters. The same pair of reductions works after translating both parameters by any common multiple of $2^h$ that preserves positivity.

**Uniform bound.** In any interval of $N\ge2$ positive parameters the number of joint labels at $h=\lceil\log_2 N\rceil$ is $O(N^{0.975})$, independently of its location. This bounds the number of distinct questions to be checked for (1). Merger of the two arms of a retained question remains a separate problem.

Here are the details. For either arm write $T^h(x)=3^q x/2^h+R_h(x)$ with $R_h\ge0$. In a complete binary block of parameters, each arm samples each parity word exactly once: its starting coefficient, 1 or 5, is odd. On exposing a fresh fair parity bit the new remainder is $R_j/2$ or $(3R_j+1)/2$ with equal probabilities, so its mean is $h/4$ at time $h$. An interval of length $N$ lies in at most two complete blocks of length $2^h$. Markov's inequality discards $O(N^{1-0.028}\log(2N))$ parameters at which either remainder exceeds $N^{0.028}$. The binomial tail discards $O(N^{H_2(0.595)})$ parameters at which either arm has more than $0.595h$ odd steps. Independence between arms is unnecessary.

Fix the remaining two odd counts. The arm with larger coefficient on $t$ spans $O(N^{0.595\log_2 3}+N^{0.028})$ integer endpoints. Once that endpoint is specified, the other lies within $2N^{0.028}$ of a fixed real value: eliminate $t$ from the two affine expressions, using the ratio of the smaller coefficient to the larger, at most one. Thus the label count in this group is $O(N^{0.595\log_2 3+0.028})$. There are $(h+1)^2$ count choices. Both $H_2(0.595)<0.974$ and $0.595\log_2 3+0.028<0.972$ leave room to absorb the logarithms in the stated bound.

For an explicit decidable test set, put $h(t)=\lceil\log_2(2t)\rceil$ and retain $t$ precisely when no $1\le u<t$ has its joint label at time $h(t)$. Full Collatz is equivalent to checking (1) on every retained parameter, by strong induction. Every interval of length $N$ contains $O(N^{0.975})$ retained parameters. Indeed those with $t\ge N/2$ have $h(t)\ge\lceil\log_2 N\rceil$, and only the first occurrence of each joint label at that common clock can survive. For $t<N/2$ partition the initial range into dyadic intervals and sum their sublinear bounds as a geometric series; in each such interval the same common-clock argument applies.

The same argument compresses **any fixed finite list** of odd-slope affine arms. In fact for any $\gamma<1-\tfrac12\log_2 3$ and $m$ fixed arms, all but $O(N^{1-\epsilon})$ parameters in every interval have at least $\lfloor N^\gamma\rfloor$ smaller parameters in the interval with the same full joint label, for some $\epsilon>0$. Take $0\le\gamma<1-\tfrac12\log_2 3$ (negative $\gamma$ is trivial), a count cutoff $p>1/2$ and remainder cutoff $N^\delta$ with $\gamma+p\log_2 3+(m-1)\delta<1$ and $\delta<p\log_2 3$. The atypical fraction is power-saving by the same two marginal estimates. The ordinary endpoints for each count vector give $O(N^{p\log_2 3+(m-1)\delta})$ typical labels by eliminating $t$ against the largest coefficient. At most the first $\lfloor N^\gamma\rfloor$ parameters per typical label can fail the multiplicity conclusion. Constants may depend on the arms and $\gamma$, and all starts in the interval must be positive.

### A sharper bound from the common binary digits

For two fixed positive odd slopes, both the number of joint labels and the count of retained parameters above are $O(N^{0.967})$. The improvement bounds the odd counts and the affine remainders together. Set $q_{\max}=\max_i q_i$ and $R_{\max}=\max_j R_h(x_j)$ for the two arms. In a complete $2^h$-block, the two next parities conditioned on the exposed parameter bits are either identical fair bits or opposite fair bits. Indeed, changing the next bit flips each parity by its odd coefficient times an odd power of three.

Put $u=0.32$ and $L=\max\{(1+3^u)/2,\;2^{-u}(1+3^{2u})/2\}$. For an arm $j$ let $b_{j,l}$ count the odds in its final $l$ steps, including $b_{j,0}=0$. For any arms $i,j$ and $0\le l\le h$,
$$
 \mathbb E\big[(3^{q_i}3^{b_{j,l}}2^{-l})^u\big]\le L^h .
$$
For the first $h-l$ bits use the ordinary fair-bit moment. For each remaining bit the identical-parity case gives the second term in $L$; opposite parities give a smaller or equal moment by $2\cdot3^u\le1+3^{2u}$. Iterated conditional expectation proves the inequality, also when $i=j$. Unfolding the remainder recursion bounds $1+R_{\max}$ by $(h+1)\max_{j,l}3^{b_{j,l}}2^{-l}$. Markov's inequality and the union bound now discard at most $O((h+1)^{1+u}2^{\theta h})$ starts for which $3^{q_{\max}}(1+R_{\max})>2^{\theta h}$, where
$$
 \theta=\frac{1+\log_2 L}{1+u}<0.966492.
$$
On the remaining starts fix the two counts and a dyadic bin $B\le1+R_{\max}<2B$. The larger-slope arm spans $O(3^{q_{\max}}+B)=O(3^{q_{\max}})$ possible integer endpoints, since each remainder is at most $(3/2)^{q_i}$. Eliminating the parameter leaves $O(B)$ endpoints on the other arm. Their product is $O(2^{\theta h})$, and there are only polynomially many count and bin choices. This proves the asserted exponent after covering the interval by complete blocks. The same argument for the retained set uses persistence of joint labels just as above.

## Two quantitative consequences

Let $G(X)$ be the longest interval in $[1,X]$ containing no start reaching 1, with value zero if no such interval exists. A second component would force
$$
 \limsup_{X\to\infty}\frac{G(X)}{\log\log\log X}=\infty .
$$
Indeed fix a ternary-unit target $u$ in that component. In an interval of $M$ consecutive starts take the critical profile clock $D=O(\log^2(2M))$. There are only $K=O(M^\rho/(1+\log M)^{3/2})$ different endpoint and odd-count pairs, and each tie persists under simultaneous shifts by $2^D v$. Start with $[1,M]$. Apply the affine construction successively to bring these $K$ arms to one state. Equivalently refine the cell of the interval's first member, retaining the original offsets $0,\ldots,M-1$. Each refinement costs at most a constant times the existing bit count plus $O(\log(2M))$, so the final clock is $H\le (D+\log(2M))\exp(O(K))$. Every arm has unit initial slope and its clock equals the number of fixed binary digits. If needed pad to $H\ge D$ by fixing more bits. [Critical profile count](CRITICAL_INTERVALS.md)

Write the common endpoint as $y+3^q v$ on this final class. For the canonical first member between 0 and $2^H-1$, the affine bound gives $0\le y\le2\cdot3^q$. If $q>0$ then $3\nmid y$ because the last odd step yields a ternary unit and halvings preserve it. Choose $J=O(3^q+H+\log(2M))$ with $2^J u\equiv y\pmod{3^q}$ and $2^J u$ large enough to give a positive first member above $M$. This uses a whole period of the powers of two, or simply large $J$ when $q=0$. The last member $X$ is at most $M+2^H(1+2^J u)$. Thus $X\ge M$, $G(X)\ge M$ and $\log\log\log X=O_u(\log H+1)=O_u(K+\log\log(2M))=o(M)$. In particular, an eventual bound $G(X)=O(\log\log\log X)$ would suffice to prove full Collatz. Such a bound is open.

### A polynomial synchronization time for a whole interval

There are absolute constants $C_0,C_1$ such that for every $M\ge2$ some binary class of starting values $a$ makes **all** $a,a+1,\ldots,a+M-1$ have the same endpoint and odd count at a common clock $H\le C_0 M^{C_1}$. This holds for every positive lift. First we reduce the number of distinct profiles to $O(\log M)$ in $O(\log M)$ steps.

Fix a class modulo $2^h$ for the first start. Its $K$ distinct profiles have current values $3^{q_i}(w+U)+e_i$, with free integer parameter $w$, accumulated odd counts $q_i$, common real center $U$, and errors $0\le e_i\le B_{\rm old}$. Initially use $w+1,\ldots,w+M$ with $h=0$, $U=0$ and $B_{\rm old}=M$. Profiles with the same count and value at $w=0$ agree for all lifts.

Choose the next $j$ bits $v$ of $w$ uniformly. Each arm samples a fair parity word since its coefficient is odd. Write $r_i$ for its new odd count and $R_i$ for its new affine remainder. Uniformly in $j$, $\mathbb E\sqrt{R_i}\le C_2$ for an absolute constant. The remainder recursion and $\sqrt{x+y}\le\sqrt x+\sqrt y$ give a multiplier $(1+\sqrt3)/(2\sqrt2)<1$ on the previous moment, plus a bounded term. Also $r_i\le0.55j$ except with probability $2^{-cj}$ for an absolute $c>0$ by the binomial upper tail. Choose $j$ large enough that
$$
 K2^{-cj}\le1/8,\qquad 2^{-(1-0.55\log_2 3)j}B_{\rm old}\le1.
$$
With probability at least $7/8$ every inherited error $3^{r_i} e_i/2^j$ is at most one. Simultaneously with positive probability one has $\max_i R_i\le(8C_2K)^2$ and at most $8C_2K/\sqrt B$ arms with $R_i>B$, for any prescribed $B\ge1$. Each of these last two tests fails with probability at most $1/8$ by Markov's inequality.

On such a refinement put $U'=(v+U)/2^j$. At new free parameter zero the endpoints are
$$
 3^{q_i+r_i}U'+3^{r_i} e_i/2^j+R_i .
$$
On further lifts the free parameter has coefficient $3^{q_i+r_i}$. The new maximum error is at most $1+(8C_2K)^2$. For each total odd count, the arms with $R_i\le B$ occupy at most $B+3$ integer endpoints. Taking $B=\max(1,(K/(h+j+1))^{2/3})$ bounds the new profile count by
$$
 K'\le C_3\big[(h+j+1)+(h+j+1)^{1/3}K^{2/3}\big]. \tag{3}
$$

Set $P=\lceil\log_2(2M)\rceil$ and $\nu=3/4$. At round $l=0,1,\ldots$ take $j_l=\lceil D(\nu^l P+\log_2(P+2))\rceil$. Stop after the first $r$ rounds satisfying $\nu^r P\le1$. Then $r=O(\log(2P))$ and $\sum_{l<r}j_l\le C_D P$ by the geometric series and $(\log(2P))^2=O(P)$. At every stage,
$$
 K_l\le C_4 P\,2^{\nu^l P}.
$$
This holds initially. Substituting it and $h+j+1\le(C_D+1)P$ in (3) proves the next bound, using $2/3<\nu$ and choosing $C_4$ sufficiently large to absorb its $C_4^{2/3}$ term.

To check the two clock requirements in this induction, take $D$ large first in terms of $c$, $1-0.55\log_2 3$ and $\nu$. For sufficiently large $P$, the fixed multiplicative constants $C_D,C_4,C_2$ each cost at most $\log_2(P+2)$ bits. The inductive bound controls $\log_2(8K_l)$; the preceding round bounds $\log_2 B_{\rm old}$ by $O(\nu^{l-1}P+\log_2(P+2))$ with an absolute coefficient. At round zero use $B_{\rm old}=M$. Since $\nu^{l-1}=\nu^l/\nu$, the chosen $j_l$ suffices for both tests. Bounded $M$ may be absorbed in the final constants.

At termination $K_r=O(P)$ and $h=O(P)$. Apply the affine-pair construction successively to these representatives, retaining every previous tie under further refinement. All original translates have unit slope so the pair identities have identical clocks and odd counts. Each new bit count is at most a constant times the previous bit count plus $O(\log(2M))$, by the constructive bound applied to the original translates. Thus $H\le(h+O(\log(2M)))\exp(O(K_r))=M^{O(1)}$.

The preceding construction in a prescribed component now gives $\log\log X=O_u(H+\log(2M))=O_u(M^{C_1})$. A second component would force $G(X)\ge c_u(\log\log X)^\eta$ along an unbounded sequence of $X$ for some absolute $\eta>0$ and $c_u>0$. Thus an eventual bound $G(X)=o((\log\log X)^\eta)$ would suffice to prove the full conjecture. This upper bound remains open.

### A lower bound for the meeting clock

There is a separate restriction for (1) even at one parameter. If $t$ and $5t+1$ meet before either orbit falls below $t$, their clocks cannot both be short: their maximum is at least $c t^\epsilon$ for absolute $c,\epsilon>0$. More generally replace $t$ in this lower bound by the smallest value $m$ seen on the two arms up to their meeting. Remove loops from the two prefixes ending at the meeting; the shortened paths are simple and their minimum is at least $m$. On a simple path supported in $[m,\infty)$ the sum of $1/x$ is $O(m^{\rho-1})$, by summing the critical interval count over dyadic shells. In the multiplicative formula for each path its logarithmic correction is therefore $O(m^{\rho-1})$. A meeting with odd counts $p,q$ at the shortened clocks $i,j$ forces
$$
 0< |(p-q)\log3-(i-j)\log2-\log5|\ll m^{\rho-1}+1/t.
$$
The term $1/t$ bounds $\log(5+1/t)-\log5$. Nonvanishing is unique factorization. The classical theorem on linear forms in the logarithms of $2,3,5$ bounds the left side below by a constant times $(2+i+j)^{-C}$ for an absolute effective $C$. This proves the clock lower bound, with adjustment at bounded $m$. This use of Baker–Wüstholz is separate from the elementary equivalence (1). [Linear forms theorem](https://doi.org/10.1515/crll.1993.442.19)

A second lower bound depends on the number of even inputs, with no restriction on either clock. Suppose the arms from $t$ and $5t+1$ meet and $B$ is the larger of their two even-step counts. Then $B\gg\log(2t)$ by elementary arithmetic for sufficiently large $t$. Using the same linear forms theorem gives
$$
 B\ge\log_2 t-O(\log\log(3t)).
$$
To see this, write the endpoint formula in the normalized form $3^p2^{-i}(t+E)$ for the first arm and likewise with $q,j,E'$ for the second. The nonnegative offsets $E,E'$ are at most $2^B$. Write $e=i-p$, $e'=j-q$, and $R=(3/2)^{p-q}2^{e'-e}$. Then $R(t+E)=5t+1+E'$. The case $2^B>t/4$ already gives the claimed bounds. Otherwise $4\le R\le7$ and $|R-5|\le (1+6\cdot 2^B)/t$. Taking logarithms bounds $|p-q|$ by $O(B+1)$ since $|e'-e|\le B$. Unique factorization gives $R\ne5$, and the rational denominator of $R$ is at most $2^{O(B+1)}$. This proves the elementary estimate. For the second bound apply the linear forms theorem to $\log(R/5)$, whose integer coefficients on $\log 2,\log 3,\log 5$ are all $O(B+1)$. It yields $|R-5|\gg(B+2)^{-C}$. If $B\le\log_2 t$, taking logarithms proves the result, and larger $B$ already suffices. [Affine offset bound](README.md#affine-identities) · [Linear forms theorem](https://doi.org/10.1515/crll.1993.442.19)
