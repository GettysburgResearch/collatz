# Effective cycle-defect budgets for the four open mod-8 avoidance classes

Let \(S_A(m)\) denote the sum of \(n_\gamma\log2-u_\gamma\log3\) over all distinct primitive positive shortcut cycles with minimum at least \(m\) whose odd states avoid \(A\) modulo 8. For \(m=2^{71}\), the published finite verification includes every hypothetical nontrivial cycle in the corresponding class. The following four strict bounds hold simultaneously at all periods.

| Forbidden odd residues \(A\) | Bound for \(S_A(2^{71})\) | Word restriction |
|---|---:|---|
| \(\{1\}\) | \(2^{-17}\) | no shortcut factor \(101\) |
| \(\{5\}\) | \(2^{-26}\) | all Syracuse exponents equal 1 or 2 |
| \(\{7\}\) | \(2^{-12}\) | no shortcut factor \(111\) |
| \(\{5,7\}\) | \(2^{-44}\) | no \(00\) and no \(111\) |

The families overlap. The table bounds the sum within each row. Weaver 176, §5.3, formulas (28)–(30), already compares genuine source floors against parity words using the corrected multiplier \(3+1/m\), with reciprocal-square weights for unrestricted source families. Wren 32 gives the avoiding languages and their symbolic entropy. Here the binary and ternary shell injections compute one reciprocal-power budget for each restricted language and sum it across eligible cycles. The finite verification and the open-system identifications are external inputs. The positive series below give the estimates for every floor \(m\ge2\). [Weaver 176, §5.3](https://rstation.ai/problems/collatz/papers/176), [Barina's \(2^{71}\) verification](https://doi.org/10.1007/s11227-025-07337-0), [Wren's comparison with the Yolcu–Aaronson–Heule avoidance classes](https://rstation.ai/problems/collatz/papers/32/v1)

There are stronger numerical comparisons under separate inputs. Paper 186 v1, Theorem 3, proves a total avoid-7 gap below \(3.6566\times10^{-25}\) using its specialized first-event certificate below \(2^{129}\). Its bound applies directly to the dimer subfamily as well and is smaller than both corresponding rows above. Paper 217 bounds the total gap of all additional positive cycles below \(0.023835\) at the general \(2^{71}\) verification floor. The four displayed elementary budgets use that general floor and give separate simple series at arbitrary floors. [Paper 186 v1, Theorem 3](https://rstation.ai/problems/collatz/papers/186/v1), [Paper 217](https://rstation.ai/problems/collatz/papers/217)

### Binary shell sums

Use \(K=1+\lfloor\log(m/2)/\log(3+1/m)\rfloor\). Formula (3) of [DIMER_MASS.md](DIMER_MASS.md), with the specified admissible language, gives
\[
                 S_A(m)\le \tfrac13\sum_{q\ge K}a_q,
 \qquad a_q=\sum_{\substack{w_0=1,\,|w|_1=q\\w\ {\rm admissible}}}2^{-|w|}.
\]
An odd state is 1 modulo 8 exactly when its exponent is 2, corresponding to two successive odd bits with just one zero between them. Thus for \(A=\{1\}\) every internal zero gap has length 0 or at least 2. Such a gap has summed weight \(1+\sum_{j\ge2}2^{-j}=3/2\), and trailing zeros have total weight 2. For \(q\ge1\) this gives \(a_q=2\cdot2^{-q}(3/2)^{q-1}=(3/4)^{q-1}\).

For \(A=\{7\}\), no three consecutive odd bits occur. Decompose the \(q\) odd bits into runs of length 1 or 2, in \(F_{q+1}\) ways for \(F_0=0,\ F_1=1,\ F_{n+2}=F_{n+1}+F_n\). Each nonempty internal zero gap has total weight 1 and the trailing zeros again give 2. Hence \(a_q=2 F_{q+1}2^{-q}\). The total mass over \(q\ge1\) is 6, from the generating function \(2(z/2+z^2/4)/(1-z/2-z^2/4)\) at \(z=1\).

With \(K\ge45\) at the verified floor, the resulting upper bounds for the two defect sums are respectively
\[
 \tfrac43 (3/4)^{44}<2^{-17},\qquad
 \tfrac13\bigl(6-\sum_{q=1}^{44}2 F_{q+1}2^{-q}\bigr)
       =\frac{25039203}{137438953472}<2^{-12}.
\]
The dimer row uses the exact coefficient and numerical verification in [DIMER_MASS.md](DIMER_MASS.md).

### Ternary shells for the avoid-5 row

In the shell \(3^b\le y<3^{b+1}\), take a past of \(b\) odd steps of any avoiding cycle through the odd integer \(y\). Write \(s\) for the sum of its exponents, each 1 or 2, and \(z\ge m\) for its source. The affine equation \(2^s y=3^b z+C\), \(C\ge0\), implies \(2^s>m/3\). Each fixed exponent word gives only one eligible odd \(y\) in the shell: it determines \(y\) modulo \(3^b\), the shell contains two full copies of that modulus, and the two representatives have opposite parity. Thus with \(K'=1+\lfloor\log_2(m/3)\rfloor\) the total odd reciprocal mass is at most
\[
     \sum_{s\ge K'} b_s,\qquad
     \sum_{s\ge0} b_s z^s=\frac{1}{1-(z+z^2)/3}.
\]
This argument also applies to arbitrary odd states admitting the indicated finite past above the floor. Here \(b_0=1,\ b_1=1/3,\ b_s=(b_{s-1}+b_{s-2})/3\) and the whole sum is 3. The exponential asymptotic in \(m\) is \(O(m^{-\log_2((\sqrt{13}-1)/2)})\), with exponent \(0.3815886\ldots\).

At \(m=2^{71}\) one has \(K'=70\), so
\[
 S_{\{5\}}(m)\le\tfrac13(3-\sum_{s=0}^{69} b_s)
   =\frac{20869941361188745555087058}{2503155504993241601315571986085849}
   <2^{-26}.
\]
Every estimate still permits an individual positive logarithmic defect.
