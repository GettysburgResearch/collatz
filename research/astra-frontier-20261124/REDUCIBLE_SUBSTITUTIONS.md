# Physical completions for every nonidentity binary substitution

**PROPOSED written extension.** Let $\sigma$ be an endomorphism of the free monoid on $\{0,1\}$, different from the identity. Let $s$ be any one-sided infinite fixed word, so that $\sigma(s)$ is infinite and equals $s$. Let $W_0,W_1$ be nonempty finite words of positive accelerated odd Collatz gaps whose rational inverse affine maps have different fixed points. The physical odd 2-adic completion of the concatenated itinerary is rational when $s$ is eventually periodic and transcendental over $\mathbb Q$ otherwise. The new cases include reducible substitutions with unequal letter growth rates and those with a repeated dominant eigenvalue.

The uniform and primitive results used below are MPS-1 through MPS-6 of PR190, head ba58227c5a047ff3859a148a5fdaac4fd1451e4c. Its physical affine reduction, formal transcendence and weighted leading-term arguments are the dependencies. The new argument treats reducible incidence matrices. An infinite word with finitely many copies of either letter is eventually periodic, so both letters occur infinitely often in the rest of the proof. [Uniform source](https://github.com/GettysburgResearch/collatz/blob/ba58227c5a047ff3859a148a5fdaac4fd1451e4c/research/mahler-physical-scripts-20261124/README.md) · [Primitive source](https://github.com/GettysburgResearch/collatz/blob/ba58227c5a047ff3859a148a5fdaac4fd1451e4c/research/mahler-physical-scripts-20261124/PRIMITIVE_MORPHISMS.md)

## 1. Classification and recurrence at the zeros

If both images are empty, there is no infinite fixed word. If exactly one is empty, an infinite image consists of copies of the single surviving image and is periodic. Thus an aperiodic fixed word requires both images to be nonempty.

An irreducible nonprimitive binary incidence matrix has zero diagonal. Its two images begin with the opposite letter, making a fixed first letter impossible. A diagonal incidence matrix sends each letter to a positive power of itself. If a fixed word contains a letter sent to a power of length at least two, consider the first occurrence of any such letter. All earlier letters are fixed individually. Iteration fills the entire remaining suffix with that one letter. The identity is the only remaining diagonal substitution admitting an aperiodic fixed word.

It remains, up to exchanging letter names, to consider

$$
 \sigma(0)=v,\qquad |v|_0=a,\quad |v|_1=b>0,\qquad \sigma(1)=1^d,\quad d\ge1.
$$

The existence of infinitely many zeros requires $a\ge1$. Index the zeros of $s$ by $i=0,1,\ldots$ and let $k_i$ count the ones strictly before zero $i$. Write $h_t$ for the number of ones preceding zero $t$ in $v$, where $0\le t<a$. Grouping the fixed word into images gives

$$
 k_{ai+t}=b i+d k_i+h_t. \tag{1}
$$

At $i=t=0$ this forces $h_0=0$, and also $k_0=0$ if $d>1$. If $a=1$, taking $i=1,t=0$ gives $k_1=b+d k_1$, which is impossible. Hence $a\ge2$.

Let $x,y$ be the positive rational slopes of the two physical inverse maps, with $v_2(x),v_2(y)>0$. Use the series

$$
 V(X,Y)=G_0(X,Y)=\sum_{i\ge0} X^iY^{k_i}\in\mathbb Z[Y][[X]].
$$

The physical reduction and the telescope $(1-X)G_0+(1-Y)G_1=1$ make the completion an invertible rational affine function of $V(x,y)$. Both denominators in the telescope are nonzero because the slopes have positive 2-adic valuation. The transcendence of $V$ over $\mathbb Q(X,Y)$ follows from that of $G_1$ in MPS-3 using the same telescope. Equivalently, $V(z,z)$ is the indicator series of the zeros of $s$. By the finite-alphabet recurrence argument it is transcendental. A purported polynomial relation can be divided by its largest coefficientwise common power of $X-Y$ before restricting to the diagonal.

Equation (1) gives the exact functional equation

$$
 V(X,Y)=P(X,Y)V(X^aY^b,Y^d),\qquad
 P(X,Y)=\sum_{t=0}^{a-1}X^tY^{h_t}. \tag{2}
$$

Start the monomial iteration $x_{n+1}=x_n^a y_n^b,\ y_{n+1}=y_n^d$ at $(x,y)$. The value $P(x_n,y_n)$ is a nonzero positive rational and a 2-adic unit, since $h_0=0$. Equation (2) propagates a hypothetical algebraic $B_0=V(x,y)$ to $B_n=V(x_n,y_n)$ in the one number field $K=\mathbb Q(B_0)\subseteq\mathbb Q_2$ by $B_{n+1}=B_n/P(x_n,y_n)$.

## 2. Growth of the monomial points

Write $u=v_2(x)>0,\ v_*=v_2(y)>0$, and let $h$ denote absolute logarithmic Weil height. Set

$$
 L_n=\sum_{j=0}^{n-1}a^{n-1-j}d^j,\qquad
 x_n=x^{a^n}y^{bL_n},\quad y_n=y^{d^n}.
$$

When $a\ne d$, $L_n=(a^n-d^n)/(a-d)$. When $a=d$ and $n\ge1$, $L_n=na^{n-1}$. Define $T_n=a^n+bL_n+d^n$. Then $h(x_n)+h(y_n)=O(T_n)$ and (2) gives $h(B_{n+1})\le h(B_n)+O(T_n)$. Since $a\ge2$, the formulas give $\sum_{j<n}T_j=O(T_n)$, including when $a=d$. Thus $h(B_n)=O(T_n)$, with constants independent of any auxiliary polynomial. Every nonzero $\eta\in K$ obeys $v_2(\eta)\log 2\le[K:\mathbb Q]h(\eta)$ in the chosen embedding.

If $d>a$, the triangular incidence matrix has positive right Perron vector $w=(b/(d-a),1)$ and secondary eigenvalue $a$. Its valuation vector satisfies

$$
 (v_2(x_n),v_2(y_n))= v_* d^n w+O(a^n).
$$

These are exactly the growth hypotheses of MPS-5, §§3–6. Normalize $w$ to coprime positive integers $(p,q)$ and absorb its scale in $C>0$. Then $y_n^p/x_n^q=(y^p/x^q)^{a^n}$. If the initial ratio differs from 1, the ratios are distinct rationals of height $O(a^n)$. In an integer auxiliary series of high total order for $G_1$, the least $pi+qj$ homogeneous part is a monomial times a polynomial in that ratio. It is eventually nonzero and its valuation is at most $C(pi+qj)d^n+O_R(a^n)$. All higher weights have strictly larger valuation eventually. If the ratio is 1, the orbit lies on $(x_n,y_n)=(z_n^p,z_n^q)$ with rational $z_n$ by Bézout. MPS-6 gives transcendence of this one-variable specialization of $G_1$. In either case the auxiliary height contradiction of MPS-5 applies. Heights of $G_1(x_n,y_n)$ also follow from those of $B_n$ by the telescope. The argument uses the displayed explicit growth estimates for this triangular matrix.

## 3. A parameter that grows more slowly

Suppose $a>d\ge2$, or $a=d\ge2$. Then

$$
 v_2(x_n)=ua^n+v_* bL_n \asymp T_n,\qquad h(y_n)=d^n h(y)=o(T_n).
$$

The second relation uses $b>0$ in the repeated-eigenvalue case. Fix $m\ge1$, and put $D=(m+1)^2-1$. Over the coefficient field $\mathbb Q(Y)$, choose a nonzero polynomial in $X,W$ of degree at most $m$ in each such that the first $D$ coefficients in $X$ of its value at $W=V(X,Y)$ vanish. These are $D$ homogeneous linear equations in $(m+1)^2$ unknowns over that field. Clearing denominators yields $R\in\mathbb Z[X,Y,W]$. Its finite degree in $Y$ can depend arbitrarily on $m$. The formal transcendence of $V$ gives

$$
 F(X,Y)=R(X,Y,V(X,Y))=\sum_{j\ge t}X^j f_j(Y),\quad
 t\ge D,\quad 0\ne f_t\in\mathbb Z[Y].
$$

Each coefficient is a polynomial in $Y$ by the expression for $V$ with a single monomial at each $X$-degree.

The positive rationals $y_n=y^{d^n}$ are distinct because $v_2(y)>0$ and $d\ge2$. Thus $f_t(y_n)\ne0$ eventually. Its valuation is at most $O_R(1+h(y_n))=o(T_n)$ by the rational height bound. For fixed $R$ and sufficiently large $n$, this is strictly less than $v_2(x_n)$. Higher $X$-terms have valuation at least $(t+1)v_2(x_n)$ by integrality. Therefore

$$
 0\ne R(x_n,y_n,B_n),\qquad v_2(R(x_n,y_n,B_n))\ge D v_2(x_n).
$$

On the other hand polynomial evaluation gives

$$
 h(R(x_n,y_n,B_n))
 \le m(h(x_n)+h(B_n))+\deg_Y(R)\,h(y_n)+O_R(1).
$$

First let $n\to\infty$ with $m,R$ fixed. After division by $T_n$ the term containing $\deg_Y R$ vanishes. The product formula gives $cD\le C'm$ with $c>0,C'$ independent of $m$, an impossibility for large $m$. This proves transcendence when the slower parameter is moving, including the repeated-eigenvalue case.

## 4. The fixed-parameter case

It remains to treat $a\ge2,\ d=1$. Define

$$
 S(Z)=V(Z,y)=\sum_{i\ge0}y^{k_i}Z^i.
$$

We prove that $S$ is transcendental over $\mathbb Q(Z)$ for every positive rational $y\ne1$. Take the positive real algebraic root $\theta=y^{1/(a-1)}$ to rescale the formal coefficients. Set

$$
 U(Z)=S(\theta^{-b}Z)=\sum_{i\ge0}u_iZ^i,\qquad u_i=\theta^{(a-1)k_i-bi}.
$$

By (1),

$$
 u_{ai+t}=c_tu_i,\quad c_t=\theta^{(a-1)h_t-bt},\quad c_0=1,\quad
 P_*(Z)=\sum_{t=0}^{a-1}c_tZ^t,\quad U(Z)=P_*(Z)U(Z^a). \tag{3}
$$

Here $\deg P_*=a-1$, and $u_i>0$ at the chosen real embedding. If $S$ is algebraic, $U$ is algebraic over $\mathbb Q(\theta)(Z)$. Its coefficients then satisfy a nonzero polynomial recurrence $\sum_{j=0}^r p_j(n)u_{n+j}=0$ for all large $n$, by differentiation in a finite separable extension and coefficient extraction as in MPS-3. For each fixed $i\ge0$ choose $\ell$ with $i+r<a^\ell$. Iterating (3), allowing leading zeros because $c_0=1$, gives

$$
 u_{a^\ell h+i+j}=u_h u_{i+j}/u_0\qquad(0\le j\le r).
$$

Use the recurrence at $n=a^\ell h+i$ and divide by $u_h/u_0\ne0$. The polynomial $\sum_j p_j(a^\ell h+i)u_{i+j}$ vanishes for infinitely many $h$ and hence identically. Write $E=\max_j\deg p_j$. Comparing coefficients of $h^E$ and canceling $a^{\ell E}$ yields

$$
 \sum_{j=0}^r [T^E]p_j(T)\,u_{i+j}=0\qquad\text{for every }i\ge0.
$$

The coefficients are constant and at least one is nonzero. Thus $U$ is a nonzero rational generating function.

In a reduced fraction $U=A/B$, (3) gives $A(Z)B(Z^a)=P_*(Z)B(Z)A(Z^a)$. The polynomials $A(Z^a),B(Z^a)$ are coprime by a substituted Bézout identity. Hence $A(Z^a)\mid A(Z)$, so $A$ is constant. Taking degrees gives $a\deg B=(a-1)+\deg B$, whence $\deg B=1$. It follows that $u_i=u_0\gamma^i$ with $\gamma=u_1/u_0>0$. The equality $u_a=u_1$ forces $\gamma^{a-1}=1$ and hence $\gamma=1$. Since $\theta$ is positive and different from 1, the integers $(a-1)k_i-bi$ are all equal. Every pair of consecutive zeros has exactly $b/(a-1)$ intervening ones. This makes $s$ eventually periodic, the required contradiction.

The transcendental formal series $S$ converges on the 2-adic open unit disk since $v_2(y)>0$ and $k_i\ge0$. Here $B_n=S(x_n)$, $v_2(x_n)\asymp a^n$ and $h(x_n)+h(B_n)=O(a^n)$. Pick $0\ne R(Z,W)\in\mathbb Z[Z,W]$ of degree at most $m$ in each variable so that $R(Z,S(Z))$ has order at least $(m+1)^2-1$. The series is nonzero. Its first nonzero term dominates at $x_n\to0$ for fixed $R$, giving valuation at least $((m+1)^2-1)v_2(x_n)+O_R(1)$. The height is at most $Cma^n+O_R(1)$. The product formula again gives a contradiction for large $m$.

## 5. Scope and examples

In the eventually periodic case, compose the finite inverse prefix with the rational fixed point of the period. Its inverse slope has positive 2-adic valuation, giving existence and uniqueness. The distinct-fixed-point hypothesis is essential. With a common fixed point every directive has the same rational completion. Each actual odd rational source following the given infinite itinerary would equal the completion in $\mathbb Q_2$. Finite additions or shifts of the physical itinerary preserve the rational/transcendental classification because each finite prefix acts by an invertible rational affine map.

Two newly treated examples are $\sigma(0)=001,\ \sigma(1)=1$ and $\sigma(0)=001,\ \sigma(1)=11$. In each prolongable fixed word there are infinitely many zeros and arbitrarily long runs of ones between consecutive zeros. Indeed $\sigma^r(0)$ ends in at least $r$ ones by induction. The prefix $00$ of $\sigma(0)$ places $\sigma^r(0)\sigma^r(0)$ in the fixed word, so each such suffix is followed by a zero. An eventually periodic word having infinitely many zeros has bounded zero spacing.

The identity substitution fixes every binary word. The theorem supplies no mechanism assigning a nonidentity binary substitution to every exceptional ordinary Collatz itinerary. Binary codings of substitutions on larger alphabets can also fall outside its scope. The Collatz conjecture remains open.


## 6. Physical output words and arbitrary block boundaries

**Corollary.** Let $s$ be a fixed one-sided word of a nonidentity binary endomorphism. Replace each of its letters by a fixed finite word of positive gaps, and suppose the resulting gap output is infinite. Its odd 2-adic physical completion is rational precisely when the *output gap word* is eventually periodic. Otherwise the completion is transcendental. The same dichotomy holds for arbitrary finite output blocks of shortcut parity bits, using the source in $\mathbb Z_2$. In both cases finite deletion or prepending of individual output symbols is allowed, including cuts inside a substitution block.

If one output block is empty, the entire infinite output is a repetition of the other block. For two nonempty gap blocks with a common inverse fixed point, that odd point follows both periodic gap itineraries. The uniqueness of the successive forward gap valuations makes their infinite repetitions identical. Both block lengths are periods of this common infinite word and each block is its prefix. Successively removing such prefixes leaves the same periodic infinite word. Every concatenation therefore produces that word, even for a completely arbitrary directive. For distinct fixed points apply the theorem above. If the directive itself is eventually periodic its image is eventually periodic. In every case an eventually periodic output has a rational completion by the affine period formula.

For shortcut bits the two single-bit inverse branches are $J_0(t)=2t$ and $J_1(t)=(2t-1)/3$. They send every $t\in\mathbb Z_2$ to the required first parity and undo exactly one shortcut step. Both have positive rational slopes with positive 2-adic valuation. Their finite products meet all the algebraic and analytic slope hypotheses used above, with the shared fixed-point argument now using uniqueness of the shortcut parity. Each finite inverse prefix in either model is an invertible rational affine transformation, which proves the claims about prepending and deletion.

A related preprint claims that under an ordinary coded-frequency hypothesis the parity of a positive rational shortcut orbit is eventually periodic throughout a larger class of exponentially growing morphic presentations. Its hypothesis is a coded parity frequency, and its conclusion concerns positive rational inputs. The result above gives a transcendence statement for the unique 2-adic source and works with a binary presentation and two output blocks. Its proof and the six source verdicts do not rely on the preprint. [Exponentially growing morphic parity with a frequency](https://rstation.ai/problems/collatz/papers/68)

