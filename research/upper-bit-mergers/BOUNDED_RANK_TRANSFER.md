# What a bounded number of odd steps on the known arm can certify

**Proposed theorem.** Use the positive shortcut Collatz map. For a start reaching 1, write $r(n)$ for the number of odd inputs before its first arrival and $\tau(n)$ for that first clock. Let $x=16k+1>1$ be a start already known to reach 1, with $p=r(x)$, and put $y=2x-1$. A *lifted merger* means a meeting on finite parity words whose affine endpoint functions in the parameter $k$ agree. Such a meeting holds throughout a binary residue class.

There is an effective test, using at most $7(2p+1)^2+1$ simultaneous steps after the initial step on $y$, which decides whether **any** lifted merger exists at this $k$.

* If it exists then $y$ reaches 1, with $r(y)\le2p$.
* Otherwise every finite certificate that $y$ reaches 1 has
  $$r(y)\ \ge\ \frac{\lfloor\log_2 x\rfloor-1}{7(p+1)}. \tag{1}$$

For $p=2$ and $p=3$, the second alternative holds at **every** index of that rank. At rank four there is an infinite family where both starts reach 1 in exactly four odd steps. At fixed rank, the second alternative forces a certificate length in odd steps at least proportional to the number of binary digits of the input, if a certificate exists. Establishing its existence in all cases is the missing implication in [the basin criterion](THREE_RAY_ONE_SIDED.md).

## A bilinear bound for two parity words

After one odd step on $y$, synchronize the clocks on $U=x$ and $V=3x-1$. Write $U_i,V_i$ for their endpoints at common clock $i$ and $p_i,q_i$ for the odd counts. A lifted merger at this clock occurs exactly when $U_i=V_i$ and $p_i=q_i+1$. Conversely any independent-clock lifted merger of the original arms has this form: matching the initial slopes 16 and 32 by unique factorization forces the right clock to exceed the left by one and the two full odd counts to be equal. We show that if no lifted merger has occurred through $h$, then
$$
 h\le7(p_h+1)(q_h+1). \tag{2}
$$

For any input $u$, its endpoint on an $i$-step parity word with $a$ odd inputs has form $3^a2^{-i}(u+E)$, with $0\le E\le2^i$. This follows by summing $2^d/3^j$ over odd input positions $d<i$ and their ordinal numbers $j\ge1$. At time $i$ define the rational
$$
 D_i=V_i-3^{q_i+1-p_i}U_i.
$$

If $D_i=0$, then the two affine endpoint functions of $x$ are proportional. Take their common zero $u_*$ in the first input's coordinate. Reversing a legal word from zero gives a rational in the 2-adic integers with reduced denominator exactly $3^a$, where $a$ is its odd count. Indeed the inverses are doubling and $(2v-1)/3$. The first odd inverse gives $-1/3$ and subsequent odd inverses increase the power of three in the denominator by one. The two starting roots here are $u_*$ and $3u_*-1$. If $p_i=0$ these would be $0,-1$, and $-1$ is fixed. Otherwise their denominator exponents are $p_i$ and $p_i-1$, so $q_i=p_i-1$. Thus the slopes and endpoints agree. Under the survival hypothesis of (2), $D_i\ne0$ at all these clocks.

Take as base the arm with the smaller total odd count $r=\min(p_h,q_h)$, and let $s=\max(p_h,q_h)$. Write the other endpoint as a rational multiple (the ratio of the two slopes) of the base endpoint plus a remainder $R_i$. In the first orientation $R_i=D_i$. Its denominator divides $3^{p_i}$ and the offset formula gives $|D_i|\le5\cdot3^{q_i}$. In the opposite orientation $R_i=-3^{p_i-q_i-1}D_i$, of denominator dividing $3^{q_i+1}$ and absolute value at most $5\cdot3^{p_i}$. Thus $|R_i|\le5\cdot3^s$ and its denominator divides $3^{r+1}$ in either orientation.

Consider a run of $d$ even steps on the base. Its initial value is divisible by $2^d$. The other arm and $R_i$ have the same parities for the next $d$ steps, because their difference is divisible by $2^d$ among rationals of odd denominator. During the run, each new remainder is exactly the ordinary shortcut of the preceding remainder with that parity. This also follows by subtracting the scaled even base endpoint on each branch. All the remainders are nonzero and their denominators divide $3^{r+1}$. Hence each has absolute value at least $3^{-(r+1)}$. An even step halves this magnitude, and an odd step increases it by at most the factor $(3+3^{r+1})/2$. If the other arm takes $t$ odd steps during this run, then
$$
 3^{-(r+1)}\le 5\cdot3^s (3+3^{r+1})^t2^{-d},\qquad
 d\le 5+2r+2s+(3+2r)t.
$$

There are at most $r+1$ such runs, and the sum of their $t$ is at most $s$. Add the $r$ odd steps of the base, then use $r\le s$ to bound the total by $(r+1)(6+7s)\le7(r+1)(s+1)$. This proves (2).

## Applying the bound to actual certificates

For a convergent positive start $n$, define $K(n)=2r(n)-\tau(n)$. On the cycle $1,2$, one complete turn changes $2r-\tau$ by zero. Therefore $K(n)=2a-i+K(T^i(n))$ at every clock $i$, including after a first arrival. In the presence of a lifted merger, $y$ converges and $K(y)=K(x)-1$. Conversely that equality, when both converge, allows complete turns at 1 to match total odd counts and finish one clock apart. [Phase criterion](BASIN_PHASE.md)

The positive first-hit path satisfies $2^{\tau(n)}=n3^{r(n)}2^{e(n)}$, where $0\le e(n)\le r(n)\log_2(10/9)$. Indeed each odd input is at least 3 and contributes $\log_2(1+1/(3T^i(n)))$ to $e(n)$. Set $q=r(y)$. The phase equality implies
$$
 (2-\log_2 3)(q-p)=\log_2(y/(2x))+e(y)-e(x)\le q\log_2(10/9).
$$
Since $(10/9)^2<4/3$, we have $q\le2p$. By appending turns at 1 to the shorter of the two odd-count certificates, there is a lifted merger with total odd count $\max(p,q)$ on each original arm. Every prefix before that merger uses at most $2p$ odd inputs per arm. Applying (2) to the last unmerged prefix proves the stated uniform deadline. If the test fails, take $h=\lfloor\log_2 x\rfloor-1$. Neither synchronized start can reach 1 by $h$, since each step retains at least half its input. Their counts are at most $p$ and $r(y)-1$ whenever $y$ converges. Now (2) proves (1).

## The first three nontrivial ranks

At rank two let $9k+1=2^a$, with $6\mid a$ and $a\ge6$. The lower start first reaches 1 at clock $a+4$. The upper arm reaches $W=3^{a+1}-1$ after $a+5$ steps using $a+3$ odd inputs. If $y$ converges, $K(W)\ge-\log_2 W$ since $2T(n)/n\le4$ along every odd step. It follows that
$$K(y)-K(x)+1=2(a+1)+K(W)>(2-\log_2 3)(a+1)>0.$$

At rank three the odd exponents in the accelerated path to 1 are $2,c,A$, where $c\ge2$ because the first odd successor is $12k+1\equiv1\pmod4$. Thus $K(x)=6-(2+c+A)$. The [three-step inverse identities](RANK_THREE_MERSENNE.md#positive-inverse-paths-and-their-companions) take $y$ in $c+3$ steps, of which $c+1$ are odd, to $W=3^{c-2}(2^A-1)-1$. Since $W<3^{c-2}2^A$,
$$K(y)-K(x)+1=2(c-2)+A+K(W)>(2-\log_2 3)(c-2)\ge0.$$
Thus a lifted merger is impossible in both ranks, whether or not $y$ converges.

For an explicit rank-four family take $k=(2^e-14)/81$ with $2^e\equiv14\pmod{81}$ and $e$ sufficiently large. Such exponents form an infinite arithmetic progression since 2 generates the units modulo 81. After four steps the arms are $A=9k+1$ and $2A-1$, with two odd inputs on each path. The next two odd steps from $A$ give $(81k+14)/4=2^{e-2}$. From $2A-1$ the five parities odd, even, even, even, odd give $(81k+14)/16=2^{e-4}$. These parities can be checked at $k\equiv-14/81\pmod{32}$ and lift throughout that class. Two halvings bring the first endpoint to the second, proving a lifted merger at clocks eight and nine. Each arm first reaches 1 after exactly four odd inputs.

## Which ranks admit bounded lifted mergers?

Every integer $p\ge4$ occurs infinitely often as the common exact rank of a pair with a lifted merger. Take a fixed odd ternary unit $t$ of rank $s=p-4$. In the rank-four construction replace $2^e$ by $2^e t$. The condition $2^e t\equiv14\pmod{81}$ admits an exponent class modulo 54. For all sufficiently large such $e$, exactly the same initial words land at $2^{e-2}t$ and $2^{e-4}t$, each with four odd inputs. After halvings to $t$ both arms use precisely $s$ further odd inputs to their first arrival at 1. The intermediate values before $t$ exceed 1 for large $e$, apart from $t$ itself if $s=0$.

Every integer $p\ge2$ also occurs infinitely often as the exact rank of a first arm with **no** lifted merger. Take a fixed odd ternary unit $u$ of rank $p-2$ and let $a$ grow along the class $2^a u\equiv1\pmod9$. Put $k=(2^a u-1)/9$. The first arm reaches $2^a u$ at clock four with two odd inputs, so has rank $p$. The second arm reaches $2^{a+1}u-1$ at clock four and its next $a+1$ inputs are all odd. These inputs exceed 1 for large $a$. Consequently any finite witness on that arm must use at least $a+3$ odd inputs. For $a+3>2p$ the bound for a lifted merger excludes every such merger, independently of whether the second arm converges.

The required odd ternary units exist at every rank. Start with 1 at rank zero. Given any odd ternary unit $v$ of rank $j$, choose a sufficiently large $d$ with $2^d v\equiv4\pmod9$, using that 2 generates the units modulo 9. Then $(2^d v-1)/3>v$ is an odd ternary unit whose next accelerated odd iterate is $v$. Its rank is exactly $j+1$.

## Explicit lower bounds when either arm has rank at most three

Suppose first $r(x)\le3$ with $k>0$. Put $9k+1=2^a u$ with $u$ odd. The first four steps from $x$ use two odd inputs and end at $2^a u$. Consequently $u=(2^h-1)/3$ with $h\ge2$: if $u>1$ it takes one accelerated odd step to 1, and if $u=1$ use $h=2$. The partner $y$ reaches $2^{a+1}u-1$ after four steps, again with two odd inputs. A run of $a+1$ odd steps takes it to

$$
 W=3^a2^h-(3^a+1).
$$

The next $h$ parities are those of the negative integer $-(3^a+1)$, since the starting difference is divisible by $2^h$. For a negative integer $-M$, each even step halves its magnitude and each odd step multiplies its magnitude by $(3-1/M)/2$. Every resulting integer is still negative. Thus if the signed trajectory uses $t$ odd inputs in $h$ steps, $1\le|T^h(-M)|\le M3^t/2^h$. Applying this at $M=3^a+1$ gives $t\ge h\log_3 2-\log_3(3^a+1)$. All these steps count before the partner can first reach 1. Its first four states and the following increasing odd run start above 1, and $W>2^{h-1}$ except when $(a,h)=(0,2)$, which would force $k=0$. Therefore $T^i(W)>1$ for $i<h$.

If $y$ converges, its rank $b$ satisfies $b\ge a+3$ and $b\ge3+(h-1)\log_3 2$ since $3^a+1\le 2\cdot3^a$. Also $x=(16\cdot2^a(2^h-1)-21)/27<2^{a+h}$. Eliminating $a,h$ gives the explicit bound

$$
 r(y)>3+\log_6(x/2).
$$

Now suppose instead $r(y)\le3$ with $k>0$. The first four steps from $y$ end at the odd integer $18k+1>1$. Hence $r(y)=3$ and $18k+1=(2^h-1)/3$. The resulting condition $2^h\equiv4\pmod{54}$ gives $h=18s+2$ with $s\ge1$, since 2 has order 18 modulo 27. At clock four the lower arm is $(2^{h-1}+1)/3$, an odd integer. Its next step gives $2^{h-2}+1$. This shadows the ordinary cycle from 1 for another $h-2=18s$ steps and reaches $W'=3^{9s}+1$. At each of these clocks $i\le h-2$, the exact state is $T^i(1)+3^{\lceil i/2\rceil}2^{h-2-i}>1$. Thus, whenever $x$ converges,

$$
 r(x)\ge3+9s=2+h/2>2+\tfrac12\log_2 y,
$$

where $y=(16\cdot2^h-37)/27<2^h$. Also $K(y)=2-h$ and $K(x)=1+K(W')$, so $K(y)-K(x)+1=2-h-K(W')\le2-h+\log_2 W'<0$, using $3^{9s}+1<4^{9s}$. This excludes a lifted merger when the right arm has rank three as well.

In particular, for two fixed integer rank budgets $P,Q$, infinitely many pairs with $r(x)\le P$ and $r(y)\le Q$ exist exactly when $P,Q\ge4$. The displayed logarithmic bounds give finiteness whenever one budget is at most three, and the rank-four family supplies the converse.

## An exact test on an entire family of stopping certificates

Fix the finite initial parity word of a certified lower arm up to its last odd step. Let its length be $\ell$, its odd count $p\ge1$ and its affine numerator offset $B$. The lower starts with this same initial word followed only by halvings have the form
$$
 x_N=(2^N-B)/3^p,\qquad y_N=2x_N-1=(2^{N+1}-C)/3^p,\qquad C=2B+3^p.
$$
Here $N$ is the total clock to 1. Consider the arbitrarily large admissible $N$ giving positive integers $x_N\equiv1\pmod{16}$. On a nonempty template of this kind integrality recurs periodically in $N$ since 2 is a unit modulo $3^p$, and the prescribed initial word and binary class hold thereafter as soon as enough low bits are fixed. The numerator $B$ is a ternary unit: in the offset sum only the summand for the last odd input survives modulo 3.

Apply the shortcut branches to the signed rational $-C/3^p$ using the parity of the numerator in lowest terms. Stop immediately after its $p$th odd input. This takes a computable finite number $L$ of steps and leaves an integer $z$. Indeed a nonzero rational has only finitely many consecutive halvings before an odd numerator, and while the denominator is divisible by three each odd step removes exactly one factor of three. The outcome $z$ decides the following alternative for **all sufficiently large admissible** $N$.

* If $z=0$, the upper arm reaches $2^{N+1-L}$ at clock $L$. Both starts reach 1 with exactly $p$ odd inputs, one clock apart, and two fixed finite words certify a lifted merger across the template. To obtain those words, extend the shorter power-of-two prefix by halvings until the clocks differ by one and the exponents agree.
* If $z\ne0$, none of these sufficiently large inputs admits a lifted merger at any clocks. In fact the upper arm already uses at least $p+(N+1-L-\log_2|z|)/2$ odd steps before any possible first arrival at 1. For negative $z$ the denominator 2 in this lower bound improves to $\log_2 3$.

In detail, put $h=N+1-L$. The initial $L$ parities of $y_N$ agree with those of the rational since their difference is divisible by $2^L$ in the rationals of odd denominator. Their endpoint difference equals $2^h$, so $T^L(y_N)=2^h+z$. The first $L$ actual states grow without bound with $N$, on fixed affine formulas. For $0\le i\le h$, if $s_i$ counts odd inputs of the integer trajectory from $z$, the exact lifted endpoint is
$$
 T^{L+i}(y_N)=2^{h-i}3^{s_i}+T^i(z).
$$
If $z>0$, each endpoint in this display is at least 2, while $1\le T^h(z)\le z4^{s_h}/2^h$ gives the lower bound. If $z<0$ the signed integer stays negative, with $1\le |T^i(z)|\le |z|3^{s_i}/2^i$. The displayed positive endpoint is then at least $(2^h-|z|)/|z|$, uniformly in $i$, proving both the sharper odd-count bound and absence of an early hit for large $N$. Once the number of odd inputs on the upper arm exceeds $2p$, the phase bound above excludes every lifted merger, even if the upper start eventually reaches 1. No assumption about convergence of signed orbits enters this test.
