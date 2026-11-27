# Exact rows at a surviving ordinary endpoint

**PROPOSED. Collatz remains open.** For the shortcut map \(T\), write \(P_s(x)\) for the number of odd inputs among \(x,\ldots,T^{s-1}x\). A unit is a positive odd integer prime to three. At one supplied unit \(a\), the PR206 predicate \(\mathrm{FullRow}(a,b,m)\) asks for a common forward suffix of \(b-m\) odd steps ending above two and, before that suffix, all \(2^{m-1}\) prescribed words in the two nonzero residues modulo three. The prefix clock is common to the words and the whole clock is \(2b\). [PR206, definition and exact itinerary theorem at 37d2b5d644664a746891042c199e58cfb06f1176](https://github.com/GettysburgResearch/collatz/blob/37d2b5d644664a746891042c199e58cfb06f1176/research/clock-itineraries/README.md)

For each fixed rational \(0<\epsilon<1\) and all sufficiently large \(b\), the exact high-carry count is strictly below \(2^{\lceil b/32\rceil}\) uniformly for unit endpoints \(q\ge(3/2)^{351b/352}\). A lower bound on the real carry forces the same balanced parity word to attain a large excess of even over odd inputs at a prefix. Reflecting at its first visit gives an explicit binomial upper bound at every finite clock. All terminals exhibited by the PR201 failure construction eventually lie in the uncovered range, since their heights are \(O_{q_0}((3/2)^{31b/32})\) for its fixed gate \(q_0\). [Opposing upper bound and proof](UPPER.md)

## The row can be decided by its one forward suffix

For every actual shortcut prefix, including one on an eventually convergent trajectory,
\[
             T^s x>2 \quad\Longrightarrow\quad
             2^{5s}\le 2^{8P_s(x)}x^5.                                      \tag{1}
\]
Consequently let \(a\le2^j\) be a unit, \(m\ge2\), and \(22m+5j+35\le2b\). Follow the supplied \(a\) for exactly \(b-m\) odd steps and call its odd endpoint \(q\). Then
\[
                 \mathrm{FullRow}(a,b,m)\quad\Longleftrightarrow\quad q>2.   \tag{2}
\]
In particular \(m=\lfloor b/12\rfloor\) works whenever \(b\ge30j+210\). This onset is uniform over the entire indicated ordinary source-height range.

To prove (1), the 32 starts \(0\le x<32\) enter \(\{0,1,2\}\) by shortcut clock 70 and stay there. For these starts a finite decision checks (1) at the 2,272 pairs with \(0\le s\le70\). For \(x\ge32\) use induction on the clock, starting the shorter path at \(T x\). At an even input \(2T x=x\). At an odd input \(32(3x+1)\le97x\) and \(97^5\le2^8\,32^5\), giving \((2T x)^5\le2^8x^5\). These are precisely the two factors needed in (1).

If the suffix uses \(v\) shortcut steps, (1) gives \(5v\le8(b-m)+5j\) whenever \(q>2\). The remaining time \(2b-v\) is at least \(6m+7\). PR206's exact itinerary theorem fills every requested word into the same ordinary gate \(a\) at this time. For the other implication, two odd endpoints reached from \(a\) at the same odd depth have the same clock and value. A later clock would already have counted the odd input at the earlier endpoint. This argument includes trajectories with repeated vertices. The equivalence identifies where a missing-word proof would have to act. At these budgets, even one absent requested word establishes that the supplied forward suffix has already reached the cycle through one. [Kernel proof of (1), clock uniqueness and (2)](FiniteSurvival.lean)

PR206's subsequent head independently proves (2) and allows the sharper budget \(22m+5j+35\le 2b+5Q\) when \(q\ge2^Q\). Its synchronous construction also gives the same convergent climb used below and makes one gate pass every admissible row test in a finite list. The present Lean file imports the earlier pinned itinerary. The conditional escaping terminals in PR207 occur at odd depths of order \(\sqrt b\) from a fixed gate and lie below the high-endpoint range of the ballot bound for all sufficiently large \(b\). [PR206 fixed-gate theorem](https://github.com/GettysburgResearch/collatz/blob/611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2/research/clock-itineraries/FixedGate.md) · [PR206 synchronous construction](https://github.com/GettysburgResearch/collatz/blob/611fb796d01f2c6f3794508fb4a9acf5ebc5a5b2/research/clock-itineraries/SynchronousShadow.md) · [Frozen comparison and control replays](../../../../reports/astra-global-closure-20261124/round9/rows/LATE_INTAKE.md)

## An upper bound uniform in the carry threshold fails

Use PR201's internally filtered maximum \(R_b(\epsilon)\). It counts unit sources arriving with exactly \(b\) odd steps and \(2b\) shortcut steps, relative affine carry at least \(\epsilon\), unit endpoint \(q>1\), and either \(q>b/64\) or a repeated recorded state. At every integer \(b\ge17\),
\[
         R_b\!\left(2^{-\lceil4b/5\rceil-7}\right)\ \ge\ 2^{\,b/5-5}.        \tag{3}
\]
The relative carry threshold here depends on \(b\). [PR201, exact definition and fixed-threshold equivalence at 2978d84f8a1fda9083593b26c6bf724d5976d859](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md)

Take \(m=\lfloor(b-7)/5\rfloor\), \(k=b-m\). Then \(m\ge2\), \(k\ge4m+7\), and \(k\le4b/5+12/5\). The ordinary gate \(a=6\cdot2^k-1\) follows exactly \(k\) gaps of length one to \(q=6\cdot3^k-1>b/64\). Its \(i\)-th odd state is \(6\cdot2^{k-i}3^i-1\). With \(k+2m\ge6m+7\) clocks available before the gate, PR206 constructs all \(2^{m-1}\) marked prefixes. Each corresponding source is a unit. Reading its actual residues recovers the requested word and proves that these sources are distinct. The first odd step out of \(a\) ensures relative carry at least \(1/(3a+1)\) on the entire path. Finally \(18\cdot2^{12/5}<128\) and \(m-1\ge b/5-5\), giving (3). The theorem covers every indicated finite clock irrespective of the later orbit of \(q\). The Lean theorem `climbing_witnesses` retains the supplied endpoint through the exact suffix, each requested prefix, and the integer relative-carry inequality. [Ordinary witness construction](FiniteSurvival.lean)

There are also arbitrarily large internally filtered rows of the same freely marked form whose **every displayed source provably reaches one**. Keep \(k,m\), set \(d=3^{k+1}+1\) and \(p=(2^{d-1}+1)/3^{k+2}\). Successive cubing of \(-1\) modulo increasing powers of three shows \(p\) is a positive integer. Explicitly \(3^h\mid y+1\) implies \(3^{h+1}\mid y^3+1\) when \(h\ge1\), by factoring \(y^3+1\), and \(3\mid2+1\). Replacing the gate and endpoint by \(a=6p\,2^k-1\) and \(q=6p\,3^k-1\) preserves the same ones and the full \(2^{m-1}\) population. Now \(3q+1=2^d\), so \(U(q)=1\). All recorded paths are simple. Their guaranteed threshold is \(1/(3a+1)\), which decreases along this family. The threshold in (3) is proved for \(p=1\).

## What the analytic estimates give on this row

At the central clock an elementary upper bound is already
\[
                 N_b(q,\epsilon)\le 1+(1-\epsilon)q(4/3)^b
\]
since every counted source is a distinct positive integer \(x=(4/3)^b(q-\beta)\). A closer analytic input, rStation paper 9 Theorem 18, gives a finite \(L^p\) bound on the low-real-offset mass at an exact central clock, conditional on the paper's stated mixing input. Apply its equation (C13) to one depth-\(b\) residue of Haar mass \(3^{-b}\) and the real cutoff \(q\). With \(W_b=\binom{2b-1}{b-1}\) equiprobable words this gives an upper bound \(C_p W_b(1+q)^{1-1/p}3^{-b(1-1/p)}\) on the larger count including low carries. Even for \(q=\exp(o(b))\), the infimum of the resulting exponential bases over fixed \(p\) is \(4/3\). PR201 asks for a cofinal upper strictly below \(2^{\lceil b/32\rceil}\) on the actual high-carry maximum, for each fixed rational \(\epsilon\). Tao's almost-bounded-values theorem concerns logarithmic density of starting integers. The Krasikov–Lagarias theorem gives a lower predecessor count. [Paper 9, Appendix C](https://rstation.ai/problems/collatz/papers/9) · [Tao, Forum of Mathematics, Pi](https://doi.org/10.1017/fmp.2022.8) · [Krasikov and Lagarias, Acta Arithmetica](https://doi.org/10.4064/aa109-3-4)

Under the separately proposed fixed-terminal count floor F used by PR201, polynomially decreasing thresholds can also support large populations. For \(b\) sufficiently large, take \(k=\lceil\log_3 b\rceil\) and use the \(p=1\) climb above. F at the gate \(a\), source class one modulo three, \(b-k\) odd steps and clock \(2b-k\) applies since \(k\le\sqrt{b-k}\). Appending the actual climb gives
\[
 R_b\!\left(\frac1{18\cdot 2^k}\right)
 \ \ge\ c(4/3)^b(3/2)^k/\sqrt b .
\]
The threshold is comparable to \(b^{-\log_3 2}\). Moreover F at terminal one, source class \(-1\bmod 3^{k+1}\), a depth \(h=O(k)\) within F's precision range, and clock \(2h\), supplies a convergent odd \(q\equiv-1\bmod3^{k+1}\) with \(2\cdot3^{k+1}-1\le q<(4/3)^h\). Put \(p=(q+1)/(6\cdot3^k)\). This is a positive integer by the parity of \(q\), and \(a=6p\,2^k-1\) is polynomial in \(b\). The same central floor at this \(a\) gives the displayed count with threshold \(b^{-C}\) for some fixed \(C\), now entirely in the basin of one. Both uses of F are conditional. [PR201, precise input F](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/two-end-bridge/README.md) · [Paper 48, Lemma 7 and Theorem 8](https://rstation.ai/problems/collatz/papers/48)

The open step remains the upper bound at **every fixed rational** \(0<\epsilon<1\) along arbitrarily large exact rows. The finite survival equivalence explains why a contradiction based solely on an absent prefix would already have to prove forward stopping at the supplied gate. The explicit examples distinguish that requirement from upper bounds uniform in a decreasing threshold. [Local execution and finite controls](../../../../reports/astra-global-closure-20261124/round9/rows/EXECUTION.md)
