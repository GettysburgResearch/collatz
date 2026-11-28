# Exact algebra of the signed entrance tree

[ConformalTree.lean](ConformalTree.lean) proves the finite word identities
used by the [atomic conformal construction](../escape/phase9/ATOMIC_ADELIC_CONFORMAL_LAWS.md).
The maps are the actual rational shortcut inverses
\(I_0(x)=2x\) and \(I_1(x)=(2x-1)/3\). A Boolean word denotes outer
composition: its last letter is applied first. Write \(e(w)\) for its
number of even inverses and \(F_1(x)=(3x+1)/2\). The central identities are
\[
 I_w(F_1^{|w|}z)=I_w(-1)+3^{e(w)}(z+1),\qquad
 (4/9)^{|w|}\operatorname{weight}(w)=9^{-e(w)}.
\]
The branch weights are \(1/4\) and \(9/4\). The kernel also proves that
the word weight times the square of the inverse slope is one, that the
word map is affine with the stated slope, and that every word preserves
strict negativity of rational inputs.

These are unconditional identities of actual rational word maps. The
theorems do not assume branch legality, because the identities hold even
before that restriction. In the accompanying written construction,
ternary legality selects the negative integer predecessors of \(-1\),
and the identities then identify the finite entrance measures and their
weights. Finiteness of the infinite Green series, the stationary measure,
the positive real lift and the binary parity compatibility are separate
written arguments. They are not claimed as Lean theorems.

The source compiled with strict warnings and no implicit variables under
the pinned Lean/Mathlib setup. The checkpoint's fresh all-declaration
audit is the authoritative reproducibility receipt.
