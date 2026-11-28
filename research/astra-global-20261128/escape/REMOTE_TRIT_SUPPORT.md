# Simultaneous remote trit blocks in a 3-adic affine support

Let $[z]_j$ be the representative of $z\in\mathbb Z_3$ in $[0,3^j)$. The expressions $[z]_j/3^j$ below are viewed in the **real** circle. The depth $j$ will vary.

**Lemma.** Let $K\subset\mathbb Z_3$ be uncountable and closed under $F(z)=z_*+3^h m^{-1}(z-z_*)$, where $h\ge1$, $m=2^s$, $s\ge1$, and $z_*\in\mathbb Q\cap\mathbb Z_3$. Fix any finite list of triples $(b_i,t_i,I_i)$, where $b_i$ is an integer, $t_i$ is a nonnegative depth offset, and $I_i$ is a nonempty open interval of the real circle. For some arbitrarily large common depths $k$ there exist $y_i\in K$ such that

$$\frac{[(y_i-b_i)/m]_{k+t_i}}{3^{k+t_i}}\in I_i\quad\hbox{for all }i.\tag{1}$$

The points $y_i$ can be different. This is simultaneous support at one band of depths, without any quantitative lower bound on the mass of those cylinders.

Select $z_i\in K$ so that $\delta_i=(z_i-z_*)/m$ are linearly independent over $\mathbb Q$. At each choice the forbidden rational span is countable, whereas $K$ is uncountable. Put $c_i=(z_*-b_i)/m\in\mathbb Q\cap\mathbb Z_3$. For $j=hn$ the quotient $c'_{i,j}=(c_i-[c_i]_j)/3^j$ is eventually periodic in $n$. In fact write $c_i=A/B$ with $B>0$, $3\nmid B$. Then $B c'_{i,j}$ is an integer congruent to $A3^{-j}$ modulo $B$ and in $(A/3^j-B,A/3^j]$. For large $j$ each residue has a fixed representative in that interval, including the sign-dependent endpoint choice for the zero residue. There is a common integer $P\ge1$ such that along all sufficiently large multiples $n$ of $P$ each tail equals one rational $c'_i$.

There is $d\ge1$ with $1+3^d\mathbb Z_3$ contained in the closure of $\{m^{-Pj}:j\ge1\}$. Indeed 2 has order $2\cdot3^{a-1}$ modulo $3^a$, so its powers topologically generate the units; the powers with exponent divisible by $sP$ form a subgroup of finite index, and any tail of its sequence is dense there. Let $v$ be Haar on the additive coset $1+3^d\mathbb Z_3$. As $N\to\infty$, the real torus vector

$$\left(\frac{[c'_i+v\delta_i]_N}{3^N}\right)_i$$

converges in distribution to product Haar. For a fixed nonzero integer vector $a$, the Fourier coefficient is a deterministic phase times the mean of the additive character with coefficient $\sum a_i\delta_i\ne0$. Its mean is exactly zero as soon as $N>d+v_3(\sum a_i\delta_i)$. This proves weak convergence by trigonometric polynomial approximation. It uses only fixed Fourier frequencies as $N$ grows. The $3$-adic tuple $(v\delta_i)_i$ itself remains a one-parameter set.

Write $T=\max_i t_i$, $N=D+T$, and let $D\to\infty$. Multiplying the $i$th coordinate of the torus vector by $3^{T-t_i}$ gives exactly the coordinate with depth $D+t_i$, modulo one. The inverse images of any strictly smaller open subintervals of $I_i$ have positive product Haar mass. For some large $D$ and $v$ in the coset all the shorter-depth coordinates lie in the subintervals, at a uniform positive distance from their complements in $I_i$. One may fix the inner subintervals and their margins first and take $D$ large enough that $3^{-D}$ is less than the minimum margin.

Choose arbitrarily large multiples $n$ of $P$ such that $m^{-n}\equiv v\pmod{3^N}$. Set $y_i=F^n(z_i)\in K$ and $k=hn+D$. Since $(y_i-b_i)/m=c_i+3^{hn}m^{-n}\delta_i$, its normalized residue at depth $k+t_i$ is exactly

$$\frac{[c'_i+m^{-n}\delta_i]_{D+t_i}}{3^{D+t_i}}+
 \frac{[c_i]_{hn}}{3^{hn+D+t_i}}.$$

The second summand lies in $[0,3^{-D})$, which proves (1). The lemma also applies to a stationary measure with support $K$: each strict inequality describes an open finite cylinder, hence has positive measure.
