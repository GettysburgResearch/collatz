# Total positive defect separates escape from nontrivial periodic points

For the ordinary shortcut map on positive integers, choose rational weights
\[
 q(n)=\begin{cases}1,&n=1,2,\\1+n^{-2},&n\ge3,\end{cases}
 \qquad W(n)=(Tn/n)^2q(n).
\]
Let $\Phi$ be the minimum, over total-computable rational $0<u(n)\le1$, of the extended nonnegative quantity
\[
                    \sum_{n\ge1}[\log(W(n)u(n)/u(Tn))]_+ .            \tag{1}
\]
The same value and attainment hold on restricting to programs whose positive log defect is at most $\log 4$ at every edge. Then the two possibilities are
\[
 \Phi=
 \begin{cases}
   +\infty,&\text{some positive ordinary trajectory escapes},\\[2mm]
   \displaystyle\sum_{\substack{n\ge3\\ n\ {\rm periodic}}}\log(1+n^{-2}),
       &\text{every positive ordinary trajectory is bounded}.
 \end{cases}                                                          \tag{2}
\]
Thus $\Phi=0$ is equivalent to every ordinary positive trajectory reaching 1. A finite strictly positive value would mean that there is a nontrivial positive cycle and no escaping trajectory. This characterization leaves the value of $\Phi$ undetermined.

**Escape lower bound.** Along a simple orbit from $s$ to its first state $x_t\ge X$, telescope the signed sum before taking its positive part at each edge. The result is at least
\[
           2\log(X/s)+\log u(s),
\]
since the physical height ratios telescope exactly, $q\ge1$ and $u\le1$. All contributing departures are distinct sites below $X$. Hence (1) is infinite for every candidate if any source escapes. The constant $u=1$ is admissible even under the stated defect cap. Here $W(1)=4$, $W(2)=1/4$, and at odd $n\ge3$ one has $W(n)\le(5/3)^2(1+1/9)<4$; even sites satisfy the bound as well. This argument uses no reciprocal packing.

**Cycle lower bound.** Around one complete positive cycle $C$, the product of physical height ratios and of the $u$-ratios equals one. The sum of positive log defects is at least $\log Q_C$, $Q_C=\prod_{x\in C}q(x)$. Distinct cycles are disjoint, and the sum of these lower bounds is finite since $\sum_{n\ge3}\log(1+n^{-2})\le\sum_{n\ge3}n^{-2}<1$.

**Attainment under boundedness.** Assume all positive starts eventually repeat. From any $n$, find its first repeat, identify its cycle, and mark its largest state $z$. This gives a terminating program under the boundedness hypothesis. For this component define $B(n)$ as the maximum product of $W$ over the ordinary prefixes up to and including first arrival at $z$, with the empty product equal to one. The same $z$ is chosen from every starting point in that component. Put $u(n)=1/B(n)$, a positive rational at most one. At every unmarked site the maximum recurrence $B(n)=\max(1,W(n)B(Tn))$ makes the positive defect zero.

At $z$ the possible nonempty products from $z$ until its next return are
\[
              (T^jz/z)^2\prod_{i<j}q(T^iz).
\]
The height factor is at most one because $z$ is maximal on the cycle. Each partial $q$ product is at most $Q_C$, and the full lap attains $Q_C$. Hence the positive log defect at $z$ is exactly $\log Q_C$. These sites and only these sites can contribute, giving the second line of (2). The individual defect cap follows from $\log Q_C<1<\log4$. This argument works with infinitely many bounded components. It establishes an existential minimum for the actual graph without an algorithm to decide that its inputs will all repeat.

The weights in (1) use true physical height ratios and add a summable positive charge outside the standard cycle. The separate [escape flux identity](ESCAPE_FLUX.md) uses the original squared branch slopes and counts the number of escaping components. Both have ordinary integer quantifiers; neither computes its minimizing value.
