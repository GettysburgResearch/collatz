# The incoming and outgoing prime parts and their common divisor

Use the actual consecutive ramps, $N=3^{s+h}\beta$, $v=2^{v_2(N-1)}$, $W=x'+1$ and $R=vW=N+v-1$ from [Uncancelled prime factors](REDUCED_CORE_TRANSPORT.md). Fix any finite $S$ containing 2 and 3. Put $B=\beta_{S^c}$, $B'=\beta'_{S^c}$ and $G=\gcd(B,B')$. Then for every $\epsilon>0$,
$$
                 BB'\gg_{S,\epsilon}N^{1-\epsilon},\qquad
                 G\ll_{S,\epsilon}N^\epsilon\sqrt B .                 \tag{1}
$$
Both bounds are simultaneous at each supplied ordinary $x$. The first shows that at least one core contains outside-$S$ factors of combined size $\gg_{S,\epsilon}N^{1/2-\epsilon}$. The second bounds how much of the incoming core survives into the outgoing core. The exponent $1/2$ in that retention bound is attained asymptotically by an explicit family.

### The three-variable product and its exceptional planes

Apply the rational $S$-adic subspace theorem to $(N,v,1)$. Use $(X,Y,Z)$ at infinity. At every prime in $S$ use $(X,Y,X+Y-Z)$, whose determinant is $-1$. Every evaluated factor is positive as a rational number. The maximum norm is $N$, since $2\le v\le N-1$. The product of the normalized absolute values is
$$
    \frac{Nv}{N_S\,v\,R_S}=\frac{N}{N_S R_S}=rac{BB'}{R},
$$
where $M_S=M/M_{S^c}$ and $R_{S^c}=W_{S^c}=B'$. The product is at least $N^{-\epsilon}$ off a finite union of proper rational subspaces. Thus $BB'\ge R N^{-\epsilon}>N^{1-\epsilon}$ off that union. The exceptional subspaces here can contain infinitely many primitive vectors, so the following argument is needed. [Varjú, *Times 2, 3 mod Q*, Theorem 5](https://publications.hse.ru/pubs/share/direct/809451625.pdf)

Enlarge each exceptional subspace to a rational plane $aX+bY+cZ=0$ with fixed coefficients not all zero. If $a=0$, necessarily $b\ne0$ for the plane to contain any $(N,v,1)$, and then $v=-c/b$ is fixed. The two-dimensional bound $W\ll_{S,\epsilon}N^\epsilon UV$ from the earlier theorem, with $U=B'/G$, $V=B/G$, yields $BB'\ge UV\gg_{S,\epsilon}N^{-\epsilon}W\gg_v N^{1-\epsilon}$. If $a\ne0$ then $N/v=-b/a-c/(av)$ is bounded above by a plane-dependent constant on positive solutions, even as $v$ varies. Thus $v\gg_{a,b,c}N$. The other two-dimensional bound $v\ll_{S,\epsilon} N^\epsilon B$ gives $BB'\ge B\gg_{S,\epsilon,a,b,c}N^{1-\epsilon}$. Replace the finitely many constants by their minimum. Its dependence is on $S,\epsilon$ and it is ineffective. This proves the first estimate in (1).

The same two-dimensional proof gave $B\ll_{S,\delta} N^\delta V^2$. As $B=GV$, this says $G\ll_{S,\delta} N^{\delta/2}\sqrt B$. Taking $\delta=2\epsilon$ proves the second bound.

### Sharp retention and a directional control

For any $m\ge0$ take $f=6m+2$, $v=2^f$ and $N=(v-1)(2v-1)$. Then $N\equiv3\pmod9$, so $x=2N/3-1$ is odd and $x+1=2(N/3)$ with $(N/3,6)=1$. Its first shortcut lands on $N-1=v(2v-3)$. Its next odd state is $x'=2v-3$, with $\beta'=(v-1)/3$. For $S=\{2,3\}$ we have $G=(v-1)/3$ and $B=(v-1)(2v-1)/3$. For any larger fixed $S$, each extra fixed odd prime $p$ has $v_p(2^r-1)=O_p(1+\log r)$, by using the order of 2 at $p$ and lifting the exponent when the order divides $r$. Apply this at $r=f,f+1$. It follows that $\log G/\log B\to1/2$ for every fixed $S$. In this family $U=B'/G=1$ throughout.

There is also an infinite family returning directly to 5. Take the same $f,v$ and put $N=5v+1$, again of ternary valuation one. Then $x=2N/3-1$ has next odd state 5, hence $U=1$. Conversely an ordinary Mersenne start $2^s-1$ has $\beta=1$ and therefore $V=1$. These physical trajectories realize both directions of the individual bound in the earlier note.

### The proportion of outgoing height outside a fixed prime pool

On any fixed escaping trajectory $N_i\to\infty$ along its successive crests. Summing the first inequality in (1) gives
$$
  2\sum_{i<k}\log\beta_{i+1,S^c} \ge
       (1-\epsilon)\sum_{i<k}\log N_i-O_{S,\epsilon}(k)-\log\beta_{0,S^c}.
$$
Consequently the lower limit of the ratio of the outgoing sum to the $\log N_i$ sum is at least $1/2$. This includes prime powers retained from the incoming state; the separate $1/4$ lower limit in the earlier note counts only the uncancelled increase of valuations. Both statements sample the physical crests with the displayed height weights.
