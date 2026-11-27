# Explicit signed exceptions to a pointwise lifting argument

The adjacent-pair bound concerns Haar sources, and its ordinary application gives a natural-density statement. Two explicit signed examples separate this conclusion from a pointwise positive-integer proof. One gives a nonmerging adjacent pair. The other has expanding homogeneous gain at every original prefix. Both are rational and periodic at the upper source.

For an \(O,E\) word \(w\), write \(2^{|w|}T_w(x)=3^{f}(x+1)+C_w\), where \(f\) is its odd count. A word is maximal if no equal-length word of strictly higher grade shares its signed offset. For \(x\in\mathbb Z_2\), set
\[
                   x_\delta=3^{-\delta}(x+1)-1,\qquad \delta\ge1 .
\]
If a physical prefix \(w\) of \(x\) is nonmaximal, its matching heavier word \(\beta\) of grade \(f+\delta\) yields \(T^{|w|}(x_\delta)=T^{|w|}(x)\). Indeed its formal endpoint at \(x_\delta\) equals the integral two-adic upper endpoint; divisibility of its numerator by \(2^{|w|}\) gives the actual initial parity word \(\beta\). This implication applies to rational as well as nonrational inputs. Its converse can fail on rational inputs through accidental affine intersections. [Parity and offset derivation](SYNCHRONIZATION.md)

## Two members of the signed three-cycle

The signed cycle is \(-5\to-7\to-10\to-5\). Take \(x=-7\), with parity ray \((OEO)^\infty\). Then \(x_1=-3\) reaches the fixed point \(-1\) via \(-4,-2\). The adjacent signed pair \(2x_1,2x_1+1=-6,-5\) goes in one step to \(-3,-7\); its two complete forward orbits are disjoint. The state \(-5\) of the adjacent pair is already on the three-cycle, and the state \(-6\) and its entire future are outside that cycle.

For \(\delta\ge2\), the centered coordinate of \(x_\delta\) starts at \(r=x_\delta+1=-2/3^{\delta-1}\). The centered updates are \(r\mapsto3r/2\) at an \(O\) and \(r\mapsto(r+1)/2\) at an \(E\). While a positive power of three remains in the reduced denominator, an \(E\) preserves that power and an \(O\) reduces it by exactly one. All these states are two-adic integers, so the ordinary rational denominator contains no power of two. Hence the signed trajectory cannot reach the integer three-cycle before the \((\delta-1)\)-st odd step. If that step occurs at clock \(d\ge1\), its centered value is an ordinary integer satisfying \(r_d\ge-2/2^d\ge-1\), since all affine even-edge additions are nonnegative in the ordinary real ordering. Its signed value is at least \(-2\). The integers at least \(-2\) are forward-invariant. If the required step never occurs, the trajectory remains nonintegral. Thus the orbit of \(-7\) is disjoint from the complete orbit of every \(x_\delta\), and every finite prefix of \((OEO)^\infty\) is maximal.

The rotation \(x=-5\), with word \((OOE)^\infty\), also avoids every scaled companion. For \(\delta=1\), \(x_1=-7/3\to-3\to-4\to-2\to-1\). For \(\delta\ge2\) start at \(r=-4/3^\delta\). At the first denominator-clearing clock \(d\ge\delta\ge2\), the ordinary centered integer satisfies \(r_d\ge-4/2^d\ge-1\), and the same argument applies. This proves maximality of every prefix of \((OOE)^\infty\). Each complete three-letter block has homogeneous gain \(9/8\), and the one- and two-letter partial-block factors are \(3/2,9/4\). Therefore every nonempty prefix has homogeneous gain strictly greater than one. Every positive ordinary realization of that finite prefix remains strictly above its own starting point at each of its displayed positive clocks.

## Exactly what a positive lift preserves

For any \(L\ge4\), the positive pair \(y_L=2^L-3,\ x_L=3y_L+2=3\cdot2^L-7\) follows the respective signed parity words of \(-3,-7\) for \(L\) steps. At a clock \(j\le L\), the two lifts differ from their signed states by \(3^{a}2^{L-j}\) and \(3^{b+1}2^{L-j}\), where \(a,b\) count their respective odds. Counted fusion from initial gap one requires \(a=b+1\); the lifts would then differ by the nonzero difference of the signed states. Thus no counted fusion occurs by \(L\). Even equality of the two values at the same clock cannot occur by \(L-4\), because unequal integer coefficients differ by at least one and the signed-state differences have magnitude at most nine. These assertions concern synchronous clocks. They do not exclude a late visit by one complete visitor orbit to an earlier displayed point.

For an ordinary original source with \(H\) initial odds, write \(n=2^Hv-1\), with post-ascent state \(x=3^Hv-1\). For either signed example \(x_*\), choose \(v\equiv3^{-H}(x_*+1)\bmod2^L\). This forces its entire postword of length \(L\). Independently a desired ternary class \(n\equiv a\bmod3^K\) fixes \(v\equiv2^{-H}(a+1)\bmod3^K\). The Chinese remainder theorem gives arbitrarily large positive ordinary \(v\) satisfying both conditions. For the \(-5\) word, if \(H\ge6q+3K+3\), \(a\in F_K\), and \(2n\ge K(1+3^K)\), the existing common-guard theorem excludes every positive smaller endpoint visitor of odd cost at most \(H+f+K\). Here \(f,q\) count the postword's odds and evens. For \(H\ge400,\ 6(L+1)\le H\), the all-clock theorem additionally gives a positive relative density of completely protected sources in the full dyadic cylinder. It does not assert this latter fraction on each individually prescribed ternary class. [Common finite guard](../../../root/phase5/COMMON_PROTECTION.md) · [All-clock cylinder result](STOPPED_LAW.md)

The positive representatives above can depend on \(L\). Holding \(H\) fixed and imposing the \(-5\) word at every depth specifies \(3^Hv-1=-5\) in \(\mathbb Z_2\), since the parity map is injective. This unique compatible parameter is \(v=-4/3^H\), outside the positive ordinary sources. The exact signed examples therefore do not contradict the ordinary conjecture.

## The expanding-prefix restriction retains its full symbolic dimension

Let \(\mathcal B\) be the infinite dyadic words whose every prefix is maximal and whose every nonempty prefix satisfies \(3^{f_j}>2^j\). With \(\alpha=\log_3 2\), its dyadic Hausdorff dimension is exactly
\[
                  \dim_H\mathcal B=h_2(\alpha),
 \qquad h_2(u)=-u\log_2u-(1-u)\log_2(1-u).
\]
This equals the dimension obtained by imposing only the displayed expanding-prefix condition.

Prepending \(m\) odd letters preserves maximality. In the real formal walk from \(-1\), each initial \(O\) fixes \(-1\). The first \(E\) gives \(-1/2\), then each subsequent letter increases the reduced binary denominator exponent by one (the updated numerator stays odd). Words of a common length and common signed endpoint therefore have the same initial run of odds. An all-odd word is the only word of its length ending at \(-1\). Consequently every competitor to \(O^mw\) starts with \(O^m\); stripping these letters preserves the grade difference and signed endpoint equality. In particular an all-prefix maximal path stays so after an initial odd buffer.

Fix \(p>\alpha\) below one. The grade-by-grade fibre estimate proved in the companion note gives the all-prefix maximal event tilted Bernoulli mass at least \((2p-1)/p>0\). Under this same tilt,
\(\log(3^{f_j}/2^j)/j\to p\log3-\log2>0\) almost surely. Its running infimum is finite almost surely. Choose \(m\) so that the chance of this infimum being at or below \(-m\log(3/2)\) is less than half the known all-prefix maximal mass. Their intersection supplies a positive-mass set of maximal suffixes whose negative excursions fit strictly inside the odd buffer. The event that the first \(m\) letters are all odd and the remaining suffix belongs to this set still has positive tilted mass. Every resulting path lies in \(\mathcal B\). The tilted cylinder mass argument in the companion note gives \(\dim_H\mathcal B\ge h_2(p)\). Let \(p\downarrow\alpha\). For the upper bound, at depth \(j\) even the unrestricted expanding words require \(f_j>\alpha j\), so there are at most \(2^{j h_2(\alpha)+o(j)}\) candidate cylinders by the binomial entropy bound. This proves the claimed equality. [Tilted maximal-fibre estimate](SYNCHRONIZATION.md)

An integer lacking smaller mergers would entail a particular positive source persisting through infinitely many clocks. The estimates above count changing finite ordinary sources or infinite two-adic paths. A sufficient but unproved amplification step would be to deduce from one positive exceptional source at least order \(2^L/\sqrt L\) distinct exceptional depth-\(L\) residues with an unbounded constant factor. A single persistent residue contributes only one at each depth, while the square-root Haar tail permits order \(2^L/\sqrt L\). The examples explain why low-complexity parity words, ternary guards and the expanding-prefix floor do not themselves provide that amplification.

## Matched-depth inverse amplification

Let \(M_d\) be the maximum, over fixed integer targets, of the number of legal reverse words with exactly \(d\) shortcut letters. One always has the inverse even step \(y\mapsto2y\); an inverse odd is possible only at \(y=2\bmod3\). At such a branch, choosing even first lands at \(1\bmod3\), where the next letter is forced even. Thus for \(d\ge2\),
\[
                 M_d\le M_{d-1}+M_{d-2},\qquad M_0=1,\ M_1\le2.
\]
At targets without the initial odd choice even the first term alone bounds the count. Consequently \(M_d\le F_{d+2}\), with \(F_0=0,F_1=1\). The number of distinct physical sources feeding polynomially many fixed anchor states in at most \(L\) reverse steps is at most \(\mathrm{poly}(L)\varphi^L\), even before imposing any synchronized pair condition. The same upper bound holds for the number of distinct depth-\(L\) dyadic residues furnished by those sources. This is exponentially below \(2^L/\sqrt L\). A proof by amplification would need more input than these matched-depth reverse embeddings; longer reverse depths, moving anchors, and families with additional arithmetic structure are outside this count.

## A positive point where the counted model misses a real merger

The source \(n=7\) has exactly \(H=3\) initial odd steps and prescribed smaller sibling \(m=3\). At the ends of their respective ramps the canonical values are \(x=26\) and \(y=8\). Their initial ordinary paths are
\[
 26\to13\to20\to10\to5\to8\to4\to2\to1,\qquad
 8\to4\to2\to1 .
\]
There is no equal-clock meeting in these displayed prefixes. The first visits to 1 differ by five clocks, so the two states have opposite phases in the positive two-cycle forever after. The counted synchronization time is infinite. The prescribed ordinary visitor nevertheless reaches \(5\) in one step from \(m=3\), and the original \(7\) reaches \(5\) in seven steps. This is its first original point visited by that particular sibling. The exact unrestricted sibling-law identity in the companion note is an equality of relative natural densities. This convergent positive counterexample shows exactly why it cannot be used as a pointwise identity or as a demand that all positive inputs counted-fuse. [Density identity](SYNCHRONIZATION.md)

## The actual source obstruction is one minimum per component

For positive integers, let \(C(n)\) consist of starts whose complete forward orbit meets that of \(n\). This is an equivalence class: two meetings on a shared third orbit can both be advanced to the later of their two clocks there. Consequently
\[
 \bigl[\text{no smaller positive start meets the orbit of }n\bigr]
                  \quad\Longleftrightarrow\quad n=\min C(n).
\]
Every component has exactly one such source. Even arbitrarily many larger predecessors of a hypothetical bad minimum would therefore generate **no additional sources** with this global no-smaller-merger property: the minimum itself is already a smaller visitor to each of their complete orbits. An amplification proof must instead track a different property, such as unresolved pairs from distinct components, or construct genuinely new component minima. The signed examples and the matched-depth count above address limitations of those proposed routes. They furnish no additional positive component.
