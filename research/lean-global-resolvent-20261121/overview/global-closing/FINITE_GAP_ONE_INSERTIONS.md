# Every finite gap-one insertion repair has a source-dependent last-edit bound

## Result and scope

Fix a positive odd ordinary integer `n`. Follow its actual accelerated odd
Collatz trajectory. Keep every gap of a finite prefix, in its original order,
and insert `t >= 1` additional gaps equal to one. Require the modified word to
start at another positive ordinary integer and to finish at the **same ordinary
endpoint** as the original prefix.

Every successful repair of this kind starts at a smaller positive odd integer
`m`. If `N = bitlength(n)`, its last insertion occurs at original shortcut clock

\[
A\le (N-2)(2^t-1),\qquad 3^t<2^t n,\qquad 2^t<n^2.
\]

The two trajectories first merge in this alignment at the last insertion.
Consequently the modified trajectory merges by shortcut clock

\[
\boxed{A+t<N(n^2+2).}
\]

This is a bound for the **entire insertion-only, same-endpoint repair class**
at a fixed ordinary source. Moving the endpoint arbitrarily far along the
original trajectory does not create an unbounded last-edit search: after the
last insertion, both trajectories already agree.

This does not rule out all finite repairs. It does not apply to replacing or
deleting original gaps, changing the endpoint, general rational endpoints,
or infinite modified words that never attain a common ordinary endpoint.
It does not prove that an escaping ordinary source has a successful repair.

## 1. Conventions and the exact source formula

For a positive odd integer `q`, put

\[
U(q)=\frac{3q+1}{2^{a(q)}},\qquad a(q)=v_2(3q+1)\ge1.
\]

Write the actual orbit and its prefix data as

\[
q_0=n,\quad q_{i+1}=U(q_i),\quad a_i=a(q_i),\quad
A_i=\sum_{h<i}a_h,\quad
2^{A_i}q_i=3^i n+C_i.
\]

Here `C_0=0` and `C_(i+1)=3 C_i+2^(A_i)`. A gap `a` has inverse affine map
`g_a(v)=(2^a v-1)/3`. The shortcut map used for the clock is
`T(v)=v/2` on even integers and `T(v)=(3v+1)/2` on odd integers. Thus an odd gap
`a` takes `a` shortcut steps.

Choose insertion cuts

\[
0\le i_1\le\cdots\le i_t\le j.
\]

A cut `i` means just before original gap `a_i`, or at the endpoint when `i=j`.
Repeated cuts are allowed. Pull the enlarged gap word backward from the
unchanged endpoint `q_j` and call the resulting rational number `m`.

Define

\[
\delta_i=\frac{2^{A_i}(q_i+1)}{3^{i+1}}
=\frac13\left(n+\frac{C_i+2^{A_i}}{3^i}\right)>\frac n3.
\]

The exact source is

\[
\boxed{
m=n-\sum_{\ell=1}^t
\left(\frac23\right)^{\ell-1}\delta_{i_\ell}
=n-\sum_{\ell=1}^t
\frac{2^{A_{i_\ell}+\ell-1}(q_{i_\ell}+1)}{3^{i_\ell+\ell}}.
}
\tag{1}
\]

To prove this, insert the extra gaps from left to right. At cut `i_ell`, the
unmodified suffix pulls the common endpoint back to `q_(i_ell)`. Inserting
`g_1` changes this value by `-(q_(i_ell)+1)/3`. The preceding inverse prefix
has slope `2^(A_(i_ell)+ell-1)/3^(i_ell+ell-1)`. Multiplying gives exactly the
`ell`-th summand in (1).

The cut costs are nondecreasing:

\[
\delta_{i+1}-\delta_i
=\frac{2^{A_i}(2^{a_i}-2)}{3^{i+2}}\ge0,
\tag{2}
\]

with equality precisely at original gaps equal to one. Delaying an insertion
therefore cannot improve its real-valued source cost; it can still change the
ternary integrality condition.

### Integrality really implies literal realization

Every suffix inverse value is a rational number with odd numerator and a
denominator that is a power of three. If the initial `m` is an integer, it is
odd. The prescribed forward equation is
`3 z+1=2^a z_next`. The right-hand suffix value has odd denominator, whereas
the left-hand side divided by `2^a` has denominator a power of two. Hence
`z_next` is an integer, and its suffix representation makes it odd. Induction
shows that every prescribed gap is the exact valuation, rather than just a
nonexact division by a power of two. If `m>0`, all forward values are positive.
Thus a positive integral inverse source produces a literal ordinary orbit.

## 2. Number of inserted gaps

Equation (1) and `delta_i > n/3` give

\[
m<n-\frac n3\sum_{\ell=0}^{t-1}(2/3)^\ell
=\left(\frac23\right)^t n.
\tag{3}
\]

If `m` is a positive integer, then

\[
3^t<2^t n.
\tag{4}
\]

In particular `m<n`; a successful repair is automatically a smaller ancestor
of the common endpoint. Squaring (4) and using `8^t<9^t` for `t>=1` yields

\[
2^t<n^2.
\tag{5}
\]

Since `n<2^N`, (5) also gives `t<2N`. These are uniform in all insertion cuts
and in the terminal prefix length `j`.

## 3. The aligned difference cannot change sign

Track the original state `q` and modified state `z` after the same number of
**original** gaps have been consumed. An insertion advances only `z`.
Set `D=q-z`.

Initially `D=n-m>0` is an even integer. A common gap `a` changes the difference
by

\[
D\longmapsto\frac{3D}{2^a}.
\tag{6}
\]

An inserted gap one changes it by

\[
D\longmapsto\frac{3D-q-1}{2}
=D-\frac{z+1}{2}<D.
\tag{7}
\]

All aligned states are positive odd integers. Once `D<0`, common gaps preserve
its sign and insertions decrease it further, so it could never become zero.
If `D=0` before any remaining insertion, that next insertion makes it negative.
Since the final endpoints agree, `D` is therefore strictly positive until the
last insertion, becomes zero at that insertion, and stays zero through the
remaining common suffix.

This sign argument is where the unchanged endpoint and retention of every
original gap are essential.

## 4. Each interval between insertions has a finite clock budget

Consider a block of `d` common original gaps with total valuation `B`, before
the next insertion. Its starting difference `D_start` is a positive even
integer, and its ending difference is also a positive even integer. By (6),

\[
D_{\rm end}=\frac{3^dD_{\rm start}}{2^B},\qquad
2^{B+1}\mid D_{\rm start},\qquad
2^{B+1}\le D_{\rm start}.
\tag{8}
\]

Suppose `i` original gaps, with cumulative valuation `A_prev`, have been
consumed before this block. Common gaps increase `D` by at most `3/2` each;
insertions strictly decrease it. Consequently

\[
D_{\rm start}\le (3/2)^i(n-m)
<2^{N+i}\le2^{N+A_{\rm prev}},
\tag{9}
\]

where `i<=A_prev` because every original gap is at least one. Comparing (8)
and (9) gives the integer inequality

\[
B\le A_{\rm prev}+N-2.
\tag{10}
\]

Let `A_ell=A_(i_ell)` and `A_0=0`. This gives

\[
A_\ell\le2A_{\ell-1}+N-2,
\qquad
\boxed{A_\ell\le(N-2)(2^\ell-1).}
\tag{11}
\]

A successful repair requires `n>=3`, so `N>=2`. This includes zero-length
common blocks and repeated insertion cuts. Combining (11) for `ell=t` with
(5) and `t<2N` proves

\[
A_t+t<Nn^2+2N=N(n^2+2).
\]

### A sharper real-valued version

The same proof, keeping `(3/2)^i` in (9), gives

\[
A_t\le\beta\frac{\alpha^t-1}{\alpha-1},\qquad
\alpha=\log_2 3,\quad
\beta=\log_2\frac{n-m}{2}.
\tag{12}
\]

Here `n-m>=2`, so `beta>=0`. Indeed (8) implies
`B <= beta + (alpha-1)i <= beta+(alpha-1)A_prev`, and induction gives (12).
One can replace `beta` by `log_2((n-1)/2)` for a bound depending only on `n`.
The all-integer bound (11) is enough to make the complete finite-search claim.

## 5. One insertion and a nonempty family

For one insertion at cut `i`, integrality is equivalent to

\[
3^{i+1}\mid q_i+1.
\tag{13}
\]

Since `q_i+1 <= (3/2)^i(n+1)`, (13) forces

\[
3\cdot2^i\le n+1.
\tag{14}
\]

This elementary single-insertion restriction does not extend by imposing
(13) separately on every inserted gap: cancellations between the rational
summands in (1) can occur. The multi-insertion argument above does not make
that mistake. For example, `45` has original gap word `[3]` to endpoint `17`.
Insert ones at cuts `[0,1]`: the enlarged word `[1,3,1]` is the literal orbit
`19 -> 29 -> 11 -> 17`. Inserting only the first of these ones gives the
nonintegral source `89/3`; the second insertion repairs its denominator.

Successful repairs certainly exist. For every positive integer `u` and `t>=1`,
take `n=2u*3^t-1` and insert all `t` gaps at cut zero. The inverse source is
`m=2u*2^t-1`, and it reaches `n` in exactly `t` successive gap-one steps.
The theorem bounds their count and locations; it does not outlaw them.

## 6. What this resolves, and the exact remaining step

For fixed `n`, all successful repairs in this class can be found by a finite
search: compute the original orbit only to shortcut clock `N(n^2+2)`, take
`1<=t<2N`, enumerate nondecreasing cuts whose cumulative original clock obeys
(11), and test (1) for positive integrality. Any longer common suffix is
irrelevant because the trajectories already merged at the last insertion.
The bound is not claimed to give a practical algorithm for large `n`.

In particular, an infinite construction that inserts more and more gap-one
steps into a symbolic ray cannot be legalized at one fixed positive ordinary
source simply by asking its finite same-endpoint approximations eventually
to stabilize: (4) already bounds their number of insertions, and (11) bounds
their last possible location. This statement concerns precisely those finite
approximations; it makes no assertion about all infinite source codes.

The attempted convergence route is to apply such a surgery to an assumed
escaping ordinary source. At a least positive counterexample, one successful
repair would give a smaller positive source merging into the escaping orbit,
a contradiction. The first unsupported statement is:

> A least escaping ordinary source admits a positive integral same-endpoint
> repair made only by inserting gap-one steps while preserving every original
> gap.

Neither finite-block genericity, favorable real-valued pressure, nor the
ability to insert sublinearly many ones into a symbolic ray proves that
ternary divisibility statement. The result here identifies a complete finite
search domain for this exact proposed surgery; it does not supply the missing
existence theorem. A universal repair assertion for every `n>1` would even be
false: `n=3` has `N=2`, so (11) forces all cuts to zero, while integrality then
requires `3^t | 4`, impossible for `t>=1`. There is also a direct check: the
only smaller positive odd source is `1`, whose first exact gap is `2`.
The original source `3` starts with gap `1`, and prepending any inserted gap
also starts the enlarged word with `1`. Thus no enlarged word in this class
can be the actual gap word of `1`.

## 7. Validation and provenance

`check_finite_gap_one_insertions.py` independently compares inverse-word
evaluation with (1), replays every positive integer candidate as an actual
odd Collatz trajectory, checks the aligned differences and block divisibility,
and checks (3)--(5), (11), and the merger clock bound. It includes repeated
cuts and candidates whose intermediate partial insertion source is not an
integer. This is a finite arithmetic diagnostic, not a substitute for the
proof above and not a proof of Collatz.

The recorded run checks 46,101 rational candidates over odd `n=3..255`, final
cuts `0..10`, and insertion counts `1..3`, including all nondecreasing cut
multisets with the chosen final cut. All 155 positive integral candidates
pass literal replay and every asserted bound. Seven of those have a
nonintegral partial insertion source, including the `45 -> 19` example above.
Forty additional all-parameter-family instances with up to eight insertions
also pass. Exact output is in `CHECK_RESULT.json`.

Every checker condition uses an explicit `require` function that raises on
failure, so Python optimization cannot remove the checks. The checker writes
only to stdout. Normal and `python -O` executions are required to produce
identical output, including the number of conditions executed.
`EXECUTION_METADATA.json` records the two exit codes, output hashes, Python
version, and SHA-256 hashes of the checker, proof note, source ledger, and
recorded result.

This argument was developed in checkpoint 18 in response to the proposed
infinite gap-one insertion route. It uses elementary inverse-word algebra and
the standard common-parity-prefix divisibility mechanism. No claim of
literature priority is made. `SOURCES.json` pins the repo work consulted and
distinguishes contextual results from ingredients actually used here.
