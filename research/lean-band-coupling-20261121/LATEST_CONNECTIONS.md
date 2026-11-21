# Targeted combination with the simultaneous band updates

**Status: targeted statement and proof-bridge inspection, not a blanket review
of these PRs.** The three heads below were refreshed during this attempt. The
only new dependency used in our formal extension is the credited elementary
height argument from PR183, proved again in `LowerMarkedMerger.lean` from our
pinned PR173 imports. Neither an analytic population hypothesis nor an
unproved trajectory-statistics premise is installed as an axiom.

| PR | Frozen head | Relevant interface |
|---|---|---|
| 180 | `5c0b59be54d7f54351141c407f84584373a06d80` | Marked predecessor populations and survivor criterion |
| 182 | `8372e302041a55057742a9e6ee9b4fa600c88fdb` | Selected-exponent marked contractions; phase/valuation comparison |
| 183 | `8659cf62ac685540cadeef320e596c852fbb0959` | Lower marked forward return from a sufficiently small directed endpoint |

## PR183: a successful extension to ordinary component mergers

The source is `research/band-completion-20261121/lean/BandDescent.lean`,
`return_descent_of_small_hit`. It requires an actual forward hit
\(T^k(n)=x\), with \(x>0\), \(2^d\le n\), and
\(4\lfloor\sqrt x\rfloor+2\lfloor\log_2x\rfloor\le d\).
It forces a smaller marked point on the forward orbit of \(n\), then uses
the return-capture theorem.

Our new `lower_marked_from_small_merger` replaces that directed-hit premise by
\(T^a(x)=T^b(n)\). With the same room bound at \(d=\lfloor\log_2n\rfloor\),
a bounded marked visit \(y=T^t(x)\) has

\[
y\le2^t x<2^{t+\lfloor\log_2x\rfloor+1}
\le2^{\lfloor\log_2n\rfloor}\le n.
\]

The merger remains physical and explicit:

\[
T^a(y)=T^{b+t}(n).
\]

The conclusion is a lower marked **component partner**, not necessarily a
forward iterate of \(n\). Our checked
`collatz_iff_marked_merger_descent` proves that this weaker directional
requirement is nevertheless sufficient for induction on marked values.
The quantitative `SmallMarkedMergerCover` is equivalent to Collatz after
an explicit kernel-checked finite base below 16.

This extension solves the induction-interface issue. It does not prove the
existence of a sufficiently small ordinary partner for every marked source.

## PR182: selected contraction cannot yet be transferred to a prescribed source

The source is `research/lean-dyadic-descent-20261121/InfiniteDescent.lean`,
`arbitrarily_strong_from_certificate`, with the physical padded identity in
`MarkedOffsetReturn.lean`.

Fix a certified odd offset \(r\), with \(T^h(r)=1\) and \(p\) odd steps.
The theorem selects suitable arbitrarily large \(q\), sets

\[
D=h+2(q-p)+1,\qquad y=2\cdot3^q+1,
\]

and proves an actual marked-return contraction from \(2^D+r\) to \(y\).
It permits any requested relative factor \(C\), but it selects \(D\).
In the displayed construction \(q>N+5(p+C+1)+r+5\). Increasing \(C\)
therefore also pushes the selected endpoint upward; a small ratio to the new
source is not an absolute bound below an earlier prescribed source.

We tested the exact reserved splice as the missing connection. For a fixed
\(n_0=2^d+r\), retaining the same residual offset in

\[
n_0=2^h3^s v+r,\qquad v\ge1
\]

forces \(s=0\), because a power of two has no factor of three. A positive
reserve requires changing the offset and finding a new shadow history.

For any reserved decomposition of that fixed source,
\(P=p_h(r')+s\le h+s\le\lfloor\log_2n_0\rfloor\), since
\(2^{h+s}\le2^h3^sv\le n_0\). Every strictly cheaper reserved partner
satisfies \(x\ge2^t\), hence
\(t\le\lfloor\log_2(n_0-1)\rfloor\). Thus arbitrarily long selected
contraction words cannot simply be inserted into the finite inverse budget
of one prescribed source.

The exact missing data are still

\[
T^t(u)=T^h(r'),\qquad a=p_t(u)\le P,
\qquad 2^t3^Pv+3^a u<3^a n_0.
\]

The inspected theorem does not supply this new short inverse history. If the
splice is performed after a forced marked visit, the right-hand bound must
refer to the earlier original source, or the resulting partner must be
converted to a smaller marked component partner by the new theorem above.

The same PR's `PhaseFrequency.lean` proves Fourier cancellation of leading
binary phases on a fixed escaping odd trajectory, and excludes escape under
an additional unbiased low-bit average. The circle character removes the
integer two-adic valuation from the phase recurrence. Our marked-return clock
bound and finite carry identities do not recover that missing low-bit
average. No independence of those quantities is used in our packet.

## PR180: population and return depth do not give survivor decay

The source is
`research/lean-forward-band-20261121/MARKED_PREDECESSOR_POPULATIONS.md`.
Its statement is a written analytic consequence of the selected-density
construction and the stated Tao fine-scale mixing input. It is not presently
a Lean formalization of that analytic input. The Lean survivor criterion
keeps `DenseBandFans` as an explicit supplied hypothesis.

The written theorem gives an absolute \(\gamma>0\): every positive target
coprime to three has arbitrarily high, target-dependent octaves containing
at least \(\gamma 2^d/(d+1)^2\) distinct marked predecessors. All reach that
target at one ordinary clock at most \(15(d+1)\). The clock bound belongs to
the written analytic statement; the Lean `DenseBandFans` structure itself
only asserts a common clock.

Combining the written clock bound with our checked return-clock theorem
has one exact consequence. Choose \(H\) with \(1024\,4^H\le d/2\).
Any two marked visits starting at binary height at least \(d/2\) must be
separated by more than \(H\) ordinary clocks. A fan path of length at most
\(15(d+1)\) therefore has at most

\[
1+\left\lfloor\frac{15(d+1)}{H+1}\right\rfloor
\]

such high marked visits. This is a bound on visits along each path, of order
\(d/\log d\), not on the number of surviving starting points. The many fan
paths can merge freely; no estimate here controls that concentration.

For a least hypothetical bad target \(q\), the large fan sources already
descend to \(q\). Proving descent below each fan member's own source is
therefore compatible with every member remaining nonconvergent. The needed
saving crosses the fixed floor \(q\), or reaches the known basin of one.
Likewise, a parity large-deviation count for failure of relative descent is
not an upper bound on avoidance of that fixed floor.

The missing global population estimate remains an upper bound on actual
survivors in all sufficiently high octaves, strong enough to beat
\(2^d/(d+1)^2\). The theorem's target-dependent witness octaves cannot be
replaced by an arbitrary subsequence of octaves with a favorable test.

## Result of the combined attempt

The successful new connection is a kernel-checked component-merger extension
of the lower-mark argument, and a valid marked-induction criterion. The
selected contraction and population routes supply complementary information,
but none of the inspected results establishes the universal witness cover.
The remaining assertion is kept as a proposition with explicit quantifiers;
it is neither postulated as an axiom nor asserted as a proved theorem.
