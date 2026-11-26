# The full weighted Koopman spectrum on every ordinary component

**Proposed theorem, with written proof.** Let $Tn=n/2$ for even positive $n$ and $Tn=(3n+1)/2$ for odd $n$. Let $C$ be any ordinary weak component, or all positive integers. For $1\le p<\infty$ and $\sigma\ge0$, write $X=\ell^p(C,n^{-\sigma})$ and $Uf(n)=f(Tn)$. Essential spectrum means the set of $\lambda$ such that $U-\lambda I$ fails to be Fredholm. Set
$$
                  R=(3/2)^{\sigma/p}.
$$

**Theorem O8.** If $3^\sigma\ge2$, the ordinary spectrum and the Fredholm essential spectrum of $U$ on $X$ are both the entire closed disk $\{|z|\le R\}$. For every $\sigma\ge0$ the essential spectrum contains this disk. If $\sigma>1$, $R^{-k}U^k$ is uniformly bounded in operator norm and converges strongly to zero, while $\|U^k\|_{\rm ess}\ge R^k$ for every $k$. All conclusions hold separately on each ordinary component, including the known basin of 1, without a convergence assumption on other orbits. No sharp transition at $3^\sigma=2$ is claimed.

## 1. Ordinary inverse fiber multiplicities

A length-$k$ forward word with $q$ odd inputs at positions $0\le d_1<\cdots<d_q<k$ and endpoints $x,T^kx=a$ satisfies
$$
   2^ka=3^q x+F,\qquad
   F=\sum_{i=1}^q 3^{q-i}2^{d_i}
      \le 2^{k-q}(3^q-2^q).                                       \tag{1}
$$
Composition proves the identity. Each $d_i\le k-q+i-1$ gives the bound after summing a geometric series. For fixed $q>0$ the carry $F$ determines all positions. Its 2-adic valuation gives $d_1$, and subtracting $3^{q-1}2^{d_1}$ allows the procedure to continue. A fixed endpoint $a$ requires $F\equiv 2^ka\bmod 3^q$. There are at most $1+2^{k-q}$ possible integers in this residue class in the interval from (1). For $q=0$ the unique all-even path gives the same bound. Each possible word determines at most one ordinary $x$ by (1). The estimate imposes no independence assumption on odd steps.

The isometry $J:X\to\ell^p(C)$ given by $Jf(n)=n^{-\sigma/p}f(n)$ conjugates $U$ to
$$
  Wg(n)=(Tn/n)^{\sigma/p}g(Tn).
$$
Define $c_0=2^{-\sigma/p}$, $c_1=(3/2)^{\sigma/p}=R$ and $Bg(n)=c_{n\bmod2}g(Tn)$. Each ordinary point has at most two predecessors so these operators are bounded. The difference $W-B$ vanishes on even outputs, and its odd coefficient tends to zero. Truncating this difference to finitely many output rows approximates it in norm, by the same two-predecessor bound. It is compact on every component, also for $p=1$.

The columns of $B^k$ have disjoint supports because $T^k$ is a function. Hence its $p$-th norm power is the supremum, over endpoints $a$, of the sum of $(3^q/2^k)^\sigma$ over the ordinary inverse fiber. By (1),
$$
   \|B^k\|^p\le R^{kp}
        \sum_{e=0}^k(1+2^e)3^{-\sigma e},\qquad e=k-q.             \tag{2}
$$
The sum is bounded if $3^\sigma>2$, and $O(k+1)$ at equality. The spectral radius formula therefore gives $r(B)\le R$ if $3^\sigma\ge2$.

For $|\lambda|>R$ under this hypothesis, $B-\lambda I$ is invertible. Compact perturbation implies $W-\lambda I$ is Fredholm of index zero. An eigenfunction of $U$ would satisfy $f(T^k n)=\lambda^k f(n)$. Since $Tn+1\le(3/2)(n+1)$ for every $n\ge1$,
$$
    |\lambda|^k |f(n)| \le \|f\|_X (T^k n)^{\sigma/p}
                    \le \|f\|_X (n+1)^{\sigma/p}R^k .
$$
Taking $k\to\infty$ gives $f=0$. Thus $W-\lambda I$ is injective and its Fredholm index makes it surjective. This proves the ordinary spectral upper bound.

## 2. Two ordinary inverse chains give the full essential disk

For each $k\ge1$ choose a positive $a\in C$ satisfying $4a+1\equiv0\pmod{3^{k+2}}$. Such $a$ can be chosen arbitrarily large in the required component by Kenneth M. Monks’s arithmetic-progression sufficiency theorem. For $C=\mathbb N_{>0}$ a residue class suffices directly. Set
$$
 b_0=2a,\quad b_1=(2a-1)/3,\quad
 u_{i,0}=2b_i,\quad
 u_{i,j}=(2/3)^j(u_{i,0}+1)-1\quad(1\le j\le k).
$$
Both $b_i$ map to $a$ with parities $i$. The $u_{i,0}$ are even and map to $b_i$. Since $u_{0,0}+1=4a+1$ and $u_{1,0}+1=(4a+1)/3$, all the $u_{i,j}$ for $j\ge1$ are odd integers mapping to $u_{i,j-1}$. For fixed $k$ they are positive at large $a$. All displayed vertices belong to $C$.

The affine functions of $a$ defining this finite collection have pairwise distinct slopes. The slopes at $a,b_0,b_1$ are $1,2,2/3$. Those at $u_{0,j},u_{1,j}$ are $4(2/3)^j,(4/3)(2/3)^j$. Their 2-adic valuations distinguish different levels, and their 3-adic valuations distinguish the two entries within a level. Thus a finite set of accidental crossings can be avoided by taking $a$ large. Every vertex of both chains tends to infinity with $a$, so patches for successive $k$ can be chosen with pairwise disjoint supports.

Let $p'$ be the conjugate exponent, including $p'=\infty$ for $p=1$. In the counting-space adjoint, $B^*\delta_x=c_{x\bmod2}\delta_{Tx}$. Define
$$
 v_0=c_0^{-1}\delta_{b_0}-c_1^{-1}\delta_{b_1},\qquad
 v_{j+1}=c_0^{-1}R^{-j}
       (c_0^{-1}\delta_{u_{0,j}}-c_1^{-1}\delta_{u_{1,j}})
       \quad(0\le j\le k).
$$
Then $B^*v_0=0$ and $B^*v_{j+1}=v_j$. The vectors $v_j$ have disjoint supports, $\|v_0\|>0$, and $\|v_{j+1}\|=c_0^{-1}R^{-j}\|v_0\|$. For any complex number $\mu$ with $|\mu|<R$, set $g_k=\sum_{j=0}^{k+1}\mu^j v_j$. Its norm is at least $\|v_0\|$, while
$$
   (B^*-\mu I)g_k=-\mu^{k+2}v_{k+1}.
$$
The relative error tends to zero. The normalized $g_k$ can be chosen with disjoint supports, hence are separated in norm, also when $p'=\infty$. If $B-\bar\mu I$ were Fredholm, its adjoint would be Fredholm. A bounded operator with closed range bounds the distance to its kernel by a fixed constant times the residual; normalized approximate null vectors would therefore approach its finite-dimensional kernel and admit a convergent subsequence. This contradicts norm separation. Compact perturbation preserves the Fredholm set, and the essential spectrum is closed. Consequently the entire closed disk of radius $R$ belongs to the essential spectrum of $U$, for every $\sigma\ge0$.

Equivalently (or by the Calkin spectral radius formula) $\|U^k\|_{\rm ess}\ge R^k$ for every $k$. This proof uses finite trees of positive ordinary integers. The rational numbers $-1,-1/2,-1/4$ behind the congruence serve to select those trees.

## 3. Uniform bounds and strong stability at summable exponents

The same disjoint-column argument gives
$$
   \|U^k\|^p=\sup_{a\in C}\sum_{x\in C:\,T^kx=a}(a/x)^\sigma.
$$
For $\sigma>1$, equation (1) and $(s+t)^\sigma\le 2^{\sigma-1}(s^\sigma+t^\sigma)$ imply
$$
 (a/x)^\sigma
 \le 2^{\sigma-1}\left[ (3^q/2^k)^\sigma
                      + (3/2)^{k\sigma} x^{-\sigma}\right].
$$
Indeed $F/2^k\le(3/2)^q-1\le(3/2)^k$. The first sum over the fiber obeys (2). Each positive integer $x$ occurs at most once in the second. Thus
$$
 \sup_{k\ge0}\|R^{-k}U^k\|^p
  \le 2^{\sigma-1}\left[\sum_{e\ge0}(1+2^e)3^{-\sigma e}
                         +\sum_{n\ge1} n^{-\sigma}\right]<\infty .
$$
For a bounded function $f$, $\|U^kf\|_X\le\|f\|_\infty(\sum n^{-\sigma})^{1/p}$. Since $R>1$, its normalized powers converge to zero in norm. Bounded functions are dense in $X$, and the uniform operator bound extends strong convergence to all $f\in X$. The lower essential norm bound shows the strong limit comes with no decay in operator norm.

## Sources and scope

The disjoint-column identity for composition operators is standard. Leventides and Poulios study iterates on sequence spaces and give a Fibonacci upper bound on inverse fiber sizes. Béhani studies the transfer operator $z^n\mapsto z^{Tn}$ on weighted analytic coefficient spaces for the shortcut map, including hypercyclicity. The rStation paper 47, Theorem 5, treats **unweighted** ordinary shortcut composition, ternary branch-word multiplicities, and the specific ternary algebraic coalescence at $-1/4$. Here those two congruent inverse germs produce separate, arbitrarily long ordinary arms; the carry bound fixes the full disk for a range of polynomial weights. The conclusion does not determine whether every orbit reaches 1.

- Kenneth M. Monks, *The sufficiency of arithmetic progressions for the 3x+1 conjecture*, Proc. Amer. Math. Soc. 134 (2006), 2861–2872, Theorem 1.1. <https://monks.scranton.edu/content/pubs/SufficiencyRev4.pdf>
- J. Leventides and C. Poulios, *Koopman operators and the 3x+1-dynamical system*, §5. <https://arxiv.org/abs/2010.12987>
- V. Béhani, *Linear dynamics of an operator associated to the Collatz map*, Proc. Amer. Math. Soc. 152 (2024). <https://doi.org/10.1090/proc/16627>
- rStation, *Two-Horizon Trajectory Merge Regimes ... and Iterated Composition Norms in the Collatz Map*, Theorem 5, contemporary unrefereed comparison. <https://rstation.ai/problems/collatz/papers/47>
