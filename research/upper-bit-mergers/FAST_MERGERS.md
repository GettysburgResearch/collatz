# Positive families that merge in one further step

Use the shortcut map and the merger cost $M_h(r)$ from the [main proof](README.md). Both families below are exact. The common endpoint need not have any known path to 1 for the merger to hold.

## A universal minimum

For every odd $1\le r<2^h$, the endpoints after $h$ steps cannot merge with zero further even steps on both paths, even at different clocks. Write these endpoints as $x,x+g$, $g=3^s$, with $s\ge1$. They have opposite parity. If $x$ is even, it must stand still while an upper path using only odd steps can only increase. Otherwise $x+g$ must stand still; reaching it from $x$ after $a\ge1$ odd steps requires

$$
(3^a-2^a)(x+1)=2^a 3^s.
$$

The positive factor $3^a-2^a$ is relatively prime to six, so it equals 1. This forces $a=1$ and $x=2g-1$. Yet the prefix bound in the main proof gives $x/g<1+2^{-s}\le3/2$, and $2-1/g\ge5/3$. Thus $M_h(r)\ge1$ whenever the endpoints merge.

## A prescribed number of odd steps

For every even $h\ge2$ and every odd $s$ with $1\le s<h$, there is an odd $r<2^h$ with $s_h(r)=s$ and $M_h(r)=1$. Put $e=h-s-1$, an even nonnegative integer, and take

$$
r=2^{h-1}-(2^{e+1}+1)/3.
$$

The division is exact and $r$ is positive and odd. Its first step produces $2^e(3\cdot2^{s-1}-1)$. Take $e$ even steps, then $s-1$ odd steps. Each of these odd steps replaces $x+1$ by $3(x+1)/2$, so the result is $3^s-1$. One last even step completes exactly $h$ steps. The endpoints for $r$ and $r+2^h$ are therefore $x=(3^s-1)/2$ and $x+3^s=3x+1$. Since $s$ is odd, $3^s\equiv3\pmod8$, so $x\equiv1\pmod4$ and $T(x)=(3x+1)/2$ is even. The upper endpoint halves straight to $T(x)$. The paths meet in one step. With zero even steps the upper path can visit only its starting point, and the lower path can visit only $x$ and $T(x)$, both smaller. Thus the minimum cost is exactly one.

For $h=6$ and $s=3$, the formula gives $r=29$. The starts 29 and 93 reach 13 and 40 after six steps. Both then reach 20. The construction permits $s$ within one of $h/2$ at every even depth.

## Which pairs meet after exactly one step on each path?

Define the auxiliary map $S(z)=z/2$ for even positive $z$ and $S(z)=(3z-1)/2$ for odd positive $z$. For $h\ge2$ the two post-prefix endpoints meet on their next step if and only if $p=2^{h-1}-r$ is positive, $S^{h-1}(p)=1$, and the first $h-1$ steps from $p$ under $S$ have odd total odd-step count.

Indeed, simultaneous equality is possible only when $x$ is odd and the upper endpoint is even. It then reads $3x+1=x+g$, giving $x=(g-1)/2$ and $s$ odd. The prefix inequality $r/2^h\le x/g<1/2$ gives $p>0$. The last step into $x$ had to be even: an odd input $u$ would give $3u=g-2$, impossible modulo three. Thus $T^{h-1}(r)=g-1$, with $s$ odd steps at that earlier depth as well.

Writing $s_i$ for the number of odd $S$-steps among the first $i$ steps from $p$, we have

$$
T^i(r)+S^i(p)=2^{h-1-i}3^{s_i},\qquad 0\le i\le h-1.
$$

At time zero this is $r+p=2^{h-1}$. Before time $h-1$ the sum is even, so both inputs have the same parity. Two even steps halve the sum, and for two odd steps the $+1$ and $-1$ cancel, multiplying the sum by $3/2$. This proves the identity and equality of the parity counts. At $h-1$ it gives $S^{h-1}(p)=1$. Conversely, that endpoint and an odd count $s$ give $T^{h-1}(r)=3^s-1$, and the next steps give the merger above. The characterization concerns equal one-step clocks. The universal minimum also permits unequal clocks.

## Exponentially many distinct pairs at every large depth

For every $h\ge13$, the number of odd $r<2^h$ with $M_h(r)=1$ is at least $2^{\lfloor(h-1)/6\rfloor-1}$.

The fixed point 1 of $S$ supplies finite words that give actual mergers for the positive $3x+1$ map. For an odd $z$ prime to three, choose an exponent $1\le v\le6$ for which $p=(2^v z+1)/3$ is an integer prime to three. There are exactly two choices. The six powers of two run through the units modulo nine. The residues $2^v z\equiv 2,5\pmod9$ give children $p\equiv1,2\pmod3$, respectively. These two exponents have the same parity, determined by $z\bmod3$. Each child is odd and moves to $z$ under $S$ by one odd step and $v-1$ even steps.

Set $\ell=\lfloor(h-1)/6\rfloor\ge2$. Make $\ell$ successive inverse choices from 1. The $2^\ell$ resulting inputs $p$ are distinct, because each input uniquely determines its first $\ell$ odd-step valuations in the forward direction. For a word with exponent sum $V$, we have $V\le6\ell\le h-1$ and $p\le 2^{V-\ell}<2^{h-1}$ by iterating $(2^v z+1)/3\le2^{v-1}z$. Follow the word to 1, then remain there until time $h-1$. The number of odd steps is $s=\ell+h-1-V$.

Exactly half the words give odd $s$. Fix the first $\ell-2$ inverse choices. At the next inverse choice the two exponents have the same parity, while the two resulting children have different residues modulo three. Consequently the exponent parity for the final inverse choice is odd at one child and even at the other. Of the four completions of the fixed prefix, two give each parity of $V$.

For each retained input set $r=2^{h-1}-p$. The characterization above gives the one-step meeting, and distinct $p$ give distinct $r$, proving the count.
