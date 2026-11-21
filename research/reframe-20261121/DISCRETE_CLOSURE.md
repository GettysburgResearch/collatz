# Canonical witness languages and the arithmetic budget of a repeated block

## Outcome and scope

This pass examined a global, target-aware certificate grammar, using the
repository's complete exponent-histogram rank as the induction order. The
universal arithmetic dispatcher is still missing. The new checked result is a
constraint on how such a dispatcher can be organized: an odd-containing fixed
inverse block cannot be pumped indefinitely through ordinary integers, except
at its exact fixed point. Canonical first-hit certificates exclude that fixed
point exception as well.

The arithmetic and canonical-pump statements are proved in
[`lean/DiscretePump.lean`](lean/DiscretePump.lean), using Lean 4.34.1 with its
default `Init` environment and no external imports. The language-theoretic
corollaries below are mathematical deductions from that checked theorem; this
packet does **not** claim a Lean formalization of automata, pumping lemmas,
or the translation from Collatz words into affine equations.

There are two precise language consequences:

1. Over any fixed finite alphabet of positive accelerated exponents, every
   context-free sublanguage of positive canonical Collatz certificates is
   finite. In particular, every regular sublanguage is finite.
2. Over the ordinary two-letter parity alphabet, every regular sublanguage of
   positive canonical certificates has a uniform bound on its number of odd
   steps. Even-only loops remain possible.

Neither statement proves that every positive integer has a certificate. They
also do not exclude a finite collection of rewrite schemas carrying unbounded
arithmetic state. The theorem concerns context-free languages of fully valid,
canonical words, without such additional state.

## What the repository now makes available

This branch started from PR178 at
`0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`. The comparison with the following
heads was read-only:

| Packet | Pinned head | Relevant result and remaining scope |
| --- | --- | --- |
| [PR177](https://github.com/GettysburgResearch/collatz/pull/177) | `00a611094043afeb256d6532b477c0709e8ed270` | A complete exponent-histogram order admits arbitrarily long lower-grade rewrites. `GapComparison.Complete` is still an assumption in the global closure theorem. High-gap pumps, low-gap loops, and resets supply guarded cases. |
| [PR175](https://github.com/GettysburgResearch/collatz/pull/175) | `06215e69346c4d32bf970af9c846a6894586c1e7` | Actual marked returns can expand and reset their trailing-one depth. Every finite odd-source parity cylinder has cofinal marked realizations. A finite feature rank cannot infer the required universal return behavior. |
| [PR179](https://github.com/GettysburgResearch/collatz/pull/179) | `27a2c7414fdb92eeca57ad552a9ab5c36d8430d8` | Coefficient and crossing budgets turn some paired trajectories into ordinary descent, with explicit hypotheses. The known source's first hit alone does not pay the target's debt. |
| [PR181](https://github.com/GettysburgResearch/collatz/pull/181) | `5f03d809b4495802971211ef13ff905f741d700d` | An expanding paired block has a finite divisibility budget. Selected paying exits repay it. Switching between different blocks and obligations is not covered by that one-block budget. |
| [PR182](https://github.com/GettysburgResearch/collatz/pull/182) | `8372e302041a55057742a9e6ee9b4fa600c88fdb` | Strong marked contractions and exact phase/balance restrictions hold on specified families or under specified balance conditions. No universal phase condition is supplied. |
| [PR141](https://github.com/GettysburgResearch/collatz/pull/141) | `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b` | Finite bounded-popcount cores and guarded string-rewriting ranks provide genuine finite closures. They do not give a fixed population cap for all ordinary sources. |

The useful global change in PR177 is its induction order. Replacing one
exponent by arbitrarily many smaller exponents is legitimate; a fixed-base
sum of weights is unnecessary. For a powered source certificate `(e,w)`, the
rank consists of the grade `2e+1` when `e>0` and the grades `2a` for the gaps
`a` in `w`, ordered at the highest changed grade. This removes a restriction
on the *size of a successful rewrite*. It does not make its arithmetic guard
true for every source and target.

The proposed global architecture therefore remains: consume actual source
certificates, use an arithmetic guard to select a strictly lower-grade child
comparison, and close all comparisons by well-founded induction. The result
below identifies a constraint on attempts to replace this arithmetic selection
with a regular language of valid witness words.

## Ordinary integer inverse blocks

Use the shortcut Collatz map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

A fixed valid parity block of length `A`, with `r` odd steps, has the affine
identity

\[
2^A T^A(x)=3^r x+C.
\]

An accelerated exponent block has the same identity, where `A` is the sum of
its exponents and `r` is its number of entries. Reversing the block therefore
acts by

\[
F(x)=\frac{2^A x-C}{3^r}.
\]

Fix `A`, `r`, and the ordinary integer `C`. Suppose ordinary integers
`q₀,…,qₖ` satisfy

\[
3^r q_{j+1}+C=2^A q_j\qquad(0\le j<k).
\]

Define the integer defect

\[
\Delta(q)=(2^A-3^r)q-C.
\]

One step gives

\[
3^r\Delta(q_{j+1})=2^A\Delta(q_j),
\]

and induction gives the exact identity

\[
3^{rk}\Delta(q_k)=2^{Ak}\Delta(q_0).
\]

The two exponential coefficients are coprime. Thus

\[
\boxed{3^{rk}\mid |\Delta(q_0)|.}
\]

This divisibility statement is valid even when the defect is zero. If the
defect is nonzero, it yields the finite budget

\[
\boxed{3^{rk}\le |\Delta(q_0)|.}
\]

For `r>0`, an infinite ordinary integer chain would make this inequality hold
for arbitrarily large `k`. Consequently its initial defect must be zero. The
initial value is an exact fixed point of `F`, and cancellation in the block
equation then shows that every `qⱼ` equals `q₀`.

This is an ordinary integer statement. It does not argue that a prescribed
infinite 3-adic expansion must terminate, and it does not use a probability or
density estimate. Positivity is not needed for the arithmetic theorem.

### Checked declarations

All names below are in namespace `CollatzDiscretePump`.

| Declaration | Statement proved |
| --- | --- |
| `defect_step` | One-step exact defect scaling. |
| `defect_iter` | The exact finite-chain identity. |
| `loop_divisibility` | `3^(r*k)` divides the natural absolute value of the initial defect. |
| `loop_budget` | The nonzero-defect numerical bound. |
| `infinite_chain_fixed` | An infinite chain with `r>0` has zero initial defect. |
| `infinite_chain_fixed_equation` | Its initial value satisfies the original fixed-point block equation. |
| `infinite_chain_constant` | Every value in the chain equals its initial value. |
| `first_hit_unique` | A deterministic ordinary source has at most one first-hit clock. |
| `no_canonical_affine_pump` | A fixed odd-containing affine pump, a fixed affine prefix, and canonical first-hit clocks cannot coexist. |

The last theorem is deliberately stated for an arbitrary function
`f : Nat → Nat`. It retains the actual first-hit predicate instead of replacing
it with mere endpoint equality. Its hypotheses are:

\[
\begin{aligned}
3^r q_{j+1}+C&=2^A q_j,\\
3^b n_j+P&=2^U q_j,\\
\operatorname{FirstHit}_f(n_j,U+jA+Z)&,
\end{aligned}
\]

with `r>0` and `A>0`. The first equation forces `q₁=q₀`. The fixed-prefix
equation forces `n₁=n₀`. First-hit uniqueness then forces
`U+A+Z=U+Z`, contradicting `A>0`.

## Canonical first hits close the fixed-point exception

A *canonical certificate* records the orbit only up to its first visit to one.
For the source one, the canonical word is empty. Appending the terminal
`1 → 2 → 1` cycle does not produce another canonical certificate.

Consider a family of canonical words

\[
u\,v^j\,z\qquad(j=0,1,2,\ldots).
\]

The suffix `z` has a fixed final value one. Its affine identity determines a
unique ordinary starting value `q₀`. The values at the start of `v^j z` are
therefore the successive inverse iterates `qⱼ=F^j(q₀)`. Each is an actual
positive ordinary orbit value because every member of the family is a valid
certificate. The fixed prefix `u` determines the corresponding ordinary
source `nⱼ` by one fixed affine equation.

If `v` contains an odd step, its odd count is positive and the checked theorem
applies. It gives identical sources for `j=0` and `j=1`, but their first-hit
clocks differ by the positive length of `v`. This is impossible.

This argument also handles `q₀=1`. A pumped loop based at one would insert a
visit to one before the claimed final clock. It is excluded by the first-hit
hypothesis, without needing a separate classification of positive Collatz
cycles. A putative fixed point greater than one is excluded by the same
deterministic first-hit argument.

## Consequences for finite alphabets

### Accelerated exponent words

Fix a finite alphabet `E ⊂ {1,2,3,…}`. Let `C_E` be the set of words over `E`
that are canonical accelerated certificates of some positive odd ordinary
source. Each letter includes one odd step followed by its halvings; a separate
initial power of two is not part of this word encoding.

**Claim.** Every context-free language contained in `C_E` is finite.

**Proof.** By the context-free pumping lemma, an infinite context-free
language contains a family `u v^j x y^j z` for every `j≥0`, where at least one
of `v,y` is nonempty. If `y` is nonempty, examine the actual orbit suffix
`y^j z`. Each such suffix is itself a canonical first-hit certificate of its
ordinary starting state. The fixed suffix `z` determines its initial inverse
tail value. Here `r=length(y)>0` and `A=sum(y)>0`, so the canonical affine
pump theorem, with an empty prefix, rules out this family. If `y` is empty,
`v` is nonempty and the same argument applies to the canonical suffixes
`v^j xz`, whose fixed tail is `xz`. ∎

Regular languages are context-free, so their sublanguages obey the same
finiteness conclusion. The simpler regular pumping form `u v^j z` also gives
the result directly.

This is explicitly a statement about the accelerated exponent alphabet. It
is not invariant under recoding an unbounded exponent as a string over some
other alphabet.

### Literal parity words

Let `C_par` be the set of canonical shortcut parity words over `{O,E}`.

**Claim.** If an `N`-state deterministic automaton recognizes a sublanguage of
`C_par`, every accepted word has fewer than `N` odd letters.

**Proof.** Suppose an accepting run contains at least `N` odd transitions.
Take its initial state and the states immediately following its first `N`
odd transitions. Two of these `N+1` cut states coincide. The intervening
nonempty segment contains an odd transition, so it can be repeated any
number of times while preserving acceptance. This produces a forbidden
odd-containing canonical pump. ∎

The conclusion permits infinite regular languages. For example `E*` records
the first-hit certificates of powers of two. The language

\[
O\,EEE\,(EE)^*
\]

records the first-hit certificates of `(4^k−1)/3` for `k≥2`. It has exactly
one odd step and an unbounded gap. In accelerated notation these are the
one-letter words `[2k]`; they do not belong to one fixed finite exponent
alphabet.

### The bounded-gap assertion is nonvacuous

There are actual positive canonical certificates of arbitrarily large odd
length using only the exponents `{2,3,4,5}`. The following construction is
included to establish that scope, not as a coverage theorem for all sources.

Start from `q=5`, whose certificate is `[4]`. Suppose `q>1` is odd and is not
divisible by three. Choose a base exponent `a=2` when `q≡1 (mod 3)`, or `a=3`
when `q≡2 (mod 3)`, and put

\[
p=\frac{2^a q-1}{3}.
\]

The number `p` is an odd integer greater than `q`. If `p` is not divisible
by three, use it. Otherwise replace it by

\[
p'=4p+1=\frac{2^{a+2}q-1}{3}.
\]

Now `p'≡1 (mod 3)`. Both choices give a larger odd ternary unit with an
actual accelerated edge to `q`, using one of the gaps `2,3,4,5`. The orbit
along this edge consists of the initial odd value followed by positive
power-of-two multiples of `q>1`, so it does not introduce an earlier visit to
one. Inductively the sources increase strictly and the canonical odd-step
counts are unbounded.

For example the first sources obtained by this rule are
`5, 13, 17, 181, 241, 1285`. The argument is symbolic; no finite search bound
is being promoted to an infinite claim.

In particular the bounded-gap canonical language on `{2,3,4,5}` is infinite
and has no infinite context-free sublanguage. The full literal-parity canonical
language has unbounded odd count and therefore is not regular.

## What remains for a full global closure

The repeated-block theorem gives an exact finite budget for *one fixed block
at one fixed suffix value*. A change of block changes its defect. The proof
does not supply one nonnegative account that decreases across arbitrary
changes of blocks or across changes of the active source-target comparison.

The bounded-gap predecessor construction above makes this distinction
concrete. It builds an infinite ordinary inverse path by switching among a
finite set of gap values. Such a path is compatible with every fixed-block
budget. It is not a divergent forward orbit: each of its sources has a finite
forward certificate to one.

For the PR177 architecture the remaining universal statement is still the
complete dispatcher: for every active comparison and every actual source
certificate, select either an ordinary closure or a legitimate child
comparison of strictly smaller complete histogram. In the important `ψ`
case the comparison is

\[
\operatorname{Basin}(s)\Longrightarrow\operatorname{Basin}(2s-1).
\]

Universal `ψ` closure would imply Collatz by strong induction on the target:
an even target halves, and an odd target `n>1` is `2s−1` with
`s=(n+1)/2<n`. The current guarded clauses do not cover every such source
certificate.

A target-aware grammar can carry unbounded arithmetic information and thus
is not ruled out by the regular-language theorem. Its missing invariant must
control changes of affine block and target obligation. Merely proving that
each individual repeated block eventually stops does not control an
unbounded sequence of different blocks. Likewise, invoking a lower-rank
comparison yields a basin fact; it does not automatically yield a new
certificate whose histogram is small enough for another induction call.

This pass does not discharge that dispatcher. It supplies a checked generic
ordinary-integer budget and a precise reason that unconditional finite-state
word selection cannot supply universal canonical coverage.

## Validation

The source was checked with Lean 4.34.1, one worker, and warnings as errors:

```sh
lean -j1 -DwarningAsError=true \
  -o .build/discrete/DiscretePump.olean DiscretePump.lean
```

The command completed with exit status zero. The repository's combined
[`lean/build.sh`](lean/build.sh) also includes this module. The module uses
neither `sorry`, `axiom`, `admit`, nor `native_decide`. Its theorem assumptions
are the explicit equations and first-hit hypotheses shown above. No claim
that Collatz, the complete dispatcher, or the language corollaries have been
fully formalized is made here.
