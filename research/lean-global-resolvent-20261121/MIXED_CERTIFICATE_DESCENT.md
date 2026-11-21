# Combining certificate consumption and longer replacements

**PROVED IN LEAN:** one common well-founded order, a sound finite-rule induction
kernel, and its exact applicability to two infinite paired descent families.
**OPEN:** a sound rule covering every obligation reachable from the full theorem,
including the terminal multiplier families.

The ordinary map is `T(n)=n/2` for even `n` and `(3n+1)/2` for odd `n`.
The standalone Mathlib file [MixedCertificate.lean](mathlib/MixedCertificate.lean)
defines this map and `Basin n` as an actual finite iterate reaching one. Its
definitions agree with the core project, but it does not import the core's
compatibility shim for `Nat.strong_induction_on`, which conflicts with Mathlib.

## A common order that tolerates longer certificates

Associate a supplied finite ordinary certificate with the multiset of its
states, counting multiplicities. Use the **existing Dershowitz–Manna multiset
order** induced by the ordinary order on natural numbers. Mathlib supplies
its well-foundedness; this work does not claim a new ordering theorem.

If an old prefix has bag `O`, a replacement has bag `N`, and the unchanged
suffix has bag `S`, then

\[
 N+S\prec O+S
\]

whenever `O` is nonempty and every entry of `N` is smaller than an entry of
`O`. No bound is required on the number of replacement entries. Two useful
cases are established explicitly:

1. **Consume a prefix:** `N` is empty. The remaining source value may be
   larger than the original value; removing the used states still decreases
   the multiset.
2. **Replace a prefix:** every inserted state is below a single removed
   state. The new certificate may have many more steps than the old one.

Thus a proof program can use both kinds of moves without asserting that
ordinary height decreases along every source orbit, or that certificate
length decreases under every replacement.

`close_of_complete_rules` formalizes the resulting induction. A rule has
finitely many child obligations, a proof that each child's measure decreases,
and a proof reconstructing the parent goal from the child goals. **The premise
that every state has such a rule remains an explicit theorem argument.** It
is neither an axiom nor a verified property of an all-input Collatz program.

## Exact paired replacements

The two arithmetic families come from
[PR169, frozen at `6cb9bfdc828f91576066b0e4a099d47d8144e915`](https://github.com/GettysburgResearch/collatz/blob/6cb9bfdc828f91576066b0e4a099d47d8144e915/research/certificate-renewal-20261121/C5_CERTIFIED_BYPASSES.md).
The new contribution here is their Lean proof and their compatibility with
the same order as source consumption. Write `X(k)=128k+1`, `Y(k)=64k+1`.
For every natural `t`:

| Family | Parent `k` | Child `k'` | Upper clocks to one common endpoint | Child lower clock to `Y(k)` |
|---|---|---|---|---|
| A | `1889568t+1686382` | `524288t+467911` | 11 and 25 | 14 |
| B | `1889568t+1196494` | `1048576t+663969` | 11 and 26 | 15 |

The file proves the following genuine implication in each family:

\[
 [X(k')\in C\Rightarrow Y(k')\in C]
 \quad\Longrightarrow\quad
 [X(k)\in C\Rightarrow Y(k)\in C].
\]

The upper paths reach the same positive ordinary endpoint. The lower path
from `Y(k')` reaches `Y(k)` itself. Consequently an existing upper certificate
can be replaced before its common suffix, and the child implication supplies
a lower certificate for the parent target.

Crucially, **every inserted ordinary shortcut state**, including even states,
lies below the original parent `X(k)`. The bounds are:

| Family | Parent initial state | Maximum inserted upper-prefix state | Strict difference |
|---|---|---|---|
| A | `241864704t+215856897` | `100663296t+89838914` | `141201408t+126017983` |
| B | `241864704t+153151233` | `201326592t+127482050` | `40538112t+25669183` |

The endpoints are excluded from both stored prefixes and belong to the common
suffix. The suffix may be arbitrarily long or have arbitrarily high states;
it cancels in the multiset comparison. The statements
`a_source_certificate_decreases` and `b_source_certificate_decreases` hold
for **every** suffix bag and every natural parameter, not a bounded sample.

The finite tables are checked by `decide` after a general affine checker has
been proved sound. A table entry `(a,b)` denotes `a*t+b` for all `t`. The
checker proves parity and the exact numerator equation at each ordinary
step. There is no unproved bridge from Python output to a universal theorem,
and no use of `native_decide` or an additional computation-trust axiom.

## What the full-proof attempt still needs

The order removes a conflict between two already useful types of recursive
move. It does not furnish a missing move. The exact transport formulas in
[EXACT_FORWARD_FLOOR.md](EXACT_FORWARD_FLOOR.md) show why consuming only a known
source is insufficient: the target can retain an unbounded ternary multiplier
when the source reaches one.

The new core module
[MersenneRecursion.lean](lean/Collatz/MersenneRecursion.lean) supplies a real
uniform recursion for part of that boundary:

\[
 \operatorname{Basin}(2^{2r+2}-1)
 \iff \operatorname{Basin}(2^{2r+1}-1),\qquad r\ge0.
\]

It proves the corresponding identity for `3^(2r+2)-1` and `3^(2r+1)-1`
by exact ordinary moves, then transports it through the pinned predecessor
identity. The remaining odd-exponent family and a complete rule selector
are still open. The formal kernel is intended for a selector that supplies
those moves, with every reconstruction and decrease checked.
