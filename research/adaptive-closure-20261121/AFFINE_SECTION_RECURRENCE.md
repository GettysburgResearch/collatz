# Exact affine sections: a recurrent finite core under binary Haar input

**PROPOSED.** The theorem below is an exact probabilistic statement about
the binary parity input of the shortcut Collatz map. It does **not** prove
forward-five closure or the Collatz conjecture for positive integers.
The ordinary-input obstruction is stated explicitly in Section 8.

## 1. Map, source comparison, and the theorem

Write

\[
T(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

The same formula defines a continuous map on the binary integers
\(\mathbb Z_2\). Binary Haar measure means the probability measure that
assigns each residue class modulo \(2^h\) probability \(2^{-h}\).
This use of completion is restricted to the explicit probabilistic
theorem. All finite positive-integer comparisons below use the ordinary
map with its exact parity guards.

PR166, head `5996b9f525ca50978bc34f423192c36a87765bf3`,
`research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`
and `LADDER_RENEWAL.md`, gives disjoint same-clock paired returns and
a contracting energy renewal on their union. PR146, head
`fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`, gives
further paired-return cylinders and bounded-height lift selectors.
Those statements concern explicit finite ordinary trajectories. The
present construction follows the **entire relative affine section** of
the two paths, without first choosing a successful return dictionary.
Neither cited source is a premise of the theorem proved here.

Let

\[
\mathcal S=\{(k,c): k\in\mathbb Z,\quad
c\in 3^{-\max(0,-k)}\mathbb Z\}.
\]

For \((k,c)\in\mathcal S\), put \(\lambda=5\,3^k\), and for an unbiased
fresh bit \(\epsilon\in\{0,1\}\), set

\[
\eta\equiv\epsilon+c\pmod2,\quad \eta\in\{0,1\},
\qquad k'=k+\eta-\epsilon,
\qquad c'=\frac{3^\eta c+\eta-5\,3^{k'}\epsilon}{2}.
\tag{S1}
\]

Parity of \(c\) is well-defined because its denominator is odd.

**Theorem S.** From every state in \(\mathcal S\), the Markov chain (S1)
visits the following finite set infinitely often, with probability one:

\[
\mathcal F=\left\{(k,c)\in\mathcal S:
 |k|\le2003,\quad
 \sqrt{\frac{|c|}{1+5\,3^k}}\le25\,000\,000\right\}.
\tag{S2}
\]

In particular this holds for the affine sections of the pair \((x,5x)\)
when \(x\) is Haar distributed. It holds after conditioning on any
specified finite source parity prefix as well. The theorem asserts
returns to a finite set. The companion
`AFFINE_SECTION_ROOT_RETURN.md` imports a subsequently inspected
control theorem from PR146 to upgrade this result to returns to
the particular state \((0,0)\).

The deliberately loose constants in (S2) make every estimate explicit.
No external random-orbit hypothesis, mixing conjecture, GRH, or
numerical estimate is used in the proof.

## 2. Exact realization and the state lattice

Suppose that at a common shortcut clock the two values satisfy

\[
y=\lambda x+c,\qquad \lambda=5\,3^k.
\]

Let \(\epsilon\) be the parity of \(x\) and \(\eta\) that of \(y\).
Since \(\lambda\) is odd as a binary unit, the parity relation is
\(\eta=\epsilon+c\pmod2\). Substituting
\(x'=(3^\epsilon x+\epsilon)/2\) gives

\[
T(y)=5\,3^{k+\eta-\epsilon}T(x)
 +\frac{3^\eta c+\eta-5\,3^{k+\eta-\epsilon}\epsilon}{2}.
\]

Thus (S1) is an exact identity. Starting with \((x,5x)\), the initial
section is \((k,c)=(0,0)\), and \(k\) is the target odd-input count
minus the source odd-input count up to that clock.

The lattice \(\mathcal S\) is preserved. If the two bits are equal,
the allowed power of three in the denominator does not increase.
If \((\epsilon,\eta)=(0,1)\), then
\(c'=(3c+1)/2\) and \(k'=k+1\), cancelling one allowed denominator
factor when \(k<0\). If \((\epsilon,\eta)=(1,0)\), then
\(c'=(c-5\,3^{k-1})/2\) and \(k'=k-1\), adding at most the one
allowed factor. In each case the numerator has the required even
parity, so division by two creates no factor two in the denominator.

For every \(h\), the length-\(h\) source parity vectors are in
bijection with residue classes modulo \(2^h\). This follows
inductively: on a specified length-\(h\) parity cylinder,

\[
T^h(x)=\frac{3^p x+B}{2^h},
\]

where \(3^p\) is odd. The next parity selects exactly one of the two
refinements modulo \(2^{h+1}\). Consequently the source parity bits
are independent fair bits under Haar input. After any fixed prefix,
the remaining bits are again independent fair bits. This proves the
Markov realization claimed in Theorem S; it does not claim that the
parities of any one specified positive integer are random.

The same construction from an arbitrary \((k,c)\in\mathcal S\) is
realized by Haar \(x\) and \(y=5\,3^k x+c\) in \(\mathbb Z_2\).
Ordinary positivity is not required for that arbitrary-state realization.

## 3. A martingale with uniformly renewed variance

When \(c\) is even, \(\eta=\epsilon\) and \(k'=k\). When \(c\) is
odd, \(\eta=1-\epsilon\), so \(k'-k\) takes the values \(+1,-1\)
with equal probability. Therefore \(k_t\) is a martingale with
increments bounded by one.

For every integer \(k\), including negative \(k\),

\[
v_2(5\,3^k-1)=
\begin{cases}2,&k\text{ even},\\1,&k\text{ odd}.
\end{cases}
\tag{S3}
\]

Indeed \(3^k\) is respectively one or three modulo eight. From any
state there is probability at least \(1/4\) of an active step
(one starting with odd \(c\)) among the next three steps:

* An initially odd \(c\) is already active.
* If \(v_2(c)=1\), choose \(\epsilon=0\); then \(c'=c/2\) is odd.
* If \(v_2(c)\ge2\) and \(k\) is odd, choose \(\epsilon=1\).
  The next carry \((3c-(\lambda-1))/2\) is odd by (S3).
* If \(k\) is even and \(v_2(c)=2\), two successive zero bits
  make the carry odd.
* If \(k\) is even and \(v_2(c)\ge3\), including \(c=0\),
  a one bit gives carry valuation one, and a zero bit then gives
  odd carry.

In the last two cases the active increment is the third step, after
the two specified bits. Martingale increments at distinct times are
orthogonal in conditional second moment. Hence, conditional on any
initial state and with \(\Delta=k_{t+3}-k_t\),

\[
\mathbb E\Delta=0,\qquad |\Delta|\le3,\qquad
\mathbb E\Delta^2\ge\frac14.
\tag{S4}
\]

These estimates are uniform in both the real magnitude and the
denominator of \(c\).

## 4. The normalized carry has fractional-moment drift

Put

\[
r=\frac{|c|}{1+\lambda},\qquad R=\sqrt r.
\]

From (S1), using \(|\eta-\lambda'\epsilon|\le1+\lambda'\),

\[
r'\le A r+\frac12,\qquad
A=\frac{3^\eta(1+\lambda)}{2(1+\lambda')}.
\tag{S5}
\]

Always \(1/2\le A\le3/2\). For even \(c\), its two values are
\(1/2,3/2\). For odd \(c\), its two values are

\[
A_0=\frac{3(1+\lambda)}{2(1+3\lambda)},\qquad
A_1=\frac{3(1+\lambda)}{2(3+\lambda)}.
\]

Their reciprocals belong to \([2/3,2]\) and sum to \(8/3\).
The convex function \(u\mapsto u^{-1/2}\) has its largest sum at
the endpoints when evaluated at two points of that interval with
sum \(8/3\). Thus in both parity cases

\[
\mathbb E\sqrt A\le
\rho:=\frac{\sqrt2+\sqrt6}{4}<\frac{97}{100}.
\]

By \(\sqrt{u+v}\le\sqrt u+\sqrt v\),

\[
\mathbb E[R'\mid(k,c)]
\le\rho R+\frac1{\sqrt2}
\le\frac{97}{100}R+\frac{71}{100}.
\tag{S6}
\]

Iterating conditional expectations three times gives

\[
\mathbb E R_{t+3}\le aR_t+b,
\quad a=(97/100)^3,
\quad b=(71/100)(1+97/100+(97/100)^2).
\tag{S7}
\]

The strict moment contraction and the martingale in Section 3 are
compatible: the carry is normalized by the possibly very large or
small relative slope.

## 5. An explicit proper Foster function

Define

\[
g(k)=\frac1{10^6+k^2},\quad
\phi(k)=\log(10^6+k^2),\quad
V(k,c)=\phi(k)+\frac1{100}g(k)R.
\tag{S8}
\]

This function is nonnegative and proper on the lattice \(\mathcal S\).
Indeed a bound on \(V\) bounds \(|k|\), and with \(k\) bounded it
bounds \(|c|\). There are finitely many allowable \(k\), and for
each such \(k\) the allowable \(c\) form a fixed discrete lattice.
Thus every sublevel set of \(V\) is finite. In particular (S2) is
finite despite its very generous bounds.

Let \(M=1000/997\). Since

\[
|\phi'(u)|=| (\log g)'(u)|
=\frac{2|u|}{10^6+u^2}\le\frac1{1000},
\]

and \(|\Delta|\le3\), both \(g(k+\Delta)/g(k)\) and its
reciprocal are at most \(e^{3/1000}\le M\). The last inequality
uses \(e^z\le(1-z)^{-1}\) for \(0\le z<1\).
Together with (S7), this gives

\[
\begin{aligned}
\mathbb E[g(k_{t+3})R_{t+3}]-g(k_t)R_t
&\le g(k_t)\big((Ma-1)R_t+Mb\big)\\
&\le g(k_t)\left(-\frac2{25}R_t+\frac{211}{100}\right),
\end{aligned}
\tag{S9}
\]

because the following are exact rational comparisons:

\[
Ma=\frac{912673}{997000}<\frac{23}{25},\qquad
Mb=\frac{2066739}{997000}<\frac{211}{100}.
\]

Suppose first that \(|k|\ge2003\). Every \(u\) between \(k\) and
\(k+\Delta\) has \(|u|\ge2000\), and hence

\[
\phi''(u)=\frac{2(10^6-u^2)}{(10^6+u^2)^2}
\le-\frac65g(u)\le-\frac6{5M}g(k).
\]

Taylor's theorem, \(\mathbb E\Delta=0\), and (S4) imply

\[
\mathbb E[\phi(k_{t+3})-\phi(k_t)]
\le-\frac3{20M}g(k_t).
\]

Adding one hundredth of (S9),

\[
\mathbb E[V_{t+3}-V_t\mid(k,c)]
\le-g(k)\left(\frac{2569}{20000}+\frac R{1250}\right)
\le-g(k)\left(\frac18+\frac R{1250}\right)<0.
\tag{S10}
\]

If \(|k|\le2003\), the logarithmic contribution is at most
\(3/1000\). For \(R>25\,000\,000\), (S9) instead yields

\[
\mathbb E[V_{t+3}-V_t\mid(k,c)]
\le\frac3{1000}
-\frac{R/1250-211/10000}{5012009}<0,
\tag{S11}
\]

since

\[
\frac{25000000/1250-211/10000}{5012009}
=\frac{199999789}{50120090000}>\frac3{1000}.
\]

Equations (S10)--(S11) give strictly negative three-step drift outside
\(\mathcal F\). There is no claim of a uniform negative constant
over the entire infinite state space; strict drift plus properness
will suffice.

## 6. Why the drift proves repeated finite-core returns

Consider the chain at clocks \(0,3,6,\ldots\), and let \(\tau\)
be its first hitting time of \(\mathcal F\). Stop \(V\) at \(\tau\).
The resulting process is a nonnegative supermartingale and therefore
converges almost surely. Every one-step conditional expectation is
finite, since there are just eight possible three-bit continuations.

For a state outside \(\mathcal F\), denote its positive conditional
decrease in \(V\) over three steps by \(\delta(k,c)>0\), and set
\(\delta=0\) after stopping. Taking expectations of the stopped drift
identity up to a finite time \(N\) shows

\[
\mathbb E\sum_{j=0}^{N-1}\delta(X_j)\mathbf1_{\{j<\tau\}}
\le V(X_0).
\]

Monotone convergence therefore implies that the accumulated positive
decrease is finite almost surely.

On the event \(\tau=\infty\), convergence of the stopped
supermartingale makes its values bounded. Properness of \(V\) then
confines that entire sample path to some finite sublevel set. The
strictly positive function \(\delta\) has a positive minimum on that
finite set outside \(\mathcal F\). The accumulated decrease would
then be infinite, a contradiction. It follows that \(\tau<\infty\)
almost surely from every initial state.

For each deterministic skeleton clock \(j\), apply the same conclusion
conditionally to the state at that clock. With probability one there
is a visit to \(\mathcal F\) at or after \(j\). Intersecting these
probability-one events over the countably many \(j\) proves infinitely
many visits and completes the proof of Theorem S. This argument also
covers a chain which eventually stays inside \(\mathcal F\).

## 7. Exact finite-cylinder consequences and their limits

For any specified finite source prefix and any fixed delay \(H\),
the event that a section enters \(\mathcal F\) at some finite clock
after \(H\) has Haar probability one. Each finite-time entrance can
be decided from a finite parity prefix, hence from a single binary
residue class. Finite unions of such successful cylinders have
measures approaching one.

It follows that, for that **fixed delay** and without restricting the
initial prefix, the set of positive integers with such a finite
certificate has natural density one: any finite cylinder union has
its exact natural density, and its complement upper-bounds the
complement of the full successful set. Within a specified prefix of
length h, the corresponding assertion is relative natural density
one; the successful subset has absolute density 2^(-h). The argument
does not infer natural density one for the countable intersection over
all delays, and it does not prove success for every positive integer.

The complement in the fixed-delay statement in fact has zero upper
Banach density. Each finite cylinder union is periodic, so its density
holds uniformly in the starting point of a long interval, with bounded
error depending only on its finite period. Approximating the full
successful union by finite unions of measure approaching one proves
the assertion. The prefix-qualified statement is again relative to
that prefix. No rate of this uniform sparsity is asserted.

Nor does entrance to \(\mathcal F\) imply the paired-return equality
\(T^L(5x)=5T^L(x)\). The affine identity across an entire parity
cylinder requires the single section state \((k,c)=(0,0)\);
a numerical equality at just one input may occur in a different
section. For example, at x=5 and L=12 the two values are one and
five while the section is \((k,c)=(1,-10)\). The finite core may
contain other recurrent
communicating classes. Communication to \((0,0)\) is a separate
input, supplied with an exact source pin in the companion note.

## 8. The ordinary first-five failure is not excluded

The forward-five obligation is

\[
x\text{ reaches }1\quad\Longrightarrow\quad5x\text{ reaches }1
\]

for the specified positive ordinary domain. After an actual source
reaches one, its future parity bits alternate one and zero. This
eventually periodic drive belongs to a Haar-null set. It is invalid to
replace those bits by the fair independent bits used in (S1), or to
condition the probability-one theorem on that particular infinite
tail.

Positivity alone does not remove this distinction. Along a hypothetical
pair with source already in \(\{1,2\}\), the exact relation is

\[
c_t=y_t-5\,3^{k_t}x_t.
\]

The constraints \(x_t,y_t>0\) allow a positive slope to grow while
the carry cancels most of \(5\,3^{k_t}x_t\). The ratio
\(|c_t|/(1+5\,3^{k_t})\) can stay bounded while \(k_t\) grows.
The Foster function grows in that situation, but its negative drift
is an **average over the two next source bits**; it is not a
pointwise inequality along the prescribed periodic source drive.
Excluding every such ordinary drive is the first unsupported step
in a proposed inference from Theorem S to forward-five closure.

There is also a verified obstruction to a complete **synchronous**
paired-return compiler of a particularly strong form. The ordinary
first-hit shortcut times are

\[
\tau(85)=8,\qquad\tau(425)=39.
\]

The value five occurs exactly once in the trajectory of 425, at clock
35, four clocks before its first hit of one. At that clock the 85
trajectory is at two. Therefore there is no clock \(L\) at which
\((T^L(85),T^L(425))=(1,5)\), even though both trajectories converge.
Appending any number of source \(1\leftrightarrow2\) cycles does
not change that fact. A compiler built exclusively by concatenating
same-clock paired blocks until its endpoint is \((1,5)\) cannot
cover every convergent source. Independent ordinary clocks may still
give perfectly valid invariant-label identities.

The recurrence theorem is a new exact control on the unrestricted
section process. Neither a finite-energy bound on the uncovered
ordinary sources, a source-preserving deterministic selector, nor a
full Collatz proof follows from it here.

## 9. Validation boundary

`check_affine_section_recurrence.py` independently implements the
literal ordinary map and the rational state recurrence. It checks
all length-12 positive binary residue representatives, a grid of
three-step rational sections, the lattice and moment identities,
the exact rational constants used above, and the 85/425 phase
obstruction. Normal and optimized Python runs must produce identical
JSON. These are bounded arithmetic checks. The unbounded statements
are justified by the proofs in Sections 2--6, not by the finite grid.
