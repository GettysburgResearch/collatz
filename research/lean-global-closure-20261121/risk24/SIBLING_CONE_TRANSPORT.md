# The actual sibling transport: bounded atomic odds and an unavoidable logarithmic cost

Date: 2026-11-23.

**Status: exact written deductions on a hypothetical ordinary escaping
component, and a direct noncollapse attempt that does not close.** The
new finite atomic conformal measure has uniformly bounded first-digit
odds. The natural attempt was to transfer that property to the canonical
inverse law. This note calculates the transfer and proves an ordinary
arithmetic obstruction to its strongest version: matching the retained
source at the same inverse depth in successive sibling cones requires
at least `N log_2 N - O_p(N)` extra division exponents in total.

The obstruction is to the proposed transport, not to Collatz itself.
It does not exclude transports with changed depths, unbounded costs, or
compensating multiplicities. No collision upper bound or canonical
first-digit tightness theorem is asserted.

## 1. Sources, laws, and the actual sibling map

Use the odd map on positive integers coprime to six,

\[
 U(n)=\frac{3n+1}{2^{a(n)}},\qquad
 a(n)=v_2(3n+1),\qquad w(n)=3/2^{a(n)}.
 \tag{1}
\]

The retained sources are:

| Source | Exact input |
|---|---|
| PR177, `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`, `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md` | The positive product \(\Lambda(n)=\prod_{i\ge0}3U^in/(3U^in+1)\), the edge identity \(r(n)=w(n)r(Un)\) for \(r=\Lambda/n\), and the finite atomic conformal measure \(\mu_s=\sum_{n\in E}r(n)^s\delta_n\), \(s>1\). These are elementary written results conditional only on the existence of the actual escaping component. |
| PR178, `2169884b64871b448cda16c7d74a0d5914ed870b`, `research/high-variance-20261123/entropy/COARSE_DIGIT_MEMORY_AND_TRACE_FRONT.md` | The actual sibling involution below; the critically harmonic trace \(F\), its bounds \(\alpha\le F(q)\le Mq\), and the actual-clock first-digit log-odds target. The trace inputs retain their source qualifications. |
| PR180, `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`, `research/high-variance-20261123/ANALYTIC_GLUING.md` and `ENTROPY_RIGIDITY.md` | The distinction between a common whole-path boundary and a root-dependent transform. No replacement of the original source by a newly sampled source is made below. |

Let \(E\) be an actual escaping component. At every root \(q\in E\),
list all positive exponents \(e\) for which

\[
 I_e(q)=(2^eq-1)/3
\]

is a positive odd unit. Pair consecutive exponents in this list:
first with second, third with fourth, and so on. If \(n=I_e(q)\),
define \(\mathcal S n\) to be the parent paired with \(n\).
The legal exponents are two residue classes modulo six. Each pair
has exponent difference two or four, and the paired parents have
opposite nonzero residues modulo three. Therefore

\[
 \mathcal S^2 n=n,\qquad U(\mathcal S n)=Un,
 \qquad \mathcal S n\ne n.                              \tag{2}
\]

In the increasing direction the paired integers satisfy either

\[
 n\longmapsto4n+1\quad\text{or}\quad n\longmapsto16n+5.
 \tag{3}
\]

The decreasing direction is their inverse. In particular, in both
directions,

\[
 0<\frac{\mathcal S n}{n}\le21.                         \tag{4}
\]

The constant is deliberately loose and uniform. The shifted real
phase cannot distinguish this pair:
\(\{\log_2(n+1/3)\}=\{\log_2(\mathcal S n+1/3)\}\).
The present attempt therefore uses the ordinary inverse cones, not
real phase equidistribution.

## 2. The new atomic law really does have bounded first-digit odds

For \(s>1\), define

\[
 p_s(q)=\sum_{Un=q}w(n)^s,
 \qquad R_s(q,n)=\mathbf1_{Un=q}\frac{w(n)^s}{p_s(q)}.
 \tag{5}
\]

This is exactly the distribution of an atom of \(\mu_s\), conditional
on its forward image being \(q\): the edge identity gives
\(\mu_s\{n\}=w(n)^s\mu_s\{q\}\). It is not the canonical inverse
kernel and \(\mu_s\) is not asserted forward invariant.

For each nonzero parent digit there is exactly one allowed exponent
class modulo six. Its contribution to (5) is

\[
 \frac{3^s2^{-se_r}}{1-2^{-6s}},\qquad 1\le e_r\le6.
\]

The two smallest class representatives differ by two or four. Thus
the two digit probabilities under \(R_s(q,\cdot)\) have ratio
\(4^{\pm s}\) or \(16^{\pm s}\), and in particular

\[
 \boxed{\frac1{1+16^s}\le
 R_s(q,\{n:n\equiv r\pmod3\})\le
 1-\frac1{1+16^s}\quad(r=1,2).}                         \tag{6}
\]

The same bounded distortion holds for the global atomic involution:

\[
 \frac{\mu_s\{\mathcal S n\}}{\mu_s\{n\}}
 =2^{-s(a(\mathcal S n)-a(n))}
 \in\{4^s,4^{-s},16^s,16^{-s}\}.                        \tag{7}
\]

These are genuine uniform noncollapse statements for the specified
atomic law. The unresolved step is their transfer to

\[
 K_F(q,n)=\mathbf1_{Un=q}\frac{w(n)F(n)}{F(q)},
 \qquad P_1F=F.                                        \tag{8}
\]

## 3. Why the pointwise symmetry does not transport inverse cones

Write

\[
 \operatorname{Pred}(q)=\{n\in E:U^kn=q\text{ for some }k\ge0\}.
\]

Since the component is nonperiodic, a positive integer reaches \(q\)
at at most one depth. The following exact identity is the first
obstruction to a Harnack argument from (7):

\[
 \boxed{\mathcal S(\operatorname{Pred}(q))
 =\bigl(\operatorname{Pred}(q)\setminus\{q\}\bigr)
   \cup\{\mathcal S q\}.}                              \tag{9}
\]

Indeed, if \(U^kn=q\) with \(k\ge1\), (2) gives
\(U^k\mathcal S n=q\). Neither member of this pair can be \(q\):
that would imply a positive return of \(q\). The involution therefore
permutes the strict cone. The only remaining point is the root, and
\(\mathcal S q\notin\operatorname{Pred}(q)\), again by nonperiodicity.

In particular,

\[
 \mu_s(\mathcal S\operatorname{Pred}(q))
 =\mu_s(\operatorname{Pred}(q))-r(q)^s+r(\mathcal S q)^s.
 \tag{10}
\]

This is not a comparison with
\(\mu_s(\operatorname{Pred}(\mathcal S q))\).
The pointwise bounded-distortion map stays inside the original strict
cone; it supplies no map to its sibling cone. Replacing its image by
that different cone would be the first false equality in the proposed
transfer.

## 4. Any same-depth cone lift pays a logarithmic cost

Now retain one original source \(p\in E\), with

\[
 q_j=U^jp,\qquad A_j=\sum_{i<j}a(q_i),\qquad
 \Lambda_j=\prod_{i<j}\frac{3q_i}{3q_i+1}.
\]

Then \(\Lambda_j\ge\Lambda(p)>0\) and the exact product identity is

\[
 q_j=\frac{3^jp}{2^{A_j}\Lambda_j}.                    \tag{11}
\]

For each \(j\ge1\), choose **any** legal ordinary inverse word of
exactly \(j\) odd steps from \(\mathcal S q_j\). Denote its
endpoint by \(x_j\), its total division exponent by \(A'_j\), and
its additional cost by \(\Delta_j=A'_j-A_j\). Such words exist,
because every unit has legal unit parents.

### Source separation

The cones \(\operatorname{Pred}(\mathcal S q_j)\), \(j\ge1\), are
pairwise disjoint. A path through \(\mathcal S q_j\) first meets the
specified forward spine at \(q_{j+1}\). It cannot meet that spine
earlier: its subsequent deterministic path would then stay on it,
whereas \(\mathcal S q_j\) is not a spine vertex. A common ancestor
of two such sibling roots would have two different first meetings,
which is impossible. Consequently the positive integers \(x_j\)
are pairwise distinct.

This conclusion can also be checked directly at the retained clocks:
if \(j<k\) and \(x_j=x_k\), after \(j+1\) steps this common source
is at \(q_{j+1}\), so after \(k\) steps it is at \(q_k\), contradicting
the required endpoint \(\mathcal S q_k\ne q_k\).

### Exact cost and its consequences

The positive affine offset of the alternate word gives

\[
 x_j\le\frac{2^{A'_j}\mathcal S q_j}{3^j}
 =2^{\Delta_j}\frac{p}{\Lambda_j}
     \frac{\mathcal S q_j}{q_j}
 \le B_p2^{\Delta_j},\qquad
 B_p:=\frac{21p}{\Lambda(p)}.                           \tag{12}
\]

Therefore

\[
 \Delta_j\ge\log_2x_j-\log_2B_p.                       \tag{13}
\]

Since \(N\) distinct positive integers have product at least \(N!\),

\[
 \boxed{\sum_{j=1}^N\Delta_j
 \ge\log_2(N!)-N\log_2B_p
 =N\log_2N-O_p(N).}                                    \tag{14}
\]

No expectation or sampling convention occurs in this inequality.
It holds simultaneously for every family of the specified actual,
same-depth alternate words. Its counting form is

\[
 \boxed{\#\{1\le j\le N:\Delta_j\le t\}
 \le\lfloor B_p2^t\rfloor.}                            \tag{15}
\]

For any fixed \(\gamma<1\), only \(O_p(N^\gamma)\) of the first
\(N\) lifts can have \(\Delta_j\le\gamma\log_2N\).
Thus a uniformly bounded extra-exponent cone lift of the retained
prefixes is impossible under the escaping hypothesis. This directly
addresses the proposed mechanism; it does not presume that a useful
transport must satisfy that bounded-cost condition.

The exact pressure cost is visible as well. The ratio between the
products of \(w\) along the alternate and original words is
\(2^{-\Delta_j}\); for the conformal power it is
\(2^{-s\Delta_j}\). These are **unnormalized word weights**.
Their ratio must not be called a ratio of normalized \(R_s\)-path
probabilities: those also contain the row factors \(p_s\).
Multiplying the unnormalized ratios and using (14) gives

\[
 \prod_{j=1}^N2^{-s\Delta_j}
 \le\frac{B_p^{sN}}{(N!)^s}.                            \tag{16}
\]

Equations (14)--(16) concern unweighted counts of the retained orbit
indices and exactly matched inverse depths. They do not settle
unequal-depth transports, weighted averages, or a construction with
sufficiently many alternate words to compensate for the cost.

## 5. The relative-entropy attempt keeps the direction of comparison

The other natural way to transfer (6) is a relative-entropy estimate.
For the source-qualified trace \(F\), direct division of (5) by (8)
gives

\[
 \log\frac{R_s(q,n)}{K_F(q,n)}
 =(s-1)\log w(n)+\log F(q)-\log F(n)-\log p_s(q).
 \tag{17}
\]

Every term is integrable under a fixed \(R_s\) row: its exponent
tail is geometric and \(\alpha\le F(n)\le Mn\).
Thus the exact reverse divergence is

\[
 D(R_s(q,\cdot)\Vert K_F(q,\cdot))
 =\log F(q)-R_s\log F(q)
  +(s-1)R_s\log w(q)-\log p_s(q).                       \tag{18}
\]

Here \(R_s\log F(q)=\sum_{Un=q}R_s(q,n)\log F(n)\);
it is not the logarithm of \(F\) at the actual predecessor.

If the actual predecessor digit has \(K_F\)-probability
\(1-\varepsilon_j\) at root \(q_{j+1}\), (6) and binary data
processing imply

\[
 D(R_s(q_{j+1},\cdot)\Vert K_F(q_{j+1},\cdot))
 \ge\frac1{1+16^s}\log\frac1{\varepsilon_j}-\log2.
 \tag{19}
\]

This is the divergence direction that detects the disappearing digit.
But summing (18) along the actual roots does **not** telescope
\(\log F(q_{j+1})-\log F(q_j)\): its second term averages all
parents with \(R_s\), rather than selecting \(q_j\).
Replacing that average by the actual predecessor is the first
unsupported estimate in this entropy version of the attack.

The forward divergence \(D(K_F\Vert R_s)\) does not repair this:
when a \(K_F\) row concentrates on one parent, that divergence need
only approach the negative logarithm of its positive \(R_s\) weight.
It need not charge \(\log(1/\varepsilon_j)\).

Finally, integration against the finite atomic measure keeps the root
weight \(r(q_j)^s\). These weights are summable along the distinct
ordinary forward states, since \(r(q_j)\le1/q_j\) and \(s>1\).
Such an integral is not the unweighted ordinary-time average in the
first-digit criterion. No deletion of those weights has been proved.

## 6. Outcome

The new conformal measure supplies a real uniform first-digit comparison,
but its pointwise sibling symmetry preserves the strict original cone.
A true cone lift at the retained depth encounters the exact factorial
cost (14), with every ordinary source label retained. The attempted
entropy alternative exposes the missing expectation transfer in (18).

An escape exclusion still requires a mechanism that compensates for
this transport cost or controls the canonical inverse law directly.
Neither bounded atomic odds nor a finite conformal measure supplies
that mechanism by itself. The statements here are written proofs;
they do not claim a Lean proof of an infinite probability theorem or
of Collatz convergence.
