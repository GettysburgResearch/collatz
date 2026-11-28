# Two adjacent Mersenne moduli distinguish one genuine boundary source

**PROPOSED written theorem, unconditional.** Write \(B=2^k\). Fix a positive ordinary anchor \(d\). Look for positive \(n\) satisfying the simultaneous congruences
\[
              n\equiv d\pmod {B-1},\qquad 2n\equiv d\pmod{2B-1}.       \tag{1}
\]
The positive integer \(Bd\) always qualifies. For every \(0<\delta<1\), and all sufficiently large \(k\), if
\[
            \log_2 n\le (1-\delta)k^2
\]
then either \(n=Bd\), or any first hit of 1 from \(n\) requires more than \(\sqrt{\delta k}/64\) odd departures. This holds simultaneously for \(\log_2(d+1)\le\delta k/128\), with the onset depending only on \(\delta\). Thus the [centred boundary amplitude](CENTRED_BOUNDARY_AMPLITUDE.md) of every competing source is \(O(\exp(-c\sqrt{\delta k}))\), while the canonical one has exactly \(W(d)\). The two moduli are coprime, and their product is about \(2^{2k+1}\). The height permitted in this theorem is exponentially larger than that product.

The leading constant one on the \(k^2\) scale is sharp, even if the competition must exceed the canonical amplitude. For the true convergent anchor 37 and infinitely many \(k\), there is an ordinary source satisfying (1), with three odd departures before 1, amplitude tending to \(36/85>W(37)=8/37\), and \(\log_2 n=k^2+2k+O(1)\). These witnesses and all comparisons use unmodified positive integer trajectories.

## Positive carries modulo the first Mersenne number

Suppose a physical word first reaches 1 at date \(t\) with \(p\) odd departures, at positions \(0\le s_0<\cdots<s_{p-1}<t\). Even starting inputs are allowed. Its actual positive numerator gives
\[
         2^t=3^p n+\sum_{i=0}^{p-1}3^{p-1-i}2^{s_i},
                \qquad t\le\log_2 n+2p.                                \tag{2}
\]
The bound follows since an odd step is at most twice the current state while an even one halves it. It includes \(p=0\).

Put \(D=\lceil\log_2(d+1)\rceil\), \(\nu=v_2(d)\) and \(N=D+4(p+1)^2\). Modulo \(B-1\), substitute \(d\) for \(n\) in (2). Write all nonnegative coefficients \(3^pd\) and \(3^{p-1-i}\) in binary, and put one token in the corresponding residue position modulo \(k\) for every one-bit, with the exponent \(s_i\) added for the latter coefficients. There are at most \(N\) tokens, by summing their binary lengths. Suppose for the moment \(\nu+N<k/2\).

While a position has two tokens, merge a pair into one at the next position cyclically. Each merge decreases the number of tokens and preserves the residue modulo \(2^k-1\). The final occupied subset has between one and \(N<k\) positions. Its binary representative is strictly between zero and \(2^k-1\), so by (2) it consists of the single bit at \(t\bmod k\). Along its ancestry each original token moved forward by at most \(N-1\) positions. There is an original token at \(\nu\), since \(3^pd\) has lowest bit \(\nu\). There is also a token at each \(s_i\bmod k\), since all its coefficients are odd. Represent \(t\bmod k\) by a signed integer \(r_t\in[\nu,\nu+N]\), and each \(s_i\bmod k\) by an integer \(r_i\in[r_t-N,r_t]\). This simultaneous localization uses positivity, including the physical sign of every offset term. Merely having few nonzero summands with arbitrary signs would not force it.

Write \(t=Lk+r_t\) and \(s_i=m_i k+r_i\). Then \(0\le m_i\le L\) and \(L\ge0\), since the original exponents are nonnegative, \(s_i<t\), and the signed representatives lie in an interval of length less than \(k\). Define the rational polynomial
\[
   P(z)=3^{-p}\left(2^{r_t} z^L
                    -\sum_{i=0}^{p-1}3^{p-1-i}2^{r_i}z^{m_i}\right).
                                                                         \tag{3}
\]
Thus \(P(B)=n\). After collecting equal degrees, all coefficients below \(L\) are nonpositive, and the leading coefficient is positive because \(P(B)>0\). The case \(p=0\) gives just one monomial.

## The second evaluation and its height budget

Set \(J=N+\nu\) and \(D_0=3^p2^J\). All coefficients of \(D_0P\) are integers. Their sum of absolute values is at most \(2^{2J}(1+\sum_{i<p}3^{p-1-i})\le 2^{2J+1}3^p\). The integer \(D_0d\) is at most \(3^p 2^{J+D}\). In particular, with \(H=2J+D+2p+4\), both \(|D_0(P(1)-d)|\) and \(2^{-L}|2^LD_0(2P(1/2)-d)|\) are less than \(2^H\). Only the positive base and integer exponents in the monomials are used to bound the evaluations.

The first integer is divisible by \(B-1\) from (1), since \(D_0P(B)\equiv D_0P(1)\). The second unscaled integer \(2^L D_0(2P(1/2)-d)\) is divisible by \(2B-1\), since \(2B\equiv1\bmod(2B-1)\). Clearing \(D_0\) before substitution avoids any unit assumption on its power of three. If \(H+L<k-1\), each integer has absolute value less than its respective modulus and therefore vanishes. We get
\[
                         P(1)=d=2P(1/2).                                \tag{4}
\]

Here are explicit margins under the stated assumptions. If \(p\le\sqrt{\delta k}/64\) and \(\log_2(d+1)\le\delta k/128\), then for all sufficiently large \(k\) in terms of \(\delta\), \(J<\delta k/32\), \(H<\delta k/4\), and \(\nu+N<k/2\). Also \(L\le t/k\le(1-\delta)k+2p/k\) by (2). These give \(H+L<k-1\). In particular the argument also works along any sequence with \(p^2+\log(d+1)=o(k)\) and \(t/k\le(1-\delta)k\).

Degree zero contradicts (4) since \(d>0\). For \(L\ge1\) write \(P(z)=a z^L-\sum_{m<L}b_m z^m\), where \(a>0,b_m\ge0\). Positivity gives
\[
           2^{L-1}d=2^L P(1/2)
                 =a-\sum_{m<L}2^{L-m}b_m\le P(1)=d.
\]
Thus \(L=1\) and equality forces every lower coefficient to vanish. Equation (4) now gives \(P(z)=dz\), hence \(n=Bd\). This proves the theorem.

## The single-modulus window and the sharp counterfamilies

With only \(n\equiv d\bmod (2^k-1)\), write \(n=(2^k-1)b+d\) at large \(n\), \(b\ge1\). For \(b\ne d\), the signed ordinary integer \(z=d-b\ne0\) shares its first \(k\) real shortcut parity bits with \(n\). The signed map never takes a nonzero integer to zero, and an odd departure satisfies \(|Tz|\le2|z|\). Consequently \(1\le|T^kz|\le |z|2^{2q_k(z)-k}\). Since \(n\ge2^k\), no departure before date \(k\) occurs at 1. The positive amplitude therefore obeys
\[
             W(n)\le(5/6)^{(k-\log_2|d-b|)/2}.                         \tag{5}
\]
For fixed \(d\), every noncanonical representative with \(1\le b\le o(2^k)\) has amplitude tending uniformly to zero. The canonical \(b=d\) has \(W(2^kd)=W(d)\). This isolates the low anchor through all heights \(o(4^k)\).

For an even \(E>0\) divisible by six put
\[
                 y_E=(340\cdot2^E-7)/9.
\]
It is an odd positive integer. Directly,
\[
         y_E\ \xrightarrow{\;2\;}\ (85\cdot2^E-1)/3
              \ \xrightarrow{\;E\;}\ 85
              \ \xrightarrow{\;8\;}\ 1,
\]
where arrows are true odd steps labelled by their exact positive gaps. Hence \(W(y_E)=2^{E+4}/y_E\to36/85\). The true first-hit gaps of 37 are \(4,1,1,2,3,4\), yielding \(W(37)=8/37\). For \(k\equiv3\bmod6\) take \(E=2k\). Then \(2^k+1\equiv0\bmod9\), so
\[
             y_E-37=(340/9)(2^E-1)
\]
is divisible by \(2^k-1\). This is a noncanonical witness at quadratic height \(y_{2k}\sim(340/9)(2^k-1)^2\), exceeding the anchor's amplitude in the limit.

For the paired moduli take \(k\equiv8\bmod18\) and \(E=k(k+1)\). The two Mersenne numbers are coprime since \(2B-1=2(B-1)+1\), and both divide \(2^E-1\). Moreover \((2^E-1)/(2^k-1)=1+2^k+\cdots+(2^k)^k\) is a multiple of nine: \(3\mid 2^k-1\) and \(9\mid k+1\), so grouping the terms in nines gives a sum zero modulo nine in each group. Indeed if \(u\equiv1\bmod3\), then \(u^i\equiv1+i(u-1)\bmod9\), and the first nine powers sum to zero modulo nine. The other Mersenne number \(2^{k+1}-1\) is prime to three. Thus \(9(2^k-1)(2^{k+1}-1)\) divides \(2^E-1\). Now \(y_E\equiv37\) modulo both and \(n=2^k y_E\) satisfies (1) at \(d=37\). Its even prefix preserves its amplitude. Its log-height is \(E+k+O(1)=k^2+2k+O(1)\), as claimed. This is also the scale of the next unconditional pure dyadic lift \(2^{E+k}d\), since \(E\) is the least common multiple of the two consecutive exponent periods.

## The remaining boundary question

As far as the paired test is concerned, a positive lower bound on the maximum actual amplitude below the displayed horizon would force the canonical source itself to reach 1. The proof supplies the rigidity direction only. Standard fixed-target progression counts select true predecessors of 1 with odd depth proportional to the logarithm of the source height and position them in a supplied odd residue class. They do not give a predecessor with the small odd depth required here. A lower estimate at a fixed ordinary anchor would have to exploit its arithmetic position in both moduli. Even an exponentially numerous collection of other true predecessors would not on its own supply such a shallow witness. [PR215, fixed-target CRT floor and clock range](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/ARITHMETIC_PROGRESSION_FLOOR.md)
