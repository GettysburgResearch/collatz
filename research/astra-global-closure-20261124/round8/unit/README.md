# Ordinary descent on a progression inside every ternary unit class

**Lean verification of ordinary contraction and the grade obstruction. Written corollaries for directed failures. Universal transfer remains OPEN.** Write $T(2n)=n, T(2n+1)=3n+2$, and let $C$ be the positive ordinary basin of 1. A forward failure is an odd ternary unit $u$ with $u\in C, 3u\notin C$. A reverse failure has the opposite labels. In **each prescribed class** of odd ternary units modulo $3^k$, there is a full arithmetic subprogression on which any forward failure forces a forward failure below $u/5$. For the reverse direction there is a subprogression on which any failure forces one below $u/8$. Each subprogression can also be intersected with any prescribed odd binary class. No counterexample is assumed in constructing the progressions.

The physical theorem, including existence of the subprogression and the smaller ordinary predecessor for **every** member, is [kernel-checked](RayGrade.lean), theorem `every_cell`. The passage from a small bad vertex to a smaller failure uses the bounded directed paths of [round seven](../../round7/head/README.md), at commit `0e8a7f9f965416189b30b57b8aa818fbcb7757c7`. The exact coverage quantifiers are

$$
  \forall\text{ coarse cell }I\quad\exists\text{ subcell }J\subset I
  \quad\forall u\in J:\quad \text{failure}(u)\Rightarrow
       \exists v<u:\ \text{failure}(v).
$$

A prescribed failing $u\in I$ can lie outside $J$. The calculation below gives the precision of the subset and an obstruction to forcing an arbitrary ordinary input into a bounded-grade proof.

## Steering the actual bad arm

For any positive $q$ prime to three and $p\ge0$, there are $0\le t<3^r$, $A\le4p$, $r=5p+13$, such that **every**

$$
 Q=q+3^p(t+3^r l),\qquad l\ge0,
$$

has a positive ordinary $z$ satisfying $T^{r+A}z=Q$ and $171z<Q$. With the least positive representative $q$ of the initial cell, this includes every positive member of the final residue class.

Let $I_e(y)=(2^ey-1)/3$. Choose $e=2,1,2,3,4,1$, respectively, for $y=1,2,4,5,7,8\bmod9$. The result is a positive odd ternary unit and reaches $y$ in exactly the specified $e$ steps, beginning with one odd step followed by $e-1$ halvings. Apply this $p$ times at the reference $q$, ending at $y$ with total length $A\le4p$. For every lift $Q=q+3^pL$ the same backward words are legal and end at $Y=y+2^A L$. This follows by successive integer division in the inverse formulas. In particular $3^pY\le2^A Q$.

The equation $y+2^At+1=0\bmod3^r$ has one solution for $t\bmod3^r$. For $L=t+3^r l$, put $m=(Y+1)/3^r\ge1$ and $z=2^rm-1>0$. All $r$ initial steps at $z$ are odd and reach $Y$. Since $r>0$, one has $3^r z<2^rY$. Finally

$$
 171\,2^{r+A}\le171\,2^{13}512^p<3^{13}729^p=3^{r+p}.
$$

This proves the height claim. The $p+r$ odd inputs all occur on the actual path to $Q$. The preceding prefix can be replaced by any legal inverse word on the reference with $p$ odds and total raw length $A$, provided $K2^{r+A}\le3^{r+p}$ for the desired height factor $K$. Theorems `back_lift` and `steered_descent` implement this version.

For a forward failure take $q=(9u_0+1)/2=T(3u_0)$ and $p=k+2$, with $u_0$ the least positive odd representative of the chosen unit class modulo $3^k$. The entire selected odd subclass is

$$
 u=u_0+2\,3^k(t+3^r l).
$$

Its actual $T(3u)$ is $Q<5u$ for $u>1$. Thus $z\notin C$. Round seven supplies a forward failure $v\le(167/27)z<u/5$. A reverse failure has bad $u$, so apply the construction directly at $q=u_0,p=k$, choosing the least positive representative modulo $3^k$ and retaining odd $Q$. There is a reverse failure $v\le(2351/123)z<u/8$. Reapplying the second construction inside the first selected subclass gives a subprogression with both properties. A finite intersection with an odd binary class preserves an infinite arithmetic progression by coprimality.

## A sharper precision using the critical inverse paths of Applegate and Lagarias

**SOURCE-QUALIFIED sharpening.** For any prescribed ternary unit cell with precision $p\ge1$, the same height factor 171 is attained on a subcell of precision at most

$$
                   p+\lceil 5p/6\rceil+65.
$$

Applegate and Lagarias's Theorem 4.1 supplies a finite lower-bound certificate for ones-ratio $14/29$. Its Table 3 gives maximum odd weight 29 and depth 60. Definition 3.2 and the iteration in the proof of Theorem 3.1(i) give positive ordinary inverse blocks, with unit endpoints and weight/raw-clock ratio at least $14/29$. To use their noncycle hypothesis as stated, start at a power $2^e>2$ in the supplied unit cell. Such powers exist since 2 generates the units modulo $3^p$. Cubing $4=1+3$ raises its difference-from-one valuation by exactly one, giving order $3^{p-1}$ for 4, and 2 has even order. Every ancestor of this chosen noncyclic root is noncyclic. [Applegate and Lagarias, *Lower Bounds for the Total Stopping Time of 3x+1 Iterates*, Definitions 3.1–3.2, Theorems 3.1(i), 4.1 and Table 3](https://arxiv.org/pdf/math/0103054)

Stop at the first block boundary with $b\ge p$ cumulative odd inputs. Then $p\le b\le p+28$ and the cumulative clock $A\le29b/14$. Transfer the fixed inverse word to the least positive representative of its initial root modulo $3^b$. All inverse edges are integral on this class because each reversed odd step consumes one ternary digit. Each inversion preserves positivity for positive integral targets. Any reversed halving after the last reversed odd step may be discarded, preserving $b$ and decreasing $A$. Group the remaining reverse steps into the $I_e$ above. The final ancestor can have either ternary residue. The free digit argument only needs its change $2^A L$.

Now take $r=\lceil5b/6\rceil+13$. The exact inequality $2^{122}<3^{77}$ gives $(2^{29/14}/3)(2/3)^{5/6}<1$ by raising to power 42. Together with $171\,2^{13}<3^{13}$, it pays $171\,2^{A+r}\le3^{b+r}$. The final precision is $b+r\le p+\lceil5p/6\rceil+65$. This sharpening imports the primary paper's computer certificate. Its 350,688,758 entries were not regenerated here. The elementary $6p+13$ precision theorem above has no external certificate dependency.

## The odd-count cost on the initial all-odd excursion

Suppose $q+1=2^ia$ with $a>0$. Let $z<q$ be positive and $T^h z=T^i q$. Put $P$ equal to the number of odd inputs on the path from $z$ to this meeting. Then

$$
                  h>i,\qquad P>i+v_3(q-1) \quad(q>1).
$$

This applies to unbounded $h$, all possible starting $z<q$, and all legal inverse paths into any of the first $v_2(q+1)$ steps. A stronger certificate holds for every $1\le b\le q$ for which $3^P\mid 3^i(q-b)$.

$$
                            2(q+1)\le (b+1)(z+1).                 \tag{1}
$$

For the proof write $h=j+i$, $v=T^jz$, with counts $P_0,P_1$ before and after $v$. For an arbitrary trajectory of length $t$ and count $P_t$, induction on its first edge gives

$$
 3^{P_t}(x+1)\le2^t(T^tx+1)\le3^{P_t}x+3^t.
$$

The all-odd upper arm obeys $2^i(T^iq+1)=3^i(q+1)$. The upper bound at $z$ rules out $h\le i$, since the maximal forward factor $3/2$ through a shorter clock cannot reach the all-odd endpoint from a smaller start. The upper bound on the suffix at $v$ gives $3^iq\le3^{P_1}v$. Let $k=3^i(q-b)/3^P$. If $z\le2^jk$, then $v\le3^{P_0}k$. This last integer ceiling follows by induction. An odd start below an even ceiling is at least one unit below it, so its odd step stays below three times the halved ceiling. This would give $3^iq\le3^i(q-b)$, impossible. Consequently $z\ge2^jk+1$.

The lower carry bound at $z$ now gives $2\cdot3^P\le2^j3^i(b+1)$, after subtracting $2^j3^Pk=2^j3^i(q-b)$ from both sides. Multiply by $q-b$, use the formula for $k$, and use $z\ge2^jk+1$ again to obtain (1). Taking $b=1$ would force $z\ge q$. Hence $3^P\nmid3^i(q-1)$, proving the strict grade bound. These are theorems `reference_barrier` and `strict_grade` in [RayGrade.lean](RayGrade.lean). The grade inequality is attained when $q=13,z=11,i=1,h=4,P=3$, since this gives $3=1+v_3(12)+1$.

## Paying unbounded odd-count grades on the Mersenne ray

PR192 reselects a first bad $M_d=2^d-1$ with odd $d$ from a one-odd parent. Its canonical height may exceed the original $JN$ upper bound. Here the descent uses the directed unit rank directly. For $d>1$ odd the grade in the preceding theorem at $Q=M_d$ is $s=1+v_3((d-1)/2)$, unbounded already at $d=1+2\cdot3^j$. Every smaller representative meeting by upper clock $d$ must spend more than $i+s$ odd inputs at the meeting clock $i$. [PR192, `b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b`, canonical-source reselection](https://github.com/GettysburgResearch/collatz/blob/b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b/research/astra-closing-step-20261124/descent/README.md)

For **each** exact $s\ge1$, let $r=s+13$. Write $Q=1+3^sa$. The ordinary path from $Y=1+4^sa$ reaches $Q$ at clock $2s$, using $s$ copies of $1+4v\to2+6v\to1+3v$. If $3^r\mid Y+1$, then $z=2^r(Y+1)/3^r-1$ reaches $Q$ at clock $r+2s$. The inequality $171\,2^r4^s<3^{r+s}$ follows from $171\,2^{13}<3^{13}$ and $8^s\le9^s$. The theorem `repaid_descent` gives $171z<Q$.

Writing $d=1+2j$, the legality and exact grade are imposed simultaneously by

$$
        4^j\equiv 1-3^s4^{-s}\pmod{3^{s+r}}.
$$

The order of 4 proved above gives one class $j\bmod3^{s+r-1}$. Its exact $v_3(j)=s-1$ follows by $v_3(4^j-1)=1+v_3(j)$. For $s\ge2$, one has $3\nmid d+1$, so $u=(2^{d+1}-1)/3$ is a positive odd ternary unit, with an explicit lower path to 1. Its upper $3u=M_{d+1}$ has the same component as $M_d$. Their all-odd prefixes land at $3^{d+1}-1,3^d-1$, and $3^d=3\bmod4$ gives a common endpoint $(3^{d+1}-1)/4$ after two further steps on each arm. Thus a failure at such $u$ forces a forward failure $v\le(167/27)z<u/18$, since $Q=(3u-1)/2$. These exponents have unbounded $s$ and explicit admissible progression for every $s\ge2$.

For a fixed ordinary target $Q$, every constructed $z$ has $z=2^rm-1\ge2^r-1$ with $m\ge1$. The required $171z<Q$ therefore forces $r<\log_2(1+Q/171)$. The elementary construction has $r=5p+13$, so each fixed $Q$ has an explicit finite range of permissible input precisions. The critical-path refinement also has $r\ge5p/6+13$.

The [critical-profile count](CRITICAL_PROFILES.md) compares this pointwise difficulty to the bad arm’s required odd frequency at a least directed failure. The grade barrier addresses all smaller representatives meeting along a specified all-odd excursion. The constructive result supplies one high-digit choice in every prescribed low-digit cell. A least directed failure, if it exists, must avoid these contracting progressions. Their density inside a $p$-digit cell can decrease exponentially in $p$. The argument supplies no route from that one ordinary failure to one of the selected extensions while preserving its labels and repaying its height. Establishing such a route, or ruling out the simultaneously unserved actual integers by a different argument, remains **OPEN**.
