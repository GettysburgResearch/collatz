# An exact real-window formulation and a fixed overlap clock

**PROPOSED.** The strict six-branch chart has a positive ordinary all-time survivor if and only if there is a real $C>0$ for which every term $C(P/Q)^n$ lies in a specified union of 36 closed intervals repeated modulo $PQ$. Each interval has width less than 26, and $PQ=278628139008$. This equivalence permits a real starting parameter and reconstructs ordinary integer edges in the reverse direction. Excluding all such parameters remains open.

For every survivor the minimal cap–root overlap horizon is one *exact* lower mechanical clock with fixed intercept. The characteristic zero-intercept increment word, which has exactly the required limiting slope, is impossible for every starting state.

## Source and constants

Use [L-0041](../../claims/lemmas/L-0041-six-branch-root-cap-recurrence.md) and [T-0046](../../claims/theorems/T-0046-two-sided-cap-root-overlap.md) at main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The physical source is PR #45, `a7846473b10aa5caf8c9c57b0a612db0b8db402a`, `research/smooth-cycle-synthesis/claims/T-8403-six-branch-ordinary-counterexample-criterion.md`. The coordinate here is the chart root. Set $P=3^{12}$, $Q=2^{19}$, $\lambda=P/Q$ and retain the following ordered triples of source residue, output residue and affine increment.

| i | $r_i$ | $c_i$ | $a_i$ |
|---:|---:|---:|---:|
| 0 | 294912 | 298936 | 229376 |
| 1 | 331776 | 336303 | 258048 |
| 2 | 438784 | 444771 | 290304 |
| 3 | 297024 | 301077 | 326592 |
| 4 | 6472 | 6561 | 367416 |
| 5 | 466033 | 472392 | 413343 |

A source $x=r_i+Qk$, $k\ge0$, maps to $F(x)=c_i+Pk=(Px+a_i)/Q$. Define $b_-=229376/7153$, $b_+=413343/7153$, and $w=b_+-b_-<26$. The identities $b_\pm(P-Q)=a_\pm$ make these the real correction bounds from T-0046.

## From ordinary values to windows, and back

For an infinite legal type sequence set
$$
 B_n=\sum_{j\ge0}\frac{a_{i_{n+j}}}{Q\lambda^{j+1}},
 \qquad C=x_0+B_0.
$$
This is an absolutely convergent real series, independent of the interpretation of any 2-adic completion. Its terms give $b_-\le B_n\le b_+$ and $\lambda B_n=B_{n+1}+a_{i_n}/Q$. Hence $y_n=C\lambda^n=x_n+B_n$. For every $n\ge1$, $x_n$ has an allowed source residue modulo Q and an allowed previous output residue modulo P. Discard the first state when passing to an all-time window sequence.

Let $\mathcal Z$ be the 36 residues z modulo $M=PQ$ satisfying $z\bmod Q\in\{r_i\}$ and $z\bmod P\in\{c_i\}$. Existence and uniqueness for every pair follow from coprimality. The windows are
$$
 \bigcup_{z\in\mathcal Z,\,k\in\mathbb Z}
       [z+kM+b_-,z+kM+b_+].                                      \tag{1}
$$
In particular their total length divided by M is $36w/M<3.33\cdot10^{-9}$.

Conversely suppose $C>0$ and every $y_n=C\lambda^n$ lies in (1). There is a unique integer $x_n$ under its window. Indeed distinct eligible integers either differ modulo Q, where the least circular separation among distinct source residues is 2112, or differ by at least Q. Write $e_n=y_n-x_n\in[b_-,b_+]$. Since $y_n\to\infty$, discard a finite prefix to ensure $x_n>0$. Its source residue gives a legal F edge. Now
$$
 F(x_n)-x_{n+1}=e_{n+1}-\lambda e_n+a_{i_n}/Q.
$$
The absolute value is at most $w+(a_+-a_-)/Q<27$. On the other hand both $F(x_n)$ and $x_{n+1}$ reduce modulo P to output residues. Their least distinct circular separation is 2141, and P itself exceeds 27. The difference therefore vanishes. This proves the reverse implication for a whole ordinary orbit. The second residue constraint is used here: with $x=5523840113$ the actual image is $5599203327$, but $x'=5599203328$ has a valid source residue and lies within one unit. Taking $y=x+45$ puts $y$ and $\lambda y$ in the source-residue windows around $x$ and $x'$ alone, giving a spurious local edge if the output test is discarded.

## The exact overlap word

Return to the original survivor before discarding any prefix. Since $Q-\max r_i=58255>b_+$, the interval $[x_n,x_n+B_n]$ contains no positive multiple of Q as a right endpoint or interior point. Every positive power $Q^k$, $k\ge1$, is such a multiple. Since $x_n\ge1$, this proves
$$
 \ell_n=1+\lfloor\log_Q x_n\rfloor
       =1+\lfloor n\alpha+\beta\rfloor,
 \quad \alpha=\log_Q\lambda,\quad\beta=\log_Q(x_0+B_0).           \tag{2}
$$
Thus every sufficiently late equality $S_{u_n}=R_{v_{n,\ell_n}}$ of T-0046 uses the same fixed phase in (2), at every n. An exclusion still has to cover every admissible initial root and its phase.

Here $0<\alpha<1$ is irrational by unique factorization. The lower mechanical increment word of irrational slope determines its intercept modulo one: if two intercepts differ by $0<d<1$ modulo one, density of $\{n\alpha+\beta\}$ makes the two floor sequences differ alternately by two adjacent integers. They cannot have identical increments. In particular the zero-intercept word cannot be the overlap increment word of a survivor, even on an entire tail restarted at an arbitrary chart state: it would give $C=Q^k$ for some integer k. Since $C=x_0+B_0>1$, k must be positive, contrary to the absence of a multiple of Q in that interval.

The choice $\log_Q x_0$ as a surrogate for $\beta$ also disagrees on a positive proportion of horizon values. The intercept difference is $d=\log_Q(1+B_0/x_0)\in(0,1)$, and irrational rotation gives disagreement with limiting frequency exactly d. Equating the two horizon sequences because their slopes agree would discard actual overlap obligations.
