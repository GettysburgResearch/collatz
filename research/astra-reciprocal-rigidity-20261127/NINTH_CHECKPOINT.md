# The remaining exceptions: spliced cycles, record types and fixed sources

**PROPOSED research. Collatz remains open.** The eighth checkpoint gives
the strongest population and variational statements. This checkpoint
tests whether an isolated ordinary exception can be amplified into
something those statements exclude. It proves several precise
obstructions and identifies a narrower predecessor-growth question after
checking an existing counterexample to the unrestricted version.

## Mixing rotations increases their denominator

Consider affine parity words whose multipliers are all below one, or all
above one. Their periodic anchors can be positive or negative. If the
chosen anchors span an interval of length \(R>0\), the anchor of their
concatenation, at every constituent cut, is a strict convex combination
of those anchors. Let its common full reduced denominator be \(d'\).
At a cut with an extremal anchor \(p_i/b_i\) and word length \(L_i\),
the two anchors share \(L_i\) parity bits. Their nonzero reduced cross
difference is divisible by \(2^{L_i}\), giving

\[
                         d'b_iR>2^{L_i}.
\]

A consecutive run at the same extremal anchor pays the combined length.
Pure repetition instead preserves both the reduced denominator and
least period. Mixing contractions with expansions falls outside the
convexity argument and has explicit counterexamples.

The [splice proof](cycles/phase9/ROTATION_SPLICES.md) also counts
distinct boundary phases. For a dictionary of \(a\ge2\) distinct words
of common length \(n\), if the sequence of dictionary symbols has least
period \(k\ge2\), pigeonholing their common prefixes yields

\[
                         d'R>2^{-n}k^{\,n/\log_2a}.
\]

This does not identify the least physical period with \(nk\); it uses
only that the physical period \(P\) is at most \(nk\). For full rotations
of an ordinary parent cycle, \(a\le n\). Combining the two elementary
inequalities with the cited logarithm-separation bound gives
\(d'>(nk)^A\), for every fixed \(A\), uniformly in \(k\) once the parent
period \(n\) is sufficiently large. The finitely many smaller positive
ordinary parent periods can be treated separately. Consequently there
is an absolute \(c>0\) such that every nonconstant rotation splice of a
positive ordinary primitive lap has

\[
                              d'\ge cP^2.
\]

Thus repetition cannot make new least periods, and nonconstant mixing
does not preserve the integer denominator. These are explicit failures
of two proposed ways to propagate a hypothetical isolated ordinary cycle
into the positive-density period family that the previous census forbids.

### Proper prefixes and the exact full return

For a signed rational parent of least period \(N\), denominator \(d\),
and a proper length-\(L\) prefix with cyclic anchor \(a/q\), the native
parity congruence always gives

\[
                         dq\,|y-a/q|\ge2^L.
\]

At a minimum-magnitude phase, the cited logarithm-separation input gives
the stronger bounds
\[
 dq\gg N^{-14.3}2^{(\log_3 2)L},\qquad
 dq\gg N^{-27.6}2^{L-(N-L)}.
\]
In particular, along any sequence of nonzero ordinary cycles with
least periods \(N\to\infty\), **every** proper prefix
\(L=N-o(N)\) at this phase has cyclic denominator \(q=2^{N+o(N)}\).
The exact full return has denominator one.

The endpoint identity explains the discontinuity. With
\(\Delta=d(T^Ly-y)\) and \(D_L=2^L-3^{s_L}\),
\[
                 \frac q{\gcd(q,d)}
                    =\frac{|D_L|}{\gcd(|D_L|,\Delta)}.
\]
At a genuine proper prefix, the displacement is nonzero. At the full
return it vanishes. Transporting the initial dyadic difference to the
other endpoint exchanges a factor \(2^L\) for \(3^{s_L}\) in the same
integer; it does not create an independent divisibility condition.

The elementary congruences are separate from their quantitative
consumers, which use Rhin's cited bound. The earlier compact-shadow
argument in PR200 and its specialized near-full denominator theorem
are explicitly credited. The finite control checked 666 same-side
mixed lists, 1,698 extremal runs, 15,818 proper factors and 73,262
transported integer differences. This is bounded verification, not a
replacement for the written universal arguments.

## Exactly which critical types refuse to split

Put \(p=\log_3 2\), \(u=\lfloor np\rfloor\), and
\(\delta_n=\{np\}\). A lower record means
\(\delta_n<\{Lp\}\) for every \(1\le L<n\). The
[record-type criterion](cycles/phase10/RECORD_TYPES.md) proves:

> Every circular binary word of type \((n,u)\) can be rotated and split
> into two nonempty contracting pieces if and only if \(n\) is not a
> lower record.

This is independent of the order of the bits. If both pieces contract,
their positive logarithmic deficits add to \(\delta_n\), which is
impossible at a lower record. Conversely, if
\(\{Lp\}<\delta_n\), the cyclic windows of length \(L\) have average
odd count within one of \(\lfloor Lp\rfloor\). Adjacent windows change
their count by at most one, so some window has exactly that count.
It and its complement both contract.

At a lower record, \(\gcd(n,u)=1\), so every such word is primitive.
Every ordering has a positive rational periodic realization. If \(U_j\)
counts its first \(j\) odd letters, the actual cycle heights have exactly
the same strict order as
\[
                              H_j=nU_j-uj.
\]
The unique minimum therefore starts a word whose every proper prefix
has multiplier above one. Its first coefficient contraction is the
exact full return.

For example, the lower-record type \((5,3)\) has the word \(11100\)
and positive rational cycle \((19,31,49,76,38)/5\). The integer heights
are \(0,2,4,6,3\), in the same order as its physical values. There are
infinitely many lower-record lengths. This supplies an infinite family
where the contracting-piece strategy cannot start, without asserting
that any nontrivial ordinary cycle occurs in that family.

## Why the meeting law cannot be read pointwise

The [signed-exception note](descent/postpeak/stopped/SIGNED_EXCEPTION.md)
contains a positive ordinary check that is especially useful for
interpreting the previous checkpoint. Take \(n=7\), its three initial
odd steps, and the prescribed smaller source \(m=3\). After their
respective ramps the canonical states are \(26\) and \(8\). They reach
one five clocks apart and remain in opposite phases forever. Thus their
counted equal-clock synchronization time is infinite. Nevertheless,
the complete orbit of \(3\) visits \(5\), and \(7\) reaches \(5\) in
seven steps. Their genuine asynchronous smaller-orbit meeting is finite.

The exact complete-sibling reduction in the previous checkpoint is an
equality of source densities. It is not a pointwise identity, even on
positive convergent sources.

The signed three-cycle supplies complementary tests. Starting at
\(-5\), the ray \((OOE)^\infty\) is maximal in every signed-offset
fiber and has homogeneous gain above one at every nonempty prefix.
Every finite prefix has arbitrarily large positive ordinary
realizations, independently of any specified finite ternary congruence.
Those ordinary representatives can change with the prefix length.
The unique source realizing the entire infinite ray is \(-5\).

The dyadic language imposing both all-prefix maximality and all-prefix
expansion has Hausdorff dimension \(H_2(\log_3 2)\), equal to that from
the expansion condition alone. Conversely, reverse trees of fixed
integer targets have at most \(F_{L+2}\) legal words of length \(L\).
Polynomially many fixed anchors at matched inverse depth therefore
cannot supply the \(2^L/\sqrt L\) scale needed to overwhelm the
square-root survival law.

There is a further elementary obstruction to amplifying the actual
global no-smaller-merger property. Complete forward-orbit intersection
is an equivalence relation on positive integers. A source has no smaller
visitor anywhere on its future precisely when it is the minimum of its
component. Every component has exactly one such source. Larger
predecessors of a hypothetical exceptional minimum are already met by
that minimum; they do not create further no-smaller-merger exceptions.

## A sparse comparison map with an escaping spine

The [comparison construction](rigidity/phase11/SPARSE_SPINE.md) changes
the shortcut map at a geometric sequence of odd multiples of three,
using bounded changes to create a genuine escaping spine for the
**changed map**. Complete predecessor sets of those marked inputs are
dyadic chains. Their union has \(O(\log^2X)\) members below \(X\).
Outside that set, the two complete trajectories agree.

Choosing the initial mark high enough preserves any prescribed finite
set of starting trajectories. An optional additional attachment can
give the changed map a positive-density escaping basin while preserving
any prescribed finite collection of verified traces. The latter version
does not assert almost-everywhere agreement of complete trajectories.

The written comparison also retains all-clock smaller-visitor population
laws through growing original deadlines \(d\le(\log_2X)/90\), with an
explicit \(O(X^{-11/3600}\log^2X)\) shell error. It imports the repository's
ordinary trajectory-image bound. The delayed-gate construction still
has vanishing weighted defects while losing positivity along the
planted escape.

This is not a Collatz counterexample. It separates the arithmetic that
the exact update formula must provide from the population estimates,
finite trace preservation and gate properties shared by these changed
maps.

## Genuine escaping trajectories would have very small other branches

Return now to the true shortcut map. Choose one common cutoff
subsequence along which every predecessor set has a limiting frequency
\(d(v)\). The
[sibling-share proof](rigidity/phase12/SIBLING_SHARES.md) uses the cited
fixed-target positivity result for odd ternary units. If \(s\) is an
escaping odd unit seed and \(x_j\) its successive odd states, then
\[
              \sum_{j\ge1}
              \frac{d(3x_j+1)}{d(Tx_j)}
                         \le\log\frac1{d(s)}.
\]
The two parent branches are disjoint at every escaping target. Their
mass increments telescope, while the main-path masses stay at least
\(d(s)>0\). In particular, the indices for which
\[
        \log(2+x_j)\frac{d(3x_j+1)}{d(Tx_j)}\ge\varepsilon
\]
have finite sum of \(1/j\), for every \(\varepsilon>0\).

Weaver's logarithmic named-sibling proposal and Wren's relative-sibling
summability are prior work, recorded in Paper 200 v2. More decisively,
Weaver Paper 202 already disproves an inverse-logarithmic lower bound
uniform over all large odd units, even for the full other-parent branch.
In the tree of one it supplies ratios \(O((\log x)^{-D})\) for every
fixed \(D>1\).

Those examples have \(d(x)\asymp(\log x)^D/x\to0\). The narrower
unproved condition that would suffice here is a lower share
\[
 \frac{d(3x+1)}{d(Tx)}\ge\frac{c_\eta}{\log(2+x)}
                  \quad\text{whenever } d(x)\ge\eta>0
\]
for all sufficiently large odd units in one common profile. An
escaping main path carries just such a fixed positive mass floor.
The packet proves neither this condition nor a substitute on a set
of odd indices with divergent harmonic sum.

## Evidence and the first unsupported conclusions

The splice control was independently replayed in both normal and
optimized Python, with unchanged source and identical outputs. It is
the thirty-ninth distinct dual-mode finite program in the packet.
No new Lean module is claimed in this checkpoint; the cumulative
independent count remains 57. The new statements are written proofs
with the indicated external inputs and independent mathematical reads.

An isolated integer cycle can still occupy an exceptional least period.
A positive component minimum can still escape the density theorems.
The energy minimum has not been shown to vanish, and its approximating
functions can lose positivity at an escaping source. The new results
locate these gaps more sharply; they do not close them.
