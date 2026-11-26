# A power obstruction to uniform affine descent

Use the two-branch graph on $u=(x+1)/2$ from [the mixed-base theorem](MIXED_MAHLER.md). Its partial map $T$ has branches $A(u)=3u/2$ and $B(u)=(3u+1)/4$. A natural attempt to turn a large polynomial cycle indicator into a smaller one would rescale all physical vertices, rounding by a bounded correction while preserving edges.

**Proposition.** Let $F$ map sufficiently large nonnegative integers to nonnegative integers. Suppose $F(u)=\lambda u+o(u)$ with fixed $\lambda>0$, and $F$ sends each legal edge with sufficiently large endpoints to a legal edge in the same graph. If $\lambda\ne1$, then for all sufficiently large $X$,
$$
 \max_{u_0\le u\le X}|F(u)-\lambda u|
 \gg_\lambda X^\gamma,\qquad
 \gamma=(2-\log_2 3)\frac{\log(3/2)}{\log 3}>0.
$$
Here $u_0$ may be any fixed point above which $F$ is defined. The proposition tests a universal graph map. A map defined only on a particular cycle need not send the words used below to legal edges.

At large $u$, the image of a legal edge has the same letter, since $F(Tu)/F(u)=Tu/u+o(1)$ and the two possible limiting ratios $3/2$ and $3/4$ differ. Choose $m\to\infty$, $H=\lfloor m\log_2 3\rfloor$, $b=H-m$, $a=2m-H$. The word $B^b A^a$ has slope $\rho=3^m/2^H\in[1,2)$ and additive constant
$$
 c=(3/2)^a[1-(3/4)^b].
$$
It occurs at an ordinary integer $u\in[2^H,2^{H+1})$. Indeed its unique admissible residue modulo $2^H$ is obtained by solving the integral endpoint congruence, since $3^m$ is odd. Integrality of the endpoint forces the prefix branch congruences successively by reduction modulo the corresponding powers of two. During the $B$ run the values decrease to at least $(3/4)^b2^H$, which tends to infinity, and then increase to $v=\rho u+c\ll 3^m$. Image letters are therefore the same throughout the word for all large $m$. With $D(w)=F(w)-\lambda w$ this gives
$$
 D(v)-\rho D(u)=(1-\lambda)c .
$$
One of the two errors has absolute value at least $|1-\lambda|c/(1+\rho)$. Since $a\ge(2-\log_2 3)m$, this is $\gg_\lambda (3^m)^\gamma$. The maximum physical vertex is bounded by an absolute constant times $3^m$. Choosing the greatest $m$ permitted by that bound proves the all-$X$ claim. [Exact ordinary controls](../../../reports/astra-unconventional-20261126/arithmetic/SECTIONS.json)

## A cycle-dependent inverse selector

For an actual odd backward edge $x'=(2^e x-1)/3$ and an alternative $y'=(2^f y-1)/3$, write $y=2^d x+c$. Then
$$
 d'=d+f-e,\qquad 3c'=2^{d'}+2^f c-1,\qquad y'=2^{d'}x'+c'.
$$
At each step the actual exponent $e$ supplies $x\bmod3=2^{-e}\bmod3$. The alternative can continue exactly when $2^f y\equiv1\pmod3$; then $f\ge1$ ensures the new point is an odd integer. This allows alternative exponents greater than two. On an actual large bounded branch all offsets below are negligible compared with the positive reference.

One concrete certificate starts at $(d,4c)=(0,0)$. The reference backward word for the nineteen paired steps is
$$
 (1,2,2,2,2,2,2,2,2,1,1,2,1,2,1,2,1,2,1).
$$
The alternative exponents in the same order are
$$
 (3,3,2,1,1,4,2,2,1,1,1,1,1,1,1,1,1,1,1).
$$
The successive pairs $(d,4c)$ are
$$
 (2,4),(3,20),(3,36),(2,28),(1,20),(3,116),(3,164),(3,228),(2,156),
 (2,108),(2,76),(1,52),(1,36),(0,24),(0,16),(-1,10),(-1,6),(-2,3),(-2,1).
$$
If the next reference exponent is 1, the last reference state is $2\bmod3$ and the alternative $y=(x+1)/4$ is divisible by three. It is a positive odd backward seed with the indicated forward route to the initial phase. The size test relative to a specific least-disagreement certificate remains a separate hypothesis. This certificate controls one finite selector, and does not prove an entropy bound strong enough to settle the bounded branch.
