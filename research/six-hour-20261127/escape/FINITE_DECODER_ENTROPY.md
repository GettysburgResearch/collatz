# Finite ternary decoding attains the entropy supremum below the physical drift threshold

**Status.** Proposed written theorem and exact obstruction to an entropy-only ambiguity argument. The construction gives stationary inverse processes, genuine negative rational cycles, and arbitrary finite words on positive integers in the known basin. It gives no fixed escaping positive integer and no positive limiting mass in the original collision law.

Let \(1<m<\alpha=\log_2 3\) and \(H(m)=m\log m-(m-1)\log(m-1)\) in nats per odd step. For every \(\epsilon>0\), there exist a finite ternary depth \(d\), one finite table \(D:\mathbb Z/3^d\to\mathbb N_{>0}\), an integer block length \(L\ge d\), and a finite collection \(\mathcal W\) of words of length \(L\) with the following properties.

* Arbitrary doubly infinite concatenations of the blocks have a consistent ternary orbit \(z_i\) under \(z_{i+1}=(3z_i+1)/2^{e_i}\), and \(D(z_{i+1}\bmod3^d)=e_i\) at **every** position. Thus knowing one ternary residue predicts the last \(r\) exponents exactly at precision \(d+r-1\), uniformly on the entire concatenation system.
* Every block has average exponent within \(\epsilon\) of \(m\), strictly below \(\alpha\), and \(L^{-1}\log|\mathcal W|\ge H(m)-\epsilon\). Uniform independent block choices with a uniform random phase give a stationary ergodic exponent process of at least this entropy rate, with a finite exponent ceiling.
* One may prescribe finitely many finite-word frequencies to lie within \(\epsilon\) of their iid geometric frequencies of mean \(m\), in each block with cyclic boundary. Ordinary concatenation changes each fixed word frequency by at most its length divided by \(L\). In particular a positive frequency of large exponents is compatible with exact finite ternary decoding.
* Each periodization of a nonempty sequence of these blocks gives a genuine negative rational Syracuse cycle with this same decoder. Every finite segment of every concatenation is realizable on arbitrarily many different positive integer trajectories in the basin of 1. Use the ordinary routing construction on a longer segment if the initial \(d\) residue digits at the marked site must agree with those in the system.

It follows that the supremal stationary odd-step entropy subject to mean at most \(\alpha\) and perfect prediction by *some finite ternary table* is precisely \(H(\alpha)\). The upper bound is the geometric maximum-entropy bound on a positive integer with given mean. The lower bound follows by \(m\uparrow\alpha\). Finite tables and ceilings may vary in this supremum.

## Uniform finite information loss in strict positive real drift

Use independent geometric gaps of mass \(p(1-p)^{e-1}\) with \(p=1/m\), \(s=1-p\). Let \(Z\) be the stationary ternary value, obtained from the contracting sequence of past maps. For the \(n\)-letter chronological past, of total \(A\), write
\[
 C=\sum_{j=0}^{n-1} 3^{n-1-j}2^{A_j},\qquad
 2^A Z\equiv C\bmod3^n,\qquad A_0=0 .
\]
Given \(A,C,n\), the word is unique. For \(n\ge2\), \(v_2(C-3^{n-1})=e_0\), since the next term divided by \(2^{e_0}\) is odd and all later ones are even. Remove the first term and divide by \(2^{e_0}\); continue, recovering the final exponent from the total. A word of given \(A\) has probability \((p/s)^n s^A\).

The uniform entropy bound
\[
            \sup_n H(e_{-n},\ldots,e_{-1}\mid Z\bmod3^n)<\infty          \tag{3}
\]
has the following proof. Under \(m<\alpha\), choose \(0<t<1\) so small that \(\mathbb E[(2^e/3)^t]<1\), using the negative derivative at zero and the finite exponential moment. The inequality \((\sum u_j)^t\le\sum u_j^t\) bounds \(\sup_n\mathbb E[(C/3^n)^t]\) by a convergent geometric series. Write \(J=\lceil\log_2(1+C/3^n)\rceil\); its tail is uniformly exponential and its entropy uniformly bounded. Given \(J,Z\bmod3^n,A\), at most \(2^J+1\) numerators satisfy the congruence and size bound. Let \(A_0'\) be the smallest feasible total for given \(J,Z\bmod3^n\). The probability of any such minimum-total word lower-bounds the conditional normalizer. Hence
\[
 \Pr(A-A_0'\ge u\mid J,Z\bmod3^n)
       \le \min(1,(2^J+1)s^u/(1-s)).
\]
The conditional mean of this nonnegative difference is \(O_m(J+1)\) by summing the tail starting at a constant multiple of \(J+1\). Comparison with a geometric distribution bounds its conditional entropy by \(O_m(1+\log(1+J))\). Retaining \(J\), the difference, and the numerator index given its total suffices to specify the word. Taking expectations proves (3). This extends the count and geometric-likelihood proof of the specific tilt \(p=3/4\) in [Weaver, Paper 9, §5](https://rstation.ai/problems/collatz/papers/9). That source also proves an exponential clock-error tail at its chosen tilt.

Put \(h_d=H(e_{-1}\mid Z\bmod3^d)\). The exact chain rule in backwards time gives
\[
           H(e_{-n},\ldots,e_{-1}\mid Z\bmod3^n)=\sum_{j=1}^n h_j .
\]
Indeed, given the last exponent and current ternary residue, one reconstructs the previous residue with one fewer digit. Conversely that previous residue and exponent determine the current residue. The last exponent is independent of the earlier iid letters. Iteration proves the equality. Thus the nonincreasing \(h_d\) are summable, so \(d h_d\to0\). The least one-label prediction error \(\delta_d\) of a table \(D_d\) satisfies \(\delta_d\le h_d\) by \(-\log(\max_i q_i)\ge1-\max_i q_i\) for each conditional distribution \(q\). Maxima exist on the countable alphabet. Define arbitrary positive outputs on null cells. In particular \(d\delta_d\to0\).

## Cyclic sampling removes the boundary compatibility loss

Choose integers \(L=L(d)\) with \(L/d\to\infty\) and \(L\delta_d\to0\), possible by the preceding estimate. Sample \(L\) iid geometric letters on a circle. At each position the previous \(d\) letters, including the one to be decoded, have their exact iid distribution. They determine the ternary state at that position modulo \(3^d\), independently of all earlier letters. The same finite table \(D_d\) therefore predicts incorrectly at a given position with probability \(\delta_d\), including at the seam. With probability at least \(1-L\delta_d\) it makes zero errors over the entire cyclic word.

The iid law of large numbers simultaneously puts the average and all prescribed finite-word frequencies within any fixed small tolerances with probability tending to one. Cyclic wrapping affects each frequency by at most its prescribed word length divided by \(L\); for fixed word lengths elementary finite-dependence variance bounds suffice. The same average condition ensures that each chosen word has probability at most \(\exp[-(H(m)-\epsilon/3)L]\), by the exact length/total likelihood after taking the tolerances sufficiently small. Consequently at least \(\tfrac12\exp[(H(m)-\epsilon/3)L]\) distinct chronological words pass all tests for sufficiently large \(d\).

Partition these words according to the ternary state modulo \(3^d\) at their chosen block boundary in periodic repetition. This state is the offset of the preceding \(d\) cyclic letters. A class of size at least \(3^{-d}\) times the total has a common boundary state \(c\). Starting at \(c\) each of its words returns to \(c\) on the finite quotient and passes every table test. Concatenation therefore preserves all tests, including both seams, by the deterministic forward residue maps. The two-sided ternary orbit itself is defined by contraction of past maps, and its residues coincide with these finite computations. As \(d/L\to0\), the entropy lower bound follows. Randomizing the phase of independent uniform blocks gives an ergodic shift law (a shift-invariant event restricts on one phase to an invariant event of the Bernoulli block shift). Its exponent entropy rate is \(\log|\mathcal W|/L\), since a specified phase parses the equal-length blocks uniquely and hiding the phase costs at most \(\log L\) in each word entropy.

For any periodization the total multiplier \(3^N/2^A>1\) makes the fixed point \(-C/(3^N-2^A)\) negative, with odd denominator prime to three and odd numerator. The congruences obtained by reversing a full period make its specified valuations exact: every inverse step from an odd dyadic is odd dyadic, and the period fixes the same point. The label sequence at this rational point and at the symbolic period has the same ternary residues by contraction. This gives signed arithmetic controls with every finite digit of the decoder fixed. Positive convergent realization of segments uses the independent source for each finite word in [ORDINARY_DECODER_CONTROLS.md](ORDINARY_DECODER_CONTROLS.md).

**First unsupported step.** Entropy arbitrarily close to its drift-limited maximum, positive frequencies of any fixed collection of high exponents, and equality in all table predictions therefore do not distinguish the proposed critical process. Converting these periodic or finite positive controls into one positive source with its original-law macroscopic amplitude has not been done. No pressure or entropy upper bound here proves cancellation of the clipped current.
