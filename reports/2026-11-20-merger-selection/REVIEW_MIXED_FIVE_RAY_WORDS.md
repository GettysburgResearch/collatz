# Independent addendum: terminal realizations of mixed five-ray words

**Verdict: VERIFIED at the stated scope.** This review covers the
nonempty mixed-word theorem in zen_merger/FIVE_RAY_RECURSION.md,
SHA-256

    3c42beb093772aae23cb623174e9529d15672c9117ad5fade0f0469d32fca17c

It does not certify that the guards cover every ordinary parameter.

The composed numerator is correctly

\[
3^e t+B,\qquad
B_{j+1}=a_jB_j+b_j64^j.
\]

For a nonempty word, positivity and the action on \((0,1]\) prove
\(0<B<64^k-3^e\). The proposed congruence for \(4^m\), modulo
\(3^{e+1}\), is exactly the condition
\(64^k(4^m-1)/3\equiv B\bmod3^e\). Since four has order \(3^e\)
on the subgroup congruent to one modulo three, there is one exponent
class, with infinitely many positive representatives.

For every such representative, the constructed integer satisfies
\(t>s\ge1\), including the smallest admissible exponents; no
unmentioned large-\(m\) qualification is required.

Final integrality of a prescribed shortcut word does force its legal
parity class. Modulo two the numerator determines the first input
parity; after performing that integral first step, induction applies
to the remaining word. Positivity then follows from ordinary forward
iteration. This checks all intermediate guards, not only the final
congruence.

The composed right-arm offset is

\[
5B+64^k-3^e.
\]

At the initial value \(5t+1\), its endpoint is consequently \(5s+1\),
and the same integrality argument makes that word physical. Strict
decrease holds at each six-step parameter boundary. It is not a
claim that every individual shortcut step decreases the integer.

For \(s=(4^m-1)/3\), the left arm reaches one at time \(2m\);
the right arm reaches five at the same time. Four further steps
put both at one. Thus the displayed common clock
\(6k+2m+4\) is correct.

The final note correctly limits disjointness of guard cylinders to
equal-length words and permits nesting for prefix extensions. As an
additional consequence, the terminal-ending successful families are
disjoint even for distinct word lengths: terminal parameters have
residues \(1,5,21\bmod64\), so they satisfy neither next guard
\(11,35\bmod64\). This observation is separate from the frozen note.

The empty word is not in the stated theorem. If added separately, it
has \(t=s\) and the original terminal certificate; strict reduction
would not apply to that case.

## Independent exact arithmetic

mixed_word_review_report.json records 14 nonempty words of lengths
one through three, two exponent representatives for each word, and
68 six-step returns. All 28 ordinary parameters satisfy every
guard, strict block decrease, both physical endpoint identities,
and the common terminal certificate. Equal-length residue classes
are distinct; prefix classes nest correctly. Large terminal
halving strings were verified by exact powers-of-two identities,
without floating arithmetic or an inferred orbit limit.

The universal statement follows from the algebra above. This
bounded replay checks its arithmetic interface and does not
replace the all-word proof.
