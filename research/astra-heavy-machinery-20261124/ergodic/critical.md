# A critical marked arm in three odd steps, with specified ternary digits

Fix any $b\ge1$. Every hypothetical escaping odd orbit has arbitrarily late actual class windows with the following property. Fix a unit residue $u\bmod 3^b$. There is an ordinary positive marked $z\equiv u\pmod{3^b}$ lying in one of these classes. Relative to its true least unit representative $x=n_{i+j}$ it satisfies
$$
U^3(z)=U^3(x),\quad r=E_3(z)-E_3(x)=e+c_b,
\quad e=v_2(3z+1),\quad |2^{-r}z-x|<13,
$$
where $c_b=2\,3^{2+b}+5$. The choice of class $i+j$ and the integers $e,r$ can be made **the same for every** $u\in(\mathbb Z/3^b\mathbb Z)^\times$. The time measured on the original class sequence is $0\le j\le O_b((\log n_i)^C)$ for an absolute $C$. This result reaches the original critical leading strip. It fixes the terminal odd clock and gives the exact cost in the added dyadic rank.

**Proof.** Use the notation and the hypotheses for an injective positive ordinary trajectory from [E3](proof.md). Choose $i$ arbitrarily late at a future-tail record of the unrestricted class minima. The sibling and packing bounds in [the quantitative proof](quantitative.md) give $D_i\ll n_i^{\theta-1}$ and $M_i/n_i\to1$. Let $Q$ be the first continued-fraction denominator of $\alpha=\log_2 3$ exceeding $\log_2 M_i+c_b+100$. Then $Q\ll_b(\log n_i)^C$ by Baker–Wüstholz: if $q$ is the preceding denominator, then $\|q\alpha\|<1/Q$ and $\|q\alpha\|\gg q^{-C}$. In particular $QD_i<1$ for large $i$. [Bourgain et al., Theorem 4.3](https://math.stanford.edu/~akshay/research/blmv.pdf)

For the convergent $p/Q$, each $j\alpha$, $0\le j<Q$, is within $1/Q$ of $jp/Q$ on the circle. The latter values form the complete grid. Consequently for some $j<Q$ the phase of $\log_2 M_{i+j}=\log_2 M_i+j\alpha\bmod1$ lies between $2/Q$ and $6/Q$ (target $4/Q$). Put $k=\lfloor\log_2 M_{i+j}\rfloor$, $e=\lfloor(k+c_b)/4\rfloor+1$, and $r=e+c_b$. Apply E2 with the one-gap prefix $(e)$, so $h=2$, $G=e$ and its required rank is exactly $r$. For each $u$ this produces a physical positive odd $z$ with the required residue, horizon and clock excess. In particular $M(z)=2^r M_{i+j}$.

Since $0<\log_2(M(z)/z)\le D_i<1/Q$, the ordinary phase $\delta_z=\{\log_2 z\}$ lies between $1/Q$ and $6/Q$, and $d=\lfloor\log_2 z\rfloor=k+r$. By the choice of $e$,
$$
1\le5e-d=4e-(k+c_b)\le4.
$$
Also $k\le\log_2 M_i+j\log_2(3/2)$ by the lower bound one on the corrected clocks. Thus $k+c_b\le2Q$ and $d+1\le(5/4)(k+c_b)+2\le3Q$. By convexity $2^{\delta_z}-1\le\delta_z$ on $[0,1]$. The resulting mark even satisfies $(d+1)(z-2^d)\le18\cdot2^d$, within the required $70\cdot2^d$. Together these estimates imply the PR197 mark and its valuation strip.

Finally, the affine identity of E3 with $A\le8$, original carry $C_x=3+2^{v_2(3x+1)}\le19$ and chosen carry $C=3+2^e$ gives
$$
9(2^{-r}z-x)=C_x-2^{-r}(3+2^e)+(2^A-2^{A-2s})/3 .
$$
Here $s\ge0$ is the sibling parameter and $r\ge e$. The absolute value on the right is less than $19+4+256/3<117$, proving the stated ordinary distance. The first actual image equals $3\,2^{c_b}(x+O(1))+2^{-e}$. The full synchronized construction pays a fixed excess above the chosen first valuation. Its merged endpoint does not give a drop below the original escape floor.
