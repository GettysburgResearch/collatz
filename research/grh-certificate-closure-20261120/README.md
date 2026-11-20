# Unbounded certificate transport and the precise GRH interface

**Collatz remains OPEN, including under the GRH hypotheses investigated
here.** This packet contains proposed elementary results, explicitly
source-qualified analytic inputs, and completion attempts with their
first unsupported steps recorded. It does not claim that GRH cannot imply
Collatz through a different argument.

The source refresh includes PR146 at
`e238c63a5d57f96bb063b7472498d1977df51951` and the newly available PR163 at
`051237135a34ae7d4b973ee5fcf5da04ded6f0fc`. The
[source ledger](SOURCES.md) distinguishes direct overlap checks from new
proofs and from quoted results. No accepted baseline result is changed.

## The positive certificate result

PR157 reduces Collatz to the physical implication

\[
x\text{ odd},\quad 3\nmid x,\quad x\in C
\quad\Longrightarrow\quad 5x\in C,
\]

where C is the actual basin of 1. This formulation is useful because its
antecedent can come with a complete finite certificate. A closing route
would transform every such certificate into a certificate for 5x.

The [ladder theorem](FIVE_CERTIFICATE_LADDER.md) gives one unbounded part
of that transformation. With `I_a(q)=(2^a q-1)/3`, for r>=2 and b>=4,

\[
5I_2^r I_b(q)=I_4 I_2^{r-2}I_3 I_{b-3}(5q).
\]

Every inverse on the right is proved integral, positive and odd when the
supplied source word is legal. The corresponding ordinary paths have the
same shortcut clock. The r=1 case is explicitly credited to PR162.

The local transformation composes into a complete compiler for every
first-hit exponent word in the language `(2+[4,infinity))*`. Here `2+`
means a nonempty run of letters equal to two. If the original certificate
has odd count p and shortcut clock N, the target has exact first-hit count
p+1 and clock N+4. The compiler consumes the known finite source word,
so this is not termination inferred from a finite search of the target.
Closed families realize every source odd rank at least two.

The initial source cylinders are disjoint, have relative density 1/24
among odd ternary units, and transport to a smaller certified antecedent
q<=x/7. Their union is not all sources. A valid certificate outside the
language returns `UNRESOLVED`; a malformed certificate is rejected.

All those cylinders already admit a simple ordinary height decrease from
5x. The added result is transport to the *specific* endpoint 5q and the
complete compiler on the stated language. Knowledge that x reaches 1
does not give convergence of every smaller positive integer.

## A positive analytic consequence on the whole ladder family

The [renewal theorem](LADDER_RENEWAL.md) connects the ladder to the energy
approach in the new PR163. For any ordinary-invariant metric label f, let
E(X) sum `d(f(5x),f(x))/x` over odd ternary units x<=X. Let R(X) be the
same sum over the inputs outside the ladder cylinders. Then

\[
E(X)\le R(X)+\frac{16}{21}E(X/7),\qquad
E(\infty)\le\frac{21}{5}R(\infty)
\quad\text{if }R(\infty)<\infty.
\]

The same complete family also contracts with the subcritical weight
`x^(-.84)`, with an exact rational coefficient `81744/82925<1`.
This uses the zero defect at endpoint one to sharpen the inverse-height
bound for every remaining endpoint; no assumption of its convergence is
made. At either exponent, finite energy on the full domain is equivalent
to finite energy on the uncovered complement.

The proof sums the complete inverse fibers, keeps their unit guards and
uses finite cutoffs before subtracting energies. It extends PR163's
single-cylinder partial renewal to every ladder cylinder. The complement
still has no established finite energy. This does not fill the analytic
gap in PR163's all-source five-to-tripling energy comparison.

## What assuming GRH actually helped with

[GRH_INTERFACES.md](GRH_INTERFACES.md) gives a concrete conditional
construction. Every odd binary residue modulo `2^H` has a prime realizer
smaller than `2(2^H H log2)^2`, by a standard GRH least-prime theorem.
Thus every finite odd-starting parity word has a prime realization with
at most `2H+2ceil(log_2 H)+1` bits. In particular there are arbitrarily
large primes with explicitly growing H-step prefixes.

This selects a new ordinary source with the same finite prefix. It does
not select an ancestor of a supplied target, or preserve the original
source's unknown all-time component. The distinction survives the
stronger Dedekind/Artin versions of the GRH hypothesis unless a suitable
source-preserving arithmetic encoding is exhibited.

An exact obstruction makes the issue sharper. At a prescribed ternary
level e, a one-step inverse core `(2^a n-1)/3^e<n` needs
`a<e log_2 3`. If `n=-1 mod3^e`, divisibility instead forces
`a=3^(e-1) mod2*3^(e-1)`. For e>=3 these demands are incompatible.
The explicitly convergent depth-one sources

\[
n_E=(2^{3^E+1}-1)/3
\]

satisfy this obstruction simultaneously at every prescribed level
3<=e<=E. Having a complete source certificate does not repair that
particular inverse recipe. Higher actual stripping, longer inverse
words and forward excursions are deliberately left possible.

The same note reconstructs the elementary fact that an eventually
periodic ordinary-invariant label is constant. A fixed finite Dirichlet
character expansion is therefore already too rigid for a nonconstant
component label; GRH cannot stand in for the missing controlled
approximation with growing conductors.

## Completion attempts and the remaining mathematical step

The certificate compiler does not handle arbitrary letters one or three,
or even every one-letter convergent source. The rank-one shifted-power
obligation was already identified in PR157. Processing an inverse
denominator can leave a nonzero signed offset and a new shifted-power
orbit. The supplied certificate has then been consumed without proving
the companion terminates. No induction is asserted across that gap.

[UNIFORM_J_COMPLETION_ATTEMPT.md](UNIFORM_J_COMPLETION_ATTEMPT.md)
records the parallel rigidity attempt. It distinguishes a bare global
cutoff on high-exponent laws from PR146's stronger eventual availability
of each fixed small exponent. It gives legal adjacent equality on a
restricted progression and a certified 43-move descent at J=8. The
bounded searches do not cover all sources.

An application of the cited Evertse--Schlickewei--Schmidt theorem also
shows that a fixed target, bounded ternary core and bounded inverse odd
depth admit only finitely many such ancestors. A repair reaching
arbitrarily high ternary levels while preserving those first two bounds
must let its inverse depth grow. This is a source-qualified finiteness
result, not a computed maximum height or an exclusion of adaptive paths.

The full route remains: transform every supplied terminating certificate
with a justified terminating recursion, or prove the uncovered invariant
energy finite, or supply a different complete descent argument. Neither
GRH prime selection nor the proved restricted transformations provides
that all-source step.

## Review and reproduction

The [review guide](../../reports/2026-11-20-grh-closure/README.md) records
frozen source hashes, independent internal mathematical reconstructions,
finite replays and actual clean-checkout validation. Those checks are not
human referee acceptance, formal verification or a proof of Collatz.
No Lean build of the prior PR146 files is claimed for this packet.
