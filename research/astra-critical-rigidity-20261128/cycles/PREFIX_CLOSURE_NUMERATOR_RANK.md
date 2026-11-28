# Large multiplicative rank in the signed rational closures of ordinary prefixes

Fix a positive integer \(n\), use the ordinary shortcut map \(T(x)=x/2\) at even \(x\) and \(T(x)=(3x+1)/2\) at odd \(x\), and take the actual first \(t\) parities from \(n\). Repeat those \(t\) parities periodically and let \(z_t\) be their signed rational affine fixed point. Among the \(g_t\) odd phases of that repeating display, reduce every state to the common positive denominator \(q_t\). Let \(r_t\) be the multiplicative rank of the **absolute integer numerators** of those odd phases.

* On every fixed ordinary source, as \(t\to\infty\) through dates with \(T^t n\ne n\),
  \[
                        \liminf\frac{r_t}{\sqrt t}\ge\frac1{\sqrt3}.       \tag{1}
  \]
  This includes both signs of the rational center.
* If the ordinary source is eventually periodic of least ultimate shortcut period \(P\), then on the same nonreturns,
  \[
                        \liminf\frac{r_t}{t}\ge\frac1{2P}.                \tag{2}
  \]
  In particular the ordinary trajectory from \(3\) eventually alternates \(1,2\) and never returns to \(3\). For all large \(t\), the rank of its prefix closure is at least \((1/4-o(1))t\).

The objects of growing rank are the signed rational periodic closures, even when the original ordinary trajectory only visits finitely many states. At an actual return the rational closure is the ordinary cycle, so the nonreturn restriction is material. This is not a growth claim for the state set of a fixed eventually periodic ordinary source.

## A height cost for both signs

Consider first any signed rational periodic itinerary with \(p>0\) odd phases, total shortcut length \(A\), common full denominator \(q\) prime to six, and positive integer absolute odd numerators \(y_i\), each coprime to \(q\). All odd phases have the same sign \(\sigma\), by the strictly positive full affine carry at every odd cut and the common signed determinant \(2^A-3^p\). Thus \(2^{e_i}y_{i+1}=3y_i+\sigma q\). A displayed repetition is harmless.

On the positive branch the [rank and full-denominator lemma](MISMATCH_EVENT_FACTORS.md) gives
\[
                 r(r+2)\ge \frac{p\log_2q-A}{2A-p},                     \tag{3}
\]
for \(r\) the rank of the numerators. On the negative branch \(A<p\gamma\), where \(\gamma=\log_2 3\), and \(q<3y_i\) for every \(i\). Put \(H_i=\log y_i,\ c_i=\log3+(e_i-1)\log2\) with natural logarithms. Over each forward arc the gcd of its two endpoint \(y\)'s divides the positive affine carry: the signed multiplier of that carry is \(-q\), and each endpoint is coprime to \(q\). Hence (3) of the rank lemma still gives the pair-gcd upper bound by the sum of the \(c_i\), including on a full lap. Each positive rise of \(H\) is at most \(\log(3/2)\). On the circle the total downward variation equals the total upward variation. The enlarged costs
\[
               c_i^*=c_i+(H_i-H_{i+1})_+
\]
dominate \(|H_{i+1}-H_i|\), control all pair gcds, and have sum at most \([A+2(\gamma-1)p]\log2 <(3\gamma-2)p\log2\). Thus the same backwards-interval proof at \(\eta=1\) bounds \(\sum H_i\) by \(r(r+2)\sum c_i^*\). Since \(q<3y_i\), we obtain
\[
                  r(r+2)\ge\frac{\log_2q-\gamma}{3\gamma-2}              \tag{4}
\]
whenever its right side is nonnegative. A numerator equal to one contributes zero height. The full-lap gcd bound ensures all backwards intervals are shorter than a turn regardless of the size of \(q\).

The [actual nonreturn denominator theorem](../literature/PREFIX_CLOSURE_DENOMINATORS.md) gives \(\log_2q_t\ge t-O_n(\log(t+1))\) at every nonreturn of the fixed source. The first \(t\) positive shortcut steps satisfy
\[
                 1\le T^t n\le n\,2^{2g_t-t},
\]
because each odd step grows by at most two and each even step divides by two. Therefore \(p=g_t\ge(t-\log_2 n)/2\) and \(A=t\). In (3), \(p/(2t-p)\) is increasing in \(p\), giving \(r_t(r_t+2)\ge(1/3-o(1))t\). Equation (4) on the negative branch gives the larger asymptotic coefficient \(1/(3\gamma-2)>1/3\). This proves (1) without any assumption on the ultimate ordinary orbit.

## Repeated boundaries in an eventual ordinary cycle

For (2), take a fixed odd cut of the ultimate ordinary cycle after the preperiod. Its block spanning \(P\) shortcut steps has \(d\ge1\) odd departures and affine law \(bx'=ax+c\), where \(a=3^d,\ b=2^P,\ c\) is a fixed positive integer prime to six. The cycle's actual positive fixed phase gives \(b>a\). The prefix of length \(t\) contains \(L=t/P+O_n(1)\) consecutive complete blocks from this cut. At large \(t\) its full multiplier \(3^{g_t}/2^t\) tends to zero exponentially, so its rational periodic closure is positive. The physical odd states of that closure stay between two positive constants depending only on \(n\), as follows.

If \(x_j=T^j n\), the starting center is
\[
           z_t=\frac{x_t-(3^{g_t}/2^t)n}{1-3^{g_t}/2^t}.
\]
It is bounded for large \(t\). Through the actual prefix symbols, the rational state differs from \(x_j\) by \((3^{g_j}/2^j)(z_t-n)\). Both \((x_j)\) and \((3^{g_j}/2^j)\) are bounded on this eventually periodic input. At every odd phase the incoming exponent is bounded by a constant depending on \(n\), including the single cyclic seam joining the possible last and first even runs. The positive incoming odd-step recurrence then gives a uniform positive lower bound. Thus all the absolute odd numerators at the displayed repeated boundaries \(0\le j\le L\) satisfy \(y_j\asymp_n q_t\). The positive determinant gives \(q_t\le 2^t\), and the nonreturn theorem gives \(\log q_t=t\log2-O_n(\log t)\).

Here the repeated physical boundary numerators obey \(b y_{j+1}=a y_j+q_t c\). Use the Lucas-factorial prime-power argument of Weaver's Paper 161, adapted to these actual numerators with moving reduced \(q_t\). Put \(g=\gcd(y_0,q_t c)=\gcd(y_0,c)\le c,\ w_j=y_j/g\). The gcd of \(y_j\) with \(q_t c\) is constant: all its prime divisors are coprime to \(ab\), and the recurrence preserves the gcd at each step. Therefore every \(w_j\) is integral and coprime to \(q_t c/g\). For any prime power \(l^k\) dividing both \(w_i,w_{i+h}\), the iterated recurrence
\[
       b^h w_{i+h}-a^h w_i=(q_t c/g) V_h,\qquad
                              V_h=(b^h-a^h)/(b-a)
\]
forces \(l^k\mid V_h\). For each \(l^k\) with at least one occurrence in \(w_0,\ldots,w_L\), retain the first occurrence and associate each later one to its distinct distance \(h\) from that first one. This charges that level once to each of the indicated \(V_h\)'s, and proves
\[
              \frac{\prod_{j=0}^{L} w_j}{\operatorname{lcm}_{0\le j\le L}w_j}
                         \ \mid\ \prod_{h=1}^{L} V_h .                   \tag{5}
\]
The prime-power and multiplicative-rank methods of this step are prior. Paper 161's stated trajectory theorem is for ordinary integer inputs with the original additive constant; here the growing denominator enters the recurrence through \(q_tc\). Its coprimality and the fixed-source estimate above supply the required normalization and height. [Weaver, Paper 161, §§1–4](https://rstation.ai/problems/collatz/papers/161)

Since \(V_h\le b^h\) and \(g\le c\), (5) implies
\[
  \log\operatorname{lcm}_{j\le L} y_j
        \ge (L+1)\log q_t-O_n(L)-\tfrac12 L(L+1)\log b .
\]
For positive integers of multiplicative rank \(r\) and maximum \(M\), their lcm is at most \(M^r\). For completeness, choose \(r\) pivot prime columns on the rational span of their valuation rows, and take a row basis of largest absolute determinant on those columns. Every row has basis coefficients of modulus at most one by Cramer's rule. Nonnegativity then bounds each prime valuation of every row by the sum of the corresponding basis valuations. The lcm divides the product of the basis integers; rank zero is immediate. Apply this to the displayed boundary states, whose rank is at most \(r_t\) and whose logarithmic maximum is \(\log q_t+O_n(1)\). Since \(L\log b=t\log2+O_n(1)\), the last two inequalities give \(r_t\ge (1/2-o(1))L\), proving (2).

[Exact signed-prefix and Lucas checker](check_prefix_closure_rank.py) · [Finite receipt](prefix_closure_rank_controls.json). It replays all signed rational states on 314 positive and 120 negative closures of actual ordinary prefixes, including 28 ordinary-return controls. Its 442 repeated-boundary systems include 31 nontrivial fixed gcd normalizations and 147 nontrivial lcm-surplus divisibilities. The limiting theorems also use the separately proved nonreturn denominator input.
