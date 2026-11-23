# Scoped review: fixed-endpoint bounded block languages

Date: 2026-11-22. **Verdict: VERIFIED as a complete written elementary argument in the stated fixed-language scope.** No Lean claim or global Collatz closure follows.

Reviewed artifact: `machinery22/arithmetic/BOUNDED_LANGUAGE_SOURCE_RIGIDITY.md`.

SHA256: `b4707282898366ea6b0b3f2c50458f26ca43394646c7beed1712ba4c032934be`.

I independently reconstructed the following steps.

- For a block with at least one odd bit, `u=3^s`, `v=2^L`, and `D=v−u` are as stated. The repeated correction obeys `D c_e = c(v^e−u^e)`. Multiplying the whole source numerator by D gives `v^e(Dm−c)+c u^e`. Both D and v are units modulo `u^e`, so integrality is exactly `u^e | (Dm−c)`. The exponent-zero and zero-defect cases are both handled explicitly.
- The backward finite recursion follows because each current integer endpoint has a finite set of distinct integer preimages under powers of that fixed block. When the defect vanishes, all powers give the same endpoint, not infinitely many sources. Composition of finitely many such finite inverse-set operations remains finite even with independently chosen exponents.
- An integer start and integer endpoint of a supplied binary word do force its entire parity sequence: reduce the complete affine equation modulo two, apply the forced integer branch, and recurse on the remaining word. Thus no nonphysical rational intermediate state has been admitted by the algebra. A positive endpoint also excludes a nonpositive start because the ordinary integer map preserves nonpositivity.
- All-zero blocks are the genuine exception: their inverse sources are `2^(Le)m`. A uniform zero-run bound puts a finite bound on each such repetition exponent. Fixed intervening words must remain in the composition, as the note states.
- A finite dictionary with a uniformly bounded number of powered factors gives a finite union of fixed ordered bounded languages. The source-finiteness conclusion therefore applies to that entire class, not just to an affine one-parameter schedule.
- For a nonperiodic endpoint, a fixed-point exception at an intermediate positive state would make the supplied repeated block a physical cycle, whose forward endpoint must remain on that cycle. Hence it is impossible; each admissible exponent is then finite, yielding finitely many complete words as well as sources.

The application to PR177 retains that source's cofinal family, bounded initial exponent, bounded odd gaps, and fixed endpoint eleven. It only concludes unbounded complexity in the explicitly defined finite-dictionary/powered-factor representation. It does not classify arbitrary unbounded descriptions or prove that the carried target descends.

No correction was required. The proof uses exact powers of three and the full affine correction; it requires neither the 1998 integer-root theorem nor the 2002 integral-quotient theorem. I did not recompile the imported cofinal-source construction.
