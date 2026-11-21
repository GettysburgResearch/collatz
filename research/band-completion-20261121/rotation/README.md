# Rotation, integer height, and the short-return obstruction

**Status: locally Lean-checked at the statements below. Full Collatz remains open.**
This is a direct attempt to extract ordinary descent from the forced narrow
dyadic band in PR 173. The outcome is a positive descent certificate for short
marked returns, together with an explicit ordinary family showing why the
existing forcing argument cannot supply that certificate at every start.

## Source and normalization

The source pin is PR 173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`, specifically
`research/lean-shell-cover/{ShellCover,ForwardSection,SectionDynamics,RisingReturns}.lean`.
The map is the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

Write \(x_j\) for the odd-only orbit of an odd positive source \(n\):
\(x_{j+1}=(3x_j+1)/2^{a_j}\), where
\(a_j=v_2(3x_j+1)\). A mark is an odd positive \(x\) satisfying

\[
(d_x+1)(x-2^{d_x})\le70\,2^{d_x},
\qquad d_x=\lfloor\log_2x\rfloor.
\]

All clocks below count odd-only steps. The source theorem that every positive
integer reaches a mark counts shortcut steps, and the clocks must not be
interchanged.

## 1. Keep the actual integer valuation sum

Put

\[
\alpha=\log_2 3,\qquad
A_j=\sum_{i<j}v_2(3x_i+1),\qquad
E_j=\sum_{i<j}\log_2\left(1+\frac1{3x_i}\right).
\]

The exact identity is

\[
\boxed{\log_2x_j=\log_2n+j\alpha-A_j+E_j.}
\]

If all \(x_i\ge m>0\) for \(i<j\), then
\(0\le E_j\le j/m\). The new module defines both sums using the actual
ordinary orbit and proves this identity as `exact_height`, with the bound in
`error_sum_bounds`. Thus the integer part has not been hidden in an
existential approximation variable.

To force \(x_j<n\), the identity requires
\(A_j>j\alpha+E_j\). A phase target controls the fractional part of the
identity; it does not by itself supply this inequality for the actual
valuation sum. Changing the target phase changes that fractional condition.
The same missing integer inequality remains.

## 2. A one-sided estimate for every non-descending marked return

A marked value has logarithmic offset

\[
0\le\eta_x:=\log_2x-d_x\le\frac{140}{d_x+1}.
\]

Suppose \(n\) and \(x_j\) are marked and every odd value through clock
\(j\) is at least \(n\). Then \(d_{x_j}\ge d_n\), so

\[
b=A_j+d_{x_j}-d_n
\]

is a nonnegative integer. The exact identity becomes

\[
j\alpha-b=\eta_{x_j}-\eta_n-E_j.
\]

Both endpoint offsets are nonnegative. Consequently their contribution is
bounded by one window width, rather than the sum of two widths:

\[
\boxed{\quad
|j\alpha-b|\le\frac{140}{d_n+1}+\frac jn.
\quad}
\]

This is `marked_return_approx`. It applies to arbitrary actual marked
returns that have not descended; no rising-prefix assumption is used.

## 3. A short marked return certifies ordinary descent

Let \(H\ge0\) and suppose

\[
(d_n+1)H\le n,
\qquad
141(4^H+1)\le d_n+1.
\]

Then any positive marked return at an odd clock \(j\le H\) forces
an ordinary orbit value smaller than \(n\).

Indeed, otherwise every odd value through \(j\) is at least \(n\).
The preceding approximation gives

\[
|j\alpha-b|
\le\frac{141}{d_n+1}
\le\frac1{4^H+1}.
\]

The source theorem `grid_barrier`, based on the separation of the distinct
integers \(3^j\) and \(2^b\), then gives

\[
4^H+1\le4^j\le4^H,
\]

a contradiction. `early_marked_return_forces_descent` concludes
\(\exists y<n,\;\mathrm{Hits}(n,y)\), where `Hits` means a finite ordinary
shortcut trajectory. The no-descent assumption appears only inside its
proof, not in its statement.

The certificate window is roughly
\(H\le\log_4((d_n+1)/141-1)\), which is of order
\(\log\log n\). The existing forced-visit bound is of order
\(\sqrt n\), and its induced positive return need not be in this short
window. These are quantitatively different obligations.

## 4. The short forcing complement is false for ordinary integers

For every prescribed \(H\), choose

\[
m=2H+10,\qquad d=2^m,\qquad
n=2^{d-m}(d+1)-1.
\]

The leading bits and trailing bits perform separate roles:

\[
n=2^d+2^{d-m}-1.
\]

The positive offset above \(2^d\) is about \(2^d/d\), so \(n\)
is marked. In fact, its defining band inequality has the stronger bound

\[
(d+1)(n-2^d)\le2\,2^d.
\]

The last \(d-m\) binary digits are all ones. For every
\(0\le j\le H<d-m\), the actual ordinary trajectory obeys

\[
T^j(n)+1=3^j2^{d-m-j}(d+1),
\]

and every term in this window is odd. Thus the shortcut and odd-only
clocks agree there, and all these values are at least \(n\).

The same family satisfies both numerical budgets of the descent
certificate. In particular,

\[
d=1024\,4^H\ge141(4^H+1)-1.
\]

It follows that there is no positive marked visit at any odd clock at
most \(H\). The theorem `short_return_window_can_be_empty` verifies all
of these assertions for every \(H\), using this explicit ordinary
construction rather than changing finite witnesses without a common
source inside a single window.

This rules out the proposed completion step “the forced mark can always be
chosen inside the early-return certificate window.” It does not rule out
eventual descent after the window or any argument that accumulates enough
actual valuation information across longer returns.

The upstream `RisingReturns.lean` already proves that first returns can
expand by arbitrarily large factors. This packet does not claim that
phenomenon as new. Its additional result is the early-return descent
certificate for arbitrary non-descending marked orbit segments, together
with an explicit family satisfying the certificate's two numerical budgets
while having no return in the certificate window.

## 5. What this attempt did not establish

The complete-proof target was to use repeated or adaptively chosen leading
phase visits to force eventual ordinary descent. The exact identity and
the return-spacing theorem do not force
\(A_j>j\alpha+E_j\) at some clock for every fixed positive ordinary
source. The short-clock steering substitute is disproved by the explicit
family above. A successful continuation must control actual valuations
across the longer return blocks, or supply a different global ordinary
invariant. Neither irrational rotation recurrence nor the positivity of
\(E_j\) alone has supplied that control here.

## Formal artifact

The new source is [BandRotation.lean](../lean/BandRotation.lean). It imports
the build module generated from the pinned `ForwardSection.lean`, uses no
`sorry`, custom axioms, or `native_decide`, and prints the dependencies of
the main theorems. The exact upstream files are retained in `lean/vendor`;
the build uses the documented module/import/export visibility adjustments
to support Lean 4.34.1's `module` syntax and `@[expose] public section`.
The packet's build driver records the full transformation; the upstream
vendor files remain byte-identical to the frozen source.

The full `BandRotation.lean` compiled successfully on 2026-11-21 with Lean
4.34.1, mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, one compiler
worker, and warnings treated as errors:

```sh
lean -j1 -DwarningAsError=true -o .build/BandRotation.olean BandRotation.lean
```

The successful source SHA256 is
`ae451eae34c9964537bc447ce973778fd01e05b404298ffdc5e20a330db18c9d`.
All five printed main theorem audits reported only `propext`,
`Classical.choice`, and `Quot.sound`. The file contains no `sorry`, custom
axioms, or `native_decide`. This local kernel replay checks the stated
results; it does not supply the missing global valuation argument or an
independent mathematical review of this packet.
