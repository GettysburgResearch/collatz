# An exact signed carry compiler for every supplied source word

Date: 2026-11-22. **Status: kernel-checked finite arithmetic and complete-source
transport. The universal stopping/interval-cover assertion remains OPEN.**

The new module `CollatzGlobalClosure/SignedCarry.lean` replaces the finite
carry-state alphabet by an exact signed state `(p,c)`, without bounding either
coordinate or the supplied source word. It handles the original carry
`9*r+2` as `(2,-2)`, retains the actual complete source suffix, and proves
the original target's ordinary path and exact odd-count budget. A separate
finite signed-ray theorem supports the analytic continuation's use of
negative arithmetic scaffolds. No assertion about convergence of negative
Collatz integers is used.

This is a constructive arithmetic component, not a total successful Collatz
dispatcher. The compiler is total on a finite supplied word because it can
return an explicitly unresolved terminal carry. Its theorem does not erase
that alternative.

## Sources and what changed

The current finite-language predecessor is PR185 at
`276be8154f4e867acc0230466b34d9cb224aacf5`, specifically
`research/whole-repo-closure-20261122/CARRY_LANGUAGE.md` and its
`lean/CarryLanguage.lean`. Its all-length language `1 {2,3}* 2 1` uses debts
`D_p(r)=3^p*r-1` with `p` in `{1,2}`. It correctly leaves larger debts and
the transition from state two through source gap one outside that template.

The global source interface is PR177 at
`a0a0d76f91b4e3846c1b1f0706cad56cb6098317`, particularly
`research/lean-exact-witness-global-20261121/lean/Collatz/BoundedGapCofinal.lean`
and `LowIntervalRefinement.lean`. Its unresolved low-interval program has
initial even exponent in `{1,2,3}` and all supplied odd gaps in `{1,2,3,4}`,
with no length bound. Those are actual complete source certificates, not
arbitrary formal gap words.

The new Lean module imports only the existing `EndpointSteering` module and
the unchanged frozen `Collatz.GapMultiset` foundation already used in PR175.
That foundation is pinned to PR177
`00a611094043afeb256d6532b477c0709e8ed270`; this continuation does not quietly
replace its vendored files by the newer PR177 sources.

## 1. Finite signed trajectories give exact ordinary positive rays

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

Its signed extension has the same formula on integers. Define a separate
arithmetic scaffold

\[
S(z)=\begin{cases}z/2&z\equiv0\pmod2,\\(3z-1)/2&z\equiv1\pmod2.\end{cases}
\]

Thus `T(-z)=-S(z)` on integers. Write `o_k^-(z)` for the number of odd
inputs in the first `k` scaffold steps. For **every** `k>=0` and integers
`v,z`, Lean proves

\[
T^k(2^k v-z)+S^k(z)=3^{o_k^-(z)}v. \tag{1}
\]

The target and scaffold have exactly the same first-`k` odd count. At the
first step their parity agrees because `2v-z` and `z` agree modulo two.
The one-step identity is

\[
T(2v-z)+S(z)=3^{z\bmod2}v.
\]

Induction proves (1), retaining the remaining binary factor at each step.
This proof is valid for positive, zero, and negative `z`; there is no
truncated-subtraction convention hidden in it.

The public theorem `finite_signed_lift` packages the useful ordinary form.
If `n` is a natural number with

\[
n=2^k v+\mathrm{seed},
\]

where `v` and `seed` are signed integers, then

\[
T^k(n)=3^{o_k(\mathrm{seed})}v+T^k(\mathrm{seed}),
\qquad o_k(n)=o_k(\mathrm{seed}). \tag{2}
\]

The left orbit in (2) is the existing ordinary natural-number map, with
Lean proving its equality to the signed extension on natural inputs. If
`n>0`, every target state stays positive.

In particular, a verified negative path from `z<0` to `-1`, with total
shortcut clock `B` and `l` odd inputs, yields the positive ray

\[
x_j=z+2^{B+1}M j,
\qquad T^B(x_j)=-1+2M3^l j,
\]

for all sufficiently large positive `j`. All original parities are actual
ordinary parities, and the endpoint and odd count are exact. This is the
formal arithmetic bridge used by the parallel mixed-modulus potential
argument. Its density/asymptotic conclusions remain separate written
mathematics.

## 2. Every source gap has one exact carry transition

Let a supplied source gap be

\[
3r+1=2^a u,
\]

and represent the original target as an ordinary natural number

\[
n=3^p r-c,\qquad p>0,\quad c\in\mathbb Z.
\]

Put

\[
z=3^{p-1}+c,\qquad
p'=p-1+o_a^-(z),\qquad c'=S^a(z). \tag{3}
\]

Then Lean proves the unconditional finite-path identity

\[
\boxed{T^a(n)=3^{p'}u-c'.} \tag{4}
\]

Indeed,

\[
3^p r-c=2^a3^{p-1}u-(3^{p-1}+c),
\]

so (4) is (1). The actual number of odd inputs in this target segment is
exactly `o_a^-(z)`. Thus neither its clock nor its parity count has been
chosen independently of the original source and target.

The original carry `9r+2` is `(p,c)=(2,-2)`. Its first source gap has `z=1`,
so for every `a` its next state is

\[
(2,-2)\longmapsto(a+1,1). \tag{5}
\]

Thereafter the debt stays nonnegative. This includes every row of the
earlier carry table and its previously unsupported transitions. For example,
state `(2,1)` through gap one goes to `(1,2)`, representing `3u-2`; it
does not pretend to remain in the narrower family `3^p u-1`.

## 3. Whole-word composition retains the literal complete suffix

`run` recursively applies (3). `Enabled(s,front)` asserts that the current
power is positive before each consumed source gap. It has a computable
decidable instance. Reaching power zero is a stopping event, not permission
to apply a formula with a nonexistent factor of three.

For any actual supplied certificate

\[
\operatorname{Certificate}(r,\mathrm{front}\Vert\tau)
\]

and any enabled initial carry `(p,c)`, `complete_word_transport` constructs
an actual odd endpoint `u` with the **unchanged literal certificate**
`Certificate(u,tau)`, and proves

\[
T^{A}(n)=3^{p_f}u-c_f,
\qquad A=\sum\mathrm{front}. \tag{6}
\]

It peels the supplied certificate using `certificate_cons_iff`, not by
extracting a new uncontrolled certificate from a previously proved basin
membership. The companion `complete_word_budget` proves

\[
\boxed{p_f+|\mathrm{front}|=p+o_A(n).} \tag{7}
\]

This is the exact relative odd-count budget: consuming each source odd gap
spends one ternary exponent, while each actual target odd input adds one.

`initial_complete_compiler` applies these results to `9r+2` and every
nonempty supplied complete word. It constructs a nonempty consumed prefix,
a remaining word, and a genuine complete endpoint source. It proves all of
the following together: the source word split, actual positive target path,
literal suffix certificate, nonnegative final debt, equation (7), strict
source-grade decrease, and the explicit alternative

\[
p_f=0\quad\text{or the selected supplied word has been exhausted}. \tag{8}
\]

There is no bound on any word length, gap size, source value, or carry value.
The source-certificate restrictions needed by the low-alphabet program are
therefore preserved rather than replaced by an arbitrary symbolic language.

## 4. The recursive query uses the existing common grade

Deleting any nonempty consumed prefix gives

\[
\Gamma(0;\tau)\prec\Gamma(0;\mathrm{front}\Vert\tau),
\]

in exactly the existing highest-changed-grade multiset order. The tail
cancels; its length and exponents are unrestricted.

The general `interval_query_rule` applies the explicitly displayed lower
grade induction hypothesis when the final actual target satisfies

\[
3^{p_f}u-c_f\le2u+1. \tag{9}
\]

Positivity follows from the original positive target and its actual
trajectory. The simpler `zero_power_query_rule` uses the sufficient guard
`p_f=0,c_f>=0`, which makes the target at most `u`.

These are sound recursive rules. They do not assert the lower-grade
interval hypothesis unconditionally. Also, the initial query `(r,9r+2)`
is itself outside the interval `t<=2r+1`; a larger dispatcher that produces
this carry must account for its relation to its actual parent query and
preserve the parent's available grade. No extra budget is created here.

## 5. The full-closure attempt and the remaining terminal dynamics

The promising proposed completion was to consume the actual cap-four
source certificate until either (9) held or its structure forced a
controlled terminal debt. The compiler now makes that proposal exact. It
also shows why source-word consumption alone is insufficient.

If the whole complete word is consumed, the source endpoint is one and
the remaining original target is

\[
3^{p_f}-c_f>0.
\]

Equation (7) still permits a positive remaining exponent, and no uniform
bound for this terminal target has been proved. The cap-four restriction
does not even keep the carry exponent below four: the actual source 17
has complete word `[2,3,4]`, and the initial target 155 reaches 668 after
nine clocks, represented by `(p_f,c_f)=(6,61)`.

The exponent by itself is also an inadequate stopping rank. The Lean
theorems `terminal_one_fixed` and `terminal_two_fixed` prove, for **every**
`p>0`,

\[
\operatorname{advance}(2,(p,3^p-1))=(p,3^p-1),
\]

\[
\operatorname{advance}(2,(p,3^p-2))=(p,3^p-2).
\]

These represent the already convergent ordinary values one and two.
Adding literal terminal gap-two padding can therefore continue forever
without ever making the carry power zero. A valid stopping argument must
recognize the actual debt/interval condition, rather than demand strict
exponent decrease on every symbolic transition.

More generally, gap-two padding at source one reproduces the actual
ordinary map `T^2` on the remaining target. Treating exhaustion followed
by padding as automatic success would insert the unresolved convergence
claim again. The negative scaffold is a way to compute the exact positive
target; it does not supply an independent source of convergence.

The first missing mathematical assertion is now specific: a total policy
must drive every reachable low-interval carry into an actual lower-grade
interval query such as (9), or supply another sound grade-decreasing
complete-source replacement, while preserving all reachability and
complete-word constraints. That assertion remains open. No axiom or
`sorry` asserts it in this module.

## 6. Actual validation

Development compilation used Lean 4.34.1 with `-j1`, warnings as errors,
and `autoImplicit=false`, against the previously audited project imports.
All 31 public theorem declarations have individual `#print axioms` audits.
Their dependency union is exactly `propext`, `Classical.choice`, and
`Quot.sound`; no `sorryAx`, native decision axiom, or custom Collatz axiom
appears. The module itself needs no Mathlib.

`SignedCarry.receipt.json` and `SignedCarry.log` record that development
execution. A fresh complete-project replay is a separate publication
event, to be recorded by the integrating root agent; this note does not
relabel the development compile as that replay.
