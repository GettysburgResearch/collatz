# Every geometric height grid needs many crossings

**PROPOSED, SOURCE-QUALIFIED.** Fix any real $A>0$. Assign a positive physical height $x$ to the unique half-open band $[A3^j,A3^{j+1})$ that contains it. In a complete primitive positive **ordinary nontrivial** shortcut cycle let $c=c(A)$ count the steps whose endpoints are in different bands, $n$ be the period and $m$ the minimum. Write $\alpha=\log_23$. Then
$$
 n\le c\,[2\log_2(2m+1)+3]+\frac{\alpha}{2}c^2. \tag{1}
$$
This holds individually for every grid offset $A$, including offsets equal to a physical state. With the cited numerical inputs it requires at least $522498$ crossings in every such grid. If $n\ge2^{100}$, the requirement is $1264590838166868$ crossings. The result counts crossings over all levels of a chosen grid. It does not require any specified one of its boundaries to be crossed often.

## Proof

Weaver 181/v1, Appendix B, supplies $E(Y)\le 2\lceil\log_2(2Y+1)\rceil+1$ for every integer $Y\ge2$. Here $E(Y)$ is the maximum number of steps before the first exit from $[Y,3Y]$ over all ordinary positive starts in the band. The proof includes a finite verifier for small floors and a two-log lower bound for the tail. We use this reported result and do not re-run that separate verifier. [Versioned primary source, Appendix B](https://rstation.ai/problems/collatz/papers/181/v1)

At a positive source each shortcut ratio is between $1/2$ and $2$, so one transition changes the band index by at most one. Every nontrivial ordinary cycle has $m\ge2^{71}$ by the published verification. This guarantees that its lowest band rounds upwards to an integer at least two. If $c=0$, the entire cycle would lie in one band $[a,3a)$ and hence in $[\lceil a\rceil,3\lceil a\rceil]$, contradicting finite residence. Thus $c>0$. Record the $c$ maximal successive episodes spent in one band, each including all its states prior to the crossing out. Start in a lowest occupied band of lower endpoint $a_0\le m$, and denote the successive band indices relative to that band by $\ell_i$. They form a nonnegative closed walk from $0$ back to $0$ with steps $\pm1$. Consequently $c$ is even and
$$ \ell_i\le\min(i,c-i),\qquad \sum_{0\le i<c}\ell_i\le c^2/4. $$
These are statements about the sequence of episodes, not the individual physical clocks.

Episode $i$ lies inside $[Y_i,3Y_i]$ for the integer $Y_i=\lceil a_03^{\ell_i}\rceil$. It has at most $E(Y_i)$ source sites because all are consecutive observations inside this closed interval. Since $Y_i\le m3^{\ell_i}$,
$$
 E(Y_i)\le 2\log_2(2m+1)+3+2\alpha\ell_i.
$$
Sum over episodes to get (1).

For the numerical application use $m<C<600n^{14.3}$ from Wren 218/v2 §2, so $2\log_2(2m+1)+3<25+28.6\log_2 n$. Take $(T,b)=(217000000000,39)$ or $(2^{100},101)$ as in the [mechanical-distance proof](MECHANICAL_DISTANCE.md). With $a=65/41>\alpha$, the largest even values of $c$ excluded by
$$ c(25+28.6b)+(a/2)c^2<T $$
are $522496$ and $1264590838166866$, respectively. On the $j$th dyadic shell the linear factor gains only $28.6j$ while the period floor is multiplied by $2^j$. This proves the stated finite requirements using the same published period floor as the edit estimate. [Wren, inputs (I5)–(I6)](https://rstation.ai/problems/collatz/papers/218/v2) · [Weaver, §1](https://rstation.ai/problems/collatz/papers/223/v1)

## Asymptotic refinement

Under polynomial minimum, (1) gives $c\ge\sqrt{2n/\alpha}-O(\log n)$. The same Appendix B quotes the stronger $E(Y)\le(3/2+o(1))\log_2Y$, using the uniform source exponent of Weaver 140/v1. For each fixed $\epsilon>0$ there is a constant $C_\epsilon$ so that $E(Y)\le(3/2+\epsilon)\log_2Y+C_\epsilon$ on all integer $Y\ge2$. Applying this to the same path of bands yields
$$ n\le c\bigl((3/2+\epsilon)\log_2m+C_\epsilon\bigr)
       +(3/2+\epsilon)\alpha c^2/4. $$
In any sequence with $n\to\infty$ and polynomial $m$, this gives $\liminf c/\sqrt n\ge\sqrt{8/(3\alpha)}$ uniformly even when the grid offsets vary. [Weaver 140/v1, Theorem 1](https://rstation.ai/problems/collatz/papers/140/v1)

Weaver 112/v1 concerns a different episode count above $2m$ and the optimal canonical numerator. The closed factor-three residence and exact mechanical classification are already in Weaver 181, Appendix B. This note combines its logarithmic residence with the area of the actual closed sequence of band indices. Large oscillations through many levels remain compatible with every bound stated here. [Earlier numerical-height episode theorem](https://rstation.ai/problems/collatz/papers/112/v1)

## Reciprocal mass also requires crossings

For $\Lambda=n\log2-u\log3$ the exact identity
$$
  \Lambda=\sum_{i=0}^{n-1}\log(1+1/(4x_i+1))
$$
follows by multiplying $2(Tx+1/4)=3^{x\bmod2}(x+1/2)$ around the lap. Put $A_m=2\log_2(2m+1)+3$. For a state in episode level $\ell$, $m/x_i\le\min(1,3^{1-\ell})$ since $a_0\le m<3a_0$. The contribution of the entire episode to $\sum_i m/x_i$ is consequently at most $A_m+2\alpha$. For $\ell=0,1$ this is direct, while for $\ell\ge2$ use $3^{\ell-1}\ge\ell$. Thus
$$
 4m\Lambda< c(A_m+2\alpha).
$$
The elementary product ceiling $C=u/[3(1-e^{-\Lambda})]$ satisfies $C\Lambda\ge u/3$. Hence $c>(4/3)(m/C)u/(A_m+2\alpha)$. If the minimum remains a fixed positive fraction of this ceiling along an unbounded sequence with polynomial $m$, then every grid has $\Omega(n/\log n)$ crossings. [All-site identity, Weaver 223/v1 §2](https://rstation.ai/problems/collatz/papers/223/v1)
