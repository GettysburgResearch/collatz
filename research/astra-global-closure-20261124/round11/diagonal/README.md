# An explicit vanishing range on the ordinary integer trace

**PROPOSED.** At every balanced depth and every ordinary endpoint \(q\ge 2^{139}\), the simple row has no source of relative carry at least \(9/50\). In particular,
\[
              E_b(\epsilon)=0\qquad(b\ge 2^{278},\ 9/50\le\epsilon<1).
\]
The endpoint cutoff uses Bařina's published computational coverage and accompanying path-record table. The argument is independent of the fixed-total renewal floor F and the grade-spreading input P. The conjecture and vanishing for smaller fixed thresholds remain open. [Bařina, §6](https://doi.org/10.1007/s11227-025-07337-0) · [Shortcut path records, entry 97](https://pcbarina.fit.vut.cz/path-records.htm) · [PR207, integer trace at b56c4dc](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/README.md)

## A finite-path bound above a supplied floor

Use the shortcut map \(T(x)=x/2\) at even inputs and \(T(x)=(3x+1)/2\) at odd inputs. Fix one finite segment \(z_0,\ldots,z_n\) of **distinct** positive shortcut states prime to three. Assume \(z_i\ge2^m\) for every \(i\), with \(m\ge6\). A simple odd-to-odd row expands to a distinct shortcut segment. A repetition in different halving runs would repeat their following odd state, and each halving run strictly decreases. A positive odd unit source stays prime to three.

Let \(A_j\) bound the number of segment states below \(2^j\), with \(A_j=0\) for \(j\le m\). Let \(B_j\) bound the number of odd states in \([2^j,2^{j+1})\). Put \(o=0\) to calculate \(A_j\), or \(o=1\) to calculate \(B_j\). The ambient intervals are \([0,2^j)\) and \([2^j,2^{j+1})\), respectively. Each has length \(2^j\).

Choose \(\ell\in\{0,1,2,3,4\}\), \(k=j-\ell\), and \(o\le p\le k\). If the next \(k\) steps from \(x\) have \(P\le p\) odd departures, their actual image satisfies
\[
        T^k x\le 3^P(2^{-k}x+1/3)
             \le 3^p(2^{\ell+o}+1/3).
\]
For the first inequality expand the affine offset and divide by \(3^P\). Each odd departure at \(i<k\) contributes at most \(2^{i-k}/3\). Let \(s\) be the bit length of the integer part of the last bound. Use this choice when \(A_s\) is already available. Each low-grade index \(i\) with \(i+k\le n\) gives a distinct state below \(2^s\) at its actual clock \(i+k\). At most \(k\) indices lack that clock.

Each parity word with \(P>p\) occupies exactly one residue modulo \(2^k\). Indeed, the two lifts differing by \(2^i\) after a length-\(i\) word have \(i\)th images differing by the odd number \(3^{P_i}\). The next bit splits the class between the two lifts. For \(o=1\) the first bit is fixed to one. There are exactly \(2^\ell\) copies per residue in the ambient interval. Consecutive copies differ by \(2^k\), a unit modulo three, so at most \(2^\ell-\lfloor 2^\ell/3\rfloor\) can lie on the path. Either count is therefore bounded by
\[
 A_s+k+
 (2^\ell-\lfloor 2^\ell/3\rfloor)
 \sum_{v=p+1-o}^{k-o}\binom{k-o}{v}.                         \tag{1}
\]
Take the minimum of the available bounds and the trivial \(2^j\). At each \(j>m\) first compute \(A_j\) with \(s<j\), then \(B_j\) with \(s\le j\). At \(j=m\), \(A_m=0\) is already known.

For every \(J>m\) divisible by 40 this gives
\[
  \sum_{i:\,z_i\ {\rm odd}}\frac1{z_i}
   \le R(m,J):=\sum_{j=m}^{J-1} 2^{-j}B_j+200\,2^{-J/40}.       \tag{2}
\]
For the tail, the resident elementary simple-path estimate S bounds the number of distinct odd states up to \(t\) by \(5t^{39/40}\). For each state \(u\ge2^J\), integrate \(t^{-2}\) from \(u\) to infinity and sum. Integrating \(5t^{39/40}t^{-2}\) from \(2^J\) to infinity gives (2), including when the path contains smaller states elsewhere. [S at the pinned PR201 source](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md)

At \(m=71,\ J=640\) the exact integer and rational recurrence gives
\[
   \sum_{71\le j<640}2^{-j}B_j < 590638/10^6,\qquad
   R(71,640)<593690/10^6<3/5 .
\]
The tail is exactly \(25/8192\). The certificate compares the unrounded sum to the stated rational upper bound. [Reproducible recurrence](check.py) · [Exact certificate output](../../../../reports/astra-global-closure-20261124/round11/diagonal/certificate.json)

## From physical states to the trace

For odd departures \(u\), the relative carry is \(1-w\), where \(w=\prod_u(1+1/(3u))^{-1}\). Hence \(-\log w\le R(m,J)/3\). At \(m=71\), (2) gives \(w>41/50\). Indeed, with \(r=9/50\),
\[
    -\log(1-r)\ge r+r^2/2+r^3/3>593690/(3\cdot10^6).
\]
A simpler rational estimate gives \(w>4/5\) from \(1-w\le\sum_u1/(3u+1)<1/5\).

For any floor \(2^m\), suppose that all positive sources below the floor have forward orbits bounded by \(H\). Every simple unit row ending at \(q>H\) then avoids the floor's lower interval at **every shortcut clock**. A visit to it would put \(q\) on a trajectory capped by \(H\). For any strict upper bound \(r_*>R(m,J)\), the relative carry on this row is strictly below \(1-\exp(-r_*/3)\). This implication allows arbitrary gap count and total. For PR207's balanced trace take \(s=2b,\ G_b=(4/3)^b\), and sum the counts divided by \(qG_b\) over unit endpoints \(\lceil\sqrt b\rceil\le q\le 2^{\lceil\sqrt b\rceil}\), \(q>1\).

Bařina reports convergence below \(2^{71}\). His shortcut record table gives maximum \(494114680693632162318569565806744468898092<2^{139}\) through this floor. The checker separately replays that single record-holder. Exhaustive coverage of smaller inputs remains an external input. Convergence alone gives an unspecified finite \(H\); the record table supplies the explicit onset in the opening statement. [Published computation](https://doi.org/10.1007/s11227-025-07337-0) · [Author's record table](https://pcbarina.fit.vut.cz/path-records.htm)

## A single dyadic shell on a hypothetical cycle

Let \(q>1\) belong to a positive cycle of least odd period \(p\) and shortcut period \(A\). All states in its component avoid integers below \(2^{71}\) by the external convergence verification. For **one** lap take the segment from \(q\) to the shortcut state immediately before the repeated \(q\). Those states are distinct and include every odd departure in the lap. Its multiplier \(\lambda=3^p/2^A\) satisfies \(4/5<\lambda<1\). Separately, a first-hit segment to \(q\) has distinct states, since an earlier repeat would complete a loop containing \(q\). Its residual \(w_0\) likewise exceeds \(4/5\).

In round ten's lower construction, take a prefix to an off-cycle predecessor of \(q\), then its edge into \(q\), followed by \(r\) laps. The displayed visit after the predecessor is the first \(q\) because the cycle cannot visit an off-cycle vertex. For \(k\ge1\), take the least \(r\) with \(\lambda^r\le2^{-k}\). The full residual satisfies
\[
   2^{-k-1}<(4/5)^2\,2^{-k}<w_0\lambda^r\le2^{-k}.
\]
Thus the conditional lower count from round ten is retained with a shell of width one binary digit. The narrower upper follows by inclusion. At \(q=1\) select the fixed off-cycle unit predecessor \(a=(2^e-1)/3\) large enough that \(2F_0/a<1/8,\ 2^{-e}<1/8\). Permitted even exponents include \(e=2\bmod6\). The counted prefix has real offset at most \(2F_0\), so the two pre-lap factors exceed \(7/8\). Here \(\lambda=3/4\) and \((7/8)^2(3/4)>1/2\), proving the same shell for that lower construction. The count retains F and the previous depth and clock restrictions. The moderate-deviation upper and lower exponents for a hypothetical nontrivial cycle remain compatible. [Round ten, §§2 and 5](../../round10/rows/README.md) · [PR207's original shell](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/NEAR_DIAGONAL.md)

## Remaining pointwise obligation

An escape from a fixed unit \(a\) yields the PR207 lower at \(\epsilon_a=1/(3a+1)\). Every possible such \(a\) exceeds the verified floor. Increasing \(m\) provides a bound on paths that avoid that larger floor. Applying it to every large endpoint also requires bounded forward orbits for every smaller gate. Invoking this coverage at arbitrarily high floors would itself rule out escape. Moving to later points on an escaping ray does not establish the coverage: inverse witnesses to those later endpoints can still pass through the original \(a\).

Weaver's fixed-count Haar cell has volume \(2^{-s}\) at shortcut clock \(s\). Recovering its specified integer multiplicity from the cell integral costs the reciprocal volume. The real/ternary disintegration result at a fixed root is a Cesàro statement. PR197's many-clock grid retains one original parent while exposing different exterior bits in its different tests. Its persistent-pair example permits many failed clocks on one input. A product of individual failure probabilities would require a new joint theorem for its trit queries. [Weaver, paper 19/v2, §§9.2 and 11](https://rstation.ai/problems/collatz/papers/19/v2) · [PR197 grid transfer](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/source-progress/GRID_TRANSFER.md)

[TraceCensus.lean](TraceCensus.lean) proves the physical image envelope by induction on actual shortcut steps, the common-clock injection with its finite end correction, the residual-product bound, the rational threshold comparison and the record height bit count. The parity-word census, large recurrence, logarithmic inequality and external exhaustive computation are outside that kernel proof. [Compiler inventory](../../../../reports/astra-global-closure-20261124/round11/diagonal/lean.log)
