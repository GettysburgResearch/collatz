# How large an off-cycle partner offset must be

**CS4, written proof.** Suppose $S(x)=x/2$ for even positive $x$ and $S(x)=(3x-1)/2$ for odd positive $x$. A target $b>0$ is off-cycle if it does not belong to a periodic $S$-orbit. For every positive $c$ with $S^t(c)=b$, put $a=\#\{0\le j<t:S^j(c)\text{ is odd}\}$. Then

$$
                   3^a c\ \le\ 2^t b(3a+1)^{1/6}.
$$

Indeed the magnitudes $S^j(c)$ on this finite path are all distinct. A repetition would put its endpoint on the resulting cycle. Reading the steps backwards gives

$$
 c = \frac{2^t}{3^a}b \prod_{j=1}^a\left(1+\frac{1}{2B_j}\right),
$$

where $B_j$ are the distinct positive targets of the odd forward steps. Each target of an odd step is $(3v-1)/2\equiv1\pmod3$ and is greater than 1, since $S(1)=1$ while $b$ is off-cycle. Thus in increasing order the $j$-th target is at least $3j+1$. Put $x=1/(6j+2)$. Since $(1+x)^{-1}\ge1-x>0$ and $(1-x)^6\ge1-6x$, we have
$$
       (1+x)^6\le\frac{3j+1}{3j-2}.
$$
The sixth powers telescope to an upper bound $3a+1$. This includes $t=a=0$. The use of the ternary target residue sharpens the earlier square-root bound from unrestricted distinct positive targets.

For $n=2^p u-17>0$, $p,u\ge1$, consider an ordinary partner $m=2^t u-c>0$ with this shadow. Its positive shortcut trajectory reaches $3^a u-b$ at clock $t$, by the signed lifting identity. A strictly smaller partner of this form with off-cycle $b$ necessarily satisfies

$$
                    b(3a+1)^{1/6}\ \ge\ \frac{3^a}{2^p}.
$$

Otherwise the first inequality gives $c<2^{t-p}$. If $t\le p$ this contradicts $c\ge1$. If $t=p+r>p$, then $c<2^r$ and
$m-n=2^p(2^r-1)u+17-c>0$ since $2(2^r-1)\ge2^r$ for $r\ge1$. Either case rules out $m<n$.

In particular, on the family $p=33k$ with matched odd count $a=21k$, any such off-cycle offset must satisfy

$$
 b\ \ge\ \frac{(2187/2048)^{3k}}{(63k+1)^{1/6}}.
$$

Thus any fixed finite set of off-cycle offsets eventually becomes unavailable to the equal-slope smaller-partner construction, even when the realizing shadow lengths $t$ may grow arbitrarily. The successful branches in the main packet use periodic offsets 1 and 10. An arbitrary longer merger can use other shapes, different slopes, a moving offset, or a periodic offset. CS4 does not restrict those alternatives. No theorem about the complete list of negative Collatz cycles is assumed.
