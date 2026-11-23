# One maximal reserve per forward clock

This strengthens the same reserved-merger completeness theorem. It reduces
the outer parameter search without asserting that the smaller-partner cover
holds for every positive source.

Use the ordinary shortcut map and actual odd count from
`CollatzGlobalClosure/EndpointSteering.lean`. Fix a source \(n\) and a forward
clock \(h\) satisfying \(2^h\le n\). Put

\[
Q=\left\lfloor n/2^h\right\rfloor>0.
\]

There exists a unique integer \(s\ge0\) such that

\[
3^s\le Q<3^{s+1}.
\tag{1}
\]

The new core Lean module `CollatzGlobalClosure/MaximalReserve.lean` proves
existence by induction on \(Q\), and uniqueness by strict monotonicity of
powers of three. Thus this reserve is available for every source horizon;
it is not an extra supplied coverage hypothesis.

## The single canonical decomposition

Choose

\[
v=\left\lfloor\frac{n}{2^h3^s}\right\rfloor,\qquad
r=n\bmod(2^h3^s).
\]

Then \(v\in\{1,2\}\) and \(n=2^h3^sv+r\). The decomposition is fixed
before any partner is selected. Let

\[
p=A_h(n)=A_h(r),\qquad P=p+s,\qquad q=T^h(n).
\]

The exact normalized-quotient theorem gives

\[
3^P\le q<3^{P+1}.
\tag{2}
\]

In particular, \(P\) is exactly the leading ternary exponent of the actual
endpoint \(q\).

Suppose now that a partner history satisfies

\[
T^t(x)=q,\qquad 2^t\le x.
\]

If \(a=A_t(x)\), exact quotient preservation gives \(3^a\le q\). Formula
(2) forces \(a\le P\). The affordable inverse-extraction theorem therefore
constructs an ordinary \(u\ge0\) with

\[
T^t(u)=T^h(r),\qquad A_t(u)=a,\qquad
x=2^t3^{P-a}v+u.
\]

Thus **every** partner inside its binary horizon uses this one fixed maximal
reserve. The reverse implication is the checked ordinary lifting theorem.
`maximal_reserve_iff_short_merger` proves the exact equivalence, while
`single_reserve_complete` packages existence, uniqueness, and completeness
of the reserve for every actual source horizon.

## Consequence for the PR184 parameter menu

The original `find_reserved` outer loop tries every \(h\) and every allowable
ternary reserve \(s\), choosing the maximal quotient for each pair. The
canonical completeness theorem shows that this menu retains every merger
whose two clocks fit their source binary horizons. The new theorem shows
that the inner loop over \(s\) can be replaced by its **largest** value. All
earlier reserve choices are redundant for that exact merger class.

Equivalently, for each actual endpoint \(q=T^h(n)\), one may explore its
ordinary inverse tree with odd-count cap \(P\), where \(3^P\le q<3^{P+1}\).
Any actual ancestor inside that cap automatically satisfies \(2^t\le x\).
For a desired positive partner \(x<n\), the complete clock bound is
\(t\le\lfloor\log_2(n-1)\rfloor\). No empirical bound is substituted for
this exact finite frontier. A practical node cap can still interrupt the
inverse search and must be reported as such.

The reduction does not prove that any of these finite trees contains the
required smaller partner. An inverse history past the partner horizon lies
in the fully exhausted regime described by `long_inverse_exhausts_carry`;
the fixed-source selection obligation there remains open.

## Formal declarations and validation

The public theorems are:

- `CollatzMaximalReserve.maximal_power_exists`
- `CollatzMaximalReserve.maximal_power_unique`
- `CollatzMaximalReserve.endpoint_ternary_shell`
- `CollatzMaximalReserve.maximal_quotient_one_or_two`
- `CollatzMaximalReserve.maximal_reserve_iff_short_merger`
- `CollatzMaximalReserve.single_reserve_complete`

They depend only on the same-pass core Lean inverse and merger modules. The
build receipt and `MaximalReserve.log` record the source hash, compiler
version, actual exit status, and printed dependency axioms. The mathematical
scope is the complete finite merger mechanism above; no global Collatz
assertion is installed as an axiom or presented as a theorem.
