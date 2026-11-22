# Scoped review of the original-rank selector attempt

Date: 2026-11-22.

**Verdict: VERIFIED in the requested algebraic and logical scope,
retaining the displayed imported certificate and rank hypotheses.**
No substantive correction was identified. The reviewed file reports an
unsuccessful proof attempt; it does not prove or claim nontermination.

Reviewed artifact:
research/lean-global-closure-20261121/central/ORIGINAL_RANK_SELECTOR_ATTEMPT.md

SHA256:
3b08d87f8eb0b403cef7f4d40ae961260c19f79b6a6feac9efe2560ba2640c93

Publication-byte update: the original reviewed scratch artifact had SHA256
2c8b1810ff04d35c04d63f0d09d38cdd2b6e6d5b79082ef1cf0f83000661f21e.
An exact byte comparison confirms that the delivered file changes only
the provenance sentence from "The copied new statement files and their
exact hashes are recorded in sources.json." to "The upstream inputs and
their exact byte hashes are recorded in SOURCE_SNAPSHOT.json."
The Markdown code formatting and line break were included in that
comparison. No mathematical text changed. The prior mathematical review
below is retained without repeating its checks.

I reconstructed the calculations below, read the cited original-floor
and mixed-grade statements, and inspected the two named high-gap
dispatcher conclusions at PR177 commit
8ef9bf0d828fc533721dee1f90c5d78fac80ad39. No legacy build was replayed,
and this receipt makes no new Lean-verification claim.

## 1. Complete-word identities and the actual carry recurrence

The source recurrence \(3q_j+1=2^{a_j}q_{j+1}\) gives
\(C_{j+1}=3C_j+2^{A_j}\), hence
\[
2^{A_j}q_j=3^j q_0+C_j.
\]
At the supplied endpoint one, this is exactly
\(3^m q_0+C_m=2^{A_m}\), including its congruence modulo \(3^m\).
The note retains the positive odd intermediate states; it does not
mistake this necessary congruence for a sufficient complete-word test.

At one source edge, put \(z=3^{p-1}+c\). The actual current target is
\[
y=2^a(3^{p-1}q')-z.
\]
The imported signed complement identity therefore gives
\(T^a y=3^{p-1+o}q'-S^a z\), with the same actual target
parities. This proves the displayed \(p'\) and \(c'\).
Dividing by \(3^{p'}\) gives
\[
x'=\frac{1+3x}{2^a}-\frac{B}{2^a3^{p'}},
\qquad
q'-x'=\frac{3(q-x)}{2^a}+\frac{B}{2^a3^{p'}}.
\]
The signs are correct. Discarding the nonnegative correction in the
second formula gives a lower bound, not the upper bound needed for
target descent.

For the specified initial pair \((p,c)=(2,-2)\), one has \(z=1\)
and \(S(1)=1\). Thus \(o=a\) and the first update is
\((a+1,1)\), as stated. Subsequent debts stay nonnegative while this
compiler continues. Summing the power recurrence and the actual target
affine identity gives all three equations in (7), including
\[
2^{A_j}c_j=3^{p_j}C_j+3^{O_j}c_0-H_j.
\]

## 2. The original-target floor

The cited source-selection statement supplies the complete source
and its entire future floor. Since \(N\equiv3\pmod4\),
\(L=(N-1)/2\) is odd and \(L>1\). An orbit remaining at most \(L\)
cannot visit \(L\), because its next odd shortcut would exceed \(L\).
For every retained odd endpoint \(q_j\), its next shortcut is
therefore at most \(L-1\). Consequently
\[
3q_j+2\le2L-1=N-2<N.
\]
The padding \(2^f q_{j+1}\), \(f<a_j\), is likewise a real state
of the just-consumed source segment. The warning against funding it
from an earlier discarded gap is correct.

Using the accumulated actual target identity, descent below the
original target is exactly
\[
3^{O_j}y_0+H_j<2^{A_j}N.
\]
Replacing \(N\) by an enlarged current carry would weaken the desired
claim. The note keeps that distinction throughout.

## 3. Variable-run exchange and grade comparison

For the supplied segment \([3]++[2]^k++[4,b]\), each \(v_i\)
is \(1\bmod4\), so \((v_i+1)/2\) is positive and odd.
The five displayed edge types in the replacement follow by direct
substitution. In particular its last edge is exactly
\[
3(4a+1)+1=2^{b+2}z,
\]
with odd \(z\); no extra factor of two is suppressed. The case
\(k=1\) also works, with the interior repeated list empty.

Under the pinned grade convention \(a\mapsto2a\), retaining the
same powered-source exponent and literal tail cancels the common
multiset of \(k\) fours and one eight. The remaining comparison is
precisely
\[
\{6,2b\}\quad\hbox{versus}\quad\{2,2b+4\}.
\]
For \(b=1\) these multisets agree and the source increases. For
every \(b\ge2\), \(2b+4>\max(6,2b)\), so the highest changed grade
increases. The equal-grade source tie cannot license that move.
The alternative gap-three exit gives \(2a+1\), rather than \(a\);
copying the old tail onto it would be invalid.

The inspected high-gap theorem bounds inserted gaps by four and
proves a decrease relative to the intermediate high-gap certificate.
It supplies no bound on their multiplicities relative to the original
bounded-four certificate. The note correctly does not compose those
two grade comparisons without a further argument.

## 4. Logical conclusion

The terminal equation \(y_m=3^{p_m}-c_m\) is not treated as an exit,
and the note explicitly distinguishes arbitrary such representations
from those reachable by this compiler. It identifies the missing
universal success inference without asserting that any actual target
evades all guards forever.

Failure to prove this selector is therefore not used as evidence of
a divergent Collatz orbit, an impossible universal selector, or the
failure of a different arithmetic route. The scope and unsuccessful
status are stated accurately.
