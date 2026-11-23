# General certificate dispatcher: exact reductions and the remaining carry

## Scope and source convention

This note records a further full-closure attempt after the checked terminal
reset. It does not supply a complete dispatcher or a proof of Collatz. The
identities and reductions below are written mathematics; this pass did not add
them as new Lean theorems. The existing checked comparison, certificate, and
terminal-reset modules supply the formal interface described here.

Write `Basin(n)` for actual finite iteration of the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}\end{cases}
\]

to 1. A supplied complete certificate `Certificate(q, a :: tail)` means

\[
3q+1=2^a r,\qquad a\ge1,\qquad
\operatorname{Certificate}(r,\mathrm{tail}),
\tag{1}
\]

where both \(q,r\) are positive odd integers and \(a\) is the exact valuation.
The common well-founded rank is the multiset

\[
\Gamma(e;\mathbf a)=
  \bigl(\{2e+1\}\text{ if }e>0\text{, otherwise }\varnothing\bigr)
  \uplus\{2a:a\in\mathbf a\}.
\tag{2}
\]

Every recursive query must have its own actual complete source certificate
and a smaller rank than the same parent certificate. A proved `Basin` output
does not carry a bound on the rank of its newly extracted certificate.

The pinned foundation is PR177 at
`00a611094043afeb256d6532b477c0709e8ed270`, including
`Collatz/Witness.lean`, `Collatz/GapMultiset.lean`, and the comparison and
handoff modules used by this pass. The current PR175 packet at
`2055b8a311ab87d07bffc730154a7f8546fe382c`
adds `CollatzGlobalClosure/TerminalReset.lean` and the common core-only build.
The reductions here use the exact `certificate_cons_iff` decomposition and
the comparison kernel `CollatzGapComparison`; they do not assume an
unproved source-word selector.

## 1. Odd psi sources reduce to one predecessor comparison

The mandatory query is

\[
\Psi(n):\quad\operatorname{Basin}(n)\Longrightarrow
                     \operatorname{Basin}(2n-1),\qquad n>0.
\]

If the supplied odd source has first gap \(a\), equation (1) gives

\[
T^2(2n-1)=\frac{3n-1}{2}=2^{a-1}r-1.
\tag{3}
\]

For **\(a\ge2\)** this is another psi target, with actual child source
\(2^{a-2}r\). The child powered certificate is `(a-2, tail)`. Its only
possible new initial even grade is \(2a-3<2a\); the full tail is retained.
Thus the required recursive source has strictly smaller rank.

For **\(a=1\)** the target in (3) is \(r-1\). Here \(n\ge3\), so
\(r\ge5\). Deleting the actual first source gap permits the lower query

\[
\operatorname{Pred}(r):\quad
r>1\text{ odd},\qquad
\operatorname{Basin}(r)\Longrightarrow\operatorname{Basin}(r-1).
\tag{4}
\]

For `Pred(u)`, write its own supplied certificate as
\(3u+1=2^b v\), with actual suffix certificate for \(v\).

| Guard on the supplied gap | Exact reduction | Certificate accounting |
|---|---|---|
| \(b=1\) | \(\operatorname{Basin}(u-1)\iff\operatorname{Basin}(v-1)\), with \(v>1\) | The actual suffix supplies `Pred(v)`; delete grade 2. |
| \(b\ge3\) | \(u=4r+1\), \(r\) positive odd, and \(3r+1=2^{b-2}v\); hence \(\operatorname{Basin}(u-1)=\operatorname{Basin}(4r)\) follows directly | Construct the actual complete certificate `(b-2) :: tail` of \(r\); no further comparison is needed. |
| \(b=2\) | \(u=8s+1\), \(s>0\), \(v=6s+1\), and \(\operatorname{Basin}(u-1)\iff\operatorname{Basin}(s)\) | Consume grade 4 and retain the supplied complete suffix certificate of \(6s+1\). |

The last row produces the specific remaining family

\[
\boxed{\operatorname{Basin}(6s+1)\Longrightarrow
       \operatorname{Basin}(s),\qquad s>0.}
\tag{5}
\]

The target transport in each row is reversible along actual shortcut
steps. In the second row, \(b\ge3\) implies \(u\equiv5\pmod8\), making
\(r=(u-1)/4\) odd. In the third row, exact \(b=2\) gives
\(u\equiv1\pmod8\). The guard \(u>1\) is needed for \(s>0\).

Repeated gap-two steps do not disappear for free. If \(k\) such source
steps take \(u\) to \(v\), then
\(u-1=(4/3)^k(v-1)\). The remaining target therefore retains a division
by \(3^k\), with integrality supplied by the original source. A later
high gap constructs a certificate for a corresponding multiple, but
removing that multiple still requires a covered comparison.

## 2. Why the carry family has not yet become a complete rule

There are useful exact subcases of (5), but they expand the comparison
shapes instead of closing them.

* If \(s\) is odd, its target step is \(t=(3s+1)/2\). The source
  \(6s+1\) has exact gap one and successor \(9s+2=6t-1\).
  Thus the supplied suffix reduces (5) to `(source 6t-1, target t)`.
* If \(s=2t\) with \(t\) odd, \(12t+1\) has first gap \(a\ge3\).
  From \(36t+4=2^a v\) one constructs the complete certificate
  `(a-2) :: tail` of \(3t\). A lower reverse-tripling query `(3t,t)`
  would close this subcase.
* For `(6t-1,t)`, an even \(t=2r\) consumes a source gap one and becomes
  `(18r-1,r)`. For odd \(t\), putting \(w=(3t+1)/2\) instead gives
  \(3w-2=2^{b-2}v\), where \(b\ge2\) is the supplied source gap.
  Its exact powered suffix is available, but the comparison shape has
  changed again.

Consequently the strongest ordinary-certificate candidate from this
branch is a uniform carry dispatcher that handles these affine
source/target pairs while constructing every child certificate from a
strictly spent supplied prefix. Listing more residue cases does not prove
that such a dispatcher is complete. In particular, sequential applications
of reverse-tripling or psi cannot reuse an output as a new ranked source
without a separate output-certificate bound.

## 3. The terminal reset does not extend to the fixed general child

The checked `TerminalReset` rule closes all power-of-two *source cases
inside the common induction*. For \(e\ge4\) it replaces the source
\(2^e\) by \(3\cdot2^{e-1}\), using the explicit complete word `[1,4]`
of 3 and preserving any complete terminal tail of 1. The new grades
\(2e-1,2,8\) all lie below \(2e+1\). The remaining four exponents
are explicit terminal cases.

For a general supplied source \(2^e q\), the analogous target identity is
still exact:

\[
T(2^{e+1}q-1)=2(3\cdot2^{e-1}q)-1,\qquad e\ge1.
\tag{6}
\]

But its required child certificate need not have smaller rank. The
supplied word of \(q=7\) is `[1,1,2,3,4]`. Every complete certificate of
\(3q=21\) starts with gap 6, since \(3\cdot21+1=64\). For
\(1\le e\le5\), the parent grades are all at most 11, whereas the
child in (6) has the unavoidable odd grade 12. Terminal gap-two padding
does not remove it. In particular source \(112=2^4\cdot7\) would require
child \(168=2^3\cdot21\), whose grade 12 exceeds the parent maximum 9.
Thus (6) cannot be the universal rank-decreasing general rule.

## 4. A continuation stack avoids intermediate certificate reuse

Define \(\Phi_e(z)=2^{e+1}z-1\). A nested target can be kept intact,
rather than proving its inner query and extracting a new source
certificate. If \(e_1,\ldots,e_k\ge1\) and the actual bottom source has
first gap \(a\), then one target step gives

\[
\begin{aligned}
T\bigl(\Phi_{e_1}\cdots\Phi_{e_k}(q)\bigr)
={}&\Phi_{e_1-1}\Phi_0\Phi_{e_2-1}\Phi_0\cdots\\
 &\qquad\Phi_0\Phi_{e_k-1}\Phi_{a-1}(r).
\end{aligned}
\tag{7}
\]

This follows from \(3\Phi_f(z)=\Phi_0\Phi_{f-1}(3z)\) for \(f\ge1\)
and \(3q=\Phi_{a-1}(r)\). If every context \(\Phi_e\), including
\(e=0\), is charged grade \(2e+1\), the whole new stack in (7) has
strictly smaller multiset rank: old context grades decrease by two,
\(k-1\) grade-one contexts are added, and source grade \(2a\) becomes
context grade \(2a-1\). The complete actual source tail is unchanged.
This is a **single** possible induction query on the nested target, so
it does not assume a bound on a returned certificate.

Some initial zero runs also have direct descending rewrites. Let \(U\)
denote the accelerated odd map. For odd \(w>0\), \(f\ge2\),

\[
U(\Phi_0\Phi_f(w))=\Phi_{f-2}(3w),
\tag{8}
\]

and for \(k\ge2\), \(f\ge2\),

\[
U(\Phi_0^k\Phi_f(w))
=\Phi_0^{k-2}\Phi_1\Phi_{f-2}(3w).
\tag{9}
\]

The exact odd gaps are 3 and 2 respectively. The old context grade
\(2f+1\ge5\) pays for grades \(3\) and \(2f-3\); propagating the
remaining factor 3 requires additional covered rules or a supplied
source gap. Formulas (8)--(9) are not an arbitrary-stack termination
proof.

The unresolved zero-context carry can increase this rank. For example,

\[
9=\Phi_0\Phi_0\Phi_1(1),\qquad
U(9)=7=\Phi_2(1),
\]

so grades \(\{1,1,3\}\) become \(\{5\}\). The ordinary one-step
example \(35=\Phi_1\Phi_0\Phi_0\Phi_1(1)\) to
\(53=\Phi_0\Phi_1\Phi_2(1)\) likewise replaces
\(\{3,1,1,3\}\) by \(\{1,3,5\}\). These are failures of this
particular ranking proposal, not failures of convergence.

More generally, a continuation \(N=2^Bq-C>0\), \(B\ge1\), updates
exactly as

\[
\begin{array}{ll}
C\text{ odd}:&
T(N)=2^{B+a-1}r-
  \left(2^{B-1}+\dfrac{3C-1}{2}\right),\\[4pt]
C\text{ even}:&T(N)=2^{B-1}q-C/2.
\end{array}
\tag{10}
\]

The odd case consumes the actual supplied bottom-source gap. After all
such gaps are consumed, its terminal offset is a general \(2^B-C\),
which is outside the specific Mersenne terminal reset. A new ranking or
carry normalization must cover that residual family rather than assume
its convergence.

## Remaining full-closure candidate

The strongest candidate from this attempt is a single induction on an
actual supplied complete source certificate **and a charged affine
continuation**, with rules that consume source prefixes and normalize
the resulting carries. Equations (3)--(5) identify its first mandatory
ordinary carry family; equations (7)--(10) retain the complete target
without reusing an unranked intermediate certificate. What is missing is
a well-founded measure and a total rule for the zero-context/affine
carry cases, including the general terminal offsets. The current
terminal reset, actual suffix accounting, and positive-context rules do
not establish that missing termination statement.
