# Counting disjoint first-hit patterns near the minimum possible clock

**PROPOSED written theorem.** Let $F$ be a fixed finite set of nonnegative offsets containing zero, fix a relative width $\delta>0$, and fix the source congruence data of a [relative-window placement theorem](FAST_FIRST_HIT_PAIRS.md). For pairs, one can take $F=\{0,d\}$ and any prescribed ternary source class. The [Lean-checked finite-profile extension](FastBlocks.lean) gives arbitrary fixed finite $F$ and prescribed mixed binary and ternary residues. Write
$$
                      L=\log_2(X/y),\qquad a=\log_2 3.
$$
All targets $y$ below are positive and prime to three. All logarithms in this note are base two. A pattern is an actual translate $x+F$ entirely inside $[X,(1+\delta)X]$. Its members have the same first-hit time to $y$ and the same number of odd departures before that hit.

1. For every fixed integer $l\ge1$ and all sufficiently large $X/y$, there are $\gg_l L^l$ pairwise disjoint patterns with one shared first-hit clock at most $L+al+K$ and one shared grade. The constant $K$ is independent of $l,X,y$ and the supplied ternary source class. The implicit constant and the onset may depend on $l$ and the fixed placement data.
2. Let $N_\eta(X,y)$ count a largest disjoint collection with one shared first clock $D\le(1+\eta)L$ and one shared grade, with the fixed pattern and source congruences above. For small $\eta>0$ and $L\to\infty$, its lower and upper exponential rates per unit $L$ have the same two leading terms as $\eta\downarrow0$. With $\rho=\eta/a$, they are
$$
             \rho\log_2(1/\rho)+\rho\log_2(e/3)+O(\rho^2).
$$
More precisely, the liminf and limsup of $L^{-1}\log_2 N_\eta$ lie between two quantities with this expansion, uniformly over $y$ and the permitted ternary source class. The limit in $L$ need not exist.
3. With a fixed additive time allowance $K'\ge0$, even the number of *all single starts* in the window visiting $y$ by $L+K'$ is $O_{K'}((1+L)^{\lfloor K'/a\rfloor})$. Thus each added odd-depth layer in part 1 has the asymptotically optimal additive cost per new power of $L$.

All constants giving a baseline placement are taken uniformly over the target. The counting argument uses no predecessor-density input or independence assumption.

## Branch choices and disjointness

For a current ternary unit $b$, and an integer $e\ge3$ with $2^e b\equiv4$ or $7\pmod9$, set $b'=(2^e b-1)/3$. This is an odd ternary unit reaching $b$ after exactly $e$ shortcut steps with one odd departure. The six powers of two modulo nine traverse every unit once. Exactly two exponents in each complete set of six produce an allowed child. With $3\le e\le M$, each vertex therefore offers at least
$$q_M=2\left\lfloor(M-2)/6\right\rfloor$$
children.

At the target, discard any child on the forward orbit of $y$. There is at most one. If $e<f$ and both children $z_e,z_f$ were on that orbit, then $T^{f-e}z_f=2^e y=3z_e+1$. Both $z_e$ and $3z_e+1$ would belong to the cycle of $y$ and reach $y$ in exactly $e$ steps. Injectivity on the cycle contradicts their distinctness. If $y$ is not periodic, no child can be on its forward orbit.

Choose $l$ inverse exponents as above and write $b_0=y,b_1,\ldots,b_l=b$, $S=e_1+\cdots+e_l$. No $b_i$ with $i\ge1$ lies on the forward orbit of $y$, since every $b_i$ reaches $b_1$. The backward odd vertices grow by at least a factor two per step. All intervening even vertices on the direct leg to $b_{i-1}$ are positive multiples $2^j b_{i-1}$ with $j\ge1$. The whole direct leg from $b$ therefore visits $y$ for the first time at $S$.

Each accepted exponent vector labels a separate terminal branch. In any ordinary trajectory first reaching $y$, the $l$-th preceding *odd departure* is unique whenever there are at least $l$ of them. If the start first visits $b$ and follows its displayed leg, exactly $l$ odd departures remain and the first is at $b$. There was no earlier $y$ since otherwise $y$ would reach $b$. Hence this last-odd-departure rule recovers $b$ from each individual member of a placed pattern. The intervening clocks to the next odd vertex, and the final clock to $y$, recover the entire exponent vector. This reasoning also works for even $y$, where the final even run stops at that specified target. Distinct exponent vectors cannot share any ordinary member across their placed patterns.

There are at least $(q_M-1)q_M^{l-1}$ accepted vectors for $q_M\ge2$. Their exact affine products give
$$
\frac{3^l b}{2^S y}=\prod_{i=1}^l\left(1-\frac1{2^{e_i}b_{i-1}}\right)
\ge 1-\sum_{i=1}^l\frac1{8\cdot2^{i-1}y}\ge\frac34 .
$$
In particular $b\le2^S y\le2^{lM}y$ and
$$ S\le\log_2(b/y)+al+\log_2(4/3). $$

## Using the same physical window for every vector

Choose baseline constants $C_0\ge1,K_0,G_0$ so the placement theorem supplies a pattern at every unit $b$ in $[X,(1+\delta)X]$ for $X\ge C_0 b$, with common first clock at most $\log_2(X/b)+K_0$ and common odd count at most $G_0$. If $C_0 2^{lM}y\le X$, apply this theorem in the **same** physical interval at every accepted $b$. Its concatenation with the direct leg yields a first clock at most
$$
               L+al+K,\qquad K=K_0+\log_2(4/3),
$$
and grade between $l$ and $l+G_0$. Every first clock is at least $L$ because $x\ge X$ and $T(n)\ge n/2$. Thus at most $(G_0+1)(\lceil al+K\rceil+1)$ clock/grade pairs occur. Some one pair accounts for at least the inverse of this factor times the total disjoint count.

For fixed $l$, take $M=\lfloor(L-\log_2 C_0)/l\rfloor$. The branch lower bound then gives part 1.

For fixed small $\eta>0$, choose $M=\lceil a/\eta\rceil+1$ and $l=\lfloor(L-\log_2 C_0)/M\rfloor$. For all sufficiently large $L$ we have $l\ge1$, $q_M\ge2$ and $al+K\le\eta L$, since $a/M<\eta$. Pigeonholing the clocks costs only a factor $O(L)$. We get
$$
\liminf_{L\to\infty}\frac{\log_2 N_\eta(X,y)}{L}
\ \ge\ \frac{\log_2 q_M}{M}
\ =\ \frac{\eta}{a}\log_2(1/\eta)+O(\eta).
$$
The displayed liminf is uniform in the targets and permitted source classes. A variable allocation of the exponent budget gives the sharper second term below.

## The ordinary parity-word upper bound

Every start $x\ge X$ reaching $y$ after $D$ clocks and $g$ odd departures satisfies $3^g x\le2^D y$. Hence $g\le(D-L)/a$. At a fixed $(D,g)$, the at most $\binom Dg$ parity words determine at most that many starts, since the affine identity $2^D y=3^g x+B$ gives a unique $x$ from its word and endpoint.

For a fixed additive allowance $K'$, there are at most $\lfloor K'\rfloor+1$ possible integer clocks in $[L,L+K']$ and $g\le\lfloor K'/a\rfloor$. Summing the word bound proves part 3. In a fixed dyadic octave the reciprocal sum of such starts is consequently $O_{K'}((1+L)^{\lfloor K'/a\rfloor}/X)$. A fixed-overhead rule gives finite total reciprocal mass when summed over octaves at a fixed target.

## Counting the permissible inverse exponents

Each inner reverse odd step must produce a ternary unit, since its odd child has another odd ancestor. The outermost odd vertex can be divisible by three. This distinguishes the true small-grade inverse count from a count of unrestricted parity words. Write $\rho=\eta/a$ and take $\eta$ sufficiently small that $1+(a-8)\rho>0$.

For the lower estimate, take $l=\lfloor(\eta L-K)/a\rfloor$. At the first inverse step choose a single unit child outside the target's future with exponent in $[3,8]$. There are two eligible exponents and at most one excluded child. At every remaining step choose
$$
              e_i=6k_i+r_i,\qquad k_i\ge0,
$$
where $r_i$ is either of the two admissible residues selected from $[3,8]$ at the current state. The chosen residue numbers can depend on that state. For each fixed nonnegative vector of quotients there are exactly $2^{l-1}$ choices of the binary residue indices, and the resulting exponent vectors are all distinct. Require
$$
\sum_{i=2}^l k_i\le A=\left\lfloor\frac{L+al-8l-\log_2 C_0}{6}\right\rfloor .
$$
Then $S\le L+al-\log_2 C_0$ and $b\le 2^S y/3^l\le X/C_0$. Every chosen branch therefore supports a pattern in the same window with first clock at most $L+al+K\le(1+\eta)L$. The number of exponent vectors is
$$
                     2^{l-1}\binom{A+l-1}{l-1}.
$$
Pass to globally common clock and grade as before, losing only a polynomial factor in $L$.

For the upper estimate, fix a clock $D$ and grade $g\ge1$ to $y$. From the target backwards, locate the $g$ odd departure states. Between consecutive odd states there is a positive gap $e_i$; the gap nearest $y$ ends at that specified target even when $y$ itself is even. Any initial string of halving steps at the source has length $D-\sum e_i$, which is determined. For each $i$ write $e_i=6k_i+r_i$ with $k_i\ge0$ and $1\le r_i\le6$. For all but the outermost odd gap the residue $r_i$ has at most two choices at the current state. For the last gap it has at most three choices, since integrality alone requires $2^{e_i}b\equiv1\bmod3$. The resulting bound is
$$
\#\{x:T^D x=y,\ O_D(x)=g\}\le 3\cdot2^{g-1}\binom{\lfloor D/6\rfloor+g}{g}.
$$
At $g=0$ there is at most one start. Since $g\le\rho L$ and $D\le(1+\eta)L$, the right side increases when either upper parameter increases. It also bounds the maximum over any disjoint collection of patterns having a shared clock and grade. Summing all clocks and grades would only add a polynomial factor in $L$.

To compare the exponents, define, with base-two logarithms,
$$
H(b,t)=(b+t)\log_2(b+t)-b\log_2 b-t\log_2 t.
$$
Stirling's formula and $l/L\to\rho$ yield the uniform squeeze
$$
\rho+H\!\left(\frac{1+(a-8)\rho}{6},\rho\right)
\ \le\ \liminf\frac{\log_2 N_\eta}{L}
\ \le\ \limsup\frac{\log_2 N_\eta}{L}
\ \le\ \rho+H\!\left(\frac{1+a\rho}{6},\rho\right).
$$
For either first argument $b=1/6+O(\rho)$, Taylor expansion gives $H(b,\rho)=\rho\log_2(1/\rho)+\rho\log_2(e/6)+O(\rho^2)$, where $e$ is Euler's number. The linear term $+\rho$ from the two allowable residues therefore gives $\rho\log_2(e/3)$ on both sides. These estimates count actual first-visiting patterns in every fixed-width relative window. They leave the supplied-source descent problem open.
