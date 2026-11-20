# The time needed to merge a start with a power-of-three multiple

**PROPOSED, with a source-qualified upper bound.** Use the shortcut map $T(x)=x/2$ on even positive integers and $(3x+1)/2$ on odds. For $r,h\ge1$ let a start $n$ miss the deadline if $T^i(n)\ne T^j(3^rn)$ for **every** pair $0\le i,j\le h$.

In every complete block of $2^h$ positive starts lying above $6^h$, the fraction missing the deadline is between
$$
 c\min(1,r/\sqrt h)\quad\text{and}\quad C\min(1,r/\sqrt h)
 \tag{1}
$$
with absolute positive constants. For $r\gg\sqrt h$ the fraction *meeting* by the deadline is at most $2\exp(-r^2/(2h))$. The lower bound and the exponential obstruction are elementary. The upper estimate uses the uniform remaining-time lemma in David Leen’s October 2026 preprint. It applies to blocks at every height.

In particular, in **any** interval of $N\ge2$ consecutive positive parameters, the number for which $n$ and $3^rn$ never meet is at most
$$
 C' N\min(1,r/\sqrt{\log(2N)}).
 \tag{2}
$$
Take $h=\lfloor\log_2 N\rfloor$ and cover by at most two blocks of $2^h$ consecutive integers, allowing a partial block at the end and bounding it by a full block. Thus for every fixed $r$, permanent failures have zero upper Banach density. The case $r=1$ is the ray whose pointwise invariance is equivalent to full Collatz. Estimate (1) concerns finite deadlines and supplies no positive lower bound for permanent failures. [Pointwise equivalence](THREE_RAY.md)

## Reducing all clock choices to one finite pair process

On a length-$i$ parity word with $a$ odd inputs,
$$
 2^i T^i(n)=3^a n+B_i,\qquad 0\le B_i\le3^i-2^i.
$$
The offset bound follows by induction. An even step retains $B_i$, and an odd step gives $3B_i+2^i$. For a meeting of $n$ and $3^rn$ the two offsets therefore give
$$
 (2^j3^a-2^i3^{r+a'})n=2^i B'_j-2^j B_i.
$$
The absolute right side is less than $6^h$, uniformly in $r$. For $n>6^h$ the slope coefficient must vanish, which by unique factorization forces $i=j$ and $a=r+a'$. The offsets then match as well.

In the oriented pair process, the current entries are related by $Y=3^sX+D$ with $s\ge0$. The initial state for $(n,3^r n)$ is $(r,0)$. The level $s$ equals the absolute difference between the two exponents of three in their slopes with respect to the original variable. Absorption at $(0,0)$ gives a same-clock merger on its whole binary cylinder. Conversely the slope and offset calculation shows that **every** meeting before the deadline for $n>6^h$ gives absorption.

Here is the finite probability model. Given a history of the orientated base parities, the next base parity is fair on the two binary lifts. In fact write $X=2U+\epsilon$. After an unswapped step the new base is $U$ or $3U+2$, and after a swap it is $U+(D+1)/2$ in the odd-offset, odd-base swap case. The coefficient of $U$ is odd in every case. Thus each history of $h$ labels describes one residue modulo $2^h$, and every consecutive block of that length samples them all. [Full transition formulas and the binary-lift construction](PREFIX_COMPRESSION.md)

## Avoiding level zero

At positive level, an even offset leaves the level fixed. At an odd offset the two possible labels raise and lower the level by one with equal probabilities. These jump decisions are fresh fair signs because the parity of the offset is already determined *before* revealing the label. Equivalently generate the process with two independent fair bit streams. Use one for holding steps and the other whenever the level is about to jump, until first reaching zero. Extra bits of the jump stream exist whether or not another jump actually occurs. If the walk made of its first $h$ signs stays strictly above zero from $r$, then during the first $h$ shortcut steps the actual process cannot have reached zero.

For a simple fair walk $S_0=0$, the reflection principle gives
$$
 \Pr\!\left(\min_{0\le j\le h}(r+S_j)>0\right)
 =\Pr(1-r\le S_h\le r).
$$
The middle $O(\sqrt h)$ allowed locations each have probability comparable to $h^{-1/2}$ by the binomial formula and Stirling's bound, for instance throughout $|S_h|\le\sqrt h$. This proves the lower estimate in (1). Reflection and the binomial tail bound give the stated exponential upper estimate for the complementary hitting event. If $r>h$, reaching zero in $h$ steps is impossible.

For the upper bound on missing the deadline, use the lemma titled *Uniform remaining-time estimate* in Leen’s preprint. For its canonical process, $z=D/3^s$ and $0<\lambda\le1$, it states
$$
 \mathbb E_{(s,D)}[1-e^{-\lambda\tau}]
 \ll (1+s+|z|^\alpha)\sqrt\lambda
$$
for an absolute choice of $\alpha\in(0,1)$ and a uniform implied constant. This specific lemma permits arbitrary initial $s$, whereas the headline quantitative pair theorem is stated for $s=0$. At $(s,D)=(r,0)$ choose $\lambda=1/h$. On $\{\tau>h\}$ the integrand is at least $1-e^{-1}$, proving the claimed upper bound for every $r\ge1$. Absorption is sufficient at any height. [Leen, *Quantitative synchronization of Collatz trajectories*](https://doi.org/10.5281/zenodo.23268755)

## Explicit late mergers on the tripling ray

Fix $k\ge3$, odd $t\ge5$, and $n=2^kt-1$. For $0\le i\le k$ the first arm has
$$
 T^i(n)=3^i2^{k-i}t-1.
$$
The other arm starts at $3\cdot2^kt-3$ and then visits $9\cdot2^{k-1}t-4$ and $9\cdot2^{k-2}t-2$. From $3\le j\le k$ its value is $3^{j-1}2^{k-j}t-1$. These equations follow by checking the parities and using $T(x)+1=3(x+1)/2$ on odd inputs. The first three values cannot equal any first-arm value since such an equality would force $t$ to divide $2,3$ or $1$. For the remaining values equality would force $i=j$ by the powers of two in the coefficients of $t$ and would then fail by the powers of three. Thus these starts miss every pair of clocks through $k$, without any height cutoff.

Put $W=3^{k-1}t$. At time $k$ the two arms are $3W-1$ and $W-1$. If $W\equiv3\pmod4$, both halve to $3U+1$ and $U$, respectively, where $U=(W-1)/2$ is odd. Their next steps coincide. Exactly half the odd residue classes of $t$ modulo 4 satisfy this sufficient condition, for every $k$. Hence arbitrarily long delays occur for ordinary tripling pairs that are proved to meet just two steps after the displayed obstruction.

## When a whole binary class has a bounded merger time

Fix $r\ge1$ and a class modulo $2^h$ of the parameter $n$. There exists a finite $H$, possibly greater than $h$, by which **every** positive lift has some independent-clock meeting of $n$ and $3^r n$ if and only if the symbolic pair has already absorbed by step $h$. In that case two fixed equal-length prefixes work on the entire class.

For the converse suppose absorption has not occurred by $h$. At positive level, choose the next label to raise the level on any jump. A holding move leaves the level positive, so this prescription avoids zero for as many new bits as desired. At level zero with nonzero even offset $D$, choose an even base step repeatedly until the offset becomes odd, replacing it by $D/2$ each time. At an odd offset the two parities differ, so the next step has positive level after orienting the pair. In particular, at every depth $k\ge h$ the original class has an extension still unabsorbed at $k$. Choose an ordinary positive lift in that extension above $6^k$. Slope separation from the first section excludes every meeting through $k$, even with independently chosen clocks. This disproves every proposed uniform horizon on the original class. Thus allowing a different bounded witness for each lift does not enlarge the set of successful binary classes. The result leaves individual ordinary orbits with parameter-dependent meeting times open.
