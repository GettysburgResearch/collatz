# Cofinal complete sources with strictly contracting prefixes

**Status.** This note gives exact, all-word written deductions from the
compiled bounded-four cofinality and literal-certificate interfaces. No
finite search, bound on binary complexity, analytic population assumption,
or new Lean theorem is used. The negative-shadow and target-floor results
are cited by their declarations in the current checkpoint.

The complementary domain to a noncontracting source-prefix rule is itself
cofinal. More strongly, arbitrarily large complete alphabet-four sources
have every later odd state strictly below their initial state. Consequently
source growth alone cannot cover the remaining global interval problem.
The target-floor construction supplies the appropriate return interface.

## 1. Literal notation

Let a supplied complete certificate be

\[
q_0\xrightarrow{a_0}q_1\xrightarrow{a_1}\cdots
\xrightarrow{a_{r-1}}q_r=1,
\qquad 3q_i+1=2^{a_i}q_{i+1},\quad a_i\ge1.
\tag{1}
\]

Every state is a positive odd integer. Define

\[
A_j=\sum_{i<j}a_i,\qquad
C_j=\sum_{i<j}3^{j-1-i}2^{A_i},\qquad
Q_j=\frac{2^{A_j}}{3^j}.
\tag{2}
\]

The prefix identity is

\[
2^{A_j}q_j=3^j q_0+C_j,
\qquad
q_j=\frac{q_0+C_j/3^j}{Q_j}.
\tag{3}
\]

For `j>0`, `C_j>0`. Thus `Q_j≤1` forces `q_j>q_0`.
This is exactly the arithmetic content of
`CollatzLowIntervalRefinement.prefix_expands`.

Call a complete supplied word **strictly prefix-contracting** when

\[
2^{A_j}>3^j\qquad(1\le j\le r).
\tag{4}
\]

This concerns the linear coefficient of each prefix. It does not by
itself assert that its actual affine endpoint is below the original
source: the positive correction in (3) must also be retained.

## 2. Every complete word has a contracting suffix above its source

**Proposition 1.** From every supplied complete certificate (1), one can
retain a literal suffix starting at some `q_j≥q_0` such that every nonempty
coefficient prefix of that suffix strictly contracts. If `j>0`, then
`q_j>q_0` and deletion of the supplied prefix strictly decreases the
original complete-source grade.

**Proof.** Choose the last index `j` minimizing the finite list
`Q_0,...,Q_r`. Since `Q_0=1`, `Q_j≤1`. Equation (3) gives `q_j≥q_0`,
strictly if `j>0`. For every `k>0` with `j+k≤r`, the choice of the last
minimum gives

\[
\frac{2^{A_{j+k}-A_j}}{3^k}
=\frac{Q_{j+k}}{Q_j}>1.
\tag{5}
\]

This is (4) for the retained suffix. The suffix ends at the same literal
terminal one, without replacing any certificate. If `q_0>1`, then
`q_j≥q_0>1`, so `j<r` and the retained suffix is nonempty.

Deleting a nonempty front from the supplied word strictly decreases
`Γ(e;W)` for every retained initial even exponent `e`; this is the
existing `CollatzLowIntervalRefinement.prefix_rank`. When `j>0`, the
source has also increased, so the original target's interval ceiling is
preserved. The existing coefficient or actual-source-growth rule therefore
closes that original interval query under its original rank hypothesis. ∎

An equivalent terminating procedure consumes any nonempty
noncontracting prefix, then repeats on the supplied suffix. Every such
move raises the actual source and shortens the finite word. It must end
with (4). The finite-minimum proof (5) makes its terminal domain explicit.

**Corollary 2.** Complete alphabet-four sources satisfying (4) are cofinal
in the positive integers. They remain cofinal after requiring that their
literal certificate pass through 11.

**Proof.** Given a bound `N`, obtain a complete alphabet-four source
`q_0>max(N,69)` from `CollatzBoundedGapCofinal.cofinal_predecessors`.
Apply Proposition 1. Its retained source is at least `q_0`, and its
literal suffix still has every gap at most four. The theorem
`CollatzBoundedFourNormalForm.above_core_passes_eleven` then factors
that suffix as a nonempty prefix to 11, the fixed tail `[1,2,3,4]`, and
possibly terminal gap-two padding. ∎

Thus a theorem asserting that every sufficiently large supplied
alphabet-four certificate has a noncontracting prefix is false. Cofinality
here is an all-word consequence of exact existing cofinality, not an
extrapolation from numerical examples.

## 3. A stronger cofinal domain: actual future odd maxima

**Proposition 3.** Arbitrarily large complete alphabet-four sources `p`
have

\[
U^k(p)<p\qquad\text{for every }k\ge1.
\tag{6}
\]

Their complete literal certificates satisfy (4), and they pass through 11
once `p>69`.

**Proof.** Start with any complete alphabet-four source above `max(N,69)`.
Among its finite odd states in (1), choose the **last** occurrence of the
maximum, say `p=q_j`. Then `p≥q_0>N`, and every later odd state in the
supplied certificate is strictly smaller than `p`. After the certificate
ends, the accelerated map remains at one, also strictly smaller than `p`.
This proves (6) while retaining the same supplied suffix.

For any nonempty prefix of that suffix, write its endpoint as `v`, its
length as `k`, total exponent as `B`, and positive correction as `C`.
Then `v<p` and

\[
2^Bv=3^k p+C>3^k p.
\]

If `2^B≤3^k`, the left side would be strictly smaller than `3^k p`,
a contradiction. Hence `2^B>3^k` for every nonempty prefix. The literal
11 factorization again follows from the existing normal form. ∎

Selecting the last maximum avoids any auxiliary assumption about cycles.
The entire selected path is already a supplied certificate to one.
The statement allows unrestricted certificate length and unrestricted
binary run count. It does not contradict binary-run forcing: that theorem
may force a later state with more runs while its ordinary height is smaller.

For these sources, `CollatzSourceOrbitProgress.odd_growth_interval_rule`
has no possible future odd endpoint satisfying its growth hypothesis.
This is stronger than the absence of a noncontracting coefficient prefix.
It leaves target-dependent paid rewrites and ordinary mergers available.

### Consequence for negative-block selectors

The new negative-shadow theorem proves that

\[
p+m=2^D u,\qquad m>0\text{ odd},\qquad D\ge6m
\tag{7}
\]

forces an actual nonempty odd prefix with `2^A≤3^k` and a strictly larger
odd endpoint. Therefore no source satisfying (6) admits (7).
The same exclusion holds for a complete strictly prefix-contracting word:
before its terminal one the displayed coefficient is forbidden by (4),
and after terminal one the only odd gap is two, whose coefficient further
contracts. Thus the forced growing endpoint cannot lie after that terminal
either.

Equation (7) is a proved sufficient condition for success. Cofinality of
the complementary domain shows that (7) cannot be made into a universal
source-only selector by allowing more negative shadows or larger search
depths while retaining that same successful-prefix conclusion.

## 4. The target return needed beyond source growth

For an original interval query, put `S=2^e p`, `1≤e≤3`, with odd target
`t` satisfying

\[
S+1<t\le2S+1.
\tag{8}
\]

At an actual future-maximum source (6), consuming a source suffix alone
can lower its grade, but can also lower the interval ceiling past `t`.
That comparison cannot be discarded. Two exact ways to finish are:

1. Supply a certified child comparison for the relevant target with
   strictly smaller original grade and its required interval inequality.
2. Supply an actual target path to a positive integer below the **original
   target**, and use strong induction on that original integer.

The current `CollatzRootedSourceFloor` module makes the second option
concrete without any conjectural source selector. For every `t≥177`,
it supplies a canonical complete source `S=2^e u`, `1≤e≤3`, such that

\[
\frac{t-1}{2}<S\le t-1,\qquad t\le2S+1,
\qquad
T^j(T(S))\le L:=\left\lfloor\frac{t-1}{2}\right\rfloor
\quad(j\ge0).
\tag{9}
\]

The source retains a literal nonempty prefix to 11 over gaps at most four.
When `t≡3 (mod 4)`, the floor `L` is odd and greater than one. No positive
orbit wholly confined below `L` can visit `L`: the next shortcut step
from that odd state would exceed it.

Consequently every odd literal source endpoint `v` in the future of `u`
has its next shortcut state strictly below `L`. If an actual target prefix
returns to `z` with

\[
0<z\le3v+2,
\tag{10}
\]

then, writing `w=T(v)<L`,

\[
z\le3v+2=2w+1<2L+1=t.
\tag{11}
\]

This is the compiled `original_target_cap_descent`, used by
`target_prefix_cap_closes`. It retains the original floor after arbitrary
literal source-prefix consumption. Likewise a return
`z≤2(2^f v)+1` funded by a consumed source gap is below `t`, because
the paid padded source is itself an actual state of the same confined
source orbit; see `consumed_gap_cap_descent`.

The selector (9) deliberately controls the whole future ordinary source
orbit. It does not require or produce source growth. What remains is the
target-dependent assertion that the actual target path reaches a cone
such as (10), or a different comparison paid by the original certificate.
The negative-shadow theorem supplies a strict-grade comparison in its
stated separated-negative source domain; it does not establish the target
return for the cofinal domain in Propositions 1--3.

## Source and formalization ledger

- `lean/Collatz/BoundedGapCofinal.lean`:
  `cofinal_predecessors`, `cofinal_alphabet_iff`.
- `lean/Collatz/BoundedFourNormalForm.lean`:
  `above_core_passes_eleven`, `cofinal_eleven_prefixes`.
- `lean/Collatz/LowIntervalRefinement.lean`:
  `prefix_expands`, `prefix_rank`, `coefficient_interval_rule`.
- Current checkpoint, `lean/Collatz/NegativeShadow.lean`:
  `bounded_negative_prefix`, `physical_negative_return`.
- Current checkpoint, `lean/Collatz/SourceOrbitProgress.lean`:
  `odd_growth_interval_rule`, `negative_block_interval_rule`.
- Current checkpoint, `lean/Collatz/RootedSourceFloor.lean`:
  `source_for_every_target`, `original_target_cap_descent`,
  `consumed_gap_cap_descent`, `target_prefix_cap_closes`.

Propositions 1--3 and their cofinality conclusions are written deductions,
not additional Lean declarations. No exploratory cutoff or new test is
needed for these finite-word arguments.
