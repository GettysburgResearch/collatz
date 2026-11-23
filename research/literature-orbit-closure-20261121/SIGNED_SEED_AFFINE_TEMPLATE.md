# Signed-seed scaffolds for different affine merger intercepts

Research checkpoint, 2026-11-21 UTC. This note contains exact written algebra
and a small executable arithmetic certificate. It is not an additional
Lean-checked theorem and does not assert a universal cover.

## General positive theorem

Extend the shortcut map to all integers by the same parity formulas. Suppose
one particular negative odd integer \(-m\), \(m>0\), reaches \(-1\) in
\(a\) steps, with \(p\) odd steps in that verified finite trajectory.
For an ordinary integer \(v>0\), set

\[
n=2^{a+1}v-m,\qquad x=2^a v-m,
\qquad A=3^p v.
\]

Assume \(x>0\) and \(A\equiv3\pmod4\). Then

\[
0<x<n,\qquad 2x+m=n,\qquad
T^{a+2}(x)=T^{a+3}(n).
\]

This is a source-half merger with intercept \(-m/2\). It need not be the
previous pure-erasure partner \((n-1)/2\).

### Proof

For \(0\le h\le a\), let \(p_h\) count the odd steps in the first \(h\)
steps of the fixed negative trajectory. Induction on \(h\) gives

\[
T^h(n)-T^h(-m)=3^{p_h}2^{a+1-h}v,
\qquad
T^h(x)-T^h(-m)=3^{p_h}2^{a-h}v.
\]

For \(h<a\), each difference is even, so the two positive trajectories and
the negative scaffold have identical parity at that step. This justifies the
induction; no probabilistic parity substitution is used. At \(h=a\),

\[
T^a(n)=2A-1,\qquad T^a(x)=A-1.
\]

The first value is odd and \(T(2A-1)=3A-1\). For \(A\equiv3\pmod4\), the
already proved two-clock diamond says

\[
T^2(A-1)=T^2(3A-1).
\]

Combining the formulas proves the merger. All trajectory inputs used in the
conclusion are positive ordinary integers. The negative orbit is only a finite
algebraic device for certifying a parity word.

This theorem assumes one explicit finite negative trajectory, not convergence
of all negative inputs. Negative Collatz has other cycles, so that stronger
assumption would be false.

## Concrete new-intercept cylinder

The verified negative trajectory is

\[
-53,-79,-118,-59,-88,-44,-22,-11,-16,-8,-4,-2,-1.
\]

It has \(a=12\), \(p=4\), and parity word `110100010000`. Taking
\(v=4t+3\), \(t\ge0\), yields

\[
n=32768t+24523,\qquad x=16384t+12235=\frac{n-53}{2}.
\]

The exact physical certificate is

\[
\boxed{T^{14}(16384t+12235)=T^{15}(32768t+24523)=243t+182.}
\]

The source word is `110100010000100`, and the partner word is
`11010001000001`. The executable companion checks the integer affine
coefficient and constant at every step; it does not merely sample numerical
values of \(t\).

### Direct marked preservation on this cylinder

Suppose this \(n\) is marked, and put \(d=\lfloor\log_2 n\rfloor\),
\(\rho=n-2^d\). Since \(n\ge24523\), we have \(d\ge14\). Also
\(n\equiv-53\pmod{8192}\), so

\[
\rho\equiv8139\pmod{8192},\qquad \rho\ge8139>53.
\]

Thus

\[
x=2^{d-1}+\frac{\rho-53}{2},\qquad
\lfloor\log_2x\rfloor=d-1.
\]

The partner is odd, and

\[
d\frac{\rho-53}{2}
\le\frac{(d+1)\rho}{2}
\le70\,2^{d-1}.
\]

Hence \(x\) is marked. This is a direct lower marked-component merger,
without a separate return-height bound.

For example, every
\(n_d=2^d+24523\), \(d\ge15\), is a source in this cylinder and is marked:
the band inequality holds at \(d=15\), and its right-hand side doubles while
its left-hand side grows by a factor less than two as \(d\) increments. Its
marked partner is \(2^{d-1}+12235\).

### Exact limit of this example

This cylinder already has ordinary forward descent after 12 steps:

\[
T^{12}(n)=648t+485<n.
\]

Thus it does not improve ordinary least-counterexample exclusion. Its useful
feature is the direct *marked* smaller partner with a different intercept.
The cylinder is \(75\pmod{128}\), disjoint from the current 446-row packet's
source cylinder \(27\pmod{128}\). No completeness or priority claim follows
from that observation.

Appending repeated \(-1\to-1\) steps to the negative certificate produces
longer parameterized clocks, but by itself does not produce a universal marked
cover. The first unsupported step in a proposed completion would be to claim
that every remaining marked word admits one of these signed-seed reductions,
or that the resulting partners remain in a closed terminating language. No
such cover or closed language has been proved.
