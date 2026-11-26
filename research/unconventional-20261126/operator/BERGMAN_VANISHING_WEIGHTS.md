# Hypercyclicity and Gaussian mixing with a weight of liminf zero

Béhani’s Question 4.3 asks whether the shortcut Collatz transfer on a weighted Bergman quotient can be bounded, hypercyclic or ergodic when $\liminf_{n\to\infty}\omega(n)=0$, and whether its adjoint can have any eigenvalue. The first three properties can hold simultaneously for an explicit weight.

**Theorem O10.** Write $n=2^j u$ with $u$ odd. For positive integers set
$$
 \omega(2^ju)=2^j h(u),\qquad
 h(u)=
 \begin{cases}u,&3\nmid u,\\1/u,&3\mid u.\end{cases}
$$
Give degree zero any positive weight. Then $\liminf\omega(n)=0$. The transfer $\mathcal Te_k=e_{Tk}$, $e_k=z^k$, is bounded on $X_\omega$ with $\|f\|^2=\sum_{k\ge3}|c_k|^2/\omega(k)$ and deletion of degrees $0,1,2$. It is topologically mixing, has dense periodic points, and preserves a full-support strongly mixing Gaussian probability. In particular it is frequently hypercyclic and ergodic for that measure.

The weights satisfy $\omega(n)\le n$ and $\omega(2n)=2\omega(n)$. Thus all coefficient-space elements define holomorphic functions in the unit disk by Cauchy–Schwarz. The odd multiples of three show the vanishing liminf. An endpoint $a\ge3$ always has even predecessor $2a$, of weight ratio 2. If its odd predecessor $b=(2a-1)/3$ exists, then $3\nmid a$ and $\omega(a)=a$, while $\omega(b)\le b<a$. The fiber norm formula (Béhani, Proposition 2.1) gives $\|\mathcal T\|^2\le3$. The right inverse $Se_k=e_{2k}$ satisfies $\mathcal TS=I$ and $\|S\|=1/\sqrt2$.

Let $D=\bigcup_m\ker \mathcal T^m$. We prove $D$ dense on all ordinary components. If $k$ enters $\{1,2\}$, $e_k$ already lies in $D$. Otherwise for every $n$,
$$
    e_k-e_{2^n T^n k}\in\ker\mathcal T^n .
$$
Every orbit has an odd input after finitely many divisions by two. Immediately after an odd shortcut the state is a ternary unit, and both branches preserve the set of ternary units thereafter. Hence for all sufficiently large $n$,
$$
   \omega(2^n T^n k)=2^n\omega(T^n k)=2^n T^n k\ \ge\ 2^n.
$$
The norm of the correcting monomial tends to zero. Each monomial lies in the closure of $D$, and finite polynomials are dense.

For completeness one can see topological mixing directly. Given open sets choose $v,w\in D$ in the respective sets. Then $v+S^Nw\to v$ and $\mathcal T^N(v+S^Nw)=w$ for all sufficiently large $N$. For a periodic approximation, take $v\in D$ and $N$ large enough that $\mathcal T^N v=0$. The convergent series $\sum_{j\ge0}S^{jN}v$ is fixed by $\mathcal T^N$ and tends to $v$ as $N\to\infty$.

Here is an explicit construction of the invariant Gaussian probability. Choose a sequence $v_i\in D$ whose linear span is dense and put
$$
 x_{i,t}=
 \begin{cases}S^t v_i,&t\ge0,\\
               \mathcal T^{-t}v_i,&t<0 .
 \end{cases}
$$
For each $i$ the negative tail is eventually zero, the positive tail is square summable, and $\mathcal T x_{i,t}=x_{i,t-1}$. Choose positive $b_i$ with $\sum_{i,t}b_i^2\|x_{i,t}\|^2<\infty$. On the product space of independent standard centered complex Gaussian coordinates $\gamma_{i,t}$, the random series $\Phi=\sum_{i,t}b_i\gamma_{i,t}x_{i,t}$ converges in mean square and defines a centered Gaussian random element. Its law has full support. The vectors $b_i x_{i,0}=b_i v_i$ have dense span. More explicitly, any desired finite linear combination can be approximated with positive probability by finitely many independent coordinates, while an independent tail of sufficiently small mean-square norm lies in a prescribed small ball with positive probability. The product shift $(\gamma_{i,t})\mapsto(\gamma_{i,t+1})$ is strongly mixing and satisfies $\mathcal T\Phi=\Phi\circ\mathrm{shift}$ as mean-square random elements. The pushed-forward law is consequently invariant and strongly mixing. Birkhoff’s theorem applied to a countable basis of nonempty open balls gives frequent hypercyclicity.

**The adjoint existence question.** Across all weights in Question 4.3 for which the transfer is bounded, existence of an adjoint eigenvalue for *some* such weight is equivalent to existence of an ordinary component disjoint from $\{1,2\}$. To check this, identify a continuous functional with the values $f(k)$ it takes on $e_k$. Its squared norm is $\sum_{k\ge3}\omega(k)|f(k)|^2$. Extend $f$ by zero at $0,1,2$. The adjoint eigen-equation is $f(Tk)=\lambda f(k)$ on $k\ge3$, up to harmless conjugation of the eigenvalue. If $\lambda=0$, evaluation at $2k$ shows $f(k)=0$ at every $k\ge3$. If $\lambda\ne0$, every $k$ whose orbit enters $\{1,2\}$ has $f(k)=0$. Conversely, given a component $C$ disjoint from $\{1,2\}$, choose $\omega(k)=k^{-2}$ for positive $k$. The one-step fiber ratios are bounded since $Tk/k\le2$ and there are at most two predecessors, and the liminf is zero. Then $f={\bf1}_C$ has finite functional norm and is fixed by the adjoint. Thus the remaining existential subquestion is as strong as the existence of a counterexample to Collatz. For the explicit Gaussian-mixing example the adjoint has no eigenvalues. A dense generalized kernel already forces this for nonzero eigenvalues, and $\mathcal TS=I$ excludes zero.

- V. Béhani, *Linear dynamics of an operator associated to the Collatz map*, Proc. Amer. Math. Soc. 152 (2024), 1191–1206, §2, Theorems 1.1–1.2 and Question 4.3. <https://doi.org/10.1090/proc/16627> <https://arxiv.org/pdf/2303.03203>
