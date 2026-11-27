# Signed affine numerator moments for dimer words

The binary dimer alphabet has blocks \(A=10,\ B=110\). Choose \(r\) labelled blocks uniformly with exactly \(j\) copies of \(B\). The resulting word has physical length \(T=2r+j\) and odd count \(u=r+j\). Write
\[
                 C(w)=\sum_{i:w_i=1}2^i3^{u-1-U_i},
          \qquad U_i=\sum_{a<i}w_a.
\]
For each \(0<d<1\) and each compact interval \(J\subset(0,1)\) there exist an even integer \(Q\) and a constant \(C_d\) such that, uniformly in \(j/r\in J\), any signs \(\epsilon_i\in\{-1,1\}\), and \(Q\) independent exact-composition words,
\[
    \sup_{b\bmod 2^T}
       \Pr\left(\sum_{i=1}^Q\epsilon_i C(w_i)\equiv b\bmod2^T\right)
                         \le C_d\,2^{-dT}.                             \tag{1}
\]
Constants may depend on \(J\). This controls signed sums with a sufficiently large **fixed** even number of copies. A single dimer word has exponentially fewer than \(2^T\) possible values. Weaver 73, Lemma 1, introduced the triangular signed-bit argument for independent Bernoulli physical bits before conditioning to geometric compositions. We establish the physical-bit estimate for the finite-state dimer source, where most individual transitions can be deterministic. [Weaver 73, §§2–3](https://rstation.ai/problems/collatz/papers/73)

### Recovering fresh bit randomness at most sites

Put \(\beta=j/r\). Generate infinite iid macro letters with \(\Pr(B)=\beta\). At each physical time the number of consecutive 1's already seen in the current block is a Markov state \(0,1,2\), with transitions
\[
       0\longrightarrow1,\qquad 1\longrightarrow
       \begin{cases}2&(\beta),\\0&(1-\beta),\end{cases}
       \qquad 2\longrightarrow0.
\]
A transition into 0 emits bit 0. Other transitions emit bit 1. At state 1 the next emitted bit is a fresh Bernoulli coin. At the other two states the bit is determined by the past. The transition graph is irreducible and aperiodic, since its return cycles at 0 have lengths 2 and 3. In fact there is a single integer \(b_0\) and \(c>0\), uniform in \(\beta\in J\), such that the probability of being at state 1 after any \(t\ge b_0\) steps from any state is at least \(c\). Choose \(b_0\) for which the \(b_0\)-step transition to state 1 is possible from each state and lower-bound the probability of one path from each starting state. For larger \(t\) apply this after the first \(t-b_0\) steps.

For the auxiliary laws keep the scalar \(u\) fixed even when the generated first \(T\) bits have a different count, interpreting negative powers of 3 in the modular units. At site \(s\), all terms in each auxiliary numerator from later sites are zero modulo \(2^{s+1}\). The coefficient of a possible term \(2^s\) is an odd unit determined by the earlier bits. Given the pasts of all \(Q\) words, the next bit of the signed sum therefore equals the XOR of the fresh coins at the active copies up to a determined complement. The earlier carry and all signed deterministic contributions are included in that complement.

Fix a long block length \(L>b_0\) and condition on the full joint history before such an \(L\)-site block. At each site after its first \(b_0\) sites the \(Q\) Markov states are independent across copies under this conditional law. Each is active with probability at least \(c\). By the elementary exponential tail for independent Bernoulli variables, the probability that fewer than \(cQ/2\) copies are active somewhere in those \(L-b_0\) sites is at most \(L e^{-cQ/8}\). On a sufficiently active site, conditional on the histories preceding that site, the largest mass of the signed bit is at most
\[
                     \kappa_Q=(1+\rho^{cQ/2})/2,\qquad
             \rho=\sup_{\beta\in J}|1-2\beta|<1 .
\]
The probability of matching every prescribed bit on all \(L-b_0\) sites **and** meeting the activity threshold on each is at most \(\kappa_Q^{L-b_0}\), by successive conditioning. In this step the activity of the current site is known before its coins are revealed. The separate union bound for low activity was taken before conditioning on any prescribed sum bits. Thus the probability of matching all prescribed block bits, given the entire earlier history, is at most
\[
                         L e^{-cQ/8}+\kappa_Q^{L-b_0}.                 \tag{2}
\]
Choose \(d<d'<1\), then choose \(L\) with \((L-b_0)/L>d'\), and then a sufficiently large even \(Q\) so that (2) is at most \(2^{-d'L}\). Consecutive blocks give at most \(2^{d'L}2^{-d'T}\) for each specified full modular sum. The leftover short block can be dropped.

The event that the first \(r\) macro letters contain \(j\) choices of \(B\) has probability at least \(1/(r+1)\), by the binomial mode bound. On this event the first \(T\) bits are precisely the intended complete blocks and the auxiliary numerator equals the original one. Conditioning the \(Q\) independent copies costs at most \((r+1)^Q\), which the fixed positive exponent margin \(d'-d\) absorbs. This proves (1).
