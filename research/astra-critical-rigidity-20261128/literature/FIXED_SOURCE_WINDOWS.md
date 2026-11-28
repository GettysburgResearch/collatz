# A restriction on every late window of one exceptional trajectory

**Status: PROPOSED corollaries** of the [open height theorem](OPEN_ARC_HEIGHT.md). The first statement retains the same positive ordinary source for all times. The second example shows a limit on effectivizing its underlying sharp coefficient.

## Uniform windows in the parity sequence of a fixed source

Let \(x_t=T^t(n)\) for one fixed positive integer whose orbit is not eventually periodic. Fix an integer \(K\ge1\) and a real \(\lambda>\log_2(3/2)\). Let \(D_t=\lceil\lambda t\rceil\). There is a positive \(\delta_{K,\lambda}\) such that, at **all sufficiently large** \(t\), every presentation of the actual parity window \([t,t+D_t)\) by at most \(K\) powered words has total literal length at least \(\delta_{K,\lambda}D_t\). Templates may be chosen separately for every time and need not come from a preassigned dictionary. In particular this holds on every window \([t,2t)\). With separated rational reference arcs in place of powered words, the corresponding conclusion is that some reference endpoint has logarithmic height at least \(\delta'_{K,\lambda}D_t\).

Both shortcut branches satisfy \(T(x)+1\le(3/2)(x+1)\), so
\[
 \frac{\log_2 x_t}{D_t}\le
 \frac{t\log_2(3/2)+\log_2(n+1)}{\lceil\lambda t\rceil}.
\]
This is eventually at most \(1-\eta\), where \(\eta=\tfrac12(1-\log_2(3/2)/\lambda)>0\) is independent of \(n\). A powered piece cannot start at its own center, since that would force an ordinary return. If the asserted bound failed for a sequence of windows with total literal cost \(o(D_t)\), it would contradict the sharp original-source bound. Uniformity of \(\delta\) follows by the contrapositive formulation in [POWERED_WORD_HEIGHT.md](POWERED_WORD_HEIGHT.md): all positive starting states and all windows satisfying the same gap \(\eta\) are covered beyond one onset in \(D_t\). For reference arcs apply the same argument to the maximum of their endpoint logarithmic heights. The onset along the fixed orbit can depend on \(n\). An explicit constant or deadline is not obtained.

This is stronger in a specific respect than iterating a bound with a \(K\)-dependent multiple of the starting bit length. A large such multiple can absorb an entire window of length \(t\) starting at \(x_t\). The coefficient one in the open theorem gives the restriction above for *every fixed* \(K\). Complexity here measures only this finite list of powered blocks or matching rational reference arcs. A hypothetical orbit can have parity windows which require the stated linear literal cost; no opposing universal compression has been proved.

## A logarithmic additive excess is unavoidable even on simple integer paths

For odd \(t\ge1\), put \(a=2^t\) and \(n=2^a-1\). Its first \(a\) shortcut departures are odd: after \(j\le a\) of them the value is \(3^j2^{a-j}-1\). The final value \(3^a-1\) is even and
\[
 v_2(3^{2^t}-1)=t+2.
\]
Indeed \(3^2-1=8\), and each later squaring adds the factor \(3^{2^j}+1\equiv2\pmod8\) for \(j\ge1\). Thus a two-run prefix has physical length \(D=a+t+2\). Its excess above the starting bit logarithm is
\[
 D-\log_2 n=t+2-\log_2(1-2^{-a})=\log_2D+2+o(1).
\]
All vertices, including the last, are distinct. The initial odd vertex is 0 modulo three; all later odd-run vertices are 2 modulo three. The odd landing after the \(t+2\) even steps is 1 modulo three since \(t\) is odd. The interior even values strictly decrease and the odd-run values strictly increase. Hence an additive constant cannot replace the \(o(D)\) in the two-piece sharp height estimate, even if physical simplicity is required. This example neither proves nor disproves an additive \(O(\log D)\) upper estimate.
