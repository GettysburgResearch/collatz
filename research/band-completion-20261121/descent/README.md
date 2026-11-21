# The offset-certificate completion attempt

**Status: OPEN.** This route does not complete Collatz. It does produce an
explicit sufficient certificate for descent of the actual marked-return map,
not just an ordinary one-step or finite-clock decrease. It also identifies an
infinite, exponentially thin family on which the proposed universal offset
clock fails. Proofs are given below, with a formalization in
[`../lean/BandDescent.lean`](../lean/BandDescent.lean). **Lean checked:** the
complete module compiled with Lean 4.34.1, `-j1 -DwarningAsError=true`, against
the freshly compiled pinned dependencies. Its printed main theorems use only
`propext`, `Classical.choice`, and `Quot.sound`; no `sorry`, custom axiom, or
`native_decide` is used. The exact source hash and execution receipt are in
[the local receipt](../../../reports/band-completion-20261121/band-descent-local.json). The successful and outer-band family
specializations that are explicitly identified as mathematical calculations
below are not additional claims of Lean verification.

## Map and source boundary

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

The imported section is exactly PR 173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`, files
`research/lean-shell-cover/{ShellCover,ForwardSection,SectionDynamics}.lean`.
For a positive odd integer \(x\), put \(d=\lfloor\log_2x\rfloor\). It is marked
when

\[
(d+1)(x-2^d)\le70\,2^d.
\]

The source supplies a marked visit from every positive \(y\) in fewer than
\(4\lfloor\sqrt y\rfloor+\lfloor\log_2y\rfloor\) ordinary clocks. Its
`collatz_iff_return_descent` theorem requires a *marked* value below each marked
start, after finitely many complete positive returns. A decrease to an
unmarked endpoint is insufficient on its own.

## 1. The exact low-bit borrowing calculation

Let \(q_k(u)\) count the odd inputs among the first \(k\) shortcut steps from
\(u\). For all nonnegative integers \(k,u,h\),

\[
T^k(2^kh+u)=3^{q_k(u)}h+T^k(u).
\tag{1}
\]

This is an identity about ordinary inputs and their actual parities, not a
formal parity word. Induction uses
\(T(2a+b)=3^{b\bmod2}a+T(b)\). In particular, for \(k\le d\),

\[
T^k(2^d+u)=3^{q_k(u)}2^{d-k}+T^k(u).
\tag{2}
\]

The nonnegative affine remainder gives

\[
3^{q_k(u)}u\le2^kT^k(u).
\tag{3}
\]

Thus a strict descent \(T^k(u)<u\) forces \(3^{q_k(u)}<2^k\), and (1) proves
strict descent at the same clock for every translate \(2^kh+u\). A
non-strict endpoint \(T^k(u)\le u\) also works if the coefficient is strictly
contracting and \(h>0\). This includes the offset \(u=1\), whose two-clock
cycle has coefficient \(3/4\).

The shared-prefix budget is exact. At clock \(d\), the difference between the
two orbits is \(3^{q_d(u)}\), which is odd. Therefore their next input parities
are opposite. There is no lawful extension of the same certificate past
clock \(d\) without a fresh argument.

Lean names: `prefix_lift`, `coefficient_lower`, `descent_lift`,
`nonincrease_lift`, `offset_lift`, `offset_boundary_parity`, `offset_descent`.

## 2. A certificate that really decreases the marked-return dynamics

The first attempt stopped too early: ordinary descent of a marked \(x\)
need not produce a lower marked return. The endpoint may be unmarked, and the
next marked visit can exceed \(x\). The following stronger calculation closes
that particular transport gap.

Suppose \(u>0\), \(k\le d\), and a complete ordinary certificate gives
\(T^k(u)=1\). Equations (2) and (3) imply

\[
y:=T^k(2^d+u)
 =1+3^{q_k(u)}2^{d-k}
 \le 1+\left\lfloor\frac{2^d}{u}\right\rfloor=:B.
\tag{4}
\]

Assume the explicitly computable guard

\[
\boxed{4\lfloor\sqrt B\rfloor+2\lfloor\log_2B\rfloor\le d.}
\tag{5}
\]

Take the bounded marked visit \(T^t(y)\), where
\(t<4\lfloor\sqrt y\rfloor+\lfloor\log_2y\rfloor\). The elementary upper
bound \(T^t(y)\le2^ty\), together with
\(y<2^{\lfloor\log_2y\rfloor+1}\), gives

\[
T^t(y)
 <2^{t+\lfloor\log_2y\rfloor+1}
 \le2^d
 <2^d+u.
\tag{6}
\]

This endpoint is marked. The source theorem `captures` places it in the
actual induced-return orbit. Consequently some finite induced return of
\(2^d+u\) is strictly smaller than \(2^d+u\).

This is a universal certificate theorem, with every guard and endpoint in
ordinary integers. It applies regardless of how the certificate of \(u\) was
obtained. It proves no assertion that all offsets possess such a certificate.
The key Lean theorem is `offset_certificate_return_descent`.

The guard is useful near the outer part of the original band. If
\(u\) is comparable to \(2^d/d\), (4) makes \(B\) comparable to \(d\), and
(5) eventually holds. The unproved condition in that regime is the complete
certificate clock \(k\le d\).

The guards have an explicit unbounded family of successes. For \(a\ge4\),
take \(k=4^a\), \(d=k+2a\), and \(u=(2^k-1)/3\). Since \(k\) is even,
\(u\) is an odd integer, its first step reaches \(2^{k-1}\), and the next
\(k-1\) halvings reach one. Also \(u\ge2^k/4\), so
\(B\le4k+1\). Consequently

\[
4\lfloor\sqrt B\rfloor+2\lfloor\log_2B\rfloor
\le8\,2^a+4a+4\le4^a+2a=d.
\]

The start \(x=2^d+u\) is marked because
\((d+1)u\le70\,2^d\). The theorem therefore supplies a lower actual
marked return for every member of this family. This family calculation is
given mathematically; the generic theorem is the formalized result. It is a
successful guarded family, not a complete section cover.

## 3. The universal quick-offset rule fails on an unbounded family of scales

For \(a\ge1\), set

\[
u_a=2^{2a}-1,
\qquad x_a=2^{3a}+u_a.
\]

These ordinary integers satisfy all of the following:

1. \(\lfloor\log_2x_a\rfloor=3a\).
2. \(x_a\) is marked in the exact source section.
3. Their relative offsets are exponentially small:
   \(2^a(x_a-2^{\lfloor\log_2x_a\rfloor})
     <2^{\lfloor\log_2x_a\rfloor}\).
4. For every \(0\le j\le3a\),
   \(T^j(u_a)\ge u_a\) and \(T^j(x_a)\ge x_a\).

To prove the fourth assertion, write either start as
\(2^{2a}v-1\), with \(v=1\) or \(v=2^a+1\). The first \(2a\) steps are
odd and nondecreasing, ending at \(3^{2a}v-1\). At every later clock, one step
decreases by at most a factor of two. Even \(a\) further maximal halvings
cannot go below the start, because

\[
2^a(2^{2a}v-1)\le3^{2a}v-1
\]

follows from \(8^a\le9^a\). This is a symbolic all-parameter proof, not a
bounded experiment or an extension of the already proved expanding-first-return
family in `RisingReturns.lean`.

In particular, replacing the marked band by an exponentially narrower leading
interval does not force the offset's stopping time, or its full convergence
clock, to fit within the available \(d\) bits. The sufficient certificate
from Section 2 excludes this infinite family. This fact does not assert
nonconvergence of any member.

Lean names: `thin_depth`, `thin_marked`, `thin_relative_offset`,
`thin_offset_no_descent`, `thin_start_no_descent`, `thin_no_quick_certificate`.

### The same clock failure where the small-endpoint guard already holds

There is also a family in the relevant outer part of the band. For \(a\ge4\),
put

\[
d=4^a,\qquad b=d-2a,\qquad u=2^b-1,\qquad x=2^d+u.
\]

Here \(d+1\le70\,2^{2a}\), so \(x\) is marked; its relative offset is
approximately \(1/d\). The integer \(b\) is even, and \(d\ge6a\), whence

\[
3^b=9^{b/2}\ge8^{b/2}=2^{3b/2}\ge2^d.
\]

The generic theorem `offset_pair_no_descent` therefore proves that both
\(u\) and \(x\) stay at least as large as their initial values throughout all \(d\) clocks.
But \(u\ge2^{b-1}\), so

\[
B=\left\lfloor\frac{2^d}{u}\right\rfloor+1\le2d+1.
\]

Consequently \(\lfloor\sqrt B\rfloor\le2^{a+1}\) and
\(\lfloor\log_2B\rfloor\le2a+1\). The inequality
\(8\,2^a+4a+2\le4^a=d\), valid for every \(a\ge4\) by induction, verifies
the guard (5). Thus the missing rapid certificate is an actual failure even
where the later transport back to the section has enough room. The
specialization inequalities in this paragraph are ordinary mathematical
proofs; the generic survival implication is included in the Lean file.

## 4. Attempts to make the transformation total

### Borrow the offset's known convergence certificate

For a fixed convergent \(u>1\), some clock \(k\) exists, and every translate
\(2^d+u\) with \(d\ge k\) has ordinary descent. This quantified statement is
proved by `convergent_offset_eventually_lifts`. It cannot be made uniform over
\(u\le70\,2^d/(d+1)\) by exchanging the quantifiers. The family in Section 3
refutes that exchange even for strict stopping, which is weaker than hitting
one.

Induction has a separate issue. Induction over marked starts does not already
certify every smaller unmarked offset: that offset's first guaranteed marked
visit may be larger than the current start. Conversely, a global least
nonconvergent ordinary integer \(N\) certifies all \(u<N\), but a marked
point \(x\) on its orbit may satisfy \(x>N\) and have offset \(u\ge N\).
Even a decrease from such an \(x\) need not cross below \(N\).

### Continue the comparison after its carry boundary

At clock \(d\), write the two endpoints as \(b\) and \(b+A\), where
\(A=3^{q_d(u)}\) is odd. Their next parities are opposite. If \(b\) is even,
the new difference is

\[
\frac{3A+2b+1}{2};
\]

if \(b\) is odd, the signed new difference is

\[
\frac{A-2b-1}{2}.
\]

These identities supply the exact carry/borrow terms, but neither gives an
always decreasing ordinary resource. Once the smaller orbit reaches the
\(1,2\) cycle, the coupled recurrence still contains the unrestricted dynamics
of the larger integer. Knowing the smaller orbit has ended does not end the
larger one.

### Steer the leading phase adaptively

To force an offset below a fixed certified threshold \(N\), an orbit value
\(x\) near \(2^d\) would need relative error below approximately \(N/x\).
The source visit theorem supplies a relative error of order \(1/\log x\).
Along a potentially growing ordinary orbit, the required target can shrink
exponentially in the clock, while the available target shrinks only with the
logarithmic height. The source irrational-rotation proof provides no estimate
bridging these scales. Its finite grid argument cannot simply be reused with
an input-dependent, exponentially smaller target.

One can also try to exploit the predictable \(1,2\) cycle after a short
offset certificate, while unused low bits remain. The resulting terms have
the exact form \(1+3^J2^e\). Their leading phases are samples of
\(J\log_2 3\). A uniform one-sided return within the remaining linear bit
budget would require an additional quantitative approximation statement;
the source's inverse-logarithmic visit theorem does not establish it. The
small-endpoint estimate in Section 2 avoids that extra assertion when its
explicit guard holds.

## Exact first unsupported step and remaining closure target

The proposed universal claim

> Every marked \(2^d+u>1\) has a complete offset certificate by clock \(d\).

is **REFUTED** by Section 3. Replacing "complete" by "strict stopping" does
not repair it.

The remaining route would have to cover the failed offsets by a *different*
finite ordinary transformation, and prove that the combined transformations
always reach a lower marked integer under one well-founded order. Neither
the existence of marked visits nor the exact lifting identities supply that
coverage or termination. No unproved total selector is invoked, and no
Collatz conclusion is claimed.
