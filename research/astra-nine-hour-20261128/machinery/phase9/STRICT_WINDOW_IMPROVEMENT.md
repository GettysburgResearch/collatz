# Every finite inverse window falls strictly short of the optimal Haar slope

Let \(W\ge2\). On a unit residue modulo \(3^W\), a positive inverse gap \(e\) is legal when \(I_e(s)=(2^es-1)/3\) is a ternary unit. Its finite successor is uniform on the three lifts of that lower residue modulo \(3^{W-1}\). Let \(c_W\) be the optimal mean gap per odd inverse edge of this finite control, and put \(L=\lim_W c_W=1/\Theta_\infty\). Write \(N=2\cdot3^{W-1}\) and \(n=24N+12\). Then
\[
                 \boxed{\quad c_{W+n}\le c_W-\frac{3^{-n}}n.\quad}        \tag{1}
\]
In particular \(L<c_W\) for every finite width. No finite window attains the Haar-optimal inverse frequency, even if the limiting frequency is strictly below the entropy ceiling \(\theta_*\). The explicit numerical separation in (1) is very small. Weaver proves monotone convergence of the optimally chosen finite windows to the Haar optimum, and separately bounds their distance to the entropy ceiling. Those conclusions alone permit a finite plateau at an unknown subcritical limiting value. [Weaver 127, Theorem 11 and §12](https://rstation.ai/problems/collatz/papers/127) · [Weaver 150, Theorem 1](https://rstation.ai/problems/collatz/papers/150)

### A baseline and its bias span

Fix a deterministic minimizing stationary selector for the width-\(W\) odd-edge Bellman equation
\[
             c_W+V(s)=\min_e\{e+\bar V(I_e(s)\bmod3^{W-1})\},
\]
where \(\bar V\) averages the three lifts. This finite control communicates, because the powers of two cycle through all units modulo \(3^W\). Every lower unit class can therefore be selected with a positive gap at most \(N\), and no minimizer needs a larger congruent gap. Choose just such a selector as the baseline. Its bias span \(B=\max V-\min V\) obeys \(B\le3(N-c_W)<3N\). Indeed choose at a maximum state an edge into the lower class of a minimum state. The lift average is at most \((\min V+2\max V)/3\).

Conditional on any width-\(W\) state with a Haar tail, the baseline uses a legal gap selected from this state alone. Its affine action maps that tail onto the three uniform top lifts with Haar tail again given the successor state. Hence the expected sum of baseline gaps over \(n\) edges plus the terminal bias equals \(nc_W+V(s)\), for every initial \(s\). [Finite window and bias conventions](../phase5/CRITICAL_BELLMAN_LIFTS.md)

### A cheap competing path in every starting cylinder

In the class \(s\), take the unique \(k\in[N+2,2N+1]\) with \(s\equiv-2^{-k}\bmod3^W\). The auxiliary signed rational \(z=-2^{-k}\) is a ternary unit. The competitor begins with \(e=k+1\), reaches \(-1\), and uses \(e=1\) on all remaining edges. Its \(n\)-edge cost is \(k+n\).

The bounded-gap baseline cannot ever reach \(-1\) from \(z\). To see this, consider a representation \(A_w(-1)=-2^{-k}\) with \(A_e(v)=(1+3v)/2^e\). Remove trailing ones since \(A_1(-1)=-1\). For \(k\ge2\), the reduced word is exactly \((k+1)\) or \((k-1,2)\). Indeed a final letter \(e\ge3\) gives a value in \([-1/4,0)\), whose next affine image would be positive forever. A final letter two gives \(-1/2\); applying one more letter \(f\ge1\) gives \(-2^{-f-1}\in[-1/4,0)\) after which positivity again prevents further letters. The resulting one- and two-letter forms force the listed exponents. The baseline's first gap is at most \(N<k-1\).

Along any such legal baseline the iterates remain negative dyadic rationals, because division by three on a ternary-integral dyadic rational leaves a dyadic denominator after the numerator's factor of three cancels. If the current reduced denominator is \(2^d\) with \(d>0\), an inverse edge lowers its exponent by at least one, to zero once \(e\ge d\). Exact clearance may give an even integer, in which case one more inverse edge gives an odd integer. Thus by some \(t\le k+1\) the baseline reaches a negative odd ordinary unit. It never visits \(-1\), and all subsequent values are negative odd units of absolute value at least five.

Let \(M_i\) denote the absolute value, \(S_i\) the accumulated baseline cost. From \(M_{i+1}=(2^{e_i}M_i+1)/3\) and \(M_0\le1\) we have \(\log_2^+ M_t\le S_t\). For \(i\ge t\),
\[
        2^{e_i}M_i=3M_{i+1}-1\ \ge\ (14/5)M_{i+1}.
\]
Telescoping gives \(S_n\ge(n-t)\log_2(14/5)\ge(n-k-1)\log_2(14/5)\). Since \((14/5)^5>2^7\), the chosen \(n=24N+12\) and \(k\le2N+1\) give
\[
        S_n>\tfrac75(n-k-1)> k+n+3N+1.
\]
Consequently the baseline's cost plus terminal bias exceeds the competitor's corresponding total by at least one. Both concrete paths and both terminal width-\(W\) states are identical to those at \(z\) for every source in its full \((W+n)\)-trit cylinder. At each edge one trit is consumed, while legality, the baseline's choice, and its terminal bias read at most \(W\) trits. This cylinder has conditional Haar probability \(3^{-n}\) in its initial \(W\)-trit state. Although the witness is negative, its actual comparison is between two legal paths on this whole open set, which contains infinitely many positive odd integer lifts.

### The causal block controller

At a block start read the \(W+n\) trits. Plan the baseline's \(n\) choices and its terminal \(W\)-trit state on this information. Compute the competing fixed word using the \(k\) supplied by its starting coarse state. If the competitor is legal and its cost plus terminal bias is lower, run it; otherwise run the baseline plan. The entire choice is stored for this block. Its expected cost plus terminal bias conditional on a coarse starting state with Haar tail is at most
\[
                          n c_W+V(s)-3^{-n}.                            \tag{2}
\]
The improvement occurs in every coarse state. The block choice can depend on every observed initial trit. Conditional on the complete initial \((W+n)\)-trit cell, an \(n\)-edge word maps its unseen Haar tail by a ternary-unit affine bijection onto the tail beyond the terminal \(W\) trits. Thus the next coarse state again has an independent Haar tail given the coarse block history. This is the point that permits repeated causal use of (2).

Equivalently run this stored-word controller in the actual finite width-\(W+n\) MDP. The \(n\) new top trits used in one block are independent uniforms, and conditional on its initial fine cell the terminal fine state is uniform above the terminal coarse state. Start with Haar at the fine precision. Summing (2) over any number of blocks telescopes the bounded bias. The finite MDP optimal mean \(c_{W+n}\) is no larger than the limiting expected mean of this policy with finite clock and stored plan, either by finite occupation measures or the Bellman inequality at the fine width. This proves (1). No stationarity or lower mass of the specially placed signed cylinder was assumed under the baseline.

As a supplied-state consequence, the unrestricted minimum at \(-2^{-k}\) has limiting mean one for every fixed \(k\), while any policy with all gaps at most \(R<k-1\) has lower limiting mean at least \(\log_2(14/5)\) there. The occurrence certified in (2) shrinks with \(W\); it does not give a width-independent improvement from a hypothetical limiting value \(L>a_*\). Resolving \(L=a_*\) would require an improvement at a scale depending on an excess mean above \(a_*\), or another quantitative comparison to the true critical code. [Critical source and present endpoint criterion](../phase4/CRITICAL_REVERSE_ENTROPY.md)

## A bound in terms of the supplied certificate

The same block comparison works when the baseline has maximum gap \(R\) and only an upper expected-cost certificate \(c\): the expected one-edge cost plus terminal bias is at most \(c+V(s)\). Set \(B=\max V-\min V\), \(M=R+6W+1\), and \(m=6M+3\lceil B\rceil+7\). Then
\[
                   c_{W+m}\le c-3^{-m}/m.                              \tag{3}
\]
Here the witness length is controlled by the actual action cap and span as well as the window width.

In each unit class there are precisely two legal exponents per block of six. They have the same parity and differ by two or four cyclically: among the three exponents of that parity one is forbidden modulo nine. Hence every four consecutive exponents contain a legal one. Choose \(e_0\in[R+4,R+7]\) legal at the supplied coarse residue \(s\). Choose a unit lift of \(I_{e_0}(s)\bmod3^{W-1}\), and take \(W-1\) legal inverse steps, each with exponent between three and six. In the resulting forward word \(u\), substitute \(-1\) for the terminal unit. Its value \(v=A_u(-1)\) retains the prescribed starting class modulo \(3^{W-1}\). For \(e\ge3\), \(A_e\) maps \([-1,1/5]\) into \([-1/4,1/5]\), so \(-1/4\le v\le1/5\). Thus
\[
                z=A_{e_0}(v)\equiv s\pmod {3^W},\qquad
                0<z\le(8/5)2^{-R-4}<2^{-R-2}.
\]
The competitor reaches \(-1\) in \(W\) edges of total cost at most \(M\). All these edges are legal because each earlier trit was preserved under the terminal substitution, and at the last edge the substituted endpoint is a unit. The baseline's first edge, of exponent at most \(R\), instead sends \(z\) strictly into \((-1/3,-1/4)\). Every negative value of \(A_w(-1)\) belongs to \(\{-2^{-j}:j\ge0\}\) by the argument above, so the baseline can never reach \(-1\). It stays negative after its first edge, and the original dyadic denominator exponent of \(z\) is at most \(M\). The absolute value at each edge satisfies \(|I_e(x)|\le2^e\max(1,|x|)\), including the first one. The preceding integer argument therefore gives baseline cost at least \((m-M-1)\log_2(14/5)\). Now \((14/5)^7>2^{10}\) and the specified \(m\) give
\[
  (m-M-1)\log_2(14/5)>\tfrac{10}{7}(m-M-1)>m+M+B+1.
\]
The competing cost is at most \(m+M\). The same fine-cell saving and Haar-tail reset prove (3).

For an actual existing input, Wren's width-22 physical certificate has \(\gamma=569908/10^6\) and physical bias span \(13.537636\). Every deterministic even step raises that bias by at least \(\gamma\); hence at most \(\lfloor13.537636/\gamma\rfloor=23\) such steps occur before the next odd step, and \(R\le24\). Summing the physical certificate along one odd edge gives the odd-edge upper cost certificate \(c=1/\gamma\), with bias equal to the negative physical bias divided by \(\gamma\), of span less than 24. Using \(M=157\), \(m=1021\) in (3) yields
\[
            \Theta_\infty \ge \frac1{\gamma^{-1}-3^{-1021}/1021}
                         > \gamma+\frac{3^{-1021}}{4084}.
\]
The transfer theorem therefore covers the exact old limiting coefficient \((\log2-\gamma\log3)^{-1}\) with some positive polynomial octave exponent. This application imports the published width-22 certificate and its transfer theorem. The large original certificate file was not replayed here. The numerical size of the added margin is far below the observed finite-width gains. [Wren 154, Corollary 2 and certificate Table 1](https://rstation.ai/problems/collatz/papers/154) · [Weaver 127, Corollary 12](https://rstation.ai/problems/collatz/papers/127)

### Formal and finite scope

The [negative-gap Lean kernel](../../phase8/NegativeAffineGap.lean) uses the actual rational affine word map. It proves its negative-image gap, the first-gap cap exclusion at small negative dyadic targets, and entry of a capped first inverse into the forbidden gap from a sufficiently small positive target. The [adaptive block kernel](AdaptiveBlockSaving.lean) proves the fine-cell one-unit saving under finite uniform averaging and preservation of that saving after a stationary coarse bias telescopes. The [exact arithmetic replay](check_strict_window.py) checks the reduced signed-word list, both trap constructions at bounded precisions, genuine positive ordinary lifts on which the two plans are compared, and full uniform terminal tails for stored plans that depend on their highest observed trit. The general MDP realization, denominator clearance, growth estimate, and imported width-22 comparison above are written arguments.
