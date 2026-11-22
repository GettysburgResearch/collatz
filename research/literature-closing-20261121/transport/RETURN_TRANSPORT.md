# Return transport with every original atom retained

**Status: PROPOSED, with proofs below. The full Collatz conclusion is OPEN.**
This is a new completion attempt, not a review of the earlier packet. Its
positive output is an actual first-return upper bound with an exactly identified
residual, followed by a stronger quantitative recurrence test. Neither the
residual nor a small original source weight is discarded.

## 1. Map, source measure, and frozen input

Use the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\]

on positive ordinary integers. Write

\[
D=\{x\text{ odd}>0:(d+1)(x-2^d)\le70\,2^d,
\ d=\lfloor\log_2x\rfloor\}.
\]

Let \(E\) be the first entrance into \(D\), including time zero, and
\(R\) the first strictly positive return. The input is PR183 at
`8659cf62ac685540cadeef320e596c852fbb0959`, including its pinned section
dependencies. Its `BandMass.lean` proves

\[
K:=\sum_{n\ge1}n^{-4}L(E(n))^4\le4096\zeta(2)<\infty,
\qquad L(m)=1+\lfloor\log_2m\rfloor.                 \tag{T1}
\]

Set

\[
\mu=\sum_{n\ge1}n^{-4}\delta_n,\quad
\mu_o=\sum_{n\ge1\text{ odd}}n^{-4}\delta_n,\quad
\rho=E_*\mu,\quad \rho_o=E_*\mu_o.
\]

All measures below are countable nonnegative atomic measures. Pushforward means
grouping the original weights over complete fibers; it does not replace a
source weight by a weight at its endpoint. In particular
\(\rho(m)=\sum_{E(n)=m}n^{-4}\), including collisions. The notation
\(\eta\le\theta\) means the inequality on every subset, equivalently at
each atom.

Let \(P\eta=R_*\eta\). The killed operator is

\[
(Q\eta)(m)=\mathbf1_{m\ne1}
 \sum_{\substack{r\in D\setminus\{1\}\\R(r)=m}}\eta(r).
\]

Thus a source is killed only when its actual induced orbit reaches one.
For a failed original source \(s\), every packet \(Q^j\rho\) contains
its unchanged atom \(s^{-4}\) at \(z_j=R^j(E(s))\).

## 2. An actual upper bound, before any global hypothesis

### T-RT-001: fresh marked sources have bounded first-return transport

Let \(\mu_D=\sum_{n\in D}n^{-4}\delta_n\). Then

\[
\boxed{P\mu_D\le16\rho.}                            \tag{T2}
\]

Indeed, \(R(n)=E(Tn)\) for marked \(n\), the map \(T\) is injective
on odd integers, and \(Tn\le2n\). For every subset \(A\subseteq D\),

\[
\sum_{\substack{n\in D\\R(n)\in A}}n^{-4}
\le16\sum_{\substack{n\in D\\E(Tn)\in A}}(Tn)^{-4}
\le16\rho(A).
\]

The finite positive-test-function form is the theorem
`fresh_return_packet_le` in `../lean/RetainedTransport.lean`. Its source
integers are explicit on both sides. The domain is fresh marked source
weights \(\mu_D\); this is not yet an estimate on \(P\rho\).

### T-RT-002: an accelerated inverse-branch calculation improves the constant

Let \(U(n)=(3n+1)/2^{v_2(3n+1)}\) on positive odd integers. An elementary
calculation gives

\[
U_*\mu_o\le8\mu_o,\qquad P\mu_D\le8\rho_o.          \tag{T3}
\]

Here is the entire inverse-branch bound. An odd predecessor of an odd \(y\)
has the form \((2^a y-1)/3\), with \(a\ge1\) and divisibility by three.
There are no such predecessors when \(3\mid y\). If \(y\equiv1\pmod3\),
the exponents are \(a=2+2k\). With \(n_0=(4y-1)/3\ge y\), the
predecessors are

\[
n_k=4^kn_0+(4^k-1)/3\ge4^kn_0,
\]

and their total weight is at most \((256/255)y^{-4}\). If
\(y\equiv2\pmod3\), oddness gives \(y\ge5\); now \(a=1+2k\) and
\(n_0=(2y-1)/3\ge3y/5\). Their total weight is at most

\[
\frac{256}{255}\left(\frac53\right)^4y^{-4}
=\frac{160000}{20655}y^{-4}<8y^{-4}.
\]

These cases include \(y=1\). Because the intervening even values are
unmarked, \(R(n)=E(U(n))\) on \(D\). Positivity and pushforward now give
the second assertion of T3. This improvement to eight is proved here on paper;
the Lean module presently checks the independent shortcut proof with sixteen.

### T-RT-003: the exact residual after transporting the entrance law

Put

\[
\sigma=E_*\bigl(\mu_o|_{D^c}\bigr).
\]

Even sources satisfy \(E(2n)=E(n)\). Splitting the source sum into even
and odd integers gives

\[
\rho=\frac1{16}\rho+\rho_o,
\qquad
\boxed{\rho=\frac{16}{15}(\mu_D+\sigma).}            \tag{T4}
\]

Consequently T3 yields the actual, unconditional measure inequality

\[
\boxed{Q\rho\le8\rho+\varepsilon,
\qquad \varepsilon:=\frac{16}{15}Q\sigma.}           \tag{T5}
\]

Every odd integer with \(\lfloor\log_2n\rfloor\le69\) is marked: its
band width covers the entire dyadic shell. Hence every original source in
\(\sigma\) exceeds \(N=2^{70}\). Integrating \(x^{-4}\) over the
disjoint intervals \([n-2,n]\) for the odd integers \(n\ge N+1\) gives

\[
\|\sigma\|_1\le\frac1{6(N-1)^3},\qquad
\boxed{\|\varepsilon\|_1\le\frac8{45(2^{70}-1)^3}.} \tag{T6}
\]

This is a bound on the weights of the **original sources**, not a statement
that residual endpoints are large. Their entrances and later returns can be
small. T4 is exact before killing, and T5 retains the complete surviving
residual after killing.

T5 does not establish a finite constant \(C_1\) with \(Q\rho\le C_1\rho\).
Such a conclusion would require control of
\(\sup_m\varepsilon(m)/\rho(m)\); a small total residual mass supplies
no such control. Nor would a one-step factor eight, by itself, establish
recurrence: naive iteration gives exponential rather than critical growth.
Even with zero residual, the abstract shift \(F(n)=n+1\) and
\(\rho(n)=2^{-n}\) satisfy \(F_*\rho\le2\rho\le8\rho\) and have
finite fourth logarithmic moment, while all their orbits escape. This is an
exact limitation of that inequality, not a Collatz counterexample.

## 3. A stronger quantitative version of the atomic recurrence argument

The following result is independent of any conjectural Collatz estimate.
Its premise explicitly concerns the actual transported packets.

### T-RT-004: a retained atom consumes a weighted reference budget

Let \(\lambda\) be any nonnegative measure on the positive integers with

\[
K_\lambda=\sum_m\lambda(m)L(m)^4<\infty.
\]

Suppose \(z_j\) are distinct endpoints, a fixed atom \(a>0\) is present
at \(z_j\) in packet \(\nu_j\), and

\[
\nu_j\le C_j\lambda,\qquad 0<C_j<\infty.
\]

For every finite set \(I\) of time indices,

\[
\boxed{a\sum_{j\in I}\frac{L(z_j)^4}{C_j}
\le\sum_{m\in z(I)}\lambda(m)L(m)^4
\le K_\lambda.}                                     \tag{T7}
\]

The proof is termwise: \(a\le C_j\lambda(z_j)\), followed by division,
multiplication by the nonnegative cost, and summation. Distinct endpoints
justify counting each reference atom only once. The variable-cost and
constant-cost finite inequalities are formalized as `retained_atom_budget`
and `retained_atom_uniform_budget`. They do not assert the transport premise.

For Collatz, take \(\lambda=\rho\), \(a=s^{-4}\), and T1. A source
whose orbit never enters any cycle has distinct induced endpoints: a repeated
marked endpoint would make its ordinary orbit eventually periodic.

### T-RT-005: the critical logarithmic transport envelope

Assume \(C_j\) is nondecreasing; replacing it by its running maximum
enforces this while preserving the domination inequality. Partition time into
\(I_k=[2^k,2^{k+1})\), for \(k\ge1\). At most \(2^{k-1}\) distinct
positive endpoints can be below \(2^{k-1}\). Thus at least \(2^{k-1}\)
members of \(I_k\) have \(L(z_j)\ge k\). Summing T7 over finitely many
disjoint blocks and then taking their increasing limit proves

\[
\boxed{a\sum_{k\ge1}
 \frac{2^{k-1}k^4}{C_{2^{k+1}}}\le K_\lambda.}        \tag{T8}
\]

Therefore the actual-packet bound

\[
C_j\le A(j+1)\bigl(1+\log(j+2)\bigr)^5             \tag{T9}
\]

for a finite constant \(A\) is incompatible with a nonperiodic surviving
source: the summands in T8 dominate a positive multiple of \(1/k\).
This extends the uniform power-boundedness threshold to a nearly linear
envelope, provided the finite fourth logarithmic reference moment is retained.

The forced band adds an exact finite-scale improvement. If
\(B_b=\#(D\cap[0,2^b))\), the pinned section count gives
\((b+2)B_b\le426\,2^b\). For a uniform bound \(\nu_j\le C\rho\)
through \(j<J\), T7 therefore implies

\[
\boxed{s^{-4}(J-B_b)_+(b+1)^4\le C K.}              \tag{T10}
\]

This is a lower bound on the actual transport cost of keeping one ordinary
source alive at distinct marked endpoints. It is not an upper bound on that
cost.

### The exponent five is sharp for the stated moment mechanism

For any \(p>5\), consider the shift \(F(n)=n+1\) and
\(\lambda(n)=1/[n(\log(n+1))^p]\). The fourth logarithmic moment is
finite, every orbit escapes, and

\[
F_*^j\lambda\le C_p(j+1)\bigl(1+\log(j+2)\bigr)^p\lambda.
\]

Indeed, writing an endpoint as \(n+j\), its density ratio is
\((n+j)/n\,[\log(n+j+1)/\log(n+1)]^p\). The first factor is at most
\(j+1\); the logarithmic ratio is at most
\(1+\log(j+2)/\log2\). This abstract example is not a Collatz orbit.
It shows that the moment-only argument cannot replace exponent five by an
arbitrary larger exponent. Band arithmetic would have to supply extra input.

## 4. Trying to manufacture the missing transport bound

There is a useful trap in constructing a reference measure. For any killed
deterministic map at all, define

\[
c_j=\frac1{(j+1)(\log(j+2))^2},\qquad
\alpha=\sum_{j\ge0}c_jQ^j\rho.
\]

The measure is finite, and \(\alpha\ge c_0\rho\). Direct comparison of
coefficients gives, for every \(k\ge0\),

\[
Q^k\alpha\le
(k+1)\left(1+\frac{\log(k+1)}{\log2}\right)^2\alpha. \tag{T11}
\]

To check it, use
\((j+k+1)/(j+1)\le k+1\) and
\(j+k+2\le(j+2)(k+1)\). Thus the desired scale of operator growth can
be manufactured without knowing anything about Collatz.

The necessary regularity is exactly what this manufacture does not preserve:

\[
\sum_m\alpha(m)L(m)^4
=\sum_{j\ge0}c_j\sum_m(Q^j\rho)(m)L(m)^4.           \tag{T12}
\]

Tonelli justifies this equality, including value infinity. T1 bounds only the
term \(j=0\). T3 bounds the fourth log moment transported from fresh
marked weights, whereas T4 exposes the remaining \(P\sigma\) contribution.
No bound for the series in T12 was obtained. By T8 and T11, a nonperiodic
failed source would force T12 to be infinite. Calling \(\alpha\) a finite
measure does not settle this stronger moment question.

The residual in T5 can also be absorbed into a reference with exponential
growth. Set
\(\beta=\rho+\sum_{j\ge0}8^{-j-1}Q^j\varepsilon\). Then
\(Q\beta\le8\beta\), and its added total mass is at most
\(\|\varepsilon\|_1/7\). This construction retains every residual atom
but gives only \(8^j\), far above T9. Neither residual construction closes
the required critical estimate.

### An Archimedean attempt at the residual

The new Siegel--O'Dwyer preprint, section 7.2, motivates replacing a congruence
condition by an exact Archimedean affine identity. We tested that identity
directly on the residual without assuming their almost-boundedness theorem.
For a legal shortcut word \(w\) of length \(t\) and odd count \(q\), write

\[
T^t(n)=A_wn+B_w=m,\qquad A_w=3^q/2^t>0.
\]

The exact weight to be carried through that word is

\[
\boxed{n^{-4}=\frac{A_w^4}{(m-B_w)^4}.}              \tag{T13}
\]

The test was to use a small coefficient \(A_w\) and the marked window for
\(m\) to make the residual small after return. T13 shows the term that must
also be controlled. For a fixed original source, \(m-B_w=A_wn\), so the
coefficient gain cancels exactly against the denominator. Archimedean
closeness of \(m\) to \(B_w\) is not an upper bound on this negative
moment. Even after grouping words, a proposed bound must retain the small
denominators, ordinary divisibility, first-entrance restrictions, and the
actual source labels. We obtained no weighted small-denominator estimate
for the residual from the closeness condition alone.

There is a second remaining issue: T8 excludes nonperiodic orbits, not
nontrivial cycles. A persistent cycle can repeatedly use the same reference
atoms. Full Collatz needs either exclusion of those cycles or a budget that
kills every source. For example, a genuinely proved packet drift

\[
M_{j+1}+c\|Q^j\rho\|_1\le M_j+e_j,
\quad M_j\ge0,\quad M_0<\infty,\quad c>0,\quad
 e_j\ge0,\quad\sum_je_j<\infty
\]

would imply finite total occupation by telescoping, and would exclude cycles
as well. No such drift is asserted here.

## 5. What the primary literature contributes, and where its hypotheses stop

The exact source statements and URLs are in [SOURCES.md](SOURCES.md).

Tao's first-passage theorem concerns logarithmically uniform odd inputs in
the windows \([y,y^{1.001}]\), for two specified successive scales. It
provides a vanishing non-passage error and total-variation stabilization of
the passage laws. Its convention assigning passage location one to a
non-passing input is accompanied by the separate non-passage estimate; that
convention is not physical absorption. No theorem there states T9 for the
fixed atomic law \(\rho\), or bounds T12.

The attempted replacement by a fresh window law has a direct atomic test.
Normalize the **unkilled** transported measure \(P^j\rho\) by its
constant total mass. A particular original source always leaves an atom of
at least \(s^{-4}/\zeta(4)\). A fresh logarithmic input window tending to
infinity has largest atom tending to zero. Its total-variation distance
from that transported measure is therefore at least
\(s^{-4}/\zeta(4)-o(1)\), by testing the actual endpoint singleton.
Thus a vanishing fresh-window replacement error cannot simply be applied to
this measure. This observation concerns replacement of the input law, not
an assertion that Tao's passage laws themselves are diffuse.

Assani's finite measure characterization keeps a positive atom at every
integer and requires a single bound on all iterated pullbacks. Its bounded
orbit conclusion is consistent with T8, while the full Collatz statement
also identifies the conservative part with the trivial cycle. A finite
invariant measure supported only on known cycles does not retain the missing
source atoms.

The Foster--Lyapunov route was checked at its recurrence input as well.
For deterministic \(R\) with \(R(1)=1\), declaring all of \(D\) a
petite set is already a very strong assumption. If a sampled kernel
\(\sum_ka_k\delta_{R^k(r)}\) minorizes a nonzero measure uniformly over
\(r\in D\), the test at \(r=1\) forces that measure to be supported on
one. If its mass is \(\delta>0\), choose \(K\) with
\(\sum_{k>K}a_k<\delta\). Every \(r\in D\) must then reach one by
return index \(K\). Bounded access to \(D\) supplies no such statement.

## 6. Precise completion boundary

The new upper estimate is T5 with the exact residual T4--T6. The new
quantitative lower estimate is T7--T10, which preserves a fixed original
atom. Their comparison motivates a concrete target: obtain a reference with
finite fourth logarithmic moment and actual return transport bounded as in
T9, or obtain a cycle-sensitive packet drift with a summable error budget.

The first unsupported step would be to treat the tiny additive residual as
a bounded multiple of the entrance law, or to assert that the reference
constructed in T11 retains the moment in T12. Neither step has been proved.
The paper calculations here do not establish any decay of the retained
survivor mass, an exclusion of nontrivial positive cycles, or full Collatz.

The Lean execution status and exact theorem coverage are recorded by the
parent packet's replay receipt. `RetainedTransport.lean` covers the finite
transfer theorem with sixteen and the finite retained-atom budgets.
`EntranceRenewal.lean` separately supplies `entranceMass_renewal`, the exact
atomwise identity T4 with summability of all fibers. The improvement to eight,
the residual's total-mass estimate, the infinite measure inequality T5, the
dyadic summation and the sharpness example have the mathematical proofs above;
they are not represented as separately kernel-checked declarations here.
