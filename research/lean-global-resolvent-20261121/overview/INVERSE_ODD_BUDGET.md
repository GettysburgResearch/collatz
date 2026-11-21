# A sharp lower bound on the odd-step budget of a smaller merger

**Status:** a kernel-checked, finite, all-word arithmetic theorem. It does not
assert universal existence of a smaller merger or prove Collatz. The companion
Lean file formalizes the inverse-word inequality, the actual shortcut-orbit
bridge, and the explicit unbounded family. The final run exited successfully
with warnings treated as errors; all three principal axiom audits contain only
`propext`, `Classical.choice`, and `Quot.sound`.

The shortcut map is

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

## Theorem

Let \(n\ge1\), and let \(j,L\ge0\) satisfy

\[
2^j\mid n+1,\qquad 3^L\mid n-1.
\]

Let \(x\) be a positive ordinary integer and suppose

\[
T^q(x)=T^j(n)
\]

for any finite shortcut clock \(q\). If the path from \(x\) to this endpoint
uses \(a\le j+L\) odd inputs, then

\[
\boxed{x\ge n.}
\]

The backward clock and every run of even steps are unrestricted. Therefore
any genuinely smaller ordinary merger partner at any clock within the initial
all-odd ascent must spend **more than \(L\) extra odd inputs** beyond the
\(j\) odd inputs used by the original source.

The condition applies simultaneously to every
\(0\le j\le v_2(n+1)\). In particular, when \(n>1\), the sharp intrinsic
budget is \(L=v_3(n-1)\): a smaller partner must have
\(a-j\ge L+1\).

## Relation to the earlier result

The proof mechanism is credited to PR146 at
`f431078244e868dc699fad011044f0d5e7f76437`,
`research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md`, final section
“How deep an ordinary path to a smaller representative can have to go.”
That source uses the ordinary comparison center 184 and a special eligible
Mersenne family to obtain the lower bound \(x\ge M/100\) throughout the
ascent, with arbitrary even inverse clocks and odd budget \(j+H\).

The present result uses center 1. It applies to every source satisfying the
two divisibilities and gives the exact bound \(x\ge n\). Thus it excludes
**all** strictly smaller partners inside the budget, rather than only partners
below a fixed fraction of the source. It also does not require the earlier
rank-five certificate eligibility class.

## Proof by comparison of two virtual inputs

The first divisibility gives the exact ascent formula

\[
y_j=T^j(n)=(3/2)^j(n+1)-1.
\]

Reverse the actual path from \(y_j\) to \(x\). Each inverse instruction is
one of the increasing rational affine maps

\[
E(u)=2u,\qquad O(u)=(2u-1)/3.
\]

The actual inverse values are positive integers. Write \(W\) for the
composition of these instructions and \(\lambda\) for the multiplier of
the composite map

\[
G(v)=W\big((3/2)^j(v+1)-1\big).
\]

Thus \(G(n)=x\), and \(\lambda>0\).

First, \(G(-1)\le-1\), because the initial value at \(-1\) is \(-1\),
\(O\) fixes \(-1\), and both inverse maps preserve \((−\infty,-1]\).

Second, \(G(1)\ge1\). Here the initial comparison value
\(2(3/2)^j-1\) can be a dyadic rational, so it would be incorrect simply
to assume the whole comparison path consists of ordinary integers. The
following argument supplies the missing positivity and integrality.

After \(k\le j\) inverse instructions, the comparison value is at least
\[
2(3/2)^{j-k}-1\ge1.
\]
Indeed \(E(u)\ge O(u)\) for \(u\ge1\), and applying \(k\) copies of
\(O\) gives the displayed minimum. Once \(k\ge j\), let \(a_k\) be
the number of odd inverse instructions already used. The difference between
the actual and comparison values is

\[
2^{k-j}3^{j-a_k}(n-1).
\]

This is an integer because \(3^L\mid n-1\) and
\(a_k\le a\le j+L\). The actual value is an integer, so the comparison
value is an integer as well. At each subsequent instruction, a positive
integral input and an integral output remain positive: doubling is immediate,
and an integral value of \((2u-1)/3\) for integer \(u\ge1\) is at least
one. This proves \(G(1)\ge1\).

As \(G\) is affine,

\[
2\lambda=G(1)-G(-1)\ge2,
\]

so \(\lambda\ge1\). Consequently

\[
x=G(n)=G(1)+\lambda(n-1)\ge1+(n-1)=n.
\]

All quantities in the final merger are ordinary integers. The virtual dyadic
comparison only proves the inequality; it is not supplied as an ordinary
ancestor or as a convergence witness.

## Independent budgets and an explicit large family

The moduli \(2^J\) and \(3^L\) are coprime. The Chinese remainder theorem
gives an infinite arithmetic progression of positive \(n\) satisfying

\[
n\equiv-1\pmod{2^J},\qquad n\equiv1\pmod{3^L}.
\]

For every such \(n\), the conclusion holds at **every** forward clock
\(j\le J\). Thus the available early forward window and the necessary
excess odd budget can both be made arbitrarily large, independently.

There is also a simple Mersenne subfamily. For \(H\ge0\), take

\[
e=2\cdot3^H+1,\qquad n=2^e-1.
\]

The elementary lifting identity
\(3^{H+1}\mid4^{3^H}-1\) gives
\(3^{H+1}\mid n-1\). Throughout its entire \(e\)-step initial ascent,
any smaller merger therefore needs at least \(H+2\) extra odd inputs.
The proof of the lifting identity is induction using
\(X^3-1=(X-1)(X^2+X+1)\), since the second factor is divisible by three
when \(X\equiv1\pmod3\).

## The same obstruction occurs inside the new marked band

Fix any \(J\ge1\) and \(L\ge0\), and put \(M=2^J3^L\). The two
congruences above determine a residue class modulo \(M\). For every
sufficiently large octave index \(d\), choose its first representative
\(n\ge2^d\). Then

\[
2^d\le n<2^d+M,
\qquad
(d+1)(n-2^d)<(d+1)M\le70\,2^d.
\]

The last inequality holds eventually because \(M\) is fixed. Also take
\(d\) large enough that \(M\le2^d\), so
\(\lfloor\log_2 n\rfloor=d\). The congruence modulo \(2^J\) makes
\(n\) odd. Hence \(n\) is in the exact constant-70 marked section, and
it has the all-word merger obstruction simultaneously at every \(j\le J\).

Thus each pair of prescribed budgets occurs among marked sources in **every
sufficiently large octave**. This is an elementary written CRT corollary of
the formal theorem; the current Lean file does not import the section's
logarithm definition or formalize this asymptotic CRT selection.

The role of this statement is specific: being in the shrinking band does not
supply a uniform upper bound on the odd-count surplus needed for a smaller
merger during an initial ascent. For example, PR184's even obstruction-family
repair uses a clock beyond that initial ascent, which is consistent with the
present theorem.

## What this says about the global constructive attack

PR184's exact rebasing theorem now gives a sound algebraic way to move beyond
the binary horizon. A universal source-lowering compiler must still produce
an ordinary partner below the **original** source. The theorem here shows
that no uniformly bounded excess-odd budget can do this while staying inside
the source's initial all-odd ascent, even if its search includes every inverse
word and permits arbitrary even clocks.

The theorem does not exclude a successful method. It identifies two concrete
resources that such a method must control: it may advance beyond the initial
ascent, or it may pay an unbounded odd-count surplus. It supplies no monotone
quantity guaranteeing that either choice eventually produces a saving. That
existence and repayment step remains unsupported in the present full-theorem
attempt.

## Formal interfaces and reproducibility

`InverseOddBudget.lean` is self contained over mathlib. Its principal
interfaces are:

- `no_smaller_inverse_word`: every integral inverse word within the budget
  has source at least the original source;
- `smaller_merger_odd_surplus`: the exact actual shortcut-orbit consequence,
  with both clocks and the partner quantified;
- `mersenne_merger_odd_budget`: the explicit unbounded Mersenne family, over
  its entire ascent;
- `sharp_small_example`: `27` reaches `31` with exactly two odd inputs, while
  `v_3(31-1)=1`, so the strict generic threshold is attained.

The file proves the shortcut trace reconstruction and rising-endpoint formula
internally. It does not postulate an inverse-word legality theorem or a
Collatz convergence property. The virtual-integrality lemma explicitly checks
when the comparison path becomes ordinary; no dyadic rational is silently
used as a positive integer.

The intended toolchain is Lean 4.34.1 with mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. From that built mathlib checkout,
run:

```sh
lake env lean -j1 -DwarningAsError=true /absolute/path/InverseOddBudget.lean
```

The source prints the axiom dependencies of its three main theorems. The
execution receipt records the actual source hash and process exit code; the
log records those audits. The marked-band CRT consequence above is a written
corollary and is outside the current Lean theorem list.
