# A forced ordinary excursion from the least bad multiple

**PROPOSED.** If a positive Collatz counterexample exists, choose the least positive odd tripling disagreement $q$ for the basin of 1 and set $n=3q$. An actual bad trajectory then has one of the following behaviors.

* It crosses $2n$ after a sequence of odd runs separated by exactly one even input. The sequence starts at $n$, or, in one specified case, at the bad odd number $(n-1)/2$ whose trajectory meets that of $n$.
* $q\equiv1\pmod {12}$, and $(n-1)/2$ itself is the minimum of a nontrivial positive cycle. The whole cycle has exactly one even input after each maximal odd run. Every odd run has length at most five. Every entry to an odd run is at most $2n$.

The crossing or the first repetition occurs in $O(q^\gamma)$ odd runs, with $\gamma=\log_3\lambda=0.61529868\ldots$, where $\lambda>1$ solves $\lambda^5=\lambda^4+\lambda^3+\lambda^2+\lambda+1$. In the first alternative the original orbit of $n$ also takes a value greater than $2n$. The count is per supplied ordinary source. The original orbit crosses, or enters the specified cycle, within $O(q^\gamma)$ shortcut clocks. The theorem forces growth on a hypothetical bad branch. It does not make that growth contradictory.

Use $T(2u)=u, T(2u+1)=3u+2$. Write $C(x)$ for reaching 1 and $x\sim z$ for a common positive forward value, possibly at different clocks. We use exactly the conclusions that $C(x)$ for all $0<x\le q$, that $n=3q$ is bad, and that all positive multiples of three strictly below $n$ are good. These are proved in PR192, head 26f070c38ad9edd21ed7dac6efaab6554550c2a3, `research/astra-minimum-source-20261124/minimal/MinimumFailure.lean`. Its two-run continuation is in `second/README.md` at the same head. No predecessor-density, mixing or source-randomness input is needed.

## The physical edges

For odd $x>1$ write $x+1=2^m a$, $a$ odd, and $R=3^m a$. Its first $m$ inputs are odd and $T^m x=R-1$. There are only two exits.

* If $R\equiv1\pmod4$, then $x\sim(x-1)/2$. Write $Y=R/3\equiv3\pmod4$. The two paths reach $3Y-1,Y-1$ after $m,m-1$ steps. Two more on each reach $(3Y-1)/4$.
* If $R\equiv3\pmod4$, then $x\sim2x+1$, by the previous comparison on $2x+1$, whose run has length $m+1$. The next odd state is
  $$
  F(x)=T^{m+1}x=(3^m a-1)/2\equiv1\pmod6.
  $$
  This run has exactly one even input after its maximal string of odd inputs. Call it a singleton exit.

At an odd bad $x=6u+1\le2n$, $u>0$ since 1 is good, and $3u=(x-1)/2<n$ is good. The first exit is impossible. The second makes $2x+1$ a bad multiple of three, giving $2x+1\ge n$. Thus every such interior point has a forced singleton exit and is at least $(n-1)/2$. Equality at $x=2n+1$ in the next band cannot be absorbed into this rule, because its shadow equals the original bad multiple $n$.

## The first run and reversal

If $n$ starts with a singleton exit, start the chain at $y_0=n$. Otherwise $s=(n-1)/2\sim n$ is bad. If $n\equiv1\pmod4$, its positive half $(n-1)/4<q$ is good, a contradiction. Hence $n\equiv3\pmod4$, making $s$ an odd $1\bmod6$ bad state. Write $n=3^h w$, $3\nmid w$. The odd number $z=2^h w-1$ reaches $n-1$ after $h$ steps, hence is bad. We have $z<n$, so $3\nmid z$. Since $z+1$ is a ternary unit, $z\equiv1\pmod3$. Its first odd run has length exactly $h$, with exit parameter $3^h w=n\equiv3\pmod4$. Thus $2z+1$ is a bad multiple of three. For $h\ge2$,
$$
2z+1=2(2/3)^h n-1<n,
$$
which is impossible. Therefore $h=1$, $z=2q-1\equiv1\pmod3$, and $n\equiv3\pmod4$ yields $q\equiv1\pmod{12}$. On this surviving branch start at $y_0=s$.

In either chain every input satisfies $3\nmid y_i+1$. On a singleton edge the output determines its input uniquely because
$$
 m=v_3(2y_{i+1}+1),\qquad
 y_i=2^m(2y_{i+1}+1)/3^m-1.
$$
A repetition $y_i=y_j$, $i<j$, rewinds to $y_0=y_{j-i}$. From $y_0=n\equiv0\pmod3$ this is impossible, since all later sites equal 1 modulo three. From $y_0=s$ it means $s$ itself is periodic. Every interior site is at least $s$, and the physical path from one odd-run entry strictly rises through consecutive odd inputs before its single halving. Therefore $s$ is the minimum of that physical cycle.

There are finitely many interior integers, so a first crossing of $2n$ or a repetition must occur. In the recentered case, write $n+1=2^m a$. Since $s$ is odd, $m\ge2$. Its first run has length $m-1$, and $F(s)=(3^{m-1}a-1)/2$. The original $n$ and $s$ paths have already merged at $T(F(s))=(3^m a-1)/4$. If $F(s)>2n$, this common point exceeds $2n$ because $F(s)$ is odd. Every later crossing site on the $s$ chain is on the original orbit.

## The ternary bound on the actual first crossing

Put $y'=F(y)$. If $y,y'\le 2n$, then $y\ge(n-1)/2$ by the preceding physical floor, also true of the initial root. Consequently
$$
 y'+1/2=\tfrac12(3/2)^m(y+1)\ge(3/2)^m(n+1)/4.
$$
For $m\ge6$ this exceeds $2n+1/2$. Thus every completed interior-to-interior run has length in ${1,2,3,4,5}$.

Let $c_0=1$ and $c_k=\sum_{m=1}^{\min(k,5)}c_{k-m}$. For an interior site with at least $k$ preceding odd inputs in the chain, read precisely $k$ of them backwards, truncating the oldest run if necessary. The list of their run lengths is a composition of $k$ into parts at most five. Each composition determines one output residue modulo $3^k$. In the oldest block, with truncated length $r$, its output satisfies $2y'+1=0\pmod{3^r}$, even if the full length was larger. To append a later complete block of length $m$, use
$$
 2^{m+1}y'=3^m(y+1)-2^m.
$$
A residue of $y\pmod{3^r}$ uniquely determines $y'\pmod{3^{r+m}}$. Thus there are at most $c_k$ residue classes. Taking $k=\lceil\log_3(2n+1)\rceil$ leaves at most one interior integer per class. At most $k$ initial sites lack $k$ prior odd inputs since all run lengths are positive. The first hitting index for either event is therefore at most $k+c_k$. The recurrence gives $c_k=O(\lambda^k)$ by induction. Every earlier run costs at most six shortcut clocks, and even the last crossing run has $m\le\log_2(2n+1)$ at its launching site. In the recentered case the original path is one clock later at their common point. Thus a crossing occurs on the original orbit in $O(q^\gamma)$ shortcut clocks, or the nontrivial cycle is reached in that bound. Independently of this time estimate, the first crossing entry is at most $(2n+1)^{\log_2 3}/2$, by $a=(y+1)/2^m$ and $m\le\log_2(y+1)$.

The modular counting argument is related in spirit to path restrictions in Monks, Monks, Monks and Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the $3x+1$ graph*, Discrete Math. 313 (2013), 468–489, §§6.2–6.4. Their strong sufficiency conclusions concern prescribed **infinite** divergent or periodic trajectories. Applying one of them to a finite excursion would require a hitting deadline on that excursion. The deadline above follows instead by an explicit inverse and a bounded list of ternary residues. [Primary paper](https://arxiv.org/abs/1204.3904)

## Arbitrary lengths and both outcomes on ordinary progressions

There is no fixed run number at which the bounded-height mechanism must pay. Both a later valid merger and an actual crossing occur on full ordinary progressions following the same arbitrarily long initial list of singleton exits. This is a statement about initial dynamics only.

Fix any length $J\ge2$. Take first $m_1=3$. Maintain the product $D=\prod_i\big((3/2)^{m_i}/2\big)$, initially $27/16$, where the factor $1/2$ is included once per run. Append $m_i=1$ if $D\ge4/3$, and $m_i=2$ otherwise. The product stays in $[1,27/16]$. Prescribe $J$ such singleton blocks and then a run with four odd inputs. The final even input may be followed either by an odd sentinel or by a second even input. Every prescribed finite parity word is one binary residue class, as follows by lifting the next source bit using the odd high-quotient coefficient. It can be combined by CRT with any exact $v_3(n)=h\ge1$. For large positive lifts, every prior odd entry lies in $[n,2n)$, since its exact affine expression has the indicated coefficient and a nonnegative constant. The final singleton choice crosses $2n$, since it multiplies the coefficient by $81/32>2$. The final double-even choice merges with the positive multiple of three $(y-1)/2<n$ belonging to the last starting site. Thus the latter entire progression is excluded from minimality, even though its first two exits and an arbitrary subsequent number of exits satisfy the old surviving parity condition. On the crossing progression the initial $m_1=3$ allows $q\equiv5\pmod8$ and $9\mid q$ by taking $h\ge3$.

## Evidence and remaining pointwise obligation

`OneEvenEscape.lean` imports the literal PR192 modules `SourceDeletion` (through `MinimumFailure`) and `UpperRepresentative`. It checks uniqueness of the reverse edge, no repetition from a multiple root, a finite linear pigeonhole deadline, rewinding in the recentered case, both local physical implications at an actual least disagreement, and its internal height floor. The composition bound, initial classification, ordinary CRT family and assembly are written arguments. `check_escape.py` uses explicit guards and replays positive ordinary inputs in both Python modes. The balanced controls prescribe the actual final branch, and do not infer basin colors from finite nonmerger.

An escaping source may enter the new region at $y=2n+1$, where the known smaller-multiple bound first fails, or higher. The first outgoing lower comparison there can meet a multiple at least as large as $n$. Its convergence is exactly the new information one would need. The exceptional cycle branch also retains its full ordinary cycle divisibility condition. Neither the bound on residence time nor the exhibited early crossing supplies a contradiction for every least disagreement.
