# A monotone finite shell test with two physical dates

Let \(I_X=[X,21X/20]\cap\mathbb N\), \(J_X=[5X,21X/4]\cap\mathbb N\), with both sets nonempty and all starts positive. For \(A=I_X,J_X\) sample uniformly and write \(\mu_{A,t}\) for the law of the literal shortcut endpoint after \(t\) steps. Put
\[
     \nu_{A,t}=\tfrac12(\mu_{A,t}+\mu_{A,t+3}),\qquad
     B_X(t)=\|\nu_{I_X,t}-\nu_{J_X,t}\|_{\rm TV}.
\]
This is a rational number calculable from finite ordinary trajectories. At each fixed \(X\) it decreases weakly with \(t\), since the two measures undergo the same deterministic pushforward. At **every** \(t\), it bounds from above each of the two literal fractions of escaping inputs. If every tested input visits 1, then \(B_X(t)=0\) at some finite clock. Conversely any observed zero certifies that every tested orbit is bounded, conditional only on the published simple-segment correction bound and its verified floor. It need not determine to which cycle an input belongs.

Indeed take \(x\in I_X,y\in J_X\) with \(T^{t+i}x=T^{t+j}y\) for \(i,j\in\{0,3\}\). The exact positive affine identities yield
\[
       (y/x)2^{i-j}=3^{a-b}U/V,
\]
where \(a,b\) count the odd departures up to the respective dates and \(U,V\ge1\) are the true prefix correction products. The unscaled ratio lies between \(100/21\) and \(21/4\). After multiplying by \(8\), \(1\), or \(1/8\), it respectively lies in
\[
   [(4/3)27,81/(4/3)],\quad [(4/3)3,9/(4/3)],\quad
   [(4/3)/3,1/(4/3)].
\]
Thus at least one product is at least \(4/3\), permitting equality in the displayed interval endpoints. If one source escapes then both do, and both products would be below \(4/3\) by Weaver 175 (23) and Bařina's published verification through \(2^{68}\). So an escaping endpoint in either two-date ensemble receives zero mass from the opposite ensemble, giving the two upper bounds by testing the corresponding support. Once both finite sets have all visited 1, the odd lag 3 gives the exact distribution \((\delta_1+\delta_2)/2\) for each subsequently sampled start. This proves the assertion about zeros. [Verified high simple-segment estimate and its attribution](https://rstation.ai/problems/collatz/papers/175/v1) · [Prior same-date finite kernel](../phase3/NonresonantMerge.lean)

For the supercritical source limit \((t-\mu\log X)/b_X\to+\infty\), the bounded-source parts of both dates on both intervals converge in total variation to the same mixture of uniform true cycle phases. The escape parts have disjoint supports by the finite argument and masses each tending to \(d_{\rm esc}\). Consequently \(B_X(t)\to d_{\rm esc}\). This extends the unsmoothed [fixed shell theorem](../phase3/SEPARATED_SOURCE_SHELLS.md) by permitting a finite zero under individual termination. The two-date smoothing removes the possible \(1\leftrightarrow2\) phase discrepancy at each finite scale. It uses actual integer source intervals with their own exact cardinalities. No decay estimate for the monotone upper bound is known.

## A fixed finite set contains every common transient endpoint

Let \(W\) be the union of the complete true forward orbits of all positive integers through \(2^{68}\). It is a fixed finite set because each of these finitely many starts has certified convergence to 1. If \(y\) is any common endpoint of the two ensembles at any of the four pairs of dates, then
\[
                   y\text{ is periodic}\qquad\hbox{or}\qquad y\in W.   \tag{1}
\]
The cone argument forces one of the two prefixes to have correction at least \(4/3\). If that prefix repeats a state, its ending state lies on the resulting cycle. Otherwise the prefix is simple and the published high-segment estimate forces a visit to an integer through the verified floor. Its endpoint then belongs to \(W\). This argument is finite. Given an observed meeting, inspection of the two recorded prefixes exhibits either a repeated state, giving its cycle literally, or a floor visit, for which the published computation supplies termination at 1.

Write \(\pi=\sum_{C\ {\rm bounded}}d_C\operatorname{Unif}(\Gamma_C)\), \(b_X=\sigma\sqrt{\log X}\), and \(u_X(t)=(t-\mu\log X)/b_X\). The full transition profile is
\[
          \sup_{t\ge0}\left|B_X(t)-1+\Phi(u_X(t))\,\pi(\mathbb N)\right|
                                  \longrightarrow0 .                    \tag{2}
\]
It holds also for the unsmoothed common-date shell laws. To prove it, for \(A=I_X,J_X\) the largest nonperiodic atom of \(\nu_{A,t}\) is at most \(C/\sqrt{\log X}\), uniformly in the date. This follows by dominating each proportional-interval subcount by the corresponding count through its upper endpoint and using the published all-clock bound. As \(\|p-q\|_{\rm TV}=1-\sum_y\min(p(y),q(y))\), (1) bounds the entire nonperiodic overlap of the two measures by \(C|W|/\sqrt{\log X}\). No estimate on the cardinality of \(W\) is needed for the limit. Whenever \(u_X(t)\to u\in[-\infty,+\infty]\), the restriction of each endpoint law to the actual cycles converges in TV to \(\Phi(u)\pi\). This is the periodic-phase law applied by differencing the prefix at the two ends of each fixed proportional shell; changing the clock by three or the logarithmic source height by a fixed constant does not change \(u\). The sum of the minima on periodic vertices consequently tends to \(\Phi(u)\pi(\mathbb N)\). Compactness of the extended line upgrades this sequential result to (2). [PR213, uniform atom theorem (1) and periodic restriction in (2)](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/mass/NATIVE_ENDPOINT_ATOMS.md)

The exact control checked 1,252,368 pairs of physical dates on six source scales. All 465,736 observed meetings forced the stated rational correction. It checked monotonicity at 1,338 dates. The smoothed measures agreed exactly on all six finite pairs of windows; at the first such date the unsmoothed measures still differed on five of the six. Independently of the published floor, if an actual prefix has \(U\ge4/3\) at duration \(k\), some state through that date is at most \(2k\): otherwise \(\log U\le k/(6k)=1/6<\log(4/3)\) for \(k>0\), while \(k=0\) cannot qualify. All observed meetings passed this separate date-dependent floor check. [Exact integer controls](check_shell_phase.py)

The [Lean graph kernel](PrefixOrbitWhitelist.lean) proves that a repeated state makes the tested endpoint periodic and proves the whitelist disjunction for any finite-duration predicate incompatible with a high simple prefix. Its orbit parameters instantiate with the literal shortcut iteration and `Collatz.MinimumWindow.orbit_add`. For the specialization the finite set may include zero, which is irrelevant to positive starts. The rational four-date separation and the published high-path certificate are written inputs to this application.
