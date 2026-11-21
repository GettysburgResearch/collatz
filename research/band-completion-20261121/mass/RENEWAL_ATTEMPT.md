# The source mass after a forced band entrance

**Status: an unconditional global entrance estimate; the renewal estimate needed
to finish Collatz is OPEN.** This is a completion attempt through the new
shrinking section and the cycle-sensitive primitive survivor mass. No decay of
the primitive survivor moment is claimed.

The useful positive estimate obtained here is

\[
 \sum_{n\ge1}n^{-4}\bigl(1+\lfloor\log_2 E(n)\rfloor\bigr)^4
 \le4096\sum_{n\ge1}n^{-2}<\infty,                 \tag{M1}
\]

where \(E(n)\) is the **first actual marked point on the ordinary shortcut
orbit of this same source**. All entrance fibers and original source weights
remain in the sum. The companion Lean file proves the pointwise estimate,
summability, and exact finite packet conservation. It does not prove that this
moment remains bounded through an unbounded number of returns.

## 1. Frozen inputs and conventions

The shortcut map is

\[
 T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

For \(d=\lfloor\log_2x\rfloor\), mark the positive odd integers satisfying
\((d+1)(x-2^d)\le70\,2^d\), and call their set \(D\). The input from
**PR173, `fa0c9e2a2851e6324391e39c17afcb5913185aec`,
`research/lean-shell-cover/ForwardSection.lean`, `bounded_visit` and
`marked_count_bound`**, is

\[
 \tau(n)<4\lfloor\sqrt n\rfloor+\lfloor\log_2 n\rfloor,
 \qquad T^{\tau(n)}n\in D,
 \qquad (\lfloor\log_2N\rfloor+2)\#(D\cap[0,N))\le426N. \tag{M2}
\]

Take \(\tau(n)\) to be the first such time and write \(E(n)=T^{\tau(n)}n\).
The least choice and its bound are
**the same PR and SHA, `research/lean-shell-cover/SectionDynamics.lean`,
`firstVisit`, `firstVisit_bound`**. The induced map \(R:D\to D\) is the
first **strictly positive** return. In particular \(R(1)=1\), with shortcut
return clock two. The shortcut map itself does not fix one.

The source-survival input is **PR176,
`ad9a0611d22b48c0fd0c1da31091179654ba31a9`,
`research/lean-global-resolvent-20261121/mathlib/PrimitiveSurvival.lean`,
`aliveMass_decomposition`, `liftRemainder_bound`, and
`fullCollatz_iff_primitiveMoment_tendsto_zero`**. For the odd accelerated map
\(U(n)=(3n+1)/2^{v_2(3n+1)}\), its exact identity is

\[
 A_q=\sum_{\substack{n>0\text{ odd}\\U^q(n)\ne1}}n^{-4}
 =B_q+\mathcal R_q,
 \qquad 0\le\mathcal R_q\le\frac{\zeta(4)}{16}\,15^{-q}.\tag{M3}
\]

Thus the outstanding target remains \(B_q\to0\). The index \(q\) counts
odd accelerated steps. It is not identified with the shortcut clock in M2 or
with the number of induced returns below.

## 2. The actual entrance estimate

Let \(s=\lfloor\sqrt n\rfloor\), with \(n\ge1\). The elementary inequalities

\[
 n<(s+1)^2\le2^{2s+1}
\]

give \(\lfloor\log_2n\rfloor\le2s\). The second inequality holds for every
integer \(s\ge0\): it is true at zero, and
\((s+2)^2\le4(s+1)^2\) advances the induction. Consequently M2 gives
\(\tau(n)<6s\).

Every positive shortcut step obeys \(T(x)\le2x\). Hence

\[
 T^t(n)\le2^t n,
 \qquad\lfloor\log_2T^t(n)\rfloor\le t+\lfloor\log_2n\rfloor.
\]

At the first entrance this yields the precise integer bound

\[
 L(E(n)):=1+\lfloor\log_2E(n)\rfloor\le8s.
\]

Since \(s^2\le n\),

\[
 L(E(n))^4\le8^4s^4\le4096n^2.                    \tag{M4}
\]

Multiplication by the **unchanged** source weight \(n^{-4}\), followed by
positive summation, proves M1. This also proves M1 restricted to the positive
odd sources used in M3. The first entrance clock has finite source expectation:

\[
 \sum_{n\ge1}n^{-4}\tau(n)
 \le6\sum_{n\ge1}n^{-7/2}<\infty.                \tag{M5}
\]

The same calculation gives finite entrance log-height moment of any real order
\(0\le p<6\), because \(L(E(n))^p\le8^pn^{p/2}\). The Lean result uses
the integral exponent four in M4, not this real-exponent extension or the
numerical evaluation of any zeta value.

## 3. Exact renewal packets, including collisions and cycles

For positive odd sources, use the original mass \(\mu(n)=n^{-4}\). Define

\[
 z_j(n)=R^j(E(n)),
 \qquad
 \nu_j(m)=\mathbf1_{m\ne1}
      \sum_{\substack{n>0\text{ odd}\\z_j(n)=m}}\mu(n),
 \quad m\in D.                                      \tag{M6}
\]

The index \(j\) is a return count. Each original source remains a distinct
summand even if several sources have the same endpoint. Since \(R(1)=1\),

\[
 \nu_{j+1}(m)=\mathbf1_{m\ne1}
       \sum_{\substack{r\in D\setminus\{1\}\\R(r)=m}}\nu_j(r),
\]

and therefore

\[
 \|\nu_{j+1}\|_1
 =\|\nu_j\|_1-\sum_{\substack{r\in D\setminus\{1\}\\R(r)=1}}\nu_j(r).
                                                               \tag{M7}
\]

These are ordinary sums of nonnegative numbers. They permit arbitrary
many-to-one transport. The only mass lost is the original-source mass whose
trajectory is actually absorbed at one. Neither the size of \(D\) nor the
number of occupied endpoints is a loss term in M7.

A nontrivial cycle is retained by these packets. Every positive orbit visits
\(D\), so a hypothetical nontrivial cycle has at least one marked point. Its
marked points form a cycle of \(R\). Each source on that cycle contributes
its fixed \(n^{-4}\) at every return index. A nonperiodic failed source also
contributes its fixed weight at every return index, regardless of how large
its endpoints become.

For finite source sets \(S\), the exact, formalized conservation identity is

\[
 \sum_{m\in E(S)}\ \sum_{\substack{n\in S\\E(n)=m}}w(n)
   =\sum_{n\in S}w(n).                              \tag{M8}
\]

It holds for arbitrary real weights. Its infinite positive version gives M6
without an injectivity or multiplicity assumption. Eventual killing in M6 is
the same ordinary event as eventual killing in M3, although their finite
observation clocks differ.

## 4. Where the completion attempt stops

M1 is a real first-transport estimate. It is not a renewal contraction.
Its endpoint control is in \(L(m)^4\). Applying M2 after an entrance or
return would require control of \(\sqrt m\), a substantially larger
function. There is no constant \(C\) such that
\(\sqrt m\le C L(m)^4\) for all marked \(m\). For example, the marked
integers \(m_d=2^d+1\) satisfy this membership condition for all sufficiently
large \(d\), whereas \(\sqrt{m_d}/L(m_d)^4\to\infty\).

Thus the argument cannot restart M5 with the transported source law. This is
an integrability gap in this estimate, not a claim that the actual transported
law has infinite square-root moment. Its square-root moment has not been
bounded or shown infinite here.

The section count in M2 also does not fill this gap. Even on a sparse set, a
packet \(\nu_j(m)\) can carry the unchanged weight of a much smaller original
source and many colliding sources. A bound on \(\#(D\cap[0,N))\) gives no
upper bound for those packet weights. Inserting endpoint weights \(m^{-4}\)
in their place would discard precisely the persistent source mass that M3 was
constructed to retain.

An attempted closing budget was

\[
 \sum_{j\ge0}\ \sum_{n>0\text{ odd}}n^{-4}
        \mathbf1_{z_j(n)\ne1}<\infty.              \tag{M9}
\]

It would be sufficient: one failed ordinary source would contribute the same
strictly positive summand for every \(j\), including on a nontrivial cycle.
M1 and M5 bound only the first entrance. No estimate for the full double sum
in M9 has been obtained. We do not assert M9, a uniform bound on the successive
log-height moments, a return killing fraction, or \(B_q\to0\).

The first unsupported step of this route would therefore be to replace the
fixed-source packet on a later return by a fresh distribution satisfying the
first-entrance moment bound. Neither bounded access, density zero, nor M3
authorizes that replacement. The outstanding work is an estimate for the
**actual packets** in M6 that forces source mass to be killed; M4 alone does
not provide one.

## 5. Quantitative localization of the global survivor mass

The entrance clock also supplies an explicit remainder at a global observation
time. This corollary is proved mathematically here; it is not a separate
declaration in the Lean file.

Let \(q\ge6\), \(J=\lfloor q/6\rfloor\), and \(K=J^2\). If
\(1\le n\le K\), then \(\lfloor\sqrt n\rfloor\le J\), so

\[
 \tau(n)<6\lfloor\sqrt n\rfloor\le6J\le q.
\]

Consequently, a source that has not entered the marked set through shortcut
clock \(q\) must exceed \(K\). Its total fourth-power source mass is at most

\[
 \sum_{n>K}n^{-4}
 \le\int_K^\infty x^{-4}\,dx
 =\frac1{3K^3}
 =\frac1{3\lfloor q/6\rfloor^6}.                 \tag{Q1}
\]

This includes all positive sources and hence bounds the odd-source mass too.
For an odd start, every marked shortcut value is an odd value and therefore
appears in the accelerated odd orbit. Its accelerated index is no larger than
its shortcut clock. Thus the same Q1 bound holds for the mass \(H_q\) of odd
sources with no marked visit among \(U^0(n),\ldots,U^q(n)\).

Define the actual post-entrance survivor mass

\[
 P_q=\sum_{\substack{n>0\text{ odd}\\U^q(n)\ne1\\
                    \exists j\le q:\ U^j(n)\in D}}n^{-4}.
\]

Since one is marked, every source counted by \(H_q\) is still alive. Exact
source partitioning therefore gives \(A_q=P_q+H_q\). Combining this with M3,

\[
 |B_q-P_q|
 \le H_q+\mathcal R_q
 \le\frac1{3\lfloor q/6\rfloor^6}
       +\frac{\zeta(4)}{16}\,15^{-q},\qquad q\ge6. \tag{Q2}
\]

This is an unconditional quantitative coupling of the primitive moment to
**actual post-entrance survivors**. The first term is a polynomial
never-entered remainder; the second is the complete higher-lift remainder.
The estimate proves that any persistent primitive mass has already passed
through the section. It supplies no loss from \(P_q\), and the return-packet
problem in M6--M9 remains unchanged.

## 6. Direct attack on the primitive denominator

The primitive-word route was also tested without replacing its denominator.
Write a marked primitive endpoint as \(r_w=2^d+e\). Its affine equation gives

\[
 b_w=\frac{2^{A+d}+2^A e-C_w}{3^q},
 \qquad 0\le(d+1)e\le70\,2^d.                     \tag{M10}
\]

The band condition narrows the permitted \(e\). It does not control the
word-dependent shifted center \(2^{A+d}-C_w\). To bound \(B_q\), one still
needs either a lower bound for the positive cancellation denominator in M10,
or an appropriately weighted count of words where that denominator is small.
Discarding \(C_w\) has the wrong effect on a negative source moment.

There is a definite scale mismatch in a proposed use of ternary residue
equidistribution. For a fixed ordinary odd source \(n\),

\[
 U(x)+1\le\tfrac32(x+1),
 \qquad U^q(n)+1\le(3/2)^q(n+1).
\]

Once \(2^q\ge n+1\), its actual endpoint is below \(3^q\) and is already its
primitive representative. Any marked window containing that endpoint has
length at most a constant times its height divided by its logarithm; relative
to the ternary modulus \(3^q\), this is at most a constant times
\((n+1)2^{-q}\), even before the logarithmic improvement. The window therefore
does not contain a full period of the congruence used to define \(r_w\).
An estimate averaged over a complete ternary period cannot be restarted there
without an additional short-interval estimate that retains the source
denominator. No such estimate was obtained.

The two architectural inputs also need an arithmetic ingredient specific to multiplier three to become a completion. The primitive-cylinder source partition
and its higher-lift geometric bound extend to an odd multiplier five. The
rotation proof of a shrinking dyadic section extends with adjusted constants
as well. But the odd accelerated \(5x+1\) map has the exact positive cycle
\(13\mapsto33\mapsto83\mapsto13\), since its three division exponents are
\(1,1,5\). Thus access to a sparse section plus the source-tail decomposition
is not, by itself, an absorption mechanism. This comparison does not exclude
a multiplier-three proof; it identifies arithmetic information that such a
proof must additionally use.

## 7. Formalization boundary

[`../lean/BandMass.lean`](../lean/BandMass.lean) imports the frozen ordinary
section development and proves:

- `firstVisit_lt_six_sqrt`: the simplified clock bound;
- `entrance_log_height_le`: \(L(E(n))\le8\lfloor\sqrt n\rfloor\);
- `entrance_log_four_le`: the exact pointwise inequality M4;
- `entranceLogTerm_summable`: summability in M1 over all positive sources;
- `entranceLogTerm_sum_le`: the explicit global upper bound in M1;
- `sum_entrance_packets`: finite fiber conservation M8.

The complete file compiled successfully with Lean 4.34.1, one worker, and
warnings treated as errors. Its four printed axiom checks report only
`propext`, `Classical.choice`, and `Quot.sound`. No custom axiom,
`sorry`, or `native_decide` is used. This execution checks the stated entrance
and finite-packet theorems; it does not check the unproved absorption estimate.

The infinite renewal formulas are the nonnegative grouping argument written
above, and Q1--Q2 are the cutoff and p-series argument in section 5; they are
not presented as separately formalized Lean declarations. In particular, the
file has no assertion of M9 or of full Collatz.
