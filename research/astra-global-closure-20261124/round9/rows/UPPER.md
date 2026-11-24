# A high-endpoint upper bound for the exact-row maximum

**PROPOSED written theorem.** Fix the balanced row with \(b\ge1\) odd inputs and \(2b\) shortcut steps, and let \(N_b(q,\epsilon)\) count positive unit sources ending at the supplied odd unit \(q\) with relative carry at least \(\epsilon\). Set
\[
                    h=\left\lceil\log_{3/2}\big((1+\epsilon q)/2\big)\right\rceil .
\]
For \(1\le h<b\) one has the finite bound
\[
                   N_b(q,\epsilon)\le \binom{2b-1}{b-h-1}.                    \tag{1}
\]
For \(h\ge b\) the count is zero. For \(h\le0\) the same method gives the total word count \(\binom{2b-1}{b-1}\). The internal height-or-repeat filter from PR201 can only decrease the count. [Exact source count and row filter](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md)

In particular, for every fixed rational \(0<\epsilon<1\) and every sufficiently large \(b\),
\[
          \max_{q\ge(3/2)^{351b/352}} N_b(q,\epsilon)<2^{\lceil b/32\rceil}.
                                                                            \tag{2}
\]
The maximum ranges over unit endpoints. The proof gives a strict saving in the exponential rate uniformly throughout this height range.

## Carry forces a large excursion of the same word

Encode an even shortcut input by \(+1\) and an odd input by \(-1\). Each balanced word is a walk from zero to zero in \(2b\) steps beginning at \(-1\). Let \(H\) be the maximum height taken by its partial sums, including the two endpoints. Index the odd inputs backwards. At the \(r\)-th odd input counted from the end, its remaining suffix, including this input, has \(r\) odd inputs and some \(D_r\) even inputs. The height immediately before that suffix is \(r-D_r\), since the full word is balanced. Thus \(D_r\ge\max(0,r-H)\).

An odd step contributes \(1/2\) immediately to the affine carry. Each later odd input multiplies it by \(3/2\) and each later even by \(1/2\). Consequently the carry in the literal equation \(q=(3/4)^b x+\beta\) obeys
\[
\begin{aligned}
 \beta
 &= \sum_{r=1}^b \frac{3^{r-1}}{2^{r+D_r}}\\
 &\le \sum_{r=1}^{H}\frac{3^{r-1}}{2^r}
       +2^H\sum_{r=H+1}^b\frac{3^{r-1}}{4^r}\\
 &\le (3/2)^H-1+2^H(3/4)^H
   = 2(3/2)^H-1.
\end{aligned}
\]
Both sums telescope, with successive terms from \((3/2)^r\) in the first and \((3/4)^r\) in the second. Empty sums are allowed. In particular \(\beta\ge\epsilon q\) implies \(H\ge h\).

There is a separate kernel proof of the carry bound at the supplied positive integer. Let \(L\) be the running maximum of the even surplus minus its current value. An odd input increases \(L\) by one and multiplies \(1+\beta\) by \(3/2\). An even input sends \(L\) to \(\max(0,L-1)\) and \(1+\beta\) to \((1+\beta)/2+1/2\). These two updates preserve \(1+\beta\le2(3/2)^L\). On an even step from level \(j+1\) the required inequality follows from \((3/2)^j\ge1\). At a balanced endpoint \(L=H\). For a rational cutoff \(p/r\), the kernel combines this bound with the literal affine row from \(x\) to \(q\) to give \((r+pq)2^H\le2r3^H\). [Physical endpoint and carry theorem](BarrierEnvelope.lean)

Reflect the portion of the walk **after its first visit** to the integer level \(h>0\). The reflected walk ends at \(2h\) and still starts with a down step. Conversely every length-\(2b\) walk beginning with a down step and ending at \(2h\) visits \(h\), and the same reflection recovers a balanced walk. There are \(b-h\) down steps in the reflected path, including its fixed initial one. Choosing the other down steps gives the right side of (1), and gives no walk when \(h\ge b\). Each counted ordinary source yields such a word. For a fixed word and terminal the affine equation determines a unique source. This proves the upper bound even after allowing every binary word compatible with the initial bit.

## The exponential threshold

Let \(C_\epsilon=|\log_{3/2}(\epsilon/2)|+1\). In the range of (2), \(r=b-h-1\le b/352+C_\epsilon\). The cases \(r<0\) and \(r=0\) give counts zero and at most one, respectively. For \(r>0\), use \(\binom{2b-1}{r}\le (2eb/r)^r\), which follows from \(\exp(r)\ge r^r/r!\). The function \(r\log(2eb/r)\) is increasing for \(0<r<2b\). On taking base-two logarithms per \(b\), the limsup of the endpoint-uniform upper bound is at most
\[
                \frac{\log_2(704e)}{352}
                        <\frac{11}{352}=\frac1{32}.
\]
Indeed \(e<11/4\) and \(704\cdot11/4=1936<2^{11}\). This proves (2). The same reasoning, using the binomial entropy bound, works for any fixed \(\delta\) with \(2H_2(\delta/2)<1/32\) when \(q\ge(3/2)^{(1-\delta)b}\) and \(0<\delta<1\).

The [independent enumerator](check.py) checks the carry bound on every balanced first-odd word through its reported cutoff, and checks equality of the barrier histogram with the reflected binomial counts. The finite reflection count and its asymptotic consequence are written mathematics.

The remaining interval \(1<q<(3/2)^{351b/352}\) contains every terminal in PR201's exhibited failure family for all sufficiently large \(b\). In that construction \(q_i=U^i(q_0)\) for a fixed \(q_0\), where \(i=b-m-2\) and \(m\ge\lceil b/32\rceil\). Every ordinary odd step obeys \(U(z)+1\le(3/2)(z+1)\), so \(q_i+1\le(q_0+1)(3/2)^{31b/32-2}\). Here \(31/32=341/352<351/352\). Fixed cycle targets also stay below the cutoff. PR206's fixed gate with \(m=\lfloor b/12\rfloor\) gives the analogous endpoint ceiling with exponent \(11b/12+O(1)\). Proving the opposing bound throughout the lower interval still requires an additional argument. [Finite survival and explicit examples](README.md)
