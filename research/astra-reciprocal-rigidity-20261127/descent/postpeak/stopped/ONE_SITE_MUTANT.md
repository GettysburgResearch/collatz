# One arithmetic input can change global fate while preserving complete first-meeting clocks

Let \(T\) be the positive shortcut Collatz map. For any deterministic positive-integer map \(U\), let \(H_U(n)\) be the first original clock at which \(n\)'s orbit intersects the complete orbit of some \(1\le m<n\). Set \(H_U(n)=\infty\) if no such meeting occurs.

Choose arbitrarily large \(k\ge2\) with \(3\nmid k\), and set \(a=(4^k-1)/3\). This is an odd integer prime to three: modulo nine the powers of four have period three. Its ordinary shortcut successor is \(2^{2k-1}\), followed by halvings to the positive cycle. Let \(S_a\) be its finite complete forward orbit. Define \(U(a)=a\) and \(U(n)=T(n)\) everywhere else. This substitute violates the genuine odd update at exactly one positive input.

**For every \(n>\max S_a\), \(H_U(n)=H_T(n)\) exactly, including infinity.** For every target outside \(S_a\), its entire set of ancestors is unchanged. Indeed both maps agree until the first visit to \(a\); subsequent states under either map remain in \(S_a\). For the original source \(n\), all its states before first entry into \(S_a\) thus have the same smaller-visitor status. If entry occurs, the entry state is the same for both maps and is strictly below \(n\). That state is its own visitor at clock zero. If entry never occurs the two complete paths and all their smaller-visitor tests agree.

Any prescribed finite set of preverified convergent traces remains intact when \(a\) exceeds their maximal visited state. At every fixed cutoff on source and adjacent-pair clocks the corresponding parity and counted-fusion tests also have the same ordinary densities: only finitely many initial integers can reach \(a\) by that deadline, since each genuine reverse step has at most two choices.

Nevertheless \(U\) has an additional positive fixed point. Choose a distinct \(b=(4^\ell-1)/3>1\), \(3\nmid\ell\). Neither gate occurs in the other's genuine orbit, even under the unaccelerated map, since after the first odd departure both proceed through powers of two to the trivial cycle. Both genuine raw predecessor basins have positive lower natural density. These odd targets survive shortcutting. All but \(o(X)\) of each basin below \(X\) reach their respective gate in \(O(\log X)\) genuine steps by the fixed-target lemma. [Source-qualified inputs and lemma](SOURCE_VARIANCE.md)

From the first gate onward the modified orbit stays odd forever. The second basin avoids the first gate and still reaches the alternating cycle after a bounded additional number of steps. Thus at \(L_X=\lceil\log_2(2X)\rceil^2\) two positive fractions of the modified sources have odd frequencies respectively \(1+o(1)\) and \(1/2+o(1)\). Their empirical variance has positive lower limit by the independent-pair variance identity.

The example separates pointwise arithmetic from first-meeting statistics. It neither decides the genuine map's variance nor supplies a genuine Collatz counterexample.
