# A sublinear first-crossing kernel at every depth

**Status:** complete written arithmetic deduction, with the actual finite
crossing and coefficient core verified separately in `FirstCrossingBound.lean`.
The native no-descent counting estimate is a pinned, elementary written
input; it is not installed as a Lean axiom. No Collatz convergence claim.

The new estimate sums every admissible first-hitting clock at a supplied
target. Neither the number of odd steps nor their valuations is bounded.
The saving comes from charging each physical source once, at its last
upcrossing of a height floor, and then counting the possible sources.

## 1. Actual sources, first hits, and word weights

Use the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

Fix integers \(H\ge2\) and \(q\ge H\). Let \(E_H(q)\) consist of the
positive integers \(n<H\) for which there is an integer \(A\ge1\) such that

\[
T^A(n)=q,\qquad T^j(n)\ge H\quad(1\le j\le A),
\qquad T^j(n)\ne q\quad(0\le j<A).
\tag{1}
\]

Thus the source lies below the floor, its next state is above the floor,
and it stays above the floor until its **first** hit of \(q\). The first-hit
condition makes \(A=A_q(n)\) unique. An even source cannot satisfy (1),
since its first step would decrease. If \(q\) is odd, (1) is equivalently
an odd inverse word whose source is its first point below \(H\), with
first hitting imposed at \(q\). The intermediate even states introduce
no extra exception: each halving segment decreases to its next odd state.

Let \(s_q(n)\) be the number of odd shortcut steps before this first hit,
and put

\[
\omega_q(n)=3^{s_q(n)}2^{-A_q(n)}.
\tag{2}
\]

The affine branch identity has nonnegative correction, so

\[
q\ge \omega_q(n)n.
\tag{3}
\]

The sum below is over the entire set of sources in (1). It is finite
because \(n<H\), even though there is no prescribed bound on \(A_q(n)\).
These are sources of the crossing segments; distinct original upstream
histories may already have merged at one such boundary source. Their
arriving masses are not included in an unweighted boundary sum.
For a nonperiodic target this includes every reverse first-downcrossing
path. For a periodic target the first-hit qualification is essential:
repeated circuits through \(q\) are not additional physical sources.

## 2. The all-depth late-boundary theorem

Set \(N_H=\lfloor\log_2 H\rfloor\), and define

\[
E_H^{\rm late}(q)=\{n\in E_H(q):A_q(n)\ge N_H\}.
\]

Let

\[
\mathcal N(H)=\{1\le n\le H:T^j(n)\ge n
                      \text{ for every }0\le j\le N_H\}.
\tag{4}
\]

The native no-descent bound recorded in the repository is

\[
\#\mathcal N(H)\le6499+2H^{19/20}.
\tag{5}
\]

### Theorem 1

For every \(H\ge2\) and \(q\ge H\),

\[
\boxed{
\sum_{n\in E_H^{\rm late}(q)}\omega_q(n)
\le\frac{3q}{2H-1}\bigl(6499+2H^{19/20}\bigr).
}
\tag{6}
\]

This estimate includes arbitrarily large hitting clocks and arbitrarily
large odd gaps.

**Proof.** The first step in (1) gives

\[
H\le T(n)\le(3n+1)/2,
\qquad\text{hence}\qquad
\frac{2H-1}{3}\le n<H.
\tag{7}
\]

Every late source stays above \(H>n\) during its first \(N_H\) steps,
so it lies in \(\mathcal N(H)\). Equations (3) and (7) imply

\[
\omega_q(n)\le\frac qn\le\frac{3q}{2H-1}.
\]

Sum this bound over the distinct late boundary sources and apply (5). No
sum over possible clocks remains, and no distinct boundary sources have
been identified.
\(\square\)

The proof applies more generally at any chosen horizon \(N\): replace
\(N_H\) by \(N\) and the right side by
\(3q\#\mathcal N(H;N)/(2H-1)\). This is the exact formal interface.

## 3. An unrestricted first-crossing bound for large targets

Every shortcut step satisfies

\[
T(x)+1\le\tfrac32(x+1).
\]

Thus a crossing source satisfies

\[
q+1\le(3/2)^{A_q(n)}(n+1)
       \le H(3/2)^{A_q(n)}.
\tag{8}
\]

Consequently, if

\[
q+1>H(3/2)^{N_H},
\tag{9}
\]

every crossing source is late. Theorem 1 then gives the **whole** boundary
bound

\[
\boxed{
\sum_{n\in E_H(q)}\omega_q(n)
\le\frac{3q}{2H-1}\bigl(6499+2H^{19/20}\bigr)
\le q\left(\frac{19497}{H}+6H^{-1/20}\right).
}
\tag{10}
\]

The final estimate uses \(2H-1\ge H\). All statements up to the native
cardinality substitution are proved for the actual map in the Lean module.

### A convenient exact scale

For every integer \(m\ge1\), take \(H=2^m\) and any \(q\ge3^m\).
Then \(N_H=m\) and \(H(3/2)^m=3^m<q+1\). Hence

\[
\boxed{
\sum_{n\in E_{2^m}(q)}\omega_q(n)
\le\frac{3q}{2^{m+1}-1}
       \left(6499+2\,2^{19m/20}\right).
}
\tag{11}
\]

Let \(a=\log_3 2\), and for \(q\ge3\) choose the largest \(m\) with
\(3^m\le q\). Then \(H=2^m>q^a/2\). In particular,

\[
\boxed{
\sum_{n\in E_{2^m}(q)}\omega_q(n)
\le38994q^{1-a}+6\,2^{1/20}q^{1-a/20}
=O\!\left(q^{1-(\log_3 2)/20}\right).
}
\tag{12}
\]

The exponent of the leading power is approximately \(0.968454\). This is
an actual pointwise sublinear estimate on an entire first-crossing kernel,
uniform over every target at that scale. It is not a bound on \(D_k(q)\),
\(V(q)\), or the full inverse Green kernel.

## 4. Why the count in (5) is the correct source count

The pinned source is PR176 at
`c83a8459066d8223aefe7fc5f6b75faeea557345`,
`research/external/mazur-2026/fixed-height-forward-power-saving.md`,
claim **MZ-FH-001**, equations (2)--(7). Its native horizon is exactly
\(N_H\) for all sources \(n\le H\), as in (4), rather than a horizon
silently evaluated at the larger target \(q\).

For completeness, its counting proof is elementary. If \(n\ge6500\)
stays above itself for \(N_H\) clocks and has \(s\) odd steps, then

\[
2^{N_H}\le(3+1/6500)^s.
\]

The exact inequality
\(19501^{6309}<2^{10000}6500^{6309}\) forces
\(10000s>6309N_H\). Each length-\(N_H\) parity word represents one
residue modulo \(2^{N_H}\), hence at most two integers up to \(H\).
The binomial exponential-moment bound with \(z=6309/3691\), together with

\[
10000^{10000}<2^{9500}3691^{3691}6309^{6309},
\]

bounds those words by \(2^{19N_H/20}\). Adding the at most 6499 smaller
sources proves (5). Both displayed integer inequalities were rechecked
exactly for this packet. Their receipt does not claim that the entropy
count or its real-power conclusion has been formalized in Lean.

## 5. Potential weights and the exact global gap

Retain the largeness condition (9), or the dyadic setup of (11). For any
nonnegative source potential \(f\) and constant \(M_H\ge0\), if
\(f(n)\le M_H\) on \(E_H(q)\), then (10) gives

\[
\sum_{n\in E_H(q)}\omega_q(n)f(n)
\le M_H\,\frac{3q}{2H-1}\bigl(6499+2H^{19/20}\bigr).
\tag{13}
\]

This finite weighted interface is also formalized. A bound
\(M_H=o(H^{1/20})\) would make this particular contribution \(o(q)\).
It has not been proved for the canonical obstacle potential or harmonic
envelope on these crossing sources. Their values cannot be replaced by
one merely because the corresponding unweighted kernel is sublinear.

There are two other restrictions in any proposed global use. First, an
inverse history can remain entirely above \(H\), so the crossing kernel
need not exhaust a full inverse potential. Second, if \(q\) is periodic,
raw inverse-word sums can repeat its cycle before reaching a crossing
source; (6)--(12) count first hits and do not pay that extra multiplicity.
No cycle has been excluded or silently discarded.

Thus the estimate removes all late-clock summation from this physically
defined crossing part. The remaining arithmetic task is to control the
potential arriving at its sparse source set and the histories that never
cross the floor. No such estimate follows from native source counting
alone.

## 6. Relation to the new literature and formal scope

The unrestricted shielding work in
[rStation 148](https://rstation.ai/problems/collatz/papers/148) was useful
for ruling out a tempting shortcut: its all-valuation protected languages
permit arbitrary concatenations, so summing a shielding cost independently
for each large gap can repeatedly charge the same earlier prefix. Its
linear shielding constructions do not bound the delay for an arbitrary
fixed positive source. Likewise, the chosen-label absorbing word of
[rStation 81](https://rstation.ai/problems/collatz/papers/81) selects a
compatible binary cylinder, not the future labels of a supplied integer.
Neither result is an input to (6)--(13).

`FirstCrossingBound.lean` defines the actual shortcut map and proves its
agreement with iteration, the coefficient lower affine bound, shifted
growth, first-hit uniqueness, the narrow crossing strip, inclusion in the
native no-descent set, all-source cardinality and weight bounds, the exact
dyadic case, and the bounded-potential interface. It contains 21 public
theorems, all explicitly audited. The noncomputable first-hit choice is
unique on the finite source set; it is not an algorithmic bound on the
hitting time.

The written asymptotic saving (12) uses the separately documented native
count (5). It does not use an almost-everywhere density at an ordinary
integer, an unproved mixing law, a gap cap, or a global bound on word
complexity. The compilation receipt records the precise verified scope.
