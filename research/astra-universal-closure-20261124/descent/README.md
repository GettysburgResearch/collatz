# Lower-core descent on short singleton exits

**PROPOSED positive descent and limits of a hitting-time rank.** For every
ternary exponent at least two, a complete progression with a one-step
initial odd run has a physical merger at a strictly smaller base. The
proof uses a converging reference and two further shortcut clocks.
The [construction and precise frontier guards](CORE_PREFIX.md) include the formula.

A different candidate descent follows a large crossing to its next lower
merger. Below, ordinary controls show that the returned source on that
route can exceed the old one both in size and in every possible clock
for reaching 1. Even its count of odd steps can grow without bound.
Collatz remains **OPEN**.

Use the least odd tripling disagreement from [PR192](../../astra-minimum-source-20261124/README.md),
commit `26f070c38ad9edd21ed7dac6efaab6554550c2a3`. The crossing
threshold is that of PR205,
`32d722c5d5597846da5dad842c8ea15742abc176`,
`research/astra-fixed-target-closure-20261124/ordinary/README.md`.
The calculations below concern positive ordinary integers.

## Exact shadow along any singleton exit

Write \(x=2^{d+1}a-1\), with \(a\) odd and positive. If
\(3^da=4u+1\), the first odd run ends with exactly one even input before
the next odd entry. The two synchronized paths satisfy
\[
 T^{d+2}x=6u+1,\qquad T^{d+2}((x-1)/2)=u .
\]
Indeed the first \(d+1\) odd steps of \(x\) give \(12u+2\);
the first \(d\) odd steps of its shadow give \(4u\). In particular, from a
site \(x=6v+1\) this edge transports the actual orbit of \(3v\) to \(u\)
in exactly as many clocks as it takes to transport \(x\) to \(6u+1\).
Thus a good lower shadow stays good at its returned source at any height.
The hypothesis that \(a\) is odd identifies the full run; the displayed
path identities themselves hold for every positive \(a\).

## An unbounded loss in the hitting clock

For \(t\ge0\), put
\[
 m=56+72t,\quad n=7\cdot2^m-1=3q,\qquad
 u=(7\cdot3^{m-1}-1)/4,\qquad y=6u+1.
\]
Here \(q\) is odd, \(27\mid n\), and \(u\equiv3\pmod8\). These
follow from \(7\cdot2^m\equiv28\pmod{54}\) and
\(7\cdot3^{m-1}\equiv13\pmod{32}\), by periodicity.
The first actual run gives \(T^{m+1}n=y>2n\), while its lower shadow
gives \(T^{m+1}((n-1)/2)=u\). Thus on the hypothetical minimum's
hypotheses \(u\) is good: if \(n=3^h w\), then \(h\ge3\) and the
positive source \(2^hw-1<q\) reaches \(n-1\) in \(h\) steps.

The *very next run* of \(y\) joins \(3u\). Writing \(u=8v+3\)
gives the two literal paths
\[
 \begin{aligned}
 48v+19&\to72v+29\to108v+44\to54v+22\to27v+11,\\
 24v+9&\to36v+14\to18v+7\to27v+11.
 \end{aligned}
\]
Consequently \(T^{m+5}n=T^3(3u)\). If \(n\) were the least bad
multiple, this would return an odd disagreement at \(u\) with a good lower arm.

The old source \(q\) reaches 7 in \(m\) clocks, first making an odd
step and then halving. The path
\(7,11,17,26,13,20,10,5,8,4,2,1\) gives the exact first hitting time
\(m+11=67+72t\). All earlier entries exceed 1. Meanwhile
\(u>q\) and \(u\ge2^{83+108t}\). For the latter inequality, use
\(2u=(7\cdot3^{m-1}-1)/2\ge 3^m\) and
\(3^m=9^{m/2}\ge2^{3m/2}\).
Since \(z\le2T(z)\) for every positive input, any clock \(h\) at
which \(T^h(u)=1\) satisfies
\[
             h\ge83+108t\ge (m+11)+16+36t .
\]
Thus unbounded extra physical clocks are required even immediately after
the first crossing, when the next comparison gives an actual merger.
No convergence assertion about every returned \(u\) is needed for this
lower bound.

## Arbitrary finite continuation of the returned source

For every \(d>0\),
\[
 v_2(u(t+d)-u(t))
 =v_2(3^{72d}-1)-2=3+v_2(d).
\]
To verify the last equality, \(v_2(3^{72}-1)=5\), an odd exponent of
\(3^{72}\) preserves this valuation in the difference from 1, and each
squaring raises it by exactly one since the base is 1 modulo 4.
Hence \(v(t)=(u(t)-3)/8\) permutes the residue classes modulo
\(2^k\) for every \(k\). Differences of parameters divisible by
\(2^k\) preserve the residue, and differences of distinct parameters
modulo \(2^k\) give distinct residues.

The three initial clocks of the returned source are
\(8v+3\to12v+5\to18v+8\to9v+4\). Since 9 is odd,
\(T^3u\) therefore takes every residue modulo \(2^k\), for infinitely
many parameters each. Every prescribed word of \(k\) shortcut parities
selects one such residue. For an elementary justification, two sources
differing by \(2^k\) preserve their first \(k\) parities and their
endpoints differ by an odd power of 3, so exactly one lift supplies each
next parity. The claim follows inductively starting with the empty word.

In particular choose \(J\) odd inputs in succession after clock 3, and
take a sufficiently large parameter that \(2^{J+3}<u\). None of these
clocks can already have reached 1. This forces at least \(J+2\) odd
inputs before any possible first hit; the old arm uses exactly six. The
same choice forces a subsequent ascent by a factor at least \((3/2)^J\)
relative to \(T^3u\). Each prescribed finite word is realized on
ordinary inputs. Different words may require different parameters.

At \(m=56\), direct ordinary iteration gives first hitting clocks
\(H(q)=67\), \(H(u)=440\), \(H(n)=422\) and \(H(3u)=364\).
Thus both arms converge in this control. It refutes a direct
unconditional stopping-time comparison without making any assertion
about an actual counterexample.

[Lean proof](CrossingRank.lean) checks the two synchronized paths, all
three modular assertions, the strict crossing, both arms of the merger,
the old arm's explicit hitting clock and the universal lower bound on
every possible returned clock. The permutation and odd-count statements
above are written proofs. [Ordinary replay](check_crossing.py) verifies
the finite controls. The open step is still a descent valid for **every**
least disagreement, possibly using the ternary information in \(u\) or a
different source in one of the two components. This example places no
restriction on such an alternative.

[An all-clocks test for the smaller smooth tower](SMOOTH_RAY.md) records a separate obstruction to an affine extension of the positive minimum-core theorem.
