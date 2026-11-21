# Unbalanced correction synthesis: exact normalization and the remaining selector

**The full closure theorem remains unproved.** This route tried to escape the
balanced-return restriction by allowing both target odd rank and target clock
to change. The completed Lean component makes the resulting correction
calculus exact, proves all positive ordinary guards from one affine identity,
and identifies what changing those two budgets can and cannot accomplish.

The source is [Descent/Correction.lean](../lean/Descent/Correction.lean).
It builds in Lean 4.34.1 using only the enclosing dependency-free project.
There are no admitted proofs or custom axioms. The nine printed principal
axiom lists contain only propext, Classical.choice, and Quot.sound.

## The arbitrary-budget target equation

For a supplied source certificate write

\[
2^A=3^R n+B.
\]

A target certificate for \(5n\), with arbitrary proposed rank \(P\), clock
\(D\), and correction \(C\), must satisfy

\[
2^D=3^P(5n)+C.
\]

The kernel proves the exact equivalence

\[
\boxed{
3^R C+5\,3^P2^A
=3^R2^D+5\,3^P B.
}
\]

This form allows the target rank and clock to increase or decrease and uses
only natural-number equalities. It avoids a hidden sign or division
assumption in the often-used parametrization \(P=R+s,\ D=A+d\).
The specialized identity for nonnegative \(s,d\) is also proved.

This is an exact necessary and sufficient equation for the proposed
correction, not an assertion that the correction belongs to the positive
word grammar.

## One affine identity supplies every ordinary guard

For a positive exponent word \(w=(a_1,\ldots,a_p)\), define

\[
L(w)=\sum_i a_i,\qquad
B([])=0,\qquad
B(a::w)=3^{|w|}+2^aB(w).
\]

For natural \(n,q\), with \(q\) odd, the theorem equation_iff_path states

\[
2^{L(w)}q=3^{|w|}n+B(w)
\quad\Longleftrightarrow\quad
\text{the word }w\text{ is an exact positive odd Collatz path from }n\text{ to }q.
\]

The path relation requires positive exponents, odd source and target at every
step, and the exact equality \(2^a q=3n+1\). Oddness also supplies positivity.
The proof derives each intermediate integral quotient from coprimality of
powers of two and three. Parity of the remaining correction then proves
that the extracted exponent is exact.

The theorem equation_clock_replay connects the path to the original
shortcut map: exactly \(L(w)\) ordinary shortcut steps reach \(q\).
certificate_sound specializes the endpoint to one and proves the
repository's actual Basin n proposition.

Thus a candidate synthesis need not carry separately assumed inverse
divisibility guards. A positive exponent word and one checked natural-number
equation suffice. This integrality principle is already used in written
proofs in the repository; the present file is a kernel-checked general
implementation, not a claim of first discovery.

## Budget changes do not create a local control

Suppose a prospective correction head is

\[
B=3^r+2^a C,\qquad A=a+d.
\]

With the appropriate tail parity, head_forced proves that this head forces
one and only one actual next odd state \(q\):

\[
2^a q=3n+1,\qquad
2^d z=3^r q+C.
\]

Consequently head_budget_independent proves that any two valid
normalizations starting at the same \(n\), regardless of their proposed
rank, clock or terminal endpoint, must decode the same first exponent.
prefix_budget_cancel proves the analogous cancellation after an arbitrary
supplied physical prefix. first_path_unique proves uniqueness of the
complete first-hit word when one exists.

This does **not** show that unbalanced synthesis cannot succeed. It shows
that the budgets are search bounds, not controls that can steer the next
positive Collatz step. A proof of a uniform successful choice of budgets,
or a different nonhomogeneous certificate architecture, could still
complete the intended argument. No such choice theorem was obtained here.

A finite control uses the known pair \(17,85\): its first-hit words are
\((2,3,4)\) and \((8)\). Therefore nonnegative rank overhead is not a
complete parametrization of *first-hit* outputs. Padding the \(1,2\) cycle
allows non-first-hit outputs of larger rank; the formal statement does not
claim otherwise.

## Scope relative to the latest sources

The targeted comparison used:

- PR173, a09eb47197cd99f218b3fa013c681df65ea0f69a,
  research/lean-shell-cover/README.md and the definitions in
  ShellCover.lean. Its unproved later-time survivor estimate was not
  imported as a theorem.
- PR172, b22d94240f3d44a04231508e5dfe9a4947a57125,
  UNBOUNDED_FIRST_ONE_TRANSPORT.md, especially the hard negative-offset
  boundary. Its general normalizing freedom does not supply the unknown
  target continuation.
- PR146, f431078244e868dc699fad011044f0d5e7f76437,
  WHOLE_INTERVAL_SYNCHRONIZATION.md. Its representatives still depend on
  a freely selected input lift, whereas the target in the present problem
  is one fixed ordinary integer.
- The core basin definitions and elementary moves are inherited from
  PR174, 7034109ed60a26bc49824e1ed43c239ceca81194, through the enclosing
  project's pinned Collatz sources.
- Complete balanced correction recognition and the \(17,85\) control
  already occur in PR168, e4599b32e4b1a955ac9315d46782d4ad6a5db96c,
  FIVE_RETURN_LANGUAGE.md; fixed-prefix decoding also occurs in PR169.

The new formal component is a reusable arbitrary-budget correction kernel.
It neither supplies a successful total compiler nor proves a new unconditional
convergence family. It should support a genuine selector argument if one is
found, rather than being counted as that missing argument.
