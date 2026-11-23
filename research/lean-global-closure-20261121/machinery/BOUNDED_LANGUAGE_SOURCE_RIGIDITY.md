# Exact fixed-endpoint rigidity for bounded block languages

Date: 2026-11-22. **Status: complete written elementary proof.** This
strengthens the fixed-endpoint affine-schedule deduction considered during
the literature attack. The source statement does not need a deep
Diophantine theorem: exact 3-adic divisibility gives a stronger result.
The companion cycle theorem in `FIXED_BLOCK_INTEGRAL_RIGIDITY.md` retains
its genuine Corvaja–Zannier dependency.

## 1. Single-block repetition: an exact integrality test

Let \(V\) be a nonempty binary shortcut parity word, containing
\(s\ge1\) odd letters and having total length \(L\). Its full
affine map is

\[
t_V(x)=\frac{3^s x+c}{2^L},\qquad c\in\mathbb Z_{>0}.
\]

Write \(u=3^s\), \(v=2^L\), and \(D=v-u\). The nonzero
integer \(D\) is coprime to three. For any fixed integer endpoint
\(m\), let \(q_e(m)\) be the unique rational source sent to \(m\)
by the repeated word \(V^e\), where \(e\ge0\). Define

\[
E_V(m)=Dm-c.
\]

**Lemma BL1.** The following exact criterion holds:

\[
q_e(m)\in\mathbb Z
\quad\Longleftrightarrow\quad
3^{se}\mid E_V(m).
\tag{1}
\]

If \(E_V(m)=0\), every \(q_e(m)=m\). If \(E_V(m)\ne0\),
the possible exponents are precisely

\[
0\le e\le\left\lfloor\frac{v_3(|E_V(m)|)}s\right\rfloor.
\tag{2}
\]

Here the valuation is used only on a nonzero integer. No value
\(v_3(0)\) is assumed.

**Proof.** Repeating the affine map gives the integer correction

\[
c_e=c\sum_{j=0}^{e-1}v^{e-1-j}u^j,
\qquad Dc_e=c(v^e-u^e).
\]

The empty sum for \(e=0\) is zero. Hence

\[
q_e(m)=\frac{v^e m-c_e}{u^e},
\qquad
D(v^e m-c_e)=v^eE_V(m)+cu^e.
\tag{3}
\]

Since both \(D\) and \(v\) are units modulo every power of three,
\(u^e\mid(v^em-c_e)\) if and only if
\(u^e\mid E_V(m)\). This proves (1). If \(E_V(m)=0\),
equation (3) gives \(q_e(m)=c/D=m\). Otherwise (2) is exactly the
valuation form of (1). \(\square\)

The criterion keeps the entire correction of the repeated block. It is
not a congruence check at a selected proper factor of a cycle denominator.

## 2. Arbitrary independent repetition counts

Fix a finite list \(V_1,\ldots,V_r\), each containing an odd letter,
and a fixed integer endpoint \(m\). Consider all words in the bounded
language

\[
V_1^*V_2^*\cdots V_r^*
=\{V_1^{e_1}\cdots V_r^{e_r}:e_i\in\mathbb N_0\}.
\]

The exponents are independent; there is no affine schedule hypothesis.

**Theorem BL2.** Only finitely many integer sources are mapped to \(m\)
by these words. This finite set can be constructed exactly by the
following backward recursion.

Start with \(B_r=\{m\}\). For \(i=r,r-1,\ldots,1\), replace
each \(y\in B_i\) by

\[
\begin{cases}
\{y\},&E_{V_i}(y)=0,\\[2mm]
\{q_e^{(i)}(y):0\le e\le
\lfloor v_3(|E_{V_i}(y)|)/s_i\rfloor\},&E_{V_i}(y)\ne0.
\end{cases}
\tag{4}
\]

Their union is \(B_{i-1}\). Each set is finite by BL1, so the final
set \(B_0\) is finite. The recursion is exact because every complete
integer source has integer states at the block boundaries and must
satisfy the single-block criterion at each boundary. Conversely, every
choice admitted by (4) gives an integer affine preimage at that block.

Fixed intervening words are preserved as fixed maps; they cannot be
deleted. They may either be explicitly inserted in the backward
recursion or treated as singleton allowed exponent sets. Empty blocks
and zero repetition counts introduce only the identity and cause no
problem.

## 3. Why the integer words are physical

An integer formal source and integer endpoint for a finite supplied
shortcut word force the prescribed parities. The affine equation
\(2^Lm=3^sq+c\), reduced modulo two, forces the first bit of
\(q\). After applying that legal branch, the same argument applies to
the remaining word and its integer current source. Induction proves
every branch.

Thus the sets in BL2 describe actual integer paths. In particular, when
the endpoint is positive, an admitted source is positive: integer zero
stays zero and negative integers stay negative under the ordinary map.
Alternatively one may restrict (4) to positive states; the resulting
positive-source set is the same.

A block with no odd letter is \(0^L\), whose inverse sources are
\(2^{Le}m\). This is the essential exception to BL2. For positive
\(m\), unrestricted repetitions produce infinitely many distinct
sources. Such a block may still be included when its exponent is bounded.

## 4. Uniformly bounded gaps and finite dictionaries

Suppose words have a uniform bound \(K\) on every consecutive zero
run, including an initial or terminal run. In a fixed bounded-language
expression, an all-zero block \(V_i=0^{L_i}\) can then occur at most
\(\lfloor K/L_i\rfloor\) times consecutively. It contributes only a
finite inverse set. Applying BL2 to the other blocks gives:

**Corollary BL3.** For a fixed endpoint and a fixed bounded language
\(V_1^*\cdots V_r^*\), the words satisfying a uniform zero-run bound
have only finitely many distinct positive integer sources.

The conclusion remains true for a finite union of such bounded
languages. Equivalently, fix a finite dictionary of nonempty binary
blocks and a bound \(r\) on the number of powered dictionary factors.
Among uniformly bounded-zero-run words ending at a fixed integer,
there are only finitely many positive sources. There are only finitely
many ordered dictionary lists of length at most \(r\), so this is a
finite union of BL3 applications.

Consequently, the cofinal bounded-four certificates with bounded initial
exponent and fixed endpoint eleven in PR177 cannot have a uniformly
bounded number of powered factors from any fixed finite block dictionary.
Their needed block complexity must be unbounded in that precise sense.

This conclusion does not refute the cofinal construction; it constrains
how its adaptive words can be compressed. No claim is made about a
dictionary that changes with the source or contains infinitely many
blocks.

## 5. Nonperiodic endpoints and repeated-source exceptions

If the endpoint \(m\) is nonperiodic, no positive intermediate state
in the backward recursion can satisfy \(E_V(y)=0\). Such a state
would have an actual loop \(V\), and any later endpoint on its orbit
would lie on that cycle. Hence all permitted exponents are bounded in
this case, and there are only finitely many complete words in the
bounded language as well as finitely many sources.

For endpoint eleven, nonperiodicity follows from its explicit odd orbit
\(11\to17\to13\to5\to1\), followed by the trivial cycle. For
endpoint one, repeated loops at one can give infinitely many words but
still only finitely many sources in a fixed bounded language. This is
why BL2 counts sources rather than asserting finiteness of words for
every endpoint.

## 6. Regular languages of complete words

**Corollary BL4.** Let \(\mathcal L\) be a regular language of binary
shortcut words. Suppose **every word in \(\mathcal L\)** is an actual
integer path ending at the same fixed integer \(m\), and suppose a
uniform bound \(K\) holds on every zero run of every accepted word.
Then the words in \(\mathcal L\) have only finitely many distinct
integer sources.

To prove this, choose a deterministic finite automaton for
\(\mathcal L\), with \(N\) states. An accepted word of length at
least \(N\) has a repeated state and factors as \(AVB\), where
\(V\ne\varnothing\) is a loop. Every \(AV^tB\), \(t\ge0\), is
accepted. The loop must contain an odd letter: otherwise pumping it
would contradict the uniform zero-run bound. The fixed suffix \(B\)
has a unique rational preimage \(y\) of \(m\); validity of the
accepted words makes \(y\) an integer. For every \(t\), the block
\(V^t\) therefore has an integer preimage of this same \(y\).
BL1 forces \(E_V(y)=0\), so every one of these preimages equals
\(y\). Inverting the fixed prefix \(A\) now shows that deleting
\(V\) leaves the original source unchanged. Repeat until the word
has length less than \(N\). There are only finitely many such words,
and each has a unique source. This proves BL4.

The universal validity condition applies to the entire regular language.
A regular **superset** of some valid words does not meet the hypothesis:
its pumped words may fail integrality. BL4 does not rule out a finite
automaton used inside an algorithm with unbounded arithmetic memory.
It rules out a regular language consisting wholly of bounded-gap
complete certificates and covering a cofinal set of source integers.

## 7. Relation to the attempted full proof

The fixed-schema cycle theorem uses a deep integral-quotient theorem to
classify an entire family. Trying to use a finite collection of such
repetition templates as a universal source selector now has a sharper
boundary: BL3 rules out their cofinal coverage even when repetition
counts vary independently.

The missing full argument must therefore handle unbounded dictionary
complexity, an infinite adaptive dictionary, or another arithmetic
mechanism. BL4 further rules out a regular complete-certificate selector
with bounded gaps. No contrary arithmetic upper bound on the required
complexity has been proved for the actual cofinal construction or the
original target orbit. This note does not prove that every such adaptive evolution
reaches a return guard, and it does not prove descent of the original
target. It supplies neither a nontrivial positive cycle nor a divergent
positive orbit.

## Inputs and evidence

The proof of BL1–BL3 is elementary and complete above. Its only external
repository application is PR177 at
`431d858d1ac92e88f4a58f6610c0d67733dc7242`,
`research/lean-exact-witness-global-20261121/BOUNDED_FOUR_NORMAL_FORM.md`
and `ROOTED_SOURCE_FLOOR.md`, which supply the cofinal complete-source
family with the stated endpoint and gap restrictions. That imported
construction was not recompiled in this pass.

No finite enumeration is a proof premise. `BoundedLanguage.lean`
formalizes the repeated-affine-block arithmetic underlying BL1, the
finite inverse source set, an exact executable finite-set recursion,
and finiteness of its composition for arbitrary independent repetition
counts. It uses the coarse proved cutoff
\(e<|E_V(m)|\) when the defect is nonzero; its divisibility filter is
exact. The sharper valuation cutoff, the translation from binary words
to affine blocks and physical paths, zero-run restrictions, and the
automata deduction BL4 remain written proofs above. No additional
infinite analytic assumption is used. The separate build receipt records
the exact checked source, dependencies, and standard Lean axioms.
