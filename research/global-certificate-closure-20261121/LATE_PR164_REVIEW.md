# Late source review: PR164 direct reverse-tripling packet

**Frozen head:** `5a7c86c94a9e2a7a064c0c84faa697d00d1c4d1b`.
**Compared with:** `6fa6b429870a9cd53cde0fc77ad64a3c3956199f`.

**Conclusion:** the added `research/witness-global-closure-20261121`
packet contains valid-looking new explicit witness families and guarded
reductions, with all four supplied replays passing independently under
`python3 -OO -B`. It explicitly leaves the global theorem open. It does
not close this packet's same-minimum bridge or supersede the arbitrary-tail
\(c=3\) descent.

This was a focused late-source audit of the new proof sections and their
executed checkers, not a second full independent implementation of their
finite cover. The earlier PR164 source pin remains valid for the earlier
P/Q statements already used in this packet.

## New mathematical content

The new target is

\[
R(m):\quad27m\in C\Longrightarrow9m\in C,
\qquad m>0\text{ odd}.
\]

The equivalence of all \(R(m)\) with Collatz is credited to PR146's
71-cell directed cover. The new packet reconstructs that cover and obtains
the exact query cost \(H=213597/23\), hence an all-integer floor with
\(G=355995/23\), **relative to the least failed direct-R antecedent**
\(N_*\).

`DIRECT_R_WORDS.md` gives complete first-letter normal forms and two
arbitrary-tail rewrites:

\[
(2^k,4,b,\ldots)\mapsto(1,2^k,1,b+2,\ldots),
\]

\[
(2^k,3,1^\ell,2,b,\ldots)
\mapsto(1,2^k,1^{\ell+2},b+2,\ldots).
\]

Here superscripts denote repeated letters. Each rewrite preserves total
exponent and adds one odd step. Their affine commutations and the stated
nonempty-tail checks support the claimed arbitrary-witness scope.

`R_BYPASS.md` adds a partial finite atlas: 27 certified infinite cells,
29 retained smaller child calls, and 341 explicitly unresolved cells.
It also gives the unbounded conditional family

\[
p=\frac{3^{k-3}(27m-1)}{2^{2k+1}}\in\mathbb Z_{>0},
\quad p\equiv3\pmod8,\quad k\ge3
\quad\Longrightarrow\quad[R(p)\Rightarrow R(m)].
\]

Here \(p<m\); the supplied child witness loses exactly \(k\) odd
steps and \(2k+1\) total exponent. The proof orders its child calls and
does not assume certificates for large intermediate vertices.

The least-R analysis excludes some initial valuations and rank-one/rank-two
families. It still leaves, for example, source words
\((5,88+162j)\), whose direct-R targets are equivalent to
\(2^{89+162j}-1\). No proof for that whole residual family appears.

## Why the new minimum and our minimum cannot be interchanged

For a \(c=3\) source in the current packet, write the binary index as
\(k=2m\). Then

\[
X=256m+1\sim N=27m,
\qquad Y=128m+1\sim54m+1=2N+1.
\]

Its original comparison is \(P(m)\), whereas the new direct-R conclusion
is \(9m=N/3\). Even if \(N/3\) has a witness, this does not give a
witness for \(2N+1\). It would require a further valid implication;
reversing \(Q(m)\) is not justified merely by its forward statement.
Thus the \(N\) attached to a least binary failure need not itself be a
direct-R failure, let alone the least one.

Accordingly, the new constants \(H,G\), and restrictions proved for
\(N_*\), cannot be substituted for the original \(176106\) floor at
the same fixed \(X_*\) without a separately accounted reduction. The
new source explicitly observes this distinction.

There is no duplicated arbitrary-tail \(c=3\) guard in this head. At
the corresponding direct source \(N\), the first exponent is 1 and its
successor is our \(z\). The two new direct word-rewrite languages start
with 2, 3, or 4, and the unbounded bypass also has first exponent 2.
More fundamentally, their output is \(N/3\), while our new guard
\(e\ge3a+80\) certifies the component of \(2N+1\), using the original
binary minimum and allowing an arbitrary remaining tail. Individual
finite cells can overlap inputs; no global supersession follows.

## Positive renewal qualification

`POSITIVE_RENEWAL.md` proves the lower bound

\[
K_s\ge(\beta/\delta)c^{s-1}\quad(0<s<1),
\qquad K_1\ge\beta/\delta,
\]

for positive rows retaining unit mass on a set of density \(\beta\),
with children below \(ck\), inside a domain of density \(\delta\).
Its positive cutoff-sum proof is sound. It does not exclude our partial
renewals or every witness-dependent method: genuinely killed rows and
their density are explicitly retained as an unresolved input. It also
correctly says that the sparse least-failure sieve does not count all
genuine failures.

## Executed late-source checks

The new directory was materialized from the frozen Git objects into an
isolated scratch directory. All four commands passed with `-OO -B`:

| Replay | Salient result |
|---|---|
| `check_reverse_cover.py` | 71 rows; all 20,736 unit residues; 284 tripling queries; exact \(213597/23\) ratio. |
| `check_direct_r_words.py` | Normal forms, six affine identities, padded reconstructions, and guarded language transformations pass. |
| `check_least_r_failure.py` | Complete finite endpoint witnesses, modular progressions, and exact height margins pass. |
| `check_r_bypass.py` | 523 affine forms; 27 certified cells; 341 unresolved cells; 29 calls; missing children remain `UNRESOLVED`. |

No old unchanged source was re-reviewed wholesale, no root files were
edited, and no all-input witness construction was inferred from these
finite replays.
