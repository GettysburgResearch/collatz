# Capacity of ordinary references that reach one before a tripling comparison

Use the positive shortcut map \(T(2u)=u\), \(T(2u+1)=3u+2\). Write \(H(y)\) for the first shortcut clock at which \(T^h y=1\), with \(H(y)=\infty\) if there is none. For \(s\ge0\), define two sets of positive odd integers by

\[
 \begin{aligned}
 E_s&=\{q:\exists\text{ positive odd }m<q,\quad H(3m)+s\le v_2(q-m)\},\\
 F_s&=\{q:\exists\text{ positive odd }m<q,\quad
          \max(H(m),H(3m))+s\le v_2(q-m)\}.
 \end{aligned}
\]

Inequalities with an infinite left side fail. A pair in the second line shadows the same physical parity words as an actual ordinary pair that reaches 1, on each arm through its own first arrival. The two hit clocks may differ. The reserve \(s\) counts the further available source bits.

**Theorem R1.** Relative natural densities within the positive odd integers exist for \(E_s,F_s\) and are effectively computable. For every positive integer \(X\), their absolute counts up to \(X\) are at most \(X/(12\cdot2^s)\). Their relative densities are at most \(1/(6\cdot2^s)\), unconditionally on Collatz. Complete finite truncations give the following sharper bounds.

| Family | Lower bound on relative density | Upper bound on relative density |
|---|---:|---:|
| Upper arm, \(E_0\) | 0.09904194 | 0.09904203 |
| Both arms, \(F_0\) | 0.06628673 | 0.06628684 |
| Both arms and two reserve bits, \(F_2\) | 0.01657488 | 0.01657491 |

More than 98.34 percent of positive odd integers admit no member of the full family \(F_2\), regardless of the permitted reference clocks. The result concerns the supply of this certificate. It leaves the fates of excluded sources open.

## The binary mass of all first-hit triple leaves

At a positive odd unit \(y\) modulo 3, reverse odd gaps have the form \(I_e(y)=(2^e y-1)/3\) for \(e\ge1\), of the parity making the result integral. All such results are odd. A positive odd multiple of three has no odd predecessor. In reverse shortcut bits the gap has code \(0^{e-1}1\) and weight \(2^{-e}\). The first inverse gap from 1 has even \(e\). Exclude \(e=2\), which would revisit 1 and record a later return. The remaining first children have total weight \(\sum_{j\ge2}4^{-j}=1/12\). Every subsequent set of one-gap child weights sums to at most \(\sum_{j\ge0}2^{-(2j+1)}=2/3\).

Every odd triple \(3m\) that reaches 1 is a terminal leaf of this first-arrival tree. Distinct leaves have prefix-free reverse bit words. A continuation beyond a multiple of three can only double it, and never again reaches an odd value. The binary cylinders for all leaves lie disjointly in the union of the permitted first-gap cylinders. Consequently

\[
             \sum_{m\ {\rm odd},\,H(3m)<\infty}2^{-H(3m)}\le1/12.
\]

For a particular \(m\), the positive \(q>m\) realizing the upper condition belong to \(q=m+k2^{H(3m)+s}\), \(k\ge1\). At most \(X2^{-H(3m)-s}\) such sources are at most \(X\). The strict lower-reference inequality removes the additive endpoint term, even in an infinite union. Sum over the leaves. There are \(\lceil X/2\rceil\) positive odds at most an integer \(X\), giving the factor two for relative densities.

To obtain a natural density, truncate at a finite clock, keeping both clocks finite and bounded when both are required. The finite union is eventually periodic, since \(q>m\) removes only finitely many initial members of each residue class. The same count bounds the omitted relative density by a tail tending to zero. For \(F_s\), leaves with \(H(3m)\le D\) but \(H(m)>D\), including possible lower-arm nonconvergence, require separate accounting.

## Effective enclosures

Start the reverse shortcut search at 1. Each live \(y\) admits the even predecessor \(2y\). It also admits the odd predecessor \((2y-1)/3\) when \(y=2\bmod3\). Delete a return to 1 and stop at each odd triple leaf. At depth \(D\), write \(L_D\) for the number of live reverse prefixes. Uninspected leaves have total weight at most \(L_D/2^D\) by disjoint prefix capacity. Every two inverse shortcut bits have at most three live continuations, since when the odd predecessor exists the doubling predecessor is 1 modulo 3 and has no odd predecessor. Thus \(L_D\le2\cdot3^{\lfloor D/2\rfloor}\), and \(L_D/2^D\) tends effectively to zero.

For \(F_s\), run each lower \(m\) from a known leaf for \(D\) steps. Let \(P_D\) of them fail to reach 1 by then. Each contributes at most \(2^{-D-1-s}\) to the absolute density, even if it reaches 1 much later. The total relative-density remainder above the union of certified cylinders is at most

\[
                           \frac{2L_D+P_D}{2^{D+s}}.
\]

For \(E_s\) put \(P_D=0\). The error tends effectively to zero because the number of leaves through \(D\) is \(O(3^{D/2})\) by the same two-bit branching bound. For the lower endpoint, sort all certified residue classes by increasing modulus and discard each contained in an earlier retained class. The remaining dyadic cylinders are disjoint, so their relative masses add.

At \(D=40\) the exhaustive inversion gives 22,289 leaves and \(L_D=44,474\). Exactly 16,259 listed lower sources have not reached 1 by clock 40. These sources are charged in the upper endpoint. Only certified two-arm sources enter the lower endpoint. The 5,862 surviving two-arm cylinders with two reserve bits give the exact enclosure

\[
 \frac{18,224,273,713}{1,099,511,627,776}
 \le {\rm dens}_{\rm odd}(F_2) \le
 \frac{72,897,200,059}{4,398,046,511,104}.
\]

The lower endpoint for \(E_0\) is a union of 13,483 cylinders. The script reconstructs the first-hit clock by actual forward iteration for every listed triple and obtains all six rational intervals in the data file.

## An infinite ordinary family that misses every spare-bit reference

**Theorem R2.** For \(N=12\bmod18,\ N\ge12\), let \(q_N=(2^N-19)/27\). Both \(q_N\) and \(3q_N\) first reach 1 at shortcut clock \(N\), but \(q_N\notin E_1\). For \(N\ge30\), \(q_N\in F_0\).

The delayed odd merger is the zero-cross-difference family of the companion tripling-clock paper, specialized to endpoint 1. Since \(2^{12}=19\bmod27\) and \(2^{18}=1\bmod27\), \(q_N\) is a positive odd integer, and \(q_N=23\bmod32\). On every positive lift \(q=32t+23\), the first five steps of \(q\) and \(3q\) have odd dates respectively \(0,1,2\) and \(0,4\). Both reach \(27t+20=(27q+19)/32\). For \(q_N\) this is \(2^{N-5}\), followed only by halvings to 1. All earlier entries exceed 1.

For every positive odd \(m\) with finite \(H(3m)\), this clock is at least five. A shorter first hit would give \(3m\le 2^4\) since \(T(x)\ge x/2\), leaving \(3,9,15\), none of which reaches 1 in four steps. If \(0<m<q_N\) and \(v_2(q_N-m)\ge h+1\) for \(h=H(3m)\), then \(h<\log_2q_N<N\). The two upper sources agree modulo \(2^{h+1}\). After \(h\) shortcut steps they have equal parity, since each low source bit fixes one physical parity bit. But \(T^h(3q_N)=2^{N-h}\) is even and \(T^h(3m)=1\) is odd. This contradiction proves the exclusion. For \(N\ge30\) the earlier \(m=q_{N-18}\) has both first-hit clocks \(N-18\) and exactly \(v_2(q_N-m)=N-18\).

## Relation to an ordinary descent proof

The two-bit family supplies the direct positive reference in PR192's cycle-scale comparison of \(q\) with the smaller ordinary point \(m+3(q-m)/4\), using the two steps of the 1-cycle. Starting later on the same cycle does not enlarge the admitted set. A rational reference cannot extend this particular contraction: if \(q'=m+(3^a/2^b)(q-m)\) with \(a\ge1,\ 0<3^a<2^b\), and \(q,q'\) ordinary, the reduced denominator of \(m\) divides \(2^b-3^a\), which is coprime to 3. A rational \(m\) reaching 1 has denominator dividing a power of 3 by the exact affine formula. Hence \(m\) is integral. A nonpositive integer cannot reach positive 1, and preserving the first parity bit of an odd triple requires \(m\) odd.

For an actual least numerical disagreement, all its smaller positive odd references and their triples are good. That fact supplies eventual termination. The finite inequalities \(H(3m)+s\le v_2(q-m)\) or \(\max(H(m),H(3m))+s\le v_2(q-m)\) require more. R2 demonstrates failure of the spare-bit inference on ordinary inputs with explicit successful futures. R1 measures the size of the complete certificate family. Other references, mergers before the first hit of 1, unequal-parity comparisons and other forms of contraction remain available.

**Verification boundary.** The Lean module defines the ordinary shortcut dynamics, checks the exact five-step family, proves the spare-bit contradiction for all positive integer parameters satisfying the terminal power equation, and proves the uniform \(1/12\) bound for the recursive finite binary cut at every depth. The prefix-to-density passage and rational-reference argument are written proofs. The Python checker and JSON data supply the depth-40 enclosure and finite controls.

[PR192, smaller references at two clocks](https://github.com/GettysburgResearch/collatz/blob/0e313e2cd42cfce1275dbef6129ac13e9a49abd5/research/astra-minimum-source-20261124/descent/README.md). [PR192, ordinary affine lift](https://github.com/GettysburgResearch/collatz/blob/0e313e2cd42cfce1275dbef6129ac13e9a49abd5/research/astra-minimum-source-20261124/arithmetic/SourceDeletion.lean).
