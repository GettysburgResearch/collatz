# Mixed source induction, interior surgery, and the final head-three family

**New result:** the remaining low-alphabet head-three query now has an
exhaustive reduction to **one affine valuation-three family**. Valuation one,
valuation two, and every valuation at least four are discharged. The proof
combines exact smaller-target mergers, larger-source lower-grade surgery,
and a new well-founded permission to enlarge the source at the **same**
complete grade multiset. Full Collatz and the final residual return remain
**OPEN**; the theorem does not assume their conclusions.

The physical identities, finite-ceiling induction, successful surgery rules,
valuation-two exhaustion, and final classification are in
[`lean/MixedCoverAttack.lean`](lean/MixedCoverAttack.lean). An additional
unbounded two-run permutation is proved constructively in writing below.
The density descriptions concern an earlier arithmetic residual set; they
are neither Lean theorems nor survivor-density bounds.

## 1. Exact inputs and what is new

| Input | Frozen source | Reused fact |
|---|---|---|
| PR177 | `9af9118a7e9af870a32a72a4efdcf77e886940ec`, `research/lean-exact-witness-global-20261121/PSI_HEAD_THREE_FRONTIER.md` | The remaining normalized psi branch has source `S=4q`, first gap three, and target `8q-1`. The example `q=205,u=77` has a smaller partner whose independently extracted source certificate has larger grade. |
| PR176 | `c83a8459066d8223aefe7fc5f6b75faeea557345`, `research/lean-global-resolvent-20261121/overview/whole/SOURCE_TARGET_INDUCTION.md` | One can use smaller ordinary targets at the same supplied source and complete source certificate. The comparison must be with the original target of that query. |
| PR175 | `54b5a324f55d97925ecb8100aa15ce7b08a12093`, `research/lean-global-closure-20261121/AFFINE_MERGER_RIGIDITY.md` | The ordinary rising-run half-erasure diamond has a successful phase; its complement leaves the pair `(6c+1,c)` with `c=2 mod3`. The generic diamond is not claimed new here. |
| PR180 | `cfe70e02f246119a55fb5bf8fd573f148d746beb`, `research/lean-wide-pass-20261122/lean/WitnessSynthesis.lean` and its pinned imports | The physical shortcut map, actual finite orbit, complete trace, interval, and original source-grade interface used by the new Lean module. |

The source and target are positive ordinary integers. Write

\[
3q+1=8u,\qquad u\text{ odd},\qquad
n=8q-1,\qquad p=18u-3.
\tag{M1}
\]

An actual complete source certificate has the form `3 :: tail`; the edge
above deletes that literal first gap and leaves the same certificate at
`u`. The new target transformations do not alter or replace this tail.

The new part starts with an all-parameter diamond **at the correct original
target**, then uses the actual supplied tail to discharge almost all of its
failed phase. The source order is extended by a finite numerical defect,
which makes an equal-grade permutation a legal recursive move. Every
source surgery retains the literal complete suffix at its real endpoint.

## 2. Four clocks expose the relevant arithmetic

The supplied gap gives the actual identity

\[
\boxed{T^4(n)=36u-5=4(9u-1)-1.}
\tag{M2}
\]

The proposed partner satisfies

\[
\boxed{0<p=18u-3<n.}
\tag{M3}
\]

These are public Lean theorems. Neither uses convergence or
a bounded numerical search.

Since `u` is odd, there is a unique factorization

\[
9u-1=2^t w,\qquad t\ge1,\qquad w>0\text{ odd}.
\tag{M4}
\]

Then the two relevant starts are

\[
T^4(n)=2^{t+2}w-1,\qquad p=2^{t+1}w-1.
\tag{M5}
\]

The usual rising-run identity retains the exact physical clocks:

\[
T^b(2^bw-1)=3^bw-1.
\tag{M6}
\]

## 3. Successful phase: arbitrary valuations and arbitrary supplied tails

Suppose

\[
3^t w\equiv1\pmod4.
\tag{M7}
\]

Set `a=3^(t+1)w-1`. Then `a=2 mod4`, so the ordinary two-clock
diamond is

\[
T^2(a)=T^2(3a+2).
\]

Combining it with (M2), (M5), and (M6) gives the exact merger

\[
\boxed{T^{t+8}(8q-1)=T^{t+3}(18u-3).}
\tag{M8}
\]

The lag is five clocks for every `t`, but neither clock has a universal
finite bound. Both trajectories are actual ordinary trajectories.

For an activated query at the already supplied source `S`, the inner
hypothesis of PR176 states that every smaller positive target in the same
interval has reached the basin. Formula (M3) makes `p` such a target.
Formula (M8) then proves the original target belongs to the basin.
`head_three_same_source_rule` checks this argument in Lean.

No source certificate for `p`, `9u-1`, or an odd core extracted from either
number is needed. The same complete source certificate and its original
grade remain fixed during this inner induction.

### The former rank-obstruction example is covered

For `q=205,u=77`, we have `9u-1=692=2^2*173`. Thus `t=2,w=173`,
and `3^t w=1557=1 mod4`. Formula (M8) specializes to

\[
T^{10}(1639)=T^5(1383)=3503.
\]

PR177 correctly observed that obtaining a fresh source certificate for
the number 692 would increase the complete source grade. The new use of
the mixed induction never requests that certificate: 1383 is directly
smaller than the original target 1639. This removes that example's rank
objection without treating it as a proof of every remaining head-three
case.

## 4. Failed phase: the exact ordinary obligation survives

The complementary phase is

\[
3^t w\equiv3\pmod4.
\tag{M9}
\]

It makes the positive integer

\[
c=\frac{3^{t+1}w-1}{4}
\tag{M10}
\]

well defined. The same physical calculation now gives

\[
\boxed{
T^{t+7}(n)=6c+1,\qquad T^{t+3}(p)=c.
}
\tag{M11}
\]

Consequently

\[
\operatorname{Basin}(n)\iff\operatorname{Basin}(6c+1),\qquad
\operatorname{Basin}(p)\iff\operatorname{Basin}(c).
\tag{M12}
\]

The smaller-target hypothesis already supplies `Basin(p)`, hence
`Basin(c)`. It does **not** supply `Basin(6c+1)`. The latter is exactly
the remaining ordinary return question. The residual `c` may be larger
than the original target; its known basin membership comes from its
actual trajectory from the smaller partner, not from an illicit numerical
induction at the enlarged carry.

## 5. Eighteen exact residual families

The original source edge in (M1) forces `u=2 mod3`. Thus (M4) retains
the additional exact constraint

\[
\boxed{2^t w\equiv17\pmod{27}.}
\tag{M13}
\]

In particular, `w` is a ternary unit. Formula (M10) therefore has

\[
v_3(4c+1)=t+1\ge2,
\qquad c\equiv2\pmod9.
\tag{M14}
\]

The powers of two modulo 27 have period 18, and the powers of three
modulo four have period two. Combining (M9) and (M13) by the Chinese
remainder theorem gives

\[
w=108j+w_r,\qquad j\ge0,\qquad r=t\bmod18,
\tag{M15}
\]

with the following complete table:

| `r` | `w_r` | `r` | `w_r` | `r` | `w_r` |
|---:|---:|---:|---:|---:|---:|
| 0 | 71 | 6 | 107 | 12 | 35 |
| 1 | 49 | 7 | 13 | 13 | 85 |
| 2 | 11 | 8 | 47 | 14 | 83 |
| 3 | 73 | 9 | 37 | 15 | 1 |
| 4 | 23 | 10 | 59 | 16 | 95 |
| 5 | 25 | 11 | 97 | 17 | 61 |

Lean checks the finite `18 x 108` residue identity by kernel `decide`,
then proves its lift to every unbounded `t,w`. It is a finite arithmetic
certificate for a universal congruence theorem, not an enumeration of
source values or orbit lengths. `head_three_exhaustive_split` proves
that every ordinary odd head-three source has either the actual smaller
merger (M8) or the residual description (M10)--(M15), with both clocks
in (M11) preserved.

Equivalently, every failed residual belongs to

\[
\mathcal R=
\left\{\frac{3^{t+1}(108j+w_{t\bmod18})-1}{4}:
t\ge1,\ j\ge0\right\}.
\tag{M16}
\]

Every displayed parameter pair is arithmetically realizable: (M15)
implies (M9) and (M13), so
`u=(2^t w+1)/9` is a positive odd integer congruent to two modulo three,
and `q=(8u-1)/3` is positive odd. This does not assert that these newly
reconstructed sources possess a complete convergence certificate; any
application in the original witness program still retains that premise.

## 6. Interior source surgery removes every valuation except two and three

Suppose the supplied complete word is `[3] ++ B ++ tail`, with actual
source segment

\[
q\mathrel{\longmapsto^{3}}u\mathrel{\longmapsto^{B}}v.
\]

If `B` is nonempty, `v>u`, and `3q'+1=8v` for a positive integer `q'`,
then the source with word `[3] ++ tail` is larger: `q'>q`. At every
initial exponent `e`, the replacement `2^e q'` contains the entire old
interval. Its grade strictly decreases because the nonempty interior
block `B` is deleted; the initial grade, leading gap three, and complete
literal tail cancel. `interior_splice_interval_rule` proves this in Lean,
with the actual bridge `GapTrace u v B` explicitly retained.

Two important instances close **all** interval targets:

| Supplied prefix | New prefix | New source relation | Deleted block |
|---|---|---|---|
| `[3,1]` | `[3]` | `q'=4u+1=(3q+3)/2>q` | `[1]` |
| `[3,2,1]` | `[3]` | `q'=(8v-1)/3=(9q+19)/8>q` | `[2,1]` |

For the second row, `v=(9u+7)/8>u`. Both new endpoints have ternary
class two, so the retained gap three has an integer positive predecessor.
The whole prefix `[3,2,1]` contracts, but its interior `[2,1]` expands;
that is why keeping the leading gap is decisive.

The factorization (M4) forces exactly these prefixes at all but two
binary valuations:

- At `t=1`, oddness of `w` forces `u=3 mod4`, so the actual next gap is
  one. The supplied prefix is `[3,1]`.
- At every `t>=4`, `9u=2^t w+1` forces `u=9 mod16`. The actual next
  two gaps are two and one. The supplied prefix is `[3,2,1]`.

`head_three_valuation_one_rule` and `head_three_valuation_large_rule`
check both forcing arguments and their interval conclusions. They do not
restrict the later tail or the half-erasure phase.

Combining these rules with the exact cofactor table leaves

| Valuation | `q` | `u` | `c` | Forced source information |
|---:|---|---|---|---|
| 2 | `128j+13` | `48j+5` | `729j+74` | The next gap is at least four; if every supplied gap is at most four, then `j` is even and the prefix is `[3,4]`. |
| 3 | `256j+173` | `96j+65` | `2187j+1478` | The supplied prefix is `[3,2,2]`, ending at `54j+37`. |

The intermediate theorem `head_three_two_family_frontier` retains the
actual complete source certificate and gives precisely these two
remaining affine families. The next section eliminates the entire first
row in the low-alphabet problem.

## 7. A finite source defect licenses larger sources at the same grade

Let `G` be the complete list of source grades. Every actual complete
powered source certificate satisfies

\[
\boxed{S\le2^{e+\sum\mathrm{word}}\le2^{\sum G}.}
\tag{M18}
\]

For the first bound, induction down the literal source word gives
`q<=2^(sum word)` from `3q+1=2^a u` and the endpoint one. The second
uses the grade convention: the initial exponent contributes `2e+1`
when positive, and each odd gap contributes twice its value.
`powered_source_ceiling` formalizes this bound.

Equal grade multisets have equal sums, even when their words are
permuted. Therefore the secondary coordinate

\[
D_G(S)=2^{\sum G}-S
\tag{M19}
\]

strictly decreases when a new **complete** source `S'>S` has the same
grade multiset. Its completeness supplies `S'<=2^(sum G)`, so truncated
natural subtraction cannot invalidate the decrease. This is a bounded
reverse source order, not unrestricted induction on increasing integers.

The new recursive order is:

1. Decrease the existing complete source-grade multiset; or
2. Retain its multiset and decrease `D_G(S)` by enlarging the supplied source; or
3. Retain source and complete certificate and decrease the original queried target.

`fixed_grade_source_tie_wellFounded` proves the second coordinate is
well founded, and `close_fixed_grade_with_source_and_target` simultaneously
justifies the second and third permissions by nested ordinary induction
at every fixed outer grade. Its complete dispatcher is an explicit
premise. The existing outer multiset induction remains the first
coordinate; no complete dispatcher is asserted here.

### Two exact interval surgeries

For a supplied prefix `[3,4,1]` at initial exponent two, write the common
endpoint as `z=27h+2`. The old odd source is `q=256h+13`. Replace it by

\[
r=192h+13\mathrel{\longmapsto^{3}}
72h+5\mathrel{\longmapsto^{3}}z.
\]

The new powered source is `8r>4q`. The old grades before the common tail
are `[5,6,8,2]`; the new grades are `[7,6,6]`. The highest changed grade
eight disappears, so the complete grade strictly drops. The tail at `z`
is unchanged. `head_three_four_one_interval_rule` closes every old
interval target by the original outer hypothesis.

For a supplied prefix `[3,4,2]`, write the endpoint as `z=27h+1`.
Then `q=512h+13`, and the new word is

\[
q+4\mathrel{\longmapsto^{2}}384h+13
\mathrel{\longmapsto^{3}}144h+5
\mathrel{\longmapsto^{4}}z.
\]

This is the permutation `[3,4,2] -> [2,3,4]`. At every initial exponent,
the complete grade multiset is unchanged, the source grows by `2^e*4`,
and its finite defect decreases. `head_three_four_two_interval_rule`
uses the justified `LargerSameGradeHyp` and closes every old interval
target. It does not apply the older strict-grade hypothesis to a tie.

### Exhaustion of the valuation-two low-alphabet family

The actual next gap four gives `v=9j+1`. Since this endpoint is odd,
`j` is even. These cases exhaust every such `j`:

| Parameter case | Successful rule |
|---|---|
| `j=0` | Original target `103` has `T^56(103)=1`, checked by Lean kernel reduction. |
| `j=2 mod4` | `v=3 mod4`, so the supplied source starts `[3,4,1]`; use the strict-grade surgery. |
| `j>0`, `j=0 mod8` | `v=1 mod8`, `v>1`, so the supplied source starts `[3,4,2]`; use the finite-defect surgery. |
| `j=4 mod8` | Write `j=8h+4`; use the exact original-target descent below. |

In the final row the original target and its exact orbit satisfy

\[
\boxed{T^{13}(8192h+4199)=6561h+3364<8192h+4199.}
\tag{M20}
\]

Indeed the residual identity first reaches `34992h+17941` in nine clocks,
and
`3(34992h+17941)+1=16(6561h+3364)` pays four more clocks. The endpoint
is positive and strictly below the **original** queried target, so the
same-source inner induction applies. `head_three_two_residue_descent`
and `head_three_two_low_family_rule` formalize the exact descent and
this exhaustive parameter split.

## 8. An unbounded, same-grade two-run permutation

The following additional rule is a **written theorem**, proved here from
actual supplied edges. It is not included in the Lean theorem count.
For every `k>=1`,

\[
[3]\mathbin{++}2^k\mathbin{++}[4,1]
\quad\rightsquigarrow\quad
[2,4]\mathbin{++}2^{k-1}\mathbin{++}[1,3]
\tag{M21}
\]

replaces the odd source `q` by `q+4`, with the identical endpoint and
literal complete tail. Here `2^k` denotes a list of `k` gaps equal to
two, not an arithmetic power.

Write the old segment as

\[
q\xrightarrow{3}u\xrightarrow{2}v_1
\xrightarrow{2}\cdots\xrightarrow{2}v_k
\xrightarrow{4}a\xrightarrow{1}b.
\]

The new segment is explicitly

\[
q+4\xrightarrow{2}2u+3
\xrightarrow{4}\frac{v_1+1}{2}
\xrightarrow{2}\cdots\xrightarrow{2}\frac{v_k+1}{2}
\xrightarrow{1}4a+1\xrightarrow{3}b.
\]

Every displayed state is a positive ordinary odd integer. For `i<k`,
the actual gap two makes `v_i=1 mod4`; the last actual gap four gives
`v_k=1 mod4` as well. Thus every shifted `(v_i+1)/2` is odd. The edge
identities follow directly:

\[
\begin{aligned}
3(q+4)+1&=4(2u+3),\\
3(2u+3)+1&=16\frac{v_1+1}{2},\\
3\frac{v_i+1}{2}+1&=4\frac{v_{i+1}+1}{2},\\
3\frac{v_k+1}{2}+1&=2(4a+1),\\
3(4a+1)+1&=8b.
\end{aligned}
\]

The gap multiplicities are identical: one three, one four, one one,
and `k` twos. The same powered-source exponent and literal tail therefore
preserve the full grade multiset. The new powered source is larger, so
(M18)--(M19) license the rewrite. This removes every occurrence of the
entire displayed prefix family, including `[3,2,2,4,1]`, without a bound
on `k` or on the later tail. It does not say every remaining complete
word has this prefix.

### A further successful interior block in the valuation-three family

For `j=3 mod4` in (M22), the supplied word necessarily begins
`[3,2,2,1,1]`. After the first three gaps, the endpoint is `54j+37`;
the next endpoint is `81j+56`. Both are three modulo four, forcing the
two displayed gaps one. The endpoint after that block is

\[
a=(243j+169)/2>96j+65=u,\qquad a=2\pmod3.
\]

Delete the interior `[2,2,1,1]` while retaining the initial gap three.
The replacement odd source is

\[
q'=(8a-1)/3=324j+225>256j+173=q.
\]

Its complete word is `[3] ++ tail`, with exactly the same tail at `a`.
This is a written direct application of the kernel-checked
`interior_splice_interval_rule`: the nonempty interior block is deleted,
the source grows, and every old interval target remains covered. Thus
this parameter subfamily is also discharged. No new formal theorem or
claim of exhaustion of the other valuation-three parameters is made.

### Remaining written parameter refinements

The same unbounded permutation also closes the whole valuation-three
class `j=0 mod16`, with one complementary physical descent:

- If `j=0 mod32`, the supplied source forces `[3,2,2,4,1]`, which is
  (M21) with `k=2`.
- If `j=32h+16`, then the exact residual clock first gives
  `T^10(65536h+34151)=419904h+218821`. The next six states are
  `629856h+328232`, `314928h+164116`, `157464h+82058`,
  `78732h+41029`, `118098h+61544`, and `59049h+30772`.
  Their parities are respectively even, even, even, odd, even, and
  unrestricted at the final endpoint. Hence
  `T^16(65536h+34151)=59049h+30772<65536h+34151`, so the original-target
  inner induction closes this class.

Finally `j=8 mod16` forces a source gap at least five immediately after
`[3,2,2]`: its endpoint `z=54j+37` has `32 | 3z+1`. This is impossible
in the low-alphabet domain. Combining these written deductions with the
previous `j=3 mod4` interior rule leaves only

\[
j=1\pmod4,\qquad j=2\pmod4,\qquad\text{or}\qquad j=4\pmod8
\]

as unclassified parameter phases inside the formal valuation-three
frontier. These are **written refinements**; the Lean theorem remains the
exhaustive valuation-three statement (M22), with no claim that this last
three-phase domain has been discharged.

## 9. Two arithmetic descriptions of the pre-surgery split

These describe the arithmetic split in Sections 3--5 **before** the
successful source surgeries below are applied. They are not counts of
eternal survivors, surviving Collatz inputs, or predecessor basins.

**Exactly half of the admissible ordinary source progression is in the
successful phase.** Among `u=5 mod6`, the valuation in (M4) has relative
density `2^-t`, for each `t>=1`. The odd cofactor has the two residues
modulo four with equal relative density. Thus the successful phase in
(M7) contributes `2^(-t-1)` at depth `t`, and their disjoint sum is
one half. The remaining high-valuation tail has relative density at most
`2^-T`, justifying the infinite union.

**The residual set R has natural density `1/162`.** For each fixed `t`,
(M16) is one complete positive progression with step

\[
\frac{3^{t+1}\,108}{4}=3^{t+4}.
\]

Different `t` have different exact valuations in (M14), so these
progressions are disjoint. Their density sum is

\[
\sum_{t\ge1}3^{-(t+4)}=\frac1{162}.
\]

To justify passage to the infinite union, every element of the `t`th
progression is at least `(3^(t+1)-1)/4`. Up to height `X`, only
`O(log X)` progressions occur. After any fixed depth `T`, their count is
at most `X*sum_(t>T) 3^(-t-4)+O(log X)`. Divide by `X`, let `X` grow,
then let `T` grow. No statistical assumption about Collatz is used.

## 10. Exact final frontier and first unsupported inference

`head_three_low_final_frontier` now proves the following exhaustive result.
Given the actual complete source `q ->[3] u ->word 1`, all supplied gaps
at most four, and the three justified recursive permissions, either the
original target is in the basin, or there are `j>=0` and a literal tail
such that

\[
\begin{aligned}
q&=256j+173,&u&=96j+65,\\
\mathrm{word}&=[2,2]\mathbin{++}\mathrm{tail},&
54j+37&\xrightarrow{\mathrm{tail}}1,\\
c&=2187j+1478,&\operatorname{Basin}(c)&\text{ holds},\\
\operatorname{Basin}(8q-1)&\iff\operatorname{Basin}(6c+1).
\end{aligned}
\tag{M22}
\]

The exact remaining clocks are `T^10(8q-1)=6c+1` and
`T^6(18u-3)=c`. The ordinary partner is smaller than the original target;
its known convergence supplies `Basin(c)`.

A sufficient final return is therefore

\[
\boxed{\operatorname{Basin}(2187j+1478)
\Longrightarrow\operatorname{Basin}(13122j+8869)}
\tag{M23 -- OPEN}
\]

on the displayed supplied-certificate domain. A successful lower-grade
or same-grade source surgery, or a merger with a target below `8q-1`,
could also discharge a remaining query. The unbounded rule (M21)
removes further genuine words from this domain. What is **not** proved is
that every remaining supplied `[3,2,2]` tail either reaches such a source
rewrite or yields an ordinary target descent. Inferring that exhaustion
is the first unsupported step; it is not a theorem in this packet.

The earlier Lean `ResidualReturn` and `head_three_of_residual_return`
remain as a broader sufficient condition for the pre-surgery set (M16).
They are explicitly conditional and are superseded as a frontier by
(M22). Neither return premise is an axiom.

Even eliminating (M23) would close this normalized psi branch in the
combined induction. Arbitrary non-psi interval targets still require
complete coverage. This module therefore proves neither `MixedCover`
nor universal Collatz convergence.

## 11. Formal evidence and scope

The module contains **twenty-nine public theorem declarations**, each with
an explicit `#print axioms` audit. **All twenty-nine passed** Lean 4.34.1
with `-DwarningAsError=true`. Their reported transitive axioms are only
subsets of `propext`, `Classical.choice`, and `Quot.sound`.

| Formal group | Theorem count | Scope |
|---|---:|---|
| Exact physical prefix, partner, merger, residual, cofactor table, and original conditional consumer | 12 | The all-parameter arithmetic split from Sections 2--5 |
| Interior grade deletion and source enlargement, `[3,1]` / `[3,2,1]` surgeries, forced valuation exclusions, two-family frontier | 7 | Every tail at `t=1` and `t>=4` closes |
| `[3,4,1]` surgery, source ceiling, finite-defect decrease and well-foundedness, `[3,4,2]` permutation, nested source/target induction | 6 | Strict-grade and equal-grade source rewrites with actual complete certificates |
| Thirteen-clock descent, whole valuation-two low-family closure, forced valuation-three prefix, final low frontier | 4 | Only the supplied valuation-three family remains |

The only direct project import is pinned PR180 `WitnessCritical`, which
imports `WitnessSynthesis` and its recorded chain. The reused helper is
the existing arbitrary-prefix grade decrease; the new module lifts it
past the retained initial exponent and gap three. No source proof from
another branch is modified or silently accepted through the audit.

The unbounded permutation (M21), the subsequent valuation-three word and
parameter refinements, and the two arithmetic density calculations retain
written-proof status. The complete global dispatcher remains open.
