# Primitive positive cycles at every prescribed local coordinate

Choose any trace in the full-measure, dimension-$H_2(\log_3 2)$ family of FULL_DENOMINATOR_SHORT_CLOSURES.md (SHA-256 3138a2b8a9acdf78b6fc46f73ada49de288b37132f7150dc6923ce178ff8aeda), with $C_n=n^{B+o(1)}$, $B>1$. Write $\alpha\in\mathbb Z_2$ for its transcendental parity source, $S_n=\sum_{i<n:b_i=1}(3C_i)^{-1}\to S>0$. Fix any $c>0$, any $u_3\in\mathbb Z_3^\times$ and any collection $u_p\in\mathbb Z_p$ for the primes $p\ge5$.

**Theorem.** For every sufficiently large $n$ there is a positive primitive rational shortcut cycle with starting phase $z_n$, period $N_n=n+O(\log n)$ and the prescribed first $n$ bits, such that

$$
 z_n\to c\ \text{in }\mathbb R,\qquad
 z_n\to\alpha\ \text{in }\mathbb Q_2,\qquad
 z_n\to u_p\ \text{in }\mathbb Q_p\quad(p\ge3).
$$

Its maximum real height is $n^{B+o(1)}$. The full cyclic moving correlations are Bernoulli on calendars $\ell/\log n\to\infty$, as in the compact closure theorem. The common reduced denominator of all phases is $d_n=2^{n+o(n)}$ and its least prime divisor tends to infinity. Thus integrality at every *fixed* prime eventually holds, while no one of the large denominators equals one. The limits above concern individual local coordinates.

### A finite system of places

Prescribe $u_3\pmod{3^h}$ and one class $a\pmod Q$, $(Q,6)=1$. The latter combines any finite list of other prime powers by the Chinese remainder theorem. Write $E(x)=x/2$, $O(x)=(3x+1)/2$ for the two formal shortcut branches.

A fixed word $V$ with $h$ odd steps can force its terminal residue to $u_3\bmod3^h$ for every initial value integral at three. To construct one, take a positive odd unit $y$ in the prescribed class. Successively choose $e\ge1$ with $2^ey\equiv1\bmod3$ and $2^ey\not\equiv1\bmod9$, and replace $y$ by $(2^ey-1)/3$. Such a choice exists because $4$ has order three modulo nine. Each new state is again a positive odd unit. Reverse the resulting $h$ ordinary blocks. Its affine slope is $3^h$ times a ternary unit, so its terminal residue is independent of the initial value. For $h=0$ the empty word suffices.

Modulo $Q$ both branches are invertible. The finite group they generate contains every translation since $(O\circ E)\circ(E\circ O)^{-1}$ is translation by $1/4$. Its semigroup equals its group, so each group element has a word using only forward branch letters. The desired total affine map $F(x)=(x+a)/2$ belongs to this group. For each possible affine action $A$ of the initial trace prefix choose a correction word $H_A$ with $V\circ H_A\circ A=F\pmod Q$. After $H_A,V$, append a common fixed number of zero bits, divisible by the order of two modulo both $Q$ and $3^h$ (ignore modulus one). Take this number large enough that every one of these finitely many final blocks has real affine form $y\mapsto g_Ay+c_A$ with $0\le c_A<c/2$. It preserves both finite-place conclusions.

### Tuning the positive fixed point

Between the trace prefix and this final block insert $t$ ones and then $k$ zeros. Require both $t$ and $k$ to be multiples of a common exponent $T$ of the finite branch group modulo $Q$, taking $T=1$ for the trivial group. The finite-place calculations therefore remain unchanged. Since $O^t(y)=(3/2)^t(y+1)-1$, the fixed-point equation of the complete word is

$$
 z=r(z+S'_n)+c_A,\quad
 r=g_AC_n(3/2)^t2^{-k},\quad
 S'_n=S_n+\frac{1-(2/3)^t}{C_n}.
$$

The finite list of target multipliers $r_A=(c-c_A)/(c+S)$ is contained in $(0,1)$. Write $t=Tj$, $k=Tv$. The fractional parts of $j\log_2(3/2)$ are dense, and the maximum gap of their first $J$ points tends to zero. Taking $0\le j\le J(n)$ with $J(n)\to\infty$ and $TJ(n)=o(\log n)$ allows $v$ to be chosen so $r/r_A\to1$, uniformly in the initial phase $\log_2(g_AC_n/r_A)/T$ and $A$. More explicitly choose $j$ so this phase plus $j\log_2(3/2)$ is close to an integer $v$. Eventually $v\ge0$ and $k=\log_2 C_n+o(\log n)$. Thus $r<1$, $S'_n\to S$, and the positive fixed point $(rS'_n+c_A)/(1-r)$ tends to $c$.

Writing the integer intercept $D'$ and slope $3^{q}/2^N$ of the complete word, the fixed point is $z=D'/(2^N-3^q)$. Its true denominator is coprime to six, so the $2$-adic parity coding and ternary force apply. The action $F$ modulo $Q$ has $1-1/2$ invertible. Hence $2^N-3^q$ is a unit there and $z$ is integral and congruent to $a\bmod Q$. The first $n$ strict-supercritical prefixes prevent any genuine positive lap of length at most $n$, while a proper divisor of $N=n+O(\log n)$ would be at most $n$ eventually. The whole period is primitive. The first $n$ real states have the prescribed polynomial scale. The $t$ ones add a factor $(3/2)^{o(\log n)}=n^{o(1)}$, the zeros reduce height, and the finitely many final letters enlarge by at most a fixed factor. This proves the global height assertion for fixed local data. The cyclic seam argument from the compact closure theorem applies to any $O(\log n)$ suffix. Every such compact closure has full denominator exponent one by the cited full-denominator result.

### Increasing the finite conditions

At stage $j$, impose the first $j$ desired prime congruences to precision $j$, the desired ternary precision $j$, and real error below $1/j$. For fixed $j$ all correction lengths and tuning constants are finite. Increase a starting threshold $n_j$ so that for every $n\ge n_j$ the finite construction meets this real error, the total number of tuning ones and fixed correcting letters is at most $(\log n)/j$, and $|k-\log_2 C_n|\le (\log n)/j$. Use stage $j$ from $n_j$ until the next threshold. These choices ensure $O(\log n)$ total extra letters and only $o(\log n)$ expanding or fixed-correction letters, preserving all preceding bounds. Every fixed prime is eventually excluded from $d_n$ and its specified integral residue is reached to arbitrary precision. The dyadic prefix gives the stated $2$-adic limit. This proves the theorem.

The exclusion of zero classes modulo three is necessary for nontrivial rational cycles prime to three: after an odd step the physical state is a ternary unit, and both subsequent branches preserve that property. No statement identifies the transcendental dyadic source with the real target. The construction gives no denominator saving below the fixed ordinary $2^n$ congruence threshold.
