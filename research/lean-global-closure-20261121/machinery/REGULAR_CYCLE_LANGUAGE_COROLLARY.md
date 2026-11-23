# Regular complete cycle languages have finitely many realizers

Date: 2026-11-22. **Status: written corollary of the fixed-block
integral-rigidity theorem; retains its Corvaja–Zannier dependency.**

Let \(\mathcal L\) be a regular language consisting entirely of
**nonempty** binary shortcut words. Suppose every accepted word \(W\)
has an integral full-cycle quotient

\[
z_W=\frac{C_W}{2^{|W|}-3^{\#1(W)}}.
\]

Then \(\{z_W:W\in\mathcal L\}\) is finite. No uniform zero-run
bound is needed for this cycle statement. The quotients may have any sign.

**Proof.** Fix a deterministic finite automaton with \(N\) states.
An accepted word of length at least \(N\) contains a nonempty loop
and factors as \(AVB\). Every word \(AV^kB\), \(k\ge0\), is
accepted and hence nonempty and has integral full-cycle quotient. This
is a fixed-block schema: the possibly empty buffers \(A,B\) have
fixed exponent one and \(V\) has exponent \(k\). The theorem in
`FIXED_BLOCK_INTEGRAL_RIGIDITY.md` proves that its full quotient is one
constant integer for every retained nonempty index. In particular,
deleting \(V\) leaves the cycle realizer unchanged. Continue deleting
loops until the accepted word has length less than \(N\). There are
only finitely many such words, each with one quotient. \(\square\)

The nonempty-language condition ensures loop deletion never leaves an
accepted empty word, whose displayed denominator would be zero. Fixed
buffers are retained throughout the proof and may connect different
phases of the same cycle. This is not an assertion that every cycle has
bounded word length, that every cycle word belongs to one such regular
language, or that the finitely many retained cycle realizers are trivial.
A regular superset containing nonintegral words does not satisfy the
hypothesis. The full Collatz conclusion does not follow.

The companion source statement BL4 in
`BOUNDED_LANGUAGE_SOURCE_RIGIDITY.md` is elementary and does require a
uniform zero-run bound. Both results restrict exact regular languages
of valid words; neither imports automaticity of an unknown orbit.
