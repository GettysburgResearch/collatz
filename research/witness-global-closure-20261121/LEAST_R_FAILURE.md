# Least reverse-tripling failures: height and low-rank exclusions

**PROPOSED, with complete algebraic proofs for the stated exclusions. The
universal implication remains OPEN.** These statements concern the least
failure over the entire reverse-tripling problem. They are not unconditional
convergence assertions for all members of the displayed infinite families.

Let `E` have the witness definition in [DIRECT_R_WORDS.md](DIRECT_R_WORDS.md),
and let `C` include positive even integers as well, by removing powers of two.
The independently reconstructed reduction [RGA-002](REDUCTION_AUDIT.md)
shows that full convergence is equivalent to

\[
R(m):\quad 27m\in E\Longrightarrow9m\in E
\qquad(m>0\text{ odd}).
\]

If this assertion is false, let \(N_*\) be the least positive odd multiple
of 27 such that \(N_*\in E\) and \(N_*/3\notin E\). All references to
minimality below concern this same minimum. A first-hit witness ends at its
first visit to 1; its odd rank is the number of odd steps before that visit.

## LRF-001: the precise height floor

The 71 directed descent paths of PR146 use ordinary edges in either direction
and arrows \(v\longrightarrow3v\) with \(v\) an odd multiple of nine. On
every positive odd ternary-unit source \(n>1\), the selected path ends at a smaller
ternary unit, at most \(24n/25\). The independent replay in this packet checks
the maximum of the actual reverse-tripling antecedent ratios:

\[
H=\sup\frac{3v}{n}=\frac{213597}{23}.
\tag{1}
\]

The supremum is attained at \(n=23\), \(v=71199\), in the cell
\(n=432t+23\). Every ratio is bounded on the whole cell by checking its
affine limit and its first permitted parameter. Thus (1) is a universal
height bound, not a maximum over sampled trajectories. Its source and
independent replay are specified in RGA-003 of
[REDUCTION_AUDIT.md](REDUCTION_AUDIT.md).

It follows that

\[
\boxed{3\nmid n,\quad Hn<N_*\quad\Longrightarrow\quad n\in C.}
\tag{2}
\]

Indeed, use strong induction on such ternary units. Even units halve. For an
odd unit the directed certificate ends at a smaller unit, already in `C`.
Each extra arrow has antecedent \(3v\le Hn<N_*\), so the corresponding
reverse-tripling implication holds by minimality. Propagating membership
backwards along the certificate proves (2). No upper bound on the stopping
time of the smaller unit is assumed.

For a general positive integer, strip its powers of two to obtain an odd
\(q\). If \(3\mid q\), then \(q\ge3\) and its shortcut successor is the
ternary unit \((3q+1)/2\le5q/3\). Hence, with

\[
G=\frac53H=\frac{355995}{23},
\]

we also have

\[
\boxed{Gn<N_*\quad\Longrightarrow\quad n\in C.}
\tag{3}
\]

These constants refer to the least **direct reverse-tripling** antecedent.
They do not replace the constants for the differently defined least binary
comparison in PR163, `LEAST_FAILURE_HEIGHT.md`.

## LRF-002: finitely many possible first letters

Write the first odd step of a supplied witness as

\[
N_*=\frac{2^a t-1}{3},\qquad t\in E,\quad t\text{ odd},
\quad2^at\equiv1\pmod{81}.
\]

The exact normal forms DRW-001 give

\[
N_*/3\in E\iff
\begin{cases}
3^{d-2}t\in E,&a=2d\ge4,\\
2\cdot3^{d-1}t+1\in E,&a=2d+1\ge3.
\end{cases}
\tag{4}
\]

For even \(a=2d\), let \(q=3^{d-2}t\). Multiplication by 69 gives

\[
69(N_*-Gq)
=\bigl(23\,4^d-355995\,3^{d-1}\bigr)t-23.
\]

At \(d=30\) the right side at \(t=1\) is exactly

\[
2085123415945956840>0.
\]

The inequality persists for every \(t\ge1\) and \(d\ge30\). For example,
if \(A4^d-B3^d-D>0\), then its value at the next index is
\(3(A4^d-B3^d-D)+A4^d+2D>0\). Equation (3) would then certify `q`,
contradicting (4). Thus every even \(a\ge60\) is excluded.

For odd \(a=2d+1\), \(d\ge2\), the endpoint
\(q=2\cdot3^{d-1}t+1\) is itself a ternary unit, so use (2) directly:

\[
69(N_*-Hq)
=\bigl(46\,4^d-427194\,3^d\bigr)t-640814.
\]

At \(d=32,t=1\), this is

\[
56951120834265369368>0.
\]

The same elementary comparison excludes every odd \(a\ge65\). Also
\(a=4\) is unconditionally solved by DRW-003, whose exact rewrite is
\((4,b,\ldots)\mapsto(1,1,b+2,\ldots)\). Consequently a least failure
must have

\[
\boxed{a\in\{1,2\}\cup\{3,5,\ldots,63\}
                 \cup\{6,8,\ldots,58\}.}
\tag{5}
\]

This is a restriction on one letter of an arbitrarily long witness; it is
not a finite list of candidate integers.

## LRF-003: no rank-one source can be the least failure

For a first-hit source word of length one, \(t=1\). The order of 2 modulo
81 is 54, so

\[
N_*=\frac{2^{54j}-1}{3},\qquad j\ge1.
\]

Its target is equivalent to \(3^{27j-2}\), by DRW-005. If \(j\ge2\),
its first letter is at least 108, excluded by (5). At \(j=1\), the target
is equivalent to \(3^{25}=847288609443\). The full certificate in
[low_rank_witnesses.json](low_rank_witnesses.json) has 137 odd steps and
total exponent 257. The companion checker verifies its complete defining
integer identity and every exact intermediate valuation. Thus this remaining
case also cannot fail.

It follows that the least direct reverse-tripling failure, if one exists,
has first-hit source odd rank at least two. This statement does not assert
that all the rank-one implications have been proved independently of the
global-minimum hypothesis.

## LRF-004: rank two cannot start with 1, 2, 3, or 4

Suppose the first-hit source word is \((a,b)\). Then \(b\ge4\) is even:
the intermediate odd value \(t=(2^b-1)/3\) must be integral and greater
than 1. The source is

\[
N=\frac{2^{a+b}-2^a-3}{9}.
\tag{6}
\]

Its divisibility by 27 is exactly

\[
2^{a+b}\equiv2^a+3\pmod{243}.
\tag{7}
\]

The order of 2 modulo 243 is 162, and its powers exhaust the units. Solving
the finite congruence (7) therefore gives the following *complete*
progressions for the three specified first letters:

| First letter | Last letter | Ordinary target prefix from \(N/3\) | Endpoint after that prefix | Equivalent pure power |
|---|---|---|---|---|
| \(a=1\) | \(b=22+162j\) | \((2,2,1)\) | \(2^{b-4}+1\) | \(3^{(b-6)/2}\) |
| \(a=2\) | \(b=68+162j\) | \((1,2,1)\) | \(2^{b-2}+1\) | \(3^{(b-4)/2}\) |
| \(a=3\) | \(b=118+162j\) | \((1,1,1)\) | \(2^b+1\) | \(3^{(b-2)/2}\) |

Here \(j\ge0\). All displayed prefix divisions are exact; substitution in
(6) proves the stated positive odd endpoints. Finally
\(4^k+1\in E\iff3^{k-1}\in E\) gives the last column.

Let `q` denote that pure power. The exact inequalities \(Gq<N\) already
hold at \((a,b)=(2,68)\) and \((3,118)\). After multiplication by 207,
their positive margins are respectively

\[
21216613977327659747436,
\]

\[
61129396765715944561205053526148460248.
\]

For \(a=1\), the inequality holds at \(b=184\), with positive margin

\[
1127916708755960028487587856817003422024439345672964291156.
\]

Each comparison has the form
\(A2^b-B3^{b/2}-D>0\), with positive constants. Raising `b` by 162
multiplies its positive exponential by \(4^{81}\), its subtracted
exponential by \(3^{81}\), and leaves `D` fixed. Positivity at one index
therefore proves it at every later index. Under the global least-failure
hypothesis, (3) certifies these endpoints and excludes the corresponding
sources.

The only remaining case in these three progressions is \((a,b)=(1,22)\).
Its endpoint is \(3^8=6561\), whose complete certificate in
`low_rank_witnesses.json` has 24 odd steps and total exponent 51. It is
verified exactly by the same checker. The case \(a=4\) was already solved
for arbitrary input rank by DRW-003.

Thus a rank-two least failure, if one exists, has its first letter in

\[
\boxed{\{5,7,\ldots,63\}\cup\{6,8,\ldots,58\}.}
\tag{8}
\]

The remaining progressions are unbounded and are not certified by this
argument. For example \(a=5\) gives \(b=88+162j\) and a target equivalent
to the Mersenne value \(2^{89+162j}-1\). No convergence claim for that whole
family follows from the present inequalities.

## Replay and precise evidence

Run `python -B research/witness-global-closure-20261121/check_least_r_failure.py`
and the same command with `-O`. The checker validates both complete finite
witnesses, the modular orders and residue solutions, every affine step in
the three rank-two formulas, the exact height margins, the monotonicity
identity, and rejection of damaged finite witnesses.

The source height bound is separately reconstructed by
`check_reverse_cover.py`; the all-input normal forms are proved and checked
in `DIRECT_R_WORDS.md`. These dependencies are explicit. The computations do
not establish convergence of the remaining endpoints, universal reverse
tripling, or the full theorem.
