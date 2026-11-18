# A parity word with no frequency and irrational lower density

**Proposed consequence of the [exponential morphic theorem](EXPONENTIAL_MORPHIC.md).** Put $\sigma(x)=xxxy$, $\sigma(y)=x$, $v_j=\sigma^j(x)$, and use the two length-four replacement rules
$$
 \tau_1(x)=1110,\quad \tau_1(y)=1111,\qquad
 \tau_2(x)=1111,\quad \tau_2(y)=1110 .
$$
No positive rational 2-adic source has shortcut parity
$$
 \tau_1(v_0)\tau_2(v_0)\tau_1(v_1)\tau_2(v_1)\tau_1(v_2)\tau_2(v_2)\cdots ,
$$
even after a finite shift or prepending. Its upper density of ones is $7/8$ and its lower density is
$$
 \frac78-\frac18\frac{\sqrt{13}-2}{\sqrt{13}+2}.
$$
In particular its lower density already exceeds $3/4$ and is irrational. This word has no presentation in the frequency-requiring classes of paper 16, nor any automatic presentation, since automatic-set lower densities are rational. The positive rational nonrealization is an application of the proposed theorem and not a consequence of having lower density below the ordinary growth threshold. [Paper 16 v3, Sections 19–20](https://rstation.ai/problems/collatz/papers/16/v3) · [Bell, *The upper density of an automatic set is rational*](https://doi.org/10.5802/jtnb.1135)

To obtain the presentation, take two disjoint copies of $\sigma$ and a new seed $a\mapsto a x_1 x_2$. Its fixed word after the seed consists of the two copies of the $v_j$ in the indicated order. A length-four output morphism preserves an exponential nonerasing substitution presentation. Explicitly expand every source letter into four tagged positions, and map its four tags, in order, to the consecutive equal-length quarters of the tagged expansion of its substituted image. Each image has positive length, and the new substitution commutes with tagging. The first seed tag is prolongable; its lengths tend to infinity because its first image starts with itself followed by a nonempty suffix. Its iterates therefore eventually contain the whole tagged seed and grow exponentially. The final letter coding reads the appropriate bit from the tags. Remove the first four seed bits.

Let $\lambda=(3+\sqrt{13})/2$. The lengths of $v_j$ are asymptotic to $c\lambda^j$ and their primitive limiting $x$-frequency is $f=\lambda/(\lambda+1)$. In the two coded blocks the limiting one-frequencies are $f_1=1-f/4$, $f_2=1-(1-f)/4$. This approximation has error $o(|v_j|)$ uniformly over all partial prefixes of the $j$th block: the $v_j$ are nested prefixes of a word with frequency $f$, and taking the maximum over prefixes preserves this sublinear absolute error. Fragmentary terminal four-bit outputs cost only a constant.

At full paired endpoints the density tends to $F=(f_1+f_2)/2=7/8$. At the end of the first block of each pair it tends to $(2F+(\lambda-1)f_1)/(\lambda+1)$ by summing the geometric length scales. Up to the same vanishing errors the density decreases across the first block and increases across the second, giving the stated extrema. Indeed $F-f_1=(\lambda-1)/(8(\lambda+1))$, and $(\lambda-1)^2/(\lambda+1)^2=(\sqrt{13}-2)/(\sqrt{13}+2)$. The two extrema also rule out eventual periodicity.
