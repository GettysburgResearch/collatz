# Global forcing attempts: carry transport, joint renewal, and shifted rank

**Collatz remains unresolved.** This pass pursues the current physical
five-closure, energy, and arithmetic gaps with three independent authors
and cross-reconstruction. It produces an unbounded carry compiler, a
joint positive renewal on a larger domain, and an effective cycle ceiling
controlled by shifted multiplicative rank. It also proves why a specified
finite-terminal compiler architecture cannot be extended to all inputs.

The [source comparison](SOURCES.md) records the inspected GitHub heads,
including the publication refresh of PR146 and new PR167--169. These are
proposed research results with scoped internal reviews. The arithmetic
theorem retains its named external inputs; none of the results is
advertised as a full proof. The short four-step identity below also
appears in concurrent PR168 and PR169. PR168's general balanced-word
recognizer contains our concrete compiler as a specialization; our
contribution is the explicit carry family, its ordinary all-rank
realization, and its use in the coupled renewal.

## 1. A nonzero carry transports arbitrarily long runs

Use the ordinary shortcut map T and its accelerated odd map U. Exponent
words list the exact valuations of `3n+1`. Define

\[
E=(2,1,1,1,2,1,7),\qquad F=(3,6,1,2,1,1,1).
\]

The first paired words send `(x,5x)` to `(y,5y+4)`. The offset four
survives every further valuation-one step. An exact two-step exit removes
it. Consequently, for every `r>=0,b>=2`, the legal source word

\[
E,1^r,3,b
\]

has the target word

\[
F,1^r,4,b-1
\]

on `5x`, ending at the corresponding `5q`. Both use `r+9` odd inputs and
`r+b+18` shortcut steps. Here `1^r` means r repetitions of the exponent
one, not an arithmetic power.

This supplies a physical identity for **arbitrarily long actual runs**.
The proof gives explicit positive ternary-unit first-hit examples at
every source rank at least nine. A separate block, also independently
present in PR168 FR2 and PR169 FW3(B),
`(1,1,1,b) -> (1,2,5,b-5)`, `b>=6`, covers `271 mod512` and reduces the
comparison to a smaller actual endpoint.

Together with the explicitly credited PR166 ladder, these blocks give a
compiler on their concatenation language. PR168 already supplies a more
general recognizer for all balanced affine returns. Our concrete compiler
consumes a supplied finite first-hit certificate, proves every target step,
and adds exactly one odd
input and four shortcut steps. Unsupported valid inputs return
`UNRESOLVED`. No source-height decrease is claimed for unrestricted carry
blocks; some really expand.

[Statement and proofs](certificates/CARRY_COMPILER.md) ·
[Executable compiler and replay](certificates/check_carry_compiler.py)

## 2. Endpoint congruences preserve contraction across all three families

For any ordinary-invariant metric label f, define the physical five defect
and its positive finite-cutoff energy by

\[
e(x)=d(f(5x),f(x)),\qquad
E_s(X)=\sum_{\substack{x\le X\\x\text{ odd},\;3\nmid x}}
\frac{e(x)}{x^s}.
\]

Take the disjoint union of the old valuation-two ladder, the new
`271 mod512` block, and **every** new carry block with `b>=r+2`. Write
`Q_s(X)` for the same energy on the entire remaining complement.

The new proof obtains

\[
\boxed{E_{21/25}(X)\le Q_{21/25}(X)
+\frac{248549}{248775}E_{21/25}(X/6),}
\]

\[
\boxed{E_1(X)\le Q_1(X)+\frac45E_1(X/6).}
\]

The shared endpoint matters. At fixed q, inverse fibers in different
families obey compatible congruences modulo27; their separate worst cases
cannot all occur there. For the unbounded carry family, the same
congruence makes the required exit exponent periodic modulo18, and the
entire sum over run lengths is a finite rational expression times a
geometric tail. All power comparisons at `21/25` are exact integer
inequalities.

Both displayed coefficients are below one. Thus full energy is finite
exactly when the corresponding uncovered energy is finite, with explicit
constants. **There is still no absolute finite bound for Q.** The existing
PR163 five-to-tripling comparison and its stated rigidity inputs do not
supply that missing bound. No fresh-residue or independence assumption is
inserted after a return.

[Joint renewal proof](energy/COUPLED_RENEWAL.md) ·
[Exact energy and phase checks](energy/check_renewal_phase.py)

## 3. Shifted rank gives effective cycle finiteness without known generators

Let `m=n+1`, and call an odd edge a defect when `v_2(3n+1)>=2`. Suppose
its two shifted endpoints lie in a union of k cosets of one multiplicative
group of positive rationals of rank at most r. The new source-qualified
bound on the number of distinct such ordinary edges is

\[
D(r,k)=k^2\,2^{4\cdot18^9(r+1)}.
\]

The generators, their heights and prime factors, and the coset
representatives are unrestricted. The proof uses the shifted equation
from PR161 and the general-rank theorem of Evertse--Schlickewei--Schmidt.
It does not substitute the number of primes for multiplicative rank.

A reconstructed classical cycle estimate gives, for d defects in a least
period,

\[
N,\ \log_2\max_i(n_i+1)<256d2^d.
\]

Therefore `d<=D(r,k)` gives a computable height ceiling for **all** cycles
with that shifted rank/coset budget, before the group is known. The
resulting finite decision procedure is astronomically impractical and
was not run. Classical fixed-block cycle finiteness and the external
logarithmic-form estimate are credited explicitly.

An elementary additional clause excludes every nontrivial cycle with
absolute shifted rank one. A fixed ordinary nonperiodic orbit, if one
exists, must have unbounded shifted rank. There is no opposing upper
bound: an explicit inverse tower already gives known convergent inputs
whose shifted ranks are unbounded as the source varies.

[Arithmetic proof and limits](arithmetic/SHIFTED_RANK_COMPACTNESS.md) ·
[Exact finite controls](arithmetic/check_shifted_rank.py)

## 4. A complete compiler needs a different kind of transition

For a convergent source, let `H(n)=tau(n)-2 omega(n)`, its first-hit
shortcut clock minus twice its odd count. The existing stopping-grade
mechanism implies that every pair of native affine paths transporting
`(x,5x)` to `(q(x),5q(x))` on a whole progression preserves
`Delta(x)=H(5x)-H(x)`. This includes reverse ordinary edges and the new
carry blocks, whose final endpoints are proportional again.

For the always-certified rank-one sources `x_a=(4^a-1)/3`, with
`a>=2` and `3` not dividing a, a successful target certificate would imply

\[
2^{\Delta(x_a)}<\frac{20}{3}\left(\frac56\right)^{2a-1}.
\]

Hence no dictionary of those rewrites, however large or adaptively
selected, followed by a terminal library with phases bounded below, can
cover all supplied certificates. Every finite certified terminal library
has such a bound. The argument invokes target convergence only after a
hypothetical successful certificate establishes it.

This is an application and extension of the existing phase mechanism to
the current compiler architecture. It leaves inhomogeneous terminal
comparisons, singleton certificates, and independently justified
unbounded terminal families available. Its known-good examples do not
refute a possible energy argument on genuinely failed pairs.

[Exact theorem and source comparison](energy/TERMINAL_PHASE.md) ·
[Independent phase review](arithmetic/TERMINAL_PHASE_REVIEW.md)

## The missing global step

The alternatives are now concrete: prove a finite bound for the full
uncovered defect energy; construct an all-input certificate transformation
that escapes the preserved terminal-phase restriction; or derive an
arithmetic constraint incompatible with unrestricted rank creation and
unrestricted positive cycles. The results above do not provide any of
those closing steps. They are alternative approaches, not completed
stages of one nearly finished proof.

Proof reconstruction, finite execution, and repository integrity are
recorded separately in the [review and publication report](../../reports/2026-11-21-global-forcing/README.md).
