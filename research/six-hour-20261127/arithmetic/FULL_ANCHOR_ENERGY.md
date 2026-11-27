# Exact signed fourth moments at the full physical ceiling

Let an ordinary positive cycle have distinct odd phases of least period $p$, minimum $s$, maximum at most $(16s+7)/3$, and every odd valuation in $\{1,2\}$. Then for each $\varepsilon>0$,
$$
                     p\ll_\varepsilon s^{37/100+\varepsilon}.
$$
The external analytic input is Weaver's fixed-place Subspace-Theorem separation, Paper 145, Lemma 4. The earlier physical fourth moment gave $0.373834\ldots$ in the exponent, and PR200's modular three-grade estimate gives the height exponent $5/2$. The present count uses the full signed carry from the common terminal grade in each short return. It requires only the stated cycle hypotheses. The exponent remains above $1/3$. [Original four-segment source proof](FOUR_COPY_TAILS.md) · [Weaver, Paper 145](https://rstation.ai/problems/collatz/papers/145/v1) · [PR200, modular three-grade count](https://github.com/GettysburgResearch/collatz/blob/df2f17a117bea06bb34040a5a97e7dc9711d9871/research/six-hour-20261127/cycles/THREE_GRADE_MODULAR_BAND.md)

Use four $n$-edge interiors and guards of length $\lceil\eta n\rceil$ for $n\sim(\log_3 s)/3$. Write $F_i=\lfloor i\gamma+\varphi\rfloor$, $f_i=\{i\gamma+\varphi\}$, $\gamma=\log_2 3$, with the upper intercept of the cited source proof. Put $k_i=F_i-E_i$, where $E_i$ is the actual accumulated valuation. The full physical width is
$$
     \log_2((16s+7)/(3s))+O(n/s)=2+(2-\gamma)+O(n/s).
$$
Thus $k_i\in\{0,1,2\}$, and $k_i=2$ is allowed only when $f_i\le2-\gamma+O(n/s)$. Mark vertices within $s^{-1/3}$ of $2-\gamma$ on the circle. The count is $o(n)$ uniformly in the intercept by irrational equidistribution. Off these marks the allowed earlier grades on edge $i$ are $0\le k_i\le3-m_i$, where $m_i=F_{i+1}-F_i$ is one on $f_i<2-\gamma$ and two otherwise. Every ordinary edge from earlier grade $x$ to later grade $y$ also requires $m_i+x-y\in\{1,2\}$.

Take consecutive reverse returns to $[0,1/700)$. The previously verified clipped rotation has exactly three reverse schedules of lengths $665,971,1636$, including all its singleton cuts. Delete partial returns and returns touching marked vertices. They contain $o(n)$ edges, including a bounded endpoint loss. Condition on all their ordinary dates and the guard words, as well as the mechanical schedule, marked positions and the original cut dates. Distinct environments number $\exp(O(\eta n)+o(n))$, as all dates are within constant distance of $i\gamma$ and the schedule has $O(n)$ phase cells. The four-interior separation and Fourier source argument then require only the largest modular continuation count on each clean return. [Rotation proof and signed conditional targets](ANCHOR_CARRIES.md)

On an $r$-edge clean return, fix the actual suffix and four terminal grades. Its signed numerator has a prescribed residue modulo $3^r$. Fourier inversion and Hölder bound this atom by the maximum zero-residue fourth moment of any of the three one-copy terminal grades, using four copies of a common family. Its reverse recurrence, starting with common grade $k$ and $z=0$, is
$$
    3z_{\rm earlier}=2^m z_{\rm later}
        +2^{2-x_1}+2^{2-x_2}-2^{2-x_3}-2^{2-x_4}.
$$
Retain every divisible choice and impose no condition on the earliest resulting integer. To check equivalence to the modular count, list reverse increments $m_1,\ldots,m_r$, put $S_j=\sum_{a=1}^j m_a$ and write $d_j$ for the signed digit at reverse step $j$. After $j$ recurrences the carry is $2^{S_j}3^{-j}\sum_{a=1}^j 3^{a-1}2^{-S_a}d_a$. Its integrality is exactly prefix cancellation modulo $3^j$ in the ring with denominators powers of two. Cancellation on the whole return implies it on every prefix. The ordered predecessor multiplicities are unchanged by sorting each equal-sign pair, or by exchanging the two sides while negating the carry. These symmetries preserve all later path counts, so the code combines their states.

The nine resulting exact energies $Q_{r,k}$ obey $Q_{r,k}^{100}<3^{111r}$. The control includes all nine integers and six short schedules with an independent literal path-pair histogram. On each preceding return the actual suffix determines the next target, even if its carry is nonzero. Multiplication gives $3^{(111/100)n}$ per clean $n$-edge interior, with fixed deleted dates already paid in its environment. The four-interior source inequality and $\eta\downarrow0$ give the assertion. [Exact replay](check_full_anchor.py) · [Integer controls](FULL_ANCHOR_CONTROLS.json)
