# A single ordinary edge can carry a positive-density boundary value

Let $T$ be the usual shortcut and write $f(n)=1$ if $T^k n=5$ for
some $k\ge0$, and $f(n)=0$ otherwise. This simple control retains an
exception at one specified ordinary source. For all positive integers,
$$
 f(n)-f(Tn)=\mathbf1_{n=5},\qquad f(2n)=f(n).
$$
Indeed, every visit to 5 from a different start factors through the next
step, while the forward path from $T5=8$ is $8,4,2,1,2,\ldots$.
Consequently $f(2n+1)=f(3n+2)$ except at $n=2$.

Both values have positive lower natural density, using a separate
predecessor-count input. The two rooted ancestor sets of 5 and 85 are
disjoint. Their positive orbits reach one through $8$ and $128$,
respectively, without visiting each other. Both roots are ternary units.
The cited Paper 10/v1, Theorem 1, gives $\#\{n\le X:T^kn=a
\text{ for some }k\}\ge cX/a$ for every ternary-unit root $a$ and
$X\ge a$, with absolute $c>0$. Thus the lower densities of $f=1$
and $f=0$ are at least $c/5$ and $c/85$. The positivity statement
uses that source; the single-edge identity above is elementary.
[Uniform predecessor floor and its stated mixing input](https://rstation.ai/problems/collatz/papers/10/v1)

The rooted indicator also has uniform shift stability. Let $w=w(N)$ be
a nonnegative integer with $\log(2+w)=o(\log N)$. Then
$$
 \sup_{A\ge1}\frac1N\sum_{A\le n<A+N}|f(n+w)-f(n)|\longrightarrow0 .
$$
To see this, discard $n<\sqrt N$ and set
$h=\lfloor\tfrac14\log_2N\rfloor$. Both trajectories exceed 5
through this clock since $T^i n\ge2^{-i}n$. If they meet by clock $h$,
their future visits to 5 agree, and neither has already visited it.
The cited affine absorption estimate on a complete $2^h$ block bounds
the failed fraction by
$O((1+\sqrt{\log(2+w)})/\sqrt h)$. Covering any length-$N$ interval
by complete blocks costs a factor $1+O(2^h/N)$. The discarded terms
cost at most $N^{-1/2}$. Negative shifts follow by exchanging the two
starts and discarding any nonpositive indices. This argument passes an
existing finite-clock absorption theorem to a rooted indicator even
though that indicator has a one-point exception.
The fixed-target dyadic-window argument also appears in Paper 179, Appendix A.6.
[Rooted indicator shift estimate](https://rstation.ai/problems/collatz/papers/179)
[Affine pair estimate for growing shifts](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md#reaching-a-small-normalized-offset)

Finally $f(3n+2)=f(2n+1)$ apart from the single source already given.
The two unit shifts $f(2n+1)-f(2n)$ and $f(3n+2)-f(3n)$ have vanishing
mean absolute value on every length-$N$ interval of $n$, by bounding each
sum on its full translated interval of length $2N$ or $3N$. Hence
$f(3n)-f(n)$ has vanishing mean absolute value there as well, while
doubling invariance is exact. A method that retains only these asymptotic
shift and dilation identities and positive density sees the same control.
Exact component indicators satisfy the forward edge identity also at the
marked source. An argument using that stronger pointwise condition can
still distinguish them.
