# A further complete-certificate source reset

## Result and scope

`CertificateBoundary.lean` adds a local branch to the complete-certificate
interval program. Its original known source is

\[
S=4q=4(4p+1)=16p+4,
\]

and the supplied odd certificate of \(q\) starts with gap four. Under the
explicit predecessor guards below, the theorem constructs another known
source \(S'=8z\) with

\[
S+4\le S',\qquad
\Gamma(3;W\mathbin{+\!+}(2::\tau))
  <\Gamma(2;4::\tau).
\]

The suffix \(\tau\) is exactly the supplied suffix, of arbitrary length and
with no bound on its entries. Every wanted target \(t\) in the original
interval \(0<t\le2S+1\) remains in the new interval. The target is unchanged.

This is a new local rewrite, with its complete child certificate and its
multiplicity comparison checked in this module. It does not complete the
remaining interval dispatcher or prove Collatz convergence.

## Frozen sources used

The comparison program is PR177 at commit
`a0a0d76f91b4e3846c1b1f0706cad56cb6098317`:

| Source file under `research/lean-exact-witness-global-20261121/lean/Collatz/` | Interface used |
|---|---|
| `Witness.lean` | The complete algebraic odd-gap certificate |
| `GapMultiset.lean` | `Less`, `grades`, `PoweredCertificate`, and `certificate_cons_iff` |
| `RetainedEvenReset.lean` | The four exact predecessor prefixes in `doubling_prefix` |
| `RetainedEvenBoundary.lean` | The sibling identity removing two from the first odd gap |
| `BoundedGapCofinal.lean` | Context: the high-gap cases reduce to a low alphabet |
| `LowIntervalRefinement.lean` | Context: additional low-alphabet source/target rules |

The fetched Git blob IDs of the three central files are respectively
`5298352d883a66289244a34d818ef7974224a3d7` for `GapMultiset.lean`,
`2eaf32078f9043764a35c25744bf75eba908417b` for `RetainedEvenReset.lean`, and
`9f2b1627fe5a00bb880f78f7f7d131eeb4709194` for `RetainedEvenBoundary.lean`.

These are source pins, not dependencies silently imported by the new module.
The new module imports `OffsetDescent`, using the existing ordinary shortcut
map \(T(n)=n/2\) for even \(n\), and \((3n+1)/2\) for odd \(n\).

## Exact certificate interface

The local inductive predicate `Certificate n word` has these constructors:

\[
\operatorname{Certificate}(1,[]),
\]

\[
a>0,\quad3n+1=2^a u,\quad
\operatorname{Certificate}(u,\tau)
\quad\Longrightarrow\quad
\operatorname{Certificate}(n,a::\tau).
\]

The module proves that every represented source is odd and that every such
certificate supplies an actual finite ordinary orbit ending at one. It does
not assume that one is first reached at the final clock. For example, gap-two
padding at one is allowed.

PR177 uses its algebraic certificate instead. Its pinned
`certificate_cons_iff` proves precisely the same positive-gap recurrence,
and its empty certificate is exactly the terminal value one. Structural
induction therefore identifies the two certificate predicates mathematically.
This cross-file equivalence is source-qualified here; the new module does
not import PR177 or provide a Lean theorem naming both predicates.

The order definitions are reproduced literally, apart from namespace and the
name `GradeLess`:

\[
\begin{aligned}
\operatorname{GradeLess}(A,B)
&\iff\exists h,\quad \#_A(h)<\#_B(h)
   \quad\text{and}\quad
   \forall j>h,\ \#_A(j)=\#_B(j),\\
\Gamma(e;\tau)
&=(\,[2e+1]\text{ if }e>0\text{, otherwise }[]\,)
  \mathbin{+\!+}\operatorname{map}(2\cdot,\tau).
\end{aligned}
\]

The new module checks the particular comparison at pivot eight. The general
well-foundedness proof remains the pinned PR177 theorem; it is not reproved
or silently assumed as a new axiom here. The local interval rule explicitly
takes the usual lower-rank induction hypothesis.

## Construction of the child source

Let the supplied source certificate be

\[
\operatorname{Certificate}(4p+1,4::\tau).
\]

Its first edge gives an odd \(u\) such that

\[
3(4p+1)+1=16u,
\quad\text{hence}\quad3p+1=4u.
\]

Consequently the same supplied suffix gives
\(\operatorname{Certificate}(p,2::\tau)\). Since \(u\) is odd,
\(p\equiv1\pmod8\). This phase is a conclusion, not an extra assumption.

The reset assumes

\[
p\not\equiv0\pmod3,\quad p\ne1,\quad
p\not\equiv7\pmod9,\quad p\not\equiv19\pmod{27}.
\]

Those guards give the following disjoint exact cover:

| Guard on \(p\) | Inserted prefix \(W\) | New predecessor \(z\) |
|---|---|---|
| \(p\equiv2\pmod3\) | \([3]\) | \((8p-1)/3\) |
| \(p\equiv4\pmod9\) | \([3,2]\) | \((32p-11)/9\) |
| \(p\equiv10\pmod{27}\) | \([3,2,2]\) | \((128p-65)/27\) |
| \(p\equiv1\pmod{27}\), \(p>1\) | \([2,2,2]\) | \((64p-37)/27\) |

Each row is checked by exact positive gap edges into the already supplied
certificate of \(p\). Thus

\[
\operatorname{Certificate}(z,W\mathbin{+\!+}(2::\tau)),
\qquad2p\le z.
\]

The complete certificate also forces \(z\) odd. This small parity fact makes
the source comparison stronger than a coarse real-valued estimate:

\[
2p+1\le z
\quad\Longrightarrow\quad
S'=8z\ge16p+8=S+4.
\]

Accordingly, no exceptional target at the old upper boundary remains in the
main reset. Every target obeying \(t\le2S+1=32p+9\) also obeys
\(t\le2S'+1\).

## Full multiset comparison

The parent and child grades are

\[
\begin{aligned}
\Gamma(2;4::\tau)&=[5,8]\mathbin{+\!+}2\tau,\\
\Gamma(3;W\mathbin{+\!+}(2::\tau))
  &=[7]\mathbin{+\!+}2W\mathbin{+\!+}[4]
    \mathbin{+\!+}2\tau.
\end{aligned}
\]

Every entry of \(W\) is at most three. All newly inserted grades are therefore
at most seven. At grade eight, the child loses exactly one occurrence; above
eight, the multiplicities are unchanged. Every contribution of the literal
suffix cancels, even when the suffix itself contains larger grades.

`second_even_source_reset` checks this construction without a target or a
convergence assumption about any wanted target. `second_boundary_interval_rule`
then applies the explicit lower-rank hypothesis to the unchanged target and
the new complete source certificate. Ordinary source value is allowed to
increase because the supplied complete-certificate rank strictly decreases.

For a concrete example, \(q=69\) has certificate \([4,3,4]\), and
\(p=17\) has \([2,3,4]\). The first row gives \(z=45\) with certificate
\([3,2,3,4]\). The known source changes from \(276\) to \(360\), while all
targets through \(553\) are retained. The source grades change from
\([5,8,6,8]\) to \([7,6,4,6,8]\); the common suffix grades \([6,8]\)
are untouched.

## Independent physical boundary transport

The module also proves four exact ordinary identities, derived from the
already checked affine lifting theorem:

\[
\begin{aligned}
T^4(32p+3)&=18p+2,\\
T^2(32p+5)&=24p+4,\\
T^2(32p+9)&=24p+7,\\
T^8(256v+39)&=243v+38.
\end{aligned}
\]

If \(p\equiv1\pmod8\), write \(p=8v+1\). The last identity becomes

\[
T^8(32p+7)=\frac{243p+61}{8}.
\]

For \(p\ne1\), the phase forces \(p\ge9\), and all four displayed endpoints
are positive and at most \(32p+1\). An even boundary target halves into that
interval in one step; a target already inside uses time zero.
`full_boundary_transport` therefore proves

\[
0<t\le32p+9
\quad\Longrightarrow\quad
\exists k\le8,\quad0<T^k(t)\le32p+1.
\]

This finite transport is independent of the predecessor guards and of any
certificate. It is not needed to justify the main source reset, whose child
source is larger. In particular, it is not presented as a new global descent
or convergence theorem.

## What remains outside the rule

The three residue exclusions and the terminal value are explicit. If
\(3\mid p\), there is no nonempty positive odd-gap prefix ending at \(p\):
its last edge would assert \(3z+1=2^a p\), impossible modulo three. Merely
allowing a longer inserted prefix cannot remove that obstruction.

This leftover can occur with a complete low-alphabet certificate. For example,
\(p=33\) and \(q=133\) give the supplied certificate
\([4,2,1,3,1,2,3,4]\) for \(q\). Its suffix is entirely in the alphabet
\(1,2,3,4\), but \(3\mid p\), so the new reset deliberately does not apply.
Other existing or future rules can inspect more of the supplied certificate
or use an actual target merger; no such universal selector is asserted here.

The remaining task is therefore still a genuine coverage argument on the
unbounded low-alphabet source words. Neither this source-growing reset nor
the independent eight-step boundary transport supplies that coverage by
itself.
