# A quantitative moving gate clock for actual integers

**PROPOSED written theorem.** Fix \(0<\epsilon<1\). There exist
computable \(c,\eta>0\), depending only on \(\epsilon\), such that
uniformly for integers \(1\le t\le c\log X\) the following holds.
Among all actual sources \(m\ge X^\epsilon\) with
\(q=H^t(m)\in[X,2X)\), use mass \(1/(m\log2)\) and record the \(t\)
internal words in outward order. Its distance in the \(\ell^1\) norm
from the probability law \(p^{\otimes t}\) is \(O_\epsilon(X^{-\eta})\).
The unrestricted all-source mass consequently satisfies the exact
asymptotic decomposition
\[
 \sum_{m:\ H^t(m)\in[X,2X)}\frac1m
  =\log2+\sum_{m<X^\epsilon:\ H^t(m)\in[X,2X)}\frac1m
     + O_\epsilon(X^{-\eta}).
\]
The calculations below use the actual half-open physical shell, a
deterministic positive orbit at every counted source, and all possible
individual internal lengths. The mass of small sources in the last
display is left explicit.

## Uniformity for a light tuple

Write \(D=\log(3/2)\), and fix \(0<\kappa\) so small that
\(\kappa\log3<1/3\) and \(\kappa D<(1-\epsilon)/3\).
Set \(K=\lfloor\kappa\log X\rfloor\). For a tuple with total internal
length \(J\le K\) and sum of internal letters \(S\), its slope is
\(a=4^t2^S/3^J\). Write its affine endpoint as \(m=a(q-b)\).
Each elementary step \(y\mapsto\alpha y-\beta\) has
\(0\le\beta\le1\). Every prefix slope is at least \((2/3)^J\).
Dividing each accumulated subtraction by the slope of its prefix
through that step proves \(0\le b\le(t+J)(3/2)^J\).
All implementing classes give positive integer paths for \(q\ge1\),
since the allowed branches preserve positivity on their residue classes.
The size bound in the [fixed-clock theorem](FIXED_GATE_CLOCKS.md)
gives \(m\ge X(2/3)^K>X^\epsilon\) for sufficiently large \(X\).

There is exactly one ternary class \(q\bmod 3^J\) for the tuple.
Partial summation of the class count \(u/3^J+O(1)\) on \([X,2X)\)
gives
\[
 \frac{1}{\log2}\sum_{q\ {\rm in\ class}}\frac{1}{m}
 =4^{-t}2^{-S}
      \left(1+O\!\left(\frac{3^J+b}{X}\right)\right).
\]
Here \(1/(q-b)=q^{-1}(1+O(b/X))\) uniformly. Thus the sum of
absolute errors over *all* light tuples is \(O_\epsilon(X^{-\eta_1})\)
for some \(\eta_1>0\). Relative error allows summation without a
factor for the word count.

Under the product probability the \(t\) internal lengths are
independent geometric variables \(G_i\) with
\(\Pr(G_i=j)=(3/4)^j/4\). Choose
\(s=\frac12\log(4/3)\) and \(B=[4(1-3e^s/4)]^{-1}>1\).
Then \(\Pr(\sum G_i>K)\le e^{-sK}B^t\). Hence for
\(c< s\kappa/(2\log B)\) the omitted product tail is a negative
power of \(X\).

## A uniform long-path bound in physical shells

On an actual path of internal length \(J\), the ratios obey
\(3^t(2/3)^J\le m/q\le4^t(4/3)^J\).
For \(m\in[M,2M)\) put \(r=|\log(M/X)|\).
The preceding inequalities imply
\(r\le J+t\log4+\log2\), since both absolute logarithmic
per-letter bounds are less than one. Thus every heavy tuple has
\(J\ge K\) and \(J\ge r-t\log4-\log2\).
Take nonnegative integer part
\[
 k=\left\lfloor\min\bigl(
        \max(K,r-t\log4-\log2),\,(\log M)/(2\log3)\bigr)\right\rfloor .
\]
The first \(k\) slow \(F\)-steps have at most \(t\) gates, including
the gate steps that initiate the blocks in outward order. Indeed the
whole forward passage has \(J+t\) steps, precisely \(t\) of them gates.
A prescribed slow word has one dyadic class with measure equal to
the product of the letter probabilities \(1/2,1/4,1/4\).
The error in counting a class in \([M,2M)\) is at most one.
After dividing by \(M\), its shell's heavy \(1/m\)-mass is bounded by
\[
    \Pr(\mathrm{Binomial}(k,1/4)\le t)+3^k/M.
\]
Every source occurs at most once, by determinism.

Use dyadic \(M\) with \(M>X^\epsilon/2\).
Choose \(c\) smaller, if needed, so
\(c<\min(\kappa/32,\epsilon/(64\log3),\kappa/(8\log4))\).
For large \(X\), \(t\le k/8\). Markov's inequality on
\(2^{-\mathrm{Binomial}(k,1/4)}\) gives the first probability at
most \((2^{1/8}7/8)^k\); its base is less than one.
The second term is at most \(M^{-1/2}\).
As \(t\log4+\log2\le K/2\) for large \(X\),
\(\max(K,r-t\log4-\log2)\ge\frac12\max(K,r)\).
Hence the bound for a single shell is
\[
  O\!\left(e^{-\delta\max(K,r)}+M^{-\delta'}\right)
\]
with absolute positive \(\delta,\delta'\).
Summing over dyadic \(M>X^\epsilon/2\) costs
\(O((K+1)e^{-\delta K}+X^{-\epsilon\delta'})\).
This is a power saving and establishes the theorem.

## Real-height fluctuations

Write \(L=\log(4\,2^{S(w)}/3^{|w|})\) for one limiting block and
\(L_1,\ldots,L_t\) for independent copies. On every light tuple
\[
    \log(m/q)=\sum_{i=1}^t L_i+O_\epsilon(X^{-\eta_2}).
\]
Consequently for every bounded 1-Lipschitz \(f\) with
\(\|f\|_\infty\le1\), its source-truncated harmonic average of
\(f(\log(m/q))\) differs from the product average
\(\mathbb Ef(\sum_iL_i)\) by \(O_\epsilon(X^{-\eta_3})\).
This follows from the preceding light error and the two heavy tails.
For \(t\to\infty\) in the theorem's range the normalized displacement
\((\log(m/q)-t\mu)/(\sigma\sqrt t)\) thus tends in law to a standard
normal. With \(b_0=\log2\), the constants are
\[
   \mu=3\log(4/3),\qquad
   \sigma^2=\tfrac23 b_0^2+
       12\bigl(\tfrac43 b_0-\log3\bigr)^2 .
\]
Indeed \(L=\log4+\sum_{h=1}^G (A_h\log2-\log3)\), with \(G\)
geometric of mean 3 and variance 12, and independent
\(A_h\in\{1,2\}\) of probabilities \(2/3,1/3\).
Use the usual iid central limit theorem. No moment assertion about
all-source unbounded tails is needed.

A fixed positive integer whose moving root \(H^t(m)\) enters
\([X,2X)\) eventually lies below the cutoff \(X^\epsilon\). Its
mass \(1/m\) then contributes entirely to the explicit correction.
The estimate on large sources cannot decide if the gate path of
that particular integer enters infinitely many such shells.
