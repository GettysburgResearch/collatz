# Why a global ordering of fresh Pell primes needs an all-time input

**PROPOSED finite obstruction.** For every $N\ge1$ and every modulus $m\ge1$, infinitely many positive integer starts give $N$ consecutive odd Syracuse steps for which (i) the $N+1$ states are strictly increasing, squarefree units at six, all congruent to $-1\pmod m$, and (ii) every edge is the **fundamental** solution of a different Pell equation in the [rank proof](README.md). There is no higher Pell index anywhere on these segments from which to extract a new prime.

Choose an integer $P>2(N+1)+2$, let $Q$ be the product of the primes up to $P$, and set
\[
    x_i(t)=3^i2^{N+1-i}(6mQ)t-1\qquad (0\le i\le N,\ t\ge1).
\]
These are positive increasing odd integers. They equal $-1$ modulo $6m$, and $3x_i+1=2x_{i+1}$ for $i<N$. Thus these are literal consecutive odd steps with stripping exponent one. Write $c_i$ for the positive coefficient of $t$. A prime dividing $c_i$ cannot divide $x_i(t)$, which handles every prime up to $P$. For any other prime $q>P$, at most $T/q^2+1$ parameters $1\le t\le T$ have $q^2\mid x_i(t)$, since that condition fixes one residue modulo $q^2$. Only $q\le\sqrt{c_iT}$ can occur. Bounding the sum of $1/q^2$ by the sum over all integers above $P$, and the number of relevant primes by $\sqrt{c_iT}$, the union of all bad parameters has size at most
\[
        (N+1)T/P + \sqrt T\sum_{i=0}^N\sqrt{c_i}.
\]
The remaining parameters have positive lower density for these fixed $N,m,P$. Coprimality of successive odd states now makes $6x_i x_{i+1}$ squarefree. Equation (2) of the rank proof gives $D_i=6x_i x_{i+1}$ and $V_i=2$. The discriminants strictly increase. If $u+v\sqrt D$ is the fundamental unit in integer coordinates, the second solution has coefficient $2uv\ge4$, and subsequent coefficients are larger. Thus every displayed edge has Pell index one. The first and last states agree modulo the full chosen $m$. They are distinct positive ordinary integers.

**What is shared on a real lap.** Write a positive odd state that is a unit at three as $x_i=s_i b_i^2$ with $s_i$ squarefree. Coprimality of neighboring states and $2^{a_i}x_{i+1}=3x_i+1$ give the exact formulas
\[
  D_i=3\,2^{a_i\bmod2}s_i s_{i+1},\qquad
  V_i=2^{1+\lfloor a_i/2\rfloor} b_i b_{i+1}.
\]
For an odd prime dividing $V_i$ on a cycle, exactly one of $b_i,b_{i+1}$ contains that prime. The other edge at that vertex has exactly the same valuation in its Pell coefficient, by neighboring coprimality again. A prime first appearing in the Lucas sequence of one discriminant is therefore not automatically new in the full list of Pell coefficients. On a closed lap the squareclass product $[\prod_iD_i]=[3^p2^{\sum_i a_i}]$ follows immediately for $p$ odd steps, since the vertex factors occur twice. This identity allows many different discriminants.

Neither distinct discriminants on all edges nor fundamental index throughout has been ruled out on a positive integer counterexample. The construction concerns changing starts as $N,m$ vary and does not exhibit an infinite trajectory with these properties. A proof using a global prime order would have to force higher indices or suitably restricted discriminants on the same fixed escaping orbit or on the entire exact primitive return, and would have to account for the duplication of prime valuations at adjacent edges.
