# Complete inverse continuation and the exact reserved-merger frontier

## Result and scope

This packet proves universal arithmetic and completeness theorems for **actual
finite ordinary Collatz histories**. It supplies a complete continuation rule
after an inverse history consumes the ternary reserve, and it characterizes
exactly which ordinary mergers the full nonnegative reserved architecture
represents. It does not supply a smaller partner for every positive source.

The map is the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

Write \(A_t(x)\) for the number of odd inputs in the first \(t\) steps from
\(x\). The Lean function is `CollatzEndpointSteering.odds t x`; the clock is
the first argument throughout. All source and shadow variables are ordinary
nonnegative integers. Positivity is stated explicitly when required.

The formal files are `CollatzGlobalClosure/InverseBudget.lean` and
`CollatzGlobalClosure/ReservedMergerCompleteness.lean`. They import the
core-only port of the existing `EndpointSteering.lean`; no mathlib facts,
`sorry`, custom axioms, `native_decide`, or unsafe computation are used.
The build receipt records the exact source hashes, commands, exits, and
axiom output. Source predicates and remaining open obligations below are
not postulated as axioms.

## 1. Exact normalized quotient

For every \(x,t\),

\[
\boxed{\left\lfloor\frac{T^t(x)}{3^{A_t(x)}}\right\rfloor
       =\left\lfloor\frac{x}{2^t}\right\rfloor.}
\tag{1}
\]

More directly, every integer threshold \(v\) satisfies

\[
3^{A_t(x)}v\le T^t(x)\quad\Longleftrightarrow\quad 2^tv\le x.
\tag{2}
\]

The one-step assertion is elementary in both parities. In the odd case,
\(3v\le(3x+1)/2\) is equivalent to \(2v\le x\), since all variables are
integers. Induction composes these exact thresholds. Formula (1) follows by
applying the thresholds to the two integral quotients. In particular,

\[
x<2^t\quad\Longleftrightarrow\quad T^t(x)<3^{A_t(x)}.
\tag{3}
\]

Lean names: `quotient_threshold`, `normalized_quotient`, and
`short_source_iff_small_endpoint`.

## 2. Constructive inverse extraction, including an exhausted reserve

Suppose a supplied **actual** history satisfies

\[
T^t(x)=3^P v+y,
\qquad a=A_t(x).
\]

Put

\[
d=(a-P)_+,\qquad
W=3^{(P-a)_+}\left\lfloor\frac{v}{3^d}\right\rfloor,
\qquad
Y=3^P(v\bmod 3^d)+y.
\tag{4}
\]

Then there is a unique ordinary \(u\ge0\) with

\[
\boxed{x=2^tW+u,\qquad A_t(u)=a,\qquad T^t(u)=Y.}
\tag{5}
\]

The proof first uses Euclidean division to obtain
\(3^Pv+y=3^aW+Y\). Formula (2) gives \(2^tW\le x\), so
\(u=x-2^tW\) is nonnegative. Exact binary lifting then preserves the complete
actual parity word and subtracts precisely \(3^aW\) from the endpoint.

When \(a\le P\), this recovers the previous reserve rule:
\(W=3^{P-a}v\), \(Y=y\). When \(a>P\), it retains the full remainder
\(3^P(v\bmod 3^{a-P})\). No extra odd-count branch is discarded.
If additionally \(y<3^P\), the exhausted-budget endpoint satisfies
\(Y<3^a\), so (3) gives \(u<2^t\). Consequently \(u=x\bmod 2^t\).

The converse is constructive too. Given any ordinary shadow history with
\(a=A_t(u)\) and \(T^t(u)=Y\), the integer
\(x=2^tW+u\) is an actual inverse history into \(3^Pv+y\). The theorem
`complete_carried_rebase` states both directions with all quantifiers.

The leading coefficient survives exactly when

\[
W>0\quad\Longleftrightarrow\quad 3^{(a-P)_+}\le v.
\tag{6}
\]

This allows continued extraction beyond the original budget using the
**magnitude** of the remaining quotient; divisibility of \(v\) by the
consumed power of three is not assumed. The missing divisibility is retained
as an explicit endpoint remainder.

Lean names include `extract_endpoint_block`, `extract_reserved_inverse`,
`carry_partition`, `extract_inverse_with_carry`,
`extract_inverse_with_canonical_carry`, `retained_coefficient_positive_iff`,
`carried_rebase_hits`, and `complete_carried_rebase`.

## 3. Complete characterization of the full reserved architecture

Allow every nonnegative decomposition, not merely a finite menu. A reserved
certificate for a merger between \(n\) and \(x\) at clocks \(h,t\) consists of

\[
n=2^h3^s v+r,\qquad v>0,
\]

and an ordinary shadow \(u\) with

\[
T^t(u)=T^h(r),\qquad
a=A_t(u)\le A_h(r)+s,
\]

\[
x=2^t3^{A_h(r)+s-a}v+u.
\]

The new completeness theorem proves the exact equivalence

\[
\boxed{\text{such a reserved certificate exists}
\quad\Longleftrightarrow\quad
T^t(x)=T^h(n),\quad 2^h\le n,\quad 2^t\le x.}
\tag{7}
\]

The same equivalence holds with the **canonical** restrictions
\(0\le r<2^h3^s\) and \(v=\lfloor n/(2^h3^s)\rfloor\). Thus every actual
merger inside both sources' binary horizons has a reserved representation
with the maximal quotient. The forward direction is the existing lifting mechanism;
the reverse direction constructs all of its data from the actual merger.

Here is that construction. Set

\[
r_0=n\bmod2^h,\quad v_0=\lfloor n/2^h\rfloor,\quad
p=A_h(r_0),\quad a=A_t(x),\quad s=(a-p)_+.
\]

Choose

\[
V=\lfloor v_0/3^s\rfloor,
\qquad R=2^h(v_0\bmod3^s)+r_0.
\]

Then \(n=2^h3^sV+R\), the new shadow has the same \(h\)-step odd count
\(p\), and the unrestricted carry theorem constructs \(u\). If \(a\le p\),
\(V=v_0>0\). If \(a>p\), canonical extraction gives
\(x=2^tV+(x\bmod2^t)\); the partner horizon \(2^t\le x\) forces \(V>0\).
This proves the positivity required by a genuine reserved certificate.
The construction also gives \(R<2^h3^s\) and the maximal-quotient identity.
Therefore the outer parameter menu in PR184's `find_reserved` experiment is
complete in this precise two-horizon domain. Its inverse-tree node cap can
still truncate an implementation; the theorem does not certify an exhausted
search when that cap was reached.

Lean names: `short_merger_to_reserved`, `reserved_to_short_merger`, and
`reserved_splice_iff_short_merger`, `short_merger_to_canonical`, and
`canonical_reserved_splice_iff_short_merger`.

## 4. The intrinsic finite frontier and ancestor padding

Whenever \(W>0\), (5) forces \(2^t\le x\). Thus any represented partner
\(x<B\) occurs at

\[
t\le\lfloor\log_2(B-1)\rfloor.
\]

This is an exhaustive mathematical bound, independent of a search's node cap.
If a smaller history has a longer clock, the unrestricted carry theorem
instead forces \(W=0\) and \(Y=3^Pv+y\). Its recovered shadow is the full
original source \(u=x\). The representation remains complete but no longer
reduces the inverse problem. This degeneration is proved, not hidden as a
successful recursive step.

Ordinary inverse padding cannot improve the available horizon. If
\(T^k(M)=n\), formula (2) gives the exact equivalence

\[
\boxed{2^{k+h}\le M
\quad\Longleftrightarrow\quad 3^{A_k(M)}2^h\le n.}
\tag{8}
\]

Therefore \(n<2^h\) implies \(M<2^{k+h}\) for **every** ordinary ancestor
\(M\). Additional binary height pays for the ancestor prefix's own clocks;
each odd input also consumes a factor of three in the remaining budget.

Lean names: `affordable_inverse_clock`, `smaller_affordable_inverse_clock`,
`long_inverse_exhausts_carry`, `ancestor_horizon_exact`, and
`ancestor_padding_preserves_late`.

## 5. Full-closure attempt and first unsupported step

The attempted global route was to combine ordinary inverse construction and
upper-bit mergers from PR146 with the selected marked contractions in PR182
and the reserved continuation in PR184. The desired outcome was an actual
partner below the **original** source, rather than below a potentially much
larger marked visit.

PR146's `SHORTER_ANCESTORS.md` constructs an ancestor of a prescribed target
in every binary cylinder. Its additional binary-clock cost is
\(D(p)=\exp(O(p/\log(p+2)))\). That construction does not establish the
coefficient saving \(2^t/3^a<2^h/3^p\) required for a cheaper replacement
history. Formula (8) now explains exactly why simply prepending a large
ordinary ancestor cannot repair a late original meeting clock.

PR182's selected-exponent theorem chooses arbitrarily large new sources with
strong marked contractions. It does not supply an absolute saving below a
prescribed earlier source. The carried grammar removes the old odd-count cap
from the algebra, but it does not change those quantifiers.

The remaining global obligation is to choose, for every prescribed \(n>1\),
actual clocks and a positive partner \(x<n\) with \(T^t(x)=T^h(n)\), or to
prove a genuinely decreasing replacement criterion on marked components.
Theorems (4)–(7) describe and recover every covered witness; they do not prove
that the required smaller witness exists. Once the high coefficient vanishes,
continuing the same recursion just presents the full inverse problem again.

The unmodified premise that every source has a smaller merger inside both
binary horizons is false already at small ordinary sources. This does not
decide whether a modified premise holds beyond a cutoff. No finite census is
used to infer an all-source statement, and this packet does not claim the
Collatz theorem has been completed.

## Frozen inputs inspected

| Source | Frozen head | Inspected paths relevant to this attempt |
|---|---|---|
| PR146 | `f431078244e868dc699fad011044f0d5e7f76437` | `research/upper-bit-mergers/SHORTER_ANCESTORS.md`, `PREFIX_COMPRESSION.md`, `THREE_RAY_SMALLER.md`, `STABILIZED_CORE_DESCENT.md`, `WHOLE_INTERVAL_SYNCHRONIZATION.md` |
| PR182 | `8372e302041a55057742a9e6ee9b4fa600c88fdb` | `research/lean-dyadic-descent-20261121/InfiniteDescent.lean` |
| PR184 | `366dab89ee9548084ab9b5e4e90ff82abf287a20` | `research/lean-band-coupling-20261121/lean/OffsetDescent.lean`, `SourceBoundedMerge.lean`, `LowerMarkedMerger.lean`, `ClockSteering.lean`, `RisingMerge.lean`, and `LATEST_CONNECTIONS.md` |
| PR175 foundation | `06215e69346c4d32bf970af9c846a6894586c1e7` | `research/lean-global-closure-20261121/CollatzGlobalClosure/EndpointSteering.lean`, subsequently ported to Lean core without changing its statements |

These are targeted source inspections, not blanket independent reviews of the
listed PRs. The new formal proofs depend only on the stated core foundation.
