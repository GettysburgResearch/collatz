# The forward return words seen from a true gate

Let $\mathcal P$ be the strict future parity gate and let $A$ be a union of full components, or a single fixed odd-unit predecessor basin, of ordinary density $d$. Let $c_0=\sqrt{\log(4/3)}/(2\sqrt\pi)$. For some absolute $\theta>0$, uniformly in all integers $0\le r\le\theta\log X$ and all residue classes $u\bmod3^r$,
\[
 \frac{3^r\sqrt{\log X}}X\,
      \#\{X\le n<2X:n\in\mathcal P\cap A,\ n\equiv u\pmod{3^r}\}
             =c_0 d+o_A(1).                                            \tag{1}
\]
The positive exponent in this theorem comes from extra ternary precision at the physical output. It does not assert a distribution in shrinking real intervals. In particular fixed or growing congruence restrictions at the original sampled integer retain the full future test.

To prove (1), use the marked mixing proof in [sharp true gate sampling](SHARP_TRUE_GATE_SAMPLING.md). Leave enough room in its choice of $k$ that $k+r+1\le\delta_B b$ and $3^{j+r+1}=o(Y)$ throughout the physical crop. This holds for an absolute $\theta>0$. For a fixed complete prefix word of length $j$ odd gaps and total $S$, the required $n$-class is exactly the output congruence
\[
 y\equiv F_j+3^j2^{-S}u\pmod{3^{j+r}}.
\]
Since an endpoint is odd, this congruence ensures a genuine odd inverse start with the specified class. Use the density column $3^{j+r}$ times its probability. Its normalized physical count divides the summed column by $3^rY$ instead of $Y$. The additional translation is fixed at fixed total and vanishes modulo $3^m$. If $j+r$ is odd, use one extra trit in (2) and project it away. The same argument applies to the source-ballot offset conditioned on its own word. All complete-period errors consequently bear exactly the prefactor $3^{-r}$ at the final ordinary count. To treat discarded clock tails at this relative scale, include the congruence on initial sources in the binary period count directly: modulo $3^r$ each complete block of $2^{3j+1}$ consecutive representatives of the class observes every binary word once, by coprimality. Thus the normalized relative remainder is $O(3^r2^{3j+1}/X)=o((\log X)^{-1/2})$ after decreasing $\theta$. Every other step in the sharp theorem, including the actual mark $g(y)$, is identical and uniform.

## Consecutive strict future minima

A finite native word $w$ with $q$ odd departures connects one true gate immediately to the next precisely when its shortcut surplus is strictly positive at all its positive dates and finishes at height one, and the endpoint is a true gate. In this description no intermediate date can be a true gate, since its level is at least one and the endpoint has level one. Conversely the future running minimum increases in unit increments at exactly the gates; at the very next gate its level is one. Such words have $t=2q-1$ shortcut letters. The initial letter is odd and removing it leaves an ordinary nonnegative Dyck excursion of length $2q-2$. Any one of the $C_{q-1}$ possible words ($C_i$ a Catalan number) lifts backwards from a compatible positive odd endpoint to its unique integer source. Its affine map is $y=3^q2^{-t}n+F_w$. Thus the inclusive endpoint $y$ needs exactly one residue modulo $3^q$, including when the word ends in a halving. The binary parity word and the prescribed odd final endpoint verify all forward letters on this lift.

More generally let $w$ be a fixed concatenation of $a$ such words and let $q,t$ denote the total odd and shortcut counts. At the endpoint upper and lower crops differ from the ideal physical octave $[3^q2^{-t}X,2\cdot3^q2^{-t}X)$ by $O_w(1)$ integers. The first and subsequent true gates are determined by the prescribed words once the endpoint itself is a gate. For fixed-target $A$, all intermediate sites exceed its target at sufficiently large $X$. Counting those endpoints by (1) gives
\[
 \Pr\{\text{first }a\text{ return words equal }w
          \mid n\in\mathcal P\cap A\cap[X,2X)\}
                  \longrightarrow 2^{-t},\qquad d>0.                 \tag{2}
\]
The constant is $3^{-q}(3^q2^{-t})$. The mass of the one-word distribution is $\sum_{q\ge1}C_{q-1}2^{1-2q}=1$ by the Catalan generating function. Missing returns are sent to a cemetery state. Truncating to a finite set of words of arbitrarily large limiting mass proves joint total-variation convergence for any fixed number of returns, with independent successive words. The odd length of one return has mass $C_{q-1}2^{1-2q}\asymp q^{-3/2}$ and infinite mean. All these laws hold even after conditioning on any individual positive-mass component.

A uniform version controls a growing initial segment of the induced history. For any $W=W(X)=o(\log X)$ and fixed $d>0$, uniformly over all concatenations with total odd length $q\le W$,
\[
 \frac{\Pr\{\text{prescribed successive words}\mid
          n\in\mathcal P\cap A\cap[X,2X)\}}{2^{-t}}
                                      =1+o_A(1).                       \tag{3}
\]
Indeed $t\le2q$, $Y'=3^q2^{-t}X=X^{1+o(1)}$, and the actual single final ternary class satisfies $q\le\theta\log Y'$. The affine offset obeys $0\le F_w\le(3/2)^q-1=X^{o(1)}$. The crop endpoint error is at most $O((3/2)^q+1)$ possible integers, negligible relative to $X2^{-t}/\sqrt{\log X}$. Every intermediate height exceeds $X2^{-2q}$ and transports $A$. The chosen uniform form of (1) applies at $Y'$ and uses $\sqrt{\log X/\log Y'}=1+o(1)$. For some fixed sufficiently small $\eta>0$ the same proof permits $q\le\eta\log X$ on retaining the factor $\sqrt{\log X/\log Y'}$ on the right of (3).

In particular for any $a=a(X)=o(\sqrt{\log X})$ the total variation distance between the first $a$ actual return words of this sampler and $a$ independent Catalan words tends to zero. Choose $a^2\ll W\ll\log X$, also when $a$ is bounded. Under the independent law $\Pr(\sum_{i\le a}q_i>W)\ll a/\sqrt W$, by removing any $q_i>W$ and applying Markov's inequality with $\mathbb E[q_i1_{q_i\le W}]\ll\sqrt W$. On the remaining event the relative comparison (3) can be summed without multiplying the error by the number of words. This also controls the actual omitted mass, including cemetery events.

The limiting mean gap is infinite for the spatially chosen gate. At an individual escaping start the long-run upper mean gap between gates is at most $1/(2-\log_2 3)$ once finite initial delays are absorbed. The proof above follows the true future up to $o(\sqrt{\log X})$ returns from the sampled start, whose incoming first-minimum history itself contains order $\sqrt{\log X}$ gates. It supplies no upper on occupation strictly after that minimum.
