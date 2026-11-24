# A sub-square-root deadline and a continued-fraction restriction

**PROPOSED, with a finite integer certificate.** In either alternative of the ordinary least-disagreement theorem in [the preceding proof](README.md), the original orbit crosses $2n$ or enters the specified cycle within $O(q^{49/100})$ shortcut steps. In the bounded cycle alternative, write $h,p$ for its least shortcut period and number of odd inputs. For all sufficiently large $q$, the reduced fraction $h/p$ must be a continued-fraction convergent **above** $\log_2 3$. It satisfies the stronger quantitative estimate
$$
  0<h/p-\log_2 3\ll p^{-100/49}.
$$
These are restrictions on a putative ordinary cycle. They do not exclude that cycle, and the first-crossing branch remains open.

## What the actual bounded excursion allows

Retain the preceding proof's $n=3q$, $s=(n-1)/2$. Count the odd sites within completed singleton runs whose next run entry is still at most $2n$. Every such odd site $x$ satisfies
$$
 s\le x\le(8n-1)/3.
$$
The lower bound holds at the run entry, and the consecutive odd steps rise. The last odd site of the run maps to $2y'$, where $y'\le 2n$ is its next entry. Thus $x_{\rm last}=(4y'-1)/3$. Include the bounded entry at the end of the last run when counting suffixes. This bound does not extend across an unbounded final crossing run.

The odd-to-odd steps along this part of the path have the form
$$
 x_{i+1}=(3x_i+1)/2^{1+e_i},\qquad e_i\in\{0,1\}.
$$
Put $A=\log_2(3/2)$, $H_i=\log_2(x_i/s)$, $D_i=\sum_{j<i}e_j$. On a block of $L=512$ steps,
$$
 H_i=H_0+iA-D_i+E_i,\qquad
 0\le E_i=\sum_{j<i}\log_2(1+1/(3x_j))\le L/s .
$$
We may assume $n\ge10^6$, absorbing smaller $n$ into an absolute constant using the preceding finite deadline. Then $0\le H_i<2.42$, since the ratio of the two height bounds is less than $267/50$, and $267^{100}<50^{100}2^{242}$.

Set $A_0=58496/100000$, so that $0<A-A_0<10^{-5}$ by comparing $3^{100000}$ with $2^{158496}$ and $2^{158497}$. Choose $B=(\lceil100H_0\rceil+1)/100$. This belongs to the tested grid $0,.01,\ldots,2.44$. For every $i\le L$ we have
$$
 0\le B+iA_0-D_i\le 2.44.
$$
Indeed $B-H_0\ge.01$ and $L(10^{-5}+1/s)<.01$. The upper bound follows from $B-H_0<.02$, $A_0\le A$ and $E_i\ge0$. All logarithms have now been replaced by rational inequalities in a finite path count.

## The integer certificate and original-source bound

For each grid start $B$ initialize $d_0(0)=1$ and all other initial entries to zero. At time $i$ keep $d_i(j)=d_{i-1}(j)+d_{i-1}(j-1)$ precisely for integers $j$ such that $0\le B+iA_0-j\le2.44$, setting all other entries to zero. The sum of all terminal entries across the 245 starting bins is the upper bound $C$ printed in [the exact replay](strip_controls.json). In integer arithmetic it satisfies $C^{100}<3^{49L}$. [Portable certificate](check_strip.py)

Every length-$k$ suffix of the actual bounded odd path therefore has at most $C^{\lfloor k/L\rfloor}2^{k\bmod L}=O(3^{49k/100})$ possible binary words across all starts. The starting bin may change between blocks. Counting every choice independently provides a valid upper bound. A single word determines its terminal ordinary residue modulo $3^k$, by iterating $2^{1+e_i}x_{i+1}=3x_i+1$. This holds when the earliest sampled odd site is internal to a run as well.

Set $k=\lceil\log_3(2n+1)\rceil$. Apart from at most $k$ initial run entries, every bounded entry has at least $k$ preceding odd steps in the same bounded segment. There is at most one positive interior integer in each of these residues. The injectivity/nonrepetition argument in the preceding proof now gives the $O(q^{49/100})$ run count. Each pre-crossing interior run costs at most six physical clocks and the last crossing run costs $O(\log q)$, which gives the stated shortcut clock deadline. The block size can make the absolute bound very large.

## The exceptional cycle

On the bounded cycle, summing the logarithm of the exact odd-step identity gives
$$
 0< h/p-\log_2 3
   ={1\over p}\sum_{x\text{ odd in the cycle}}\log_2(1+1/(3x))
   <1/s.
$$
The period bound just proved gives $p\ll s^{49/100}$, hence $1/s\ll p^{-100/49}$. Also $p^2/s\ll s^{-1/50}$. For sufficiently large $s$, the error is strictly less than $1/(2p^2)$, and therefore less than $1/(2b^2)$ for the reduced denominator $b\le p$. Legendre's criterion supplies the claimed upper convergent. If such cycles existed with unbounded $q$, the reduced denominators would be unbounded because $\log_2 3$ is irrational. This would force its irrationality exponent to be at least $100/49$. The argument supplies no contradictory upper bound on that exponent. [Legendre's criterion and proof, Theorem 2.3 in Vaughan's notes](https://personal.science.psu.edu/rcv4/677C02.pdf)

The seven Lean theorems in the preceding proof concern the ordinary edges and finite escape logic. The height enclosure, use of the finite word count, and continued-fraction application here are written proofs. Both Python modes independently executed the same integer recurrence and printed identical output.
