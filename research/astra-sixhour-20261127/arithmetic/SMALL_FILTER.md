# A small rank projection preserves the complete odd denominator

**Written theorem, including a positive version.** Suppose an actual rational cycle has the bounded-branch rank representation
$$
U_{r+p}=2U_r,\qquad c_{r+p}=2c_r,\qquad U_{r+h}=3U_r+c_r,\qquad
4s\le U_r<8s,\quad c_r\in\{1,2,4\}\quad(0\le r<p).
$$
Here $s$ is its real minimum, $U_r=2^{2-k_r}x_r$, and every $U_r$ has the same odd reduced denominator $q$. For a positive odd-denominator rational, define its lowbit as $2^{v_2(U_r)}$; then $c_r$ really is its lowbit. Extend the arrays to nonnegative ranks as displayed. Take $1\le h/p\le2$. Fix any $L\ge1$, write $m_j=\lfloor jh/p\rfloor$ and $t_j=jh-m_jp$.

There is a single integer filter $b_0,\ldots,b_L$ depending only on $h,p,L$, with $|b_j|\le3$, for which
$$
 W_r=\sum_{j=0}^L b_j U_{r+t_j},\qquad
 2^{m_L}W_r-U_r\in\mathbb Z,\qquad
 |W_r-2^{-m_L}U_r|\le4L
 \quad(0\le r<p).
$$
The reduced denominator of **each individual** $W_r$ equals $q$. A second common filter with $|b_j|\le6$ gives all the same assertions with $0\le W_r-2^{-m_L}U_r\le8L$. Taking $L=\max(1,\lceil\log_2(8s)\rceil)$ makes every positive projection at most $1+8L$. Both results are independent of how often the original bands change. The input includes the unrestricted layer choices in the stated representation. [Physical rank representation](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-global-closure-20261124/round13/cycle/README.md)

**Proof.** Start $g_0=2^{-m_L}$. Write $g_j=n_j/2^{m_L-m_j}$ with $n_j$ an integer, and choose $b_j$ in the class $n_j(2^{m_L-m_j})^{-1}\bmod3$. Use a nearest representative to $g_j$ for the signed version, or the largest representative at most $g_j$ for the positive version. For $\beta_j=m_{j+1}-m_j\in\{1,2\}$ put
$$
 g_{j+1}=\frac{2^{\beta_j}}3(g_j-b_j).
$$
Its denominator divides $2^{m_L-m_{j+1}}$ by construction. In the signed version $|g_{j+1}|\le2$ and $|g_j-b_j|\le3/2$, giving $|b_j|\le3$. In the positive version $0\le g_{j+1}<4$ and $0\le g_j-b_j<3$, so the displayed bound six is ample. At $j=L$ set $b_L=g_L$, an integer. Telescoping gives the exact identity
$$1=\sum_{j=0}^L b_j\,2^{m_L-m_j}3^j.$$

The lifted rank relation, at every $r$, gives $u_j=U_{r+t_j}$ and $v_j=c_{r+t_j}$ satisfying $2^{\beta_j}u_{j+1}=3u_j+v_j$. Hence
$$W_r=g_0 U_r+\sum_{j<L}\frac{g_j-b_j}{3}v_j.$$
Here $0<v_j\le8$ as $0\le r+t_j<2p$. The asserted real estimates follow. Moreover $2^{m_L}(g_j-b_j)/3$ is an integer for every $j$ by the ternary choice of $b_j$. This proves the exact integral residual. An integer translate of $U_r$ retains denominator $q$, and $W_r$ already has odd denominator as a sum of odd-denominator rationals. Multiplication by $2^{m_L}$ therefore gives precisely the same denominator at $W_r$. This proves the result.

The integer residual also gives a pointwise $q=1$ test. In the positive version an ordinary cycle would supply a positive integer $W_r\le1+8L$ at every rank. For all sufficiently large bounded least-disagreement candidates these values are below the least bad integer, so they all reach 1. The Lean module proves the arbitrary-length rational telescoping identity, its cleared integer residual, and exact reduced-denominator preservation under a coprime dilation. The choice and real bounds of the filter digits are given by the written argument. [RankFilter.lean](RankFilter.lean)

## Ordinary branch comparison

Write $d=h-p$ and $P(c)_r=\sum_jb_j c_{r+t_j}$. The exact transferred equation is
$$2W_{r+d}=3W_r+P(c)_r.$$
An actual positive ordinary projected trajectory on this prescribed normalized clock would require $P(c)_r=2^{v_2(W_r)}$ at every rank, together with ordinary integrality. Then taking odd parts along the positive integral trajectory gives physical transitions, and the prescribed full halving count $h$ rules out a trivial odd cycle for $h<2p$. Consequently a globally locked positive filter of the displayed small height on a sufficiently large bounded ordinary candidate would contradict its least bad minimum. To see the halving count, write $W_r=2^{j_r}w_r$ in one circular representative, with odd $w_r$. After restoring the wrapped power of two, the exponents are $\beta(r)+j_{r+d\bmod p}-j_r$, which telescope to $h$. They are positive by the odd edge equation. This is a conditional implication.

There is a simple obstacle to a uniform directed-word interpretation of the filter's small homogeneous coefficient. On any fixed ordinary forward shortcut script of length $a$ with $b$ odd inputs its coefficient is $3^b/2^a$. Equality with $2^{-m_L}$ forces $b=0$ and $a=m_L$, by unique factorization. The input of such a script is divisible by $2^{m_L}$, whereas ordinary base-band $U_r$ has valuation at most two. This comparison concerns a single forward script with the same homogeneous coefficient as a formal identity in the source. It does not exclude a contextual path at an individual numerical state or an undirected comparison.

Testing literal controls shows why integrality alone does not establish branch locking. With the positive filter at $L=12$, the genuine ordinary fixed point represented by $p=1,h=2,U_0=4$ gives $W_0=24$ and filtered correction $24$, whereas its lowbit is $8$. For the $5,8,41$-phase rational controls with denominators $13,1631,44835377399$, respectively, exactly $2,2,11$ ranks satisfy the required equality. Every rank retains the corresponding full denominator. The filtered arrays for the last two controls also lose their sorted order. The ordinary fixed point is outside the nontrivial bounded branch. [Exact checker](check_small_filter.py) · [Control output](../../../reports/astra-sixhour-20261127/arithmetic/small_filter.json)

For comparison, direct differences at two macroscopic rank displacements already have physical good labels throughout any bounded ordinary counterexample. Indeed
$$
 U_{r+d}-U_r=(U_r+c_r)/2,\qquad
 2U_r-U_{r+d}=(U_r-c_r)/2.
$$
Taking odd parts gives those of $x_r+1$ and $x_r-1$; the bounded-branch neighbor theorem makes both good. The full displacement $U_{r+p}-U_r=U_r$ is bad. The first displacement with a bad positive difference between these endpoints has not been classified. [Ordinary neighbor theorem](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md)
