# Synchronized smaller partners in extensions of every binary prefix

**PROPOSED, unconditional.** Use the positive shortcut map $T$. Two paths are synchronized here if their endpoints and counts of odd inputs agree at a common clock. For every integer gap $D$ there is a constructive binary residue class on which all positive pairs $(x,x+D)$ synchronize by a common horizon

$$
 H(D)\le \frac{3}{3-\log_2 3}\log_2\max(1,|D|-1)+7 .
 \tag{1}
$$

The assertion concerns a chosen class for each $D$. Other classes may require more steps. Said Duran’s September 2026 preprint gives an absorbing-word construction and proves almost-sure coalescence. Leen’s October preprint gives the pair transitions and another reducing boundary word. The bound below uses an explicit contracting choice that charges its length to the decrease in $|D|-1$. [Duran’s paper and formalization](https://doi.org/10.5281/zenodo.23003524) · [Leen’s pair process](https://doi.org/10.5281/zenodo.23268755)

## Choosing and realizing the parity word

Orient the two entries as $X$ and $3^sX+D$, $s\ge0$. Initially $s=0$. The bit prescribed at a step is the parity of the current base $X$. Direct substitution in $T$ gives the six transitions below.

| Condition | Bit | New $(s,D)$ | New base |
| --- | ---: | --- | --- |
| $D$ even | 0 | $(s,D/2)$ | $T(X)$ |
| $D$ even | 1 | $(s,(3D+1-3^s)/2)$ | $T(X)$ |
| $D$ odd, $s>0$ | 0 | $(s+1,(3D+1)/2)$ | $T(X)$ |
| $D$ odd, $s>0$ | 1 | $(s-1,(D-3^{s-1})/2)$ | $T(X)$ |
| $D$ odd, $s=0$ | 0 | $(1,(3D+1)/2)$ | $T(X)$ |
| $D$ odd, $s=0$ | 1 | $(1,(1-3D)/2)$ | $T(3^sX+D)$ |

The last row exchanges the two entries. At all times $s$ is the odd-count excess of the nonbase arm over the base arm. This follows from the parities in each row, including the swap when the former base obtains one more odd step. State $(0,0)$ therefore gives synchronization. Every chosen word of length $H$ specifies exactly one residue for the initial base modulo $2^H$. Indeed, upon writing the current base as $2u+\epsilon$, the new base is $u$, $3u+2$ or $u+(D+1)/2$. Its coefficient of $u$ is odd, so either next bit can always be chosen by lifting one more binary digit of the original base. Taking sufficiently large lifts keeps both starting values positive, and every positive lift follows the same word.

At level zero take the following actions. If $D=0$ stop. With even nonzero $D$ a single zero bit replaces $D$ by $D/2$. With odd $D$ choose the bit so that the level-one offset $E=(1+3D)/2$ or $(1-3D)/2$ is even. Precisely one of these integers is even, and neither can be zero for integral $D$. Write $v=v_2(|E|)\ge1$. Use $v$ zero bits, which hold the level at one and replace $E$ by its odd part, and then one bit equal to 1, returning to level zero with
$$
 D'=\frac{E/2^v-1}{2}.
$$
This costs $b=v+2$ steps. An odd part of $1$ gives absorption. An odd part of $-1$ gives $D'=-1$. From either $D=1$ or $-1$ the even choice gives $E=2$ and the next two bits $01$ give absorption. Thus the terminal cost for $|D|=1$ is three.

For $d=|D|\ge3$ odd and $d'=|D'|$, the inequalities
$$
 2^b d'\le 3d+1+2^{v+1},\qquad
 2^b(d'-1)\le3(d-1)
$$
follow from $2|E|\le3d+1$ and $2^{v+1}\ge4$. If $d'\ge2$, the drop in $\log_2(d-1)$ is at least $b-\log_2 3$, and $b\ge3$ gives $b\le C(b-\log_2 3)$ with $C=3/(3-\log_2 3)$. For an even step with $d/2\ge2$ the drop is at least one. Every nonterminal reduction decreases $d$. For a last odd reduction from $d\ge3$ to $d'\le1$, $2^v\le(3d+1)/2$ gives $b\le\log_2(d-1)+4$. A last even reduction from $d=2$ costs one. Telescoping the preceding drops and adding at most three terminal steps proves (1), including either sign of $D$.

There is a scale lower bound. If $D\ne0$ and a synchronized clock $H$ has common odd count $p$, the offsets of its two words differ by $3^p |D|$. Each offset lies between zero and $2^{H-p}3^p-2^H$ by the elementary [affine bound](README.md#affine-identities). Hence $2^{H-p}>|D|$, so at least $\lfloor\log_2|D|\rfloor+1$ even steps are necessary. In particular (1) has the correct order in the gap.

## Application to an arbitrary initial prefix

Fix $h\ge1$ and a binary cell, written uniquely $n=2^h t-a$ with $1\le a\le2^h$ and integer $t\ge1$. Use the mirror map $S(x)=x/2$ on even positive inputs and $(3x-1)/2$ on odd ones. If $r=S^h(a)$ and $q$ counts its odd inputs in that prefix, complementary parity lifting gives
$$
 T^h(n)=3^q t-r,\qquad s_h(n)=q,\qquad 1\le r\le3^q.
$$
The bound follows by multiplying the one-step inequalities $S(x)\le3^{x\bmod2}x/2$ and using $a\le2^h$. Set $m=2^q t-1$. It has $q$ initial odd steps ending at $3^q t-1$. Thus the two endpoints have the fixed gap $D=r-1$. The map $t\mapsto3^q t-r$ has an odd coefficient and lifts every prescribed binary residue class uniquely. Applying (1) gives one extension of the original binary prefix by at most $Cq\log_2 3+7$ additional bits, on **all** of whose sufficiently large ordinary lifts $n,m$ meet at clocks $h+H(D),q+H(D)$ with equal odd counts. This applies simultaneously on every further lift of the chosen extension. In particular every original class has a successful extension of depth $O(h)$ without using a density theorem.

Write $e=h-q$. For $t\ge2$ one has $n\ge2^h(t-1)$ and $m<2^q t$, giving $m/n<2^{1-e}$. Thus $e\ge1$ suffices for a strictly smaller positive companion, and in the limit of large $t$ the ratio tends to $2^{-e}$. With $e=0$ the all-odd prefix has $a=1$ and this construction gives $m=n$. A specified integer in the initial cell can still lie outside the constructed extension.

## Extending any already prescribed pair of paths

The choice of higher bits can also be made after prescribing an arbitrary length-$h$ joint prefix for the **same pair** $(x,x+D_0)$. To see this, take its current canonical state $(s,D)$ and set $z=D/3^s$. From every positive level $j$ force a downward move as follows. Put $e_j=v_2(3^j-1)$. At an even, nonzero offset of valuation $v\le e_j$, use $v$ zero bits to make it odd. If the even offset is zero or has valuation $v>e_j$, first use one bit equal to 1. The new offset $(3D+1-3^j)/2$ has valuation exactly $e_j-1$. Use $e_j-1$ zero bits. At an odd offset use a single bit equal to 1 to decrease the level. Each descent thus costs at most $1+e_j$ steps. Odd $j$ have $e_j=1$. For even $j$, factoring differences of squares gives $e_j=2+v_2(j)$. The total return clock has the bound
$$
 R\le2s+\lfloor s/2\rfloor+v_2(s!)\le7s/2.
$$

Every one of these forced updates gives $1+|z'|\le(3/2)(1+|z|)$. An even-offset zero bit halves $z$. An even-offset one bit gives $3z/2+(3^{-j}-1)/2$, and the downward move gives $3z/2-1/2$. At level zero the raw offset therefore has size at most $(3/2)^R(1+|D|/3^s)$. With $C=3/(3-\log_2 3)$, the previous construction forces absorption in a further
$$
 C\log_2(1+|D|/3^s)+C R\log_2(3/2)+7
$$
steps. This works for every integer offset, from either orientation, including a zero offset at positive level.

For the already prescribed initial $h$ bits from $(0,D_0)$, each of the six transitions gives $1+|z'|\le(3/2)(1+|z|)$, and the level rises at most once per step. Consequently every such cylinder has an explicitly determined successful subcylinder by total clock $O(h+\log(2+|D_0|))$, with an absolute constant. In terms of ordinary integers, the two given starts may both be extended by the same sufficiently large multiple of $2^h$ so that they synchronize by that clock. Exact equality on these lifted pairs leaves the eventual behavior of the original unshifted pair open.

The arbitrary-state extension also permits several offsets to be synchronized successively through refinements of the same binary cell. [Affine rays and ordinary components](AFFINE_RAYS.md)
