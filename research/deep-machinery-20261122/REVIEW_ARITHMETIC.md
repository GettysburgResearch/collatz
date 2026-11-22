# Independent review of the whole-source arithmetic attack

Date: 2026-11-22.

**Result: the reconstructed clock bound, survivor inequality, real
whole-source buffer, and integer splice obstruction are mathematically
consistent.** The result supplies necessary restrictions on a surviving
target and rules out the specified splices. It does not prove that every
target descends or that some different legal splice exists.

Reviewed: ARITHMETIC_RIGIDITY.md, Sections 2--4 and the separately written
altered-history estimate in Section 6.
The source interface was checked against PR177 at
431d858d1ac92e88f4a58f6610c0d67733dc7242,
research/lean-exact-witness-global-20261121/JOINT_MINIMAL_COUNTEREXAMPLE.md,
with ROOTED_SOURCE_FLOOR.md and STRICT_PREFIX_CONTRACTION.md used to
clarify the ordinary clocks and literal certificate.
The new Lean statements and their proofs were inspected in
lean/WholeSourceBuffer.lean.

## 1. The first-hit clock really follows from this witness

The joint witness supplies
\[
S=2^e q,\quad 1\le e\le3,\quad
W=P\mathbin{++}[1,2,3,4],\quad P\ne[],
\]
with an actual literal path from \(q\) through \(11\) to \(1\). Put
\[
A=\sum W,\qquad r=|W|,\qquad L=\lfloor(t-1)/2\rfloor.
\]
Here \(A\) is the shortcut clock starting at the odd source \(q\).
It excludes the initial \(e\) halvings from the powered source \(S\).
The supplied floor bounds every positive-clock state of \(S\); since
\(e\ge1\), it therefore bounds \(q\) itself and every later ordinary
state from \(q\).

The literal prefix to \(11\) cannot have hit \(1\) earlier, because the
accelerated map fixes \(1\). The fixed last tail has ordinary states
\[
11,17,26,13,20,10,5,8,4,2,1
\]
and hits \(1\) only at its end. Thus \(A\) is the first ordinary hit of
\(1\) from \(q\).

The \(A+1\) states at clocks \(0,\ldots,A\) are distinct. If two
earlier clocks agreed, determinism would move the final hit of \(1\)
to a strictly earlier clock. They are positive and at most \(L\).
Hence
\[
A+1\le L,\qquad A\le L-1,\qquad 2A<t.
\]
The Lean cardinality argument translates the state interval \([1,L]\)
to Finset.range \(L\) by subtracting one. Positivity makes that
subtraction injective, so its domain and endpoint counts are correct.

## 2. Survivor inequality, including the strict constant

Let \(x_j=T^j(t)\), and let \(o_j\) count odd inputs at clocks
\(0,\ldots,j-1\). Under \(x_j\ge t>0\) through clock \(A\), define
\[
Q=3t+1,\qquad H_j=3^{o_j}t,\qquad X_j=2^jx_j,\qquad
F_j=QH_j+(j-Q)X_j.
\]
The starting value is \(F_0=0\).

At an even step, \(H_{j+1}=H_j\), \(X_{j+1}=X_j\), so
\(F_{j+1}-F_j=X_j\ge0\). At an odd step,
\[
H_{j+1}=3H_j,\qquad X_{j+1}=3X_j+2^j,
\]
and direct expansion gives
\[
F_{j+1}-3F_j=2^j(3x_j-3t+j)\ge0.
\]
This proves the displayed invariant in the note and Lean module without
discarding any additive \(+1\) term.

At clock \(A\), using \(x_A\ge t>0\) gives
\[
(3t+1-A)2^A\le(3t+1)3^{o_A}.
\]
Since \(2A<t\), we have \(6A<3t+1\); therefore
\[
5\cdot2^A<6\cdot3^{o_A}.
\]
The complete source identity
\[
3^r q+C=2^A,\qquad C>0
\]
then yields the strict inequality
\[
5\cdot3^r q<6\cdot3^{o_A}.
\]
The multiplication order, odd-count convention, and strictness all agree
with the formal statements. No independence of target parities is used.

## 3. The real buffer is valid, and its integer use is blocked

The formal affine map for the complete source word is
\[
F_W(z)=\frac{3^r z+C}{2^A},\qquad F_W(q)=1.
\]
For \(q>1\), its coefficient is below one and its real fixed point
\(C/(2^A-3^r)\) lies strictly between zero and one.
From \(t\le2S+1\le16q+1\), one gets \(F_W(t)<17\).
These are real affine statements.

The actual witness has \(r\ge5\), so
\[
2^A>3^r q\ge243q>16q+1\ge t.
\]
Also the source floor gives \(q<t\). If \(F_W(t)\) were an integer,
subtracting its numerator identity from the identity at \(q\) would
force
\[
2^A\mid3^r(t-q),\qquad 2^A\mid(t-q),
\]
using coprimality of powers of two and three. This is impossible for
\(0<t-q<2^A\). Thus the attractive formal endpoint below \(17\)
is not an integer endpoint for this target.

## 4. The target-prefix splice has the stated exact obstruction

Let the target's actual \(A\)-clock prefix end at \(n\ge t\), with
\[
3^o t+D=2^A n.
\]
Retaining that same affine prefix while substituting an endpoint \(v<t\)
would require
\[
3^o u+D=2^A v.
\]
If \(u>0\) were an integer, \(v<n\) first implies \(u<t\).
Subtracting the two identities gives
\[
3^o(t-u)=2^A(n-v).
\]
Coprimality forces \(2^A\mid(t-u)\), contradicting
\[
0<t-u<t<2^A.
\]
The proof does not need a sign assumption on \(D\), and does not assume
that a real affine pullback is legal merely because it is smaller.

This excludes a positive integer source for this fixed target prefix and
these lower endpoints. It does not exclude adaptive changes of the
prefix, changes of the clock, or independently justified comparison rules.

## 5. Formal scope

The module defines the same physical shortcut map on natural numbers.
Its first-hit clock theorem, survivor estimate, and splice obstruction
have their needed positivity and floor premises explicitly in their
types. The combined survivor theorem derives the short-clock premise
from the actual first-hit source data internally.

The complete source affine identity, first-hit property, and transfer
from the upstream JointBadQuery interface are supplied or explained
premises; the standalone module does not import that interface and
silently discharge them. The original full target-return obligation
remains open. The review does not relabel a surviving-target restriction
or an impossible splice as a universal return theorem.

The root's separate fresh-output build receipt and complete axiom log were
also inspected under reports/2026-11-22-deep-machinery/. They report clean
compilation of the source and audit modules and only the standard
propext, Classical.choice, and Quot.sound axiom sets. This reviewer did
not duplicate that compilation or claim a rebuild of the upstream
JointBadQuery import tree.

## 6. The separately written altered-history estimate

For two legal positive odd inverse histories of equal depth \(r\), with
\(0\le k\le r\) changed initial letters and a common remaining word,
subtracting their common-word identities gives
\[
3^{r-k}\mid(p'-p).
\]
The intermediate states are distinct: otherwise their actual \(k\)-step
forward endpoints would coincide, contrary to \(n'=B^j(n)>n\).
Since both intermediate states are positive,
\[
3^{r-k}<\max(p,p').
\]
The two prefix identities then give
\[
3^r<\max(2^E n,2^{E'}n').
\]
With changed gaps at most \(h\), \(\eta n\le2^r\), and
\(3n'<4\cdot64^j n\), this yields exactly
\[
\eta(3/2)^r<\frac43\,2^{hk+6j}.
\]
The use of strict inequalities is justified also when \(k=0\).
No claim that stopped-obstacle mass all has the same
depth is needed or made. The estimate constrains the length of an
initial repair block; it does not bound the number of sparse edits or
exclude a fully adaptive nonlocal replacement.
