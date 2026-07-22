# Cross-direction lemma forge: wave fourteen

Agent: `gpt56-synthesis-01`
Issue: `#29`
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Date: 2026-07-22

## Starting point

This wave followed three newly exposed interfaces:

- PR #3's positive 257-term stage equation, qualitative fresh-prime theorem,
  fixed-room law, and later all-boundary room coding;
- the exact cap-head cell left open by `T-9802`; and
- PR #20's proposed use of a nine-phase linear-independence measure to append
  one scalar period-ten phase.

The source branches moved during review.  The final audited heads are PR #3
`c37e96e`, PR #13 `dc7f966`, and PR #20 `93739b4`.  The `L-0031` and `T-0032`
blobs used by the first result are unchanged across the PR #3 move.  The new
PR #3 `T-0036` strengthens the room interpretation but does not contain the
finite-room theorem below.  PR #20's late `R-9408` supplied the exact published
measure and forced a substantive refinement of the period-ten audit; its later
move to `93739b4` added `L-9415` without changing the audited source blobs.

## Delegation and review

- The quantitative-prime lane converted S-unit finiteness into an explicit
  finite-prefix count and audited the tuple-group rank.
- The cap lane telescoped the last internal connector and resolved the third
  and fourth head symbols into a finer dyadic cell hierarchy.
- The period-ten lane proved a source-independent p-adic Dirichlet floor, then
  incorporated the live quantitative-source update.
- The integrating lane proved a lossless stage-toll decoder and a global
  fixed-room cardinality bound.

Every theorem received a nonauthoring cold review.  `T-9807` received two
independent reviews because the source changed while it was under review.
All four claims remain `PROPOSED`.

## New results

### `T-9805` -- an explicit fresh-prime budget

For `N` consecutive corrected stages, let `s_N` count the distinct primes in
all `N+1` boundary words.  With

```text
C=(6*257)^(3*257)=1542^771,
```

the quantitative Evertse--Schlickewei--Schmidt theorem gives

```text
N <= 4^256 floor(exp(C(2s_N+2))).
```

Equivalently,

```text
s_N >= max(0, ceil((C^(-1) log(N/4^256)-2)/2)).
```

The safe ambient product group has rank `257d`, not `d`.  The sharper count
freezes a source word and exploits the correlated exponent geometry: all
binary and ternary scale powers use one common parameter `D_m`, while every
boundary prime contributes only a numerator direction and a denominator
direction.  The relevant rank is therefore at most `2s_N+1`.

This is an effective strengthening of PR #3's qualitative fresh-prime
necessity.  Its constant is far too large for computation and it does not say
which stage introduces a prime or how that prime crosses a cap stitch.

### `T-9806` -- an exact two-level cap-head hierarchy

Fix the first two symbols `(a,b)` of a stabilized four-symbol head and put

```text
mathcal W_m=q_0/64.
```

All sixteen corrections indexed by `(c,k)` share one remainder modulo
`mathcal W_m`; only their cyclic cell index changes.  The offset splits as

```text
omega_(c,k)=delta_c+q_1 kappa_k mod 64q_1,
kappa=(0,3,53,1),
delta mod64=(0,33,7,11).
```

The sixteen cells are pairwise distinct.  Hence for every threshold
`0<H<=mathcal W_m`, at most one `(c,k)` per fixed `(a,b)` has correction below
`H`.  Globally there are at most 16 exact-zero heads and at least 240 of 256
corrections are at least `mathcal W_m`.

The exact width is

```text
log_2 mathcal W_m=(1419/128)2^m+5.
```

The known conditional cap cusp is wider by leading exponent
`44983/10496`.  Thus this is a genuine algebraic refinement and zero
classification, but not an improvement of `T-9802`'s 64-word cusp filter.

### `T-9807` -- the p-adic dimension floor closes scalar/full-measure elimination

For `D` p-adic values linearly independent with one, elementary pigeonholing
on `(H+1)^(D+1)` integer coefficient boxes produces unbounded forms with

```text
v_p(L(a)) >= (D+1) log_p H(a)-O(1).
```

Every uniform full-space linear-independence exponent therefore satisfies

```text
omega_D>=D+1.
```

For the nine retained period-ten phases this gives `omega_9>=10`.  The live
PR #20 update allowed a stronger, rigorous route closure.  Apply the same
Vaananen--Wallisser measure at dimension one to the tenth phase `beta` and
the coefficient vector `(-p_n,q_n)` of any odd-denominator scalar rational
approximant.  Its height is exactly the reduced rational height and

```text
limsup v_2(beta-p_n/q_n)/log_2 H_n
    <= omega_1
    < 17/5
    < 10
    <= omega_9.
```

No scalar approximant family can satisfy the strict comparison required by
`L-9414`.  The lower value `9/log_2(81)` proved in `L-9413` is only a certified
liminf lower bound; treating it as the exact exponent would not prove the
closure.  The dimension-one upper bound supplies the missing argument.

The canonical PR #20 replay gives
`omega_9=2318.657271149257...`.  The nearby decimal printed in `R-9408` is a
non-load-bearing transcription error.  Directional estimates on the native
coefficient rays, triangular q-difference dynamics, and coupled
Hermite--Pade constructions remain open.

### `T-9808` -- stage words are decoded and eventual rooms are finite

The stage toll

```text
mathcal T_m(w)
 =sum_(k=0)^255 2^(U_(m,k)+alpha_(i_k))
                 3^(V_(m,k)+beta_(i_k))
```

is a lossless dyadic code.  Modulo `2^(U_(m,q))`, successive valuations and
exact subtraction recover the first `q` symbols.  In particular the full toll
is injective modulo `2^(mathcal E_m)`, and the incoming boundary residue

```text
W_m = -3^(-mathcal A_m) mathcal T_m(w_m)
      mod 2^(mathcal E_m)
```

determines the entire 256-symbol word.

Combining these `4^256` incoming residue addresses with the PR #3 floor law

```text
W_m=floor(C H_m)
```

gives

```text
number of eventual rooms <=4^256=2^512.
```

The proof does not assume uniform room sizes or starting scales: it selects a
finite contradictory set, takes its common size bound, common onset, and
positive minimum separation, then uses one sufficiently late scale.  One room
determines at most one eventual boundary and source-word tail.

This strengthens the refreshed all-boundary coding in PR #3 `T-0036` from a
one-parameter representation to a finite exceptional-set theorem.  The finite
set can still be nonempty and is not effectively listed.

## Exact checks and review

- `T-9805`: the primary ESS count, all affine exponent identities through
  scales `12..30`, endpoint generator coordinates, scale distinctness, word
  count, and integer inversion were checked independently.
- `T-9806`: two derivations recovered both offset vectors and the exact cusp
  exponent gap; all 256 corrections were replayed at scales `12,13`.
- `T-9807`: two cold reviewers reconstructed the `D+1` floor, dimension-one
  source applicability, odd-denominator valuation identity, exact rational
  comparison, and directional caveat.  All 30 displays have unique tags.
- `T-9808`: shortened four- and six-letter models recovered every word from
  its toll residue; the reviewer independently derived the room-scale bounds
  and the finite-subset packing argument.

Memory remained healthy throughout the wave; the integration snapshot had
10.39 GiB free and 32.6% physical memory in use.  One overbroad exact cap replay
left its identified Python child process alive after termination; that exact
PID was stopped, and no unknown process was touched.

## Candidate counterexamples

None.  No `K-####` candidate is proposed.

## Closed routes and remaining boundaries

- Fixed finite prime support now has an explicit finite-prefix cost, but the
  bound is structural and does not control prime size or timing.
- The cap head has a finer exact cell hierarchy and at most 16 exact zeros,
  but the available cusp is wider than the new cells.
- Full-space scalar one-phase elimination at period ten is closed.  Only
  directional or genuinely coupled constructions remain in that lane.
- Eventual corrected-stage rooms form a finite set and determine their words,
  but finiteness is not emptiness and no seam-compatible room is identified.

## Files changed

Four theorem files, the packet claim/status/verification ledgers, and this
append-only report.  No canonical root ledger or competing branch file is
changed.

## Recommended next actions

1. Use only the shortest toll prefix whose modulus dominates the room scale;
   the `4^256` bound may collapse dramatically.
2. Absorb the bounded `2`- and `3`-adic endpoint signatures into fixed-word
   coefficients and sharpen the S-unit rank/count.
3. Import the exact Ridout theorem needed by PR #3's two-place room
   approximation and check every normalization before promoting its
   rational-or-transcendental corollary.
4. For each decoded room, intersect the head hierarchy with its 84 exact
   triple seams instead of branching over an independent stage word.
5. Replace period-ten full-space measures by native directional estimates or
   coupled q-difference/Hermite--Pade systems.

## Organizational improvement ideas

When a source claims an approximation exponent from a one-sided height bound,
record whether it is a liminf lower certificate, a limsup upper bound, or an
exact limit.  The distinction changed the proof of `T-9807`.  Quantitative
S-unit applications should display both the safe ambient tuple rank and every
special correlated rank reduction.  Finally, live source heads should be
refreshed after cold review as well as before delegation; both PR #3 and PR #20
moved during this wave.
