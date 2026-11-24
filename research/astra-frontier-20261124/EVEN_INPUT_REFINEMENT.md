# Even inputs required for a smaller ordinary merger

**PROPOSED, written corollary.** Let $T(z)=z/2$ for even $z$ and $T(z)=(3z+1)/2$ for odd $z$. Write $p=p_a(x)$ for the number of odd inputs in the first $a$ steps from $x$. Let $n,x$ be positive ordinary integers with $x<n$, and $a,b$ nonnegative integer clocks. Suppose $e=v_3(n)\ge1$, $2^b\mid n+1$, and $T^a(x)=T^b(n)$. Then

$$a-p>e\log_2(3/2),\qquad a>b+1+e\log_2 3.$$

Equivalently, $2^{a-p+e}>3^e$ and $2^{a-b-1}>3^e$. The only source input is the odd-count inequality and the terminal carry computation in the [frozen odd-step proof](GLOBAL_CLOSURE_ATTEMPT.md), SHA-256 `455c4d0737fb0f93823ab68f103fa74457a59bd642b4aefb6826048916218860`.

**Proof.** The first $b$ inputs from $n$ are odd. The frozen theorem gives $p>b+e$, hence $a>b$. Put $D=a-b$. Let $p_1$ count odd inputs on the first $D$ competing steps from $x$, and $p_2$ those on the last $b$. Set $k=b-p_2$. On the last $b$ steps, $2^b T^a(x)=3^{p_2}T^D(x)+C$ with integer carry $0\le C\le3^b-2^b$. On the source arm, $2^bT^b(n)=3^bn+3^b-2^b$. Comparing these integers gives

$$T^D(x)=3^kn+m,\qquad m=(3^b-2^b-C)/3^{p_2},\qquad 0\le m<3^k.$$

In particular $m$ is an integer. Since $p=p_1+p_2>b+e$, the number $r=p_1-k-e$ is positive. Let $d$ be the number of steps through and including the $r$-th odd input on the first $D$ steps, so $d\ge r$. Set $N=D-d$, $z=T^d(x)$ and $u=n/3^e$. The next $N$ steps have exactly $k+e$ odd inputs. They end at $3^{k+e}u+m$.

Extend $T$ to signed integers by the same parity formula. The integer $z_0=z-2^Nu$ has the same first $N$ parities as $z$. Indeed, congruent inputs modulo $2^j$ for $j\ge1$ have the same parity and their outputs are congruent modulo $2^{j-1}$. The affine formula on that common word gives $T^N(z_0)=T^N(z)-3^{k+e}u=m$. Every negative integer stays negative, so $z_0\ge0$. The orbit of zero has no odd input, whereas $k+e\ge1$. Hence $z_0\ge1$. This also rules out $m=0$ because a positive integer stays positive. The nonnegative carry of the $N$ steps from $z_0$ now gives

$$3^{k+e}\le 3^{k+e}z_0\le 2^N m<2^N3^k.$$

Thus $N>e\log_2 3$. Since $a-p=N+(d-r)-e$ and $d\ge r$, the number of even inputs is strictly greater than $e\log_2(3/2)$. Adding $p\ge b+e+1$ proves the stated total-clock inequality. This argument gives necessary resource bounds for each finite merger satisfying the hypotheses. Existence of a merger for every source remains open.

**Finite replay.** For each positive $n\le12{,}000$ divisible by three, the [exact checker](controls/check_even_input_refinement.py) examined every $0<x<n$, every $0\le a\le40$, and every $0\le b\le v_2(n+1)$ through a complete endpoint index. It independently replayed both paths for each equality and checked both strict powers-of-two inequalities using integer arithmetic. The 4,000 eligible sources yielded 577 exact mergers, all passing. The [receipt](../../reports/astra-frontier-20261124/even-input-controls.json) records the finite scope.
