# Final closure pass: the automatic clock inequality is false

**Full Collatz remains open.** The completed terminal compiler was left
unchanged. This separate continuation tests whether its whole accepted
carry-minus-one language automatically enters the PR177 multiset order.
It finds a precise counterexample to one proposed shortcut, then supplies
the general certificate interface that repairs any given finite shortfall.

## 1. A genuine ordinary source violates t >= B

Take the prefix

```
w = [4,1,1,2,2,1,2,4,4,4].
```

It has `B=25`, `s=11`, and Hplus carry `p=-84966775`. Its complete carry
program is

```
OOEOEEEEEEEEOEEOOOOOOOE
```

with `t=23` and final carry `d=-1`. Thus `t=B-2`.

This is an actual ordinary certificate obstruction, not an unrealized word.
Let

\[
h=8744,\qquad
m=\frac{2^{8769}-42571961}{177147}.
\]

Lean verifies that `m` is a positive natural number, that its entire exact
odd-gap word is `w ++ [8744]`, and that `Basin m` follows from that word.
The declarations `concrete_full_word`, `follows_basin`, and
`concrete_source_basin` include the ordinary replay and basin bridge.
The large source is kept as the exact compact integer expression above.

## 2. The shortfall is preserved by arbitrary initial one-gap loops

For every `k>=0`, let `w_k = [1]^k ++ w`. The exact identities are

\[
B_k=k+25,\qquad t_k=k+23,\qquad d_k=-1.
\]

The compiler's odd transition proves this for every k: adding one gap-one
prefix changes the initial carry by

\[
p\longmapsto2p-3^s,
\]

and one odd compiler step returns to the old state. Theorems
`carry_prepend_one`, `program_prepend_one`, `padded_program`, and
`padded_clock_shortfall` formalize the entire language.

The one-extra-step handoff from the main packet would have initial even
exponent `e=h+1`. Its initial grade is `2h+3`. Every gap of `w_k` is at most
four; therefore, for `h>=4`, this new grade exceeds **every** parent grade
in `w_k ++ [h]`. `padded_handoff_grade_increases` proves those inequalities.
Consequently the proposed automatic use of that particular rank decrease
is false.

There is also a direct arithmetic reason not to dismiss the example only
because the base prefix begins with gap four. The base program's minimum
prefix coefficient is `81/32768`. Prepending fifteen gap-one loops raises
every subsequent prefix coefficient above one because

\[
(3/2)^{15}\frac{81}{32768}=
\frac{3^{19}}{2^{30}}>1.
\]

The remaining minus-one shadow uses only odd branches before its binary
horizon. Since ordinary shortcut corrections are nonnegative, every valid
positive realization with at least fifteen such initial loops remains above
its original target throughout that horizon. This coefficient argument is
an elementary written consequence of a finite exact prefix check; it is
**not** included among the separately audited Lean declarations.

## 3. A general repair for a deficit D

The failure above does not make every longer handoff fail. Suppose the
whole-prefix compiler has carry minus one and

\[
B=t+D,\qquad D\ge0.
\]

The first normal form has height `H=h+D+1`. Run another `D+1` ordinary odd
steps. These steps fit inside that height whenever `h>=0`, and give the exact
identity

\[
\boxed{
T^{B+1}(n)=3^{D+1}2^h-1.
}\tag{1}
\]

For `h>=1`, this is the psi target of

\[
\boxed{S=3^{D+1}2^{h-1}.}\tag{2}
\]

The **exact required auxiliary certificate** is a complete ordinary exponent
word `v` for the positive integer `3^(D+1)`, satisfying

\[
\forall a\in v,\qquad a<h.\tag{3}
\]

With that supplied certificate, `S` has the powered certificate
`(h-1;v)`. Every child grade is below the old terminal grade `2h`:

\[
2(h-1)+1<2h,\qquad 2a<2h\quad(a\in v).
\]

The actual target transport, the known child source, and all these grade
inequalities are proved by `deficit_normal_form` and
`deficit_certificate_handoff`. The latter accepts an actual `Follows`
certificate, rather than assuming a general convergence theorem for powers
of three. PR177's existing multiset replacement theorem can then consume
the entire parent word.

For the exhibited deficit `D=2`, the required odd part is `3^3=27`, which
has the complete ordinary odd-gap word

```
[1,2,1,1,1,1,2,2,1,2,1,1,2,1,1,1,2,3,1,1,2,
 1,2,1,1,1,1,1,3,1,1,1,4,2,2,4,3,1,1,5,4].
```

Its largest gap is five. Thus **three extra ordinary odd steps repair the
two-clock shortfall whenever h>=6**. In particular the concrete `h=8744`
example defeats the unqualified one-step handoff, but is covered by this
longer handoff. It is not a counterexample to every certificate rewrite.

## 4. Exact unresolved statements

No universal bound on `D=B-t` for carry-minus-one prefixes is proved here.
Nor is a uniform family of certificates for `3^(D+1)` with all gaps below
the available terminal `h` proved. Either would need an actual theorem;
successful finite searches do not supply it.

Arbitrary signed carries may require an additional finite signed
continuation or a different source-preserving comparison. No universal
dispatcher for those cases was established. The new general interface
identifies precisely which power-of-three certificate would pay a given
deficit, while keeping the source, original target, ordinary clocks, and
terminal grade synchronized.

## 5. Verification

[TerminalCarryClosure.lean](../lean/Collatz/TerminalCarryClosure.lean) imports the already completed
`Collatz.TerminalCarry`. The arithmetic counterexample, all initial-loop
identities, grade reversal, and concrete positive full-word certificate are
kernel checked. The general deficit handoff is checked in the same module.
[AuditTerminalCarryClosure.lean](lean/AuditTerminalCarryClosure.lean) audits its public declarations; only
the standard Lean axioms are permitted. Main packet files were not modified.
