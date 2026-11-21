# Late PR183 merger refresh and final coupling attempt

## Exact source boundary

Inspected PR183 at
`907a540943090968bc683b1b9246208e9053c1f8`, three commits after the earlier
pin `8659cf62ac685540cadeef320e596c852fbb0959`. The scientific proof commit
is `a1167734093b5fc30f1d7b5ad57bc3e61dbf4cc0`; the final commit records
receipts without changing Lean proofs.

This was targeted exact-head source inspection, not an independent compiler
replay or blanket revalidation of PR183. The inspected paths are:

- `research/literature-closing-20261121/README.md`
- `research/literature-closing-20261121/mergers/MixedBaseNormalForm.lean`
- `research/literature-closing-20261121/mergers/CONSTRUCTIVE_NORMAL_FORM.md`
- `research/literature-closing-20261121/arithmetic/BandArithmetic.lean`
- `research/literature-closing-20261121/lean/EntranceRenewal.lean`
- `research/literature-closing-20261121/lean/RetainedTransport.lean`

## What changes the earlier architecture

`MixedBaseNormalForm.lean` independently formalizes the ten-rule subsystem
obtained by omitting `f1 -> 0t` from the Yolcu–Aaronson–Heule mixed-base
system. Its concrete natural matrix rank strictly decreases under every
retained rewrite. Every rewrite preserves ordinary value or takes exactly
one ordinary shortcut step. Every positive integer therefore reaches a
normal word on its actual orbit.

A nonempty normal word has a blocked suffix

\[
w=\mathrm{pre}\;f1\;\mathrm{post},
\]

where the final suffix is ternary. Writing its length as \(k\), its value as
\(0\le r<3^k\), and the positive prefix value as \(q\), the parent and the
erased candidate are

\[
n=3^k(6q+1)+r,
\qquad m=3^k(2q)+r.
\]

Erasing the blocked ternary one decreases **both** ordinary value and the
same matrix rank, even in arbitrary mixed contexts. Consequently the rank
argument can legitimately tolerate value growth during normalization. This
is a genuine alternative to induction on the original ordinary source and
does not require the normal-form endpoint to be below that original source.

The exact general theorem is nevertheless conditional:

```text
CollatzShell.MixedBaseNormalForm.blocked_erasure_iff_universal
  : BlockedErasureCover ↔ Universal
```

`BlockedErasureCover` requires an actual finite ordinary merger for at least
one blocked erasure in every nonempty normal word. `universal_of_blocked_erasure`
uses that supplied merger to transfer the smaller-rank candidate's
convergence. Neither theorem establishes the cover.

The new explicit all-prefix class is `terminal_double_one_merger`: for every
mixed prefix, terminal `f11` erases to `f1`, with values \(18q+4\) and
\(6q+1\), whose first shortcut images are both \(9q+2\). Arbitrary other
ternary suffixes remain outside that merger theorem.

## Attempt to supply the missing merger using inverse carry

Our exact quotient, unrestricted carry, and maximal-reserve recovery retain
every actual ordinary merger inside both source horizons. They recover an
already legal inverse history and preserve its full ternary remainder; they
do not manufacture an inverse word for a prescribed candidate.

For the blocked erasure, the candidate is prescribed. Its relation to the
parent is

\[
n=3m+\delta,\qquad \delta=3^k-2r.
\]

The two starts have opposite parity because \(\delta\) is odd. In particular,
they are not a common binary-prefix pair to which ordinary binary lifting
can immediately be applied. A reserve decomposition cannot replace this
missing parity-word information.

For a fixed pair of legal words asserted uniformly over an arithmetic class
of prefix values \(q\), coefficient comparison forces equal ordinary clocks
and one extra odd input on the candidate arm. If the common clock is \(h\),
the parent odd count is \(p\), and the two affine corrections are \(C_n,C_m\),
the remaining exact condition is

\[
C_m-C_n=3^p(3^k-2r).
\]

Legality of both words for the prescribed ordinary \(q\) is still required.
The terminal `f11` case has \(\delta=1\) and satisfies this in one step.
The normalization and erasure rank inequalities impose no such word identity
for a general suffix.

Already the normal word `f1` proposes \(n=7,m=2\). Their merger is real,
but the parent does not meet either point of the candidate's orbit in its
binary horizon \(h\le\lfloor\log_2 7\rfloor=2\). It reaches two at clock ten.
Thus the horizon-complete inverse mechanism cannot by itself cover even all
these prescribed candidates. The unrestricted carry remains exact beyond
that frontier, but a vanished leading coefficient leaves the full original
endpoint as its shadow and supplies no new decreasing argument.

No universal blocked-erasure merger, source-bound partner selector, or
controlled continuation certificate was obtained from this coupling.

## Relation to the nonterminal certificate attempt

The exact nested-context and offset calculations were sent separately for
`NONTERMINAL_DISPATCH_ATTEMPT.md`. With
\(\Phi_e(z)=2^{e+1}z-1\), \(e\ge1\), and a supplied source prefix
\(3q+1=2^a r\), they give

\[
T(\Phi_e(q))=\Phi_{e-1}(\Phi_{a-1}(r)).
\]

The inner comparison consumes a genuinely smaller supplied certificate. Its
returned ordinary certificate has no proved grade bound for the outer call.
Keeping the exact target as \(2^Bq-C\) instead gives, for odd \(C\) and
\(B\ge1\),

\[
T(2^Bq-C)=2^{B+a-1}r-
\left(2^{B-1}+\frac{3C-1}{2}\right).
\]

This retains the carry without certificate reuse, but leaves a general
terminal offset when the source certificate ends. The simple nested-context
multiset does not decrease: contexts \([1,0,0,1]\) and \([0,1,2]\) over source
one represent the actual step \(35\to53\), with grades
\([3,1,1,3]\to[1,3,5]\). PR183 supplies a different sound matrix rank for its
own retained rewrite rules, but leaves its corresponding erasure merger as
an explicit open condition. These ranks have not been combined as an
unproved common induction.
