# Complete denominators from every rotation of a shortcut parity word

**Status.** Independently reviewed written theorem for genuine positive rational cycles. A kernel-checked comparison of the closed coordinates supports the proof. All logarithms labeled by a subscript use that base. The complete positive integer cycle exclusion is open.

## The two-cycle theorem

A chronological length-$n$ binary word $w$ acts by $T_0(x)=x/2$ and $T_1(x)=(3x+1)/2$. Take two **distinct aligned words** $w,v$ of the same length, each with a positive rational fixed point, its actual parity branches, and a closed lap. The two grades may differ and the displayed length may exceed either least period. Let $q_w,q_v$ denote the complete reduced denominators, common to the phases of each lap, and put $Q=\operatorname{lcm}(q_w,q_v)$. Orient the pair so $w$ has at least as many ones as $v$. Let $\mu$ be the smallest real phase of $w$, let $s$ be the Hamming distance, and let $r$ count positions with $w_j=0,v_j=1$. Then $r\le s/2$. Put $\alpha=\log_2 3$ and $H_s=\sum_{j=0}^s\alpha^j$. The **full-denominator bound** is

\[
 \boxed{\quad\log_2 Q>\frac{n+1}{H_s}-1-r\alpha-\log_2(\mu+1).\quad}                 \tag{1}
\]

For a primitive positive rational cycle take $v$ to be any nonidentity rotation of $w$. Then $Q=q_w$, $r=s/2$, and (1) applies at **every shift**, including shifts of order two. For any fixed $s_0$, every such cycle admitting a shift of distance at most $s_0$ has $\log_2 q_w\ge n/H_{s_0}-O_{s_0}(\log n)$. Along any sequence of positive ordinary primitive cycles with $n\to\infty$, the minimum over all nonidentity rotational distances satisfies
\[
 \min_{0<d<n}s(d)\ \ge\ \frac{\log n-\log\log n}{\log\alpha}-O(1).                 \tag{2}
\]
Here unscripted logs are natural. More generally, bounded complete denominator on each side gives the same lower estimate for the distance between any two distinct aligned positive periodic words of that length.

## Positive comparison at the two physical phases

Set $Y=2x+1$. Each branch has the same strictly positive additive term,
\[
                         2Y_{j+1}=3^{w_j}Y_j+1.
\]
Writing $p_w=\sum_j w_j$ and $D_w=2^n-3^{p_w}>0$, a closed lap gives
\[
 D_wY_0=C^*_w,\qquad C^*_w=\sum_{j=0}^{n-1}2^j3^{\sum_{k=j+1}^{n-1}w_k}.       \tag{3}
\]
Every term occurs at every word. At corresponding terms the exponent for $v$ exceeds that for $w$ by at most $r$. Hence $C_v^*\le3^r C_w^*$. Our orientation gives $D_w\le D_v$, so $Y^v_i\le3^rY^w_i$ at **every aligned phase** by simultaneous rotation. In particular $x^v_i+1\le3^r(x^w_i+1)$. This comparison uses the true real ordinates even when the words have different grades or reduced denominators.

Rotate both words so $x^w_0=\mu$. Write their phases as $a_t/Q,b_t/Q$ with integer numerators. These integer coordinates satisfy $2a_{t+1}=3^{w_t}a_t+w_tQ$ and the analogous law for $b$. Distinct aligned periodic words never share an aligned phase. The fixed-point expression has odd raw denominator prime to 3. If an aligned phase is $a/q$ in lowest terms, its real branch is determined by $a$ modulo 2, and its next numerator is $(3^e a+eq)/2$. Coprimality to $q$ persists since 2 and 3 are units modulo $q$. Equality would therefore force identical future parities on the odd-denominator lattice, hence identical periodic words. If the next $\ell$ bits agree, composing the shared affine branches gives
\[
       2^\ell(a_{t+\ell}-b_{t+\ell})=3^k(a_t-b_t).
\]
Thus $2^\ell\le|a_t-b_t|$. In either branch $T(x)+1\le(3/2)(x+1)$ for positive $x$. Combining this with (3),
\[
 \ell < B+t(\alpha-1),\qquad
 B=\log_2 Q +r\alpha+\log_2(\mu+1).                                               \tag{4}
\]
This also holds for an empty agreement run.

Cut the displayed lap into agreement runs followed by one mismatch, with a final agreement run after the last mismatch. Empty first or last runs are allowed. If one chunk starts at elapsed time $t$, the next starts before $\alpha t+B+1$. Treat the final run as followed by one virtual step so the last elapsed time is $n+1$. Starting at zero and iterating $s+1$ times gives $n+1<(B+1)H_s$, proving (1). The directed carry estimate and the two-arm length bound do not require a modular inverse of the shift.

## External scalar input and explicit ordinary distances

The real minimum of a positive rational lap is polynomially bounded in its length independently of its reduced denominator. The telescoping physical ratios give
\[
 0<\Lambda=n\log2-p_w\log3
 =\sum_{j:w_j=1}\log(1+1/(3x_j))<p_w/(3\mu).
\]
Lagarias, Lemma 2.2(1), equation (2.4), gives $|\log_3 2-p_w/n|\ge 1/(1200n^{14.3})$. Thus $\mu< (400/\log3)n^{14.3}<400n^{14.3}$. In (1), $\log_2(\mu+1)<9+15\log_2 n$. For $s\ge 2\log n/\log\alpha$, (2) is immediate. Otherwise $s=O(\log n)$ and $H_s<\alpha^{s+1}/(\alpha-1)$ gives (2) directly. [Lagarias, *Ternary expansions of powers of 2*, Lemma 2.2](https://arxiv.org/pdf/math/0512006)

**Every nontrivial positive ordinary cycle has at least 42 mismatches at every nonidentity shift on its least shortcut period. For $n\ge2^{100}$, every such shift has at least 134.** For the first claim, Hercher's Corollary 29 and Bařina's published computation give $p_w>137{,}500{,}000{,}000>2^{37}$. Positivity gives $n>p_w\log_2 3>3p_w/2$, hence $n>3\cdot2^{36}$. The computation below imports these published external results. [Hercher, Corollary 29](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf) · [2026 corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf) · [Bařina, published computation](https://link.springer.com/article/10.1007/s11227-025-07337-0)

Take $j=\lfloor\log_2 n\rfloor$ and an assumed even mismatch cap $b$. Rotation preserves grade, so the distance is even. Since $3^{29}<2^{46}$ and $\alpha/2<4/5$, (1) with $Q=1$ would imply
\[
 n+1 < U(j,b)=\left(10+15(j+1)+4b/5\right)\sum_{k=0}^b(46/29)^k.
\]
The following upper bounds are exact rational ceilings. The shell factor in parentheses grows by 15 when $j$ grows by one, strictly less than doubling. Thus the shell floor $2^j$ grows faster throughout the indicated tails.

| Assumed cap | Shell $j$ | Ceiling of $U(j,b)$ | Lower floor for $n$ |
|---:|---:|---:|---:|
| 40 | 37 | 171,180,259,775 | 206,158,430,208 |
| 40 | 38 and induction onward | 175,375,854,377 at 38 | 274,877,906,944 at 38 |
| 132 | 100 and induction onward | 1,236,386,936,155,913,536,042,277,872,012 at 100 | 1,267,650,600,228,229,401,496,703,205,376 at 100 |

## Prior work, checks and the remaining arithmetic question

Wren's Paper 218/v3 proves a full-denominator mismatch bound on the same shortcut clock through factor complexity, continued fractions and Armstrong's repetition argument. Its displayed Theorem 1 assumes shift order at least the mismatch count plus one. Corollary 3 gives at least the smaller of the order and 24 on every nontrivial cycle, and the smaller of the order and 110 beyond $2^{100}$. There are stronger known results at the nearest shifts. The argument here compares the actual closed ordinates term by term in (3), gives an unrestricted order quantifier and also compares different cycles. Brox's theorem for descending odd phases concerns the adjacent native shift and uses different constants. The same common-word numerator divisibility used in (4) appears in Paper 216. [Wren, Paper 218/v3](https://rstation.ai/problems/collatz/papers/218) · [Solomon, Paper 216](https://rstation.ai/problems/collatz/papers/216) · [Brox, *Collatz cycles with few descents*](https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9229.pdf)

[The strict Lean module](ShiftCenter.lean) proves (3) in integer centered coordinates, the directed carry comparison with unequal grades, the divisibility on a shared word, growth, and an integer clock bound using $46/29$. The geometric covering argument, the external height and period inputs and their corollaries are written mathematics. [The exact replay](check_shifts.py) exercises 12,282 shift comparisons and 1,119 different-script comparisons through length 13, checks the trivial cycle and $19/5$ control, and verifies the three displayed ceilings. The order-two words of lengths 82, 166 and 334 each have exactly two mismatches and an actual reduced denominator of the indicated full bit length. [Replay output](../../../reports/astra-sixhour-20261127/arithmetic/shifts.json)

A physical positive rational cycle of length 485 and grade 306 in the same replay has minimum exceeding 5,000 and at least 194 mismatches at **every** nonidentity rotation. Its reduced denominator is larger than one. Thus large all-shift distance, near-critical grade and a substantial physical minimum coexist. The missing universal step would have to use complete ordinary integrality to prohibit such high-distance words or supply an independent contradiction in that sector. The estimates above do not provide an escaping-orbit exclusion.
