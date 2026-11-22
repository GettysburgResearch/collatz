# A complete source buffer, the actual target word, and the missing repair

## Result and proof boundary

This pass uses the **whole actual complete source certificate** selected by
the latest joint minimum argument. It does not replace that certificate by
a contracting symbolic word or a rational shadow.

For its odd source `q`, total ordinary clock `A`, odd-step count `r`, and
positive affine correction `C`, put

\[
P=2^A,\qquad Q=3^r,\qquad Qq+C=P.
\tag{1}
\]

There are three exact conclusions.

1. The formal complete-source branch sends every captured target into
   `(0,17)`, and its fixed point lies in `(0,1)`.
2. If the **actual** target never drops below its original value while this
   source word is consumed, its odd count `o` must satisfy
   \[
   \boxed{6\,3^o>5\,3^r q.}
   \tag{2}
   \]
   This is a logarithmic surplus of target odd steps over source odd steps.
   The proof uses the actual first-hit source and the original-target floor.
3. Reusing the actual target's entire `A`-clock prefix and attaching any
   supplied source suffix is impossible: its proposed starting source is
   either nonintegral or nonpositive. This obstruction holds for every
   positive complete source in the stated canonical domain.

The arithmetic and actual-orbit statements are kernel-checked in
[`lean/WholeSourceBuffer.lean`](lean/WholeSourceBuffer.lean), including the
composition from the first-hit floor directly to (2). They do **not** prove
target return. The constructive attempt still needs an altered-word repair
that preserves positive integer Collatz semantics and pays the original
source grade. A bounded real carry by itself does not provide that repair.

## 1. Exact inputs from the refreshed branches

| Input | Frozen head | Fact used here |
|---|---|---|
| PR177 | `431d858d1ac92e88f4a58f6610c0d67733dc7242` | `JOINT_MINIMAL_COUNTEREXAMPLE.md`: one supplied witness with minimum complete grade, maximum source at that grade, the original-target floor, and canonical complete tail |
| PR176 | `5cb67181758186b372944ef60a1bd09416b97f89` | `FIXED_SOURCE_SIBLING_LIFTS.md`: exact cost of retaining a whole inverse word under a sibling change |
| PR178 | `23456d145df23ef2b412f61f7e49e38a222bc2b1` | `ARITHMETIC_WORDS.md`: existing S-unit and word-complexity audits; no new claim of fixed prime support or bounded complexity is made here |
| PR185 | `4b0c2c27812db555061f5d9006de82a87e7e364f` | `RATIONAL_SHADOW_DISPATCH.md`: a repeated-block compiler requires its actual binary pin and paid target descent |
| PR186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | `03_arithmetic_and_logic.md`: fixed-pattern Diophantine results do not supply a variable-word carry bound |
| Published PR180 base | `a9f471543d7fed0a76f348e6d97a9d6d44fa369e` | The earlier source, sibling, and rational-shadow obstructions; this pass strengthens the input to a complete positive joint witness |

Use the ordinary shortcut convention

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

The PR177 joint counterquery supplies a least bad target `t`, an initial
exponent `1≤e≤3`, a positive odd source `q`, and a complete word

\[
W=V\mathbin{++}[1,2,3,4],\qquad V\ne[],\qquad
q\xrightarrow{V}11\xrightarrow{[1,2,3,4]}1.
\tag{3}
\]

Every gap is at most four. With `S=2^e q`,

\[
S+1<t\le2S+1\le16q+1,\qquad t>1105,
\qquad T^{j+1}(S)\le L:=\left\lfloor\frac{t-1}{2}\right\rfloor.
\tag{4}
\]

The complete grade is

\[
\Gamma(e;W)=\{2e+1\}\uplus\{2a:a\in W\}.
\]

The same witness permits every lower-grade recursive query and every query
from a strictly larger source at the same grade. Both permissions retain
arbitrary queried targets; they are not limited to targets below `t`.
These are inherited results, not new assumptions that a chosen rewrite
will satisfy them.

Let `r=|W|` and `A=sum W`. The literal nonempty prefix in (3) gives `r≥5`.
The first hit of 1 occurs at clock `A`: an earlier hit would remain in the
ordinary `1,2` cycle and could not subsequently visit 11. Its accelerated
affine identity is exactly (1), with `C>0`.

## 2. The whole completed block really does bound the formal carry

The affine branch associated with the supplied source word is

\[
F_W(z)=\frac{Qz+C}{P}
      =1+\frac QP(z-q).
\tag{5}
\]

Completeness gives more than a contracting coefficient. Since `q>1`,

\[
0<Q<P,\qquad 0<C<P-Q,\qquad
c_*:=\frac C{P-Q}\in(0,1).
\tag{6}
\]

For every `0<t≤16q+1`,

\[
Qt+C\le16Qq+Q+C=16P-15C+Q<17P.
\tag{7}
\]

Thus `0<F_W(t)<17`, uniformly in the length, grade, and order of the
complete source word. `complete_source_buffer` checks the natural-number
inequalities underlying (6) and (7). It does not assert that `F_W(t)` is an
integer or an actual target iterate.

This is the strongest version of the buffering idea attempted here: wait
until the entire certified source has reached 1, then use its complete
affine block for normalization. The real carry bound succeeds. The next
question is whether normalization can preserve a legal target word.

### Why the source branch itself cannot be the target branch

In the joint domain,

\[
P=Qq+C>3^5q=243q>16q+1\ge t>q.
\tag{8}
\]

If `F_W(t)` were an integer, subtracting the source identity would give
`P | Q(t−q)`. Since `gcd(P,Q)=1`, this would force `P | t−q`, whereas
`0<t−q<P`. Therefore the bounded value in (7) is **nonintegral** on every
joint counterquery. The source's actual parity branch cannot simply be
reused at the target.

## 3. What actual target survival forces during that same whole block

### The source floor bounds its first-hit clock

The initial `e` steps from `S` to `q` are even. Since `e≥1`, (4) bounds
every ordinary state of `q`, including clock zero, by `L`.

The `A+1` states from `q` through its first hit of 1 are distinct. If clocks
`i<j≤A` had the same state, iterating both another `A−j` steps would produce
a hit of 1 at `i+A−j<A`. All these states are positive and lie in `{1,…,L}`.
Consequently

\[
\boxed{A+1\le L,\qquad 2A<t.}
\tag{9}
\]

`first_hit_clock_bound` proves this finite injection argument for an actual
ordinary orbit. It does not assume a bound on the number of steps from an
arbitrary target.

### An exact target invariant, with every additive term charged

Write

\[
x_j=T^j(t),\quad o_j=\#\{i<j:x_i\text{ odd}\},\quad
b=3t+1,\quad H_j=3^{o_j}t,\quad X_j=2^j x_j.
\]

Assume `x_j≥t` for `0≤j≤A`. The exact invariant is

\[
\boxed{bH_j+jX_j\ge bX_j.}
\tag{10}
\]

At clock zero it is equality. At an even step, `H` and `X` stay unchanged,
so the difference between the two sides increases by `X_j`. At an odd
step,

\[
H_{j+1}=3H_j,\qquad X_{j+1}=3X_j+2^j.
\]

Writing the left-minus-right quantity in (10) as `E_j`, the exact update is

\[
E_{j+1}-3E_j
=2^j(3x_j-3t+j)\ge0.
\tag{11}
\]

This proof uses actual target parity and the lower bound by the original
target. There is no statistical parity assumption and no uncharged
intermediate target.

When `j≤b`, (10), `x_j≥t`, and positivity of `t` imply

\[
\boxed{(3t+1-j)2^j\le(3t+1)3^{o_j}.}
\tag{12}
\]

At the complete source clock, (9) gives `6A<3t+1`. Thus

\[
\frac{3^{o_A}}{2^A}
\ge1-\frac A{3t+1}>\frac56.
\tag{13}
\]

Combining `2^A>3^r q` from (1) with (13) proves (2). In ordinary real
notation, for `o=o_A`,

\[
3^{o-r}>\frac{5q}{6},\qquad
o-r>\log_3 q+\log_3(5/6).
\tag{14}
\]

In particular the surviving target has strictly more odd events than the
entire source word. The natural-number theorem avoids subtraction of
exponents and states (2) directly.

`joint_source_survivor_surplus` composes the actual first-hit and source
floor premises with (10)–(13). It does not accept a separate short-clock
assumption. The source identity remains an explicit supplied-certificate
premise; the full PR177 import tree is not silently reconstructed here.

## 4. Attempted target-dependent splice, with exact legality

The next constructive attempt was to turn the target's surplus into a
cheaper complete source. Retain its actual entire `A`-clock parity prefix:

\[
n=T^A(t),\qquad R=3^o,\qquad Rt+D=Pn.
\tag{15}
\]

Choose any positive endpoint `v` of the supplied source suffix. The source
floor gives `v≤L<t`, while survival gives `n≥t`. The only possible starting
point for that target prefix followed by the source suffix is

\[
u=\frac{Pv-D}{R}
 =t+P\frac{v-n}{R}.
\tag{16}
\]

Because `gcd(P,R)=1`, its exact integrality condition is

\[
\boxed{u\in\mathbb Z\quad\Longleftrightarrow\quad
       v\equiv n\pmod{3^o}.}
\tag{17}
\]

If that congruence holds, then `(v−n)/R` is a negative integer. Equations
(8) and (16) give

\[
\boxed{u\le t-P<0.}
\tag{18}
\]

Thus every choice of supplied suffix fails this unaltered whole-prefix
splice before a grade comparison can even be applied. The obstruction is
not that the original extremal order lacks permission: it is that there is
no positive integer complete source to which that permission could apply.

`positive_splice_impossible` proves the exact general statement from the
two affine identities, `v<n`, and `t<2^A`. `whole_source_splice_impossible`
derives this last bound from `r≥5`, the complete source identity, and
`t≤16q+1`. The proof checks the necessary coprimality rather than treating
formal affine inversion as a legal path.

There is a second limitation on a literal whole-word replacement: (14)
already gives more target odd events than the total number of source gaps.
A same-initial-exponent certificate containing that entire prefix cannot
have the same gap multiset. This does not exclude a **strictly lower**
multiset grade, which can contain many smaller entries. Such a grade drop
would still require a different, physically legal completion.

## 5. The primary transducer theorem and the attempted import

Akiyama, Frougny, and Sakarovitch, *Powers of rationals modulo 1 and rational
base number systems*, Israel Journal of Mathematics 168 (2008), 53–91,
Proposition 13, gives a finite right transducer for digit conversion in a
fixed coprime rational base `p/q>1`. For a finite input alphabet containing
`{0,…,p−1}`, its transition is

\[
qz+d=pz'+a,\qquad 0\le a<p.
\tag{19}
\]

The quotient/remainder selects the next carry and output digit. The
accessible carries are bounded; digitwise addition is one application.
The theorem does not require the integer representation language to be
regular. [Primary author-uploaded paper, Proposition 13, p. 69](https://www.researchgate.net/publication/225408913_Powers_of_rationals_modulo_1_and_rational_base_number_systems),
[DOI](https://doi.org/10.1007/s11856-008-1056-4).

The completed source makes a particularly favorable proposed substitution:
take the base `P/Q`, digit `C`, and carry input `t`. Its quotient in (19)
is at most 16 by (7). At the actual source input `q`, the output digit is
zero and the next carry is 1. At the target input, the output digit is
nonzero by (8).

This is an algebraic one-block normalization. It does not assert that the
arbitrary incoming carry `t` is accessible from the transducer's prescribed
initial state, or that one fixed machine works across all complete words.

**The first unsupported import is that the normalized output digit is the
correction of an actual target Collatz word.** A rational-base digit may be
any member of the canonical alphabet. A Collatz correction must encode
the actual binary parity decisions, with the correct number of odd steps.
In the surviving joint domain (14) requires a different numerator base
`3^o`, not the fixed source numerator base `3^r`. The finite carry theorem
does not change the base in this manner or certify a lower-grade complete
source after doing so.

This pinpoints a concrete constructive task: a nonlocal converter must
normalize the actual variable parity word, preserve its integer endpoint,
and account for its source grade. A finite transducer merely supplied with
valid source words is not ruled out by nonregularity of the input language;
the obstruction demonstrated here is the explicit parity and endpoint
arithmetic.

### Why a prefix-only carry bound is weaker

For contrast, even strict contraction of every source prefix does not
uniformly bound a forced affine carry. Let

\[
W_m=[4]^m[1]^{4m},\qquad c_{j+1}=(3c_j+1)/2^{a_j},\qquad c_0=0.
\]

Here `m≥1`.

Every nonempty prefix has `2^(sum gaps)>3^(number of gaps)`: during the
last run the smallest ratio is `(256/243)^m>1`. But direct solution gives

\[
c_{\rm end}=
\frac{14-(3/16)^m}{13}(3/2)^{4m}-1\longrightarrow\infty.
\tag{20}
\]

This is a statement about a forced algebraic recurrence. It is not asserted
to be a legal positive integer source orbit. Sections 2–4 deliberately use
the stronger actual complete witness, for which (7) succeeds.

## 6. Altering a short part of a high-density inverse witness

The sibling analysis asked whether changing letters, rather than copying
them, can avoid the large cost found in PR176. The following necessary
condition applies even when the changed letters are arbitrary.

Let `n'=B^j(n)` with `B(n)=64n+21`, `j≥1`, `n≥1`. Consider two **legal
positive odd inverse histories of equal depth `r`**. Permit their first
`k` inverse letters, with `0≤k≤r`, nearest the endpoints, to differ. Require the remaining
`r−k` inverse letters to agree. Let `p,p'` be the states just after those
first `k` inverse letters, and `E,E'` their ordinary clocks.

The shared inverse part has an affine numerator `C_0` and clock `H`, so

\[
3^{r-k}x+C_0=2^H p,\qquad
3^{r-k}x'+C_0=2^H p'.
\]

Hence `3^(r−k) | p'−p`. Also `p≠p'`, since otherwise applying the same
deterministic odd map `k` times would give `n=n'`. Positivity then yields
`3^(r−k)<max(p,p')`. The two changed prefixes give

\[
3^k p\le2^E n,\qquad 3^k p'\le2^{E'}n'.
\]

Consequently every such repair satisfies the exact bound

\[
\boxed{3^r<\max(2^E n,2^{E'}n').}
\tag{21}
\]

For the next comparison, write `V_r` for the finite obstacle `V^[r]` of
the preceding packet's `CRITICAL_BOUNDARY.md`, Section 6: with its canonical
unit obstacle `u` and critical inverse operator `𝒫`,

\[
V_0=u,\qquad V_{s+1}=\max(u,\mathcal P V_s),\qquad 0\le u\le1.
\]

The operator weights a legal gap-`a` predecessor by `3/2^a`; its row sum is
at most two, so induction gives `V_r≤2^r`. This notation does not refer to
a sampled density or an unrestricted full-depth population.

If every changed gap is at most `h`, then `E,E'≤hk`. For `η>0`, the finite
high-linear sector `V_r(n)≥ηn` therefore gives `ηn≤2^r`. Since

\[
3n'+1=64^j(3n+1),\qquad 3n'<4\,64^j n,
\]

(21) implies

\[
\boxed{\eta(3/2)^r<\frac43\,2^{hk+6j}.}
\tag{22}
\]

For bounded sibling index and bounded changed gaps, the permitted changed
block must reach a distance proportional to the inverse depth. This is a
necessary condition for pairs of legal histories; it does not assert that
all of the stopped obstacle's mass lies at depth `r` or that an arbitrary
transport preserves that depth.

Retaining an initial inverse prefix imposes the earlier complementary
condition from PR176: if the first `i≥1` inverse letters are untouched,
integrality requires `3^(i−1) | j` for this `B` convention. A cheap sibling
repair must therefore begin changing early, and (22) prevents it from
ending after a uniformly short initial block in the high-linear sector.
Neither statement bounds the number of edits, excludes sparse edits far
apart, nor rules out a fully nonlocal adaptive transport. Equations
(21)–(22) are written deductions, not additional Lean declarations.

## 7. Two other exact literature substitutions

### Analytic interpolation applies to the sibling map

Poonen's *p-adic interpolation of iterates*, Bull. London Math. Soc. 46
(2014), 525–527, Theorem 1, assumes an analytic integral self-map `f` on a
closed unit polydisk with coefficientwise `f(x)≡x mod p^c`, where
`c>1/(p−1)`. It then interpolates `f^n` analytically in the iteration
variable. [Primary author PDF, Theorem 1](https://math.mit.edu/~poonen/papers/p-iteration.pdf).

Here the substitution works for `B` on `Z_3`:

\[
B(x)-x=63x+21\in3\mathbb Z_3[x],\qquad 1>1/(3-1).
\]

Its analytic interpolation is explicitly

\[
B^z(x)=64^z(x+1/3)-1/3,\qquad z\in\mathbb Z_3.
\tag{23}
\]

This changes no ordinary-size constraint in (21)–(22). The analytic theorem
controls the map and its parameter, not the canonical real-valued inverse
population `G` evaluated along that map. Analyticity or a quantitative
Harnack estimate for `G∘B^z` has not been established.

For an actual fixed nonempty source branch `(3^r x+C)/2^A`, the same
near-identity substitution fails at the relevant primes: its linear
coefficient has negative 2-adic valuation, while at 3 its difference from
the identity has a unit linear coefficient. Changing the branch at every
word is an additional issue; it does not define a repeated iterate of one
near-identity analytic map. These are direct checks of the theorem's
hypotheses, not assertions that all p-adic approaches are excluded.

### The S-unit theorem controls fixed complexity

Evertse, Schlickewei, and Schmidt, Annals of Mathematics 155 (2002),
807–836, Theorem 1.1, bounds nondegenerate solutions of a fixed equation
`a_1x_1+⋯+a_dx_d=1` in a finite-rank subgroup of `(K*)^d` by
`exp((6d)^(3d)(R+1))`, where `R` is the group rank.
[Primary paper, Theorem 1.1](https://arxiv.org/pdf/math/0409604).

The source correction in (1) contains `r` monomials, one for every odd
step. Keeping them individually lets the dimension grow with `r`; the
direct product of `d` copies of the group generated by 2 and 3 has rank
`2d`. Replacing the entire sum by one carry variable does not keep that
variable in a fixed finite-rank multiplicative group. PR178 already
derives the valid fixed-prime-support restriction. Neither (2) nor the
whole-block carry bound supplies the missing fixed complexity or prime
support, so no S-unit finiteness theorem is applied as a universal closure.

## 8. Formal scope and the exact next step

The Lean module defines the same ordinary shortcut map, its orbit, and its
actual odd-step count. It imports Mathlib only. Its public results are:

| Declaration | Checked conclusion |
|---|---|
| `first_hit_clock_bound` | Actual first-hit source below a floor has `A+1≤L` |
| `survivor_coefficient_budget` | Exact actual-target coefficient inequality (12) |
| `short_survivor_coefficient` | `2A<t` forces the strict multiplier bound (13) |
| `complete_source_survivor_surplus` | Complete source identity plus the short-clock bound gives (2) |
| `joint_source_survivor_surplus` | Actual source first hit and original-target floor directly give (2) |
| `complete_source_buffer` | Complete-source coefficient, fixed-point, and formal target bounds (6)–(7) |
| `positive_splice_impossible` | No positive source satisfies the unaltered prefix splice identities when `2^A>t` |
| `whole_source_splice_impossible` | The canonical whole-source hypotheses imply that splice exclusion |

All eight declarations compile under Lean 4.34.1 with warnings treated as
errors. Their transitive axiom audits contain only subsets of `propext`,
`Classical.choice`, and `Quot.sound`. Root's separate fresh replay and
complete audit also passed; the report is under
`reports/2026-11-22-deep-machinery/`.

No complete-word dispatcher is introduced as an axiom. The following
inference is still unsupported: that the excess actual target odd events
in (14), together with the global grade minimum and source maximum,
necessarily produce a legal altered-word certificate with a lower grade,
a larger same-grade source, or a return below the original `t`. The
unaltered whole-word construction is excluded by (17)–(18); the transducer
theorem leaves its output legality open. A fully nonlocal repair remains
the arithmetic closing task.
