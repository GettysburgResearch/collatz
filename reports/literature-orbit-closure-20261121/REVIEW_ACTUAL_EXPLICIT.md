# Independent review: actual survivor mass and explicit closure target

Reviewer: `/root/literature_symbolic`. Date: 2026-11-21 UTC.

**Verdict: VERIFIED for the written conditional implications at the exact
file contents below. No blocking mathematical issue found.** This review
does not assert the missing transport improvement, universal Collatz, or
independent compiler replay. Per the review assignment, no builds were run
and no reviewed source file was edited.

## Exact scope and pins

Repository HEAD observed while reading:
`7ddfa8c1818fe3ad48789fd4381fba48278f7509`. The reviewed files were working
tree files; their individual content hashes, rather than that HEAD alone,
identify this verdict.

| File | SHA-256 |
|---|---|
| `ActualSurvivorMass.lean` | `72d0015fc8ba05adaa5291f1f5f19a3766c688f985e35016e4403e9820065b98` |
| `ExplicitClosure.lean` | `a5aba915c11ae95e7640970ec1f924a708ec873fd57b69ce9444cad67ac4dbed` |
| `ExplicitSeed.lean` | `c018a47358194358da3fcb4eedc5e5192a803cdbbc37b56965af769fc665d8b4` |

Their directory is `research/literature-orbit-closure-20261121/lean`.
`actual_explicit_review_pins.json` also records Git blob SHA-1s and the
hashes of the inspected `FiniteResolvent`, `BandAbsorption`, and
`HarmonicTransport` dependencies. The actual return-map definitions and
physical hit bridge were read in the resident `SectionDynamics` interface.

## Source identity and absorption

The definition is the actual nonnegative source sum

\[
I_k(y)=\sup_{E\subset\mathbb N\text{ finite}}
\sum_{n\in E}a_n\,
\mathbf1_{\{n\text{ marked},\ R^j(n)\ne1\ (j\le k),\ R^k(n)=y\}}.
\]

Each term retains its **original** weight `a n`. The supremum varies only
the finite set of original sources, not the weights or a replacement
endpoint distribution. `FiniteMass` bounds every such sum by the same
finite `S`; the empty set provides a nonnegative lower bound. Thus the real
conditional supremum is used within its boundedness hypotheses.

For a fixed marked source surviving through `k`, the singleton `{n}` proves
`a n <= I_k(R^k(n))`. `survives_of_not_basin` correctly uses the actual
complete-return hit bridge: a return endpoint equal to 1 is a physical
ordinary Collatz hit. The argument therefore applies to a hypothetical
nontrivial cycle as well as a divergent orbit; injectivity is not required.

There is no hidden resampling, independence hypothesis, generic 2-adic
input, or change from a fixed source to changing finite witnesses.

## Finite budget and the exact conditional deduction

For fixed endpoint `y`, the budget is

\[
B_k(y)=\sum_{r=0}^k c_{k-r}2^{-r}I_{k-r}(y),\qquad
c_j=\frac1{(j+1)(j+2)}.
\]

The endpoint is frozen throughout this sum. Earlier fibers may contain
different original sources. It would be incorrect to describe these as
the mass of one source along its moving endpoints; the proof makes no such
claim. The unproved transport inequality is exactly the relation required
between the frozen-endpoint fibers.

The inspected finite coefficient estimate gives
`B_k(y) <= 8*c_k*S`. Combining it with
`c_0*I_k(y) <= L*B_k(y)` and the singleton source bound yields

\[
(k+1)(k+2)a_n\le16LS.
\]

The coefficient-ratio inequality and the finite geometric-growth sum
support this constant and order. No infinite summation interchange is
used.

## Explicit seed and quantifiers

`ExplicitSeed` supplies the fixed choice
`a_n = c_n` and finite total budget `S=1` by telescoping. Every original
marked source has strictly positive weight. The unconditional baseline
comes solely from retaining the depth-`k` term of the budget:

\[
\tfrac12 I_k(y)\le\tfrac{(k+1)(k+2)}2 B_k(y).
\]

The closure theorem assumes the genuinely additional statement

\[
\forall\varepsilon>0\ \exists k\ \forall y:\quad
\tfrac12 I_k(y)\le\varepsilon(k+1)(k+2)B_k(y).
\]

For a fixed hypothetical bad marked source, choose
`epsilon = c_n/32`. At the selected `k`, the singleton bound gives
`Q*c_n <= Q*c_n/2`, where `Q=(k+1)(k+2)>0`, a contradiction. This is a valid
implication to universal Collatz through the proved marked-section bridge.

The **same selected depth must work for every endpoint**. Swapping
`exists k, forall y` to `forall y, exists k` would not support this proof,
because the relevant endpoint itself depends on `k`. The inequality is
required for this one explicit fixed seed; it is not stated for every
possible input distribution.

The baseline is proved; its arbitrarily small relative improvement is
not proved or implied by it. No converse is claimed. The terminating-shift
example in `FiniteResolvent` correctly cautions that a uniform
subquadratic improvement need not follow from termination for a general
map.

## Nonblocking wording qualification

The general `saving` premise in `ActualSurvivorMass` is
`forall epsilon>0, exists k`, without a cofinality clause. It allows a
finite depth with zero transport bound, which would itself force uniform
absorption. Calling these "selected depths" is exact; saying an
unbounded subsequence is required would be stronger than the formal
hypothesis. This does not affect the proof.
