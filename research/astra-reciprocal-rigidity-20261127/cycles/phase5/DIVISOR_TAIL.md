# Entropy bound for each large divisor of a Collatz determinant

Use natural logarithms and \(H(p)=-p\log p-(1-p)\log(1-p)\). For chronological binary words of length \(n\) and weight \(u\), write \(C(w)=\sum_{i:w_i=1}2^i3^{u-1-U_i}\), where \(U_i\) counts earlier odd bits, and \(D=|2^n-3^u|\). Set \(p=u/n\), \(B=\max(2,3^p)\), and give this slice the uniform measure. Assume \(1/2\le p<1\). These densities include every ordinary positive cycle: at the minimum odd member \(m\ge1\), the positive cycle product gives \(2^{n/u}\le3+1/m\le4\).

**Theorem.** If \(g\mid D\), \(0\le s\le n\), and \(sB^s<g\), put \(k=n-s\). The exact count of rooted words with \(g\mid C\) is bounded by
\[
       n \sum_{r\ge\lceil pk\rceil}\binom{k}{r}
          \ \le\  n e^{kH(p)} .                                      \tag{1}
\]
Here \(r\le k\) is implicit. For a prescribed residue \(C\equiv a\bmod g\), the same bound holds with one additional factor \(u+1\). In particular
\[
       {\mathbb P}(g\mid C)\le n^{O(1)} g^{-H(p)/\log B}              \tag{2}
\]
uniformly over these densities and divisors; a fixed power of \(n+1\) suffices. For critical positive types the exponent tends to \(H(\log_32)/\log2=0.94995\ldots\). The estimate addresses individual divisors at exponential size. The all-modulus law and the full divisor distribution in [phase4](../phase4/DENOMINATOR_LAW.md) give stronger additive control for smaller divisors.

### Canonical cut and short list

On the periodic lift of \(w\) take a minimum of the periodic function \(F(j)=U_j-pj\). Rotate to start there. Every prefix of the rotated word has weight at least \(p\) times its length, and every suffix has weight at most \(p\) times its length. This follows directly by comparing each endpoint to the minimum and by periodicity at the end of the lap.

Let \(z\) be the suffix of length \(s\). Every terminal segment of \(z\) obeys the same upper weight bound. Its local affine numerator satisfies \(C(z)<sB^s\) for \(s\ge1\): the term at its odd position \(i\) is \(2^i3^{q_i-1}\), with \(q_i\le p(s-i)\) the inclusive suffix odd count, so each such term is strictly below \(B^s\). For \(s=0\) the numerator is zero. For the complementary prefix \(v\) the total weight of \(z\) is known, and
\[
             C(vz)=3^{|z|_1}C(v)+2^{|v|}C(z).
\]
Once a residue of \(C(vz)\bmod g\) is fixed, \(C(z)\) is determined as an integer by its range, since \(g\) is odd. Its length and weight determine \(z\) from \(C(z)\): peel off the lowest occupied power of 2 and repeat. Thus each \(v\) contributes at most one canonical word at that residue. The known lower bound on the weight of \(v\) gives (1) after allowing \(n\) choices of the original cut. The usual binomial upper-tail bound holds at \(p\ge1/2\) also at the endpoints by continuity.

The congruence \(2C(\operatorname{rot}w)\equiv3^{w_0}C(w)\pmod g\) follows from \(g\mid D\). Thus zero is preserved. For a nonzero prescribed original residue and a fixed rotation length \(j\), its canonical value has at most \(u+1\) possibilities, indexed by the number of ones in the rotated-away prefix. This proves the extension to all residues. Choose \(s=\max(0,\lfloor(\log g-\log(n+1))/\log B\rfloor)\) in (1); because \(g\le D< B^n\) this fits within the word. The type cardinality is at least \(e^{nH(p)}/(n+1)\), by the binomial mode bound. These estimates prove (2).

For any \(e\mid D\), take \(g=D/e\). This counts words whose reduced denominator **divides** \(e\), including all smaller divisors of \(e\). Rhin's two-log estimate gives \(B^n/D\ll n^{13.3}\) uniformly at \(0<u<n\), so (1) bounds this whole list by \(n^{O(1)} e^{H(p)/\log B}\). The polynomial bound at fixed \(e\) alone can also be obtained from the classical bound on the minimum cycle state, followed by counting the possible integral numerators. The smaller exponent of the varying height parameter \(e\) is the content of this estimate. For \(g=D\) on critical types, discreteness permits no uniform relative positive asymptotic for the event. [Rozier–Terracol v5, Proposition 6.3](https://arxiv.org/pdf/2502.00948v5#page=19)

### Dimer compositions at the critical ratio

Take a circular arrangement of \(m\) blocks \(10,110\), with \(b\) of the second type and \(\beta=b/m\ge1/2\). Its length and odd count are \(n=2m+b,\ u=m+b\). Put \(B'=\max(2^{2+\beta},3^{1+\beta})\). The model here is uniform on macro arrangements rooted at a block boundary.

At a block boundary minimizing the centered cumulative number of second blocks minus \(\beta\) times the number of blocks used, every prefix has second-block density at least \(\beta\), and each suffix has density at most \(\beta\). In an erased suffix of \(s\) complete blocks the physical length is at most \((2+\beta)s\). For every suffix of complete blocks inside it the physical odd density is at most \(p=(1+\beta)/(2+\beta)\), because \((1+b')/(2+b')\) is increasing in the fraction \(b'\) of second blocks. A suffix starting inside a block differs by at most three bits from an aligned suffix. Therefore each terminal segment of \(\ell\) physical bits has at most \(p\ell+3\) odd positions.

The preceding numerator estimate gives \(C(z)<81s(B')^s\) for \(s\ge1\): each term is bounded by \(3^3\max(2,3^p)^{|z|}\), and there are at most \(3s\) possible positions. Fixed length and weight again recover the erased bit word, whose zeros identify every complete macro block. Thus for \(g\mid D\)
\[
 \#\{\hbox{rooted macro words}:g\mid C\}
  \le m\exp((m-s)H(\beta))\qquad(81s(B')^s<g).
\]
Consequently the probability is at most \(m^{O(1)}g^{-H(\beta)/\log B'}\). At a critical positive macro type \(\beta\to(2\log_32-1)/(1-\log_32)\), the exponent tends to \(h_D=0.3208518\ldots\). Equivalently the list of positive macro words whose reduced denominator divides \(e\mid D\) has size at most \(m^{O(1)}e^{H(\beta)/\log B'}\). Wren calculated the symbolic density and critical composition. The polynomially weighted count per complete divisor follows here from control of the full numerator at the minimizing cut. [Wren's dimer scope](https://rstation.ai/r/collatz/posts/44)
