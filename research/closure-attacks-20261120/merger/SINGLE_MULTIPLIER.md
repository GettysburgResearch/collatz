# One multiplicative-five slice already forces component collapse

**Status: PROPOSED, with a complete elementary proof.** The unbounded
family of factors `5*3^i` in PR154's CR-001 can be replaced by the single
factor `5`. The later PR157 already proves a stronger one-way basin
criterion on this same slice; the present short proof is an independent
reconstruction of its symmetric corollary, not a strengthening of that
latest criterion. The remaining merger hypothesis is **OPEN**. This is an
implication about actual components, not a proof that the required
components coincide.

All integers and paths below are positive and ordinary. We use

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n,\end{cases}
\]

and write `x ~ y` for an actual finite merger at independently chosen clocks.
Put `U={n>=1:3 does not divide n}`.

## M5-001. The single-slice equivalence

The following statements are equivalent:

1. Every positive integer reaches 1.
2. `x ~ 5x` for every positive odd `x` in `U`.
3. `4x ~ 20x+1` for every positive odd `x` in `U`.

Consequently the old five-ray hypothesis `t ~ 5t+1` need only be imposed at
`v_2(t)=2`, `3` not dividing `t`. No higher even valuation is required.

The equivalence of 2 and 3 uses only ordinary paths:

\[
T^2(4x)=x,\qquad T^2(20x+1)=15x+1=2T(5x).
\]

Statement 1 implies 2. We prove that 2 implies 1 through the following
functional statement, so the domain of every use is visible.

## M5-002. Rigidity on the ternary units

Let `f:N_{>0}->A`, with `A` any set, satisfy `f(T(n))=f(n)`. Suppose only

\[
f(5x)=f(x)\qquad(x\in U\text{ odd}).                 \tag{M5}
\]

Then `f` is constant.

First, ordinary halving extends (M5) to every `x` in `U`: write
`x=2^v u` with `u` odd, and halve both `x` and `5x` exactly `v` times.
Thus multiplication or division by 2 and 5 preserves labels within `U`.
No multiplication-by-three invariance is used.

For `n` in `U` with `n=3 (mod 4)`, the first two inputs beginning at `5n`
are odd and

\[
T^2(5n)=5p,\qquad p=\frac{9n+1}{4}\in U.
\]

Hence the two uses of (M5), at `n` and `p`, give

\[
f(n)=f(5n)=f(5p)=f(p),\qquad p=\frac{9n+1}{4}.
                                                               \tag{C5}
\]

This is the only extra affine law needed. It remains conditional on (M5).

Assume that some ternary unit has a label different from `f(1)`, and choose
the least such `n>1`. Every smaller positive ternary unit has label `f(1)`.
Every smaller parameter constructed below is again a ternary unit; this
point replaces the old use of tripling invariance.

**Initial reductions.** If `n` is even, halve it. If `5` divides `n`, divide
by five. If `n=1 (mod 4)`, the ordinary value `(3n+1)/4<n` has the same
label and is in `U`.

Thus `n` is coprime to 10 and `n=3 (mod 4)`. If `n=7 (mod 8)`, set

\[
m=\frac{3n-1}{4}.
\]

It is a positive odd ternary unit smaller than `n`. Also
`(9n+1)/4=3m+1`, so (C5), halving, and the ordinary odd step at `m`
give `f(n)=f(m)`. Therefore

\[
n\equiv3\pmod8.                                    \tag{1}
\]

**The first three residues modulo five.** Each row supplies a positive
integer `q<n` in `U` with `f(q)=f(n)`:

| `n mod 5` | `q` | Justification |
|---:|---|---|
| 3 | `(3n+1)/10` | The ordinary odd step, then divide by five. |
| 1 | `(9n+1)/20` | (C5), then divide by five. |
| 4 | `(27n+7)/40` | Put `p=(9n+1)/4`. By (1), `p` is odd; it is in `U` and is `3 (mod 5)`. Use (C5), the ordinary odd step at `p`, then divide by five. |

The numerators are nonzero modulo three and the denominators are units
modulo three, so all displayed quotients are in `U`.

**The final residue.** It remains that

\[
n\equiv3\pmod8,\qquad n\equiv2\pmod5,
\quad\text{hence }n\equiv27\pmod{40}\text{ and }n\ge27.           \tag{2}
\]

There is no need to split according to `n mod 3`, or use a transferred
`15n+1` law. Take the actual ordinary path

\[
u=T(n)=\frac{3n+1}{2},\qquad
v=T^2(u)=\frac{3u+1}{4}=\frac{9n+5}{8}.
\]

Here `u` is odd and is `1 (mod 4)`, so these are three legal shortcut
steps from `n`. Both `u` and `v` are ternary units, and (2) gives

\[
v\equiv1\pmod{15}.
\]

Indeed `n=40k+27` gives `v=45k+31`. Now use its three parity cases:

| Case | Smaller unit `q` | Justification |
|---|---|---|
| `v` even | `(9n+5)/16` | Halve `v`. |
| `v=1 (mod 4)` | `(27n+23)/32` | Two ordinary steps from `v`. |
| `v=3 (mod 4)` | `(81n+53)/160` | (C5) at `v`, then divide by five, using `v=1 (mod 5)`. |

Each `q` is a positive integer. The middle inequality `q<n` uses `n>23/5`,
which follows from (2); the other two inequalities hold for every `n>=1`.
The three numerators are respectively `2,2,2 (mod 3)`, so division by
their ternary-unit denominators keeps the output in `U`. This contradicts
the choice of `n` in every case.

Thus `f` is constant on `U`. For arbitrary `n`, remove its powers of two.
If the remaining odd integer is divisible by three, its ordinary odd step
has output in `U`. Its label is therefore the same constant. This proves
M5-002. Taking `f` to be the actual merger-component label proves M5-001,
since the component of 1 is exactly its basin. The cycle is `1 -> 2 -> 1`.

## M5-003. Finite path size and the unremoved dependency

The proof gives an explicit selector on `U\{1}`. In every branch,

\[
1\le q<n,\qquad q\le\frac{27n+23}{32}.              \tag{3}
\]

Thus abstract reductions reach 1 in `O(log(2n))` stages. One stage uses
at most three (M5) calls, each at a ternary-unit parameter at most `3n`,
and every vertex in the displayed ordinary/bridge path is at most `15n`.
These bounds refer to the abstract paths with a supplied merger for each
(M5) call. They do not bound the clocks or peaks of the missing supplied
mergers. Replacing an even query by its odd part uses additional actual
halving paths and does not increase height.

The companion checker verifies all the path identities, domains and
inequalities as affine identities on the 320 ternary-unit cells modulo
480. It is not a census of finitely many starts. It records every use of
(M5) separately from actual ordinary edges.

**Why this is not yet a well-founded physical certificate program.** The
smaller output `q` does not make the oracle calls smaller. For example,
on the whole class

\[
n=40k+11\in U,\qquad p=90k+25,
\]

the second row above invokes (M5) at both `n` and the strictly larger
odd unit `p`, before reaching `q=p/5<n`. The actual path is

\[
n\ \stackrel{\mathrm{M5}(n)}{\sim}\ 5n
 \ \stackrel{T^2}{\longrightarrow}\ 5p
 \ \stackrel{\mathrm{M5}(p)}{\sim}\ p
 \ \stackrel{\mathrm{M5}(p/5)}{\sim}\ p/5.
\]

Consequently the proof does not discharge its own calls by induction on
their positive integer parameter. Uniform weighted multiplicity after
replacement by odd parts is also not asserted here.

The first open physical step is exactly: produce an actual finite merger
of `x` and `5x` for every fixed positive odd ternary unit `x`, with a proof
that the production procedure succeeds. No `3^i` family remains necessary
in that target.

## Source pins and scope

- **PR157**, `64361ecca770092d6c8242dc6211e38818af2e50`,
  `research/global-closure-20261120/merger.md`, GCM-001 and GCM-002:
  the stronger forward-five implication in the actual basin already
  suffices. That source has 464 infinite affine cells using 55 words;
  it was fetched and inspected after the present symmetric argument had
  been written. M5-001 is therefore retained as a short independently
  derived corollary, with a ten-branch hand proof and no claim of new
  criterion strength relative to PR157. This note does not re-certify
  every cell of the directed source certificate.
- **PR154**, `fe40bb6f88e8094290ef01207d9bf7c4798d35d0`,
  `research/structural-reset-20261120/component/PROOF.md`, CR-001 and CR-002:
  source of the older restricted family and the residue descent architecture.
  This note removes the auxiliary `F=f(5·)`, the tripling invariance and
  the transferred `15n+1` law; the descent is re-proved on ternary units.
- Same full SHA,
  `research/structural-reset-20261120/component/REDUCED_LAWS.md`: its smaller sufficient system
  still assumes tripling invariance. That assumption is not used here.
- **PR146**, `6863d298187af8b2619efbf78cc4b0aa8e627393`,
  `research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md`: separately supplies
  the one-sided tripling/basin criteria. None is assumed as an ordinary
  merger in this proof.
- **PR151**, `02a9f6ad17e5f1904cb4ff806fd0217d199e8437`,
  `research/ordinary-merger-selection/FIVE_RAY_RECURSION.md`: its physical
  recursive certificates remain distinct from the conditional selector here.
- Latest **PR146**, `1608bb607fadae62723a22156bc96f6ebb452e43`,
  `research/upper-bit-mergers/DEEP_REVERSE_BASIN.md` and
  `research/upper-bit-mergers/RANK_THREE_MERSENNE.md`: the later reverse
  criterion and the three-odd-step Mersenne reduction were also inspected.
  No proof by antecedent certificate length is inferred from them.

The root agent independently reconstructed the argument during this task.
That check does not promote the unproved (M5) hypothesis.
