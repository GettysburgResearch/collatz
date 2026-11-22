# Scoped review: regular-language source rigidity

Date: 2026-11-22.

Reviewed only the newly added Section 6 (Corollary BL4) and its corresponding scope statements in:

`machinery22/arithmetic/BOUNDED_LANGUAGE_SOURCE_RIGIDITY.md`

SHA-256: `63af23e8fa3594d6e1355dcc35a9d3bea52040528f37891b5420a2706f7a52d8`.

**PASS.** This extends the separate review of BL1–BL3 at its earlier pinned hash. No correction is needed in the new argument.

For an accepted word of length at least the number of DFA states, two visited states coincide. Its nonempty loop V can therefore be pumped an arbitrary nonnegative number of times with the fixed prefix A and suffix B retained. Because every pumped word is accepted, the uniform bound on consecutive zeroes forces V to contain an odd letter. This use of the zero-run hypothesis is valid even when the loop appears next to other zeroes.

The suffix B has one rational inverse image y of the fixed endpoint m. Since each accepted complete word is a valid integer path, its state at the start of B is exactly this same integer y. Hence the inverse source of V^t at y is integral for every t. BL1 implies that 3^(s t) divides the one fixed integer E_V(y) for arbitrarily large t, forcing E_V(y)=0. Thus all these inverse sources equal y. Inverting the unchanged prefix A shows that removing V preserves the complete word's original integer source.

The shortened word is still accepted, so this operation can be repeated until its length is smaller than the DFA state count. There are finitely many resulting words and each affine word has one rational source for endpoint m. Consequently there are finitely many integer sources for the entire regular language. Positivity is not needed.

The hypothesis that *every* accepted word is a valid complete path to m is essential and is explicitly stated. The proof does not apply to a regular superset of valid words, to an automaton supplemented by unbounded arithmetic state, or to an arbitrary adaptive certificate generator. The scope paragraphs retain these distinctions.

The added descriptions of `BoundedLanguage.lean` are not part of this scoped review; the separate build receipt owns their verification. No new external theorem, numerical enumeration, or legacy compilation was used for this review.
