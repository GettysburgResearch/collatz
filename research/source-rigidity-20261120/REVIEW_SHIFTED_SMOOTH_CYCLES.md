# Independent review of shifted two-prime cycles and confinement

**Verdict: VERIFIED for SS1–SS3; VERIFIED with the stated external
dependency for SS4.** No mathematical correction is requested at the
frozen proof hash below. These verdicts concern this packet and the
specified dependency interface, not unrestricted Collatz convergence.

Reviewer: the independent merger agent. Review date: 2026-11-20.
The reviewer did not edit the author's proof, checker, or reports.

## Frozen artifacts

These are pre-publication content pins. They do not purport to identify
a later GitHub revision.

| File | Bytes | SHA-256 |
|---|---:|---|
| `SHIFTED_SMOOTH_CYCLES.md` | 8441 | `e3db28e9e944a36dacd54f661cda8a1856664bfac3d248caefdf23b1a9875c60` |
| `check_shifted_smooth_cycles.py` | 4668 | `63ec9728012f7bd2071a1d190b04233f03d5daba075ee0b01b34ffec47f354d6` |
| `shifted-smooth-cycles-report.json` | 2311 | `40deffb6517ce927fa3f55a8a8ec7997f62b5a592a735ac3ecdcaebd26a80ea2` |

The author's optimized report has the same bytes and hash as the normal
report. The source directory reviewed was
`/workspace/scratch/46eba7b29f50/agent-analytic-remains/`.

The two dependency files were also read and their hashes checked:

| Dependency | Claims used | SHA-256 |
|---|---|---|
| `SHIFTED_CORE_TRANSITIONS.md` | SC1–SC3 and the conservative clock | `f53846e08e1522058797c6cab57111cf9c7ed4385f39b0e055ab05264f7acb71` |
| `BOUNDED_CORE_HORIZON.md` | SC4, integer horizon and endpoint convention | `48b87b072ebd2a8e31f6767efd300d42df3599c10efdd9c82543eae2d266dec8` |

## Normalization and the actual boundary map

The state is one positive odd ordinary integer, with the accelerated
map `U(n)=(3n+1)/2^v2(3n+1)`. The class is

\[
\mathcal S=\{2^s3^t-1:s\ge1,\ t\ge0\}.
\]

Unique factorization makes the pair `(s,t)` and its sum `k=s+t`
unambiguous. If `s>=2`, direct substitution gives

\[
3n+1=2\bigl(2^{s-1}3^{t+1}-1\bigr).
\]

The parenthesized term is odd. Hence the division exponent is exactly
one, the new coordinates are `(s-1,t+1)`, and `k` is preserved.
After precisely `s-1` such transitions the state is
`N_k=2*3^(k-1)-1`. Its next exponent is at least two, so this is the
end of the run, including when the initial run has length zero.

At this boundary,

\[
3N_k+1=2(3^k-1),\qquad
b=v_2(3^k-1),\qquad a(N_k)=b+1.
\]

Consequently the author's successor formula and its shifted
factorization use the correct denominator `2^b`. There is no confusion
between that denominator and the full Collatz division exponent `b+1`.

## SS1: universal increase is proved, not inferred from a search

I reconstructed the complete argument for every `k>=16`.

For odd `k`, `3^k-1` is 2 modulo 4, giving `b=1`. For even
`k=2^v u`, with `u` odd, the factor remaining after
`3^(2^v)-1` is removed is odd. The base valuation at `v=1` is
`v2(3^2-1)=3`; each further squaring contributes a factor
`3^(2^v)+1` with valuation one. Thus `b=2+v2(k)`.

Let `w=floor(log2 k)`. For `k>=16`,

\[
b\le w+2<k.
\]

Also `0<2^b-1<3^b`, so its ternary valuation is strictly below
`b`. Since the two summands in `3^k+(2^b-1)` have different
ternary valuations, the valuation of their sum is exactly the smaller
one. If the successor is in the class, its exponents therefore satisfy

\[
t'=v_3(2^b-1)\le b-1.
\]

Assume for contradiction that the next compressed index `k'=s'+t'`
is at most `k`. The exact shifted equality then gives

\[
3^k<2^{b+s'}3^{t'}
=2^{b+k'}(3/2)^{t'}
\le 2^{k+1}3^{b-1}.
\]

The reverse strict inequality holds uniformly. At the start of the
first dyadic block it is certified by
`3^11=177147>131072=2^17`. If

\[
(3/2)^{2^w}>2\,3^{w+1},
\]

squaring yields the statement at `w+1`, because the squared lower
bound exceeds `2*3^(w+2)` by the factor `2*3^w>1`.
Within a dyadic block the left side increases with `k`, while
`b-1<=w+1`. This proves the required opposite inequality for all
`k>=16` and establishes the contradiction.

The successor-core condition is essential: the argument uses the full
equation with no factor outside 2 and 3. At `k=16`, the actual successor
shift has coordinates `(s',t',q')=(1,2,37367)`, so its coordinate sum
is 3. That is a counterexample to the proposed increase if `q'=1`
is omitted, and is correctly retained as a negative control.

## SS2: a complete cycle argument

I reconstructed all fifteen rows from the literal ordinary odd map,
not by importing the author's functions. The table agrees exactly.
The only class-preserving boundary edges among these indices are

\[
1\to1,\qquad2\to1,\qquad4\to2.
\]

A finite cycle contained in `S` has a nonempty finite cyclic list of
boundary states: every intervening valuation-one run terminates after
its finite coordinate `s-1` is consumed. If the largest boundary index
were at least 16, SS1 would force its next index to be strictly larger.
Thus every boundary index lies in the complete small table. Its only
cycle is the fixed index 1, whose actual boundary value is 1.

There is no possibility of hiding a cycle in an indefinitely long
valuation-one run. Such a run would require a fixed positive integer
shift to be divisible by arbitrarily high powers of two. The physical
coordinate calculation already excludes this.

The conclusion is exactly the odd-map cycle `{1}`, or the shortcut-map
cycle `{1,2}`. It excludes all cycles whose shifted odd values stay in
this particular prime class, with no bound on their maximum value or
length. It does not exclude a cycle containing an odd state outside
the class.

## SS3: the exact finite within-class basin

A finite class-preserving path to 1 cannot include a boundary index
at least 16. Once such an index occurred, SS1 would make every
subsequent admissible boundary index strictly larger, so the index 1
could not be reached. The small table then forces all boundary
indices on a terminating path to be in `{1,2,4}`.

The initial state's index is the index of its first boundary.
Enumerating the exponent pairs at indices 1, 2, and 4 gives

\[
\{1\},\qquad\{3,5\},\qquad\{15,23,35,53\}.
\]

All seven really terminate within the class. The longest displayed
path is checked directly:

\[
15\to23\to35\to53\to5\to1.
\]

This is an exact characterization of **finite** paths to 1 that stay
within the class. The elementary argument alone does not rule out an
infinite path whose boundary indices increase forever. The author
explicitly preserves that distinction before invoking SC3 in SS4.

## SS4: dependency and unchanged deadline

I read SC1–SC4 at the two frozen hashes and checked the exact interface
needed here. I also opened Evertse's primary author-hosted paper,
*The number of solutions of decomposable form equations*, and checked
Theorem 3 on printed page 7:

<https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf>

Its coefficient-uniform bound for nondegenerate solutions in `d`
variables is `(2^35*d^2)^(d^3*t)`, with `t` counting all places,
including infinity. The specialization `d=3`, `P={2,3}` therefore
has `t=3` and bound `B_2=(9*2^35)^81`. This review uses that published
theorem as an external result; it does not independently reprove it.

For a defect transition of a fixed ordered core pair, the source
reduction has three nonzero signed summands in the normalized S-unit
equation. Its two potentially troublesome pairwise sums are
`2^(a-1)(1-m')<0` and `1-2^(a-1)<0`, since `m'>=2` and `a>=2`.
The third pairwise sum is positive. The encoding determines the
ordinary source and transition uniquely. Thus the bound counts
distinct actual defect transitions; it is not merely a bound on
formal factorizations. The exponent-one case is degenerate and is
correctly excluded from this count.

If a tail is confined to `S` and never repeats a state, its core is
always 1, so it can contain only finitely many defects by SC1–SC2.
Its remaining tail would have only exponent-one steps, contradicting
the finite run calculation. Hence SC3 makes that actual tail
eventually periodic. SS2 then identifies the eventual cycle as 1.
No assumption that a shifted-smooth initial value stays smooth has
been inserted.

For the quantitative statement set `K=1`, `Q={1}`, and
`ell=ceil(log2(n0+1))`. The SC4 clock is

\[
H=\ell(2^{B_2+1}-1).
\]

The endpoint convention is sound. If there were neither a repeated
state nor an exit among `n0,...,nH`, the `H+1` ordinary states would
be distinct, and the first `H` transitions would contain at most
`B_2` defects. The source clock gives the strict inequality

\[
H<\ell(2^{D+1}-1)\le\ell(2^{B_2+1}-1)=H,
\]

a contradiction. That conservative clock follows from
`R_(j+1)<=2R_j+ell` and the fact that the next defect has not yet
completed at the tested prefix endpoint.

If instead a state repeats at `i<j<=H`, its actual deterministic
cycle is already the segment `ni,...,n_(j-1)` inside the tested
prefix. With no exit, this cycle is contained in `S`. SS2 makes it
the fixed point 1, so a visit to 1 has already occurred by time `H`.
Adding another hypothetical cycle length would be unnecessary.

The full SC3 proof is not needed separately for this finite-horizon
version: SC1–SC2, the elementary clock, and SS2 suffice. The author's
dependency presentation allows this. The optional PR145
compressed-word strengthening does not enter either deduction.

## Executed controls and their limits

The author's checker was run in normal and `-OO` modes. Both outputs
were byte-identical to the frozen normal and optimized reports.

A separate reviewer script, which does not import that checker,
reconstructed the literal boundary table, parsed the written rows,
and examined the finite complement determined by `1<=s+t<=15`.
Among its 120 states, exactly the seven listed starts reach 1 while
staying in the class; the other 113 leave. Its only cycle is `{1}`.
It also replayed 109 compressed runs, totaling 1221 actual odd
transitions; checked 23 selected valuation instances and nine
dyadic induction endpoints; and verified the two negative controls.
These are finite arithmetic controls for the written proof, not an
exhaustive classification of all large admissible boundary indices.

The reviewer script and its normal/optimized reports were executed
in `/workspace/scratch/46eba7b29f50/agent-merger-remains/`:

| Review artifact | SHA-256 |
|---|---|
| `review_shifted_smooth_replay.py` | `40e80d5199063b62609b81387e75184a447f91fc247b844d813401a906aec227` |
| `review-shifted-smooth-replay.json` | `ce4313a3b12120da0a0115a6245d31cebb9842f7142d8498e099793195792e1a` |

The optimized reviewer report is identical. The reviewer script defaults
to co-located source files and accepts `--source-root` for another source
directory. It invokes both author replays with `-X utf8 -B`. The actual
staging commands used `--source-root ../agent-analytic-remains` in normal
and `-OO` modes. Thus the independent controls can also be rerun after
the packet files are placed together in a repository checkout.
Neither script computes the astronomical horizon or independently
verifies the external S-unit theorem. The universal dyadic induction,
cycle argument, dependency normalization, and same-horizon deduction
were checked mathematically above.

## Publication boundary

The packet supports a complete restricted-class cycle theorem and an
exact restricted basin. With the named S-unit dependency it also
supports eventual-confinement convergence and a finite hit-or-exit
deadline. An exit can increase the ordinary integer and supplies no
convergence certificate. None of these statements shows that an
arbitrary ordinary orbit enters, remains in, or returns suitably to
the shifted two-prime class. That missing all-source control remains
outside the verified claims.
