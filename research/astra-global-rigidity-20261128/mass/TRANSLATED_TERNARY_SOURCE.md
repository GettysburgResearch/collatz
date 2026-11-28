# Original ternary digits and the true future on every translated interval

**Source-qualified finite theorem.** Let \(I\) be any interval of \(W\) consecutive positive integers and take \(n\) uniformly in \(I\). Write \(e=v_2(n)\), \(x=n/2^e\), \(U(x)=(3x+1)/2^{v_2(3x+1)}\), and \(H_t(x)=\sum_{i<t}v_2(3U^ix+1)\). Put
\[
  Z_t(n)=(e,e+H_t(x),U^t x).
\]
These are the true initial halving count, original shortcut clock since \(n\), and state after \(t\) complete odd departures and their following halvings. For every \(A>0\) there are \(\delta_A,C_A>0\) such that with \(t=\lfloor(\log_2 W)/32\rfloor\ge1\) and \(0\le b\le\delta_A t\),
\[
 \left\|\mathcal L(n\bmod3^b,Z_t(n))-
        \operatorname{Unif}(\mathbb Z/3^b)\otimes\mathcal L(Z_t(n))\right\|_1
              \le C_A t^{-A}.                                        \tag{1}
\]
The norm sums absolute differences of probability masses. Every bound is uniform over the interval's location. Every deterministic observable of the exposed endpoint and clock, including any arbitrarily long actual future, may replace \(Z_t\). The conclusion tests all ternary digits jointly, also against a test selected from the actual future.

The analytic input is Weaver–Wren v1, Theorem 6, equations (65)–(66), with observation depth \(t+b\) and coarse depth \(t\). The one-extra-digit reciprocal-mass transport on an octave is prior. The argument below counts unweighted ordinary starts on a translated interval, prices residue cycles and exceptional endpoints against its length, and keeps the full product-law error on a growing ternary modulus. [Weaver–Wren, Paper 48/v1, §8, Theorem 6](https://rstation.ai/problems/collatz/papers/48/v1) · [PR195, original physical source, at 3fa7ef4a0011b35447a70f587b400878d5ea8ebe](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/PHYSICAL_SOURCE.md) · [PR195, retained native clock and one ternary digit](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/MARKED_FIBRES.md)

## A translated odd input interval

Take the odd integers of a real interval \(J\) of length \(V\ge2\). For sufficiently large \(V\) there are \(V/2+O(1)\) such starts. We shall need \(2^{4t}3^b\le V\) with \(2^{4t}/V\) small. Set \(q=3^t,\ B=3^b,\ Q=qB\). For a word of \(t\) positive geometric gaps with total \(h\), write its affine output as
\[
                y=q2^{-h}x+F,\qquad 0<F<q .
\]
Word reversal puts \((F,h)\) in the stationary offset order used by the cited joint mixing theorem and preserves each weight \(2^{-h}\). Define \(P_h(z)=\Pr(F=z\bmod Q,H_t=h)\), where this probability refers to the independent fair geometric word. Congruences of the dyadic \(F\) modulo any odd modulus are well-defined. Let \(MP_h(z)\) be the average of its masses in the \(B\) classes over \(z\bmod q\). The primary input gives
\[
             \sum_h\|P_h-MP_h\|_{\ell^1(\mathbb Z/Q)}
                      \le C_A t^{-A},\quad b\le\delta_A t.           \tag{2}
\]
We can decrease \(\delta_A\) to at most one.

First discard \(h>4t\). Across the odd integers of any interval of length \(V\), their fraction is \(O(e^{-ct}+2^{4t}/V)\). The event is determined by the binary residue through the first \(4t+1\) native digits. On complete periods its probability among odds is the fair geometric tail \(\Pr(H_t>4t)\le [3(2/3)^4]^t\). A partial period costs \(O(2^{4t})\) starts. For \(h\le4t\), replace \(x\in J\) with \(y\in q2^{-h}J\). A discrepancy implies \(x\) is within \(2^h+1\) of an endpoint of \(J\), since \(F2^h/q<2^h\). Over all these clocks combined, each start has a unique genuine word, and the resulting change costs \(O(2^{4t})\) counts. Conversely every legal inverse from a positive odd \(y\) has only positive odd intermediate integers: at each legal step \((2^g y-1)/3\) is positive and odd. Restricting to positive odd outputs in the replaced interval thus introduces no extra signed or formal paths.

In the replaced table, for each odd \(y\in q2^{-h}J\) and source ternary residue \(r\bmod B\), the number of words is exactly
\[
                 2^h P_h(y-2^{-h}q r\bmod Q).                        \tag{3}
\]
Indeed \(x=2^h(y-F)/q\); legality forces \(F=y\bmod q\) and the extra digit block selects \(r\). Uniformizing \(r\) at this \((h,y)\) replaces \(P_h\) by \(MP_h\). Each residue of \(y\bmod Q\) has at most \(1+V/(2^h B)\) representatives in the indicated interval, up to an absolute endpoint constant. For each \(r\), its shift permutes all \(Q\) residues. The unnormalized joint sum error contributed by this \(h\) is at most
\[
                C(2^h B+V)\|P_h-MP_h\|_1 .
\]
Summing and dividing by the actual \(V/2+O(1)\) inputs, (2) yields \(O_A(t^{-A})\) whenever \(2^{4t}B\le V\). Restoring both the table and its uniformized marginal costs at most twice the earlier discarded fraction. The resulting odd-input error is
\[
                   O_A(t^{-A}+e^{-ct}+2^{4t}/V).                    \tag{4}
\]
No ratio of the interval's position to its width has entered the estimate.

## Return to every positive input

With \(n\) uniform in \(I\), the contribution of \(e>\lfloor(\log_2 W)/4\rfloor\) is \(O(W^{-1/4}+W^{-1})\) by counting multiples of that power of two in a translated interval. For each remaining fixed \(e\), the odd parts are uniform on the odd integers of an interval of length comparable to \(V=W/2^e\ge W^{3/4}\), with immaterial endpoint rounding. For the chosen \(t\), \(2^{4t}3^b\le 2^{(4+\log_2 3)t}\le W^{(4+\log_2 3)/32}\), so all retained intervals satisfy (4) with uniform error \(O_A(t^{-A})\). Multiplication by \(2^e\) permutes residues modulo \(3^b\). Adjoin the fixed \(e\), shift the clock by it, and average the conditional estimates with their actual frequencies. This proves (1).

The exact-mark contraction also permits a finite first-hit label \(F_A\) with a finite target set. In retained strata and outside \(H_t>4t\), the absolute clock \(e+H_t\) is at most \((\log_2 W)/4+4t\le(3/8)\log_2 W\). At most \(2|A|2^{(3/8)\log_2 W}\) ordinary starts anywhere have visited a fixed target by that clock, by indegree two. At all other starts the first-hit label is a deterministic function of the exposed state. Replacing its true value in both parts of the product comparison costs \(O(|A|W^{-5/8}+W^{-1/4}+e^{-ct})\). Thus the same estimate after changing \(C_A\) for a fixed target set applies to the joint vector \((Z_t,F_A(n))\), and also to the label of a completely invariant set with no such replacement.

In particular (1) holds for the first-visit colors of \(5,85\), even though their ordinary predecessor densities segregate into almost pure moving windows of subpower width. Local ternary uniformity against these true colors does not imply physical overlap of their windows. [Ordinary separated predecessor windows](ORDINARY_BASIN_WINDOWS.md)
