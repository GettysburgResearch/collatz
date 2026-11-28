# A growing number of separated reference arcs on one actual source

**Status: PROPOSED corollary** of the [sharp open-trajectory inequality](OPEN_ARC_HEIGHT.md). Consider any sequence of actual positive integer shortcut paths of durations $D$, starting from possibly varying positive integers $n$. Cover each path by $K$ nonempty affine reference arcs with both endpoint heights at most $H\ge1$. Every reference must satisfy its word's affine law and differ from the physical input at the start of its own arc. Put

$$
        U=1+\log_2(n+1)+\log_2 H.
$$

Whenever $D/U\to\infty$ one has

$$
                    \frac{K}{\log(D/U)}\longrightarrow\infty .       \tag{1}
$$

In particular, for any **fixed** positive ordinary source and any $\theta<1$, all separated covers of its first $D$ actual steps with $\log_2H\le D^\theta$ satisfy $K/\log D\to\infty$ as $D\to\infty$. More explicitly, for each desired factor $A>0$ there is a duration beyond which every such cover uses at least $A\log D$ pieces. The initial source can even belong to a cycle provided the stated separation holds on each arc.

Fix $\varepsilon>0$ and an integer $m\ge1$. There is a constant $C_{m,\varepsilon}$ such that every block of $L$ steps under at most $m$ arcs of endpoint height at most $H$ from an integer $x>0$ satisfies

$$
 L\le(1+\varepsilon)\log_2(x+1)+C_{m,\varepsilon}(1+\log_2H).        \tag{2}
$$

Otherwise examples violating (2) for arbitrarily large constants would have $L\to\infty$, $\log_2H/L\to0$, and $\log_2x/L<1/(1+\varepsilon)$. This contradicts the open theorem at reduced denominator one. The source coefficient is independent of $m$.

Group the arcs chronologically in packets of at most $m$. Let $r=\lceil K/m\rceil$, $h_j=\log_2(x_j+1)$ at their starting boundaries, $B=1+\log_2H$, and $c=\log_2(3/2)$. Since either true branch satisfies $T(x)+1\le(3/2)(x+1)$, a packet of duration $L_j$ has

$$
 h_{j+1}\le h_j+cL_j\le a h_j+cC_{m,\varepsilon}B,\qquad
 a=1+c(1+\varepsilon)>1.
$$

Iteration of this elementary inequality, followed by summation of (2), gives $D\le C'_{m,\varepsilon}a^r(h_0+B)$ with a constant independent of the path, the number of packets, and $H$. Hence $\log(D/U)\le(K/m+1)\log a+O_{m,\varepsilon}(1)$. For the sequence under consideration this gives $\liminf K/\log(D/U)\ge m/\log a$. First keep $\varepsilon$ fixed, then make the previously fixed $m$ arbitrarily large. This proves (1). No effective onset follows from that compactness argument.

For genuinely fixed $H$, [physical normalization](REFERENCE_SHADOWS.md) gives a finite set of possible signed rational reference endpoints. A physical path between any two such endpoints consists of its first visit followed by zero or more laps at the terminal state, if that state is periodic. This is a finite periodic dictionary with finitely many finite initial words, possibly with very large and unknown first-visit times. The dictionary estimates in [Paper 15, Theorems 1, 5 and 9](https://rstation.ai/problems/collatz/papers/15/v2) concern actual odd-map exponent factors and charge their template description budget. Neither a bound for those first-visit times uniform in a growing $H$ nor an automatic small cover for an exceptional ordinary source follows from this finite observation. Inequality (1) instead allows arbitrary reference points to change with the duration and does not pay for the lengths of their internal traces.
