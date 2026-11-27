# The extra odd steps paid at the positive anchor 589

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers. On an orbit of $U$, odd rank counts departures. The physical division clock counts all the shortcut steps, including even steps. For $R\ge1$ define
\[
 D_R=\min_{U^R(w)=589}\sum_{i=0}^{R-1}v_2(3U^i(w)+1),
 \qquad \beta_R=2^{D_R}/3^R.
\]
Every positive ternary unit has an inverse odd step to another ternary unit with division exponent at most four. Indeed try $1,3$ for a unit congruent to two modulo three, and $2,4$ for a unit congruent to one. Both choices give an integer and at most one gives a multiple of three. Thus $D_R\le4R$, its minimum is attained, and enumerating all compositions of total at most $4R$ computes it. The projection and construction below use the actual minimizing word.

For a positive delayed index $k$, set $m=12\cdot2^{18k}-1$, $X=2^m-1$, $81z=128\cdot2^m-271$. For $R\ge6$ restrict to indices of **exact** ternary depth $v_3(2^m-590)=R$. Let $L_R$ be the minimum of $q-R$ over this shell and all ordinary positive $W\equiv17\bmod48$ with $2^{40}W<z$ and $U^q(W)=X$.

**Proposed quantitative theorem.** Each such minimum exists, and
\[
 \log_{3/2}(2^{38}\beta_R)\ \le\ L_R\
 \le\ \left\lceil\log_{3/2}(2^{44}\beta_R)\right\rceil+2.
\]
The lower bound also holds without the canonical residue condition. For each fixed $R$, an explicit nonempty residue class of positive delayed $k$ attains the stated upper bound on the cost. The theorem optimizes across the exact shell. It supplies a direct subfloor predecessor of the genuine $M_m$ at every selected $k$.

## Lower bound at every member of the shell

For any positive odd anchor $a$, the displacement between two terminals lifts through a common inverse exponent $e$ by the factor $2^e/3$. In particular, if $X-a$ is an even multiple of $3^R$, then every actual $j\le R$ word to $X$ projects to a positive odd start $w$ reaching $a$ with that same word, and
\[
 y=w+\frac{2^d}{3^j}(X-a),\qquad w\le\frac{ay}{X}.
\]
Here $d$ is the physical clock. Positivity holds inductively in reverse because $(2^e v-1)/3$ is positive whenever the numerator is divisible by three and $v$ is positive odd. The inequality follows from $3^j w\le2^d a$ and the displayed identity. This is PR200's positive projection theorem. [Prior positive projection](https://github.com/GettysburgResearch/collatz/blob/bf7d52e78631954a9fd35e4ce973acd27738fc80/research/six-hour-20261127/pointwise/ADAPTIVE_POSITIVE_ANCHORS.md)

Take $a=589$. Since $z<2X$ and $X>2^{80}$ on the delayed family, a positive $W$ with $2^{40}W<z$ cannot reach $X$ in $q\le R$. Its projected positive integer would be at most $589W/X<1$. For a longer word write $q=R+L$ and $u=U^L(W)$. Applying projection to the final $R$ departures gives $u\ge\beta_R(X-589)$. Each ordinary odd step satisfies $U(x)+1\le(3/2)(x+1)$, hence
\[
 \beta_R(3X/4)\le u+1\le(3/2)^L(W+1)
 \le(3/2)^L(3X/2^{40}).
\]
This proves the claimed lower bound at every supplied $k$ of depth $R$. The argument imposes no bound on any individual division exponent.

## Constructing an ordinary source at each prescribed shell depth

Fix a word from $w$ attaining $D_R$. If $3$ divides $w+1$, replace $w$ by $w'=4w+1$. Otherwise use $w'=w$. The replacement increases the first full division exponent by two and leaves the remaining path identical. Thus $3\nmid w'+1$, the adjusted rank is still $R$, and its multiplier $\beta'=2^{d'}/3^R$ satisfies $\beta'\le4\beta_R$. Also $w'\le589\beta'$.

Take the smallest positive $p$ satisfying $(3/2)^p\ge2^{44}\beta_R$. Since $\beta_R\ge1/589$, it is exactly the ceiling in the theorem. Write $2^m=590+3^R Q$. Prescribe $Q\bmod3^{p+3}$ by
\[
 w'+2^{d'}Q+1\equiv 3^p\cdot 11\cdot(2^p)^{-1}\pmod{3^{p+3}},
\]
where the inverse in the product may be taken modulo $27$. This has exactly one solution class and its members are units modulo three. It therefore enforces the **exact** shell. The map $j\mapsto 2^{11+162j}$ covers the entire ball $2^{11}\bmod3^5$ with one $j\bmod3^b$ per target modulo $3^{5+b}$. This follows from $v_3(2^{162h}-1)=5+v_3(h)$. Since $590\equiv2^{11}\bmod3^5$, our chosen class is realized by one exponent class $j\bmod3^{R+p-2}$. The map $k\mapsto j=2(2^{18k}-1)/27$ permutes every quotient modulo a power of three, again by LTE. This gives an explicit positive-density class of actual delayed $k$. Each resulting $Q$ is even and positive.

At any such index define
\[
 Y=w'+2^{d'}Q,\qquad c=(Y+1)/3^p,\qquad V=2^p c-1,\qquad W=(16V-7)/9.
\]
Lifting the adjusted positive word gives $U^R(Y)=X$. The integer $c$ is positive and even. Therefore $V$ reaches $Y$ by $p$ actual exponent-one steps. The prescribed digit gives $V\equiv10\bmod27$. Writing $V=27n+10$, the positive source $W=48n+17$ reaches $V$ by two odd departures with division exponents $(2,2)$, since $V$ is odd. Positivity also follows directly from $p\ge1$, $c\ge2$, and the congruence for $V$. This proves $U^{R+p+2}(W)=X$.

Finally $Y=w'+\beta'(X-589)\le\beta'X$ and $\beta'X\ge1$. The exact source therefore satisfies
\[
 W<2(2/3)^p(Y+1)\le4(2/3)^p\beta'X\le X/2^{40}<z/2^{40}.
\]
In particular the subfloor implication at the original least parent proves goodness for these inputs without any use of the canonical implication. The physical clock actually paid is $d'+p+4$, and $R+p+2$ is its odd rank.

## Consequences for rank growth

The orbit of $589$ first hits one in 42 odd steps and cannot visit $589$ again. For any $B>0$, each $R$ with $\beta_R\le B$ has its own positive odd $w\le589B$. Different ranks cannot use the same $w$. Hence at most $\lfloor(589B+1)/2\rfloor$ ranks qualify. In particular $\beta_R\to\infty$ and the optimum extra rank tends to infinity. For each $\epsilon>0$ the exceptional $R\le H$ with $\beta_R\le R^{1-\epsilon}$ number $O(H^{1-\epsilon})$. The theorem thus forces at least $(1-\epsilon)\log_{3/2}R+O(1)$ extra departures for a density-one set of shell depths, even after choosing the most favorable $k$ in each shell.

One can also express the answer by $w_R=\min\{w: U^R(w)=589\}$. Always $w_R/589\le\beta_R$. The earlier uniform reciprocal bound on a finite simple ordinary segment gives $\beta_R\le e^{200/3}w_R/589$ by evaluating the multiplier on $w_R$. Its segment is simple because $589$ never returns to itself. This yields $L_R=\log_{3/2} w_R+O(1)$. Only this alternate formulation uses the prior reciprocal estimate. If $L_R=o(R)$ on a sequence, the corresponding ordinary $w_R$ reach 589 after $R$ odd steps with $\log w_R=o(R)$. Their first-hit times at one grow superlogarithmically on the sequence. This specializes a stopping-time transfer to the original hard Mersenne shells. [Earlier simple-path estimate, T-A3-651](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/astra-three-routes/pass3/FINITE_RECORDS.md) · [PR200 reflected-family stopping-time transfer](https://github.com/GettysburgResearch/collatz/blob/bf7d52e78631954a9fd35e4ce973acd27738fc80/research/six-hour-20261127/pointwise/STOPPING_TIME_TRANSFER.md)

## Boundary and controls

The earlier classification at 590 covers undirected finite words. PR192 obtains quantitative lower bounds on all numerical undirected cut walks under its different first-hit and height controls. The result here concerns directed positive ancestors of a prescribed original Mersenne. It gives matched upper and lower bounds in odd rank, including a constructive ordinary class on each exact ternary shell. Obtaining any successful route at an arbitrary supplied index remains open. [PR192 cut-walk theorem](https://github.com/GettysburgResearch/collatz/blob/75eac0cbc744469ae2886bc2f140685c484e9fe7/research/astra-sixhour-20261127/descent/CUT_WALK_DEPTH.md) · [Prior 590 fixed-word calculation](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/renormalization/FINITE_COVER_BARRIER.md)

[AnchorRoute.lean](AnchorRoute.lean) verifies physical realization of the odd-word relation, its multiplier inequality, the positive projection and lift, the first-exponent adjustment, route concatenation, and the two canonical prefix pieces. The optimization, LTE addresses and asymptotic deductions are written proofs. [The checker](check_anchor_overhead.py) certifies $D_R$ at nine depths by ordinary source enumeration and a multiplier bound that excludes every unseen source. It reconstructs the corresponding $j,k$ classes and iterates complete positive chart representatives with all individual division exponents. The finite chart controls use ordinary $N=590+3^RQ$. The guaranteed delayed members exist by the displayed isometries. [Archived controls](ANCHOR_OVERHEAD_CONTROLS.json)
