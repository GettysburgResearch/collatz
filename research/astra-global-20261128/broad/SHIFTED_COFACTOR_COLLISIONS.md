# A repeated shifted cofactor forces an actual low state

**PROPOSED, written proof.** For an ordinary positive shortcut state $x$, let $Z(x)=2x+1$ and
$$
 K(x)=\frac{Z(x)}{3^{v_3(Z(x))}}.
$$
This positive odd integer is prime to 3. The affine normalization is useful because its correction is the same on both branches:
$$
 2Z(Tx)=3^{x\bmod2}Z(x)+1. \tag{1}
$$

## 1. One physical path

Suppose $K(x_a)=K(x_b)$ on a positive orbit, with $r=b-a\ge1$ and input floor $m=\min_{a\le i<b}x_i$. There are absolute constants $r_0,C$ such that
$$
 2m+1<r^{5.116201}\quad(r\ge r_0),\qquad
 2m+1\le C r^{5.116201}\quad(r\ge1). \tag{2}
$$
Consequently, along any family of starting integers $n\to\infty$, a cofactor collision anywhere in the first $o(n^{1/5.116201})$ steps forces a visit below $n$ by the later collision time. Equivalently, every prefix that stays at or above $n$ on that horizon has pairwise distinct labels. This is a descent criterion conditional on an actual collision. The proof does not imply one occurs.

Indeed let $s$ count the odd inputs in the interval and let $d=v_3(Z(x_b))-v_3(Z(x_a))$. The collision gives $Z(x_b)/Z(x_a)=3^d$. Multiplication of (1) over the interval gives, with $k=s-d\in\mathbb Z$,
$$
 \Lambda=r\log2-k\log3
 =\sum_{i=a}^{b-1}\log\left(1+\frac1{3^{x_i\bmod2}Z(x_i)}\right),\qquad
 0<\Lambda<\frac r{2m+1}. \tag{3}
$$
These logs are natural. In particular $0<k<r$ because $m\ge1$, $\log2>1/3$ and $\log2<\log3$. Bondareva, Luchin and Salikhov's Theorem 1 states that for integers $h_1,h_2,h$ and $H=\max(|h_1|,|h_2|)$ sufficiently large,
$$
 |h_1\log2+h_2\log3+h|>H^{-4.116201}.
$$
Apply it with $(h_1,h_2,h)=(r,-k,0)$, so $H=r$. This gives the first assertion in (2). For $r<r_0$ there are finitely many possible pairs $(r,k)$ and each nonzero form has a positive absolute value, so one common constant suffices. No numerical value for the source's onset is claimed. [Bondareva, Luchin and Salikhov, *Chebyshevskii Sbornik* 19 (2018), Theorem 1, printed p. 18](https://www.mathnet.ru/eng/cheb619).

In particular this concerns the original state at a specific input time, not simply a small coefficient in a parity expression. The additive one in (1) prevents a zero logarithmic form on every nonempty single path.

## 2. Two paths reaching one common endpoint

Let $x,z$ reach the same ordinary $y$ after $r_1,r_2$ steps respectively. Both paths have input floor at least $m\ge1$. Let $s_1,s_2$ count their odd inputs, and put $R=\max(r_1,r_2)\ge1$. If $K(x)=K(z)$, put $d=v_3(Z(z))-v_3(Z(x))$. Either
$$
 r_1=r_2,\qquad s_1+v_3(Z(x))=s_2+v_3(Z(z)), \tag{4}
$$
or $2m+1\le C R^{5.116201}$ with an absolute constant. On the nonzero-form alternative the multiplicative constant can be taken to be one for all sufficiently large $R$.

To prove this, let $P_1,P_2$ denote the products of the correction factors in (3) for the two paths; an empty product is one. From the common endpoint,
$$
 \Lambda=(r_1-r_2)\log2-(s_1-s_2-d)\log3=\log P_1-\log P_2,\qquad
 |\Lambda|< R/(2m+1).
$$
Set $k=s_1-s_2-d$ and $j=r_1-r_2$. Then $|k|\log3\le |j|\log2+R/3<R\log3$, so $\max(|j|,|k|)\le R$. If the form vanishes, multiplicative independence of 2 and 3 gives $j=k=0$, exactly (4). Otherwise the same external theorem gives $|\Lambda|>R^{-4.116201}$ when the coefficient height is large. The finite possibilities at bounded coefficient height have a fixed positive lower bound and satisfy this weaker estimate once $R$ is sufficiently large. This proves the claim.

Thus short high paths to one endpoint have disjoint sets of shared cofactor labels across different depths. At a fixed depth $r$, every fiber at a given label has at most $r+1$ distinct ordinary sources under the high-floor hypothesis that excludes the second alternative. Condition (4) fixes $s+v_3(Z(x))$ throughout such a fiber; for each $s=0,\ldots,r$ the label then determines $Z(x)$ uniquely.

Same-depth multiplicity is real. Identity (1) also gives $4T(x)+1=3^{x\bmod2}Z(x)$, hence $K(x)$ equals the part of $4T(x)+1$ prime to three. All immediate ordinary parents of the same endpoint therefore share a label. At endpoint $2$, its positive parents are $1$ and $4$, and both have label $1$. Arbitrarily large such sibling pairs are $x$ and $3x+1$ for positive odd $x$, with common image $(3x+1)/2$.

## 3. Relation to the two-run endpoint estimate

For the earlier shifted observation $x+1$, an analogous correction occurs only on even inputs. When the initial and terminal odd cofactors agree, the logarithmic form in [two-run transport](TWO_RUN_TRANSPORT.md) is again a homogeneous combination of $\log2$ and $\log3$. If the gap has $h\ge1$ even inputs, and the least shifted input at those evens is $m'$, then $0<\Lambda<h/m'$. With coefficient height $H_*=\max(r+g',g+s)$, the same primary theorem yields $m'<hH_*^{4.116201}$ for $H_*$ sufficiently large. Thus a return from one large Mersenne input to another on a subexponential-in-bit-length clock must pass below the original input when the horizon grows slower than every fixed exponential in that bit length. The $Z=2x+1$ normalization in (1) provides the single form (3) without selecting runs or omitting homogeneous segments.
