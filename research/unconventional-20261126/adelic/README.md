# How much of an ordinary Collatz window can periodic words explain?

**PROPOSED written theorems H and A, pending independent review.** An ordinary shortcut path that agrees with a finite collection of periodic parity sequences outside finitely many intervals obeys a two-ended height bound. Positions, contents and lengths of those intervals can vary with the path. At the successive minima of an escaping ordinary orbit this gives a positive lower bound on the total length of the intervals. On any fixed escape, an estimate for the sum of reciprocal odd states strengthens the covering bound to $\log_3 2$ on long windows. The deduction uses the classical $p$-adic Subspace Theorem. It does not assume typical parities, uniformly bounded record gaps or a density theorem.

## 1. A finite statement, with source and endpoint retained

Use $T(x)=x/2$ on even positive integers and $(3x+1)/2$ on odd ones. A letter is the parity **before** the step. Let $W$ be any fixed finite nonempty collection of nonempty binary words. A good interval follows a contiguous piece of a periodic repetition of any word in $W$, starting at any phase. A window of $L$ letters may have at most $k$ ordered, disjoint exceptional intervals, of lengths $d_i\ge0$ and total $B$. Each complementary good interval can choose its own word and phase. A zero-length exceptional interval permits a phase change with no letters charged. Good intervals may also be empty. The two endpoints of the ordinary path are $x$ and $q=T^L(x)$.

**Theorem H.** For every fixed $W,k$ and $0<\epsilon<1$ there is $C=C(W,k,\epsilon)$ such that every such window satisfies at least one inequality

$$
  (x+1)3^B\ \ge\ 2^{(1-\epsilon)L},
  \qquad q+1\ \le\ C(3/2)^B.                                      \tag{H}
$$

The same $C$ works for all positive ordinary sources, clocks, endpoints and parses with the stated fixed parameters. There is no common drift condition on the words. In particular the library can include both single letters. For $B=0$ an unbounded-endpoint sequence of fixed-budget windows costs at least $(1-o(1))L$ bits of initial height. The exponent $1$ is sharp even for the all-odd word. Indeed $x=2^L-1$ follows exactly $L$ odd steps and ends at $3^L-1$. In the opposite direction the window of any length on the ordinary $1,2$ cycle has a two-letter periodic template, $B=0$ and bounded endpoints. Omitting the endpoint alternative would give a false theorem.

### Periodic rational phases

For a bit string $w$ let $p(w)$ be its number of ones and put

$$
 F_w(z)=\frac{3^{p(w)}z+A_w}{2^{|w|}},\qquad
 0\le A_w\le 3^{|w|}-2^{|w|}.
$$

An append of $0$ keeps the numerator carry, and an append of $1$ changes it to $3A_w+2^{|w|}$. These updates give the bound by induction. The empty word acts identically. For each periodic phase of a word of period $h$ and grade $p$, take its rational fixed point $A_w/(2^h-3^p)$. The denominator is odd and nonzero, including for the all-zero word. The successive phases obey their indicated branch equations by cyclically permuting the word and uniqueness of the period fixed point. All phases lie in $\mathbb Z_2$. Their indicated bits are genuine because the rational branch outputs remain in $\mathbb Z_2$ only for the correct bit. Let $Z$ be this finite set and choose an odd common positive denominator $D$.

We need a uniform upper bound on the dyadic cancellation across a whole exceptional interval. Suppose the interval starts at the old good phase $z\in Z$, has arbitrary word $w$ of length $d$, and is followed by phase $u\in Z$. Its shifted numerator is the integer

$$
 c=D(3^{p(w)}z+A_w-2^d u).
$$

There are constants $C_0,C_1$ depending only on the library such that

$$
 |c|\le C_0 3^d,\qquad c\ne0\ \Longrightarrow\ 0\le v_2(c)\le d+C_1.          \tag{V}
$$

The real bound follows from the carry bound. For the second, follow the literal word starting at rational $z$. At the first wrong bit the numerator of that shortcut is a dyadic unit and division by two makes its valuation $-1$. Thereafter multiplying by an odd unit and adding an integral constant, then dividing by two, drops the valuation by one at every bit. If the first mismatch has index $j$ from zero, then $v_2(c)=j$. Indeed the end reference $u$ is dyadically integral and $D$ is odd. With no mismatch, the end value is another phase $v\in Z$. Either $v=u$ and $c=0$, or $c=2^dD(v-u)$ with $v_2(c)\le d+C_1$ by the finiteness of $Z$. This includes $d=0$.

### Three-place proof

Suppose (H) fails. There is a sequence with $(x+1)3^B<2^{(1-\epsilon)L}$ and $(q+1)/(3/2)^B\to\infty$. It has $L\to\infty$ after restriction: bounded $L$ bounds $x$ and $q$. Fix the number of intervals on a subsequence. For each internal good stretch choose a further subsequence on which its length is bounded or tends to infinity. Merge across the bounded ones, adding their actual letters to the exceptional intervals. The resulting total $B'$ is at most $B+O(1)$; the implicit constant is fixed on this subsequence. The new shifted numerators are computed afresh from the literal merged words and endpoint phases, so (V) continues to apply. Remove zero *coordinates* from the identity below. This operation does not require the corresponding intervals to become good. Consecutive retained intervals have a gap tending to infinity.

Write $a(t)$ for the number of odd letters before clock $t$, $P=a(L)$, and $t_j,d_j,c_j$ for the start, length and shifted numerator of each retained interval. Let $z_0,z_L\in Z$ be the chosen boundary phases, which exist even if a good boundary interval is empty. Put $Y=D(x-z_0)$ and $V=D(q-z_L)$. Subtracting the reference phase from the ordinary state and clearing denominators gives

$$
  2^L V=X_0+\sum_j X_j,\qquad
  X_0=3^P Y,\qquad X_j=2^{t_j}3^{P-a(t_j+d_j)}c_j .                       \tag{T}
$$

On a good stretch the shifted variable is multiplied by its true affine slope. An exceptional interval of length $d$ and grade $p$ changes its cleared shifted variable to $3^p$ times the old one plus $c$. Multiplying by the preceding dyadic clock and following ternary clock gives (T). If $Y=0$, the ordinary source is a phase and its deterministic orbit remains in the finite phase set. Then $q$ is bounded. The same contradiction follows if $V=0$. If there are no nonzero interval terms, (T) implies $2^L\mid Y$, whence $2^L\le |Y|\le O_W(x+1)$, contradicting the assumed strict exponential loss for large $L$.

Otherwise apply Schlickewei's rational-field Subspace Theorem with $S=\{\infty,2,3\}$. At infinity and three use the coordinate forms. At two replace the form $X_0$ with $X_0+\sum_jX_j$, retaining the other coordinates. Each local system is linearly independent. Their product on this integer vector is at most

$$
  2^{-L}|Y|\prod_j |c_j|_\infty |c_j|_2 |c_j|_3
    \le O_{W,k}\bigl(2^{-L}(x+1)3^{B'}\bigr).
$$

Here the powers of $2,3$ in every $X_j$ cancel by the product formula, the $3^P$ in the source cancels at three, and $|V|_2\le1$. All coordinates are at most $\exp(O_W(L))$ by the starting height bound, $P\le L$ and (V). The product is exponentially small, so for some fixed $\delta>0$ it is at most $\|X\|_\infty^{-\delta}$ for large $L$. The integer-vector form of the theorem applies directly (Bilu, Theorem 2.3). Equivalently, making the vector primitive divides the product by the dimension-th power of the prime-to-six part of its gcd and only reduces the height. Thus one fixed nonzero rational linear relation holds infinitely often.

That relation must involve $X_0$. For a retained interval, (V) places the valuation of $X_j$ in $[t_j,t_j+d_j+C_1]$. These intervals of valuations are separated by gaps tending to infinity. Among nonzero fixed rational multiples of the $X_j$, the earliest term therefore has strictly smallest valuation for all sufficiently late members, so their sum cannot vanish. Solve the relation for $X_0$ and substitute into (T). We obtain $2^L V=\sum b_jX_j$ with fixed rational coefficients. There must be a nonzero coefficient since $V\ne0$. If $j$ is the first such index, the same least-valuation argument gives

$$
 L\le v_2(2^L V)=v_2(b_j)+v_2(X_j)\le t_j+d_j+O(1).
$$

Thus the surviving interval ends within bounded distance $r=L-t_j-d_j$ of the window end. There can be no later retained interval for large members of the subsequence. In particular $2^L V=b_jX_j$. The final $r$ steps contribute at most $r$ further odd letters. Hence

$$
 |V|\le |b_j|2^{-d_j-r}3^r C_0 3^{d_j}
        \ll (3/2)^{d_j}\le (3/2)^{B'}.
$$

This bounds $(q+1)/(3/2)^B$ on the subsequence and proves (H). The proof supplies no effective numerical value for $C$.

## 2. A quantitative obstruction on one fixed escaping source

Let $x_j=T^j(x_0)$ be an injective positive ordinary orbit. It tends to infinity because every bounded set of positive integers is finite. There are cofinally many suffix minima: choose the index attaining the minimum of each arbitrarily late tail. Write $a=x_i$ for any such minimum, so $x_{i+s}\ge a$ for every $s\ge0$. Set

$$
 \alpha=\log_2 3,\quad c=\log_2(3/2),\quad \lambda=1+\alpha/c,\quad
 L=\lfloor\lambda\log_2(a+1)\rfloor .
$$

**Corollary M.** At these actual windows, for every fixed $W,k$ and every admissible choice of the exceptional intervals,

$$
 \liminf_{a\to\infty}\frac{B}{L}\ \ge\ \frac{1}{\alpha+c}
  =0.4608454206\ldots .                                                     \tag{M}
$$

In the first alternative of (H), $B/L\ge (1-\epsilon-1/\lambda-o(1))/\alpha$. In the second, $q\ge a$ gives $B/L\ge (1/\lambda-o(1))/c$. Let $\epsilon$ decrease to zero. Our choice $\lambda=3.709511291\ldots$ equalizes the two limits. The constant optimizes this two-branch bound; no optimality assertion for the genuine orbit is made. The same deduction applies to any finite segment whose endpoint is at least its starting height, at this choice of $L$.

For example let $W=\{1\}$ and let $E_a\subset[0,1]$ be the even departure positions in the window divided by $L$. Every Hausdorff subsequential limit $E$ has Lebesgue measure at least $1/(\alpha+c)$. The sets are eventually nonempty by (M). For any $\eta>0$, compactness and outer regularity cover $E$ by finitely many relatively open intervals of total length at most $|E|+\eta$. The union contains all $E_a$ sufficiently far along the convergent subsequence. Rounding the endpoints to shortcut clocks adds $O(1)$ covered letters per interval; outside these intervals every bit is one. Now apply (M) with this fixed finite number of intervals and let $\eta\to0$. This is a lower bound on **macroscopic covering length**. A set of $o(L)$ positions with spacing $o(L)$ can still have Hausdorff limit $[0,1]$.

As an exact-pattern consequence, let $R_W(n)$ be the minimum number of periodic pieces covering the first $n$ parity bits, with value $+\infty$ if impossible. On an escaping source, $R_W(n)/\log n\to\infty$. Indeed on $[j,2j)$ the start is at most $(x_0+1)(3/2)^j$ after adding one, because $T(u)+1\le(3/2)(u+1)$. The endpoint tends to infinity. Taking $B=0$ and $1-\epsilon>c$, (H) rules out every fixed piece budget eventually. For $2^h\le n<2^{h+1}$ split a prefix parse at $1,2,4,\ldots,2^h$. Each cut adds at most one piece. The full parse therefore has at least the sum of the minimal costs on the completed dyadic windows minus $h+1$. Dividing by $h$ gives divergence by Cesàro averaging. Finite completion of an unparseable prefix is impossible, so the infinite-cost convention causes no ambiguity. With the two single-letter templates this also implies that on a fixed escaping source the number of even steps divided by $\log n$ tends to infinity. A positive eventual cycle has at least one even step per period, so the latter statement holds for every positive ordinary source. Related stronger global complexity estimates exist in the odd-gap convention; see below.

## 3. On an actual escape the second alternative disappears

Fix a positive ordinary source with an injective shortcut orbit $(x_j)$. Fix a finite set of primes $S\supseteq\{2,3\}$. For an integer $u\ne0$ define its part away from $S$ by $H_S(u)=\prod_{p\notin S}p^{v_p(u)}$ and use $H_S(0)=1$. For each pair of clocks $i,L$ take any window beginning at $x_i$, with library and interval budget fixed as above. Use the **original unmerged** shifted numerators $c_j$ of its exceptional intervals. There is no need for any gaps between these intervals.

**Theorem A (arithmetic cost on one ordinary escape).** Along every sequence $i,L\to\infty$,

$$
 \liminf\frac{\log_2(x_i+1)+\sum_j\log_2 H_S(c_j)}{L}\ \ge 1.             \tag{A}
$$

Consequently the same bound holds with $\alpha B$ in place of the sum, since $H_S(c_j)\le C_0 3^{d_j}$. In particular whenever $\log(x_i+1)=o(L)$, the exceptional intervals have total length at least $(\log_3 2-o(1))L$, with $\log_3 2=0.6309297535\ldots$.

**Real estimate.** The sole orbit estimate used here is the finite reciprocal moment on a simple positive orbit. In this repository T-A3-651 in `research/astra-three-routes/pass3/FINITE_RECORDS.md` on `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` bounds the number of odd states below $X$ on any finite simple path by $5X^{39/40}$; summation over dyadic shells gives $\sum_{j:x_j\text{ odd}}1/x_j<\infty$. Set $e_i=\sum_{j\ge i:x_j\text{ odd}}1/(3x_j)$ and $m_i=\min_{j\ge i}x_j$. Then $e_i\to0$ and $m_i\to\infty$. For any true subpath after $i$, starting at $b$ and ending at $d=rb+\beta$, its positive multiplier is $r=3^{p}/2^s$ and its affine offset $\beta\ge0$. The exact product identity gives

$$
 0\le \beta/d=1-\prod_{j\text{ odd in subpath}}(1+1/(3x_j))^{-1}
       \le e_i .                                                               \tag{R}
$$

The last inequality follows by bounding $1-e^{-v}\le v$ and $\log(1+t)\le t$. Let $q=x_{i+L}$. For an exceptional interval with input $b$, output $d$, and phases $z,u$, write $r'$ for the multiplier of the actual remaining suffix, so $r'd\le q$. The $j$th term of (T) obeys

$$
 \frac{|X_j|}{D2^L q}
   =\frac{r'|rz+\beta-u|}{q}
   \le |z|/b+\beta/d+|u|/d\le 2\max_{v\in Z}|v|/m_i+e_i .                  \tag{R1}
$$

For the full window, $X_0/(D2^L q)=r_{\rm full}(x_i-z_0)/q\to1$ uniformly in $L$ by (R). Every other coordinate is $o(|X_0|)$ in the ordinary absolute value. This is where common ordinary realization enters. The entries of a family of unrelated finite cylinders have no such common tail estimate.

**Fixed-forms descent.** If (A) fails, there is $\delta>0$ and a subsequence on which $(x_i+1)\prod_j H_S(c_j)\le2^{(1-\delta)L}$. Remove zero coordinates and pass to a subsequence fixing their number and indices. The start $Y=D(x_i-z_0)$ is nonzero eventually because $x_i\to\infty$. Maintain the integer vector consisting of $X_0$ and a subset of the original nonzero $X_j$. Its dyadic linear form has the shape $X_0+\sum d_j X_j=2^L D(q-z_L)$ with fixed rational $d_j$, initially all one. Its dyadic absolute value is at most $2^{-L}$. At all places $S\cup\{\infty\}$ use coordinate forms, except for replacing the source form at two by this linear form. Linear independence holds at two because its source coefficient is exactly one. The product is bounded by

$$
 2^{-L}|Y|\prod_{\text{retained }j}H_S(c_j)
 \le O_W(2^{-\delta L}).                                                     \tag{P}
$$

Indeed each switch coordinate is an integral $S$-unit monomial times $c_j$ and its full local product is exactly $H_S(c_j)$. The product from $X_0$ outside the removed dyadic factor is at most $|Y|$. The $S$-unit monomial terminology here refers to powers of $2$ and $3$, not to $c_j$. Each deleted factor $H_S(c_j)$ is at least one. The original height bound is $\|X\|_\infty\le\exp(O_W(L))$ under the alleged failure; a retained subvector has the same upper bound. For dimensions at least two, (P) therefore puts these integer vectors in finitely many proper rational subspaces by the same classical fixed-forms theorem. This also follows in its primitive formulation: division by the common gcd $g$ multiplies the local product by $H_S(g)^{-d}\le1$ in dimension $d$, and the primitive sup norm is no larger. Zero dyadic form would put $q$ in the finite phase set, impossible on these late windows.

One rational hyperplane recurs on a further subsequence. Its source coefficient must vanish: divide its relation by $X_0$ and use (R1). Solve for a switch coordinate with nonzero coefficient, substitute into the dyadic form, and delete that coordinate. All new coefficients are fixed rationals on this subsequence; the source coefficient remains one. This is a finite induction on dimension, with one Subspace Theorem application per reduction. At dimension one the dyadic identity is $X_0=2^L D(q-z_L)$. Thus $2^L\mid Y$, since $3^P$ is odd, while $0<|Y|\le O_W(x_i+1)\le O_W(2^{(1-\delta)L})$. This final contradiction proves (A).

**A sharper starting charge when the raw height is controlled.** If $\log(x_i+1)=O(L)$, the numerator $Y=D(x_i-z_0)$ can replace $x_i+1$ in (A) with the charge $2^{v_2(Y)}H_S(Y)$. This is at most $|Y|=O_W(x_i+1)$ and can save a large odd $S$-part. The source contribution from all places except the removed dyadic factor is exactly this integer. A failure therefore gives exponential decay in (P); the extra hypothesis supplies the required $\exp(O(L))$ height bound even when $Y$ has large $S$-part. At dimension one the conclusion $2^L\mid Y$ forces $2^{v_2(Y)}H_S(Y)\ge2^L$ directly. For example the reference $-1$ charges only the dyadic and outside-$S$ factors of $x_i+1$; a large ternary part at the entrance is consequently relevant. An initial zero-length exceptional interval can put this reference before a different first good phase at bounded additional cost. The two-window real dominance in PR193 and its one-window rough source bound are the methodological predecessors of this refinement.

**Macroscopic support on full prefixes.** For $N\to\infty$ take $i=\lfloor\sqrt N\rfloor$ and $L=N-i$. Then $\log_2(x_i+1)\le O_{x_0}(1)+i\log_2(3/2)=o(L)$. Restricting a whole-prefix parse to this suffix increases neither its interval count nor its total exceptional length. It follows that at least $(\log_3 2-o(1))N$ letters of any full prefix lie in the exceptional intervals, for every fixed $W,k$. For any fixed periodic parity pattern, the rescaled set of its bitwise mismatch positions within $[0,N)$ has Hausdorff subsequential limits of Lebesgue measure at least $\log_3 2$. An interval avoiding mismatches follows the relevant phase, so the finite open cover argument from §2 applies. In particular this holds for even positions (template $1$) and odd positions (template $0$). These two closed macroscopic limits can overlap.

More generally, the same proof applies across any family of possibly different ordinary windows for which the minimum visited height diverges and the sum of reciprocal odd departures in the window tends to zero. Replace $m_i,e_i$ in (R1) by these local quantities. Thus across any hypothetical family of distinct positive cycles with minima $a\to\infty$, windows starting at these minima with $\log a=o(L)$ and $L=o(a)$ obey the same $\log_3 2$ covering bound. The ratio $L/a\to0$ controls the sum even when the period is repeated. This does not exclude one fixed cycle.

The same conclusion on suffix-minimum windows of arbitrary length $L/\log(a+1)\to\infty$ follows directly from (A). In the special range $L=o(a)$ the one-window bound $e\le L/(3a)$ already suffices in (R), so this local corollary needs no global reciprocal theorem. None of these statements gives lower natural density $\log_3 2$ for either bit.

**Adaptive periods at the same orbit.** The proof of (A) also tolerates a changing library with bounded interval count. Only the actual good pieces matter. Let $D_i$ be an odd common denominator of their phases, and $Z_i$ their phase values, including both phases at each exceptional boundary. Suppose

$$
 \log D_i+\log(1+\max_{z\in Z_i}|z|)=o(L),\qquad
 \max_{z\in Z_i}|z|=o(m_i).
$$

Use these moving $D_i,Z_i$ in the definition of $c_j$. Then (R1) still tends to zero relative to $D_i2^Lq$, and the form coefficients are still fixed: their initial list consists only of coordinate forms and the sum. The factor from $Y$ in (P) is at most $D_i(x_i+\max|z|)=2^{o(L)}(x_i+1)$. The initial norm remains $\exp(O(L))$ under a failure. All subsequent subspace eliminations take place on subsequences, with rational coefficients fixed at that stage. The last one-dimensional bound is $|Y|\le 2^{(1-\delta+o(1))L}$. These estimates prove (A) with this moving choice, and $\sum\log_2 H_S(c_j)\le\alpha B+o(L)$. In particular one may choose a fresh periodic template on each good interval, provided the sum of the lengths of their chosen periods is $o(\min(L,\log(m_i+1)))$. The denominator of every rotation of one period divides $|2^h-3^p|\le3^h$, and $|z|\le3^h$ for every phase, so the two displayed conditions follow. Nothing permits a new interval per bit.

## 4. Why record growth and recurrence do not force a cheap cover

Take the chronological odd-gap record blocks $A=(1)$ and $B=(2,1)$, with literal shortcut bit encodings $1$ and $101$. Their coefficients are $3/2$ and $9/8$. Both give strict first ladder crossings; the first odd step inside $B$ has coefficient $3/4<1$. Every concatenation thus has exact record gaps at most two. Starting the *prescribed real affine* maps at any positive real number gives exponentially increasing heights at record times, uniformly comparable intermediate heights and a finite reciprocal sum. These statements do not assert that the real numbers obey the integer parity tests.

An explicit uniformly recurrent example is obtained by using the Thue–Morse word $t_n$ to choose $A$ or $B$. It has bounded lengths of agreement with **each fixed** periodic shortcut template. Here is a proof covering the variable bit encoding. The identity $t_{2n}=t_n$, $t_{2n+1}=1-t_n$ rules out any eventual period: reduce an even period by two, and an odd period $2h+1$ would give $t_{n+h}=t_{n+h+1}=1-t_n$ for all large $n$. Every occurring factor appears with bounded gaps. It occurs inside some iterate of $0$ under the substitution $0\mapsto01,\ 1\mapsto10$, and the second iterate of either letter contains $0$. Thus no periodic word has arbitrarily long factors in common with $t$: a mismatch pair at distance its period appears throughout $t$ with bounded gaps. Variable-length decoding here is local. The starts of $B$ are exactly the positions of $10$, and the positions outside their length-three blocks are the single $A$ letters. A two-sided periodic limit of the shortcut encoding would therefore decode to a periodic limit of the block letters. Compactness would give such a limit if a fixed periodic bit template had unbounded matching length. This proves the assertion. Bounded-gap recurrence of the physical word follows from bounded expansion of each block and bounded-gap recurrence of every block factor.

There is also a positive-factor-entropy variant. Interleave $t_n$ at even block indices with a binary sequence $b_n$ containing every finite binary word at odd indices (for instance concatenate the list of all finite binary words in order of length). An arbitrarily long periodic block factor would yield arbitrarily long periodic factors on the Thue–Morse subsequence at bounded period, even if the factor begins at odd index. The same decoding proof applies. At least $2^m$ distinct block factors of length $2m$ occur, by projection to $b$. Their distinct bit encodings have lengths at most $6m$; injectivity on complete codewords follows by locating $10$ and then the single $A$ letters. Since the word is infinite, factor counts are nondecreasing with length, and its number of factors of length $6m$ is at least $2^m/(6m+1)$. This variant need not be uniformly recurrent.

For either example, a fixed finite library and fixed interval budget can explain only $O_{W,k}(1)$ good letters in any window, since each good piece has bounded length. Their exceptional intervals occupy $L-O_{W,k}(1)$ letters, fully compatible with (M) and the covering conclusion of (A). Each *finite* bit window has positive ordinary lifts in its unique residue class modulo $2^L$, by inverting the odd multiplier modulo $2^L$ and replaying the successive parities. Neither a single all-time positive ordinary source nor its existence follows. The uniformly recurrent example is already excluded by independent low-complexity methods. Its role here is to test the proposed implication from record growth, recurrence and reciprocal summability to a useful cover. The high-complexity variant tests a different attempted implication.

There are countable-limit symbolic controls as well. Isolated $B$ blocks separated by runs of $A$ whose lengths tend to infinity give only single-defect and constant patterns in the two-sided block limit. Taking defect spacings of order the logarithm of time, for example $A^{\lceil\log(j+1)\rceil}B$ at stage $j$, makes every fixed positive-length normalized interval in a long prefix contain a defect, although the density of defects tends to zero. The rescaled even locations have Hausdorff limit $[0,1]$, consistent with the bound above. No fixed ordinary realization is asserted for this script. In particular the new macroscopic restriction does not exclude countable cluster sets in general.

## 5. Provenance and proof boundary

* Schlickewei's rational-field $p$-adic Subspace Theorem is the external Diophantine input. Bilu, Theorem 2.3, states the integer-vector version with the sup norm; Theorem 2.3′ states the $S$-integer height version. [Original linear-forms paper](https://doi.org/10.1016/0022-314X(77)90073-7) · [Precise formulation, preprint p. 4](https://arxiv.org/pdf/0907.2098).
* PR193 `4cc06e7d8fdec923eed73a26b1e9d680c9f701d1`, `research/astra-multiple-attacks-20261125/arithmetic/README.md`, proves a matched-forms lower bound for one positive carry, and a two-actual-window bound on a fixed escape via real dominance and rank reduction. The rank-reduction idea in (A) is inherited. Here the comparison is with signed rational periodic phases, arbitrary phase changes and exceptional intervals of unrelated grade. The finite all-source alternative (H), the explicit local covering costs, and the prefix Hausdorff-support consequence involve a different set of quantities. Its bound for an arbitrary unshifted carry does not bound the separate shifted hole terms from above.
* PR206 `3729d84e00cf8794dab43fe2f500213b2b643f83`, `research/clock-itineraries/SparseDefects.md`, applies Evertse to a fixed number of exceptions from the neutral odd gap two, with a cost for exceptional division totals. Its whole-path superlogarithmic conclusion concerns high-relative-carry exact rows of total clock twice the number of odd steps. The neutral shift and exceptional-term analysis are close precedents. Here the finite theorem uses arbitrary periodic shortcut phases, no exact-row condition and two endpoints; the one-orbit conclusion concerns all windows.
* PR187 `099058f3f2602a48e109c964899f0a9a2a223338`, `research/fixed-source-repeat-obstruction-20261124/README.md`, FSR-2, excludes specified bounded digit-weight schedules by shared-factor congruences between two actual states. Our theorem assumes no such occurrence of the same word. PR210 `592328fecf8ea2cf41736294856d95f890a1ba98` concerns rationality of backward critical ternary traces and a distinct stammering criterion. Neither an algebraic ternary limit nor a periodic directive is assumed here.
* Lyapunov Weaver's rStation Paper 15, Theorem 9, gives an effective $\gg\log t\log\log t$ global count in its phase-flexible odd-gap dictionary convention, with adaptive dictionary budget. Paper 173 gives superlinear whole-word factor complexity and a different finite local-descent criterion. Paper 172 treats sparse aligned positions in a growing period. We claim no priority for global periodic-piece counting or the Subspace Theorem technique. Here the native shortcut clock, arbitrary charged intervals, explicit local length/height alternatives, and Hausdorff support of actual prefixes are the relevant distinctions. [Paper 15](https://rstation.ai/problems/collatz/papers/15) · [Paper 172](https://rstation.ai/problems/collatz/papers/172) · [Paper 173](https://rstation.ai/problems/collatz/papers/173/v1).

**First unsupported step.** No argument supplies a small union of exceptional intervals, or small prime-to-$S$ product of their shifted numerators, for an arbitrary large actual escape window. The symbolic controls show why real growth, bounded strict-record gaps, summability and recurrence alone cannot do so. These results do not exclude all injective positive orbits or any new class of positive cycles.

## 6. Finite evidence

`PeriodicWindows.lean` was compiled with Lean 4.34.1 and the matching Mathlib checkout. It derives the cleared affine equations from a physical integer itinerary, proves the two-clock rule for joining shifted intervals, proves the exact dyadic factor given the genuine-prefix identity and the oddness of the wrong branch numerator (the parity interpretation is in the written proof), and discharges the one-coordinate divisibility case. Its six printed declarations use only `propext`, `Quot.sound` and, in the parity factorization, `Classical.choice`. The external Subspace Theorem, limits, covering argument and countercontrol remain written mathematics.

`python -B research/unconventional-20261126/adelic/controls.py` and the optimized interpreter reproduced `CONTROLS.json`. The checks used 22 distinct positive, negative and zero rational phases, allowed empty intervals, and covered 123,420 choices of old phase, new phase and arbitrary exceptional word. They included 119,548 exact valuations at a wrong shortcut bit, 176 zero coefficients, 2,500 directly replayed positive windows, and 6,239 independent identities before and after merging neighboring intervals. Sharpness and the bounded-endpoint control were replayed up to clock 512. These finite checks do not certify the infinite analytical theorems.
