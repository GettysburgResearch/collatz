# A direct closing attempt: no universal proof obtained

**22 November 2026. Status: UNSUCCESSFUL CLOSING ATTEMPT.**

This pass responds to the concern that the preceding work improved
families and interfaces without crossing the central universal
quantifier. Three parallel attacks targeted that quantifier directly.
No new residue family, fixed cycle schema, or conditional criterion is
being presented as a substitute for the missing conclusion.

The goal was actual ordinary descent:
\[
 \forall n>1,\quad \exists k\ge1,\quad T^k(n)<n,
\]
for the shortcut map \(T(n)=n/2\) on even inputs and
\(T(n)=(3n+1)/2\) on odd inputs. Strong induction would then give full
Collatz. The analytic attempt below would exclude escapes if completed;
it would still need the separate cycle obligation.

**We did not prove the goal.** This note records the strongest direct
attempts and the exact inferences at which they stopped. It adds no new
Lean theorem count and changes no earlier proof receipt.

## Frozen current inputs

| PR | Exact head | Central source inspected |
|---|---|---|
| 177 | 8ef9bf0d828fc533721dee1f90c5d78fac80ad39 | ROOTED_SOURCE_FLOOR.md, NEGATIVE_SHADOW_RETURN.md, STRICT_PREFIX_CONTRACTION.md |
| 180 | ab3973099f0d285bbe88972382ad599bb02cd460 | lean-joint-20261122/MIXED_COVER.md, ORDINARY_BOUNDARY.md, CONTACT_CLOCK.md |
| 185 | 53f01ca5b443ef57ef2160b4996dbb2cc87f7395 | multiple-attacks-20261122/RATIONAL_SHADOW_DISPATCH.md, HARMONIC_KERNEL_FACTORIZATION.md, CONTACT_EXIT_ACCOUNTING.md |
| 175 | 728389c2ad4796853948250a90188b0697483d92 | LATE_GREEN_HARMONIC_MOMENT.md, FIVE_EDGE_TRANSPORT.md |
| 176 | 31c4a880ea4acf6eec4783e68bfc75e2cf8e7fe6 | overview/profound/HEAD_THREE_TARGET.md, MOVING_TILT_WINDOW.md |

The original full paths and links used below remove any ambiguity between
these files and earlier packets in the same PR. The current source
inspection does not re-certify their analytic assumptions.

## 1. Try to force descent using the global source floor

PR177's
[rooted source theorem](https://github.com/GettysburgResearch/collatz/blob/8ef9bf0d828fc533721dee1f90c5d78fac80ad39/research/lean-exact-witness-global-20261121/ROOTED_SOURCE_FLOOR.md)
supplies a complete bounded-four source for every target \(t\ge177\).
Writing \(L=\lfloor(t-1)/2\rfloor\), its source satisfies
\[
 L<S\le t-1,\qquad t\le2S+1,\qquad
 T^{j+1}(S)\le L\quad(j\ge0).
\]
For the remaining targets \(t=3\bmod4\), an actual target return to the
permitted source cone then gives descent below the original target.
The attempted completion was to force that return by following the
complete supplied source to one.

### The completion by source exhaustion is false

Take \(t=319\), \(L=159\), and \(S=296=8\cdot37\). The complete odd
certificate of \(37\) is
\[
 [4,1,1,2,3,4],
\]
with literal prefix \([4,1]\) ending at eleven. The complete source path
has eighteen shortcut clocks:
\[
\begin{split}
296,&148,74,37,56,28,14,7,11,17,\\
&26,13,20,10,5,8,4,2,1.
\end{split}
\]
Every state after the first is at most \(148<L\), and
\(S+1<t\le2S+1\). This source occurs in the actual last-crossing
construction: the known odd source \(197>L\) first goes to \(296\),
then stays below \(159\).

But every target iterate through that same eighteenth clock is at least
\(319\), and
\[
 T^{18}(319)=650>319.
\]
Its first strict descent occurs at clock twenty-one:
\[
 650\longmapsto325\longmapsto488\longmapsto244<319.
\]

The complete exact paths and checks are in
[central-attempt-control.json](../../reports/2026-11-22-global-synthesis/central-attempt-control.json).
This refutes the proposed source-exhaustion completion, not Collatz or
the source-floor theorem.

After the supplied source reaches one, the current exact carry compiler
retains unrestricted target \(T^2\) dynamics unless further reachable-state
information is used. Its total transition rule therefore does not supply
the missing successful-return theorem.

### An extremal source identifies the queries that source surgeries miss

For a fixed positive \(n\), consider all actual complete certificates whose
interval \(0<z\le2S+1\) contains \(n\). Known cofinal sources make this set
nonempty. Choose its least multiset grade
\(G_n\), then the largest source \(S_n\) among certificates at that grade.
The first choice exists by well-foundedness; the second exists from the
complete-certificate bound \(S\le2^{\sum G_n}\).

Every lower-grade certified source \(S'\) then satisfies
\[
 2S'+1<n.
\]
Otherwise it would already cover \(n\), contrary to the least-grade
choice. No larger same-grade source exists either.

Consequently a successful lower-grade interval query at this extremal
witness necessarily captures an actual value below \(n\). Equal-grade
source enlargement is unavailable. A proof based on a sufficiently
complete menu of static source surgeries must still handle these
extremal queries through actual target descent or a merger with a smaller
value.

For the remaining large queries \(n\ge177\), the existing source-advance
rules make the later source states lie below the original half-target
threshold; terminal-cycle states already satisfy that bound.
This is compatible with the source floor, but it does not itself force
a target return. We obtained no universal invariant that does so.

This selection is a mathematical reduction, not an asserted effective
algorithm and not a new proof of descent.

## 2. Try to remove the canonical escape boundary by Green smoothing

This attempt uses the new strict Green factorization in
[PR185](https://github.com/GettysburgResearch/collatz/blob/53f01ca5b443ef57ef2160b4996dbb2cc87f7395/research/multiple-attacks-20261122/HARMONIC_KERNEL_FACTORIZATION.md)
and the canonical harmonic moment in
[PR175](https://github.com/GettysburgResearch/collatz/blob/728389c2ad4796853948250a90188b0697483d92/research/lean-global-closure-20261121/LATE_GREEN_HARMONIC_MOMENT.md).
All their analytic qualifications remain in force.

Work on nonperiodic positive odd ternary units, killing forward transport
on first entry into any periodic state. Let \(L\) be forward mass
transport, \(S=\sum_{j\ge0}L^j\), \(D(n)=1/(3n+1)\), and
\[
 K=SLD,\qquad
 Au=\frac{K(\nu u)}{\nu},\qquad
 f=\frac h\nu\in[\delta,1].
\]
The actual canonical identity \(\nu=h+Kh\) gives
\[
 \boxed{Af=1-f.}
\]
Put \(R=1-\lambda f\), where \(\lambda(n)=3n/(3n+1)\).
Positivity gives
\[
 A1\le\delta^{-1}(1-f)\le\delta^{-1}R.
\]
The pinned canonical theorem proves
\[
 \|R\|_H=\sum_q\frac{R(q)}q<\infty,\qquad
 H=\ell^1(q^{-1}).
\]
Thus \(A:\ell^\infty\to H\) is bounded and compact: the image of its unit
ball is dominated by the single summable function \(A1\).

The proposed arithmetic improvement was to exploit the factor \(D\) to
control multiplication-by-five differences on this canonical object.
For \(M_5u(q)=u(5q)\), with zero extension at removed states,
\[
 \|M_5\|_{\infty\to\infty}\le1,\qquad
 \|M_5\|_{H\to H}\le5.
\]
It follows that the static commutator really is controlled:
\[
 \|[M_5,A]\|_{\infty\to H}
 \le6\delta^{-1}\|R\|_H.
\]
The bound is specific to the normalized canonical operation. It does not
incorrectly infer boundedness of raw forward transport from it.

### The actual forward commutator retains the full escape label

Let \(C\) be killed forward composition, \(Cu(q)=u(Uq)\). The expression
needed for the boundary is \(C^kAf\), not \(AC^kf\):
\[
 C^kAf=AC^kf+[C^k,A]f.
\]
The reordered term is uniformly controlled in \(H\) because
\(|AC^kf|\le A1\). This is the genuine gain from the \(D\) factor.

Let \(E\) be the escaping domain and let \(F\) be the canonical invariant
escape label. On each escaping component \(\mathcal C\),
\[
 d(q)=\frac{h(q)}{3q+1},\qquad
 D_{\mathcal C}=\sum_{q\in\mathcal C}d(q),\qquad
 C_{\mathcal C}=\lim_k\nu(U^kq),
\]
\[
 F_{\mathcal C}=\frac{D_{\mathcal C}}{C_{\mathcal C}}>0,
\]
and \(F=0\) on eventually periodic components. The pinned component
limits imply
\[
 C^kAf\longrightarrow F,\qquad
 C^kf\longrightarrow 1_E(1-F)
\]
pointwise. Since the latter limit is constant on each component,
dominated convergence with \(A1\in H\) gives
\[
 AC^kf\longrightarrow1_E(1-F)A1
 \quad\text{in }H.
\]
Therefore the remaining physical commutator has the exact boundary
\[
 \boxed{[C^k,A]f\longrightarrow F-1_E(1-F)A1
 \quad\text{pointwise}.}
\]
The second term has finite harmonic mass. The first is the entire escape
label with coefficient one. We found no arithmetic identity or bound
annihilating it. Static five-commutator compactness therefore does not
complete this proposed argument.

The same loss can be seen directly in the canonical charge:
\[
 Sd=\nu R,\qquad d=(I-L)(\nu R).
\]
The tempting componentwise cancellation would require adequate
unweighted summability of the primitive. Along an escaping spine,
\(\nu(q_k)R(q_k)\to D_{\mathcal C}>0\), so that summability fails
precisely on the hypothetical escape sector.

### Contact-reset convergence does not make the boundary stationary

The current
[ordinary-boundary theorem](https://github.com/GettysburgResearch/collatz/blob/ab3973099f0d285bbe88972382ad599bb02cd460/research/lean-joint-20261122/ORDINARY_BOUNDARY.md)
constructs a strong finite-reference limit after inverse contact
projection. The
[actual contact-clock theorem](https://github.com/GettysburgResearch/collatz/blob/ab3973099f0d285bbe88972382ad599bb02cd460/research/lean-joint-20261122/CONTACT_CLOCK.md)
shows why this does not prove absorption: with the strong \(\ell^1\)
boundary projection \(B=\lim_k\Pi L^k\) and reset operator \(Q=\Pi L\),
one obtains \(BQ=B\), but not \(QB=B\).
Positive escape mass is not stationary under the reset clock.
Interchanging those two compositions would insert the missing theorem.

## 3. Try to close arbitrary source words by a rational-shadow invariant

The newest
[physical rational-shadow compiler](https://github.com/GettysburgResearch/collatz/blob/53f01ca5b443ef57ef2160b4996dbb2cc87f7395/research/multiple-attacks-20261122/RATIONAL_SHADOW_DISPATCH.md)
was tested as the arithmetic route to arbitrary-word coverage.
The exact state retains a source \(r\), target \(n\), exponent \(p\), and
debt \(d\ge0\), with \(p>0\) and \(n+d=3^p r\).
For a source gap \(3r+1=2^a u\), the complementary \(3x-1\) shortcut
gives
\[
 b=3^{p-1}+d,\quad d'=S_-^a(b),\quad
 p'=p-1+\#\{\text{odd inputs of }S_-\text{ in those }a\text{ clocks}\},
\]
\[
 T^a(n)+d'=3^{p'}u.
\]

The attempted new invariant had to control this unbounded pair
\((p,d)\) on every reachable bounded-four source history. No valid
decreasing quantity was obtained.

Repeated contracting source blocks do supply the existing dyadic
separation budget. An arbitrary changing source word has no proved
bounded repeat description. The original integer's finite binary
expansion does not, by itself, bound the complexity of its future parity
itinerary.

At source exhaustion, discarding the low-alphabet/history restriction
leaves unrestricted ordinary target dynamics. That does not prove the
restriction is useless: a successful argument could still exploit the
exact reachable set. We did not find the required invariant on that set.

## Outcome and publication boundary

No central closing implication was proved in this pass. The source-floor
completion was refuted by an actual compatible certificate; the
canonical smoothing proposal was carried through to an exact nonvanishing
candidate residual; the arbitrary-word carry attempt produced no
well-founded invariant.

These are records of failed closing arguments, not additional evidence
that Collatz is solved or that the remaining quantifier has been reduced
to a finite list. No new Lean modules were added, and no earlier
compilation was relabeled as a new run. The existing twenty-statement
packet and its separately qualified written results retain their scope.
