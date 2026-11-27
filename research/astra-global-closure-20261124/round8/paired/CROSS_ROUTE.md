# Both arms of every prescribed binary prefix have many short ordinary continuations to 1

**R8-P5, PROPOSED written synthesis.** Assume the named one-arm analytic floor F, in the form used in PR203's mixed-cylinder depth bank. Fix a positive ordinary integer \(n\). There are absolute constants \(D,c>0\) such that for every sufficiently large \(k\) there are at least \(\exp(ck)\) distinct positive integers \(m\) satisfying
\[
 m\equiv n\pmod{2^k},\qquad m\equiv n\pmod3,\qquad
 2^{Dk}\le m<2^{Dk+1}.
\]
Both \(m\) and \(3m\) reach 1 in \(O(k)\) physical shortcut steps, and the two trajectories meet one another by \(40(k+1)\) steps. In particular they begin with the actual first \(k\) parities of the given \(n\) and \(3n\), respectively. For an odd ternary unit \(n\), all \(m\) are also odd ternary units. The implicit time constant is independent of \(k\).

There is a simultaneous restriction on the descriptions of those stopping words. Fix a positive integer \(b\). For some \(\epsilon=\epsilon(n,D,b)>0\), for all sufficiently large \(k\), **every** such \(m\) and **each** arm satisfies the following. Express any actual continuation from its clock-\(k\) state to 1 as a concatenation of at most \(b\) powers of nonempty binary words. The sum of the lengths of those base words is at least \(\epsilon k\). The linear-time upper bound and the lower description bound therefore hold on exponentially many ordinary, same-prefix, two-arm witnesses at every depth. F is required for their abundance. The description lower bound uses the signed-carry theorem and ultimately Evertse's Corollary 1. These are different sources of evidence.

## Linear steering after the prescribed history

Expose the first \(k\) bits of \(m\), fixing the prescribed cylinder. At each clock orient the two ordinary affine rays over the unexposed binary parameter as \(X,3^sX+d\), with \(s\ge0\). Initially \(s=1,d=0\). Both slopes in the current high parameter are odd, so the next parity of the base is selected by exactly one of its two binary lifts. In PR146's canonical transition table an individual step changes \(s\) by at most one and gives
\[
   1+|d'/3^{s'}|\le(3/2)(1+|d/3^s|).
\]
For example, on a downward jump at positive level the normalized new offset is \(3(d/3^s)/2-1/2\); at an odd level-zero departure it is \(1/6\pm d/2\). The two even-offset choices give \(d/(2\cdot3^s)\) and \(3d/(2\cdot3^s)+(3^{-s}-1)/2\). An upward jump at positive level gives \(d/(2\cdot3^s)+1/(2\cdot3^{s+1})\). Consequently at clock \(k\) one has \(s\le k+1\) and \(1+|d/3^s|\le(3/2)^k\).

At a positive level \(j\), write \(e_j=v_2(3^j-1)\). For \(d\) odd choose the downward bit. For nonzero \(d\) with \(1\le v_2(d)\le e_j\), choose zeros until the offset becomes odd, then descend. From \(d=0\) or \(v_2(d)>e_j\), one bit equal to 1 makes its valuation \(e_j-1\), followed by the requisite zeros and the downward bit. Thus \(1+e_j\) bits per level suffice. Since \(e_j=1\) for \(j\) odd and \(e_j=2+v_2(j)\) otherwise, the deterministic cost to reach level zero is at most
\[
 R\le 2s+\lfloor s/2\rfloor+v_2(s!)\le 7s/2.
\]
The raw offset \(d_0\) there satisfies \(1+|d_0|\le(3/2)^{k+R}\). From level zero PR146's constructive gap lemma gives an absorbing word of length at most
\[
 \frac{3}{3-\log_2 3}\log_2\max(1,|d_0|-1)+7 .
\]
The logarithmic bound follows by its odd-offset reduction \(2^a(d'-1)\le3(d-1)\) in the positive magnitudes when both are at least 2, together with the even halvings and the final three-bit cases. This is the cost of a *chosen word*, not a typical hitting-time estimate for random bits. Since the coefficient is less than 3 and \(\log_2(3/2)<1\), the total binary precision \(K\), including the first \(k\) bits, is at most \(40(k+1)\). The reached pair has identical endpoints and identical slopes on the entire selected cylinder \(m=r\bmod2^K\), \(r\equiv n\bmod2^k\). An earlier absorption can simply be retained through clock \(k\). [PR146, arbitrary-state steering and logarithmic gap lemma](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/PREFIX_COMPRESSION.md) · [Canonical transition table](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)

## Positive ordinary sources in the chosen cylinder

PR203's depth bank, sections 2–4, deduces from F alone that any one binary residue of depth \(K\), and simultaneously any one ternary residue of depth one, contains \(\gg X/(2^K3)\) predecessors of 1 in a fixed octave whenever \(K+1\le\eta\log X\). Its construction reaches a *fixed* nonperiodic predecessor of 1 at a clock \(O(\log X)\), then follows a fixed finite suffix to 1. The count and the bounds on the clock are uniform over the binary and ternary choices in this budget. Concretely, after the specified binary word one can prescribe one odd step to secure a ternary-unit output on a refined cell even if the original output was a multiple of three. The depth-bank proof then uses its central \((b,s)\) rows, each of total \(O(\log X)\). [PR203, F-only proof and first-hit clocks](https://github.com/GettysburgResearch/collatz/blob/3f2c89f12b057b8bb8655bd6fc794c772aa8b65d/research/mixed-adic-basin-density-20261124/fixed_target_depth_bank.md) · [Statement A and affine transfer](https://github.com/GettysburgResearch/collatz/blob/3f2c89f12b057b8bb8655bd6fc794c772aa8b65d/research/mixed-adic-basin-density-20261124/README.md) · [Weaver and Wren, Lemma 7 (76) and proof of Theorem 8](https://rstation.ai/problems/collatz/papers/48/v2)

Choose a fixed integer \(D>82\) with \(\eta D\log2>82\) and take \(X=2^{Dk}\). Both budget and lower bound hold for large \(k\), since \(K\le40(k+1)\). The count is at least \(\exp(ck)\) for some absolute \(c>0\), even if one removes the upper octave endpoint. These sources reach 1 in \(O(k)\) steps on the first arm. The triple coalesces at clock \(K\). If the first arm has hit 1 before \(K\), its state at \(K\) is 1 or 2 and another step suffices for the triple. Otherwise the triple follows the first arm's remaining stopping word. This proves the two physical time bounds.

## What the signed-carry estimate decides on these witnesses

Write \(m=n+2^k t\), so \(3m=3n+2^k(3t)\). For large \(k\), \(1\le t\le 2^{Dk+1}\), hence both displacement quotients have log size \(O(k)\). The [arithmetic theorem](../arithmetic/README.md) applies separately at the two *fixed* sources \(n\) and \(3n\), with target 1 on both paths. If no \(\epsilon\) as asserted existed for the fixed \(n,D,b\), one could choose increasing \(k\), a lift, a stopping continuation and a representation with ratio of total root length to \(k\) tending to zero. One of the two arms occurs on an infinite subsequence. The arithmetic theorem would force the logarithm of its positive displacement quotient divided by \(k\) to tend to infinity, contradicting the size bound. This proves the uniform positive lower rate on every sufficiently late octave, without an effective value of \(\epsilon\). The trivial description of the first-hit suffix as one word has length \(O(k)\), so the scale for fixed block count is linear on the constructed first hits.

This result gives many ordinary short stopping witnesses even in the prescribed prefixes of a hypothetical nonconvergent arm. The witnesses are distinct other integers. For a failed directed unit they therefore do not carry the nonconvergent component of its triple. Sparse terminal descriptions are realized by the quite different, very tall arithmetic lifts. No lift satisfying both source-size control and sublinear description length at an arbitrary supplied source follows.
