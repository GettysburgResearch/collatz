# Ordinary height gives entropy in a single escape's occupation law

Let \(x_j=T^j(x_0)\) be one injective positive ordinary shortcut orbit and \(w_j=x_j\bmod2\). Use binary logarithms and measure entropy in bits. Along any subsequence \(N\to\infty\) suppose the empirical shifted parity words converge weakly to \(\mu\). The shift-invariance of \(\mu\) follows by discarding the two endpoints. For every fixed \(B>0\) put
\[
 \pi_B=\limsup_N N^{-1}\#\{0\le j<N:x_j\le N^B\}
\]
on this same subsequence. Then
\[
                        h_\mu(\sigma)\ge \frac{\pi_B}{B}.            \tag{1}
\]
This gives a partial answer to the positive-entropy question, S5, in the binary-window rigidity paper. In particular every empirical limit of an escape satisfying \(\max_{j<N}x_j\le N^{B+o(1)}\) has entropy at least \(1/B\). At a zero-entropy empirical limit, the fraction of times with \(x_j\le N^B\) tends to zero for **each** fixed \(B\). [Window rigidity and its open S5, §§4.4–4.5, 6](https://rstation.ai/problems/collatz/papers/170)

## Finite-window proof

Select \(J\) uniformly from \(\{0,\ldots,N-1\}\) and let \(H_N(d)\) be the entropy of the length-\(d\) parity word beginning at \(J\). Windows may extend into the genuine orbit beyond clock \(N-1\). At \(d=\lceil B\log_2N\rceil+1\), all starts at most \(N^B\) have distinct words: the starts are distinct ordinary integers in \([1,2^d)\), and a length-\(d\) parity prefix specifies a unique residue modulo \(2^d\). Conditional on selecting one of these \(M\) starts, the word has entropy \(\log_2 M\). Conditioning cannot increase entropy on average, so \(H_N(d)\ge(M/N)\log_2 M\) for \(M>0\).

For fixed \(k\), partition the long word into \(\lfloor d/k\rfloor\) full \(k\)-blocks and one remainder. The start distribution of each full block differs from that of \(J\) by total variation at most \(d/N\). Its entropy tends to \(H_\mu(k)\), uniformly over the offsets under consideration, by uniform continuity of entropy on the fixed \(2^k\)-point simplex. Subadditivity therefore gives
\[
        H_N(d)\le \lfloor d/k\rfloor [H_\mu(k)+o_k(1)]+k .
\]
Take a subsequence realizing \(\pi_B>0\), divide by \(d\), and then take the infimum over \(k\), proving (1). The case \(\pi_B=0\) is immediate. To use an exponent \(B+o(1)\), apply (1) first at each fixed \(B'>B\).

If the running maximum is polynomial on this subsequence, the one-letter marginal of every such limit is \(b=\log_3 2\). Indeed
\[
 \log(x_N/x_0)=P_N\log3-N\log2+
       \sum_{j<N,\;w_j=1}\log(1+1/(3x_j)).
\]
The sum is \(O(\log N)\) by distinctness, and \(x_N\le(3\max_{j<N}x_j+1)/2\). Consequently
\[
                    1/B\le h_\mu(\sigma)\le H_2(b).
\]
The numeric peak lower bound at \(1/H_2(b)\) is known and weaker than a published power improvement. The new assertion here constrains the actual empirical measures at each polynomial-height volume fraction. [Earlier peak estimate](../../astra-global-closure-20261124/round9/critical/ESCAPE.md) · [Weaver, interval compression, Thm. A](https://rstation.ai/problems/collatz/papers/28)

## What measure rigidity supplies

Under the native dyadic parity conjugacy the limiting invariant measure \(\nu\) on \(\mathbb Z_2\) has the entropy in (1). If \(\eta=\pi_B/B>0\), choose \(0<\delta<1/2\) with \(H_2(\delta)<\eta/2\). Write \(p_\omega\) and \(h_\omega\) for the odd fraction and entropy of an ergodic component. Since \(h_\omega\le H_2(p_\omega)\), the integral of \(h_\omega\) over \(p_\omega>\delta\) is at least \(\eta/2\). The odd mass \(\rho=\int p_\omega>0\), and its **odd-weighted** entropy obeys
\[
              \rho^{-1}\int p_\omega h_\omega \ge \delta\eta/(2\rho)>0.
\]
Apply Theorem 2 in the primary window-rigidity paper to this specific invariant measure. Every weak limit of its odd-part binary-window measures averaged over digit heights has a Lebesgue component of at least the displayed weight. Time is taken to infinity first to produce \(\nu\). Its Proposition 5 also shows that Bernoulli parity of any fixed positive bias can have Lebesgue window limit, so this new ordinary lower bound supplies no opposing parity bias. [Theorem 2 and Proposition 5](https://rstation.ai/problems/collatz/papers/170)

## Simultaneous time and digit height

There is a distinct integral consequence when the digit depth itself is comparable to the logarithm of the observation time. Let the preceding orbit satisfy $\max_{j<N}x_j\le N^{B+o(1)}$ on a subsequence. Write $O_N=\{j<N:x_j\text{ odd}\}$ and take integers $D_N$ with $D_N/\log_2N\to s\in(0,\infty)$. Sample $j$ uniformly in $O_N$, independently sample $1\le d\le D_N$ uniformly, and form the circle point $(x_j\bmod2^d)/2^d$. Every weak limit $\lambda$ of these laws has a Lebesgue component whose exact mass $c$ satisfies
\[
 \frac{[1-(B-s)_+]_+}{s}\ \le\ c\ \le\ \min(1,B/s).                 \tag{2}
\]
In particular at $s=B$ the guaranteed weight is $1/B$. This examines digit windows on a simultaneous scale different from the time-first limit above.

For the proof, $|O_N|/N\to \log_3 2$ on this subsequence. Let $\alpha_N$ be the uniform measure on the odd states and let $H_N$ be the entropy of their residues modulo $2^{D_N}$. Each residue contains at most $1+N^{B+o(1)}/2^{D_N}$ distinct states. Hence
\[
 H_N\ge\log_2 |O_N|-\log_2(1+N^{B+o(1)}/2^{D_N}).
\]
The finite-height covering estimate, Lemma 3 in the window paper, applies to each $\alpha_N$ individually. For fixed $q$, the $q$-digit entropy of the averaged window law, after merging the two atoms adjacent to zero, is at least $q H_N/D_N-1-O(q^2/D_N)$. The deterministic joint invariance bounds in its Theorem 1 give invariance of $\lambda$ under multiplication by 2 and 3. In particular its only possible dyadic point mass is at zero, so the merged partition has null boundary and its entropy passes to the weak limit. Divide by $q$ and send $q\to\infty$ to get $h_{\times2}(\lambda)\ge\limsup H_N/D_N$ in bits. Rudolph's theorem and ergodic decomposition identify this entropy with the exact Lebesgue weight. This proves the lower bound. [Window identity, finite entropy covering and partition-boundary argument, §§4.2–4.4](https://rstation.ai/problems/collatz/papers/170)

For $s>B$, a proportion at least $1-(B+\delta)/s+o(1)$ of the digit depths exceeds $(B+\delta)\log_2 N$ for any fixed $0<\delta<s-B$. At these depths the unwrapped quotient $x_j/2^d$ tends to zero uniformly. Passing first to the weak limit using closed neighborhoods of zero, and then sending $\delta\downarrow0$, gives $\lambda(\{0\})\ge1-B/s$. This proves the upper bound. It arises from the finite leading digit and does not bound the Lebesgue component in the time-first limit. Both conclusions also hold for sequences of proper finite simple segments, including whole least periods with lengths tending to infinity, when the polynomial cap and a positive odd fraction hold. The finite covering proof uses the original integer representatives at the supplied horizon.

## A critical, summable, high-entropy word without long powers

Fix any \(\epsilon>0\). There exist uncountably many binary directives whose excess number of odd letters above \(bh\) at clock \(h\) is comparable to \(\sqrt h\) for all sufficiently large \(h\), whose every time-occupation limit has entropy at least \(H_2(b)-\epsilon\), and whose factors all avoid \(V^K\) for one finite \(K=K(\epsilon)\) and every nonempty word \(V\). They can all be taken to have irrational binary seeds. The native reciprocal coefficient series \(\sum_h2^h/3^{P_h}\) converges for each, while every finite prefix still has arbitrarily large positive ordinary realizations. Thus entropy and real coefficient growth alone cannot force unboundedly many [staircase stages](STAIRCASE.md).

Here is an elementary construction. Fix a large block length \(L\), put \(m=\lceil4\log_2 L\rceil\), and start block \(n\) with \(0^m1s_n1\), where \(s_n=v_2(n+1)\bmod2\). End every block with one and prohibit \(0^m\) in its remaining payload. This leaves the marker \(0^m\) exactly at block boundaries. The sequence \(s_n\) has no fifth powers. Indeed for a proposed period \(t=2^a u\), \(u\) odd, an interval of \(4t\) consecutive indices contains an \(n\) with \(n+1\equiv2^{a+1}\bmod2^{a+2}\). Then \(v_2(n+t+1)=a\) differs in parity from \(v_2(n+1)=a+1\), contradicting a length-\(5t\) periodic factor.

Let \(k=\lfloor bL\rfloor,\ \lambda=bL-k\in(0,1)\), \(c=(1-\lambda)/2>0\), and \(H_n=\lfloor \lambda n+c\sqrt n\rfloor\). Give block \(n\) exactly \(k+H_{n+1}-H_n\) ones, so its weight is either \(k\) or \(k+1\). At block boundaries the excess is \(c\sqrt n+O(1)\), and within a block it changes by at most \(L\). For either weight and backbone bit the number of payload choices is \(2^{H_2(b)L-o(L)}\) as \(L\to\infty\). To check this, the payload has length \(L-m-4\) and weight \(\lfloor bL\rfloor+O(1)\). Stirling's estimate gives this count before the forbidden-run condition. The fraction with an internal zero run of length \(m\) is at most \(L(1-\text{weight}/\text{length})^m=o(1)\) by sampling without replacement and a union bound. Take \(M\ge2^{(H_2(b)-\epsilon)L}\) common indexed payload choices for each of the four block types.

Any length-\(Kt\) periodic factor with period \(t\ge1\), \(K=2L+8\), contains a full marker whose translate by \(t\) stays inside the factor. Therefore \(L\mid t\). Writing \(t=qL\), at least \(Kq-1\ge5q\) full consecutive blocks lie inside. Their backbone projection has period \(q\), contradicting the preceding fifth-power bound.

Choose the free indices as a sequence normal over the \(M\)-symbol alphabet. Almost every independent uniform choice has this property. For each fixed \(r\), a binary block of length \((r+2)L\) starting in any fixed phase contains \(r\) complete consecutive encoded indices at a fixed internal offset, and determines them. Along starts in that phase their limiting joint law is uniform on \(M^r\). For every occupation limit, entropy of its \((r+2)L\)-letter law is at least \(r\log_2 M\), first conditional on the start phase and then by concavity. Sending \(r\to\infty\) gives the stated entropy bound. The free sequences have a nonatomic product law, the literal coding is injective, and there are only countably many rational binary seeds. Removing them leaves uncountably many examples.

These controls do not claim sustained growth of any positive ordinary orbit. For a fixed ordinary source the integrality of the selected infinite seed remains an additional constraint.
