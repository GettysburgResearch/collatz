# The head-three branch: preserve the source and decrease the target

## Result and limit

The new module `Collatz.HeadThreeTarget` proves an exhaustive arithmetic
split for the remaining initial-exponent-two, first-gap-three psi target
identified by PR177. One phase always has a smaller ordinary merger
partner. The partner is admitted by checkpoint9's target induction while
the **original complete source certificate remains fixed**. This removes
the certificate-rank obstruction exhibited in PR177's head-three note.

The complementary phase has an exact positive-nine residual. The smaller
partner proves convergence of its companion, but this gives neither a
lower-ranked certificate for that companion nor an interval hypothesis
around it. A new universal closure argument for that residual was not
obtained. `MixedCover`, `LowIntervalStep`, and full Collatz remain open.

This is a theorem about unbounded valuation families, with an exhaustive
opposite-phase description, rather than a bounded residue census. The
entire supplied source-prefix family `[3,3]` is an immediate application,
with unrestricted source size and unrestricted remaining certificate.

## Source pins and what is reused

The fresh comparison reads were:

| PR | Commit | New material used in the mathematical comparison |
|---|---|---|
|177|`9af9118a7e9af870a32a72a4efdcf77e886940ec`|`PSI_HEAD_THREE_FRONTIER.md`, `LOW_GAP_GLOBAL.md`, `CLOCK_SYNCHRONIZATION.md`, `PSI_EVEN_HEAD_FOUR.md`, and the refreshed source synthesis|
|180|`cfe70e02f246119a55fb5bf8fd573f148d746beb`|The arbitrary-debt transition, successful language, and terminal-debt obstruction in `research/lean-critical-20261122/WITNESS_ATTACK.md`|
|185|`7889fc680f5ee22237732eccc172b1699ef565da`|The terminating finite complement-credit machine and its literal-one-prefix guard in `research/profound-closure-20261122/NEGATIVE_CARRY.md`|

Those new PR heads were inspected as source material; they were not
independently replayed or added as assumptions. The module imports only
the already frozen checkpoint9 `Collatz.SourceTargetInduction` closure,
published by PR176 at `c83a8459066d8223aefe7fc5f6b75faeea557345`.
The exact imported source hashes and the 19-module closure are recorded
in the combined `DEPENDENCIES.json`. The PR177 modules in that closure remain
the byte-identical files pinned at `a0a0d76f91b4e3846c1b1f0706cad56cb6098317`.

The physical half-merger diamond is reused mathematics. It is already
present in the PR184/185 merger work and the new PR177 odd-valuation psi
rules. The new integration here specializes it to the outstanding
head-three query and pays its smaller partner through the **same-source
target induction**, eliminating the need to certify a new source whose
rank may be larger. The exact failure phase and the companion-height
theorem retain the resulting global obligation instead of treating the
diamond as exhaustive success.

## 1. Keep the original query

Use the ordinary shortcut map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Suppose the actual supplied complete odd certificate begins at `q` with
gap three:

\[
3q+1=8u,\qquad u\text{ odd},\qquad
\operatorname{Certificate}(q;3\Vert\tau).
\]

The original powered source is `S=4q`, with unchanged grade
`grades 2 (3 :: τ)`. Its psi target is

\[
n=8q-1.
\]

Define

\[
v=9u-1,\qquad x=2v-1=18u-3.
\]

The source edge and four actual shortcut steps give

\[
T^4(n)=36u-5=4v-1.
\]

Moreover,

\[
n=\frac{64u-11}{3},\qquad
n-x=\frac{10u-2}{3}>0.
\]

Thus `x` is a positive target strictly below the original target `n`.
It remains inside the **same** activated interval
`0 < x ≤ 2S+1`. Under `SameSourceHyp S n`, it already has a basin
proof. No certificate for `x`, or for a later iterate of `x`, needs to be
extracted or assigned an invented grade.

These statements are checked by `head_three_prepare`. All public
arithmetic equalities use addition where needed, so truncated subtraction
is not an implicit proof premise.

## 2. Every valuation has an exact success/failure split

Since `u` is odd, `v` is positive and even. Factor it exactly as

\[
v=2^h r,\qquad h\ge1,\qquad r\text{ positive and odd}.
\]

Set

\[
b=3^{h+1}r.
\]

The ordinary odd-run formula, checked as `mersenne_ascent`, gives

\[
T^{h+2}(4v-1)=3b-1,
\qquad
T^{h+1}(2v-1)=b-1.
\]

Because `b` is odd, precisely the following two phases remain.

### Successful phase: `b = 4z+3`

The two endpoints are `12z+8` and `4z+2`. Two further shortcut steps
send both to `3z+2`. Including the original four steps from `n`,

\[
\boxed{T^{h+8}(n)=3z+2=T^{h+3}(x).}
\]

The clocks are independent and explicitly accounted for. Since `x<n`,
`head_three_success_rule` closes the original target through the existing
same-source induction hypothesis. It does not invoke a new powered source
or a new complete odd certificate.

### Failed phase: `b = 4z+1`

The two endpoints are `12z+2` and `4z`. Two further shortcut steps give

\[
\boxed{T^{h+8}(n)=9z+2,\qquad T^{h+3}(x)=z.}
\]

The parameter `z` is positive. The original inner induction proves
`Basin x`, so ordinary transport proves `Basin z`. It also gives the
exact equivalence

\[
\operatorname{Basin}(9z+2)
\quad\Longleftrightarrow\quad
\operatorname{Basin}(n).
\]

These are the conclusions of `head_three_failure_transport` and
`failure_companion_basin`. Neither theorem asserts the implication
`Basin z → Basin (9z+2)`.

The theorem `head_three_dichotomy` supplies the factorization and both
alternatives for **every** head-three input satisfying the actual source
edge and odd endpoint condition. It does not leave an unstated valuation
or parity case.

## 3. Every `[3,3]` source prefix is now paid

Suppose the supplied source also has a second gap three:

\[
3u+1=8w,\qquad w\text{ odd}.
\]

Then `u=16a+13` for a natural `a`, so

\[
v=9u-1=4(36a+29).
\]

Here `h=2`, `r=36a+29`, and

\[
3^{h+1}r=27(36a+29)=4(243a+195)+3.
\]

The entire family is in the successful phase. Its clocks specialize to

\[
\boxed{T^{10}(8q-1)=T^5(18u-3),\qquad 18u-3<8q-1.}
\]

`head_three_three_merger` proves this identity from the two actual source
edges. `head_three_three_mixed` turns it into a genuine `MixedWitness`
at the original source grade, for any complete tail. The arithmetic
theorem itself is stronger than the certificate application: it needs only
the two edges and odd endpoint, not convergence of that endpoint.

### The previously displayed rank obstruction

PR177's note used

\[
q=205,\quad u=77,\quad S=820,\quad n=1639,\quad x=1383.
\]

Its newly proposed source `692=4·173` has a larger complete source grade
than `820=4·205`. That comparison remains correct. It is simply not
required by the new application: the source stays `820`, its complete
certificate stays unchanged, and the queried target falls from `1639`
to `1383`. The uniform identity above gives the displayed meeting at
`3503`. This is not presented as a newly discovered isolated merger ray;
the new theorem pays the **entire structural family** in the combined
induction.

## 4. The failed companion is always larger once `h ≥ 3`

The source arithmetic imposes more than the shape `9z+2`. It retains

\[
27q+1=8\cdot2^h r,
\qquad
27n+35=64\cdot2^h r.
\]

These are checked by `head_three_source_identity`. In particular,
`2^h r ≡ 17 (mod 27)`; the residual is not a free positive-nine state
with an arbitrarily reassigned source.

In the failed phase,

\[
108z+27=3^{h+4}r,
\qquad
108n+140=2^{h+8}r.
\]

At `h=3`, `3^7=2187 > 2048=2^11`; the ratio grows by `3/2` with
each increment of `h`. Hence, for every `h≥3` and every positive `r`,

\[
\boxed{z>n.}
\]

This is the fully checked theorem `failure_large_companion`. The forward
orbit of the smaller, already certified partner `x` is allowed to rise
above `n`. Its basin membership remains proved, but the inequality needed
for a fresh smaller-target induction at `z` does not hold. For `h=1,2`,
the two displayed identities instead give `z<n`; that algebraic
observation alone still does not prove the convergence of `9z+2`.

The claim here is conditional on the actual head-three equations. It
does not assert a cofinal construction of all-low complete source words
realizing every prescribed valuation, and it does not turn a high-gap
source family into a new low-gap obstruction.

## 5. The attempted global continuation and the remaining premise

The two natural continuations were checked against their exact budgets.

First, retaining the proof of `Basin x` does allow every ordinary iterate
of `x`, including `z`, to be called convergent. It does **not** establish
an interval around `z`, or convergence of its affine companion `9z+2`.
Adding either conclusion to the induction hypothesis would be an
unsupported strengthening.

Second, PR185's finite complement machine pays every prescribed finite
credit on a sufficiently long literal source one-run. The needed source
run is not forced here. In the failed phase with large `h`, the original
source can instead start with a two/one entrance and a long run of gap
twos while the target follows a long odd ascent. The credit theorem and
the total arithmetic transition do not alone supply a successful return
to the original lower-grade interval. PR180's terminal-debt embedding also
prevents replacing the remaining positive target by an assumed harmless
terminal state.

The precise next goal is therefore a paid handoff for the failed phase
with **all** of the following data retained: the original source `4q`,
its supplied certificate `3 :: τ`, its grade, the current original target
`n`, the smaller partner `x`, the actual clocks, and
`2^h r ≡ 17 (mod 27)`. Such a handoff may use lower source grades or a
merger with a target below `n`; it may also consume more of the supplied
tail. An arbitrary certificate extracted from `Basin z` has no proved
grade bound and cannot be substituted for this missing step.

Closing the entire failed phase would close this particular psi head.
It must still be distinguished from complete coverage of arbitrary
targets in the larger active interval. No reduction identifying those
two obligations is assumed in this packet.

## Formal receipt

`HeadThreeTarget.lean` contains 13 public theorems. The audit prints the
axioms of every one. Source and audit are checked using Lean4.34.1 core,
`-j1 -DwarningAsError=true`, with the pinned imported closure and no
Mathlib dependency. The receipt records the actual exit codes, source
hashes, audit log, and dependency manifest. No `sorry`, custom axiom,
or `native_decide` is introduced. The theorem count includes the
explicitly credited ordinary transport lemmas; it is not a count of
13 independently new mathematical ideas.
