# A least-failure rank for the single directed transfer

**PROPOSED written reduction on ordinary positive integers.** Use the shortcut map \(T(2s)=s,\ T(2s+1)=3s+2\), let \(C\) be the basin of 1, and write \(x\sim y\) when their forward orbits meet, allowing different clocks. For \(v=9k+2\), set
\[
 h=v_3((4v+1)/9),\qquad b=(4v+1)/(9\,3^h),\qquad r(v)=2^h b.
\]
Here \(b\) is odd and coprime to 3. The two directed arms at PR193 are \(A=4v\) and \(B=8v+1\). The first is in the component of \(v\), and \(T^3 B=9v+2\).

**Rank criterion.** Universal convergence is equivalent to checking \(v\in C\Rightarrow 9v+2\in C\) only for those \(v=9k+2\) for which a specified positive ordinary representative \(w(v)\sim 9v+2\) satisfies
\[
                         22w(v)\ge r(v).                       \tag{1}
\]
Any explicit selection is allowed. With a menu, it suffices to check parameters for which every available representative passes (1). This statement makes a least-failure argument across the complete finite descent certificate. A small representative in a different component gives no pruning.

**Even lifts.** Take \(v=2^m a\), \(a\) odd, \(m\ge1\). One explicit choice is
\[
 w(v)=9\,3^{\lfloor m/2\rfloor}a+\epsilon_m,\qquad
 \epsilon_m=\begin{cases}2&m\text{ even},\\1&m\text{ odd}.\end{cases}      \tag{2}
\]
It is the actual vertex \(T^m(9v+2)\); also \(T^m v=a\). In the remaining global criterion, for each fixed ordinary \(a\) the list of such exponents is **finite and effectively bounded**, with an absolute effective constant:
\[
           m\ll (1+\log a)\log(2+\log a).                         \tag{3}
\]
No convergence assumption on \(a\) is needed in obtaining the bound. In testing the directed implication one can of course use only \(a\in C\). A cutoff uniform independently of \(a\) is not obtained.

**Odd lifts.** Take odd \(v=(2^m a-1)/3\), where \(a\) is positive odd and \(2^m a\equiv7\pmod {27}\), \(m\ge1\). The two physical arms \((v,9v+2)\) land after exactly \(m\) steps at
\[
                         (a,3^{m+1}a-1).                            \tag{4}
\]
Thus a single known convergent odd target leaves a lacunary sequence in this half. For every fixed such \(a\) coprime to three, a positive proportion of its admissible exponents have explicit representatives below the cutoff in (1). The remaining odd lifts are open even on the ray \(a=1\). The [forced peak](PEAK.md) applies to the full undirected graph between the two specified original arms.

## From the complete certificate to the rank

Use PR193 at 67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e, directory research/astra-global-resolution-20261124/rewriting. Its 291 affine paths cover every \(n>1\), end below \(n\), and use ordinary moves and precisely the extra directed move \(8s-1\to9s-1\), \(s\ge1\). Write \(F(s)\) for \(9s-1\in C,\ 8s-1\notin C\). The path table and its exact ratio replay bound **each input of an extra move** by \((20970919/122875)n<171n\). Therefore \(s=(\text{move input}+1)/8<22n\). The ratio is a bound on all lifts of a leaf: for positive affine functions the ratio on \(t\ge0\) lies between its value at zero and its limit. [Table and proof](https://github.com/GettysburgResearch/collatz/blob/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/rewriting/SEVEN_RETURN.md) · [Exact ratio replay](https://github.com/GettysburgResearch/collatz/blob/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/rewriting/check.py)

If convergence fails, the certificate supplies some \(F(s)\). Choose its least parameter \(r\). For every \(z>0\) with \(22z<r\), strong induction on \(z\) gives \(z\in C\): the endpoint of its table path is smaller, and every directed move used has parameter strictly less than \(r\), so membership propagates backwards. The same physical steps \(T(18s-1)=27s-1\), \(T(16s-1)=24s-1\) show \(F(3s)\iff F(2s)\). Thus \(3\nmid r\). Also \(T^2(8r-1)=18r-1\); consequently \(F(r)\) asks for distinct directed colors at \((9r-1,18r-1)\). For \(r=2^h b\) with \(b\) odd, applying \(h\) actual odd steps on both arms replaces this pair by the pair at \(r'=3^h b\). If \(r'=4k+3\), the two arms meet after two and three steps respectively at \(27k+20\). Otherwise \(r'=4k+1\), so the arms are \((4v,8v+1)\) with \(v=9k+2\). Since \(3\nmid b\), the displayed definition recovers exactly \(r(v)=r\). Conversely for each such \(v\), these physical exchanges identify the two corresponding colors with the pair at \(r(v)\). Any witness \(w\sim9v+2\) is then outside \(C\) at the least failure, forcing (1). This proves the criterion; the forward implication follows by universal convergence.

## Discharging the even tail by a 3-adic logarithm bound

The two-step identity \(T^2(4u+2)=3u+2\) proves (2) by peeling pairs of bits. For odd \(m\), remove the last even step from a number of the form \(2u+2\). From (1), using \(4v+1\ge 4\,2^m a\) and \(9\,3^{\lfloor m/2\rfloor}a+2\le 11(\sqrt3)^m a\), we get
\[
     m\log(2/\sqrt3)\le h\log(3/2)+\log(22\cdot 9\cdot11/4).
\]
Here \(h+2=v_3(2^{m+2}a+1)\) and \(3\nmid a\). Apply Kunrui Yu, *Linear forms in p-adic logarithms III*, Corollary to Theorem 1, pp. 244–245, with \(p=3\), rational bases \(2,-a\) and exponents \(m+2,1\). The product minus one is nonzero. Take \(A_1=3,A_2=\max(3,a)\); the last exponent has minimal 3-adic valuation, so the corollary's additional logarithmic factor uses \(A=A_1=3\). It follows with an absolute effective constant that \(h+2\ll (1+\log a)\log(m+3)\). This includes \(a=1\). The inequality \(m\ll D\log(m+3)\) with \(D=1+\log a\ge1\) implies \(m\ll D\log(2D)\), by monotonicity of \(m/\log(m+3)\) beyond an absolute threshold. This proves (3). All cited constants could be evaluated from Yu's formula. [Primary theorem](https://www.numdam.org/article/CM_1994__91_3_241_0.pdf)

## Ordinary smaller representatives on each odd ray

On the odd row the left arm takes one odd step to \(2^{m-1}a\), then halves to \(a\). The right arm starts at \(3\cdot2^m a-1\); its successive values through clock \(m\) are \(3^{i+1}2^{m-i}a-1\). This gives (4). The all-odd power formula is classical. [Lagarias, overview, §1](https://www.ams.org/bookstore/pspdf/mbk-78-prev.pdf)

For a concrete additional menu, suppose \(16r(v)\equiv1\pmod{3^{15}}\). Set
\[
            w=2^{15}(16r(v)-1)/3^{15}-1.
\]
This is positive. Its first 15 odd steps lead to \(16r(v)-2=2(8r(v)-1)\), so \(w\sim9v+2\) by the physical exchanges above. As \(22\cdot16\cdot 2^{15}<3^{15}\), it satisfies \(22w<r(v)\). This disposes of the whole indicated ternary unit class in the global criterion.

For a fixed odd \(a\) prime to three, even the subfamily \(h=0\) here contains an arithmetic progression of exponents. Let \(c\) be the inverse of 16 modulo \(3^{15}\). Require \(2^{m+2}a\equiv1+27c\pmod{3^{18}}\). The number 2 generates the units modulo \(3^{18}\): \(4=1+3\) has order \(3^{17}\) by repeated cubing, and 2 has even order. Thus there is one residue class of \(m\) modulo \(2\cdot3^{17}\), contained in the original admissible class modulo 18. On it \((4v+1)/9=(2^{m+2}a-1)/27\equiv c\pmod{3^{15}}\) is a ternary unit, so \(h=0\) and the claimed window applies. This gives relative proportion \(3^{-15}\) among admissible exponents, independently of \(a\). The route supplies an actual ordinary smaller representative, and its use in (1) requires the least-failure argument. It does not certify convergence of each ray term solely from its size.

For \(a=1\) all odd-lift admissible exponents have \(m=16\bmod18\). The post-excursion value is \(3^{m+1}-1\). One further exact exchange when \(N=m+1\) is odd gives \(T^2(3^N-1)=(3^{N+1}-1)/4\). Thus testing these terms is equivalent to testing \(3^{18j}-1\), \(j\ge1\), on this fixed subray. The 3-adic bound that pruned the even lifts cannot give comparable real contraction after the all-odd excursion: interchanging \(3^N-1\) with \(3^{N+1}-1\) only shifts the exponent, and the number of immediately available halvings is \(v_2(3^{18j}-1)=3+v_2(j)\). The other odd lifts and the varying ordinary targets in (3) also remain. The estimates above do not bound the previously identified undetected original head mass.
